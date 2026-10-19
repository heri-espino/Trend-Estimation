"""Study K: exact matched-seed 25-draw replay of the completed Study J pilot.

26 reconstruction methods: 18 new Cortes-Toto/Guerrero criterion policies
(4 criteria + 2 externally PREDECLARED smoothness values) x 3 mean
modes (zero, joint, known fixed mu oracle), plus 8 previous estimators.
One numerical search algorithm is held FIXED per campaign (default
multibracket) so objective and solver effects do not get confounded.

The original Study J generator, seed identities, R3 shock pools and five
paired mu interventions are preserved exactly. No 4800 new independent
draws are produced; this is a REPLAY of 4800 prior independent shock pools
and 48k paired/nested treatment evaluations. As in prior studies, the
realized latent stochastic tau is used only to evaluate the reconstruction,
never to choose lambda or mu for feasible estimators.

Six shift-equivariant new joint/exogenous-mu results are computed ONCE
per independent seed/R and reused for five mu interventions. Only the
fixed-zero-mean arm requires refitting separately at each nonzero mu.
The original 8 comparators are reproduced by the prior fast_rows()
affine-equivariant implementation on exactly the same generator data.

Results are immutable 25-base-shock shards with gzip individual rows,
mean/SD summaries and paired per-shock MSE differences versus previous
fitted-mean ML/CV, plus source SHA256/provenance. Raw results are ignored
by git. Launching all 192 shards is user-controlled, NEVER CI/push.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import platform
from dataclasses import dataclass
from datetime import datetime,timezone
from pathlib import Path

import numpy as np
import scipy

from .cortes_optimality_criteria import CRITERIA, PenalizedCriteria, choose
from .mean_difference_methods import particular_polynomial
from .run_nonzero_difference_mean import (
    MeanScenario, METHODS as PRIOR_METHODS, MU_FACTORS, compare_pool
)
from .run_nonzero_mean_multorder import fast_rows, _sha
from .run_nonzero_mu_nongaussian import (
    FINITE_REGIMES, NoiseShard, draw_pool, seed_for, PILOT_REPS,
    SIGMA_EPSILON, LENGTHS, ETA_SDS, ORDERS
)

PROTOCOL = "cortes_criteria_paired_J25_replay_v1"
CONTROLLED_S = (0.5,0.8)
MEAN_MODES = ("zero","joint","fixed")
DEFAULT_SOLVER = "multibracket"
DEFAULT_SCAN_POINTS = 41
OLD_PREFIX="existing__"
NEW_METHODS=tuple(
    [f"{criterion}_{mode}" for mode in MEAN_MODES for criterion in CRITERIA]
    + [f"controlled_S{smooth:g}_{mode}"
       for mode in MEAN_MODES for smooth in CONTROLLED_S]
)
OLD_METHODS=tuple(OLD_PREFIX+m for m in PRIOR_METHODS)
ALL_METHODS=NEW_METHODS+OLD_METHODS
# First minus second: positive means the NEW method is worse.
ANCHORS = (
    OLD_PREFIX+"estimated_mu_gaussian_gls_ml",
    OLD_PREFIX+"estimated_mu_fold_clean_pooled_loocv",
    OLD_PREFIX+"pooled_guerrero_plugin_mu_plus_gaussian_ml",
)
# Exact, prespecified comparisons of similar statistical selectors.
PAIRS=tuple([(new,ref) for new in NEW_METHODS
                 if not new.endswith("_fixed") for ref in ANCHORS]
            + [("gcv_joint","cv_joint"),("aicc_joint","cv_joint"),
               ("bic_joint","cv_joint"),("gcv_zero","cv_zero"),
               ("aicc_zero","cv_zero"),("bic_zero","cv_zero")])
assert len(ALL_METHODS)==26 and len(PAIRS)==42


@dataclass(frozen=True)
class CriteriaShard:
    regime:str
    d:int
    n:int
    sigma_eta:float
    start:int
    count:int

    def __post_init__(self):
        if self.regime not in FINITE_REGIMES or self.d not in ORDERS or self.n not in LENGTHS or self.sigma_eta not in ETA_SDS:
            raise ValueError("Invalid paired-criteria pilot stratum")
        if not 0 <= self.start < self.start+self.count <= PILOT_REPS:
            raise ValueError("Replay seed indices must lie in J-pilot [0,25)")

    @property
    def suffix(self):
        return (f"{self.regime}/d{self.d}/N{self.n}/eta{self.sigma_eta:g}/"
                f"rep_{self.start:05d}_{self.start+self.count:05d}")

    @property
    def shock_pools(self):
        return self.count

    @property
    def treatment_pools(self):
        return self.count*2*len(MU_FACTORS)

    @property
    def rows(self):
        return self.treatment_pools*len(ALL_METHODS)


def evaluate_new(y,truth,d:int,mu:float,mode:str,solver:str,scan_points:int):
    obj=PenalizedCriteria(y,order=d,mean_mode=mode,
                          fixed_mu=mu if mode=="fixed" else None)
    rows=[]
    for criterion in CRITERIA:
        selected=choose(obj,criterion,solver=solver,scan_points=scan_points)
        fitted=obj.trend(selected.lam)
        rows.append({
            "method":f"{criterion}_{mode}",
            "family":"cortes_2017_criterion_extended_to_shared_mu",
            "criterion":criterion,
            "mean_mode":mode,
            "requires_true_mu_oracle":mode=="fixed",
            "selected_lambda":selected.lam,
            "selected_s_nominal":selected.smoothness,
            "estimated_mu":selected.mu_fit,
            "edf_total":selected.edf_total,
            "criterion_score":selected.score,
            "criterion_calls":selected.evaluated,
            "boundary":selected.boundary,
            "solver":solver,
            "true_trend_mse":float(np.mean((fitted-truth)**2)),
            "true_trend_mae":float(np.mean(np.abs(fitted-truth))),
        })
    for s in CONTROLLED_S:
        selected=obj.choose_fixed_smoothness(s)
        fitted=obj.trend(selected.lam)
        rows.append({
            "method":f"controlled_S{s:g}_{mode}",
            "family":"predeclared_guerrero_smoothness_policy",
            "criterion":"exogenous_fixed_smoothness",
            "mean_mode":mode,
            "requires_true_mu_oracle":mode=="fixed",
            "selected_lambda":selected.lam,
            "selected_s_nominal":selected.smoothness,
            "estimated_mu":selected.mu_fit,
            "edf_total":selected.edf_total,
            "criterion_score":None,
            "criterion_calls":selected.evaluated,
            "boundary":None,
            "solver":"inverse_smoothness",
            "true_trend_mse":float(np.mean((fitted-truth)**2)),
            "true_trend_mae":float(np.mean(np.abs(fitted-truth))),
        })
    return rows


def _new_baseline(prior: list[dict]):
    if len(prior)!=len(PRIOR_METHODS):
        raise ValueError("The original eight-method baseline is incomplete")
    return [{
        "method":OLD_PREFIX+x["method"],"family":"existing_study_J_estimator",
        "criterion":"prior_method_definition",
        "mean_mode":x["mu_status"],
        "requires_true_mu_oracle":x["method"] in (
            "known_mu_true_ratio_oracle","known_mu_estimated_variance_ml",
            "known_mu_pooled_loocv"),
        "selected_lambda":x["selected_lambda"],
        "selected_s_nominal":x["selected_s_nominal"],
        "estimated_mu":x["estimated_mu"],
        "edf_total":None,"criterion_score":None,"criterion_calls":None,
        "boundary":None,"solver":"existing_selector",
        "true_trend_mse":x["realized_true_trend_mse"],
        "true_trend_mae":x["realized_trend_mae"],
    } for x in prior]


def _reuse_equivariant(rows: list[dict],mu:float):
    """Re-use same latent-MSE from the EXACT common polynomial shift."""
    return [{**x,"estimated_mu":float(x["estimated_mu"]+mu)}
            for x in rows]


def evaluate_shock(shard:CriteriaShard,rep:int,
                   solver=DEFAULT_SOLVER,scan_points=DEFAULT_SCAN_POINTS):
    original=NoiseShard(shard.regime,shard.d,shard.n,shard.sigma_eta,
                        rep,1,phase="pilot")
    y0,tau0=draw_pool(original,rep)
    p=particular_polynomial(shard.n,shard.d)
    result=[]
    for R in (1,3):
        data0=y0[:R]
        truth0=tau0[:R]
        sc0=MeanScenario(shard.n,shard.sigma_eta,SIGMA_EPSILON,0.,d=shard.d)
        baseline={r["method"]:r for r in compare_pool(sc0,data0,truth0)}
        joint_base=evaluate_new(data0,truth0,shard.d,0.,"joint",solver,scan_points)
        known_base=evaluate_new(data0,truth0,shard.d,0.,"fixed",solver,scan_points)
        # At true mu=0, imposed zero and known zero are the same fit/score.
        zero_base=[{**x,"method":x["method"].replace("_fixed","_zero"),
                    "mean_mode":"zero","requires_true_mu_oracle":False}
                   for x in known_base]
        for factor in MU_FACTORS:
            sc=MeanScenario(shard.n,shard.sigma_eta,SIGMA_EPSILON,factor,d=shard.d)
            y=data0+sc.mu*p[None,:]
            truth=truth0+sc.mu*p[None,:]
            zero=(zero_base if factor==0 else
                  evaluate_new(y,truth,shard.d,0.,"zero",solver,scan_points))
            joint=_reuse_equivariant(joint_base,sc.mu)
            fixed=_reuse_equivariant(known_base,sc.mu)
            previous=_new_baseline(fast_rows(sc,y,truth,baseline))
            combined=zero+joint+fixed+previous
            if len(combined)!=len(ALL_METHODS) or {x["method"] for x in combined}!=set(ALL_METHODS):
                raise ValueError("Method design incomplete or duplicated")
            for x in combined:
                result.append({
                    "regime":shard.regime,"d":shard.d,"N":shard.n,
                    "sigma_eta":shard.sigma_eta,
                    "sigma_epsilon":SIGMA_EPSILON,
                    "replicate":rep,"seed":seed_for(original,rep),
                    "R":R,"mu_factor":factor,
                    **x,
                })
    return result


def _accumulate(stat:dict, row:dict):
    key=(row["R"],row["mu_factor"],row["method"])
    x=row["true_trend_mse"]
    a=stat.setdefault(key,{"n":0,"sum":0.,"sum2":0.,"mae":0.,
                            "lambda_inf":0,"lower_boundary":0})
    a["n"]+=1;a["sum"]+=x;a["sum2"]+=x*x
    a["mae"]+=row["true_trend_mae"]
    a["lambda_inf"]+=int(np.isinf(row["selected_lambda"]))
    a["lower_boundary"]+=int(row["boundary"]=="truncated_lower_lambda_limit")


def _pair_accumulate(pairs:dict,R:int,mu:float,rows:list[dict]):
    table={x["method"]:x["true_trend_mse"] for x in rows}
    for first,second in PAIRS:
        delta=table[first]-table[second]
        key=(R,mu,first,second)
        a=pairs.setdefault(key,{"n":0,"sum":0.,"sum2":0.,"second_win":0})
        a["n"]+=1;a["sum"]+=delta;a["sum2"]+=delta*delta
        a["second_win"]+=int(delta>0)


def _summary(stat:dict,expected:int,*,paired:bool):
    out=[]
    for key,v in sorted(stat.items()):
        n=v["n"]
        if n!=expected:
            raise ValueError("Wrong independent seed count for method/paired cell")
        mean=v["sum"]/n
        var=max(0.,(v["sum2"]-n*mean*mean)/(n-1)) if n>1 else None
        if paired:
            R,mu,first,second=key
            out.append({
                "R":R,"mu_factor":mu,"first_method":first,
                "second_method":second,"independent_base_shock_draws":n,
                "mean_paired_MSE_first_minus_second":mean,
                "sample_sd_paired_difference":None if var is None else float(np.sqrt(var)),
                "diagnostic_paired_SE":None if var is None else float(np.sqrt(var/n)),
                "second_lower_realized_MSE_count":v["second_win"],
            })
        else:
            R,mu,method=key
            out.append({
                "R":R,"mu_factor":mu,"method":method,
                "independent_base_shock_draws":n,
                "mean_realized_trend_MSE":mean,
                "sample_sd_realized_trend_MSE":None if var is None else float(np.sqrt(var)),
                "diagnostic_SE":None if var is None else float(np.sqrt(var/n)),
                "mean_realized_trend_MAE":v["mae"]/n,
                "infinite_lambda_count":v["lambda_inf"],
                "truncated_lower_domain_count":v["lower_boundary"],
            })
    if len(out)!=(2*len(MU_FACTORS)*(len(PAIRS) if paired else len(ALL_METHODS))):
        raise ValueError("Missing required method or paired contrasts")
    return out


def calculate_shard(shard:CriteriaShard,out:Path,*,solver=DEFAULT_SOLVER,
                    scan_points=DEFAULT_SCAN_POINTS,dry_run=False):
    if solver not in ("multibracket","bounded") or scan_points<5:
        raise ValueError("Invalid numerical solver or search grid")
    run_sha=_sha()
    source=NoiseShard(shard.regime,shard.d,shard.n,shard.sigma_eta,
                      shard.start,shard.count,phase="pilot")
    man={
        "protocol":PROTOCOL,"status":"planned" if dry_run else "executed_shard",
        "study_J_original_seed_bank_reused":True,
        "statistical_unit":"one independent original J-pilot 3-series shock draw",
        "original_study_J_source_sha":"33c8eef425e56c6e17b9a5f3d331869e2af99c30",
        "source_git_sha":run_sha,"created_utc":datetime.now(timezone.utc).isoformat(),
        "regime":shard.regime,"difference_order_fixed":shard.d,
        "N":shard.n,"sigma_eta_population_SD":shard.sigma_eta,
        "sigma_epsilon_population_SD":SIGMA_EPSILON,
        "R_values":[1,3],"mu_factors":list(MU_FACTORS),
        "methods":list(ALL_METHODS),"paired_comparisons":[list(x) for x in PAIRS],
        "search_solver":solver,"search_scan_points":scan_points,
        "positive_log_lambda_search_bounds":[-20,35],
        "BIC_positive_domain_unbounded_logRSS_excluded":True,
        "fixed_true_mu_modes_infeasible_oracle":True,
        "controlled_smoothness_exogenous_preset":list(CONTROLLED_S),
        "conditional_Gaussian_quasi_MLE_outside_normality":True,
        "student_t3_infinite_fourth_moment_caution":True,
        "Cauchy_excluded":True,
        "source_phase":"J_pilot_not_a_new_independent_replication_cohort",
        "paired_same_random_shocks_across_mu":True,
        "R1_first_series_of_R3":True,
        "seed_start_inclusive":shard.start,
        "seed_stop_exclusive":shard.start+shard.count,
        "expected_independent_shock_draws":shard.shock_pools,
        "expected_treatment_pools":shard.treatment_pools,
        "expected_method_rows":shard.rows,
        "truth_used_for_feasible_selector":False,
        "numpy":np.__version__,"scipy":scipy.__version__,
        "python":platform.python_version(),
    }
    if dry_run:return man
    if out.exists():raise FileExistsError(f"Output exists; never overwrite raw results: {out}")
    out.mkdir(parents=True)
    method_acc,pair_acc={},{}
    csv_path=out/"method_comparison.csv.gz"
    total=0
    with gzip.open(csv_path,"wt",encoding="utf-8",newline="",compresslevel=5) as f:
        writer=None
        for rep in range(shard.start,shard.start+shard.count):
            cases=evaluate_shock(shard,rep,solver,scan_points)
            grouped={}
            for row in cases:
                if writer is None:
                    writer=csv.DictWriter(f,fieldnames=list(row))
                    writer.writeheader()
                writer.writerow(row)
                _accumulate(method_acc,row)
                grouped.setdefault((row["R"],row["mu_factor"]),[]).append(row)
                total+=1
            for (R,mu),records in grouped.items():
                _pair_accumulate(pair_acc,R,mu,records)
    if total!=shard.rows:raise ValueError("Incomplete observed pilot replay")
    sha=hashlib.sha256()
    with csv_path.open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):sha.update(block)
    man.update({"actual_method_rows":total,
                "compressed_csv_bytes":csv_path.stat().st_size,
                "compressed_csv_sha256":sha.hexdigest()})
    (out/"summary.json").write_text(json.dumps({
        "status":"completed_shard",
        "by_R_mu_method":_summary(method_acc,shard.count,paired=False),
        "paired_R_mu_method_contrasts":_summary(pair_acc,shard.count,paired=True),
    },indent=2)+"\n",encoding="utf-8")
    (out/"manifest.json").write_text(json.dumps(man,indent=2)+"\n",
                                     encoding="utf-8")
    return man


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--regime",choices=FINITE_REGIMES,required=True)
    p.add_argument("--d",type=int,choices=ORDERS,required=True)
    p.add_argument("--n",type=int,choices=LENGTHS,required=True)
    p.add_argument("--sigma-eta",type=float,choices=ETA_SDS,required=True)
    p.add_argument("--start",type=int,default=0)
    p.add_argument("--count",type=int,default=1)
    p.add_argument("--solver",choices=("multibracket","bounded"),default=DEFAULT_SOLVER)
    p.add_argument("--scan-points",type=int,default=DEFAULT_SCAN_POINTS)
    p.add_argument("--root",type=Path,default=Path(
        "results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/pilot"))
    p.add_argument("--dry-run",action="store_true")
    a=p.parse_args()
    sh=CriteriaShard(a.regime,a.d,a.n,a.sigma_eta,a.start,a.count)
    out=a.root/sh.suffix
    result=calculate_shard(sh,out,solver=a.solver,
                           scan_points=a.scan_points,dry_run=a.dry_run)
    print(json.dumps({"output":str(out),**result},indent=2))


if __name__=="__main__":
    main()
