"""Reproducible simulated time-series mechanisms for the joint paper campaign.

One generated series holds OBSERVED, LATENT TREND, SEASONAL and NOISE
separately. Only observed data may enter feasible tuning algorithms.
No source-paper parameters are silently rescaled for Experiment A.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product

import numpy as np
from scipy.stats import beta as beta_distribution


A_SHAPES = ("source_linear", "source_beta")
B_SHAPES = (
    "linear", "quadratic_up", "quadratic_turn", "cubic_s",
    "cubic_bend", "quartic", "sine_slow", "sine_fast",
    "beta_mix", "sigmoid", "slope_break_early", "slope_break_late",
    "two_breaks", "terminal_bend", "flat", "oscillatory_trend",
)
C_SHAPES = (
    "stationary_linear", "stationary_curve",
    "abrupt_slope", "abrupt_curvature", "gradual_curvature",
    "variance_change", "temporary_regime", "two_regime_switches",
)


# Study D stress-tests irregular latent dynamics, not arbitrary cherry-picked
# individual runs. Full factorial: 12 shapes x 2 N x 3 sigma x 5 noise x
# 2 seasonal = 720 scenarios. "mega" adds these to 528 A/B/C scenarios.
D_SHAPES = (
    "terminal_jump", "double_jump", "jump_recovery",
    "transient_pulse", "chirp", "harmonic_beating",
    "piecewise_plateau", "terminal_spike", "accelerating_oscillation",
    "double_sigmoid", "stochastic_level", "stochastic_slope",
)


@dataclass(frozen=True)
class Scenario:
    study: str
    shape: str
    n_obs: int
    sigma: float
    noise: str
    seasonal: bool = False

    @property
    def key(self) -> str:
        return (f"{self.study}__{self.shape}__N{self.n_obs}__"
                f"{self.noise}__sd{self.sigma:g}__"
                f"seasonal{int(self.seasonal)}")

    @property
    def window(self) -> int:
        if self.study == "A":
            return 22 if self.n_obs == 50 else 60
        return 48 if self.n_obs <= 200 else 72


@dataclass(frozen=True)
class GeneratedSeries:
    observed: np.ndarray
    trend: np.ndarray
    seasonality: np.ndarray
    noise: np.ndarray


def _shape(shape: str, u: np.ndarray) -> np.ndarray:
    """Deterministic function on the SAME full-series time scale u in [0,1]."""
    if shape in {"linear", "stationary_linear"}:
        return .5 + 4*u
    if shape in {"quadratic_up"}:
        return .4 + 4*u*u
    if shape in {"quadratic_turn"}:
        return .6 + 3.8 * (1 - 4*(u - .52)**2)
    if shape == "cubic_s":
        return 2.2 + 16*(u - .5)**3
    if shape == "cubic_bend":
        return .8 + 3*u + 5*u**3
    if shape == "quartic":
        return .5 + 2*u + 7*(u-.38)**4
    if shape in {"sine_slow", "stationary_curve"}:
        return .8 + 3*u + 1.2*np.sin(2*np.pi*u)
    if shape == "sine_fast":
        return .8 + 3*u + .8*np.sin(6*np.pi*u)
    if shape == "beta_mix":
        return .6 * beta_distribution.pdf(u, 30, 17) + .4 * beta_distribution.pdf(u, 3, 11)
    if shape == "sigmoid":
        return .8 + 3*u + 3/(1+np.exp(-22*(u-.63)))
    if shape == "slope_break_early":
        return .8 + 1.1*u + 5*np.maximum(0, u-.38)
    if shape == "slope_break_late":
        return .8 + 1.1*u + 8*np.maximum(0, u-.76)
    if shape == "two_breaks":
        return .8 + 3*u + 6*np.maximum(0,u-.35) - 9*np.maximum(0,u-.73)
    if shape == "terminal_bend":
        return .8 + 3*u + 20*np.maximum(0,u-.72)**2
    if shape == "flat":
        return np.full_like(u, 2.0)
    if shape == "oscillatory_trend":
        return 1 + 3*u + 1.1*np.sin(4*np.pi*u+.3)
    if shape == "abrupt_slope":
        return 1 + 1.1*u + 8*np.maximum(0,u-.64)
    if shape == "abrupt_curvature":
        return 1 + 2*u + 15*np.maximum(0,u-.62)**2
    if shape == "gradual_curvature":
        return 1 + 1.2*u + 2.7*u*u + 7*u**3
    if shape == "variance_change":
        return .8 + 3*u + .5*np.sin(3*np.pi*u)
    if shape == "temporary_regime":
        return 1+2*u + 5*np.maximum(0,u-.38)-5*np.maximum(0,u-.68)
    if shape == "two_regime_switches":
        return 1+2*u+7*np.maximum(0,u-.27)-11*np.maximum(0,u-.55)+8*np.maximum(0,u-.81)
    if shape == "terminal_jump":
        return 1+2*u+3.2*(u>=.88)
    if shape == "double_jump":
        return 1+2*u+3*(u>=.35)-4*(u>=.72)
    if shape == "jump_recovery":
        return 1+2*u-3*(u>=.65)+12*np.maximum(0,u-.65)
    if shape == "transient_pulse":
        return 1+2*u+2.5*np.exp(-((u-.72)/.065)**2)
    if shape == "chirp":
        return 1+2*u+.6*np.sin(2*np.pi*(u+5*u*u))
    if shape == "harmonic_beating":
        return 1+2*u+1.2*np.sin(12*np.pi*u)*np.cos(1.5*np.pi*u)
    if shape == "piecewise_plateau":
        return 1+2*np.minimum(u,.35)+4*np.maximum(0,u-.75)
    if shape == "terminal_spike":
        return 1+2*u+4*np.exp(-((u-.96)/.025)**2)
    if shape == "accelerating_oscillation":
        return 1+2*u+2*u*np.sin(6*np.pi*u)
    if shape == "double_sigmoid":
        return 1+1/(1+np.exp(-45*(u-.3)))+2/(1+np.exp(-55*(u-.78)))
    if shape in {"stochastic_level","stochastic_slope"}:
        # A dedicated RNG generates stochastic tau in make_series.
        return np.zeros_like(u)
    raise ValueError(f"Unknown trend shape: {shape!r}")


def make_series(scenario: Scenario, seed: int) -> GeneratedSeries:
    """Independent Monte Carlo replication; fully reproducible from specs/seed."""
    if scenario.n_obs < 40 or scenario.sigma < 0:
        raise ValueError("n_obs must be >=40 and sigma nonnegative.")
    n = scenario.n_obs
    u = np.linspace(0., 1., n)
    if scenario.study == "A":
        if scenario.shape == "source_linear":
            tau = 4*np.arange(1, n+1, dtype=float)/n
        elif scenario.shape == "source_beta":
            source_u = np.arange(1, n+1, dtype=float)/n
            tau = .6*beta_distribution.pdf(source_u,30,17)+.4*beta_distribution.pdf(source_u,3,11)
        else:
            raise ValueError("Experiment A accepts only its two source-paper trends.")
    else:
        if scenario.shape in {"stochastic_level","stochastic_slope"}:
            trend_rng = np.random.default_rng(
                np.random.SeedSequence([int(seed), n, 1913])
            )
            if scenario.shape=="stochastic_level":
                increments = trend_rng.normal(0,.13,n)+.014
                tau = np.cumsum(increments)
            else:
                slope = np.cumsum(trend_rng.normal(0,.012,n))
                tau = np.cumsum(slope+.018)
        else:
            tau = _shape(scenario.shape, u)
        if scenario.shape != "flat":
            span = float(np.ptp(tau))
            if not span > 0:
                raise ValueError("Trend shape is unexpectedly flat.")
            tau = (tau - np.min(tau)) * (4.0 / span)
        tau = np.asarray(tau, dtype=float)

    rng = np.random.default_rng(np.random.SeedSequence([int(seed), n]))
    sigma = float(scenario.sigma)
    if scenario.noise == "iid":
        eps = rng.normal(0, sigma, n)
    elif scenario.noise == "ar1":
        phi = .7
        eps = np.zeros(n)
        eps[0] = rng.normal(0, sigma)
        eps[1:] = rng.normal(0, sigma*np.sqrt(1-phi*phi), n-1)
        for i in range(1,n):
            eps[i] += phi*eps[i-1]
    elif scenario.noise == "student_t":
        eps = sigma*np.sqrt(3/5)*rng.standard_t(5,n)
    elif scenario.noise == "heteroskedastic":
        std = sigma*(.45+1.1*u)
        eps = rng.normal(0,1,n)*std
    elif scenario.noise == "contaminated":
        # 4% contamination, rare shocks with 5x Gaussian SD. Normalized
        # so unconditional noise variance still equals nominal sigma^2.
        base_sd = sigma / np.sqrt(1.+.04*(25.-1.))
        eps = rng.normal(0,base_sd,n)
        mask = rng.random(n) < .04
        eps[mask] = rng.normal(0,5*base_sd,int(np.sum(mask)))
    else:
        raise ValueError("Unsupported noise model.")
    if scenario.shape == "variance_change":
        eps = eps * np.where(u < .65,.6,1.8)
    season = (
        np.resize(np.array([1.,-.5,-2.5,2.]),n)
        if scenario.seasonal else np.zeros(n)
    )
    return GeneratedSeries(np.asarray(tau+season+eps,float),tau,season,eps)


def grid_scenarios(preset: str) -> tuple[Scenario,...]:
    """Balanced, interpretable factors. Horizon/order vary *within* a scenario.

    Every seed shares the same generated series across its methods/d/h.
    """
    if preset == "smoke":
        return (
            Scenario("A","source_linear",50,.5,"iid"),
            Scenario("B","cubic_s",160,.5,"iid"),
            Scenario("C","abrupt_slope",180,.5,"ar1"),
        )
    if preset == "pilot":
        a = list(Scenario("A",shape,n,sd,"iid",season)
                 for shape,n,sd,season in product(A_SHAPES,(50,200),(.5,2.),(False,True)))
        b = list(Scenario("B",shape,180,.5,noise)
                 for shape,noise in product(
                    ("linear","quadratic_turn","cubic_s","sine_slow",
                     "slope_break_late","beta_mix"),("iid","ar1")))
        c = list(Scenario("C",shape,240,.5,"iid") for shape in C_SHAPES)
        return tuple(a+b+c)
    if preset == "formal8h":
        # Deliberately LIMITED balanced scientific panel, not the exploratory
        # 1,248-cell exhaustive stress suite. Each study is represented,
        # including the original complete source 2^4 control A.
        # B: 8 tau shapes x 2 N x 2 sigma = 32 cells, iid.
        # C: 8 changes x 2 N x 2 noise = 32 cells, fixed sigma.
        # D: 12 unusual shapes x 2 N x 2 noise = 48 cells, fixed sigma.
        # 16+32+32+48=128 interpretable cells with identical outer origins
        # and independent seeds within each DGP cell.
        a=tuple(Scenario("A",shape,n,sd,"iid",season)
                for shape,n,sd,season in product(
                    A_SHAPES,(50,200),(.5,2.),(False,True)))
        b=tuple(Scenario("B",shape,n,sd,"iid")
                for shape,n,sd in product(
                    ("linear","quadratic_up","quadratic_turn","cubic_s",
                     "quartic","sine_slow","slope_break_late","beta_mix"),
                    (180,360),(.25,1.)))
        cc=tuple(Scenario("C",shape,n,.5,noise)
                 for shape,n,noise in product(
                    C_SHAPES,(240,400),("iid","ar1")))
        dd=tuple(Scenario("D",shape,n,.8,noise)
                 for shape,n,noise in product(
                    D_SHAPES,(300,600),("iid","contaminated")))
        result=a+b+cc+dd
        if len(result)!=128 or len({s.key for s in result})!=128:
            raise AssertionError("Formal 8h design must have 128 distinct factorial cells.")
        return result
    if preset == "stress":
        return tuple(
            Scenario("D",shape,n,sd,noise,season)
            for shape,n,sd,noise,season in product(
                D_SHAPES,(300,600),(.25,.8,1.6),
                ("iid","ar1","student_t","heteroskedastic","contaminated"),
                (False,True),
            )
        )
    if preset == "mega":
        return grid_scenarios("extensive")+grid_scenarios("stress")
    if preset != "extensive":
        raise ValueError("preset must be smoke, pilot, extensive, stress or mega.")
    a = [Scenario("A",shape,n,sd,"iid",season)
         for shape,n,sd,season in product(A_SHAPES,(50,200),(.5,2.),(False,True))]
    b = [Scenario("B",shape,n,sd,noise)
         for shape,n,sd,noise in product(
            B_SHAPES,(180,360),(.25,.5,1.),("iid","ar1","student_t","heteroskedastic"))]
    c = [Scenario("C",shape,n,sd,noise)
         for shape,n,sd,noise in product(
            C_SHAPES,(240,400),(.25,.8),("iid","ar1","student_t","heteroskedastic"))]
    return tuple(a+b+c)
