"""Recreate an interpretable case without storing millions of full F matrices.

Run from the repo root, for example:
    python -m experiments.smoothness_cv.inspect_simulation_case \
      --preset pilot --scenario 'B__cubic_s__N180__iid__sd0.5__seasonal0' \
      --seed 0 --order 2 --horizon 3

Exports raw components, each temporal weighted F grid, local-minimum branch
trajectories, and per-method forecast decisions; optional Plotly HTML.
This inspection can be used *after* observing exploratory summary results,
but must not retroactively alter a frozen confirmatory method.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from .simulation_dgps import grid_scenarios, make_series
from .simulation_evaluation import outer_origins
from .weighted_surface_study import run_weighted_surface_study


def main(argv=None) -> int:
    p=argparse.ArgumentParser(description="Regenerate case-level F curves and branch histories.")
    p.add_argument("--preset",choices=("smoke","pilot","extensive"),default="pilot")
    p.add_argument("--scenario",required=True,help="Exact scenario key listed in the manifest.")
    p.add_argument("--seed",type=int,default=0)
    p.add_argument("--order",type=int,default=2)
    p.add_argument("--horizon",type=int,default=3)
    p.add_argument("--outer-index",type=int,default=-1)
    p.add_argument("--grid-points",type=int,default=161)
    p.add_argument("--max-folds",type=int,default=32)
    p.add_argument("--output",type=Path,default=Path("results/smoothness_cv/inspection"))
    p.add_argument("--html",action="store_true",help="Also render interactive Plotly HTML, requires plotly.")
    args=p.parse_args(argv)
    scenarios={s.key:s for s in grid_scenarios(args.preset)}
    if args.scenario not in scenarios:
        p.error("Scenario key not found in preset. Check --scenario spelling.")
    s=scenarios[args.scenario]
    horizons=(1,3) if s.study=="A" and s.n_obs==50 else (1,3,6,12)
    if args.horizon not in horizons:
        p.error(f"Allowed h values for this case: {horizons}")
    data=make_series(s,args.seed)
    ts=outer_origins(s,horizons)
    if not -len(ts)<=args.outer_index<len(ts):
        p.error("--outer-index is outside available chronological outer origins.")
    T=ts[args.outer_index]
    if T+args.horizon>s.n_obs:
        p.error("The selected horizon extends beyond generated series.")
    run=run_weighted_surface_study(
        data.observed[:T+args.horizon],orders=(args.order,),
        window=s.window,horizon=args.horizon,
        stride=max(args.horizon,1),
        max_folds=args.max_folds,grid_points=args.grid_points,
        refine_pooled=True,holdout=True,
    )
    target=args.output
    target.mkdir(parents=True,exist_ok=True)
    pd.DataFrame({
        "t":np.arange(1,s.n_obs+1),
        "observed":data.observed,"trend_true":data.trend,
        "seasonal":data.seasonality,"noise":data.noise,
        "available_at_outer_T":np.arange(s.n_obs)<T,
    }).to_csv(target/"generating_components.csv",index=False)
    run.summary.to_csv(target/"method_decisions.csv",index=False)
    run.branches.to_csv(target/"local_minima_branches.csv",index=False)
    combined=[]
    for (method,d),matrix in run.surfaces.items():
        table=pd.DataFrame(matrix,columns=[f"S={v:.6f}" for v in run.grid])
        table.insert(0,"origin",run.origins)
        table.to_csv(target/f"weighted_F_{method}_d{d}.csv",index=False)
        for k,origin in enumerate(run.origins):
            combined.append(pd.DataFrame({
                "method":method,"d":d,"origin":int(origin),
                "S":run.grid,"F":matrix[k],
            }))
    if args.html:
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
        fig=make_subplots(rows=2,cols=1,shared_xaxes=False,
                          subplot_titles=("Observed and true latent trend","Weighted F history"))
        t=np.arange(1,s.n_obs+1)
        fig.add_trace(go.Scatter(x=t,y=data.observed,name="observed"),row=1,col=1)
        fig.add_trace(go.Scatter(x=t,y=data.trend,name="latent"),row=1,col=1)
        for (method,d),matrix in run.surfaces.items():
            fig.add_trace(go.Scatter(x=run.grid,y=matrix[-1],
                       name=f"F latest {method}, d={d}"),row=2,col=1)
        fig.add_vline(x=T+.5,row=1,col=1,line_dash="dash")
        fig.update_layout(height=850,title=f"{s.key} seed={args.seed} T={T} h={args.horizon}")
        fig.write_html(str(target/"case_overview.html"),include_plotlyjs="cdn")
    pd.concat(combined,ignore_index=True).to_csv(
        target/"all_weighted_F_long.csv.gz",index=False,compression="gzip"
    )
    (target/"PROVENANCE.txt").write_text(
        f"scenario={s.key}\nseed={args.seed}\n"
        f"d={args.order}\nL={s.window}\nh={args.horizon}\n"
        f"T={T}\nwindow_ends_at={T}\n"
        f"outer_targets={T+1}..{T+args.horizon}\n"
        f"grid_points={args.grid_points}\n"
        "All F curves are from completed historical h-step losses only.\n",
        encoding="utf-8",
    )
    print(run.summary.to_string(index=False))
    print(f"Case exported to {target}")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
