"""Read-only independent audit of uploaded Cortes-Toto Study K 25-seed replay.

No Monte Carlo, no access to 1.248M raw compressed method rows.
Confirms original pilot SHA and exact J-baseline parity provenance,
192 original (non-new) 25-seed shock streams, 26 methods/42 paired
contrasts for each 2R x 5mu cell, agrees paired mean MSE with method
MSE to floating error, and preserves t3 infinite-fourth-moment caveat.

Disaggregation is mandatory: law/d/N/eta/R/mu. Cross-law and cross-d
MSE averages are DESCRIPTIVE only; these are not homogeneous risks.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

from .run_nonzero_mu_nongaussian import FINITE_REGIMES, HEAVY_FOURTH
from .run_nonzero_mean_multorder import ORDERS, LENGTHS, ETA_SDS, MU_FACTORS
from .run_cortes_criteria_pilot import ALL_METHODS, PAIRS, OLD_PREFIX, PRIOR_METHODS, PROTOCOL

ROOT = Path("results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001")
GLS="existing__estimated_mu_gaussian_gls_ml"
PLUGIN="existing__pooled_guerrero_plugin_mu_plus_gaussian_ml"
OLD_CV="existing__estimated_mu_fold_clean_pooled_loocv"
FOCUS = (GLS, PLUGIN, "gcv_joint", "cv_joint", "aicc_joint", OLD_CV,
         "bic_joint", "controlled_S0.8_joint", "cv_zero")


def _rows(path):
    with path.open("r", newline="", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError(f"Missing CSV fields in {path}")
        return list(reader)


def _number(row, field):
    return float(row[field])


def verify(root=ROOT):
    manifest=json.loads((root/"campaign_manifest.json").read_text(encoding="utf-8"))
    expected={(reg,d,n,eta) for reg in FINITE_REGIMES
              for d in ORDERS for n in LENGTHS for eta in ETA_SDS}
    if (manifest["protocol"] != PROTOCOL or
        manifest["status"] != "COMPLETE_25_SEED_PAIRED_REPLAY_EXPLORATORY" or
        manifest["underlying_seedbank"] != "Study J 25 independent original R3 shocks per 192 strata" or
        manifest["source_git_sha"] != "1785889d7d64a77f548d8746d41a9ea786e3e588" or
        manifest["strata_required"] != 192 or
        manifest["strata_present"] != 192 or
        manifest["independent_original_J_shock_draws_replayed"] != 4800 or
        manifest["method_rows_represented"] != 1248000 or
        manifest["method_aggregate_cells"] != 49920 or
        manifest["paired_aggregate_cells"] != 80640 or
        manifest["solver_and_scan_points"] != ["multibracket",41] or
        manifest["methods"] != list(ALL_METHODS) or
        manifest["comparisons"] != [list(x) for x in PAIRS]):
        raise ValueError("Not the complete, source-pinned Study K pilot")
    par=manifest["original_eight_method_parity"]
    if (par["status"] != "checked_same_25_J_seeds" or
        par["saved_J_baseline_cells_matched"] != 15360 or
        par["maximum_mean_true_MSE_difference"] != 0):
        raise ValueError("Original J 8-method exact baseline parity failed")
    cells={(s["regime"],s["d"],s["N"],s["sigma_eta"]):s
           for s in manifest["per_cell"]}
    if set(cells) != expected or any(
            x["replayed_independent_J_base_seeds"]!=25 for x in cells.values()):
        raise ValueError("Missing or duplicate original 25-seed strata")
    if len(manifest["shards"])!=192:
        raise ValueError("Missing original gzip provenance")
    seen=set()
    for s in manifest["shards"]:
        key=(s["regime"],s["d"],s["N"],s["sigma_eta"])
        if (key not in expected or key in seen or
            s["start"]!=0 or s["stop"]!=25 or
            len(s["compressed_csv_sha256"])!=64):
            raise ValueError("Invalid/duplicated source gzip shard interval")
        seen.add(key)
    if seen!=expected:raise ValueError("Missing source gzip shard")

    rows=_rows(root/"by_regime_d_N_eta_R_mu_26_methods.csv")
    paired=_rows(root/"paired_criterion_vs_original_MLE_LOOCV_plugin.csv")
    if len(rows)!=49920 or len(paired)!=80640:
        raise ValueError("Unexpected aggregate row counts")
    index={}
    for x in rows:
        law,d,n,eta,R,mu,m=x["regime"],int(x["d"]),int(x["N"]),_number(x,"sigma_eta"),int(x["R"]),_number(x,"mu_factor"),x["method"]
        key=(law,d,n,eta,R,mu,m)
        if ((law,d,n,eta) not in expected or R not in (1,3) or
            mu not in MU_FACTORS or m not in ALL_METHODS or
            int(x["n_independent_base_J_shocks"])!=25 or
            x["fourth_moment_infinite_normal_CI_not_valid"]!="True" if False else False):
            # Boolean warning checked below, without ternary precedence ambiguity.
            raise ValueError("Malformed factor-method row")
        if bool(x["fourth_moment_infinite_normal_CI_not_valid"]=="True") != (law in HEAVY_FOURTH):
            raise ValueError("Incorrect Student-t3 infinite-fourth-moment label")
        val=_number(x,"mean_true_trend_MSE")
        if key in index or val<0 or not math.isfinite(val):
            raise ValueError("Duplicate or invalid method MSE")
        index[key]=x
    if len(index)!=49920:
        raise ValueError("Missing method cells")

    max_error=0.; seen_pairs=set()
    for x in paired:
        law,d,n,eta,R,mu=x["regime"],int(x["d"]),int(x["N"]),_number(x,"sigma_eta"),int(x["R"]),_number(x,"mu_factor")
        first,second=x["first_method"],x["second_method"]
        key=(law,d,n,eta,R,mu,first,second)
        if ((law,d,n,eta) not in expected or R not in (1,3) or
            mu not in MU_FACTORS or (first,second) not in PAIRS or
            int(x["n_independent_base_J_shocks"])!=25 or
            key in seen_pairs):
            raise ValueError("Malformed, missing or repeated paired contrast")
        seen_pairs.add(key)
        if bool(x["fourth_moment_infinite_normal_CI_not_valid"]=="True")!=(law in HEAVY_FOURTH):
            raise ValueError("Incorrect paired Student-t3 moment flag")
        delta=(_number(index[(*key[:6],first)],"mean_true_trend_MSE")-
               _number(index[(*key[:6],second)],"mean_true_trend_MSE"))
        error=abs(delta-_number(x,"paired_mean_MSE_first_minus_second"))
        max_error=max(max_error,error)
        if error>1e-7:raise ValueError(f"Paired arithmetic discrepancy for {key}")
        count=int(x["second_lower_MSE_count"])
        if not 0<=count<=25:raise ValueError("Impossible per-seed winner count")
    return manifest,index,paired,max_error


def descriptive(root=ROOT):
    manifest,idx,pairs,max_error=verify(root)
    subsets=[]
    for R in (3,1):
        for law in FINITE_REGIMES:
            for d in ORDERS:
                for n in LENGTHS:
                    for eta in ETA_SDS:
                        shared=(law,d,n,eta,R,1.0)
                        r={"regime":law,"R":R,"d":d,"N":n,"sigma_eta":eta,
                           "mu_factor":1.0,"independent_reused_J_shocks":25}
                        for method in ALL_METHODS:
                            r[method]=_number(idx[(*shared,method)],"mean_true_trend_MSE")
                        subset=[(m,r[m]) for m in ALL_METHODS
                                if (not m.endswith("_fixed") and
                                    m not in (OLD_PREFIX+"known_mu_true_ratio_oracle",
                                              OLD_PREFIX+"known_mu_estimated_variance_ml",
                                              OLD_PREFIX+"known_mu_pooled_loocv"))]
                        winner=min(subset,key=lambda x:x[1])
                        r["best_feasible_method_IN_THIS_PILOT"]=winner[0]
                        r["best_feasible_MSE_IN_THIS_PILOT"]=winner[1]
                        r["BIC_joint_lower_bound_shock_count"]=int(
                            idx[(*shared,"bic_joint")]["truncated_lower_lambda_count"])
                        subsets.append(r)
    summarized=[]
    for R in (3,1):
        for law in FINITE_REGIMES:
            a=[r for r in subsets if r["R"]==R and r["regime"]==law]
            summary={"regime":law,"R":R,"scenario_cells":16,
                     "independent_reused_shocks_per_cell":25,
                     "gaussian_GLS_better_cell_count":sum(
                         r[GLS]<r["cv_joint"] for r in a),
                     "GCV_better_than_GLS_count":sum(
                         r["gcv_joint"]<r[GLS] for r in a),
                     "AICc_better_than_GLS_count":sum(
                         r["aicc_joint"]<r[GLS] for r in a),
                     "plugin_better_than_GLS_count":sum(
                         r[PLUGIN]<r[GLS] for r in a),
                     "BIC_joint_lower_bound_selections":sum(
                         r["BIC_joint_lower_bound_shock_count"] for r in a)}
            for method in FOCUS:
                summary["mean_MSE__"+method]=sum(r[method] for r in a)/16
            summarized.append(summary)
    global_report={
        "status":"COMPLETE_EXPLORATORY_25_SEED_PAIRED_REPLAY_INDEPENDENT_AGGREGATE_AUDIT",
        "original_J_seedbank_reused_not_new_confirmatory":True,
        "original_reused_independent_shocks":4800,
        "source_git_sha":manifest["source_git_sha"],
        "original_J_eight_method_MSE_parity":manifest["original_eight_method_parity"],
        "mean_method_cells":len(idx),
        "paired_cells":len(pairs),
        "max_paired_arithmetic_discrepancy":max_error,
        "R3_restricted_mu_plus1_cells":192,
        "R1_restricted_mu_plus1_cells":192,
        "R3_GLS_better_than_CV_multibracket":sum(
            r[GLS]<r["cv_joint"] for r in subsets if r["R"]==3),
        "R3_GLS_better_than_GCV":sum(
            r[GLS]<r["gcv_joint"] for r in subsets if r["R"]==3),
        "R3_GLS_better_than_AICc":sum(
            r[GLS]<r["aicc_joint"] for r in subsets if r["R"]==3),
        "R1_AICc_better_than_GLS":sum(
            r["aicc_joint"]<r[GLS] for r in subsets if r["R"]==1),
        "BIC_joint_at_lower_search_limit_in_R3":sum(
            r["BIC_joint_lower_bound_shock_count"] for r in subsets
            if r["R"]==3),
        "BIC_joint_at_lower_search_limit_in_R1":sum(
            r["BIC_joint_lower_bound_shock_count"] for r in subsets
            if r["R"]==1),
        "per_regime_and_R":summarized,
        "warnings":[
            "All methods use the original Study J 25 shocks per regime/d/N/eta, not 4800 newly independent repetitions.",
            "Normal 95% MSE uncertainty is not guaranteed for Student-t(3) with infinite fourth moment.",
            "BIC plug-in logRSS is unbounded as lambda->0; bounded search is not meaningful unrestricted BIC comparison.",
            "The new CV multibracket and old exact-fold CV may optimize identical scores with DIFFERENT numerical strategies; risk gaps alone do not identify which has lower CV objective on individual seeds.",
            "Descriptive mean MSE over d/N/eta/laws is not a homogeneous risk or automatic model-order selector.",
            "Only compact GitHub aggregates audited here; local compressed individual-shock records cannot be independently SHA verified without local raw files.",
            "No independent new 10000-seed Study K confirmation exists.",
        ],
    }
    return global_report,subsets,summarized


def write_csv(path,rows):
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)


def execute(root=ROOT,out_dir=None):
    report,scenarios,regimes=descriptive(root)
    if out_dir is not None:
        if out_dir.exists():
            raise FileExistsError(f"Refusing overwrite: {out_dir}")
        out_dir.mkdir(parents=True)
        (out_dir/"audit_summary.json").write_text(
            json.dumps(report,indent=2)+"\n",encoding="utf-8")
        write_csv(out_dir/"R1_R3_mu_plus1_26_methods_per_scenario.csv",scenarios)
        write_csv(out_dir/"by_regime_R_mu_plus1_key_methods.csv",regimes)
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,default=ROOT)
    p.add_argument("--out-dir",type=Path,default=None)
    a=p.parse_args()
    result=execute(a.root,a.out_dir)
    print(json.dumps({k:result[k] for k in (
        "status","original_reused_independent_shocks","mean_method_cells",
        "paired_cells","max_paired_arithmetic_discrepancy",
        "R3_GLS_better_than_CV_multibracket",
        "R3_GLS_better_than_GCV",
        "R3_GLS_better_than_AICc",
        "BIC_joint_at_lower_search_limit_in_R3")},indent=2))


if __name__=="__main__":
    main()
