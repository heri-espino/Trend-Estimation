from __future__ import annotations

import argparse
import gzip
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import time

import numpy as np
import pandas as pd

from common import (
    classical_selections,
    fit_and_forecast,
    forecast_cv_curve,
    git_short_sha,
    grid_argmin,
    latent_forecast_oracle_curve,
    make_simulated_series,
    recovery_curve,
    smoothness_grid,
)


@dataclass(frozen=True)
class CP03Preset:
    name: str
    seeds: tuple[int, ...]
    trend_kinds: tuple[str, ...]
    noise_models: tuple[str, ...]
    noise_stds: tuple[float, ...]
    horizons: tuple[int, ...]
    n_obs: int
    order: int
    window: int
    outer_origins: tuple[int, ...]
    inner_step: int
    max_inner_origins: int
    n_s_grid: int


CORE_TRENDS = (
    "linear",
    "smooth_curve",
    "oscillatory",
    "recent_slope_change",
    "terminal_bend",
)

PRESETS = {
    "smoke": CP03Preset(
        name="smoke",
        seeds=(0,),
        trend_kinds=("linear", "oscillatory", "recent_slope_change"),
        noise_models=("iid", "ar1"),
        noise_stds=(0.5,),
        horizons=(1, 6, 12),
        n_obs=240,
        order=2,
        window=60,
        outer_origins=(156, 204),
        inner_step=4,
        max_inner_origins=24,
        n_s_grid=121,
    ),
    "paper": CP03Preset(
        name="paper",
        seeds=tuple(range(100)),
        trend_kinds=CORE_TRENDS,
        noise_models=("iid", "ar1", "student_t"),
        noise_stds=(0.3, 0.7),
        horizons=(1, 3, 6, 12),
        n_obs=360,
        order=2,
        window=60,
        outer_origins=(228, 252, 276, 300, 324, 348),
        inner_step=2,
        max_inner_origins=48,
        n_s_grid=601,
    ),
}


FEASIBLE_SELECTORS = (
    "forecast_cv_h",
    "forecast_cv_1",
    "cv",
    "gcv",
    "aicc",
)

ORACLE_SELECTORS = (
    "recovery_oracle_train",
    "latent_forecast_oracle",
)

ALL_SELECTORS = FEASIBLE_SELECTORS + ORACLE_SELECTORS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Checkpoint 03: frozen paper-scale simulation for forecast-optimal "
            "smoothness. The design was fixed after CP02 and must not be changed "
            "after inspecting paper-preset results."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser.parse_args()


def default_run_dir(preset_name: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return (
        Path("results")
        / "smoothness_cv"
        / "checkpoint_03"
        / f"{stamp}_{preset_name}_{git_short_sha()}"
    )


def scenario_id(trend_kind: str, noise_model: str, noise_std: float) -> str:
    return f"{trend_kind}__{noise_model}__sd{noise_std:g}"


def evaluate_selector(
    *,
    selector: str,
    selected_s: float,
    selector_score: float,
    y_window: np.ndarray,
    true_window: np.ndarray,
    observed_future: np.ndarray,
    latent_future: np.ndarray,
    order: int,
    horizon: int,
    latent_oracle_mse: float,
) -> dict:
    fitted_trend, prediction, lambda_, edf = fit_and_forecast(
        y_window,
        order=order,
        horizon=horizon,
        smoothness=selected_s,
    )
    observed_error = observed_future - prediction
    latent_error = latent_future - prediction
    recovery_error = true_window - fitted_trend

    return {
        "selector": selector,
        "selected_s": float(selected_s),
        "selected_lambda": float(lambda_),
        "edf": float(edf),
        "selector_score": float(selector_score),
        "forecast_mse_observed": float(np.mean(observed_error**2)),
        "forecast_mae_observed": float(np.mean(np.abs(observed_error))),
        "forecast_mse_latent": float(np.mean(latent_error**2)),
        "train_recovery_mse": float(np.mean(recovery_error**2)),
        "latent_oracle_mse": float(latent_oracle_mse),
        "latent_excess_mse": float(
            max(np.mean(latent_error**2) - latent_oracle_mse, 0.0)
        ),
    }


def series_aggregate(block_results: pd.DataFrame) -> pd.DataFrame:
    group = [
        "seed",
        "scenario_id",
        "trend_kind",
        "noise_model",
        "noise_std",
        "order",
        "window",
        "horizon",
        "selector",
    ]
    return (
        block_results.groupby(group, dropna=False)
        .agg(
            n_outer_origins=("outer_origin", "nunique"),
            mean_selected_s=("selected_s", "mean"),
            median_selected_s=("selected_s", "median"),
            endpoint_one_rate=("selected_s", lambda x: np.mean(np.isclose(x, 1.0))),
            mean_edf=("edf", "mean"),
            msfe=("forecast_mse_observed", "mean"),
            mae=("forecast_mae_observed", "mean"),
            latent_mse=("forecast_mse_latent", "mean"),
            recovery_mse=("train_recovery_mse", "mean"),
            latent_oracle_mse=("latent_oracle_mse", "mean"),
            latent_excess_mse=("latent_excess_mse", "mean"),
        )
        .reset_index()
    )


def paired_series_comparisons(series_results: pd.DataFrame) -> pd.DataFrame:
    keys = [
        "seed",
        "scenario_id",
        "trend_kind",
        "noise_model",
        "noise_std",
        "order",
        "window",
        "horizon",
    ]
    proposed = series_results.loc[
        series_results["selector"] == "forecast_cv_h",
        keys + ["msfe", "mae", "latent_mse", "mean_selected_s"],
    ].rename(
        columns={
            "msfe": "msfe_proposed",
            "mae": "mae_proposed",
            "latent_mse": "latent_mse_proposed",
            "mean_selected_s": "s_proposed",
        }
    )

    rows: list[pd.DataFrame] = []
    for comparator in ("forecast_cv_1", "cv", "gcv", "aicc"):
        other = series_results.loc[
            series_results["selector"] == comparator,
            keys + ["msfe", "mae", "latent_mse", "mean_selected_s"],
        ].rename(
            columns={
                "msfe": "msfe_comparator",
                "mae": "mae_comparator",
                "latent_mse": "latent_mse_comparator",
                "mean_selected_s": "s_comparator",
            }
        )
        paired = proposed.merge(other, on=keys, validate="one_to_one")
        paired["comparator"] = comparator
        paired["mse_ratio"] = paired["msfe_proposed"] / paired["msfe_comparator"]
        paired["rmsfe_ratio"] = np.sqrt(paired["mse_ratio"])
        paired["log_mse_ratio"] = np.log(
            np.maximum(paired["msfe_proposed"], 1e-15)
            / np.maximum(paired["msfe_comparator"], 1e-15)
        )
        paired["mae_ratio"] = paired["mae_proposed"] / paired["mae_comparator"]
        paired["s_difference"] = paired["s_proposed"] - paired["s_comparator"]
        rows.append(paired)

    return pd.concat(rows, ignore_index=True)


def oracle_series_comparisons(series_results: pd.DataFrame) -> pd.DataFrame:
    keys = [
        "seed",
        "scenario_id",
        "trend_kind",
        "noise_model",
        "noise_std",
        "order",
        "window",
        "horizon",
    ]

    def take(selector: str, prefix: str) -> pd.DataFrame:
        return series_results.loc[
            series_results["selector"] == selector,
            keys + [
                "mean_selected_s",
                "latent_mse",
                "recovery_mse",
                "latent_oracle_mse",
                "latent_excess_mse",
            ],
        ].rename(
            columns={
                "mean_selected_s": f"s_{prefix}",
                "latent_mse": f"latent_mse_{prefix}",
                "recovery_mse": f"recovery_mse_{prefix}",
                "latent_oracle_mse": f"latent_oracle_mse_{prefix}",
                "latent_excess_mse": f"latent_excess_mse_{prefix}",
            }
        )

    out = take("forecast_cv_h", "proposed")
    out = out.merge(
        take("recovery_oracle_train", "recovery"),
        on=keys,
        validate="one_to_one",
    )
    out = out.merge(
        take("latent_forecast_oracle", "forecast_oracle"),
        on=keys,
        validate="one_to_one",
    )

    out["s_gap_proposed_oracle"] = (
        out["s_proposed"] - out["s_forecast_oracle"]
    )
    out["s_gap_recovery_oracle"] = (
        out["s_recovery"] - out["s_forecast_oracle"]
    )
    out["latent_excess_scaled_by_noise_var"] = (
        out["latent_mse_proposed"] - out["latent_mse_forecast_oracle"]
    ) / np.maximum(out["noise_std"] ** 2, 1e-12)
    return out


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    run_dir = args.output_dir or default_run_dir(preset.name)
    run_dir.mkdir(parents=True, exist_ok=True)

    s_grid = smoothness_grid(preset.n_s_grid)
    scenarios = list(
        product(
            preset.seeds,
            preset.trend_kinds,
            preset.noise_models,
            preset.noise_stds,
        )
    )
    total_blocks = len(scenarios) * len(preset.outer_origins) * len(preset.horizons)

    rows: list[dict] = []
    curve_rows: list[dict] = []
    block_counter = 0
    started = time.perf_counter()

    for scenario_index, (seed, trend_kind, noise_model, noise_std) in enumerate(
        scenarios,
        start=1,
    ):
        sid = scenario_id(trend_kind, noise_model, float(noise_std))
        y, true_trend = make_simulated_series(
            n_obs=preset.n_obs,
            trend_kind=trend_kind,
            noise_model=noise_model,
            noise_std=float(noise_std),
            seed=int(seed),
        )

        print(
            f"[scenario {scenario_index}/{len(scenarios)}] seed={seed} "
            f"trend={trend_kind} noise={noise_model} sd={noise_std}",
            flush=True,
        )

        for origin_index, origin in enumerate(preset.outer_origins):
            history = y[:origin]
            y_window = history[-preset.window :]
            true_window = true_trend[origin - preset.window : origin]

            one_step_curve = forecast_cv_curve(
                history,
                order=preset.order,
                window=preset.window,
                horizon=1,
                step=preset.inner_step,
                max_inner_origins=preset.max_inner_origins,
                s_grid=s_grid,
            )
            s_one, score_one, _ = grid_argmin(s_grid, one_step_curve)

            recovery_values = recovery_curve(
                y_window,
                true_window,
                order=preset.order,
                s_grid=s_grid,
            )
            s_recovery, score_recovery, _ = grid_argmin(s_grid, recovery_values)

            classical = classical_selections(
                y_window,
                order=preset.order,
                s_grid=s_grid,
            )

            for horizon in preset.horizons:
                block_counter += 1
                block_started = time.perf_counter()
                observed_future = y[origin : origin + horizon]
                latent_future = true_trend[origin : origin + horizon]

                matched_curve = forecast_cv_curve(
                    history,
                    order=preset.order,
                    window=preset.window,
                    horizon=horizon,
                    step=preset.inner_step,
                    max_inner_origins=preset.max_inner_origins,
                    s_grid=s_grid,
                )
                s_matched, score_matched, _ = grid_argmin(s_grid, matched_curve)

                oracle_curve = latent_forecast_oracle_curve(
                    y_window,
                    latent_future,
                    order=preset.order,
                    s_grid=s_grid,
                )
                s_oracle, oracle_mse, _ = grid_argmin(s_grid, oracle_curve)

                selected = {
                    "forecast_cv_h": (s_matched, score_matched),
                    "forecast_cv_1": (s_one, score_one),
                    "cv": classical["cv"],
                    "gcv": classical["gcv"],
                    "aicc": classical["aicc"],
                    "recovery_oracle_train": (s_recovery, score_recovery),
                    "latent_forecast_oracle": (s_oracle, oracle_mse),
                }

                for selector in ALL_SELECTORS:
                    selected_s, selector_score = selected[selector]
                    row = evaluate_selector(
                        selector=selector,
                        selected_s=selected_s,
                        selector_score=selector_score,
                        y_window=y_window,
                        true_window=true_window,
                        observed_future=observed_future,
                        latent_future=latent_future,
                        order=preset.order,
                        horizon=horizon,
                        latent_oracle_mse=oracle_mse,
                    )
                    row.update(
                        {
                            "seed": seed,
                            "scenario_id": sid,
                            "trend_kind": trend_kind,
                            "noise_model": noise_model,
                            "noise_std": noise_std,
                            "order": preset.order,
                            "window": preset.window,
                            "outer_origin": origin,
                            "horizon": horizon,
                        }
                    )
                    rows.append(row)

                # Save representative objective curves only. This is enough for
                # manuscript figures and keeps the paper run versionable.
                if (
                    seed == preset.seeds[0]
                    and origin_index == 0
                    and trend_kind in ("linear", "oscillatory", "recent_slope_change")
                    and noise_std == preset.noise_stds[0]
                ):
                    for s, loss_h, loss_1, loss_rec, loss_oracle in zip(
                        s_grid,
                        matched_curve,
                        one_step_curve,
                        recovery_values,
                        oracle_curve,
                    ):
                        curve_rows.append(
                            {
                                "scenario_id": sid,
                                "seed": seed,
                                "trend_kind": trend_kind,
                                "noise_model": noise_model,
                                "noise_std": noise_std,
                                "outer_origin": origin,
                                "horizon": horizon,
                                "smoothness": float(s),
                                "forecast_loss_h": float(loss_h),
                                "forecast_loss_1": float(loss_1),
                                "recovery_mse": float(loss_rec),
                                "latent_forecast_oracle_mse": float(loss_oracle),
                            }
                        )

                if block_counter % 100 == 0 or block_counter == total_blocks:
                    elapsed = time.perf_counter() - started
                    rate = elapsed / block_counter
                    remaining = rate * (total_blocks - block_counter)
                    print(
                        f"    [{block_counter}/{total_blocks}] h={horizon} "
                        f"elapsed={elapsed/60:.1f}m eta={remaining/60:.1f}m",
                        flush=True,
                    )

    block_results = pd.DataFrame(rows)
    series_results = series_aggregate(block_results)
    paired = paired_series_comparisons(series_results)
    oracle = oracle_series_comparisons(series_results)
    curves = pd.DataFrame(curve_rows)

    block_path = run_dir / "block_results.csv.gz"
    block_results.to_csv(block_path, index=False, compression="gzip")
    series_results.to_csv(run_dir / "series_results.csv", index=False)
    paired.to_csv(run_dir / "paired_method_comparisons.csv", index=False)
    oracle.to_csv(run_dir / "oracle_comparisons.csv", index=False)
    curves.to_csv(run_dir / "objective_curves.csv", index=False)

    elapsed = time.perf_counter() - started
    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_short_sha(),
        "checkpoint": "03",
        "preset": preset.name,
        "design_frozen_before_paper_run": True,
        "preset_definition": asdict(preset),
        "feasible_selectors": list(FEASIBLE_SELECTORS),
        "oracle_selectors": list(ORACLE_SELECTORS),
        "bic_status": (
            "omitted from CP03 primary comparisons because CP02 showed the "
            "published global BIC score was pinned to the left finite boundary "
            "on every audited curve."
        ),
        "common_random_numbers": (
            "Within a seed/noise-model/noise-scale combination, the same random "
            "innovation stream is reused across trend mechanisms. Inference must "
            "therefore resample by seed, not by scenario row."
        ),
        "n_scenarios": len(scenarios),
        "n_outer_horizon_blocks": total_blocks,
        "n_block_rows": len(block_results),
        "n_series_rows": len(series_results),
        "elapsed_seconds": elapsed,
        "files": {
            "block_results": "block_results.csv.gz",
            "series_results": "series_results.csv",
            "paired_method_comparisons": "paired_method_comparisons.csv",
            "oracle_comparisons": "oracle_comparisons.csv",
            "objective_curves": "objective_curves.csv",
        },
    }
    (run_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    latest = Path("results/smoothness_cv/checkpoint_03/LATEST.txt")
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text(run_dir.as_posix() + "\n", encoding="utf-8")

    print("")
    print(f"Checkpoint 03 complete: {run_dir}")
    print(f"Block rows: {len(block_results)}")
    print(f"Series rows: {len(series_results)}")
    print(f"Elapsed: {elapsed/60:.1f} minutes")
    print(
        "Next: python experiments/smoothness_cv/analyze_checkpoint_03.py "
        f"--run-dir {run_dir}"
    )


if __name__ == "__main__":
    main()
