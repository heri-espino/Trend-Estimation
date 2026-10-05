from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal

import numpy as np

from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.core.smoothness import effective_degrees_of_freedom


ClassicalCriterion = Literal["cv", "gcv", "aicc", "bic"]


@dataclass(frozen=True)
class ClassicalSmoothnessScore:
    """One in-sample smoothing-parameter score for a fixed smoothness value."""

    criterion: ClassicalCriterion
    smoothness: float
    lambda_: float
    score: float
    rss: float
    edf: float


@dataclass(frozen=True)
class ClassicalSmoothnessSelection:
    """Best grid value under one classical in-sample selector."""

    criterion: ClassicalCriterion
    smoothness_: float
    lambda_: float
    score_: float
    rss_: float
    edf_: float
    scores_: tuple[ClassicalSmoothnessScore, ...]


def _validate_criterion(criterion: str) -> ClassicalCriterion:
    name = str(criterion).lower()
    allowed = {"cv", "gcv", "aicc", "bic"}
    if name not in allowed:
        raise ValueError(f"criterion must be one of {sorted(allowed)}; got {criterion!r}.")
    return name  # type: ignore[return-value]


def pure_smoother_score(
    y,
    *,
    order: int,
    smoothness: float,
    criterion: ClassicalCriterion,
    eps: float = 1e-12,
) -> ClassicalSmoothnessScore:
    """Evaluate CV, GCV, AICc, or BIC for the pure finite-difference smoother.

    The score definitions follow the PLS comparison used by Cortés-Toto,
    Guerrero, and Reyes (2017), up to additive or multiplicative constants that
    do not affect the minimizing smoothing parameter.

    Notes
    -----
    CV
        mean((e_i / (1 - H_ii))**2)
    GCV
        (RSS / n) / (1 - edf / n)**2
    AICc
        log(RSS / n) + (2*edf + 1) / (n - edf - 2)
    BIC
        log(RSS / n) + edf * log(n) / n

    Values whose denominators are not well-defined are assigned +infinity.
    """

    criterion = _validate_criterion(criterion)
    y = np.asarray(y, dtype=float).ravel()
    if y.size == 0:
        raise ValueError("y must not be empty.")

    n = int(y.size)
    order = int(order)
    if order < 0 or order >= n:
        raise ValueError("order must satisfy 0 <= order < len(y).")

    s = float(smoothness)
    if not 0.0 <= s <= 1.0:
        raise ValueError("smoothness must lie in [0, 1].")

    solver = cached_pure_solver(n, order)
    lambda_ = solver.lambda_from_s(s)
    fit = solver.fit_for_lambda(y, lambda_)
    residual = y - fit.trend
    rss = float(np.dot(residual, residual))
    edf = float(effective_degrees_of_freedom(lambda_, n_obs=n, order=order))

    rss_scaled = max(rss / float(n), float(eps))

    if criterion == "cv":
        denom = 1.0 - fit.diag_smoother
        if np.any(np.abs(denom) <= eps):
            score = float("inf")
        else:
            score = float(np.mean((residual / denom) ** 2))
    elif criterion == "gcv":
        denom = 1.0 - edf / float(n)
        if abs(denom) <= eps:
            score = float("inf")
        else:
            score = float(rss_scaled / (denom**2))
    elif criterion == "aicc":
        denom = float(n) - edf - 2.0
        if denom <= eps:
            score = float("inf")
        else:
            score = float(np.log(rss_scaled) + (2.0 * edf + 1.0) / denom)
    else:
        score = float(np.log(rss_scaled) + edf * np.log(float(n)) / float(n))

    return ClassicalSmoothnessScore(
        criterion=criterion,
        smoothness=s,
        lambda_=float(lambda_),
        score=score,
        rss=rss,
        edf=edf,
    )


def select_classical_pure_smoothness(
    y,
    *,
    order: int,
    criterion: ClassicalCriterion,
    smoothness_grid: Iterable[float],
) -> ClassicalSmoothnessSelection:
    """Select smoothness by a classical in-sample score over a fixed grid."""

    criterion = _validate_criterion(criterion)
    grid = np.asarray(tuple(float(v) for v in smoothness_grid), dtype=float)
    if grid.ndim != 1 or grid.size == 0:
        raise ValueError("smoothness_grid must be a non-empty one-dimensional iterable.")
    if np.any(~np.isfinite(grid)):
        raise ValueError("smoothness_grid values must be finite.")
    if np.any((grid < 0.0) | (grid > 1.0)):
        raise ValueError("smoothness_grid values must lie in [0, 1].")

    scores = tuple(
        pure_smoother_score(
            y,
            order=int(order),
            smoothness=float(s),
            criterion=criterion,
        )
        for s in grid
    )
    finite = [item for item in scores if np.isfinite(item.score)]
    if not finite:
        raise ValueError(
            f"No finite {criterion.upper()} score was available on the supplied grid."
        )

    best = min(finite, key=lambda item: item.score)
    return ClassicalSmoothnessSelection(
        criterion=criterion,
        smoothness_=best.smoothness,
        lambda_=best.lambda_,
        score_=best.score,
        rss_=best.rss,
        edf_=best.edf,
        scores_=scores,
    )
