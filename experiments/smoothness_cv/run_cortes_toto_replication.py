"""Faithful *in-sample smoothing* factorial reference to Cortés-Toto et al. (2017).

This is deliberately SEPARATE from our new rolling-origin forecasting
experiments: the source article selected lambda on FULL simulated N=50/200
series for the original 2^4 design, without untouched future forecasting.

Run from repo root (manual; no heavy GitHub workflow):
    python -m experiments.smoothness_cv.run_cortes_toto_replication --seeds 100 --jobs 32

Compares CV/GCV/AICc/BIC on discrete pure d=2 PLS; reports their raw
Guerrero smoothness scale as well as our normalized index. More Monte Carlo
seeds, deterministic NumPy RNG and a fixed grid imply an approximate
methodological replication, not literal reproduction of their R draws.
"""
from __future__ import annotations
import os
for _var in (
    "OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS","VECLIB_MAXIMUM_THREADS","BLIS_NUM_THREADS"
):
    os.environ[_var]="1"

import argparse
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import multiprocessing as mp
from pathlib import Path
import sqlite3

import numpy as np
import pandas as pd

from .simulation_dgps import Scenario,grid_scenarios,make_series
from .simulation_evaluation import _spectral_candidates
from .run_simulation_campaign import git_revision,resolve_jobs


def _replicate(task: tuple[Scenario,int,int]) -> tuple[str,list[tuple]]:
    scenario,seed,grid_points=task
    data=make_series(scenario,seed)
    n=scenario.n_obs
    grid,fits,selected,recovery=_spectral_candidates(
        data.observed,data.trend,order=2,grid_points=grid_points
    )
    values=[]
    for criterion in ("cv","gcv","aicc","bic"):
        s=float(selected[criterion])
        i=int(np.argmin(np.abs(grid-s)))
        edf=n-(n-2)*s
        raw_s=1-edf/n
        rss=float(np.sum((data.observed-fits[i])**2))
        values.append((
            scenario.key,int(seed),criterion,
            scenario.shape,int(scenario.seasonal),float(scenario.sigma),
            n,s,float(raw_s),float(edf),rss,
            float(recovery[i]),
        ))
    return f"{scenario.key}__seed{seed:06d}",values


def _db(path: Path) -> sqlite3.Connection:
    c=sqlite3.connect(path,timeout=90)
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA synchronous=NORMAL")
    c.execute(
        "CREATE TABLE IF NOT EXISTS outcomes ("
        "scenario TEXT NOT NULL,seed INTEGER NOT NULL,criterion TEXT NOT NULL,"
        "shape TEXT NOT NULL,seasonal INTEGER NOT NULL,sigma REAL NOT NULL,"
        "N INTEGER NOT NULL,S_normalized REAL NOT NULL,S_Guerrero REAL NOT NULL,"
        "edf REAL NOT NULL,rss REAL NOT NULL,latent_recovery_mse REAL NOT NULL,"
        "PRIMARY KEY(scenario,seed,criterion)) WITHOUT ROWID"
    )
    c.execute(
        "CREATE TABLE IF NOT EXISTS completed ("
        "task_key TEXT PRIMARY KEY,n_rows INTEGER NOT NULL)"
    )
    c.commit()
    return c


def _effect_table(frame: pd.DataFrame) -> pd.DataFrame:
    """Descriptive high-minus-low main effects, not inferential ANOVA p-values."""
    factors=[
        ("shape","source_linear","source_beta"),
        ("seasonal",0,1),
        ("sigma",.5,2.),
        ("N",50,200),
    ]
    records=[]
    # Separate results by criterion; each factorial cell receives equal
    # weight after averaging its own independent seeds.
    cell=frame.groupby(
        ["criterion","shape","seasonal","sigma","N"],as_index=False
    )[["S_Guerrero","S_normalized","latent_recovery_mse"]].mean()
    for criterion in ("cv","gcv","aicc","bic"):
        chunk=cell[cell.criterion==criterion]
        for factor,low,high in factors:
            for measure in ("S_Guerrero","S_normalized","latent_recovery_mse"):
                low_mean=float(chunk.loc[chunk[factor]==low,measure].mean())
                high_mean=float(chunk.loc[chunk[factor]==high,measure].mean())
                records.append({
                    "criterion":criterion,"factor":factor,
                    "low":str(low),"high":str(high),"measure":measure,
                    "mean_low":low_mean,"mean_high":high_mean,
                    "main_effect_high_minus_low":high_mean-low_mean,
                })
    return pd.DataFrame(records)


def analyze(conn: sqlite3.Connection,out_dir: Path) -> None:
    report=out_dir/"reports"
    report.mkdir(exist_ok=True)
    all_rows=pd.read_sql_query("SELECT * FROM outcomes",conn)
    if all_rows.empty:
        return
    all_rows.to_csv(report/"source_factorial_replicates.csv.gz",
                    index=False,compression="gzip")
    by_cell=all_rows.groupby(
        ["shape","seasonal","sigma","N","criterion"],as_index=False
    ).agg(
        n_replicates=("seed","nunique"),
        mean_source_smoothness=("S_Guerrero","mean"),
        sd_source_smoothness=("S_Guerrero","std"),
        mean_normalized_smoothness=("S_normalized","mean"),
        mean_edf=("edf","mean"),
        mean_latent_recovery_mse=("latent_recovery_mse","mean"),
    )
    by_cell.to_csv(report/"source_factorial_by_cell.csv",index=False)
    _effect_table(all_rows).to_csv(report/"main_effect_contrasts.csv",index=False)
    (report/"README_RESULTS.md").write_text(
        "# Cortes-Toto factorial reference\n\n"
        "Original 2^4 trends/seasonality/noise SD/N, with d=2, mu=0.\n"
        "CV/GCV/AICc/BIC were evaluated on the COMPLETE N-point series.\n"
        "The paper's smoothness axis is S_Guerrero=1-edf/N, not S_normalized.\n"
        "This is a methodological Monte Carlo reproduction (different random "
        "samples, explicit Python grid), not a literal replication of source R runs.\n"
        "Latent-recovery MSE is OUR added diagnostic, not a reported source endpoint.\n"
        "Forecast accuracy is evaluated in the separate rolling-origin campaign.\n"
        "Contrast outputs are descriptive mean effects without ANOVA p-values.\n",
        encoding="utf-8",
    )


def main(argv=None) -> int:
    p=argparse.ArgumentParser(description="Original Cortes-Toto 2^4 PLS in-sample factorial.")
    p.add_argument("--seeds",type=int,default=100)
    p.add_argument("--seed-start",type=int,default=0)
    p.add_argument("--jobs",type=int,default=0)
    p.add_argument("--grid-points",type=int,default=501)
    p.add_argument("--max-tasks",type=int,default=None)
    p.add_argument("--run-dir",type=Path,default=Path("results/smoothness_cv/source_factorial"))
    p.add_argument("--dry-run",action="store_true")
    args=p.parse_args(argv)
    if args.seeds<1 or args.seed_start<0 or not 11<=args.grid_points<=2001:
        p.error("Require seeds>0, seed-start>=0, and grid-points 11..2001.")
    scenarios=[s for s in grid_scenarios("extensive") if s.study=="A"]
    tasks=[(s,seed,args.grid_points)
           for s in scenarios for seed in range(args.seed_start,args.seed_start+args.seeds)]
    jobs=resolve_jobs(args.jobs)
    print(f"Source 2^4 replication: cells={len(scenarios)}, scenario-seed "
          f"series={len(tasks):,}, grid={args.grid_points}, jobs={jobs}",flush=True)
    if args.dry_run:
        return 0
    payload={
        "protocol":"source_factorial_v1",
        "cells":[s.key for s in scenarios],
        "seeds":args.seeds,"seed_start":args.seed_start,
        "grid_points":args.grid_points,
        "git_revision":git_revision(),
    }
    fingerprint=hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
    root=args.run_dir
    root.mkdir(parents=True,exist_ok=True)
    mpath=root/"manifest.json"
    if mpath.exists():
        previous=json.loads(mpath.read_text())
        if previous["fingerprint"]!=fingerprint:
            p.error("Run parameters/code changed: use a new --run-dir.")
    else:
        mpath.write_text(
            json.dumps({
                "fingerprint":fingerprint,"configuration":payload,
                "created":datetime.now(timezone.utc).isoformat(),
            },indent=2),encoding="utf-8",
        )
    conn=_db(root/"source_factorial.sqlite")
    done={r[0] for r in conn.execute("SELECT task_key FROM completed")}
    todo=[t for t in tasks if f"{t[0].key}__seed{t[1]:06d}" not in done]
    if args.max_tasks is not None:
        if args.max_tasks<1:
            p.error("--max-tasks must be positive.")
        todo=todo[:args.max_tasks]
    print(f"Previously completed={len(done)}, pending now={len(todo)}",flush=True)
    if jobs==1:
        iterator=map(_replicate,todo)
        pool=None
    else:
        pool=ProcessPoolExecutor(
            max_workers=jobs,mp_context=mp.get_context("spawn")
        )
        iterator=pool.map(_replicate,todo,chunksize=1)
    try:
        for i,(key,rows) in enumerate(iterator,start=1):
            with conn:
                conn.executemany(
                    "INSERT OR REPLACE INTO outcomes VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    rows,
                )
                conn.execute(
                    "INSERT OR REPLACE INTO completed VALUES (?,?)",
                    (key,len(rows)),
                )
            if i%max(1,len(todo)//100)==0 or i==len(todo):
                print(f"[{i}/{len(todo)}] complete",flush=True)
    finally:
        if pool is not None:
            pool.shutdown(wait=True)
    analyze(conn,root)
    conn.close()
    print(f"Factorial source reports: {root/'reports'}",flush=True)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
