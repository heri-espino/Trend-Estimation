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

from run_regime_transition import TRANSITIONS


SMOKE_HORIZONS = (1,)
EXPLORE_HORIZONS = (1, 3, 6, 12)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare adaptive re-selection of (d, L, S) against hyperparameters "
            "frozen at the regime point using only pre-change information."
        )
    )
    parser.add_argument("--preset", choices=("smoke", "explore"), default="explore")
    parser.add_argument("--n-seeds", type=int, default=None)
    parser.add_argument("--n-obs", type=int, default=300)
    parser.add_argument("--regime-point", type=int, default=180)
    parser.add_argument("--slope-noise-std", type=float, default=0.01)
    parser.add_argument("--observation-noise-std", type=float, default=0.5)
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


def git_short_sha() -> str:
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


def _block_metrics(observed, prediction) -> tuple[float, float]:
    error = np.asarray(observed, dtype=float) - np.asarray(prediction, dtype=float)
    mse = float(np.mean(error**2))
    rmse = float(np.sqrt(mse))
    return mse, rmse


def _period(relative_origin: int) -> str:
    if relative_origin < 36:
        return "early"
    if relative_origin < 72:
        return "mid"
    return "late"


def _fit_frozen_forecast(
    history,
    *,
    order: int,
    window: int,
    lambda_: float,
    horizon: int,
):
    fit_history = np.asarray(history[-window:], dtype=float)
    model = td.PurePenalizedTrend(
        order=order,
        smoothness=None,
        lambda_=lambda_,
    ).fit(fit_history)
    return model.forecast(horizon)


def run_configuration(
    *,
    seed: int,
    transition: str,
    pre_phi: float,
    post_phi: float,
    horizon: int,
    args: argparse.Namespace,
) -> list[dict]:
    data = td.make_two_regime_local_linear_series(
        n_obs=args.n_obs,
        regime_point=args.regime_point,
        pre_slope_noise_std=args.slope_noise_std,
        post_slope_noise_std=args.slope_noise_std,
        pre_observation_noise_std=args.observation_noise_std,
        post_observation_noise_std=args.observation_noise_std,
        pre_ar1_phi=pre_phi,
        post_ar1_phi=post_phi,
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

        frozen_prediction = _fit_frozen_forecast(
            history,
            order=int(frozen.order),
            window=int(frozen.window),
            lambda_=float(frozen.lambda_),
            horizon=observed.size,
        )
        adaptive_prediction = np.asarray(record.prediction, dtype=float)
        benchmark_prediction = np.asarray(
            record.benchmark_prediction,
            dtype=float,
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

        rows.append(
            {
                "seed": int(seed),
                "transition": transition,
                "pre_phi": float(pre_phi),
                "post_phi": float(post_phi),
                "horizon": int(horizon),
                "regime_point": rp,
                "outer_origin": origin,
                "relative_origin": relative_origin,
                "period": _period(relative_origin),
                "adaptive_order": int(record.selected_order),
                "adaptive_window": int(record.selected_window),
                "adaptive_lambda": float(record.selected_lambda),
                "adaptive_smoothness": float(record.selected_smoothness),
                "frozen_order": int(frozen.order),
                "frozen_window": int(frozen.window),
                "frozen_lambda": float(frozen.lambda_),
                "frozen_smoothness": float(frozen.smoothness_),
                "adaptive_order_differs": float(
                    int(record.selected_order) != int(frozen.order)
                ),
                "adaptive_window_differs": float(
                    int(record.selected_window) != int(frozen.window)
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


def _aggregate_summary(frame: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    group_cols = ["transition", "horizon"]

    for keys, group in frame.groupby(group_cols, dropna=False):
        transition, horizon = keys
        period_groups = [("all_post", group)]
        period_groups.extend(
            (period, part)
            for period, part in group.groupby("period", dropna=False)
        )

        for period, part in period_groups:
            adaptive_mse = float(part["adaptive_mse"].mean())
            frozen_mse = float(part["frozen_mse"].mean())
            benchmark_mse = float(part["benchmark_mse"].mean())

            rows.append(
                {
                    "transition": transition,
                    "horizon": int(horizon),
                    "period": period,
                    "n_blocks": int(len(part)),
                    "adaptive_mse": adaptive_mse,
                    "frozen_mse": frozen_mse,
                    "benchmark_mse": benchmark_mse,
                    "adaptive_rmse_vs_frozen": float(
                        np.sqrt(adaptive_mse / frozen_mse)
                    ),
                    "adaptive_relative_rmsfe_vs_no_change": float(
                        np.sqrt(adaptive_mse / benchmark_mse)
                    ),
                    "frozen_relative_rmsfe_vs_no_change": float(
                        np.sqrt(frozen_mse / benchmark_mse)
                    ),
                    "mean_adaptive_mse_advantage_vs_frozen": float(
                        part["adaptive_mse_advantage_vs_frozen"].mean()
                    ),
                    "order_diff_share": float(
                        part["adaptive_order_differs"].mean()
                    ),
                    "window_diff_share": float(
                        part["adaptive_window_differs"].mean()
                    ),
                    "mean_abs_smoothness_change": float(
                        np.abs(
                            part["adaptive_smoothness_minus_frozen"]
                        ).mean()
                    ),
                }
            )

    return pd.DataFrame(rows)


def _paired_transition_control(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    pairs = (
        ("low_to_high", "stable_low"),
        ("high_to_low", "stable_high"),
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
    if args.selector_max_inner_origins <= 1:
        raise ValueError("selector-max-inner-origins must exceed 1.")
    if not args.outer_initial_train < args.regime_point < args.n_obs:
        raise ValueError(
            "Require outer_initial_train < regime_point < n_obs."
        )

    configs = list(
        product(
            range(n_seeds),
            tuple(TRANSITIONS.items()),
            horizons,
        )
    )

    rows: list[dict] = []
    total_start = time.perf_counter()

    for i, (seed, transition_item, horizon) in enumerate(configs, start=1):
        transition, (pre_phi, post_phi) = transition_item
        config_start = time.perf_counter()
        print(
            f"[{i}/{len(configs)}] seed={seed} transition={transition} "
            f"phi={pre_phi}->{post_phi} h={horizon}",
            flush=True,
        )

        new_rows = run_configuration(
            seed=int(seed),
            transition=transition,
            pre_phi=float(pre_phi),
            post_phi=float(post_phi),
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
        / f"{stamp}_adaptive-value_{args.preset}_{git_short_sha()}"
    )
    run_dir.mkdir(parents=True, exist_ok=True)

    frame.to_csv(run_dir / "adaptive_value_grid.csv", index=False)

    summary = _aggregate_summary(frame)
    summary.to_csv(run_dir / "adaptive_value_summary.csv", index=False)

    paired, paired_summary = _paired_transition_control(frame)
    paired.to_csv(run_dir / "paired_adaptation_value.csv", index=False)
    paired_summary.to_csv(
        run_dir / "paired_adaptation_value_summary.csv",
        index=False,
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_short_sha(),
        "experiment": "adaptive_vs_frozen_pre",
        "preset": args.preset,
        "n_seeds": n_seeds,
        "n_obs": args.n_obs,
        "regime_point": args.regime_point,
        "slope_noise_std": args.slope_noise_std,
        "observation_noise_std": args.observation_noise_std,
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
            name: {"pre_phi": pre, "post_phi": post}
            for name, (pre, post) in TRANSITIONS.items()
        },
        "horizons": list(horizons),
        "n_configurations": len(configs),
        "n_output_rows": len(frame),
        "elapsed_seconds": elapsed,
        "comparison": {
            "adaptive": (
                "re-select d, L, lambda at every outer origin using only "
                "history available at that origin"
            ),
            "frozen_pre": (
                "select d, L, lambda once at T0 using only y[:T0], then "
                "keep hyperparameters fixed while refitting on the latest "
                "frozen window at each later origin"
            ),
            "benchmark": "no-change level forecast",
        },
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(f"Wrote results to {run_dir} in {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
