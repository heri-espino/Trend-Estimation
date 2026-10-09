"""Paper 3 diagnostics on EXACTLY the Paper 1/2 historical F(S).

A reproducible, predeclared seed subsample. Bracketed bounded Brent
minimization, analytic derivative-based adaptive stationary search,
and a dense GRID REFERENCE are compared for the same m,d,L,h,T.
The grid reference is numerical, NOT an exhaustive root certificate.
Sturm is a separate exact small-instance control, run only ONCE
via run_sturm_minicheck.py, not on 400-point Monte Carlo windows.

Only PRETEST observed y[:T] is used to construct the objective;
latent tau and the external y[T:T+h] never enter the minimizer.
"""
from __future__ import annotations

import json
import time
import numpy as np
from scipy.optimize import minimize_scalar

from experiments.smoothness_cv.pooled_lab import (
    all_grid_fold_losses, chronological_origins,
)
from experiments.smoothness_cv.simulation_dgps import Scenario, make_series
from experiments.smoothness_cv.simulation_evaluation import METHODS, outer_origins
from trend_estimation.core.smoothness import smoothness_to_lambda
from trend_estimation.forecasting.objectives import prepare_rolling_pure_forecast_objective
from trend_estimation.selection.smoothness_numerical import find_stationary_points_smoothness
from trend_estimation.validation.rolling_origin import RollingOriginSplit


def historical_weighted_objective(prepared, weights):
    """Return exact (F,F_lambda,F_lambda_lambda) from one fixed fold panel."""
    w=np.asarray(weights,dtype=np.float64).reshape(-1)
    if len(w)!=prepared.n_origins or np.any(w<0) or not np.isfinite(w).all():
        raise ValueError("Wrong number of finite nonnegative historical weights.")
    if w.sum()<=0:
        raise ValueError("Historical weights must sum to a positive number.")
    w=w/w.sum()
    eigvals=prepared.eigvals
    H=prepared.spectral_history
    G=prepared.spectral_to_future.T
    O=prepared.prediction_offset
    Y=prepared.targets
    def objective(lam):
        lam=float(lam)
        if lam<0:
            raise ValueError("lambda must be nonnegative.")
        if np.isinf(lam):
            alpha=np.zeros_like(eigvals)
            alpha[:prepared.nullity]=1.
            alpha1=np.zeros_like(alpha)
            alpha2=np.zeros_like(alpha)
        else:
            alpha=1./(1.+lam*eigvals)
            alpha1=-eigvals*alpha*alpha
            alpha2=2.*eigvals*eigvals*alpha*alpha*alpha
        pred=(H*alpha)@G+O
        pred1=(H*alpha1)@G
        pred2=(H*alpha2)@G
        residual=Y-pred
        value=np.mean(residual*residual,axis=1)
        grad=np.mean(-2.*residual*pred1,axis=1)
        hess=np.mean(2.*(pred1*pred1-residual*pred2),axis=1)
        return float(w@value),float(w@grad),float(w@hess)
    return objective


def numerical_case(
    scenario: Scenario, seed: int, *,
    order: int = 2, horizon: int = 3,
    outer_count: int = 4, max_folds: int = 32,
    grid_points: int = 161, dense_points: int = 501,
    methods: tuple[str,...] = ("uniform_all","recent_exp_8"),
    adaptive_depth: int = 6,
) -> list[dict]:
    """Compute numerical methods on last completed inner objective, not outer test."""
    if dense_points<=grid_points or dense_points>5001:
        raise ValueError("Use a denser comparison grid (<=5001); not certification.")
    data=make_series(scenario,seed)
    valid=(1,3) if scenario.study=="A" and scenario.n_obs==50 else (1,3,6,12)
    if horizon not in valid:
        return []
    T=outer_origins(scenario,valid,count=outer_count)[-1]
    L=scenario.window
    origins=chronological_origins(T,L,horizon,max(1,horizon),max_folds)
    splits=[RollingOriginSplit(
        train=slice(int(t)-L,int(t)),
        validation=slice(int(t),int(t)+horizon)
    ) for t in origins]
    assert max(int(t)+horizon for t in origins)<=T
    prepared=prepare_rolling_pure_forecast_objective(
        data.observed[:T],splits,order=order
    )
    s_grid=np.linspace(0.,1.,grid_points)
    dense_grid=np.linspace(0.,1.,dense_points)
    results=[]
    for method_name in methods:
        method=next((m for m in METHODS if m.name==method_name),None)
        if method is None:
            raise ValueError(f"Unrecognized method {method_name}")
        start,w=method.weights(len(origins))
        weights=np.zeros(len(origins))
        weights[start:]=w
        objective=historical_weighted_objective(prepared,weights)
        def F(s:float)->float:
            return objective(smoothness_to_lambda(float(s),L,order))[0]

        # Dense reference is a NUMERICAL control, not certified ground truth.
        t0=time.perf_counter()
        # Use exact fixed scalar F for each point; unlike the CUDA benchmark
        # this part measures numerical root-finding, which remains CPU.
        dense_values=np.asarray([F(float(s)) for s in dense_grid])
        dense_best_i=int(np.argmin(dense_values))
        dense_best_s=float(dense_grid[dense_best_i])
        dense_best_f=float(dense_values[dense_best_i])
        dense_s=time.perf_counter()-t0

        sampled=all_grid_fold_losses(prepared,s_grid,L,order)
        grid_curve=weights@sampled
        grid_idx=int(np.argmin(grid_curve))
        grid_s=float(s_grid[grid_idx])
        grid_f=float(F(grid_s))
        # Every strict grid valley is separately refined using bounded
        # Brent; a single global bounded Brent call is NOT global
        # optimization of a multimodal objective.
        t0=time.perf_counter()
        brent_candidates=[(0.,F(0.)),(1.,F(1.))]
        brent_calls=0
        for i in range(1,len(s_grid)-1):
            if grid_curve[i]<=grid_curve[i-1] and grid_curve[i]<=grid_curve[i+1] and (
                grid_curve[i]<grid_curve[i-1] or grid_curve[i]<grid_curve[i+1]
            ):
                solution=minimize_scalar(
                    F,method="bounded",
                    bounds=(float(s_grid[i-1]),float(s_grid[i+1])),
                    options={"xatol":1e-9,"maxiter":200},
                )
                brent_calls+=int(solution.nfev)
                if solution.success and np.isfinite(solution.fun):
                    brent_candidates.append((float(solution.x),float(solution.fun)))
        brent_best_s,brent_best_f=min(brent_candidates,key=lambda x:(x[1],x[0]))
        brent_s=time.perf_counter()-t0

        t0=time.perf_counter()
        adaptive=find_stationary_points_smoothness(
            objective,n_obs=L,order=order,initial_grid_size=9,
            max_depth=adaptive_depth,min_interval=1e-3,
            boundary_margin=1e-6,
        )
        adaptive_candidates=[
            (float(p.smoothness_),float(p.objective_))
            for p in adaptive.points_ if p.kind_=="minimum"
        ]+[(0.,F(0.)),(1.,F(1.))]
        adaptive_best_s,adaptive_best_f=min(adaptive_candidates,key=lambda x:(x[1],x[0]))
        adaptive_s=time.perf_counter()-t0
        sampled_valleys=int(np.sum(
            ((grid_curve[1:-1]<=grid_curve[:-2])&
             (grid_curve[1:-1]<=grid_curve[2:])&
             ((grid_curve[1:-1]<grid_curve[:-2])|
              (grid_curve[1:-1]<grid_curve[2:])))
        ))
        results.append({
            "study":scenario.study,"scenario":scenario.key,
            "shape":scenario.shape,"sigma":float(scenario.sigma),
            "noise":scenario.noise,"N":int(scenario.n_obs),
            "seed":int(seed),"T":int(T),
            "L":int(L),"d":int(order),"h":int(horizon),
            "method":method_name,"n_completed_folds":int(len(origins)),
            "grid_points":int(grid_points),"dense_points":int(dense_points),
            "grid_s":grid_s,"grid_F":grid_f,
            "dense_s":dense_best_s,"dense_F":dense_best_f,
            "brent_s":brent_best_s,"brent_F":brent_best_f,
            "adaptive_s":adaptive_best_s,"adaptive_F":adaptive_best_f,
            "n_grid_valleys":sampled_valleys,
            "n_brent_refined":int(len(brent_candidates)-2),
            "brent_objective_evaluations":int(brent_calls),
            "n_adaptive_stationary":int(len(adaptive.points_)),
            "n_adaptive_minima":int(sum(p.kind_=="minimum" for p in adaptive.points_)),
            "adaptive_objective_evaluations":int(adaptive.n_evaluations_),
            "brent_regret_to_dense":float(brent_best_f-dense_best_f),
            "adaptive_regret_to_dense":float(adaptive_best_f-dense_best_f),
            "grid_regret_to_dense":float(grid_f-dense_best_f),
            "dense_seconds":float(dense_s),
            "brent_seconds":float(brent_s),
            "adaptive_seconds":float(adaptive_s),
            "reference_type":"dense-numerical-not-certified",
            "sturm_exact":"separate-small-instance-only",
        })
    return results


def write_numerical(conn, rows: list[dict]):
    """Atomic, independent Paper 3 table in the *same* campaign SQLite."""
    conn.execute(
        "CREATE TABLE IF NOT EXISTS numerical_diagnostics ("
        "scenario TEXT NOT NULL,seed INTEGER NOT NULL,d INTEGER NOT NULL,"
        "h INTEGER NOT NULL,method TEXT NOT NULL,payload TEXT NOT NULL,"
        "PRIMARY KEY (scenario,seed,d,h,method))"
    )
    conn.executemany(
        "INSERT OR REPLACE INTO numerical_diagnostics VALUES (?,?,?,?,?,?)",
        [(row["scenario"],row["seed"],row["d"],row["h"],row["method"],
          json.dumps(row,sort_keys=True)) for row in rows]
    )
    # Caller commits this table independently of or with scenario outcomes.
