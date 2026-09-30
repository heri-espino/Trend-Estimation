from __future__ import annotations

from functools import lru_cache

import numpy as np

from .difference import difference_matrix


@lru_cache(maxsize=256)
def _cached_penalty_eigenvalues(n_obs: int, order: int) -> np.ndarray:
    D = difference_matrix(int(n_obs), int(order))
    eigvals = np.linalg.eigvalsh(D.T @ D)
    eigvals.setflags(write=False)
    return eigvals


def penalty_eigenvalues(n_obs: int, order: int) -> np.ndarray:
    """Eigenvalues of D.T @ D for the finite-difference penalty.

    The eigendecomposition is cached by sample length and difference order.
    A copy is returned so callers can safely mutate the public result.
    """
    return _cached_penalty_eigenvalues(int(n_obs), int(order)).copy()


def effective_degrees_of_freedom(lambda_: float, n_obs: int, order: int) -> float:
    """Return trace((I + lambda D.T D)^-1)."""
    eigvals = _cached_penalty_eigenvalues(int(n_obs), int(order))
    return float(np.sum(1.0 / (1.0 + float(lambda_) * eigvals)))


def lambda_to_smoothness(lambda_: float, n_obs: int, order: int) -> float:
    """Map a penalty parameter to Guerrero's normalized smoothness index."""
    lambda_ = float(lambda_)
    if lambda_ < 0:
        raise ValueError("lambda_ must be nonnegative.")
    if order == 0:
        return lambda_ / (1.0 + lambda_)
    tr = effective_degrees_of_freedom(lambda_, n_obs, order)
    s_raw = 1.0 - tr / n_obs
    s_max = 1.0 - order / n_obs
    return float(s_raw / s_max) if s_max > 0 else 0.0


def smoothness_derivatives(
    lambda_: float,
    n_obs: int,
    order: int,
) -> tuple[float, float]:
    """Return first and second lambda derivatives of normalized smoothness."""
    lambda_ = float(lambda_)
    n_obs = int(n_obs)
    order = int(order)
    if lambda_ < 0.0:
        raise ValueError("lambda_ must be nonnegative.")
    if n_obs <= 0:
        raise ValueError("n_obs must be positive.")
    if order < 0 or order >= n_obs:
        raise ValueError("order must satisfy 0 <= order < n_obs.")

    if order == 0:
        denom = 1.0 + lambda_
        return float(denom**-2), float(-2.0 * denom**-3)

    eigvals = np.clip(_cached_penalty_eigenvalues(n_obs, order), 0.0, None)
    denom = 1.0 + lambda_ * eigvals
    normalizer = float(n_obs - order)
    first = float(np.sum(eigvals / denom**2) / normalizer)
    second = float(-2.0 * np.sum(eigvals**2 / denom**3) / normalizer)
    return first, second


def smoothness_to_lambda(
    smoothness: float,
    n_obs: int,
    order: int,
    *,
    tol: float = 1e-11,
    max_iter: int = 100,
) -> float:
    """Map smoothness in [0, 1) to the penalty parameter using bisection."""
    smoothness = float(smoothness)
    if smoothness <= 0:
        return 0.0
    if smoothness >= 1.0:
        smoothness = 0.999999
    if order == 0:
        return smoothness / (1.0 - smoothness)

    eigvals = _cached_penalty_eigenvalues(int(n_obs), int(order))
    s_max = 1.0 - order / n_obs
    target = smoothness * s_max

    def s_raw(lmb: float) -> float:
        return 1.0 - float(np.sum(1.0 / (1.0 + lmb * eigvals))) / n_obs

    lo, hi = 0.0, 1.0
    while s_raw(hi) < target and hi < 1e16:
        hi *= 10.0
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        val = s_raw(mid)
        if abs(val - target) < tol:
            return float(mid)
        if val < target:
            lo = mid
        else:
            hi = mid
    return float(0.5 * (lo + hi))
