"""Aplicación principal: selección de orden y suavidad en dos validaciones.

Ejecutar: streamlit run apps/smoothness_lab.py
Análisis avanzado de ramas: streamlit run apps/smoothness_lab_advanced.py
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
def analyze(values: tuple[float, ...], **kwargs):
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
    a, b, c, e, n = (
        result.val1_start, result.val1_end,
        result.val2_end, result.pretest_end, result.test_end,
    )
    spans = [
        (3, a-L, a, "Ajuste inicial", "#737373"),
        (3, a, b, "Validación 1", COLORES_D[1]),
        (2, b-L, b, "Nuevo ajuste", "#737373"),
        (2, b, c, "Validación 2", COLORES_D[3]),
        (1, e-L, e, "Ajuste final", "#737373"),
        (1, e, n, "Prueba reservada", COLORES_D[2]),
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
        tickmode="array", tickvals=[1, 2, 3],
        ticktext=["Ajuste definitivo y prueba", "Selección en validación 2",
                  "Búsqueda en validación 1"],
        range=[0.5, 3.5], showgrid=False,
    )
    fig.update_xaxes(range=[0, n+1])
    return fig


def _val1_figure(result, order: int) -> go.Figure:
    curve = result.surfaces.loc[result.surfaces["d"].eq(order)]
    minima = result.candidates.loc[result.candidates["d"].eq(order)]
    selected = minima.loc[minima["rank"].eq(1)]
    fig = go.Figure()
    fig.add_scatter(
        x=curve["smoothness"], y=curve["val1_mse"],
        mode="lines", name="Superficie del ECM de validación 1",
        line={"color": COLORES_D[order], "width": 2.4},
    )
    fig.add_scatter(
        x=minima["smoothness"], y=minima["val1_mse"],
        mode="markers", name="Mínimos locales candidatos",
        marker={"symbol": "diamond", "color": "#3F3F46", "size": 9},
        hovertemplate="S = %{x:.4f}<br>ECM = %{y:.6g}<extra></extra>",
    )
    if not selected.empty:
        fig.add_scatter(
            x=selected["smoothness"], y=selected["val1_mse"],
            mode="markers", name="Candidato seleccionado en validación 2",
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


def _forecast_figure(frame: pd.DataFrame, result, unidad: str, *,
                     reveal: bool, truth: bool) -> go.Figure:
    x, label_x = _axis(frame)
    y = frame["observed"].to_numpy(dtype=float)
    a, e, n = result.train_start, result.pretest_end, result.test_end
    fig = go.Figure()
    fig.add_scatter(
        x=x[:e], y=y[:e], mode="lines", name="Serie observada anterior a la prueba",
        line={"color": "#656565", "width": 1.75},
    )
    if truth and "latent" in frame:
        fig.add_scatter(
            x=x[:e], y=frame["latent"].to_numpy(dtype=float)[:e],
            mode="lines", name="Componente verdadera de la simulación",
            line={"color": "#9C6BB3", "dash": "dot", "width": 1.8},
        )
    fig.add_scatter(
        x=x[a:e], y=result.trend,
        mode="lines", name=f"Tendencia reajustada (d = {result.selected_order})",
        line={"color": "#D55E00", "width": 3},
    )
    fig.add_scatter(
        x=x[e:n], y=result.forecast,
        mode="lines+markers", name=f"Pronóstico con S = {result.selected_s:.4f}",
        marker={"size": 8},
        line={"color": "#D55E00", "width": 2.8, "dash": "dash"},
    )
    if reveal:
        fig.add_scatter(
            x=x[e:n], y=y[e:n], mode="lines+markers",
            name="Observaciones de prueba (solo evaluación)",
            marker={"size": 7},
            line={"color": "#202020", "dash": "dot", "width": 1.8},
        )
    if e < n:
        fig.add_vrect(
            x0=x[e], x1=x[n-1], fillcolor="#E5E7EB",
            opacity=0.5, line_width=0, layer="below",
        )
        fig.add_vline(x=x[e], line_dash="dot", line_color="#858585")
    return _style(
        fig, "Tendencia estimada y pronóstico desde el último origen",
        label_x, unidad, height=540,
    )


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


def main() -> None:
    st.set_page_config(page_title="Selección de suavidad y orden", layout="wide")
    st.title("Selección predictiva de la suavidad y el orden de tendencia")
    st.caption(
        "Mínimos cuadrados penalizados · validación cronológica en dos etapas · "
        "pronóstico desde el último origen disponible."
    )
    st.markdown(
        "**Validación 1:** detectar todos los mínimos locales de suavidad para "
        "cada orden. **Validación 2:** seleccionar el par (orden, suavidad) "
        "con el menor error predictivo. **Pronóstico final:** reajustar el "
        "mismo modelo utilizando las últimas observaciones anteriores a la prueba."
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

        st.header("3. Diseño de las dos validaciones")
        ordenes = st.multiselect(
            "Órdenes de diferencias que se compararán, d",
            [1, 2, 3, 4], default=[1, 2, 3, 4],
        )
        L = st.slider("Observaciones por ventana de ajuste, L", 25, 160, 60, 5)
        h = st.slider("Horizonte de cada validación, h", 1, 20, 5)
        test_size = st.slider(
            "Observaciones reservadas para la prueba", 1, 20, 5
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
        st.caption(
            "Los órdenes altos pueden producir pronósticos inestables. "
            "La elección se realiza exclusivamente con validación 2."
        )

    if not ordenes:
        st.error("Seleccione al menos un orden d.")
        st.stop()
    minimo = L + 2 * h + test_size
    if len(frame) < minimo:
        st.error(
            f"El diseño necesita al menos {minimo} observaciones. "
            f"Solo hay {len(frame)} disponibles."
        )
        st.stop()
    valores = frame["observed"].to_numpy(dtype=float)
    with st.spinner("Buscando mínimos y evaluándolos en la segunda validación..."):
        try:
            resultado = analyze(
                tuple(valores), orders=tuple(sorted(ordenes)), window=L,
                horizon=h, test_size=test_size, candidate_spacing=spacing,
                grid_points=grid, search_depth=depth,
            )
        except (ValueError, ArithmeticError, RuntimeError) as exc:
            st.error(f"La selección no pudo completarse: {exc}")
            st.stop()

    st.subheader("Modelo seleccionado mediante validación 2")
    metricas = st.columns(4)
    metricas[0].metric("Orden seleccionado, d*", str(resultado.selected_order))
    metricas[1].metric("Suavidad seleccionada, S*", f"{resultado.selected_s:.4f}")
    metricas[2].metric("ECM de validación 2", f"{resultado.selected_val2_mse:.5g}")
    metricas[3].metric("Mínimos candidatos evaluados", len(resultado.candidates))
    st.caption(
        f"Serie: {serie} · Transformación: {transformacion_es} · "
        f"Método: {resultado.method} · Ventana L = {L} · "
        f"Horizonte h = {h}. Ninguna observación de prueba intervino en la selección."
    )

    tab_diseno, tab_val1, tab_val2, tab_final, tab_h = st.tabs([
        "División cronológica",
        "Validación 1: mínimos de S",
        "Validación 2: elección de d y S",
        "Tendencia y pronóstico",
        "Matriz de suavizamiento",
    ])

    with tab_diseno:
        st.subheader("Bloques utilizados para estimar y seleccionar")
        st.plotly_chart(_timeline(resultado), use_container_width=True)
        st.write(
            "**Ajuste inicial:** últimas L observaciones antes de validación 1. "
            "**Validación 1:** para cada d se construye una curva ECM(S) y se "
            "recuperan todos sus mínimos locales. **Nuevo ajuste:** se utilizan "
            "las últimas L observaciones hasta el final de validación 1. "
            "**Validación 2:** se evalúan los candidatos sobre el bloque siguiente. "
            "**Ajuste final:** con d* y S* ya elegidos, se utilizan las últimas "
            "L observaciones anteriores a la prueba. La prueba nunca se utiliza "
            "para elegir d ni S."
        )
        st.latex(
            r"(d^*,S^*)=\underset{d,\;S\in\mathcal M_d}"
            r"{\operatorname{arg\,min}}\;\operatorname{ECM}_2(d,S)"
        )

    with tab_val1:
        st.subheader("Superficies de pérdida predictiva y mínimos locales")
        st.write(
            "Para cada orden de diferencias d, los rombos indican los mínimos "
            "locales de la función de error de pronóstico en validación 1. "
            "Cada mínimo se conserva como candidato para validación 2, "
            "incluso cuando no es el mínimo global."
        )
        for order in sorted(ordenes):
            st.plotly_chart(_val1_figure(resultado, order),
                            use_container_width=True)
        st.caption(
            "El algoritmo recupera mínimos con derivadas; las líneas son "
            "una visualización muestreada de la función de error. "
            "Los extremos S = 0 y S = 1 se consideran cuando son candidatos."
        )

    with tab_val2:
        st.subheader("Selección por el menor ECM de la segunda validación")
        st.plotly_chart(_val2_figure(resultado), use_container_width=True)
        st.write(
            "Cada punto corresponde a un par (d, S) recuperado en validación 1. "
            "Antes de pronosticar validación 2 se **reajusta la tendencia** "
            "incorporando las observaciones de validación 1. "
            "La estrella negra identifica el menor ECM de validación 2."
        )
        st.markdown("**Matriz de comparación de candidatos**")
        st.dataframe(_table(resultado.candidates),
                     use_container_width=True, hide_index=True)
        st.caption(
            "ECM: error cuadrático medio. RECM: raíz del error cuadrático medio. "
            "Todos los candidatos se evalúan en el mismo bloque temporal. "
            "Actualmente solo se compara el método de mínimos cuadrados "
            "penalizados; la comparación de otros estimadores es una posible extensión."
        )
        st.download_button(
            "Descargar la matriz de candidatos (CSV)",
            _table(resultado.candidates).to_csv(index=False).encode("utf-8-sig"),
            file_name="candidatos_validacion_2.csv", mime="text/csv",
        )

    with tab_final:
        st.subheader("Pronóstico utilizando el orden y la suavidad seleccionados")
        left, right = st.columns(2)
        revelar = left.checkbox(
            "Mostrar las observaciones reservadas para prueba", False
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
        st.caption(
            "Se conservan el **orden d*** y la **suavidad S*** seleccionados. "
            "El modelo se vuelve a estimar con la última ventana de L "
            "observaciones anteriores a la prueba. Los puntos discontinuos "
            "constituyen el pronóstico desde el último origen conocido."
        )
        if revelar:
            test = valores[resultado.pretest_end:resultado.test_end]
            mse = float(np.mean((test - resultado.forecast)**2))
            st.metric("ECM en prueba no utilizada para selección", f"{mse:.6g}")
            st.caption(
                "La prueba es exclusivamente una evaluación posterior. "
                "Su valor no modifica d*, S* ni las predicciones."
            )
        pronosticos = pd.DataFrame({
            "Número de observación": np.arange(
                resultado.pretest_end+1, resultado.test_end+1
            ),
            "Pronóstico": resultado.forecast,
            "Observación de prueba": valores[
                resultado.pretest_end:resultado.test_end
            ],
        })
        st.download_button(
            "Descargar pronósticos y prueba (CSV)",
            pronosticos.to_csv(index=False).encode("utf-8-sig"),
            file_name="pronostico_fuera_de_muestra.csv", mime="text/csv",
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

    with st.expander("Análisis avanzado: persistencia histórica de ramas"):
        st.write(
            "El seguimiento de mínimos a través de muchos orígenes y las "
            "reglas dinámicas φ(Vⱼ) son una **extensión opcional**, no intervienen "
            "en el procedimiento de dos validaciones presentado arriba. "
            "La implementación anterior se conserva en "
            "apps/smoothness_lab_advanced.py."
        )


if __name__ == "__main__":
    main()
