from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate manuscript-ready Checkpoint 03 simulation figures."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser.parse_args()


def resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_03/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError(
            "No completed Checkpoint 03 run was found. "
            "run_checkpoint_03.py must finish successfully first."
        )
    return Path(latest.read_text(encoding="utf-8").strip())


def save(fig, base: Path) -> None:
    base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(base.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(base.with_suffix(".png"), dpi=240, bbox_inches="tight")
    plt.close(fig)


def horizon_matching_by_noise(ratios: pd.DataFrame, out: Path) -> None:
    frame = ratios[
        (ratios["comparator"] == "forecast_cv_1")
        & (ratios["noise_scope"] != "all")
        & (ratios["horizon"] > 1)
    ].copy()

    fig, ax = plt.subplots(figsize=(6.1, 3.9))
    for noise, group in frame.groupby("noise_scope"):
        group = group.sort_values("horizon")
        y = group["geometric_rmsfe_ratio"].to_numpy(dtype=float)
        lo = y - group["ci95_low"].to_numpy(dtype=float)
        hi = group["ci95_high"].to_numpy(dtype=float) - y
        ax.errorbar(
            group["horizon"],
            y,
            yerr=np.vstack([lo, hi]),
            marker="o",
            capsize=3,
            label=str(noise),
        )
    ax.axhline(1.0, linestyle="--", linewidth=1.0)
    ax.set_xlabel("Forecast horizon")
    ax.set_ylabel("Geometric RMSFE ratio: matched / one-step")
    ax.grid(alpha=0.2)
    ax.legend(frameon=False)
    fig.tight_layout()
    save(fig, out / "fig_sim01_horizon_matching_by_noise")


def comparison_to_classical(ratios: pd.DataFrame, out: Path) -> None:
    frame = ratios[
        (ratios["noise_scope"] == "all")
        & (ratios["comparator"].isin(["cv", "gcv", "aicc", "forecast_cv_1"]))
    ].copy()

    fig, ax = plt.subplots(figsize=(6.2, 3.9))
    for comparator, group in frame.groupby("comparator"):
        group = group.sort_values("horizon")
        ax.plot(
            group["horizon"],
            group["geometric_rmsfe_ratio"],
            marker="o",
            label=str(comparator),
        )
    ax.axhline(1.0, linestyle="--", linewidth=1.0)
    ax.set_xlabel("Forecast horizon")
    ax.set_ylabel("Geometric RMSFE ratio")
    ax.grid(alpha=0.2)
    ax.legend(frameon=False)
    fig.tight_layout()
    save(fig, out / "fig_sim02_forecast_cv_vs_competitors")


def selected_s_by_horizon(selected: pd.DataFrame, out: Path) -> None:
    frame = selected[
        (selected["selector"] == "forecast_cv_h")
    ].copy()

    fig, ax = plt.subplots(figsize=(6.1, 3.9))
    for noise, group in frame.groupby("noise_model"):
        group = group.sort_values("horizon")
        ax.plot(
            group["horizon"],
            group["mean_s"],
            marker="o",
            label=str(noise),
        )
    ax.set_xlabel("Forecast horizon")
    ax.set_ylabel(r"Mean selected smoothness $S^\star_h$")
    ax.set_ylim(0.0, 1.02)
    ax.grid(alpha=0.2)
    ax.legend(frameon=False)
    fig.tight_layout()
    save(fig, out / "fig_sim03_selected_s_by_horizon")


def oracle_targets(oracle: pd.DataFrame, out: Path) -> None:
    summary = (
        oracle.groupby("horizon", dropna=False)
        .agg(
            s_proposed=("s_proposed", "mean"),
            s_recovery=("s_recovery", "mean"),
            s_forecast_oracle=("s_forecast_oracle", "mean"),
        )
        .reset_index()
        .sort_values("horizon")
    )

    fig, ax = plt.subplots(figsize=(6.1, 3.9))
    ax.plot(
        summary["horizon"],
        summary["s_proposed"],
        marker="o",
        label="Forecast-CV",
    )
    ax.plot(
        summary["horizon"],
        summary["s_recovery"],
        marker="o",
        label="Recovery oracle",
    )
    ax.plot(
        summary["horizon"],
        summary["s_forecast_oracle"],
        marker="o",
        label="Latent forecast oracle",
    )
    ax.set_xlabel("Forecast horizon")
    ax.set_ylabel("Mean smoothness")
    ax.set_ylim(0.0, 1.02)
    ax.grid(alpha=0.2)
    ax.legend(frameon=False)
    fig.tight_layout()
    save(fig, out / "fig_sim04_smoothness_targets")


def objective_curves(curves: pd.DataFrame, out: Path) -> None:
    if curves.empty:
        return
    preferred = curves[
        (curves["trend_kind"] == "oscillatory")
        & (curves["noise_model"] == "ar1")
    ].copy()
    case = preferred if not preferred.empty else curves.copy()
    scenario = case["scenario_id"].iloc[0]
    case = case[case["scenario_id"] == scenario].copy()

    fig, ax = plt.subplots(figsize=(6.2, 3.9))
    for horizon, group in case.groupby("horizon"):
        group = group.sort_values("smoothness")
        values = group["forecast_loss_h"].to_numpy(dtype=float)
        finite = np.isfinite(values)
        if not np.any(finite):
            continue
        minimum = float(np.min(values[finite]))
        scale = minimum if minimum > 1e-15 else 1.0
        ax.plot(
            group["smoothness"],
            values / scale,
            label=f"h={int(horizon)}",
        )
    ax.set_xlabel(r"Normalized smoothness $S$")
    ax.set_ylabel("Forecast loss / minimum")
    ax.set_xlim(0.0, 1.0)
    ax.grid(alpha=0.2)
    ax.legend(frameon=False, ncol=2)
    fig.tight_layout()
    save(fig, out / "fig_sim05_objective_curves")


def write_tables(
    ratios: pd.DataFrame,
    selected: pd.DataFrame,
    oracle_summary: pd.DataFrame,
    out: Path,
) -> list[str]:
    tables = out / "tables"
    tables.mkdir(parents=True, exist_ok=True)

    primary = ratios[ratios["noise_scope"] == "all"].copy()
    primary.to_csv(tables / "table_sim_primary_comparisons.csv", index=False)

    matched_noise = ratios[
        (ratios["comparator"] == "forecast_cv_1")
        & (ratios["noise_scope"] != "all")
    ].copy()
    matched_noise.to_csv(
        tables / "table_sim_horizon_matching_by_noise.csv",
        index=False,
    )

    selected.to_csv(tables / "table_sim_selected_s.csv", index=False)
    oracle_summary.to_csv(tables / "table_sim_oracle_summary.csv", index=False)

    return [
        "tables/table_sim_primary_comparisons.csv",
        "tables/table_sim_horizon_matching_by_noise.csv",
        "tables/table_sim_selected_s.csv",
        "tables/table_sim_oracle_summary.csv",
    ]


def main() -> None:
    args = parse_args()
    run_dir = resolve_run_dir(args.run_dir)
    output = args.output_dir or (run_dir / "paper_artifacts")
    figures = output / "figures"

    ratios = pd.read_csv(run_dir / "diagnostics/paired_rmsfe_summary.csv")
    selected = pd.read_csv(run_dir / "diagnostics/selected_s_summary.csv")
    oracle_summary_frame = pd.read_csv(run_dir / "diagnostics/oracle_summary.csv")
    oracle = pd.read_csv(run_dir / "oracle_comparisons.csv")
    curves = pd.read_csv(run_dir / "objective_curves.csv")

    horizon_matching_by_noise(ratios, figures)
    comparison_to_classical(ratios, figures)
    selected_s_by_horizon(selected, figures)
    oracle_targets(oracle, figures)
    objective_curves(curves, figures)
    tables = write_tables(ratios, selected, oracle_summary_frame, output)

    manifest = {
        "source_run_dir": run_dir.as_posix(),
        "figures": [
            "figures/fig_sim01_horizon_matching_by_noise.pdf",
            "figures/fig_sim02_forecast_cv_vs_competitors.pdf",
            "figures/fig_sim03_selected_s_by_horizon.pdf",
            "figures/fig_sim04_smoothness_targets.pdf",
            "figures/fig_sim05_objective_curves.pdf",
        ],
        "tables": tables,
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "artifact_manifest.json").write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote CP03 paper artifacts to {output}")


if __name__ == "__main__":
    main()
