from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate CP05 external-panel figures."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    return parser.parse_args()


def _resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_05/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError("No completed Checkpoint 05 run was found.")
    return Path(latest.read_text(encoding="utf-8").strip())


def _save(fig, base: Path) -> None:
    base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(base.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(base.with_suffix(".png"), dpi=240, bbox_inches="tight")
    plt.close(fig)


def _series_ratio_figure(series: pd.DataFrame, out: Path) -> None:
    frame = series.sort_values(
        ["asset_class", "geometric_rmse_ratio_vs_pooled", "series"]
    ).reset_index(drop=True)
    x = np.arange(len(frame))
    fig, ax = plt.subplots(figsize=(11.0, 5.2))
    for asset_class, group in frame.groupby("asset_class", sort=True):
        ax.scatter(
            group.index.to_numpy(),
            group["geometric_rmse_ratio_vs_pooled"],
            label=asset_class,
            s=24,
        )
    ax.axhline(1.0, linestyle="--", linewidth=1.0)
    ax.set_xlabel("External-panel series (grouped by asset class)")
    ax.set_ylabel("Geometric RMSE ratio: recency-hl3 / pooled CV")
    ax.set_title("CP05 external validation by series")
    ax.set_xticks([])
    ax.grid(axis="y", alpha=0.2)
    ax.legend(frameon=False)
    fig.tight_layout()
    _save(fig, out / "fig_cp05_series_vs_pooled")


def _asset_class_figure(summary: pd.DataFrame, out: Path) -> None:
    frame = summary.loc[~summary["group"].eq("all")].copy()
    frame = frame.sort_values("group").reset_index(drop=True)
    y = np.arange(len(frame))
    point = frame["geometric_rmse_ratio_vs_pooled"].to_numpy(dtype=float)
    lo = frame["cluster_ci95_lo_vs_pooled"].to_numpy(dtype=float)
    hi = frame["cluster_ci95_hi_vs_pooled"].to_numpy(dtype=float)
    xerr = np.vstack([point - lo, hi - point])
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    ax.errorbar(point, y, xerr=xerr, fmt="o", capsize=3)
    ax.axvline(1.0, linestyle="--", linewidth=1.0)
    ax.set_yticks(y)
    ax.set_yticklabels(frame["group"])
    ax.set_xlabel("Geometric RMSE ratio: recency-hl3 / pooled CV")
    ax.set_title("CP05 by asset class")
    ax.grid(axis="x", alpha=0.2)
    fig.tight_layout()
    _save(fig, out / "fig_cp05_asset_class_ratios")


def main() -> None:
    args = parse_args()
    run_dir = _resolve_run_dir(args.run_dir)
    diagnostics = run_dir / "diagnostics"
    series = pd.read_csv(diagnostics / "series_summary.csv")
    summary = pd.read_csv(diagnostics / "primary_summary.csv")
    out = run_dir / "paper_artifacts" / "figures"
    _series_ratio_figure(series, out)
    _asset_class_figure(summary, out)
    print(f"Wrote CP05 figures to {out}")


if __name__ == "__main__":
    main()
