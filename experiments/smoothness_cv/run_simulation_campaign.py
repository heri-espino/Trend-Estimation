"""High-throughput, resumable Paper 1 / Paper 2 Monte Carlo campaign.

Run from repository root:
    python -m experiments.smoothness_cv.run_simulation_campaign --preset smoke --jobs 2
    python -m experiments.smoothness_cv.run_simulation_campaign --preset extensive --jobs 32

Workers use ONE BLAS/OpenMP thread each: 32 CPUs -> 32 processes, not
32 processes times 32 BLAS threads. The RTX GPU is not required for
eigendecompositions of these short/medium dense matrices.

Only the *main process* writes SQLite. Each independent scenario/seed
replication is committed atomically; a rerun resumes missing tasks
without erasing completed rows. This is a manual, long-running job,
NEVER part of routine CI or auto-paper-build.
"""
from __future__ import annotations

import os

# MUST precede numpy/scipy imports in workers (including spawned workers).
for _var in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS",
):
    os.environ[_var] = "1"

import argparse
from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
from datetime import datetime, timezone
import hashlib
from itertools import groupby
import json
import multiprocessing as mp
from pathlib import Path
import sqlite3
import subprocess
import sys
import time
import traceback

from .simulation_dgps import Scenario, grid_scenarios
from .simulation_evaluation import evaluate_replication


FIELDS = (
    "task_key", "study", "scenario", "shape", "n_obs", "noise",
    "sigma", "seasonal", "seed", "origin", "d", "L", "h",
    "selector", "is_oracle", "branch_support", "n_branches", "n_local_minima",
    "selected_s", "selected_lambda",
    "edf", "raw_guerrero_s", "forecast_mse_obs", "forecast_mae_obs",
    "forecast_mse_latent", "forecast_mse_conditional",
    "past_recovery_mse", "fit_residual_mse", "lead_squared_errors",
)
NUMERIC = {
    "n_obs", "sigma", "seasonal", "seed", "origin", "d", "L", "h",
    "is_oracle", "branch_support", "n_branches", "n_local_minima",
    "selected_s", "selected_lambda", "edf",
    "raw_guerrero_s", "forecast_mse_obs", "forecast_mae_obs",
    "forecast_mse_latent", "forecast_mse_conditional",
    "past_recovery_mse", "fit_residual_mse",
}
INTS = {"n_obs","seasonal","seed","origin","d","L","h","is_oracle",
        "branch_support","n_branches","n_local_minima"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def git_revision() -> str:
    try:
        result=subprocess.run(
            ["git","rev-parse","HEAD"],capture_output=True,text=True,
            timeout=4,check=True,
        )
        return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return "unknown"


def resolve_jobs(jobs: int) -> int:
    if jobs < 0:
        raise ValueError("jobs must be >= 0.")
    logical = os.cpu_count() or 1
    actual = min(logical,32) if jobs == 0 else jobs
    if os.name == "nt" and actual > 61:
        raise ValueError("Windows ProcessPoolExecutor supports at most 61 workers.")
    return max(actual,1)


def arguments(argv: list[str] | None = None) -> argparse.Namespace:
    p=argparse.ArgumentParser(description="Resumable CPU Monte Carlo grid for two smoothness papers.")
    p.add_argument("--preset",choices=("smoke","pilot","extensive","stress","mega","formal8h"),default="smoke")
    p.add_argument("--backend",choices=("cpu","cuda"),default="cpu",
                   help="CUDA batches PLS forecast losses across independent seeds; CPU keeps 32 workers.")
    p.add_argument("--gpu-batch-size",type=int,default=64,
                   help="Number of same-scenario Monte Carlo series per CUDA batch.")
    p.add_argument("--gpu-verify",type=int,default=0,
                   help="Optional one-time numeric audit; 0 during formal runs. Do it ONCE in a small preflight run.")
    p.add_argument("--seeds",type=int,default=None,
                   help="Independent replicates per scenario. Defaults: smoke=1,pilot=5,extensive=100.")
    p.add_argument("--seed-start",type=int,default=0)
    p.add_argument("--orders",default="2",help="Fixed continuation orders, e.g. '2' or '1,2,3,4'.")
    p.add_argument("--horizons",default="1,3,6,12")
    p.add_argument("--outer-count",type=int,default=4)
    p.add_argument("--max-folds",type=int,default=32)
    p.add_argument("--grid-points",type=int,default=None)
    p.add_argument("--jobs",type=int,default=0,
                   help="0=up to 32 logical cores; explicit --jobs 32 uses 32 processes.")
    p.add_argument("--time-budget-hours",type=float,default=None,
                   help="Soft wall-clock budget: finish current GPU/CPU task then stop; 8 for formal study.")
    p.add_argument("--seed-wave",type=int,default=8,
                   help="Round-robin blocks of seeds across studies/cells for balanced partial progress.")
    p.add_argument("--numerical-every",type=int,default=0,
                   help="Paper 3 on each K-th seed *per scenario*, 0 disabled; typical 32.")
    p.add_argument("--numerical-dense-grid",type=int,default=501,
                   help="Dense numerical reference points for sampled Paper 3 diagnostics.")
    p.add_argument("--numerical-adaptive-depth",type=int,default=6)
    p.add_argument("--max-tasks",type=int,default=None,
                   help="Execute at most N *remaining* tasks, useful for staging/resume.")
    p.add_argument("--run-dir",type=Path,default=None)
    p.add_argument("--dry-run",action="store_true",help="Show design without writing files.")
    p.add_argument("--continue-on-error",action="store_true",
                   help="Record failed tasks, continue; retries failed tasks on the next run.")
    return p.parse_args(argv)


def config_from_args(args) -> dict:
    seeds = args.seeds if args.seeds is not None else {
        "smoke":1,"pilot":5,"extensive":100,"stress":100,"mega":100,"formal8h":1000,
    }[args.preset]
    grid = args.grid_points if args.grid_points is not None else {
        "smoke":21,"pilot":61,"extensive":161,"stress":161,"mega":161,"formal8h":161,
    }[args.preset]
    order=tuple(int(part.strip()) for part in args.orders.split(",") if part.strip())
    horizon=tuple(int(part.strip()) for part in args.horizons.split(",") if part.strip())
    if seeds<1 or args.seed_start<0 or not order or not horizon:
        raise ValueError("Require positive seeds and nonempty order/horizon sets.")
    if len(set(order))!=len(order) or len(set(horizon))!=len(horizon):
        raise ValueError("Orders/horizons must not repeat.")
    if any(d < 1 or d>4 for d in order) or any(h<1 or h>24 for h in horizon):
        raise ValueError("Supported 1<=d<=4 and 1<=h<=24.")
    if grid<11 or grid>501 or args.outer_count<2 or args.max_folds<2:
        raise ValueError("Need grid 11..501, at least 2 outer origins and inner folds.")
    if args.max_tasks is not None and args.max_tasks<1:
        raise ValueError("--max-tasks must be positive.")
    if args.time_budget_hours is not None and not 0 < args.time_budget_hours <= 24*30:
        raise ValueError("Time budget must be between 0 and 720 hours.")
    if args.seed_wave<1 or args.numerical_every<0 or args.numerical_adaptive_depth<0:
        raise ValueError("Invalid seed-wave or numerical sampling/depth.")
    if not 11<=args.numerical_dense_grid<=5001:
        raise ValueError("Numerical reference grid must be 11..5001.")
    if args.numerical_every and args.numerical_dense_grid<=grid:
        raise ValueError("Paper 3 dense reference grid must exceed selection S grid.")
    if args.gpu_batch_size<1 or args.gpu_verify<0:
        raise ValueError("--gpu-batch-size must be positive and --gpu-verify nonnegative.")
    return {
        "protocol":"weighted_F_campaign_v2_cuda",
        "backend":args.backend,
        "gpu_batch_size":int(args.gpu_batch_size) if args.backend=="cuda" else None,
        "gpu_verify":int(args.gpu_verify) if args.backend=="cuda" else None,
        "gpu_kernel_dtype":"float32" if args.backend=="cuda" else "float64",
        "gpu_mode":"formal-no-cpu-rechecks" if args.backend=="cuda" and not args.gpu_verify else "audited",
        "preset":args.preset,"seeds":int(seeds),
        "seed_start":int(args.seed_start),
        "orders":order,"horizons":horizon,
        "outer_count":int(args.outer_count),
        "max_folds":int(args.max_folds),
        "grid_points":int(grid),
        "numerical_every":int(args.numerical_every),
        "numerical_dense_grid":int(args.numerical_dense_grid) if args.numerical_every else None,
        "numerical_adaptive_depth":int(args.numerical_adaptive_depth) if args.numerical_every else None,
        "scenario_keys":[s.key for s in grid_scenarios(args.preset)],
        "git_revision":git_revision(),
    }


def digest(config: dict) -> str:
    return hashlib.sha256(json.dumps(config,sort_keys=True).encode()).hexdigest()


def task_key(scenario: Scenario, seed: int) -> str:
    return f"{scenario.key}__seed{seed:06d}"


def connect_db(filename: Path) -> sqlite3.Connection:
    conn=sqlite3.connect(str(filename),timeout=90)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA busy_timeout=90000")
    columns=[]
    for field in FIELDS:
        typ="INTEGER" if field in INTS else "REAL" if field in NUMERIC else "TEXT"
        columns.append(f"{field} {typ} NOT NULL")
    conn.execute(
        f"CREATE TABLE IF NOT EXISTS outcomes ({','.join(columns)}, "
        "PRIMARY KEY(task_key,origin,d,h,selector)) WITHOUT ROWID"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS completed ("
        "task_key TEXT PRIMARY KEY, n_rows INTEGER NOT NULL, "
        "elapsed_sec REAL NOT NULL, completed_utc TEXT NOT NULL)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS failures ("
        "task_key TEXT PRIMARY KEY, message TEXT NOT NULL, occurred_utc TEXT NOT NULL)"
    )
    conn.commit()
    return conn


def _worker(task: tuple[Scenario,int,dict]) -> tuple[str,float,list[dict]]:
    scenario,seed,config=task
    begin=time.perf_counter()
    rows=evaluate_replication(
        scenario,seed,
        orders=tuple(config["orders"]),
        horizons=tuple(config["horizons"]),
        outer_count=int(config["outer_count"]),
        max_folds=int(config["max_folds"]),
        grid_points=int(config["grid_points"]),
    )
    if not rows:
        raise ValueError(f"No evaluations for {scenario.key}, seed={seed}.")
    return task_key(scenario,seed),time.perf_counter()-begin,rows


def record(conn: sqlite3.Connection,key: str,elapsed: float,rows: list[dict]):
    data=[(key,)+(tuple(row[col] for col in FIELDS[1:])) for row in rows]
    placeholders=",".join("?" for _ in FIELDS)
    with conn:
        conn.executemany(
            f"INSERT OR REPLACE INTO outcomes ({','.join(FIELDS)}) "
            f"VALUES ({placeholders})",data
        )
        conn.execute(
            "INSERT OR REPLACE INTO completed VALUES (?,?,?,?)",
            (key,len(rows),float(elapsed),utc_now()),
        )
        conn.execute("DELETE FROM failures WHERE task_key=?",(key,))


def _checked_manifest(run_dir: Path,config: dict):
    run_dir.mkdir(parents=True,exist_ok=True)
    path=run_dir/"manifest.json"
    meta={
        "fingerprint":digest(config),"configuration":config,
        "created_utc":utc_now(),
        "notes":"Pilot/large simulation; no summary implies verified superiority.",
        "hardware":(
            "One CUDA context, batched float32 PLS losses with FP64 spectral setup; "
            "CPU classical criteria, matching, refit and SQLite"
            if config["backend"]=="cuda" else
            "CPU process-level parallelism; each worker 1 BLAS thread"
        ),
        "resume":"Only atomic completed replications are skipped",
    }
    if path.exists():
        existing=json.loads(path.read_text(encoding="utf-8"))
        if existing.get("fingerprint")!=meta["fingerprint"]:
            raise ValueError(
                "Existing manifest has a different design/code version. "
                "Choose a NEW --run-dir instead of mixing incompatible results."
            )
    else:
        tmp=path.with_suffix(".tmp")
        tmp.write_text(json.dumps(meta,indent=2,ensure_ascii=False),encoding="utf-8")
        tmp.replace(path)


def balanced_seed_wave_schedule(
    scenarios: tuple[Scenario,...], first_seed: int, seed_count: int,
    *, seed_wave: int, completed: set[str]
) -> list[tuple[Scenario,int]]:
    """Balanced sequential waves rather than burning hours on earliest A cell.

    Each wave visits all four STUDIES round-robin, then the next seed
    block begins. The last interrupted wave is explicitly incomplete;
    no global CI is justified by a biased partial slice.
    """
    if seed_wave<=0 or seed_count<=0:
        raise ValueError("Positive seed_wave and seed_count required.")
    studies={kind:[s for s in scenarios if s.study==kind] for kind in ("A","B","C","D")}
    result=[]
    for begin in range(first_seed,first_seed+seed_count,seed_wave):
        stop=min(begin+seed_wave,first_seed+seed_count)
        # Interleave by study: do not use A, then all B, then all C, then D.
        max_cells=max(len(v) for v in studies.values())
        for i in range(max_cells):
            for kind in ("A","B","C","D"):
                cells=studies[kind]
                if i>=len(cells):
                    continue
                scenario=cells[i]
                for seed in range(begin,stop):
                    if task_key(scenario,seed) not in completed:
                        result.append((scenario,seed))
    return result


def main(argv: list[str] | None = None) -> int:
    args=arguments(argv)
    cfg=config_from_args(args)
    scenarios=grid_scenarios(args.preset)
    total=len(scenarios)*cfg["seeds"]
    # A deliberately generous estimate; each study has different horizons.
    approx=total*cfg["outer_count"]*len(cfg["horizons"])*len(cfg["orders"])*21
    jobs=resolve_jobs(args.jobs) if args.backend=="cpu" else 1
    print(
        f"CAMPAIGN preset={cfg['preset']} | scenarios={len(scenarios)} "
        f"seeds/scenario={cfg['seeds']} scenario-seed tasks={total:,} "
        f"| d={cfg['orders']} h={cfg['horizons']} outer={cfg['outer_count']} "
        f"grid={cfg['grid_points']} | backend={cfg['backend']} "
        f"| workers={jobs} | cuda_batch={cfg['gpu_batch_size']} "
        f"| upper-bound method-rows ~{approx:,}",flush=True,
    )
    if args.dry_run:
        for study in ("A","B","C","D"):
            cells=sum(s.study==study for s in scenarios)
            print(f"  Experiment {study}: {cells} factorial cells, {cells*cfg['seeds']:,} series.")
        return 0

    # Never initialize CUDA inside spawned CPU workers or silently fall back
    # to CPU. A CUDA-enabled torch install is required for --backend cuda.
    cuda_torch = None
    if args.backend=="cuda":
        from .cuda_simulation import require_cuda
        cuda_torch=require_cuda()
        cfg["cuda_device"]=cuda_torch.cuda.get_device_name(0)
        cfg["torch_version"]=str(cuda_torch.__version__)
        cfg["cuda_runtime"]=str(cuda_torch.version.cuda)
        print(f"CUDA active: {cfg['cuda_device']} | torch={cfg['torch_version']} "
              f"| runtime={cfg['cuda_runtime']} | one GPU context; "
              "--jobs applies to CPU backend only.",flush=True)
    run_dir=args.run_dir or Path("results/smoothness_cv")/f"campaign_{args.preset}_{args.backend}"
    _checked_manifest(run_dir,cfg)
    db=connect_db(run_dir/"outcomes.sqlite")
    completed={row[0] for row in db.execute("SELECT task_key FROM completed")}
    remaining=[
        (s,seed,cfg) for s,seed in balanced_seed_wave_schedule(
            scenarios,cfg["seed_start"],cfg["seeds"],
            seed_wave=args.seed_wave,completed=completed
        )
    ]
    if args.max_tasks is not None:
        remaining=remaining[:args.max_tasks]
    print(
        f"Saved={len(completed):,}/{total:,}; pending this invocation={len(remaining):,}; "
        f"run_dir={run_dir}",flush=True,
    )
    if not remaining:
        db.close()
        return 0

    started=time.perf_counter()
    deadline=(started+args.time_budget_hours*3600
              if args.time_budget_hours is not None else None)
    max_batch_seconds=0.
    budget_stopped=False
    def budget_allows_next():
        nonlocal budget_stopped
        if deadline is None:
            return True
        # Soft deadline: admit a new batch only while a small time
        # reserve remains; an unusually slow batch can overrun the
        # eight-hour target. Results still commit atomically.
        reserve=max(20.,1.5*max_batch_seconds)
        if time.perf_counter()+reserve < deadline:
            return True
        budget_stopped=True
        return False
    success=0
    failures=0
    update=max(1,len(remaining)//100)
    if args.backend=="cuda":
        from .cuda_simulation import gpu_batch_evaluate
        # A single CUDA context evaluates all series for a scenario in
        # contiguous seed batches. No separate CUDA worker per CPU process.
        for _scenario_key, group in groupby(remaining,key=lambda x:x[0].key):
            pending_for_scenario=list(group)
            for index in range(0,len(pending_for_scenario),args.gpu_batch_size):
                if not budget_allows_next():
                    break
                batch_start=time.perf_counter()
                batch=pending_for_scenario[index:index+args.gpu_batch_size]
                scenario=batch[0][0]
                seeds=[task[1] for task in batch]
                try:
                    output,audits=gpu_batch_evaluate(
                        scenario,seeds,
                        orders=tuple(cfg["orders"]),
                        horizons=tuple(cfg["horizons"]),
                        outer_count=cfg["outer_count"],
                        max_folds=cfg["max_folds"],
                        grid_points=cfg["grid_points"],
                        verify=cfg["gpu_verify"],torch=cuda_torch,
                    )
                    # Explicit precision checks are a ONE-TIME preflight,
                    # not repeated during the formal campaign (default 0).
                    # Write an audit log ONLY for runs that requested checks.
                    if cfg["gpu_verify"] > 0:
                        with (run_dir/"gpu_audit.jsonl").open("a",encoding="utf-8") as f:
                            f.write(json.dumps({
                                "scenario":scenario.key,"seed_first":seeds[0],
                                "seed_last":seeds[-1],"batch_size":len(seeds),
                                "checks":sum(a.checks for a in audits),
                                "max_absolute_error":max(a.maximum_absolute_error for a in audits),
                                "max_relative_error":max(a.maximum_relative_error for a in audits),
                                "different_grid_minima":sum(a.differing_minima for a in audits),
                                "max_selected_regret":max(a.selected_regret for a in audits),
                            })+"\n")
                    for seed,seconds,rows in output:
                        key=task_key(scenario,seed)
                        record(db,key,seconds,rows)
                        success+=1
                except Exception:
                    detail=traceback.format_exc()
                    for seed in seeds:
                        key=task_key(scenario,seed)
                        with db:
                            db.execute("INSERT OR REPLACE INTO failures VALUES (?,?,?)",
                                       (key,detail,utc_now()))
                        failures+=1
                    print(f"FAILED CUDA batch {scenario.key} seeds={seeds[:2]}... "
                          f"({len(seeds)} tasks)\n{detail}",file=sys.stderr,flush=True)
                    if not args.continue_on_error:
                        db.close()
                        raise
                max_batch_seconds=max(max_batch_seconds,time.perf_counter()-batch_start)
                count=success+failures
                elapsed=(time.perf_counter()-started)/60
                print(f"[{count:,}/{len(remaining):,}] CUDA batches "
                      f"ok={success:,} fail={failures:,} "
                      f"elapsed={elapsed:.1f} min",flush=True)
            if budget_stopped:
                break
    elif jobs==1:
        for task in remaining:
            if not budget_allows_next():
                break
            batch_start=time.perf_counter()
            key=task_key(task[0],task[1])
            try:
                k,seconds,rows=_worker(task)
                record(db,k,seconds,rows)
                success+=1
            except Exception:
                failures+=1
                detail=traceback.format_exc()
                with db:
                    db.execute("INSERT OR REPLACE INTO failures VALUES (?,?,?)",(key,detail,utc_now()))
                print(f"FAILED {key}\n{detail}",file=sys.stderr,flush=True)
                if not args.continue_on_error:
                    db.close()
                    raise
            max_batch_seconds=max(max_batch_seconds,time.perf_counter()-batch_start)
            if (success+failures)%update==0:
                elapsed=(time.perf_counter()-started)/60
                print(f"[{success+failures}/{len(remaining)}] complete={success}, "
                      f"failed={failures}, elapsed={elapsed:.1f} min",flush=True)
    else:
        # The CPU worker pool can have in-flight jobs after a soft budget
        # expires. Limit new submissions; completed in-flight jobs are kept.
        # Bounded queue: do not submit 50,000 futures at once or hold all
        # generated Monte Carlo outcomes in RAM. Windows-safe spawn.
        iterable=iter(remaining)
        capacity=jobs*2
        with ProcessPoolExecutor(max_workers=jobs,mp_context=mp.get_context("spawn")) as pool:
            pending={}
            def submit_one() -> bool:
                if not budget_allows_next():
                    return False
                try:
                    task=next(iterable)
                except StopIteration:
                    return False
                pending[pool.submit(_worker,task)]=task_key(task[0],task[1])
                return True
            for _ in range(capacity):
                if not submit_one():
                    break
            while pending:
                done,_=wait(pending,return_when=FIRST_COMPLETED)
                for future in done:
                    key=pending.pop(future)
                    try:
                        completed_key,seconds,rows=future.result()
                        if completed_key!=key:
                            raise RuntimeError("Returned task key does not match.")
                        record(db,key,seconds,rows)
                        success+=1
                    except Exception:
                        failures+=1
                        detail=traceback.format_exc()
                        with db:
                            db.execute(
                                "INSERT OR REPLACE INTO failures VALUES (?,?,?)",
                                (key,detail,utc_now()),
                            )
                        print(f"FAILED {key}\n{detail}",file=sys.stderr,flush=True)
                        if not args.continue_on_error:
                            for item in pending:
                                item.cancel()
                            db.close()
                            raise
                    submit_one()
                    count=success+failures
                    if count%update==0 or count==len(remaining):
                        elapsed=(time.perf_counter()-started)/60
                        print(f"[{count:,}/{len(remaining):,}] ok={success:,} "
                              f"fail={failures:,} elapsed={elapsed:.1f}min",flush=True)
    count_final=int(db.execute("SELECT COUNT(*) FROM completed").fetchone()[0])
    final_status={
        "status":"budget_exhausted_partial" if budget_stopped else
                 "complete" if count_final==total else "partial_invocation",
        "backend":cfg["backend"],"preset":cfg["preset"],
        "finished_task_count":count_final,"expected_task_count":total,
        "remaining":total-count_final,
        "elapsed_seconds":time.perf_counter()-started,
        "time_budget_hours":args.time_budget_hours,
        "numerical_every":cfg["numerical_every"],
        "timestamp_utc":utc_now(),
        "note":"Incomplete waves are exploratory and MUST NOT be called confirmatory.",
    }
    (run_dir/"run_status.json").write_text(
        json.dumps(final_status,indent=2),encoding="utf-8"
    )
    print(f"Finished invocation: {final_status['status']} "
          f"completed={count_final:,}/{total:,} "
          f"elapsed={final_status['elapsed_seconds']/3600:.2f} h; "
          f"data={run_dir/'outcomes.sqlite'}",flush=True)
    db.close()
    return 0 if not failures else 1


if __name__=="__main__":
    raise SystemExit(main())
