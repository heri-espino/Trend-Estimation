from __future__ import annotations

from dataclasses import dataclass

from trend_estimation.core.smoothness import lambda_to_smoothness
from trend_estimation.forecasting.objectives import rolling_pure_forecast_loss_derivatives
from trend_estimation.selection.numerical import (
    StationaryPointSearchResult,
    find_stationary_points_log_lambda,
)
from trend_estimation.utils.arrays import as_1d_float_array
from trend_estimation.validation.rolling_origin import RollingOriginSplit


@dataclass(frozen=True)
class ForecastOptimalCandidate:
    """One fixed-window/order candidate after inner rolling-origin selection."""

    order: int
    window: int
    horizon: int
    lambda_: float
    smoothness_: float
    objective_: float
    n_origins_: int
    n_scored_: int
    inner_origins_: tuple[int, ...]
    search_: StationaryPointSearchResult


@dataclass(frozen=True)
class ForecastOptimalSelection:
    """Best fixed-window/order candidate and all candidates evaluated."""

    best_: ForecastOptimalCandidate
    candidates_: tuple[ForecastOptimalCandidate, ...]
    common_inner_origins_: tuple[int, ...]


def _common_fixed_window_splits(
    n_obs: int,
    windows: tuple[int, ...],
    horizon: int,
    step: int,
    max_origins: int | None,
) -> dict[int, list[RollingOriginSplit]]:
    """Create candidate-window splits on exactly the same validation origins."""

    valid_windows = tuple(sorted({w for w in windows if w + horizon <= n_obs}))
    if not valid_windows:
        return {}

    first_origin = max(valid_windows)
    origins = list(range(first_origin, n_obs - horizon + 1, step))
    if max_origins is not None:
        keep = int(max_origins)
        if keep <= 0:
            raise ValueError("max_origins must be positive when provided.")
        origins = origins[-keep:]

    return {
        window: [
            RollingOriginSplit(
                train=slice(origin - window, origin),
                validation=slice(origin, origin + horizon),
            )
            for origin in origins
        ]
        for window in valid_windows
    }


def select_fixed_window_pure_smoothness(
    y_history,
    *,
    orders=(1, 2, 3),
    windows=(20, 40, 60),
    horizon: int = 1,
    step: int = 1,
    max_origins: int | None = None,
    min_origins: int = 2,
    log_bounds: tuple[float, float] = (-12.0, 20.0),
    n_grid: int = 257,
) -> ForecastOptimalSelection:
    """Select order, fixed window, and lambda by inner rolling-origin forecast loss.

    This is an inner selector at one outer forecast origin. The caller must pass
    only data available at that outer origin.

    All candidate windows are scored on the same validation origins. Candidate
    window L changes only the amount of past data supplied to the fit, not the
    future blocks on which competing windows are compared.

    For each fixed window L, all inner fits contain exactly L observations. Thus
    for fixed order d a common lambda corresponds to one common normalized
    smoothness value across those inner origins.
    """

    y_history = as_1d_float_array(y_history)
    horizon = int(horizon)
    step = int(step)
    min_origins = int(min_origins)

    if y_history.size == 0:
        raise ValueError("y_history must not be empty.")
    if horizon <= 0 or step <= 0:
        raise ValueError("horizon and step must be positive.")
    if min_origins <= 0:
        raise ValueError("min_origins must be positive.")

    orders = tuple(int(order) for order in orders)
    windows = tuple(int(window) for window in windows)
    if not orders or not windows:
        raise ValueError("orders and windows must be non-empty.")
    if any(order < 0 for order in orders):
        raise ValueError("orders must be nonnegative.")
    if any(window <= 0 for window in windows):
        raise ValueError("windows must be positive.")

    split_map = _common_fixed_window_splits(
        n_obs=y_history.size,
        windows=windows,
        horizon=horizon,
        step=step,
        max_origins=max_origins,
    )
    if not split_map:
        raise ValueError("No candidate window leaves room for the forecast horizon.")

    common_origins = tuple(
        int(split.validation.start)
        for split in next(iter(split_map.values()))
    )
    if len(common_origins) < min_origins:
        raise ValueError(
            "No valid candidate produced enough common inner rolling origins. "
            "Provide more history, shorter windows/horizon, a smaller step, "
            "or a smaller min_origins."
        )

    candidates: list[ForecastOptimalCandidate] = []

    for window, splits in split_map.items():
        for order in orders:
            if order > window:
                continue

            def value_grad_hess(lambda_value: float):
                result = rolling_pure_forecast_loss_derivatives(
                    y_history,
                    splits,
                    order=order,
                    lambda_=lambda_value,
                )
                return result.value, result.first, result.second

            search = find_stationary_points_log_lambda(
                value_grad_hess,
                log_bounds=log_bounds,
                n_grid=n_grid,
            )
            pooled = rolling_pure_forecast_loss_derivatives(
                y_history,
                splits,
                order=order,
                lambda_=search.best_lambda_,
            )
            smoothness = lambda_to_smoothness(
                search.best_lambda_,
                n_obs=window,
                order=order,
            )
            candidates.append(
                ForecastOptimalCandidate(
                    order=order,
                    window=window,
                    horizon=horizon,
                    lambda_=search.best_lambda_,
                    smoothness_=smoothness,
                    objective_=pooled.value,
                    n_origins_=pooled.n_origins,
                    n_scored_=pooled.n_scored,
                    inner_origins_=common_origins,
                    search_=search,
                )
            )

    if not candidates:
        raise ValueError("No valid order/window candidate could be evaluated.")

    best = min(candidates, key=lambda candidate: candidate.objective_)
    return ForecastOptimalSelection(
        best_=best,
        candidates_=tuple(candidates),
        common_inner_origins_=common_origins,
    )
