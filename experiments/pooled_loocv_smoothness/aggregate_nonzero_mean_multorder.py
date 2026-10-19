"""Audit and aggregate immutable Monte Carlo shards without loading 12.8M rows.

Shard summaries preserve within-seed paired MSE differences and their
sample variance. Independent units are d/N/eta/seed R3 shock draws,
not the five mu shifts or the nested R1 observations.
Only a COMPLETE 10k-seed set for ALL 16 (d,N,eta) cells can be
labelled complete; missing shards yield exploratory/incomplete labels.

Do not overwrite raw snapshots or infer statistical significance from
pooled counts across different d, N, observation noise, mu or R.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

from .run_nonzero_mean_multorder import (
    ORDERS, LENGTHS, ETA_SDS, FULL_REPLICATES, MU_FACTORS, METHODS, PAIRS
)


def _merge(records: list[dict], *, mean_key: str, sd_key: str,
           count_key: str):
    n=sum(int(x[count_key]) for x in records)
    if n <= 0:
        raise ValueError("empty aggregation")
    mu=sum(int(x[count_key])*float(x[mean_key]) for x in records)/n
    if n==1:
        sd=None
    else:
        within=sum(
            (int(x[count_key])-1)*float(x[sd_key])**2
            for x in records if x[sd_key] is not None)
        between=sum(
            int(x[count_key])*(float(x[mean_key])-mu)**2 for x in records)
        sd=((within+between)/(n-1))**.5
    return n,mu,sd


def _sha256(path:Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()


def collect(root:Path, *, check_csv_digest:bool=False):
    manifests=sorted(root.rglob("manifest.json"))
    if not manifests:
        raise FileNotFoundError(f"No generated shards under {root}")
    seen_seeds=set()
    sha_sources=set()
    summary_groups={}
    paired_groups={}
    per_stratum={}
    all_artifacts=[]
    for path in manifests:
        m=json.loads(path.read_text(encoding="utf-8"))
        if m.get("protocol")!="nonzero_difference_mean_multorder_confirmatory_v1":
            raise ValueError(f"Wrong experiment protocol: {path}")
        if m.get("status")!="executed_shard":
            raise ValueError(f"Unfinished shard: {path}")
        d,n,eta=(m["difference_order_fixed"],m["N"],m["sigma_eta"])
        if d not in ORDERS or n not in LENGTHS or eta not in ETA_SDS:
            raise ValueError("Unknown factorial cell")
        start,stop=m["seed_start_inclusive"],m["seed_stop_exclusive"]
        if not 0<=start<stop<=FULL_REPLICATES:
            raise ValueError("Invalid seed interval")
        if m["expected_independent_base_draws"]!=stop-start:
            raise ValueError("Seed count mismatch")
        if m["actual_method_rows"] != ((stop-start)*2*len(MU_FACTORS)*len(METHODS)):
            raise ValueError("Wrong per-shard row count")
        artifact=path.parent/"method_comparison.csv.gz"
        if not artifact.is_file() or artifact.stat().st_size!=m["compressed_csv_bytes"]:
            raise ValueError(f"Missing/incomplete compressed CSV: {artifact}")
        if check_csv_digest and _sha256(artifact)!=m["compressed_csv_sha256"]:
            raise ValueError(f"Compressed CSV checksum mismatch: {artifact}")
        for rep in range(start,stop):
            key=(d,n,eta,rep)
            if key in seen_seeds:
                raise ValueError(f"OVERLAPPING independent seed: {key}")
            seen_seeds.add(key)
        sha_sources.add(m["source_git_sha"])
        cell=(d,n,eta)
        per_stratum[cell]=per_stratum.get(cell,0)+(stop-start)
        data=json.loads((path.parent/"summary.json").read_text(encoding="utf-8"))
        if data.get("status")!="completed_shard":
            raise ValueError("Missing completed-shard summary")
        if len(data["by_R_mu_method"])!=2*len(MU_FACTORS)*len(METHODS):
            raise ValueError("Incomplete method summary")
        if len(data["paired_R_mu_method_contrasts"])!=2*len(MU_FACTORS)*len(PAIRS):
            raise ValueError("Incomplete paired summaries")
        for row in data["by_R_mu_method"]:
            key=(d,n,eta,row["R"],row["mu_factor"],row["method"])
            summary_groups.setdefault(key,[]).append(row)
        for row in data["paired_R_mu_method_contrasts"]:
            key=(d,n,eta,row["R"],row["mu_factor"],
                 row["first_method"],row["second_method"])
            paired_groups.setdefault(key,[]).append(row)
        all_artifacts.append({
            "manifest":str(path.relative_to(root)),
            "compressed_csv":str(artifact.relative_to(root)),
            "csv_sha256":m["compressed_csv_sha256"],
            "replicate_start":start,"replicate_stop":stop,
            "d":d,"N":n,"sigma_eta":eta,
        })
    if len(sha_sources)!=1 or None in sha_sources:
        raise ValueError(
            "Cannot combine data produced under different or unidentified code commits")
    expected_cells={(d,n,eta) for d in ORDERS for n in LENGTHS for eta in ETA_SDS}
    full=(set(per_stratum)==expected_cells and
          all(per_stratum[key]==FULL_REPLICATES for key in expected_cells))
    method_rows=[]
    for (d,n,eta,R,mu,method),rows in sorted(summary_groups.items()):
        reps,m,sd=_merge(rows,mean_key="mean_latent_trend_mse",
                         sd_key="sample_sd_latent_mse",
                         count_key="independent_base_shock_draws")
        wt=lambda field:sum(
            x[field]*x["independent_base_shock_draws"] for x in rows)/reps
        method_rows.append({
            "d":d,"N":n,"sigma_eta":eta,"R":R,"mu_factor":mu,
            "method":method,"independent_base_shock_draws":reps,
            "mean_latent_trend_mse":m,
            "sample_sd_latent_mse":sd,
            "standard_error_latent_mse":None if sd is None else sd/reps**.5,
            "mean_absolute_latent_error":wt("mean_absolute_latent_error"),
            "mean_absolute_mu_estimation_error":wt("mean_absolute_mu_estimation_error"),
            "infinite_lambda_count":sum(x["infinite_lambda_count"] for x in rows)
        })
    paired_rows=[]
    for (d,n,eta,R,mu,first,second),rows in sorted(paired_groups.items()):
        reps,mean,sd=_merge(rows,mean_key="mean_paired_MSE_first_minus_second",
                             sd_key="sample_sd_paired_difference",
                             count_key="independent_base_shock_draws")
        paired_rows.append({
            "d":d,"N":n,"sigma_eta":eta,"R":R,"mu_factor":mu,
            "first_method":first,"second_method":second,
            "independent_base_shock_draws":reps,
            "paired_mean_MSE_first_minus_second":mean,
            "sample_sd_paired_difference":sd,
            "paired_standard_error":None if sd is None else sd/reps**.5,
            "second_lower_realized_MSE_count":
                sum(x["second_lower_MSE_count"] for x in rows)
        })
    report={
        "protocol":"nonzero_difference_mean_multorder_confirmatory_v1",
        "status":("complete_10000_independent_draws_per_cell"
                  if full else "INCOMPLETE_EXPLORATORY_DO_NOT_CLAIM_CONFIRMATION"),
        "source_git_sha":next(iter(sha_sources)),
        "total_independent_base_R3_shock_draws":len(seen_seeds),
        "distinct_cells_present":len(per_stratum),
        "required_cells":len(expected_cells),
        "expected_replicates_per_cell":FULL_REPLICATES,
        "counts_by_cell":[{"d":d,"N":n,"sigma_eta":eta,
                           "independent_seeds":per_stratum.get((d,n,eta),0)}
                          for d,n,eta in sorted(expected_cells)],
        "method_level_rows_represented":len(seen_seeds)*2*len(MU_FACTORS)*len(METHODS),
        "individual_methods":list(METHODS),
        "paired_comparisons":[list(pair) for pair in PAIRS],
        "shards":all_artifacts,
        "statistical_warning":"Within a fixed d/N/eta/mu/R stratum, unique independent base seeds give paired MSE differences. Values for five mu shifts and nested R cannot be treated as independent. Never average raw MSE across d without controlling signal scale.",
    }
    return report,method_rows,paired_rows


def _save_csv(path:Path, rows:list[dict]):
    if not rows:
        raise ValueError("No statistics to write")
    with path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)


def execute(root:Path,out:Path,*,require_complete=False,check_csv_digest=False):
    report,methods,pairs=collect(root,check_csv_digest=check_csv_digest)
    if require_complete and not report["status"].startswith("complete_"):
        raise ValueError("Cannot mark or export an incomplete campaign as confirmation")
    if out.exists():
        raise FileExistsError("Aggregate directory exists; do not overwrite analysis")
    out.mkdir(parents=True)
    (out/"campaign_manifest.json").write_text(
        json.dumps(report,indent=2)+"\n",encoding="utf-8")
    _save_csv(out/"by_d_N_eta_R_mu_method.csv",methods)
    _save_csv(out/"paired_MSE_contrasts_by_d_N_eta_R_mu.csv",pairs)
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,default=Path(
        "results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/confirmatory"))
    p.add_argument("--out-dir",type=Path,required=True)
    p.add_argument("--require-complete",action="store_true")
    p.add_argument("--verify-digests",action="store_true")
    args=p.parse_args()
    report=execute(args.root,args.out_dir,
                   require_complete=args.require_complete,
                   check_csv_digest=args.verify_digests)
    print(json.dumps({k:report[k] for k in (
        "status","total_independent_base_R3_shock_draws","distinct_cells_present",
        "method_level_rows_represented")},indent=2))


if __name__=="__main__":
    main()
