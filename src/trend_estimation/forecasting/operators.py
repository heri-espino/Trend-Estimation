from __future__ import annotations

from dataclasses import dataclass
from math import comb

import numpy as np


@dataclass(frozen=True)
class ForecastAffineOperator:
    """Affine finite-difference continuation operator.

    Forecasts satisfy

        forecast = trend_matrix @ fitted_trend + drift_loading * m_hat

    for the same recurrence used by forecast_trend.
    """

    trend_matrix: np.ndarray
    drift_loading: np.ndarray

    def apply(self, trend, m_hat: float = 0.0) -> np.ndarray:
        trend = np.asarray(trend, dtype=float).ravel()
        if trend.size != self.trend_matrix.shape[1]:
            raise ValueError(
                f"trend has length {trend.size}; expected {self.trend_matrix.shape[1]}."
            )
        return self.trend_matrix @ trend + self.drift_loading * float(m_hat)


def finite_difference_forecast_operator(
    n_fit: int,
    order: int,
    steps: int,
) -> ForecastAffineOperator:
    """Build the affine operator equivalent to forecast_trend.

    The matrix part is the H used in the active paper's derivative formulas.
    The drift-loading vector matters for nonzero-drift extensions such as the
    Guerrero plug-in model.
    """

    n_fit = int(n_fit)
    order = int(order)
    steps = int(steps)

    if n_fit <= 0:
        raise ValueError("n_fit must be positive.")
    if order < 0:
        raise ValueError("order must be nonnegative.")
    if steps < 0:
        raise ValueError("steps must be nonnegative.")

    H = np.zeros((steps, n_fit), dtype=float)
    drift = np.zeros(steps, dtype=float)
    if steps == 0:
        return ForecastAffineOperator(H, drift)

    if order == 0:
        drift[:] = 1.0
        return ForecastAffineOperator(H, drift)

    d_eff = min(order, n_fit)
    state_H = np.zeros((d_eff, n_fit), dtype=float)
    state_H[:, n_fit - d_eff :] = np.eye(d_eff, dtype=float)
    state_m = np.zeros(d_eff, dtype=float)

    coeffs = np.array(
        [(-1) ** (d_eff - k) * comb(d_eff, k) for k in range(d_eff)],
        dtype=float,
    )

    for i in range(steps):
        next_H = -(coeffs @ state_H)
        next_m = 1.0 - float(coeffs @ state_m)

        H[i] = next_H
        drift[i] = next_m

        if d_eff > 1:
            state_H[:-1] = state_H[1:]
            state_m[:-1] = state_m[1:]
        state_H[-1] = next_H
        state_m[-1] = next_m

    return ForecastAffineOperator(H, drift)
