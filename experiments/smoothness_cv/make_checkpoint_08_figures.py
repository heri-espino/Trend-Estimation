from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


RESULT_ROOT = Path("results/smoothness_cv/checkpoint_08")
DISPLAY_ORDER = (
    "last", "recency_hl3", "linear_k3", "linear_k5", "linear_k10",
    "ew_linear_hl3", "ew_linear_hl5", "delta_hl3", "delta_hl5",
)
RULE_LABELS = {
    "recency_hl3": "Recency mean (HL 3)",
    "linear_k3": "Linear (K=3)",
    "linear_k5": "Linear (K=5)",
    "linear_k10": "Linear (K=10)",
    "ew_linear_hl3": "Weighted linear (HL 3)",
    "ew_linear_hl5": "Weighted linear (HL 5)",
    "delta_hl3": "Weighted increments (HL 3)",
    "delta_hl5": "Weighted increments (HL 5)",
    "last": "Latest tracked minimum",
    "pooled_cv_same_config": "Pooled forecast-CV",
}


def _run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    return Path((RESULT_ROOT / "LATEST.txt").read_text(encoding="utf-8").strip())


def _save(fig, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(target.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(target.with_suffix(".png"), bbox_inches="tight", dpi=240)
    plt.close(fig)


def _relative_forecast_losses(summary: pd.DataFrame, folder: Path) -> None:
    # Present rules in a conceptual rather than performance-based order.
    frame = summary.set_index("rule").loc[
        [name for name in DISPLAY_ORDER if name in set(summary["rule"])]
    ]
    labels = [RULE_LABELS.get(name, name) for name in frame.index]
    y = np.arange(len(frame), dtype=float)
    fig, ax = plt.subplots(figsize=(9.0, 5.1))
    ax.plot(frame["changing_g_ratio_vs_pooled"], y - 0.13, "o", label="Changing roughness")
    ax.plot(frame["stationary_g_ratio_vs_pooled"], y + 0.13, "s", label="Stationary roughness")
    ax.axvline(1.0, linestyle="--", linewidth=1.0)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("Geometric RMSE ratio relative to pooled forecast-CV")
    ax.set_title("Rule-family behavior under latent roughness regimes")
    ax.grid(axis="x", alpha=0.22)
    ax.legend(frameon=False)
    fig.tight_layout()
    _save(fig, folder / "fig_cp08_rule_family_losses")


def _clipping(summary: pd.DataFrame, folder: Path) -> None:
    frame = summary.set_index("rule").loc[
        [name for name in DISPLAY_ORDER if name in set(summary["rule"])]
    ]
    y = np.arange(len(frame), dtype=float)
    fig, ax = plt.subplots(figsize=(8.4, 4.9))
    ax.barh(y, 100.0 * frame["clipping_rate"])
    ax.set_yticks(y)
    ax.set_yticklabels([RULE_LABELS.get(name, name) for name in frame.index])
    ax.invert_yaxis()
    ax.set_xlabel("Forecast decisions requiring clipping (%)")
    ax.set_title("Boundary behavior of smoothness functionals")
    ax.grid(axis="x", alpha=0.22)
    fig.tight_layout()
    _save(fig, folder / "fig_cp08_rule_clipping")


def _illustrative_decisions(paired: pd.DataFrame, folder: Path) -> None:
    # Deliberately fixed example; not selected on forecasting performance.
    ex = paired.loc[
        paired["seed"].eq(100)
        & paired["mechanism"].eq("switch_to_rough")
        & np.isclose(paired["observation_noise_sd"], 0.01)
    ].copy()
    if ex.empty:
        raise ValueError("Frozen illustrative scenario seed=100/switch_to_rough/noise=0.01 not found.")
    names = ("recency_hl3", "ew_linear_hl5", "linear_k3", "delta_hl3")
    fig, ax = plt.subplots(figsize=(8.5, 4.7))
    for name in names:
        sub = ex.loc[ex["rule"].eq(name)].sort_values("outer_number")
        ax.plot(
            sub["outer_number"], sub["s_rule"], marker="o",
            label=RULE_LABELS.get(name, name)
        )
    baseline = ex.loc[ex["rule"].eq("recency_hl3")].sort_values("outer_number")
    ax.plot(
        baseline["outer_number"], baseline["s_last"],
        linestyle=":", marker="x", label="Latest tracked minimum"
    )
    ax.plot(
        baseline["outer_number"], baseline["s_pooled"],
        linestyle="--", marker="s", label="Pooled forecast-CV"
    )
    ax.set_xlabel("Chronological outer decision")
    ax.set_ylabel("Selected normalized smoothness S")
    ax.set_ylim(0.0, 1.02)
    ax.set_title("Different decisions from the same branch history: fixed example")
    ax.grid(alpha=0.2)
    ax.legend(loc="best", frameon=False, fontsize=8)
    fig.tight_layout()
    _save(fig, folder / "fig_cp08_illustrative_smoothness_selections")


def main() -> None:
    parser = argparse.ArgumentParser(description="CP08 illustrative paper figures (no rule winner).")
    parser.add_argument("--run-dir", type=Path, default=None)
    args = parser.parse_args()
    run_dir = _run_dir(args.run_dir)
    diagnostics = run_dir / "diagnostics"
    summary = pd.read_csv(diagnostics / "rule_summary.csv")
    paired = pd.read_csv(diagnostics / "paired_rule_results.csv.gz")
    output = run_dir / "paper_artifacts" / "figures"
    _relative_forecast_losses(summary, output)
    _clipping(summary, output)
    _illustrative_decisions(paired, output)
    print(f"Wrote three CP08 figures (PDF + PNG) to {output}")


if __name__ == "__main__":
    main()
