"""PLAN ONLY by default; manually launch resumable non-Gaussian mu-shift shards.

Finite-variance distributions only, excluding Cauchy. A pilot of 25
independent shocks per (regime,d,N,eta) is the preflight stage;
10k fresh/unique seeds per cell is a separate large confirmatory stage.
The two phases have non-overlapping paths and seed indices.

No automatic work after git push. '--execute' explicitly starts CPU jobs.
Matching completed shards (source SHA plus file SHA256) are reused; wrong
source, incomplete files and overlapping intervals STOP rather than overwrite.
32 workers are permitted but memory and CPU oversubscription are user-managed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from .run_nonzero_mu_nongaussian import (
    FINITE_REGIMES, ORDERS, LENGTHS, ETA_SDS,
    NoiseShard, PILOT_REPS, CONFIRMATORY_REPS, PROTOCOL,
    calculate_shard, design, _sha,
)

DEFAULT_ROOT = Path("results/pooled_loocv_smoothness/guerrero/nonzero_mu_nongaussian")


def plan(*,phase="pilot",regimes=FINITE_REGIMES,ds=ORDERS,
         ns=LENGTHS,noise_sds=ETA_SDS,seed_start=0,seed_stop=None,
         shard_size=None):
    total=PILOT_REPS if phase=="pilot" else CONFIRMATORY_REPS if phase=="confirmatory" else None
    if total is None:raise ValueError("invalid phase")
    if seed_stop is None:seed_stop=total
    if shard_size is None:shard_size=25 if phase=="pilot" else 100
    if not 0<=seed_start<seed_stop<=total or not 1<=shard_size<=total:
        raise ValueError("bad seed interval or shard size")
    return [
        NoiseShard(regime,d,n,eta,start,min(shard_size,seed_stop-start),phase)
        for regime in regimes for d in ds for n in ns for eta in noise_sds
        for start in range(seed_start,seed_stop,shard_size)
    ]


def file_sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()


def _metadata(shard:NoiseShard):
    return (shard.regime,shard.d,shard.n,shard.sigma_eta,
            shard.start,shard.start+shard.count)


def _run_one(item):
    shard,root,sha=item
    target=root/shard.phase/shard.suffix
    if target.exists():
        mf=target/"manifest.json"
        if not mf.is_file():
            raise RuntimeError(f"Interrupted shard, inspect or move: {target}")
        meta=json.loads(mf.read_text(encoding="utf-8"))
        if (meta.get("protocol")!=PROTOCOL or
            meta.get("source_git_sha")!=sha or
            meta.get("status")!="executed_shard" or
            meta.get("phase")!=shard.phase or
            meta.get("regime")!=shard.regime or
            meta.get("difference_order_fixed")!=shard.d or
            meta.get("N")!=shard.n or
            meta.get("sigma_eta_population_SD")!=shard.sigma_eta or
            meta.get("seed_start_inclusive")!=shard.start or
            meta.get("seed_stop_exclusive")!=shard.start+shard.count or
            meta.get("actual_method_rows")!=shard.rows):
            raise RuntimeError(f"Existing shard differs from requested protocol: {target}")
        zipped=target/"method_comparison.csv.gz"
        if (not zipped.is_file() or
            zipped.stat().st_size!=meta["compressed_csv_bytes"] or
            file_sha(zipped)!=meta["compressed_csv_sha256"] or
            not (target/"summary.json").is_file()):
            raise RuntimeError(f"Missing/corrupted compressed output: {target}")
        return "verified_existing",str(target)
    calculate_shard(shard,target)
    return "new_completed",str(target)


def execute(jobs:list[NoiseShard],root:Path,workers=1):
    if not jobs or workers<1:raise ValueError("no jobs or invalid worker count")
    sha=_sha()
    if not sha:raise RuntimeError("Must execute in a Git checkout with a source SHA")
    phase=jobs[0].phase
    if any(j.phase!=phase for j in jobs):
        raise ValueError("do not mix pilot and confirmatory in same request")
    # Pre-check every already-committed interval in requested phase, not
    # just the exact target folder. E.g. [0,2) preflight vs [0,25) pilot.
    wanted=defaultdict(list)
    for job in jobs:
        wanted[_metadata(job)[:4]].append(_metadata(job)[4:])
    existing_root=root/phase
    for path in existing_root.rglob("manifest.json") if existing_root.exists() else ():
        m=json.loads(path.read_text(encoding="utf-8"))
        if m.get("protocol")!=PROTOCOL:
            raise RuntimeError(f"Foreign protocol in results tree: {path}")
        key=(m["regime"],m["difference_order_fixed"],m["N"],m["sigma_eta_population_SD"])
        lo,hi=m["seed_start_inclusive"],m["seed_stop_exclusive"]
        for start,end in wanted.get(key,()):
            if max(lo,start)<min(hi,end) and (lo,hi)!=(start,end):
                raise RuntimeError(f"Partially overlapping seeds {path}: [{lo},{hi}) vs [{start},{end}); "
                                   "use isolated --root for preflight")
    print(json.dumps({"status":"STARTING_MANUAL_RUN","jobs":len(jobs),
        "source_git_sha":sha,"worker_processes":workers},indent=2),flush=True)
    args=((job,root,sha) for job in jobs)
    counts={"new_completed":0,"verified_existing":0}
    if workers==1:
        it=map(_run_one,args)
        for label,folder in it:
            counts[label]+=1
            print(f"[{sum(counts.values())}/{len(jobs)}] {label}: {folder}",flush=True)
        return counts
    with ProcessPoolExecutor(max_workers=workers) as pool:
        for label,folder in pool.map(_run_one,args):
            counts[label]+=1
            print(f"[{sum(counts.values())}/{len(jobs)}] {label}: {folder}",flush=True)
    return counts


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase",choices=("pilot","confirmatory"),default="pilot")
    parser.add_argument("--regime",choices=("all",)+FINITE_REGIMES,default="all")
    parser.add_argument("--d",choices=("all","1","2","3","4"),default="all")
    parser.add_argument("--n",choices=("all","50","200"),default="all")
    parser.add_argument("--sigma-eta",choices=("all","0.5","2"),default="all")
    parser.add_argument("--seed-start",type=int,default=0)
    parser.add_argument("--seed-stop",type=int)
    parser.add_argument("--shard-size",type=int)
    parser.add_argument("--workers",type=int,default=1)
    parser.add_argument("--root",type=Path,default=DEFAULT_ROOT)
    parser.add_argument("--execute",action="store_true")
    a=parser.parse_args()
    regimes=FINITE_REGIMES if a.regime=="all" else (a.regime,)
    orders=ORDERS if a.d=="all" else (int(a.d),)
    ns=LENGTHS if a.n=="all" else (int(a.n),)
    sds=ETA_SDS if a.sigma_eta=="all" else (float(a.sigma_eta),)
    jobs=plan(phase=a.phase,regimes=regimes,ds=orders,ns=ns,noise_sds=sds,
              seed_start=a.seed_start,seed_stop=a.seed_stop,shard_size=a.shard_size)
    print(json.dumps({
        "mode":"EXPLICIT_EXECUTE" if a.execute else "PLAN_ONLY",
        "phase":a.phase,"workers":a.workers,"shards":len(jobs),
        "independent_R3_base_shock_draws":sum(j.base_draws for j in jobs),
        "paired_mu_and_nested_R_treatment_pools":sum(j.pools for j in jobs),
        "per_method_rows":sum(j.rows for j in jobs),
        "source_git_sha":_sha(),"Cauchy_included":False,
        "first_jobs":[j.suffix for j in jobs[:3]],
        "root":str(a.root),
    },indent=2),flush=True)
    if a.execute:
        print(json.dumps(execute(jobs,a.root,a.workers),indent=2))


if __name__=="__main__":
    main()
