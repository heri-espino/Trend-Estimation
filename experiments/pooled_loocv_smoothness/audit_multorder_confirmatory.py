"""Independently audit the uploaded 160,000-base-draw multiorder aggregates.

Never re-run or read 12.8M raw method rows in CI. This audit validates
method/paired table correspondence, full 16-cell x 10000 independent-base-
draw coverage, eight matched procedures, 4 paired comparisons, completeness
manifest with all 1600 non-overlapping shards, and inferential unit.

It reports each (d,N,observation_SD,R,mu) separately; 95% Monte Carlo
intervals use *within-draw paired differences*, not erroneously the five
mu treatments or R1/R3 as independent samples. These are Monte Carlo
error bars conditional on the specified Gaussian simulator, NOT empirical
coverage guarantees for unknown financial market trends.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

from .run_nonzero_mean_multorder import (
    METHODS, MU_FACTORS, ORDERS, LENGTHS, ETA_SDS, FULL_REPLICATES,
    PAIRS, SHARD_SIZE
)

ROOT = Path("results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/audit_001")
ML = "estimated_mu_gaussian_gls_ml"
CV = "estimated_mu_fold_clean_pooled_loocv"
M0 = "zero_mu_gaussian_difference_ml"
CV0 = "zero_mu_pooled_loocv"


def _csv(path: Path) -> list[dict]:
    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        if not reader.fieldnames or not data:
            raise ValueError(f"Missing/empty CSV: {path}")
    text_fields = {"method", "first_method", "second_method"}
    return [{k:(v if k in text_fields else
                 None if v == "" else float(v)) for k, v in row.items()}
            for row in data]


def read_and_verify(root: Path = ROOT):
    manifest = json.loads((root / "campaign_manifest.json").read_text(
        encoding="utf-8"))
    methods = _csv(root / "by_d_N_eta_R_mu_method.csv")
    contrasts = _csv(root / "paired_MSE_contrasts_by_d_N_eta_R_mu.csv")
    if (manifest["status"] != "complete_10000_independent_draws_per_cell" or
        manifest["total_independent_base_R3_shock_draws"] != 160000 or
        manifest["method_level_rows_represented"] != 12800000 or
        manifest["distinct_cells_present"] != 16):
        raise ValueError("Not a complete verified 10k-per-cell campaign")
    if (len(methods) != 16*2*5*len(METHODS) or
        len(contrasts) != 16*2*5*len(PAIRS)):
        raise ValueError("Wrong method or paired aggregate coverage")
    if len(manifest["shards"]) != 1600:
        raise ValueError("Missing independent source shard provenance")
    expected = {(d,n,eta) for d in ORDERS for n in LENGTHS for eta in ETA_SDS}
    if {(x["d"], x["N"], x["sigma_eta"]) for x in manifest["counts_by_cell"]} != expected:
        raise ValueError("Incomplete factorial cells")
    if any(x["independent_seeds"] != FULL_REPLICATES
           for x in manifest["counts_by_cell"]):
        raise ValueError("A factorial cell has fewer than 10,000 seeds")
    if not manifest["source_git_sha"]:
        raise ValueError("No run source commit identifier")
    index = {}
    for record in methods:
        d,n,eta,R,mu = (
            int(record["d"]), int(record["N"]), record["sigma_eta"],
            int(record["R"]),record["mu_factor"])
        if (d,n,eta) not in expected or R not in (1,3) or mu not in MU_FACTORS:
            raise ValueError("Invalid method grouping")
        name=record["method"]
        if name not in METHODS or record["independent_base_shock_draws"]!=FULL_REPLICATES:
            raise ValueError("Wrong method or seed count")
        key=(d,n,eta,R,mu,name)
        if key in index:
            raise ValueError("Duplicate method aggregate")
        if (record["mean_latent_trend_mse"] < 0 or
            record["standard_error_latent_mse"] < 0 or
            not math.isfinite(record["mean_latent_trend_mse"])):
            raise ValueError("Invalid method-level reconstruction MSE")
        index[key]=record
    pindex={}
    for record in contrasts:
        d,n,eta,R,mu = (
            int(record["d"]), int(record["N"]), record["sigma_eta"],
            int(record["R"]),record["mu_factor"])
        first,second=record["first_method"],record["second_method"]
        key=(d,n,eta,R,mu,first,second)
        if key in pindex or (first,second) not in PAIRS:
            raise ValueError("Unrecognized or duplicate method comparison")
        if record["independent_base_shock_draws"]!=FULL_REPLICATES:
            raise ValueError("Wrong paired-sample replication count")
        if not 0<=record["second_lower_realized_MSE_count"]<=FULL_REPLICATES:
            raise ValueError("Impossible paired win count")
        if record["paired_standard_error"] < 0:
            raise ValueError("Invalid paired standard error")
        difference = (index[(d,n,eta,R,mu,first)]["mean_latent_trend_mse"] -
                      index[(d,n,eta,R,mu,second)]["mean_latent_trend_mse"])
        if not math.isclose(
                difference,record["paired_mean_MSE_first_minus_second"],
                rel_tol=1e-7,abs_tol=1e-8):
            raise ValueError(f"Paired contrast does not match method means: {key}")
        pindex[key]=record

    expected_shard_ranges=defaultdict(set)
    for item in manifest["shards"]:
        d,n,eta=item["d"],item["N"],item["sigma_eta"]
        interval=(item["replicate_start"],item["replicate_stop"])
        if (d,n,eta) not in expected or interval[1]-interval[0] != SHARD_SIZE:
            raise ValueError("Unexpected source shard size/cell")
        if not 0 <= interval[0]<interval[1]<=FULL_REPLICATES:
            raise ValueError("Bad seed interval")
        if interval in expected_shard_ranges[(d,n,eta)]:
            raise ValueError("Duplicate source seed interval")
        if not item["csv_sha256"] or len(item["csv_sha256"])!=64:
            raise ValueError("Missing SHA256 source provenance")
        expected_shard_ranges[(d,n,eta)].add(interval)
    required_ranges={(i,i+SHARD_SIZE)
                     for i in range(0,FULL_REPLICATES,SHARD_SIZE)}
    if set(expected_shard_ranges)!=expected or any(
            intervals!=required_ranges for intervals in expected_shard_ranges.values()):
        raise ValueError("Overlapping or missing source seed intervals")
    return manifest,index,pindex


def infer(index: dict, comparisons: dict, R: int = 3) -> list[dict]:
    result=[]
    for d in ORDERS:
        for n in LENGTHS:
            for eta in ETA_SDS:
                for mu in MU_FACTORS:
                    base=(d,n,eta,R,mu)
                    def score(name):
                        return index[(*base,name)]["mean_latent_trend_mse"]
                    def paired(first,second):
                        return comparisons[(*base,first,second)]
                    a=paired(M0,ML)
                    b=paired(CV0,CV)
                    c=paired(ML,CV)
                    p=paired("pooled_guerrero_plugin_mu_plus_gaussian_ml",ML)
                    def ci(x):
                        center=x["paired_mean_MSE_first_minus_second"]
                        se=x["paired_standard_error"]
                        return center-1.96*se,center+1.96*se
                    result.append({
                        "d":d,"N":n,"sigma_eta":eta,"R":R,
                        "mu_over_sigma_epsilon":mu,
                        "n_independent_base_shock_draws":FULL_REPLICATES,
                        "oracle_true_MSE":score("known_mu_true_ratio_oracle"),
                        "zero_mu_ML_MSE":score(M0),
                        "zero_mu_CV_MSE":score(CV0),
                        "estimated_mu_GLS_ML_MSE":score(ML),
                        "estimated_mu_fold_clean_CV_MSE":score(CV),
                        "pooled_guerrero_plugin_ML_MSE":score(
                            "pooled_guerrero_plugin_mu_plus_gaussian_ml"),
                        "misspecified_mu_ML_MSE_penalty":a["paired_mean_MSE_first_minus_second"],
                        "misspecified_mu_ML_MSE_penalty_SE":a["paired_standard_error"],
                        "misspecified_mu_ML_ci95_low":ci(a)[0],
                        "misspecified_mu_ML_ci95_high":ci(a)[1],
                        "misspecified_mu_CV_MSE_penalty":b["paired_mean_MSE_first_minus_second"],
                        "misspecified_mu_CV_MSE_penalty_SE":b["paired_standard_error"],
                        "misspecified_mu_CV_ci95_low":ci(b)[0],
                        "misspecified_mu_CV_ci95_high":ci(b)[1],
                        "GLS_ML_minus_CV_MSE":c["paired_mean_MSE_first_minus_second"],
                        "GLS_ML_minus_CV_SE":c["paired_standard_error"],
                        "GLS_ML_minus_CV_ci95_low":ci(c)[0],
                        "GLS_ML_minus_CV_ci95_high":ci(c)[1],
                        "CV_lower_realized_MSE_count":c["second_lower_realized_MSE_count"],
                        "plugin_minus_GLS_ML_MSE":p["paired_mean_MSE_first_minus_second"],
                        "plugin_minus_GLS_ML_SE":p["paired_standard_error"],
                    })
    return result


def _write_csv(path: Path, records: list[dict]) -> None:
    with path.open("w",newline="",encoding="utf-8") as file:
        writer=csv.DictWriter(file,fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def summary(rows: list[dict],manifest:dict):
    main=[x for x in rows if x["mu_over_sigma_epsilon"] == 1 and x["R"]==3]
    if len(main)!=16:
        raise ValueError("Expected 16 R3 primary cells")
    return {
        "status":"independently_audited_complete_gaussian_confirmatory",
        "source_git_sha":manifest["source_git_sha"],
        "independent_R3_base_shock_draws":160000,
        "experimental_unit":"one R3 shock pool per (d,N,eta,replicate)",
        "independent_draws_per_cell":10000,
        "full_method_records_represented":12800000,
        "primary_R3_mu_plus_1_cells":16,
        "primary_R3_mu_plus_1_cells_GLS_ML_lower_mean_MSE":sum(
            x["GLS_ML_minus_CV_MSE"] < 0 for x in main),
        "primary_R3_mu_plus_1_cells_CV_lower_mean_MSE":sum(
            x["GLS_ML_minus_CV_MSE"] > 0 for x in main),
        "primary_R3_mu_plus_1_cells_where_forced_zero_mu_Gaussian_penalty_exceeds_abs_ML_CV_gap":
            sum(x["misspecified_mu_ML_MSE_penalty"] >
                abs(x["GLS_ML_minus_CV_MSE"]) for x in main),
        "primary_R3_mu_plus_1_cells_where_misspecification_cost_95CI_excludes_zero":
            sum(x["misspecified_mu_ML_ci95_low"] > 0 and
                x["misspecified_mu_CV_ci95_low"] > 0 for x in main),
        "warnings":[
            "95% Monte Carlo intervals use within-seed paired loss SE and normal approximation; conditional on the specified Gaussian DGP, not market data.",
            "Five mu treatments and nested R are NOT statistically independent extra seeds.",
            "Analyst fixes and matches d in DGP and smoother; cross-d MSE is not order selection.",
            "Data-confirmed Gaussian dominance is not a claim of uniform non-Gaussian optimality.",
            "For R=1, both misspecification patterns and ML versus CV comparisons differ: inspect disaggregated tables.",
            "Guerrero already allows nonzero difference mean; pooled plug-in + variance ML is our hybrid.",
            "Only compact original aggregate files are on GitHub; source gzip shards stay local, verified by user-run digest aggregation.",
        ]
    }


def execute(root:Path=ROOT, output:Path|None=None):
    manifest,index,comparisons=read_and_verify(root)
    r3=infer(index,comparisons,R=3)
    r1=infer(index,comparisons,R=1)
    report=summary(r3,manifest)
    if output is not None:
        if output.exists():
            raise FileExistsError(f"Refusing to overwrite {output}")
        output.mkdir(parents=True,exist_ok=False)
        _write_csv(output/"R3_with_paired_95pct_CIs.csv",r3)
        _write_csv(output/"R1_with_paired_95pct_CIs.csv",r1)
        (output/"audit_summary.json").write_text(
            json.dumps(report,indent=2)+"\n",encoding="utf-8")
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,default=ROOT)
    p.add_argument("--out-dir",type=Path,default=None)
    args=p.parse_args()
    result=execute(args.root,args.out_dir)
    print(json.dumps(result,indent=2))


if __name__=="__main__":
    main()
