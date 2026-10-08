"""Analyze large SQLite campaign WITHOUT loading every origin/lead into memory.

Paired uncertainty is computed from independent Monte Carlo replications
(seed WITHIN the scenario), NOT from overlapping forecast origins. A
scenario-specific confidence interval can be interpreted conditionally on
its DGP; cross-factor pooled summaries are descriptive, not independent
per-origin hypothesis tests.

From repo root:
    python -m experiments.smoothness_cv.analyze_simulation_campaign \
        --run-dir results/smoothness_cv/campaign_pilot
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sqlite3
import json

import numpy as np
import pandas as pd


def _summarize_independent(
    data: pd.DataFrame, group: list[str], outcome: str,
) -> pd.DataFrame:
    """Group replicate averages: standard errors use n independent seeds."""
    if data.empty:
        return pd.DataFrame(columns=group+[
            "n_replicates","mean","sd_replicate","se","ci95_low","ci95_high"
        ])
    frame=data.groupby(group,dropna=False)[outcome].agg(
        n_replicates="size",mean="mean",sd_replicate="std"
    ).reset_index()
    frame["se"]=frame["sd_replicate"]/np.sqrt(frame["n_replicates"])
    frame["ci95_low"]=frame["mean"]-1.96*frame["se"]
    frame["ci95_high"]=frame["mean"]+1.96*frame["se"]
    frame.loc[frame.n_replicates<2,["se","ci95_low","ci95_high"]]=np.nan
    return frame


def analyze(run_dir: Path, *, allow_partial: bool=False) -> dict[str,int]:
    manifest_path=run_dir/"manifest.json"
    db_path=run_dir/"outcomes.sqlite"
    if not manifest_path.exists() or not db_path.exists():
        raise FileNotFoundError("Expected both manifest.json and outcomes.sqlite.")
    manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    cfg=manifest["configuration"]
    expected=len(cfg["scenario_keys"])*cfg["seeds"]
    conn=sqlite3.connect(str(db_path),timeout=300)
    finished=int(conn.execute("SELECT COUNT(*) FROM completed").fetchone()[0])
    n_failed=int(conn.execute("SELECT COUNT(*) FROM failures").fetchone()[0])
    if finished!=expected and not allow_partial:
        conn.close()
        raise ValueError(
            f"Only {finished:,}/{expected:,} replications are complete. "
            "Use --allow-partial for exploratory interim summaries; "
            "they must NOT be presented as final results."
        )
    if not finished:
        conn.close()
        raise ValueError("No completed replications.")
    output=run_dir/"reports"
    output.mkdir(exist_ok=True)

    # One row per independent (DGP, seed, method, d, h), aggregating
    # *correlated* repeated outer-origin outcomes BEFORE uncertainty inference.
    query="""
    SELECT study,scenario,shape,n_obs,noise,sigma,seasonal,
           seed,d,h,selector,is_oracle, COUNT(*) AS n_outer,
           AVG(forecast_mse_obs) AS observed_msfe,
           AVG(forecast_mse_latent) AS latent_msfe,
           AVG(past_recovery_mse) AS recovery_mse,
           AVG(forecast_mse_conditional) AS conditional_msfe,
           AVG(selected_s) AS mean_selected_s,
           AVG(edf) AS mean_edf,
           AVG(branch_support) AS mean_branch_support,
           AVG(n_branches) AS mean_branch_count,
           AVG(n_local_minima) AS mean_local_minima_count,
           AVG(CASE WHEN selected_s<=0.0001 THEN 1.0 ELSE 0.0 END) AS at_zero,
           AVG(CASE WHEN selected_s>=0.9999 THEN 1.0 ELSE 0.0 END) AS at_one
      FROM outcomes
     GROUP BY study,scenario,shape,n_obs,noise,sigma,seasonal,
              seed,d,h,selector,is_oracle
    """
    seed_means=pd.read_sql_query(query,conn)
    seed_means.to_csv(output/"replicate_means.csv.gz",index=False,compression="gzip")
    group=[
        "study","scenario","shape","n_obs","noise","sigma","seasonal",
        "d","h","selector","is_oracle"
    ]
    agg=seed_means.groupby(group,dropna=False).agg(
        n_replicates=("seed","nunique"),
        n_outer_mean=("n_outer","mean"),
        mean_msfe=("observed_msfe","mean"),
        sd_msfe=("observed_msfe","std"),
        mean_latent_msfe=("latent_msfe","mean"),
        mean_recovery_mse=("recovery_mse","mean"),
        mean_conditional_msfe=("conditional_msfe","mean"),
        mean_s=("mean_selected_s","mean"),
        sd_s=("mean_selected_s","std"),
        mean_edf=("mean_edf","mean"),
        mean_branch_support=("mean_branch_support","mean"),
        mean_branch_count=("mean_branch_count","mean"),
        mean_local_minima_count=("mean_local_minima_count","mean"),
        fraction_s_zero=("at_zero","mean"),
        fraction_s_one=("at_one","mean"),
    ).reset_index()
    agg["rmse_obs"]=np.sqrt(agg["mean_msfe"])
    agg["rmse_latent"]=np.sqrt(agg["mean_latent_msfe"])
    agg["se_msfe"]=agg.sd_msfe/np.sqrt(agg.n_replicates)
    agg["ci95_msfe_low"]=agg.mean_msfe-1.96*agg.se_msfe
    agg["ci95_msfe_high"]=agg.mean_msfe+1.96*agg.se_msfe
    agg.loc[agg.n_replicates<2,["se_msfe","ci95_msfe_low","ci95_msfe_high"]]=np.nan
    agg.to_csv(output/"scenario_method_summary.csv",index=False)
    agg[agg.is_oracle==1].to_csv(output/"oracles_diagnostic_only.csv",index=False)

    # Matched comparisons at the same SEED and outer origins.
    # Single replication's risk gap averages over its own outer origins.
    # It is NOT computed as a difference between incomparable samples.
    pair_query="""
    SELECT a.study,a.scenario,a.shape,a.n_obs,a.noise,a.sigma,a.seasonal,
           a.seed,a.d,a.h,a.selector,a.is_oracle,
           COUNT(*) AS n_outer,
           AVG(a.forecast_mse_obs-b.forecast_mse_obs) AS paired_msfe_diff,
           AVG(a.forecast_mse_latent-b.forecast_mse_latent) AS paired_latent_diff,
           AVG(a.past_recovery_mse-b.past_recovery_mse) AS paired_recovery_diff,
           AVG(a.forecast_mse_obs) AS method_msfe,
           AVG(b.forecast_mse_obs) AS baseline_msfe
      FROM outcomes a JOIN outcomes b
        ON a.task_key=b.task_key AND a.origin=b.origin
       AND a.d=b.d AND a.h=b.h
       AND b.selector='pooled_uniform_all'
     GROUP BY a.study,a.scenario,a.shape,a.n_obs,a.noise,a.sigma,a.seasonal,
              a.seed,a.d,a.h,a.selector,a.is_oracle
    """
    paired_seeds=pd.read_sql_query(pair_query,conn)
    paired_seeds.to_csv(output/"paired_replicate_differences.csv.gz",index=False,compression="gzip")
    pair_group=[
        "study","scenario","shape","n_obs","noise","sigma","seasonal",
        "d","h","selector","is_oracle"
    ]
    paired=paired_seeds.groupby(pair_group,dropna=False).agg(
        n_replicates=("seed","nunique"),
        mean_paired_msfe_diff=("paired_msfe_diff","mean"),
        sd_paired_msfe_diff=("paired_msfe_diff","std"),
        mean_paired_latent_diff=("paired_latent_diff","mean"),
        mean_paired_recovery_diff=("paired_recovery_diff","mean"),
        mean_method_msfe=("method_msfe","mean"),
        mean_baseline_msfe=("baseline_msfe","mean"),
        win_fraction=("paired_msfe_diff",lambda x:float(np.mean(x<0))),
    ).reset_index()
    paired["relative_rmse"]=np.sqrt(
        paired.mean_method_msfe/paired.mean_baseline_msfe
    )
    paired["se_paired_diff"]=paired.sd_paired_msfe_diff/np.sqrt(paired.n_replicates)
    paired["ci95_paired_low"]=paired.mean_paired_msfe_diff-1.96*paired.se_paired_diff
    paired["ci95_paired_high"]=paired.mean_paired_msfe_diff+1.96*paired.se_paired_diff
    paired.loc[paired.n_replicates<2,[
        "se_paired_diff","ci95_paired_low","ci95_paired_high"
    ]]=np.nan
    paired.to_csv(output/"paired_scenario_comparisons.csv",index=False)

    # Across-scenario factor contrasts are descriptive and give equal weight
    # to each factorial cell, rather than giving one origin or seed more weight.
    for factor in ("study","shape","noise","n_obs","sigma","seasonal","d","h"):
        factor_data=agg[agg.is_oracle==0].groupby(
            [factor,"selector"],dropna=False,
        ).agg(
            n_cells=("scenario","size"),
            mean_s=("mean_s","mean"),
            mean_edf=("mean_edf","mean"),
            mean_branch_count=("mean_branch_count","mean"),
            mean_branch_support=("mean_branch_support","mean"),
            mean_msfe=("mean_msfe","mean"),
            mean_recovery_mse=("mean_recovery_mse","mean"),
            mean_latent_msfe=("mean_latent_msfe","mean"),
        ).reset_index()
        factor_data["rmse_from_mean_msfe"]=np.sqrt(factor_data.mean_msfe)
        factor_data.to_csv(output/f"effects_by_{factor}.csv",index=False)
    worst=paired[(paired.is_oracle==0)&(paired.selector!="pooled_uniform_all")].copy()
    worst=worst.sort_values("relative_rmse",ascending=False)
    worst.head(100).to_csv(output/"worst_relative_rmse_cases.csv",index=False)
    best=worst.sort_values("relative_rmse",ascending=True)
    best.head(100).to_csv(output/"best_relative_rmse_cases.csv",index=False)
    tasks=pd.read_sql_query(
        "SELECT AVG(elapsed_sec) AS mean_seconds, MIN(elapsed_sec) AS min_seconds, "
        "MAX(elapsed_sec) AS max_seconds, COUNT(*) AS n_tasks FROM completed",conn
    )
    tasks.to_csv(output/"task_timing.csv",index=False)
    conn.close()
    status=(
        f"# Campaign analysis ({'PARTIAL — EXPLORATORY' if finished<expected else 'COMPLETE'})\n\n"
        f"- Completed independent scenario/seed replications: {finished:,}/{expected:,}\n"
        f"- Logged failures: {n_failed}\n"
        f"- Distinct scenario cells in manifest: {len(cfg['scenario_keys'])}\n"
        f"- Repetitions per cell planned: {cfg['seeds']}\n"
        "- Unit for scenario-level uncertainty: **seed/replication**, not origin or forecast lead.\n"
        "- Mean MSE is averaged first within seed, then across independent seeds; "
        "RMSE is sqrt of mean MSE, not a mean of root errors.\n"
        "- Confidence bands are nominal 1.96*SE from independent replication averages "
        "(not multiple-comparison-adjusted).\n"
        "- 'paired' compares each method to pooled_uniform_all on identical scenario/seed/origins/d/h.\n"
        "- Oracle rows use latent ground truth unavailable to deployable methods: "
        "**diagnostics only**.\n"
        "- Factor effect CSVs are descriptive aggregates of cells, not inferential "
        "tests treating reused seed IDs across scenarios as independent.\n"
        "- All source-inspired A designs have exact source DGP parameters, "
        "but extended outer-forecast results are our experiment, not reproduced source results.\n"
        "- The main grid-based tracked minima are approximate; root-convergence and "
        "correspondence benchmarks are still required.\n"
        "- Methods were evaluated as predeclared alternatives. Picking a winner on this "
        "same external test invalidates independent confirmation.\n"
    )
    (output/"README_RESULTS.md").write_text(status,encoding="utf-8")
    return {
        "replications_complete":finished,
        "replications_expected":expected,
        "rows_seed_means":len(seed_means),
        "scenario_method_rows":len(agg),
        "paired_comparison_rows":len(paired),
    }


def main(argv=None)->int:
    p=argparse.ArgumentParser(description="Aggregate independent Monte Carlo units from campaign SQLite.")
    p.add_argument("--run-dir",type=Path,required=True)
    p.add_argument("--allow-partial",action="store_true")
    args=p.parse_args(argv)
    print(json.dumps(analyze(args.run_dir,allow_partial=args.allow_partial),indent=2))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
