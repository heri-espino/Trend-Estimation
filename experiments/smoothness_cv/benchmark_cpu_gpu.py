"""Float32 CPU-vs-CUDA benchmark of the real PLS forecast-loss kernel.

Run from the repo root after installing trend-estimation:
    python -m experiments.smoothness_cv.benchmark_cpu_gpu --jobs 32

Benchmarks one NumPy CPU worker, a warm multi-process NumPy pool,
and PyTorch CUDA (resident tensors and transfer-inclusive). The inputs
are genuine rolling-window spectral PLS arrays with normalized-S weights,
not invented random matrix dimensions. All measured arithmetic is FLOAT32
on both CPU and GPU. The one-time eigendecomposition/S->lambda mapping
is the existing CPU preprocessing step and is timed separately.

This is an *isolated kernel benchmark*, not a full GPU implementation
of either paper's end-to-end experiment. Do not extrapolate its speedup
directly to the whole simulation campaign.
"""
from __future__ import annotations

import os
# Important: set BEFORE importing NumPy/SciPy/PyTorch, in spawned workers too.
for _key in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS",
):
    os.environ[_key] = "1"

import argparse
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import json
import multiprocessing as mp
from pathlib import Path
import platform
import statistics
import time

import numpy as np
import pandas as pd

from experiments.smoothness_cv.pooled_lab import cached_uniform_spectral_weights
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.forecasting.operators import finite_difference_forecast_operator


def build_real_inputs(
    *, batch: int, window: int, order: int, horizon: int,
    origins: int, grid_points: int, seed: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Create spectral inputs with the exact semantics of the paper's F_t(S).

    Inputs:
      spectral_history [batch, origins, window]
      spectral_filter  [S_grid, window]
      continuation     [horizon, window]
      offset           [batch, origins, horizon]
      targets          [batch, origins, horizon].
    """
    if min(batch, window, order, horizon, origins, grid_points) < 1:
        raise ValueError("All shape parameters must be positive.")
    if not 1 <= order < window or grid_points < 11:
        raise ValueError("Require 1 <= d < L and grid_points >= 11.")

    step = max(1, horizon)
    n = window + (origins - 1) * step + horizon + 1
    time_axis = np.arange(n, dtype=np.float64)
    rng = np.random.default_rng(seed)
    y = (
        5.0 + 0.018 * time_axis[None, :]
        + 0.9 * np.sin(time_axis[None, :] / 12.0)
        + rng.normal(0.0, 0.4, size=(batch, n))
    )
    t_origins = window + np.arange(origins) * step
    history = np.stack([
        y[:, int(t) - window:int(t)] for t in t_origins
    ], axis=1)
    targets = np.stack([
        y[:, int(t):int(t) + horizon] for t in t_origins
    ], axis=1)

    # The U, G and S mapping are identical to the production PLS path.
    U = cached_pure_solver(window, order).eigvecs
    spectral_history = history @ U
    continuation = finite_difference_forecast_operator(
        window, order, horizon
    ).trend_matrix @ U
    spectral_filter = cached_uniform_spectral_weights(window, order, grid_points)
    offset = np.zeros_like(targets)

    return tuple(np.ascontiguousarray(x, dtype=np.float32) for x in (
        spectral_history, spectral_filter, continuation, offset, targets
    ))


def numpy_loss(inputs: tuple[np.ndarray, ...], *, kernel="einsum") -> np.ndarray:
    """Exact PLS loss contraction: production einsum or equivalent GEMM.

    GEMM reformulation stacks the K*h (filter, horizon) products,
    then performs a single matrix multiply over the L spectral modes.
    """
    spectral_history, filters, future, offset, target = inputs
    if kernel == "einsum":
        predicted = np.einsum(
            "bml,kl,hl->bmkh",
            spectral_history, filters, future, optimize=True,
        )
    elif kernel == "gemm":
        batch, origins, L = spectral_history.shape
        K = filters.shape[0]
        h = future.shape[0]
        combined = (filters[:, None, :] * future[None, :, :]).reshape(K*h,L)
        predicted = (
            spectral_history.reshape(batch*origins,L) @ combined.T
        ).reshape(batch,origins,K,h)
    else:
        raise ValueError("kernel must be einsum or gemm")
    predicted = predicted + offset[:, :, None, :]
    return np.mean((target[:, :, None, :] - predicted) ** 2, axis=-1)


def _cpu_worker(payload) -> np.ndarray:
    inputs, kernel = payload
    return numpy_loss(inputs,kernel=kernel)


def pooled_numpy_loss(pool, inputs, jobs: int, *, kernel="einsum") -> np.ndarray:
    H, W, G, O, Y = inputs
    indices = [a for a in np.array_split(np.arange(len(H)), min(len(H), jobs))
               if a.size]
    chunks = [((H[ix], W, G, O[ix], Y[ix]),kernel) for ix in indices]
    return np.concatenate(list(pool.map(_cpu_worker, chunks)), axis=0)


def median_time(callable_, *, repetitions: int, warmups: int,
                synchronize=None):
    for _ in range(warmups):
        result = callable_()
        if synchronize is not None:
            synchronize()
    samples = []
    for _ in range(repetitions):
        if synchronize is not None:
            synchronize()
        start = time.perf_counter()
        result = callable_()
        if synchronize is not None:
            synchronize()
        samples.append(time.perf_counter() - start)
    return float(statistics.median(samples)), result


def _cuda_available():
    try:
        import torch
    except ImportError:
        return None, "PyTorch is not installed."
    if not torch.cuda.is_available():
        return None, (
            f"CUDA unavailable (torch={torch.__version__}, "
            f"torch CUDA build={torch.version.cuda})."
        )
    return torch, None


def _torch_loss(torch, arrays, *, kernel):
    H, W, G, O, Y = arrays
    if kernel == "einsum":
        pred = torch.einsum("bml,kl,hl->bmkh", H, W, G)
    elif kernel == "gemm":
        B, M, L = H.shape
        K = W.shape[0]
        h = G.shape[0]
        combined = (W[:, None, :] * G[None, :, :]).reshape(K*h,L)
        pred = (H.reshape(B*M,L) @ combined.T).reshape(B,M,K,h)
    else:
        raise ValueError("kernel must be einsum or gemm")
    pred = pred + O[:, :, None, :]
    return ((Y[:, :, None, :] - pred)**2).mean(dim=-1)


def cuda_results(torch, inputs, reference, *, kernel: str, repetitions: int, warmups: int):
    gpu = torch.device("cuda")
    resident = tuple(torch.as_tensor(a, dtype=torch.float32, device=gpu)
                     for a in inputs)
    torch.cuda.synchronize()
    torch.cuda.reset_peak_memory_stats()

    resident_seconds, _ = median_time(
        lambda: _torch_loss(torch, resident, kernel=kernel),
        repetitions=repetitions, warmups=warmups,
        synchronize=torch.cuda.synchronize,
    )

    def with_transfers():
        copies = tuple(torch.as_tensor(a, dtype=torch.float32, device=gpu)
                       for a in inputs)
        return _torch_loss(torch, copies, kernel=kernel).cpu().numpy()

    end_to_end_seconds, result = median_time(
        with_transfers, repetitions=repetitions, warmups=warmups,
        synchronize=torch.cuda.synchronize,
    )

    error = np.abs(result.astype(np.float64) - reference.astype(np.float64))
    # Optimize mean F across the M completed origins, for every series.
    cpu_choice = np.argmin(reference.mean(axis=1), axis=1)
    cuda_choice = np.argmin(result.mean(axis=1), axis=1)
    return {
        "cuda_resident_seconds":resident_seconds,
        "cuda_transfer_seconds":end_to_end_seconds,
        "max_absolute_loss_error":float(np.max(error)),
        "max_scaled_loss_error":float(np.max(
            error / (1.0 + np.abs(reference.astype(np.float64)))
        )),
        "different_selected_s_count":int(np.count_nonzero(cpu_choice != cuda_choice)),
        "cuda_peak_memory_mib":float(
            torch.cuda.max_memory_allocated() / (1024**2)
        ),
    }


def run_benchmark(
    *,
    batch_sizes=(1, 32, 256),
    window=72, order=2, horizon=6, origins=32,
    grid_points=161, jobs=32, repetitions=5, warmups=2,
    seed=73, require_cuda=False, skip_cpu_pool=False,
    tf32=False, kernel="gemm",
) -> tuple[pd.DataFrame, dict]:
    if any(b < 1 for b in batch_sizes) or jobs < 1:
        raise ValueError("Batch sizes and jobs must be positive.")
    if kernel not in {"einsum", "gemm"}:
        raise ValueError("kernel must be einsum or gemm")
    if repetitions < 1 or warmups < 0:
        raise ValueError("Require repetitions >= 1 and warmups >= 0.")
    if os.name == "nt" and jobs > 61:
        raise ValueError("Windows supports at most 61 worker processes.")

    torch, problem = _cuda_available()
    metadata = {
        "timestamp_utc":datetime.now(timezone.utc).isoformat(),
        "python":platform.python_version(),
        "platform":platform.platform(),
        "reported_logical_cpus":os.cpu_count(),
        "cpu_jobs":jobs,
        "arithmetic_dtype":"float32",
        "kernel_implementation":kernel,
        "spectral_preparation_dtype":"float64 then cast to float32",
        "cuda_available":problem is None,
        "cuda_status":problem or "available",
        "gpu_name":torch.cuda.get_device_name(0) if torch else None,
        "pytorch_version":str(torch.__version__) if torch else None,
        "cuda_build":str(torch.version.cuda) if torch else None,
        "tf32_enabled":bool(tf32),
        "kernel":"m×k×h forecast-loss surface via spectral PLS einsum",
        "pool_note":"Multiprocessing timing includes host interprocess copies; "
                    "this is not a complete Monte Carlo worker benchmark.",
    }
    if problem and require_cuda:
        raise RuntimeError(problem)
    if torch is not None:
        torch.backends.cuda.matmul.allow_tf32 = bool(tf32)
        if hasattr(torch.backends, "cudnn"):
            torch.backends.cudnn.allow_tf32 = bool(tf32)

    rows = []
    pool = None
    if not skip_cpu_pool and jobs > 1:
        pool = ProcessPoolExecutor(
            max_workers=jobs, mp_context=mp.get_context("spawn")
        )
    try:
        for batch in batch_sizes:
            prep_start=time.perf_counter()
            args=dict(batch=int(batch), window=window, order=order,
                      horizon=horizon, origins=origins,
                      grid_points=grid_points, seed=seed)
            inputs=build_real_inputs(**args)
            prep_seconds=time.perf_counter()-prep_start
            cpu_seconds, reference=median_time(
                lambda: numpy_loss(inputs,kernel=kernel),
                repetitions=repetitions, warmups=warmups,
            )
            if pool is not None:
                process_seconds, cpu_process_result = median_time(
                    lambda: pooled_numpy_loss(pool, inputs, jobs, kernel=kernel),
                    repetitions=repetitions, warmups=warmups,
                )
                cpu_pool_abs_diff=float(np.max(np.abs(
                    reference.astype(np.float64)
                    -cpu_process_result.astype(np.float64)
                )))
            else:
                process_seconds=float("nan")
                cpu_pool_abs_diff=float("nan")

            result={
                **args,
                "float_dtype":"float32",
                "kernel":kernel,
                "prep_seconds":prep_seconds,
                "cpu_1_seconds":cpu_seconds,
                "cpu_pool_seconds":process_seconds,
                "pool_vs_cpu_max_abs_error":cpu_pool_abs_diff,
                "cuda_resident_seconds":float("nan"),
                "cuda_transfer_seconds":float("nan"),
                "max_absolute_loss_error":float("nan"),
                "max_scaled_loss_error":float("nan"),
                "different_selected_s_count":float("nan"),
                "cuda_peak_memory_mib":float("nan"),
            }
            if torch is not None:
                result.update(cuda_results(
                    torch, inputs, reference, kernel=kernel,
                    repetitions=repetitions, warmups=warmups,
                ))
            result["gpu_vs_cpu_1_full_speedup"]=(
                cpu_seconds/result["cuda_transfer_seconds"]
                if np.isfinite(result["cuda_transfer_seconds"]) else float("nan")
            )
            result["gpu_vs_cpu_pool_full_speedup"]=(
                process_seconds/result["cuda_transfer_seconds"]
                if np.isfinite(result["cuda_transfer_seconds"])
                and np.isfinite(process_seconds) else float("nan")
            )
            rows.append(result)
            def seconds(value):
                return "n/a" if not np.isfinite(value) else f"{value:.5f}s"
            print(
                f"batch={batch} | CPU1={seconds(cpu_seconds)}"
                f" | CPU{jobs}={seconds(process_seconds)}"
                f" | CUDA resident={seconds(result['cuda_resident_seconds'])}"
                f" | CUDA+transfer={seconds(result['cuda_transfer_seconds'])}"
                f" | GPU/CPU{jobs} speedup={result['gpu_vs_cpu_pool_full_speedup']:.2f}x",
                flush=True,
            )
    finally:
        if pool is not None:
            pool.shutdown(wait=True)
    return pd.DataFrame(rows), metadata


def main(argv=None):
    p=argparse.ArgumentParser(description="Float32 PLS forecast-loss CPU vs CUDA throughput.")
    p.add_argument("--batch-sizes", default="1,32,256")
    p.add_argument("--window", type=int, default=72)
    p.add_argument("--order", type=int, default=2)
    p.add_argument("--horizon", type=int, default=6)
    p.add_argument("--origins", type=int, default=32)
    p.add_argument("--grid-points", type=int, default=161)
    p.add_argument("--jobs", type=int, default=32)
    p.add_argument("--repeats", type=int, default=5)
    p.add_argument("--warmup", type=int, default=2)
    p.add_argument("--seed", type=int, default=73)
    p.add_argument("--require-cuda", action="store_true")
    p.add_argument("--skip-cpu-pool", action="store_true")
    p.add_argument("--tf32", action="store_true",
                   help="Allow faster CUDA TF32 matrix kernels (may reduce accuracy).")
    p.add_argument("--kernel", choices=("einsum","gemm"), default="gemm",
                   help="einsum reproduces existing code; gemm is matrix-multiply form.")
    p.add_argument("--output", type=Path,
                   default=Path("results/smoothness_cv/gpu_benchmark"))
    args=p.parse_args(argv)
    sizes=tuple(int(s.strip()) for s in args.batch_sizes.split(",") if s.strip())
    if not sizes:
        p.error("Provide at least one batch size.")
    results, meta=run_benchmark(
        batch_sizes=sizes, window=args.window, order=args.order,
        horizon=args.horizon, origins=args.origins,
        grid_points=args.grid_points, jobs=args.jobs,
        repetitions=args.repeats, warmups=args.warmup,
        seed=args.seed, require_cuda=args.require_cuda,
        skip_cpu_pool=args.skip_cpu_pool, tf32=args.tf32,
        kernel=args.kernel,
    )
    args.output.mkdir(parents=True, exist_ok=True)
    results.to_csv(args.output/"timings_float32.csv", index=False)
    (args.output/"hardware.json").write_text(
        json.dumps(meta,indent=2,ensure_ascii=False),encoding="utf-8"
    )
    print(f"Results saved to {args.output}",flush=True)
    if meta["cuda_available"]:
        winners=results.loc[
            results["gpu_vs_cpu_pool_full_speedup"]>1.0,"batch"
        ].tolist()
        print(
            "GPU faster than CPU pool INCLUDING GPU transfers at batches: "
            f"{winners if winners else 'none measured'}.",
            flush=True,
        )
    else:
        print("GPU timings unavailable: no CUDA device; no GPU performance conclusion.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
