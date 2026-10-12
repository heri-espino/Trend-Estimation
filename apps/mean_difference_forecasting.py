"""Paper 4 interactive research app: Guerrero and profile-mean forecast CV.

Run from repository root:
    streamlit run apps/mean_difference_forecasting.py

The app calls the shared library's exact affine PLS model; it does NOT
reimplement mathematical selection. Reserved h-step outer observations
(and any synthetic latent tau) are never passed into selectors.

Scientific status: exploratory, not publication evidence.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from apps.dynamic_branch_cv import load_data
from experiments.smoothness_cv.pooled_lab import chronological_origins
from trend_estimation.forecasting.mean_difference_cv import (
    select_mean_difference_cv, observed_mean_difference,
)

MODE_LABELS={
    "zero":"PLS puro · μ=0",
    "guerrero":"Guerrero (2007) · media de diferencias observadas",
    "profile":"Forecast-CV · media μ(S) perfilada",
}
COLOR={"zero":"#777777","guerrero":"#CC6633","profile":"#2E689D"}


@st.cache_data(show_spinner=False,max_entries=12)
def calculate(y_values:tuple[float,...], *,
              d:int,L:int,h:int,stride:int,max_folds:int,
              grid_points:int,weighting:str,decay:float):
    y=np.asarray(y_values,dtype=float)
    origins=chronological_origins(len(y),L,h,stride,max_folds)
    if not len(origins):
        raise ValueError("Need at least one completed historical h-step fold.")
    weights=(
        np.ones(len(origins),dtype=float) if weighting=="uniform"
        else decay**np.arange(len(origins)-1,-1,-1,dtype=float)
    )
    grid=np.linspace(0,1,grid_points)
    return {
        mode:select_mean_difference_cv(
            y,order=d,window=L,horizon=h,
            historical_origins=origins,smoothness_grid=grid,
            mean_mode=mode,weights=weights,
        ) for mode in MODE_LABELS
    }


def main():
    st.set_page_config(
        page_title="Trend simulation · Mean difference forecast-CV",
        layout="wide",
    )
    st.title("Trend forecasting with a nonzero mean difference")
    st.caption(
        "NEW working paper. Guerrero (2007) already introduced the "
        "observed-difference mean; we investigate profiling one common μ(S) "
        "by completed historical forecast losses before choosing S. "
        "Exploratory interface, not publication evidence."
    )
    source=st.sidebar.selectbox(
        "Observed series source",
        ["Synthetic formula","Cortés-Toto source generator",
         "CSV upload","Yahoo Finance"],
    )
    frame=load_data(source)
    frame=frame.replace([np.inf,-np.inf],np.nan).dropna(subset=["observed"]).reset_index(drop=True)
    y=frame["observed"].to_numpy(dtype=float)
    if len(y)<40:
        st.warning("At least 40 observed values are required.")
        st.stop()
    d=st.sidebar.selectbox("Difference order d",[1,2,3,4],index=1)
    h=st.sidebar.slider("Operational horizon h",1,min(12,max(1,(len(y)-10)//5)),3)
    holdout=st.sidebar.checkbox("Reserve final h points for external evaluation",True)
    T=len(y)-h if holdout else len(y)
    minimum=max(d+2,8)
    maximum=min(120,T-h-3)
    if maximum<minimum:
        st.warning("Not enough completed observations for this horizon and order.")
        st.stop()
    L=st.sidebar.slider("Fit width L",minimum,maximum,min(40,maximum))
    stride=st.sidebar.slider("Historical-origin spacing",1,12,min(3,h))
    max_folds=st.sidebar.slider("Maximum completed forecast folds",3,50,16)
    grid_points=st.sidebar.select_slider(
        "Grid points including S=0 and S=1",
        options=[31,61,101,161,321],value=101,
    )
    weight=st.sidebar.selectbox(
        "Weights for completed forecast-loss functions",
        ["uniform","exponential"],
    )
    decay=st.sidebar.slider("Exponential origin decay",0.1,1.,0.8,0.05)
    if T<L+h:
        st.warning("Need a fit window plus at least one completed h-step block.")
        st.stop()
    try:
        results=calculate(
            tuple(y[:T]),d=d,L=L,h=h,stride=stride,
            max_folds=max_folds,grid_points=grid_points,
            weighting=weight,decay=decay,
        )
    except Exception as exc:
        st.error(f"Cannot calculate completed historical forecast CV: {exc}")
        st.stop()
    records=[]
    for mode,result in results.items():
        records.append({
            "Rule":MODE_LABELS[mode],
            "S selected":result.selected_s,
            "μ applied":result.selected_mu,
            "Historical forecast CV MSE":result.selected_loss,
            "Penalty-coordinate EDF":result.forecast_fit.penalty_edf,
            "Guerrero plug-in EDF":(
                result.forecast_fit.plugin_edf if mode=="guerrero" else np.nan
            ),
            "Folds":len(result.historical_origins),
            "μ identified by profile":(
                bool(result.identified_mu_by_s[
                    int(np.argmin(result.weighted_losses))
                ]) if mode=="profile" else np.nan
            ),
        })
    summary=pd.DataFrame.from_records(records)
    st.subheader("Three separately defined scientific decision rules")
    st.dataframe(summary,hide_index=True,use_container_width=True)
    st.caption(
        "Penalty EDF tr(H) is NOT the effective df of the full data-selected "
        "profile estimator; the separate plug-in EDF applies only when μ "
        "comes from the observed differences within a fit window."
    )
    one,two,three=st.tabs([
        "Forecast and true trend","Forecast-CV loss curves","μ(S) and reproducible exports"
    ])
    with one:
        f=go.Figure()
        ts=np.arange(1,len(y)+1)
        f.add_scatter(
            x=ts[:T],y=y[:T],name="Observed history y",
            mode="lines",line={"width":1.2},
        )
        if holdout:
            f.add_scatter(
                x=ts[T:],y=y[T:],name="Outer observed test — display only",
                mode="lines+markers",line={"dash":"dot"},
            )
        if "latent" in frame.columns:
            f.add_scatter(
                x=ts,y=frame["latent"],name="True latent trend τ — display only",
                mode="lines",line={"color":"black","width":2},
            )
        for mode,result in results.items():
            fit=result.forecast_fit
            c=COLOR[mode]
            f.add_scatter(
                x=np.arange(T-L+1,T+1),y=fit.fitted,
                name=f"{mode}: fitted τ",line={"color":c,"width":2},
            )
            f.add_scatter(
                x=np.arange(T+1,T+h+1),y=fit.forecast,
                mode="lines+markers",name=f"{mode}: forecast",
                line={"color":c,"dash":"dash","width":2},
            )
        f.add_vline(x=T+.5,line_dash="dot",
                    annotation_text="Future starts after this origin")
        f.update_layout(template="plotly_white",height=550,
                        xaxis_title="Observation index",yaxis_title="Level")
        st.plotly_chart(f,use_container_width=True)
        if holdout:
            mse=[]
            for mode,result in results.items():
                pred=result.forecast_fit.forecast
                val=float(np.mean((pred-y[T:T+h])**2))
                mse.append({"Rule":mode,"External observed MSE":val})
            st.dataframe(pd.DataFrame(mse),hide_index=True,use_container_width=True)
            st.warning(
                "Do not select a winning d/L/h/mode after inspecting these "
                "outer errors and reuse the same holdout as confirmation."
            )
    with two:
        fig=go.Figure()
        for mode,selected in results.items():
            fig.add_scatter(
                x=selected.grid,y=selected.weighted_losses,
                name=MODE_LABELS[mode],
                line={"color":COLOR[mode],"width":2},
            )
            fig.add_scatter(
                x=[selected.selected_s],y=[selected.selected_loss],
                mode="markers",showlegend=False,
                marker={"color":COLOR[mode],"size":10},
            )
        fig.update_layout(
            template="plotly_white",height=480,
            xaxis_title="Normalized penalty smoothness S",
            yaxis_title="Weighted completed historical h-step MSE",
        )
        st.plotly_chart(fig,use_container_width=True)
        st.caption(
            "For each S, μ(S) is selected by COMPLETED forecast losses. "
            "The profiled curve is not guaranteed convex/unimodal. "
            "Lower historical F for the more flexible model does NOT "
            "guarantee better external forecasting."
        )
    with three:
        selected=results["profile"]
        fig=go.Figure()
        fig.add_scatter(
            x=selected.grid,y=selected.mu_by_s,
            mode="lines",name="Analytically profiled μ(S)",
        )
        fig.add_hline(
            y=observed_mean_difference(y[T-L:T],d),
            line_dash="dash",annotation_text="Guerrero μ from final fit window",
        )
        fig.update_layout(
            template="plotly_white",height=390,
            xaxis_title="Normalized smoothness S",yaxis_title="Mean d-th difference μ",
        )
        st.plotly_chart(fig,use_container_width=True)
        st.download_button(
            "Download model comparison CSV",summary.to_csv(index=False),
            file_name="mean_difference_decisions.csv",mime="text/csv",
        )
        curves=pd.DataFrame({"S":selected.grid})
        for mode,item in results.items():
            curves[f"F_{mode}"]=item.weighted_losses
        curves["mu_profile"]=selected.mu_by_s
        st.download_button(
            "Download completed CV curves CSV",curves.to_csv(index=False),
            file_name="mean_difference_cv_surfaces.csv",mime="text/csv",
        )
        config={
            "paper":"Trend Simulation and Mean-Difference Forecasting",
            "protocol":"mean_difference_cv_v1",
            "source":source,"T":T,"d":d,"L":L,"h":h,
            "stride":stride,"max_folds":max_folds,
            "grid_points":grid_points,"weights":weight,"decay":decay,
            "holdout":holdout,
            "oracle_latent_used_in_selection":False,
            "external_test_used_in_selection":False,
        }
        st.download_button(
            "Download configuration JSON",
            json.dumps(config,indent=2),
            file_name="mean_difference_config.json",mime="application/json",
        )
    st.caption(
        "The numerical and scientific hypotheses are documented in the "
        "new working paper's Markdown proof ledger and simulation atlas."
    )


if __name__=="__main__":
    main()
