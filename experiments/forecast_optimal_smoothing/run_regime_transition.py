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


TRANSITIONS = {
    "stable_low": (0.0, 0.0),
    "low_to_high": (0.0, 0.8),
    "high_to_low": (0.8, 0.0),
    "stable_high": (0.8, 0.8),
}

SMOKE_HORIZONS = (1,)
EXPLORE_HORIZONS = (1, 3, 6, 12)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Within-series persistence-regime transition experiment. "
            "Tracks the forecast-optimal (order, window, smoothness) path "
            "against paired stationary controls."
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
    parser.add_argument("--max-inner-origins", type=int, default=30)
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


def _forecast_block_relation(start: int, stop: int, regime_point: int) -> str:
    if stop <= regime_point:
        return "pre"
    if start >= regime_point:
        return "post"
    return "crossing"


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

    nested = td.nested_rolling_pure_forecast(
        data.y,
        outer_initial_train=args.outer_initial_train,
        horizon=horizon,
        outer_step=args.outer_step,
        orders=tuple(args.orders),
        windows=tuple(args.windows),
        inner_step=args.inner_step,
        max_inner_origins=args.max_inner_origins,
        min_inner_origins=2,
        log_bounds=(args.log_lambda_min, args.log_lambda_max),
        n_grid=args.n_grid,
    )

    rows: list[dict] = []
    rp = int(args.regime_point)

    for record in nested.records:
        origin = int(record.origin)
        relative_origin = origin - rp
        post_seen = max(0, relative_origin)
        inner_origins = np.asarray(
            record.inner_selection.common_inner_origins_,
            dtype=int,
        )
        inner_post_fraction = float(np.mean(inner_origins >= rp))
        window = int(record.selected_window)
        selected_post_count = min(window, post_seen)
        selected_pre_count = window - selected_post_count
        selected_post_fraction = selected_post_count / window

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

        search = record.inner_selection.best_.search_

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
                "post_observations_seen": post_seen,
                "inner_origin_count": int(inner_origins.size),
                "inner_origin_earliest": int(inner_origins[0]),
                "inner_origin_latest": int(inner_origins[-1]),
                "inner_origin_post_fraction": inner_post_fraction,
                "selected_window_pre_count": selected_pre_count,
                "selected_window_post_count": selected_post_count,
                "selected_window_post_fraction": selected_post_fraction,
                "forecast_block_relation": _forecast_block_relation(
                    int(record.validation_start),
                    int(record.validation_stop),
                    rp,
                ),
                "selected_order": int(record.selected_order),
                "selected_window": window,
                "selected_lambda": float(record.selected_lambda),
                "selected_smoothness": float(record.selected_smoothness),
                "inner_objective": float(record.inner_objective),
                "search_source": search.best_source_,
                "n_stationary_points": len(search.points_),
                "outer_block_mse": block_mse,
                "benchmark_block_mse": benchmark_mse,
                "relative_rmsfe_block": relative_rmsfe,
            }
        )

    return rows


def _mode_int(values: pd.Series) -> int:
    mode = values.mode()
    if mode.empty:
        raise ValueError("Cannot compute mode of an empty series.")
    return int(mode.iloc[0])


def write_path_summary(frame: pd.DataFrame, path: Path) -> pd.DataFrame:
    working = frame.copy()
    working["is_lower_boundary"] = working["search_source"].eq("lower_boundary")
    working["is_upper_boundary"] = working["search_source"].eq("upper_boundary")

    group_cols = ["transition", "pre_phi", "post_phi", "horizon", "relative_origin"]
    summary = (
        working.groupby(group_cols, dropna=False)
        .agg(
            n_seeds=("seed", "size"),
            mean_order=("selected_order", "mean"),
            modal_order=("selected_order", _mode_int),
            mean_window=("selected_window", "mean"),
            modal_window=("selected_window", _mode_int),
            mean_smoothness=("selected_smoothness", "mean"),
            median_smoothness=("selected_smoothness", "median"),
            mean_selected_window_post_fraction=(
                "selected_window_post_fraction",
                "mean",
            ),
            frac_lower_boundary=("is_lower_boundary", "mean"),
            frac_upper_boundary=("is_upper_boundary", "mean"),
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
    return summary


def write_selection_shares(frame: pd.DataFrame, path: Path) -> None:
    group_cols = ["transition", "horizon", "relative_origin"]
    shares = (
        frame.groupby(
            group_cols + ["selected_order", "selected_window"],
            dropna=False,
        )
        .size()
        .reset_index(name="count")
    )
    totals = shares.groupby(group_cols)["count"].transform("sum")
    shares["fraction"] = shares["count"] / totals
    shares.to_csv(path, index=False)


def build_paired_comparisons(frame: pd.DataFrame) -> pd.DataFrame:
    index_cols = ["seed", "horizon", "relative_origin"]
    value_cols = index_cols + [
        "selected_order",
        "selected_window",
        "selected_smoothness",
        "selected_window_post_fraction",
    ]

    def scenario(name: str, prefix: str) -> pd.DataFrame:
        subset = frame.loc[frame["transition"].eq(name), value_cols].copy()
        return subset.rename(
            columns={
                "selected_order": f"{prefix}_order",
                "selected_window": f"{prefix}_window",
                "selected_smoothness": f"{prefix}_smoothness",
                "selected_window_post_fraction": f"{prefix}_window_post_fraction",
            }
        )

    outputs: list[pd.DataFrame] = []
    for transition, start_name, target_name in (
        ("low_to_high", "stable_low", "stable_high"),
        ("high_to_low", "stable_high", "stable_low"),
    ):
        trans = scenario(transition, "transition")
        start = scenario(start_name, "start")
        target = scenario(target_name, "target")

        merged = (
            trans.merge(start, on=index_cols, validate="one_to_one")
            .merge(target, on=index_cols, validate="one_to_one")
        )
        merged.insert(0, "direction", transition)
        merged["abs_smoothness_gap_to_target"] = np.abs(
            merged["transition_smoothness"] - merged["target_smoothness"]
        )
        merged["order_match_target"] = (
            merged["transition_order"].eq(merged["target_order"]).astype(float)
        )
        merged["window_match_target"] = (
            merged["transition_window"].eq(merged["target_window"]).astype(float)
        )
        merged["discrete_config_match_target"] = (
            merged["transition_order"].eq(merged["target_order"])
            & merged["transition_window"].eq(merged["target_window"])
        ).astype(float)
        outputs.append(merged)

    return pd.concat(outputs, ignore_index=True)


def build_adaptation_path(paired: pd.DataFrame) -> pd.DataFrame:
    path = (
        paired.groupby(["direction", "horizon", "relative_origin"], dropna=False)
        .agg(
            transition_smoothness=("transition_smoothness", "mean"),
            start_reference_smoothness=("start_smoothness", "mean"),
            target_reference_smoothness=("target_smoothness", "mean"),
            mean_abs_smoothness_gap_to_target=(
                "abs_smoothness_gap_to_target",
                "mean",
            ),
            mean_transition_order=("transition_order", "mean"),
            mean_start_order=("start_order", "mean"),
            mean_target_order=("target_order", "mean"),
            mean_transition_window=("transition_window", "mean"),
            mean_start_window=("start_window", "mean"),
            mean_target_window=("target_window", "mean"),
            order_match_target_share=("order_match_target", "mean"),
            window_match_target_share=("window_match_target", "mean"),
            discrete_config_match_target_share=(
                "discrete_config_match_target",
                "mean",
            ),
            mean_transition_window_post_fraction=(
                "transition_window_post_fraction",
                "mean",
            ),
        )
        .reset_index()
    )

    denom = (
        path["target_reference_smoothness"]
        - path["start_reference_smoothness"]
    )
    numer = (
        path["transition_smoothness"]
        - path["start_reference_smoothness"]
    )
    path["reference_smoothness_shift"] = denom
    path["smoothness_progress"] = np.where(
        np.abs(denom) > 1e-8,
        numer / denom,
        np.nan,
    )
    return path


def _first_sustained_threshold(
    path: pd.DataFrame,
    *,
    threshold: float,
    consecutive: int = 3,
) -> float:
    post = path.loc[path["relative_origin"].ge(0)].sort_values("relative_origin")
    values = post["smoothness_progress"].to_numpy(dtype=float)
    times = post["relative_origin"].to_numpy(dtype=float)

    for i in range(0, len(values) - consecutive + 1):
        window = values[i : i + consecutive]
        if np.all(np.isfinite(window)) and np.all(window >= threshold):
            return float(times[i])
    return float("nan")


def write_adaptation_outputs(
    paired: pd.DataFrame,
    *,
    path_output: Path,
    summary_output: Path,
) -> None:
    adaptation_path = build_adaptation_path(paired)
    adaptation_path.to_csv(path_output, index=False)

    rows: list[dict] = []
    for (direction, horizon), group in adaptation_path.groupby(
        ["direction", "horizon"],
        dropna=False,
    ):
        post = group.loc[group["relative_origin"].ge(0)]
        mean_reference_shift = float(
            np.nanmean(np.abs(post["reference_smoothness_shift"]))
        )
        for threshold in (0.5, 0.8):
            delay = _first_sustained_threshold(
                group,
                threshold=threshold,
                consecutive=3,
            )
            rows.append(
                {
                    "direction": direction,
                    "horizon": int(horizon),
                    "threshold": threshold,
                    "consecutive_origins_required": 3,
                    "mean_abs_reference_smoothness_shift_post": (
                        mean_reference_shift
                    ),
                    "adaptation_delay_observations": delay,
                    "achieved": bool(np.isfinite(delay)),
                }
            )

    pd.DataFrame(rows).to_csv(summary_output, index=False)


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

    args.n_grid = default_n_grid if args.n_grid is None else int(args.n_grid)
    args.log_lambda_min = (
        -18.0 if args.log_lambda_min is None else float(args.log_lambda_min)
    )
    args.log_lambda_max = (
        24.0 if args.log_lambda_max is None else float(args.log_lambda_max)
    )
    n_seeds = default_seeds if args.n_seeds is None else int(args.n_seeds)

    if n_seeds <= 0:
        raise ValueError("n-seeds must be positive.")
    if not args.outer_initial_train < args.regime_point < args.n_obs:
        raise ValueError(
            "Require outer_initial_train < regime_point < n_obs so both "
            "pre- and post-change outer origins are observable."
        )
    if args.n_obs - args.regime_point < max(args.windows):
        raise ValueError(
            "The post-change segment must be at least as long as the largest "
            "candidate window so full post-regime memory is observable."
        )

    transition_items = tuple(TRANSITIONS.items())
    configs = list(
        product(
            range(n_seeds),
            transition_items,
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
            f"outer rows={len(new_rows)}",
            flush=True,
        )

    frame = pd.DataFrame(rows)
    elapsed = time.perf_counter() - total_start

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = (
        Path("results")
        / "forecast_optimal_smoothing"
        / f"{stamp}_regime-transition_{args.preset}_{git_short_sha()}"
    )
    run_dir.mkdir(parents=True, exist_ok=True)

    frame.to_csv(run_dir / "transition_grid.csv", index=False)
    write_path_summary(frame, run_dir / "path_summary.csv")
    write_selection_shares(frame, run_dir / "selection_shares.csv")

    paired = build_paired_comparisons(frame)
    paired.to_csv(run_dir / "paired_controls.csv", index=False)
    write_adaptation_outputs(
        paired,
        path_output=run_dir / "adaptation_path.csv",
        summary_output=run_dir / "adaptation_summary.csv",
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_short_sha(),
        "experiment": "within_series_persistence_regime_transition",
        "preset": args.preset,
        "n_seeds": n_seeds,
        "n_obs": args.n_obs,
        "regime_point": args.regime_point,
        "slope_noise_std": args.slope_noise_std,
        "observation_noise_std": args.observation_noise_std,
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
        "transitions": {
            name: {"pre_phi": pre, "post_phi": post}
            for name, (pre, post) in TRANSITIONS.items()
        },
        "horizons": list(horizons),
        "n_configurations": len(configs),
        "n_output_rows": len(frame),
        "elapsed_seconds": elapsed,
        "adaptation_definition": {
            "smoothness_progress": (
                "(transition - matched start control) / "
                "(matched target control - matched start control)"
            ),
            "thresholds": [0.5, 0.8],
            "consecutive_origins_required": 3,
            "delay_unit": "post-change observations available at forecast origin",
        },
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(f"Wrote results to {run_dir} in {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
