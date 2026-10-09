"""Paper 3 app: stationary points and endpoint-aware search of a SINGLE F(S).

Run:
    streamlit run apps/numerical_methods.py

Unlike Paper 2 this never tracks minima between historical surfaces.
It does not use Validation 2. Existing root search is adaptive and
not a certificate that all stationary points are recovered.
"""
from __future__ import annotations

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
from experiments.smoothness_cv.pooled_lab import chronological_origins,all_grid_fold_losses
from experiments.smoothness_cv.weighted_surface_study import LossWeighting,weighted_surface_history
from trend_estimation.forecasting.objectives import prepare_rolling_pure_forecast_objective
from trend_estimation.validation.rolling_origin import RollingOriginSplit
from trend_estimation.core.smoothness import smoothness_to_lambda,smoothness_derivatives
from trend_estimation.selection.smoothness_numerical import find_stationary_points_smoothness


def weighted_analytic_objective(prepared, weights):
    """One fixed F: weighted loss and its exact lambda derivatives.

    With weights frozen in advance, differentiating the sum is valid.
    This callback is NOT a different statistical estimator.
    """
    w=np.asarray(weights,dtype=float)
    w=w/w.sum()
    if len(w)!=prepared.n_origins:
        raise ValueError("Weights and completed historical origins disagree.")
    delta=prepared.eigvals
    history=prepared.spectral_history
    continuation=prepared.spectral_to_future.T
    offset=prepared.prediction_offset
    truth=prepared.targets

    def calculate(lam:float):
        if lam<0:
            raise ValueError("lambda must be >=0.")
        if np.isinf(lam):
            a=np.zeros_like(delta);a[:prepared.nullity]=1
            a1=np.zeros_like(delta);a2=np.zeros_like(delta)
        else:
            a=1/(1+lam*delta)
            a1=-delta*a*a
            a2=2*delta*delta*a*a*a
        pred=(history*a)@continuation+offset
        pred1=(history*a1)@continuation
        pred2=(history*a2)@continuation
        residual=truth-pred
        v=np.mean(residual*residual,axis=1)
        d1=np.mean(-2*residual*pred1,axis=1)
        d2=np.mean(2*(pred1*pred1-residual*pred2),axis=1)
        return float(w@v),float(w@d1),float(w@d2)
    return calculate


@st.cache_data(show_spinner=False,max_entries=12)
def cached_numeric(values:tuple[float,...],L:int,d:int,h:int,
                   stride:int,nfolds:int,grid_points:int,
                   scheme:str,lookback:int,decay:float,
                   depth:int):
    y=np.asarray(values,dtype=float)
    T=len(y)-h
    origins=chronological_origins(T,L,h,stride,nfolds)
    splits=[RollingOriginSplit(train=slice(int(t)-L,int(t)),
                               validation=slice(int(t),int(t)+h)) for t in origins]
    prep=prepare_rolling_pure_forecast_objective(y[:T],splits,order=d)
    grid=np.linspace(0,1,grid_points)
    losses=all_grid_fold_losses(prep,grid,L,d)
    method=LossWeighting("chosen",scheme,
                         None if lookback==0 else lookback,decay)
    weighted=weighted_surface_history(losses,method)
    start,w=method.weights(len(origins))
    full_weights=np.zeros(len(origins),dtype=float)
    full_weights[start:]=w
    callback=weighted_analytic_objective(prep,full_weights)
    # Numerical paper: search *one* current historical objective with
    # analytic derivatives, compare stationary candidates and boundaries.
    roots=find_stationary_points_smoothness(
        callback,n_obs=L,order=d,initial_grid_size=9,
        max_depth=depth,min_interval=0.001,
        boundary_margin=1e-6,
    )
    records=[]
    for point in roots.points_:
        records.append({
            "S":point.smoothness_,
            "lambda":point.lambda_,
            "F":point.objective_,
            "dF_dlambda":point.gradient_lambda_,
            "d2F_dlambda2":point.curvature_lambda_,
            "dF_dS":point.gradient_smoothness_,
            "d2F_dS2":point.curvature_smoothness_,
            "kind":point.kind_,
            "source":"adaptive",
        })
    for s in (0.,1.):
        val=callback(smoothness_to_lambda(s,L,d))[0]
        records.append({
            "S":s,"lambda":smoothness_to_lambda(s,L,d),"F":val,
            "dF_dlambda":float("nan"),"d2F_dlambda2":float("nan"),
            "dF_dS":float("nan"),"d2F_dS2":float("nan"),
            "kind":"boundary","source":"exact_endpoint",
        })
    candidates=pd.DataFrame(records).sort_values(["S","F"]).reset_index(drop=True)
    eligible=candidates[candidates.kind.isin(["minimum","flat","boundary"])]
    if eligible.empty:
        candidate_s=float(grid[np.argmin(weighted[-1])])
        best_source="grid fallback"
        candidate_loss=float(np.min(weighted[-1]))
    else:
        best=eligible.sort_values(["F","S"]).iloc[0]
        candidate_s=float(best.S)
        candidate_loss=float(best.F)
        best_source=str(best.source)
    # gradient in smoothness coordinates is not always well conditioned
    # extremely close to S=1. Plot interior only.
    grad=np.full(len(grid),np.nan)
    for i,s in enumerate(grid[1:-1],start=1):
        lam=smoothness_to_lambda(float(s),L,d)
        _,value1,_=callback(lam)
        slope,_=smoothness_derivatives(lam,n_obs=L,order=d)
        grad[i]=value1/slope
    return grid,origins,losses,weighted,candidates,roots.n_evaluations_,roots.n_brackets_,candidate_s,candidate_loss,best_source,grad


def main():
    st.set_page_config(page_title="Paper 3 · Numerical smoothness",layout="wide")
    st.title("Paper 3 · Numerical methods for smoothness selection")
    st.caption(
        "Investigate stationary points of ONE fixed, horizon-matched F(S). "
        "Adaptive derivative-root search, endpoint comparison and grid resolution "
        "are numerical questions—not temporal branch tracking."
    )
    source=st.sidebar.selectbox(
        "Source",["Synthetic formula","Cortés-Toto source generator","CSV upload","Yahoo Finance"]
    )
    frame=load_data(source)
    y=frame["observed"].dropna().to_numpy(float)
    if len(y)<40:
        st.error("At least 40 finite observations are required.")
        st.stop()
    d=st.sidebar.selectbox("Order d",[1,2,3,4],index=1)
    h=st.sidebar.slider("Declared forecast horizon h",1,min(20,(len(y)-10)//4),3)
    upper=min(120,len(y)-h-8)
    L=st.sidebar.slider("Fit window L",max(8,d+2),upper,min(40,upper))
    stride=st.sidebar.slider("Origin spacing",1,12,3)
    nfolds=st.sidebar.slider("Maximum completed origins",3,35,12)
    scheme=st.sidebar.selectbox(
        "Weighting of completed loss curves",
        ["uniform","linear","exponential"],
    )
    use_all=st.sidebar.checkbox("Use all completed origins",True)
    lookback=0 if use_all else st.sidebar.slider("Recent origin count K",2,30,8)
    decay=st.sidebar.slider("Exponential decay",0.2,1.,.8,.05)
    grid_points=st.sidebar.select_slider("Reference S grid",[31,61,101,161,321],value=101)
    depth=st.sidebar.slider("Adaptive search maximum depth",3,9,6)
    try:
        grid,origins,raw,weighted,candidates,evals,brackets,chosen_s,chosen_f,source_best,grad=cached_numeric(
            tuple(float(v) for v in y),L,d,h,stride,nfolds,
            grid_points,scheme,lookback,decay,depth,
        )
    except Exception as exc:
        st.error(f"Numerical experiment could not be completed: {exc}")
        st.stop()
    q1,q2,q3=st.columns(3)
    q1.metric("Best recovered candidate S",f"{chosen_s:.6f}")
    q2.metric("F at candidate",f"{chosen_f:.6g}")
    q3.metric("Derivative evaluations",str(evals))
    if source_best=="grid fallback":
        st.warning("Adaptive candidate set was empty; using a sampled-grid fallback.")
    tab1,tab2,tab3=st.tabs(
        ["Objective and stationary points","Spectral interpretation","Candidates / export"]
    )
    with tab1:
        f=go.Figure()
        f.add_scatter(x=grid,y=weighted[-1],mode="lines",name="Last weighted F(S)")
        valleys=candidates[candidates.kind.isin(["minimum","flat"])]
        if len(valleys):
            f.add_scatter(x=valleys.S,y=valleys.F,mode="markers",
                          name="Adaptive stationary candidates",
                          marker={"size":11,"symbol":"diamond"})
        boundaries=candidates[candidates.kind=="boundary"]
        f.add_scatter(x=boundaries.S,y=boundaries.F,mode="markers",
                      name="Exact S=0,1 endpoints",marker={"size":12,"symbol":"square"})
        f.add_vline(x=chosen_s,line_dash="dash",annotation_text="Best candidate")
        f.update_layout(template="plotly_white",height=490,
                        xaxis_title="Normalized smoothness S",
                        yaxis_title="Weighted historical forecast MSE")
        st.plotly_chart(f,use_container_width=True)
        g=go.Figure()
        g.add_scatter(x=grid,y=grad,mode="lines",name="Analytic dF/dS")
        g.add_hline(y=0,line_dash="dash")
        g.update_layout(template="plotly_white",height=320,xaxis_title="S",
                        yaxis_title="First derivative w.r.t S")
        st.plotly_chart(g,use_container_width=True)
        st.caption(
            f"{brackets} derivative sign-change brackets. Roots from adaptive "
            "sampling are not a completeness certificate; tangent roots or "
            "narrow valleys can be missed. Exact endpoints are separately compared."
        )
    with tab2:
        st.latex(r"Q=D_d^\top D_d=U\operatorname{diag}(\delta_j)U^\top")
        st.latex(r"H_\lambda=U\operatorname{diag}((1+\lambda\delta_j)^{-1})U^\top")
        st.latex(r"S(\lambda)=\frac{L-\sum_j(1+\lambda\delta_j)^{-1}}{L-d}")
        st.latex(r"\frac{dH_\lambda}{d\lambda}=-H_\lambda QH_\lambda")
        st.write(
            "Classical identities—not independently new results. The theoretical "
            "questions concern stationary-root recovery, conditioning and the "
            "ability to isolate all minima of a structured rational forecast loss."
        )
        st.caption("The full objective is the weighted F for the DECLARED d,L,h; another h is another problem.")
    with tab3:
        st.dataframe(candidates,hide_index=True,use_container_width=True)
        st.download_button("Download stationary candidate table",candidates.to_csv(index=False),
                           "numerical_minima.csv",mime="text/csv")
        df=pd.DataFrame({"S":grid,"weighted_F":weighted[-1],"dF_dS":grad})
        st.download_button("Download F(S) and derivative samples",df.to_csv(index=False),
                           "numerical_F_derivatives.csv",mime="text/csv")
        matrix=pd.DataFrame(raw,columns=[f"S={s:.6f}" for s in grid])
        matrix.insert(0,"historical_origin",origins)
        st.download_button("Download raw rolling MSE matrix",
                           matrix.to_csv(index=False),"numerical_raw_losses.csv",
                           mime="text/csv")
    st.caption(
        "Current numerical exploration. A dense grid or finite adaptive search "
        "is NOT a proof of exhaustive stationary-point isolation."
    )


if __name__=="__main__":
    main()
