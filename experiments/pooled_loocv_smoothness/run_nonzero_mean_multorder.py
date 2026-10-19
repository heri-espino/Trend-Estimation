"""Manual, resumable large-sample nonzero-mu confirmation for d=1,2,3,4.

This is a NEW protocol; it never edits or overwrites the completed d=2
five-seed pilot. Each experiment fixes d, N and sigma_eta in advance.
A *base shock draw* of R=3 trajectories is reused for R=1 and five
mu-shifts, giving paired contrasts. 10,000 genuinely separate PRNG
seed streams per (d, N, eta) => 16 * 10,000 independent base draws.
All 8 original method labels and loss definitions are retained.

LARGE RUNS ARE NOT TRIGGERED ON PUSH. Run discrete non-overlapping
replicate shards manually; only one shard is held in memory at a time.
Default result files are gzip CSV, a JSON manifest with SHA256, and a
compact summary. Never commit all 12.8M rows directly to regular Git.

This runner exploits a mathematically exact identity:
for affine-equivariant selectors M, y_mu=y_0+mu*p and
tau_mu=tau_0+mu*p => lambda_M and true reconstruction error are
invariant while fitted_mu_M(y_mu)=fitted_mu_M(y_0)+mu.
The six equivariant rows can therefore be computed once at mu=0
per base draw, while only the two forced-mu=0 selectors must be
recomputed for nonzero shifts. Tests compare this fast path against
the unmodified eight-method implementation for small d=1..4 cases.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import os
import platform
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy

from .objective import PooledLOOCV
from .search import bounded_brent
from .variance_estimation import estimate_gaussian_differences
from .run_nonzero_difference_mean import (
    METHODS, MU_FACTORS, MeanScenario, draw_pool, compare_pool,
)

SEED_BASE = 82100000  # independent of old nonzero-mu pilot and all other projects
ORDERS = (1, 2, 3, 4)
LENGTHS = (50, 200)
ETA_SDS = (0.5, 2.0)
SIGMA_EPSILON = 0.3
FULL_REPLICATES = 10000
SHARD_SIZE = 100  # up to 8,000 rows/shard; manually parallelize different shards
ZERO_ML = "zero_mu_gaussian_difference_ml"
ZERO_CV = "zero_mu_pooled_loocv"
ORACLE = "known_mu_true_ratio_oracle"
GLS = "estimated_mu_gaussian_gls_ml"
CV_JOINT = "estimated_mu_fold_clean_pooled_loocv"
PLUGIN = "pooled_guerrero_plugin_mu_plus_gaussian_ml"


@dataclass(frozen=True)
class Shard:
    order: int
    n: int
    sigma_eta: float
    start: int
    count: int

    def __post_init__(self):
        if self.order not in ORDERS or self.n not in LENGTHS:
            raise ValueError("unsupported order or N")
        if self.sigma_eta not in ETA_SDS:
            raise ValueError("unsupported observation SD")
        if self.start < 0 or self.count < 1 or self.start+self.count > FULL_REPLICATES:
            raise ValueError("shard must lie in [0,10000) with positive count")

    @property
    def suffix(self):
        eta=f"{self.sigma_eta:g}"
        return (f"d{self.order}/N{self.n}/eta{eta}/"
                f"rep_{self.start:05d}_{self.start+self.count:05d}")

    @property
    def groups(self):
        return self.count * len(MU_FACTORS) * 2

    @property
    def rows(self):
        return self.groups * len(METHODS)


def seed_for(shard: Shard, replicate: int) -> int:
    """Unique numeric seed per independent (d,N,eta,replicate)."""
    if not shard.start <= replicate < shard.start+shard.count:
        raise ValueError("replicate outside this shard")
    return (SEED_BASE + shard.order*1_000_000
            + LENGTHS.index(shard.n)*200_000
            + ETA_SDS.index(shard.sigma_eta)*100_000
            + replicate)


def _sha():
    try:
        return subprocess.check_output(["git","rev-parse","HEAD"],
            text=True,stderr=subprocess.DEVNULL,timeout=3).strip()
    except (OSError,subprocess.SubprocessError):
        return None


def fast_rows(sc: MeanScenario, observed: np.ndarray, truth: np.ndarray,
              base_at_mu0: dict[str, dict]):
    """Return results identical to compare_pool under affine invariance.

    All equivariant methods are transformed from mu=0 rows, with all
    six invariant scores and reconstructed errors retained. Only the
    two misspecified zero-mean selectors change with mu.
    """
    if set(base_at_mu0) != set(METHODS):
        raise ValueError("complete eight-method mu=0 baseline required")
    if sc.mu_factor == 0.0:
        return [dict(base_at_mu0[name]) for name in METHODS]

    obj=PooledLOOCV(observed,order=sc.d)
    fitted_var=estimate_gaussian_differences(observed,obj.d,scan_points=61)
    br=bounded_brent(obj)
    replacements={}
    for method,lam,variance in [
        (ZERO_ML,fitted_var.lambda_ratio,fitted_var),
        (ZERO_CV,br.best.lam,None)
    ]:
        reconstructed=obj.trend(lam)
        residual=reconstructed-truth
        rec=dict(base_at_mu0[method])
        rec.update({
            "true_mu":sc.mu,
            "estimated_mu":0.,
            "mu_bias":-sc.mu,
            "selected_lambda":float(lam),
            "selected_s_nominal":obj.smoothness(lam),
            "realized_true_trend_mse":float(np.mean(residual*residual)),
            "realized_trend_mae":float(np.mean(np.abs(residual))),
            "reported_press_score":obj.score(lam),
            "estimated_sigma_eta2": (
                float(variance.sigma_eta2) if variance else float("nan")),
            "estimated_sigma_epsilon2": (
                float(variance.sigma_epsilon2) if variance else float("nan")),
        })
        replacements[method]=rec

    results=[]
    for method in METHODS:
        if method in replacements:
            results.append(replacements[method])
        else:
            rec=dict(base_at_mu0[method])
            rec["true_mu"]=sc.mu
            rec["estimated_mu"]=float(rec["estimated_mu"]+sc.mu)
            rec["mu_bias"]=float(rec["estimated_mu"]-sc.mu)
            results.append(rec)
    return results


def _new_summary():
    return {}


def add_summary(summary: dict, record: dict):
    key=(record["R"],record["mu_factor"],record["method"])
    slot=summary.setdefault(key,{
        "n":0,"mse_sum":0.,"mse_sum2":0.,
        "mae_sum":0.,"mu_abs_sum":0.,
        "lambda_inf":0})
    score=record["realized_true_trend_mse"]
    slot["n"]+=1
    slot["mse_sum"]+=score
    slot["mse_sum2"]+=score*score
    slot["mae_sum"]+=record["realized_trend_mae"]
    slot["mu_abs_sum"]+=abs(record["mu_bias"])
    slot["lambda_inf"]+=int(np.isinf(record["selected_lambda"]))


def summarize(summary: dict, expected_replicates: int):
    out=[]
    for (R,mu,method),value in sorted(summary.items()):
        n=value["n"]
        if n!=expected_replicates:
            raise ValueError("summary count does not match independent replicates")
        mse=value["mse_sum"]/n
        sample_var=max(0.,(value["mse_sum2"]-n*mse*mse)/(n-1)) if n>1 else None
        out.append({
            "R":R,"mu_factor":mu,"method":method,
            "independent_base_shock_draws":n,
            "mean_latent_trend_mse":mse,
            "sample_sd_latent_mse":None if sample_var is None else float(np.sqrt(sample_var)),
            "standard_error_latent_mse":None if sample_var is None else float(np.sqrt(sample_var/n)),
            "mean_absolute_latent_error":value["mae_sum"]/n,
            "mean_absolute_mu_estimation_error":value["mu_abs_sum"]/n,
            "infinite_lambda_count":value["lambda_inf"],
        })
    if len(out)!=2*len(MU_FACTORS)*len(METHODS):
        raise ValueError("incomplete experimental summary cells")
    return out


def calculate_shard(shard: Shard, out: Path, *, dry_run=False,
                    overwrite=False):
    manifest={
        "protocol":"nonzero_difference_mean_multorder_confirmatory_v1",
        "status":"planned" if dry_run else "executed_shard",
        "created_utc":datetime.now(timezone.utc).isoformat(),
        "source_git_sha":_sha(),
        "numpy":np.__version__,"scipy":scipy.__version__,
        "python":platform.python_version(),
        "difference_order_fixed":shard.order,"N":shard.n,
        "sigma_eta":shard.sigma_eta,"sigma_epsilon":SIGMA_EPSILON,
        "true_mu_factors":list(MU_FACTORS),
        "R_values":[1,3],"methods":list(METHODS),
        "seed_base":SEED_BASE,"seed_start_inclusive":shard.start,
        "seed_stop_exclusive":shard.start+shard.count,
        "seed_formula":"82100000 + d*1000000 + N_index*200000 + eta_index*100000 + replicate",
        "paired_mu_shifts_with_same_shocks":True,
        "R1_is_first_series_of_R3":True,
        "fast_path_equivariant_methods_computed_once_per_R_and_seed":True,
        "expected_independent_base_draws":shard.count,
        "expected_nested_treatment_pools":shard.groups,
        "expected_method_rows":shard.rows,
        "truth_used_to_select_parameters":False,
        "risk_target":"realized retrospective latent trend MSE",
        "statistical_unit":"independent (d,N,eta,replicate) R3 shock draw",
        "not_a_forecast_backtest":True,
        "no_large_results_committed_directly":True,
    }
    if dry_run:
        return manifest
    if out.exists():
        if not overwrite:
            raise FileExistsError(
                f"{out} exists; use distinct non-overlapping shards; "
                "never overwrite completed results accidentally")
        raise ValueError("overwrite is disabled to protect reproducibility")
    out.mkdir(parents=True,exist_ok=False)
    data_path=out/"method_comparison.csv.gz"
    summary_acc=_new_summary()
    count=0
    fields=None
    # Only local shard data are held transiently; data is compressed as written.
    with gzip.open(data_path,"wt",encoding="utf-8",newline="",
                   compresslevel=6) as f:
        writer=None
        for replicate in range(shard.start,shard.start+shard.count):
            seed=seed_for(shard,replicate)
            sc0=MeanScenario(shard.n,shard.sigma_eta,SIGMA_EPSILON,0.,d=shard.order)
            y0,tau0=draw_pool(sc0,3,seed)
            for R in (1,3):
                observed0,truth0=y0[:R],tau0[:R]
                baseline={r["method"]:r for r in compare_pool(sc0,observed0,truth0)}
                for factor in MU_FACTORS:
                    sc=MeanScenario(shard.n,shard.sigma_eta,SIGMA_EPSILON,
                                    factor,d=shard.order)
                    p_mu=(
                        sc.mu * np.asarray([
                            __import__("math").comb(i,shard.order)
                            for i in range(shard.n)],dtype=float)
                    )
                    observed=observed0+p_mu[None,:]
                    truth=truth0+p_mu[None,:]
                    result=fast_rows(sc,observed,truth,baseline)
                    for method in result:
                        row={
                            "replicate":replicate,"seed":seed,
                            "d":shard.order,"N":shard.n,
                            "sigma_eta":shard.sigma_eta,
                            "sigma_epsilon":SIGMA_EPSILON,
                            "mu_factor":factor,"R":R,
                            **method,
                        }
                        if writer is None:
                            fields=list(row)
                            writer=csv.DictWriter(f,fieldnames=fields)
                            writer.writeheader()
                        writer.writerow(row)
                        add_summary(summary_acc,row)
                        count+=1
    if count!=shard.rows:
        raise AssertionError("wrong number of per-method simulation records")
    # A digest of the actual gzip artifact, not a digest of the original
    # method-level data recovered from a different git revision.
    hash_obj=hashlib.sha256()
    with data_path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            hash_obj.update(block)
    manifest["actual_method_rows"]=count
    manifest["compressed_csv_sha256"]=hash_obj.hexdigest()
    manifest["compressed_csv_bytes"]=data_path.stat().st_size
    (out/"summary.json").write_text(
        json.dumps({"status":"completed_shard",
                    "by_R_mu_method":summarize(summary_acc,shard.count)},
                   indent=2)+"\n",encoding="utf-8")
    (out/"manifest.json").write_text(
        json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    return manifest


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--d",type=int,choices=ORDERS,required=True)
    p.add_argument("--n",type=int,choices=LENGTHS,required=True)
    p.add_argument("--sigma-eta",type=float,choices=ETA_SDS,required=True)
    p.add_argument("--start-replicate",type=int,default=0)
    p.add_argument("--count",type=int,default=1)
    p.add_argument("--dry-run",action="store_true")
    p.add_argument("--out-dir",type=Path,default=None)
    args=p.parse_args()
    shard=Shard(args.d,args.n,args.sigma_eta,
                args.start_replicate,args.count)
    out=args.out_dir or (Path("results/pooled_loocv_smoothness/guerrero/"
                          "nonzero_mean_multorder/confirmatory")/shard.suffix)
    result=calculate_shard(shard,out,dry_run=args.dry_run)
    print(json.dumps({"output_dir":str(out),**result},indent=2))


if __name__=="__main__":
    main()
