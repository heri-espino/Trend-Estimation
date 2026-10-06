from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate CP04 development figures."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    return parser.parse_args()


def _resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_04/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError("No completed Checkpoint 04 run was found.")
    return Path(latest.read_text(encoding="utf-8").strip())


def _save(fig, base: Path) -> None:
    base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(base.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(base.with_suffix(".png"), dpi=240, bbox_inches="tight")
    plt.close(fig)


def _rule_ratio_figure(summary: pd.DataFrame, out: Path) -> None:
    frame = summary.sort_values("development_rank").copy()
    y = np.arange(len(frame))
    fig, ax = plt.subplots(figsize=(7.2, max(3.8, 0.45 * len(frame) + 1.5)))
    ax.scatter(
        frame["geometric_rmsfe_vs_last"],
        y - 0.10,
        label="vs last",
    )
    ax.scatter(
        frame["geometric_rmsfe_vs_pooled"],
        y + 0.10,
        label="vs pooled CV",
    )
    ax.axvline(1.0, linestyle="--", linewidth=1.0)
    ax.set_yticks(y)
    ax.set_yticklabels(frame["rule"])
    ax.invert_yaxis()
    ax.set_xlabel("Geometric RMSFE ratio")
    ax.set_title("CP04 development: dynamic branch rules")
    ax.grid(axis="x", alpha=0.2)
    ax.legend(frameon=False)
    fig.tight_layout()
    _save(fig, out / "fig_cp04_rule_ratios")


def _smoothness_difference_figure(decisions: pd.DataFrame, out: Path) -> None:
    frame = decisions.loc[
        ~decisions["rule"].isin(["last", "pooled_cv_same_config"])
    ].copy()
    order = list(
        frame.groupby("rule")["s_minus_current"]
        .apply(lambda x: float(np.median(np.abs(x))))
        .sort_values()
        .index
    )
    values = [
        frame.loc[frame["rule"].eq(rule), "s_minus_current"].to_numpy(dtype=float)
        for rule in order
    ]
    fig, ax = plt.subplots(figsize=(7.4, max(3.8, 0.45 * len(order) + 1.5)))
    ax.boxplot(values, vert=False, showfliers=False)
    ax.set_yticks(np.arange(1, len(order) + 1))
    ax.set_yticklabels(order)
    ax.axvline(0.0, linestyle="--", linewidth=1.0)
    ax.set_xlabel(r"Selected $S$ minus newest branch minimum")
    ax.set_title("How branch rules modify the current smoothness")
    ax.grid(axis="x", alpha=0.2)
    fig.tight_layout()
    _save(fig, out / "fig_cp04_smoothness_adjustments")


def main() -> None:
    args = parse_args()
    run_dir = _resolve_run_dir(args.run_dir)
    out = run_dir / "paper_artifacts" / "figures"
    summary = pd.read_csv(run_dir / "diagnostics/rule_summary.csv")
    decisions = pd.read_csv(run_dir / "decision_results.csv")
    _rule_ratio_figure(summary, out)
    _smoothness_difference_figure(decisions, out)
    print(f"Wrote CP04 development figures to {out}")


if __name__ == "__main__":
    main()
