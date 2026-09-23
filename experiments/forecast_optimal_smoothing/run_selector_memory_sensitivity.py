from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

from run_regime_transition import (
    EXPLORE_HORIZONS,
    SMOKE_HORIZONS,
    TRANSITIONS,
    _first_sustained_threshold,
    build_adaptation_path,
    build_paired_comparisons,
    git_short_sha,
    run_configuration,
)


MEMORY_GRID = (5, 10, 20, 30)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Sensitivity study for the memory of the inner rolling selector. "
            "Repeats the paired regime-transition experiment while varying "
            "max_inner_origins."
        )
    )
    parser.add_argument("--preset", choices=("smoke", "explore"), default="explore")
    parser.add_argument("--n-seeds", type=int, default=None)
    parser.add_argument(
        "--max-inner-origins-grid",
        type=int,
        nargs="+",
        default=list(MEMORY_GRID),
    )
    parser.add_argument("--n-obs", type=int, default=300)
    parser.add_argument("--regime-point", type=int, default=180)
    parser.add_argument("--slope-noise-std", type=float, default=0.01)
    parser.add_argument("--observation-noise-std", type=float, default=0.5)
    parser.add_argument("--outer-initial-train", type=int, default=120)
    parser.add_argument("--outer-step", type=int, default=3)
    parser.add_argument("--inner-step", type=int, default=3)
    parser.add_argument("--orders", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--windows", type=int, nargs="+", default=[24, 48, 72])
    parser.add_argument("--n-grid", type=int, default=None)
    parser.add_argument("--log-lambda-min", type=float, default=None)
    parser.add_argument("--log-lambda-max", type=float, default=None)
    return parser.parse_args()


def write_skill_summary(frame: pd.DataFrame, path: Path) -> None:
    working = frame.copy()
    working["period"] = np.select(
        [
            working["relative_origin"] < 0,
            (working["relative_origin"] >= 0) & (working["relative_origin"] < 36),
            (working["relative_origin"] >= 36) & (working["relative_origin"] < 72),
        ],
        ["pre", "early", "mid"],
        default="late",
    )

    summary = (
        working.groupby(
            [
                "selector_max_inner_origins",
                "transition",
                "horizon",
                "period",
            ],
            dropna=False,
        )
        .agg(
            n_blocks=("outer_origin", "size"),
            mean_selected_order=("selected_order", "mean"),
            mean_selected_window=("selected_window", "mean"),
            mean_selected_smoothness=("selected_smoothness", "mean"),
            mean_inner_origin_post_fraction=(
                "inner_origin_post_fraction",
                "mean",
            ),
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


def build_memory_adaptation_outputs(
    frame: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    paired_parts: list[pd.DataFrame] = []
    path_parts: list[pd.DataFrame] = []
    summary_rows: list[dict] = []

    for memory, subset in frame.groupby(
        "selector_max_inner_origins",
        dropna=False,
    ):
        paired = build_paired_comparisons(subset)
        paired.insert(0, "selector_max_inner_origins", int(memory))
        paired_parts.append(paired)

        adaptation_path = build_adaptation_path(paired)
        adaptation_path.insert(
            0,
            "selector_max_inner_origins",
            int(memory),
        )

        inner_path = (
            subset.loc[
                subset["transition"].isin(["low_to_high", "high_to_low"])
            ]
            .groupby(
                ["transition", "horizon", "relative_origin"],
                dropna=False,
            )
            .agg(
                mean_inner_origin_post_fraction=(
                    "inner_origin_post_fraction",
                    "mean",
                ),
                mean_selected_window_post_fraction=(
                    "selected_window_post_fraction",
                    "mean",
                ),
            )
            .reset_index()
            .rename(columns={"transition": "direction"})
        )

        adaptation_path = adaptation_path.merge(
            inner_path,
            on=["direction", "horizon", "relative_origin"],
            how="left",
            validate="one_to_one",
        )
        path_parts.append(adaptation_path)

        for (direction, horizon), group in adaptation_path.groupby(
            ["direction", "horizon"],
            dropna=False,
        ):
            post = group.loc[group["relative_origin"].ge(0)]
            first_all_inner_post = post.loc[
                post["mean_inner_origin_post_fraction"].ge(1.0 - 1e-12),
                "relative_origin",
            ]
            first_all_inner_post_value = (
                float(first_all_inner_post.iloc[0])
                if not first_all_inner_post.empty
                else float("nan")
            )

            for threshold in (0.5, 0.8):
                delay = _first_sustained_threshold(
                    group,
                    threshold=threshold,
                    consecutive=3,
                )
                summary_rows.append(
                    {
                        "selector_max_inner_origins": int(memory),
                        "selector_validation_span_observations": (
                            (int(memory) - 1) * int(subset["inner_step"].iloc[0])
                            if "inner_step" in subset.columns
                            else (int(memory) - 1) * 3
                        ),
                        "direction": direction,
                        "horizon": int(horizon),
                        "threshold": threshold,
                        "adaptation_delay_observations": delay,
                        "achieved": bool(np.isfinite(delay)),
                        "first_all_inner_origins_post_regime": (
                            first_all_inner_post_value
                        ),
                        "mean_abs_reference_smoothness_shift_post": float(
                            np.nanmean(
                                np.abs(post["reference_smoothness_shift"])
                            )
                        ),
                    }
                )

    return (
        pd.concat(paired_parts, ignore_index=True),
        pd.concat(path_parts, ignore_index=True),
        pd.DataFrame(summary_rows),
    )


def main() -> None:
    args = parse_args()

    if args.preset == "smoke":
        horizons = SMOKE_HORIZONS
        default_seeds = 1
        default_n_grid = 81
        memory_grid = tuple(args.max_inner_origins_grid[:2])
    else:
        horizons = EXPLORE_HORIZONS
        default_seeds = 30
        default_n_grid = 321
        memory_grid = tuple(args.max_inner_origins_grid)

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
    if not memory_grid or any(int(value) <= 1 for value in memory_grid):
        raise ValueError("All max-inner-origin values must exceed 1.")
    if not args.outer_initial_train < args.regime_point < args.n_obs:
        raise ValueError(
            "Require outer_initial_train < regime_point < n_obs."
        )

    configs = list(
        product(
            memory_grid,
            range(n_seeds),
            tuple(TRANSITIONS.items()),
            horizons,
        )
    )

    rows: list[dict] = []
    total_start = time.perf_counter()

    for i, (memory, seed, transition_item, horizon) in enumerate(
        configs,
        start=1,
    ):
        transition, (pre_phi, post_phi) = transition_item
        args.max_inner_origins = int(memory)

        config_start = time.perf_counter()
        print(
            f"[{i}/{len(configs)}] memory={memory} seed={seed} "
            f"transition={transition} phi={pre_phi}->{post_phi} h={horizon}",
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
        for row in new_rows:
            row["selector_max_inner_origins"] = int(memory)
            row["selector_validation_span_observations"] = (
                (int(memory) - 1) * int(args.inner_step)
            )
            row["inner_step"] = int(args.inner_step)
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
        / f"{stamp}_selector-memory_{args.preset}_{git_short_sha()}"
    )
    run_dir.mkdir(parents=True, exist_ok=True)

    frame.to_csv(run_dir / "memory_transition_grid.csv", index=False)
    write_skill_summary(frame, run_dir / "memory_skill_summary.csv")

    paired, adaptation_path, adaptation_summary = (
        build_memory_adaptation_outputs(frame)
    )
    paired.to_csv(run_dir / "memory_paired_controls.csv", index=False)
    adaptation_path.to_csv(
        run_dir / "memory_adaptation_path.csv",
        index=False,
    )
    adaptation_summary.to_csv(
        run_dir / "memory_adaptation_summary.csv",
        index=False,
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_short_sha(),
        "experiment": "selector_memory_sensitivity",
        "preset": args.preset,
        "n_seeds": n_seeds,
        "n_obs": args.n_obs,
        "regime_point": args.regime_point,
        "slope_noise_std": args.slope_noise_std,
        "observation_noise_std": args.observation_noise_std,
        "outer_initial_train": args.outer_initial_train,
        "outer_step": args.outer_step,
        "inner_step": args.inner_step,
        "selector_max_inner_origins_grid": list(memory_grid),
        "selector_validation_span_observations": {
            str(memory): (int(memory) - 1) * int(args.inner_step)
            for memory in memory_grid
        },
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
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(f"Wrote results to {run_dir} in {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
