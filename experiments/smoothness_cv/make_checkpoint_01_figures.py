from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from trend_estimation.core.smoothness import (
    effective_degrees_of_freedom,
    lambda_to_smoothness,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Checkpoint 01 figures and tables for the smoothness-CV paper."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Default: <run-dir>/paper_artifacts",
    )
    return parser.parse_args()


def resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_01/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError(
            "No run directory supplied and results/smoothness_cv/checkpoint_01/"
            "LATEST.txt does not exist."
        )
    return Path(latest.read_text(encoding="utf-8").strip())


def save_figure(fig, base: Path) -> None:
    base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(base.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(base.with_suffix(".png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


def fig01_s_lambda(output: Path, *, n_obs: int, order: int) -> None:
    lambdas = np.logspace(-6, 8, 500)
    smoothness = np.array(
        [lambda_to_smoothness(v, n_obs=n_obs, order=order) for v in lambdas]
    )
    fig, ax = plt.subplots(figsize=(5.7, 3.7))
    ax.plot(np.log10(lambdas), smoothness)
    ax.set_xlabel(r"$\log_{10}(\lambda)$")
    ax.set_ylabel(r"Normalized smoothness $S(\lambda)$")
    ax.set_ylim(-0.02, 1.02)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    save_figure(fig, output / "fig01_s_lambda")


def fig01b_edf_s(output: Path, *, n_obs: int, order: int) -> None:
    s = np.linspace(0.0, 1.0, 300)
    edf = n_obs - (n_obs - order) * s
    fig, ax = plt.subplots(figsize=(5.7, 3.7))
    ax.plot(s, edf)
    ax.set_xlabel(r"Normalized smoothness $S$")
    ax.set_ylabel("Effective degrees of freedom")
    ax.set_xlim(0.0, 1.0)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    save_figure(fig, output / "fig01b_edf_s")


def choose_curve_case(curves: pd.DataFrame) -> pd.DataFrame:
    preferred = curves[
        (curves["trend_kind"] == "smooth_curve")
        & (curves["noise_model"] == "iid")
    ]
    if not preferred.empty:
        min_sd = preferred["noise_std"].min()
        preferred = preferred[preferred["noise_std"] == min_sd]
        first_scenario = preferred["scenario_id"].iloc[0]
        return preferred[preferred["scenario_id"] == first_scenario].copy()

    first_scenario = curves["scenario_id"].iloc[0]
    return curves[curves["scenario_id"] == first_scenario].copy()


def fig02_objective_curves(curves: pd.DataFrame, output: Path) -> None:
    case = choose_curve_case(curves)
    fig, ax = plt.subplots(figsize=(6.1, 3.9))
    for horizon, group in case.groupby("horizon"):
        group = group.sort_values("smoothness")
        values = group["forecast_loss_h"].to_numpy(dtype=float)
        finite = np.isfinite(values)
        scale = np.min(values[finite]) if np.any(finite) else 1.0
        if not np.isfinite(scale) or scale <= 0.0:
            scale = 1.0
        ax.plot(
            group["smoothness"],
            values / scale,
            label=f"h={int(horizon)}",
        )
    ax.set_xlabel(r"Normalized smoothness $S$")
    ax.set_ylabel(r"Forecast loss / minimum loss")
    ax.set_xlim(0.0, 1.0)
    ax.legend(frameon=False, ncol=2)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    save_figure(fig, output / "fig02_objective_curves")


def fig03_selected_s_by_h(results: pd.DataFrame, output: Path) -> None:
    frame = results[results["selector"] == "forecast_cv_h"]
    horizons = sorted(frame["horizon"].unique())
    data = [
        frame.loc[frame["horizon"] == h, "selected_s"].to_numpy(dtype=float)
        for h in horizons
    ]
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    ax.boxplot(data, labels=[str(int(h)) for h in horizons], showfliers=False)
    ax.set_xlabel("Forecast horizon")
    ax.set_ylabel(r"Selected smoothness $S^\star_h$")
    ax.set_ylim(-0.02, 1.02)
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    save_figure(fig, output / "fig03_selected_s_by_horizon")


def fig04_forecast_vs_recovery(results: pd.DataFrame, output: Path) -> None:
    keys = [
        "scenario_id",
        "seed",
        "trend_kind",
        "noise_model",
        "noise_std",
        "outer_origin",
        "horizon",
    ]
    forecast = results.loc[
        results["selector"] == "forecast_cv_h",
        keys + ["selected_s"],
    ].rename(columns={"selected_s": "s_forecast"})
    recovery = results.loc[
        results["selector"] == "recovery_oracle_train",
        keys + ["selected_s"],
    ].rename(columns={"selected_s": "s_recovery"})
    paired = forecast.merge(recovery, on=keys, validate="one_to_one")

    fig, ax = plt.subplots(figsize=(4.8, 4.6))
    ax.scatter(paired["s_recovery"], paired["s_forecast"], alpha=0.45, s=18)
    ax.plot([0.0, 1.0], [0.0, 1.0], linestyle="--", linewidth=1.0)
    ax.set_xlabel(r"Recovery-optimal smoothness $S_{\mathrm{rec}}$")
    ax.set_ylabel(r"Forecast-optimal smoothness $S^\star_h$")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    save_figure(fig, output / "fig04_forecast_vs_recovery")


def fig05_method_comparison(results: pd.DataFrame, output: Path) -> None:
    selectors = ["forecast_cv_h", "forecast_cv_1", "cv", "gcv", "aicc", "bic"]
    frame = results[results["selector"].isin(selectors)].copy()
    summary = (
        frame.groupby("selector")["relative_rmsfe_to_gcv"]
        .median()
        .reindex(selectors)
    )

    labels = ["Forecast-CV h", "Forecast-CV 1", "CV", "GCV", "AICc", "BIC"]
    fig, ax = plt.subplots(figsize=(6.3, 3.8))
    x = np.arange(len(selectors))
    ax.bar(x, summary.to_numpy(dtype=float))
    ax.axhline(1.0, linestyle="--", linewidth=1.0)
    ax.set_xticks(x, labels, rotation=25, ha="right")
    ax.set_ylabel("Median relative RMSFE to GCV")
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    save_figure(fig, output / "fig05_method_comparison")


def fig06_horizon_matching(horizon_matching: pd.DataFrame, output: Path) -> None:
    frame = horizon_matching[horizon_matching["horizon"] > 1]
    if frame.empty:
        return
    horizons = sorted(frame["horizon"].unique())
    data = [
        frame.loc[
            frame["horizon"] == h,
            "mse_ratio_h_over_1",
        ].to_numpy(dtype=float)
        for h in horizons
    ]
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    ax.boxplot(data, labels=[str(int(h)) for h in horizons], showfliers=False)
    ax.axhline(1.0, linestyle="--", linewidth=1.0)
    ax.set_xlabel("Forecast horizon")
    ax.set_ylabel(r"MSE ratio: horizon-matched / one-step tuned")
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    save_figure(fig, output / "fig06_horizon_matching")


def write_tables(
    results: pd.DataFrame,
    horizon_matching: pd.DataFrame,
    output: Path,
) -> list[str]:
    tables_dir = output / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    selectors = ["forecast_cv_h", "forecast_cv_1", "cv", "gcv", "aicc", "bic"]
    comparison = (
        results[results["selector"].isin(selectors)]
        .groupby(["selector", "horizon"], dropna=False)
        .agg(
            n_blocks=("forecast_mse_observed", "size"),
            mean_selected_s=("selected_s", "mean"),
            median_selected_s=("selected_s", "median"),
            mean_edf=("edf", "mean"),
            mean_mse=("forecast_mse_observed", "mean"),
            median_relative_rmsfe_to_gcv=("relative_rmsfe_to_gcv", "median"),
        )
        .reset_index()
    )
    comparison.to_csv(tables_dir / "table_method_comparison.csv", index=False)

    horizon_summary = (
        horizon_matching.groupby("horizon", dropna=False)
        .agg(
            n_blocks=("mse_ratio_h_over_1", "size"),
            mean_s_h=("selected_s_h", "mean"),
            mean_s_1=("selected_s_1", "mean"),
            median_mse_ratio=("mse_ratio_h_over_1", "median"),
            mean_mse_ratio=("mse_ratio_h_over_1", "mean"),
        )
        .reset_index()
    )
    horizon_summary.to_csv(tables_dir / "table_horizon_matching.csv", index=False)

    recovery = (
        results[results["selector"].isin(["forecast_cv_h", "recovery_oracle_train"])]
        .groupby(["selector", "horizon"], dropna=False)
        .agg(
            mean_selected_s=("selected_s", "mean"),
            median_selected_s=("selected_s", "median"),
            mean_train_recovery_mse=("train_recovery_mse", "mean"),
            mean_forecast_mse=("forecast_mse_observed", "mean"),
        )
        .reset_index()
    )
    recovery.to_csv(tables_dir / "table_forecast_vs_recovery.csv", index=False)

    return [
        "tables/table_method_comparison.csv",
        "tables/table_horizon_matching.csv",
        "tables/table_forecast_vs_recovery.csv",
    ]


def main() -> None:
    args = parse_args()
    run_dir = resolve_run_dir(args.run_dir)
    output = args.output_dir or (run_dir / "paper_artifacts")
    output.mkdir(parents=True, exist_ok=True)

    results = pd.read_csv(run_dir / "results.csv")
    curves = pd.read_csv(run_dir / "objective_curves.csv")
    horizon_matching = pd.read_csv(run_dir / "horizon_matching.csv")

    metadata = json.loads((run_dir / "run_metadata.json").read_text(encoding="utf-8"))
    preset = metadata["preset_definition"]
    n_obs = int(preset["window"])
    order = int(preset["order"])

    figures_dir = output / "figures"
    fig01_s_lambda(figures_dir, n_obs=n_obs, order=order)
    fig01b_edf_s(figures_dir, n_obs=n_obs, order=order)
    fig02_objective_curves(curves, figures_dir)
    fig03_selected_s_by_h(results, figures_dir)
    fig04_forecast_vs_recovery(results, figures_dir)
    fig05_method_comparison(results, figures_dir)
    fig06_horizon_matching(horizon_matching, figures_dir)

    table_paths = write_tables(results, horizon_matching, output)

    manifest = {
        "source_run_dir": str(run_dir.as_posix()),
        "figures": [
            "figures/fig01_s_lambda.pdf",
            "figures/fig01b_edf_s.pdf",
            "figures/fig02_objective_curves.pdf",
            "figures/fig03_selected_s_by_horizon.pdf",
            "figures/fig04_forecast_vs_recovery.pdf",
            "figures/fig05_method_comparison.pdf",
            "figures/fig06_horizon_matching.pdf",
        ],
        "tables": table_paths,
    }
    (output / "artifact_manifest.json").write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )

    print(f"Wrote paper artifacts to {output}")
    for item in manifest["figures"]:
        print(f"  {item}")
    for item in manifest["tables"]:
        print(f"  {item}")


if __name__ == "__main__":
    main()
