"""Offline tests: finite-variance nonnormal shocks paired with nonzero mu.

CI uses tiny 1-2 seed shards only. No huge simulations and NO Cauchy
variance-ratio or expected MSE risk are silently included.
"""
from pathlib import Path
import csv
import gzip

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.objective import difference_matrix
from experiments.pooled_loocv_smoothness.mean_difference_methods import particular_polynomial
from experiments.pooled_loocv_smoothness.run_nonzero_difference_mean import (
    MeanScenario, compare_pool
)
from experiments.pooled_loocv_smoothness.run_nonzero_mean_multorder import fast_rows
from experiments.pooled_loocv_smoothness.run_nonzero_mu_nongaussian import (
    FINITE_REGIMES, HEAVY_FOURTH, PROTOCOL, NoiseShard, draw_observation_noise,
    draw_pool, seed_for, design, calculate_shard
)
from experiments.pooled_loocv_smoothness.launch_nonzero_mu_nongaussian import (
    plan, execute as launch
)
from experiments.pooled_loocv_smoothness.aggregate_nonzero_mu_nongaussian import (
    _method_records, execute as aggregate
)


def test_twelve_finite_regimes_and_explicit_cauchy_exclusion():
    assert len(FINITE_REGIMES)==12
    assert "gaussian_iid" in FINITE_REGIMES
    assert "cauchy_observation" not in FINITE_REGIMES
    assert len(HEAVY_FOURTH)==2
    pilot=design("pilot")
    assert pilot["base_strata"]==192
    assert pilot["independent_base_shock_draws"]==4800
    assert pilot["nested_pooled_treatments"]==48000
    assert pilot["method_level_rows"]==384000
    assert pilot["shards_at_default_size"]==192
    full=design("confirmatory")
    assert full["independent_base_shock_draws"]==1920000
    assert full["nested_pooled_treatments"]==19200000
    assert full["method_level_rows"]==153600000
    assert full["shards_at_default_size"]==19200


@pytest.mark.parametrize("regime",FINITE_REGIMES)
def test_noise_has_finite_theoretical_second_moments(regime):
    # Sample checks are loose by design: t3 finite variance but infinite
    # fourth moment, so empirical sample variance converges erratically.
    rng=np.random.default_rng(24681)
    n=15000 if regime=="garch_t5_observation" else 30000
    x=draw_observation_noise(regime,n,rng)
    assert x.shape==(n,)
    assert np.isfinite(x).all()
    assert abs(float(np.mean(x)))<.11
    # t3 draws are heavy-tailed, so do not insist on sample variance ~ 1.
    if regime not in HEAVY_FOURTH:
        assert .7<float(np.mean(x*x))<1.3
    if regime=="garch_t5_observation":
        squared=np.asarray(x*x)
        # Very loose finite-sample volatility-clustering sanity check.
        assert np.isfinite(np.corrcoef(squared[:-1],squared[1:])[0,1])


@pytest.mark.parametrize("d",[1,2,3,4])
@pytest.mark.parametrize("regime",[
    "gaussian_iid","student_t3_innovation","centered_gamma_left",
    "garch_t5_observation","skew_normal_p6"])
def test_dth_differences_nested_R_and_paired_mu(d,regime):
    sh=NoiseShard(regime,d,50,.5,0,1)
    y,tau=draw_pool(sh,0)
    assert y.shape==tau.shape==(3,50)
    assert np.isfinite(y).all()
    D=difference_matrix(50,d)
    assert np.all(np.isfinite(tau@D.T))
    p=particular_polynomial(50,d)
    np.testing.assert_allclose(D@p,1.,rtol=1e-6,atol=1e-6)
    sc=MeanScenario(50,.5,.3,1.,d=d)
    shifted_y=y+sc.mu*p
    shifted_tau=tau+sc.mu*p
    np.testing.assert_allclose(shifted_tau@D.T-tau@D.T,
                               sc.mu,atol=1e-5)
    # Pure location intervention: observational noise exactly unchanged.
    np.testing.assert_allclose(shifted_y-shifted_tau,y-tau,atol=1e-10)


def test_matched_baseline_methods_and_shift_reuse():
    regime="student_t3_observation"
    sh=NoiseShard(regime,2,24 if False else 50,2.,0,1)
    y,tau=draw_pool(sh,0)
    baseline_sc=MeanScenario(50,2.,.3,0.,d=2)
    for R in (1,3):
        base={r["method"]:r for r in compare_pool(baseline_sc,y[:R],tau[:R])}
        sc=MeanScenario(50,2.,.3,.25,d=2)
        p=particular_polynomial(50,2)
        observed=y[:R]+sc.mu*p
        truth=tau[:R]+sc.mu*p
        fast={r["method"]:r for r in fast_rows(sc,observed,truth,base)}
        slow={r["method"]:r for r in compare_pool(sc,observed,truth)}
        for method in slow:
            assert fast[method]["realized_true_trend_mse"]==pytest.approx(
                slow[method]["realized_true_trend_mse"],abs=1e-5,rel=1e-5)
            assert fast[method]["estimated_mu"]==pytest.approx(
                slow[method]["estimated_mu"],abs=1e-5,rel=1e-5)


def test_unique_seeds_per_stratum_and_between_phases():
    sample=set()
    for regime in FINITE_REGIMES:
        for d in [1,2,3,4]:
            for n in [50,200]:
                for eta in [.5,2.]:
                    for phase in ("pilot","confirmatory"):
                        sh=NoiseShard(regime,d,n,eta,0,1,phase)
                        seed=seed_for(sh,0)
                        assert seed not in sample
                        sample.add(seed)
    assert len(sample)==384
    with pytest.raises(ValueError):
        NoiseShard("cauchy_observation",2,50,.5,0,1)
    with pytest.raises(ValueError):
        NoiseShard("student_t3_observation",4,200,2.,9999,2,"confirmatory")
    assert len(plan(phase="pilot"))==192
    assert len(plan(phase="confirmatory"))==19200


def test_shard_sha_aggregation_pairing_and_resume(tmp_path):
    root=tmp_path/"raw"
    sh=NoiseShard("centered_gamma_right",2,50,.5,0,2,"pilot")
    target=root/"pilot"/sh.suffix
    dry=calculate_shard(sh,target,dry_run=True)
    assert dry["expected_method_rows"]==160
    assert not target.exists()
    first=calculate_shard(sh,target)
    assert first["protocol"]==PROTOCOL
    assert first["actual_method_rows"]==160
    assert first["noise_var_exists"] is True
    with gzip.open(target/"method_comparison.csv.gz","rt",encoding="utf-8",
                   newline="") as f:
        values=list(csv.DictReader(f))
    assert len(values)==160
    assert len({v["seed"] for v in values})==2
    report, method, paired=_method_records(root,"pilot",digest=True)
    assert report["status"].startswith("INCOMPLETE_")
    assert report["independent_base_R3_shock_draws_present"]==2
    assert len(method)==80
    assert len(paired)==40
    with pytest.raises(ValueError,match="Incomplete"):
        aggregate(root,tmp_path/"must_not_exist","pilot",require_complete=True)
    actual=aggregate(root,tmp_path/"valid_aggregate","pilot")
    assert actual["strata_present"]==1
    with pytest.raises(FileExistsError):
        aggregate(root,tmp_path/"valid_aggregate","pilot")
    same=launch([sh],root,workers=1)
    assert same["verified_existing"]==1
    overlap=NoiseShard("centered_gamma_right",2,50,.5,0,3,"pilot")
    with pytest.raises(RuntimeError,match="overlap"):
        launch([overlap],root,workers=1)
