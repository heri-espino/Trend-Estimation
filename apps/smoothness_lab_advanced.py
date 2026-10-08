"""Aplicación interactiva en español para paper_smoothness-cv.

Ejecutar desde la raíz del repositorio:
    python -m pip install -e ".[dashboard,finance]"
    streamlit run apps/smoothness_lab.py

No modifica la implementación matemática ni los experimentos congelados.
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
    RULES,
    make_synthetic,
    run_lab,
    smoothing_matrix,
    transform_observations,
)
import trend_estimation as td


# Identificadores internos invariables: solo cambia la capa de presentación.
MODOS = {
    "Nivel original": ("Level", "Nivel de la variable (unidades originales)"),
    "Logaritmo del nivel": ("Log level", "Logaritmo natural del nivel"),
    "Índice con base 100": ("Indexed to 100", "Índice (primera observación = 100)"),
    "Rendimiento simple": ("Simple return", "Rendimiento simple (proporción por periodo)"),
    "Rendimiento logarítmico": ("Log return", "Log-rendimiento (por periodo)"),
}
VISTAS = {
    "Tendencia estimada y pronóstico": "forecast",
    "Serie observada y tendencia": "trend",
    "Comparación de niveles de suavidad": "manual",
    "Residuos de la tendencia": "residual",
    "Primera diferencia de la tendencia": "slope",
}
REGLAS = {
    "last": "Último mínimo de la rama",
    "mean_k3": "Media de los 3 últimos mínimos",
    "mean_k5": "Media de los 5 últimos mínimos",
    "median_k3": "Mediana de los 3 últimos mínimos",
    "median_k5": "Mediana de los 5 últimos mínimos",
    "recency_hl3": "Media exponencial reciente (semivida = 3)",
    "recency_hl5": "Media exponencial reciente (semivida = 5)",
    "recency_hl10": "Media exponencial reciente (semivida = 10)",
    "val2_weighted": "Media ponderada por el error de validación 2",
    "recency_val2_hl3": "Ponderación temporal y por validación 2 (semivida = 3)",
    "recency_val2_hl5": "Ponderación temporal y por validación 2 (semivida = 5)",
    "recency_val2_hl10": "Ponderación temporal y por validación 2 (semivida = 10)",
    "linear_k3": "Extrapolación lineal de los últimos 3 mínimos",
    "linear_k5": "Extrapolación lineal de los últimos 5 mínimos",
    "linear_k10": "Extrapolación lineal de los últimos 10 mínimos",
    "ew_linear_hl3": "Extrapolación lineal con ponderación temporal (semivida = 3)",
    "ew_linear_hl5": "Extrapolación lineal con ponderación temporal (semivida = 5)",
    "delta_hl3": "Extrapolación de incrementos (semivida = 3)",
    "delta_hl5": "Extrapolación de incrementos (semivida = 5)",
}
RUIDOS = {
    "Normal (gaussiano)": "Gaussian",
    "Laplace": "Laplace",
    "t de Student (5 grados de libertad)": "Student-t (df=5)",
    "Heterocedástico": "Heteroskedastic",
}
PERIODOS = {
    "6 meses": "6mo", "1 año": "1y", "2 años": "2y",
    "5 años": "5y", "10 años": "10y",
}
FRECUENCIAS = {"Diaria": "1d", "Semanal": "1wk", "Mensual": "1mo"}
CAMPOS = {
    "Cierre ajustado": "Close", "Apertura": "Open", "Máximo": "High",
    "Mínimo": "Low", "Volumen": "Volume",
}
COLORES = {
    "observado": "#52525B",
    "seleccionado": "#D55E00",
    "agrupado": "#0072B2",
    "manual": "#009E73",
    "latente": "#9A589A",
    "prueba": "#252525",
    "alternativa": "#A1A1AA",
}
COLUMNAS_RAMAS = {
    "origin": "Origen de validación",
    "branch_id": "Identificador de rama",
    "smoothness": "Suavidad normalizada, S",
    "lambda": "Parámetro de penalización, λ",
    "val1_mse": "ECM de validación 1",
    "val2_mse": "ECM de validación 2",
    "val2_rmse": "RECM de validación 2",
    "status": "Estado de correspondencia",
    "delta_s": "Cambio absoluto de suavidad",
    "support": "Proporción de orígenes con continuidad",
    "mean_val2_rmse": "RECM media de validación 2",
    "mean_val2_mse": "ECM medio de validación 2",
    "last_historical_s": "Última suavidad histórica",
    "continued_to_final": "Continuó hasta la validación final",
    "source": "Tipo de mínimo",
}
ESTADOS = {"matched": "Correspondencia encontrada", "missing": "Sin correspondencia"}
FUENTES = {"interior": "Mínimo interior", "S=0": "Extremo S = 0",
           "S=1": "Extremo S = 1", "boundary_fallback": "Extremo"}
FORMULAS = {
    "Tendencia lineal con componente cíclico": "10 + 0.02*t + sin(t/12)",
    "Cambio de pendiente": "10 + 0.015*t + where(t>100, 0.06*(t-100), 0)",
    "Tendencia no lineal": "10 + 0.00015*(t-120)**2 + 0.8*sin(t/18)",
    "Cambio estructural de nivel": "10 + 0.015*t + where(t>110, 3, 0)",
    "Expresión personalizada": "10 + 0.02*t + sin(t/12)",
}


@st.cache_data(ttl=3600, show_spinner=False)
def yahoo_history(tickers: tuple[str, ...], period: str, interval: str) -> pd.DataFrame:
    import yfinance as yf

    if not tickers:
        raise ValueError("Debe especificar al menos un símbolo.")
    frame = yf.download(
        tickers=list(tickers), period=period, interval=interval,
        auto_adjust=True, progress=False, threads=False, group_by="ticker",
    )
    if frame.empty:
        raise ValueError("Yahoo Finance no devolvió observaciones para esta consulta.")
    return frame


@st.cache_data(show_spinner=False, max_entries=32)
def analyze(values: tuple[float, ...], **kwargs):
    return run_lab(np.asarray(values, dtype=float), **kwargs)


def _frame_from_market(raw: pd.DataFrame, ticker: str, field: str) -> pd.DataFrame:
    if isinstance(raw.columns, pd.MultiIndex):
        if ticker in raw.columns.get_level_values(0):
            column = raw[ticker][field]
        elif ticker in raw.columns.get_level_values(1):
            column = raw[field][ticker]
        else:
            raise ValueError(f"No se encontraron datos para {ticker}.")
    else:
        column = raw[field]
    column = pd.to_numeric(column, errors="coerce").dropna()
    if column.empty:
        raise ValueError(f"No se encontraron observaciones válidas de {field} para {ticker}.")
    return pd.DataFrame({"date": column.index, "observed": column.to_numpy(dtype=float)})


def _espanol(frame: pd.DataFrame) -> pd.DataFrame:
    result = frame.rename(columns=COLUMNAS_RAMAS).copy()
    name = COLUMNAS_RAMAS["status"]
    if name in result:
        result[name] = result[name].replace(ESTADOS)
    name = COLUMNAS_RAMAS["source"]
    if name in result:
        result[name] = result[name].replace(FUENTES)
    return result


def _descarga(texto: str, tabla: pd.DataFrame, archivo: str) -> None:
    st.download_button(
        texto, tabla.to_csv(index=False).encode("utf-8-sig"),
        file_name=archivo, mime="text/csv",
    )


def _nombre_rama(branch_id: str) -> str:
    if branch_id == "none":
        return "Sin continuación (referencia agrupada)"
    return f"Rama {branch_id.upper()}"


def _eje_x(frame: pd.DataFrame):
    if "date" in frame.columns:
        return pd.to_datetime(frame["date"]).tolist(), "Fecha"
    return np.arange(1, len(frame) + 1), "Número de observación"


def _estilo(fig: go.Figure, *, titulo: str, eje_x: str, eje_y: str,
            altura: int = 450, leyenda: bool = True) -> go.Figure:
    fig.update_layout(
        template="plotly_white",
        title={"text": titulo, "x": 0.015, "xanchor": "left", "font": {"size": 18}},
        xaxis_title=eje_x,
        yaxis_title=eje_y,
        height=altura,
        margin={"l": 45, "r": 25, "t": 85, "b": 75},
        font={"size": 12},
        legend={"orientation": "h", "y": -0.26, "x": 0.0,
                "font": {"size": 11}, "title_text": ""},
        showlegend=leyenda,
        hovermode="x unified",
    )
    fig.update_xaxes(showgrid=True, gridcolor="#ECECEC", zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="#ECECEC", zeroline=False)
    return fig


def _grafica_cronologia(
    n: int, *, ventana: int, horizonte: int, paso: int, reserva: int
) -> go.Figure:
    """Representación esquemática de los cortes temporales, sin datos futuros."""
    fin_preprueba = n - reserva
    fin_historico = fin_preprueba - horizonte
    cortes = td.rolling_origin_splits(
        fin_historico, initial_train=ventana, horizon=horizonte,
        expanding=False, train_window=ventana, step=paso,
    )
    pares = [
        corte for corte in cortes
        if corte.validation.stop + horizonte <= fin_historico
    ]
    if not pares:
        raise ValueError("No existe un origen histórico con dos validaciones.")
    ultimo = pares[-1]
    origen = ultimo.validation.start
    segmentos = [
        (3, origen - ventana, origen, "Ajuste histórico", "Ajuste L", "#6B7280"),
        (3, origen, origen + horizonte, "Validación 1", "Validación 1", "#0072B2"),
        (3, origen + horizonte, origen + 2*horizonte,
         "Validación 2", "Validación 2", "#009E73"),
        (2, fin_preprueba - horizonte - ventana, fin_preprueba - horizonte,
         "Ajuste antes de validación final", "Ajuste L", "#6B7280"),
        (2, fin_preprueba - horizonte, fin_preprueba,
         "Validación final 1", "Validación 1", "#0072B2"),
        (1, fin_preprueba - ventana, fin_preprueba,
         "Nuevo ajuste definitivo", "Ajuste L", "#6B7280"),
        (1, fin_preprueba, n, "Prueba fuera de muestra", "Prueba", "#D55E00"),
    ]
    fig = go.Figure()
    visibles = set()
    for fila, inicio, fin, descripcion, tipo, color in segmentos:
        fig.add_trace(go.Bar(
            orientation="h",
            y=[fila], base=[inicio], x=[fin - inicio],
            width=0.45,
            marker={"color": color, "line": {"width": 0}},
            name=tipo,
            legendgroup=tipo,
            showlegend=tipo not in visibles,
            customdata=[[inicio + 1, fin]],
            hovertemplate=(
                descripcion + "<br>Observaciones %{customdata[0]} a "
                "%{customdata[1]}<extra></extra>"
            ),
        ))
        visibles.add(tipo)
    fig = _estilo(
        fig,
        titulo="Esquema cronológico de ajuste, validación y prueba",
        eje_x="Número de observación (límites de cada bloque)",
        eje_y="Etapa del procedimiento",
        altura=370,
    )
    fig.update_layout(barmode="overlay", hovermode="closest")
    fig.update_yaxes(
        tickmode="array", tickvals=[1, 2, 3],
        ticktext=[
            "Ajuste definitivo y prueba",
            "Última validación 1",
            "Validación histórica en dos etapas",
        ],
        range=[0.4, 3.6], showgrid=False,
    )
    fig.update_xaxes(range=[0, n + 1])
    return fig


def _grafica_serie(
    frame: pd.DataFrame,
    result,
    *,
    vista: str,
    unidad: str,
    order: int,
    manual_s: float,
    revelar_prueba: bool,
    mostrar_agrupado: bool,
    mostrar_latente: bool,
    limitar_escala: bool,
) -> go.Figure:
    x, eje_x = _eje_x(frame)
    y = frame["observed"].to_numpy(dtype=float)
    inicio, fin = result.train_start, result.pretest_end
    x_ajuste, x_prueba = x[inicio:fin], x[fin:result.test_end]
    fig = go.Figure()

    def linea(xx, yy, nombre, color, *, dash="solid", width=2.3, markers=False):
        fig.add_trace(go.Scatter(
            x=xx, y=yy, mode="lines+markers" if markers else "lines",
            name=nombre, line={"color": color, "dash": dash, "width": width},
            marker={"size": 5},
        ))

    if vista == "residual":
        linea(x_ajuste, y[inicio:fin] - result.trend,
              "Residuo de la tendencia seleccionada", COLORES["seleccionado"])
        fig.add_hline(y=0, line_dash="dot", line_color=COLORES["alternativa"])
        titulo = "Residuos de la tendencia estimada"
        eje_y = f"Residuo ({unidad})"
    elif vista == "slope":
        linea(x_ajuste[1:], np.diff(result.trend),
              "Primera diferencia: método dinámico", COLORES["seleccionado"])
        if mostrar_agrupado:
            linea(x_ajuste[1:], np.diff(result.pooled_trend),
                  "Primera diferencia: validación agrupada",
                  COLORES["agrupado"], dash="dash")
        fig.add_hline(y=0, line_dash="dot", line_color=COLORES["alternativa"])
        titulo = "Variación entre observaciones consecutivas de la tendencia"
        eje_y = f"Primera diferencia ({unidad} por observación)"
    else:
        linea(x[:fin], y[:fin],
              "Serie observada (antes de la prueba)", COLORES["observado"], width=1.65)
        if revelar_prueba:
            linea(x_prueba, y[fin:result.test_end],
                  "Valores observados en prueba", COLORES["prueba"],
                  dash="dot", markers=True)
        if mostrar_latente and "latent" in frame:
            linea(x[:fin], frame["latent"].to_numpy(dtype=float)[:fin],
                  "Tendencia verdadera de la simulación", COLORES["latente"],
                  dash="dot")
        if vista in ("forecast", "trend"):
            linea(x_ajuste, result.trend,
                  "Tendencia estimada: método dinámico", COLORES["seleccionado"])
            if vista == "forecast":
                linea(x_prueba, result.forecast,
                      "Pronóstico: método dinámico", COLORES["seleccionado"],
                      dash="dash", markers=True)
                if mostrar_agrupado:
                    linea(x_ajuste, result.pooled_trend,
                          "Tendencia: validación agrupada", COLORES["agrupado"],
                          dash="dash", width=1.8)
                    linea(x_prueba, result.pooled_forecast,
                          "Pronóstico: validación agrupada", COLORES["agrupado"],
                          dash="dot", markers=True)
            titulo = (
                "Tendencia estimada y extrapolación fuera de muestra"
                if vista == "forecast"
                else "Comparación de la serie observada y la tendencia estimada"
            )
        else:
            ajustado = td.PurePenalizedTrend(
                order=order, smoothness=manual_s
            ).fit(y[inicio:fin])
            manual_pronostico = np.asarray(ajustado.forecast(len(x_prueba)), dtype=float)
            linea(x_ajuste, result.trend,
                  "Tendencia: regla dinámica seleccionada", COLORES["seleccionado"])
            linea(x_ajuste, ajustado.trend_,
                  f"Tendencia: S fijada en {manual_s:.2f}",
                  COLORES["manual"], dash="dash")
            linea(x_prueba, result.forecast,
                  "Pronóstico: regla dinámica", COLORES["seleccionado"],
                  dash="dash", markers=True)
            linea(x_prueba, manual_pronostico,
                  f"Pronóstico: S = {manual_s:.2f}", COLORES["manual"],
                  dash="dot", markers=True)
            titulo = "Sensibilidad de la tendencia al nivel de suavidad"
        eje_y = unidad
        if len(x_prueba) > 0:
            fig.add_vrect(
                x0=x_prueba[0], x1=x_prueba[-1],
                fillcolor="#E9EDF2", opacity=0.40, line_width=0,
                layer="below",
            )
            fig.add_vline(
                x=x_prueba[0], line_dash="dot",
                line_color="#8A8A8A", line_width=1,
            )
        if limitar_escala:
            visibles = y[:fin]
            minimo, maximo = np.min(visibles), np.max(visibles)
            distancia = max(float(maximo - minimo), 1e-8)
            fig.update_yaxes(range=[
                float(minimo - 0.2 * distancia),
                float(maximo + 0.2 * distancia),
            ])
    return _estilo(fig, titulo=titulo, eje_x=eje_x, eje_y=eje_y, altura=520)


def _grafica_superficie(
    result,
    *,
    relativa: bool,
) -> go.Figure:
    # El color relativo facilita comparar orígenes con distintas escalas.
    matriz = result.surfaces.pivot(
        index="origin", columns="smoothness", values="val1_mse"
    ).sort_index()
    absolutos = matriz.to_numpy(dtype=float)
    minimos = np.maximum(np.min(absolutos, axis=1, keepdims=True), 1e-15)
    valores = absolutos / minimos if relativa else absolutos
    etiqueta = ("ECM / menor ECM del mismo origen" if relativa
                else "ECM de validación 1")
    fig = go.Figure(go.Heatmap(
        x=matriz.columns.to_numpy(dtype=float),
        y=matriz.index.to_numpy(dtype=int),
        z=valores,
        customdata=absolutos,
        colorscale="Viridis",
        colorbar={"title": {"text": etiqueta}},
        hovertemplate=(
            "Origen histórico: %{y}<br>Suavidad S: %{x:.3f}"
            "<br>ECM validación 1: %{customdata:.6g}"
            + ("<br>ECM relativo: %{z:.3f} veces" if relativa else "")
            + "<extra></extra>"
        ),
    ))
    for rama, grupo in result.tracks.groupby("branch_id"):
        escogida = rama == result.selected_branch
        grupo = grupo.sort_values("origin")
        fig.add_trace(go.Scatter(
            x=grupo["smoothness"], y=grupo["origin"], mode="lines+markers",
            name=_nombre_rama(rama) + (" (seleccionada)" if escogida else ""),
            marker={"size": 7 if escogida else 4},
            line={"color": "white" if escogida else "#D6D6D6",
                  "width": 3.2 if escogida else 1.1,
                  "dash": "solid" if escogida else "dot"},
            connectgaps=False,
            hovertemplate=(
                f"{_nombre_rama(rama)}<br>Origen: %{{y}}"
                "<br>Suavidad S: %{x:.4f}<extra></extra>"
            ),
        ))
    fig = _estilo(
        fig,
        titulo="Superficie histórica del error cuadrático medio de validación 1",
        eje_x="Suavidad normalizada, S (0 = sin penalización; 1 = máxima)",
        eje_y="Número de origen de validación",
        altura=520,
    )
    fig.update_yaxes(dtick=1, autorange="reversed")
    fig.update_xaxes(range=[0, 1])
    return fig


def _grafica_ultimo_origen(result, *, escala_log: bool) -> go.Figure:
    fig = go.Figure()
    s = result.final_surface["smoothness"].to_numpy(dtype=float)
    mse = result.final_surface["val1_mse"].to_numpy(dtype=float)
    fig.add_trace(go.Scatter(
        x=s, y=mse, mode="lines",
        name="ECM de validación 1", line={"color": COLORES["observado"], "width": 2.2},
    ))
    candidatos = result.candidates
    fig.add_trace(go.Scatter(
        x=candidatos["smoothness"], y=candidatos["val1_mse"],
        mode="markers", name="Mínimos locales recuperados",
        marker={"symbol": "diamond", "size": 10, "color": COLORES["seleccionado"]},
        text=candidatos["source"].map(FUENTES),
        hovertemplate=(
            "%{text}<br>Suavidad S: %{x:.4f}<br>ECM: %{y:.6g}<extra></extra>"
        ),
    ))
    fig.add_vline(
        x=result.final_s, line_dash="dash", line_color=COLORES["seleccionado"],
        line_width=2,
    )
    fig.add_vline(
        x=result.pooled_s, line_dash="dot", line_color=COLORES["agrupado"],
        line_width=2,
    )
    fig.add_trace(go.Scatter(
        x=[result.final_s], y=[None], mode="markers",
        name=f"S elegida por la regla dinámica = {result.final_s:.3f}",
        marker={"color": COLORES["seleccionado"]},
    ))
    fig.add_trace(go.Scatter(
        x=[result.pooled_s], y=[None], mode="markers",
        name=f"S del criterio agrupado = {result.pooled_s:.3f}",
        marker={"color": COLORES["agrupado"]},
    ))
    fig = _estilo(
        fig,
        titulo="ECM de validación 1 en el último origen anterior a la prueba",
        eje_x="Suavidad normalizada, S",
        eje_y="ECM de validación 1 (unidades transformadas al cuadrado)",
        altura=440,
    )
    fig.update_xaxes(range=[0, 1])
    if escala_log and np.all(mse > 0):
        fig.update_yaxes(type="log")
    return fig


def _grafica_ramas(result, *, variable: str, escala_log: bool = False) -> go.Figure:
    fig = go.Figure()
    for rama, grupo in result.tracks.groupby("branch_id"):
        grupo = grupo.sort_values("origin")
        elegido = rama == result.selected_branch
        etiqueta = _nombre_rama(rama)
        if elegido:
            etiqueta += " (seleccionada)"
        fig.add_trace(go.Scatter(
            x=grupo["origin"], y=grupo[variable], mode="lines+markers",
            name=etiqueta, connectgaps=False,
            line={
                "color": COLORES["seleccionado"] if elegido else COLORES["alternativa"],
                "width": 3.3 if elegido else 1.5,
                "dash": "solid" if elegido else "dot",
            },
            marker={"size": 8 if elegido else 5},
        ))
    if variable == "smoothness":
        fig = _estilo(
            fig, titulo="Evolución temporal de los mínimos locales de suavidad",
            eje_x="Número de origen de validación",
            eje_y="Suavidad normalizada, S", altura=430,
        )
        fig.update_yaxes(range=[-0.025, 1.025])
    else:
        fig = _estilo(
            fig, titulo="Error cuadrático medio de validación 2 por rama",
            eje_x="Número de origen de validación",
            eje_y="ECM de validación 2 (unidades transformadas al cuadrado)",
            altura=430,
        )
        positivos = result.tracks[variable].dropna()
        if escala_log and not positivos.empty and np.all(positivos > 0):
            fig.update_yaxes(type="log")
    fig.update_xaxes(dtick=1)
    return fig


def _grafica_matriz(H: np.ndarray, *, solo_magnitud: bool) -> go.Figure:
    pesos = np.abs(H) if solo_magnitud else H
    maximo = float(np.max(np.abs(pesos)))
    fig = go.Figure(go.Heatmap(
        z=pesos,
        x=np.arange(1, H.shape[1] + 1),
        y=np.arange(1, H.shape[0] + 1),
        customdata=H,
        zmin=0 if solo_magnitud else -maximo,
        zmax=maximo,
        zmid=None if solo_magnitud else 0,
        colorscale="Viridis" if solo_magnitud else "RdBu",
        colorbar={"title": {"text": "|Hᵢⱼ|" if solo_magnitud else "Hᵢⱼ"}},
        hovertemplate=(
            "Posición estimada i: %{y}<br>Observación de entrada j: %{x}"
            "<br>Peso Hᵢⱼ = %{customdata:.5f}<extra></extra>"
        ),
    ))
    fig = _estilo(
        fig, titulo="Matriz de suavizamiento: contribución de cada observación",
        eje_x="Índice de la observación original, j",
        eje_y="Índice de la tendencia estimada, i",
        altura=590, leyenda=False,
    )
    fig.update_yaxes(autorange="reversed", scaleanchor="x", scaleratio=1)
    return fig


def main() -> None:
    st.set_page_config(page_title="Laboratorio de suavizamiento", layout="wide")
    st.title("Laboratorio de suavizamiento de tendencias para pronósticos")
    st.caption(
        "Mínimos locales de pérdida predictiva, validación cronológica y "
        "selección dinámica de suavidad mediante ramas persistentes."
    )

    with st.sidebar:
        st.header("1. Origen de la serie temporal")
        fuente = st.radio(
            "Tipo de datos", ["Función sintética", "Yahoo Finance", "Archivo CSV"]
        )
        if fuente == "Función sintética":
            plantilla = st.selectbox("Familia de tendencia", list(FORMULAS))
            expresion = st.text_input(
                "Función generadora f(t)", FORMULAS[plantilla],
                key=f"formula_{plantilla}",
                help=(
                    "Puede modificar la expresión usando t, números y operaciones. "
                    "Funciones permitidas: sin, cos, tan, exp, log, sqrt, abs, "
                    "tanh, where, minimum, maximum y clip."
                ),
            )
            n = st.slider("Número de observaciones", 90, 600, 220, 10)
            desviacion = st.slider(
                "Escala de las innovaciones de ruido, σ", 0.0, 5.0, 0.35, 0.05
            )
            tipo_ruido = st.selectbox("Distribución del ruido", list(RUIDOS))
            phi = st.slider(
                "Autocorrelación del ruido AR(1), φ", -0.90, 0.90, 0.0, 0.05
            )
            semilla = st.number_input("Semilla aleatoria", 0, 999999, 42)
            try:
                datos = make_synthetic(
                    expresion, n, desviacion,
                    RUIDOS[tipo_ruido], phi, int(semilla),
                )
            except (ValueError, ArithmeticError) as exc:
                st.error(f"No se pudo generar la función: {exc}")
                st.stop()
            serie_nombre = "Serie sintética"
        elif fuente == "Yahoo Finance":
            texto = st.text_input(
                "Símbolos bursátiles (separados por comas)", "SPY, AAPL, BTC-USD"
            )
            simbolos = tuple(dict.fromkeys(
                t.strip().upper() for t in texto.split(",") if t.strip()
            ))
            if not 1 <= len(simbolos) <= 12:
                st.error("Especifique entre 1 y 12 símbolos.")
                st.stop()
            periodo = st.selectbox("Periodo histórico", list(PERIODOS), index=2)
            frecuencia = st.selectbox("Frecuencia de observación", list(FRECUENCIAS))
            campo = st.selectbox("Variable financiera", list(CAMPOS))
            try:
                bruto = yahoo_history(
                    simbolos, PERIODOS[periodo], FRECUENCIAS[frecuencia]
                )
            except Exception as exc:
                st.error(f"Error de descarga de Yahoo Finance: {exc}")
                st.stop()
            serie_nombre = st.selectbox("Activo que se analizará", simbolos)
            try:
                datos = _frame_from_market(bruto, serie_nombre, CAMPOS[campo])
            except (ValueError, KeyError) as exc:
                st.error(str(exc))
                st.stop()
            st.download_button(
                "Descargar las series financieras (CSV)",
                bruto.to_csv().encode("utf-8-sig"),
                file_name="series_yahoo_finance.csv",
                mime="text/csv",
            )
        else:
            archivo = st.file_uploader("Archivo con observaciones en formato CSV", type="csv")
            if archivo is None:
                st.info("Seleccione un archivo CSV para iniciar el análisis.")
                st.stop()
            bruto = pd.read_csv(archivo)
            numericas = bruto.select_dtypes(include="number").columns.tolist()
            if not numericas:
                st.error("El archivo no contiene columnas numéricas.")
                st.stop()
            serie_nombre = st.selectbox("Columna de la variable observada", numericas)
            fecha = st.selectbox(
                "Columna temporal (opcional)",
                ["Sin columna temporal"] + [
                    col for col in bruto.columns if col != serie_nombre
                ],
            )
            datos = pd.DataFrame({
                "observed": pd.to_numeric(bruto[serie_nombre], errors="coerce")
            })
            if fecha != "Sin columna temporal":
                datos["date"] = pd.to_datetime(bruto[fecha], errors="coerce")
            datos = datos.dropna().reset_index(drop=True)
            if "date" in datos:
                datos = datos.sort_values("date").reset_index(drop=True)

        st.header("2. Representación de la tendencia")
        modo_es = st.selectbox("Variable sobre la que se estima la tendencia", list(MODOS))
        modo_interno, unidad = MODOS[modo_es]
        try:
            transformados = transform_observations(datos, modo_interno)
        except ValueError as exc:
            st.error(f"No es posible aplicar esta transformación: {exc}")
            st.stop()
        max_obs = st.slider("Observaciones recientes utilizadas", 90, 600, 260, 10)
        transformados = transformados.tail(max_obs).reset_index(drop=True)

        st.header("3. Diseño de validación")
        orden = st.select_slider(
            "Orden de la penalización por diferencias, d",
            options=[1, 2, 3, 4], value=2,
        )
        ventana = st.slider("Longitud de la ventana de ajuste, L", 25, 160, 60, 5)
        horizonte = st.slider(
            "Horizonte de pronóstico por validación, h", 1, 20, 5
        )
        reserva = st.slider(
            "Número de observaciones reservadas para prueba", 1, 20, 5
        )
        paso = st.slider("Separación entre orígenes históricos", 1, 20, 5)
        origenes = st.slider("Máximo de orígenes históricos", 3, 30, 12)
        epsilon = st.slider(
            "Radio de continuidad entre ramas, ε", 0.02, 0.30, 0.10, 0.01
        )
        separacion = st.slider(
            "Separación mínima entre mínimos locales", 0.01, 0.10, 0.02, 0.01
        )
        regla = st.selectbox(
            "Regla de selección final de suavidad, φ(Vⱼ)",
            list(RULES), index=list(RULES).index("recency_hl3"),
            format_func=lambda clave: REGLAS.get(clave, clave),
        )
        resolucion = st.select_slider(
            "Número de niveles mostrados en la superficie",
            [21, 41, 61], value=41,
        )
        profundidad = st.select_slider(
            "Profundidad de búsqueda de mínimos", [3, 5, 8], value=5
        )
        st.caption(
            "Los órdenes 3 y 4 producen extrapolaciones polinomiales que "
            "pueden ser inestables. Los resultados deben interpretarse con cautela."
        )

    minimo = ventana + 3 * horizonte + reserva
    if len(transformados) < minimo:
        st.error(
            f"La serie contiene {len(transformados)} observaciones, pero este "
            f"diseño requiere al menos {minimo}. Amplíe la serie o reduzca L y h."
        )
        st.stop()

    observados = transformados["observed"].to_numpy(dtype=float)
    with st.spinner("Calculando las superficies de validación y las ramas de mínimos..."):
        try:
            resultado = analyze(
                tuple(observados),
                order=orden, window=ventana, horizon=horizonte,
                step=paso, max_origins=origenes, test_size=reserva,
                track_epsilon=epsilon, candidate_spacing=separacion,
                rule=regla, grid_points=resolucion, search_depth=profundidad,
            )
        except (ValueError, ArithmeticError, RuntimeError) as exc:
            st.error(f"No fue posible completar la estimación: {exc}")
            st.stop()

    st.subheader("Resultado del procedimiento de selección")
    columnas = st.columns(4)
    columnas[0].metric("Suavidad seleccionada, S", f"{resultado.final_s:.4f}")
    columnas[1].metric("Penalización correspondiente, λ", ("∞" if np.isinf(resultado.final_lambda) else f"{resultado.final_lambda:.4g}"))
    columnas[2].metric(
        "Suavidad de la validación agrupada", f"{resultado.pooled_s:.4f}"
    )
    columnas[3].metric(
        "Rama seleccionada", _nombre_rama(resultado.selected_branch)
    )
    estado = (
        "Se encontró una rama con continuidad hasta la validación final."
        if resultado.selected_branch != "none"
        else "No se encontró continuidad final: se utilizó el criterio agrupado."
    )
    st.caption(
        f"Serie: {serie_nombre} · Transformación: {modo_es} · "
        f"Observaciones: {len(observados)} · "
        f"Orígenes históricos: {resultado.tracks['origin'].nunique()} · "
        f"Orden d = {orden} · Ventana L = {ventana} · Horizonte h = {horizonte}. "
        + estado
    )
    with st.expander("Glosario breve de las cantidades representadas"):
        st.markdown(
            "**Suavidad (S):** índice normalizado entre 0 y 1. "
            "**ECM:** error cuadrático medio de pronóstico, calculado fuera "
            "de la ventana de ajuste. **RECM:** raíz del ECM. "
            "**Validación 1:** identifica los mínimos de la superficie predictiva. "
            "**Validación 2:** evalúa el pronóstico después del nuevo ajuste. "
            "**Rama:** sucesión de mínimos locales que persisten entre orígenes. "
            "**Hλ:** matriz de pesos que transforma observaciones en tendencias."
        )
    st.info(
        "**Cómo interpretar la suavidad:** S = 0 reproduce la serie dentro de "
        "la ventana; S = 1 corresponde al límite de máxima penalización, cuya "
        f"tendencia es un polinomio de grado {orden - 1}. "
        "El parámetro λ controla la intensidad de la penalización."
    )

    pestana_tendencia, pestana_superficie, pestana_ramas, pestana_matriz, pestana_csv = st.tabs([
        "Tendencia y pronóstico",
        "Errores de validación 1",
        "Ramas y validación 2",
        "Matriz de suavizamiento",
        "Tablas y descargas",
    ])

    with pestana_tendencia:
        st.subheader("Estimación de tendencia y pronóstico fuera de muestra")
        with st.expander("Distribución cronológica de los datos", expanded=True):
            st.plotly_chart(
                _grafica_cronologia(
                    len(observados), ventana=ventana, horizonte=horizonte,
                    paso=paso, reserva=reserva,
                ),
                use_container_width=True,
            )
            st.caption(
                "La primera fila histórica presenta un ajuste, una validación "
                "para localizar mínimos y otra para evaluar su pronóstico. "
                "La última validación 1 permite continuar la rama sin acceder "
                "a la prueba. Después, el modelo se ajusta de nuevo con las "
                "últimas L observaciones anteriores a la prueba. "
                "El bloque de prueba permanece fuera de la selección."
            )
        opciones = st.columns(3)
        vista_es = opciones[0].selectbox("Representación gráfica", list(VISTAS))
        mostrar_agrupado = opciones[1].checkbox(
            "Comparar con validación agrupada", True
        )
        revelar = opciones[2].checkbox(
            "Mostrar observaciones reservadas para prueba", False
        )
        opciones2 = st.columns(3)
        mostrar_latente = opciones2[0].checkbox(
            "Mostrar la tendencia verdadera de la simulación",
            value="latent" in transformados,
            disabled="latent" not in transformados,
        )
        manual = opciones2[1].slider(
            "Suavidad de comparación manual, S", 0.0, 1.0, 0.75, 0.01
        )
        limitar = opciones2[2].checkbox(
            "Ajustar el eje vertical a los datos históricos", True,
            help="Los pronósticos extremadamente alejados pueden quedar fuera del gráfico.",
        )
        st.plotly_chart(
            _grafica_serie(
                transformados, resultado, vista=VISTAS[vista_es],
                unidad=unidad, order=orden, manual_s=manual,
                revelar_prueba=revelar, mostrar_agrupado=mostrar_agrupado,
                mostrar_latente=mostrar_latente, limitar_escala=limitar,
            ),
            use_container_width=True,
        )
        st.caption(
            "**Lectura:** la tendencia se ajusta de nuevo usando las últimas "
            "L observaciones anteriores a la prueba. La línea vertical delimita "
            "el inicio del periodo reservado; las líneas discontinuas representan "
            "extrapolaciones, no datos observados. Si se limita el eje vertical, "
            "pueden ocultarse predicciones muy extremas."
        )
        if revelar:
            verdaderos = observados[resultado.pretest_end:resultado.test_end]
            e_dinamico = float(np.mean((verdaderos - resultado.forecast)**2))
            e_agrupado = float(np.mean((verdaderos - resultado.pooled_forecast)**2))
            st.markdown("**Diagnóstico fuera de muestra (exclusivamente evaluación)**")
            c1, c2 = st.columns(2)
            c1.metric("ECM de prueba: método dinámico", f"{e_dinamico:.5g}")
            c2.metric("ECM de prueba: validación agrupada", f"{e_agrupado:.5g}")
            st.caption(
                "Estas observaciones se revelan después de la selección y no "
                "intervienen en el cálculo de S, la elección de rama ni el ajuste."
            )
        tabla_serie = transformados.rename(columns={
            "date": "Fecha", "t": "Tiempo",
            "observed": "Serie observada", "latent": "Tendencia verdadera",
        })
        _descarga(
            "Descargar la serie utilizada (CSV)", tabla_serie,
            "serie_temporal_transformada.csv",
        )

    with pestana_superficie:
        st.subheader("Pérdida predictiva según el grado de suavizamiento")
        st.write(
            "El **error cuadrático medio (ECM)** de validación 1 mide la "
            "discrepancia entre el pronóstico y las observaciones posteriores "
            "a cada ventana de ajuste. Un valor menor indica menor error "
            "predictivo en ese origen."
        )
        relativa = st.checkbox(
            "Colorear el ECM relativo al mínimo de cada origen",
            value=True,
            help=(
                "En modo relativo, 1 corresponde al menor ECM del origen. "
                "Al pasar el cursor se muestra también el ECM original."
            ),
        )
        st.plotly_chart(
            _grafica_superficie(resultado, relativa=relativa),
            use_container_width=True,
        )
        st.caption(
            "**Lectura:** cada fila es un origen cronológico de pronóstico; "
            "cada columna es un nivel de suavidad S. Los colores indican el ECM "
            "de validación 1 (o la razón respecto al menor ECM de esa fila). "
            "Las líneas superpuestas conectan mínimos locales: la rama "
            "seleccionada aparece resaltada en blanco. Un color favorable "
            "no equivale por sí solo al mejor resultado en prueba."
        )
        log_ecm = st.checkbox(
            "Emplear escala logarítmica para el ECM del último origen", False
        )
        st.plotly_chart(
            _grafica_ultimo_origen(resultado, escala_log=log_ecm),
            use_container_width=True,
        )
        st.caption(
            "**Lectura:** los rombos son mínimos locales detectados "
            "numéricamente, mientras que las líneas verticales representan "
            "la suavidad final producida por φ y la referencia agrupada. "
            "Es normal que la suavidad final de una rama no coincida "
            "exactamente con un mínimo de esta última superficie."
        )
        st.markdown("**Mínimos locales recuperados en el último origen**")
        st.dataframe(_espanol(resultado.candidates), use_container_width=True,
                     hide_index=True)

    with pestana_ramas:
        st.subheader("Persistencia de los mínimos locales y validación independiente")
        st.write(
            "Cada **rama** enlaza mínimos cercanos en orígenes consecutivos, "
            "sin utilizar la prueba. La **validación 2** mide el error del "
            "pronóstico obtenido tras ajustar nuevamente el modelo incluyendo "
            "la primera validación."
        )
        st.plotly_chart(
            _grafica_ramas(resultado, variable="smoothness"),
            use_container_width=True,
        )
        st.caption(
            "**Lectura:** el eje vertical indica el nivel de suavidad elegido "
            "por cada mínimo local (entre 0 y 1). Una interrupción significa "
            "que no se encontró una correspondencia dentro del radio ε; "
            "no significa que el ECM haya sido cero."
        )
        val2_log = st.checkbox(
            "Escala logarítmica para el ECM de validación 2", False
        )
        st.plotly_chart(
            _grafica_ramas(
                resultado, variable="val2_mse", escala_log=val2_log
            ),
            use_container_width=True,
        )
        st.caption(
            "**Lectura:** valores más bajos de ECM indican mayor precisión "
            "en validación 2. La elección de rama utiliza continuidad "
            "histórica y **RECM media** de validación 2; el gráfico presenta "
            "ECM para mostrar los errores cuadráticos."
        )
        st.markdown("**Resumen comparativo de las ramas**")
        resumen = resultado.summary.copy()
        resumen["branch_id"] = resumen["branch_id"].map(_nombre_rama)
        st.dataframe(_espanol(resumen), use_container_width=True, hide_index=True)
        rama = st.selectbox(
            "Rama cuya matriz histórica se desea consultar",
            sorted(resultado.tracks["branch_id"].unique()),
            format_func=_nombre_rama,
        )
        historia = resultado.tracks.loc[
            resultado.tracks["branch_id"].eq(rama),
            ["origin", "smoothness", "val1_mse", "val2_mse", "val2_rmse", "status"],
        ]
        st.markdown("**Matriz histórica de la rama: Vⱼ = [S, ℓ₁, ℓ₂]**")
        st.dataframe(_espanol(historia), use_container_width=True, hide_index=True)
        st.caption(
            "En la matriz Vⱼ, S es la suavidad del mínimo local; ℓ₁ es el "
            "ECM de validación 1 y ℓ₂ es el ECM de validación 2. "
            "La RECM es la raíz cuadrada del ECM correspondiente."
        )
        _descarga(
            "Descargar la matriz histórica de la rama (CSV)",
            _espanol(historia), f"matriz_historica_{rama}.csv",
        )

    with pestana_matriz:
        st.subheader("Operador lineal de suavizamiento")
        st.latex(r"H_{\lambda}=(I+\lambda D_d^{\mathsf T}D_d)^{-1},"
                 r"\qquad \widehat{\boldsymbol\tau}=H_{\lambda}\mathbf y")
        st.write(
            "El elemento **Hᵢⱼ** representa el peso de la observación original "
            "j en la estimación de la tendencia correspondiente al instante i. "
            "No es una matriz de errores ni de correlaciones."
        )
        c1, c2 = st.columns(2)
        procedencia = c1.radio(
            "Suavidad empleada en la matriz",
            ["Suavidad seleccionada", "Suavidad manual"],
            horizontal=True,
        )
        magnitud = c2.checkbox(
            "Mostrar magnitudes absolutas de los pesos", False,
            help="Los signos se conservan en el valor consultado al pasar el cursor.",
        )
        s_matriz = (
            resultado.final_s if procedencia == "Suavidad seleccionada" else manual
        )
        H = smoothing_matrix(ventana, orden, s_matriz)
        st.plotly_chart(
            _grafica_matriz(H, solo_magnitud=magnitud),
            use_container_width=True,
        )
        st.caption(
            "**Lectura:** la diagonal muestra cuánto influye cada observación "
            "sobre su propia tendencia estimada; los elementos fuera de la "
            "diagonal representan la influencia de otros instantes. "
            "El contraste entre ambos revela cuánta información temporal "
            "combina el suavizador."
        )
        traza = float(np.trace(H))
        suave_real = (ventana - traza) / (ventana - orden)
        a, b, c = st.columns(3)
        a.metric("Grados de libertad efectivos: tr(H)", f"{traza:.3f}")
        b.metric("Índice normalizado de suavidad, S", f"{suave_real:.4f}")
        c.metric("Error máximo de simetría", f"{np.max(np.abs(H-H.T)):.2e}")
        st.latex(r"S=\frac{L-\operatorname{tr}(H_{\lambda})}{L-d},"
                 r"\qquad 0\le S\le 1")
        st.caption(
            "Una traza alta indica mayor flexibilidad para seguir los datos; "
            "una traza cercana a d corresponde a un ajuste muy suave. "
            "La matriz depende de L, d y λ, no de los valores observados."
        )
        _descarga(
            "Descargar la matriz de suavizamiento H (CSV)",
            pd.DataFrame(H), "matriz_suavizamiento.csv",
        )

    with pestana_csv:
        st.subheader("Resultados numéricos y archivos reproducibles")
        st.write(
            "Las tablas conservan los valores numéricos originales. "
            "Se presentan con encabezados en español para facilitar "
            "la interpretación."
        )
        st.dataframe(_espanol(resultado.tracks), use_container_width=True,
                     hide_index=True)
        _descarga(
            "Descargar historial completo de ramas (CSV)",
            _espanol(resultado.tracks), "validacion_ramas.csv",
        )
        superficies_es = resultado.surfaces.rename(columns={
            "origin": "Origen de validación",
            "smoothness": "Suavidad normalizada, S",
            "val1_mse": "ECM de validación 1",
        })
        _descarga(
            "Descargar superficies del ECM de validación 1 (CSV)",
            superficies_es, "superficies_validacion_1.csv",
        )
        _descarga(
            "Descargar resumen de ramas (CSV)",
            _espanol(resultado.summary), "resumen_ramas.csv",
        )
        pronosticos = pd.DataFrame({
            "Observación": np.arange(
                resultado.pretest_end + 1, resultado.test_end + 1
            ),
            "Pronóstico del método dinámico": resultado.forecast,
            "Pronóstico de validación agrupada": resultado.pooled_forecast,
            "Observación real de prueba":
                observados[resultado.pretest_end:resultado.test_end],
        })
        _descarga(
            "Descargar pronósticos y observaciones de prueba (CSV)",
            pronosticos, "pronosticos_prueba.csv",
        )
        st.caption(
            "El último archivo contiene los valores reservados para la prueba. "
            "Su disponibilidad para descarga no implica que se hayan "
            "utilizado en la selección del modelo."
        )
        st.info(
            "Esta aplicación tiene fines exploratorios y no modifica los "
            "resultados congelados de los experimentos CP03–CP08. "
            "La superficie de referencia agrupada se calcula con una "
            "cuadrícula discreta y los parámetros de búsqueda son ajustables."
        )


if __name__ == "__main__":
    main()
