"""Produce predeclared, interpretable simulated-trend forecast panels.

Requires a completed (or explicitly labelled partial) joint campaign.
Each panel shows the SAME latent tau and matched pooled/branch
forecasts across three noise amplitudes, plus the true test future.

This tool NEVER uses latent tau to choose a smoothing parameter.
It reads the *already selected* S in the frozen outcomes.sqlite and
re-fits only y[:T]. It does not select the "best-looking" scenario.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import numpy as np

from .pooled_lab import fit_window_forecast
from .simulation_dgps import grid_scenarios, make_series


DECLARED_EXAMPLES = (
    "linear","quadratic_turn","cubic_s","slope_break_late"
)
NOISE_LEVELS=(.25,.5,1.)
N=360
H=3
D=2


def selected_s(conn, scenario, seed, selector, h=H, d=D):
    row=conn.execute(
        """SELECT origin,selected_s FROM outcomes
            WHERE scenario=? AND seed=? AND selector=? AND h=? AND d=?
            ORDER BY origin DESC LIMIT 1""",
        (scenario,int(seed),selector,int(h),int(d)),
    ).fetchone()
    return (int(row[0]),float(row[1])) if row else None


def make_figures(run_dir:Path, *,seed:int=0, h:int=H, d:int=D):
    root=run_dir/"reports"/"figures"
    root.mkdir(parents=True,exist_ok=True)
    conn=sqlite3.connect(str(run_dir/"outcomes.sqlite"))
    lookup={s.key:s for s in grid_scenarios("formal8h")}
    shown=[]
    for shape in DECLARED_EXAMPLES:
        fig,axes=plt.subplots(1,3,figsize=(15,4.2),sharey=True)
        success=0
        for ax,sd in zip(axes,NOISE_LEVELS):
            key=f"B__{shape}__N{N}__iid__sd{sd:g}__seasonal0"
            scenario=lookup.get(key)
            if scenario is None:
                ax.set_visible(False)
                continue
            pooled=selected_s(conn,key,seed,"pooled_recent_exp_8",h,d)
            tracking=selected_s(conn,key,seed,"tracked_recent_exp_8",h,d)
            if pooled is None or tracking is None or pooled[0]!=tracking[0]:
                ax.set_visible(False)
                continue
            data=make_series(scenario,seed)
            T=pooled[0]
            L=scenario.window
            x=np.arange(1,T+h+1)
            ax.plot(x,data.trend[:T+h],label="True latent trend",lw=2.2)
            ax.scatter(
                x,data.observed[:T+h],label="Observed y",
                s=7,alpha=.32,zorder=2
            )
            for label,s,style in (
                ("Weighted pooled",pooled[1],"-"),
                ("Tracked branch",tracking[1],"--"),
            ):
                history,pred=fit_window_forecast(
                    data.observed[:T],origin=T,window=L,
                    order=d,horizon=h,smoothness=s,
                )
                ax.plot(np.arange(T-L+1,T+1),history,
                        style,lw=1.8,label=f"{label}: S={s:.3f}")
                ax.plot(np.arange(T+1,T+h+1),pred,style,
                        lw=2.1,marker="o",markersize=3)
            ax.axvline(T+.5,ls=":",lw=1,color="black")
            ax.set_xlim(max(1,T-L-3),T+h+1)
            ax.set_title(f"noise SD={sd:g}; T={T}")
            ax.set_xlabel("Time index (future starts right of dotted line)")
            ax.grid(alpha=.15)
            success+=1
        if success:
            axes[0].set_ylabel("Series level and h-step forecasts")
            axes[0].legend(fontsize=7,loc="best")
            fig.suptitle(
                f"PREDECLARED illustration: {shape}, d={d}, h={h}, seed={seed}\\n"
                "Same true trend; different Gaussian noise; same weighted F for both decisions"
            )
            fig.tight_layout()
            name=f"tau_forecast_{shape}_seed{seed}_d{d}_h{h}"
            fig.savefig(root/f"{name}.pdf",bbox_inches="tight")
            fig.savefig(root/f"{name}.png",dpi=180,bbox_inches="tight")
            shown.append(name)
        plt.close(fig)
    conn.close()
    status="INCOMPLETE EXPLORATORY" if len(shown)<len(DECLARED_EXAMPLES) else "ALL PREDECLARED EXAMPLES FOUND"
    (root/"README_FIGURES.md").write_text(
        "# Predeclared simulation figures\n\n"
        f"Status: **{status}**.\n"
        "The figure's underlying DGP is reproduced from scenario + seed; "
        "all forecasts use **only the pretest observed history** and "
        "previously chosen S from outcomes.sqlite. True latent tau is "
        "shown only as diagnostic ground truth, never for model fitting. "
        "The visible dotted T separates completed history and withheld "
        "outer h-step observations. Axes are shared across Gaussian noise "
        "levels for the SAME true trend. Curves use the SAME exponential "
        "weighted F for P1 and P2. Missing cells are not invented.\n\n"
        f"Figures created: {', '.join(shown) if shown else '(none yet)'}\n",
        encoding="utf-8",
    )
    return shown


def main(argv=None):
    p=argparse.ArgumentParser(description="Predeclared latent/observed/trend forecast figures.")
    p.add_argument("--run-dir",type=Path,required=True)
    p.add_argument("--seed",type=int,default=0)
    p.add_argument("--horizon",type=int,default=H)
    p.add_argument("--order",type=int,default=D)
    args=p.parse_args(argv)
    print(f"Figures saved: {make_figures(args.run_dir,seed=args.seed,h=args.horizon,d=args.order)}")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
