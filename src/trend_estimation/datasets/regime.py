from __future__ import annotations

import numpy as np

from .synthetic import SyntheticTrendData


def _validate_phi(phi: float) -> float:
    phi = float(phi)
    if not -1.0 < phi < 1.0:
        raise ValueError("AR(1) phi must lie strictly between -1 and 1.")
    return phi


def _piecewise_ar1_noise(
    rng: np.random.Generator,
    noise_std: np.ndarray,
    phi: np.ndarray,
) -> np.ndarray:
    """Generate AR(1) observation noise with time-varying local parameters.

    For constant parameters, noise_std is the stationary marginal standard
    deviation. With a regime change, the recursion transitions into the new
    marginal scale rather than being reset artificially at the breakpoint.
    """

    noise_std = np.asarray(noise_std, dtype=float)
    phi = np.asarray(phi, dtype=float)
    if noise_std.ndim != 1 or phi.ndim != 1 or noise_std.size != phi.size:
        raise ValueError("noise_std and phi must be one-dimensional arrays of equal length.")
    if np.any(noise_std < 0.0):
        raise ValueError("noise standard deviations must be nonnegative.")
    if np.any(np.abs(phi) >= 1.0):
        raise ValueError("All AR(1) coefficients must have absolute value < 1.")

    n_obs = noise_std.size
    if n_obs == 0:
        return np.array([], dtype=float)

    error = np.empty(n_obs, dtype=float)
    error[0] = rng.normal(0.0, noise_std[0])

    for t in range(1, n_obs):
        innovation_std = noise_std[t] * np.sqrt(max(0.0, 1.0 - phi[t] ** 2))
        error[t] = phi[t] * error[t - 1] + rng.normal(0.0, innovation_std)

    return error


def make_local_linear_ar1_series(
    n_obs: int = 240,
    *,
    initial_slope: float = 0.02,
    slope_noise_std: float = 0.01,
    observation_noise_std: float = 0.5,
    ar1_phi: float = 0.0,
    random_state: int | None = 123,
) -> SyntheticTrendData:
    """Local-linear latent trend observed with stationary AR(1) noise.

    slope_noise_std controls latent-trend roughness.
    observation_noise_std controls the marginal observation-noise scale.
    ar1_phi changes serial dependence without changing that target marginal
    standard deviation in the constant-parameter case.
    """

    n_obs = int(n_obs)
    if n_obs <= 1:
        raise ValueError("n_obs must be at least 2.")
    slope_noise_std = float(slope_noise_std)
    observation_noise_std = float(observation_noise_std)
    if slope_noise_std < 0.0 or observation_noise_std < 0.0:
        raise ValueError("Noise standard deviations must be nonnegative.")
    ar1_phi = _validate_phi(ar1_phi)

    rng = np.random.default_rng(random_state)

    slope = np.empty(n_obs, dtype=float)
    true_trend = np.empty(n_obs, dtype=float)
    slope[0] = float(initial_slope)
    true_trend[0] = 0.0

    for t in range(1, n_obs):
        slope[t] = slope[t - 1] + rng.normal(0.0, slope_noise_std)
        true_trend[t] = true_trend[t - 1] + slope[t]

    noise_scale = np.full(n_obs, observation_noise_std, dtype=float)
    phi = np.full(n_obs, ar1_phi, dtype=float)
    error = _piecewise_ar1_noise(rng, noise_scale, phi)
    y = true_trend + error

    return SyntheticTrendData(
        y=y,
        true_trend=true_trend,
        index=np.arange(n_obs),
        metadata={
            "type": "local_linear_ar1",
            "initial_slope": float(initial_slope),
            "slope_noise_std": slope_noise_std,
            "observation_noise_std": observation_noise_std,
            "ar1_phi": ar1_phi,
        },
    )


def make_two_regime_local_linear_series(
    n_obs: int = 300,
    *,
    regime_point: int | None = None,
    initial_slope: float = 0.02,
    pre_slope_noise_std: float = 0.005,
    post_slope_noise_std: float = 0.02,
    pre_observation_noise_std: float = 0.25,
    post_observation_noise_std: float = 0.75,
    pre_ar1_phi: float = 0.1,
    post_ar1_phi: float = 0.7,
    level_shift: float = 0.0,
    slope_shift: float = 0.0,
    random_state: int | None = 123,
) -> SyntheticTrendData:
    """Two-regime local-linear trend with separately controlled noise features.

    The regime can change latent-trend roughness, observation-noise scale,
    serial dependence, level, and slope. These controls are deliberately
    separate so experiments do not equate regime with volatility alone.
    """

    n_obs = int(n_obs)
    if n_obs <= 2:
        raise ValueError("n_obs must be at least 3.")
    rp = n_obs // 2 if regime_point is None else int(regime_point)
    if not 1 <= rp < n_obs:
        raise ValueError("regime_point must satisfy 1 <= regime_point < n_obs.")

    pre_phi = _validate_phi(pre_ar1_phi)
    post_phi = _validate_phi(post_ar1_phi)

    pre_slope_noise_std = float(pre_slope_noise_std)
    post_slope_noise_std = float(post_slope_noise_std)
    pre_observation_noise_std = float(pre_observation_noise_std)
    post_observation_noise_std = float(post_observation_noise_std)

    if min(
        pre_slope_noise_std,
        post_slope_noise_std,
        pre_observation_noise_std,
        post_observation_noise_std,
    ) < 0.0:
        raise ValueError("Noise standard deviations must be nonnegative.")

    rng = np.random.default_rng(random_state)

    slope = np.empty(n_obs, dtype=float)
    true_trend = np.empty(n_obs, dtype=float)
    slope[0] = float(initial_slope)
    true_trend[0] = 0.0

    for t in range(1, n_obs):
        slope_sd = pre_slope_noise_std if t < rp else post_slope_noise_std
        slope[t] = slope[t - 1] + rng.normal(0.0, slope_sd)

        if t == rp:
            slope[t] += float(slope_shift)
            true_trend[t] = true_trend[t - 1] + slope[t] + float(level_shift)
        else:
            true_trend[t] = true_trend[t - 1] + slope[t]

    noise_scale = np.where(
        np.arange(n_obs) < rp,
        pre_observation_noise_std,
        post_observation_noise_std,
    ).astype(float)
    phi = np.where(
        np.arange(n_obs) < rp,
        pre_phi,
        post_phi,
    ).astype(float)
    error = _piecewise_ar1_noise(rng, noise_scale, phi)
    y = true_trend + error

    return SyntheticTrendData(
        y=y,
        true_trend=true_trend,
        index=np.arange(n_obs),
        metadata={
            "type": "two_regime_local_linear",
            "regime_point": rp,
            "initial_slope": float(initial_slope),
            "pre_slope_noise_std": pre_slope_noise_std,
            "post_slope_noise_std": post_slope_noise_std,
            "pre_observation_noise_std": pre_observation_noise_std,
            "post_observation_noise_std": post_observation_noise_std,
            "pre_ar1_phi": pre_phi,
            "post_ar1_phi": post_phi,
            "level_shift": float(level_shift),
            "slope_shift": float(slope_shift),
        },
    )
