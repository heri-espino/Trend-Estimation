"""Manual parallel Study K replay with the same 25 seeds as prior Study J.

Default prints a plan ONLY. Full execution requires --execute.
One source code SHA and ONE numerical solver/search grid per root.
Resume verifies SHA256 of existing compressed CSVs; never overwrite.
Tiny [0,1) or [0,2) PREFLIGHT must be in a DIFFERENT --root than the
25-seed per-cell pilot; overlapping seed intervals are rejected.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from .run_nonzero_mu_nongaussian import (
    FINITE_REGIMES, ORDERS, LENGTHS, ETA_SDS, PILOT_REPS
)
from .run_nonzero_mean_multorder import _sha
from .run_cortes_criteria_pilot import (
    PROTOCOL, CriteriaShard, calculate_shard, DEFAULT_SOLVER,
    DEFAULT_SCAN_POINTS, ALL_METHODS
)

ROOT=Path("results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/pilot")


def plan(*,regimes=FINITE_REGIMES,ds=ORDERS,ns=LENGTHS,
         noises=ETA_SDS,start=0,stop=PILOT_REPS,shard_size=PILOT_REPS):
    if not 0<=start<stop<=PILOT_REPS or not 1<=shard_size<=PILOT_REPS:
        raise ValueError("Invalid 25-seed J pilot replay interval")
    return [CriteriaShard(reg,d,n,eta,first,min(shard_size,stop-first))
            for reg in regimes for d in ds for n in ns for eta in noises
            for first in range(start,stop,shard_size)]


def _sha256(path:Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):h.update(block)
    return h.hexdigest()


def _task(item):
    shard,root,expected_sha,solver,scan=item
    output=root/shard.suffix
    if output.exists():
        manifest_path=output/"manifest.json"
        if not manifest_path.is_file():
            raise RuntimeError(f"Interrupted shard, inspect manually: {output}")
        m=json.loads(manifest_path.read_text(encoding="utf-8"))
        if (m.get("protocol")!=PROTOCOL or
            m.get("status")!="executed_shard" or
            m.get("source_git_sha")!=expected_sha or
            m.get("regime")!=shard.regime or
            m.get("difference_order_fixed")!=shard.d or
            m.get("N")!=shard.n or
            m.get("sigma_eta_population_SD")!=shard.sigma_eta or
            m.get("seed_start_inclusive")!=shard.start or
            m.get("seed_stop_exclusive")!=shard.start+shard.count or
            m.get("search_solver")!=solver or
            m.get("search_scan_points")!=scan or
            m.get("actual_method_rows")!=shard.rows):
            raise RuntimeError(f"Incompatible completed replay shard: {output}")
        gz=output/"method_comparison.csv.gz"
        if (not gz.is_file() or
            gz.stat().st_size!=m["compressed_csv_bytes"] or
            _sha256(gz)!=m["compressed_csv_sha256"] or
            not (output/"summary.json").is_file()):
            raise RuntimeError(f"Corrupt or incomplete output: {output}")
        return ("verified_existing",str(output))
    calculate_shard(shard,output,solver=solver,scan_points=scan)
    return ("new_completed",str(output))


def execute(shards:list[CriteriaShard],root:Path,workers:int,
            solver:str,scan:int):
    if not shards or workers<1:
        raise ValueError("No shards or invalid worker count")
    sha=_sha()
    if not sha:raise RuntimeError("Must run from source-controlled checkout")
    desired=defaultdict(list)
    for sh in shards:
        desired[(sh.regime,sh.d,sh.n,sh.sigma_eta)].append((sh.start,sh.start+sh.count))
    for manifest_path in root.rglob("manifest.json") if root.exists() else ():
        m=json.loads(manifest_path.read_text(encoding="utf-8"))
        if m.get("protocol")!=PROTOCOL:raise RuntimeError(f"Foreign existing file {manifest_path}")
        key=(m["regime"],m["difference_order_fixed"],m["N"],m["sigma_eta_population_SD"])
        lo,hi=m["seed_start_inclusive"],m["seed_stop_exclusive"]
        for start,stop in desired.get(key,()):
            if max(lo,start)<min(hi,stop) and (lo,hi)!=(start,stop):
                raise RuntimeError(f"OVERLAPPING seed intervals: {manifest_path}; "
                                   "use an isolated --root for shorter preflights")
    items=((sh,root,sha,solver,scan) for sh in shards)
    counts={"new_completed":0,"verified_existing":0}
    if workers==1:
        iterator=map(_task,items)
        for status,loc in iterator:
            counts[status]+=1
            print(f"[{sum(counts.values())}/{len(shards)}] {status}: {loc}",flush=True)
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for status,loc in pool.map(_task,items):
                counts[status]+=1
                print(f"[{sum(counts.values())}/{len(shards)}] {status}: {loc}",flush=True)
    return counts


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--regime",choices=("all",)+FINITE_REGIMES,default="all")
    p.add_argument("--d",choices=("all","1","2","3","4"),default="all")
    p.add_argument("--n",choices=("all","50","200"),default="all")
    p.add_argument("--sigma-eta",choices=("all","0.5","2"),default="all")
    p.add_argument("--start",type=int,default=0)
    p.add_argument("--stop",type=int,default=PILOT_REPS)
    p.add_argument("--shard-size",type=int,default=PILOT_REPS)
    p.add_argument("--workers",type=int,default=1)
    p.add_argument("--solver",choices=("multibracket","bounded"),default=DEFAULT_SOLVER)
    p.add_argument("--scan-points",type=int,default=DEFAULT_SCAN_POINTS)
    p.add_argument("--root",type=Path,default=ROOT)
    p.add_argument("--execute",action="store_true")
    a=p.parse_args()
    jobs=plan(regimes=FINITE_REGIMES if a.regime=="all" else (a.regime,),
              ds=ORDERS if a.d=="all" else (int(a.d),),
              ns=LENGTHS if a.n=="all" else (int(a.n),),
              noises=ETA_SDS if a.sigma_eta=="all" else (float(a.sigma_eta),),
              start=a.start,stop=a.stop,shard_size=a.shard_size)
    summary={
        "mode":"EXPLICIT_EXECUTE" if a.execute else "PLAN_ONLY",
        "source_git_sha":_sha(),"workers":a.workers,
        "source":"SAME_25_J_pilot_shocks_not_new_independent_draws",
        "solver":a.solver,"scan_points":a.scan_points,
        "shards":len(jobs),"shock_draws_replayed":sum(x.shock_pools for x in jobs),
        "nested_mu_R_treatment_pools":sum(x.treatment_pools for x in jobs),
        "method_rows":sum(x.rows for x in jobs),
        "distinct_reconstruction_methods":len(ALL_METHODS),
        "root":str(a.root),"first_shards":[x.suffix for x in jobs[:3]],
    }
    print(json.dumps(summary,indent=2),flush=True)
    if a.execute:
        print(json.dumps(execute(jobs,a.root,a.workers,a.solver,a.scan_points),
                         indent=2),flush=True)


if __name__=="__main__":
    main()
