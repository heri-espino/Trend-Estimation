"""CUDA batching of the actual joint Paper 1/Paper 2 Monte Carlo fold losses.

One CUDA device/context, many *independent series* in the first tensor
dimension, and all completed origins and candidate normalized-S levels
in the remaining dimensions. All statistical decisions (weights,
minima, branch tracking, classical criteria, refit, metrics) are still
made by simulation_evaluation.evaluate_replication.

No oracle target enters any GPU tuning loss. GPU is solely a float32
evaluation backend for the *same completed observed forecast losses*.
FP64 is retained for spectral eigenanalysis / S-to-lambda inversion.

Do not create a CUDA context in ProcessPoolExecutor worker processes.
"""
from __future__ import annotations

from dataclasses import dataclass
import time

import numpy as np

from experiments.smoothness_cv.pooled_lab import (
    all_grid_fold_losses, cached_uniform_spectral_weights, chronological_origins,
)
from experiments.smoothness_cv.simulation_dgps import GeneratedSeries, Scenario, make_series
from experiments.smoothness_cv.simulation_evaluation import (
    evaluate_replication, outer_origins,
)
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.forecasting.objectives import prepare_rolling_pure_forecast_objective
from trend_estimation.forecasting.operators import finite_difference_forecast_operator
from trend_estimation.validation.rolling_origin import RollingOriginSplit


@dataclass(frozen=True)
class GPUAudit:
    """Precision audit for a reference subset of completed-origin F matrices."""

    checks: int
    maximum_absolute_error: float
    maximum_relative_error: float
    differing_minima: int
    selected_regret: float


def require_cuda():
    """Lazily import CUDA; CPU-only installs can import this module safely."""
    try:
        import torch
    except ImportError as exc:
        raise RuntimeError(
            "CUDA simulations need PyTorch installed in this Conda environment."
        ) from exc
    if not torch.cuda.is_available():
        raise RuntimeError(
            "No PyTorch CUDA device is available. Verify torch CUDA build and "
            "nvidia-smi, or use --backend cpu."
        )
    # Avoid reduced-precision TF32 contractions when testing consistency of S.
    torch.backends.cuda.matmul.allow_tf32 = False
    if hasattr(torch.backends, "cudnn"):
        torch.backends.cudnn.allow_tf32 = False
    return torch


def candidate_horizons(scenario: Scenario, requested: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        h for h in requested
        if scenario.study != "A" or scenario.n_obs != 50 or h in (1, 3)
    )


def _actual_fold_losses(
    torch, observed: np.ndarray, *,
    T: int, d: int, L: int, h: int, max_folds: int,
    grid_points: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Batched GPU h-step loss on the exact production origins.

    Output shape = (B, M, K). The raw observations may include an outer
    future block, but we NEVER index it while producing tuning losses.
    """
    if T < L + h or observed.ndim != 2 or observed.shape[1] < T:
        raise ValueError("Insufficient *pretest* observations for h-step folds.")
    origins = chronological_origins(T, L, h, max(1, h), max_folds)
    if not np.all(origins + h <= T):
        raise AssertionError("Historical validation block extends beyond outer T.")
    B = len(observed)
    if B < 1:
        raise ValueError("Need at least one independent simulated series.")

    # CPU spectral preprocessing is done in FP64 to retain the exact
    # eigenvalue nullspace and precise normalized-S -> lambda mapping.
    solver = cached_pure_solver(L, d)
    U = solver.eigvecs
    indices = origins[:, None] - L + np.arange(L, dtype=int)[None, :]
    targets_idx = origins[:, None] + np.arange(h, dtype=int)[None, :]
    spectral = observed[:, indices] @ U
    targets = observed[:, targets_idx]
    filters = cached_uniform_spectral_weights(L, d, grid_points)
    G = finite_difference_forecast_operator(L, d, h).trend_matrix @ U

    device = torch.device("cuda")
    # FP32 multiplication matches the dedicated CPU vs CUDA benchmark.
    histories = torch.as_tensor(spectral, dtype=torch.float32, device=device)
    target_tensor = torch.as_tensor(targets, dtype=torch.float32, device=device)
    shrinkage = torch.as_tensor(filters, dtype=torch.float32, device=device)
    continuation = torch.as_tensor(G, dtype=torch.float32, device=device)
    K = grid_points

    # (K,h,L) -> (K*h,L), single batched GEMM across B*M origins.
    combined = (shrinkage[:, None, :] * continuation[None, :, :]).reshape(K * h, L)
    predictions = (histories.reshape(B * len(origins), L) @ combined.T).reshape(
        B, len(origins), K, h
    )
    squared = (target_tensor[:, :, None, :] - predictions).square()
    result = squared.mean(dim=-1).cpu().numpy()
    if not np.all(np.isfinite(result)) or np.any(result < 0):
        raise RuntimeError("CUDA forecast losses contain invalid values.")
    return result.astype(np.float64), origins


def _verify_cuda(
    observed: np.ndarray,
    losses: np.ndarray,
    origins: np.ndarray,
    *,
    T: int, d: int, L: int, h: int, grid_points: int,
    check_count: int, atol: float, rtol: float,
) -> GPUAudit:
    if check_count == 0:
        return GPUAudit(0, 0., 0., 0, 0.)
    subset = np.unique(
        np.linspace(0, len(observed) - 1, min(check_count, len(observed)))
        .round().astype(int)
    )
    splits = [
        RollingOriginSplit(
            train=slice(int(t) - L, int(t)),
            validation=slice(int(t), int(t) + h),
        )
        for t in origins
    ]
    grid = np.linspace(0., 1., grid_points)
    max_err = 0.
    max_rel = 0.
    diffs = 0
    max_regret = 0.
    for i in subset:
        prepared = prepare_rolling_pure_forecast_objective(
            observed[i, :T], splits, order=d
        )
        reference = all_grid_fold_losses(prepared, grid, L, d)
        actual = losses[i]
        error = np.abs(reference - actual)
        max_err = max(max_err, float(np.max(error)))
        max_rel = max(max_rel, float(np.max(error / (1 + np.abs(reference)))))
        if not np.allclose(actual, reference, atol=atol, rtol=rtol):
            raise RuntimeError(
                f"CUDA/CPU loss mismatch for T={T},h={h},d={d},"
                f"seed_batch_index={i}; max_abs={np.max(error):.5g}, "
                f"max_scaled={np.max(error/(1+np.abs(reference))):.5g}. "
                "Reduce batch size, inspect precision, or use --backend cpu."
            )
        # Check a *decision*, not just a kernel output. For each retained
        # prefix, the final weighted F for m=uniform_all is the average.
        cpu_min = int(np.argmin(reference.mean(axis=0)))
        gpu_min = int(np.argmin(actual.mean(axis=0)))
        if cpu_min != gpu_min:
            diffs += 1
            cpuF = reference.mean(axis=0)
            max_regret = max(max_regret, float(cpuF[gpu_min] - cpuF[cpu_min]))
            # A near-tied adjacent-cell switch is within FP32 discretion,
            # but a materially distinct S or a sizable risk gap is not.
            if abs(cpu_min - gpu_min) > 1 and (
                cpuF[gpu_min] - cpuF[cpu_min]
            ) > atol + rtol * max(1., abs(float(cpuF[cpu_min]))):
                raise RuntimeError(
                    "CUDA/CPU selected different nonnear-tied smoothness minima "
                    f"at T={T},h={h},d={d}: indices {gpu_min}, {cpu_min}."
                )
    return GPUAudit(len(subset), max_err, max_rel, diffs, max_regret)


def gpu_batch_evaluate(
    scenario: Scenario,
    seeds: list[int],
    *,
    orders: tuple[int,...],
    horizons: tuple[int,...],
    outer_count: int,
    max_folds: int,
    grid_points: int,
    verify: int = 0,  # formal runs never repeat CPU/GPU checks by default
    verify_atol: float = 1e-3,
    verify_rtol: float = 1e-3,
    torch=None,
) -> tuple[list[tuple[int, float, list[dict]]], list[GPUAudit]]:
    """Evaluate the *complete* existing selectors with CUDA-computed folds.

    A single scenario group must have the same N,L and order/horizon
    grid. Each independent simulated series remains identifiable by seed.
    """
    if not seeds:
        return [], []
    if torch is None:
        torch = require_cuda()
    else:
        if not torch.cuda.is_available():
            raise RuntimeError("The injected torch backend has no CUDA device.")
        torch.backends.cuda.matmul.allow_tf32 = False
    started = time.perf_counter()
    simulated: list[GeneratedSeries] = [make_series(scenario, seed) for seed in seeds]
    observations = np.stack([data.observed for data in simulated], axis=0)
    valid = candidate_horizons(scenario, horizons)
    if not valid:
        raise ValueError(f"No valid horizons for {scenario.key}.")
    outer = outer_origins(scenario, valid, count=outer_count)
    cache: list[dict[tuple[int,int,int],np.ndarray]] = [dict() for _ in seeds]
    audits: list[GPUAudit] = []
    for T in outer:
        for h in valid:
            for d in orders:
                matrix, origins = _actual_fold_losses(
                    torch, observations, T=T, d=d, L=scenario.window, h=h,
                    max_folds=max_folds, grid_points=grid_points,
                )
                audit = _verify_cuda(
                    observations, matrix, origins, T=T, d=d,
                    L=scenario.window, h=h, grid_points=grid_points,
                    check_count=verify, atol=verify_atol, rtol=verify_rtol,
                )
                audits.append(audit)
                for index in range(len(seeds)):
                    cache[index][(int(T),int(h),int(d))] = matrix[index]

    results = []
    for i, seed in enumerate(seeds):
        rows = evaluate_replication(
            scenario, seed, orders=orders, horizons=horizons,
            outer_count=outer_count, max_folds=max_folds,
            grid_points=grid_points, generated=simulated[i],
            precomputed_losses=cache[i],
        )
        if not rows:
            raise RuntimeError(f"GPU batch produced no output for seed={seed}.")
        results.append((int(seed), 0., rows))
    # Per-task timings must cover both the CUDA loss tensor *and* all
    # CPU selector/branch/classical work, not misleading kernel-only time.
    full_batch_seconds = (time.perf_counter()-started)/len(seeds)
    results = [(seed, full_batch_seconds, rows) for seed, _, rows in results]
    return results, audits
