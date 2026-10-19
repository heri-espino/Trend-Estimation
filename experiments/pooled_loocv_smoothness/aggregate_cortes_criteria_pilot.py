"""Audit/aggregate saved Study K source-matched 25-seed replay shards.

The pilot is COMPLETE only if all 12 x 4 x 2 x 2 = 192 strata
contain exactly Study J's 25 independent base R3 shocks. Reusing J
seeds does not constitute 4,800 *new* independent confirmations.

Merge per-shard summary sufficient statistics, not all 1.248M rows.
Check disjoint seed intervals, single code SHA, solver policy, method
coverage, SHA256 (optional slow reread) and original J baseline parity.

For Student-t3 noise, squared-loss fourth moments can diverge; the
usual normal SE of the sample mean (including paired differences)
must NOT be represented as a validated 95% confidence interval.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

from .aggregate_nonzero_mean_multorder import _merge, _sha256
from .run_nonzero_mu_nongaussian import FINITE_REGIMES,HEAVY_FOURTH,LENGTHS,ETA_SDS,ORDERS,PILOT_REPS
from .run_nonzero_difference_mean import MU_FACTORS
from .run_cortes_criteria_pilot import (
    ALL_METHODS, PAIRS, OLD_PREFIX, PRIOR_METHODS, PROTOCOL
)

ROOT=Path("results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/pilot")
PRIOR_ROOT=Path("results/pooled_loocv_smoothness/guerrero/nonzero_mu_nongaussian/audit_pilot_001")


def _read_csv(path):
    with path.open("r",newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))


def collect(root:Path=ROOT,*,verify_digests=False,verify_prior=True):
    files=sorted(root.rglob("manifest.json"))
    if not files:raise FileNotFoundError("No completed replay shards found")
    expected={(reg,d,n,eta) for reg in FINITE_REGIMES
              for d in ORDERS for n in LENGTHS for eta in ETA_SDS}
    intervals=defaultdict(list)
    a=defaultdict(list);b=defaultdict(list);shards=[]
    versions=set()
    solvers=set()
    for file in files:
        m=json.loads(file.read_text(encoding="utf-8"))
        if m.get("protocol")!=PROTOCOL or m.get("status")!="executed_shard":
            raise ValueError(f"Unexpected/incomplete source shard: {file}")
        if (m.get("original_study_J_source_sha")!="33c8eef425e56c6e17b9a5f3d331869e2af99c30" or
            not m.get("study_J_original_seed_bank_reused") or
            m.get("methods")!=list(ALL_METHODS) or
            m.get("paired_comparisons")!=[list(z) for z in PAIRS]):
            raise ValueError(f"Changed statistical baseline or selectors: {file}")
        key=(m["regime"],m["difference_order_fixed"],m["N"],
             m["sigma_eta_population_SD"])
        if key not in expected:
            raise ValueError("Unknown noise/order/N/eta cell")
        start,stop=m["seed_start_inclusive"],m["seed_stop_exclusive"]
        if not 0<=start<stop<=PILOT_REPS:
            raise ValueError("Seed interval outside the 25-seed pilot")
        if m["actual_method_rows"]!=(stop-start)*2*len(MU_FACTORS)*len(ALL_METHODS):
            raise ValueError("Incorrect per-method source row count")
        data=file.parent/"method_comparison.csv.gz"
        if not data.is_file() or data.stat().st_size!=m["compressed_csv_bytes"]:
            raise ValueError(f"Missing/incomplete gzip raw shard: {data}")
        if verify_digests and _sha256(data)!=m["compressed_csv_sha256"]:
            raise ValueError(f"Gzip checksum invalid: {data}")
        intervals[key].append((start,stop))
        versions.add(m.get("source_git_sha"))
        solvers.add((m["search_solver"],m["search_scan_points"]))
        data=json.loads((file.parent/"summary.json").read_text(encoding="utf-8"))
        if (data.get("status")!="completed_shard" or
            len(data["by_R_mu_method"])!=2*len(MU_FACTORS)*len(ALL_METHODS) or
            len(data["paired_R_mu_method_contrasts"])!=2*len(MU_FACTORS)*len(PAIRS)):
            raise ValueError(f"Incomplete source sufficient statistics: {file}")
        for x in data["by_R_mu_method"]:
            if (x["R"] not in (1,3) or x["mu_factor"] not in MU_FACTORS or
                x["method"] not in ALL_METHODS or
                x["independent_base_shock_draws"]!=stop-start):
                raise ValueError("Malformed per-method summary")
            a[(*key,x["R"],x["mu_factor"],x["method"])].append(x)
        for x in data["paired_R_mu_method_contrasts"]:
            if (x["R"] not in (1,3) or x["mu_factor"] not in MU_FACTORS or
                (x["first_method"],x["second_method"]) not in PAIRS or
                x["independent_base_shock_draws"]!=stop-start):
                raise ValueError("Malformed paired summary")
            b[(*key,x["R"],x["mu_factor"],x["first_method"],x["second_method"])].append(x)
        shards.append({"manifest":str(file.relative_to(root)),
                       "regime":key[0],"d":key[1],"N":key[2],
                       "sigma_eta":key[3],"start":start,"stop":stop,
                       "compressed_csv_sha256":m["compressed_csv_sha256"]})

    if len(versions)!=1 or None in versions or len(solvers)!=1:
        raise ValueError("Mixed source code commit or mixed numerical search budgets")
    observed={}
    for key,ints in intervals.items():
        ints.sort()
        for i,(start,stop) in enumerate(ints):
            if i and start<ints[i-1][1]:
                raise ValueError(f"Overlapping independent seed intervals: {key}")
        observed[key]=sum(stop-start for start,stop in ints)
    complete=(set(intervals)==expected and
              all(ints[0][0]==0 and ints[-1][1]==PILOT_REPS and
                  all(u[1]==v[0] for u,v in zip(ints,ints[1:]))
                  for ints in intervals.values()))
    methods=[]
    for (reg,d,n,eta,R,mu,method),rows in sorted(a.items()):
        reps,avg,sd=_merge(rows,mean_key="mean_realized_trend_MSE",
            sd_key="sample_sd_realized_trend_MSE",
            count_key="independent_base_shock_draws")
        methods.append({
            "regime":reg,"d":d,"N":n,"sigma_eta":eta,"R":R,"mu_factor":mu,
            "method":method,"n_independent_base_J_shocks":reps,
            "mean_true_trend_MSE":avg,
            "sample_SD_true_trend_MSE":sd,
            "diagnostic_mean_MSE_SE":None if sd is None else sd/reps**.5,
            "fourth_moment_infinite_normal_CI_not_valid":reg in HEAVY_FOURTH,
            "mean_true_trend_MAE":sum(
                r["mean_realized_trend_MAE"]*r["independent_base_shock_draws"]
                for r in rows)/reps,
            "infinite_lambda_count":sum(r["infinite_lambda_count"] for r in rows),
            "truncated_lower_lambda_count":sum(
                r["truncated_lower_domain_count"] for r in rows),
        })
    contrasts=[]
    for (reg,d,n,eta,R,mu,first,second),rows in sorted(b.items()):
        reps,avg,sd=_merge(rows,mean_key="mean_paired_MSE_first_minus_second",
            sd_key="sample_sd_paired_difference",
            count_key="independent_base_shock_draws")
        contrasts.append({
            "regime":reg,"d":d,"N":n,"sigma_eta":eta,"R":R,"mu_factor":mu,
            "first_method":first,"second_method":second,
            "n_independent_base_J_shocks":reps,
            "paired_mean_MSE_first_minus_second":avg,
            "sample_SD_paired_difference":sd,
            "diagnostic_paired_SE":None if sd is None else sd/reps**.5,
            "fourth_moment_infinite_normal_CI_not_valid":reg in HEAVY_FOURTH,
            "second_lower_MSE_count":sum(r["second_lower_realized_MSE_count"] for r in rows),
        })
    if complete and (len(methods)!=len(expected)*2*len(MU_FACTORS)*len(ALL_METHODS)
                     or len(contrasts)!=len(expected)*2*len(MU_FACTORS)*len(PAIRS)):
        raise ValueError("Missing aggregate cells despite claimed complete seed coverage")

    # The 8 previously published pilot MSEs MUST remain invariant when
    # generated with the same seeds and generator. This direct test can
    # detect changes in RNG, PLS, mu or variance estimators after Study J.
    prior_parity={"status":"skipped_prior_replay_not_checked"}
    if verify_prior and complete:
        file=PRIOR_ROOT/"by_regime_d_N_eta_R_mu_method.csv"
        if not file.is_file():
            raise FileNotFoundError(f"J pilot aggregate missing for reproducibility: {file}")
        previous={(x["regime"],int(x["d"]),int(x["N"]),float(x["sigma_eta"]),
                   int(x["R"]),float(x["mu_factor"]),OLD_PREFIX+x["method"]):
                  float(x["mean_realized_latent_MSE"])
                  for x in _read_csv(file)}
        max_error=0.;checked=0
        for row in methods:
            if row["method"] not in (OLD_PREFIX+x for x in PRIOR_METHODS):
                continue
            key=(row["regime"],row["d"],row["N"],row["sigma_eta"],
                 row["R"],row["mu_factor"],row["method"])
            expected_mean=previous.get(key)
            if expected_mean is None:
                raise ValueError(f"Missing saved J reference for {key}")
            discrepancy=abs(row["mean_true_trend_MSE"]-expected_mean)
            max_error=max(max_error,discrepancy)
            if discrepancy>1e-5+1e-5*abs(expected_mean):
                raise ValueError(f"Pilot baseline not reproducible: {key}; delta {discrepancy}")
            checked+=1
        prior_parity={"status":"checked_same_25_J_seeds",
                      "saved_J_baseline_cells_matched":checked,
                      "maximum_mean_true_MSE_difference":max_error}
    if verify_prior and not complete:
        prior_parity={"status":"skipped_incomplete_shards_cannot_compare_single_seed_to_25_seed_J_means"}
    report={
        "protocol":PROTOCOL,
        "status":"COMPLETE_25_SEED_PAIRED_REPLAY_EXPLORATORY" if complete
             else "INCOMPLETE_PAIRED_REPLAY_EXPLORATORY",
        "underlying_seedbank":"Study J 25 independent original R3 shocks per 192 strata",
        "source_git_sha":next(iter(versions)),
        "solver_and_scan_points":list(next(iter(solvers))),
        "strata_required":len(expected),"strata_present":len(intervals),
        "independent_original_J_shock_draws_replayed":sum(observed.values()),
        "method_rows_represented":sum(observed.values())*2*len(MU_FACTORS)*len(ALL_METHODS),
        "method_aggregate_cells":len(methods),
        "paired_aggregate_cells":len(contrasts),
        "methods":list(ALL_METHODS),
        "comparisons":[list(x) for x in PAIRS],
        "per_cell":[{"regime":r,"d":d,"N":n,"sigma_eta":eta,
                     "replayed_independent_J_base_seeds":observed.get((r,d,n,eta),0)}
                    for r,d,n,eta in sorted(expected)],
        "original_eight_method_parity":prior_parity,
        "shards":shards,
        "warnings":[
            "Reusing original Study J 25 shock pools is deliberate PAIRING, not independent new confirmation.",
            "R1 is nested in R3 and five mu values share shocks, so no sample size inflation.",
            "Known mu (fixed mode) is an ORACLE, never feasible.",
            "Simple BIC logRSS diverges as lambda approaches 0, so any selected BIC is positive-domain constrained and its nominal optimum not global.",
            "Student-t3 squared-loss has infinite fourth moment; normal MC confidence intervals are not licensed by sample SE.",
            "Different stochastic trend order d, lengths N, noises and regimes must remain disaggregated.",
        ],
    }
    return report,methods,contrasts


def _write_csv(path,rows):
    if not rows:raise ValueError("Nothing to export")
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def execute(root:Path,out:Path,*,require_complete=False,verify_digests=False,
            verify_prior=True):
    report,methods,pairs=collect(root,verify_digests=verify_digests,
                                 verify_prior=verify_prior)
    if require_complete and not report["status"].startswith("COMPLETE_"):
        raise ValueError("Incomplete 25-J-seed pilot replay, no completeness claim")
    if out.exists():raise FileExistsError(f"Do not overwrite previous audit: {out}")
    out.mkdir(parents=True,exist_ok=False)
    (out/"campaign_manifest.json").write_text(
        json.dumps(report,indent=2)+"\n",encoding="utf-8")
    _write_csv(out/"by_regime_d_N_eta_R_mu_26_methods.csv",methods)
    _write_csv(out/"paired_criterion_vs_original_MLE_LOOCV_plugin.csv",pairs)
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=ROOT)
    parser.add_argument("--out-dir",type=Path,required=True)
    parser.add_argument("--require-complete",action="store_true")
    parser.add_argument("--verify-digests",action="store_true")
    parser.add_argument("--skip-original-J-parity",action="store_true")
    args=parser.parse_args()
    report=execute(args.root,args.out_dir,
                   require_complete=args.require_complete,
                   verify_digests=args.verify_digests,
                   verify_prior=not args.skip_original_J_parity)
    print(json.dumps({
        "status":report["status"],"source_git_sha":report["source_git_sha"],
        "strata_present":report["strata_present"],
        "original_J_shocks_replayed":report["independent_original_J_shock_draws_replayed"],
        "per_method_rows":report["method_rows_represented"],
        "method_aggregate_cells":report["method_aggregate_cells"],
        "paired_aggregate_cells":report["paired_aggregate_cells"],
        "original_J_baseline_parity":report["original_eight_method_parity"],
    },indent=2))


if __name__=="__main__":
    main()
