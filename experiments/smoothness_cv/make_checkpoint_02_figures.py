from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Checkpoint 02 figures and tables."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser.parse_args()


def resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_02/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError(
            "No completed Checkpoint 02 run was found. "
            "run_checkpoint_02.py must finish successfully first."
        )
    return Path(latest.read_text(encoding="utf-8").strip())


def save(fig, base: Path) -> None:
    base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(base.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(base.with_suffix(".png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


def figure_mechanism_smoothness(paired: pd.DataFrame, out: Path) -> None:
    summary = (
        paired.groupby(["trend_kind", "horizon"])["s_cvh"]
        .mean()
        .reset_index()
    )
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    for trend, group in summary.groupby("trend_kind"):
        group = group.sort_values("horizon")
        ax.plot(group["horizon"], group["s_cvh"], marker="o", label=trend)
    ax.set_xlabel("Forecast horizon")
    ax.set_ylabel(r"Mean selected smoothness $S^\star_h$")
    ax.set_ylim(-0.02, 1.02)
    ax.grid(alpha=0.2)
    ax.legend(frameon=False, fontsize=8, ncol=2)
    fig.tight_layout()
    save(fig, out / "fig_cp02_selected_s_by_mechanism")


def figure_oracle_targets(paired: pd.DataFrame, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(5.0, 4.7))
    ax.scatter(
        paired["s_recovery"],
        paired["s_forecast_oracle"],
        s=14,
        alpha=0.35,
    )
    ax.plot([0.0, 1.0], [0.0, 1.0], linestyle="--", linewidth=1.0)
    ax.set_xlabel(r"Recovery-optimal $S_{\mathrm{rec}}$")
    ax.set_ylabel(r"Latent future forecast-oracle $S_{\mathrm{oracle},h}$")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    save(fig, out / "fig_cp02_recovery_vs_forecast_oracle")


def figure_cvh_vs_oracle(paired: pd.DataFrame, out: Path) -> None:
    fig, ax = plt.subplots(figsize=(5.0, 4.7))
    ax.scatter(
        paired["s_forecast_oracle"],
        paired["s_cvh"],
        s=14,
        alpha=0.35,
    )
    ax.plot([0.0, 1.0], [0.0, 1.0], linestyle="--", linewidth=1.0)
    ax.set_xlabel(r"Latent forecast-oracle $S_{\mathrm{oracle},h}$")
    ax.set_ylabel(r"Forecast-CV selected $S^\star_h$")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    save(fig, out / "fig_cp02_forecast_cv_vs_oracle")


def figure_horizon_matching(paired: pd.DataFrame, out: Path) -> None:
    frame = paired[paired["horizon"] > 1].copy()
    summary = (
        frame.groupby(["window", "horizon"])["mse_ratio_cvh_to_cv1"]
        .median()
        .reset_index()
    )
    fig, ax = plt.subplots(figsize=(6.0, 3.9))
    for window, group in summary.groupby("window"):
        group = group.sort_values("horizon")
        ax.plot(
            group["horizon"],
            group["mse_ratio_cvh_to_cv1"],
            marker="o",
            label=f"L={int(window)}",
        )
    ax.axhline(1.0, linestyle="--", linewidth=1.0)
    ax.set_xlabel("Forecast horizon")
    ax.set_ylabel("Median MSE ratio: matched / one-step")
    ax.grid(alpha=0.2)
    ax.legend(frameon=False)
    fig.tight_layout()
    save(fig, out / "fig_cp02_horizon_matching_by_window")


def figure_method_comparison(results: pd.DataFrame, out: Path) -> None:
    selectors = ["forecast_cv_h", "forecast_cv_1", "cv", "gcv", "aicc"]
    frame = results[results["selector"].isin(selectors)].copy()
    summary = (
        frame.groupby(["selector", "horizon"])["relative_rmsfe_to_gcv"]
        .median()
        .reset_index()
    )
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    for selector, group in summary.groupby("selector"):
        group = group.sort_values("horizon")
        ax.plot(
            group["horizon"],
            group["relative_rmsfe_to_gcv"],
            marker="o",
            label=selector,
        )
    ax.axhline(1.0, linestyle="--", linewidth=1.0)
    ax.set_xlabel("Forecast horizon")
    ax.set_ylabel("Median relative RMSFE to GCV")
    ax.grid(alpha=0.2)
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    save(fig, out / "fig_cp02_method_comparison")


def figure_bic_audit(audit: pd.DataFrame, out: Path) -> None:
    bic = audit[audit["criterion"] == "bic"].copy()
    if bic.empty:
        return
    first = bic[
        (bic["trend_kind"] == bic["trend_kind"].iloc[0])
        & (bic["noise_model"] == bic["noise_model"].iloc[0])
        & (bic["noise_std"] == bic["noise_std"].iloc[0])
        & (bic["window"] == bic["window"].iloc[0])
    ].sort_values("smoothness")
    values = first["score"].to_numpy(dtype=float)
    finite = np.isfinite(values)
    if not np.any(finite):
        return
    floor = np.nanmin(values[finite])
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    ax.plot(
        first.loc[finite, "smoothness"],
        values[finite] - floor,
    )
    ax.set_xlabel(r"Normalized smoothness $S$")
    ax.set_ylabel("BIC score minus minimum")
    ax.set_xlim(0.0, 1.0)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    save(fig, out / "fig_cp02_bic_score_audit")


def write_tables(results: pd.DataFrame, paired: pd.DataFrame, out: Path) -> list[str]:
    tables = out / "tables"
    tables.mkdir(parents=True, exist_ok=True)

    methods = (
        results[
            results["selector"].isin(
                ["forecast_cv_h", "forecast_cv_1", "cv", "gcv", "aicc"]
            )
        ]
        .groupby(["selector", "window", "horizon"], dropna=False)
        .agg(
            n=("forecast_mse_observed", "size"),
            mean_s=("selected_s", "mean"),
            mean_mse=("forecast_mse_observed", "mean"),
            median_relative_rmsfe=("relative_rmsfe_to_gcv", "median"),
        )
        .reset_index()
    )
    methods.to_csv(tables / "table_cp02_method_comparison.csv", index=False)

    oracle = (
        paired.groupby(["trend_kind", "window", "horizon"], dropna=False)
        .agg(
            n=("s_cvh", "size"),
            mean_s_cvh=("s_cvh", "mean"),
            mean_s_recovery=("s_recovery", "mean"),
            mean_s_forecast_oracle=("s_forecast_oracle", "mean"),
            median_mse_ratio_cvh_cv1=("mse_ratio_cvh_to_cv1", "median"),
        )
        .reset_index()
    )
    oracle.to_csv(tables / "table_cp02_oracle_targets.csv", index=False)

    return [
        "tables/table_cp02_method_comparison.csv",
        "tables/table_cp02_oracle_targets.csv",
    ]


def main() -> None:
    args = parse_args()
    run_dir = resolve_run_dir(args.run_dir)
    output = args.output_dir or (run_dir / "paper_artifacts")
    figures = output / "figures"

    results = pd.read_csv(run_dir / "results.csv")
    paired = pd.read_csv(run_dir / "paired_comparisons.csv")
    audit = pd.read_csv(run_dir / "classical_score_audit.csv")

    figure_mechanism_smoothness(paired, figures)
    figure_oracle_targets(paired, figures)
    figure_cvh_vs_oracle(paired, figures)
    figure_horizon_matching(paired, figures)
    figure_method_comparison(results, figures)
    figure_bic_audit(audit, figures)
    tables = write_tables(results, paired, output)

    manifest = {
        "source_run_dir": run_dir.as_posix(),
        "figures": [
            "figures/fig_cp02_selected_s_by_mechanism.pdf",
            "figures/fig_cp02_recovery_vs_forecast_oracle.pdf",
            "figures/fig_cp02_forecast_cv_vs_oracle.pdf",
            "figures/fig_cp02_horizon_matching_by_window.pdf",
            "figures/fig_cp02_method_comparison.pdf",
            "figures/fig_cp02_bic_score_audit.pdf",
        ],
        "tables": tables,
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "artifact_manifest.json").write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote CP02 artifacts to {output}")


if __name__ == "__main__":
    main()
