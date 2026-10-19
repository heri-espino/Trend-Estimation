"""Check and combine disjoint finite-variance non-Gaussian mu-shift shards.

Avoid loading all raw rows. Preserve per-(regime,d,N,eta,R,mu)
independent-base-seed mean MSE, paired MSE differences and win counts.
For Student-t(3) observation/innovation loss, ordinary sample SEs
are shown ONLY as diagnostics: the underlying fourth moments of
Gaussian-type quadratic losses may be infinite. The expected squared
risk can exist without a finite variance of the Monte Carlo loss.

Cauchy is excluded by construction and requires separate robust loss.
NEVER declare full confirmation if a single seed or cell is missing.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

from .run_nonzero_mu_nongaussian import (
    FINITE_REGIMES, HEAVY_FOURTH, PROTOCOL, PILOT_REPS, CONFIRMATORY_REPS
)
from .run_nonzero_mean_multorder import (
    ORDERS, LENGTHS, ETA_SDS, MU_FACTORS, METHODS, PAIRS, _sha
)
from .aggregate_nonzero_mean_multorder import _merge, _sha256

BASE = Path("results/pooled_loocv_smoothness/guerrero/nonzero_mu_nongaussian")


def _method_records(root:Path, phase:str, *, digest=False):
    source=root/phase
    manifests=sorted(source.rglob("manifest.json"))
    if not manifests:raise FileNotFoundError(f"No complete shards in {source}")
    count_expected=PILOT_REPS if phase=="pilot" else CONFIRMATORY_REPS
    strata={(regime,d,n,eta) for regime in FINITE_REGIMES
            for d in ORDERS for n in LENGTHS for eta in ETA_SDS}
    ranges=defaultdict(list)
    src=set()
    mgroup,pgroup=defaultdict(list),defaultdict(list)
    shards=[]
    for path in manifests:
        m=json.loads(path.read_text(encoding="utf-8"))
        if m.get("protocol")!=PROTOCOL or m.get("phase")!=phase or m.get("status")!="executed_shard":
            raise ValueError(f"Foreign or incomplete shard: {path}")
        regime,d,n,eta=(m["regime"],m["difference_order_fixed"],m["N"],m["sigma_eta_population_SD"])
        key=(regime,d,n,eta)
        if key not in strata:raise ValueError(f"Unknown stratification: {key}")
        lo,hi=m["seed_start_inclusive"],m["seed_stop_exclusive"]
        if not 0<=lo<hi<=count_expected or m["expected_independent_base_draws"]!=hi-lo:
            raise ValueError(f"Impossible seed interval: {path}")
        if m["actual_method_rows"]!=(hi-lo)*2*len(MU_FACTORS)*len(METHODS):
            raise ValueError(f"Wrong method count: {path}")
        if m.get("noise_var_exists") is not True or (m.get("error_fourth_moment_exists") is not (regime not in HEAVY_FOURTH)):
            raise ValueError(f"Moment labels missing or contradicted: {path}")
        artifact=path.parent/"method_comparison.csv.gz"
        if not artifact.is_file() or artifact.stat().st_size!=m["compressed_csv_bytes"]:
            raise ValueError(f"Incomplete method CSV: {path}")
        if digest and _sha256(artifact)!=m["compressed_csv_sha256"]:
            raise ValueError(f"Method data hash mismatch: {path}")
        ranges[key].append((lo,hi))
        src.add(m["source_git_sha"])
        summary=json.loads((path.parent/"summary.json").read_text(encoding="utf-8"))
        if summary.get("status")!="completed_shard" or len(summary["by_R_mu_method"])!=2*len(MU_FACTORS)*len(METHODS) or len(summary["paired_R_mu_method_contrasts"])!=2*len(MU_FACTORS)*len(PAIRS):
            raise ValueError(f"Invalid per-method/paired summaries: {path}")
        for x in summary["by_R_mu_method"]:
            subkey=(*key,x["R"],x["mu_factor"],x["method"])
            if subkey[-1] not in METHODS or subkey[-2] not in MU_FACTORS or subkey[-3] not in (1,3) or x["independent_base_shock_draws"]!=hi-lo:
                raise ValueError(f"Malformed mean MSE cell: {path}")
            mgroup[subkey].append(x)
        for x in summary["paired_R_mu_method_contrasts"]:
            subkey=(*key,x["R"],x["mu_factor"],x["first_method"],x["second_method"])
            if subkey[-2:] not in PAIRS or subkey[-3] not in MU_FACTORS or subkey[-4] not in (1,3) or x["independent_base_shock_draws"]!=hi-lo:
                raise ValueError(f"Malformed paired MSE cell: {path}")
            pgroup[subkey].append(x)
        shards.append({"file":str(path.relative_to(source)),"regime":regime,
                       "d":d,"N":n,"sigma_eta":eta,
                       "first":lo,"last":hi,
                       "compressed_csv_sha256":m["compressed_csv_sha256"]})

    if None in src or len(src)!=1:
        raise ValueError("Mixed or unknown code versions; do not combine")
    n_total=0
    counts={}
    for k,intervals in ranges.items():
        intervals.sort()
        position=0
        for lo,hi in intervals:
            if lo<position:raise ValueError(f"OVERLAPPING seed intervals in {k}")
            position=hi
        # An incomplete pilot or partial confirmation is ALLOWED for
        # descriptive checkpoint, but holes must not be silently counted.
        counts[k]=sum(hi-lo for lo,hi in intervals)
        if counts[k]>count_expected:raise ValueError("Excess seeds")
        n_total+=counts[k]
    full=(set(ranges)==strata and all(
        ranges[k][0][0]==0 and
        all(a[1]==b[0] for a,b in zip(ranges[k],ranges[k][1:])) and
        ranges[k][-1][1]==count_expected for k in strata))
    method_rows=[]
    for (regime,d,n,eta,R,mu,method),data in sorted(mgroup.items()):
        num,mean,sd=_merge(data,mean_key="mean_latent_trend_mse",
                            sd_key="sample_sd_latent_mse",
                            count_key="independent_base_shock_draws")
        weighted=lambda f:sum(x[f]*x["independent_base_shock_draws"] for x in data)/num
        method_rows.append({
            "regime":regime,"d":d,"N":n,"sigma_eta":eta,"R":R,
            "mu_factor":mu,"method":method,
            "independent_base_shock_draws":num,
            "mean_realized_latent_MSE":mean,
            "sample_SD_realized_MSE":sd,
            "diagnostic_SE_of_MSE_NOT_VALID_for_t3":
                None if sd is None else sd/(num**.5),
            "SE_interpretation":("not_valid_normal_Monte_Carlo_CI_infinite_fourth_moment"
                if regime in HEAVY_FOURTH else "ordinary_Monte_Carlo_SE_conditional_on_DGP"),
            "mean_absolute_reconstruction_error":weighted("mean_absolute_latent_error"),
            "mean_absolute_mu_estimation_error":weighted("mean_absolute_mu_estimation_error"),
            "infinite_lambda_count":sum(x["infinite_lambda_count"] for x in data),
        })
    paired_rows=[]
    for (regime,d,n,eta,R,mu,first,second),data in sorted(pgroup.items()):
        num,mean,sd=_merge(
            data,mean_key="mean_paired_MSE_first_minus_second",
            sd_key="sample_sd_paired_difference",
            count_key="independent_base_shock_draws")
        paired_rows.append({
            "regime":regime,"d":d,"N":n,"sigma_eta":eta,"R":R,
            "mu_factor":mu,
            "first_method":first,"second_method":second,
            "independent_base_shock_draws":num,
            "paired_mean_realized_MSE_first_minus_second":mean,
            "sample_SD_paired_difference":sd,
            "diagnostic_SE_of_paired_difference_NOT_VALID_for_t3":
                None if sd is None else sd/(num**.5),
            "SE_interpretation":("not_valid_normal_Monte_Carlo_CI_infinite_fourth_moment"
                if regime in HEAVY_FOURTH else "ordinary_Monte_Carlo_SE_conditional_on_DGP"),
            "second_lower_realized_MSE_count":sum(x["second_lower_MSE_count"] for x in data),
        })
    report={
        "protocol":PROTOCOL,"phase":phase,
        "status":("COMPLETE_"+phase.upper() if full
                  else "INCOMPLETE_EXPLORATORY_NOT_FULL_"+phase.upper()),
        "source_git_sha":next(iter(src)),
        "finite_variance_distribution_count":len(FINITE_REGIMES),
        "strata_expected":len(strata),
        "strata_present":len(ranges),
        "target_seed_count_per_cell":count_expected,
        "independent_base_R3_shock_draws_present":n_total,
        "method_level_rows_represented":n_total*2*len(MU_FACTORS)*len(METHODS),
        "shards":shards,
        "by_cell":[{"regime":r,"d":d,"N":n,"sigma_eta":e,
                    "independent_shock_draws":counts.get((r,d,n,e),0)}
                   for r,d,n,e in sorted(strata)],
        "fourth_moment_warning":"Student-t3 has finite second but infinite fourth moment. Sample SE for realized quadratic losses is not a validated normal-CI estimator. Report robust statistics/win fractions too; do not claim all 95pct Monte Carlo intervals valid.",
        "variance_warning":"All twelve included regimes have a finite population observation variance. Gaussian fitted likelihood is a quasi-likelihood outside true Gaussian density; for GARCH-t5 observations are serially uncorrelated but conditionally heteroskedastic.",
        "cauchy_warning":"Cauchy is EXCLUDED; no finite noise variance, no Guerrero true variance ratio, no expected squared-error risk. Design separate absolute-error boundary stress.",
        "paired_warning":"Mu treatments and nested R reuse shock realizations; no independent replication inflation, no pooling different d/N/eta/noise laws in claims.",
    }
    return report,method_rows,paired_rows


def _save(path:Path, rows:list[dict]):
    if not rows:raise ValueError("empty aggregate")
    with path.open("w",encoding="utf-8",newline="") as file:
        w=csv.DictWriter(file,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)


def execute(root:Path,output:Path,phase:str,*,require_complete=False,verify_digests=False):
    report,methods,paired=_method_records(root,phase,digest=verify_digests)
    if require_complete and not report["status"].startswith("COMPLETE_"):
        raise ValueError("Incomplete pilot/confirmation; refusing completion claim")
    if output.exists():
        raise FileExistsError(f"Aggregate output already exists: {output}")
    output.mkdir(parents=True)
    (output/"campaign_manifest.json").write_text(json.dumps(report,indent=2)+"\n",
                                                 encoding="utf-8")
    _save(output/"by_regime_d_N_eta_R_mu_method.csv",methods)
    _save(output/"paired_by_regime_d_N_eta_R_mu.csv",paired)
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--phase",choices=("pilot","confirmatory"),default="pilot")
    p.add_argument("--root",type=Path,default=BASE)
    p.add_argument("--out-dir",type=Path,required=True)
    p.add_argument("--require-complete",action="store_true")
    p.add_argument("--verify-digests",action="store_true")
    a=p.parse_args()
    out=execute(a.root,a.out_dir,a.phase,
                require_complete=a.require_complete,verify_digests=a.verify_digests)
    print(json.dumps({k:out[k] for k in ("status","strata_present",
        "independent_base_R3_shock_draws_present",
        "method_level_rows_represented")},indent=2))


if __name__=="__main__":
    main()
