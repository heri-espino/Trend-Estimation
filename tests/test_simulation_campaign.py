"""Low-cost correctness and resumability checks for the prospective big campaign."""
from __future__ import annotations

import json
import sqlite3

import numpy as np
import pytest

from experiments.smoothness_cv.simulation_dgps import (
    Scenario, grid_scenarios, make_series,
)
from experiments.smoothness_cv.simulation_evaluation import (
    _spectral_candidates, evaluate_replication, outer_origins,
)
from experiments.smoothness_cv.analyze_simulation_campaign import analyze
from experiments.smoothness_cv.run_simulation_campaign import (
    main as campaign_main, config_from_args, arguments, digest, resolve_jobs,
)
from trend_estimation.selection.classical import pure_smoother_score


def test_factorial_cell_counts_and_source_a_precision():
    assert len(grid_scenarios("smoke")) == 3
    assert len(grid_scenarios("pilot")) == 36
    assert len(grid_scenarios("extensive")) == 528
    a=[s for s in grid_scenarios("extensive") if s.study=="A"]
    assert len(a)==16
    assert {s.shape for s in a}=={"source_linear","source_beta"}
    assert {s.sigma for s in a}=={.5,2.0}
    assert {s.seasonal for s in a}=={False,True}
    assert {s.n_obs for s in a}=={50,200}
    s=Scenario("A","source_linear",50,.5,"iid",True)
    generated=make_series(s,seed=4)
    assert np.allclose(generated.trend,4*np.arange(1,51)/50)
    assert np.allclose(generated.seasonality[:4],[1,-.5,-2.5,2])
    assert np.allclose(
        generated.observed,
        generated.trend+generated.seasonality+generated.noise,
    )


def test_seed_determinism_and_different_shapes_and_regimes():
    a=Scenario("B","quadratic_up",180,.5,"iid")
    b=Scenario("C","variance_change",240,.8,"ar1")
    one=make_series(a,seed=12)
    two=make_series(a,seed=12)
    other=make_series(a,seed=13)
    assert np.array_equal(one.observed,two.observed)
    assert not np.array_equal(one.observed,other.observed)
    assert np.isclose(np.ptp(one.trend),4.)
    assert len(make_series(b,seed=12).trend)==240


def test_joint_outer_origins_have_no_horizon_leakage():
    s=Scenario("B","linear",180,.5,"iid")
    horizons=(1,3,6,12)
    ts=outer_origins(s,horizons)
    assert ts==tuple(sorted(set(ts)))
    assert len(ts)==4
    for T in ts:
        assert T+max(horizons)<=s.n_obs
        assert T>=s.window+max(horizons)+7


def test_vectorized_classical_scores_match_exact_PLS_selectors():
    t=np.arange(30.,dtype=float)
    x=2+.02*t+np.sin(t/8)
    tau=2+.02*t
    grid,fits,choices,recovery=_spectral_candidates(
        x,tau,order=2,grid_points=31
    )
    for criterion in ("cv","gcv","aicc","bic"):
        evaluated=np.array([
            pure_smoother_score(x,order=2,smoothness=float(s),criterion=criterion).score
            for s in grid
        ])
        chosen=int(np.nanargmin(evaluated))
        assert choices[criterion]==pytest.approx(grid[chosen],abs=1e-12)
    assert choices["oracle_recovery"]==pytest.approx(grid[np.argmin(recovery)])
    assert np.isfinite(fits).all()


def test_smoke_replication_produces_paired_forecast_and_oracles():
    s=Scenario("A","source_linear",50,.5,"iid")
    results=evaluate_replication(
        s,seed=0,orders=(2,),horizons=(1,3),
        outer_count=2,max_folds=5,grid_points=11,
    )
    assert len(results)>10
    assert {1,3}=={r["h"] for r in results}
    assert {"pooled_uniform_all","tracked_uniform_all","classical_cv",
            "classical_gcv","classical_aicc","classical_bic",
            "oracle_recovery","oracle_latent_future"}.issubset(
               {r["selector"] for r in results}
            )
    assert all(r["selected_s"]>=0 and r["selected_s"]<=1 for r in results)
    assert all(np.isfinite(r["forecast_mse_obs"]) for r in results)
    assert all(np.isfinite(r["past_recovery_mse"]) for r in results)
    for r in results:
        assert len(json.loads(r["lead_squared_errors"]))==r["h"]
        assert r["edf"]==pytest.approx(r["L"]-(r["L"]-r["d"])*r["selected_s"])
        assert bool(r["is_oracle"])==r["selector"].startswith("oracle_")


def test_campaign_sqlite_is_atomic_and_resumable(tmp_path):
    args=[
        "--preset","smoke","--jobs","1","--max-tasks","1",
        "--outer-count","2","--max-folds","5",
        "--grid-points","11","--horizons","1",
        "--run-dir",str(tmp_path/"campaign"),
    ]
    assert campaign_main(args)==0
    db=sqlite3.connect(tmp_path/"campaign"/"outcomes.sqlite")
    assert db.execute("SELECT COUNT(*) FROM completed").fetchone()[0]==1
    first_count=db.execute("SELECT COUNT(*) FROM outcomes").fetchone()[0]
    assert first_count>0
    db.close()
    assert campaign_main(args)==0
    db=sqlite3.connect(tmp_path/"campaign"/"outcomes.sqlite")
    assert db.execute("SELECT COUNT(*) FROM completed").fetchone()[0]==2
    count=db.execute("SELECT COUNT(*) FROM outcomes").fetchone()[0]
    assert count>first_count
    assert db.execute("SELECT COUNT(*) FROM failures").fetchone()[0]==0
    db.close()
    manifest=json.loads((tmp_path/"campaign"/"manifest.json").read_text())
    assert manifest["fingerprint"]==digest(manifest["configuration"])

    # Analysis must work on *partial* checkpointed databases without
    # treating correlated folds as independent Monte Carlo seeds.
    report=analyze(tmp_path/"campaign",allow_partial=True)
    assert report["replications_complete"]==2
    reports=tmp_path/"campaign"/"reports"
    for name in (
        "scenario_method_summary.csv",
        "paired_scenario_comparisons.csv",
        "effects_by_shape.csv",
        "oracles_diagnostic_only.csv",
        "README_RESULTS.md",
    ):
        assert (reports/name).is_file()


def test_source_paper_factorial_uses_full_N_not_rolling_window(tmp_path):
    from experiments.smoothness_cv.run_cortes_toto_replication import main
    folder=tmp_path/"source"
    assert main([
        "--seeds","1","--jobs","1","--grid-points","11",
        "--max-tasks","1","--run-dir",str(folder),
    ])==0
    conn=sqlite3.connect(folder/"source_factorial.sqlite")
    rows=conn.execute(
        "SELECT N,criterion,edf,S_Guerrero,S_normalized "
        "FROM outcomes ORDER BY criterion"
    ).fetchall()
    conn.close()
    assert len(rows)==4
    assert all(N==50 for N,_,_,_,_ in rows)
    assert {name for _,name,_,_,_ in rows}=={"cv","gcv","aicc","bic"}
    for N,_,edf,raw,s in rows:
        assert raw==pytest.approx(1-edf/N)
        assert s==pytest.approx((N-edf)/(N-2))
    assert (folder/"reports"/"source_factorial_by_cell.csv").is_file()


def test_cpu_worker_count_can_use_all_32_logical_cores():
    assert resolve_jobs(32)==32
    assert resolve_jobs(1)==1
    assert config_from_args(arguments(["--preset","smoke"]))["seeds"]==1
