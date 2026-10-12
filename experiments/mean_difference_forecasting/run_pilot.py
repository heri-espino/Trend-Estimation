"""Pilot for new NONZERO mean-difference paper, separate from ongoing CUDA campaign.

Run from repository root:
    python -m experiments.mean_difference_forecasting.run_pilot --dry-run
    python -m experiments.mean_difference_forecasting.run_pilot --seeds 5 --max-cells 6

Pure/Guererro/profiled mu use the SAME pretest rolling origins, same
observations, same smoothness grid, same outer horizon, and separate
fully held-out external test. Trends are known only in the evaluator.
No claim of GPU support or verified large-scale experiment yet.

Results saved as one CSV row per (scenario,seed,origin,d,h,method);
append-safe for interruptions, with a matching JSON config manifest.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import time

import numpy as np

from experiments.smoothness_cv.pooled_lab import chronological_origins
from experiments.smoothness_cv.simulation_dgps import grid_scenarios, make_series
from experiments.smoothness_cv.simulation_evaluation import outer_origins
from experiments.smoothness_cv.standard_forecast_baselines import benchmark_predictions
from trend_estimation.core.difference import difference_matrix
from trend_estimation.forecasting.mean_difference_cv import select_mean_difference_cv


SELECTORS=("zero","guerrero","profile")
FIELDS=(
    "study","scenario","shape","noise","seasonal","sigma","N","L",
    "seed","T","d","h","method","s","mu","mu_true_history",
    "penalty_edf","plugin_edf","n_completed_folds",
    "weighted_cv_mse","observed_future_mse","latent_future_mse",
    "conditional_future_mse","past_latent_recovery_mse",
    "forecast_mae","lead_squared_errors","selected_mu_identified",
)


def arguments(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--seeds",type=int,default=5)
    p.add_argument("--seed-start",type=int,default=0)
    p.add_argument("--max-cells",type=int,default=6)
    p.add_argument("--shapes",default="linear,quadratic_turn,cubic_s")
    p.add_argument("--n-obs",type=int,choices=(180,360),default=360)
    p.add_argument("--orders",default="1,2,3")
    p.add_argument("--horizons",default="1,3,6")
    p.add_argument("--outer-count",type=int,default=3)
    p.add_argument("--max-folds",type=int,default=16)
    p.add_argument("--grid-points",type=int,default=41)
    p.add_argument("--weights",choices=("uniform","exponential"),default="uniform")
    p.add_argument("--decay",type=float,default=0.8)
    p.add_argument("--output",type=Path,
                   default=Path("results/mean_difference_forecasting/pilot_v1.csv"))
    p.add_argument("--dry-run",action="store_true")
    return p.parse_args(argv)


def choose_scenarios(shapes:tuple[str,...],n_obs:int,max_cells:int):
    all_cases=grid_scenarios("formal8h")
    # Group by shape first, then noise level: the same latent shape is
    # displayed across three noise SDs, not cherry-picked winners.
    chosen=[
        s for shape in shapes for s in all_cases
        if s.study=="B" and s.n_obs==n_obs and s.shape==shape
    ]
    if not chosen:
        raise ValueError("No study B scenario matched the requested shapes/length.")
    return tuple(chosen[:max_cells])


def historical_weights(n:int, *, kind:str, decay:float):
    if kind=="uniform":
        return np.ones(n,dtype=float)
    return decay**np.arange(n-1,-1,-1,dtype=float)


def replication_rows(scenario,seed:int, *, orders:tuple[int,...],
                     horizons:tuple[int,...],outer_count:int,
                     max_folds:int,grid_points:int,weights_kind:str,
                     decay:float) -> list[dict]:
    if len(orders)==0 or len(horizons)==0:
        raise ValueError("Need orders and horizons.")
    data=make_series(scenario,seed)
    valid=tuple(h for h in horizons
                if scenario.study!="A" or scenario.n_obs!=50 or h in (1,3))
    origins_external=outer_origins(scenario,valid,count=outer_count)
    grid=np.linspace(0.,1.,grid_points)
    rows=[]
    for T in origins_external:
        for h in valid:
            for d in orders:
                L=scenario.window
                if not 1<=d<L:
                    continue
                eligible=chronological_origins(
                    T,L,h,stride=h,max_folds=max_folds
                )
                assert np.all(eligible+h<=T), "Outer target leaked into CV."
                w=historical_weights(
                    len(eligible),kind=weights_kind,decay=decay
                )
                true_window=data.trend[T-L:T]
                mu_true=float(np.mean(difference_matrix(L,d)@true_window))
                for mode in SELECTORS:
                    chosen=select_mean_difference_cv(
                        data.observed[:T],order=d,window=L,horizon=h,
                        historical_origins=eligible,smoothness_grid=grid,
                        mean_mode=mode,weights=w,
                    )
                    fitted=chosen.forecast_fit.fitted
                    forecast=chosen.forecast_fit.forecast
                    future_obs=data.observed[T:T+h]
                    future_tau=data.trend[T:T+h]
                    future_cond=future_tau+data.seasonality[T:T+h]
                    error=future_obs-forecast
                    rows.append({
                        "study":scenario.study,"scenario":scenario.key,
                        "shape":scenario.shape,"noise":scenario.noise,
                        "seasonal":int(scenario.seasonal),
                        "sigma":float(scenario.sigma),
                        "N":int(scenario.n_obs),"L":int(L),
                        "seed":int(seed),"T":int(T),"d":int(d),"h":int(h),
                        "method":mode,"s":chosen.selected_s,
                        "mu":chosen.selected_mu,"mu_true_history":mu_true,
                        "penalty_edf":chosen.forecast_fit.penalty_edf,
                        "plugin_edf":chosen.forecast_fit.plugin_edf,
                        "n_completed_folds":len(eligible),
                        "weighted_cv_mse":chosen.selected_loss,
                        "observed_future_mse":float(np.mean(error**2)),
                        "latent_future_mse":float(np.mean((forecast-future_tau)**2)),
                        "conditional_future_mse":float(np.mean((forecast-future_cond)**2)),
                        "past_latent_recovery_mse":float(np.mean(
                            (fitted-true_window)**2
                        )),
                        "forecast_mae":float(np.mean(np.abs(error))),
                        "lead_squared_errors":json.dumps([float(v) for v in error**2]),
                        "selected_mu_identified":bool(
                            chosen.identified_mu_by_s[int(np.argmin(chosen.weighted_losses))]
                        ),
                    })
                # No artificial S or EDF for naive/drift/OLS.
                baselines=benchmark_predictions(data.observed[:T],T,L,h)
                for name in ("naive","drift","seasonal_naive","linear_ols"):
                    prediction=baselines[name]
                    err=data.observed[T:T+h]-prediction
                    rows.append({
                        "study":scenario.study,"scenario":scenario.key,
                        "shape":scenario.shape,"noise":scenario.noise,
                        "seasonal":int(scenario.seasonal),
                        "sigma":float(scenario.sigma),
                        "N":int(scenario.n_obs),"L":int(L),
                        "seed":int(seed),"T":int(T),"d":int(d),"h":int(h),
                        "method":name,"s":"","mu":"","mu_true_history":mu_true,
                        "penalty_edf":"","plugin_edf":"",
                        "n_completed_folds":len(eligible),
                        "weighted_cv_mse":"",
                        "observed_future_mse":float(np.mean(err**2)),
                        "latent_future_mse":float(np.mean(
                            (prediction-data.trend[T:T+h])**2
                        )),
                        "conditional_future_mse":float(np.mean(
                            (prediction-(data.trend[T:T+h]+data.seasonality[T:T+h]))**2
                        )),
                        "past_latent_recovery_mse":"",
                        "forecast_mae":float(np.mean(np.abs(err))),
                        "lead_squared_errors":json.dumps([float(v) for v in err**2]),
                        "selected_mu_identified":"",
                    })
    return rows


def main(argv=None):
    args=arguments(argv)
    if args.seeds<1 or args.seed_start<0 or args.max_cells<1:
        raise ValueError("Seeds and max-cells must be positive.")
    if args.grid_points<11 or args.max_folds<2 or args.outer_count<2:
        raise ValueError("Use >=11 grid levels and >=2 validation/outer origins.")
    if not (0<args.decay<=1):
        raise ValueError("Decay must lie in (0,1].")
    shapes=tuple(x.strip() for x in args.shapes.split(",") if x.strip())
    orders=tuple(int(x.strip()) for x in args.orders.split(",") if x.strip())
    horizons=tuple(int(x.strip()) for x in args.horizons.split(",") if x.strip())
    scenarios=choose_scenarios(shapes,args.n_obs,args.max_cells)
    config={
        "method":"mean_difference_cv_v1",
        "modes":list(SELECTORS),
        "scenarios":[s.key for s in scenarios],
        "seeds":args.seeds,"seed_start":args.seed_start,
        "orders":list(orders),"horizons":list(horizons),"outer_count":args.outer_count,
        "max_folds":args.max_folds,"grid_points":args.grid_points,
        "weights_kind":args.weights,"decay":args.decay,
        "n_obs":args.n_obs,"output":str(args.output),
        "status":"exploratory-pilot-not-confirmatory",
        "notes":"No CUDA yet; this is separate from existing mu=0 formal8h.",
    }
    print(json.dumps(config,indent=2),flush=True)
    if args.dry_run:
        return 0
    args.output.parent.mkdir(parents=True,exist_ok=True)
    manifest=args.output.with_suffix(".manifest.json")
    if manifest.exists():
        stored=json.loads(manifest.read_text(encoding="utf-8"))
        if stored!=config:
            raise ValueError("Existing pilot manifest differs; choose a new --output.")
    else:
        manifest.write_text(json.dumps(config,indent=2),encoding="utf-8")
    seen=set()
    if args.output.exists():
        with args.output.open(newline="",encoding="utf-8") as f:
            for row in csv.DictReader(f):
                seen.add((row["scenario"],int(row["seed"]),int(row["T"]),
                          int(row["d"]),int(row["h"]),row["method"]))
    started=time.perf_counter()
    with args.output.open("a",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=FIELDS)
        if not args.output.stat().st_size:
            writer.writeheader()
        for scenario in scenarios:
            for seed in range(args.seed_start,args.seed_start+args.seeds):
                rows=replication_rows(
                    scenario,seed,orders=orders,horizons=horizons,
                    outer_count=args.outer_count,max_folds=args.max_folds,
                    grid_points=args.grid_points,weights_kind=args.weights,
                    decay=args.decay,
                )
                new_rows=[row for row in rows if (
                    row["scenario"],row["seed"],row["T"],
                    row["d"],row["h"],row["method"]
                ) not in seen]
                if new_rows:
                    writer.writerows(new_rows)
                    f.flush()
                print(f"scenario={scenario.key} seed={seed} rows_new={len(new_rows)} "
                      f"elapsed={time.perf_counter()-started:.1f}s",flush=True)
    print(f"Pilot saved to {args.output}",flush=True)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
