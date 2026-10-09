"""CUDA formal-campaign invariants, without requiring CUDA for normal CI.

Full CPU/GPU agreement is an *explicit one-time preflight*, not a check
repeated for every formal Monte Carlo batch. A machine without CUDA
still tests the DGP expansion and argument/default contracts.
"""
from __future__ import annotations

import importlib.util
import numpy as np
import pytest

from experiments.smoothness_cv.simulation_dgps import D_SHAPES, grid_scenarios, make_series
from experiments.smoothness_cv.cuda_simulation import candidate_horizons, gpu_batch_evaluate
from experiments.smoothness_cv.run_simulation_campaign import arguments, config_from_args
from experiments.smoothness_cv.simulation_evaluation import evaluate_replication


def test_stress_and_mega_are_balanced_and_reproducible():
    stress=grid_scenarios("stress")
    mega=grid_scenarios("mega")
    assert len(D_SHAPES)==12
    assert len(stress)==720
    assert len(mega)==1248
    assert len({s.key for s in mega})==len(mega)
    assert {s.study for s in stress}=={"D"}
    assert {s.noise for s in stress}=={
        "iid","ar1","student_t","heteroskedastic","contaminated",
    }
    assert {s.n_obs for s in stress}=={300,600}
    assert {s.seasonal for s in stress}=={False,True}
    for shape in D_SHAPES:
        s=next(s for s in stress if s.shape==shape)
        a=make_series(s,4)
        b=make_series(s,4)
        assert np.array_equal(a.observed,b.observed)
        assert np.all(np.isfinite(a.observed))
        assert np.all(np.isfinite(a.trend))
        assert np.allclose(a.observed,a.trend+a.seasonality+a.noise)
        assert np.ptp(a.trend)==pytest.approx(4.,abs=1e-10)


def test_vectorized_external_scoring_matches_scalar_reference():
    from experiments.smoothness_cv.simulation_evaluation import _score, _score_many
    scenario=grid_scenarios("stress")[0]
    generated=make_series(scenario,5)
    T=220
    chosen={"left":0.,"inner":.3425,"right":1.,"other":.9375}
    scores=_score_many(
        generated.observed,generated.trend,generated.seasonality,
        T=T,L=scenario.window,h=6,d=2,
        choices=chosen,grid_points=161,
    )
    for name,s in chosen.items():
        ref=_score(generated.observed,generated.trend,generated.seasonality,
                   T=T,L=scenario.window,h=6,d=2,s=s)
        got=scores[name]
        for field in (
            "selected_s","edf","raw_guerrero_s",
            "forecast_mse_obs","forecast_mae_obs",
            "forecast_mse_latent","forecast_mse_conditional",
            "past_recovery_mse","fit_residual_mse",
        ):
            assert got[field]==pytest.approx(ref[field],rel=1e-9,abs=1e-10)
        assert got["selected_lambda"]==pytest.approx(ref["selected_lambda"])
        assert np.allclose(
            np.asarray(__import__("json").loads(got["lead_squared_errors"])),
            np.asarray(__import__("json").loads(ref["lead_squared_errors"])),
            rtol=1e-9,atol=1e-10,
        )


def test_cuda_formal_run_does_not_repeatedly_reference_cpu():
    args=arguments(["--backend","cuda","--preset","stress","--seeds","100"])
    assert args.gpu_verify==0
    assert args.gpu_batch_size>0
    cfg=config_from_args(args)
    assert cfg["backend"]=="cuda"
    assert cfg["gpu_verify"]==0
    assert cfg["gpu_mode"]=="formal-no-cpu-rechecks"
    assert cfg["gpu_kernel_dtype"]=="float32"
    assert len(cfg["scenario_keys"])==720
    assert len(config_from_args(arguments(["--preset","mega"]))["scenario_keys"])==1248


def test_candidate_horizon_preserves_short_source_replication():
    original=grid_scenarios("smoke")[0]
    assert candidate_horizons(original,(1,3,6,12))==(1,3)
    rare=grid_scenarios("stress")[0]
    assert candidate_horizons(rare,(1,3,6,12))==(1,3,6,12)


def test_cuda_module_imports_without_torch_installed():
    # CPU-only CI should be able to import these modules; torch is
    # required only if the CUDA backend is requested at runtime.
    import experiments.smoothness_cv.cuda_simulation as mod
    assert callable(mod.require_cuda)
    assert callable(mod.gpu_batch_evaluate)


def test_gpu_one_time_equivalence_small_replication_if_available():
    torch=pytest.importorskip("torch")
    if not torch.cuda.is_available():
        pytest.skip("CUDA device not available; execute on university workstation.")
    scenario=grid_scenarios("smoke")[0]
    kwargs=dict(orders=(2,),horizons=(1,),outer_count=2,
                max_folds=5,grid_points=21)
    gpu,audit=gpu_batch_evaluate(
        scenario,[7,8],verify=2,torch=torch,**kwargs,
    )
    assert len(gpu)==2
    assert sum(item.checks for item in audit)>=2
    assert max(item.maximum_relative_error for item in audit)<1e-3
    assert all(rows for _,_,rows in gpu)
    cpu=evaluate_replication(scenario,7,**kwargs)
    produced=gpu[0][2]
    def key(r):
        return (r["origin"],r["d"],r["h"],r["selector"])
    lhs={key(r):r for r in cpu}
    rhs={key(r):r for r in produced}
    assert lhs.keys()==rhs.keys()
    for k in lhs:
        # Four classical criteria, fixed S and oracles are CPU and
        # therefore should be identical. Pooled/tracked could switch S
        # when competing extrema are within float32 rounding.
        if not k[-1].startswith(("pooled_","tracked_")):
            assert lhs[k]["selected_s"]==pytest.approx(rhs[k]["selected_s"])
        assert abs(lhs[k]["forecast_mse_obs"]-rhs[k]["forecast_mse_obs"])<0.1
