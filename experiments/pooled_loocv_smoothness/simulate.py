"""Source-inspired Cortés-Toto et al. (2017) 2^4 trend simulation.

Additional R>1 pooling and seed counts are independent extensions,
not claimed as a direct numerical reproduction of the 2017 R code.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

import numpy as np
from scipy.stats import beta


@dataclass(frozen=True)
class Scenario:
    trend: str
    seasonality: bool
    sigma: float
    n: int

    def as_dict(self) -> dict:
        return {"trend": self.trend, "seasonality": self.seasonality,
                "sigma": self.sigma, "n": self.n}


def factorial_scenarios() -> list[Scenario]:
    """All 16 source-inspired factorial cells in deterministic order."""
    return [
        Scenario(shape, season, noise, n)
        for shape, season, noise, n in product(
            ("linear", "nonlinear"), (False, True), (0.5, 2.0), (50, 200)
        )
    ]


def latent_components(scenario: Scenario) -> tuple[np.ndarray, np.ndarray]:
    """Return latent trend and quarterly seasonal component separately."""
    n = scenario.n
    u = np.linspace(0.0, 1.0, n)
    if scenario.trend == "linear":
        trend = 4.0 * np.arange(1, n + 1, dtype=float) / n
    elif scenario.trend == "nonlinear":
        trend = 0.6 * beta.pdf(u, 30, 17) + 0.4 * beta.pdf(u, 3, 11)
    else:
        raise ValueError("trend must be 'linear' or 'nonlinear'")
    cycle = np.resize(np.array([1.0, -0.5, -2.5, 2.0]), n)
    season = cycle if scenario.seasonality else np.zeros(n)
    return trend, season


def draw_pool(scenario: Scenario, r: int, seed: int):
    """R independent noise replicates of one *shared* latent signal."""
    if r < 1:
        raise ValueError("r must be at least one")
    trend, season = latent_components(scenario)
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, scenario.sigma, (r, scenario.n))
    return trend[np.newaxis, :] + season[np.newaxis, :] + noise, trend, season
