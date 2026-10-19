"""Non-Gaussian FINITE-VARIANCE noise + common nonzero difference-mean study.

Manual Monte Carlo only, paired within independent shock-draw and five
mu-shifts. Four *analyst-fixed* difference orders, N=50/200, observed
noise population SD=0.5/2.0, R=1 and nested 3, eight identical selectors.

The 12 regimes replicate those in the old independent tail-noise pilot
with all finite-variance cases (including Gaussian reference), but now
allow d=4 and nonzero mu. Cauchy is DELIBERATELY excluded: no finite
noise mean, variance, true ratio or expected squared reconstruction risk.
It needs its own robust-risk simulation, never false 'true variance' oracle.

Student t(3) has finite variance but infinite fourth moment. Mean squared
risk is defined, yet ordinary normal-approximation Monte Carlo confidence
intervals for quadratic-loss estimates need not be valid. Flag all such
standard errors as DIAGNOSTIC ONLY. GARCH-t5 observation noise is
uncorrelated (second moment diagonal), but not independent over time.

The initial latent path tau is an actually realized d-fold integrated
stochastic trend, not E[tau] and not a real stock's mean return.
Nothing uses latent tau to choose mu or lambda (except explicit labelled
true-parameter benchmarks).
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import platform
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy

from .run_tail_noise import (
    REGIMES, SKEW_NORMAL_ALPHAS, _standard_t, centered_skew_normal,
    GAMMA_SHAPE, JUMP_PROBABILITY, JUMP_SD_MULTIPLIER,
    GARCH_ALPHA, GARCH_BETA, T3_DF, T5_DF,
)
from .run_nonzero_difference_mean import (
    MeanScenario, METHODS, MU_FACTORS, compare_pool, _integrate_order
)
from .run_nonzero_mean_multorder import (
    fast_rows, add_summary, add_paired, summarize, summarize_paired,
    LENGTHS, ETA_SDS, ORDERS, SIGMA_EPSILON, _sha
)
from .mean_difference_methods import particular_polynomial


FINITE_REGIMES = tuple(r for r in REGIMES if r != "cauchy_observation")
HEAVY_FOURTH = ("student_t3_observation", "student_t3_innovation")
NEW_SEED_BASE = 126000000  # disjoint from prior simulations
PILOT_REPS = 25
CONFIRMATORY_REPS = 10000
DEFAULT_SHARD_REPS = 25

PROTOCOL = "nonzero_mean_nongaussian_finite_variance_v1"


@dataclass(frozen=True)
class NoiseShard:
    regime: str
    d: int
    n: int
    sigma_eta: float
    start: int
    count: int
    phase: str = "pilot"

    def __post_init__(self):
        if (self.regime not in FINITE_REGIMES or self.d not in ORDERS
            or self.n not in LENGTHS or self.sigma_eta not in ETA_SDS
            or self.phase not in ("pilot", "confirmatory")):
            raise ValueError("invalid finite-noise Monte Carlo factorial cell")
        total=self.total
        if self.start<0 or self.count<1 or self.start+self.count>total:
            raise ValueError(f"replicate shard must lie within [0,{total})")

    @property
    def total(self):
        return PILOT_REPS if self.phase == "pilot" else CONFIRMATORY_REPS

    @property
    def base_draws(self):
        return self.count

    @property
    def pools(self):
        return self.count*len(MU_FACTORS)*2

    @property
    def rows(self):
        return self.pools*len(METHODS)

    @property
    def suffix(self):
        return (f"{self.regime}/d{self.d}/N{self.n}/eta{self.sigma_eta:g}/"
                f"rep_{self.start:05d}_{self.start+self.count:05d}")


def seed_for(shard: NoiseShard, rep: int) -> int:
    if not shard.start<=rep<shard.start+shard.count:
        raise ValueError("replicate outside shard")
    phase_offset=(1_000_000_000 if shard.phase == "confirmatory" else 0)
    return (NEW_SEED_BASE + phase_offset + FINITE_REGIMES.index(shard.regime)*10_000_000
            + shard.d*1_000_000
            + LENGTHS.index(shard.n)*200_000
            + ETA_SDS.index(shard.sigma_eta)*100_000 + rep)


def draw_observation_noise(regime: str, n: int, rng: np.random.Generator):
    """Population zero mean, unit marginal variance in every finite regime.

    For GARCH h_0=1; the recursion itself carries volatility information,
    which a marginal histogram does not. All scaling parameters exactly
    match run_tail_noise.py's earlier exploratory pilot.
    """
    if regime == "student_t3_observation":
        return _standard_t(rng,T3_DF,n)
    if regime in ("centered_gamma_right", "centered_gamma_left"):
        z=(rng.gamma(shape=GAMMA_SHAPE,scale=1.,size=n)-GAMMA_SHAPE)/np.sqrt(GAMMA_SHAPE)
        return z if regime.endswith("right") else -z
    if regime == "gaussian_jump_mixture":
        jumps=rng.uniform(size=n)<JUMP_PROBABILITY
        multipliers=np.where(jumps,JUMP_SD_MULTIPLIER,1.)
        variance=(1.-JUMP_PROBABILITY)+JUMP_PROBABILITY*JUMP_SD_MULTIPLIER**2
        return multipliers*rng.standard_normal(n)/np.sqrt(variance)
    if regime == "garch_t5_observation":
        z=_standard_t(rng,T5_DF,n)
        h=1.0
        prev=0.
        out=np.empty(n,dtype=float)
        omega=1.-GARCH_ALPHA-GARCH_BETA
        for t in range(n):
            if t:
                h=omega+GARCH_ALPHA*prev**2+GARCH_BETA*h
            prev=float(np.sqrt(h)*z[t])
            out[t]=prev
        return out
    if regime in SKEW_NORMAL_ALPHAS:
        return centered_skew_normal(rng,n,SKEW_NORMAL_ALPHAS[regime])
    if regime in ("gaussian_iid","student_t3_innovation"):
        return rng.standard_normal(n)
    raise ValueError("non-finite or unrecognized regime; Cauchy NOT supported")


def draw_pool(shard: NoiseShard, rep: int) -> tuple[np.ndarray, np.ndarray]:
    """Draw R=3 baseline mu=0; R1 uses the exact same first trajectory."""
    rng=np.random.default_rng(seed_for(shard,rep))
    yy,truth=[],[]
    for _ in range(3):
        if shard.regime=="student_t3_innovation":
            eps=SIGMA_EPSILON*_standard_t(rng,T3_DF,shard.n-shard.d)
        else:
            eps=SIGMA_EPSILON*rng.standard_normal(shard.n-shard.d)
        tau=_integrate_order(eps,shard.d)
        noise=shard.sigma_eta*draw_observation_noise(shard.regime,shard.n,rng)
        yy.append(tau+noise)
        truth.append(tau)
    return np.asarray(yy),np.asarray(truth)


def design(phase: str="pilot"):
    reps=PILOT_REPS if phase=="pilot" else CONFIRMATORY_REPS if phase=="confirmatory" else None
    if reps is None: raise ValueError("invalid phase")
    groups=len(FINITE_REGIMES)*len(ORDERS)*len(LENGTHS)*len(ETA_SDS)
    return {
        "phase":phase,"finite_variance_regimes":list(FINITE_REGIMES),
        "regime_count":len(FINITE_REGIMES),"base_strata":groups,
        "independent_base_shock_draws":groups*reps,
        "independent_replicates_per_stratum":reps,
        "nested_pooled_treatments":groups*reps*len(MU_FACTORS)*2,
        "method_level_rows":groups*reps*len(MU_FACTORS)*2*len(METHODS),
        "default_launcher_shard_replicates":(25 if phase=="pilot" else 100),
        "shards_at_default_size":groups*((reps+(25 if phase=="pilot" else 100)-1)//(25 if phase=="pilot" else 100)),
        "cauchy_excluded":True,
        "fourth_moment_infinite":list(HEAVY_FOURTH),
        "source_gaussian_control_included":True,
    }


def calculate_shard(shard:NoiseShard,output:Path,*,dry_run=False):
    run_sha=_sha()
    manifest={
        "protocol":PROTOCOL,
        "status":"planned" if dry_run else "executed_shard",
        "phase":shard.phase,"regime":shard.regime,
        "noise_var_exists":True,
        "error_fourth_moment_exists":shard.regime not in HEAVY_FOURTH,
        "normal_approx_MSE_SE_interpretation":(
            "diagnostic_only_quadratic_loss_may_have_infinite_variance"
            if shard.regime in HEAVY_FOURTH else
            "requires_independent_seed_sampling_and_regular_Monte_Carlo_checks"),
        "GARCH_second_moment_note":(
            "GARCH_t5 disturbances are uncorrelated but conditionally heteroskedastic"
            if shard.regime=="garch_t5_observation" else None),
        "difference_order_fixed":shard.d,"N":shard.n,
        "sigma_eta_population_SD":shard.sigma_eta,
        "sigma_epsilon_population_SD":SIGMA_EPSILON,
        "R_values":[1,3],"mu_over_sigma_epsilon":list(MU_FACTORS),
        "methods":list(METHODS),
        "paired_same_shocks_across_mu":True,
        "nested_R1_in_R3":True,
        "statistical_unit":"(regime,d,N,eta,replicate) R3 shock draw",
        "true_variance_ratio_is_known_linear_covariance_benchmark_NOT_density_oracle":True,
        "truth_used_for_feasible_parameter_selection":False,
        "seed_base":NEW_SEED_BASE + (1_000_000_000 if shard.phase=="confirmatory" else 0),
        "seed_formula":"126000000 + 1000000000*(phase==confirmatory) + regime_index*10000000 + d*1000000 + N_index*200000 + eta_index*100000 + replicate",
        "seed_start_inclusive":shard.start,
        "seed_stop_exclusive":shard.start+shard.count,
        "expected_independent_base_draws":shard.base_draws,
        "expected_method_rows":shard.rows,
        "expected_pooled_treatment_evaluations":shard.pools,
        "source_git_sha":run_sha,"python":platform.python_version(),
        "numpy":np.__version__,"scipy":scipy.__version__,
        "created_utc":datetime.now(timezone.utc).isoformat(),
        "generator_constant_ref":"run_tail_noise.py",
        "not_a_stock_forecast":True,
        "not_Cauchy":True,
    }
    if dry_run:return manifest
    if output.exists():
        raise FileExistsError(f"Shard already exists: {output}; never overwrite")
    output.mkdir(parents=True,exist_ok=False)
    p=particular_polynomial(shard.n,shard.d)
    summary_acc,paired_acc={},{}
    data=output/"method_comparison.csv.gz"
    count=0
    with gzip.open(data,"wt",encoding="utf-8",newline="",compresslevel=5) as file:
        writer=None
        for rep in range(shard.start,shard.start+shard.count):
            y0,tau0=draw_pool(shard,rep)
            seed=seed_for(shard,rep)
            for R in (1,3):
                sc0=MeanScenario(shard.n,shard.sigma_eta,SIGMA_EPSILON,0.,d=shard.d)
                # Even outside normality, likelihood methods are treated as
                # Gaussian QUASI-likelihood fitted to observations.
                baseline={r["method"]:r for r in compare_pool(sc0,y0[:R],tau0[:R])}
                for factor in MU_FACTORS:
                    sc=MeanScenario(shard.n,shard.sigma_eta,SIGMA_EPSILON,factor,d=shard.d)
                    y=y0[:R]+sc.mu*p[None,:]
                    tau=tau0[:R]+sc.mu*p[None,:]
                    result=fast_rows(sc,y,tau,baseline)
                    add_paired(paired_acc,R,factor,result)
                    for record in result:
                        row={
                            "regime":shard.regime,"d":shard.d,"N":shard.n,
                            "sigma_eta":shard.sigma_eta,
                            "sigma_epsilon":SIGMA_EPSILON,
                            "replicate":rep,"seed":seed,
                            "R":R,"mu_factor":factor,
                            **record,
                        }
                        if writer is None:
                            writer=csv.DictWriter(file,fieldnames=list(row))
                            writer.writeheader()
                        writer.writerow(row)
                        add_summary(summary_acc,row)
                        count+=1
    if count!=shard.rows:raise ArithmeticError("incomplete shard count")
    digest=hashlib.sha256()
    with data.open("rb") as file:
        for chunk in iter(lambda:file.read(1<<20),b""):
            digest.update(chunk)
    manifest["actual_method_rows"]=count
    manifest["compressed_csv_sha256"]=digest.hexdigest()
    manifest["compressed_csv_bytes"]=data.stat().st_size
    (output/"summary.json").write_text(json.dumps({
        "status":"completed_shard",
        "by_R_mu_method":summarize(summary_acc,shard.count),
        "paired_R_mu_method_contrasts":summarize_paired(paired_acc,shard.count)
    },indent=2)+"\n",encoding="utf-8")
    (output/"manifest.json").write_text(
        json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    return manifest


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--phase",choices=("pilot","confirmatory"),default="pilot")
    p.add_argument("--regime",choices=FINITE_REGIMES,required=True)
    p.add_argument("--d",choices=ORDERS,type=int,required=True)
    p.add_argument("--n",choices=LENGTHS,type=int,required=True)
    p.add_argument("--sigma-eta",choices=ETA_SDS,type=float,required=True)
    p.add_argument("--start-replicate",type=int,default=0)
    p.add_argument("--count",type=int,default=1)
    p.add_argument("--root",type=Path,default=Path(
        "results/pooled_loocv_smoothness/guerrero/nonzero_mu_nongaussian"))
    p.add_argument("--dry-run",action="store_true")
    args=p.parse_args()
    shard=NoiseShard(args.regime,args.d,args.n,args.sigma_eta,
                     args.start_replicate,args.count,args.phase)
    output=args.root/args.phase/shard.suffix
    result=calculate_shard(shard,output,dry_run=args.dry_run)
    print(json.dumps({"output":str(output),**result},indent=2))


if __name__=="__main__":
    main()
