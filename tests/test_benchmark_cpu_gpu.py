"""Fast CPU tests for the optional float32 GPU-vs-CPU benchmark.

Does not import/require torch or a CUDA device to run these checks.
"""
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pytest

from experiments.smoothness_cv.benchmark_cpu_gpu import (
    build_real_inputs, numpy_loss, pooled_numpy_loss, run_benchmark,
)
from experiments.smoothness_cv.pooled_lab import all_grid_fold_losses
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.forecasting.objectives import PreparedRollingPureForecastObjective


def test_float32_pls_kernel_matches_existing_actual_forecast_loss():
    L, d, h, M, K = 24, 2, 3, 5, 21
    H, W, G, O, Y = build_real_inputs(
        batch=2,window=L,order=d,horizon=h,origins=M,
        grid_points=K,seed=7,
    )
    assert all(x.dtype == np.float32 for x in (H,W,G,O,Y))
    assert H.shape == (2,M,L)
    assert W.shape == (K,L)
    assert G.shape == (h,L)
    assert Y.shape == (2,M,h)

    got = numpy_loss((H,W,G,O,Y))
    assert got.shape == (2,M,K)
    assert got.dtype == np.float32
    for b in range(2):
        prepared = PreparedRollingPureForecastObjective(
            eigvals=cached_pure_solver(L,d).eigvals,
            spectral_history=H[b].astype(np.float64),
            spectral_to_future=G.astype(np.float64),
            prediction_offset=O[b].astype(np.float64),
            targets=Y[b].astype(np.float64),
            n_origins=M,n_scored=M*h,nullity=d,
        )
        expected = all_grid_fold_losses(
            prepared,np.linspace(0,1,K),window=L,order=d,
        )
        assert np.allclose(got[b],expected,rtol=5e-5,atol=1e-5)


def test_cpu_pool_splitting_does_not_change_losses():
    inputs = build_real_inputs(
        batch=5,window=20,order=2,horizon=2,
        origins=4,grid_points=11,seed=31,
    )
    expected = numpy_loss(inputs)
    with ThreadPoolExecutor(max_workers=3) as pool:
        got=pooled_numpy_loss(pool,inputs,jobs=3)
    assert np.array_equal(expected,got)


def test_cpu_only_benchmark_keeps_precision_and_reports_missing_gpu(monkeypatch):
    import experiments.smoothness_cv.benchmark_cpu_gpu as bench
    monkeypatch.setattr(bench,"_cuda_available",lambda:(None,"CUDA unavailable in test"))
    result,info = run_benchmark(
        batch_sizes=(1,3),window=22,order=2,horizon=2,
        origins=3,grid_points=11,jobs=1,
        repetitions=1,warmups=0,skip_cpu_pool=True,
    )
    assert info["arithmetic_dtype"]=="float32"
    assert info["cuda_available"] is False
    assert result["float_dtype"].tolist()==["float32","float32"]
    assert (result.cpu_1_seconds>0).all()
    assert result.cuda_transfer_seconds.isna().all()
    assert result.gpu_vs_cpu_1_full_speedup.isna().all()


def test_invalid_shapes_are_rejected():
    with pytest.raises(ValueError):
        build_real_inputs(
            batch=2,window=8,order=8,horizon=1,
            origins=3,grid_points=11,seed=1,
        )
