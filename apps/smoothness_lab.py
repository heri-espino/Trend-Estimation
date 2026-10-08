"""Interactive research application for paper_smoothness-cv.

Run from repository root:
    python -m pip install -e ".[dashboard,finance]"
    streamlit run apps/smoothness_lab.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd
import plotly.express as px
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


@st.cache_data(ttl=3600, show_spinner=False)
def yahoo_history(tickers: tuple[str, ...], period: str, interval: str) -> pd.DataFrame:
    import yfinance as yf

    if not tickers:
        raise ValueError("Enter at least one valid ticker.")
    frame = yf.download(
        tickers=list(tickers), period=period, interval=interval,
        auto_adjust=True, progress=False, threads=False, group_by="ticker",
    )
    if frame.empty:
        raise ValueError("Yahoo Finance returned no rows. Try another ticker or period.")
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
            raise ValueError(f"No data returned for {ticker}.")
    else:
        column = raw[field]
    column = pd.to_numeric(column, errors="coerce").dropna()
    if column.empty:
        raise ValueError(f"No valid {field} observations for {ticker}.")
    return pd.DataFrame({"date": column.index, "observed": column.to_numpy(dtype=float)})


def _download_table(label: str, frame: pd.DataFrame, file_name: str) -> None:
    st.download_button(
        label, frame.to_csv(index=False).encode("utf-8"),
        file_name=file_name, mime="text/csv",
    )


def _line_plot(frame: pd.DataFrame, result, *, chart_type: str,
               display_s: float, manual_s: float, order: int,
               reveal_test: bool, show_baseline: bool) -> go.Figure:
    y = frame["observed"].to_numpy(dtype=float)
    x = (pd.to_datetime(frame["date"]) if "date" in frame.columns
         else np.arange(len(frame)))
    n = len(y)
    start, end = result.train_start, result.pretest_end
    train_x = x[start:end]
    future_x = x[end:result.test_end]
    fit = td.PurePenalizedTrend(order=order, smoothness=manual_s).fit(y[start:end])
    manual_trend = fit.trend_
    manual_forecast = np.asarray(fit.forecast(len(future_x)), dtype=float)

    fig = go.Figure()
    if chart_type == "Residuals (observed minus trend)":
        fig.add_scatter(x=train_x, y=y[start:end]-result.trend,
                        mode="lines", name="Selected residuals")
        fig.add_hline(y=0, line_dash="dot")
    elif chart_type == "Trend slope (first difference)":
        fig.add_scatter(x=train_x[1:], y=np.diff(result.trend),
                        mode="lines", name="Selected trend slope")
        fig.add_hline(y=0, line_dash="dot")
        if show_baseline:
            fig.add_scatter(x=train_x[1:], y=np.diff(result.pooled_trend),
                            mode="lines", name="Pooled slope", line={"dash": "dot"})
    else:
        fig.add_scatter(x=x[:end], y=y[:end], mode="lines",
                        name="Observed (available at forecast origin)", opacity=0.55)
        if reveal_test:
            fig.add_scatter(x=x[end:], y=y[end:], mode="lines+markers",
                            name="Untouched test (reveal only)",
                            line={"dash": "dot"})
        if chart_type == "Trend, residual and forecast":
            fig.add_scatter(x=train_x, y=result.trend, mode="lines",
                            name="Selected trend")
            fig.add_scatter(x=future_x, y=result.forecast, mode="lines+markers",
                            name="Selected forecast")
            if show_baseline:
                fig.add_scatter(x=train_x, y=result.pooled_trend,
                                mode="lines", name="Pooled-CV trend",
                                line={"dash": "dash"})
                fig.add_scatter(x=future_x, y=result.pooled_forecast,
                                mode="lines+markers", name="Pooled-CV forecast",
                                line={"dash": "dash"})
        elif chart_type == "Manual smoothness comparison":
            fig.add_scatter(x=train_x, y=result.trend, mode="lines",
                            name="Chosen rule")
            fig.add_scatter(x=train_x, y=manual_trend, mode="lines",
                            name=f"Manual S={manual_s:.2f}", line={"dash": "dash"})
            fig.add_scatter(x=future_x, y=manual_forecast, mode="lines+markers",
                            name="Manual continuation")
        elif chart_type == "Observed vs trend only":
            fig.add_scatter(x=train_x, y=result.trend, mode="lines",
                            name="Selected trend")
    fig.update_layout(
        height=450, title=f"{chart_type} — S={display_s:.4f}",
        xaxis_title="Date / observation", yaxis_title="Transformed series units",
        legend={"orientation": "h", "y": -0.25},
    )
    return fig


def main():
    st.set_page_config(page_title="Dynamic Smoothness Laboratory", layout="wide")
    st.title("Dynamic forecast-optimal smoothness")
    st.caption(
        "Interactive companion to paper_smoothness-cv: forecast-loss surfaces, "
        "persistent minima, branch matrix V_j, phi decisions and final refitting."
    )

    with st.sidebar:
        st.header("1. Data")
        source = st.radio("Source", ["Synthetic function", "Yahoo Finance", "Upload CSV"])
        if source == "Synthetic function":
            formulas = {
                "Linear + cycle": "0.02*t + sin(t/12)",
                "Piecewise slope": "0.015*t + where(t>100, 0.06*(t-100), 0)",
                "Nonlinear trend": "0.00015*(t-120)**2 + 0.8*sin(t/18)",
                "Level shift": "0.015*t + where(t>110, 3, 0)",
                "Custom expression": "0.02*t + sin(t/12)",
            }
            preset = st.selectbox("Function template", tuple(formulas))
            expression = st.text_input(
                "f(t) — editable numerical expression", formulas[preset],
                key=f"function_{preset}",
                help="Allowed: t, pi, e, + - * / **, comparisons, "
                     "sin, cos, tan, exp, log, sqrt, abs, tanh, where, clip, min/max.",
            )
            n = st.slider("Observations", 90, 600, 220, 10)
            noise_sd = st.slider("Innovation standard deviation", 0.0, 5.0, 0.35, 0.05)
            noise = st.selectbox("Noise family", [
                "Gaussian", "Laplace", "Student-t (df=5)", "Heteroskedastic"
            ])
            phi = st.slider("AR(1) noise phi", -0.90, 0.90, 0.0, 0.05)
            seed = st.number_input("Random seed", 0, 999999, 42)
            frame = make_synthetic(expression, n, noise_sd, noise, phi, int(seed))
            selected = "Synthetic"
        elif source == "Yahoo Finance":
            ticker_text = st.text_input("Symbols (comma-separated)", "SPY, AAPL, BTC-USD")
            tickers = tuple(dict.fromkeys(
                v.strip().upper() for v in ticker_text.split(",") if v.strip()
            ))
            if not tickers or len(tickers) > 12:
                st.error("Enter 1–12 Yahoo Finance symbols.")
                st.stop()
            period = st.selectbox("History", ["6mo", "1y", "2y", "5y", "10y"], index=2)
            interval = st.selectbox("Frequency", ["1d", "1wk", "1mo"])
            field = st.selectbox("Price field", ["Close", "Open", "High", "Low", "Volume"])
            try:
                raw = yahoo_history(tickers, period, interval)
            except Exception as exc:
                st.error(f"Yahoo Finance request failed: {exc}")
                st.stop()
            selected = st.selectbox("Series to analyze", tickers)
            try:
                frame = _frame_from_market(raw, selected, field)
            except (ValueError, KeyError) as exc:
                st.error(str(exc))
                st.stop()
            st.download_button(
                "Download Yahoo raw CSV",
                raw.to_csv().encode("utf-8"),
                "yahoo_download.csv", mime="text/csv",
            )
        else:
            uploaded = st.file_uploader("CSV with a numeric column", type="csv")
            if uploaded is None:
                st.info("Upload a CSV to analyze it.")
                st.stop()
            raw = pd.read_csv(uploaded)
            numeric = raw.select_dtypes(include="number").columns.tolist()
            if not numeric:
                st.error("The CSV has no numeric columns.")
                st.stop()
            selected = st.selectbox("Observed data column", numeric)
            date_column = st.selectbox(
                "Date column (optional)", ["None"] + [
                    x for x in raw.columns if x != selected
                ]
            )
            frame = pd.DataFrame({
                "observed": pd.to_numeric(raw[selected], errors="coerce"),
            })
            if date_column != "None":
                frame["date"] = pd.to_datetime(raw[date_column], errors="coerce")
            frame = frame.dropna().reset_index(drop=True)
        st.header("2. Trend representation")
        mode = st.selectbox("Transform before smoothing", [
            "Level", "Log level", "Indexed to 100", "Simple return", "Log return"
        ])
        try:
            transformed = transform_observations(frame, mode)
        except ValueError as exc:
            st.error(str(exc))
            st.stop()
        max_rows = st.slider("Most recent observations used", 90, 600, 260, 10)
        transformed = transformed.tail(max_rows).reset_index(drop=True)
        st.header("3. Forecast experiment")
        order = st.select_slider("Difference order d", options=[1, 2, 3, 4], value=2)
        window = st.slider("Rolling fit length L", 25, 160, 60, 5)
        horizon = st.slider("Validation horizon h", 1, 20, 5)
        reserve = st.slider("Untouched test length", 1, 20, 5)
        step = st.slider("Historical origin spacing", 1, 20, 5)
        origins = st.slider("Historical origins retained", 3, 30, 12)
        epsilon = st.slider("Branch continuation epsilon", 0.02, 0.30, 0.10, 0.01)
        spacing = st.slider("Distinct minimum spacing", 0.01, 0.10, 0.02, 0.01)
        rule = st.selectbox("Dynamic phi(V_j) rule", list(RULES),
                            index=list(RULES).index("recency_hl3"))
        resolution = st.select_slider("Heatmap resolution", [21, 41, 61], value=41)
        depth = st.select_slider("Stationary search depth", [3, 5, 8], value=5)
        st.caption("d=3/4 continuations may be unstable; compare against pooled CV.")

    if len(transformed) < window + 3*horizon + reserve:
        st.error(
            f"Insufficient observations: need at least {window+3*horizon+reserve}, "
            f"currently have {len(transformed)}. Increase history or reduce L/h."
        )
        st.stop()
    observed = transformed["observed"].to_numpy(dtype=float)
    with st.spinner("Computing chronological validation surfaces and branch histories..."):
        try:
            result = analyze(
                tuple(observed), order=order, window=window,
                horizon=horizon, step=step, max_origins=origins,
                test_size=reserve, track_epsilon=epsilon,
                candidate_spacing=spacing, rule=rule,
                grid_points=resolution, search_depth=depth,
            )
        except (ValueError, ArithmeticError, RuntimeError) as exc:
            st.error(f"Selection failed: {exc}")
            st.stop()

    a, b, c, d = st.columns(4)
    a.metric("Selected smoothness S", f"{result.final_s:.4f}")
    b.metric("Penalty lambda", f"{result.final_lambda:.4g}")
    c.metric("Pooled-CV S (grid)", f"{result.pooled_s:.4f}")
    d.metric("Selected branch", result.selected_branch)
    st.caption(
        f"{selected} · {mode} · {len(observed)} observations · "
        f"{result.tracks['origin'].nunique()} historical origins · {result.selection_status}. "
        "Selection uses only pre-test observations. CP08 rules are demonstrations, not "
        "established universally superior forecasting models."
    )

    st.subheader("Trend and forecast")
    controls, other, third = st.columns(3)
    view = controls.selectbox("Chart", [
        "Trend, residual and forecast", "Observed vs trend only",
        "Manual smoothness comparison", "Residuals (observed minus trend)",
        "Trend slope (first difference)",
    ])
    show_baseline = other.checkbox("Overlay pooled-CV baseline", True)
    reveal_test = third.checkbox("Reveal untouched test observations", False)
    manual_s = st.slider("Manual comparison smoothness S", 0.0, 1.0, 0.75, 0.01)
    st.plotly_chart(
        _line_plot(transformed, result, chart_type=view,
                   display_s=result.final_s, manual_s=manual_s,
                   order=order, reveal_test=reveal_test,
                   show_baseline=show_baseline),
        use_container_width=True,
    )
    if reveal_test:
        target = observed[result.pretest_end:result.test_end]
        m1 = np.mean((target-result.forecast)**2)
        m2 = np.mean((target-result.pooled_forecast)**2)
        st.write(
            f"**Untouched test diagnostic (not used for tuning):** "
            f"tracked MSE = {m1:.6g}; pooled MSE = {m2:.6g}"
        )
    _download_table("Download selected data CSV", transformed, "trend_data.csv")

    tab_surface, tab_branches, tab_matrix, tab_download = st.tabs([
        "Validation MSE surfaces", "Tracked branch matrix V_j",
        "Smoothing matrix H_lambda", "Results and exports",
    ])
    with tab_surface:
        matrix = result.surfaces.pivot(
            index="origin", columns="smoothness", values="val1_mse"
        ).sort_index()
        fig = px.imshow(
            matrix, aspect="auto", color_continuous_scale="Viridis",
            labels={"x": "Normalized smoothness S", "y": "Historical origin",
                    "color": "Validation-1 MSE"},
        )
        fig.update_layout(height=430)
        st.plotly_chart(fig, use_container_width=True)
        curve = go.Figure()
        curve.add_scatter(
            x=result.final_surface["smoothness"], y=result.final_surface["val1_mse"],
            mode="lines+markers", name="Final Validation-1 MSE",
        )
        for _, candidate in result.candidates.iterrows():
            curve.add_scatter(
                x=[candidate["smoothness"]], y=[candidate["val1_mse"]],
                mode="markers", name=candidate["source"],
                marker={"size": 11, "symbol": "diamond"},
                showlegend=False,
            )
        curve.update_layout(
            height=360, xaxis_title="S", yaxis_title="MSE",
            title="Final Validation-1 surface and recovered local minima",
        )
        st.plotly_chart(curve, use_container_width=True)
        st.caption(
            "The heatmap is a sampled diagnostic of Validation-1 MSE. "
            "Stationary minima are recovered with derivative-aware search, "
            "not inferred from heatmap pixel minima. The final surface "
            "uses the last pre-test Validation-1 block."
        )
        st.dataframe(result.candidates, use_container_width=True)

    with tab_branches:
        fig = px.line(
            result.tracks, x="origin", y="smoothness", color="branch_id",
            markers=True, title="One-to-one tracked local minima",
        )
        st.plotly_chart(fig, use_container_width=True)
        fig = px.line(
            result.tracks, x="origin", y="val2_mse", color="branch_id",
            markers=True, title="Validation-2 MSE (fresh refit after Validation 1)",
        )
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(result.summary, use_container_width=True)
        branch = st.selectbox("Inspect V_j", sorted(result.tracks["branch_id"].unique()))
        subset = result.tracks.loc[
            result.tracks["branch_id"].eq(branch),
            ["origin", "smoothness", "val1_mse", "val2_mse", "val2_rmse", "status"]
        ]
        st.markdown("**Branch state V_j = [S, Val1 loss, Val2 loss]**")
        st.dataframe(subset, use_container_width=True)
        _download_table("Download this V_j matrix", subset, f"{branch}_matrix.csv")
        st.caption(
            "Validation-1 and Validation-2 are forecast errors, not in-sample "
            "reconstruction errors. The paper's branch selector ranks by mean "
            "historical Validation-2 RMSE; MSE is also shown for diagnostics."
        )

    with tab_matrix:
        which = st.radio(
            "Smoothing matrix parameter", ["Selected rule", "Manual S"],
            horizontal=True,
        )
        matrix_s = result.final_s if which == "Selected rule" else manual_s
        H = smoothing_matrix(window, order, matrix_s)
        fig = px.imshow(H, color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
                        labels={"x": "Input time index", "y": "Output time index",
                                "color": "H[i,j]"})
        fig.update_layout(
            height=560, title="H_lambda = (I + lambda D_d^T D_d)^(-1)"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.write(
            f"Trace(H) = {np.trace(H):.4f} · "
            f"normalized smoothness = {1-np.trace(H)/window:.4f} · "
            f"symmetric error = {np.max(np.abs(H-H.T)):.2e}"
        )
        _download_table(
            "Download smoothing matrix CSV",
            pd.DataFrame(H), "smoothing_matrix.csv"
        )

    with tab_download:
        st.dataframe(result.tracks, use_container_width=True)
        _download_table("Download all branch validation results",
                        result.tracks, "branches_validation.csv")
        _download_table("Download Validation-1 MSE surface matrix",
                        result.surfaces, "validation1_surfaces.csv")
        _download_table("Download branch summaries",
                        result.summary, "branch_summary.csv")
        evaluation = pd.DataFrame({
            "time": np.arange(result.pretest_end, result.test_end),
            "tracked_forecast": result.forecast,
            "pooled_forecast": result.pooled_forecast,
            "test_observation": observed[result.pretest_end:result.test_end],
        })
        st.caption("Forecast export contains reserved observations; those were not used for selection.")
        _download_table("Download forecast vs test CSV",
                        evaluation, "forecast_test.csv")
        st.markdown(
            "Run the frozen paper experiments separately. This app is an "
            "exploratory interface and does not modify the paper's frozen results."
        )


if __name__ == "__main__":
    main()
