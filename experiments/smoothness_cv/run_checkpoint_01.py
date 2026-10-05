from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import time

import numpy as np
import pandas as pd

from common import (
    PRESETS,
    add_relative_losses,
    classical_selections,
    common_outer_origins,
    fit_and_forecast,
    forecast_cv_curve,
    git_short_sha,
    grid_argmin,
    make_simulated_series,
    recovery_curve,
    smoothness_grid,
    write_checkpoint_summary,
)


SELECTORS = (
    "forecast_cv_h",
    "forecast_cv_1",
    "cv",
    "gcv",
    "aicc",
    "bic",
    "recovery_oracle_train",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Checkpoint 01 for the smoothness-CV paper: compare forecast-CV, "
            "one-step tuning, classical PLS selectors, and the latent recovery oracle."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=(
            "Optional exact output directory. By default a versioned directory is "
            "created under results/smoothness_cv/checkpoint_01/."
        ),
    )
    return parser.parse_args()


def default_run_dir(preset_name: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return (
        Path("results")
        / "smoothness_cv"
        / "checkpoint_01"
        / f"{stamp}_{preset_name}_{git_short_sha()}"
    )


def scenario_id(trend_kind: str, noise_model: str, noise_std: float) -> str:
    return f"{trend_kind}__{noise_model}__sd{noise_std:g}"


def evaluate_block(
    *,
    y: np.ndarray,
    true_trend: np.ndarray,
    origin: int,
    horizon: int,
    preset,
    s_grid: np.ndarray,
    one_step_curve: np.ndarray,
    recovery_values: np.ndarray,
    classical: dict[str, tuple[float, float]],
) -> tuple[list[dict], np.ndarray]:
    history = y[:origin]
    y_window = history[-preset.window :]
    true_window = true_trend[origin - preset.window : origin]
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
    s_one, score_one, _ = grid_argmin(s_grid, one_step_curve)
    s_recovery, score_recovery, _ = grid_argmin(s_grid, recovery_values)

    selected: dict[str, tuple[float, float]] = {
        "forecast_cv_h": (s_matched, score_matched),
        "forecast_cv_1": (s_one, score_one),
        "recovery_oracle_train": (s_recovery, score_recovery),
    }
    selected.update(classical)

    rows: list[dict] = []
    for selector in SELECTORS:
        s_value, selector_score = selected[selector]
        fitted_trend, prediction, lambda_, edf = fit_and_forecast(
            y_window,
            order=preset.order,
            horizon=horizon,
            smoothness=s_value,
        )
        residual = observed_future - prediction
        latent_residual = latent_future - prediction
        training_residual = true_window - fitted_trend

        rows.append(
            {
                "selector": selector,
                "selected_s": float(s_value),
                "selected_lambda": float(lambda_),
                "edf": float(edf),
                "selector_score": float(selector_score),
                "forecast_mse_observed": float(np.mean(residual**2)),
                "forecast_mae_observed": float(np.mean(np.abs(residual))),
                "forecast_mse_latent": float(np.mean(latent_residual**2)),
                "train_recovery_mse": float(np.mean(training_residual**2)),
                "forecast_first": float(prediction[0]),
                "forecast_last": float(prediction[-1]),
            }
        )

    return rows, matched_curve


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    run_dir = args.output_dir or default_run_dir(preset.name)
    run_dir.mkdir(parents=True, exist_ok=True)

    s_grid = smoothness_grid(preset.n_s_grid)
    origins = common_outer_origins(preset)

    result_rows: list[dict] = []
    curve_rows: list[dict] = []
    series_rows: list[dict] = []

    scenarios = list(
        product(
            preset.seeds,
            preset.trend_kinds,
            preset.noise_models,
            preset.noise_stds,
        )
    )

    start_all = time.perf_counter()
    total_blocks = len(scenarios) * len(origins) * len(preset.horizons)
    block_counter = 0

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

        if seed == preset.seeds[0]:
            for t, (observed, latent) in enumerate(zip(y, true_trend)):
                series_rows.append(
                    {
                        "scenario_id": sid,
                        "seed": seed,
                        "trend_kind": trend_kind,
                        "noise_model": noise_model,
                        "noise_std": noise_std,
                        "t": t,
                        "observed": float(observed),
                        "true_trend": float(latent),
                    }
                )

        print(
            f"[scenario {scenario_index}/{len(scenarios)}] "
            f"seed={seed} trend={trend_kind} noise={noise_model} sd={noise_std}",
            flush=True,
        )

        for origin_index, origin in enumerate(origins):
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
            recovery_values = recovery_curve(
                y_window,
                true_window,
                order=preset.order,
                s_grid=s_grid,
            )
            classical = classical_selections(
                y_window,
                order=preset.order,
                s_grid=s_grid,
            )

            for horizon in preset.horizons:
                block_counter += 1
                block_start = time.perf_counter()
                rows, matched_curve = evaluate_block(
                    y=y,
                    true_trend=true_trend,
                    origin=origin,
                    horizon=horizon,
                    preset=preset,
                    s_grid=s_grid,
                    one_step_curve=one_step_curve,
                    recovery_values=recovery_values,
                    classical=classical,
                )

                for row in rows:
                    row.update(
                        {
                            "scenario_id": sid,
                            "seed": seed,
                            "trend_kind": trend_kind,
                            "noise_model": noise_model,
                            "noise_std": noise_std,
                            "order": preset.order,
                            "window": preset.window,
                            "outer_origin": origin,
                            "horizon": horizon,
                        }
                    )
                    result_rows.append(row)

                # Save dense curves only for the first seed and first outer origin.
                # This is enough for diagnostic and manuscript-ready curve figures
                # without making the result bundle unnecessarily large.
                if seed == preset.seeds[0] and origin_index == 0:
                    for s, loss_h, loss_1, loss_rec in zip(
                        s_grid,
                        matched_curve,
                        one_step_curve,
                        recovery_values,
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
                            }
                        )

                elapsed = time.perf_counter() - block_start
                print(
                    f"    [{block_counter}/{total_blocks}] origin={origin} "
                    f"h={horizon} completed in {elapsed:.2f}s",
                    flush=True,
                )

    results = pd.DataFrame(result_rows)
    results = add_relative_losses(results, baseline="gcv")
    curves = pd.DataFrame(curve_rows)
    examples = pd.DataFrame(series_rows)

    results.to_csv(run_dir / "results.csv", index=False)
    curves.to_csv(run_dir / "objective_curves.csv", index=False)
    examples.to_csv(run_dir / "series_examples.csv", index=False)
    write_checkpoint_summary(results, run_dir / "summary.csv")

    paired_keys = [
        "scenario_id",
        "seed",
        "trend_kind",
        "noise_model",
        "noise_std",
        "outer_origin",
        "horizon",
    ]
    matched = results.loc[
        results["selector"] == "forecast_cv_h",
        paired_keys + ["selected_s", "forecast_mse_observed"],
    ].rename(
        columns={
            "selected_s": "selected_s_h",
            "forecast_mse_observed": "mse_h",
        }
    )
    one = results.loc[
        results["selector"] == "forecast_cv_1",
        paired_keys + ["selected_s", "forecast_mse_observed"],
    ].rename(
        columns={
            "selected_s": "selected_s_1",
            "forecast_mse_observed": "mse_1",
        }
    )
    horizon_match = matched.merge(one, on=paired_keys, validate="one_to_one")
    horizon_match["mse_ratio_h_over_1"] = horizon_match["mse_h"] / horizon_match["mse_1"]
    horizon_match["smoothness_difference_h_minus_1"] = (
        horizon_match["selected_s_h"] - horizon_match["selected_s_1"]
    )
    horizon_match.to_csv(run_dir / "horizon_matching.csv", index=False)

    elapsed_all = time.perf_counter() - start_all
    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_short_sha(),
        "checkpoint": "01",
        "preset": preset.name,
        "preset_definition": {
            "seeds": list(preset.seeds),
            "trend_kinds": list(preset.trend_kinds),
            "noise_models": list(preset.noise_models),
            "noise_stds": list(preset.noise_stds),
            "horizons": list(preset.horizons),
            "n_obs": preset.n_obs,
            "order": preset.order,
            "window": preset.window,
            "outer_initial_train": preset.outer_initial_train,
            "outer_step": preset.outer_step,
            "inner_step": preset.inner_step,
            "max_inner_origins": preset.max_inner_origins,
            "n_s_grid": preset.n_s_grid,
        },
        "outer_origins": list(origins),
        "selectors": list(SELECTORS),
        "n_scenarios": len(scenarios),
        "n_outer_horizon_blocks": total_blocks,
        "n_result_rows": len(results),
        "n_curve_rows": len(curves),
        "elapsed_seconds": elapsed_all,
        "files": {
            "results": "results.csv",
            "objective_curves": "objective_curves.csv",
            "series_examples": "series_examples.csv",
            "summary": "summary.csv",
            "horizon_matching": "horizon_matching.csv",
        },
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    latest_file = Path("results") / "smoothness_cv" / "checkpoint_01" / "LATEST.txt"
    latest_file.parent.mkdir(parents=True, exist_ok=True)
    latest_file.write_text(str(run_dir.as_posix()) + "\n", encoding="utf-8")

    print("", flush=True)
    print(f"Checkpoint 01 complete: {run_dir}", flush=True)
    print(f"Result rows: {len(results)}", flush=True)
    print(f"Elapsed: {elapsed_all:.2f}s", flush=True)
    print(
        "Next: python experiments/smoothness_cv/make_checkpoint_01_figures.py "
        f"--run-dir {run_dir}",
        flush=True,
    )


if __name__ == "__main__":
    main()
