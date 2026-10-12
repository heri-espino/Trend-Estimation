"""New mean-difference pilot is separate, matched, resumable, and leakage-free."""
from __future__ import annotations

import csv
import json
import numpy as np

from experiments.mean_difference_forecasting.run_pilot import (
    arguments,choose_scenarios,replication_rows,main,
)
from experiments.smoothness_cv.simulation_dgps import make_series


def test_pilot_noise_triplets_preserve_true_latent_shape():
    choices=choose_scenarios(("quadratic_turn",),360,3)
    assert len(choices)==3
    assert {s.sigma for s in choices}=={.25,.5,1.}
    same=[make_series(s,12) for s in choices]
    assert all(np.array_equal(same[0].trend,x.trend) for x in same)
    assert not np.array_equal(same[0].observed,same[-1].observed)


def test_short_pilot_has_matched_outer_forecast_rows_and_correct_missing_edf():
    scenario=choose_scenarios(("linear",),180,1)[0]
    rows=replication_rows(
        scenario,seed=1,orders=(1,),horizons=(1,),
        outer_count=2,max_folds=4,grid_points=11,
        weights_kind="uniform",decay=.8
    )
    assert len(rows)==2*7
    for T in {row["T"] for row in rows}:
        matching=[x for x in rows if x["T"]==T]
        assert {x["method"] for x in matching}=={
            "zero","guerrero","profile","naive","drift",
            "seasonal_naive","linear_ols",
        }
        for r in matching:
            assert r["observed_future_mse"]>=0
            assert r["latent_future_mse"]>=0
            assert r["conditional_future_mse"]>=0
            assert r["h"]==1
            if r["method"] in ("zero","guerrero","profile"):
                assert 0<=r["s"]<=1
                assert np.isfinite(r["mu"])
                assert r["past_latent_recovery_mse"]>=0
            else:
                assert r["s"]=="" and r["penalty_edf"]==""


def test_pilot_dry_run_and_resume_do_not_duplicate_rows(tmp_path):
    target=tmp_path/"pilot.csv"
    flags=[
        "--seeds","1","--max-cells","1","--orders","1",
        "--horizons","1","--outer-count","2","--max-folds","3",
        "--grid-points","11","--n-obs","180",
        "--shapes","linear","--output",str(target),
    ]
    assert main(flags+["--dry-run"])==0
    assert not target.exists()
    assert main(flags)==0
    assert target.exists()
    with target.open(newline="",encoding="utf-8") as f:
        first=list(csv.DictReader(f))
    assert len(first)==14
    assert main(flags)==0
    with target.open(newline="",encoding="utf-8") as f:
        second=list(csv.DictReader(f))
    assert len(second)==len(first)
    manifest=json.loads(target.with_suffix(".manifest.json").read_text())
    assert manifest["method"]=="mean_difference_cv_v1"
    assert manifest["status"]=="exploratory-pilot-not-confirmatory"
