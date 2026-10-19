"""Optional single-seed teaching figures; NOT part of the 1000-seed aggregates.

Produces criterion-score-vs-smoothness curves, retrospective true-tau loss
curves (ex-post only), and multiple lambda reconstructions using the archived
Study M.1 simulator and exact current selector code.

Run from repository root:
  python -m working_papers...  # not an importable name; use script path below
  python "working_papers/Working Paper - Pooled LOOCV Numerical Optimization/presentation/export_v2_criterion_examples.py"

The simulated tau is NEVER used to choose lambda in any feasible policy.
This script is intentionally manual-only; do not add a heavy CI workflow.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from experiments.pooled_loocv_smoothness.cortes_optimality_criteria import PenalizedCriteria
from experiments.pooled_loocv_smoothness.run_process_examples import (
    DEFAULT_SEED, make_examples,
)

DEFAULT_CASES = ("gaussian_reference", "level_jump", "ar1_observation")


def export(out_dir: Path, seed: int, n: int, num_points: int,
           cases: tuple[str, ...], r: int, force: bool) -> dict:
    if num_points < 13 or n < 32 or r not in (1, 3):
        raise ValueError("num_points >= 13, n >= 32, r in {1,3} required")
    examples = make_examples(seed=seed, n=n)
    invalid = set(cases) - set(examples)
    if invalid or not cases:
        raise ValueError(f"invalid or empty cases: {sorted(invalid)}")
    if out_dir.exists() and any(out_dir.glob("v2_criterion_*.png")) and not force:
        raise FileExistsError("existing criterion figures: use --force deliberately")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    out_dir.mkdir(parents=True, exist_ok=True)
    smoothness = np.linspace(0.10, 0.94, num_points)
    created: list[str] = []
    for name in cases:
        case = examples[name]
        obj = PenalizedCriteria(case.y[:r], order=2, mean_mode="joint")
        scores = {criterion: [] for criterion in ("cv", "gcv", "aicc")}
        mse = []
        fitted = {}
        lambdas = []
        for s in smoothness:
            sol = obj.choose_fixed_smoothness(float(s))
            lam = sol.lam
            lambdas.append(lam)
            for criterion in scores:
                scores[criterion].append(float(obj.score(criterion, lam)))
            fit = obj.trend(lam)
            mse.append(float(np.mean((fit - case.truth[:r]) ** 2)))
        # Normalize each different score ONLY to permit visualization.
        # Raw criterion scores are not comparable on a common vertical axis.
        fig, ax = plt.subplots(figsize=(11, 6))
        for method, raw in scores.items():
            values = np.asarray(raw)
            finite = np.isfinite(values)
            if not finite.any():
                continue
            v = values[finite]
            span = max(float(np.max(v) - np.min(v)), 1e-12)
            transformed = np.full(values.shape, np.nan)
            transformed[finite] = (v - np.min(v)) / span
            ax.plot(smoothness, transformed, label=method.upper())
            best = np.argmin(np.where(finite, values, np.inf))
            ax.scatter(smoothness[best], transformed[best], s=40)
        truth_mse = np.asarray(mse)
        truth_norm = (truth_mse - np.min(truth_mse)) / max(
            float(np.max(truth_mse) - np.min(truth_mse)), 1e-12
        )
        ax.plot(smoothness, truth_norm, linestyle="--", linewidth=2.3,
                label="TRUE synthetic tau MSE (ex-post; unavailable on real data)")
        ax.axvline(smoothness[np.argmin(truth_mse)], linestyle=":", alpha=0.55)
        ax.set(xlabel="Nominal smoothness S",
               ylabel="Per-curve min-max normalized score (NOT comparable across types)",
               title=f"{name}: statistical criteria versus synthetic-truth reconstruction")
        ax.grid(alpha=.16)
        ax.legend(fontsize=8)
        fig.tight_layout()
        figure_name = f"v2_criterion_{name}_R{r}.png"
        fig.savefig(out_dir / figure_name, dpi=145)
        plt.close(fig)
        created.append(figure_name)

        # Show actual reconstructions at declared S points, not lambda chosen
        # with access to synthetic tau. Tau appears only in the figure.
        fig, ax = plt.subplots(figsize=(11, 6))
        ax.scatter(np.arange(n), case.y[0], s=10, alpha=.3, label="observed y1")
        ax.plot(case.truth[0], linewidth=2.5, label="true synthetic tau1")
        for s in (.20, .50, .80, .93):
            lam = obj.choose_fixed_smoothness(s).lam
            fitted[s] = obj.trend(lam)
            ax.plot(fitted[s][0], linewidth=1.4, label=f"S={s:.2f}")
        ax.set(xlabel="Observation index", ylabel="Simulated series",
               title=f"{name}: four actual PLS smoothness levels (joint fitted mu)")
        ax.legend(ncol=2, fontsize=9)
        ax.grid(alpha=.16)
        fig.tight_layout()
        fit_name = f"v2_multi_s_{name}_R{r}.png"
        fig.savefig(out_dir / fit_name, dpi=145)
        plt.close(fig)
        created.append(fit_name)

    # A numerical rather than decorative trace-versus-S graph.
    obj = PenalizedCriteria(examples[cases[0]].y[:r], order=2,
                            mean_mode="joint")
    nominal_df = []
    full_df = []
    for s in smoothness:
        sol = obj.choose_fixed_smoothness(float(s))
        nominal_df.append(float(np.trace(obj.raw.smoothness.__self__.raw.hat_matrix(sol.lam)))
                          if False else n - (n - 2) * s)
        full_df.append(float(obj.diagnostics(sol.lam)["edf_total"]))
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(smoothness, np.array(nominal_df) * r,
            label="R × tr(H): fixed-mean EDF")
    ax.plot(smoothness, full_df,
            label="Full pooled EDF with fitted common mu")
    ax.set(xlabel="Nominal S", ylabel="Effective degrees of freedom",
           title=f"Finite-sample pooled EDF: R={r}, N={n}, d=2")
    ax.grid(alpha=.18)
    ax.legend()
    fig.tight_layout()
    df_name = f"v2_edf_vs_s_R{r}.png"
    fig.savefig(out_dir / df_name, dpi=145)
    plt.close(fig)
    created.append(df_name)

    manifest = {
        "status": "ONE_SEED_TEACHING_FIGURES_ONLY",
        "seed": seed, "n": n, "R": r,
        "cases": list(cases), "grid_points": num_points,
        "files_created": created,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "warnings": [
            "Neither these plots nor their synthetic oracle curves belong to the 1000-seed risk estimand.",
            "The true tau MSE is ex-post only and never used to select lambda.",
            "CV, GCV and AICc curves are min-max normalized SEPARATELY; vertical positions across types are incomparable.",
            "These files are optional manual teaching exports. Read Study M.2 CSV for statistical inference."
        ]
    }
    (out_dir / "v2_criterion_examples_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out-dir", type=Path, default=Path(
        "working_papers/Working Paper - Pooled LOOCV Numerical Optimization/presentation/assets"
    ))
    p.add_argument("--seed", type=int, default=DEFAULT_SEED)
    p.add_argument("--n", type=int, default=80)
    p.add_argument("--r", type=int, choices=(1, 3), default=3)
    p.add_argument("--grid-points", type=int, default=55)
    p.add_argument("--cases", default=",".join(DEFAULT_CASES))
    p.add_argument("--force", action="store_true")
    args = p.parse_args()
    output = export(args.out_dir, args.seed, args.n, args.grid_points,
                    tuple(s.strip() for s in args.cases.split(",") if s.strip()),
                    args.r, args.force)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
