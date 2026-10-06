"""Shared utilities for the smoothness-CV paper experiments.

This module is intentionally paper-specific. Reusable estimator logic stays in
src/trend_estimation; experiment design, simulation mechanisms, frozen presets,
and output conventions live here.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess

import numpy as np
import pandas as pd

from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.core.smoothness import effective_degrees_of_freedom
from trend_estimation.forecasting.objectives import (
    prepare_rolling_pure_forecast_objective,
)
from trend_estimation.forecasting.operators import finite_difference_forecast_operator
from trend_estimation.selection.classical import (
    pure_smoother_score,
    select_classical_pure_smoothness,
)
from trend_estimation.validation.rolling_origin import RollingOriginSplit


@dataclass(frozen=True)
class Preset:
    name: str
    seeds: tuple[int, ...]
    trend_kinds: tuple[str, ...]
    noise_models: tuple[str, ...]
    noise_stds: tuple[float, ...]
    horizons: tuple[int, ...]
    n_obs: int
    order: int
    window: int
    outer_initial_train: int
    outer_step: int
    inner_step: int
    max_inner_origins: int
    n_s_grid: int


PRESETS: dict[str, Preset] = {
    "smoke": Preset(
        name="smoke",
        seeds=(0,),
        trend_kinds=("linear", "smooth_curve"),
        noise_models=("iid",),
        noise_stds=(0.4,),
        horizons=(1, 6),
        n_obs=220,
        order=2,
        window=60,
        outer_initial_train=140,
        outer_step=30,
        inner_step=4,
        max_inner_origins=18,
        n_s_grid=81,
    ),
    "quick": Preset(
        name="quick",
        seeds=(0, 1, 2),
        trend_kinds=("linear", "smooth_curve", "slope_change", "low_frequency"),
        noise_models=("iid", "ar1"),
        noise_stds=(0.3, 0.7),
        horizons=(1, 3, 6, 12),
        n_obs=240,
        order=2,
        window=60,
        outer_initial_train=150,
        outer_step=24,
        inner_step=3,
        max_inner_origins=24,
        n_s_grid=201,
    ),
    "paper": Preset(
        name="paper",
        seeds=tuple(range(30)),
        trend_kinds=("linear", "smooth_curve", "slope_change", "low_frequency"),
        noise_models=("iid", "ar1", "student_t"),
        noise_stds=(0.2, 0.5, 0.9),
        horizons=(1, 3, 6, 12),
        n_obs=300,
        order=2,
        window=72,
        outer_initial_train=180,
        outer_step=24,
        inner_step=2,
        max_inner_origins=36,
        n_s_grid=801,
    ),
}


def git_short_sha() -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def smoothness_grid(n: int) -> np.ndarray:
    n = int(n)
    if n < 3:
        raise ValueError("n must be at least 3.")
    return np.linspace(0.0, 1.0, n, dtype=float)


def latent_trend(n_obs: int, kind: str) -> np.ndarray:
    """Deterministic latent mechanisms with broadly comparable ranges.

    CP01 used four mild mechanisms. CP02 adds deliberately harder local-shape
    mechanisms so that the d=2 extrapolation problem is not dominated by cases
    where the maximally smooth linear limit is nearly oracle-optimal.
    """

    n_obs = int(n_obs)
    if n_obs < 8:
        raise ValueError("n_obs must be at least 8.")
    t = np.linspace(0.0, 1.0, n_obs, dtype=float)
    kind = str(kind)

    if kind == "linear":
        trend = 0.5 + 4.0 * t
    elif kind == "smooth_curve":
        trend = 0.5 + 2.8 * t + 0.7 * np.sin(2.0 * np.pi * t)
    elif kind == "slope_change":
        knot = 0.56
        trend = 0.5 + 1.6 * t + 4.0 * np.maximum(t - knot, 0.0)
    elif kind == "low_frequency":
        trend = 0.5 + 2.4 * t + 0.9 * np.sin(1.5 * np.pi * t - 0.4)
    elif kind == "quadratic":
        trend = 0.5 + 0.7 * t + 4.2 * t**2
    elif kind == "turning_point":
        trend = 0.4 + 5.0 * t - 4.2 * t**2
    elif kind == "recent_slope_change":
        knot = 0.72
        trend = 0.4 + 1.4 * t + 7.0 * np.maximum(t - knot, 0.0)
    elif kind == "oscillatory":
        trend = 0.6 + 2.2 * t + 0.8 * np.sin(4.0 * np.pi * t - 0.25)
    elif kind == "terminal_bend":
        bend = np.maximum(t - 0.68, 0.0)
        trend = 0.5 + 2.0 * t + 9.0 * bend**2
    else:
        raise ValueError(
            "Unknown trend kind. Expected one of: linear, smooth_curve, "
            "slope_change, low_frequency, quadratic, turning_point, "
            "recent_slope_change, oscillatory, terminal_bend."
        )
    return np.asarray(trend, dtype=float)


def noise_series(
    n_obs: int,
    *,
    model: str,
    noise_std: float,
    seed: int,
    ar1_phi: float = 0.7,
) -> np.ndarray:
    """Generate zero-mean noise with approximately the requested marginal SD."""

    rng = np.random.default_rng(int(seed))
    n_obs = int(n_obs)
    sigma = float(noise_std)
    if sigma < 0.0:
        raise ValueError("noise_std must be nonnegative.")

    model = str(model)
    if model == "iid":
        return rng.normal(0.0, sigma, size=n_obs)

    if model == "ar1":
        phi = float(ar1_phi)
        innovations_sd = sigma * np.sqrt(max(1.0 - phi**2, 0.0))
        innovations = rng.normal(0.0, innovations_sd, size=n_obs)
        e = np.zeros(n_obs, dtype=float)
        if sigma > 0.0:
            e[0] = rng.normal(0.0, sigma)
        for i in range(1, n_obs):
            e[i] = phi * e[i - 1] + innovations[i]
        return e

    if model == "student_t":
        df = 5.0
        scale = sigma / np.sqrt(df / (df - 2.0)) if sigma > 0.0 else 0.0
        return rng.standard_t(df, size=n_obs) * scale

    raise ValueError("noise model must be iid, ar1, or student_t.")


def make_simulated_series(
    *,
    n_obs: int,
    trend_kind: str,
    noise_model: str,
    noise_std: float,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    trend = latent_trend(n_obs, trend_kind)
    noise = noise_series(
        n_obs,
        model=noise_model,
        noise_std=noise_std,
        seed=seed,
    )
    return trend + noise, trend


def common_outer_origins(preset: Preset) -> tuple[int, ...]:
    """Use the same outer origins for every horizon in one preset."""

    max_h = max(preset.horizons)
    stop = preset.n_obs - max_h
    origins = tuple(
        range(
            int(preset.outer_initial_train),
            int(stop) + 1,
            int(preset.outer_step),
        )
    )
    if not origins:
        raise ValueError("Preset leaves no outer forecast origins.")
    if min(origins) < preset.window + max_h:
        raise ValueError("outer_initial_train is too short for the frozen window/horizon.")
    return origins


def inner_splits(
    *,
    n_history: int,
    window: int,
    horizon: int,
    step: int,
    max_origins: int,
) -> list[RollingOriginSplit]:
    """Fixed-width chronological splits ending strictly before the outer origin."""

    n_history = int(n_history)
    window = int(window)
    horizon = int(horizon)
    step = int(step)
    if n_history < window + horizon:
        raise ValueError("Not enough history for one inner rolling origin.")

    origins = list(range(window, n_history - horizon + 1, step))
    if max_origins > 0:
        origins = origins[-int(max_origins) :]
    if not origins:
        raise ValueError("No inner rolling origins were available.")

    return [
        RollingOriginSplit(
            train=slice(origin - window, origin),
            validation=slice(origin, origin + horizon),
        )
        for origin in origins
    ]


def forecast_cv_curve(
    history: np.ndarray,
    *,
    order: int,
    window: int,
    horizon: int,
    step: int,
    max_inner_origins: int,
    s_grid: np.ndarray,
) -> np.ndarray:
    """Score candidate smoothness values using historical rolling forecasts.

    This function selects/scorers the hyperparameter only. The trend fits
    created inside the rolling folds are temporary and must not be reused as
    the final outer-origin trend. After S is selected, callers must refit on
    the latest available outer-origin window before forecasting the test block.
    """

    splits = inner_splits(
        n_history=len(history),
        window=window,
        horizon=horizon,
        step=step,
        max_origins=max_inner_origins,
    )
    prepared = prepare_rolling_pure_forecast_objective(
        history,
        splits,
        order=order,
    )
    solver = cached_pure_solver(window, order)
    values = np.empty(len(s_grid), dtype=float)
    for i, s in enumerate(s_grid):
        lambda_ = solver.lambda_from_s(float(s))
        values[i] = prepared.evaluate(lambda_).value
    return values


def recovery_curve(
    y_window: np.ndarray,
    true_window: np.ndarray,
    *,
    order: int,
    s_grid: np.ndarray,
) -> np.ndarray:
    solver = cached_pure_solver(len(y_window), order)
    values = np.empty(len(s_grid), dtype=float)
    for i, s in enumerate(s_grid):
        fit = solver.fit_for_s(y_window, float(s))
        values[i] = float(np.mean((fit.trend - true_window) ** 2))
    return values


def grid_argmin(
    s_grid: np.ndarray,
    values: np.ndarray,
) -> tuple[float, float, int]:
    finite = np.isfinite(values)
    if not np.any(finite):
        raise ValueError("Objective curve has no finite values.")
    indices = np.flatnonzero(finite)
    local = int(np.argmin(values[finite]))
    idx = int(indices[local])
    return float(s_grid[idx]), float(values[idx]), idx


def fit_and_forecast(
    y_window: np.ndarray,
    *,
    order: int,
    horizon: int,
    smoothness: float,
) -> tuple[np.ndarray, np.ndarray, float, float]:
    """Freshly refit at the outer origin, then extrapolate.

    In the smoothness-CV experiments, y_window must be the most recent
    L-observation window available at the current outer origin. The supplied
    smoothness may have been selected by inner CV, but no inner-fold fit is
    carried forward into this function.
    """

    solver = cached_pure_solver(len(y_window), order)
    fit = solver.fit_for_s(y_window, float(smoothness))
    operator = finite_difference_forecast_operator(
        n_fit=len(y_window),
        order=order,
        steps=horizon,
    )
    prediction = operator.apply(fit.trend)
    edf = float(
        effective_degrees_of_freedom(
            fit.lambda_,
            n_obs=len(y_window),
            order=order,
        )
    )
    return fit.trend, prediction, float(fit.lambda_), edf



def latent_forecast_oracle_curve(
    y_window: np.ndarray,
    latent_future: np.ndarray,
    *,
    order: int,
    s_grid: np.ndarray,
) -> np.ndarray:
    """Simulation-only oracle loss for extrapolating the latent future trend.

    The fit still uses the noisy historical window; only the choice of S is
    allowed to see the latent future. This makes the oracle useful for measuring
    selection regret without turning it into a feasible forecasting method.
    """

    horizon = int(len(latent_future))
    solver = cached_pure_solver(len(y_window), order)
    operator = finite_difference_forecast_operator(
        n_fit=len(y_window),
        order=order,
        steps=horizon,
    )
    values = np.empty(len(s_grid), dtype=float)
    for i, s in enumerate(s_grid):
        fit = solver.fit_for_s(y_window, float(s))
        prediction = operator.apply(fit.trend)
        values[i] = float(np.mean((latent_future - prediction) ** 2))
    return values


def classical_score_curve(
    y_window: np.ndarray,
    *,
    order: int,
    criterion: str,
    s_grid: np.ndarray,
) -> np.ndarray:
    """Return a full classical selector score curve for diagnostics."""

    values = np.empty(len(s_grid), dtype=float)
    for i, s in enumerate(s_grid):
        values[i] = pure_smoother_score(
            y_window,
            order=order,
            smoothness=float(s),
            criterion=criterion,
        ).score
    return values


def classical_selections(
    y_window: np.ndarray,
    *,
    order: int,
    s_grid: np.ndarray,
) -> dict[str, tuple[float, float]]:
    out: dict[str, tuple[float, float]] = {}
    for criterion in ("cv", "gcv", "aicc", "bic"):
        selected = select_classical_pure_smoothness(
            y_window,
            order=order,
            criterion=criterion,
            smoothness_grid=s_grid,
        )
        out[criterion] = (selected.smoothness_, selected.score_)
    return out


def add_relative_losses(results: pd.DataFrame, baseline: str = "gcv") -> pd.DataFrame:
    """Attach within-block MSE ratios to a baseline selector."""

    keys = [
        "scenario_id",
        "seed",
        "trend_kind",
        "noise_model",
        "noise_std",
        "outer_origin",
        "horizon",
    ]
    if "window" in results.columns:
        keys.insert(5, "window")
    base = (
        results.loc[results["selector"] == baseline, keys + ["forecast_mse_observed"]]
        .rename(columns={"forecast_mse_observed": "baseline_mse"})
    )
    merged = results.merge(base, on=keys, how="left", validate="many_to_one")
    merged["relative_mse_to_gcv"] = (
        merged["forecast_mse_observed"] / merged["baseline_mse"]
    )
    merged["relative_rmsfe_to_gcv"] = np.sqrt(merged["relative_mse_to_gcv"])
    return merged


def write_checkpoint_summary(results: pd.DataFrame, path: Path) -> None:
    summary = (
        results.groupby(["selector", "horizon"], dropna=False)
        .agg(
            n_blocks=("forecast_mse_observed", "size"),
            mean_selected_s=("selected_s", "mean"),
            median_selected_s=("selected_s", "median"),
            mean_edf=("edf", "mean"),
            mean_forecast_mse=("forecast_mse_observed", "mean"),
            median_forecast_mse=("forecast_mse_observed", "median"),
            median_relative_rmsfe_to_gcv=("relative_rmsfe_to_gcv", "median"),
            mean_train_recovery_mse=("train_recovery_mse", "mean"),
        )
        .reset_index()
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(path, index=False)
