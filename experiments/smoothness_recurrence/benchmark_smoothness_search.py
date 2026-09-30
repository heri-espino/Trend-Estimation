from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import trend_estimation as td


PRESETS = {
    "smoke": {"seeds": (0,), "horizons": (1,), "dense_grid_size": 401},
    "quick": {"seeds": tuple(range(5)), "horizons": (1, 5, 20), "dense_grid_size": 2001},
    "paper": {"seeds": tuple(range(30)), "horizons": (1, 5, 20), "dense_grid_size": 10001},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Benchmark adaptive multiple-minimum search directly in normalized "
            "smoothness against a dense smoothness reference."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument("--n-obs", type=int, default=240)
    parser.add_argument("--window", type=int, default=120)
    parser.add_argument("--order", type=int, default=2)
    parser.add_argument("--step", type=int, default=3)
    parser.add_argument("--max-origins", type=int, default=30)
    parser.add_argument("--slope-noise-std", type=float, default=0.01)
    parser.add_argument("--observation-noise-std", type=float, default=0.5)
    parser.add_argument("--ar1-phi", type=float, default=0.3)
    parser.add_argument("--initial-grid-size", type=int, default=9)
    parser.add_argument("--max-depth", type=int, default=8)
    parser.add_argument("--min-interval", type=float, default=1e-3)
    parser.add_argument("--max-candidates", type=int, default=5)
    parser.add_argument(
        "--epsilons",
        type=float,
        nargs="+",
        default=list(td.DEFAULT_SPACING_EPSILONS),
    )
    parser.add_argument("--dense-grid-size", type=int, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser.parse_args()


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
    return (
        Path("results")
        / "smoothness_recurrence"
        / f"{stamp}_smoothness-search-{preset}_{_git_short_sha()}"
    )


def _dense_reference(
    prepared,
    *,
    window: int,
    order: int,
    n_grid: int,
) -> tuple[np.ndarray, np.ndarray, list[tuple[float, float]]]:
    smoothness_grid = np.linspace(0.0, 0.999999, int(n_grid))
    values = np.empty_like(smoothness_grid)

    for i, smoothness in enumerate(smoothness_grid):
        lambda_ = td.smoothness_to_lambda(
            float(smoothness),
            n_obs=window,
            order=order,
        )
        values[i] = prepared.evaluate(lambda_).value

    minima: list[tuple[float, float]] = []
    for i in range(1, len(smoothness_grid) - 1):
        if values[i] <= values[i - 1] and values[i] <= values[i + 1]:
            minima.append((float(smoothness_grid[i]), float(values[i])))

    return smoothness_grid, values, minima


def run_case(
    *,
    seed: int,
    horizon: int,
    args: argparse.Namespace,
    dense_grid_size: int,
) -> tuple[dict, list[dict]]:
    data = td.make_local_linear_ar1_series(
        n_obs=args.n_obs,
        slope_noise_std=args.slope_noise_std,
        observation_noise_std=args.observation_noise_std,
        ar1_phi=args.ar1_phi,
        random_state=seed,
    )
    splits = td.rolling_origin_splits(
        args.n_obs,
        initial_train=args.window,
        horizon=horizon,
        step=args.step,
        expanding=False,
        train_window=args.window,
    )
    splits = splits[-args.max_origins :]
    prepared = td.prepare_rolling_pure_forecast_objective(
        data.y,
        splits,
        order=args.order,
    )

    def value_grad_hess(lambda_: float):
        evaluated = prepared.evaluate(lambda_)
        return evaluated.value, evaluated.first, evaluated.second

    adaptive_start = time.perf_counter()
    search = td.find_stationary_points_smoothness(
        value_grad_hess,
        n_obs=args.window,
        order=args.order,
        initial_grid_size=args.initial_grid_size,
        max_depth=args.max_depth,
        min_interval=args.min_interval,
    )
    adaptive_seconds = time.perf_counter() - adaptive_start

    dense_start = time.perf_counter()
    dense_s, dense_values, dense_minima = _dense_reference(
        prepared,
        window=args.window,
        order=args.order,
        n_grid=dense_grid_size,
    )
    dense_seconds = time.perf_counter() - dense_start

    adaptive_minima = tuple(
        point for point in search.points_ if point.kind_ == "minimum"
    )
    best_adaptive = (
        min(adaptive_minima, key=lambda point: point.objective_)
        if adaptive_minima
        else None
    )
    dense_best_index = int(np.argmin(dense_values))
    dense_best_s = float(dense_s[dense_best_index])
    dense_best_value = float(dense_values[dense_best_index])

    summary = {
        "seed": seed,
        "horizon": horizon,
        "order": args.order,
        "window": args.window,
        "n_origins": len(splits),
        "n_adaptive_stationary_points": len(search.points_),
        "n_adaptive_local_minima": len(adaptive_minima),
        "n_dense_local_minima": len(dense_minima),
        "adaptive_evaluations": search.n_evaluations_,
        "dense_evaluations": int(dense_grid_size),
        "adaptive_seconds": adaptive_seconds,
        "dense_seconds": dense_seconds,
        "dense_best_s": dense_best_s,
        "dense_best_cv": dense_best_value,
        "adaptive_best_s": (
            best_adaptive.smoothness_ if best_adaptive is not None else np.nan
        ),
        "adaptive_best_cv": (
            best_adaptive.objective_ if best_adaptive is not None else np.nan
        ),
        "best_s_abs_error": (
            abs(best_adaptive.smoothness_ - dense_best_s)
            if best_adaptive is not None
            else np.nan
        ),
        "objective_regret": (
            best_adaptive.objective_ - dense_best_value
            if best_adaptive is not None
            else np.nan
        ),
    }

    candidate_rows: list[dict] = []
    for candidate_set in td.sweep_spaced_smoothness_minima(
        search.points_,
        epsilons=args.epsilons,
        max_candidates=args.max_candidates,
    ):
        for rank, point in enumerate(candidate_set.candidates_, start=1):
            candidate_rows.append(
                {
                    "seed": seed,
                    "horizon": horizon,
                    "epsilon": candidate_set.epsilon_,
                    "rank": rank,
                    "smoothness": point.smoothness_,
                    "lambda": point.lambda_,
                    "cv": point.objective_,
                    "curvature_smoothness": point.curvature_smoothness_,
                    "n_available_minima": candidate_set.n_available_minima_,
                    "n_removed": candidate_set.n_removed_,
                }
            )

    return summary, candidate_rows


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    dense_grid_size = (
        int(args.dense_grid_size)
        if args.dense_grid_size is not None
        else int(preset["dense_grid_size"])
    )
    if args.max_candidates <= 0:
        raise ValueError("max-candidates must be positive.")
    if dense_grid_size < 3:
        raise ValueError("dense-grid-size must be at least 3.")

    run_dir = args.output_dir or _default_run_directory(args.preset)
    run_dir.mkdir(parents=True, exist_ok=True)

    summaries: list[dict] = []
    candidates: list[dict] = []
    start = time.perf_counter()

    cases = [
        (int(seed), int(horizon))
        for seed in preset["seeds"]
        for horizon in preset["horizons"]
    ]
    for i, (seed, horizon) in enumerate(cases, start=1):
        print(f"[{i}/{len(cases)}] seed={seed} h={horizon}", flush=True)
        summary, rows = run_case(
            seed=seed,
            horizon=horizon,
            args=args,
            dense_grid_size=dense_grid_size,
        )
        summaries.append(summary)
        candidates.extend(rows)
        print(
            "    "
            f"minima={summary['n_adaptive_local_minima']} "
            f"adaptive_eval={summary['adaptive_evaluations']} "
            f"dense_eval={summary['dense_evaluations']} "
            f"|dS|={summary['best_s_abs_error']:.6g}",
            flush=True,
        )

    elapsed = time.perf_counter() - start
    pd.DataFrame(summaries).to_csv(run_dir / "search_summary.csv", index=False)
    pd.DataFrame(candidates).to_csv(run_dir / "candidate_sweep.csv", index=False)

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "preset": args.preset,
        "n_obs": args.n_obs,
        "window": args.window,
        "order": args.order,
        "step": args.step,
        "max_origins": args.max_origins,
        "slope_noise_std": args.slope_noise_std,
        "observation_noise_std": args.observation_noise_std,
        "ar1_phi": args.ar1_phi,
        "initial_grid_size": args.initial_grid_size,
        "max_depth": args.max_depth,
        "min_interval": args.min_interval,
        "max_candidates": args.max_candidates,
        "epsilons": list(args.epsilons),
        "dense_grid_size": dense_grid_size,
        "elapsed_seconds": elapsed,
        "n_cases": len(cases),
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(f"Wrote benchmark to {run_dir} in {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
