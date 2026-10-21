"""Classical in-sample CV, GCV, AICc and BIC (Cortes-Toto et al., 2017)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np

from .core import TrendSmoother

Criterion = Literal["cv", "gcv", "aicc", "bic"]


@dataclass(frozen=True)
class SelectionResult:
    criterion: str
    lambda_: float
    smoothness: float
    score: float
    grid: np.ndarray
    scores: np.ndarray


def score_lambda(
    smoother: TrendSmoother, y, *, lambda_: float,
    criterion: Criterion = "gcv", mu: float = 0.0,
) -> float:
    """Classical published scores for FIXED mu, including mu=0.

    For a data-estimated mu the full leave-one-out refit is a different
    operation, so this API deliberately rejects mu='data'.
    """
    name = str(criterion).lower()
    if name not in {"cv", "gcv", "aicc", "bic"}:
        raise ValueError("criterion must be cv, gcv, aicc, or bic.")
    if isinstance(mu, str):
        raise ValueError("Criteria require fixed numeric mu.")
    _, _, _, coord = smoother._prepare(y, float(mu))
    alpha = smoother._attenuation(lambda_)
    edf = float(np.sum(alpha))
    residual_coordinates = (1.0 - alpha) * coord
    rss = float(residual_coordinates @ residual_coordinates)
    n = smoother.n
    eps = np.finfo(float).eps * max(1.0, float(coord @ coord))

    if name == "cv":
        residual = smoother.eigenvectors @ residual_coordinates
        leverage = smoother._basis_squares @ alpha
        denom = 1.0 - leverage
        if np.any(denom <= 1e-10):
            return float("inf")
        return float(np.mean((residual / denom) ** 2))
    if name == "gcv":
        denom = 1.0 - edf / n
        return float((rss / n) / denom**2) if denom > 1e-10 else float("inf")
    if rss <= eps:
        return float("inf")
    log_mean_rss = np.log(rss / n)
    if name == "bic":
        return float(log_mean_rss + edf * np.log(n) / n)
    denom = n - edf - 2.0
    return float(log_mean_rss + (2.0 * edf + 1.0) / denom) if denom > 0 else float("inf")


def select_lambda(
    smoother: TrendSmoother, y, *, criterion: Criterion = "gcv",
    mu: float = 0.0, grid=None,
) -> SelectionResult:
    """Choose lambda from a declared grid; NOT future-forecast TSCV.

    By default use 121 logarithmic values centered at inverse median
    positive penalty eigenvalue, plus the infinite-penalty endpoint.
    """
    if isinstance(mu, str):
        raise ValueError("select_lambda requires fixed numeric mu.")
    if grid is None:
        scale = 1.0 / smoother._median_positive_eigenvalue
        grid = np.r_[scale * np.geomspace(1e-6, 1e6, 121), np.inf]
    grid = np.asarray(grid, dtype=float)
    if grid.ndim != 1 or grid.size == 0 or np.any(np.isnan(grid)) or np.any(grid < 0):
        raise ValueError("grid must contain nonnegative lambda values.")
    scores = np.asarray([
        score_lambda(smoother, y, lambda_=lam, criterion=criterion, mu=mu)
        for lam in grid
    ])
    valid = np.isfinite(scores)
    if not np.any(valid):
        raise ValueError("No finite criterion score on the grid.")
    best = int(np.argmin(np.where(valid, scores, np.inf)))
    return SelectionResult(
        criterion=str(criterion).lower(),
        lambda_=float(grid[best]),
        smoothness=smoother.smoothness(grid[best]),
        score=float(scores[best]),
        grid=grid,
        scores=scores,
    )
