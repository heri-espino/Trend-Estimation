"""Plan or EXPLICITLY launch distributed 10k-seed/d,N,noise MC shards.

DEFAULT IS DRY PLAN; no simulations. --execute is mandatory to launch
large runs. --workers controls parallel process count. Process pools
reuse cached PLS/contrast eigenbases over many shards per worker.

Existing completed shards are skipped after source-manifest and SHA256
verification. Incomplete/corrupt directories fail rather than overwrite:
investigate/rename that specific shard yourself before continuing.
This launcher never writes to Git, makes PRs, or auto-runs in CI.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from .run_nonzero_mean_multorder import (
    ORDERS, LENGTHS, ETA_SDS, FULL_REPLICATES,
    SHARD_SIZE, Shard, calculate_shard, _sha
)


def plan(orders=ORDERS, lengths=LENGTHS, noises=ETA_SDS,
         seed_start=0, seed_stop=FULL_REPLICATES, shard_size=SHARD_SIZE):
    if not 0<=seed_start<seed_stop<=FULL_REPLICATES or not 1<=shard_size<=FULL_REPLICATES:
        raise ValueError("invalid independent seed range or shard size")
    return [
        Shard(d,n,eta,st,min(shard_size,seed_stop-st))
        for d in orders for n in lengths for eta in noises
        for st in range(seed_start,seed_stop,shard_size)
    ]


def _hash_file(path:Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):
            h.update(block)
    return h.hexdigest()


def _run_one(item):
    shard,root,expected_sha=item
    target=root/shard.suffix
    if target.exists():
        marker=target/"manifest.json"
        if not marker.is_file():
            raise RuntimeError(f"Incomplete shard directory, inspect manually: {target}")
        manifest=json.loads(marker.read_text(encoding="utf-8"))
        if (manifest.get("status")!="executed_shard" or
            manifest.get("source_git_sha")!=expected_sha or
            manifest.get("difference_order_fixed")!=shard.order or
            manifest.get("N")!=shard.n or
            manifest.get("sigma_eta")!=shard.sigma_eta or
            manifest.get("seed_start_inclusive")!=shard.start or
            manifest.get("seed_stop_exclusive")!=shard.start+shard.count or
            manifest.get("actual_method_rows")!=shard.rows):
            raise RuntimeError(f"Existing shard provenance mismatch: {target}")
        csv_path=target/"method_comparison.csv.gz"
        if (not csv_path.is_file() or
            csv_path.stat().st_size!=manifest["compressed_csv_bytes"] or
            _hash_file(csv_path)!=manifest["compressed_csv_sha256"]):
            raise RuntimeError(f"Corrupt prior shard; do not silently replace: {target}")
        return "verified_existing",str(target)
    calculate_shard(shard,target)
    return "new_completed",str(target)


def execute(jobs:list[Shard],root:Path,workers:int):
    if workers<1:
        raise ValueError("workers must be >=1")
    sha=_sha()
    if not sha:
        raise ValueError("Run from a git checkout to capture exact source code SHA")
    if workers==1:
        values=map(_run_one,((s,root,sha) for s in jobs))
    else:
        pool=ProcessPoolExecutor(max_workers=workers)
        try:
            values=pool.map(_run_one,((s,root,sha) for s in jobs))
            counts={"new_completed":0,"verified_existing":0}
            for state,folder in values:
                counts[state]+=1
                print(f"[{sum(counts.values())}/{len(jobs)}] {state}: {folder}",flush=True)
            return counts
        finally:
            pool.shutdown(wait=True)
    counts={"new_completed":0,"verified_existing":0}
    for state,folder in values:
        counts[state]+=1
        print(f"[{sum(counts.values())}/{len(jobs)}] {state}: {folder}",flush=True)
    return counts


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--d",choices=("all","1","2","3","4"),default="all")
    p.add_argument("--n",choices=("all","50","200"),default="all")
    p.add_argument("--sigma-eta",choices=("all","0.5","2"),default="all")
    p.add_argument("--seed-start",type=int,default=0)
    p.add_argument("--seed-stop",type=int,default=FULL_REPLICATES)
    p.add_argument("--shard-size",type=int,default=SHARD_SIZE)
    p.add_argument("--workers",type=int,default=1)
    p.add_argument("--execute",action="store_true")
    p.add_argument("--root",type=Path,default=Path(
        "results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/confirmatory"))
    args=p.parse_args()
    ds=ORDERS if args.d=="all" else (int(args.d),)
    ns=LENGTHS if args.n=="all" else (int(args.n),)
    etas=ETA_SDS if args.sigma_eta=="all" else (float(args.sigma_eta),)
    jobs=plan(ds,ns,etas,args.seed_start,args.seed_stop,args.shard_size)
    info={
        "mode":"EXPLICIT_EXECUTE" if args.execute else "PLAN_ONLY_NO_SIMULATIONS",
        "shards":len(jobs),"independent_base_R3_draws":sum(j.count for j in jobs),
        "nested_treatment_pools":sum(j.groups for j in jobs),
        "per_method_rows":sum(j.rows for j in jobs),
        "worker_processes":args.workers,"source_sha":_sha(),
        "first_shards":[j.suffix for j in jobs[:5]],
        "root":str(args.root),
    }
    print(json.dumps(info,indent=2),flush=True)
    if args.execute:
        counts=execute(jobs,args.root,args.workers)
        print(json.dumps(counts,indent=2))
    return info


if __name__=="__main__":
    main()
