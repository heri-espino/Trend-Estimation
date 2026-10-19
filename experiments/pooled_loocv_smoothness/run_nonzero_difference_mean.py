"""Exploratory pooled observed-series LOOCV when E[D_d tau] = mu != 0.

Standalone experiment for the INDEPENDENT retrospective reconstruction
working paper. Do not modify or merge the different horizon-h forecasting
mean-difference paper. Analyst fixes d=2. Compare mu known, zero imposed,
Gaussian GLS mean estimated, and mean jointly fitted within LOOCV folds.

Every scenario holds observation-noise and difference innovations fixed
across different mu factors (common random numbers). R1 is the first
series of the corresponding R3 pool. These are PAIRED sensitivity
observations, not independent replications. Only simulated latent truth
is evaluated, never used by feasible parameter selectors.

This is NOT Guerrero's own joint MLE or forecast-CV estimator.
Guerrero's data plug-in mu=mean(D y) is separately documented.
"""

from __future__ import annotations

import argparse
import csv
import json
import platform
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy

from .objective import PooledLOOCV
from .search import bounded_brent
from .run_tail_noise import integrate_differences
from .variance_estimation import estimate_gaussian_differences
from .mean_difference_methods import (
    JointMeanPooledLOOCV, estimate_contrast_gaussian_mean,
    fitted_affine_trend, particular_polynomial,
)


METHODS = (
    "known_mu_true_ratio_oracle",
    "zero_mu_gaussian_difference_ml",
    "zero_mu_pooled_loocv",
    "known_mu_estimated_variance_ml",
    "known_mu_pooled_loocv",
    "pooled_guerrero_plugin_mu_plus_gaussian_ml",
    "estimated_mu_gaussian_gls_ml",
    "estimated_mu_fold_clean_pooled_loocv",
)
# These are ratios of difference mean to innovation STANDARD DEVIATION.
MU_FACTORS = (-1.0, -0.25, 0.0, 0.25, 1.0)
SEED_BASE = 69000000
FIXED_D = 2


@dataclass(frozen=True)
class MeanScenario:
    n: int
    sigma_eta: float
    sigma_epsilon: float
    mu_factor: float
    d: int = FIXED_D

    def __post_init__(self):
        if self.d not in (1,2,3,4) or self.n < 12:
            raise ValueError("require d in {1,2,3,4} and N>=12")
        if self.sigma_eta <= 0 or self.sigma_epsilon <= 0:
            raise ValueError("noise standard deviations must be >0")
        if not np.isfinite((self.sigma_eta,self.sigma_epsilon,self.mu_factor)).all():
            raise ValueError("scenario parameters must be finite")

    @property
    def mu(self):
        return self.mu_factor*self.sigma_epsilon

    @property
    def true_lambda(self):
        return (self.sigma_eta/self.sigma_epsilon)**2


def design(preset: str):
    if preset == "smoke":
        scenarios = [MeanScenario(24,.5,.3,f) for f in (-1.,0.,1.)]
        return scenarios,1,(1,3)
    if preset in ("pilot","confirmatory"):
        scenarios = [
            MeanScenario(n,eta,.3,mu_factor)
            for n in (50,200) for eta in (.5,2.0)
            for mu_factor in MU_FACTORS
        ]
        return scenarios,5 if preset=="pilot" else 100,(1,3)
    raise ValueError("unknown preset")


def shared_seed(base: int, n: int, sigma_eta: float, replicate: int):
    """Each mu setting gets EXACT same random innovations and observations."""
    n_index={24:0,50:1,200:2}[n]
    eta_index={.5:0,2.0:1}[sigma_eta]
    return base + n_index*10000 + eta_index*1000 + replicate


def _integrate_order(innovation: np.ndarray, order: int) -> np.ndarray:
    """Generate integrated stochastic trend with zero higher-order drift.

    Retain the historical implementation for d=1,2,3. d=4 uses
    repeated cumulative sums of the padded innovations, avoiding
    unstable high-order explicit autoregressive recurrences.
    The deterministic initial mean is the same line .02*t.
    """
    if order in (1,2,3):
        return integrate_differences(innovation, order)
    if order != 4:
        raise ValueError("unsupported integration order")
    n=len(innovation)+order
    result=np.concatenate((np.zeros(order),np.asarray(innovation,dtype=float)))
    for _ in range(order):
        result=np.cumsum(result)
    return result + .02*np.arange(n)


def draw_pool(sc: MeanScenario,R: int,seed: int):
    if R < 1:
        raise ValueError("R must be >=1")
    rng=np.random.default_rng(seed)
    p=particular_polynomial(sc.n,sc.d)
    truths,ys=[],[]
    for _ in range(R):
        centered_eps=sc.sigma_epsilon*rng.standard_normal(sc.n-sc.d)
        baseline_tau=_integrate_order(centered_eps,sc.d)
        tau=baseline_tau+sc.mu*p
        eta=sc.sigma_eta*rng.standard_normal(sc.n)
        truths.append(tau)
        ys.append(tau+eta)
    return np.asarray(ys),np.asarray(truths)


def compare_pool(sc: MeanScenario,y: np.ndarray,truth: np.ndarray):
    base=PooledLOOCV(y,order=sc.d)
    p=particular_polynomial(sc.n,sc.d)
    # Fixed and EXOGENOUS mu uses a shifted series, so PRESS correctly
    # deletes y_i but the externally supplied mu never changes in folds.
    zero_obj=base
    oracle_mu_obj=PooledLOOCV(y-sc.mu*p[None,:],order=sc.d)
    joint_obj=JointMeanPooledLOOCV(y,order=sc.d)

    zero_var=estimate_gaussian_differences(y,base.d,scan_points=61)
    oracle_mean_var=estimate_contrast_gaussian_mean(
        y,base.d,fixed_mu=sc.mu,scan_points=61)
    fitted_mean_var=estimate_contrast_gaussian_mean(
        y,base.d,fixed_mu=None,scan_points=61)
    # Guerrero (2007) uses an observed d-th difference mean plug-in
    # per series/window. This explicitly POOLED analogue uses a common
    # mean across R comparable series; the conditional variance ML step
    # that follows is OUR extension, not Guerrero's published procedure.
    pooled_plugin_mu=float(np.mean(y@base.d.T))
    plugin_var=estimate_contrast_gaussian_mean(
        y,base.d,fixed_mu=pooled_plugin_mu,scan_points=61)
    zero_brent=bounded_brent(zero_obj)
    oracle_mean_brent=bounded_brent(oracle_mu_obj)
    joint_brent=bounded_brent(joint_obj)
    fitted_cv_mu=joint_obj.fitted_mu(joint_brent.best.lam)

    entries = (
        (METHODS[0],sc.true_lambda,sc.mu,"oracle_known_mu_and_variance",None),
        (METHODS[1],zero_var.lambda_ratio,0.,"imposed_zero_mean",zero_var),
        (METHODS[2],zero_brent.best.lam,0.,"imposed_zero_mean",None),
        (METHODS[3],oracle_mean_var.variance.lambda_ratio,sc.mu,
         "oracle_known_mu",oracle_mean_var.variance),
        (METHODS[4],oracle_mean_brent.best.lam,sc.mu,
         "oracle_known_mu",None),
        (METHODS[5],plugin_var.variance.lambda_ratio,
         pooled_plugin_mu,"guerrero_style_pooled_plugin_plus_our_ML",
         plugin_var.variance),
        (METHODS[6],fitted_mean_var.variance.lambda_ratio,
         fitted_mean_var.mu,"gls_full_data_estimated_mu",
         fitted_mean_var.variance),
        (METHODS[7],joint_brent.best.lam,fitted_cv_mu,
         "fold_clean_joint_penalized_mu",None),
    )
    rows=[]
    for method,lam,mu_est,kind,var in entries:
        if method==METHODS[7]:
            fitted=joint_obj.trend(lam)
            validation=joint_obj.score(lam)
            validation_kind="exact_fold_reestimated_mu_PRESS"
        else:
            fitted=fitted_affine_trend(base,lam,mu_est)
            # If mu_est was learned from ALL observed data, the fixed-mu
            # PRESS score below is a DIAGNOSTIC, NOT leak-free validation:
            # only actual CV-selected joint mu re-fits mu within folds.
            residual_obj=(zero_obj if mu_est==0.0 else
                oracle_mu_obj if mu_est==sc.mu and kind.startswith("oracle") else
                PooledLOOCV(y-mu_est*p[None,:],order=sc.d))
            validation=residual_obj.score(lam)
            validation_kind=("known_exogenous_mu_PRESS" if kind.startswith("oracle")
                else "imposed_zero_mu_PRESS" if kind=="imposed_zero_mean"
                else "frozen_full_data_estimated_mu_PRESS_diagnostic_NOT_CV")
        rows.append({
            "method":method,
            "true_mu":sc.mu,
            "estimated_mu":float(mu_est),
            "mu_bias":float(mu_est-sc.mu),
            "mu_status":kind,
            "true_lambda":sc.true_lambda,
            "selected_lambda":float(lam),
            "selected_s_nominal":base.smoothness(lam),
            "realized_true_trend_mse":float(np.mean((fitted-truth)**2)),
            "realized_trend_mae":float(np.mean(np.abs(fitted-truth))),
            "reported_press_score":float(validation),
            "reported_press_kind":validation_kind,
            "estimated_sigma_eta2": (
                float(var.sigma_eta2) if var is not None else
                sc.sigma_eta**2 if method==METHODS[0] else float("nan")),
            "estimated_sigma_epsilon2":(
                float(var.sigma_epsilon2) if var is not None else
                sc.sigma_epsilon**2 if method==METHODS[0] else float("nan")),
            "data_selected_mu_increases_effective_degrees_of_freedom":
                method in (METHODS[5],METHODS[6],METHODS[7]),
        })
    return rows


def summarize(rows: list[dict]) -> dict:
    paired={}
    for row in rows:
        key=(row["scenario_id"],row["replicate"],row["R"])
        methods=paired.setdefault(key,{})
        if row["method"] in methods:
            raise ValueError("duplicate method in pool")
        methods[row["method"]]=row
    if not paired or any(set(slot)!=set(METHODS) for slot in paired.values()):
        raise ValueError("incomplete method comparison")
    out=[]
    for factor in MU_FACTORS:
        subset=[slot for slot in paired.values() if
                slot[METHODS[0]]["R"]==3 and
                slot[METHODS[0]]["mu_factor"]==factor]
        if not subset: continue
        out.append({
            "mu_over_sigma_epsilon":factor,
            "primary_R3_pools":len(subset),
            "methods":[{
                "name":method,
                "mean_realized_trend_mse":float(np.mean([
                    slot[method]["realized_true_trend_mse"] for slot in subset])),
                "median_realized_trend_mse":float(np.median([
                    slot[method]["realized_true_trend_mse"] for slot in subset])),
                "mean_abs_mu_error":float(np.mean([
                    abs(slot[method]["mu_bias"]) for slot in subset])),
                "selected_infinite_lambda_count":int(sum(
                    bool(np.isinf(slot[method]["selected_lambda"])) for slot in subset)),
            } for method in METHODS],
        })
    return {
        "status":"exploratory_only_not_confirmatory",
        "primary_R3_pools":sum(slot[METHODS[0]]["R"]==3 for slot in paired.values()),
        "total_nested_pools":len(paired),
        "total_method_rows":len(rows),
        "by_mu_factor_R3":out,
        "guardrails":[
            "The source Guerrero already studied nonzero mu and an observed-difference plug-in.",
            "Gaussian contrast joint mu/a/b estimation is a proposed implementation, not Guerrero's published MLE algorithm.",
            "The fold-clean pooled CV profiles one common mu jointly in the training penalty, not a historical h-step mean.",
            "For full-data GLS estimated mu, frozen-mu PRESS is diagnostic only and must not be compared as leak-free CV.",
            "Finite five-seed per-cell pilot cannot demonstrate distribution-independent superiority.",
            "S_nominal is a penalty-coordinate only; its degrees-of-freedom meaning changes if mu is estimated.",
            "Both R=1 and R=3 and the mu-factor grid share random innovations at the same N/eta/replicate.",
        ],
    }


def _sha():
    try:
        return subprocess.check_output(["git","rev-parse","HEAD"],
             text=True,stderr=subprocess.DEVNULL,timeout=3).strip()
    except (OSError,subprocess.SubprocessError):
        return None


def _plot_example(out_dir: Path, sc: MeanScenario, y: np.ndarray,
                  truth: np.ndarray, methods: list[dict]):
    """Plot actual realized reconstruction errors at one preselected seed."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    base = PooledLOOCV(y, order=sc.d)
    selected = {
        "known_mu_true_ratio_oracle": "Known mu and variances (oracle)",
        "zero_mu_pooled_loocv": "LOOCV, mu forced to 0",
        "pooled_guerrero_plugin_mu_plus_gaussian_ml": "Pooled observed-difference plug-in",
        "estimated_mu_gaussian_gls_ml": "Gaussian GLS estimated mu",
        "estimated_mu_fold_clean_pooled_loocv": "Fold-clean pooled LOOCV mu",
    }
    data = {item["method"]: item for item in methods}
    fig, ax = plt.subplots(figsize=(10, 4.8))
    x = np.arange(sc.n)
    for name, label in selected.items():
        item = data[name]
        fit = fitted_affine_trend(base, item["selected_lambda"],
                                   item["estimated_mu"])
        ax.plot(x, fit[0] - truth[0], label=label, linewidth=1.6)
    ax.axhline(0, linestyle="--", linewidth=1, color="grey")
    ax.set_xlabel("Observation index")
    ax.set_ylabel("Fitted minus true latent trend")
    ax.set_title(f"Simulated nonzero difference mean, d={sc.d}, mu={sc.mu:g}")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "example_latent_trend_errors.png", dpi=160)
    plt.close(fig)


def _plot_mu_sensitivity(out_dir: Path, summary: dict):
    """Descriptive only: mean errors aggregate different N/noise levels."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    groups = summary["by_mu_factor_R3"]
    if not groups:
        raise ValueError("no R3 mean scenarios available")
    x = [g["mu_over_sigma_epsilon"] for g in groups]
    selected = {
        "known_mu_true_ratio_oracle": "Known mu, known ratio (oracle)",
        "zero_mu_pooled_loocv": "Incorrect mu=0 LOOCV",
        "pooled_guerrero_plugin_mu_plus_gaussian_ml": "Pooled Guerrero-style plug-in + ML",
        "estimated_mu_gaussian_gls_ml": "Estimated GLS mu + ML",
        "estimated_mu_fold_clean_pooled_loocv": "Estimated mu + fold-clean LOOCV",
    }
    fig, ax = plt.subplots(figsize=(9.5, 5))
    for name, label in selected.items():
        mean_mse = [
            next(v["mean_realized_trend_mse"] for v in g["methods"]
                 if v["name"] == name)
            for g in groups
        ]
        ax.plot(x, mean_mse, marker="o", label=label)
    ax.set_xlabel("True mu / sigma_epsilon")
    ax.set_ylabel("Mean true latent trend reconstruction MSE")
    ax.set_yscale("log")
    ax.set_title("Exploratory pooled reconstruction across mu shifts (R=3)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "mean_shift_true_trend_mse_R3.png", dpi=160)
    plt.close(fig)


def execute(preset: str,out_dir: Path,dry_run: bool=False):
    scenarios,replicates,R_values=design(preset)
    base=SEED_BASE if preset!="confirmatory" else SEED_BASE+1000000
    manifest={
        "protocol":"nonzero_difference_mean_gaussian_ML_pooled_LOOCV_v1",
        "status":"planned" if dry_run else "executed",
        "created_utc":datetime.now(timezone.utc).isoformat(),
        "git_sha":_sha(),"python":platform.python_version(),
        "numpy":np.__version__,"scipy":scipy.__version__,
        "order_d_fixed":FIXED_D,
        "seed_base":base,"rng":"numpy.random.default_rng",
        "seed_formula":"base+N_index*10000+sigma_eta_index*1000+replicate",
        "shared_noise_across_mu_factor":True,
        "R1_nested_in_R3":True,
        "R_values":list(R_values),
        "scenario_count":len(scenarios),
        "replicates_per_scenario":replicates,
        "sigma_epsilon_fixed":.3,
        "mean_factors":list(sorted({s.mu_factor for s in scenarios})),
        "scenarios":[{
            "scenario_id":i,"n":s.n,"d":s.d,
            "sigma_eta":s.sigma_eta,"sigma_epsilon":s.sigma_epsilon,
            "mu_factor":s.mu_factor,"true_mu":s.mu,
            "true_lambda":s.true_lambda} for i,s in enumerate(scenarios)],
        "methods":list(METHODS),
        "expected_nested_pools":len(scenarios)*replicates*len(R_values),
        "expected_method_rows":len(scenarios)*replicates*len(R_values)*len(METHODS),
        "trend_generator":"D2 tau = mu + centered iid Gaussian innovation; fixed initial intercept 0, slope .02",
        "observed_noise":"independent iid centered Gaussian, V=I",
        "truth_used_in_parameter_tuning":False,
        "estimated_mu_selected_within_LOOCV_folds":True,
        "guerrero_plugin_is_pooled_extension_not_original_per_series":True,
        "nominal_s_not_data_selected_mu_edf":True,
    }
    if dry_run:
        print(json.dumps(manifest,indent=2))
        return manifest
    out_dir.mkdir(parents=True,exist_ok=True)
    records=[]
    for scenario_id,sc in enumerate(scenarios):
        for rep in range(replicates):
            seed=shared_seed(base,sc.n,sc.sigma_eta,rep)
            for R in R_values:
                y,tau=draw_pool(sc,R,seed)
                calculated=compare_pool(sc,y,tau)
                if (rep==0 and R==3 and sc.mu_factor>0
                    and sc.n==scenarios[0].n and
                    sc.sigma_eta==scenarios[0].sigma_eta
                    and not (out_dir/"example_latent_trend_errors.png").exists()):
                    _plot_example(out_dir,sc,y,tau,calculated)
                for item in calculated:
                    records.append({
                        "scenario_id":scenario_id,
                        "replicate":rep,"seed":seed,"R":R,
                        "n":sc.n,"d":sc.d,
                        "sigma_eta":sc.sigma_eta,
                        "sigma_epsilon":sc.sigma_epsilon,
                        "mu_factor":sc.mu_factor,
                        **item,
                    })
    summary=summarize(records)
    _plot_mu_sensitivity(out_dir,summary)
    with (out_dir/"method_comparison.csv").open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(records[0]))
        writer.writeheader();writer.writerows(records)
    (out_dir/"summary.json").write_text(
        json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    manifest["actual_method_rows"]=len(records)
    (out_dir/"manifest.json").write_text(
        json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({
        "status":"executed",
        "nested_pools":summary["total_nested_pools"],
        "method_rows":len(records),
        "output":str(out_dir),
        "mu_groups":[{"factor":g["mu_over_sigma_epsilon"],
                     "R3_pools":g["primary_R3_pools"]}
                     for g in summary["by_mu_factor_R3"]],
    },indent=2))
    return summary


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--preset",choices=("smoke","pilot","confirmatory"),
                   default="smoke")
    p.add_argument("--out-dir",type=Path,default=None)
    p.add_argument("--dry-run",action="store_true")
    a=p.parse_args()
    out=a.out_dir or (Path("results/pooled_loocv_smoothness/guerrero") /
                      "nonzero_difference_mean" / a.preset)
    execute(a.preset,out,dry_run=a.dry_run)


if __name__=="__main__":
    main()
