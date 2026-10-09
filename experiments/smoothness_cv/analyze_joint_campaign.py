"""Post-run THREE-PAPER analysis for a time-budgeted GPU simulation.

Calls the existing P1/P2 seed-level analyzer, then adds:
- Paper 3: grid vs bracketed Brent vs analytic stationary points on
  exactly the same completed historical weighted F (sampled series).
- Separate naive, drift, seasonal naive and OLS forecasting baselines
  evaluated on exactly the same external forecast origins as P1/P2.
- Exact Sturm small-instance log provenance.

Incomplete 8-hour budget runs must be labeled exploratory. Never
pretend a partially completed factorial wave is a balanced full grid.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sqlite3

import numpy as np
import pandas as pd

from .analyze_simulation_campaign import analyze as analyze_primary


def has_table(conn,table):
    return bool(conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",(table,)
    ).fetchone())


def _numeric_rows(conn):
    if not has_table(conn,"numerical_diagnostics"):
        return pd.DataFrame()
    return pd.DataFrame(
        [json.loads(blob[0]) for blob in conn.execute(
            "SELECT payload FROM numerical_diagnostics ORDER BY scenario,seed,d,h,method"
        )]
    )


def _analyze_paper3(conn,folder):
    df=_numeric_rows(conn)
    if df.empty:
        return {"numeric_rows":0}
    df.to_csv(folder/"paper3_numerical_cases.csv.gz",index=False,compression="gzip")
    grouped=df.groupby(["study","shape","d","h","method"],as_index=False).agg(
        cases=("seed","size"),
        scenario_cells=("scenario","nunique"),
        mean_grid_regret=("grid_regret_to_dense","mean"),
        mean_brent_regret=("brent_regret_to_dense","mean"),
        mean_adaptive_regret=("adaptive_regret_to_dense","mean"),
        mean_grid_valleys=("n_grid_valleys","mean"),
        mean_adaptive_minima=("n_adaptive_minima","mean"),
        mean_brent_evals=("brent_objective_evaluations","mean"),
        mean_adaptive_evals=("adaptive_objective_evaluations","mean"),
        mean_brent_seconds=("brent_seconds","mean"),
        mean_adaptive_seconds=("adaptive_seconds","mean"),
        mean_dense_seconds=("dense_seconds","mean"),
        mean_abs_delta_S_brent=("brent_s",lambda s:float(np.nanmean(np.abs(
            s.to_numpy()-df.loc[s.index,"dense_s"].to_numpy())))),
        mean_abs_delta_S_adaptive=("adaptive_s",lambda s:float(np.nanmean(np.abs(
            s.to_numpy()-df.loc[s.index,"dense_s"].to_numpy())))),
    )
    grouped.to_csv(folder/"paper3_numerical_summary.csv",index=False)
    if has_table(conn,"numerical_failures"):
        fail=pd.read_sql_query("SELECT * FROM numerical_failures",conn)
        if not fail.empty:
            fail.to_csv(folder/"paper3_failed_cases.csv",index=False)
    return {"numeric_rows":int(len(df)),
            "numerical_cell_count":int(df.scenario.nunique())}


def _analyze_baselines(conn,folder):
    if not has_table(conn,"forecast_baselines"):
        return {"baseline_rows":0}
    # Work on averaged replicate units, and retain the full pairing key.
    # SQLite JSON extraction is supported on the Python bundled SQLite of
    # current Conda installations; avoid loading raw multi-lead payloads.
    sql="""
      SELECT b.scenario,b.seed,b.h,b.baseline,
             AVG(CAST(json_extract(b.payload,'$.forecast_mse_obs') AS REAL)) AS msfe,
             AVG(CAST(json_extract(b.payload,'$.forecast_mse_latent') AS REAL)) AS latent,
             AVG(CAST(json_extract(b.payload,'$.forecast_mae_obs') AS REAL)) AS mae,
             COUNT(*) AS origins
        FROM forecast_baselines b
        JOIN completed c
          ON c.task_key=(b.scenario||'__seed'||printf('%06d',b.seed))
       GROUP BY b.scenario,b.seed,b.h,b.baseline
       ORDER BY b.scenario,b.seed,b.h,b.baseline
    """
    chunks=list(pd.read_sql_query(sql,conn,chunksize=20000))
    if not chunks:
        return {"baseline_rows":0}
    df=pd.concat(chunks,ignore_index=True)
    df.to_csv(folder/"forecast_baseline_replicate_means.csv.gz",index=False,compression="gzip")
    stats=df.groupby(["scenario","h","baseline"],as_index=False).agg(
        seeds=("seed","nunique"),mean_msfe=("msfe","mean"),sd_msfe=("msfe","std"),
        mean_latent_mse=("latent","mean"),mean_mae=("mae","mean"),
        mean_outer_origins=("origins","mean"),
    )
    stats["rmse"]=np.sqrt(stats.mean_msfe)
    stats["se_msfe"]=stats.sd_msfe/np.sqrt(stats.seeds)
    stats.to_csv(folder/"forecast_baseline_scenario_summary.csv",index=False)
    return {"baseline_rows":int(len(df))}


def _paired_against_naive(conn,folder):
    if not has_table(conn,"forecast_baselines"):
        return 0
    sql="""
    SELECT a.scenario,a.seed,a.d,a.h,a.selector,
           AVG(a.forecast_mse_obs-
               CAST(json_extract(b.payload,'$.forecast_mse_obs') AS REAL)) AS diff_naive,
           AVG(a.forecast_mse_obs) AS method_msfe,
           AVG(CAST(json_extract(b.payload,'$.forecast_mse_obs') AS REAL)) AS naive_msfe,
           COUNT(*) AS matched_origins
      FROM outcomes a JOIN forecast_baselines b
        ON a.scenario=b.scenario AND a.seed=b.seed
       AND a.origin=b.origin AND a.h=b.h
       AND b.baseline='naive'
     WHERE a.is_oracle=0
     GROUP BY a.scenario,a.seed,a.d,a.h,a.selector
    """
    paired=pd.read_sql_query(sql,conn)
    if paired.empty:
        return 0
    paired.to_csv(folder/"paired_vs_naive_by_seed.csv.gz",
                  index=False,compression="gzip")
    summ=paired.groupby(["scenario","d","h","selector"],as_index=False).agg(
        independent_seeds=("seed","nunique"),
        mean_diff_vs_naive=("diff_naive","mean"),
        sd_diff_vs_naive=("diff_naive","std"),
        method_msfe=("method_msfe","mean"),
        naive_msfe=("naive_msfe","mean"),
        win_frequency=("diff_naive",lambda x:float(np.mean(x<0))),
    )
    summ["relative_rmse_to_naive"]=np.sqrt(summ.method_msfe/summ.naive_msfe)
    summ["standard_error"]=summ.sd_diff_vs_naive/np.sqrt(summ.independent_seeds)
    summ["ci95_low"]=summ.mean_diff_vs_naive-1.96*summ.standard_error
    summ["ci95_high"]=summ.mean_diff_vs_naive+1.96*summ.standard_error
    summ.to_csv(folder/"paired_vs_naive_scenario.csv",index=False)
    return len(paired)


def main(argv=None):
    p=argparse.ArgumentParser(description="Joint 3-paper exploratory report from timed CUDA SQLite.")
    p.add_argument("--run-dir",required=True,type=Path)
    p.add_argument("--allow-partial",action="store_true",
                   help="Needed after a time-budget stop; partial evidence is NOT confirmatory.")
    args=p.parse_args(argv)
    main_stats=analyze_primary(args.run_dir,allow_partial=args.allow_partial)
    conn=sqlite3.connect(str(args.run_dir/"outcomes.sqlite"),timeout=300)
    folder=args.run_dir/"reports"
    numeric=_analyze_paper3(conn,folder)
    baselines=_analyze_baselines(conn,folder)
    paired_count=_paired_against_naive(conn,folder)
    conn.close()
    status_path=args.run_dir/"run_status.json"
    status=json.loads(status_path.read_text()) if status_path.exists() else {}
    report={
        **main_stats,**numeric,**baselines,
        "paired_vs_naive_replicate_rows":int(paired_count),
        "sturm_exact_control":bool((args.run_dir/"sturm_exact_reference.txt").exists()),
        "run_status":status.get("status","unknown"),
    }
    (folder/"THREE_PAPER_REPORT.md").write_text(
        "# Unified three-paper simulation report\n\n"
        f"- Runtime status: **{report['run_status']}**.\n"
        f"- Paired P1/P2 scenario-seed tasks: {main_stats['replications_complete']:,} "
        f"/ {main_stats['replications_expected']:,} planned.\n"
        f"- Paper 3 numerical diagnostic cases: {numeric.get('numeric_rows',0):,}.\n"
        f"- Separate benchmark replicate rows: {baselines.get('baseline_rows',0):,}.\n"
        f"- Exact tiny Sturm fixture log available: {report['sturm_exact_control']}.\n\n"
        "**Interpretation:** if any design cells or seed waves are missing, "
        "this is an exploratory truncated factorial sample, not completed "
        "confirmatory evidence. Original P1/P2 paired SEs use independent "
        "seeds *within each scenario*, not outer origins. Brent is local "
        "within each identified grid valley, adaptive root search is "
        "not guaranteed exhaustive, and the dense reference is numerical "
        "not a Sturm certificate. Sturm's fixed small rational fixture "
        "does not generalize to Monte Carlo window sizes. Oracle tau "
        "selectors are diagnostic and excluded from actionable comparisons.\n",
        encoding="utf-8",
    )
    print(json.dumps(report,indent=2))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
