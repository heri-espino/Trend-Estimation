"""Read-only independent verification of uploaded Study J compact pilot outputs.

NO raw 384k-record rerun. GitHub retains 15,360 method × cell means and
7,680 paired contrasts, corresponding to 25 independent shock streams per
192 base distribution/order/N/noise cells. The 5 mu shifts and R1 nested
in R3 do NOT provide independent extra Monte Carlo repetitions.

The original user-side aggregator verified the 192 compressed CSV
SHA256s. This independent audit verifies the compact uploaded material,
its seed-range manifest, all cell/method coverage, arithmetic agreement
of paired contrasts with mean-MSE results, and t3 moment warnings. It
cannot verify raw shard bytes which remain outside Git.

Normal-Monte-Carlo 95% MSE confidence intervals are NOT certified for
Student-t3 laws (infinite fourth moments). Even for finite-fourth-moment
regimes, 25 independent seeds per cell is EXPLORATORY.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

from .run_nonzero_mu_nongaussian import (
    FINITE_REGIMES, HEAVY_FOURTH, PROTOCOL, PILOT_REPS
)
from .run_nonzero_mean_multorder import (
    ORDERS, LENGTHS, ETA_SDS, MU_FACTORS, METHODS, PAIRS
)

ROOT=Path("results/pooled_loocv_smoothness/guerrero/nonzero_mu_nongaussian/audit_pilot_001")
ML="estimated_mu_gaussian_gls_ml"
CV="estimated_mu_fold_clean_pooled_loocv"
ZERO_ML="zero_mu_gaussian_difference_ml"
ZERO_CV="zero_mu_pooled_loocv"
PLUGIN="pooled_guerrero_plugin_mu_plus_gaussian_ml"
ORACLE="known_mu_true_ratio_oracle"


def _load(path):
    with path.open("r",newline="",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        rows=list(reader)
        if not rows:raise ValueError(f"Missing data: {path}")
    text={"regime","method","first_method","second_method","SE_interpretation"}
    return [{k:(v if k in text else None if v=="" else float(v))
             for k,v in x.items()} for x in rows]


def verify(root=ROOT):
    manifest=json.loads((root/"campaign_manifest.json").read_text(encoding="utf-8"))
    expected={(law,d,n,eta) for law in FINITE_REGIMES
              for d in ORDERS for n in LENGTHS for eta in ETA_SDS}
    if (manifest["protocol"]!=PROTOCOL or
        manifest["status"]!="COMPLETE_PILOT" or
        manifest["phase"]!="pilot" or
        manifest["strata_expected"]!=192 or
        manifest["strata_present"]!=192 or
        manifest["target_seed_count_per_cell"]!=PILOT_REPS or
        manifest["independent_base_R3_shock_draws_present"]!=4800 or
        manifest["method_level_rows_represented"]!=384000 or
        not manifest["source_git_sha"]):
        raise ValueError("Campaign incomplete or incompatible with pilot")
    if {(x["regime"],x["d"],x["N"],x["sigma_eta"])
        for x in manifest["by_cell"]}!=expected or any(
        x["independent_shock_draws"]!=PILOT_REPS for x in manifest["by_cell"]):
        raise ValueError("Expected 25 independent shock streams per base cell")

    if len(manifest["shards"])!=192:
        raise ValueError("Missing original gzip shard provenance")
    seen=set()
    for x in manifest["shards"]:
        key=(x["regime"],x["d"],x["N"],x["sigma_eta"])
        if key not in expected or key in seen:
            raise ValueError("Invalid or duplicate shard cell")
        if (x["first"]!=0 or x["last"]!=PILOT_REPS or
            len(x["compressed_csv_sha256"])!=64):
            raise ValueError("Wrong shock interval or missing compressed checksum")
        seen.add(key)
    if seen!=expected:
        raise ValueError("Not all raw source cells recorded")

    methods=_load(root/"by_regime_d_N_eta_R_mu_method.csv")
    pairs=_load(root/"paired_by_regime_d_N_eta_R_mu.csv")
    if len(methods)!=192*2*5*8 or len(pairs)!=192*2*5*4:
        raise ValueError("Incomplete method or paired aggregate coverage")

    indexed={}
    for x in methods:
        cell=(x["regime"],int(x["d"]),int(x["N"]),x["sigma_eta"])
        if (cell not in expected or int(x["R"]) not in (1,3) or
            x["mu_factor"] not in MU_FACTORS or
            x["method"] not in METHODS or
            x["independent_base_shock_draws"]!=PILOT_REPS):
            raise ValueError("Malformed method grouping")
        key=(*cell,int(x["R"]),x["mu_factor"],x["method"])
        if key in indexed:raise ValueError("Duplicate method in cell")
        if (x["mean_realized_latent_MSE"]<0 or
            not math.isfinite(x["mean_realized_latent_MSE"]) or
            (x["diagnostic_SE_of_MSE_NOT_VALID_for_t3"] is not None and
             not math.isfinite(x["diagnostic_SE_of_MSE_NOT_VALID_for_t3"]))):
            raise ValueError("Invalid realized latent MSE")
        warning=x["SE_interpretation"].startswith("not_valid_normal_")
        if warning!=(x["regime"] in HEAVY_FOURTH):
            raise ValueError("Wrong Student-t3 fourth-moment warning")
        indexed[key]=x
    pindex={}
    max_difference=0.0
    for x in pairs:
        cell=(x["regime"],int(x["d"]),int(x["N"]),x["sigma_eta"])
        R,mu=int(x["R"]),x["mu_factor"]
        a,b=x["first_method"],x["second_method"]
        if (cell not in expected or R not in (1,3) or
            mu not in MU_FACTORS or (a,b) not in PAIRS or
            x["independent_base_shock_draws"]!=PILOT_REPS):
            raise ValueError("Malformed paired comparison")
        key=(*cell,R,mu,a,b)
        if key in pindex:raise ValueError("Duplicate paired comparison")
        if not 0<=x["second_lower_realized_MSE_count"]<=PILOT_REPS:
            raise ValueError("Impossible within-seed win count")
        if x["SE_interpretation"].startswith("not_valid_normal_")!=(
            x["regime"] in HEAVY_FOURTH):
            raise ValueError("Lost fourth-moment warning on paired loss")
        left=indexed[(*cell,R,mu,a)]["mean_realized_latent_MSE"]
        right=indexed[(*cell,R,mu,b)]["mean_realized_latent_MSE"]
        mismatch=abs(left-right-x["paired_mean_realized_MSE_first_minus_second"])
        max_difference=max(max_difference,mismatch)
        if mismatch>1e-8:
            raise ValueError(f"Paired mean loss does not agree with method MSE: {key}")
        pindex[key]=x
    if len(indexed)!=15360 or len(pindex)!=7680:
        raise ValueError("Missing complete statistical dimensions")
    return manifest,indexed,pindex,max_difference


def summarize(root=ROOT):
    man,methods,pairs,maximum=verify(root)
    per_distribution=[]
    by_scenario=[]
    for R in (3,1):
        for law in FINITE_REGIMES:
            rows=[]
            for d in ORDERS:
                for n in LENGTHS:
                    for eta in ETA_SDS:
                        def get(method,mu=1.):
                            return methods[(law,d,n,eta,R,mu,method)]["mean_realized_latent_MSE"]
                        def paired(method_a,method_b,mu=1.):
                            return pairs[(law,d,n,eta,R,mu,method_a,method_b)]
                        mlcv=paired(ML,CV)
                        zero_cost=paired(ZERO_ML,ML)
                        zero_cv_cost=paired(ZERO_CV,CV)
                        weak_cost=paired(ZERO_ML,ML,.25)
                        truezero_cost=paired(ZERO_ML,ML,0.)
                        rows.append({
                            "regime":law,"R":R,"d":d,"N":n,"sigma_eta":eta,
                            "mu_over_sigma_epsilon":1.,
                            "independent_base_shock_draws":PILOT_REPS,
                            "oracle_known_mu_known_covariance_MSE":get(ORACLE),
                            "known_mu_ML_MSE":get("known_mu_estimated_variance_ml"),
                            "known_mu_CV_MSE":get("known_mu_pooled_loocv"),
                            "estimated_mu_ML_MSE":get(ML),
                            "estimated_mu_CV_MSE":get(CV),
                            "pooled_plugin_ML_MSE":get(PLUGIN),
                            "forced_zero_mu_ML_MSE":get(ZERO_ML),
                            "forced_zero_mu_CV_MSE":get(ZERO_CV),
                            "mean_ML_minus_CV_paired_MSE":
                                mlcv["paired_mean_realized_MSE_first_minus_second"],
                            "diagnostic_SE_ML_minus_CV_NOT_VALID_t3":
                                mlcv["diagnostic_SE_of_paired_difference_NOT_VALID_for_t3"],
                            "CV_lower_realized_MSE_count_among_25":
                                mlcv["second_lower_realized_MSE_count"],
                            "cost_forcing_zero_mu_ML_at_true_mu_plus_1":
                                zero_cost["paired_mean_realized_MSE_first_minus_second"],
                            "cost_forcing_zero_mu_CV_at_true_mu_plus_1":
                                zero_cv_cost["paired_mean_realized_MSE_first_minus_second"],
                            "cost_forcing_zero_mu_ML_at_true_mu_plus_point25":
                                weak_cost["paired_mean_realized_MSE_first_minus_second"],
                            "cost_forcing_zero_mu_ML_at_true_mu_zero":
                                truezero_cost["paired_mean_realized_MSE_first_minus_second"],
                            "fourth_moment_finite":law not in HEAVY_FOURTH,
                        })
            n=len(rows)
            avg=lambda key:sum(x[key] for x in rows)/n
            per_distribution.append({
                "regime":law,"R":R,"base_scenario_cells":n,
                "independent_base_draws_per_cell":PILOT_REPS,
                "Gaussian_quasi_ML_lower_mean_MSE_count":sum(
                    x["mean_ML_minus_CV_paired_MSE"]<0 for x in rows),
                "CV_lower_mean_MSE_count":sum(
                    x["mean_ML_minus_CV_paired_MSE"]>0 for x in rows),
                "forced_zero_mu_ML_cost_positive_count":sum(
                    x["cost_forcing_zero_mu_ML_at_true_mu_plus_1"]>0 for x in rows),
                "forced_zero_mu_ML_cost_exceeds_abs_method_gap_count":sum(
                    x["cost_forcing_zero_mu_ML_at_true_mu_plus_1"] >
                    abs(x["mean_ML_minus_CV_paired_MSE"]) for x in rows),
                "pooled_plugin_better_than_GLS_ML_count":sum(
                    x["pooled_plugin_ML_MSE"]<x["estimated_mu_ML_MSE"]
                    for x in rows),
                "mean_GLS_ML_latent_MSE_descriptive":avg("estimated_mu_ML_MSE"),
                "mean_fold_clean_CV_latent_MSE_descriptive":avg("estimated_mu_CV_MSE"),
                "mean_pooled_plugin_latent_MSE_descriptive":avg("pooled_plugin_ML_MSE"),
                "mean_ML_minus_CV_paired_MSE_descriptive":
                    avg("mean_ML_minus_CV_paired_MSE"),
                "mean_forced_zero_mu_ML_penalty_descriptive":
                    avg("cost_forcing_zero_mu_ML_at_true_mu_plus_1"),
                "infinite_fourth_moment_caveat":law in HEAVY_FOURTH,
            })
            by_scenario.extend(rows)

    return {
        "status":"saved_compact_pilot_verified_no_raw_shard_recheck",
        "source_git_sha":man["source_git_sha"],
        "independent_R3_shock_pools":4800,
        "method_rows_represented":384000,
        "saved_mean_method_cells":15360,
        "saved_paired_comparison_cells":7680,
        "max_paired_vs_method_arithmetic_discrepancy":maximum,
        "R3_mu_plus1_cells":192,
        "R3_cells_quasi_ML_better_than_CV":sum(
            r["mean_ML_minus_CV_paired_MSE"]<0
            for r in by_scenario if r["R"]==3),
        "R1_mu_plus1_cells":192,
        "R1_cells_quasi_ML_better_than_CV":sum(
            r["mean_ML_minus_CV_paired_MSE"]<0
            for r in by_scenario if r["R"]==1),
        "R3_cells_wrong_zero_mu_ML_more_costly_than_ML_CV_gap":sum(
            r["cost_forcing_zero_mu_ML_at_true_mu_plus_1"]>
            abs(r["mean_ML_minus_CV_paired_MSE"])
            for r in by_scenario if r["R"]==3),
        "R3_by_distribution": [r for r in per_distribution if r["R"]==3],
        "R1_by_distribution": [r for r in per_distribution if r["R"]==1],
        "warnings":[
            "Only 25 independent base draws per regime/d/N/eta. Exploratory; no robust significance or confirmation claim.",
            "Five mu shifts and nested R1/R3 deliberately reuse identical random shocks.",
            "Student-t3 in innovations or observations has infinite fourth moment; diagnostic sample MSE SE does NOT justify normal-approx confidence intervals.",
            "All noise laws have finite population variance; Gaussian covariance contrast is quasi-MLE outside Gaussianity and remains correctly specified at the second moment under these designs.",
            "Cauchy excluded: true variance ratio/expected squared risk undefined.",
            "Raw compressed shards were checksum-verified by user-side aggregator but are not on GitHub; this audit verifies only compact saved aggregates and original provenance metadata.",
            "Regime-averaged risk descriptives mix different N/eta/d DGPs; scientifically compare methods within scenario.",
        ],
    },by_scenario


def execute(root=ROOT,out=None):
    report,detail=summarize(root)
    if out is not None:
        if out.exists():raise FileExistsError("Refusing to overwrite prior audit")
        out.mkdir(parents=True)
        (out/"audit_summary.json").write_text(
            json.dumps(report,indent=2)+"\n",encoding="utf-8")
        with (out/"R1_R3_mu_plus1_all_8_methods.csv").open(
                "w",newline="",encoding="utf-8") as f:
            writer=csv.DictWriter(f,fieldnames=list(detail[0]))
            writer.writeheader()
            writer.writerows(detail)
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,default=ROOT)
    p.add_argument("--out-dir",type=Path,default=None)
    args=p.parse_args()
    report=execute(args.root,args.out_dir)
    print(json.dumps({k:report[k] for k in (
        "status","source_git_sha","independent_R3_shock_pools",
        "R3_mu_plus1_cells","R3_cells_quasi_ML_better_than_CV",
        "R1_cells_quasi_ML_better_than_CV",
        "R3_cells_wrong_zero_mu_ML_more_costly_than_ML_CV_gap",
    )},indent=2))


if __name__=="__main__":
    main()
