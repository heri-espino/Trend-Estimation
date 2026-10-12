"""Forecast-optimal finite-difference mean with exact profiling of mu.

Extends (does not replace) the existing Guerrero (2007) plug-in solver.

For d>=1 and L>d, D = finite_difference operator and Q = D.T @ D:
    tau_hat(S, mu) = H(S) @ x + mu * b_fit(S),
    b_fit(S) = (I-H(S)) @ p = lambda*H(S)@D.T@ones,
    D @ p = ones, p_j = binomial(j,d).
The equality for b_fit is valid at finite lambda; the first expression
remains valid at exact S=1 (the infinite-lambda limit).

The *affine* forecast is
    zhat_t(S,mu) = G @ H(S) @ x_t
                  + mu * (G @ b_fit(S) + g)
                 = a_t(S) + mu*b(S),
where g is the nonzero-difference continuation vector.

For fixed S and completed historical origin weights w, the MSE
criterion is quadratic in a COMMON historical mu. It has analytical
minimizer, unless b(S) vanishes. This is not the same model as
estimating an independent Guerrero plug-in mu_t from each x_t.

A selector NEVER accesses future data beyond supplied y_available.
Outer observed and latent targets must be scored separately.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import comb

import numpy as np

from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.forecasting.operators import finite_difference_forecast_operator
from trend_estimation.utils.arrays import as_1d_float_array


@dataclass(frozen=True)
class AffineMeanForecast:
    fitted: np.ndarray
    forecast: np.ndarray
    mu: float
    smoothness: float
    lambda_: float
    penalty_edf: float
    # For plug-in mu_hat = mean(Dx) only: the actual fitted-value
    # operator has trace(H + b_fit @ c.T), NOT trace(H).
    plugin_edf: float


@dataclass(frozen=True)
class MeanDifferenceCVSelection:
    mode: str
    selected_s: float
    selected_mu: float
    selected_loss: float
    grid: np.ndarray
    weighted_losses: np.ndarray
    fold_losses: np.ndarray
    mu_by_s: np.ndarray
    identified_mu_by_s: np.ndarray
    historical_origins: np.ndarray
    forecast_fit: AffineMeanForecast


def polynomial_difference_particular(n_obs: int, order: int) -> np.ndarray:
    """p_j=choose(j,d), j=0..L-1, hence D_d @ p == ones.

    d=0 deliberately excluded here: the research concerns temporal
    differences and their drift, not a centered level parameter.
    """
    n, d = int(n_obs), int(order)
    if not (1 <= d < n):
        raise ValueError("Require 1 <= order < n_obs.")
    return np.fromiter((comb(j,d) if j>=d else 0 for j in range(n)),
                       dtype=float, count=n)


def observed_mean_difference(y, order: int) -> float:
    """Guerrero (2007), equation (17): mean of OBSERVED d-th differences."""
    x = as_1d_float_array(y)
    solver = cached_pure_solver(len(x), int(order))
    if not (1 <= int(order) < len(x)):
        raise ValueError("Require 1 <= order < length of y.")
    return float(np.mean(solver.D @ x))


def affine_mean_components(window, *, order: int, smoothness: float, horizon: int):
    """Return (trend_at_mu0, trend_mu_loading, forecast_at_mu0,
    forecast_mu_loading) without unstable lambda * inverse at S=1.
    """
    x=as_1d_float_array(window)
    d=int(order)
    if not (1 <= d < len(x)) or int(horizon)<1:
        raise ValueError("Require 1 <= order < L and horizon >= 1.")
    s=float(smoothness)
    if not np.isfinite(s) or not 0. <= s <= 1.:
        raise ValueError("Smoothness must be finite and in [0,1].")
    solver=cached_pure_solver(len(x),d)
    lam=solver.lambda_from_s(s)
    alpha=np.zeros_like(solver.eigvals) if np.isinf(lam) else (
        1./(1.+lam*solver.eigvals)
    )
    if np.isinf(lam):
        alpha[:d]=1.
    U=solver.eigvecs
    base=U@(alpha*(U.T@x))
    p=polynomial_difference_particular(len(x),d)
    loading=U@((1.-alpha)*(U.T@p))
    operator=finite_difference_forecast_operator(len(x),d,int(horizon))
    return base,loading,operator.trend_matrix@base,(
        operator.trend_matrix@loading+operator.drift_loading
    )


def fit_mean_difference_forecast(window, *, order:int, smoothness:float,
                                 horizon:int, mu:float) -> AffineMeanForecast:
    """Fitted trend and h-step forecast at fixed (S,mu), endpoints exact."""
    x=as_1d_float_array(window)
    if not np.isfinite(mu):
        raise ValueError("mu must be finite.")
    base,load,forward,forward_load=affine_mean_components(
        x,order=order,smoothness=smoothness,horizon=horizon
    )
    solver=cached_pure_solver(len(x),int(order))
    lam=solver.lambda_from_s(float(smoothness))
    # The Guerrero data plug-in estimator is a LINEAR map:
    #   H x + b_fit*(1' D x)/(L-d).
    # Report its genuine trace separately from trace(H).
    c=solver.D.T@np.ones(len(x)-int(order))/(len(x)-int(order))
    plugin_edf=(len(x)-(len(x)-int(order))*float(smoothness)) + float(c@load)
    return AffineMeanForecast(
        fitted=base+float(mu)*load,
        forecast=forward+float(mu)*forward_load,
        mu=float(mu),smoothness=float(smoothness),
        lambda_=float(lam),
        penalty_edf=len(x)-(len(x)-int(order))*float(smoothness),
        plugin_edf=float(plugin_edf),
    )


def profile_mean_difference(
    residuals:np.ndarray, future_mu_loading:np.ndarray,
    normalized_weights:np.ndarray, *, tolerance:float=1e-13
) -> tuple[float,bool]:
    """Exact weighted least-squares profile of one shared mu at fixed S.

    residuals: (completed_origins, horizon)
    loading: (horizon,) common to every origin for fixed (d,L,h,S).
    Normalizing weights does not change optimal mu.
    If loading is zero, mu is unidentified, choose mu=0 only as a
    deterministic convention and record identified=False.
    """
    r=np.asarray(residuals,dtype=float)
    b=np.asarray(future_mu_loading,dtype=float).reshape(-1)
    w=np.asarray(normalized_weights,dtype=float).reshape(-1)
    if r.ndim!=2 or r.shape[1]!=len(b) or len(w)!=len(r):
        raise ValueError("Invalid residual, loading or weight shapes.")
    if not len(w) or not np.all(np.isfinite(r)) or not np.all(np.isfinite(b)):
        raise ValueError("Residuals and loadings must be finite.")
    if np.any(~np.isfinite(w)) or np.any(w<0) or w.sum()<=0:
        raise ValueError("Weights must be finite, nonnegative and have positive sum.")
    w=w/w.sum()
    denominator=float(b@b)
    if denominator <= tolerance:
        return 0.,False
    # sum_q w_q b.T(z_q-a_q) / (b.T b)
    mu=float(w@(r@b)/denominator)
    return mu,True


def select_mean_difference_cv(
    y_available, *, order:int, window:int, horizon:int,
    historical_origins, smoothness_grid,
    mean_mode:str="profile", weights=None
) -> MeanDifferenceCVSelection:
    """Select S and (for profile mode) COMMON mu on completed historical F.

    mean_mode:
      zero: mu=0 (reproduce pure forecast model).
      guerrero: each historical x_t has TRAINING-ONLY mean(D x_t);
                operational mu_T = mean(D x_T).
      profile: a single mu(S) fitted analytically to COMPLETED
               historical validation losses; operational mu_T=mu(S*).

    Historical origins are 0-based *exclusive* sample end indices.
    The latest completed target for an origin t is y[t:t+h].
    All t+h must be <= len(y_available); nothing after this prefix
    is passed to the selector.
    """
    y=as_1d_float_array(y_available)
    L,d,h=int(window),int(order),int(horizon)
    if not (1<=d<L<=len(y)) or h<1:
        raise ValueError("Require 1<=d<L<=len(y) and horizon>=1.")
    if mean_mode not in {"zero","guerrero","profile"}:
        raise ValueError("mean_mode must be 'zero', 'guerrero' or 'profile'.")
    origin=np.asarray(historical_origins,dtype=int).reshape(-1)
    if len(origin)<1 or np.any(origin<L) or np.any(origin+h>len(y)):
        raise ValueError("Every historical origin must be completed at current T.")
    if len(np.unique(origin))!=len(origin) or np.any(np.diff(origin)<=0):
        raise ValueError("Historical origins must be unique and increasing.")
    grid=np.asarray(smoothness_grid,dtype=float)
    if grid.ndim!=1 or not len(grid) or np.any(~np.isfinite(grid)) or (
        np.any(grid<0) or np.any(grid>1)
    ):
        raise ValueError("Smoothness grid must be finite, 1D and in [0,1].")
    w=np.ones(len(origin),dtype=float) if weights is None else np.asarray(
        weights,dtype=float
    )
    if w.shape!=(len(origin),) or not np.all(np.isfinite(w)) or (
        np.any(w<0) or w.sum()<=0
    ):
        raise ValueError("Weights must be nonnegative with positive total.")
    w=w/w.sum()
    X=np.stack([y[t-L:t] for t in origin])
    Z=np.stack([y[t:t+h] for t in origin])
    solver=cached_pure_solver(L,d)
    U=solver.eigvecs
    spectral=X@U
    operator=finite_difference_forecast_operator(L,d,h)
    spectral_to_future=operator.trend_matrix@U
    p=polynomial_difference_particular(L,d)
    spectral_p=U.T@p
    mus_guerrero=(X@solver.D.T@np.ones(L-d))/(L-d) if mean_mode=="guerrero" else None
    loss=np.empty((len(origin),len(grid)),dtype=float)
    selected_mus=np.empty(len(grid),dtype=float)
    identified=np.ones(len(grid),dtype=bool)
    for j,s in enumerate(grid):
        lam=solver.lambda_from_s(float(s))
        alpha=np.zeros_like(solver.eigvals) if np.isinf(lam) else (
            1./(1.+lam*solver.eigvals)
        )
        if np.isinf(lam):
            alpha[:d]=1.
        forecast0=(spectral*alpha)@spectral_to_future.T
        fitted_loading=U@((1.-alpha)*spectral_p)
        b=operator.trend_matrix@fitted_loading+operator.drift_loading
        residual=Z-forecast0
        if mean_mode=="profile":
            mu,identified[j]=profile_mean_difference(residual,b,w)
            prediction=forecast0+mu*b[None,:]
        elif mean_mode=="guerrero":
            mu=observed_mean_difference(y[-L:],d)
            prediction=forecast0+mus_guerrero[:,None]*b[None,:]
        else:
            mu=0.
            prediction=forecast0
        selected_mus[j]=mu
        loss[:,j]=np.mean((Z-prediction)**2,axis=1)
    weighted_loss=w@loss
    best=int(np.argmin(weighted_loss))
    s=float(grid[best])
    chosen_mu=float(selected_mus[best])
    operational=fit_mean_difference_forecast(
        y[-L:],order=d,smoothness=s,horizon=h,mu=chosen_mu
    )
    return MeanDifferenceCVSelection(
        mode=mean_mode,selected_s=s,selected_mu=chosen_mu,
        selected_loss=float(weighted_loss[best]),
        grid=grid.copy(),weighted_losses=weighted_loss,
        fold_losses=loss,mu_by_s=selected_mus,
        identified_mu_by_s=identified,
        historical_origins=origin.copy(),
        forecast_fit=operational,
    )
