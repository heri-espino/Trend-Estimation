"""Reproduce one J-pilot shock draw and compare Cortes-Toto's criteria.

This is a *method sanity/diagnostic* experiment on one already
specified Gaussian/non-Gaussian latent reconstruction realization,
using the EXACT same seed formula and generator as study J. It is
not 25-seed/10k-seed confirmation and never overwrites study J data.

Run:
python -m experiments.pooled_loocv_smoothness.run_cortes_criteria_case \
  --regime gaussian_iid --d 2 --n 50 --sigma-eta 0.5 \
  --R 3 --replicate 0 --mu-factor 1 --solver multibracket
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime,timezone
from pathlib import Path

import numpy as np

from .cortes_optimality_criteria import CRITERIA, PenalizedCriteria, choose
from .mean_difference_methods import particular_polynomial
from .run_nonzero_difference_mean import MeanScenario, compare_pool
from .run_nonzero_mu_nongaussian import (
    FINITE_REGIMES, NoiseShard, draw_pool, seed_for
)
from .run_nonzero_mean_multorder import ORDERS,LENGTHS,ETA_SDS,MU_FACTORS,_sha


def evaluate_case(*,regime:str,d:int,n:int,sigma_eta:float,
                  R:int,replicate:int,mu_factor:float,
                  solver="multibracket",scan_points=41):
    shard=NoiseShard(regime,d,n,sigma_eta,replicate,1,phase="pilot")
    if R not in (1,3) or mu_factor not in MU_FACTORS:
        raise ValueError("R=1,3 and a preregistered mu factor required")
    y0,tau0=draw_pool(shard,replicate)
    scenario=MeanScenario(n,sigma_eta,.3,mu_factor,d=d)
    p=particular_polynomial(n,d)
    y=y0[:R]+scenario.mu*p[None,:]
    truth=tau0[:R]+scenario.mu*p[None,:]
    methods=[]
    for mode in ("zero","joint","fixed"):
        fixed=scenario.mu if mode=="fixed" else None
        obj=PenalizedCriteria(y,order=d,mean_mode=mode,fixed_mu=fixed)
        for criterion in CRITERIA:
            result=choose(obj,criterion,solver=solver,scan_points=scan_points)
            fit=obj.trend(result.lam)
            methods.append({
                "method":f"{criterion}_{mode}_{solver}",
                "source":"Cortes-Toto et al. 2017: criterion; pooled and common-mu extension: this repo",
                "mean_mode":mode,
                "mean_is_true_oracle":mode=="fixed",
                "criterion":criterion,
                "solver":solver,
                "selected_lambda":result.lam,
                "selected_s_normalized":result.smoothness,
                "selected_s_original_guerrero":(n-d)*result.smoothness/n,
                "criterion_score":result.score,
                "reconstructed_true_trend_MSE":float(np.mean((fit-truth)**2)),
                "estimated_common_mu":result.mu_fit,
                "EDF_for_RN_observations":result.edf_total,
                "optimization_score_evaluations":result.evaluated,
                "boundary_flag":result.boundary,
                "truncated_positive_domain_for_BIC":criterion=="bic",
            })
        for smoothness in (.5,.8):
            result=obj.choose_fixed_smoothness(smoothness)
            fit=obj.trend(result.lam)
            methods.append({
                "method":f"controlled_S{smoothness}_{mode}",
                "source":"Guerrero 2007 controlled smoothness; predeclared normalized S level",
                "mean_mode":mode,
                "mean_is_true_oracle":mode=="fixed",
                "criterion":"exogenous_controlled_smoothness",
                "solver":"invert_smoothness",
                "selected_lambda":result.lam,
                "selected_s_normalized":result.smoothness,
                "selected_s_original_guerrero":(n-d)*result.smoothness/n,
                "criterion_score":None,
                "reconstructed_true_trend_MSE":float(np.mean((fit-truth)**2)),
                "estimated_common_mu":result.mu_fit,
                "EDF_for_RN_observations":result.edf_total,
                "optimization_score_evaluations":result.evaluated,
                "boundary_flag":result.boundary,
                "truncated_positive_domain_for_BIC":False,
            })
    # Existing eight entries are a baseline, not called "Cortes methods".
    reference=compare_pool(scenario,y,truth)
    report={
        "status":"single_shock_case_not_statistical_confirmation",
        "source_git_sha":_sha(),
        "generated_utc":datetime.now(timezone.utc).isoformat(),
        "reuses_J_pilot_seed_and_generator":True,
        "study_J_regime":regime,"d":d,"N":n,
        "sigma_eta_population_sd":sigma_eta,"sigma_epsilon":.3,
        "mu_over_sigma_epsilon":mu_factor,"actual_mu":scenario.mu,
        "R":R,"replicate":replicate,"seed":seed_for(shard,replicate),
        "methods":methods,
        "original_eight_method_comparators":[
            {"method":r["method"],
             "MSE_realized_latent":r["realized_true_trend_mse"],
             "selected_lambda":r["selected_lambda"],
             "estimated_mu":r["estimated_mu"]} for r in reference
        ],
        "guardrails":[
            "True realized latent trend used to evaluate MSE AFTER parameter choice only.",
            "Externally fixed mu=true is an infeasible oracle; fixed mu estimated once from full data is NOT honest CV.",
            "Pooled joint-mu CV uses exact leave-one-observation PRESS re-estimating mu.",
            "Pooled joint-mu GCV/AICc/BIC use total EDF including one common mean.",
            "BIC with unknown residual variance is unbounded as lambda->0; finite search cutoff is arbitrary, report boundaries.",
            "Uncorrected AIC excluded by Cortes-Toto et al. due unreliable behavior.",
            "Changing the numerical solver on the SAME criterion is a different experiment from comparing statistical criteria.",
            "Single shock is a proof-of-concept, not enough to recommend a method.",
        ]
    }
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--regime",choices=FINITE_REGIMES,default="gaussian_iid")
    p.add_argument("--d",type=int,choices=ORDERS,default=2)
    p.add_argument("--n",type=int,choices=LENGTHS,default=50)
    p.add_argument("--sigma-eta",type=float,choices=ETA_SDS,default=.5)
    p.add_argument("--R",type=int,choices=(1,3),default=3)
    p.add_argument("--replicate",type=int,default=0)
    p.add_argument("--mu-factor",type=float,choices=MU_FACTORS,default=1.)
    p.add_argument("--solver",choices=("bounded","multibracket"),
                   default="multibracket")
    p.add_argument("--scan-points",type=int,default=41)
    p.add_argument("--output",type=Path,default=None)
    a=p.parse_args()
    report=evaluate_case(
        regime=a.regime,d=a.d,n=a.n,sigma_eta=a.sigma_eta,
        R=a.R,replicate=a.replicate,mu_factor=a.mu_factor,
        solver=a.solver,scan_points=a.scan_points)
    if a.output is not None:
        if a.output.exists():
            raise FileExistsError(f"Refusing to overwrite {a.output}")
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({
        "case":{k:report[k] for k in (
            "study_J_regime","d","N","sigma_eta_population_sd",
            "mu_over_sigma_epsilon","R","replicate","seed")},
        "evaluated_criteria":len(report["methods"]),
        "existing_baselines":len(report["original_eight_method_comparators"]),
        "best_feasible_criterion_in_THIS_one_simulated_case":min(
            (v for v in report["methods"] if not v["mean_is_true_oracle"]),
            key=lambda v:v["reconstructed_true_trend_MSE"])["method"],
        "output":str(a.output) if a.output else None,
        "guardrail":"Single seed diagnostic; method winner cannot be chosen based on true latent MSE in real data.",
    },indent=2))


if __name__=="__main__":
    main()
