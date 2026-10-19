"""Small, offline Study K same-25-seed replay and original-J parity tests.

CI never runs 4,800-shock/1.248M-row pilot; only 1-2 seeds.
"""
from __future__ import annotations

import csv
import gzip
import json

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.mean_difference_methods import (
    particular_polynomial
)
from experiments.pooled_loocv_smoothness.run_nonzero_difference_mean import (
    MeanScenario, compare_pool
)
from experiments.pooled_loocv_smoothness.run_nonzero_mu_nongaussian import (
    FINITE_REGIMES, NoiseShard, draw_pool, PILOT_REPS
)
from experiments.pooled_loocv_smoothness.run_cortes_criteria_pilot import (
    ALL_METHODS,NEW_METHODS,OLD_METHODS,PAIRS,CriteriaShard,
    evaluate_shock,calculate_shard,PROTOCOL
)
from experiments.pooled_loocv_smoothness.launch_cortes_criteria_pilot import (
    plan, execute as launch
)
from experiments.pooled_loocv_smoothness.aggregate_cortes_criteria_pilot import (
    collect,execute as aggregate
)


def test_25_seed_full_factorial_plan_exact_counts():
    full=plan()
    assert len(full)==192
    assert sum(x.shock_pools for x in full)==4800
    assert sum(x.treatment_pools for x in full)==48000
    assert sum(x.rows for x in full)==1248000
    assert len(NEW_METHODS)==18
    assert len(OLD_METHODS)==8
    assert len(PAIRS)==42
    assert len(set(ALL_METHODS))==26
    assert all(x.count==PILOT_REPS for x in full)
    with pytest.raises(ValueError):
        CriteriaShard("cauchy_observation",2,50,.5,0,1)
    with pytest.raises(ValueError):
        CriteriaShard("gaussian_iid",2,50,.5,25,1)


def test_one_replayed_shock_has_exact_seed_complete_method_coverage_and_pairing():
    sh=CriteriaShard("gaussian_iid",2,50,.5,0,1)
    result=evaluate_shock(sh,0,solver="bounded",scan_points=9)
    assert len(result)==2*5*26
    assert {x["seed"] for x in result}=={128000000}
    assert {x["R"] for x in result}=={1,3}
    assert {x["mu_factor"] for x in result}=={-1.,-.25,0.,.25,1.}
    for R in (1,3):
        for mu in (-1.,-.25,0.,.25,1.):
            a=[x for x in result if x["R"]==R and x["mu_factor"]==mu]
            assert len(a)==26
            assert {x["method"] for x in a}==set(ALL_METHODS)
            assert all(np.isfinite(x["true_trend_mse"]) for x in a)
            assert all(x["true_trend_mse"]>=0 for x in a)
            assert all(x["true_trend_mae"]>=0 for x in a)
            assert all(x["selected_lambda"]>=0 for x in a)
            assert all(0<=x["selected_s_nominal"]<=1 for x in a)
    # Shift-equivariant joint/fixed selector losses DO NOT change
    # across mu treatments in a fixed seed/R; they are not five iid draws.
    for R in (1,3):
        for method in ("cv_joint","gcv_joint","aicc_joint","bic_joint",
                       "controlled_S0.5_joint","cv_fixed"):
            scores=[next(x for x in result if x["method"]==method and
                         x["R"]==R and x["mu_factor"]==mu)["true_trend_mse"]
                    for mu in (-1.,-.25,0.,.25,1.)]
            assert max(scores)-min(scores)<1e-12


def test_new_zero_mu_cv_equals_existing_zero_mu_cv_at_matched_seed():
    sh=CriteriaShard("centered_gamma_right",2,50,2.,0,1)
    all_rows=evaluate_shock(sh,0,solver="bounded",scan_points=11)
    for R in (1,3):
        for mu in (-1.,0.,1.):
            a={x["method"]:x for x in all_rows
               if x["R"]==R and x["mu_factor"]==mu}
            # Different numerical optimizers (new bounded versus old
            # bounded) may select same criterion but differently only
            # within numerical tolerances.
            assert a["cv_zero"]["true_trend_mse"]==pytest.approx(
                a["existing__zero_mu_pooled_loocv"]["true_trend_mse"],
                rel=5e-4,abs=5e-4)


def test_tiny_shard_hashes_aggregate_and_original_baselines(tmp_path):
    root=tmp_path/"raw"
    sh=CriteriaShard("gaussian_iid",2,50,.5,0,1)
    folder=root/sh.suffix
    dry=calculate_shard(sh,folder,solver="bounded",scan_points=9,dry_run=True)
    assert dry["expected_method_rows"]==260
    assert not folder.exists()
    man=calculate_shard(sh,folder,solver="bounded",scan_points=9)
    assert man["protocol"]==PROTOCOL
    assert man["actual_method_rows"]==260
    with gzip.open(folder/"method_comparison.csv.gz","rt",encoding="utf-8",
                   newline="") as f:
        rec=list(csv.DictReader(f))
    assert len(rec)==260
    assert {x["seed"] for x in rec}=={"128000000"}
    summary=json.loads((folder/"summary.json").read_text())
    assert len(summary["by_R_mu_method"])==2*5*26
    assert len(summary["paired_R_mu_method_contrasts"])==2*5*42
    report,methods,pairs=collect(root,verify_digests=True,verify_prior=True)
    assert report["status"].startswith("INCOMPLETE_")
    assert report["independent_original_J_shock_draws_replayed"]==1
    assert len(methods)==260
    assert len(pairs)==420
    assert report["original_eight_method_parity"]["status"]=="checked_same_25_J_seeds"
    assert report["original_eight_method_parity"]["saved_J_baseline_cells_matched"]==80
    with pytest.raises(ValueError,match="Incomplete"):
        aggregate(root,tmp_path/"not_written",require_complete=True)
    ok=aggregate(root,tmp_path/"audit",verify_digests=True)
    assert ok["method_aggregate_cells"]==260
    assert (tmp_path/"audit"/"by_regime_d_N_eta_R_mu_26_methods.csv").is_file()
    assert (tmp_path/"audit"/"paired_criterion_vs_original_MLE_LOOCV_plugin.csv").is_file()
    again=launch([sh],root,workers=1,solver="bounded",scan=9)
    assert again["verified_existing"]==1
    overlap=CriteriaShard("gaussian_iid",2,50,.5,0,2)
    with pytest.raises(RuntimeError,match="OVERLAPPING"):
        launch([overlap],root,workers=1,solver="bounded",scan=9)


def test_incompatible_numerical_search_policy_does_not_resume(tmp_path):
    root=tmp_path/"mixed_solver"
    sh=CriteriaShard("gaussian_iid",2,50,.5,0,1)
    calculate_shard(sh,root/sh.suffix,solver="bounded",scan_points=9)
    with pytest.raises(RuntimeError,match="Incompatible"):
        launch([sh],root,workers=1,solver="multibracket",scan=9)
