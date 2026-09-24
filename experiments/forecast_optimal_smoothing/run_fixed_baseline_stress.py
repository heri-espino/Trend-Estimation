from __future__ import annotations

import argparse
import json
import os
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

import trend_estimation as td

from run_adaptive_value import (
    _block_metrics,
    _fit_frozen_forecast,
    _period,
    git_short_sha,
)
from run_roughness_adaptation import _roughness_transitions


SMOKE_HORIZONS = (1,)
EXPLORE_HORIZONS = (1, 3, 6, 12)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Stress-test adaptive roughness results against stronger frozen "
            "hyperparameter baselines selected with more pre-regime evidence."
        )
    )
    parser.add_argument("--preset", choices=("smoke", "explore"), default="explore")
    parser.add_argument("--n-seeds", type=int, default=None)
    parser.add_argument("--n-obs", type=int, default=300)
    parser.add_argument("--regime-point", type=int, default=180)
    parser.add_argument("--low-slope-noise-std", type=float, default=0.005)
    parser.add_argument("--high-slope-noise-std", type=float, default=0.02)
    parser.add_argument("--observation-noise-std", type=float, default=0.5)
    parser.add_argument("--ar1-phi", type=float, default=0.0)
    parser.add_argument("--outer-initial-train", type=int, default=120)
    parser.add_argument("--outer-step", type=int, default=3)
    parser.add_argument("--inner-step", type=int, default=3)
    parser.add_argument("--selector-max-inner-origins", type=int, default=20)
    parser.add_argument("--orders", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--windows", type=int, nargs="+", default=[24, 48, 72])
    parser.add_argument("--n-grid", type=int, default=None)
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help=(
            "Worker processes. 0=auto, 1=serial. Auto leaves two logical "
            "CPUs free and caps at 16 workers."
        ),
    )
    parser.add_argument("--log-lambda-min", type=float, default=None)
    parser.add_argument("--log-lambda-max", type=float, default=None)
    return parser.parse_args()


def _select_frozen(
    history,
    *,
    horizon: int,
    args: argparse.Namespace,
    max_origins: int | None,
):
    return td.select_fixed_window_pure_smoothness(
        history,
        orders=tuple(args.orders),
        windows=tuple(args.windows),
        horizon=horizon,
        step=args.inner_step,
        max_origins=max_origins,
        min_origins=2,
        log_bounds=(args.log_lambda_min, args.log_lambda_max),
        n_grid=args.n_grid,
    ).best_


def run_configuration(
    *,
    seed: int,
    transition: str,
    pre_slope_noise_std: float,
    post_slope_noise_std: float,
    horizon: int,
    args: argparse.Namespace,
) -> list[dict]:
    data = td.make_two_regime_local_linear_series(
        n_obs=args.n_obs,
        regime_point=args.regime_point,
        pre_slope_noise_std=pre_slope_noise_std,
        post_slope_noise_std=post_slope_noise_std,
        pre_observation_noise_std=args.observation_noise_std,
        post_observation_noise_std=args.observation_noise_std,
        pre_ar1_phi=args.ar1_phi,
        post_ar1_phi=args.ar1_phi,
        level_shift=0.0,
        slope_shift=0.0,
        random_state=seed,
    )

    pre_history = data.y[: args.regime_point]
    frozen_local = _select_frozen(
        pre_history,
        horizon=horizon,
        args=args,
        max_origins=args.selector_max_inner_origins,
    )
    frozen_all_pre = _select_frozen(
        pre_history,
        horizon=horizon,
        args=args,
        max_origins=None,
    )

    adaptive = td.nested_rolling_pure_forecast(
        data.y,
        outer_initial_train=args.outer_initial_train,
        horizon=horizon,
        outer_step=args.outer_step,
        orders=tuple(args.orders),
        windows=tuple(args.windows),
        inner_step=args.inner_step,
        max_inner_origins=args.selector_max_inner_origins,
        min_inner_origins=2,
        log_bounds=(args.log_lambda_min, args.log_lambda_max),
        n_grid=args.n_grid,
    )

    rows: list[dict] = []
    rp = int(args.regime_point)

    for record in adaptive.records:
        origin = int(record.origin)
        if origin < rp:
            continue

        history = data.y[:origin]
        observed = np.asarray(record.observed, dtype=float)
        adaptive_prediction = np.asarray(record.prediction, dtype=float)
        benchmark_prediction = np.asarray(record.benchmark_prediction, dtype=float)

        local_prediction = _fit_frozen_forecast(
            history,
            order=int(frozen_local.order),
            window=int(frozen_local.window),
            lambda_=float(frozen_local.lambda_),
            horizon=observed.size,
        )
        all_pre_prediction = _fit_frozen_forecast(
            history,
            order=int(frozen_all_pre.order),
            window=int(frozen_all_pre.window),
            lambda_=float(frozen_all_pre.lambda_),
            horizon=observed.size,
        )

        adaptive_mse, adaptive_rmse = _block_metrics(
            observed, adaptive_prediction
        )
        local_mse, local_rmse = _block_metrics(
            observed, local_prediction
        )
        all_pre_mse, all_pre_rmse = _block_metrics(
            observed, all_pre_prediction
        )
        benchmark_mse, benchmark_rmse = _block_metrics(
            observed, benchmark_prediction
        )

        rows.append(
            {
                "seed": int(seed),
                "transition": transition,
                "pre_slope_noise_std": float(pre_slope_noise_std),
                "post_slope_noise_std": float(post_slope_noise_std),
                "horizon": int(horizon),
                "outer_origin": origin,
                "relative_origin": origin - rp,
                "period": _period(origin - rp),
                "adaptive_order": int(record.selected_order),
                "adaptive_window": int(record.selected_window),
                "adaptive_lambda": float(record.selected_lambda),
                "adaptive_smoothness": float(record.selected_smoothness),
                "frozen_local_order": int(frozen_local.order),
                "frozen_local_window": int(frozen_local.window),
                "frozen_local_lambda": float(frozen_local.lambda_),
                "frozen_local_smoothness": float(frozen_local.smoothness_),
                "frozen_local_n_origins": int(frozen_local.n_origins_),
                "frozen_all_pre_order": int(frozen_all_pre.order),
                "frozen_all_pre_window": int(frozen_all_pre.window),
                "frozen_all_pre_lambda": float(frozen_all_pre.lambda_),
                "frozen_all_pre_smoothness": float(frozen_all_pre.smoothness_),
                "frozen_all_pre_n_origins": int(frozen_all_pre.n_origins_),
                "adaptive_mse": adaptive_mse,
                "frozen_local_mse": local_mse,
                "frozen_all_pre_mse": all_pre_mse,
                "benchmark_mse": benchmark_mse,
                "adaptive_rmse": adaptive_rmse,
                "frozen_local_rmse": local_rmse,
                "frozen_all_pre_rmse": all_pre_rmse,
                "benchmark_rmse": benchmark_rmse,
                "adaptive_advantage_vs_frozen_local": local_mse - adaptive_mse,
                "adaptive_advantage_vs_frozen_all_pre": (
                    all_pre_mse - adaptive_mse
                ),
            }
        )

    return rows


def _summary(frame: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []

    for (transition, horizon), group in frame.groupby(
        ["transition", "horizon"],
        dropna=False,
    ):
        period_groups = [("all_post", group)]
        period_groups.extend(
            (period, part)
            for period, part in group.groupby("period", dropna=False)
        )

        for period, part in period_groups:
            a = float(part["adaptive_mse"].mean())
            fl = float(part["frozen_local_mse"].mean())
            fa = float(part["frozen_all_pre_mse"].mean())
            b = float(part["benchmark_mse"].mean())
            rows.append(
                {
                    "transition": transition,
                    "horizon": int(horizon),
                    "period": period,
                    "n_blocks": int(len(part)),
                    "adaptive_mse": a,
                    "frozen_local_mse": fl,
                    "frozen_all_pre_mse": fa,
                    "benchmark_mse": b,
                    "adaptive_rmse_vs_frozen_local": float(np.sqrt(a / fl)),
                    "adaptive_rmse_vs_frozen_all_pre": float(np.sqrt(a / fa)),
                    "adaptive_relative_rmsfe_vs_no_change": float(
                        np.sqrt(a / b)
                    ),
                    "frozen_local_relative_rmsfe_vs_no_change": float(
                        np.sqrt(fl / b)
                    ),
                    "frozen_all_pre_relative_rmsfe_vs_no_change": float(
                        np.sqrt(fa / b)
                    ),
                    "mean_adaptive_advantage_vs_frozen_local": float(
                        part["adaptive_advantage_vs_frozen_local"].mean()
                    ),
                    "mean_adaptive_advantage_vs_frozen_all_pre": float(
                        part["adaptive_advantage_vs_frozen_all_pre"].mean()
                    ),
                }
            )

    return pd.DataFrame(rows)


def _paired_control_summary(
    frame: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    pairs = (
        ("low_to_high_roughness", "stable_low_roughness"),
        ("high_to_low_roughness", "stable_high_roughness"),
    )
    keys = ["seed", "horizon", "relative_origin"]
    row_parts: list[pd.DataFrame] = []
    summary_rows: list[dict] = []

    for transition, control in pairs:
        t = frame.loc[
            frame["transition"].eq(transition),
            keys
            + [
                "period",
                "adaptive_advantage_vs_frozen_local",
                "adaptive_advantage_vs_frozen_all_pre",
            ],
        ].copy()
        c = frame.loc[
            frame["transition"].eq(control),
            keys
            + [
                "adaptive_advantage_vs_frozen_local",
                "adaptive_advantage_vs_frozen_all_pre",
            ],
        ].copy()

        t = t.rename(
            columns={
                "adaptive_advantage_vs_frozen_local": (
                    "transition_advantage_vs_frozen_local"
                ),
                "adaptive_advantage_vs_frozen_all_pre": (
                    "transition_advantage_vs_frozen_all_pre"
                ),
            }
        )
        c = c.rename(
            columns={
                "adaptive_advantage_vs_frozen_local": (
                    "control_advantage_vs_frozen_local"
                ),
                "adaptive_advantage_vs_frozen_all_pre": (
                    "control_advantage_vs_frozen_all_pre"
                ),
            }
        )

        paired = t.merge(c, on=keys, validate="one_to_one")
        paired.insert(0, "direction", transition)
        paired.insert(1, "matched_control", control)
        paired["excess_advantage_vs_frozen_local"] = (
            paired["transition_advantage_vs_frozen_local"]
            - paired["control_advantage_vs_frozen_local"]
        )
        paired["excess_advantage_vs_frozen_all_pre"] = (
            paired["transition_advantage_vs_frozen_all_pre"]
            - paired["control_advantage_vs_frozen_all_pre"]
        )
        row_parts.append(paired)

        for horizon, hgroup in paired.groupby("horizon", dropna=False):
            period_groups = [("all_post", hgroup)]
            period_groups.extend(
                (period, part)
                for period, part in hgroup.groupby("period", dropna=False)
            )
            for period, part in period_groups:
                summary_rows.append(
                    {
                        "direction": transition,
                        "matched_control": control,
                        "horizon": int(horizon),
                        "period": period,
                        "n_pairs": int(len(part)),
                        "mean_excess_advantage_vs_frozen_local": float(
                            part["excess_advantage_vs_frozen_local"].mean()
                        ),
                        "mean_excess_advantage_vs_frozen_all_pre": float(
                            part["excess_advantage_vs_frozen_all_pre"].mean()
                        ),
                    }
                )

    paired = pd.concat(row_parts, ignore_index=True)
    return paired, pd.DataFrame(summary_rows)


def _seed_summary(
    frame: pd.DataFrame,
    paired: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    direct_rows: list[dict] = []
    for (transition, horizon, seed), group in frame.groupby(
        ["transition", "horizon", "seed"],
        dropna=False,
    ):
        a = float(group["adaptive_mse"].mean())
        fl = float(group["frozen_local_mse"].mean())
        fa = float(group["frozen_all_pre_mse"].mean())
        direct_rows.append(
            {
                "transition": transition,
                "horizon": int(horizon),
                "seed": int(seed),
                "adaptive_rmse_vs_frozen_local": float(np.sqrt(a / fl)),
                "adaptive_rmse_vs_frozen_all_pre": float(np.sqrt(a / fa)),
                "adaptive_advantage_vs_frozen_local": float(fl - a),
                "adaptive_advantage_vs_frozen_all_pre": float(fa - a),
            }
        )

    excess_rows: list[dict] = []
    for (direction, control, horizon, seed), group in paired.groupby(
        ["direction", "matched_control", "horizon", "seed"],
        dropna=False,
    ):
        excess_rows.append(
            {
                "direction": direction,
                "matched_control": control,
                "horizon": int(horizon),
                "seed": int(seed),
                "mean_excess_advantage_vs_frozen_local": float(
                    group["excess_advantage_vs_frozen_local"].mean()
                ),
                "mean_excess_advantage_vs_frozen_all_pre": float(
                    group["excess_advantage_vs_frozen_all_pre"].mean()
                ),
            }
        )

    return pd.DataFrame(direct_rows), pd.DataFrame(excess_rows)


def _resolve_workers(requested: int, n_tasks: int) -> int:
    requested = int(requested)
    if requested < 0:
        raise ValueError("workers must be >= 0.")
    if requested == 1:
        return 1
    if requested > 1:
        return min(requested, n_tasks)

    logical = os.cpu_count() or 1
    auto = max(1, logical - 2)
    return min(16, auto, n_tasks)


def _run_config_payload(payload) -> list[dict]:
    seed, transition, pre_sd, post_sd, horizon, args = payload
    return run_configuration(
        seed=int(seed),
        transition=str(transition),
        pre_slope_noise_std=float(pre_sd),
        post_slope_noise_std=float(post_sd),
        horizon=int(horizon),
        args=args,
    )


def main() -> None:
    args = parse_args()

    if args.preset == "smoke":
        horizons = SMOKE_HORIZONS
        default_seeds = 1
        default_n_grid = 81
    else:
        horizons = EXPLORE_HORIZONS
        default_seeds = 30
        default_n_grid = 321

    n_seeds = default_seeds if args.n_seeds is None else int(args.n_seeds)
    args.n_grid = default_n_grid if args.n_grid is None else int(args.n_grid)
    args.log_lambda_min = (
        -18.0 if args.log_lambda_min is None else float(args.log_lambda_min)
    )
    args.log_lambda_max = (
        24.0 if args.log_lambda_max is None else float(args.log_lambda_max)
    )

    if n_seeds <= 0:
        raise ValueError("n-seeds must be positive.")
    if not args.low_slope_noise_std < args.high_slope_noise_std:
        raise ValueError(
            "Require low-slope-noise-std < high-slope-noise-std."
        )
    if args.selector_max_inner_origins <= 1:
        raise ValueError("selector-max-inner-origins must exceed 1.")

    transitions = _roughness_transitions(
        float(args.low_slope_noise_std),
        float(args.high_slope_noise_std),
    )
    configs = list(
        product(
            range(n_seeds),
            tuple(transitions.items()),
            horizons,
        )
    )

    payloads = [
        (
            int(seed),
            transition,
            float(pre_sd),
            float(post_sd),
            int(horizon),
            args,
        )
        for seed, (transition, (pre_sd, post_sd)), horizon in configs
    ]
    workers = _resolve_workers(args.workers, len(payloads))
    print(
        f"Execution: {workers} worker process" +
        ("" if workers == 1 else "es") +
        f" for {len(payloads)} configurations",
        flush=True,
    )

    rows: list[dict] = []
    total_start = time.perf_counter()

    if workers == 1:
        iterator = map(_run_config_payload, payloads)
        for i, result_rows in enumerate(iterator, start=1):
            rows.extend(result_rows)
            print(f"[{i}/{len(payloads)}] completed", flush=True)
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            iterator = executor.map(
                _run_config_payload,
                payloads,
                chunksize=1,
            )
            for i, result_rows in enumerate(iterator, start=1):
                rows.extend(result_rows)
                print(f"[{i}/{len(payloads)}] completed", flush=True)

    frame = pd.DataFrame(rows)
    elapsed = time.perf_counter() - total_start

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = (
        Path("results")
        / "forecast_optimal_smoothing"
        / f"{stamp}_fixed-baseline-stress_{args.preset}_{git_short_sha()}"
    )
    run_dir.mkdir(parents=True, exist_ok=True)

    frame.to_csv(run_dir / "baseline_stress_grid.csv", index=False)
    _summary(frame).to_csv(
        run_dir / "baseline_stress_summary.csv",
        index=False,
    )

    paired, paired_summary = _paired_control_summary(frame)
    paired.to_csv(
        run_dir / "baseline_stress_paired.csv",
        index=False,
    )
    paired_summary.to_csv(
        run_dir / "baseline_stress_paired_summary.csv",
        index=False,
    )

    seed_direct, seed_excess = _seed_summary(frame, paired)
    seed_direct.to_csv(
        run_dir / "baseline_stress_seed_summary.csv",
        index=False,
    )
    seed_excess.to_csv(
        run_dir / "baseline_stress_seed_excess.csv",
        index=False,
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_short_sha(),
        "experiment": "roughness_fixed_baseline_stress",
        "preset": args.preset,
        "n_seeds": n_seeds,
        "n_obs": args.n_obs,
        "regime_point": args.regime_point,
        "low_slope_noise_std": args.low_slope_noise_std,
        "high_slope_noise_std": args.high_slope_noise_std,
        "observation_noise_std": args.observation_noise_std,
        "fixed_ar1_phi": args.ar1_phi,
        "selector_max_inner_origins": args.selector_max_inner_origins,
        "workers": workers,
        "logical_cpus": os.cpu_count(),
        "inner_step": args.inner_step,
        "outer_step": args.outer_step,
        "orders": list(args.orders),
        "windows": list(args.windows),
        "horizons": list(horizons),
        "n_grid": args.n_grid,
        "log_lambda_bounds": [
            args.log_lambda_min,
            args.log_lambda_max,
        ],
        "frozen_baselines": {
            "frozen_local": (
                "select once at T0 using the same capped M inner origins "
                "as the adaptive selector"
            ),
            "frozen_all_pre": (
                "select once at T0 using all valid pre-T0 rolling origins "
                "at the same inner step, then keep hyperparameters fixed"
            ),
        },
        "n_configurations": len(configs),
        "n_output_rows": len(frame),
        "elapsed_seconds": elapsed,
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(f"Wrote results to {run_dir} in {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
