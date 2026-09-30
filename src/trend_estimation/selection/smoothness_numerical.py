from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np
from scipy.optimize import brentq

from trend_estimation.core.smoothness import (
    smoothness_derivatives,
    smoothness_to_lambda,
)


DEFAULT_SPACING_EPSILONS = (0.0, 0.02, 0.05, 0.10, 0.15)


@dataclass(frozen=True)
class SmoothnessStationaryPoint:
    """One stationary point of a forecast objective expressed in smoothness."""

    smoothness_: float
    lambda_: float
    objective_: float
    gradient_smoothness_: float
    curvature_smoothness_: float
    gradient_lambda_: float
    curvature_lambda_: float
    kind_: str


@dataclass(frozen=True)
class SmoothnessStationaryPointSearchResult:
    """Adaptive stationary-point search result on the smoothness domain."""

    points_: tuple[SmoothnessStationaryPoint, ...]
    n_evaluations_: int
    n_brackets_: int
    sampled_smoothness_: tuple[float, ...]
    search_interval_: tuple[float, float]


@dataclass(frozen=True)
class SmoothnessCandidateSet:
    """Separated local-minimum candidates for one spacing radius epsilon."""

    epsilon_: float
    max_candidates_: int
    candidates_: tuple[SmoothnessStationaryPoint, ...]
    n_available_minima_: int
    n_removed_: int


@dataclass(frozen=True)
class _SmoothnessEvaluation:
    smoothness: float
    lambda_: float
    value: float
    gradient_lambda: float
    curvature_lambda: float
    gradient_smoothness: float
    curvature_smoothness: float


def find_stationary_points_smoothness(
    value_grad_hess: Callable[[float], tuple[float, float, float]],
    *,
    n_obs: int,
    order: int,
    initial_grid_size: int = 9,
    max_depth: int = 8,
    min_interval: float = 1e-3,
    derivative_tol: float = 1e-8,
    curvature_tol: float = 1e-8,
    near_zero_ratio: float = 0.2,
    root_xtol: float = 1e-10,
    boundary_margin: float = 1e-6,
) -> SmoothnessStationaryPointSearchResult:
    """Adaptively locate stationary points directly on normalized smoothness.

    The callback returns objective value and first/second derivatives with
    respect to lambda. Internally each sampled smoothness value is mapped to
    lambda, while the chain rule supplies derivatives with respect to
    smoothness.

    The procedure is intentionally not a dense grid search. It begins from a
    small deterministic partition and recursively samples only intervals whose
    derivative or curvature suggests unresolved stationary structure.

    No finite sampler can certify discovery of every root of an arbitrary
    smooth objective. Dense-grid comparisons remain a required diagnostic.
    """

    n_obs = int(n_obs)
    order = int(order)
    initial_grid_size = int(initial_grid_size)
    max_depth = int(max_depth)
    min_interval = float(min_interval)
    derivative_tol = float(derivative_tol)
    curvature_tol = float(curvature_tol)
    near_zero_ratio = float(near_zero_ratio)
    root_xtol = float(root_xtol)
    boundary_margin = float(boundary_margin)

    if n_obs <= 0:
        raise ValueError("n_obs must be positive.")
    if order < 0 or order >= n_obs:
        raise ValueError("order must satisfy 0 <= order < n_obs.")
    if initial_grid_size < 3:
        raise ValueError("initial_grid_size must be at least 3.")
    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative.")
    if min_interval <= 0.0:
        raise ValueError("min_interval must be positive.")
    if derivative_tol <= 0.0 or curvature_tol <= 0.0 or root_xtol <= 0.0:
        raise ValueError("tolerances must be positive.")
    if not 0.0 < near_zero_ratio < 1.0:
        raise ValueError("near_zero_ratio must lie strictly between 0 and 1.")
    if not 0.0 < boundary_margin < 0.5:
        raise ValueError("boundary_margin must lie strictly between 0 and 0.5.")

    search_lo = 0.0
    search_hi = 1.0 - boundary_margin
    cache: dict[float, _SmoothnessEvaluation] = {}

    def evaluate_smoothness(smoothness: float) -> _SmoothnessEvaluation:
        smoothness = float(smoothness)
        if smoothness < search_lo or smoothness > search_hi:
            raise ValueError("smoothness lies outside the interior search domain.")
        cached = cache.get(smoothness)
        if cached is not None:
            return cached

        lambda_ = smoothness_to_lambda(
            smoothness,
            n_obs=n_obs,
            order=order,
        )
        value, gradient_lambda, curvature_lambda = map(
            float,
            value_grad_hess(lambda_),
        )
        first_s, second_s = smoothness_derivatives(
            lambda_,
            n_obs=n_obs,
            order=order,
        )
        if not np.isfinite(first_s) or first_s <= 0.0:
            raise FloatingPointError(
                "Smoothness derivative must be positive on the interior domain."
            )

        gradient_smoothness = gradient_lambda / first_s
        curvature_smoothness = (
            curvature_lambda / (first_s * first_s)
            - gradient_lambda * second_s / (first_s**3)
        )
        result = _SmoothnessEvaluation(
            smoothness=smoothness,
            lambda_=lambda_,
            value=value,
            gradient_lambda=gradient_lambda,
            curvature_lambda=curvature_lambda,
            gradient_smoothness=float(gradient_smoothness),
            curvature_smoothness=float(curvature_smoothness),
        )
        cache[smoothness] = result
        return result

    initial = np.linspace(search_lo, search_hi, initial_grid_size)
    for smoothness in initial:
        evaluate_smoothness(float(smoothness))

    stack = [
        (float(initial[i]), float(initial[i + 1]), 0)
        for i in range(initial_grid_size - 1)
    ]

    while stack:
        a, b, depth = stack.pop()
        left = evaluate_smoothness(a)
        right = evaluate_smoothness(b)
        mid_s = 0.5 * (a + b)
        middle = evaluate_smoothness(mid_s)

        ga = left.gradient_smoothness
        gm = middle.gradient_smoothness
        gb = right.gradient_smoothness
        ha = left.curvature_smoothness
        hm = middle.curvature_smoothness
        hb = right.curvature_smoothness

        turning_gradient = (gm - ga) * (gb - gm) < 0.0
        curvature_change = (
            min(ha, hm, hb) < -curvature_tol
            and max(ha, hm, hb) > curvature_tol
        )
        edge_scale = max(abs(ga), abs(gb), derivative_tol)
        center_near_zero = abs(gm) <= max(
            derivative_tol,
            near_zero_ratio * edge_scale,
        )
        same_endpoint_sign = np.signbit(ga) == np.signbit(gb)
        split_sign_change = (ga * gm < 0.0) or (gm * gb < 0.0)
        unresolved_pair = same_endpoint_sign and split_sign_change

        refine = (
            turning_gradient
            or curvature_change
            or center_near_zero
            or unresolved_pair
        )
        if refine and depth < max_depth and (b - a) > min_interval:
            stack.append((a, mid_s, depth + 1))
            stack.append((mid_s, b, depth + 1))

    sampled = sorted(cache)
    roots: list[float] = []
    brackets: list[tuple[float, float]] = []

    for smoothness in sampled:
        gradient = cache[smoothness].gradient_smoothness
        if np.isfinite(gradient) and abs(gradient) <= derivative_tol:
            roots.append(float(smoothness))

    def root_function(smoothness: float) -> float:
        return evaluate_smoothness(float(smoothness)).gradient_smoothness

    for a, b in zip(sampled[:-1], sampled[1:]):
        ga = cache[a].gradient_smoothness
        gb = cache[b].gradient_smoothness
        if not (np.isfinite(ga) and np.isfinite(gb)):
            continue
        if ga * gb < 0.0:
            brackets.append((float(a), float(b)))
            roots.append(
                float(
                    brentq(
                        root_function,
                        float(a),
                        float(b),
                        xtol=root_xtol,
                    )
                )
            )

    roots.sort()
    deduped: list[float] = []
    merge_tol = max(10.0 * root_xtol, 1e-8)
    for smoothness in roots:
        if not deduped or abs(smoothness - deduped[-1]) > merge_tol:
            deduped.append(smoothness)

    points: list[SmoothnessStationaryPoint] = []
    for smoothness in deduped:
        evaluated = evaluate_smoothness(smoothness)
        curvature = evaluated.curvature_smoothness
        if curvature > curvature_tol:
            kind = "minimum"
        elif curvature < -curvature_tol:
            kind = "maximum"
        else:
            kind = "flat"
        points.append(
            SmoothnessStationaryPoint(
                smoothness_=evaluated.smoothness,
                lambda_=evaluated.lambda_,
                objective_=evaluated.value,
                gradient_smoothness_=evaluated.gradient_smoothness,
                curvature_smoothness_=curvature,
                gradient_lambda_=evaluated.gradient_lambda,
                curvature_lambda_=evaluated.curvature_lambda,
                kind_=kind,
            )
        )

    points.sort(key=lambda point: point.smoothness_)
    return SmoothnessStationaryPointSearchResult(
        points_=tuple(points),
        n_evaluations_=len(cache),
        n_brackets_=len(brackets),
        sampled_smoothness_=tuple(sorted(cache)),
        search_interval_=(search_lo, search_hi),
    )


def select_spaced_smoothness_minima(
    points: Iterable[SmoothnessStationaryPoint],
    *,
    epsilon: float = 0.10,
    max_candidates: int = 5,
) -> SmoothnessCandidateSet:
    """Keep the best separated local minima under an epsilon-radius rule.

    Candidates are ranked by objective value. After accepting one minimum at
    smoothness s, every remaining minimum inside [s-epsilon, s+epsilon] is
    suppressed. Thus epsilon=0.10 corresponds to a neighborhood of total width
    0.20 around each accepted candidate.
    """

    epsilon = float(epsilon)
    max_candidates = int(max_candidates)
    if epsilon < 0.0 or epsilon > 1.0:
        raise ValueError("epsilon must lie in [0, 1].")
    if max_candidates <= 0:
        raise ValueError("max_candidates must be positive.")

    minima = sorted(
        (point for point in points if point.kind_ == "minimum"),
        key=lambda point: (point.objective_, point.smoothness_),
    )
    selected: list[SmoothnessStationaryPoint] = []

    for point in minima:
        if all(
            abs(point.smoothness_ - chosen.smoothness_) > epsilon
            for chosen in selected
        ):
            selected.append(point)
            if len(selected) >= max_candidates:
                break

    return SmoothnessCandidateSet(
        epsilon_=epsilon,
        max_candidates_=max_candidates,
        candidates_=tuple(selected),
        n_available_minima_=len(minima),
        n_removed_=len(minima) - len(selected),
    )


def sweep_spaced_smoothness_minima(
    points: Iterable[SmoothnessStationaryPoint],
    *,
    epsilons: Iterable[float] = DEFAULT_SPACING_EPSILONS,
    max_candidates: int = 5,
) -> tuple[SmoothnessCandidateSet, ...]:
    """Apply the separated-minimum rule over several epsilon radii."""

    point_tuple = tuple(points)
    epsilon_values = tuple(float(value) for value in epsilons)
    if not epsilon_values:
        raise ValueError("epsilons must not be empty.")
    return tuple(
        select_spaced_smoothness_minima(
            point_tuple,
            epsilon=epsilon,
            max_candidates=max_candidates,
        )
        for epsilon in epsilon_values
    )
