from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

from trend_estimation.core.derivatives import (
    mse_from_prediction_derivatives,
    pure_trend_derivatives,
)
from trend_estimation.forecasting.extrapolation import forecast_trend
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


def pure_forecast_loss_derivatives(
    y_past,
    y_future,
    *,
    order: int,
    lambda_: float,
) -> ForecastLossDerivatives:
    r"""Differentiate genuine future-block MSE for the pure penalized trend.

    Let S = (I + lambda Q)^(-1) and let H denote the linear continuation
    implemented by forecast_trend with zero order-th-difference drift.

    prediction = H S y
    prediction' = -H S Q S y
    prediction'' = 2 H S Q S Q S y

    The implementation never constructs H explicitly. Because the pure
    continuation is linear, the same recursion can be applied to the trend and
    to its first two lambda derivatives.
    """

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
    steps = int(y_future.size)
    prediction = forecast_trend(derivatives.trend, int(order), 0.0, steps)
    prediction_first = forecast_trend(derivatives.first, int(order), 0.0, steps)
    prediction_second = forecast_trend(derivatives.second, int(order), 0.0, steps)

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
    r"""Pool future-block forecast losses and derivatives across temporal origins.

    Each split must expose train and validation slices, as produced by
    rolling_origin_splits. Aggregation is observation-weighted:
    CV = sum_j h_j f_j / sum_j h_j.
    """

    y = as_1d_float_array(y)
    split_list = list(splits)
    if not split_list:
        raise ValueError("At least one rolling-origin split is required.")

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
