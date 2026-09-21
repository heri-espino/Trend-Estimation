from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
from scipy.optimize import brentq, minimize_scalar


@dataclass
class LambdaOptimizationResult:
    lambda_: float
    theta_: float
    objective_: float
    converged_: bool
    n_iter_: int


@dataclass(frozen=True)
class StationaryPoint:
    """One stationary point found in log-lambda space."""

    lambda_: float
    theta_: float
    objective_: float
    gradient_lambda_: float
    curvature_theta_: float
    kind_: str


@dataclass
class StationaryPointSearchResult:
    """Result of bracketed stationary-point search on a bounded log domain."""

    points_: list[StationaryPoint]
    best_lambda_: float
    best_theta_: float
    best_objective_: float
    best_source_: str
    n_brackets_: int
    log_bounds_: tuple[float, float]


def minimize_over_log_lambda(
    objective: Callable[[float], float],
    *,
    log_bounds: tuple[float, float] = (-12.0, 20.0),
    xatol: float = 1e-8,
) -> LambdaOptimizationResult:
    """Minimize a scalar objective over positive lambda using theta=log(lambda).

    This direct bounded minimizer is a benchmark. It is not a guarantee of the
    global optimum for a multimodal objective.
    """

    lo, hi = map(float, log_bounds)
    if not lo < hi:
        raise ValueError("log_bounds must satisfy lower < upper.")

    def objective_theta(theta: float) -> float:
        return float(objective(float(np.exp(theta))))

    result = minimize_scalar(
        objective_theta,
        bounds=(lo, hi),
        method="bounded",
        options={"xatol": float(xatol)},
    )
    theta = float(result.x)
    return LambdaOptimizationResult(
        lambda_=float(np.exp(theta)),
        theta_=theta,
        objective_=float(result.fun),
        converged_=bool(result.success),
        n_iter_=int(getattr(result, "nit", 0)),
    )


def newton_stationary_log_lambda(
    value_grad_hess: Callable[[float], tuple[float, float, float]],
    initial_lambda: float,
    *,
    log_bounds: tuple[float, float] = (-12.0, 20.0),
    tol: float = 1e-10,
    max_iter: int = 50,
) -> LambdaOptimizationResult:
    r"""Find one stationary point with Newton iterations in log-lambda space.

    value_grad_hess(lambda) returns (f, f', f'') with derivatives with respect
    to lambda. If g(theta)=f(exp(theta)), then
    g' = lambda f' and g'' = lambda f' + lambda^2 f''.

    Newton is local and therefore depends on initialization.
    """

    initial_lambda = float(initial_lambda)
    if initial_lambda <= 0:
        raise ValueError("initial_lambda must be positive.")
    lo, hi = map(float, log_bounds)
    if not lo < hi:
        raise ValueError("log_bounds must satisfy lower < upper.")

    theta = float(np.clip(np.log(initial_lambda), lo, hi))
    converged = False
    value = np.nan
    iteration = 0

    for iteration in range(1, int(max_iter) + 1):
        lambda_ = float(np.exp(theta))
        value, grad, hess = map(float, value_grad_hess(lambda_))
        g1 = lambda_ * grad
        g2 = lambda_ * grad + lambda_ * lambda_ * hess
        if abs(g1) <= tol:
            converged = True
            break
        if not np.isfinite(g2) or abs(g2) <= np.finfo(float).eps:
            break
        step = g1 / g2
        candidate = float(np.clip(theta - step, lo, hi))
        if abs(candidate - theta) <= tol:
            theta = candidate
            converged = True
            break
        theta = candidate

    lambda_ = float(np.exp(theta))
    value = float(value_grad_hess(lambda_)[0])
    return LambdaOptimizationResult(
        lambda_=lambda_,
        theta_=theta,
        objective_=value,
        converged_=converged,
        n_iter_=iteration,
    )


def find_stationary_points_log_lambda(
    value_grad_hess: Callable[[float], tuple[float, float, float]],
    *,
    log_bounds: tuple[float, float] = (-12.0, 20.0),
    n_grid: int = 257,
    derivative_tol: float = 1e-10,
    curvature_tol: float = 1e-9,
    root_xtol: float = 1e-12,
) -> StationaryPointSearchResult:
    r"""Find bracketed stationary points of a one-dimensional lambda objective.

    The callback returns (f, f', f'') with derivatives with respect to lambda.
    The search works with theta = log(lambda), where
    g'(theta) = lambda f'(lambda).

    A coarse theta grid discovers sign-change brackets plus near-zero grid
    points. Brent's root method then solves each bracket.

    A finite discovery grid cannot guarantee finding every stationary point of
    an arbitrary smooth function. It may miss two roots in one interval or a
    tangential root that does not change sign.
    """

    lo, hi = map(float, log_bounds)
    if not lo < hi:
        raise ValueError("log_bounds must satisfy lower < upper.")
    n_grid = int(n_grid)
    if n_grid < 3:
        raise ValueError("n_grid must be at least 3.")

    def value_grad_hess_theta(theta: float) -> tuple[float, float, float, float]:
        lambda_ = float(np.exp(theta))
        value, grad, hess = map(float, value_grad_hess(lambda_))
        g1 = lambda_ * grad
        g2 = lambda_ * grad + lambda_ * lambda_ * hess
        return value, grad, g1, g2

    def gprime(theta: float) -> float:
        return value_grad_hess_theta(float(theta))[2]

    theta_grid = np.linspace(lo, hi, n_grid)
    derivative_grid = np.array([gprime(theta) for theta in theta_grid], dtype=float)

    roots: list[float] = []
    brackets: list[tuple[float, float]] = []

    for theta, derivative in zip(theta_grid, derivative_grid):
        if np.isfinite(derivative) and abs(derivative) <= derivative_tol:
            roots.append(float(theta))

    for i in range(n_grid - 1):
        a = float(theta_grid[i])
        b = float(theta_grid[i + 1])
        fa = float(derivative_grid[i])
        fb = float(derivative_grid[i + 1])
        if not (np.isfinite(fa) and np.isfinite(fb)):
            continue
        if fa * fb < 0.0:
            brackets.append((a, b))
            roots.append(float(brentq(gprime, a, b, xtol=float(root_xtol))))

    roots.sort()
    deduped: list[float] = []
    merge_tol = max(10.0 * float(root_xtol), 1e-10)
    for theta in roots:
        if not deduped or abs(theta - deduped[-1]) > merge_tol:
            deduped.append(theta)

    points: list[StationaryPoint] = []
    for theta in deduped:
        lambda_ = float(np.exp(theta))
        value, grad, _, g2 = value_grad_hess_theta(theta)
        if g2 > curvature_tol:
            kind = "minimum"
        elif g2 < -curvature_tol:
            kind = "maximum"
        else:
            kind = "flat"
        points.append(
            StationaryPoint(
                lambda_=lambda_,
                theta_=theta,
                objective_=value,
                gradient_lambda_=grad,
                curvature_theta_=g2,
                kind_=kind,
            )
        )

    candidates = []
    for theta, label in ((lo, "lower_boundary"), (hi, "upper_boundary")):
        lambda_ = float(np.exp(theta))
        value = float(value_grad_hess(lambda_)[0])
        candidates.append((value, lambda_, theta, label))

    candidates.extend(
        (
            point.objective_,
            point.lambda_,
            point.theta_,
            "stationary_" + point.kind_,
        )
        for point in points
    )
    best_value, best_lambda, best_theta, best_source = min(
        candidates,
        key=lambda item: item[0],
    )

    return StationaryPointSearchResult(
        points_=points,
        best_lambda_=float(best_lambda),
        best_theta_=float(best_theta),
        best_objective_=float(best_value),
        best_source_=best_source,
        n_brackets_=len(brackets),
        log_bounds_=(lo, hi),
    )
