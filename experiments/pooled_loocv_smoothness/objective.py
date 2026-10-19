"""Exact-endpoint pooled leave-one-out criterion for discrete PLS smoothing.

The implementation uses the spectral identity
    T(lambda) = Q (I + lambda Q)^(-1)
and evaluates the LOOCV residual as (T y)[i] / T[i, i].
The cancellation makes the lambda=0 endpoint well-defined.

Only same-length, same-order observed series may be pooled. No forecast
targets or extrapolation are used.
"""

from __future__ import annotations

from math import comb
from functools import lru_cache

import numpy as np


def difference_matrix(n: int, order: int) -> np.ndarray:
    """Return the ordinary forward-difference matrix of integer order."""
    if not isinstance(n, int) or not isinstance(order, int):
        raise TypeError("n and order must be integers")
    if order < 1 or n <= order:
        raise ValueError("require 1 <= order < n")
    d = np.zeros((n - order, n), dtype=float)
    for i in range(n - order):
        for j in range(order + 1):
            d[i, i + j] = (-1) ** (order - j) * comb(order, j)
    return d


@lru_cache(maxsize=24)
def cached_difference_contrast_basis(n: int, order: int):
    """Cache the eigenbasis of D D.T; use SVD for near-singular order four."""
    d = difference_matrix(n, order)
    if order >= 4:
        u, singular, _ = np.linalg.svd(d, full_matrices=False)
        return singular * singular, u
    return np.linalg.eigh(d @ d.T)


@lru_cache(maxsize=24)
def _cached_penalty_spectrum(n: int, order: int):
    """Shared, read-only-by-convention spectrum for the same N and order.

    Reusing the basis avoids millions of repeated decompositions in
    large manual Monte Carlo campaigns. For order four, square singular
    values of D rather than diagonalizing the ill-conditioned D.T@D.
    """
    d = difference_matrix(n, order)
    if order >= 4:
        _, singular, vh = np.linalg.svd(d, full_matrices=True)
        return singular * singular, vh[:n-order].T, vh[n-order:].T
    q = d.T @ d
    eigval, eigvec = np.linalg.eigh(q)
    tol = 100 * np.finfo(float).eps * n * max(1., float(np.max(eigval)))
    positive = eigval > tol
    if int(np.count_nonzero(positive)) != n-order:
        raise ArithmeticError("positive spectrum rank check failed")
    return eigval[positive], eigvec[:, positive], eigvec[:, ~positive]


class PooledLOOCV:
    """Pooled ordinary LOOCV over R equally sized time series.

    Rows represent series and columns represent ordered observations.
    The same n and d imply a common smoother and normalized smoothness
    coordinate for all series in one pool.

    The underlying statistical assumption V=I, mu=0 belongs to the
    smoothing *criterion*; the observed data need not be independent.
    """

    def __init__(self, series: np.ndarray, order: int = 2) -> None:
        y = np.asarray(series, dtype=float)
        if y.ndim == 1:
            y = y[np.newaxis, :]
        if y.ndim != 2 or y.shape[0] < 1 or y.shape[1] <= order + 1:
            raise ValueError("series must have shape (R, N) with N >= order + 2")
        if not np.all(np.isfinite(y)):
            raise ValueError("all observations must be finite")
        self.y = y.copy()
        self.r, self.n = y.shape
        self.order = order
        self.d = difference_matrix(self.n, order)
        self.q = self.d.T @ self.d
        self.eigenvalues, self.u_positive, self.u_null = (
            _cached_penalty_spectrum(self.n, order))
        self.uty = self.u_positive.T @ self.y.T
        self.u2 = self.u_positive ** 2
        self.calls_score = 0
        self.calls_derivative = 0

    def reset_counts(self) -> None:
        """Reset evaluation counts for an individual optimization method."""
        self.calls_score = 0
        self.calls_derivative = 0

    def smoothness(self, lam: float) -> float:
        """Normalized [0,1] smoothness, including exact limiting endpoints."""
        if lam < 0 or np.isnan(lam):
            raise ValueError("lambda must be nonnegative")
        if np.isinf(lam):
            return 1.0
        x = lam * self.eigenvalues
        return float(np.mean(x / (1.0 + x)))

    def _residual(self, lam: float, deriv: bool = False):
        if lam < 0 or np.isnan(lam):
            raise ValueError("lambda must be nonnegative")
        if np.isinf(lam):
            if deriv:
                raise ValueError("derivative at infinite lambda is not defined")
            # I - P_null is the exact limiting residual maker.
            a = self.u_positive @ self.uty
            b = np.sum(self.u2, axis=1)
            return a / b[:, np.newaxis]
        weights = self.eigenvalues / (1.0 + lam * self.eigenvalues)
        a = self.u_positive @ (weights[:, np.newaxis] * self.uty)
        b = self.u2 @ weights
        e = a / b[:, np.newaxis]
        if not deriv:
            return e
        weights2 = weights * weights
        da = -(self.u_positive @ (weights2[:, np.newaxis] * self.uty))
        db = -(self.u2 @ weights2)
        de = (da - e * db[:, np.newaxis]) / b[:, np.newaxis]
        return e, de

    def score(self, lam: float) -> float:
        """Mean of R separate LOOCV MSEs; exact at lambda=0 and infinity."""
        self.calls_score += 1
        e = self._residual(float(lam))
        return float(np.mean(e ** 2))

    def derivative(self, lam: float) -> float:
        """Analytical d(pooled LOOCV)/d lambda at finite lambda >= 0."""
        self.calls_derivative += 1
        e, de = self._residual(float(lam), deriv=True)
        return float(2.0 * np.mean(e * de))

    def trend(self, lam: float) -> np.ndarray:
        """Return the fitted PLS trend for every series at lambda."""
        if lam < 0 or np.isnan(lam):
            raise ValueError("lambda must be nonnegative")
        null_part = self.u_null @ (self.u_null.T @ self.y.T)
        if np.isinf(lam):
            return null_part.T
        filt = (1.0 / (1.0 + lam * self.eigenvalues))[:, None] * self.uty
        return (null_part + self.u_positive @ filt).T
