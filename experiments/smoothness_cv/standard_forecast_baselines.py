"""Predeclared non-PLS forecasting benchmarks on SAME rolling outer origins.

These competitors have NO selected S, lambda or EDF; never invent one
to force them into the PLS outcomes table.

- naive: yhat(T+k|T) = y_T
- drift: y_T + k (y_T - y_{T-L+1})/(L-1)
- seasonal_naive: repeat the last complete observed 4-point cycle
- linear_ols: ordinary least-squares linear extrapolation from last L

The first three are standard simple time-series forecasting benchmarks.
Use seasonal naive when the DGP has period-four seasonality; it may also
be reported as a deliberately mismatched control on nonseasonal DGPs.
"""
from __future__ import annotations

import json
import sqlite3

import numpy as np
from experiments.smoothness_cv.simulation_dgps import Scenario, make_series
from experiments.smoothness_cv.simulation_evaluation import outer_origins


def benchmark_predictions(y: np.ndarray, T: int, L: int, h: int) -> dict[str,np.ndarray]:
    """Fit ONLY y[:T], forecast h steps; results independent of d and S."""
    if T<L or L<4 or h<1:
        raise ValueError("Insufficient history or invalid L/h.")
    previous=np.asarray(y[T-L:T],dtype=float)
    k=np.arange(1,h+1,dtype=float)
    drift=(previous[-1]-previous[0])/(L-1)
    t=np.arange(L,dtype=float)
    b=float(np.sum((t-t.mean())*(previous-previous.mean())) /
            np.sum((t-t.mean())**2))
    a=float(previous.mean()-b*t.mean())
    return {
        "naive":np.full(h,previous[-1],dtype=float),
        "drift":previous[-1]+drift*k,
        "seasonal_naive":previous[-4:][np.arange(h)%4],
        "linear_ols":a+b*(L-1+k),
    }


def evaluate_standard_baselines(
    scenario: Scenario, seed: int,
    *, horizons: tuple[int,...], outer_count: int,
) -> list[dict]:
    data=make_series(scenario,seed)
    valid=tuple(h for h in horizons
                if scenario.study!="A" or scenario.n_obs!=50 or h in (1,3))
    origins=outer_origins(scenario,valid,count=outer_count)
    rows=[]
    for T in origins:
        for h in valid:
            forecasts=benchmark_predictions(data.observed,T,scenario.window,h)
            for name,forecast in forecasts.items():
                obs_error=data.observed[T:T+h]-forecast
                latent_error=data.trend[T:T+h]-forecast
                conditional_error=(
                    data.trend[T:T+h]+data.seasonality[T:T+h]-forecast
                )
                rows.append({
                    "scenario":scenario.key,"study":scenario.study,
                    "shape":scenario.shape,"noise":scenario.noise,
                    "sigma":float(scenario.sigma),
                    "n_obs":int(scenario.n_obs),"seed":int(seed),
                    "origin":int(T),"L":int(scenario.window),
                    "h":int(h),"baseline":name,
                    "forecast_mse_obs":float(np.mean(obs_error**2)),
                    "forecast_mse_latent":float(np.mean(latent_error**2)),
                    "forecast_mse_conditional":float(np.mean(conditional_error**2)),
                    "forecast_mae_obs":float(np.mean(np.abs(obs_error))),
                    "lead_squared_errors":json.dumps([float(v) for v in obs_error**2]),
                    "seasonal":int(scenario.seasonal),
                })
    return rows


def write_baselines(conn:sqlite3.Connection,rows:list[dict]):
    conn.execute(
        "CREATE TABLE IF NOT EXISTS forecast_baselines ("
        "scenario TEXT NOT NULL,seed INTEGER NOT NULL,"
        "origin INTEGER NOT NULL,h INTEGER NOT NULL,"
        "baseline TEXT NOT NULL,payload TEXT NOT NULL,"
        "PRIMARY KEY(scenario,seed,origin,h,baseline))"
    )
    conn.executemany(
        "INSERT OR REPLACE INTO forecast_baselines VALUES (?,?,?,?,?,?)",
        [(r["scenario"],r["seed"],r["origin"],r["h"],r["baseline"],
          json.dumps(r,sort_keys=True)) for r in rows]
    )
