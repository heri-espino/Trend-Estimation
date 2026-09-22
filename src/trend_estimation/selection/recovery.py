from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

from trend_estimation.core.derivatives import (
    mse_from_prediction_derivatives,
    pure_trend_derivatives,
)
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.core.smoothness import lambda_to_smoothness
from trend_estimation.selection.numerical import (
    StationaryPointSearchResult,
    find_stationary_points_log_lambda,
)
from trend_estimation.utils.arrays import as_1d_float_array


@dataclass(frozen=True)
class RecoveryLossDerivatives:
    """Oracle trend-recovery MSE and its first two lambda derivatives."""

    value: float
    first: float
    second: float


@dataclass(frozen=True)
class RecoveryOptimalSelection:
    """Oracle recovery-optimal penalty for a known latent trend."""

    order: int
    lambda_: float
    smoothness_: float
    objective_: float
    search_: StationaryPointSearchResult


@dataclass(frozen=True)
class PreparedRollingPureRecoveryObjective:
    """Vectorized oracle recovery objective across fixed-width training windows."""

    eigvals: np.ndarray
    spectral_history: np.ndarray
    eigvecs: np.ndarray
    true_trends: np.ndarray
    n_origins: int
    n_scored: int

    def evaluate(self, lambda_: float) -> RecoveryLossDerivatives:
        """Evaluate pooled recovery loss and lambda derivatives."""

        lambda_ = float(lambda_)
        if lambda_ < 0.0:
            raise ValueError("lambda_ must be nonnegative.")

        delta = self.eigvals
        alpha = 1.0 / (1.0 + lambda_ * delta)
        first_weight = -delta * alpha**2
        second_weight = 2.0 * delta**2 * alpha**3

        trend = (self.spectral_history * alpha) @ self.eigvecs.T
        trend_first = (self.spectral_history * first_weight) @ self.eigvecs.T
        trend_second = (self.spectral_history * second_weight) @ self.eigvecs.T

        residual = self.true_trends - trend
        n = float(self.n_scored)
        value = float(np.sum(residual**2) / n)
        first = float((-2.0 / n) * np.sum(residual * trend_first))
        second = float(
            (2.0 / n)
            * (
                np.sum(trend_first**2)
                - np.sum(residual * trend_second)
            )
        )
        return RecoveryLossDerivatives(value=value, first=first, second=second)


def prepare_rolling_pure_recovery_objective(
    y_observed,
    true_trend,
    splits: Iterable,
    *,
    order: int,
) -> PreparedRollingPureRecoveryObjective:
    """Prepare pooled oracle recovery loss on rolling training windows."""

    y_observed = as_1d_float_array(y_observed)
    true_trend = as_1d_float_array(true_trend)
    if y_observed.size != true_trend.size:
        raise ValueError("y_observed and true_trend must have the same length.")

    split_list = list(splits)
    if not split_list:
        raise ValueError("At least one split is required.")

    train_lengths = [y_observed[split.train].size for split in split_list]
    if any(length <= 0 for length in train_lengths):
        raise ValueError("Training windows must be non-empty.")
    if len(set(train_lengths)) != 1:
        raise ValueError("Prepared recovery objective requires fixed-width windows.")

    n_fit = int(train_lengths[0])
    solver = cached_pure_solver(n_fit, int(order))
    history = np.stack([y_observed[split.train] for split in split_list], axis=0)
    latent = np.stack([true_trend[split.train] for split in split_list], axis=0)

    return PreparedRollingPureRecoveryObjective(
        eigvals=solver.eigvals,
        spectral_history=history @ solver.eigvecs,
        eigvecs=solver.eigvecs,
        true_trends=latent,
        n_origins=len(split_list),
        n_scored=int(latent.size),
    )


def pure_recovery_loss_derivatives(
    y_observed,
    true_trend,
    *,
    order: int,
    lambda_: float,
) -> RecoveryLossDerivatives:
    """Differentiate latent-trend recovery MSE for the pure smoother."""

    y_observed = as_1d_float_array(y_observed)
    true_trend = as_1d_float_array(true_trend)
    if y_observed.size != true_trend.size:
        raise ValueError("y_observed and true_trend must have the same length.")
    if y_observed.size == 0:
        raise ValueError("Inputs must not be empty.")

    derivatives = pure_trend_derivatives(
        y_observed,
        order=int(order),
        lambda_=float(lambda_),
    )
    value, first, second = mse_from_prediction_derivatives(
        true_trend,
        derivatives.trend,
        derivatives.first,
        derivatives.second,
    )
    return RecoveryLossDerivatives(value=value, first=first, second=second)


def select_recovery_optimal_lambda(
    y_observed,
    true_trend,
    *,
    order: int,
    log_bounds: tuple[float, float] = (-12.0, 20.0),
    n_grid: int = 257,
) -> RecoveryOptimalSelection:
    """Select the oracle recovery-optimal lambda for a simulated sample."""

    y_observed = as_1d_float_array(y_observed)
    true_trend = as_1d_float_array(true_trend)
    if y_observed.size != true_trend.size:
        raise ValueError("y_observed and true_trend must have the same length.")
    if y_observed.size == 0:
        raise ValueError("Inputs must not be empty.")

    order = int(order)

    def value_grad_hess(lambda_value: float):
        result = pure_recovery_loss_derivatives(
            y_observed,
            true_trend,
            order=order,
            lambda_=lambda_value,
        )
        return result.value, result.first, result.second

    search = find_stationary_points_log_lambda(
        value_grad_hess,
        log_bounds=log_bounds,
        n_grid=n_grid,
    )
    smoothness = lambda_to_smoothness(
        search.best_lambda_,
        n_obs=y_observed.size,
        order=order,
    )
    return RecoveryOptimalSelection(
        order=order,
        lambda_=search.best_lambda_,
        smoothness_=smoothness,
        objective_=search.best_objective_,
        search_=search,
    )
