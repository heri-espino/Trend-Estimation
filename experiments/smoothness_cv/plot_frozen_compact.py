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
    ax.boxplot(counts,tick_labels=["A","B","C","D"],showmeans=True)
    ax.set_xlabel("Predeclared DGP study")
    ax.set_ylabel("Completed independent seeds per scenario")
    ax.set_title("Partial factorial coverage (no imputation or new experiments)")
    ax.grid(axis="y",alpha=.2)
    fig.tight_layout()
    save(fig,root,"coverage_independent_seeds")
    return "coverage_independent_seeds"


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
