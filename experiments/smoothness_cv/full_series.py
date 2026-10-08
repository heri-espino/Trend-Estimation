"""Descriptive whole-series trend, separate from any forecast-CV selection.

Fit a penalized least-squares trend to every observed value *after* the
selected order and smoothness are fixed by either independent CV procedure.
Using the full series (including an outer test, when present) is deliberately
in-sample smoothing; the result must not be used to score forecasts.
"""
from __future__ import annotations

import numpy as np
import trend_estimation as td


def smooth_full_series(observed, *, order: int, smoothness: float) -> np.ndarray:
    """Return an in-sample fitted trend with exactly one value per observation."""
    y = np.asarray(observed, dtype=float)
    if y.ndim != 1 or len(y) <= order or not np.all(np.isfinite(y)):
        raise ValueError("La serie debe ser un vector finito con más de d valores.")
    if not isinstance(order, (int, np.integer)) or not 1 <= order <= 4:
        raise ValueError("El orden d debe estar entre 1 y 4.")
    if not np.isfinite(smoothness) or not 0 <= smoothness <= 1:
        raise ValueError("La suavidad S debe pertenecer a [0, 1].")
    fitted = td.PurePenalizedTrend(
        order=int(order), smoothness=float(smoothness)
    ).fit(y)
    return np.asarray(fitted.trend_, dtype=float).copy()
