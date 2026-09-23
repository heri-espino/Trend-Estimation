from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

import trend_estimation as td

from run_adaptive_value import (
    _aggregate_summary,
    _block_metrics,
    _fit_frozen_forecast,
    _period,
    _seed_level_summary,
    git_short_sha,
)


SMOKE_HORIZONS = (1,)
EXPLORE_HORIZONS = (1, 3, 6, 12)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Isolate observation-noise-scale regime changes while measuring "
            "both configuration tracking and adaptive-vs-frozen forecast value."
        )
    )
    parser.add_argument("--preset", choices=("smoke", "explore"), default="explore")
    parser.add_argument("--n-seeds", type=int, default=None)
    parser.add_argument("--n-obs", type=int, default=300)
    parser.add_argument("--regime-point", type=int, default=180)
    parser.add_argument("--low-noise-std", type=float, default=0.25)
    parser.add_argument("--high-noise-std", type=float, default=0.75)
    parser.add_argument("--slope-noise-std", type=float, default=0.01)
    parser.add_argument("--ar1-phi", type=float, default=0.0)
    parser.add_argument("--outer-initial-train", type=int, default=120)
    parser.add_argument("--outer-step", type=int, default=3)
    parser.add_argument("--inner-step", type=int, default=3)
    parser.add_argument("--selector-max-inner-origins", type=int, default=20)
    parser.add_argument("--orders", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--windows", type=int, nargs="+", default=[24, 48, 72])
    parser.add_argument("--n-grid", type=int, default=None)
    parser.add_argument("--log-lambda-min", type=float, default=None)
    parser.add_argument("--log-lambda-max", type=float, default=None)
    return parser.parse_args()


def _noise_transitions(low: float, high: float) -> dict[str, tuple[float, float]]:
    return {
        "stable_low_noise": (low, low),
        "low_to_high_noise": (low, high),
        "high_to_low_noise": (high, low),
        "stable_high_noise": (high, high),
    }


def run_configuration(
    *,
    seed: int,
    transition: str,
    pre_noise_std: float,
    post_noise_std: float,
    horizon: int,
    args: argparse.Namespace,
) -> list[dict]:
    data = td.make_two_regime_local_linear_series(
        n_obs=args.n_obs,
        regime_point=args.regime_point,
        pre_slope_noise_std=args.slope_noise_std,
        post_slope_noise_std=args.slope_noise_std,
        pre_observation_noise_std=pre_noise_std,
        post_observation_noise_std=post_noise_std,
        pre_ar1_phi=args.ar1_phi,
        post_ar1_phi=args.ar1_phi,
        level_shift=0.0,
        slope_shift=0.0,
        random_state=seed,
    )

    log_bounds = (args.log_lambda_min, args.log_lambda_max)

    frozen_selection = td.select_fixed_window_pure_smoothness(
        data.y[: args.regime_point],
        orders=tuple(args.orders),
        windows=tuple(args.windows),
        horizon=horizon,
        step=args.inner_step,
        max_origins=args.selector_max_inner_origins,
        min_origins=2,
        log_bounds=log_bounds,
        n_grid=args.n_grid,
    )
    frozen = frozen_selection.best_

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
        log_bounds=log_bounds,
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
        frozen_prediction = _fit_frozen_forecast(
            history,
            order=int(frozen.order),
            window=int(frozen.window),
            lambda_=float(frozen.lambda_),
            horizon=observed.size,
        )

        adaptive_mse, adaptive_rmse = _block_metrics(
            observed,
            adaptive_prediction,
        )
        frozen_mse, frozen_rmse = _block_metrics(
            observed,
            frozen_prediction,
        )
        benchmark_mse, benchmark_rmse = _block_metrics(
            observed,
            benchmark_prediction,
        )

        relative_origin = origin - rp
        adaptive_window = int(record.selected_window)
        frozen_window = int(frozen.window)
        post_seen = max(0, relative_origin)

        rows.append(
            {
                "seed": int(seed),
                "transition": transition,
                "pre_observation_noise_std": float(pre_noise_std),
                "post_observation_noise_std": float(post_noise_std),
                "fixed_ar1_phi": float(args.ar1_phi),
                "slope_noise_std": float(args.slope_noise_std),
                "horizon": int(horizon),
                "regime_point": rp,
                "outer_origin": origin,
                "relative_origin": relative_origin,
                "period": _period(relative_origin),
                "adaptive_order": int(record.selected_order),
                "adaptive_window": adaptive_window,
                "adaptive_lambda": float(record.selected_lambda),
                "adaptive_smoothness": float(record.selected_smoothness),
                "adaptive_window_post_fraction": float(
                    min(adaptive_window, post_seen) / adaptive_window
                ),
                "frozen_order": int(frozen.order),
                "frozen_window": frozen_window,
                "frozen_lambda": float(frozen.lambda_),
                "frozen_smoothness": float(frozen.smoothness_),
                "frozen_window_post_fraction": float(
                    min(frozen_window, post_seen) / frozen_window
                ),
                "adaptive_order_differs": float(
                    int(record.selected_order) != int(frozen.order)
                ),
                "adaptive_window_differs": float(
                    adaptive_window != frozen_window
                ),
                "adaptive_smoothness_minus_frozen": (
                    float(record.selected_smoothness)
                    - float(frozen.smoothness_)
                ),
                "adaptive_mse": adaptive_mse,
                "frozen_mse": frozen_mse,
                "benchmark_mse": benchmark_mse,
                "adaptive_rmse": adaptive_rmse,
                "frozen_rmse": frozen_rmse,
                "benchmark_rmse": benchmark_rmse,
                "adaptive_mse_advantage_vs_frozen": frozen_mse - adaptive_mse,
                "adaptive_relative_rmsfe_vs_no_change": (
                    adaptive_rmse / benchmark_rmse
                    if benchmark_rmse > 0.0
                    else float("nan")
                ),
                "frozen_relative_rmsfe_vs_no_change": (
                    frozen_rmse / benchmark_rmse
                    if benchmark_rmse > 0.0
                    else float("nan")
                ),
            }
        )

    return rows


def _paired_adaptation_value(
    frame: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    pairs = (
        ("low_to_high_noise", "stable_low_noise"),
        ("high_to_low_noise", "stable_high_noise"),
    )
    row_parts: list[pd.DataFrame] = []
    summary_rows: list[dict] = []
    keys = ["seed", "horizon", "relative_origin"]

    for transition, control in pairs:
        t = frame.loc[
            frame["transition"].eq(transition),
            keys
            + [
                "period",
                "adaptive_mse",
                "frozen_mse",
                "adaptive_mse_advantage_vs_frozen",
            ],
        ].copy()
        c = frame.loc[
            frame["transition"].eq(control),
            keys
            + [
                "adaptive_mse",
                "frozen_mse",
                "adaptive_mse_advantage_vs_frozen",
            ],
        ].copy()

        t = t.rename(
            columns={
                "adaptive_mse": "transition_adaptive_mse",
                "frozen_mse": "transition_frozen_mse",
                "adaptive_mse_advantage_vs_frozen": (
                    "transition_adaptive_mse_advantage"
                ),
            }
        )
        c = c.rename(
            columns={
                "adaptive_mse": "control_adaptive_mse",
                "frozen_mse": "control_frozen_mse",
                "adaptive_mse_advantage_vs_frozen": (
                    "control_adaptive_mse_advantage"
                ),
            }
        )

        paired = t.merge(c, on=keys, validate="one_to_one")
        paired.insert(0, "direction", transition)
        paired.insert(1, "matched_control", control)
        paired["excess_adaptive_mse_advantage"] = (
            paired["transition_adaptive_mse_advantage"]
            - paired["control_adaptive_mse_advantage"]
        )
        row_parts.append(paired)

        for horizon, hgroup in paired.groupby("horizon", dropna=False):
            period_groups = [("all_post", hgroup)]
            period_groups.extend(
                (period, part)
                for period, part in hgroup.groupby("period", dropna=False)
            )
            for period, part in period_groups:
                ta = float(part["transition_adaptive_mse"].mean())
                tf = float(part["transition_frozen_mse"].mean())
                ca = float(part["control_adaptive_mse"].mean())
                cf = float(part["control_frozen_mse"].mean())
                summary_rows.append(
                    {
                        "direction": transition,
                        "matched_control": control,
                        "horizon": int(horizon),
                        "period": period,
                        "n_pairs": int(len(part)),
                        "transition_adaptive_rmse_vs_frozen": float(
                            np.sqrt(ta / tf)
                        ),
                        "control_adaptive_rmse_vs_frozen": float(
                            np.sqrt(ca / cf)
                        ),
                        "mean_excess_adaptive_mse_advantage": float(
                            part["excess_adaptive_mse_advantage"].mean()
                        ),
                    }
                )

    return pd.concat(row_parts, ignore_index=True), pd.DataFrame(summary_rows)


def _target_tracking(
    frame: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    mappings = (
        (
            "low_to_high_noise",
            "stable_low_noise",
            "stable_high_noise",
        ),
        (
            "high_to_low_noise",
            "stable_high_noise",
            "stable_low_noise",
        ),
    )
    keys = ["seed", "horizon", "relative_origin"]
    paired_parts: list[pd.DataFrame] = []

    config_cols = [
        "adaptive_order",
        "adaptive_window",
        "adaptive_smoothness",
        "adaptive_window_post_fraction",
    ]

    for direction, start_control, target_control in mappings:
        transition = frame.loc[
            frame["transition"].eq(direction),
            keys + config_cols,
        ].copy()
        start = frame.loc[
            frame["transition"].eq(start_control),
            keys + config_cols,
        ].copy()
        target = frame.loc[
            frame["transition"].eq(target_control),
            keys + config_cols,
        ].copy()

        transition = transition.rename(
            columns={c: f"transition_{c}" for c in config_cols}
        )
        start = start.rename(
            columns={c: f"start_{c}" for c in config_cols}
        )
        target = target.rename(
            columns={c: f"target_{c}" for c in config_cols}
        )

        paired = transition.merge(start, on=keys, validate="one_to_one")
        paired = paired.merge(target, on=keys, validate="one_to_one")
        paired.insert(0, "direction", direction)
        paired.insert(1, "start_control", start_control)
        paired.insert(2, "target_control", target_control)
        paired["abs_smoothness_gap_to_target"] = np.abs(
            paired["transition_adaptive_smoothness"]
            - paired["target_adaptive_smoothness"]
        )
        paired["order_match_target"] = (
            paired["transition_adaptive_order"]
            == paired["target_adaptive_order"]
        ).astype(float)
        paired["window_match_target"] = (
            paired["transition_adaptive_window"]
            == paired["target_adaptive_window"]
        ).astype(float)
        paired["discrete_config_match_target"] = (
            (
                paired["transition_adaptive_order"]
                == paired["target_adaptive_order"]
            )
            & (
                paired["transition_adaptive_window"]
                == paired["target_adaptive_window"]
            )
        ).astype(float)
        paired_parts.append(paired)

    paired = pd.concat(paired_parts, ignore_index=True)

    path = (
        paired.groupby(
            ["direction", "horizon", "relative_origin"],
            dropna=False,
        )
        .agg(
            transition_smoothness=("transition_adaptive_smoothness", "mean"),
            start_reference_smoothness=("start_adaptive_smoothness", "mean"),
            target_reference_smoothness=("target_adaptive_smoothness", "mean"),
            mean_abs_smoothness_gap_to_target=(
                "abs_smoothness_gap_to_target",
                "mean",
            ),
            mean_transition_order=("transition_adaptive_order", "mean"),
            mean_start_order=("start_adaptive_order", "mean"),
            mean_target_order=("target_adaptive_order", "mean"),
            mean_transition_window=("transition_adaptive_window", "mean"),
            mean_start_window=("start_adaptive_window", "mean"),
            mean_target_window=("target_adaptive_window", "mean"),
            order_match_target_share=("order_match_target", "mean"),
            window_match_target_share=("window_match_target", "mean"),
            discrete_config_match_target_share=(
                "discrete_config_match_target",
                "mean",
            ),
            mean_transition_window_post_fraction=(
                "transition_adaptive_window_post_fraction",
                "mean",
            ),
        )
        .reset_index()
    )
    path["reference_smoothness_shift"] = (
        path["target_reference_smoothness"]
        - path["start_reference_smoothness"]
    )
    denom = path["reference_smoothness_shift"].to_numpy(dtype=float)
    numer = (
        path["transition_smoothness"]
        - path["start_reference_smoothness"]
    ).to_numpy(dtype=float)
    path["smoothness_progress"] = np.where(
        np.abs(denom) > 1e-8,
        numer / denom,
        np.nan,
    )

    summary_rows: list[dict] = []
    for (direction, horizon), group in path.groupby(
        ["direction", "horizon"],
        dropna=False,
    ):
        post = group.loc[group["relative_origin"].ge(0)].sort_values(
            "relative_origin"
        )
        for threshold in (0.5, 0.8):
            delay = _first_sustained_progress(
                post,
                threshold=threshold,
                consecutive=3,
            )
            summary_rows.append(
                {
                    "direction": direction,
                    "horizon": int(horizon),
                    "threshold": threshold,
                    "consecutive_origins_required": 3,
                    "adaptation_delay_observations": delay,
                    "achieved": bool(np.isfinite(delay)),
                    "mean_abs_reference_smoothness_shift_post": float(
                        np.nanmean(
                            np.abs(post["reference_smoothness_shift"])
                        )
                    ),
                    "late_order_match_target_share": float(
                        post.loc[
                            post["relative_origin"].ge(72),
                            "order_match_target_share",
                        ].mean()
                    ),
                    "late_window_match_target_share": float(
                        post.loc[
                            post["relative_origin"].ge(72),
                            "window_match_target_share",
                        ].mean()
                    ),
                    "late_discrete_config_match_target_share": float(
                        post.loc[
                            post["relative_origin"].ge(72),
                            "discrete_config_match_target_share",
                        ].mean()
                    ),
                }
            )

    return paired, path, pd.DataFrame(summary_rows)


def _first_sustained_progress(
    post: pd.DataFrame,
    *,
    threshold: float,
    consecutive: int,
) -> float:
    values = post["smoothness_progress"].to_numpy(dtype=float)
    origins = post["relative_origin"].to_numpy(dtype=float)

    for i in range(0, len(values) - consecutive + 1):
        block = values[i : i + consecutive]
        if np.all(np.isfinite(block)) and np.all(block >= threshold):
            return float(origins[i])
    return float("nan")


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
    if args.low_noise_std <= 0.0 or args.high_noise_std <= 0.0:
        raise ValueError("Noise standard deviations must be positive.")
    if not args.low_noise_std < args.high_noise_std:
        raise ValueError("Require low-noise-std < high-noise-std.")
    if not -1.0 < args.ar1_phi < 1.0:
        raise ValueError("ar1-phi must lie strictly between -1 and 1.")
    if args.selector_max_inner_origins <= 1:
        raise ValueError("selector-max-inner-origins must exceed 1.")
    if not args.outer_initial_train < args.regime_point < args.n_obs:
        raise ValueError(
            "Require outer_initial_train < regime_point < n_obs."
        )

    transitions = _noise_transitions(
        float(args.low_noise_std),
        float(args.high_noise_std),
    )
    configs = list(
        product(
            range(n_seeds),
            tuple(transitions.items()),
            horizons,
        )
    )

    rows: list[dict] = []
    total_start = time.perf_counter()

    for i, (seed, transition_item, horizon) in enumerate(configs, start=1):
        transition, (pre_noise_std, post_noise_std) = transition_item
        config_start = time.perf_counter()
        print(
            f"[{i}/{len(configs)}] seed={seed} transition={transition} "
            f"sigma={pre_noise_std}->{post_noise_std} h={horizon}",
            flush=True,
        )

        new_rows = run_configuration(
            seed=int(seed),
            transition=transition,
            pre_noise_std=float(pre_noise_std),
            post_noise_std=float(post_noise_std),
            horizon=int(horizon),
            args=args,
        )
        rows.extend(new_rows)

        print(
            f"    completed in {time.perf_counter() - config_start:.2f}s; "
            f"post-T0 rows={len(new_rows)}",
            flush=True,
        )

    frame = pd.DataFrame(rows)
    elapsed = time.perf_counter() - total_start

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = (
        Path("results")
        / "forecast_optimal_smoothing"
        / f"{stamp}_noise-scale-adaptation_{args.preset}_{git_short_sha()}"
    )
    run_dir.mkdir(parents=True, exist_ok=True)

    frame.to_csv(run_dir / "noise_adaptation_grid.csv", index=False)

    value_summary = _aggregate_summary(frame)
    value_summary.to_csv(
        run_dir / "noise_adaptive_value_summary.csv",
        index=False,
    )

    paired_value, paired_value_summary = _paired_adaptation_value(frame)
    paired_value.to_csv(
        run_dir / "noise_paired_adaptation_value.csv",
        index=False,
    )
    paired_value_summary.to_csv(
        run_dir / "noise_paired_adaptation_value_summary.csv",
        index=False,
    )

    seed_direct, seed_excess = _seed_level_summary(frame, paired_value)
    seed_direct.to_csv(
        run_dir / "noise_adaptive_value_seed_summary.csv",
        index=False,
    )
    seed_excess.to_csv(
        run_dir / "noise_paired_adaptation_value_seed_summary.csv",
        index=False,
    )

    tracking, tracking_path, tracking_summary = _target_tracking(frame)
    tracking.to_csv(
        run_dir / "noise_target_tracking.csv",
        index=False,
    )
    tracking_path.to_csv(
        run_dir / "noise_target_tracking_path.csv",
        index=False,
    )
    tracking_summary.to_csv(
        run_dir / "noise_target_tracking_summary.csv",
        index=False,
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_short_sha(),
        "experiment": "observation_noise_scale_adaptation_value",
        "preset": args.preset,
        "n_seeds": n_seeds,
        "n_obs": args.n_obs,
        "regime_point": args.regime_point,
        "low_observation_noise_std": args.low_noise_std,
        "high_observation_noise_std": args.high_noise_std,
        "slope_noise_std": args.slope_noise_std,
        "fixed_ar1_phi": args.ar1_phi,
        "level_shift": 0.0,
        "slope_shift": 0.0,
        "outer_initial_train": args.outer_initial_train,
        "outer_step": args.outer_step,
        "inner_step": args.inner_step,
        "selector_max_inner_origins": args.selector_max_inner_origins,
        "orders": list(args.orders),
        "windows": list(args.windows),
        "n_grid": args.n_grid,
        "log_lambda_bounds": [
            args.log_lambda_min,
            args.log_lambda_max,
        ],
        "transitions": {
            name: {
                "pre_observation_noise_std": pre,
                "post_observation_noise_std": post,
            }
            for name, (pre, post) in transitions.items()
        },
        "horizons": list(horizons),
        "n_configurations": len(configs),
        "n_output_rows": len(frame),
        "elapsed_seconds": elapsed,
        "comparison": {
            "adaptive": (
                "re-select d, L, lambda at every outer origin with M inner "
                "origins"
            ),
            "frozen_pre": (
                "select d, L, lambda once at T0 using only y[:T0], then "
                "refit with those hyperparameters on newly observed data"
            ),
            "benchmark": "no-change level forecast",
            "target_tracking": (
                "compare transition adaptive configuration with matched start "
                "and target stationary controls at the same seed/horizon/origin"
            ),
        },
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(f"Wrote results to {run_dir} in {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
