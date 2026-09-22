from __future__ import annotations

from functools import lru_cache

import numpy as np

from trend_estimation.core.solvers import GuerreroSpectralSolver
from trend_estimation.forecasting.extrapolation import forecast_trend
from trend_estimation.models.base import BaseTrendEstimator, TrendFitResult
from trend_estimation.utils.arrays import as_1d_float_array


@lru_cache(maxsize=32)
def _cached_solver(n_obs: int, order: int) -> GuerreroSpectralSolver:
    return GuerreroSpectralSolver(int(n_obs), int(order))


class _DriftPenalizedTrend(BaseTrendEstimator):
    """Internal configurable finite-difference penalized trend.

    Public users should choose an explicit model class such as GuerreroTrend,
    IteratedDriftTrend, HPTrend, or WhittakerTrend.
    """

    def __init__(
        self,
        order: int = 2,
        smoothness: float | None = 0.75,
        lambda_: float | None = None,
        *,
        drift_mode: str,
    ):
        self.order = int(order)
        self.smoothness = smoothness
        self.lambda_ = lambda_
        self.drift_mode = str(drift_mode)

    def fit(self, y, X=None):
        y = as_1d_float_array(y)
        self.y_ = y
        self.n_obs_ = y.size
        self.solver_ = _cached_solver(y.size, self.order)

        if self.lambda_ is None:
            if self.smoothness is None:
                raise ValueError("Either smoothness or lambda_ must be provided.")
            lambda_value = self.solver_.lambda_from_s(float(self.smoothness))
        else:
            lambda_value = float(self.lambda_)

        result = self.solver_.fit_for_lambda(
            y,
            lambda_value,
            drift_mode=self.drift_mode,
        )

        self.trend_ = result.trend
        self.fitted_values_ = self.trend_
        self.residuals_ = y - self.trend_
        self.m_hat_ = result.m_hat
        self.lambda_ = result.lambda_
        self.smoothness_ = result.smoothness
        self.sigma2_hat_ = result.sigma2_hat
        self.drift_mode_ = result.drift_mode

        model_name = {
            "data": "guerrero_plugin",
            "iterated": "iterated_drift",
            "zero": "zero_drift_penalized",
        }[self.drift_mode_]

        self.fit_result_ = TrendFitResult(
            y_=self.y_,
            trend_=self.trend_,
            residuals_=self.residuals_,
            fitted_values_=self.fitted_values_,
            order_=self.order,
            lambda_=self.lambda_,
            smoothness_=self.smoothness_,
            metadata_={
                "model": model_name,
                "drift_mode": self.drift_mode_,
                "m_hat": self.m_hat_,
                "sigma2_hat": self.sigma2_hat_,
            },
        )
        return self

    def forecast(self, steps: int) -> np.ndarray:
        if not hasattr(self, "trend_"):
            raise RuntimeError("Call fit before forecast.")
        return forecast_trend(self.trend_, self.order, self.m_hat_, int(steps))
