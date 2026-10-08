"""Selección cronológica directa en dos validaciones.

Validación 1: recuperar todos los mínimos locales de ECM para cada orden d.
Validación 2: refit tras validación 1 y seleccionar (d, S) por ECM.
Pronóstico: refit en la última ventana anterior a la prueba, con (d, S)
invariables. La prueba nunca se utiliza para seleccionar hiperparámetros.

Esta ruta es exploratoria y no altera los experimentos congelados.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

import trend_estimation as td
from experiments.smoothness_cv.live_lab import _candidates


@dataclass
class TwoStageResult:
    candidates: pd.DataFrame
    surfaces: pd.DataFrame
    selected_order: int
    selected_s: float
    selected_lambda: float
    selected_val1_mse: float
    selected_val2_mse: float
    selected_val2_rmse: float
    method: str
    trend: np.ndarray
    forecast: np.ndarray
    evaluation_trend: np.ndarray
    evaluation_forecast: np.ndarray
    train_start: int
    val1_start: int
    val1_end: int
    val2_end: int
    pretest_end: int
    test_end: int
    forecast_start: int
    forecast_end: int
    future_horizon: int
    window: int
    horizon: int


def run_two_stage_lab(
    observed,
    *,
    orders: tuple[int, ...] = (1, 2, 3, 4),
    window: int = 60,
    horizon: int = 5,
    test_size: int = 5,
    future_horizon: int = 5,
    candidate_spacing: float = 0.02,
    grid_points: int = 61,
    search_depth: int = 5,
) -> TwoStageResult:
    """Select a pure penalized trend only from Validation 1 and Validation 2.

    All orders share the same chronological blocks:
      fit1=[a, b), val1=[b, c), val2=[c, e), test=[e, n).
    For each candidate from the val1 forecast-loss minima, refit on the last
    window observations ending at c and forecast val2. Minimize val2 MSE
    over every (order, candidate). Forecast the reserved test from e without
    retuning. Then refit the same (order, S) on the entire available series to
    forecast observations beyond the last observed datum.
    """
    y = np.asarray(observed, dtype=float)
    if y.ndim != 1 or len(y) == 0 or not np.all(np.isfinite(y)):
        raise ValueError("La serie debe contener observaciones numéricas finitas.")
    if not orders or len(set(orders)) != len(orders):
        raise ValueError("Seleccione órdenes enteros distintos.")
    if any(type(d) is not int or not 1 <= d <= 4 for d in orders):
        raise ValueError("Los órdenes admitidos son 1, 2, 3 y 4.")
    if window <= max(orders) or horizon < 1 or test_size < 1 or future_horizon < 1:
        raise ValueError("Se requiere L > d, horizontes positivos y prueba no vacía.")
    if not 0 < candidate_spacing < 1 or grid_points < 5 or search_depth < 0:
        raise ValueError("Verifique la separación de mínimos y la búsqueda numérica.")
    if len(y) < window + 2 * horizon + test_size:
        raise ValueError(
            "Se requieren al menos L + 2h + observaciones de prueba."
        )

    pretest_end = len(y) - test_size
    val2_end = pretest_end
    val1_end = val2_end - horizon
    val1_start = val1_end - horizon
    train_start = val1_start - window
    val1_split = td.RollingOriginSplit(
        train=slice(train_start, val1_start),
        validation=slice(val1_start, val1_end),
    )

    surfaces = []
    candidates = []
    for order in sorted(orders):
        prepared = td.prepare_rolling_pure_forecast_objective(
            y[:pretest_end], [val1_split], order=order
        )
        found = _candidates(
            prepared, order, window,
            spacing=candidate_spacing, depth=search_depth,
        )
        for smoothness in np.linspace(0.0, 1.0, grid_points):
            smoothness = float(smoothness)
            lam = td.smoothness_to_lambda(smoothness, window, order)
            surfaces.append({
                "d": order,
                "smoothness": smoothness,
                "val1_mse": float(prepared.evaluate(lam).value),
            })

        # La validación 2 utiliza un ajuste nuevo que incluye la validación 1.
        fit_values = y[val1_end-window:val1_end]
        future = y[val1_end:val2_end]
        for candidate in found:
            s = float(candidate["smoothness"])
            fit = td.PurePenalizedTrend(order=order, smoothness=s).fit(fit_values)
            forecast = np.asarray(fit.forecast(horizon), dtype=float)
            if forecast.shape != future.shape or not np.all(np.isfinite(forecast)):
                val2_mse = float("inf")
            else:
                # El cálculo escalado evita desbordamiento intermedio.
                diff = future - forecast
                scale = float(np.max(np.abs(diff)))
                val2_mse = float(
                    (scale * scale) * np.mean((diff / scale)**2)
                ) if scale else 0.0
            candidates.append({
                "method": "Mínimos cuadrados penalizados",
                "d": order,
                "smoothness": s,
                "lambda": float(candidate["lambda"]),
                "val1_mse": float(candidate["val1_mse"]),
                "val2_mse": val2_mse,
                "val2_rmse": float(np.sqrt(val2_mse)),
                "source": str(candidate["source"]),
            })

    table = pd.DataFrame(candidates)
    if table.empty or not np.isfinite(table["val2_mse"]).any():
        raise ValueError(
            "Ningún mínimo local produjo un pronóstico finito en validación 2."
        )
    # Un desempate fijo favorece menor error en val1 y luego menor complejidad.
    table = table.sort_values(
        ["val2_mse", "val1_mse", "d", "smoothness"],
        ascending=True, kind="mergesort",
    ).reset_index(drop=True)
    table.insert(0, "rank", np.arange(1, len(table) + 1))
    winner = table.iloc[0]
    selected_s, selected_order = float(winner["smoothness"]), int(winner["d"])

    # La prueba no interviene en los pasos anteriores de selección.
    evaluation = td.PurePenalizedTrend(
        order=selected_order, smoothness=selected_s
    ).fit(y[pretest_end-window:pretest_end])
    backtest = np.asarray(evaluation.forecast(test_size), dtype=float)

    # El pronóstico operativo comienza DESPUÉS del último dato real, no antes
    # de la prueba reservada. Los hiperparámetros no vuelven a optimizarse.
    final = td.PurePenalizedTrend(
        order=selected_order, smoothness=selected_s
    ).fit(y[-window:])
    future = np.asarray(final.forecast(future_horizon), dtype=float)
    return TwoStageResult(
        candidates=table,
        surfaces=pd.DataFrame(surfaces),
        selected_order=selected_order,
        selected_s=selected_s,
        selected_lambda=float(final.lambda_),
        selected_val1_mse=float(winner["val1_mse"]),
        selected_val2_mse=float(winner["val2_mse"]),
        selected_val2_rmse=float(winner["val2_rmse"]),
        method=str(winner["method"]),
        trend=np.asarray(final.trend_, dtype=float).copy(),
        forecast=future,
        evaluation_trend=np.asarray(evaluation.trend_, dtype=float).copy(),
        evaluation_forecast=backtest,
        train_start=len(y)-window,
        val1_start=val1_start, val1_end=val1_end, val2_end=val2_end,
        pretest_end=pretest_end, test_end=len(y),
        forecast_start=len(y), forecast_end=len(y)+future_horizon,
        future_horizon=future_horizon,
        window=window, horizon=horizon,
    )
