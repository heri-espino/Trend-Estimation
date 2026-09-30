from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

from trend_estimation.core.smoothness import (
    lambda_to_smoothness,
    smoothness_derivatives,
)


@dataclass(frozen=True)
class AdversarialSmoothnessCase:
    """Analytic smoothness-space objective with known stationary structure."""

    name: str
    description: str
    coefficients: tuple[float, ...]
    true_minima: tuple[float, ...] = ()
    true_flat_minima: tuple[float, ...] = ()
    true_boundary_minima: tuple[float, ...] = ()
    true_other_stationary: tuple[float, ...] = ()

    def value(self, smoothness: float) -> float:
        return float(np.polyval(self.coefficients, float(smoothness)))

    def first(self, smoothness: float) -> float:
        return float(
            np.polyval(np.polyder(np.asarray(self.coefficients), 1), float(smoothness))
        )

    def second(self, smoothness: float) -> float:
        return float(
            np.polyval(np.polyder(np.asarray(self.coefficients), 2), float(smoothness))
        )

    def lambda_callback(
        self,
        *,
        n_obs: int,
        order: int,
    ) -> Callable[[float], tuple[float, float, float]]:
        """Return value/gradient/Hessian with respect to lambda."""

        def callback(lambda_: float) -> tuple[float, float, float]:
            smoothness = lambda_to_smoothness(lambda_, n_obs, order)
            value = self.value(smoothness)
            gradient_s = self.first(smoothness)
            curvature_s = self.second(smoothness)
            ds, d2s = smoothness_derivatives(lambda_, n_obs, order)
            gradient_lambda = gradient_s * ds
            curvature_lambda = curvature_s * ds * ds + gradient_s * d2s
            return (
                float(value),
                float(gradient_lambda),
                float(curvature_lambda),
            )

        return callback

    def truth_points(self) -> tuple[tuple[float, str], ...]:
        rows: list[tuple[float, str]] = []
        rows.extend((value, "minimum") for value in self.true_minima)
        rows.extend((value, "flat_minimum") for value in self.true_flat_minima)
        rows.extend((value, "boundary_minimum") for value in self.true_boundary_minima)
        rows.extend(
            (value, "stationary_inflection")
            for value in self.true_other_stationary
        )
        return tuple(sorted(rows))


def _normalized_polynomial(coefficients: np.ndarray) -> tuple[float, ...]:
    coefficients = np.asarray(coefficients, dtype=float)
    grid = np.linspace(0.0, 1.0, 10001)
    scale = float(np.max(np.abs(np.polyval(coefficients, grid))))
    if not np.isfinite(scale) or scale <= 0.0:
        raise ValueError("Polynomial scale must be finite and positive.")
    return tuple(float(value) for value in coefficients / scale)


def _root_power(root: float, power: int) -> np.ndarray:
    return np.poly1d([1.0, -float(root)]) ** int(power)


def _equal_minima_polynomial(roots: tuple[float, ...]) -> tuple[float, ...]:
    polynomial = np.poly1d([1.0])
    for root in roots:
        polynomial = polynomial * _root_power(root, 2)
    return _normalized_polynomial(np.asarray(polynomial.c, dtype=float))


def _single_power_polynomial(root: float, power: int) -> tuple[float, ...]:
    polynomial = _root_power(root, power)
    return _normalized_polynomial(np.asarray(polynomial.c, dtype=float))


def adversarial_smoothness_cases() -> tuple[AdversarialSmoothnessCase, ...]:
    """Return deterministic objectives spanning difficult 1-D search geometry."""

    five = (0.10, 0.25, 0.45, 0.70, 0.90)
    return (
        AdversarialSmoothnessCase(
            name="near_zero",
            description="Quadratic minimum very near the lower endpoint.",
            coefficients=_single_power_polynomial(0.001, 2),
            true_minima=(0.001,),
        ),
        AdversarialSmoothnessCase(
            name="near_one",
            description="Quadratic minimum very near the upper endpoint.",
            coefficients=_single_power_polynomial(0.999, 2),
            true_minima=(0.999,),
        ),
        AdversarialSmoothnessCase(
            name="close_pair",
            description="Two equal minima separated by only 0.02 in smoothness.",
            coefficients=_equal_minima_polynomial((0.45, 0.47)),
            true_minima=(0.45, 0.47),
        ),
        AdversarialSmoothnessCase(
            name="close_upper_pair",
            description="Two close minima concentrated in the upper tail.",
            coefficients=_equal_minima_polynomial((0.97, 0.995)),
            true_minima=(0.97, 0.995),
        ),
        AdversarialSmoothnessCase(
            name="flat_minimum",
            description="Quartic minimum with zero second derivative at the optimum.",
            coefficients=_single_power_polynomial(0.733, 4),
            true_flat_minima=(0.733,),
        ),
        AdversarialSmoothnessCase(
            name="stationary_inflection",
            description="Stationary inflection: derivative touches zero without changing sign.",
            coefficients=_single_power_polynomial(0.537, 3),
            true_boundary_minima=(0.0,),
            true_other_stationary=(0.537,),
        ),
        AdversarialSmoothnessCase(
            name="five_minima",
            description="Five separated equal local/global minima.",
            coefficients=_equal_minima_polynomial(five),
            true_minima=five,
        ),
        AdversarialSmoothnessCase(
            name="boundary_zero",
            description="Exact global minimum at S=0.",
            coefficients=(1.0, 0.0, 0.0),
            true_boundary_minima=(0.0,),
        ),
        AdversarialSmoothnessCase(
            name="boundary_one",
            description="Exact global minimum at S=1.",
            coefficients=(1.0, -2.0, 1.0),
            true_boundary_minima=(1.0,),
        ),
    )
