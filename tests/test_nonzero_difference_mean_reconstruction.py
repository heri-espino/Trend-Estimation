"""Exact fold deletion, affine smoothing and nonzero-mu pilot contracts."""

import csv
import json

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.mean_difference_methods import (
    JointMeanPooledLOOCV, estimate_contrast_gaussian_mean,
    fitted_affine_trend, particular_polynomial,
)
from experiments.pooled_loocv_smoothness.objective import (
    PooledLOOCV, difference_matrix,
)
from experiments.pooled_loocv_smoothness.run_nonzero_difference_mean import (
    METHODS, MeanScenario, compare_pool, design, draw_pool,
    execute, shared_seed,
)


@pytest.mark.parametrize("order", [1,2,3])
def test_particular_polynomial_has_unit_dth_differences(order):
    p=particular_polynomial(30,order)
    np.testing.assert_allclose(difference_matrix(30,order)@p,1.,atol=1e-10)


@pytest.mark.parametrize("order", [1,2])
@pytest.mark.parametrize("R", [1,3])
def test_joint_mu_fold_clean_PRESS_matches_direct_deleted_refit(order,R):
    """Re-estimate the actual common mu and every tau after deletion."""
    rng=np.random.default_rng(301+order+R)
    n=12
    y=rng.standard_normal((R,n))+np.arange(n)[None,:]**2*.01
    d=difference_matrix(n,order)
    q=d.T@d
    dt1=d.T@np.ones(n-order)
    obj=JointMeanPooledLOOCV(y,order)
    lam=2.7
    mu_hat=obj.fitted_mu(lam)
    # Direct all-data penalty fit: first-order equations in (R*n+1) unknowns.
    def fit_deleted(r,i):
        full=np.zeros((R*n+1,R*n+1))
        rhs=np.zeros(R*n+1)
        for rr in range(R):
            w=np.ones(n)
            if rr==r:w[i]=0
            start=rr*n
            sl=slice(start,start+n)
            full[sl,sl]=np.diag(w)+lam*q
            full[sl,-1]=full[-1,sl]=-lam*dt1
            rhs[sl]=w*y[rr]
        full[-1,-1]=lam*R*(n-order)
        theta=np.linalg.solve(full,rhs)
        return theta[r*n+i],theta[-1]
    # _parts is the exact PRESS for all corresponding deleted fits.
    zmu,t_y,b,denom=obj._parts(lam)
    assert zmu==pytest.approx(mu_hat)
    predicted_residual=(t_y-b[:,None]*zmu)/denom[:,None]
    for r in range(R):
        for i in (0,2,n//2,n-1):
            predicted,deleted_mu=fit_deleted(r,i)
            assert predicted_residual[i,r]==pytest.approx(
                y[r,i]-predicted,abs=2e-7,rel=2e-7)
            assert np.isfinite(deleted_mu)
    assert obj.score(lam)==pytest.approx(
        np.mean(predicted_residual**2))


def test_joint_mu_infinite_lambda_endpoint_and_extra_nullspace():
    rng=np.random.default_rng(123)
    R,n,d=3,14,2
    y=rng.standard_normal((R,n))+.007*np.arange(n)[None,:]**2
    obj=JointMeanPooledLOOCV(y,d)
    limit_mu=obj.fitted_mu(np.inf)
    limit_score=obj.score(np.inf)
    fitted=obj.trend(np.inf)
    assert np.all(np.isfinite(fitted))
    for tau in fitted:
        np.testing.assert_allclose(
            difference_matrix(n,d)@tau,limit_mu,atol=1e-7)
    assert limit_score==pytest.approx(obj.score(1e15),rel=1e-7,abs=1e-8)
    # The d=2 mean-free infinite fit may contain shared nonzero curvature.
    assert abs(limit_mu)>1e-5


def test_guerrero_mean_plugin_only_at_lambda_zero_for_joint_estimator():
    rng=np.random.default_rng(234)
    y=rng.normal(size=(3,24))+np.arange(24)[None,:]**2*.025
    obj=JointMeanPooledLOOCV(y,order=2)
    plugin=float(np.mean(y@difference_matrix(24,2).T))
    assert obj.fitted_mu(0.)==pytest.approx(plugin,abs=1e-9)
    # Joint penalized mean at positive lambda need not equal simple plugin:
    assert abs(obj.fitted_mu(50.)-plugin)>1e-5


def test_gaussian_profile_mean_shift_invariant_components():
    sc=MeanScenario(50,.5,.3,.25)
    y,_=draw_pool(sc,3,shared_seed(69000000,50,.5,0))
    d=difference_matrix(50,2)
    base=estimate_contrast_gaussian_mean(y,d)
    p=particular_polynomial(50,2)
    shifted=estimate_contrast_gaussian_mean(y+1.7*p[None,:],d)
    assert shifted.mu==pytest.approx(base.mu+1.7,abs=1e-7)
    assert shifted.variance.sigma_eta2==pytest.approx(
        base.variance.sigma_eta2,rel=1e-8)
    assert shifted.variance.sigma_epsilon2==pytest.approx(
        base.variance.sigma_epsilon2,rel=1e-8)
    assert shifted.variance.lambda_ratio==pytest.approx(
        base.variance.lambda_ratio,rel=1e-8)


def test_fixed_mu_affine_fit_reproduces_true_polynomial_at_infinite_lambda():
    n=30
    p=particular_polynomial(n,2)
    rng=np.random.default_rng(345)
    y=np.vstack([.23*p+rng.normal(size=n),
                 .23*p+rng.normal(size=n)])
    obj=PooledLOOCV(y,order=2)
    fitted=fitted_affine_trend(obj,np.inf,.23)
    for row in fitted:
        np.testing.assert_allclose(
            difference_matrix(n,2)@row,.23,atol=1e-10)
    # With mu forced zero the limiting trend is only linear.
    for row in obj.trend(np.inf):
        np.testing.assert_allclose(
            difference_matrix(n,2)@row,0,atol=1e-10)


def test_nested_and_mu_factor_common_random_numbers():
    base=69000000
    x=MeanScenario(50,.5,.3,-1.)
    z=MeanScenario(50,.5,.3,1.)
    seed=shared_seed(base,50,.5,3)
    y1,tau1=draw_pool(x,1,seed)
    y3,tau3=draw_pool(x,3,seed)
    yz,tauz=draw_pool(z,3,seed)
    np.testing.assert_array_equal(y1[0],y3[0])
    np.testing.assert_array_equal(tau1[0],tau3[0])
    p=particular_polynomial(50,2)
    np.testing.assert_allclose(tauz-tau3,(z.mu-x.mu)*p[None,:],atol=1e-6)
    np.testing.assert_allclose(yz-y3,(z.mu-x.mu)*p[None,:],atol=1e-6)


def test_method_rows_use_no_truth_in_selection_and_preserve_all_roles():
    sc=MeanScenario(24,.5,.3,.5)
    y,tau=draw_pool(sc,1,69010000)
    rows=compare_pool(sc,y,tau)
    assert {row["method"] for row in rows}==set(METHODS)
    assert len(rows)==7
    assert all(np.isfinite(row["realized_true_trend_mse"]) for row in rows)
    by={x["method"]:x for x in rows}
    assert by["estimated_mu_fold_clean_pooled_loocv"][
        "reported_press_kind"]=="exact_fold_reestimated_mu_PRESS"
    assert by["estimated_mu_gaussian_gls_ml"][
        "reported_press_kind"]=="frozen_full_data_estimated_mu_PRESS_diagnostic_NOT_CV"
    assert by["known_mu_true_ratio_oracle"]["estimated_mu"]==sc.mu


def test_dry_run_and_smoke_write_immutable_machine_readable_artifacts(tmp_path):
    scenarios,reps,Rs=design("pilot")
    assert len(scenarios)==20 and reps==5 and Rs==(1,3)
    dry=tmp_path/"dry"
    plan=execute("pilot",dry,dry_run=True)
    assert plan["expected_nested_pools"]==200
    assert plan["expected_method_rows"]==1400
    assert not dry.exists()
    results=tmp_path/"smoke"
    summary=execute("smoke",results)
    assert summary["total_nested_pools"]==6
    assert summary["total_method_rows"]==42
    with (results/"method_comparison.csv").open(newline="") as f:
        rows=list(csv.DictReader(f))
    manifest=json.loads((results/"manifest.json").read_text())
    assert len(rows)==manifest["expected_method_rows"]==42
    assert manifest["truth_used_in_parameter_tuning"] is False
    assert manifest["order_d_fixed"]==2
    assert {r["method"] for r in rows}==set(METHODS)
    assert {float(r["mu_factor"]) for r in rows}=={-1.,0.,1.}
    assert all(float(r["realized_true_trend_mse"])>=0 for r in rows)
