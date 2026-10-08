"""Standalone visual laboratory for pooled horizon-matched smoothness CV.

Run from repository root:
    python -m pip install -e ".[dashboard,finance]"
    streamlit run apps/pooled_forecast_cv.py

This app deliberately does NOT do branch tracking or change the older apps.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from experiments.smoothness_cv.live_lab import make_synthetic, transform_observations
from experiments.smoothness_cv.article_simulations import (
    ARTICLE_TRENDS, make_article_synthetic,
)
from experiments.smoothness_cv.full_series import smooth_full_series
from experiments.smoothness_cv.pooled_lab import (
    analyze_pooled,
    fit_window_forecast,
)
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.core.smoothness import smoothness_to_lambda

COLOR = {
    "Pooled CV": "#0072B2",
    "Last fold": "#D55E00",
    "One-step CV": "#009E73",
    "Manual S": "#9867AD",
    "Observed": "#595959",
}
EXPRESSIONS = {
    "Linear + seasonal": "10 + 0.018*t + 1.0*sin(t/16)",
    "Slope change": "10 + 0.012*t + where(t>140, 0.05*(t-140), 0)",
    "Turning point": "10 + 0.00022*(t-160)**2 + 0.5*sin(t/20)",
    "Nonlinear + cycles": "10 + 0.025*t + 1.5*sin(t/27) + 0.4*cos(t/8)",
    "Flat + level shift": "10 + where(t>135, 3, 0) + 0.5*cos(t/13)",
    "Custom formula": "10 + 0.018*t + sin(t/16)",
}
NOISE = ["Gaussian", "Laplace", "Student-t (df=5)", "Heteroskedastic"]
TRANSFORMS = {
    "Original level": "Level",
    "Log level": "Log level",
    "Indexed to 100": "Indexed to 100",
    "Simple returns": "Simple return",
    "Log returns": "Log return",
}


@st.cache_data(ttl=3600, show_spinner=False, max_entries=12)
def yahoo_data(ticker: str, period: str, interval: str, field: str) -> pd.DataFrame:
    import yfinance as yf

    raw = yf.download(
        ticker, period=period, interval=interval, auto_adjust=True,
        progress=False, threads=False,
    )
    if raw.empty:
        raise ValueError("Yahoo Finance returned no observations.")
    if isinstance(raw.columns, pd.MultiIndex):
        try:
            series = raw.xs(field, axis=1, level=0).iloc[:, 0]
        except KeyError:
            series = raw.xs(field, axis=1, level=-1).iloc[:, 0]
    else:
        if field not in raw.columns:
            raise ValueError(f"Yahoo Finance has no {field} column.")
        series = raw[field]
    series = pd.to_numeric(series, errors="coerce").dropna()
    if len(series) < 15:
        raise ValueError("Not enough numeric observations were returned.")
    return pd.DataFrame({
        "date": pd.to_datetime(series.index).tz_localize(None)
        if getattr(series.index, "tz", None) is not None
        else pd.to_datetime(series.index),
        "observed": series.to_numpy(float),
    })


@st.cache_data(show_spinner=False, max_entries=24)
def cached_result(
    observations: tuple[float, ...],
    window: int, order: int, horizon: int, stride: int,
    folds: int, grid: int, refine: bool, holdout: bool, one_step: bool,
):
    return analyze_pooled(
        np.asarray(observations),
        window=window, order=order, horizon=horizon, stride=stride,
        max_folds=folds, grid_points=grid, refine=refine,
        holdout=holdout, compare_one_step=one_step,
    )


def style(fig: go.Figure, x: str, y: str, height: int = 415) -> go.Figure:
    fig.update_layout(
        template="plotly_white", height=height,
        margin=dict(l=35, r=25, t=28, b=60),
        xaxis_title=x, yaxis_title=y,
        hovermode="closest",
        legend=dict(orientation="h", y=-0.26, x=0),
    )
    fig.update_xaxes(showgrid=True, gridcolor="#EEEEEE")
    fig.update_yaxes(showgrid=True, gridcolor="#EEEEEE")
    return fig


def preview_series(frame: pd.DataFrame, T: int) -> go.Figure:
    fig = go.Figure()
    x = np.arange(1, len(frame) + 1)
    y = frame["observed"].to_numpy(float)
    fig.add_scatter(
        x=x[:T], y=y[:T], mode="lines",
        name="Observed available at the selection origin",
        line=dict(color=COLOR["Observed"], width=1.9),
    )
    if T < len(y):
        fig.add_scatter(
            x=x[T - 1:], y=y[T - 1:], mode="lines+markers",
            name="Outer holdout (not used for selection)",
            line=dict(color="#C57B35", dash="dot", width=2),
        )
        fig.add_vline(x=T + 0.5, line_dash="dash", line_color="#C57B35")
    if "latent" in frame:
        fig.add_scatter(
            x=x, y=frame["latent"], mode="lines",
            name="Known synthetic latent signal (display only)",
            line=dict(color="#9867AD", dash="dot", width=1.4),
        )
    return style(fig, "Observation number", "Transformed observation", 290)


def loss_curves(result, focus: int, show_all: bool, log_y: bool) -> go.Figure:
    fig = go.Figure()
    grid = result.grid
    if show_all:
        for i, loss in enumerate(result.fold_losses):
            fig.add_scatter(
                x=grid, y=loss, mode="lines",
                name=f"F fold {i + 1}", legendgroup="folds",
                showlegend=(i == 0),
                line=dict(color="rgba(100,100,100,0.23)", width=1.4),
                hovertemplate=(
                    f"Fold {i + 1}<br>S=%{{x:.4f}}<br>MSE=%{{y:.5g}}<extra></extra>"
                ),
            )
    i = focus - 1
    fig.add_scatter(
        x=grid, y=result.fold_losses[i], mode="lines",
        name=f"Selected fold {focus}",
        line=dict(color=COLOR["Last fold"], width=2.5),
    )
    fig.add_scatter(
        x=grid, y=result.pooled_losses, mode="lines",
        name=f"Pooled F (mean of {len(result.origins)} folds)",
        line=dict(color=COLOR["Pooled CV"], width=3.7),
    )
    fig.add_scatter(
        x=[result.pooled_s], y=[result.pooled_mse],
        name=f"Pooled minimum S={result.pooled_s:.4f}",
        mode="markers", marker=dict(size=13, symbol="star", color=COLOR["Pooled CV"]),
    )
    fig.add_scatter(
        x=[result.last_s], y=[result.last_validation_mse],
        name=f"Last fold minimum S={result.last_s:.4f}",
        mode="markers", marker=dict(size=11, symbol="diamond", color=COLOR["Last fold"]),
    )
    fig = style(fig, "Normalized smoothness S ∈ [0,1]", "Forecast validation MSE", 530)
    fig.update_xaxes(range=[0, 1])
    if log_y and np.all(result.fold_losses > 0):
        fig.update_yaxes(type="log")
    return fig


def loss_heatmap(result, log_color: bool) -> go.Figure:
    z = result.fold_losses
    if log_color:
        z = np.log10(np.maximum(z, 1e-15))
    fig = go.Figure(go.Heatmap(
        x=result.grid,
        y=np.arange(1, len(result.origins) + 1),
        z=z, colorscale="Viridis", colorbar=dict(title="log10 MSE" if log_color else "MSE"),
        hovertemplate="Fold %{y}<br>S=%{x:.4f}<br>Display value=%{z:.5g}<extra></extra>",
    ))
    fig.add_scatter(
        x=result.fold_grid_minima,
        y=np.arange(1, len(result.origins) + 1),
        mode="markers", name="Grid minimum per fold",
        marker=dict(symbol="x", size=8, color="white", line=dict(width=1)),
    )
    fig.add_vline(x=result.pooled_s, line_color="white", line_width=1.6, line_dash="dash")
    return style(fig, "Candidate S", "Historical fold (oldest → newest)", 475)


def split_timeline(result) -> go.Figure:
    fig = go.Figure()
    for j, t in enumerate(result.origins, start=1):
        fig.add_scatter(
            x=[t - result.window + 1, t], y=[j, j],
            mode="lines", showlegend=(j == 1), name="Trend fit window",
            line=dict(color="#648DAE", width=7),
            hovertemplate=f"Fold {j}: fit ends at observation {t}<extra></extra>",
        )
        fig.add_scatter(
            x=[t + 1, t + result.horizon], y=[j, j],
            mode="lines", showlegend=(j == 1), name="Realized validation future",
            line=dict(color="#DDA050", width=7),
            hovertemplate=(
                f"Fold {j}: validation observations {t + 1}–{t + result.horizon}"
                "<extra></extra>"
            ),
        )
    fig.add_vline(
        x=result.selected_origin + 0.5, line_dash="dash", line_color="#202020",
    )
    fig = style(fig, "Observation number (not calendar days)", "Fold", max(300, min(760, 170 + len(result.origins) * 16)))
    fig.update_yaxes(dtick=1 if len(result.origins) <= 18 else None)
    return fig


def final_forecasts(
    observed: np.ndarray, result, manual_s: float, show: list[str]
) -> tuple[go.Figure, dict[str, np.ndarray]]:
    T, L, h = result.selected_origin, result.window, result.horizon
    methods = dict(result.future_forecasts)
    manual_trend, manual_forecast = fit_window_forecast(
        observed[:T], origin=T, window=L, order=result.order,
        horizon=h, smoothness=manual_s,
    )
    methods["Manual S"] = manual_forecast
    trends = {**result.final_trends, "Manual S": manual_trend}
    x_history = np.arange(1, T + 1)
    x_forecast = np.arange(T + 1, T + h + 1)
    fig = go.Figure()
    fig.add_scatter(
        x=x_history, y=observed[:T], mode="lines", name="Observed history",
        line=dict(color=COLOR["Observed"], width=1.5),
    )
    if result.holdout:
        fig.add_scatter(
            x=x_forecast, y=observed[T:T + h], mode="lines+markers",
            name="Actual held-out observations (scoring only)",
            line=dict(color="#202020", dash="dot", width=2.2),
        )
    for method in show:
        if method not in methods:
            continue
        color = COLOR[method]
        fig.add_scatter(
            x=np.arange(T - L + 1, T + 1), y=trends[method],
            mode="lines", name=f"{method}: refitted trend",
            line=dict(color=color, width=2.6),
        )
        fig.add_scatter(
            x=np.r_[T, x_forecast], y=np.r_[trends[method][-1], methods[method]],
            mode="lines+markers", name=f"{method}: future polynomial forecast",
            line=dict(color=color, dash="dash", width=2.3),
        )
    fig.add_vline(x=T + 0.5, line_dash="dash", line_color="#888888")
    fig = style(fig, "Observation number", "Transformed observation", 530)
    fig.update_xaxes(range=[max(0, T - max(2 * L, 120)), T + h + 2])
    return fig, methods


def historical_fold_preview(y: np.ndarray, result, fold_index: int) -> go.Figure:
    t = int(result.origins[fold_index])
    L, h = result.window, result.horizon
    fig = go.Figure()
    fig.add_scatter(
        x=np.arange(t - L + 1, t + h + 1), y=y[t - L:t + h],
        mode="lines+markers", name="Historical observed + realized future",
        line=dict(color="#555555", width=1.8),
    )
    for label, s in (("Pooled CV", result.pooled_s), ("Last fold", result.last_s),
                     ("Fold grid minimum", float(result.fold_grid_minima[fold_index]))):
        trend, forecast = fit_window_forecast(
            y, origin=t, window=L, order=result.order,
            horizon=h, smoothness=float(s),
        )
        color = "#9467BD" if label == "Fold grid minimum" else COLOR[label]
        fig.add_scatter(
            x=np.arange(t - L + 1, t + 1), y=trend,
            name=f"{label}: historical fit", mode="lines",
            line=dict(color=color, width=2),
        )
        fig.add_scatter(
            x=np.arange(t, t + h + 1),
            y=np.r_[trend[-1], forecast], name=f"{label}: fold forecast",
            mode="lines+markers", line=dict(color=color, dash="dash", width=2),
        )
    fig.add_vline(x=t + 0.5, line_dash="dash", line_color="#888888")
    return style(fig, "Observation number", "Transformed observation", 440)


def spectral_plot(result) -> go.Figure:
    solver = cached_pure_solver(result.window, result.order)
    eigvals = solver.eigvals
    lam = result.selected_lambda
    filt = np.zeros_like(eigvals) if np.isinf(lam) else 1 / (1 + lam * eigvals)
    if np.isinf(lam):
        filt[:result.order] = 1.0
    fig = go.Figure()
    fig.add_scatter(
        x=np.arange(1, len(filt) + 1), y=filt,
        mode="lines+markers", name="Spectral shrinkage 1/(1+λδ)",
        line=dict(color=COLOR["Pooled CV"], width=2),
    )
    fig.add_hline(y=1.0, line_dash="dot", line_color="#888888")
    return style(fig, "Penalty eigen-direction (ascending δ)", "Smoother eigenvalue", 335)


@st.cache_data(show_spinner=False, max_entries=16)
def cached_full_series(values: tuple[float, ...], order: int, smoothness: float) -> np.ndarray:
    return smooth_full_series(
        np.asarray(values, dtype=float), order=order, smoothness=smoothness,
    )


def complete_trend_plot(
    frame: pd.DataFrame, trend: np.ndarray, *, order: int, smoothness: float,
) -> go.Figure:
    x = frame["date"] if "date" in frame.columns else np.arange(1, len(frame) + 1)
    fig = go.Figure()
    fig.add_scatter(
        x=x, y=frame["observed"], name="Serie observada completa",
        mode="lines", line={"color": COLOR["Observed"], "width": 1.6},
    )
    fig.add_scatter(
        x=x, y=trend,
        name=f"Tendencia completa (d={order}, S={smoothness:.4f})",
        mode="lines", line={"color": COLOR["Pooled CV"], "width": 3},
    )
    if "latent" in frame:
        fig.add_scatter(
            x=x, y=frame["latent"], mode="lines",
            name="Tendencia verdadera de la simulación",
            line={"color": "#9867AD", "dash": "dot", "width": 1.7},
        )
    return style(
        fig, "Fecha" if "date" in frame else "Número de observación",
        "Observaciones y tendencia suavizada (ajuste completo)", 465,
    )


def main() -> None:
    st.set_page_config(page_title="CV · Promedio histórico de F(S)", layout="wide")
    st.title("Laboratorio de CV · Promedio histórico de F(S)")
    st.caption(
        "Se minimiza el promedio de las funciones de pérdida F_t(S) de "
        "los orígenes históricos. No se siguen mínimos ni ramas dinámicas; "
        "este procedimiento es distinto del laboratorio de ramas."
    )

    with st.sidebar:
        st.header("1 · Data")
        source = st.radio("Data source", ["Synthetic function", "Yahoo Finance", "Upload CSV"])
        frame = None
        try:
            if source == "Synthetic function":
                preset = st.selectbox(
                    "Function / Función generadora",
                    list(ARTICLE_TRENDS) + list(EXPRESSIONS),
                )
                if preset in ARTICLE_TRENDS:
                    kind = ARTICLE_TRENDS[preset]
                    st.latex(
                        r"\tau_t=\frac{4t}{N}" if kind == "linear"
                        else r"\tau_t=0.6\beta_{30,17}(t/N)+0.4\beta_{3,11}(t/N)"
                    )
                    n = st.slider(
                        "Número de observaciones, N", min_value=50,
                        max_value=200, value=200, step=10,
                        key="pooled_articulo_n",
                    )
                    noise_sd = st.slider(
                        "Desviación estándar del ruido gaussiano, σ",
                        min_value=0.5, max_value=2.0, value=0.5, step=0.05,
                        key="pooled_articulo_sigma",
                    )
                    seasonality = st.checkbox(
                        "Estacionalidad trimestral aditiva",
                        value=False, key="pooled_articulo_estacionalidad",
                    )
                    seed = st.number_input(
                        "Random seed / Semilla", 0, 100_000, 42,
                        key="pooled_articulo_semilla",
                    )
                    frame = make_article_synthetic(
                        kind, n=n, noise_sd=noise_sd,
                        seasonality=seasonality, seed=int(seed),
                    )
                else:
                    expr = st.text_input(
                        "f(t) (restricted numeric expression)", EXPRESSIONS[preset],
                    )
                    n = st.slider("Series length", 90, 900, 260, 10)
                    noise = st.selectbox("Innovation distribution", NOISE)
                    noise_sd = st.slider(
                        "Innovation standard deviation", 0.0, 3.0, 0.35, 0.05,
                    )
                    phi = st.slider("AR(1) correlation φ", -0.90, 0.90, 0.15, 0.05)
                    seed = st.number_input("Random seed", 0, 100_000, 42)
                    frame = make_synthetic(
                        expr, n, noise_sd, noise, phi, int(seed),
                    )
            elif source == "Yahoo Finance":
                ticker = st.text_input("Ticker", "SPY").strip().upper()
                period = st.selectbox("Lookback", ["6mo", "1y", "2y", "5y", "10y"], index=3)
                interval = st.selectbox("Observation frequency", ["1d", "1wk", "1mo"])
                field = st.selectbox("Price / volume", ["Close", "Open", "High", "Low", "Volume"])
                if not ticker:
                    raise ValueError("Enter a ticker.")
                frame = yahoo_data(ticker, period, interval, field)
            else:
                upload = st.file_uploader("CSV containing a numeric series", type=["csv"])
                if upload is not None:
                    data = pd.read_csv(upload)
                    if data.empty:
                        raise ValueError("The uploaded CSV is empty.")
                    cols = [c for c in data if pd.to_numeric(data[c], errors="coerce").notna().sum() >= 12]
                    if not cols:
                        raise ValueError("No numeric column with at least 12 observations.")
                    column = st.selectbox("Observation column", cols)
                    time_column = st.selectbox(
                        "Optional date column", ["None"] + [c for c in data if c != column]
                    )
                    vals = pd.to_numeric(data[column], errors="coerce")
                    frame = pd.DataFrame({"observed": vals})
                    if time_column != "None":
                        frame["date"] = pd.to_datetime(data[time_column], errors="coerce")
                    frame = frame.replace([np.inf, -np.inf], np.nan).dropna(
                        subset=["observed"]
                    ).reset_index(drop=True)
            if frame is None:
                st.info("Upload a CSV to start.")
                return
            transform_name = st.selectbox("Data transformation", list(TRANSFORMS))
            frame = transform_observations(frame, TRANSFORMS[transform_name])
        except (ValueError, TypeError, KeyError, ImportError, OverflowError) as exc:
            st.error(f"Cannot prepare data: {exc}")
            return
        st.caption(f"{len(frame)} usable observations after transformation.")

        st.divider()
        st.header("2 · Pooled CV design")
        n_obs = len(frame)
        if n_obs < 16:
            st.warning("Not enough observations for this experiment.")
            return
        max_h = min(60, max(1, (n_obs - 10) // 4))
        h = st.slider("Forecast horizon h", 1, max_h, min(8, max_h))
        held_out = st.checkbox(
            "Reserve a separate final h-step outer test",
            value=True, help="The final h observations are excluded from all CV tuning and fitting.",
        )
        T = n_obs - h if held_out else n_obs
        max_L = min(250, T - h)
        if max_L < 8:
            st.warning("Shorten the horizon or add more data.")
            return
        L = st.slider("Fit window L", 8, max_L, min(60, max_L))
        d = st.select_slider("Difference order d", [1, 2, 3, 4], value=2)
        stride = st.slider(
            "CV origin spacing Δ (observations)", 1, min(100, T - L - h + 1),
            min(h, max(1, T - L - h + 1)),
            help="Δ < h makes validation blocks overlap. Δ = h avoids overlap of their target blocks.",
        )
        possible = 1 + (T - h - L) // stride
        n_folds = st.slider(
            "Most recent completed CV folds M", 1, min(80, possible),
            min(16, possible),
        )
        grid_points = st.select_slider(
            "S grid resolution", [21, 41, 81, 121, 201, 301], value=121,
        )
        refine = st.checkbox(
            "Refine sampled local minima",
            value=True, help="Bounded local searches and exact endpoint comparison; "
                             "not a certified global optimizer.",
        )
        one_step = st.checkbox(
            "Compare h=1 CV on identical origins", value=True,
            help="The one-step baseline is tuned on the same historical origins, "
                 "but scored for the operational h-step forecast.",
        )

    values = frame["observed"].to_numpy(float)
    try:
        with st.spinner("Evaluating historical F curves and fitting the final trends…"):
            r = cached_result(
                tuple(float(v) for v in values),
                L, d, h, stride, n_folds, grid_points, refine, held_out, one_step,
            )
    except (ValueError, TypeError, FloatingPointError, np.linalg.LinAlgError) as exc:
        st.error(f"Cannot run pooled CV with this configuration: {exc}")
        return

    a, b, c, e = st.columns(4)
    a.metric("Pooled selected S", f"{r.pooled_s:.5f}")
    b.metric("Pooled historical MSE", f"{r.pooled_mse:.5g}")
    c.metric("Last-fold selected S", f"{r.last_s:.5f}")
    e.metric("Completed folds", str(len(r.origins)))
    st.info(
        f"At origin **T={r.selected_origin}**, each historical fold fits **L={L}** "
        f"observations, forecasts **h={h}** steps, and advances by **Δ={stride}** "
        f"observations. Pooled F is the equal-weight **mean of {len(r.origins)} "
        "historical forecast-MSE curves**. No outer-test observation enters selection."
    )

    tab_forecast, tab_loss, tab_folds, tab_math, tab_download = st.tabs([
        "Final trend & forecast", "All F curves & pooled F",
        "Folds & historical predictions", "Smoothness mathematics",
        "Data & downloads",
    ])
    with tab_forecast:
        st.subheader("Selected smoothness → refitted trend → future polynomial")
        manual_s = st.slider(
            "Inspect any S (manual comparison, not the pooled selector)",
            0.0, 1.0, 0.65, 0.005,
        )
        labels = ["Pooled CV", "Last fold", "Manual S"]
        if r.one_step_s is not None:
            labels.insert(2, "One-step CV")
        show = st.multiselect(
            "Curves to show", labels, default=["Pooled CV", "Last fold", "Manual S"],
        )
        fig, forecasts = final_forecasts(values, r, manual_s, show)
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            "The solid colored lines are independent trend refits on the latest L "
            "pre-forecast observations. Dashed extensions are h-step forecasts "
            "from the *same* zero-future-difference continuation rule. "
            "An outer holdout is displayed only after the selectors have been computed."
        )
        mostrar_toda = st.checkbox(
            "Suavizar toda la serie observada (ajuste descriptivo)",
            value=False, key="pooled_tendencia_completa",
        )
        if mostrar_toda:
            tendencia_completa = cached_full_series(
                tuple(float(v) for v in values), r.order, r.pooled_s,
            )
            st.plotly_chart(
                complete_trend_plot(
                    frame, tendencia_completa, smoothness=r.pooled_s,
                    order=r.order,
                ),
                use_container_width=True,
            )
            st.caption(
                "La suavidad S y el orden d proceden exclusivamente del CV "
                "de F promedio. Esta curva se reajusta utilizando TODAS las "
                "observaciones, incluido el test si está reservado. "
                "Es una descripción retrospectiva, NO un pronóstico fuera de muestra."
            )
            export = pd.DataFrame({
                "observado": values, "tendencia_completa": tendencia_completa,
            })
            if "date" in frame.columns:
                export.insert(0, "fecha", frame["date"].to_numpy())
            st.download_button(
                "Descargar tendencia de la serie completa (CSV)",
                export.to_csv(index=False).encode("utf-8-sig"),
                file_name="tendencia_completa_cv_promedio.csv", mime="text/csv",
            )
        if r.holdout:
            scores = pd.DataFrame([
                {"Method": k, "Selected S": (
                    r.pooled_s if k == "Pooled CV" else
                    r.last_s if k == "Last fold" else r.one_step_s
                ), "Outer test MSE": v, "Outer test RMSE": np.sqrt(v)}
                for k, v in r.test_mse.items()
            ])
            st.dataframe(scores, use_container_width=True, hide_index=True)
            st.caption("One reserved outer test is descriptive, not an unbiased comparison across many series.")

    with tab_loss:
        st.subheader("One function F per historical fold; one pooled objective")
        focus = st.select_slider(
            "Highlighted historical fold",
            options=list(range(1, len(r.origins) + 1)),
            value=len(r.origins),
        )
        l, rr = st.columns([1, 1])
        with l:
            show_all = st.checkbox("Show every fold F", value=True)
        with rr:
            log_y = st.checkbox("Log scale for loss curves", value=False)
        st.plotly_chart(loss_curves(r, focus, show_all, log_y), use_container_width=True)
        st.latex(r"F_{\mathrm{pool}}(S)=\frac{1}{M}\sum_{m=1}^{M}F_{t_m}(S),\qquad \widehat S_T=\arg\min_{S\in[0,1]}F_{\mathrm{pool}}(S)")
        st.caption(
            "Thin gray lines are individual F_t(S); orange highlights one fold, blue is "
            "their pooled mean. The pooled minimum is NOT the mean of the individual minima. "
            "The colored markers are the independently selected pooled and last-fold candidates."
        )
        st.subheader("Loss matrix: fold × fixed S grid")
        log_color = st.checkbox("Color scale = log10(MSE)", value=False)
        st.plotly_chart(loss_heatmap(r, log_color), use_container_width=True)
        st.caption("White × markers show per-fold GRID minima only; they are not tracked branches. The dashed vertical line is the pooled selected S.")
        st.dataframe(r.minima_table(), hide_index=True, use_container_width=True)

    with tab_folds:
        st.subheader("Exactly what the rolling cross-validation used")
        st.plotly_chart(split_timeline(r), use_container_width=True)
        st.caption(
            "Blue = fixed-length training window; orange = subsequently observed "
            "validation future. All orange segments end by T. If Δ<h, validation "
            "blocks overlap and their errors are not independent."
        )
        pick = st.select_slider(
            "Inspect a historical fold's trend and realized forecast",
            options=list(range(1, len(r.origins) + 1)),
            value=len(r.origins),
            key="fold_detail",
        )
        st.plotly_chart(historical_fold_preview(values[:r.selected_origin], r, pick - 1), use_container_width=True)
        st.dataframe(
            r.loss_table()[[
                "fold", "origin_1based", "train_start_1based", "train_end_1based",
                "validation_start_1based", "validation_end_1based",
            ]],
            use_container_width=True, hide_index=True,
        )
        st.caption("Fold-specific minimum values are only diagnostics. The app never follows branches.")

    with tab_math:
        st.subheader("How the normalized smoothness index changes the smoother")
        st.latex(r"Q=D_d^\top D_d=U\operatorname{diag}(\delta_j)U^\top,\quad H_\lambda=U\operatorname{diag}\!\left(\frac{1}{1+\lambda\delta_j}\right)U^\top")
        st.latex(r"S(\lambda)=\frac{L-\operatorname{tr}H_\lambda}{L-d}\in[0,1],\qquad \operatorname{edf}=L-(L-d)S")
        st.write(
            f"Pooled S = **{r.pooled_s:.6f}** · "
            f"λ = **{'∞ (projection limit)' if np.isinf(r.selected_lambda) else f'{r.selected_lambda:.6g}'}** · "
            f"effective degrees of freedom = **{r.degrees_of_freedom:.3f}**"
        )
        st.plotly_chart(spectral_plot(r), use_container_width=True)
        if st.checkbox("Show the smoothing matrix H at pooled S"):
            solver = cached_pure_solver(L, d)
            weights = np.zeros(L) if np.isinf(r.selected_lambda) else (
                1 / (1 + r.selected_lambda * solver.eigvals)
            )
            if np.isinf(r.selected_lambda):
                weights[:d] = 1
            H = (solver.eigvecs * weights) @ solver.eigvecs.T
            heat = go.Figure(go.Heatmap(z=H, colorscale="RdBu", zmid=0))
            st.plotly_chart(style(heat, "Input observation", "Fitted trend observation", 460), use_container_width=True)
        st.latex(r"H_\lambda'=-H_\lambda QH_\lambda,\qquad H_\lambda''=2H_\lambda QH_\lambda QH_\lambda")
        st.caption(
            "S=0 is the unsmoothed fit H=I; S=1 is the polynomial null-space projection. "
            "The current app samples the S-grid and can refine visible valleys. "
            "It does not certify discovery of every stationary point."
        )

    with tab_download:
        st.subheader("Inspect and export the entire experiment")
        st.plotly_chart(preview_series(frame, r.selected_origin), use_container_width=True)
        st.download_button(
            "Download complete fold × S forecast-MSE matrix (CSV)",
            data=r.loss_table().to_csv(index=False),
            file_name="pooled_cv_fold_smoothness_matrix.csv",
            mime="text/csv",
        )
        st.download_button(
            "Download individual fold minima and selected-S losses (CSV)",
            data=r.minima_table().to_csv(index=False),
            file_name="pooled_cv_fold_summary.csv",
            mime="text/csv",
        )
        surface = pd.DataFrame({
            "S": r.grid, "pooled_forecast_MSE": r.pooled_losses,
            **{f"F_fold_{i+1}": row for i, row in enumerate(r.fold_losses)},
        })
        st.download_button(
            "Download all F curves (CSV)",
            data=surface.to_csv(index=False),
            file_name="pooled_cv_F_curves.csv",
            mime="text/csv",
        )
        st.download_button(
            "Download transformed input observations (CSV)",
            data=frame.to_csv(index=False), file_name="pooled_cv_input.csv",
            mime="text/csv",
        )
        forecast_table = pd.DataFrame({
            "forecast_observation_1based": np.arange(r.selected_origin + 1, r.selected_origin + h + 1),
            **{f"{name}_forecast": vals for name, vals in r.future_forecasts.items()},
        })
        if r.holdout:
            forecast_table["actual_outer_holdout"] = values[r.selected_origin:r.selected_origin + h]
        st.download_button(
            "Download final forecasts and outer truth when available (CSV)",
            data=forecast_table.to_csv(index=False),
            file_name="pooled_cv_forecasts.csv", mime="text/csv",
        )
        config = {
            "source": source, "transform": transform_name, "n": len(frame),
            "window": L, "order": d, "horizon": h, "stride": stride,
            "requested_folds": n_folds, "completed_folds": len(r.origins),
            "origins_zero_based": r.origins.tolist(),
            "grid_points": grid_points, "refine_sampled_valleys": refine,
            "holdout": held_out, "compare_one_step": one_step,
            "outer_origin_T": r.selected_origin, "pooled_selected_s": r.pooled_s,
            "last_fold_selected_s": r.last_s, "one_step_selected_s": r.one_step_s,
            "pooled_validation_mse": r.pooled_mse, "outer_mse": r.test_mse,
        }
        st.download_button(
            "Download configuration and decisions (JSON)",
            data=json.dumps(config, indent=2), file_name="pooled_cv_run.json",
            mime="application/json",
        )
        st.caption(
            "Pure PLS with observation forecast MSE only. These interactive runs do not "
            "alter CP03–CP08 or establish market predictability."
        )


if __name__ == "__main__":
    main()
