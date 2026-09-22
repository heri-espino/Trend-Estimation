from __future__ import annotations

from dataclasses import dataclass

from trend_estimation.core.derivatives import (
    mse_from_prediction_derivatives,
    pure_trend_derivatives,
)
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


def pure_recovery_loss_derivatives(
    y_observed,
    true_trend,
    *,
    order: int,
    lambda_: float,
) -> RecoveryLossDerivatives:
    """Differentiate latent-trend recovery MSE for the pure smoother.

    This objective is available only in simulations where the latent trend is
    known. It is not a real-data tuning rule.
    """

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
