"""Paper 2 app: dynamic branches of the *weighted forecast-loss surface*.

Canonical entrypoint from the repo root:
    streamlit run apps/dynamic_branch_cv.py

This app intentionally DOES NOT import apps.smoothness_lab: that launcher
implements the archived Val1/Val2 transformed-S method, which is a
different estimator. Here m weights completed F curves, minima are
tracked one-to-one, and mean-last-three S is applied AFTER tracking.
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

from apps.pooled_forecast_cv import yahoo_data
from experiments.smoothness_cv.article_simulations import ARTICLE_TRENDS, make_article_synthetic
from experiments.smoothness_cv.live_lab import make_synthetic
from experiments.smoothness_cv.pooled_lab import fit_window_forecast
from experiments.smoothness_cv.weighted_surface_study import (
    LossWeighting, run_weighted_surface_study,
)
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.core.smoothness import smoothness_to_lambda

WEIGHTINGS = {
    "All completed origins — equal": ("uniform_all", "uniform", None),
    "Last K origins — equal": ("recent_uniform", "uniform", "recent"),
    "Last K origins — linear": ("recent_linear", "linear", "recent"),
    "Last K origins — exponential": ("recent_exp", "exponential", "recent"),
}

PRESETS = {
    "Quadratic bend": "9 + 0.00028*(t-145)**2",
    "Changing slope": "9 + 0.025*t + where(t>140, 0.08*(t-140), 0)",
    "Cubic": "8 + 0.000002*(t-140)**3",
    "Linear + oscillation": "10 + 0.018*t + sin(t/17)",
    "Custom expression": "10 + 0.02*t + 0.8*sin(t/16)",
}


@st.cache_data(show_spinner=False, max_entries=16)
def cached_study(
    values: tuple[float, ...], methods: tuple[LossWeighting, ...],
    orders: tuple[int, ...], L: int, h: int, stride: int,
    folds: int, grid: int, radius: float, min_support: int, k: int,
    holdout: bool,
):
    return run_weighted_surface_study(
        np.asarray(values), methods=methods, orders=orders,
        window=L, horizon=h, stride=stride, max_folds=folds,
        grid_points=grid, refine_pooled=True, track_radius=radius,
        branch_min_support=min_support, branch_decision_k=k,
        branch_score_k=k, holdout=holdout,
    )


def load_data(source: str) -> pd.DataFrame:
    if source == "Synthetic formula":
        n = st.sidebar.slider("Length N", 65, 600, 230, 5)
        preset = st.sidebar.selectbox("Latent shape", list(PRESETS))
        expression = st.sidebar.text_input("Trend function", value=PRESETS[preset])
        noise_sd = st.sidebar.slider("Noise SD", 0.0, 3.0, 0.35, 0.05)
        noise_kind = st.sidebar.selectbox(
            "Noise family", ["Gaussian", "Laplace", "Student-t (df=5)", "Heteroskedastic"]
        )
        phi = st.sidebar.slider("AR1 correlation phi", -0.9, 0.9, 0.0, 0.05)
        seed = st.sidebar.number_input("Seed", min_value=0, value=42, step=1)
        return make_synthetic(
            expression, n=n, noise_sd=noise_sd, noise=noise_kind,
            phi=phi, seed=int(seed),
        )
    if source == "Cortés-Toto source generator":
        trend = st.sidebar.selectbox("True trend", list(ARTICLE_TRENDS))
        N = st.sidebar.select_slider("Length N", options=[50, 200], value=200)
        sigma = st.sidebar.select_slider("Noise SD", options=[0.5, 2.0], value=0.5)
        seasonal = st.sidebar.checkbox("Quarterly seasonality", False)
        seed = st.sidebar.number_input("Seed", min_value=0, value=42, step=1)
        return make_article_synthetic(trend, n=N, noise_sd=sigma,
                                      seasonal=seasonal, seed=int(seed))
    if source == "CSV upload":
        file = st.sidebar.file_uploader("CSV containing numeric observations", type=["csv"])
        if file is None:
            st.info("Upload a CSV to begin. The numeric column is selected below.")
            st.stop()
        uploaded = pd.read_csv(file)
        numeric = [col for col in uploaded if pd.api.types.is_numeric_dtype(uploaded[col])]
        if not numeric:
            st.error("No numeric columns in uploaded CSV.")
            st.stop()
        column = st.sidebar.selectbox("Observed column", numeric)
        values = pd.to_numeric(uploaded[column], errors="coerce").dropna().to_numpy(float)
        return pd.DataFrame({"observed":values})
    ticker = st.sidebar.text_input("Yahoo Finance ticker", value="SPY").strip()
    period = st.sidebar.selectbox("Period", ["1y", "2y", "5y", "10y", "max"], index=2)
    interval = st.sidebar.selectbox("Interval", ["1d", "1wk", "1mo"], index=1)
    field = st.sidebar.selectbox("OHLCV field", ["Close", "Open", "High", "Low", "Volume"])
    if not ticker:
        st.info("Choose a ticker.")
        st.stop()
    try:
        return yahoo_data(ticker, period, interval, field)
    except Exception as exc:
        st.error(f"Yahoo Finance could not load data: {exc}")
        st.stop()


def loss_heatmap(grid: np.ndarray, origins: np.ndarray, surfaces: np.ndarray):
    fig = go.Figure(go.Heatmap(
        x=grid, y=origins, z=surfaces, colorscale="Viridis",
        colorbar={"title":"MSE"},
        hovertemplate="S=%{x:.4f}<br>historical origin=%{y}<br>weighted MSE=%{z:.5g}<extra></extra>",
    ))
    fig.update_layout(
        title="Weighted historical F surfaces (completed origins only)",
        xaxis_title="Normalized smoothness S", yaxis_title="Historical origin",
        template="plotly_white", height=435,
    )
    return fig


def branch_plot(grid, origins, surface, branches, selected_branch, pooled_s, tracked_s):
    fig=go.Figure()
    for branch_id, block in branches.groupby("branch", sort=True):
        block=block.sort_values("step")
        fig.add_scatter(
            x=block["origin"], y=block["s_local"],
            mode="lines+markers",
            name=f"Branch {branch_id}",
            line={"width":4 if branch_id==selected_branch else 1.7},
            marker={"size":9 if branch_id==selected_branch else 5},
            hovertemplate="origin=%{x}<br>S local=%{y:.5f}<extra></extra>",
        )
    fig.add_hline(y=pooled_s,line_dash="dash",line_color="#c75a39",
                  annotation_text=f"Pooled S = {pooled_s:.4f}")
    fig.add_hline(y=tracked_s,line_dash="dot",line_color="#386db1",
                  annotation_text=f"Tracked S = {tracked_s:.4f}")
    fig.update_layout(
        title="Local-minimum histories: one-to-one matching across weighted F",
        xaxis_title="Completed historical forecast origin",
        yaxis_title="Minimum location S", yaxis_range=[-0.02,1.02],
        template="plotly_white", height=440, legend={"orientation":"h"},
    )
    return fig


def smoother_matrix(L:int,d:int,s:float):
    solver=cached_pure_solver(L,d)
    lam=smoothness_to_lambda(float(s),L,d)
    weights=np.zeros(L) if np.isinf(lam) else 1/(1+lam*solver.eigvals)
    if np.isinf(lam):
        weights[:d]=1
    return (solver.eigvecs*weights) @ solver.eigvecs.T


def main():
    st.set_page_config(page_title="Paper 2 · Weighted F branch tracking",layout="wide")
    st.title("Paper 2 · Dynamic branches of weighted forecast-loss surfaces")
    st.caption(
        "Current 2026-10 protocol: choose m,d,L,h first; weight COMPLETED "
        "historical loss curves; track their local minima; choose an active "
        "branch; convert its last three S minima into one operational smoothness. "
        "No internal Val2. Outer test is used only for evaluation."
    )
    source=st.sidebar.selectbox(
        "Source",["Synthetic formula","Cortés-Toto source generator","CSV upload","Yahoo Finance"]
    )
    frame=load_data(source)
    frame=frame.replace([np.inf,-np.inf],np.nan).dropna(subset=["observed"]).reset_index(drop=True)
    values=frame["observed"].to_numpy(float)
    if len(values)<35:
        st.error("At least 35 finite observations are required.")
        st.stop()

    st.sidebar.subheader("Frozen method settings")
    d=st.sidebar.selectbox("Finite-difference order d",[1,2,3,4],index=1)
    h=st.sidebar.slider("Forecast horizon h",1,min(24,max(1,(len(values)-10)//5)),3)
    max_L=max(8,min(150,len(values)-h-5))
    L=st.sidebar.slider("Fitting window L",max(7,d+2),max_L,min(40,max_L))
    stride=st.sidebar.slider("Origin stride",1,12,min(3,h))
    folds=st.sidebar.slider("Maximum historical folds",3,50,18)
    grid=st.sidebar.select_slider("S grid points",[31,61,101,161,321],value=101)
    held_out=st.sidebar.checkbox("Reserve last h observations for outer test",True)
    st.sidebar.subheader("Weighting historical loss CURVES")
    enabled=st.sidebar.multiselect(
        "Predeclared weighting methods",
        list(WEIGHTINGS),
        default=["All completed origins — equal","Last K origins — exponential"],
    )
    if not enabled:
        st.info("Choose at least one weighting method.")
        st.stop()
    lookback=st.sidebar.slider("Last K origins",2,40,8)
    decay=st.sidebar.slider("Exponential decay per origin",0.10,1.0,0.80,0.05)
    methods=tuple(LossWeighting(
        WEIGHTINGS[name][0],WEIGHTINGS[name][1],
        lookback if WEIGHTINGS[name][2]=="recent" else None,
        decay,
    ) for name in enabled)
    st.sidebar.subheader("Branch rules (after F)")
    radius=st.sidebar.slider("Maximum matching distance in S",0.01,0.50,0.10,0.01)
    support=st.sidebar.slider("Minimum branch support",1,10,3)
    k=st.sidebar.slider("Mean of last K local minima",1,8,3)
    T=len(values)-h if held_out else len(values)
    if T<L+h:
        st.error("Not enough completed history for these L and h choices.")
        st.stop()
    try:
        study=cached_study(
            tuple(values),methods,(int(d),),L,h,stride,folds,grid,
            radius,support,k,held_out,
        )
    except Exception as exc:
        st.error(f"Unable to construct completed historical F curves: {exc}")
        st.stop()
    summary=study.summary
    st.subheader("Selections for each predeclared weighting method")
    cols=[
        "method","d","h","n_folds","pooled_s",
        "tracked_s","tracked_branch","tracked_support",
        "pooled_historical_mse","tracked_historical_score",
    ]
    if held_out:
        cols+=["pooled_test_mse","tracked_test_mse"]
    st.dataframe(summary[cols],hide_index=True,use_container_width=True)
    st.caption(
        "Do not select the best method by looking at outer-test errors here "
        "and then report those same errors as independent validation."
    )
    method=st.selectbox("Inspect one predeclared weighting method",list(summary["method"]))
    row=summary.loc[summary.method==method].iloc[0]
    surface=study.surfaces[(method,d)]
    matching=study.branches[(study.branches.method==method)&(study.branches.d==d)].copy()

    a,b,c=st.columns(3)
    a.metric("Selected branch",str(row.tracked_branch))
    b.metric("Operational tracked S",f"{row.tracked_s:.5f}")
    c.metric("Global minimum S (Paper 1)",f"{row.pooled_s:.5f}")
    tab_surface,tab_branch,tab_forecast,tab_matrix,tab_data=st.tabs(
        ["Weighted F and minima","Tracked branches","Forecast/fit","Spectral smoother H","Exports"]
    )
    with tab_surface:
        st.plotly_chart(loss_heatmap(study.grid,study.origins,surface),use_container_width=True)
        fig=go.Figure()
        fig.add_scatter(x=study.grid,y=surface[-1],mode="lines",
                        name=f"Latest complete weighted F ({method})")
        fig.add_vline(x=row.pooled_s,line_dash="dash",annotation_text="Global minimum")
        fig.add_vline(x=row.tracked_s,line_dash="dot",annotation_text="Tracked operational S")
        fig.update_layout(template="plotly_white",xaxis_title="S",yaxis_title="MSE",height=390)
        st.plotly_chart(fig,use_container_width=True)
        st.caption(
            "The grid may miss narrow local minima. These are discrete valleys, "
            "not certified stationary roots. The dynamic paper's numerical "
            "completeness question is distinct."
        )
    with tab_branch:
        st.plotly_chart(branch_plot(
            study.grid,study.origins,surface,matching,
            row.tracked_branch,row.pooled_s,row.tracked_s,
        ),use_container_width=True)
        st.dataframe(matching,hide_index=True,use_container_width=True)
        st.latex(r"\widehat S_T = \phi(V_{\widehat j_T}),\quad \phi=\text{mean of last K S minima}")
        st.caption(
            "K-mean applies AFTER tracking. The weighted loss functions "
            "are unaffected by the S averages. No internal Val2."
        )
    with tab_forecast:
        xaxis=np.arange(1,len(values)+1)
        f=go.Figure()
        f.add_scatter(x=xaxis[:T],y=values[:T],name="Observed (historically available)")
        if held_out:
            f.add_scatter(x=xaxis[T:],y=values[T:],name="Outer test (not selected on)",
                          mode="lines+markers")
        if "latent" in frame:
            f.add_scatter(x=xaxis,y=frame["latent"],name="Latent trend (display only)")
        for label,s in [("Tracked",row.tracked_s),("Pooled",row.pooled_s)]:
            fitted,forecast=fit_window_forecast(values[:T],origin=T,window=L,
                                                order=d,horizon=h,smoothness=float(s))
            f.add_scatter(x=np.arange(T-L+1,T+1),y=fitted,name=f"{label} fitted trend")
            f.add_scatter(x=np.arange(T+1,T+h+1),y=forecast,name=f"{label} future h-step",
                          mode="lines+markers")
        f.update_layout(template="plotly_white",height=480,
                        xaxis_title="Observation",yaxis_title="Observed level / forecast")
        st.plotly_chart(f,use_container_width=True)
        st.caption("Full-series retrospective smoothing is NOT an outer forecast.")
    with tab_matrix:
        s_val=st.radio("Operational S",["Tracked","Pooled"],horizontal=True)
        s=float(row.tracked_s if s_val=="Tracked" else row.pooled_s)
        H=smoother_matrix(L,d,s)
        f=go.Figure(go.Heatmap(z=H,colorscale="RdBu",zmid=0))
        f.update_layout(template="plotly_white",height=450,
                        xaxis_title="Observation j",yaxis_title="Estimated trend i")
        st.plotly_chart(f,use_container_width=True)
        st.latex(r"H_\lambda = U\mathrm{diag}((1+\lambda\delta_j)^{-1})U^\top")
        st.latex(r"S=\frac{L-\mathrm{tr}(H_\lambda)}{L-d}")
        st.write(f"EDF = {np.trace(H):.5f}; S = {s:.5f}.")
    with tab_data:
        st.download_button("Download decisions CSV",summary.to_csv(index=False),
                           "paper2_decisions.csv",mime="text/csv")
        st.download_button("Download branch histories CSV",
                           study.branches.to_csv(index=False),"paper2_branches.csv",
                           mime="text/csv")
        wide=pd.DataFrame(surface,columns=[f"S={s:.6f}" for s in study.grid])
        wide.insert(0,"origin",study.origins)
        st.download_button("Download weighted F matrix CSV",wide.to_csv(index=False),
                           "paper2_weighted_F.csv",mime="text/csv")
        provenance={
            "paper":"Dynamic Branch Selection","protocol":"weighted_F_v1",
            "weighting_method":method,"order":int(d),"window":int(L),
            "horizon":int(h),"stride":int(stride),"grid_points":int(grid),
            "track_radius":float(radius),"support":int(support),
            "branch_decision_k":int(k),"holdout":bool(held_out),
            "outer_origin_T":int(T),"minima":"grid_candidates_not_certified",
            "inner_val2":False,
        }
        st.download_button("Download configuration JSON",json.dumps(provenance,indent=2),
                           "paper2_configuration.json",mime="application/json")
    st.caption(
        "Exploratory CURRENT Paper 2 app. Historical Val1/Val2 UI remains in "
        "apps/smoothness_lab.py and apps/smoothness_lab_advanced.py, not used here."
    )


if __name__=="__main__":
    main()
