"""Streaming publication-screen summaries of an EXISTING frozen formal8h campaign.

Reads SQLite mode=ro; absolutely NO simulation, CUDA, refitting, or new draws.
Outputs compact CSVs from matched seed-level comparisons (not from
incorrect independence assumptions about overlapping outer origins).

Usage:
    python -m experiments.smoothness_cv.analyze_frozen_compact \
      --run-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN

Scans the ~65M stored rows just ONCE in primary-key order, one Monte Carlo
scenario/seed task at a time (hundreds of rows), then records one independent
seed average per method/scenario/order/horizon. Can take time, but bounded
RAM. Benchmark records are fetched by same task key, never fabricated.
All summary files are exploratory; raw Monte Carlo DB is never modified.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from contextlib import closing
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import groupby
import json
import math
from pathlib import Path
import time

from .recover_campaign import inspect, ro_connect


@dataclass
class Running:
    n: int = 0
    mean: float = 0.
    m2: float = 0.

    def add(self, x: float):
        x=float(x)
        if not math.isfinite(x):
            return
        self.n+=1
        dx=x-self.mean
        self.mean+=dx/self.n
        self.m2+=dx*(x-self.mean)

    @property
    def sd(self):
        return math.sqrt(max(0.,self.m2/(self.n-1))) if self.n>1 else math.nan

    @property
    def se(self):
        return self.sd/math.sqrt(self.n) if self.n>1 else math.nan


def add_group(store: dict, key: tuple, values: dict[str,float]):
    bucket=store.setdefault(key,{})
    for label,value in values.items():
        bucket.setdefault(label,Running()).add(value)


def details(bucket: dict, metric: str) -> dict:
    s=bucket[metric]
    return {
        metric:s.mean,
        f"sd_{metric}":s.sd,
        f"se_{metric}":s.se,
        f"ci95_{metric}_low":s.mean-1.96*s.se,
        f"ci95_{metric}_high":s.mean+1.96*s.se,
        f"n_{metric}":s.n,
    }


def write_csv(path:Path, rows:list[dict]):
    path.parent.mkdir(parents=True,exist_ok=True)
    if not rows:
        raise ValueError(f"No records available for {path.name}.")
    columns=list(dict.fromkeys(k for row in rows for k in row))
    with path.open("w",encoding="utf-8",newline="") as out:
        writer=csv.DictWriter(out,fieldnames=columns,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


# Stored columns, ordered exactly in SELECT below. Only read numbers
# needed for reporting, not huge JSON strings of per-lead errors.
SQL_ROWS="""SELECT task_key,scenario,study,shape,n_obs,noise,sigma,seasonal,
                   seed,origin,d,h,selector,is_oracle,
                   forecast_mse_obs,forecast_mse_latent,past_recovery_mse,
                   forecast_mse_conditional,forecast_mae_obs,
                   selected_s,edf,branch_support,n_local_minima
              FROM outcomes
             ORDER BY task_key,origin,d,h,selector"""


def matched_comparators(selector: str):
    if selector.startswith("tracked_"):
        return ("pooled_"+selector[len("tracked_"):],)
    if selector!="pooled_uniform_all":
        return ("pooled_uniform_all",)
    return ()


def combine_one_task(
    rows, baseline_cursor, summaries, paired, baseline_summaries, paired_naive
):
    """Reduce all rows of ONE scenario/seed to independent seed means.

    Every paired difference uses the exact same origin,d,h and only
    recognized deployable selector pairs; latent-oracle methods are NEVER
    included as deployable wins.
    """
    first=rows[0]
    task_key,scenario,study,shape,n_obs,noise,sigma,seasonal,seed=first[:9]
    prefix=(study,scenario,shape,noise,int(n_obs),float(sigma),int(seasonal))
    per_model=defaultdict(list)
    per_origin=defaultdict(dict)

    for row in rows:
        origin,d,h,selector,is_oracle=row[9:14]
        key=(int(d),int(h),str(selector),int(is_oracle))
        per_model[key].append(row)
        per_origin[(int(origin),int(d),int(h))][str(selector)]=row

    for (d,h,method,oracle),folds in per_model.items():
        n=len(folds)
        values={
            "observed_msfe":sum(float(r[14]) for r in folds)/n,
            "latent_msfe":sum(float(r[15]) for r in folds)/n,
            "recovery_mse":sum(float(r[16]) for r in folds)/n,
            "conditional_msfe":sum(float(r[17]) for r in folds)/n,
            "observed_mae":sum(float(r[18]) for r in folds)/n,
            "selected_s":sum(float(r[19]) for r in folds)/n,
            "edf":sum(float(r[20]) for r in folds)/n,
            "branch_support":sum(float(r[21]) for r in folds)/n,
            "local_minima":sum(float(r[22]) for r in folds)/n,
            "outer_origins":n,
        }
        add_group(summaries,prefix+(d,h,method,oracle),values)

    pairs=defaultdict(list)
    for (origin,d,h),lookup in per_origin.items():
        for method,row in lookup.items():
            if int(row[13]):
                continue  # ORACLES ARE NOT SELECTABLE MODELS.
            for comparator in matched_comparators(method):
                baseline=lookup.get(comparator)
                if baseline is None or int(baseline[13]):
                    continue
                pairs[(d,h,method,comparator)].append((
                    float(row[14])-float(baseline[14]),
                    float(row[14]),float(baseline[14]),
                    float(row[15])-float(baseline[15]),
                    float(row[16])-float(baseline[16]),
                ))

    for (d,h,method,comparator),matches in pairs.items():
        n=len(matches)
        v={
            "paired_observed_msfe_diff":sum(x[0] for x in matches)/n,
            "method_msfe":sum(x[1] for x in matches)/n,
            "comparator_msfe":sum(x[2] for x in matches)/n,
            "paired_latent_mse_diff":sum(x[3] for x in matches)/n,
            "paired_recovery_mse_diff":sum(x[4] for x in matches)/n,
            "seed_win":float(sum(x[0] for x in matches)/n < 0),
            "matched_origins":n,
        }
        add_group(paired,prefix+(d,h,method,comparator),v)

    # Existing (scenario, seed) baseline rows use their own primary key;
    # no full-table JOIN or temporary SQL index on 65M rows.
    base_at={}
    base_averages=defaultdict(list)
    for origin,h,name,payload in baseline_cursor.execute(
        "SELECT origin,h,baseline,payload FROM forecast_baselines "
        "WHERE scenario=? AND seed=? ORDER BY origin,h,baseline",
        (scenario,int(seed)),
    ):
        data=json.loads(payload)
        obs=float(data["forecast_mse_obs"])
        latent=float(data["forecast_mse_latent"])
        base_at[(int(origin),int(h),str(name))]=(obs,latent)
        base_averages[(int(h),str(name))].append((
            obs,latent,float(data["forecast_mae_obs"]),
        ))

    for (h,name),records in base_averages.items():
        n=len(records)
        add_group(baseline_summaries,prefix+(h,name),{
            "observed_msfe":sum(r[0] for r in records)/n,
            "latent_msfe":sum(r[1] for r in records)/n,
            "observed_mae":sum(r[2] for r in records)/n,
            "outer_origins":n,
        })
    for name in ("naive","drift","seasonal_naive","linear_ols"):
        matched=defaultdict(list)
        for (origin,d,h),lookup in per_origin.items():
            b=base_at.get((origin,h,name))
            if b is None:
                continue
            for method,row in lookup.items():
                if int(row[13]):
                    continue
                matched[(d,h,method)].append((
                    float(row[14])-b[0],float(row[14]),b[0]
                ))
        for (d,h,method),pairs_at_seed in matched.items():
            n=len(pairs_at_seed)
            add_group(paired_naive,prefix+(d,h,method,name),{
                "paired_observed_msfe_diff":sum(r[0] for r in pairs_at_seed)/n,
                "method_msfe":sum(r[1] for r in pairs_at_seed)/n,
                "comparator_msfe":sum(r[2] for r in pairs_at_seed)/n,
                "seed_win":float(sum(r[0] for r in pairs_at_seed)/n < 0),
                "matched_origins":n,
            })


META=("study","scenario","shape","noise","n_obs","sigma","seasonal")


def export_groups(folder, filename, groups, *, kind):
    result=[]
    for key,bucket in sorted(groups.items()):
        labels=(
            META+("d","h","selector","is_oracle")
            if kind=="method" else
            META+("d","h","selector","comparator")
            if kind in ("paired","naive") else
            META+("h","baseline")
        )
        row=dict(zip(labels,key))
        metric=(
            "observed_msfe" if kind in ("method","baseline")
            else "paired_observed_msfe_diff"
        )
        row["n_independent_seeds"]=bucket[metric].n
        for label in bucket:
            row.update(details(bucket,label))
        if kind in ("method","baseline"):
            row["rmse_observed"]=math.sqrt(max(0.,row["observed_msfe"]))
            row["rmse_latent"]=math.sqrt(max(0.,row["latent_msfe"]))
        else:
            base=row["comparator_msfe"]
            row["relative_rmse"]=(
                math.sqrt(max(0.,row["method_msfe"])/base)
                if base>0 else math.nan
            )
        result.append(row)
    if result:
        write_csv(folder/filename,result)
    return result


NUMERIC_METRICS=(
    "grid_regret_to_dense","brent_regret_to_dense",
    "adaptive_regret_to_dense","n_grid_valleys",
    "n_adaptive_minima","brent_objective_evaluations",
    "adaptive_objective_evaluations","brent_seconds",
    "adaptive_seconds","dense_seconds",
    "grid_outer_observed_mse","brent_outer_observed_mse",
    "adaptive_outer_observed_mse","grid_outer_latent_mse",
    "brent_outer_latent_mse","adaptive_outer_latent_mse",
    "grid_past_recovery_mse","brent_past_recovery_mse",
    "adaptive_past_recovery_mse",
)


def numerical_summaries(conn,report_dir:Path):
    tables={x[0] for x in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )}
    if "numerical_diagnostics" not in tables:
        return 0
    store={}
    total=0
    for (blob,) in conn.execute(
        "SELECT payload FROM numerical_diagnostics ORDER BY scenario,seed,d,h,method"
    ):
        row=json.loads(blob)
        key=(row["study"],row["shape"],int(row["d"]),
             int(row["h"]),row["method"])
        values={key:float(row[key]) for key in NUMERIC_METRICS
                if key in row and row[key] is not None}
        if "brent_s" in row and "dense_s" in row:
            values["abs_s_brent_dense"]=abs(float(row["brent_s"])-float(row["dense_s"]))
        if "adaptive_s" in row and "dense_s" in row:
            values["abs_s_adaptive_dense"]=abs(
                float(row["adaptive_s"])-float(row["dense_s"])
            )
        add_group(store,key,values)
        total+=1
    summary=[]
    for key,bucket in sorted(store.items()):
        row=dict(zip(("study","shape","d","h","method"),key))
        row["n_numerical_cases"]=next(iter(bucket.values())).n
        for k in bucket:
            row.update(details(bucket,k))
        summary.append(row)
    if summary:
        write_csv(report_dir/"paper3_numerical_summary_compact.csv",summary)
    return total


def analyze(run_dir:Path,*,report_dir:Path|None=None,progress_every:int=3000) -> dict:
    start=time.perf_counter()
    run_dir=Path(run_dir)
    if report_dir is None:
        report_dir=run_dir/"reports"/"frozen_compact"
    report_dir=Path(report_dir)
    if not (run_dir/"manifest.json").is_file() or not (
        run_dir/"outcomes.sqlite"
    ).is_file():
        raise FileNotFoundError(
            f"Expected frozen manifest.json and outcomes.sqlite in {run_dir}. "
            "If only outcomes.sqlite.incomplete exists, validate/finalize "
            "that backup with recover_campaign --finalize-incomplete FIRST."
        )
    manifest=json.loads((run_dir/"manifest.json").read_text(encoding="utf-8"))
    assert manifest["configuration"]["preset"]=="formal8h", (
        "This compact analysis is currently specified for frozen formal8h only."
    )
    inventory=inspect(run_dir)
    n_completed=inventory["completed_scenario_seed_tasks"]
    if not n_completed:
        raise ValueError("No completed Monte Carlo tasks in the frozen database.")
    report_dir.mkdir(parents=True,exist_ok=True)
    summary_groups={}
    pair_groups={}
    baseline_groups={}
    naive_groups={}
    method_rows=0
    completed_tasks=0
    with closing(ro_connect(run_dir/"outcomes.sqlite")) as conn:
        tables={r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )}
        if "forecast_baselines" not in tables:
            raise ValueError(
                "This campaign does not contain forecast_baselines; "
                "stop rather than silently invent benchmark comparisons."
            )
        expected_counts=dict(conn.execute(
            "SELECT task_key,n_rows FROM completed"
        ))
        if len(expected_counts)!=n_completed:
            raise RuntimeError("SQLite completed inventory is inconsistent.")
        cursor=conn.execute(SQL_ROWS)
        base_cursor=conn.cursor()
        for taskkey, iterator in groupby(cursor,key=lambda row:row[0]):
            rows=list(iterator)  # only ONE original scenario/seed task in RAM
            expected=expected_counts.get(taskkey)
            if expected is None or expected!=len(rows):
                raise RuntimeError(
                    f"Stored task {taskkey} disagrees with atomic completed row count. "
                    f"Expected {expected}, actual {len(rows)}. NO output "
                    "should be interpreted before inspecting the data."
                )
            method_rows+=len(rows)
            combine_one_task(
                rows,base_cursor,summary_groups,pair_groups,
                baseline_groups,naive_groups
            )
            completed_tasks+=1
            if completed_tasks%progress_every==0:
                print(
                    f"[analysis only] independent tasks {completed_tasks:,}"
                    f"/{n_completed:,} | stored model rows {method_rows:,} "
                    f"| elapsed {(time.perf_counter()-start)/60:.1f} min",
                    flush=True
                )
        if completed_tasks!=n_completed:
            raise RuntimeError(
                f"Found {completed_tasks} tasks but recorded {n_completed}."
            )
        if method_rows!=inventory["saved_method_rows_from_atomic_completed"]:
            raise RuntimeError(
                f"Read {method_rows} outcome rows but atomic completed "
                f"records claim {inventory['saved_method_rows_from_atomic_completed']}."
            )
        print("Stored model rows verified. Aggregating compact tables...",flush=True)
        n_numerical=numerical_summaries(conn,report_dir)
    model_rows=export_groups(
        report_dir,"paper1_2_method_scenario.csv",
        summary_groups,kind="method",
    )
    pair_rows=export_groups(
        report_dir,"paper1_2_paired_scenario.csv",
        pair_groups,kind="paired",
    )
    baselines=export_groups(
        report_dir,"baseline_scenario.csv",
        baseline_groups,kind="baseline",
    )
    vs_baselines=export_groups(
        report_dir,"paired_vs_baselines_scenario.csv",
        naive_groups,kind="naive",
    )
    # Separate tables with no oracles and explicitly matching weighting.
    write_csv(report_dir/"paper1_forecast_cv_vs_classical.csv",[
        r for r in pair_rows
        if r["comparator"]=="pooled_uniform_all"
        and r["selector"].startswith(("classical_","fixed_"))
    ])
    write_csv(report_dir/"paper2_tracking_vs_matched_pooled.csv",[
        r for r in pair_rows
        if r["selector"].startswith("tracked_")
        and r["comparator"]==
            "pooled_"+r["selector"][len("tracked_"):]
    ])
    coverage=[{
        "study":x["study"],"scenario":x["scenario"],
        "completed_seeds":x["completed"],
        "declared_seeds_per_cell":inventory["seeds_per_cell_declared"],
    } for x in inventory["scenario_completion"]]
    write_csv(report_dir/"coverage_by_scenario.csv",coverage)
    info={
        "status":"PARTIAL — EXPLORATORY, nonconfirmatory",
        "source_dir":inventory["source_dir"],
        "original_git_revision":inventory["original_git_revision"],
        "completed_scenario_seed_tasks":completed_tasks,
        "expected_scenario_seed_tasks":inventory["expected_scenario_seed_tasks"],
        "scenario_cells_present":inventory["completed_scenario_cells"],
        "method_rows_processed":method_rows,
        "numerical_diagnostic_rows":n_numerical,
        "scenario_method_summary_rows":len(model_rows),
        "paired_method_summary_rows":len(pair_rows),
        "baseline_summary_rows":len(baselines),
        "paired_vs_simple_baseline_summary_rows":len(vs_baselines),
        "runtime_minutes":round((time.perf_counter()-start)/60,2),
        "simulation_tasks_executed":0,
        "raw_snapshot_modified":False,
        "benchmark_comparison":"matched scenario/seed/outer origin/horizon",
        "independent_inference_unit":"scenario-specific Monte Carlo seed",
        "numerical_reference":"dense grid, NOT certification of all minima",
        "statistical_limitation":"Time-truncated exploratory design; multiple testing and method selection on same holdout preclude confirmatory winner claims.",
    }
    (report_dir/"ANALYSIS_MANIFEST.json").write_text(
        json.dumps(info,indent=2,ensure_ascii=False),encoding="utf-8"
    )
    (report_dir/"README_RESULTS.md").write_text(
        "# Frozen CUDA campaign — exploratory retrospective analysis\n\n"
        f"- **{completed_tasks:,} of {info['expected_scenario_seed_tasks']:,}** "
        "scenario-seed tasks retained; all 144 DGP cells represented.\n"
        f"- Processed **{method_rows:,} original saved model rows** with "
        "no new Monte Carlo runs.\n"
        f"- Numerics: **{n_numerical:,}** recorded diagnostic cases "
        "(Brent, adaptive, dense grid; NOT an exhaustive certificate).\n"
        "- The three papers here are the **previous mu=0 design**; this "
        "is NOT a result for the newer nonzero difference-mean method.\n\n"
        "## Statistical protocol\n\n"
        "1. First average correlated overlapping external origins inside "
        "each independent scenario/seed for each model/d/h.\n"
        "2. Compute differences between methods for the **same origin, "
        "seed, order and horizon**; then average at seed level.\n"
        "3. Across independent seeds **within a DGP scenario** compute "
        "mean, SD and nominal 95% CI of seed-averaged paired MSFE gaps.\n"
        "4. Paper 2 tracked_* is compared with pooled_* of the **same "
        "historical weighting**; Paper 1 classical/fixed comparisons are "
        "against pooled_uniform_all. No oracle rows in usable comparisons.\n"
        "5. Baselines naive, drift, seasonal_naive and linear_ols are "
        "genuine matched external forecasts; no artificial S or EDF.\n\n"
        "## Reporting limitations\n\n"
        "The time budget left unequal seed counts across the 144 cells; "
        "we did NOT impute missing experiments, rerun seeds, or turn "
        "overlapping forecast origins into independent replicates. "
        "Relative RMSE in a table is sqrt(mean method MSE / mean "
        "comparator MSE) within that cell; confidence intervals attach "
        "to the PAIRED MSFE difference, NOT to the RMSE ratio. "
        "Any model-selection conclusion made by inspecting this "
        "external panel is exploratory, not independent confirmation.\n\n"
        "## Compact outputs\n\n"
        "- paper1_2_method_scenario.csv: observed/latent/recovery "
        "MSE, S, EDF and branch diagnostics by scenario/d/h/selector.\n"
        "- paper1_forecast_cv_vs_classical.csv: paired CV, GCV, "
        "AICc, BIC and fixed-S comparisons with pooled_uniform_all.\n"
        "- paper2_tracking_vs_matched_pooled.csv: tracked versus "
        "pooled under the identical weighting rule.\n"
        "- paired_vs_baselines_scenario.csv and baseline_scenario.csv: "
        "comparisons against standard time-series forecasters.\n"
        "- paper3_numerical_summary_compact.csv: stored numerical "
        "diagnostics aggregated without interpreting dense grid "
        "as exact roots.\n"
        "- coverage_by_scenario.csv and ANALYSIS_MANIFEST.json: "
        "reproducible partial-coverage inventory and analysis status.\n",
        encoding="utf-8",
    )
    print(json.dumps(info,indent=2,ensure_ascii=False),flush=True)
    return info


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--run-dir",type=Path,required=True)
    p.add_argument("--report-dir",type=Path)
    args=p.parse_args(argv)
    analyze(args.run_dir,report_dir=args.report_dir)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
