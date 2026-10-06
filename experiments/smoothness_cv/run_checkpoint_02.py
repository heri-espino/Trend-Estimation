from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import time

import numpy as np
import pandas as pd

from common import (
    add_relative_losses,
    classical_score_curve,
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
class CP02Preset:
    name: str
    seeds: tuple[int, ...]
    trend_kinds: tuple[str, ...]
    noise_models: tuple[str, ...]
    noise_stds: tuple[float, ...]
    horizons: tuple[int, ...]
    windows: tuple[int, ...]
    n_obs: int
    order: int
    outer_origins: tuple[int, ...]
    inner_step: int
    max_inner_origins: int
    n_s_grid: int


PRESETS = {
    "smoke": CP02Preset(
        name="smoke",
        seeds=(0,),
        trend_kinds=("quadratic", "recent_slope_change", "terminal_bend"),
        noise_models=("iid",),
        noise_stds=(0.5,),
        horizons=(1, 6, 12),
        windows=(36, 60),
        n_obs=300,
        order=2,
        outer_origins=(180, 228, 276),
        inner_step=4,
        max_inner_origins=20,
        n_s_grid=101,
    ),
    "refine": CP02Preset(
        name="refine",
        seeds=(0, 1, 2, 3, 4),
        trend_kinds=(
            "linear",
            "smooth_curve",
            "quadratic",
            "turning_point",
            "recent_slope_change",
            "oscillatory",
            "terminal_bend",
        ),
        noise_models=("iid", "ar1"),
        noise_stds=(0.3, 0.7),
        horizons=(1, 3, 6, 12),
        windows=(36, 60, 96),
        n_obs=300,
        order=2,
        outer_origins=(180, 204, 228, 252, 276),
        inner_step=3,
        max_inner_origins=30,
        n_s_grid=301,
    ),
}


PRIMARY_SELECTORS = (
    "forecast_cv_h",
    "forecast_cv_1",
    "cv",
    "gcv",
    "aicc",
    "recovery_oracle_train",
    "latent_forecast_oracle",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Checkpoint 02: refine the smoothness-CV simulation design after CP01. "
            "Adds harder local-shape mechanisms, multiple window lengths, a latent "
            "future oracle, and an explicit audit of classical score curves."
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
        / "checkpoint_02"
        / f"{stamp}_{preset_name}_{git_short_sha()}"
    )


def scenario_id(trend_kind: str, noise_model: str, noise_std: float) -> str:
    return f"{trend_kind}__{noise_model}__sd{noise_std:g}"


def fit_selector_row(
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
    forecast_mse_observed = float(np.mean((observed_future - prediction) ** 2))
    forecast_mse_latent = float(np.mean((latent_future - prediction) ** 2))
    train_recovery_mse = float(np.mean((true_window - fitted_trend) ** 2))

    if latent_oracle_mse > 1e-14:
        latent_regret_ratio = forecast_mse_latent / latent_oracle_mse
    else:
        latent_regret_ratio = np.nan

    return {
        "selector": selector,
        "selected_s": float(selected_s),
        "selected_lambda": float(lambda_),
        "edf": float(edf),
        "selector_score": float(selector_score),
        "forecast_mse_observed": forecast_mse_observed,
        "forecast_mae_observed": float(np.mean(np.abs(observed_future - prediction))),
        "forecast_mse_latent": forecast_mse_latent,
        "train_recovery_mse": train_recovery_mse,
        "latent_oracle_mse": float(latent_oracle_mse),
        "latent_regret_mse": float(forecast_mse_latent - latent_oracle_mse),
        "latent_regret_ratio": float(latent_regret_ratio),
        "forecast_first": float(prediction[0]),
        "forecast_last": float(prediction[-1]),
    }


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

    result_rows: list[dict] = []
    curve_rows: list[dict] = []
    classical_audit_rows: list[dict] = []
    series_rows: list[dict] = []

    total_blocks = (
        len(scenarios)
        * len(preset.windows)
        * len(preset.outer_origins)
        * len(preset.horizons)
    )
    block_counter = 0
    start_all = time.perf_counter()

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

        for window in preset.windows:
            if min(preset.outer_origins) < window + max(preset.horizons):
                raise ValueError(
                    f"window={window} is too long for the earliest outer origin."
                )

            for origin_index, origin in enumerate(preset.outer_origins):
                history = y[:origin]
                y_window = history[-window:]
                true_window = true_trend[origin - window : origin]

                one_step_curve = forecast_cv_curve(
                    history,
                    order=preset.order,
                    window=window,
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

                # CP01 revealed that an endpoint-inclusive global search of the
                # published BIC score collapses to the smallest positive S on
                # this PLS path. Audit the full score curve rather than treating
                # BIC as a primary comparator until its implementation domain is
                # reconciled with the source paper.
                if seed == preset.seeds[0] and origin_index == 0:
                    for criterion in ("cv", "gcv", "aicc", "bic"):
                        values = classical_score_curve(
                            y_window,
                            order=preset.order,
                            criterion=criterion,
                            s_grid=s_grid,
                        )
                        for s, value in zip(s_grid, values):
                            classical_audit_rows.append(
                                {
                                    "scenario_id": sid,
                                    "seed": seed,
                                    "trend_kind": trend_kind,
                                    "noise_model": noise_model,
                                    "noise_std": noise_std,
                                    "window": window,
                                    "outer_origin": origin,
                                    "criterion": criterion,
                                    "smoothness": float(s),
                                    "score": float(value),
                                }
                            )

                for horizon in preset.horizons:
                    block_counter += 1
                    block_start = time.perf_counter()
                    observed_future = y[origin : origin + horizon]
                    latent_future = true_trend[origin : origin + horizon]

                    matched_curve = forecast_cv_curve(
                        history,
                        order=preset.order,
                        window=window,
                        horizon=horizon,
                        step=preset.inner_step,
                        max_inner_origins=preset.max_inner_origins,
                        s_grid=s_grid,
                    )
                    s_matched, score_matched, _ = grid_argmin(
                        s_grid,
                        matched_curve,
                    )

                    latent_oracle_curve = latent_forecast_oracle_curve(
                        y_window,
                        latent_future,
                        order=preset.order,
                        s_grid=s_grid,
                    )
                    s_latent_oracle, latent_oracle_mse, _ = grid_argmin(
                        s_grid,
                        latent_oracle_curve,
                    )

                    selected = {
                        "forecast_cv_h": (s_matched, score_matched),
                        "forecast_cv_1": (s_one, score_one),
                        "cv": classical["cv"],
                        "gcv": classical["gcv"],
                        "aicc": classical["aicc"],
                        "recovery_oracle_train": (s_recovery, score_recovery),
                        "latent_forecast_oracle": (
                            s_latent_oracle,
                            latent_oracle_mse,
                        ),
                    }

                    for selector in PRIMARY_SELECTORS:
                        selected_s, selector_score = selected[selector]
                        row = fit_selector_row(
                            selector=selector,
                            selected_s=selected_s,
                            selector_score=selector_score,
                            y_window=y_window,
                            true_window=true_window,
                            observed_future=observed_future,
                            latent_future=latent_future,
                            order=preset.order,
                            horizon=horizon,
                            latent_oracle_mse=latent_oracle_mse,
                        )
                        row.update(
                            {
                                "scenario_id": sid,
                                "seed": seed,
                                "trend_kind": trend_kind,
                                "noise_model": noise_model,
                                "noise_std": noise_std,
                                "order": preset.order,
                                "window": window,
                                "outer_origin": origin,
                                "horizon": horizon,
                            }
                        )
                        result_rows.append(row)

                    if seed == preset.seeds[0] and origin_index == 0:
                        for s, loss_h, loss_1, loss_rec, loss_oracle in zip(
                            s_grid,
                            matched_curve,
                            one_step_curve,
                            recovery_values,
                            latent_oracle_curve,
                        ):
                            curve_rows.append(
                                {
                                    "scenario_id": sid,
                                    "seed": seed,
                                    "trend_kind": trend_kind,
                                    "noise_model": noise_model,
                                    "noise_std": noise_std,
                                    "window": window,
                                    "outer_origin": origin,
                                    "horizon": horizon,
                                    "smoothness": float(s),
                                    "forecast_loss_h": float(loss_h),
                                    "forecast_loss_1": float(loss_1),
                                    "recovery_mse": float(loss_rec),
                                    "latent_forecast_oracle_mse": float(loss_oracle),
                                }
                            )

                    elapsed = time.perf_counter() - block_start
                    print(
                        f"    [{block_counter}/{total_blocks}] L={window} "
                        f"origin={origin} h={horizon} in {elapsed:.2f}s",
                        flush=True,
                    )

    results = pd.DataFrame(result_rows)
    results = add_relative_losses(results, baseline="gcv")
    curves = pd.DataFrame(curve_rows)
    classical_audit = pd.DataFrame(classical_audit_rows)
    examples = pd.DataFrame(series_rows)

    results.to_csv(run_dir / "results.csv", index=False)
    curves.to_csv(run_dir / "objective_curves.csv", index=False)
    classical_audit.to_csv(run_dir / "classical_score_audit.csv", index=False)
    examples.to_csv(run_dir / "series_examples.csv", index=False)

    keys = [
        "scenario_id",
        "seed",
        "trend_kind",
        "noise_model",
        "noise_std",
        "window",
        "outer_origin",
        "horizon",
    ]

    def selector_frame(selector: str, prefix: str) -> pd.DataFrame:
        return results.loc[
            results["selector"] == selector,
            keys + [
                "selected_s",
                "forecast_mse_observed",
                "forecast_mse_latent",
                "train_recovery_mse",
            ],
        ].rename(
            columns={
                "selected_s": f"s_{prefix}",
                "forecast_mse_observed": f"mse_obs_{prefix}",
                "forecast_mse_latent": f"mse_latent_{prefix}",
                "train_recovery_mse": f"recovery_mse_{prefix}",
            }
        )

    comparisons = selector_frame("forecast_cv_h", "cvh")
    comparisons = comparisons.merge(
        selector_frame("forecast_cv_1", "cv1"),
        on=keys,
        validate="one_to_one",
    )
    comparisons = comparisons.merge(
        selector_frame("recovery_oracle_train", "recovery"),
        on=keys,
        validate="one_to_one",
    )
    comparisons = comparisons.merge(
        selector_frame("latent_forecast_oracle", "forecast_oracle"),
        on=keys,
        validate="one_to_one",
    )
    comparisons["mse_ratio_cvh_to_cv1"] = (
        comparisons["mse_obs_cvh"] / comparisons["mse_obs_cv1"]
    )
    comparisons["s_gap_cvh_minus_cv1"] = comparisons["s_cvh"] - comparisons["s_cv1"]
    comparisons["s_gap_cvh_minus_recovery"] = (
        comparisons["s_cvh"] - comparisons["s_recovery"]
    )
    comparisons["s_gap_cvh_minus_forecast_oracle"] = (
        comparisons["s_cvh"] - comparisons["s_forecast_oracle"]
    )
    comparisons["s_gap_recovery_minus_forecast_oracle"] = (
        comparisons["s_recovery"] - comparisons["s_forecast_oracle"]
    )
    comparisons.to_csv(run_dir / "paired_comparisons.csv", index=False)

    summary = (
        results.groupby(["selector", "window", "horizon"], dropna=False)
        .agg(
            n=("forecast_mse_observed", "size"),
            mean_selected_s=("selected_s", "mean"),
            median_selected_s=("selected_s", "median"),
            endpoint_one_rate=("selected_s", lambda x: np.mean(np.isclose(x, 1.0))),
            mean_edf=("edf", "mean"),
            mean_forecast_mse=("forecast_mse_observed", "mean"),
            mean_latent_mse=("forecast_mse_latent", "mean"),
            median_relative_rmsfe_to_gcv=("relative_rmsfe_to_gcv", "median"),
            median_latent_regret_ratio=("latent_regret_ratio", "median"),
        )
        .reset_index()
    )
    summary.to_csv(run_dir / "summary.csv", index=False)

    elapsed_all = time.perf_counter() - start_all
    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_short_sha(),
        "checkpoint": "02",
        "preset": preset.name,
        "preset_definition": asdict(preset),
        "primary_selectors": list(PRIMARY_SELECTORS),
        "bic_status": (
            "diagnostic-only: CP01 global endpoint-inclusive grid selected the "
            "smallest positive smoothness throughout; full criterion curves are "
            "saved for reconciliation with the source implementation."
        ),
        "n_scenarios": len(scenarios),
        "n_blocks": total_blocks,
        "n_result_rows": len(results),
        "elapsed_seconds": elapsed_all,
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    latest = Path("results/smoothness_cv/checkpoint_02/LATEST.txt")
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text(run_dir.as_posix() + "\n", encoding="utf-8")

    print("")
    print(f"Checkpoint 02 complete: {run_dir}")
    print(f"Result rows: {len(results)}")
    print(f"Elapsed: {elapsed_all:.2f}s")
    print(
        "Next: python experiments/smoothness_cv/analyze_checkpoint_02.py "
        f"--run-dir {run_dir}"
    )


if __name__ == "__main__":
    main()
