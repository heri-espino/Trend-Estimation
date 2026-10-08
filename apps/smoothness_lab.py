"""Laboratorio de órdenes, mínimos locales, ramas y reglas de suavidad.

Modo principal: seguimiento histórico de ramas con matrices V.
Caso particular: comparación directa en dos bloques de validación.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from experiments.smoothness_cv.live_lab import (
    make_synthetic,
    smoothing_matrix,
    transform_observations,
)
from experiments.smoothness_cv.two_stage_lab import run_two_stage_lab
from experiments.smoothness_cv.branch_rule_lab import (
    run_branch_lab, RULE_SPECS, inspect_method_val1_curves,
)


TRANSFORMACIONES = {
    "Nivel original": ("Level", "Valor observado (unidades originales)"),
    "Logaritmo del nivel": ("Log level", "Logaritmo del valor observado"),
    "Índice con base 100": ("Indexed to 100", "Índice (base 100)"),
    "Rendimiento simple": ("Simple return", "Rendimiento simple por periodo"),
    "Rendimiento logarítmico": ("Log return", "Log-rendimiento por periodo"),
}
FUNCIONES = {
    "Tendencia lineal y componente cíclico": "10 + 0.02*t + sin(t/12)",
    "Cambio de pendiente": "10 + 0.015*t + where(t>100, 0.06*(t-100), 0)",
    "Tendencia no lineal": "10 + 0.00015*(t-120)**2 + 0.8*sin(t/18)",
    "Cambio de nivel": "10 + 0.015*t + where(t>110, 3, 0)",
    "Función personalizada": "10 + 0.02*t + sin(t/12)",
}
RUIDOS = {
    "Normal": "Gaussian", "Laplace": "Laplace",
    "t de Student (5 grados de libertad)": "Student-t (df=5)",
    "Heterocedástico": "Heteroskedastic",
}
PERIODOS = {
    "6 meses": "6mo", "1 año": "1y", "2 años": "2y",
    "5 años": "5y", "10 años": "10y",
}
FRECUENCIAS = {"Diaria": "1d", "Semanal": "1wk", "Mensual": "1mo"}
VARIABLES = {
    "Cierre ajustado": "Close", "Apertura": "Open",
    "Máximo": "High", "Mínimo": "Low", "Volumen": "Volume",
}
COLORES_D = {1: "#0072B2", 2: "#D55E00", 3: "#009E73", 4: "#8A57A1"}
ETIQUETAS = {
    "rank": "Posición por ECM de validación 2",
    "method": "Método de estimación",
    "d": "Orden de diferencias, d",
    "smoothness": "Suavidad normalizada, S",
    "lambda": "Penalización, λ",
    "val1_mse": "ECM de validación 1",
    "val2_mse": "ECM de validación 2",
    "val2_rmse": "RECM de validación 2",
    "source": "Procedencia del candidato",
}
FUENTES = {
    "interior": "Mínimo interior", "S=0": "Extremo S = 0",
    "S=1": "Extremo S = 1", "boundary_fallback": "Extremo del dominio",
}


@st.cache_data(ttl=3600, show_spinner=False)
def yahoo_history(symbols: tuple[str, ...], period: str, interval: str):
    import yfinance as yf

    data = yf.download(
        tickers=list(symbols), period=period, interval=interval,
        auto_adjust=True, progress=False, threads=False, group_by="ticker",
    )
    if data.empty:
        raise ValueError("La consulta no devolvió observaciones.")
    return data


@st.cache_data(show_spinner=False, max_entries=40)
def analyze(values: tuple[float, ...], *, mode: str = "ramas", **kwargs):
    if mode == "ramas":
        return run_branch_lab(np.asarray(values), **kwargs)
    return run_two_stage_lab(np.asarray(values), **kwargs)


def _market_frame(data: pd.DataFrame, symbol: str, field: str) -> pd.DataFrame:
    if isinstance(data.columns, pd.MultiIndex):
        if symbol in data.columns.get_level_values(0):
            values = data[symbol][field]
        elif symbol in data.columns.get_level_values(1):
            values = data[field][symbol]
        else:
            raise ValueError(f"No se encontraron valores de {symbol}.")
    else:
        values = data[field]
    values = pd.to_numeric(values, errors="coerce").dropna()
    if values.empty:
        raise ValueError("No existen observaciones numéricas válidas.")
    return pd.DataFrame({
        "date": values.index, "observed": values.to_numpy(dtype=float),
    })


def _table(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.rename(columns=ETIQUETAS).copy()
    source = ETIQUETAS["source"]
    if source in out:
        out[source] = out[source].replace(FUENTES)
    return out


def _axis(frame: pd.DataFrame):
    if "date" in frame.columns:
        return pd.to_datetime(frame["date"]).tolist(), "Fecha"
    return np.arange(1, len(frame) + 1), "Número de observación"


def _style(fig: go.Figure, title: str, xaxis: str, yaxis: str,
           height: int = 455) -> go.Figure:
    fig.update_layout(
        template="plotly_white", title={"text": title, "font": {"size": 18}},
        height=height, margin={"l": 45, "r": 30, "t": 70, "b": 75},
        xaxis_title=xaxis, yaxis_title=yaxis,
        font={"size": 12}, hovermode="x unified",
        legend={"orientation": "h", "y": -0.27, "x": 0, "title_text": ""},
    )
    fig.update_xaxes(showgrid=True, gridcolor="#EBEBEB")
    fig.update_yaxes(showgrid=True, gridcolor="#EBEBEB")
    return fig


def _timeline(result) -> go.Figure:
    """Cada fila muestra el intervalo exacto utilizado en el experimento."""
    L = result.window
    a, b, c, e, n, f = (
        result.val1_start, result.val1_end, result.val2_end,
        result.pretest_end, result.test_end, result.forecast_end,
    )
    spans = [
        (4, a-L, a, "Ajuste inicial", "#737373"),
        (4, a, b, "Validación 1", COLORES_D[1]),
        (3, b-L, b, "Nuevo ajuste", "#737373"),
        (3, b, c, "Validación 2", COLORES_D[3]),
        (2, e-L, e, "Ajuste retrospectivo", "#737373"),
        (2, e, n, "Prueba reservada", COLORES_D[2]),
        (1, n-L, n, "Ajuste con todos los datos", "#737373"),
        (1, n, f, "Pronóstico futuro", COLORES_D[3]),
    ]
    fig = go.Figure()
    for row, left, right, label, color in spans:
        fig.add_trace(go.Bar(
            x=[right-left], y=[row], base=[left], orientation="h", width=0.44,
            marker={"color": color}, name=label,
            customdata=[[left+1, right]],
            hovertemplate=(
                label + "<br>Observaciones %{customdata[0]} a "
                "%{customdata[1]}<extra></extra>"
            ),
        ))
    _style(
        fig, "Separación cronológica de entrenamiento, validación y prueba",
        "Número de observación", "Etapa", height=355,
    )
    fig.update_layout(barmode="overlay", hovermode="closest")
    fig.update_yaxes(
        tickmode="array", tickvals=[1, 2, 3, 4],
        ticktext=["Pronóstico operativo", "Evaluación en prueba",
                  "Selección en validación 2", "Búsqueda en validación 1"],
        range=[0.5, 4.5], showgrid=False,
    )
    fig.update_xaxes(range=[0, f+1])
    return fig


def _val1_figure(result, order: int) -> go.Figure:
    curve = result.surfaces.loc[result.surfaces["d"].eq(order)]
    minima = result.candidates.loc[result.candidates["d"].eq(order)]
    selected = minima.loc[minima["rank"].eq(1)]
    raw_minima = minima.loc[minima["source"].ne("regla_aplicada")]
    fig = go.Figure()
    fig.add_scatter(
        x=curve["smoothness"], y=curve["val1_mse"],
        mode="lines", name="Superficie del ECM de validación 1",
        line={"color": COLORES_D[order], "width": 2.4},
    )
    fig.add_scatter(
        x=raw_minima["smoothness"], y=raw_minima["val1_mse"],
        mode="markers", name="Mínimos de la función original ECM(S)",
        marker={"symbol": "diamond", "color": "#3F3F46", "size": 9},
        hovertemplate="S = %{x:.4f}<br>ECM = %{y:.6g}<extra></extra>",
    )
    if not selected.empty:
        fig.add_scatter(
            x=selected["smoothness"], y=selected["val1_mse"],
            mode="markers",
            name=("Suavidad aplicada de la regla ganadora"
                  if hasattr(result, "selected_rule")
                  else "Candidato seleccionado en validación 2"),
            marker={"symbol": "star", "size": 17, "color": COLORES_D[2],
                    "line": {"color": "white", "width": 1}},
        )
    _style(
        fig, f"Orden de diferencias d = {order}",
        "Suavidad normalizada, S (0 a 1)",
        "ECM de validación 1 (unidades transformadas al cuadrado)",
        height=370,
    )
    fig.update_xaxes(range=[0, 1])
    return fig



def _val1_method_figure(
    curves: pd.DataFrame,
    minima: pd.DataFrame,
    *,
    order: int,
    rule: str,
    selected_branch: str | None = None,
    selected_input_s: float | None = None,
) -> go.Figure:
    """Plot E1(phi_r(V_j, s)) for each method-specific tracked branch."""
    fig = go.Figure()
    branches = curves["rama"].drop_duplicates().tolist()
    colors = ["#0072B2", "#D55E00", "#009E73", "#8A57A1",
              "#B88700", "#555555", "#CC79A7", "#56B4E9"]
    for i, branch in enumerate(branches):
        group = curves.loc[curves["rama"].eq(branch)].sort_values("s_candidato")
        focus = (branch == selected_branch)
        color = colors[i % len(colors)]
        fig.add_scatter(
            x=group["s_candidato"], y=group["val1_mse"],
            mode="lines", name=f"Rama {branch}: ECM del método",
            line={"color": color, "width": 3 if focus else 1.8},
            opacity=1 if focus else 0.68,
            customdata=group[["s_aplicado"]].to_numpy(),
            hovertemplate=(
                "S candidata = %{x:.4f}<br>S aplicada = %{customdata[0]:.4f}"
                "<br>ECM de V1 = %{y:.6g}<extra></extra>"
            ),
        )
        local = minima.loc[minima["rama"].eq(branch)]
        stable = local.loc[~local["objetivo_plano"]]
        if not stable.empty:
            fig.add_scatter(
                x=stable["s_candidato"], y=stable["val1_mse"],
                mode="markers", name=f"Rama {branch}: mínimos de V1",
                marker={"color": color, "symbol": "diamond", "size": 9},
                customdata=stable[["s_aplicado"]].to_numpy(),
                hovertemplate=(
                    "S candidata = %{x:.4f}<br>S aplicada = %{customdata[0]:.4f}"
                    "<br>ECM de V1 = %{y:.6g}<extra></extra>"
                ),
            )
    if selected_branch in branches and selected_input_s is not None:
        points = curves.loc[curves["rama"].eq(selected_branch)]
        if not points.empty:
            xi = points["s_candidato"].to_numpy(float)
            yi = points["val1_mse"].to_numpy(float)
            fig.add_scatter(
                x=[selected_input_s],
                y=[float(np.interp(selected_input_s, xi, yi))],
                mode="markers", name="S candidata utilizada en la prueba",
                marker={"symbol": "star", "color": "#222222", "size": 18},
            )
    _style(
        fig,
        f"ECM de V1 por método — orden d = {order} · "
        f"{REGLAS_ES.get(rule, rule)}",
        "Suavidad candidata, s (antes de aplicar la regla)",
        "ECM de validación 1 (unidades al cuadrado)",
        height=490,
    )
    fig.update_xaxes(range=[0, 1])
    return fig


def _val2_figure(result) -> go.Figure:
    fig = go.Figure()
    table = result.candidates
    for order, chunk in table.groupby("d", sort=True):
        valid = chunk.loc[np.isfinite(chunk["val2_mse"])]
        fig.add_scatter(
            x=valid["smoothness"], y=valid["val2_mse"], mode="markers",
            name=f"Orden d = {order}",
            marker={"color": COLORES_D[int(order)], "size": 10, "opacity": 0.82},
            customdata=np.c_[valid["val1_mse"], valid["rank"]],
            hovertemplate=(
                "S = %{x:.4f}<br>ECM validación 2 = %{y:.6g}"
                "<br>ECM validación 1 = %{customdata[0]:.6g}"
                "<br>Posición = %{customdata[1]:.0f}<extra></extra>"
            ),
        )
    winner = table.iloc[0]
    fig.add_scatter(
        x=[winner["smoothness"]], y=[winner["val2_mse"]],
        mode="markers", name="Modelo seleccionado",
        marker={"symbol": "star", "size": 19, "color": "#222222",
                "line": {"color": "white", "width": 1}},
    )
    _style(
        fig, "Comparación de candidatos por error de validación 2",
        "Suavidad normalizada, S",
        "ECM de validación 2 (unidades transformadas al cuadrado)",
        height=480,
    )
    fig.update_xaxes(range=[0, 1])
    return fig


def _future_axis(frame: pd.DataFrame, length: int):
    """Future labels; dates are approximations, not market calendars."""
    if "date" not in frame.columns:
        return np.arange(len(frame)+1, len(frame)+length+1)
    dates = pd.to_datetime(frame["date"])
    tail = pd.DatetimeIndex(dates.iloc[-min(14, len(dates)):])
    try:
        frequency = pd.infer_freq(tail)
    except (TypeError, ValueError):
        frequency = None
    if frequency:
        return pd.date_range(start=tail[-1], periods=length+1, freq=frequency)[1:]
    delta = pd.Series(tail).diff().dropna().median()
    if pd.isna(delta) or delta <= pd.Timedelta(0):
        delta = pd.Timedelta(days=1)
    if delta <= pd.Timedelta(days=1) and all(d.weekday() < 5 for d in tail):
        return pd.bdate_range(start=tail[-1], periods=length+1)[1:]
    return [tail[-1] + i*delta for i in range(1, length+1)]


def _forecast_figure(frame: pd.DataFrame, result, unidad: str, *,
                     reveal: bool, truth: bool) -> go.Figure:
    x, label_x = _axis(frame)
    y = frame["observed"].to_numpy(dtype=float)
    a, n = result.train_start, result.test_end
    x_futuro = _future_axis(frame, result.future_horizon)
    fig = go.Figure()
    fig.add_scatter(
        x=x, y=y, mode="lines", name="Serie observada (todos los datos disponibles)",
        line={"color": "#656565", "width": 1.75},
    )
    if truth and "latent" in frame:
        fig.add_scatter(
            x=x, y=frame["latent"].to_numpy(dtype=float),
            mode="lines", name="Componente verdadera de la simulación",
            line={"color": "#9C6BB3", "dash": "dot", "width": 1.8},
        )
    fig.add_scatter(
        x=x[a:n], y=result.trend,
        mode="lines", name=f"Tendencia final reajustada (d = {result.selected_order})",
        line={"color": "#D55E00", "width": 3},
    )
    fig.add_scatter(
        x=[x[-1]] + list(x_futuro),
        y=[float(result.trend[-1])] + list(result.forecast),
        mode="lines+markers", name=f"Pronóstico futuro con S = {result.selected_s:.4f}",
        marker={"size": 8},
        line={"color": "#D55E00", "width": 2.8, "dash": "dash"},
    )
    if reveal:
        e = result.pretest_end
        fig.add_scatter(
            x=x[e:n], y=y[e:n], mode="markers",
            name="Valores reales reservados de prueba",
            marker={"color": "#222222", "size": 9, "symbol": "circle-open"},
        )
        fig.add_scatter(
            x=x[e:n], y=result.evaluation_forecast,
            mode="lines+markers", name="Pronóstico retrospectivo para prueba",
            marker={"size": 6},
            line={"color": "#0072B2", "width": 2, "dash": "dot"},
        )
    if len(x_futuro):
        fig.add_vrect(
            x0=x_futuro[0], x1=x_futuro[-1],
            fillcolor="#E5E7EB", opacity=0.5, line_width=0, layer="below",
        )
        fig.add_vline(x=x[-1], line_dash="dot", line_color="#858585")
    return _style(
        fig, "Tendencia reajustada y pronóstico posterior al último dato real",
        label_x, unidad, height=540,
    )



def _test_forecast_figure(
    frame: pd.DataFrame, result, unidad: str, *, truth: bool = False
) -> go.Figure:
    """The test prediction is fixed at the pretest origin, before observing test y.

    Only evaluation_trend/evaluation_forecast are used for the orange trend.
    The final full-data trend is intentionally excluded from this backtest plot.
    """
    x, x_title = _axis(frame)
    y = frame["observed"].to_numpy(dtype=float)
    cutoff, end = int(result.pretest_end), int(result.test_end)
    L = int(result.window)
    left = max(0, cutoff-min(L, 45))
    historical_x = x[left:cutoff]
    historical_trend = np.asarray(result.evaluation_trend, dtype=float)[
        left-(cutoff-L):
    ]
    forecast = np.asarray(result.evaluation_forecast, dtype=float)
    if len(forecast) != end-cutoff:
        raise ValueError("Pronóstico de prueba y periodo reservado desalineados.")
    fig = go.Figure()
    fig.add_scatter(
        x=historical_x, y=y[left:cutoff],
        name="Observaciones conocidas antes de la prueba",
        mode="lines+markers", marker={"size": 4},
        line={"color": "#777777", "width": 1.7},
    )
    fig.add_scatter(
        x=historical_x, y=historical_trend,
        name="Tendencia estimada antes del test",
        mode="lines", line={"color": "#D55E00", "width": 2.6},
    )
    fig.add_scatter(
        x=[x[cutoff-1]]+list(x[cutoff:end]),
        y=[float(historical_trend[-1])]+list(forecast),
        name="Tendencia pronosticada sin observar el test",
        mode="lines+markers", marker={"size": 7},
        line={"color": "#D55E00", "width": 3, "dash": "dash"},
    )
    fig.add_scatter(
        x=x[cutoff:end], y=y[cutoff:end],
        name="Serie real del test reservado",
        mode="lines+markers", marker={"size": 9},
        line={"color": "#202020", "width": 2.5},
    )
    if truth and "latent" in frame:
        latent = frame["latent"].to_numpy(float)
        fig.add_scatter(
            x=x[cutoff:end], y=latent[cutoff:end],
            name="Tendencia verdadera sintética en test",
            mode="lines", line={"color": "#8A57A1", "dash": "dot"},
        )
    _style(
        fig, "Pronóstico de tendencia frente a la serie real — prueba reservada",
        x_title, unidad, height=515,
    )
    fig.add_shape(
        type="line", x0=x[cutoff-1], x1=x[cutoff-1],
        yref="paper", y0=0, y1=1,
        line={"color": "#999999", "dash": "dot", "width": 1.5},
    )
    return fig


def _matrix_figure(H: np.ndarray) -> go.Figure:
    max_abs = float(np.max(np.abs(H)))
    fig = go.Figure(go.Heatmap(
        x=np.arange(1, len(H)+1), y=np.arange(1, len(H)+1),
        z=H, colorscale="RdBu", zmin=-max_abs, zmax=max_abs,
        colorbar={"title": {"text": "Peso Hᵢⱼ"}},
        hovertemplate=(
            "Tendencia estimada i = %{y}<br>Observación j = %{x}"
            "<br>Peso Hᵢⱼ = %{z:.5f}<extra></extra>"
        ),
    ))
    _style(
        fig, "Matriz de suavizamiento del modelo seleccionado",
        "Índice de observación j", "Índice de tendencia estimada i",
        height=530,
    )
    fig.update_yaxes(autorange="reversed", scaleanchor="x", scaleratio=1)
    return fig



REGLAS_ES = {
    "last": "Último mínimo (referencia polinómica)",
    "mean_k3": "Media de los últimos 3 mínimos",
    "mean_k5": "Media de los últimos 5 mínimos",
    "median_k3": "Mediana de los últimos 3 mínimos",
    "median_k5": "Mediana de los últimos 5 mínimos",
    "recency_hl3": "Media ponderada por recencia (semivida 3)",
    "recency_hl5": "Media ponderada por recencia (semivida 5)",
    "recency_hl10": "Media ponderada por recencia (semivida 10)",
    "val2_weighted": "Ponderación por ECM histórico de validación 2",
    "recency_val2_hl3": "Recencia y error histórico (semivida 3)",
    "recency_val2_hl5": "Recencia y error histórico (semivida 5)",
    "recency_val2_hl10": "Recencia y error histórico (semivida 10)",
    "linear_k3": "Extrapolación lineal (últimos 3 mínimos)",
    "linear_k5": "Extrapolación lineal (últimos 5 mínimos)",
    "linear_k10": "Extrapolación lineal (últimos 10 mínimos)",
    "ew_linear_hl3": "Regresión lineal ponderada (semivida 3)",
    "ew_linear_hl5": "Regresión lineal ponderada (semivida 5)",
    "delta_hl3": "Extrapolación de incrementos (semivida 3)",
    "delta_hl5": "Extrapolación de incrementos (semivida 5)",
}
ETIQUETAS_V = {
    "d": "Orden de diferencias, d",
    "rama": "Rama de mínimos locales",
    "regla": "Regla de suavidad",
    "origin": "Origen de validación",
    "val1_start": "Inicio de validación 1 (índice cero)",
    "val1_end": "Fin de validación 1 (exclusivo)",
    "val2_end": "Fin de validación 2 (exclusivo)",
    "s_minimo": "Argumento S del mínimo de ECM transformado",
    "s_aplicado": "Suavidad efectiva elegida por la regla",
    "s_sin_recortar": "S antes de restringir a [0, 1]",
    "objetivo_plano": "Objetivo transformado constante en S",
    "origen_minimo": "Identificación del mínimo bajo la regla",
    "val1_mse": "ECM de validación 1 con S de la regla",
    "val2_mse": "ECM de validación 2 con el mismo S",
    "val2_rmse": "RECM de validación 2 con el mismo S",
    "n_historial_disponible": "Orígenes terminados conocidos al elegir S",
    "n_historial_utilizado": "Mínimos históricos utilizados",
    "usa_s_actual": "Incluye el mínimo actual de validación 1",
    "fallback": "Utiliza regla alternativa por historia insuficiente",
    "acotado": "S restringido al intervalo [0, 1]",
    "n_origenes": "Orígenes evaluados",
    "n_validos": "Errores finitos",
    "ec_medio_val1": "ECM medio de validación 1",
    "ec_medio_val2": "ECM medio de validación 2",
    "re_cm_val2": "RECM agregado de validación 2",
    "soporte": "Proporción de orígenes evaluados",
    "elegible": "Admisible para selección",
}



def _branch_timeline(result) -> go.Figure:
    """Represent an actual completed historical pair and the final test origin."""
    history = result.branches.loc[
        result.branches["d"].eq(result.selected_order)
        & result.branches["regla"].eq(result.selected_rule)
    ].sort_values("origin")
    last = history.iloc[-1]
    a, b, c = (
        int(last["val1_start"]),
        int(last["val1_end"]), int(last["val2_end"]),
    )
    e, n, f = (
        result.pretest_end, result.test_end, result.forecast_end,
    )
    spans = [
        (4, a-result.window, a, "Ajuste histórico", "#737373"),
        (4, a, b, "Validación 1 histórica", COLORES_D[1]),
        (3, b-result.window, b, "Ajuste en origen de Val. 2", "#737373"),
        (3, b, c, "Validación 2 histórica", COLORES_D[3]),
        (2, e-result.horizon-result.window, e-result.horizon,
         "Ajuste previo a la Val. 1 final", "#737373"),
        (2, e-result.horizon, e, "Validación 1 final", COLORES_D[1]),
        (1, e-result.window, e, "Ajuste previo a la prueba", "#737373"),
        (1, e, n, "Prueba histórica real", COLORES_D[2]),
        (1, n, f, "Pronóstico futuro", COLORES_D[3]),
    ]
    fig = go.Figure()
    for row, left, right, label, color in spans:
        fig.add_trace(go.Bar(
            x=[right-left], y=[row], base=[left], orientation="h",
            name=label, width=0.42, marker={"color": color},
            customdata=[[left+1, right]],
            hovertemplate=(
                label + "<br>Observaciones %{customdata[0]} a "
                "%{customdata[1]}<extra></extra>"
            ),
        ))
    _style(
        fig, "Esquema cronológico: validaciones históricas y prueba reservada",
        "Número de observación",
        "Etapa del procedimiento", height=415,
    )
    fig.update_layout(barmode="overlay", hovermode="closest")
    fig.update_yaxes(
        tickmode="array", tickvals=[1, 2, 3, 4],
        ticktext=["Prueba y pronóstico futuro",
                  "Última validación 1",
                  "Última validación 2 histórica",
                  "Última validación 1 histórica"],
        range=[0.5, 4.5], showgrid=False,
    )
    fig.update_xaxes(range=[0, f+1])
    return fig


def _branch_figure(
    result, order: int, rule: str | None = None
) -> go.Figure:
    data = result.branches.loc[result.branches["d"].eq(order)]
    if rule is not None:
        data = data.loc[data["regla"].eq(rule)]
    fig = go.Figure()
    origenes = np.arange(1, int(result.branches["origin"].max())+1)
    for branch, group in data.groupby("rama", sort=True):
        group = group.set_index("origin").reindex(origenes)
        fig.add_scatter(
            x=origenes, y=group["s_aplicado"],
            name=f"Rama {branch}: S aplicada", mode="lines+markers",
            line={"width": 2}, marker={"size": 7},
            hovertemplate=(
                "Origen = %{x}<br>Suavidad mínima S = %{y:.4f}<extra></extra>"
            ),
        )
    _style(
        fig, f"Ramas según la regla fijada — orden d = {order}",
        "Número de origen cronológico", "Suavidad aplicada por la regla, S",
        height=430,
    )
    fig.update_yaxes(range=[-0.03, 1.03])
    return fig


def _historical_loss_figure(
    result, order: int, rule: str | None = None
) -> go.Figure:
    rows = result.historical_surfaces.query("d == @order")
    pivot = rows.pivot(index="origin", columns="smoothness", values="val1_mse")
    fig = go.Figure(go.Heatmap(
        x=pivot.columns, y=pivot.index, z=pivot.values,
        colorscale="Blues",
        colorbar={"title": {"text": "ECM"}},
        hovertemplate=(
            "Origen = %{y}<br>S = %{x:.3f}<br>ECM Val. 1 = %{z:.6g}"
            "<extra></extra>"
        ),
    ))
    local = result.branches.loc[result.branches["d"].eq(order)]
    if rule is not None:
        local = local.loc[local["regla"].eq(rule)]
    fig.add_scatter(
        x=local["s_aplicado"], y=local["origin"],
        mode="markers", name="Suavidades aplicadas por la regla",
        marker={"symbol": "circle-open", "size": 8,
                "line": {"width": 1.5, "color": "#C44E52"}},
    )
    _style(
        fig, f"ECM original y S aplicada por la regla — orden d = {order}",
        "Suavidad normalizada, S", "Origen de validación 1",
        height=445,
    )
    return fig


def _branch_rank_figure(result) -> go.Figure:
    ranked = result.summary.sort_values("ec_medio_val2")
    ranked = ranked.loc[np.isfinite(ranked["ec_medio_val2"])].head(35)
    fig = go.Figure()
    for d, group in ranked.groupby("d", sort=True):
        fig.add_scatter(
            x=group["soporte"],
            y=group["ec_medio_val2"], mode="markers",
            name=f"Orden d = {d}",
            marker={"size": 11, "color": COLORES_D[int(d)],
                    "opacity": 0.85},
            customdata=group[["rama", "regla", "n_origenes", "elegible"]].values,
            hovertemplate=(
                "Rama = %{customdata[0]}<br>Regla = %{customdata[1]}"
                "<br>Orígenes = %{customdata[2]}"
                "<br>Elegible = %{customdata[3]}"
                "<br>Soporte = %{x:.1%}<br>ECM medio = %{y:.6g}"
                "<extra></extra>"
            ),
        )
    winner = result.summary.loc[
        result.summary["d"].eq(result.selected_order)
        & result.summary["rama"].eq(result.selected_branch)
        & result.summary["regla"].eq(result.selected_rule)
    ].iloc[0]
    fig.add_scatter(
        x=[winner["soporte"]], y=[winner["ec_medio_val2"]],
        mode="markers", name="Configuración seleccionada",
        marker={"symbol": "star", "color": "#202020", "size": 19},
    )
    _style(
        fig, "Comparación histórica de ramas y reglas por ECM de validación 2",
        "Proporción de orígenes con rama evaluada",
        "ECM medio de validación 2 (unidades al cuadrado)", height=480,
    )
    return fig


def _v_figure(
    v: pd.DataFrame, d: int, branch: str, rule: str,
    *, others: pd.DataFrame | None = None,
) -> go.Figure:
    v = v.sort_values("origin")
    fig = go.Figure()
    if others is not None and not others.empty:
        for other_branch, group in others.groupby("rama", sort=True):
            group = group.sort_values("origin")
            fig.add_scatter(
                x=group["origin"], y=group["s_aplicado"],
                mode="lines+markers", name=f"Otra rama {other_branch}: S aplicada",
                line={"color": "#808080", "width": 1.5},
                marker={"size": 5}, opacity=0.23,
            )
    fig.add_scatter(
        x=v["origin"], y=v["s_minimo"], mode="lines+markers",
        name="Entrada del mínimo de ECM transformado",
        line={"color": COLORES_D[d], "width": 2},
    )
    fig.add_scatter(
        x=v["origin"], y=v["s_aplicado"], mode="lines+markers",
        name="Suavidad S aplicada por la regla",
        line={"color": "#D55E00", "width": 2.5, "dash": "dash"},
    )
    _style(
        fig, f"Historial de suavidad — d = {d}, rama {branch}",
        "Origen cronológico de validación", "Suavidad normalizada, S",
        height=380,
    )
    fig.update_yaxes(range=[-0.03, 1.03])
    return fig


def _v_losses(
    v: pd.DataFrame, d: int, branch: str, rule: str,
    *, others: pd.DataFrame | None = None,
) -> go.Figure:
    v = v.sort_values("origin")
    fig = go.Figure()
    if others is not None and not others.empty:
        for other_branch, group in others.groupby("rama", sort=True):
            group = group.sort_values("origin")
            fig.add_scatter(
                x=group["origin"], y=group["val1_mse"],
                mode="lines", name=f"Otra rama {other_branch}: ECM V1",
                line={"color": COLORES_D[1], "width": 1.3},
                opacity=0.20, legendgroup=f"otra_{other_branch}",
            )
            fig.add_scatter(
                x=group["origin"], y=group["val2_mse"],
                mode="lines", name=f"Otra rama {other_branch}: ECM V2",
                line={"color": COLORES_D[2], "width": 1.3, "dash": "dot"},
                opacity=0.20, legendgroup=f"otra_{other_branch}",
            )
    fig.add_scatter(
        x=v["origin"], y=v["val1_mse"], mode="lines+markers",
        name="ECM de validación 1 (S aplicado)",
        line={"color": COLORES_D[1], "width": 2},
    )
    fig.add_scatter(
        x=v["origin"], y=v["val2_mse"], mode="lines+markers",
        name="ECM de validación 2 (mismo S aplicado)",
        line={"color": COLORES_D[2], "width": 2},
    )
    _style(
        fig, f"Matriz V: errores registrados — d = {d}, rama {branch}",
        "Origen cronológico de validación",
        "Error cuadrático medio (unidades al cuadrado)", height=380,
    )
    return fig


def _v_table(table: pd.DataFrame) -> pd.DataFrame:
    translated = table.rename(columns=ETIQUETAS_V).copy()
    label = ETIQUETAS_V["regla"]
    if label in translated:
        translated[label] = translated[label].map(
            lambda k: REGLAS_ES.get(k, k)
        )
    return translated


def main() -> None:
    st.set_page_config(page_title="Selección de suavidad y orden", layout="wide")
    st.title("Seguimiento de mínimos locales y selección predictiva de suavidad")
    st.caption(
        "Mínimos cuadrados penalizados · varias validaciones cronológicas · "
        "ramas persistentes · reglas de agregación de suavidad."
    )
    st.markdown(
        "**Fijar el modelo:** para cada orden d y regla r se define un "
        "procedimiento que no cambia entre validaciones. "
        "**Validación 1:** buscar los mínimos del ECM transformado por r. "
        "**Ramas:** seguir esos mínimos dentro de la misma pareja (d,r). "
        "**Validación 2:** evaluar exactamente la misma S, sin reoptimizarla. "
        "**Selección:** menor ECM medio histórico de validación 2. "
        "**Prueba:** comparar contra valores que realmente ocurrieron."
    )

    with st.sidebar:
        st.header("1. Serie temporal")
        fuente = st.radio(
            "Origen de los datos",
            ["Función sintética", "Yahoo Finance", "Archivo CSV"],
        )
        if fuente == "Función sintética":
            familia = st.selectbox("Función generadora", list(FUNCIONES))
            formula = st.text_input(
                "Expresión f(t)", FUNCIONES[familia], key=f"funcion_{familia}"
            )
            n = st.slider("Número de observaciones", 90, 600, 220, 10)
            ruido_sd = st.slider("Escala del ruido, σ", 0.0, 5.0, 0.35, 0.05)
            ruido = st.selectbox("Distribución del ruido", list(RUIDOS))
            phi = st.slider("Autocorrelación AR(1), φ", -0.90, 0.90, 0.0, 0.05)
            semilla = st.number_input("Semilla aleatoria", 0, 999999, 42)
            try:
                frame = make_synthetic(
                    formula, n, ruido_sd, RUIDOS[ruido], phi, int(semilla)
                )
            except (ValueError, ArithmeticError) as exc:
                st.error(f"No se pudo construir la serie: {exc}")
                st.stop()
            serie = "Serie sintética"
        elif fuente == "Yahoo Finance":
            symbols_text = st.text_input(
                "Símbolos separados por comas", "SPY, AAPL, BTC-USD"
            )
            symbols = tuple(dict.fromkeys(
                v.strip().upper() for v in symbols_text.split(",") if v.strip()
            ))
            if not 1 <= len(symbols) <= 12:
                st.error("Introduzca entre uno y doce símbolos bursátiles.")
                st.stop()
            periodo = st.selectbox("Historia disponible", list(PERIODOS), index=2)
            intervalo = st.selectbox("Frecuencia", list(FRECUENCIAS))
            variable = st.selectbox("Variable", list(VARIABLES))
            try:
                data = yahoo_history(
                    symbols, PERIODOS[periodo], FRECUENCIAS[intervalo]
                )
                serie = st.selectbox("Activo", symbols)
                frame = _market_frame(data, serie, VARIABLES[variable])
            except Exception as exc:
                st.error(f"No se pudieron obtener los precios: {exc}")
                st.stop()
            st.download_button(
                "Descargar datos originales (CSV)",
                data.to_csv().encode("utf-8-sig"),
                file_name="serie_financiera.csv", mime="text/csv",
            )
        else:
            archivo = st.file_uploader("Seleccionar archivo CSV", type="csv")
            if archivo is None:
                st.info("Cargue un archivo para comenzar.")
                st.stop()
            csv = pd.read_csv(archivo)
            numericas = csv.select_dtypes(include="number").columns.tolist()
            if not numericas:
                st.error("El archivo no contiene variables numéricas.")
                st.stop()
            serie = st.selectbox("Variable observada", numericas)
            columna_fecha = st.selectbox(
                "Columna de fechas (opcional)",
                ["No utilizar fechas"] + [
                    name for name in csv.columns if name != serie
                ],
            )
            frame = pd.DataFrame({
                "observed": pd.to_numeric(csv[serie], errors="coerce"),
            })
            if columna_fecha != "No utilizar fechas":
                frame["date"] = pd.to_datetime(
                    csv[columna_fecha], errors="coerce"
                )
            frame = frame.dropna().reset_index(drop=True)
            if "date" in frame:
                frame = frame.sort_values("date").reset_index(drop=True)

        st.header("2. Variable que se modelará")
        transformacion_es = st.selectbox(
            "Representación de la serie", list(TRANSFORMACIONES)
        )
        modo, unidad = TRANSFORMACIONES[transformacion_es]
        try:
            frame = transform_observations(frame, modo)
        except ValueError as exc:
            st.error(f"Transformación inválida: {exc}")
            st.stop()
        ultimas = st.slider("Observaciones más recientes", 90, 600, 260, 10)
        frame = frame.tail(ultimas).reset_index(drop=True)

        st.header("3. Diseño de las validaciones")
        modo_nombre = st.radio(
            "Procedimiento",
            ["Seguimiento histórico de ramas (general)",
             "Selección directa en dos bloques (caso particular)"],
        )
        modo = ("ramas" if modo_nombre.startswith("Seguimiento") else "directo")
        ordenes = st.multiselect(
            "Órdenes de diferencias que se compararán, d",
            [1, 2, 3, 4], default=[1, 2, 3, 4],
        )
        L = st.slider("Observaciones por ventana de ajuste, L", 25, 160, 60, 5)
        h = st.slider("Horizonte de cada validación, h", 1, 20, 5)
        test_size = st.slider(
            "Observaciones reservadas para la prueba", 1, 20, 5
        )
        h_futuro = st.slider(
            "Horizonte del pronóstico posterior al último dato", 1, 30, 5
        )
        spacing = st.slider(
            "Separación mínima entre mínimos locales de S",
            0.01, 0.10, 0.02, 0.01,
        )
        grid = st.select_slider(
            "Resolución de las curvas representadas",
            options=[21, 41, 61, 101], value=61,
        )
        depth = st.select_slider(
            "Profundidad de la búsqueda numérica",
            options=[3, 5, 8], value=5,
        )
        if modo == "ramas":
            st.header("4. Seguimiento de ramas y reglas de V")
            paso = st.slider("Separación entre orígenes, en periodos", 1, 20, 5)
            n_origenes = st.slider("Máximo de orígenes históricos", 2, 24, 10)
            n_ramas = st.slider("Máximo de ramas por orden d", 1, 10, 5)
            distancia = st.slider(
                "Distancia máxima para continuar una rama, ΔS",
                0.02, 0.30, 0.10, 0.01,
            )
            soporte = st.slider(
                "Proporción mínima de orígenes para elegir una rama",
                0.25, 1.00, 0.65, 0.05,
            )
            reglas = st.multiselect(
                "Reglas históricas de suavidad (matriz V)",
                options=list(REGLAS_ES),
                default=["last", "mean_k3", "recency_hl3",
                         "val2_weighted", "linear_k3"],
                format_func=lambda k: REGLAS_ES[k],
            )
            st.caption(
                "El método 'Último mínimo' conserva la continuación "
                "polinómica original sin ponderación histórica. Las reglas "
                "son idénticas entre validación 1 y validación 2; nunca se "
                "usan errores futuros para calcular S."
            )
        else:
            reglas = []
        st.caption(
            "Los órdenes d = 3 y 4 pueden producir extrapolaciones inestables."
        )

    if not ordenes:
        st.error("Seleccione al menos un orden d.")
        st.stop()
    if modo == "ramas" and not reglas:
        st.error("Seleccione al menos una regla de suavidad.")
        st.stop()
    minimo = L + (3 if modo == "ramas" else 2) * h + test_size
    if len(frame) < minimo:
        st.error(
            f"El diseño necesita al menos {minimo} observaciones. "
            f"Solo hay {len(frame)} disponibles."
        )
        st.stop()
    valores = frame["observed"].to_numpy(dtype=float)
    with st.spinner(
        "Recuperando mínimos, siguiendo ramas y evaluando reglas cronológicas..."
    ):
        try:
            config = dict(
                orders=tuple(sorted(ordenes)), window=L, horizon=h,
                test_size=test_size, future_horizon=h_futuro,
                candidate_spacing=spacing, grid_points=grid, search_depth=depth,
            )
            if modo == "ramas":
                config.update(
                    rules=tuple(reglas), step=paso, max_origins=n_origenes,
                    track_epsilon=distancia, max_branches=n_ramas,
                    min_support=soporte,
                )
            resultado = analyze(tuple(valores), mode=modo, **config)
        except (ValueError, ArithmeticError, RuntimeError) as exc:
            st.error(f"La selección no pudo completarse: {exc}")
            st.stop()

    st.subheader(
        "Modelo seleccionado por ECM histórico de validación 2"
        if modo == "ramas" else "Modelo seleccionado mediante validación 2"
    )
    metricas = st.columns(4)
    metricas[0].metric("Orden seleccionado, d*", str(resultado.selected_order))
    metricas[1].metric("Suavidad seleccionada, S*", f"{resultado.selected_s:.4f}")
    metricas[2].metric("ECM de validación 2", f"{resultado.selected_val2_mse:.5g}")
    metricas[3].metric(
        "Combinaciones (d, rama, regla)"
        if modo == "ramas" else "Mínimos candidatos evaluados",
        len(resultado.summary) if modo == "ramas" else len(resultado.candidates),
    )
    if modo == "ramas":
        st.write(
            f"**Rama seleccionada:** {resultado.selected_branch} · "
            f"**Regla de suavidad:** "
            f"{REGLAS_ES.get(resultado.selected_rule, resultado.selected_rule)}."
        )
        st.caption(resultado.selection_status)
    st.caption(
        f"Serie: {serie} · Transformación: {transformacion_es} · "
        f"Método: {resultado.method} · Ventana L = {L} · "
        f"Horizonte h = {h}. Ninguna observación de prueba intervino en la selección."
    )

    tab_diseno, tab_val1, tab_ramas, tab_v, tab_val2, tab_final, tab_h = st.tabs([
        "División cronológica",
        "Validación 1: ECM y mínimos por d",
        "Trayectorias de ramas",
        "Matrices V: suavidades y errores",
        "Validación 2: reglas y comparación",
        "Tendencia, prueba y pronóstico",
        "Matriz H de suavizamiento",
    ])

    with tab_diseno:
        st.subheader("Bloques utilizados para estimar y seleccionar")
        if modo == "ramas":
            st.write(
                f"Se analizan {resultado.branches['origin'].nunique()} "
                "orígenes históricos por cada pareja (d, regla). "
                "En V1 se buscan mínimos de ECM₁(φᵣ(V histórica, s)); "
                "el seguimiento se hace sobre la suavidad efectiva y nunca "
                "se comparten ramas entre reglas. Cada decisión usa solo "
                "validaciones 2 que ya habían concluido."
            )
            st.write(
                "**Ajuste de la tendencia:** para pronosticar validación 2 se "
                "emplean los datos conocidos hasta su origen y el **mismo S** "
                "que fijó la regla; no hay una segunda búsqueda de suavidad. "
                "La extrapolación polinómica original sigue disponible con "
                "la regla 'Último mínimo'."
            )
            st.latex(
                r"V_{d,j,r}=\left\{("
                r"S^{\min}_{d,j,t},\;S^{(r)}_{d,j,t},\;"
                r"E_{1,d,j,r,t},\;E_{2,d,j,r,t})\right\}_t"
            )
            st.latex(
                r"(d^*,j^*,r^*)=\underset{d,j,r}{\operatorname{arg\,min}}"
                r"\ \frac{1}{|\mathcal T_{d,j,r}|}"
                r"\sum_{t\in\mathcal T_{d,j,r}}E_{2,d,j,r,t}"
            )
            st.caption(
                "Solo se consideran ramas que cumplen el soporte histórico mínimo. "
                "Los errores históricos pueden corresponder a bloques solapados; "
                "la prueba final se mantiene al margen de la selección."
            )
        else:
            st.write(
                "Caso particular: una sola validación 1 genera los mínimos "
                "locales y una sola validación 2 compara todos los pares (d,S). "
                "No se utilizan trayectorias históricas."
            )
            st.latex(
                r"(d^*,S^*)=\underset{d,\;S\in\mathcal M_d}"
                r"{\operatorname{arg\,min}}\;\operatorname{ECM}_2(d,S)"
            )
        st.plotly_chart(
            _branch_timeline(resultado) if modo == "ramas"
            else _timeline(resultado),
            use_container_width=True,
        )
        if modo == "ramas":
            st.caption(
                "La franja de validación 1 indicada al final es la superficie "
                "más reciente usada para continuar la rama ganadora hacia la prueba; "
                "los orígenes históricos anteriores aparecen en las otras pestañas."
            )

    with tab_val1:
        st.subheader("Curvas del ECM de validación 1 para distintos órdenes d")
        st.write(
            "La línea es el ECM de la continuación polinómica sin ponderación. "
            "Los rombos son sus mínimos; la estrella o línea naranja indica "
            "la suavidad aplicada por la combinación (d, rama, regla) ganadora. "
            "Para reglas distintas de 'Último mínimo', el mínimo de V1 se "
            "calcula sobre la pérdida transformada por esa misma regla."
            if modo == "ramas" else
            "Los rombos identifican los mínimos candidatos; todos se comparan "
            "posteriormente en validación 2."
        )
        for order in sorted(ordenes):
            plot = _val1_figure(resultado, order)
            if modo == "ramas" and order == resultado.selected_order:
                plot.add_vline(
                    x=resultado.selected_s, line_dash="dash",
                    line_color="#D55E00", line_width=2,
                )
            st.plotly_chart(plot, use_container_width=True)
        st.caption(
            "Se muestran las curvas de la validación 1 final, previa al bloque "
            "de prueba. En modo histórico, también puede examinarse cada "
            "origen por separado en la sección de ramas."
        )

    with tab_ramas:
        if modo == "ramas":
            st.subheader("Evolución cronológica de los mínimos locales")
            col_d, col_r = st.columns(2)
            d_ramas = col_d.selectbox(
                "Orden d del procedimiento",
                sorted(ordenes), key="orden_ramas",
            )
            regla_ramas = col_r.selectbox(
                "Regla fija para validar y seguir ramas",
                list(dict.fromkeys(resultado.evaluations["regla"].tolist())),
                format_func=lambda k: REGLAS_ES[k],
                key="regla_ramas",
            )
            st.plotly_chart(
                _branch_figure(resultado, d_ramas, regla_ramas),
                use_container_width=True
            )
            st.plotly_chart(
                _historical_loss_figure(resultado, d_ramas, regla_ramas),
                use_container_width=True,
            )
            st.dataframe(
                _v_table(resultado.branches.loc[
                    resultado.branches["d"].eq(d_ramas)
                    & resultado.branches["regla"].eq(regla_ramas)
                ]),
                use_container_width=True, hide_index=True,
            )
            st.caption(
                "Cada regla define su propia función de error de validación 1 "
                "al transformar las suavidades con su historial. Las ramas "
                "se identifican por proximidad entre las **suavidades aplicadas** "
                "de ese mismo par (d, regla), no se comparten entre métodos. "
                "Los círculos del mapa señalan S aplicada sobre el ECM original "
                "como referencia, no mínimos de la curva original."
            )
        else:
            st.info(
                "El seguimiento de ramas se utiliza en el procedimiento "
                "general. Selecciónelo en la barra lateral."
            )

    with tab_v:
        if modo == "ramas":
            st.subheader("Matriz V por orden, rama y regla de selección")
            st.write(
                "Cada fila registra el argumento que minimizó el ECM de V1 "
                "**transformado con la regla seleccionada**, la suavidad efectiva "
                "producida por esa regla y los errores obtenidos con ese mismo S "
                "en V1 y V2. La regla y d son fijos en ambas validaciones. "
                "Una regla que no depende del argumento actual puede tener "
                "ECM transformado constante: no se inventan mínimos en ese caso."
            )
            c1, c2, c3 = st.columns(3)
            d_v = c1.selectbox(
                "Orden d", sorted(ordenes), key="orden_v",
            )
            reglas_calculadas = list(
                dict.fromkeys(resultado.evaluations["regla"].tolist())
            )
            r_v = c2.selectbox(
                "Regla fija de V1 y V2", reglas_calculadas,
                format_func=lambda k: REGLAS_ES[k],
                key="regla_v",
            )
            ramas_disponibles = sorted(
                resultado.evaluations.loc[
                    resultado.evaluations["d"].eq(d_v)
                    & resultado.evaluations["regla"].eq(r_v), "rama"
                ].unique()
            )
            b_v = c3.selectbox(
                "Rama específica de esta regla", ramas_disponibles,
                key=f"rama_v_{d_v}_{r_v}",
            )
            subset = resultado.evaluations.loc[
                resultado.evaluations["d"].eq(d_v)
                & resultado.evaluations["rama"].eq(b_v)
                & resultado.evaluations["regla"].eq(r_v)
            ]
            st.plotly_chart(
                _v_figure(subset, d_v, b_v, r_v), use_container_width=True
            )
            st.plotly_chart(
                _v_losses(subset, d_v, b_v, r_v), use_container_width=True
            )
            st.dataframe(
                _v_table(subset), use_container_width=True, hide_index=True,
            )
            st.download_button(
                "Descargar esta matriz V (CSV)",
                _v_table(subset).to_csv(index=False).encode("utf-8-sig"),
                file_name=f"V_d{d_v}_{b_v}_{r_v}.csv",
                mime="text/csv",
            )
            st.download_button(
                "Descargar todas las matrices V (CSV)",
                _v_table(resultado.evaluations).to_csv(
                    index=False
                ).encode("utf-8-sig"),
                file_name="matrices_V_completas.csv", mime="text/csv",
            )
        else:
            st.info(
                "Las matrices V históricas se utilizan en el procedimiento "
                "general. Selecciónelo en la barra lateral."
            )

    with tab_val2:
        if modo == "ramas":
            st.subheader(
                "Comparación de ramas y reglas por ECM acumulado de validación 2"
            )
            st.plotly_chart(
                _branch_rank_figure(resultado), use_container_width=True
            )
            st.write(
                "Se selecciona el **orden, la rama y la regla** cuyo ECM medio "
                "en validación 2 es menor entre los candidatos con suficiente "
                "soporte. Los errores de validación 2 **no** modifican el S "
                "decidido para ese origen; quedan registrados en V y pueden "
                "utilizarse en orígenes posteriores cuando ya son conocidos."
            )
            st.markdown("**Resumen de comparaciones históricas**")
            st.dataframe(
                _v_table(resultado.summary),
                use_container_width=True, hide_index=True,
            )
            st.download_button(
                "Descargar resultados de todas las reglas (CSV)",
                _v_table(resultado.summary).to_csv(
                    index=False
                ).encode("utf-8-sig"),
                file_name="comparacion_historica_reglas.csv", mime="text/csv",
            )
            st.caption(
                "RECM agregado = raíz de la media de errores cuadráticos "
                "históricos. La diferencia en cobertura entre ramas está "
                "visible mediante el soporte. El test no participa."
            )
        else:
            st.subheader("Selección directa por ECM de la segunda validación")
            st.plotly_chart(
                _val2_figure(resultado), use_container_width=True
            )
            st.write(
                "Cada punto corresponde a un mínimo local de validación 1. "
                "El orden y la suavidad se mantienen fijos para pronosticar "
                "la validación 2; la estrella identifica el menor ECM."
            )
            st.dataframe(
                _table(resultado.candidates),
                use_container_width=True, hide_index=True,
            )
            st.download_button(
                "Descargar candidatos directos (CSV)",
                _table(resultado.candidates).to_csv(
                    index=False
                ).encode("utf-8-sig"),
                file_name="candidatos_validacion_2.csv", mime="text/csv",
            )

    with tab_final:
        st.subheader("Pronóstico utilizando el orden y la suavidad seleccionados")
        left, right = st.columns(2)
        revelar = left.checkbox(
            "Mostrar evaluación retrospectiva y los valores de prueba", True
        )
        latente = right.checkbox(
            "Mostrar la función verdadera de la simulación",
            value="latent" in frame, disabled="latent" not in frame,
        )
        st.plotly_chart(
            _forecast_figure(
                frame, resultado, unidad,
                reveal=revelar, truth=latente,
            ), use_container_width=True,
        )
        if modo == "ramas":
            st.write(
                f"Se mantiene el orden **d = {resultado.selected_order}**, "
                f"la rama **{resultado.selected_branch}** y la regla "
                f"**{REGLAS_ES[resultado.selected_rule]}**. Para pronosticar "
                "la prueba se aplica S sin reoptimizar. "
                "El pronóstico futuro se ajusta después a todos los datos "
                "disponibles, conservando la misma S y el mismo método."
            )
        st.caption(
            "Se conservan **d*** y **S*** seleccionados en validación 2. "
            "El modelo se reajusta con las últimas L observaciones realmente "
            "disponibles, incluida la prueba retrospectiva ya evaluada. "
            "Los puntos discontinuos a la derecha son el pronóstico futuro "
            "desde el último dato real. Las fechas futuras son aproximadas "
            "si no se dispone de un calendario explícito."
        )
        if revelar:
            test = valores[resultado.pretest_end:resultado.test_end]
            mse = float(np.mean((test - resultado.evaluation_forecast)**2))
            st.metric("ECM en prueba no utilizada para selección", f"{mse:.6g}")
            prueba = pd.DataFrame({
                "Observación": np.arange(
                    resultado.pretest_end+1, resultado.test_end+1
                ),
                "Valor real de la serie": test,
                "Pronóstico retrospectivo": resultado.evaluation_forecast,
                "Error de pronóstico": test-resultado.evaluation_forecast,
            })
            st.dataframe(prueba, use_container_width=True, hide_index=True)
            st.caption(
                "Los valores de prueba no modifican d* ni S*, tampoco el "
                "pronóstico retrospectivo. Sin embargo, una vez evaluados "
                "se incluyen en el reajuste para pronosticar el futuro."
            )
        pronosticos = pd.DataFrame({
            "Número futuro de observación": np.arange(
                resultado.forecast_start+1, resultado.forecast_end+1
            ),
            "Pronóstico futuro": resultado.forecast,
        })
        st.download_button(
            "Descargar pronóstico futuro (CSV)",
            pronosticos.to_csv(index=False).encode("utf-8-sig"),
            file_name="pronostico_futuro.csv", mime="text/csv",
        )
        backtest = pd.DataFrame({
            "Número de observación": np.arange(
                resultado.pretest_end+1, resultado.test_end+1
            ),
            "Pronóstico retrospectivo": resultado.evaluation_forecast,
            "Valor observado": valores[
                resultado.pretest_end:resultado.test_end
            ],
        })
        st.download_button(
            "Descargar evaluación retrospectiva (CSV)",
            backtest.to_csv(index=False).encode("utf-8-sig"),
            file_name="evaluacion_prueba.csv", mime="text/csv",
        )

    with tab_h:
        st.subheader("Interpretación del operador de suavizamiento")
        st.latex(
            r"\widehat{\boldsymbol\tau}=H_\lambda\mathbf y,\qquad "
            r"H_\lambda=(I+\lambda D_d^{\mathsf T}D_d)^{-1}"
        )
        H = smoothing_matrix(L, resultado.selected_order, resultado.selected_s)
        st.plotly_chart(_matrix_figure(H), use_container_width=True)
        st.write(
            "El peso Hᵢⱼ mide la contribución de la observación j a la "
            "tendencia estimada en i. La matriz corresponde al **modelo final "
            "seleccionado**, no a otro estimador."
        )
        c1, c2, c3 = st.columns(3)
        c1.metric("Grados de libertad efectivos, tr(H)", f"{np.trace(H):.4f}")
        c2.metric("Suavidad normalizada, S", f"{resultado.selected_s:.4f}")
        c3.metric(
            "Penalización λ",
            "∞" if np.isinf(resultado.selected_lambda)
            else f"{resultado.selected_lambda:.4g}",
        )
        st.latex(
            r"S=\frac{L-\operatorname{tr}(H_\lambda)}{L-d}"
        )

    with st.expander("Definiciones y alcance de las reglas históricas"):
        st.write(
            "**Rama:** trayectoria de mínimos de ECM de V1 bajo el mismo "
            "orden d y la misma regla, vinculados por cercanía en suavidad "
            "aplicada. **Regla:** transforma el argumento candidato y su "
            "historia disponible en un único S efectivo. "
            "**Matriz V:** historial de S mínimo, S aplicado y errores de "
            "ambas validaciones por (d, rama, regla). "
            "**Último mínimo:** continuidad polinómica original sin promedio. "
            "**Soporte:** proporción de orígenes históricos evaluados."
        )
        st.write(
            "La pareja (d, regla) está fijada al principio del experimento; "
            "define los mínimos y las ramas en V1 y se aplica igualmente en V2. La tendencia puede "
            "reestimarse al cambiar el origen y disponer de nuevos datos, "
            "pero no se vuelve a optimizar S en validación 2. "
            "El test real permanece fuera de la elección de d, rama y regla."
        )
        st.caption(
            "La variante histórica previa del laboratorio se conserva en "
            "apps/smoothness_lab_advanced.py. El caso de selección directa "
            "permanece disponible en la barra lateral."
        )


if __name__ == "__main__":
    main()
