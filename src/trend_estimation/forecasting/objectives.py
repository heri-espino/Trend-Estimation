from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

from trend_estimation.core.derivatives import (
    mse_from_prediction_derivatives,
    pure_trend_derivatives,
)
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.forecasting.operators import finite_difference_forecast_operator
from trend_estimation.utils.arrays import as_1d_float_array


@dataclass(frozen=True)
class ForecastLossDerivatives:
    """Forecast MSE and its first two derivatives with respect to lambda."""

    value: float
    first: float
    second: float
    prediction: np.ndarray
    prediction_first: np.ndarray
    prediction_second: np.ndarray


@dataclass(frozen=True)
class RollingForecastLossDerivatives:
    """Pooled rolling-origin forecast MSE and lambda derivatives."""

    value: float
    first: float
    second: float
    n_origins: int
    n_scored: int


@dataclass(frozen=True)
class PreparedRollingPureForecastObjective:
    """Vectorized fixed-window rolling forecast objective.

    The eigendecomposition, spectral transforms of training windows, and
    continuation operator are prepared once. Evaluating a new penalty then uses
    only elementwise spectral weights and small matrix products.
    """

    eigvals: np.ndarray
    spectral_history: np.ndarray
    spectral_to_future: np.ndarray
    targets: np.ndarray
    n_origins: int
    n_scored: int

    def evaluate(self, lambda_: float) -> RollingForecastLossDerivatives:
        """Evaluate pooled loss and first two derivatives at one lambda."""

        lambda_ = float(lambda_)
        if lambda_ < 0.0:
            raise ValueError("lambda_ must be nonnegative.")

        delta = self.eigvals
        alpha = 1.0 / (1.0 + lambda_ * delta)
        first_weight = -delta * alpha**2
        second_weight = 2.0 * delta**2 * alpha**3

        prediction = (self.spectral_history * alpha) @ self.spectral_to_future.T
        prediction_first = (
            self.spectral_history * first_weight
        ) @ self.spectral_to_future.T
        prediction_second = (
            self.spectral_history * second_weight
        ) @ self.spectral_to_future.T

        residual = self.targets - prediction
        n = float(self.n_scored)
        value = float(np.sum(residual**2) / n)
        first = float((-2.0 / n) * np.sum(residual * prediction_first))
        second = float(
            (2.0 / n)
            * (
                np.sum(prediction_first**2)
                - np.sum(residual * prediction_second)
            )
        )

        return RollingForecastLossDerivatives(
            value=value,
            first=first,
            second=second,
            n_origins=self.n_origins,
            n_scored=self.n_scored,
        )


def prepare_rolling_pure_forecast_objective(
    y,
    splits: Iterable,
    *,
    order: int,
) -> PreparedRollingPureForecastObjective:
    """Prepare a vectorized rolling objective for fixed-width splits."""

    y = as_1d_float_array(y)
    split_list = list(splits)
    if not split_list:
        raise ValueError("At least one rolling-origin split is required.")

    train_lengths = [y[split.train].size for split in split_list]
    forecast_lengths = [y[split.validation].size for split in split_list]
    if any(length <= 0 for length in train_lengths + forecast_lengths):
        raise ValueError("Rolling-origin blocks must be non-empty.")
    if len(set(train_lengths)) != 1:
        raise ValueError(
            "Prepared rolling objective requires one fixed training-window length."
        )
    if len(set(forecast_lengths)) != 1:
        raise ValueError(
            "Prepared rolling objective requires one fixed forecast horizon."
        )

    n_fit = int(train_lengths[0])
    horizon = int(forecast_lengths[0])
    solver = cached_pure_solver(n_fit, int(order))
    q = solver.eigvecs

    history = np.stack([y[split.train] for split in split_list], axis=0)
    targets = np.stack([y[split.validation] for split in split_list], axis=0)
    spectral_history = history @ q

    operator = finite_difference_forecast_operator(
        n_fit=n_fit,
        order=int(order),
        steps=horizon,
    )
    spectral_to_future = operator.trend_matrix @ q

    return PreparedRollingPureForecastObjective(
        eigvals=solver.eigvals,
        spectral_history=spectral_history,
        spectral_to_future=spectral_to_future,
        targets=targets,
        n_origins=len(split_list),
        n_scored=int(targets.size),
    )


def pure_forecast_loss_derivatives(
    y_past,
    y_future,
    *,
    order: int,
    lambda_: float,
) -> ForecastLossDerivatives:
    """Differentiate genuine future-block MSE for the pure penalized trend."""

    y_past = as_1d_float_array(y_past)
    y_future = as_1d_float_array(y_future)
    if y_past.size == 0:
        raise ValueError("y_past must not be empty.")
    if y_future.size == 0:
        raise ValueError("y_future must not be empty.")

    derivatives = pure_trend_derivatives(
        y_past,
        order=int(order),
        lambda_=float(lambda_),
    )
    operator = finite_difference_forecast_operator(
        n_fit=y_past.size,
        order=int(order),
        steps=int(y_future.size),
    )
    h_matrix = operator.trend_matrix
    prediction = h_matrix @ derivatives.trend
    prediction_first = h_matrix @ derivatives.first
    prediction_second = h_matrix @ derivatives.second

    value, first, second = mse_from_prediction_derivatives(
        y_future,
        prediction,
        prediction_first,
        prediction_second,
    )
    return ForecastLossDerivatives(
        value=value,
        first=first,
        second=second,
        prediction=prediction,
        prediction_first=prediction_first,
        prediction_second=prediction_second,
    )


def rolling_pure_forecast_loss_derivatives(
    y,
    splits: Iterable,
    *,
    order: int,
    lambda_: float,
) -> RollingForecastLossDerivatives:
    """Pool future-block forecast losses across temporal origins."""

    y = as_1d_float_array(y)
    split_list = list(splits)
    if not split_list:
        raise ValueError("At least one rolling-origin split is required.")

    train_lengths = [y[split.train].size for split in split_list]
    forecast_lengths = [y[split.validation].size for split in split_list]
    if len(set(train_lengths)) == 1 and len(set(forecast_lengths)) == 1:
        return prepare_rolling_pure_forecast_objective(
            y,
            split_list,
            order=int(order),
        ).evaluate(float(lambda_))

    total_value = 0.0
    total_first = 0.0
    total_second = 0.0
    total_scored = 0

    for split in split_list:
        y_past = y[split.train]
        y_future = y[split.validation]
        if y_past.size == 0 or y_future.size == 0:
            raise ValueError(
                "Rolling-origin splits must contain non-empty train and validation blocks."
            )

        result = pure_forecast_loss_derivatives(
            y_past,
            y_future,
            order=int(order),
            lambda_=float(lambda_),
        )
        weight = int(y_future.size)
        total_value += weight * result.value
        total_first += weight * result.first
        total_second += weight * result.second
        total_scored += weight

    return RollingForecastLossDerivatives(
        value=float(total_value / total_scored),
        first=float(total_first / total_scored),
        second=float(total_second / total_scored),
        n_origins=len(split_list),
        n_scored=total_scored,
    )
