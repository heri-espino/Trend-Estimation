"""Generalized order d=1..4, fast-vs-original and independent shard audits.

No 10,000-seed confirmation is launched from automated tests.
"""

from __future__ import annotations

import csv
import gzip
import json
from pathlib import Path

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.objective import (
    PooledLOOCV, difference_matrix
)
from experiments.pooled_loocv_smoothness.mean_difference_methods import (
    JointMeanPooledLOOCV, particular_polynomial,
    estimate_contrast_gaussian_mean,
)
from experiments.pooled_loocv_smoothness.run_nonzero_difference_mean import (
    METHODS, MeanScenario, draw_pool, compare_pool
)
from experiments.pooled_loocv_smoothness.run_nonzero_mean_multorder import (
    Shard, seed_for, fast_rows, calculate_shard, ORDERS, FULL_REPLICATES
)
from experiments.pooled_loocv_smoothness.aggregate_nonzero_mean_multorder import (
    collect, execute
)


@pytest.mark.parametrize("d", ORDERS)
def test_polynomial_and_latent_generation_at_all_orders(d):
    sc=MeanScenario(50,.5,.3,1.,d=d)
    y,tau=draw_pool(sc,R=3,seed=82500011+d)
    p=particular_polynomial(50,d)
    D=difference_matrix(50,d)
    np.testing.assert_allclose(D@p,np.ones(50-d),rtol=1e-6,atol=1e-6)
    assert np.all(np.isfinite(y))
    recovered=np.asarray([D@row for row in tau])
    # Stochastic innovations have population mean zero, not exact sample mean!
    assert abs(float(np.mean(recovered))-sc.mu)<.15
    assert np.all(np.isfinite(recovered))


@pytest.mark.parametrize("d", ORDERS)
def test_fast_affine_equivariance_matches_unmodified_full_methods(d):
    sc0=MeanScenario(24,.5,.3,0.,d=d)
    for R in (1,3):
        seed=82100020+d*100
        y0,tau0=draw_pool(sc0,R,seed)
        baseline={row["method"]:row for row in compare_pool(sc0,y0,tau0)}
        shift=MeanScenario(24,.5,.3,.25,d=d)
        p=particular_polynomial(24,d)
        y=y0+shift.mu*p[None,:]
        tau=tau0+shift.mu*p[None,:]
        expected={r["method"]:r for r in compare_pool(shift,y,tau)}
        actual={r["method"]:r for r in fast_rows(shift,y,tau,baseline)}
        assert set(expected)==set(actual)==set(METHODS)
        for method in METHODS:
            for name in ("true_mu","estimated_mu","mu_bias",
                         "realized_true_trend_mse","realized_trend_mae",
                         "reported_press_score","selected_s_nominal"):
                assert actual[method][name]==pytest.approx(
                    expected[method][name],abs=1e-5,rel=3e-5)
            a=actual[method]["selected_lambda"]
            b=expected[method]["selected_lambda"]
            if np.isinf(a) or np.isinf(b):
                assert np.isinf(a) and np.isinf(b)
            else:
                assert a==pytest.approx(b,abs=5e-4,rel=5e-4)


@pytest.mark.parametrize("d", ORDERS)
def test_n200_all_methods_have_finite_outputs_and_correct_spectral_rank(d):
    sc=MeanScenario(200,2.,.3,.25,d=d)
    y,tau=draw_pool(sc,R=3,seed=83010100+d)
    obj=PooledLOOCV(y,order=d)
    assert len(obj.eigenvalues)==200-d
    assert len(obj.u_null.T)==d
    assert np.isfinite(obj.score(1.))
    contrast=estimate_contrast_gaussian_mean(y,obj.d)
    assert np.isfinite(contrast.mu)
    assert np.isfinite(contrast.variance.lambda_ratio) or np.isinf(
        contrast.variance.lambda_ratio)
    joint=JointMeanPooledLOOCV(y,order=d)
    assert np.isfinite(joint.score(1.))
    # Test at one interior penalty to avoid long automated grid search.
    assert np.all(np.isfinite(joint.trend(1.)))


def test_shard_seeds_are_unique_across_all_factorial_cells():
    used=set()
    for d in ORDERS:
        for n in (50,200):
            for eta in (.5,2.):
                sh=Shard(d,n,eta,0,3)
                for rep in range(3):
                    s=seed_for(sh,rep)
                    assert s not in used
                    used.add(s)
    assert len(used)==48
    with pytest.raises(ValueError):
        Shard(4,200,2.,9999,2)
    with pytest.raises(ValueError):
        Shard(5,50,.5,0,1)


def test_tiny_compressed_shard_recovery_manifest_and_aggregation(tmp_path):
    root=tmp_path/"shards"
    sh=Shard(2,50,.5,0,2)
    out=root/sh.suffix
    planned=calculate_shard(sh,out,dry_run=True)
    assert not out.exists()
    assert planned["expected_method_rows"]==160
    complete=calculate_shard(sh,out)
    assert complete["actual_method_rows"]==160
    assert (out/"method_comparison.csv.gz").stat().st_size>0
    with gzip.open(out/"method_comparison.csv.gz","rt",encoding="utf-8",newline="") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==160
    assert {int(x["d"]) for x in rows}=={2}
    assert len({int(x["seed"]) for x in rows})==2
    assert all(float(x["realized_true_trend_mse"])>=0 for x in rows)
    with pytest.raises(FileExistsError):
        calculate_shard(sh,out)
    report,summary,paired=collect(root,check_csv_digest=True)
    assert report["status"].startswith("INCOMPLETE")
    assert report["total_independent_base_R3_shock_draws"]==2
    assert len(summary)==80
    assert len(paired)==40
    with pytest.raises(ValueError,match="incomplete"):
        execute(root,tmp_path/"must_not_exist",require_complete=True)
    aggregated=execute(root,tmp_path/"aggregated",require_complete=False)
    assert aggregated["distinct_cells_present"]==1
    assert (tmp_path/"aggregated"/"by_d_N_eta_R_mu_method.csv").is_file()
    assert (tmp_path/"aggregated"/"paired_MSE_contrasts_by_d_N_eta_R_mu.csv").is_file()
    with pytest.raises(FileExistsError):
        execute(root,tmp_path/"aggregated")


def test_aggregation_disallows_duplicate_seed_intervals(tmp_path):
    root=tmp_path/"root"
    sh=Shard(1,50,.5,0,1)
    output=root/sh.suffix
    calculate_shard(sh,output)
    import shutil
    target=root/"duplicate"/"same"
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copytree(output,target)
    with pytest.raises(ValueError,match="OVERLAPPING"):
        collect(root)



def test_full_d4_n200_large_curvature_has_finite_method_scores():
    """Catch ill-conditioned true d4 polynomial shifts, not only spectra."""
    from experiments.pooled_loocv_smoothness.mean_difference_methods import (
        particular_polynomial
    )
    from experiments.pooled_loocv_smoothness.run_nonzero_mean_multorder import (
        fast_rows
    )
    sc0=MeanScenario(200,2.,.3,0.,d=4)
    y,tau=draw_pool(sc0,3,seed=86000019)
    baseline={r["method"]:r for r in compare_pool(sc0,y,tau)}
    sc=MeanScenario(200,2.,.3,1.,d=4)
    p=particular_polynomial(200,4)
    shifted=fast_rows(sc,y+sc.mu*p[None,:],tau+sc.mu*p[None,:],baseline)
    assert {r["method"] for r in shifted}==set(METHODS)
    assert all(np.isfinite(r["realized_true_trend_mse"]) for r in shifted)
    assert all(np.isfinite(r["reported_press_score"]) for r in shifted)
    assert max(abs(r["true_mu"]-sc.mu) for r in shifted) < 1e-10


def test_manual_launcher_plans_160k_seeds_and_resume(tmp_path):
    from experiments.pooled_loocv_smoothness.launch_nonzero_mean_multorder import (
        plan, execute as launch
    )
    jobs=plan()
    assert len(jobs)==1600
    assert sum(x.count for x in jobs)==160000
    assert sum(x.groups for x in jobs)==1600000
    assert sum(x.rows for x in jobs)==12800000
    single=plan((1,),(50,),(0.5,),seed_start=0,seed_stop=1)
    assert len(single)==1
    root=tmp_path/"campaign"
    first=launch(single,root,workers=1)
    assert first["new_completed"]==1
    again=launch(single,root,workers=1)
    assert again["verified_existing"]==1
    assert first["verified_existing"]==0
