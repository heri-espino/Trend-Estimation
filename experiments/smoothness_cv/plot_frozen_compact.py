"""Publication-screen plots from compact, ALREADY SAVED summaries ONLY.

No Monte Carlo, no DGP generation, no CUDA and no database writes.
Each page states comparison, proper independent unit and limitations.
The subset in each plot is fixed by the predeclared method families,
not by sorting or choosing a winner from the test scores.

Usage:
    python -m experiments.smoothness_cv.plot_frozen_compact \
      --report-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


CLASSICAL=("classical_cv","classical_gcv","classical_aicc","classical_bic")
TRACKING=(
    ("tracked_uniform_all","pooled_uniform_all"),
    ("tracked_recent_uniform_8","pooled_recent_uniform_8"),
    ("tracked_recent_linear_8","pooled_recent_linear_8"),
    ("tracked_recent_exp_8","pooled_recent_exp_8"),
)


def save(fig,root,stem):
    fig.savefig(root/f"{stem}.pdf",bbox_inches="tight")
    fig.savefig(root/f"{stem}.png",dpi=190,bbox_inches="tight")
    plt.close(fig)


def chart_classical(root):
    df=pd.read_csv(root/"paper1_forecast_cv_vs_classical.csv")
    df=df[
        (df.selector.isin(CLASSICAL))
        & (df.comparator=="pooled_uniform_all")
    ].copy()
    if df.empty:
        return None
    d_values=sorted(df.d.unique())
    horizons=sorted(df.h.unique())
    fig,axes=plt.subplots(1,len(d_values),figsize=(6*len(d_values),4.6),
                          sharey=True,squeeze=False)
    for j,d in enumerate(d_values):
        ax=axes[0,j]
        subset=df[df.d==d]
        for i,method in enumerate(CLASSICAL):
            parts=subset[subset.selector==method]
            ratios=[
                parts.loc[parts.h==h,"relative_rmse"].median()
                if (parts.h==h).any() else np.nan for h in horizons
            ]
            ax.plot(horizons,ratios,marker=["o","s","^","D"][i],
                    label=method.removeprefix("classical_").upper(),linewidth=1.8)
        ax.axhline(1,color="black",linestyle="--",linewidth=.8)
        ax.set_title(f"Order d={d}")
        ax.set_xlabel("Forecast horizon h")
        ax.set_xticks(horizons)
        ax.grid(alpha=.15)
    axes[0,0].set_ylabel("Median cell relative RMSE / pooled uniform")
    axes[0,-1].legend(fontsize=8)
    fig.suptitle(
        "P1 | Classical PLS criteria vs horizon-matched pooled CV\n"
        "Median across predeclared DGP cells, descriptive (not a CI)",
        fontsize=11,
    )
    fig.tight_layout()
    save(fig,root,"paper1_classical_relative_rmse")
    return "paper1_classical_relative_rmse"


def chart_tracking(root):
    df=pd.read_csv(root/"paper2_tracking_vs_matched_pooled.csv")
    d_values=sorted(df.d.unique())
    horizons=sorted(df.h.unique())
    if df.empty:return None
    fig,axes=plt.subplots(1,len(d_values),figsize=(6*len(d_values),4.6),
                         sharey=True,squeeze=False)
    for j,d in enumerate(d_values):
        ax=axes[0,j]
        sub=df[df.d==d]
        for i,(tracked,pooled) in enumerate(TRACKING):
            part=sub[(sub.selector==tracked)&(sub.comparator==pooled)]
            ratios=[
                part.loc[part.h==h,"relative_rmse"].median()
                if (part.h==h).any() else np.nan for h in horizons
            ]
            ax.plot(horizons,ratios,marker=["o","s","^","D"][i],
                    label=tracked.removeprefix("tracked_"),linewidth=1.8)
        ax.axhline(1,color="black",ls="--",lw=.8)
        ax.set_title(f"Order d={d}")
        ax.set_xlabel("Forecast horizon h")
        ax.set_xticks(horizons)
        ax.grid(alpha=.15)
    axes[0,0].set_ylabel("Median cell RMSE tracking / matched pooled")
    axes[0,-1].legend(fontsize=8)
    fig.suptitle(
        "P2 | Tracking vs pooled under IDENTICAL historical weighting\n"
        "Median of scenario-level ratios (descriptive, no cross-cell CI)",
        fontsize=11,
    )
    fig.tight_layout()
    save(fig,root,"paper2_matched_tracking_relative_rmse")
    return "paper2_matched_tracking_relative_rmse"


def chart_numerical(root):
    path=root/"paper3_numerical_summary_compact.csv"
    if not path.exists():return None
    df=pd.read_csv(path)
    if df.empty:return None
    order=("grid","brent","adaptive")
    labels=(
        "grid_regret_to_dense","brent_regret_to_dense",
        "adaptive_regret_to_dense"
    )
    fig,ax=plt.subplots(figsize=(8,4.8))
    x=np.arange(len(df.h.unique()))
    horizons=sorted(df.h.unique())
    width=.23
    for i,(short,name) in enumerate(zip(order,labels)):
        val=[
            df.loc[df.h==h,name].median()
            if (df.h==h).any() else np.nan for h in horizons
        ]
        ax.bar(x+(i-1)*width,val,width,label=short)
    ax.set_xticks(x,horizons)
    ax.set_xlabel("Forecast horizon h")
    ax.set_ylabel("Median across diagnostic groups: F(selected S)-F(dense grid min)")
    ax.axhline(0,color="black",lw=.7)
    ax.grid(axis="y",alpha=.2)
    ax.legend()
    fig.suptitle(
        "P3 | Numerical optimizer regret against dense grid reference\n"
        "Reference is NOT exhaustive certified optimum; medians descriptive",
        fontsize=11,
    )
    fig.tight_layout()
    save(fig,root,"paper3_numerical_regret")
    return "paper3_numerical_regret"


def chart_coverage(root):
    df=pd.read_csv(root/"coverage_by_scenario.csv")
    if df.empty:return None
    counts=[df.loc[df.study==s,"completed_seeds"] for s in ("A","B","C","D")]
    fig,ax=plt.subplots(figsize=(8,4.6))
    ax.boxplot(counts,labels=["A","B","C","D"],showmeans=True)
    ax.set_xlabel("Predeclared DGP study")
    ax.set_ylabel("Completed independent seeds per scenario")
    ax.set_title("Partial factorial coverage (no imputation or new experiments)")
    ax.grid(axis="y",alpha=.2)
    fig.tight_layout()
    save(fig,root,"coverage_independent_seeds")
    return "coverage_independent_seeds"


def write_brief(root:Path):
    """Short factual results digest; no selection from a held-out winner."""
    import json
    inventory=json.loads((root/"ANALYSIS_MANIFEST.json").read_text(encoding="utf-8"))
    lines=[
        "# Retrospective Monte Carlo results — three previous papers",
        "",
        "**EXPLORATORY, NOT CONFIRMATORY.** This report is generated from "
        "the frozen, historically completed mu=0 CUDA experiment. "
        "It is NOT a result for the new nonzero-mean-difference paper.",
        "",
        f"- **Completed scenario/seed tasks:** "
        f"{inventory['completed_scenario_seed_tasks']:,} / "
        f"{inventory['expected_scenario_seed_tasks']:,}.",
        f"- **Originally stored method rows analyzed:** "
        f"{inventory['method_rows_processed']:,}.",
        f"- **Historical numerical cases:** "
        f"{inventory['numerical_diagnostic_rows']:,}.",
        "- **No new Monte Carlo or GPU tasks performed** during analysis.",
        "",
        "Every ratio below is sqrt(mean method MSE / mean comparator MSE) "
        "**inside one predeclared DGP cell**. Values summarized across cells "
        "are *medians* and proportions, not confidence intervals. "
        "For scenario-specific paired MSFE confidence intervals, "
        "consult the full compact CSVs.",
        "",
    ]
    def make_table(filename, title, selectors):
        df=pd.read_csv(root/filename)
        lines.extend([
            "## "+title,"",
            "| d | h | Method | Matched comparator | DGP cells | "
            "Median relative RMSE | Share of cells with ratio below 1 |",
            "|---:|---:|---|---|---:|---:|---:|",
        ])
        nrows=0
        for (d,h,selector,comparison),subset in df.groupby(
            ["d","h","selector","comparator"],dropna=False,sort=True
        ):
            if selector not in selectors:
                continue
            ratios=subset["relative_rmse"].replace([np.inf,-np.inf],np.nan).dropna()
            if ratios.empty:
                continue
            nrows+=1
            lines.append(
                f"| {d} | {h} | {selector} | {comparison} | "
                f"{len(ratios)} | {ratios.median():.4f} | "
                f"{(ratios<1).mean():.1%} |"
            )
        if not nrows:
            lines.append("| — | — | No available comparison | — | 0 | — | — |")
        lines.append("")
    make_table(
        "paper1_forecast_cv_vs_classical.csv",
        "Paper 1 — Classical CV/GCV/AICc/BIC versus pooled uniform forecast-CV",
        set(CLASSICAL),
    )
    make_table(
        "paper2_tracking_vs_matched_pooled.csv",
        "Paper 2 — Tracking versus pooled under the same temporal weighting",
        {x for x,_ in TRACKING},
    )
    numerical=root/"paper3_numerical_summary_compact.csv"
    if numerical.is_file():
        df=pd.read_csv(numerical)
        lines.extend([
            "## Paper 3 — Numerical search on the same F(S) surfaces",
            "",
            "| h | Diagnostic groups | Median grid regret | "
            "Median bounded-Brent regret | Median adaptive regret |",
            "|---:|---:|---:|---:|---:|",
        ])
        for h,part in df.groupby("h",sort=True):
            lines.append(
                f"| {h} | {len(part)} | "
                f"{part['grid_regret_to_dense'].median():.6g} | "
                f"{part['brent_regret_to_dense'].median():.6g} | "
                f"{part['adaptive_regret_to_dense'].median():.6g} |"
            )
        lines.append("")
    baselines=root/"paired_vs_baselines_scenario.csv"
    if baselines.is_file():
        df=pd.read_csv(baselines)
        # Exactly one predeclared reference for concise comparison; do not
        # select whichever of many methods happened to look best on test.
        part=df[(df["selector"]=="pooled_uniform_all")
                & (df["comparator"]=="naive")]
        lines.extend([
            "## Reference comparison with naive",
            "",
            "| d | h | DGP cells | Median pooled/naive RMSE | "
            "Share of cells with ratio below 1 |",
            "|---:|---:|---:|---:|---:|",
        ])
        for (d,h),cell in part.groupby(["d","h"],sort=True):
            ratios=cell["relative_rmse"].replace(
                [np.inf,-np.inf],np.nan
            ).dropna()
            if ratios.empty:continue
            lines.append(
                f"| {d} | {h} | {len(ratios)} | "
                f"{ratios.median():.4f} | {(ratios<1).mean():.1%} |"
            )
        lines.append("")
    lines.extend([
        "## Limits",
        "",
        "- The experiment was stopped before its full seed allocation. "
        "All 144 cells were represented, but approximately 696–704 "
        "seeds per cell were finished; actual numbers are in coverage CSV.",
        "- All retained findings are exploratory. Testing many "
        "methods and declaring a winner after seeing this external "
        "panel would need a NEW independent confirmation study.",
        "- Confidence intervals for **paired MSFE differences** are "
        "computed across independently generated seeds **within each "
        "cell**; medians and win-shares across heterogeneous DGP cells "
        "are descriptive, not joint inferential confidence bands.",
        "- Classical CV/GCV/AICc/BIC and P2 tracking do not model "
        "the new nonzero mean of differences; claims about that "
        "new estimator must await its independent pilot.",
        "- Grid/Brent/adaptive minima are numerical comparisons; "
        "the dense-grid reference is not a universal global proof.",
        "",
    ])
    (root/"REPORT_BRIEF.md").write_text(
        "\n".join(lines),encoding="utf-8"
    )


def plot(report_dir:Path):
    root=Path(report_dir)
    for required in (
        "paper1_forecast_cv_vs_classical.csv",
        "paper2_tracking_vs_matched_pooled.csv",
        "coverage_by_scenario.csv",
        "ANALYSIS_MANIFEST.json",
    ):
        if not (root/required).is_file():
            raise FileNotFoundError(
                f"Cannot draw frozen figures: {root/required} not found. "
                "Run analyze_frozen_compact FIRST."
            )
    figures=[]
    for fun in (
        chart_classical,chart_tracking,chart_numerical,chart_coverage
    ):
        chart=fun(root)
        if chart is not None:figures.append(chart)
    write_brief(root)
    (root/"README_FIGURES.md").write_text(
        "# Frozen Monte Carlo retrospective figures\n\n"
        "Figures drawn **only from stored, aggregated simulation "
        "statistics**, with no newly simulated series or fitted methods. "
        "Every ratio uses matched methods on the same scenario/seed/"
        "horizon/order; tracking uses the identical historical weighting "
        "as its pooled counterpart. Lines show medians across distinct "
        "predeclared scenarios, NOT independent seed-level confidence "
        "intervals. Source experiment was truncated at 100,848/144,000 "
        "tasks (check actual inventory for exact counts). Dense numerical "
        "grid is NOT a global certificate; no external replication "
        "has confirmed any purported winner.\n\n"
        "Generated:\n"+ "".join(f"- {x}.pdf and {x}.png\n" for x in figures),
        encoding="utf-8",
    )
    print(f"Figures: {', '.join(figures)} in {root}",flush=True)
    return figures


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-dir",required=True,type=Path)
    a=parser.parse_args(argv)
    plot(a.report_dir)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
