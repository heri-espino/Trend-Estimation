"""Feasible variance-component estimators for Guerrero's stochastic-trend model.

Observed z = D_d y, Cov(z) = sigma_eps^2 I + sigma_eta^2 D_d D_d.T.
Both estimators use only y and known D_d. The Gaussian estimator
maximizes the *marginal likelihood of the differenced observations*,
not the complete likelihood of y conditional on known initial trend.
No simulated latent tau is used at selection.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize_scalar, nnls
from .objective import cached_difference_contrast_basis, difference_matrix


@dataclass(frozen=True)
class VarianceEstimate:
    estimator: str
    sigma_eta2: float
    sigma_epsilon2: float
    lambda_ratio: float
    negative_unconstrained_moments: bool = False

    def as_dict(self) -> dict:
        return {
            "estimator": self.estimator,
            "sigma_eta2": self.sigma_eta2,
            "sigma_epsilon2": self.sigma_epsilon2,
            "lambda_ratio": self.lambda_ratio,
            "negative_unconstrained_moments": self.negative_unconstrained_moments,
        }


def _prepare(series: np.ndarray, d: np.ndarray):
    y = np.asarray(series, dtype=float)
    d = np.asarray(d, dtype=float)
    if y.ndim == 1:
        y = y[np.newaxis, :]
    if d.ndim != 2 or y.ndim != 2 or not y.shape[0] or y.shape[1] != d.shape[1]:
        raise ValueError("series must be R x N and d must be (N-order) x N")
    if not np.isfinite(y).all():
        raise ValueError("series contains nonfinite observations")
    z = y @ d.T
    a = d @ d.T
    eigvals, basis = (cached_difference_contrast_basis(y.shape[1], y.shape[1]-d.shape[0])
                      if np.array_equal(d, difference_matrix(y.shape[1], y.shape[1]-d.shape[0]))
                      else np.linalg.eigh(a))
    if np.any(eigvals <= 0):
        raise ArithmeticError("difference covariance matrix must be positive definite")
    eigenpower = np.mean((z @ basis) ** 2, axis=0)
    return z, eigvals, eigenpower


def _pack(name: str, sigma_epsilon2: float, sigma_eta2: float,
          negative_moments: bool = False) -> VarianceEstimate:
    a = float(sigma_epsilon2)
    b = float(sigma_eta2)
    if not np.isfinite(a + b) or a < 0 or b < 0 or a + b <= 0:
        raise ArithmeticError("invalid estimated variance components")
    ratio = b / a if a > 0 else float("inf")
    return VarianceEstimate(name, b, a, ratio, negative_moments)


def estimate_moments(series: np.ndarray, d: np.ndarray) -> VarianceEstimate:
    """Fit two trace moments, with nonnegative least squares if unconstrained
    moment estimates are negative. Nonnegativity may put one variance at
    zero and yield lambda=+infinity; do NOT silently regularize it.
    """
    z, eigvals, eigenpower = _prepare(series, d)
    mu = float(np.mean(eigvals))
    nu = float(np.mean(eigvals ** 2))
    observed = np.array([np.mean(z * z), np.mean(eigenpower * eigvals)])
    design = np.array([[1., mu], [mu, nu]])
    estimate = np.linalg.solve(design, observed)
    negative = bool(np.any(estimate < 0))
    if negative:
        row_scale = np.array([1., max(mu, 1.)])
        estimate, _ = nnls(design / row_scale[:, None], observed / row_scale)
    return _pack("moments_nnls", float(estimate[0]), float(estimate[1]), negative)


def estimate_gaussian_differences(series: np.ndarray, d: np.ndarray,
                                  scan_points: int = 81) -> VarianceEstimate:
    """Gaussian covariance likelihood on z=D y with scale analytically profiled.

    Write Var(z)=v[(1-p)I+(p/mean_eig(A)) A], p in [0,1], A=D D.T.
    For each p, vhat=mean_j(eigenpower_j / g_j(p)).
    The negative Gaussian likelihood (per component, up to constants)
    is 0.5*[log(vhat)+mean_j log(g_j(p))+1].
    A finite initial scan followed by bounded refinement handles multiple
    candidates, but does NOT constitute exact global optimization.
    """
    if scan_points < 5:
        raise ValueError("scan_points must be at least 5")
    _, eigvals, eigenpower = _prepare(series, d)
    eig_scaled = eigvals / float(np.mean(eigvals))

    def objective(p: float) -> float:
        g = (1.0 - p) + p * eig_scaled
        v = float(np.mean(eigenpower / g))
        if v <= 0.0:
            return float("inf")
        return .5 * (float(np.log(v)) + float(np.mean(np.log(g))) + 1.)

    grid = np.linspace(0., 1., scan_points)
    values = [objective(float(p)) for p in grid]
    candidates = [(values[0], 0.), (values[-1], 1.)]
    for i in range(1, len(grid) - 1):
        if values[i] <= values[i-1] and values[i] <= values[i+1]:
            result = minimize_scalar(
                objective,
                bounds=(float(grid[i-1]), float(grid[i+1])),
                method="bounded",
                options={"xatol": 1e-12},
            )
            if result.success:
                candidates.append((float(result.fun), float(result.x)))
    _, best_p = min(candidates)
    g = (1. - best_p) + best_p * eig_scaled
    v = float(np.mean(eigenpower / g))
    return _pack(
        "gaussian_difference_ml",
        v * (1. - best_p),
        v * best_p / float(np.mean(eigvals)),
    )
