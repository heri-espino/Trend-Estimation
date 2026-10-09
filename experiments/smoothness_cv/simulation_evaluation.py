"""Joint Paper 1/Paper 2 Monte Carlo evaluations; never use latent future for tuning.

A *replication* (scenario,seed) produces paired outcomes for every feasible
method, horizon, order and chronological outer origin. Oracle results are
marked explicitly. This module does no IO or multiprocessing.
"""
from __future__ import annotations

from functools import lru_cache
import json

import numpy as np

from experiments.smoothness_cv.pooled_lab import cached_uniform_spectral_weights
from experiments.smoothness_cv.simulation_dgps import GeneratedSeries, Scenario, make_series
from experiments.smoothness_cv.weighted_surface_study import (
    LossWeighting, run_weighted_surface_study,
)
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.forecasting.operators import finite_difference_forecast_operator


METHODS: tuple[LossWeighting,...] = (
    LossWeighting("uniform_all", "uniform"),
    LossWeighting("recent_uniform_8", "uniform", lookback=8),
    LossWeighting("recent_linear_8", "linear", lookback=8),
    LossWeighting("recent_exp_8", "exponential", lookback=8, decay=.8),
    LossWeighting("recent_exp_20", "exponential", lookback=20, decay=.9),
)
CLASSICAL = ("cv","gcv","aicc","bic")
FIXED = (0.,.5,.8,.95,1.)


def outer_origins(scenario: Scenario, horizons: tuple[int,...], *, count: int = 4) -> tuple[int,...]:
    """Same complete external origins for every horizon within each DGP."""
    n = scenario.n_obs
    hmax = max(horizons)
    L = scenario.window
    earliest = max(L + hmax + 7, int(.63*n))
    last = n - hmax
    if earliest > last:
        raise ValueError("Insufficient series length for joint outer origins.")
    values = np.unique(np.linspace(earliest,last,count).round().astype(int))
    if len(values) < 2:
        raise ValueError("Need at least two different outer origins.")
    return tuple(map(int,values))


def _spectral_candidates(
    y_window: np.ndarray,
    tau_window: np.ndarray,
    *,
    order: int,
    grid_points: int,
) -> tuple[np.ndarray,np.ndarray,dict[str,float],np.ndarray]:
    """Vectorized CV/GCV/AICc/BIC and reconstruction-oracle grid.

    Exact for the same *grid definition* as pure_smoother_score.
    Avoid repeated eigendecompositions and 4 separate grid searches.
    """
    n = len(y_window)
    solver = cached_pure_solver(n,order)
    U = solver.eigvecs
    alpha = cached_uniform_spectral_weights(n,order,grid_points)  # [grid,n]
    grid = np.linspace(0.,1.,grid_points)
    fits = (alpha * (U.T @ y_window)[None,:]) @ U.T
    residual = y_window[None,:]-fits
    rss = np.sum(residual**2,axis=1)
    edf = alpha.sum(axis=1)
    hdiag = alpha @ (U**2).T
    small = 1e-12
    denominator = 1. - hdiag
    with np.errstate(divide="ignore",invalid="ignore"):
        cv = np.mean((residual/denominator)**2,axis=1)
        cv[np.any(np.abs(denominator)<=small,axis=1)] = np.inf
        gcv = (rss/n)/(1-edf/n)**2
        gcv[np.abs(1-edf/n)<=small] = np.inf
        aicc = np.log(np.maximum(rss/n,small)) + (2*edf+1)/(n-edf-2)
        aicc[(n-edf-2)<=small] = np.inf
        aicc[rss<=small] = np.inf
        bic = np.log(np.maximum(rss/n,small)) + edf*np.log(n)/n
        bic[rss<=small] = np.inf
    scores = {"cv":cv,"gcv":gcv,"aicc":aicc,"bic":bic}
    selected={}
    for name, curve in scores.items():
        finite = np.where(np.isfinite(curve))[0]
        if not finite.size:
            raise ValueError(f"No finite score for {name} at this window/order.")
        pos = finite[int(np.argmin(curve[finite]))]
        selected[name]=float(grid[pos])
    recovery = np.mean((fits-tau_window[None,:])**2,axis=1)
    selected["oracle_recovery"] = float(grid[np.argmin(recovery)])
    return grid, fits, selected, recovery


def _oracle_future(
    grid: np.ndarray, candidate_fits: np.ndarray,
    tau_future: np.ndarray, *, order: int, horizon: int,
) -> float:
    G=finite_difference_forecast_operator(candidate_fits.shape[1],order,horizon).trend_matrix
    forecasts = candidate_fits @ G.T
    error = np.mean((forecasts-tau_future[None,:])**2,axis=1)
    return float(grid[np.argmin(error)])


def _score(
    y: np.ndarray, tau: np.ndarray, seasonal: np.ndarray,
    *, T: int, L: int, h: int, d: int, s: float,
) -> dict:
    """Refit fresh at outer T; future outcomes here only for diagnostics."""
    solver = cached_pure_solver(L,d)
    fit = solver.fit_for_s(y[T-L:T],float(s))
    G=finite_difference_forecast_operator(L,d,h).trend_matrix
    forecast = G @ fit.trend
    obs_err=y[T:T+h]-forecast
    latent_err=tau[T:T+h]-forecast
    conditional_err=(tau[T:T+h]+seasonal[T:T+h])-forecast
    recovery=tau[T-L:T]-fit.trend
    return {
        "selected_s":float(s),
        "selected_lambda":float(fit.lambda_),
        "edf":float(L-(L-d)*s),
        "raw_guerrero_s":float((L-d)*s/L),
        "forecast_mse_obs":float(np.mean(obs_err**2)),
        "forecast_mae_obs":float(np.mean(np.abs(obs_err))),
        "forecast_mse_latent":float(np.mean(latent_err**2)),
        "forecast_mse_conditional":float(np.mean(conditional_err**2)),
        "past_recovery_mse":float(np.mean(recovery**2)),
        "fit_residual_mse":float(np.mean((y[T-L:T]-fit.trend)**2)),
        "lead_squared_errors":json.dumps([float(v) for v in obs_err**2]),
    }


def evaluate_replication(
    scenario: Scenario, seed: int, *,
    orders: tuple[int,...] = (2,),
    horizons: tuple[int,...] = (1,3,6,12),
    outer_count: int = 4,
    max_folds: int = 32,
    grid_points: int = 81,
    methods: tuple[LossWeighting,...] = METHODS,
    generated: GeneratedSeries | None = None,
    precomputed_losses: dict[tuple[int,int,int], np.ndarray] | None = None,
) -> list[dict]:
    """All paired outcomes for a single independent simulation replication.

    Oracles are included as DIAGNOSTIC ONLY. They are inadmissible in
    comparisons of operational forecast selectors.
    """
    data = make_series(scenario,seed) if generated is None else generated
    horizon_set = (1,3) if scenario.study == "A" and scenario.n_obs == 50 else horizons
    valid = tuple(h for h in horizons if h in horizon_set)
    if not valid:
        return []
    origins = outer_origins(scenario,valid,count=outer_count)
    rows=[]
    for T in origins:
        # Classical scores and past reconstruction oracle do not depend on h.
        classical_by_d={}
        for d in orders:
            window=scenario.window
            if d>=window:
                raise ValueError("d must be smaller than L.")
            classical_by_d[d]=_spectral_candidates(
                data.observed[T-window:T],
                data.trend[T-window:T],
                order=d,grid_points=grid_points,
            )
        for h in valid:
            study=run_weighted_surface_study(
                data.observed[:T+h],
                methods=methods,orders=orders,window=scenario.window,
                horizon=h,stride=max(1,h),
                max_folds=max_folds,grid_points=grid_points,
                refine_pooled=False,holdout=True,
                branch_min_support=3,branch_decision_k=3,branch_score_k=3,
                precomputed_grid_losses=(
                    {d: precomputed_losses[(int(T),int(h),int(d))] for d in orders}
                    if precomputed_losses is not None else None
                ),
            )
            for d in orders:
                grid,fits,reference,recovery_curve=classical_by_d[d]
                latent_oracle=_oracle_future(
                    grid,fits,data.trend[T:T+h],order=d,horizon=h,
                )
                choices={
                    **{f"classical_{key}":value for key,value in reference.items()
                       if not key.startswith("oracle")},
                    "oracle_recovery":reference["oracle_recovery"],
                    "oracle_latent_future":latent_oracle,
                }
                choices.update({f"fixed_{s:g}":s for s in FIXED})
                condition=study.summary[study.summary.d==d]
                tracking_details = {}
                for entry in condition.itertuples():
                    choices[f"pooled_{entry.method}"]=float(entry.pooled_s)
                    name=f"tracked_{entry.method}"
                    choices[name]=float(entry.tracked_s)
                    sub=study.branches[
                        (study.branches.d==d)&(study.branches.method==entry.method)
                    ]
                    tracking_details[name]={
                        "branch_support":int(entry.tracked_support),
                        "n_branches":int(sub.branch.nunique()),
                        "n_local_minima":int(len(sub)),
                    }
                for selector,s in choices.items():
                    scores=_score(
                        data.observed,data.trend,data.seasonality,
                        T=T,L=scenario.window,h=h,d=d,s=float(s),
                    )
                    rows.append({
                        "study":scenario.study,"scenario":scenario.key,
                        "shape":scenario.shape,"n_obs":scenario.n_obs,
                        "noise":scenario.noise,"sigma":scenario.sigma,
                        "seasonal":int(scenario.seasonal),
                        "seed":int(seed),"origin":int(T),
                        "d":int(d),"L":int(scenario.window),"h":int(h),
                        "selector":selector,
                        "is_oracle":int(selector.startswith("oracle_")),
                        **tracking_details.get(selector, {
                            "branch_support":0,"n_branches":0,"n_local_minima":0,
                        }),
                        **scores,
                    })
    return rows
