from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

import trend_estimation as td


SMOKE_GRID = {
    "slope_noise_std": (0.005,),
    "observation_noise_std": (0.3,),
    "ar1_phi": (0.0, 0.7),
    "horizon": (1,),
}

PAPER_GRID = {
    "slope_noise_std": (0.002, 0.01, 0.03),
    "observation_noise_std": (0.2, 0.5, 1.0),
    "ar1_phi": (0.0, 0.4, 0.8),
    "horizon": (1, 3, 6),
}

QUICK_GRID = {
    "slope_noise_std": (0.005, 0.02),
    "observation_noise_std": (0.3, 0.8),
    "ar1_phi": (0.0, 0.7),
    "horizon": (1, 3),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run controlled forecast-optimal smoothing simulations. "
            "This script is intentionally local/manual; it is not triggered by CI."
        )
    )
    parser.add_argument("--preset", choices=("smoke", "quick", "paper"), default="quick")
    parser.add_argument("--n-seeds", type=int, default=None)
    parser.add_argument("--n-obs", type=int, default=240)
    parser.add_argument("--outer-initial-train", type=int, default=120)
    parser.add_argument("--outer-step", type=int, default=6)
    parser.add_argument("--inner-step", type=int, default=3)
    parser.add_argument("--max-inner-origins", type=int, default=30)
    parser.add_argument("--orders", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--windows", type=int, nargs="+", default=[24, 48, 72])
    parser.add_argument("--n-grid", type=int, default=161)
    parser.add_argument("--log-lambda-min", type=float, default=-10.0)
    parser.add_argument("--log-lambda-max", type=float, default=16.0)
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=(
            "Optional CSV output path. By default, create a versioned run under "
            "results/forecast_optimal_smoothing/<run-id>/."
        ),
    )
    return parser.parse_args()


def run_one_configuration(
    *,
    seed: int,
    n_obs: int,
    slope_noise_std: float,
    observation_noise_std: float,
    ar1_phi: float,
    horizon: int,
    outer_initial_train: int,
    outer_step: int,
    inner_step: int,
    max_inner_origins: int,
    orders: tuple[int, ...],
    windows: tuple[int, ...],
    log_bounds: tuple[float, float],
    n_grid: int,
) -> list[dict]:
    data = td.make_local_linear_ar1_series(
        n_obs=n_obs,
        slope_noise_std=slope_noise_std,
        observation_noise_std=observation_noise_std,
        ar1_phi=ar1_phi,
        random_state=seed,
    )

    nested = td.nested_rolling_pure_forecast(
        data.y,
        outer_initial_train=outer_initial_train,
        horizon=horizon,
        outer_step=outer_step,
        orders=orders,
        windows=windows,
        inner_step=inner_step,
        max_inner_origins=max_inner_origins,
        min_inner_origins=2,
        log_bounds=log_bounds,
        n_grid=n_grid,
    )

    rows: list[dict] = []
    for record in nested.records:
        origin = record.origin
        window = record.selected_window
        start = origin - window

        oracle = td.select_recovery_optimal_lambda(
            data.y[start:origin],
            data.true_trend[start:origin],
            order=record.selected_order,
            log_bounds=log_bounds,
            n_grid=n_grid,
        )

        forecast_error = record.observed - record.prediction
        benchmark_error = record.observed - record.benchmark_prediction
        block_mse = float(np.mean(forecast_error**2))
        benchmark_mse = float(np.mean(benchmark_error**2))
        block_rmse = float(np.sqrt(block_mse))
        benchmark_rmse = float(np.sqrt(benchmark_mse))
        relative_rmsfe = (
            float(block_rmse / benchmark_rmse)
            if benchmark_rmse > 0.0
            else (0.0 if block_rmse == 0.0 else float("inf"))
        )

        rows.append(
            {
                "seed": seed,
                "n_obs": n_obs,
                "slope_noise_std": slope_noise_std,
                "observation_noise_std": observation_noise_std,
                "ar1_phi": ar1_phi,
                "horizon": horizon,
                "outer_origin": origin,
                "selected_order": record.selected_order,
                "selected_window": window,
                "lambda_forecast": record.selected_lambda,
                "smoothness_forecast": record.selected_smoothness,
                "inner_forecast_mse": record.inner_objective,
                "lambda_recovery_oracle": oracle.lambda_,
                "smoothness_recovery_oracle": oracle.smoothness_,
                "recovery_mse_oracle": oracle.objective_,
                "smoothness_gap_forecast_minus_recovery": (
                    record.selected_smoothness - oracle.smoothness_
                ),
                "outer_block_mse": block_mse,
                "benchmark_block_mse": benchmark_mse,
                "relative_rmsfe_block": relative_rmsfe,
            }
        )

    return rows


def _git_short_sha() -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def _default_run_directory(preset: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return Path("results") / "forecast_optimal_smoothing" / f"{stamp}_{preset}_{_git_short_sha()}"


def _write_summary(frame: pd.DataFrame, path: Path) -> None:
    group_cols = [
        "seed",
        "slope_noise_std",
        "observation_noise_std",
        "ar1_phi",
        "horizon",
    ]
    summary = (
        frame.groupby(group_cols, dropna=False)
        .agg(
            n_outer_origins=("outer_origin", "size"),
            mean_selected_order=("selected_order", "mean"),
            mean_selected_window=("selected_window", "mean"),
            mean_smoothness_forecast=("smoothness_forecast", "mean"),
            mean_smoothness_recovery_oracle=("smoothness_recovery_oracle", "mean"),
            mean_smoothness_gap=(
                "smoothness_gap_forecast_minus_recovery",
                "mean",
            ),
            mean_block_relative_rmsfe=("relative_rmsfe_block", "mean"),
            median_block_relative_rmsfe=("relative_rmsfe_block", "median"),
            mean_outer_block_mse=("outer_block_mse", "mean"),
            mean_benchmark_block_mse=("benchmark_block_mse", "mean"),
        )
        .reset_index()
    )
    summary["pooled_relative_rmsfe"] = np.sqrt(
        summary["mean_outer_block_mse"]
        / summary["mean_benchmark_block_mse"]
    )
    summary.to_csv(path, index=False)


def main() -> None:
    args = parse_args()
    if args.preset == "smoke":
        grid = SMOKE_GRID
        default_seeds = 1
    elif args.preset == "quick":
        grid = QUICK_GRID
        default_seeds = 2
    else:
        grid = PAPER_GRID
        default_seeds = 30
    n_seeds = default_seeds if args.n_seeds is None else int(args.n_seeds)

    if n_seeds <= 0:
        raise ValueError("n-seeds must be positive.")

    rows: list[dict] = []
    configs = list(
        product(
            range(n_seeds),
            grid["slope_noise_std"],
            grid["observation_noise_std"],
            grid["ar1_phi"],
            grid["horizon"],
        )
    )

    total_start = time.perf_counter()
    for i, (seed, slope_sd, noise_sd, phi, horizon) in enumerate(configs, start=1):
        config_start = time.perf_counter()
        print(
            f"[{i}/{len(configs)}] seed={seed} "
            f"slope_sd={slope_sd} noise_sd={noise_sd} "
            f"phi={phi} h={horizon}",
            flush=True,
        )
        new_rows = run_one_configuration(
                seed=seed,
                n_obs=args.n_obs,
                slope_noise_std=float(slope_sd),
                observation_noise_std=float(noise_sd),
                ar1_phi=float(phi),
                horizon=int(horizon),
                outer_initial_train=args.outer_initial_train,
                outer_step=args.outer_step,
                inner_step=args.inner_step,
                max_inner_origins=args.max_inner_origins,
                orders=tuple(args.orders),
                windows=tuple(args.windows),
                log_bounds=(args.log_lambda_min, args.log_lambda_max),
                n_grid=args.n_grid,
            )
        rows.extend(new_rows)
        elapsed = time.perf_counter() - config_start
        print(
            f"    completed in {elapsed:.2f}s; "
            f"outer rows={len(new_rows)}",
            flush=True,
        )

    frame = pd.DataFrame(rows)
    total_elapsed = time.perf_counter() - total_start

    if args.output is None:
        run_dir = _default_run_directory(args.preset)
        output = run_dir / "simulation_grid.csv"
    else:
        output = args.output
        run_dir = output.parent

    run_dir.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output, index=False)
    _write_summary(frame, run_dir / "summary.csv")

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "preset": args.preset,
        "n_seeds": n_seeds,
        "n_obs": args.n_obs,
        "outer_initial_train": args.outer_initial_train,
        "outer_step": args.outer_step,
        "inner_step": args.inner_step,
        "max_inner_origins": args.max_inner_origins,
        "orders": list(args.orders),
        "windows": list(args.windows),
        "n_grid": args.n_grid,
        "log_lambda_bounds": [
            args.log_lambda_min,
            args.log_lambda_max,
        ],
        "n_configurations": len(configs),
        "n_output_rows": len(frame),
        "elapsed_seconds": total_elapsed,
        "grid": {key: list(values) for key, values in grid.items()},
        "output_csv": str(output),
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(
        f"Wrote {len(frame)} outer-origin rows to {output} "
        f"in {total_elapsed:.2f}s",
        flush=True,
    )
    print(f"Run metadata: {run_dir / 'run_metadata.json'}", flush=True)
    print(f"Summary: {run_dir / 'summary.csv'}", flush=True)


if __name__ == "__main__":
    main()
