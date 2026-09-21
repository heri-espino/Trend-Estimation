from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from trend_estimation.benchmarks.naive import no_change_forecast
from trend_estimation.models.pure_penalized import PurePenalizedTrend
from trend_estimation.selection.forecast_optimal import (
    ForecastOptimalSelection,
    select_fixed_window_pure_smoothness,
)
from trend_estimation.utils.arrays import as_1d_float_array
from trend_estimation.validation.rolling_origin import rolling_origin_splits


@dataclass(frozen=True)
class NestedForecastRecord:
    """One untouched outer forecast and the inner-selected configuration."""

    origin: int
    validation_start: int
    validation_stop: int
    horizon: int
    selected_order: int
    selected_window: int
    selected_lambda: float
    selected_smoothness: float
    inner_objective: float
    observed: np.ndarray
    prediction: np.ndarray
    benchmark_prediction: np.ndarray
    inner_selection: ForecastOptimalSelection


@dataclass(frozen=True)
class NestedRollingForecastResult:
    """Collection of chronological outer forecasts and pooled level metrics."""

    records: tuple[NestedForecastRecord, ...]
    observed: np.ndarray
    prediction: np.ndarray
    benchmark_prediction: np.ndarray
    mse: float
    rmse: float
    benchmark_mse: float
    benchmark_rmse: float
    relative_rmsfe: float


def nested_rolling_pure_forecast(
    y,
    *,
    outer_initial_train: int,
    horizon: int,
    outer_step: int = 1,
    orders=(1, 2, 3),
    windows=(20, 40, 60),
    inner_step: int = 1,
    max_inner_origins: int | None = None,
    min_inner_origins: int = 2,
    log_bounds: tuple[float, float] = (-12.0, 20.0),
    n_grid: int = 257,
) -> NestedRollingForecastResult:
    """Run leakage-free nested rolling evaluation for the pure smoother.

    At each outer origin T:
    1. expose only y[:T] to the inner selector;
    2. select (order, window, lambda) by fixed-window inner rolling origins;
    3. refit on the last selected-window observations available at T;
    4. forecast the untouched outer future block;
    5. score both the smoother and a no-change benchmark.

    The function evaluates a fixed forecast horizon. Experiments that study
    multiple horizons should call it separately for each h.
    """

    y = as_1d_float_array(y)
    outer_initial_train = int(outer_initial_train)
    horizon = int(horizon)
    outer_step = int(outer_step)

    if y.size == 0:
        raise ValueError("y must not be empty.")
    if outer_initial_train <= 0 or horizon <= 0 or outer_step <= 0:
        raise ValueError(
            "outer_initial_train, horizon, and outer_step must be positive."
        )

    outer_splits = rolling_origin_splits(
        y.size,
        initial_train=outer_initial_train,
        horizon=horizon,
        step=outer_step,
        expanding=True,
    )

    records: list[NestedForecastRecord] = []

    for split in outer_splits:
        origin = int(split.train.stop)
        # This is the central no-look-ahead invariant.
        history = y[:origin].copy()
        future = y[split.validation].copy()

        selection = select_fixed_window_pure_smoothness(
            history,
            orders=orders,
            windows=windows,
            horizon=horizon,
            step=inner_step,
            max_origins=max_inner_origins,
            min_origins=min_inner_origins,
            log_bounds=log_bounds,
            n_grid=n_grid,
        )
        best = selection.best_

        fit_history = history[-best.window :]
        model = PurePenalizedTrend(
            order=best.order,
            smoothness=None,
            lambda_=best.lambda_,
        ).fit(fit_history)

        prediction = model.forecast(future.size)
        benchmark = no_change_forecast(history, future.size)

        records.append(
            NestedForecastRecord(
                origin=origin,
                validation_start=int(split.validation.start),
                validation_stop=int(split.validation.stop),
                horizon=int(future.size),
                selected_order=best.order,
                selected_window=best.window,
                selected_lambda=best.lambda_,
                selected_smoothness=best.smoothness_,
                inner_objective=best.objective_,
                observed=future,
                prediction=np.asarray(prediction, dtype=float),
                benchmark_prediction=np.asarray(benchmark, dtype=float),
                inner_selection=selection,
            )
        )

    if not records:
        raise ValueError("No outer rolling-origin forecasts could be produced.")

    observed = np.concatenate([record.observed for record in records])
    prediction = np.concatenate([record.prediction for record in records])
    benchmark_prediction = np.concatenate(
        [record.benchmark_prediction for record in records]
    )

    error = observed - prediction
    benchmark_error = observed - benchmark_prediction
    mse = float(np.mean(error**2))
    benchmark_mse = float(np.mean(benchmark_error**2))
    rmse = float(np.sqrt(mse))
    benchmark_rmse = float(np.sqrt(benchmark_mse))

    if benchmark_rmse == 0.0:
        relative_rmsfe = 0.0 if rmse == 0.0 else float("inf")
    else:
        relative_rmsfe = float(rmse / benchmark_rmse)

    return NestedRollingForecastResult(
        records=tuple(records),
        observed=observed,
        prediction=prediction,
        benchmark_prediction=benchmark_prediction,
        mse=mse,
        rmse=rmse,
        benchmark_mse=benchmark_mse,
        benchmark_rmse=benchmark_rmse,
        relative_rmsfe=relative_rmsfe,
    )
