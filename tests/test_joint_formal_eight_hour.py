"""One cheap unit suite for a cross-paper, time-budgeted Monte Carlo study."""
from __future__ import annotations

import numpy as np
import pytest

from experiments.smoothness_cv.simulation_dgps import grid_scenarios,make_series
from experiments.smoothness_cv.run_simulation_campaign import (
    arguments,balanced_seed_wave_schedule,config_from_args
)
from experiments.smoothness_cv.standard_forecast_baselines import (
    benchmark_predictions,evaluate_standard_baselines,
)
from experiments.smoothness_cv.joint_numerical_diagnostics import (
    historical_weighted_objective,numerical_case,
)
from experiments.smoothness_cv.pooled_lab import chronological_origins,fold_loss_at_lambda
from trend_estimation.validation.rolling_origin import RollingOriginSplit
from trend_estimation.forecasting.objectives import prepare_rolling_pure_forecast_objective
from trend_estimation.core.smoothness import smoothness_to_lambda


def test_formal8h_predeclared_factorial_counts():
    scenes=grid_scenarios("formal8h")
    assert len(scenes)==144
    assert len({s.key for s in scenes})==144
    assert {kind:sum(s.study==kind for s in scenes) for kind in "ABCD"} == {
        "A":16,"B":48,"C":32,"D":48,
    }
    # The three noise panels show the same underlying tau by construction.
    b=[s for s in scenes if s.study=="B" and s.shape=="quadratic_turn" and s.n_obs==360]
    assert {s.sigma for s in b}=={.25,.5,1.}
    assert len(b)==3
    a=[make_series(s,17) for s in sorted(b,key=lambda x:x.sigma)]
    assert all(np.array_equal(a[0].trend,x.trend) for x in a)
    assert all(not np.array_equal(a[0].observed,x.observed) for x in a[1:])


def test_budgeted_round_robin_visits_all_studies_and_never_duplicates():
    sc=grid_scenarios("formal8h")
    tasks=balanced_seed_wave_schedule(
        sc,first_seed=0,seed_count=16,seed_wave=8,completed=set()
    )
    assert len(tasks)==144*16
    assert [s.study for s,_ in tasks[:8*4]]==(
        ["A"]*8+["B"]*8+["C"]*8+["D"]*8
    )
    assert len({(s.key,seed) for s,seed in tasks})==len(tasks)
    excluded={(sc[0].key,0)}
    newer=balanced_seed_wave_schedule(
        sc,0,16,seed_wave=8,completed={f"{sc[0].key}__seed000000"}
    )
    assert len(newer)==len(tasks)-1


def test_predeclared_budget_cli_with_all_three_papers():
    a=arguments([
        "--backend","cuda","--preset","formal8h",
        "--time-budget-hours","8","--seed-wave","8",
        "--numerical-every","8","--with-baselines","--sturm-once",
        "--seeds","1000","--orders","2,3",
    ])
    c=config_from_args(a)
    assert len(c["scenario_keys"])==144
    assert c["numerical_every"]==8
    assert c["with_baselines"] and c["sturm_once"]
    assert a.time_budget_hours==8
    assert c["gpu_verify"]==0


def test_standard_external_forecasts_do_not_use_future_y():
    y=np.arange(50,dtype=float)+np.sin(np.arange(50))
    T,L,h=42,20,5
    before=benchmark_predictions(y,T,L,h)
    contaminated=y.copy()
    contaminated[T:]+=1e8
    after=benchmark_predictions(contaminated,T,L,h)
    assert before.keys()==after.keys()
    for k in before:
        assert np.array_equal(before[k],after[k])
    assert np.allclose(before["naive"],y[T-1])


def test_standard_rows_have_same_outer_origins_but_no_invented_S():
    scene=grid_scenarios("formal8h")[0]
    rows=evaluate_standard_baselines(scene,seed=0,horizons=(1,3),outer_count=2)
    assert len(rows)==2*2*4
    assert {r["baseline"] for r in rows}=={
        "naive","drift","seasonal_naive","linear_ols"
    }
    assert all("selected_s" not in row and "edf" not in row for row in rows)
    assert all(r["forecast_mse_obs"]>=0 for r in rows)


def test_weighted_analytic_F_agrees_with_exact_pooled_fold_losses():
    y=np.linspace(1,5,55)+.7*np.sin(np.arange(55)/6)
    L,d,h,T=22,2,3,45
    orig=chronological_origins(T,L,h,stride=3,max_folds=5)
    splits=[RollingOriginSplit(
        train=slice(int(t)-L,int(t)),
        validation=slice(int(t),int(t)+h)) for t in orig]
    prep=prepare_rolling_pure_forecast_objective(y[:T],splits,order=d)
    w=np.linspace(1.,2.,len(orig))
    cb=historical_weighted_objective(prep,w)
    for S in (0.,.25,.5,.8,1.):
        lam=smoothness_to_lambda(S,L,d)
        expected=float(w@fold_loss_at_lambda(prep,lam)/w.sum())
        got=cb(lam)
        assert got[0]==pytest.approx(expected,abs=1e-9,rel=1e-9)
    lam=.5
    eps=1e-4
    _,derivative,_=cb(lam)
    fd=(cb(lam+eps)[0]-cb(lam-eps)[0])/(2*eps)
    assert derivative==pytest.approx(fd,abs=1e-5,rel=1e-4)


def test_paper3_brent_and_stationary_diagnostics_use_same_completed_F():
    s=grid_scenarios("formal8h")[0]
    rows=numerical_case(
        s,seed=0,order=2,horizon=1,horizons=(1,),
        outer_count=2,max_folds=4,grid_points=11,
        dense_points=25,adaptive_depth=2,
        methods=("uniform_all",),
    )
    assert len(rows)==1
    row=rows[0]
    assert row["n_completed_folds"]<=4
    assert row["h"]==1 and row["d"]==2
    assert row["reference_type"]=="dense-numerical-not-certified"
    assert row["sturm_exact"]=="separate-small-instance-only"
    assert row["grid_outer_observed_mse"]>=0
    assert row["brent_past_recovery_mse"]>=0
    assert row["adaptive_outer_latent_mse"]>=0
    assert row["n_adaptive_stationary"]>=0
