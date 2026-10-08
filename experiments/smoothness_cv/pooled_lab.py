"""Standalone pooled forecast-CV computation for the interactive research app.

No branch tracking, no future-data leakage, and no changes to frozen experiments.
All windows, horizons and origin spacing are in *observations*, not calendar days.
The objective is observation-forecast MSE of pure PLS polynomial continuation.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.core.smoothness import smoothness_to_lambda
from trend_estimation.forecasting.objectives import prepare_rolling_pure_forecast_objective
from trend_estimation.forecasting.operators import finite_difference_forecast_operator
from trend_estimation.validation.rolling_origin import RollingOriginSplit


@dataclass(frozen=True)
class PooledLabResult:
    """Loss curves and decisions at one outer forecast origin."""

    grid: np.ndarray
    origins: np.ndarray                  # zero-based end-exclusive forecast origins
    fold_losses: np.ndarray              # (n_folds, n_grid) observation forecast MSE
    pooled_losses: np.ndarray            # (n_grid,)
    fold_grid_minima: np.ndarray         # (n_folds,)
    pooled_s: float
    pooled_mse: float
    last_s: float
    last_validation_mse: float
    one_step_s: float | None
    one_step_validation_mse: float | None
    selected_origin: int                 # last observed point in input history, exclusive
    window: int
    order: int
    horizon: int
    stride: int
    holdout: bool
    final_trends: dict[str, np.ndarray]
    future_forecasts: dict[str, np.ndarray]
    test_mse: dict[str, float]
    losses_at_pooled: np.ndarray
    losses_at_last: np.ndarray
    selected_lambda: float
    degrees_of_freedom: float

    def loss_table(self) -> pd.DataFrame:
        cols = {f"S={s:.6f}": self.fold_losses[:, i]
                for i, s in enumerate(self.grid)}
        return pd.DataFrame({
            "fold": np.arange(1, len(self.origins) + 1),
            "origin_1based": self.origins,
            "train_start_1based": self.origins - self.window + 1,
            "train_end_1based": self.origins,
            "validation_start_1based": self.origins + 1,
            "validation_end_1based": self.origins + self.horizon,
            **cols,
        })

    def minima_table(self) -> pd.DataFrame:
        ids = np.arange(len(self.origins))
        return pd.DataFrame({
            "fold": ids + 1,
            "origin_1based": self.origins,
            "grid_minimum_s": self.fold_grid_minima,
            "grid_minimum_mse": self.fold_losses[ids, np.argmin(self.fold_losses, axis=1)],
            "mse_at_pooled_s": self.losses_at_pooled,
            "mse_at_last_s": self.losses_at_last,
        })


def chronological_origins(
    n_available: int, window: int, horizon: int, stride: int, max_folds: int
) -> np.ndarray:
    """End-exclusive fit origins, anchored at the latest completed validation block.

    Unlike a forward-anchored range, this always includes n_available-horizon.
    All validation blocks finish at or before n_available.
    """
    args = (n_available, window, horizon, stride, max_folds)
    if any(not isinstance(v, (int, np.integer)) for v in args):
        raise ValueError("Origin parameters must be integers.")
    if window < 3 or horizon < 1 or stride < 1 or max_folds < 1:
        raise ValueError("Require window >= 3 and positive horizon, stride and max_folds.")
    if n_available < window + horizon:
        raise ValueError("Not enough pretest history for one complete forecast-CV fold.")
    backwards = np.arange(n_available - horizon, window - 1, -stride, dtype=int)
    return backwards[:max_folds][::-1].copy()


def fold_loss_at_lambda(prepared, lambda_: float) -> np.ndarray:
    """Exact per-origin forecast MSE using the cached spectral prepared objective."""
    eigvals = prepared.eigvals
    if np.isinf(lambda_):
        weights = np.zeros_like(eigvals)
        weights[:prepared.nullity] = 1.0
    else:
        weights = 1.0 / (1.0 + float(lambda_) * eigvals)
    forecast = (
        (prepared.spectral_history * weights)
        @ prepared.spectral_to_future.T
        + prepared.prediction_offset
    )
    return np.mean((prepared.targets - forecast) ** 2, axis=1)


@lru_cache(maxsize=40)
def cached_uniform_spectral_weights(window: int, order: int, grid_points: int) -> np.ndarray:
    """Reusable spectral response for a *uniform* S grid.

    Crucial for large simulations: this matrix depends on (L,d,grid),
    not on the time series, forecast origin, or random seed. Cached per
    worker process to avoid thousands of repeated lambda inversions.
    Treat the returned array as read-only.
    """
    grid = np.linspace(0., 1., grid_points)
    eigvals = cached_pure_solver(window, order).eigvals
    weights = np.empty((grid_points, window), dtype=float)
    for i, s in enumerate(grid):
        lam = smoothness_to_lambda(float(s), window, order)
        if np.isinf(lam):
            weights[i] = 0.
            weights[i, :order] = 1.
        else:
            weights[i] = 1. / (1. + lam*eigvals)
    weights.setflags(write=False)
    return weights


def all_grid_fold_losses(prepared, grid: np.ndarray, window: int, order: int) -> np.ndarray:
    """Compute F_t(S_k) for all origins and candidate smoothness points."""
    if np.array_equal(grid, np.linspace(0., 1., len(grid))):
        weights = cached_uniform_spectral_weights(window, order, len(grid))
    else:
        weights = np.empty((len(grid), window), dtype=float)
        for i, s in enumerate(grid):
            lam = smoothness_to_lambda(float(s), window, order)
            if np.isinf(lam):
                weights[i] = 0.0
                weights[i, :order] = 1.0
            else:
                weights[i] = 1.0 / (1.0 + lam * prepared.eigvals)
    # Spectral histories are (folds, L), weights (grid, L), future map (h, L).
    predicted = np.einsum(
        "ml,kl,hl->mkh",
        prepared.spectral_history,
        weights,
        prepared.spectral_to_future,
        optimize=True,
    ) + prepared.prediction_offset[:, None, :]
    return np.mean((prepared.targets[:, None, :] - predicted) ** 2, axis=2)


def select_from_grid(
    grid: np.ndarray,
    sampled_loss: np.ndarray,
    exact_objective,
    *,
    refine: bool,
) -> tuple[float, float]:
    """Compare grid candidates and bounded refinements of sampled local valleys.

    Not a proof that every narrow local minimum was discovered. Endpoints are
    always explicitly tested. Ties prefer the smaller S.
    """
    grid = np.asarray(grid, dtype=float)
    losses = np.asarray(sampled_loss, dtype=float)
    candidates = [(float(s), float(v)) for s, v in zip(grid, losses)]
    if refine:
        for i in range(1, len(grid) - 1):
            if losses[i] <= losses[i - 1] and losses[i] <= losses[i + 1]:
                result = minimize_scalar(
                    exact_objective,
                    bounds=(float(grid[i - 1]), float(grid[i + 1])),
                    method="bounded",
                    options={"xatol": 1e-8},
                )
                if result.success:
                    candidates.append((float(result.x), float(result.fun)))
        # Check each endpoint's adjacent open interval as well as the point.
        for a, b in ((grid[0], grid[1]), (grid[-2], grid[-1])):
            result = minimize_scalar(
                exact_objective,
                bounds=(float(a), float(b)),
                method="bounded",
                options={"xatol": 1e-9},
            )
            if result.success:
                candidates.append((float(result.x), float(result.fun)))
    best = min(candidates, key=lambda pair: (pair[1], pair[0]))
    return best


def fit_window_forecast(
    history, *, origin: int, window: int, order: int,
    horizon: int, smoothness: float
) -> tuple[np.ndarray, np.ndarray]:
    """Fresh fit and native order-d zero-future-differences extrapolation."""
    y = np.asarray(history, dtype=float)
    if not window <= origin <= len(y):
        raise ValueError("The requested origin does not admit a full fit window.")
    trend = cached_pure_solver(window, order).fit_for_s(
        y[origin - window:origin], float(smoothness)
    ).trend
    operator = finite_difference_forecast_operator(window, order, horizon)
    return trend, operator.trend_matrix @ trend


def analyze_pooled(
    observed,
    *,
    window: int = 60,
    order: int = 2,
    horizon: int = 5,
    stride: int = 5,
    max_folds: int = 18,
    grid_points: int = 101,
    refine: bool = True,
    holdout: bool = False,
    compare_one_step: bool = True,
) -> PooledLabResult:
    """Analyze pooled F(S), per-fold F_t(S) and independent outer forecasts.

    With holdout=True, the last h observations are *never* supplied to a CV
    objective nor the final fit. They are used after selection for scoring.
    With holdout=False, no outer score exists; forecast beyond all given data.
    """
    y = np.asarray(observed, dtype=float)
    if y.ndim != 1 or not np.all(np.isfinite(y)):
        raise ValueError("The input must be a one-dimensional series of finite values.")
    if order < 1 or order > 4 or window <= order or window < 3:
        raise ValueError("Require 1 <= d <= 4 and L > d.")
    if horizon < 1 or grid_points < 11 or grid_points > 501:
        raise ValueError("Require h >= 1 and between 11 and 501 grid points.")
    if horizon > 90 or window > 500:
        raise ValueError("For interactive use, require h <= 90 and L <= 500.")
    T = len(y) - horizon if holdout else len(y)
    origins = chronological_origins(T, window, horizon, stride, max_folds)
    splits = [
        RollingOriginSplit(
            train=slice(int(t) - window, int(t)),
            validation=slice(int(t), int(t) + horizon),
        )
        for t in origins
    ]
    # Critical information boundary: only prefix y[:T] reaches the selector.
    prepared = prepare_rolling_pure_forecast_objective(y[:T], splits, order=order)
    grid = np.linspace(0.0, 1.0, grid_points)
    fold_losses = all_grid_fold_losses(prepared, grid, window, order)
    pooled_curve = np.mean(fold_losses, axis=0)
    fold_grid_minima = grid[np.argmin(fold_losses, axis=1)]

    def at_s(s):
        return fold_loss_at_lambda(
            prepared, smoothness_to_lambda(float(s), window, order)
        )

    def pool_value(s):
        return float(np.mean(at_s(s)))

    pooled_s, pooled_mse = select_from_grid(
        grid, pooled_curve, pool_value, refine=refine
    )
    last_s, last_mse = select_from_grid(
        grid, fold_losses[-1], lambda s: float(at_s(s)[-1]), refine=refine
    )

    one_step_s, one_step_mse = None, None
    if compare_one_step:
        splits_one = [
            RollingOriginSplit(
                train=sp.train,
                validation=slice(sp.validation.start, sp.validation.start + 1),
            )
            for sp in splits
        ]
        prepared_one = prepare_rolling_pure_forecast_objective(
            y[:T], splits_one, order=order
        )
        one_grid = np.mean(
            all_grid_fold_losses(prepared_one, grid, window, order), axis=0
        )
        def one_value(s):
            return float(np.mean(fold_loss_at_lambda(
                prepared_one, smoothness_to_lambda(float(s), window, order)
            )))
        one_step_s, one_step_mse = select_from_grid(
            grid, one_grid, one_value, refine=refine
        )

    selected = {"Pooled CV": pooled_s, "Last fold": last_s}
    if one_step_s is not None:
        selected["One-step CV"] = one_step_s
    trends, futures, scores = {}, {}, {}
    for method, s in selected.items():
        trend, future = fit_window_forecast(
            y[:T], origin=T, window=window, order=order,
            horizon=horizon, smoothness=s,
        )
        trends[method] = trend
        futures[method] = future
        if holdout:
            scores[method] = float(np.mean((y[T:T + horizon] - future) ** 2))

    lam = smoothness_to_lambda(float(pooled_s), window, order)
    return PooledLabResult(
        grid=grid,
        origins=origins,
        fold_losses=fold_losses,
        pooled_losses=pooled_curve,
        fold_grid_minima=fold_grid_minima,
        pooled_s=float(pooled_s),
        pooled_mse=float(pooled_mse),
        last_s=float(last_s),
        last_validation_mse=float(last_mse),
        one_step_s=one_step_s,
        one_step_validation_mse=one_step_mse,
        selected_origin=T,
        window=window,
        order=order,
        horizon=horizon,
        stride=stride,
        holdout=bool(holdout),
        final_trends=trends,
        future_forecasts=futures,
        test_mse=scores,
        losses_at_pooled=at_s(pooled_s),
        losses_at_last=at_s(last_s),
        selected_lambda=float(lam),
        degrees_of_freedom=float(window - (window - order) * pooled_s),
    )
