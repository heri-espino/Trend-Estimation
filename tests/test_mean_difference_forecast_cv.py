"""Math, end-point, leakage and profiling tests for mean-difference forecast CV."""
from __future__ import annotations

import numpy as np
import pytest

from trend_estimation.core.difference import difference_matrix
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.forecasting.mean_difference_cv import (
    affine_mean_components,
    fit_mean_difference_forecast,
    observed_mean_difference,
    polynomial_difference_particular,
    profile_mean_difference,
    select_mean_difference_cv,
)
from trend_estimation.forecasting.operators import finite_difference_forecast_operator


@pytest.mark.parametrize("d",[1,2,3,4])
def test_particular_polynomial_has_unit_dth_differences(d):
    L=23
    p=polynomial_difference_particular(L,d)
    assert np.allclose(difference_matrix(L,d)@p,np.ones(L-d),atol=1e-10)
    with pytest.raises(ValueError):
        polynomial_difference_particular(2,2)


@pytest.mark.parametrize("d",[1,2,3])
@pytest.mark.parametrize("s",[0.,.13,.58,.999,1.])
def test_affine_estimator_satisfies_penalized_normal_equations_and_forecast(d,s):
    L,h=16,6
    rng=np.random.default_rng(d+100)
    x=rng.normal(size=L)
    mu=.73
    fit=fit_mean_difference_forecast(x,order=d,smoothness=s,horizon=h,mu=mu)
    solver=cached_pure_solver(L,d)
    H=solver.fit_for_lambda(x,fit.lambda_).trend
    G=finite_difference_forecast_operator(L,d,h)
    if np.isfinite(fit.lambda_):
        direct=np.linalg.solve(np.eye(L)+fit.lambda_*solver.penalty,
                              x+fit.lambda_*mu*solver.D.T@np.ones(L-d))
        assert np.allclose(fit.fitted,direct,rtol=1e-7,atol=1e-7)
    else:
        # Exact endpoint: constraint D tau = mu*ones, and LS projection
        # onto corresponding affine polynomial space.
        assert np.allclose(solver.D@fit.fitted,mu*np.ones(L-d),atol=1e-6)
    assert np.allclose(fit.forecast,G.apply(fit.fitted,m_hat=mu),
                       rtol=1e-9,atol=1e-9)
    if s==0:
        assert np.allclose(fit.fitted,x,rtol=1e-11,atol=1e-11)
    if mu==0:
        assert np.allclose(fit.fitted,H,atol=1e-10)


def test_guerrero_data_plugin_matrix_and_actual_df():
    x=np.array([2.,2.3,2.8,3.7,4.,5.2,6.,7.1,8.],dtype=float)
    L,d,h=len(x),2,4
    mu=observed_mean_difference(x,d)
    s=.72
    fit=fit_mean_difference_forecast(x,order=d,smoothness=s,horizon=h,mu=mu)
    lam=fit.lambda_
    D=difference_matrix(L,d)
    Q=D.T@D
    A=np.eye(L)+lam*Q
    c=D.T@np.ones(L-d)/(L-d)
    B=np.linalg.solve(A,np.eye(L)+lam*np.outer(D.T@np.ones(L-d),c))
    assert np.allclose(fit.fitted,B@x,rtol=1e-8,atol=1e-8)
    assert fit.plugin_edf==pytest.approx(np.trace(B),rel=1e-8,abs=1e-8)
    # A mean estimated from y changes the smoother df; do NOT silently
    # equate trace(H) to trace(full plug-in operator).
    assert abs(fit.plugin_edf-fit.penalty_edf)>1e-4


def test_profile_is_closed_form_weighted_least_squares():
    r=np.asarray([[3.,2.],[-1.,5.],[2.,6.]])
    b=np.asarray([1.5,3.])
    w=np.asarray([.1,.2,.7])
    mu,identified=profile_mean_difference(r,b,w)
    assert identified
    eps=1e-5
    def F(z):
        return float(np.sum(w[:,None]*(r-z*b[None,:])**2)/r.shape[1])
    assert F(mu)<=min(F(mu-eps),F(mu+eps))+1e-12
    assert mu==pytest.approx(float(w@(r@b)/(b@b)))
    _,flag=profile_mean_difference(r,np.zeros_like(b),w)
    assert not flag


@pytest.mark.parametrize("d",[1,2,3])
def test_profiled_CV_modes_only_use_completed_blocks_and_limit_projection(d):
    rng=np.random.default_rng(22)
    y=rng.normal(size=80)+np.arange(80)*.1+np.arange(80)**2*.001
    T=70;h=3;L=30
    origins=np.array([35,43,51,60,66])
    grid=np.array([0.,.2,.5,.8,1.])
    props=dict(order=d,window=L,horizon=h,
               historical_origins=origins,smoothness_grid=grid)
    outputs={}
    for mode in ("zero","guerrero","profile"):
        out=select_mean_difference_cv(y[:T],mean_mode=mode,**props)
        outputs[mode]=out
        assert len(out.grid)==len(grid)
        assert out.fold_losses.shape==(len(origins),len(grid))
        assert np.isfinite(out.weighted_losses).all()
        assert np.all(out.weighted_losses>=0)
        assert 0.<=out.selected_s<=1.
        assert np.isfinite(out.selected_mu)
        assert len(out.forecast_fit.forecast)==h
        # A fixed S=0 still has identifiable future mean loading
        assert np.all(out.identified_mu_by_s) if mode=="profile" else True
    assert np.all(outputs["profile"].weighted_losses <=
                  outputs["zero"].weighted_losses+1e-9)
    # Historical continuation must not look ahead past T.
    contaminated=y.copy()
    contaminated[T:]+=1e12
    for mode in outputs:
        back=select_mean_difference_cv(contaminated[:T],mean_mode=mode,**props)
        assert back.selected_s==pytest.approx(outputs[mode].selected_s)
        assert back.selected_mu==pytest.approx(outputs[mode].selected_mu)
        assert np.allclose(back.weighted_losses,outputs[mode].weighted_losses)


def test_pure_zero_mu_selection_matches_explicit_zero_drift_forecasts():
    x=np.array([2.,2.2,3.1,4.4,4.6,5.3,5.8,6.6,6.7,7.1,7.9])
    selected=fit_mean_difference_forecast(
        x,order=2,smoothness=.65,horizon=5,mu=0.
    )
    solver=cached_pure_solver(len(x),2)
    expected=solver.fit_for_s(x,.65).trend
    assert np.allclose(selected.fitted,expected)
    assert np.allclose(selected.forecast,
                       finite_difference_forecast_operator(len(x),2,5).apply(expected,0.))


def test_invalid_uncompleted_origins_rejected():
    y=np.arange(40,dtype=float)
    with pytest.raises(ValueError,match="completed"):
        select_mean_difference_cv(
            y,order=2,window=20,horizon=5,
            historical_origins=[25,37],
            smoothness_grid=[0.,.5,1.]
        )


def test_profiled_F_matches_brute_force_mu_grid():
    y=np.sin(np.arange(65)/10)+.02*np.arange(65)+np.arange(65)**2*.0005
    args=dict(order=2,window=22,horizon=2,
              historical_origins=[28,33,39,43,51],
              smoothness_grid=[.2,.5,.9],weights=[1,2,3,4,5])
    output=select_mean_difference_cv(y[:60],mean_mode="profile",**args)
    norm=np.asarray(args["weights"],dtype=float)
    norm/=norm.sum()
    L=args["window"]
    G=finite_difference_forecast_operator(L,2,2)
    for j,S in enumerate(args["smoothness_grid"]):
        mu=output.mu_by_s[j]
        mu_set=mu+np.linspace(-.1,.1,31)
        vals=[]
        for m in mu_set:
            e=[]
            for T in args["historical_origins"]:
                fit=fit_mean_difference_forecast(
                    y[T-L:T],order=2,smoothness=S,horizon=2,mu=m,
                )
                e.append(float(np.mean((fit.forecast-y[T:T+2])**2)))
            vals.append(norm@e)
        assert output.weighted_losses[j]==pytest.approx(min(vals),abs=1e-9)
