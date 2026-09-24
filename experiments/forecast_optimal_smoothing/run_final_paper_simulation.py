from __future__ import annotations

import argparse
import hashlib
import json
import os

# Avoid nested BLAS/OpenMP oversubscription inside multiprocessing workers.
for _name in (
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ.setdefault(_name, "1")

import shutil
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import trend_estimation as td

from run_adaptive_value import (
    _block_metrics,
    _fit_frozen_forecast,
    _period,
    git_short_sha,
)


FINAL_HORIZONS = (1, 3, 6, 12)
SMOKE_HORIZONS = (1,)
MECHANISMS = ("persistence", "noise_scale", "roughness")
PATHS = ("stable_low", "low_to_high", "high_to_low", "stable_high")
PAIRING = (
    ("low_to_high", "stable_low", "stable_high"),
    ("high_to_low", "stable_high", "stable_low"),
)
CONVERGENCE_CHECKPOINTS = (100, 300, 500, 1000, 2000, 3000)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Final paper-scale Monte Carlo with process parallelism, atomic "
            "seed batches, automatic resume, and extensible seed targets."
        )
    )
    parser.add_argument("--preset", choices=("smoke", "final"), default="final")
    parser.add_argument(
        "--seeds",
        type=int,
        default=None,
        help="Target number of seeds per mechanism. Final default: 1000.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=None,
        help="Seeds persisted atomically per batch. Final default: 10.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help="Worker processes. 0=all available logical CPUs; 1=serial.",
    )
    parser.add_argument(
        "--run-id",
        type=str,
        default=None,
        help=(
            "Stable result directory name. Reusing it resumes the run after "
            "validating the scientific design and code signature."
        ),
    )
    parser.add_argument(
        "--aggregate-only",
        action="store_true",
        help="Skip simulation and rebuild cumulative summaries from completed batches.",
    )
    parser.add_argument("--n-obs", type=int, default=300)
    parser.add_argument("--regime-point", type=int, default=180)
    parser.add_argument("--outer-initial-train", type=int, default=120)
    parser.add_argument("--outer-step", type=int, default=3)
    parser.add_argument("--inner-step", type=int, default=3)
    parser.add_argument("--selector-max-inner-origins", type=int, default=20)
    parser.add_argument("--orders", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--windows", type=int, nargs="+", default=[24, 48, 72])
    parser.add_argument("--n-grid", type=int, default=None)
    parser.add_argument("--log-lambda-min", type=float, default=-18.0)
    parser.add_argument("--log-lambda-max", type=float, default=24.0)
    return parser.parse_args()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _json_bytes(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _hash_json(value) -> str:
    return hashlib.sha256(_json_bytes(value)).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _code_signature() -> str:
    root = _repo_root()
    paths = [Path(__file__).resolve()]
    paths.extend(sorted((root / "src" / "trend_estimation").rglob("*.py")))

    digest = hashlib.sha256()
    for path in paths:
        relative = path.relative_to(root)
        digest.update(str(relative).replace("\\", "/").encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _atomic_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")
    os.replace(tmp, path)


def _atomic_csv(frame: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    frame.to_csv(tmp, index=False)
    os.replace(tmp, path)


def _atomic_csv_gzip(frame: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    frame.to_csv(tmp, index=False, compression="gzip")
    os.replace(tmp, path)


def _resolve_workers(requested: int, n_tasks: int) -> int:
    requested = int(requested)
    if requested < 0:
        raise ValueError("workers must be >= 0.")
    if requested == 1:
        return 1
    logical = os.cpu_count() or 1
    chosen = logical if requested == 0 else requested
    return max(1, min(chosen, logical, int(n_tasks)))


def _path_pair(path: str, low: float, high: float) -> tuple[float, float]:
    if path == "stable_low":
        return low, low
    if path == "low_to_high":
        return low, high
    if path == "high_to_low":
        return high, low
    if path == "stable_high":
        return high, high
    raise ValueError(f"Unknown path: {path}")


def _mechanism_parameters(mechanism: str, path: str) -> dict[str, float]:
    if mechanism == "persistence":
        pre_phi, post_phi = _path_pair(path, 0.0, 0.8)
        return {
            "pre_phi": pre_phi,
            "post_phi": post_phi,
            "pre_observation_noise_std": 0.5,
            "post_observation_noise_std": 0.5,
            "pre_slope_noise_std": 0.01,
            "post_slope_noise_std": 0.01,
        }
    if mechanism == "noise_scale":
        pre_noise, post_noise = _path_pair(path, 0.25, 0.75)
        return {
            "pre_phi": 0.0,
            "post_phi": 0.0,
            "pre_observation_noise_std": pre_noise,
            "post_observation_noise_std": post_noise,
            "pre_slope_noise_std": 0.01,
            "post_slope_noise_std": 0.01,
        }
    if mechanism == "roughness":
        pre_slope, post_slope = _path_pair(path, 0.005, 0.02)
        return {
            "pre_phi": 0.0,
            "post_phi": 0.0,
            "pre_observation_noise_std": 0.5,
            "post_observation_noise_std": 0.5,
            "pre_slope_noise_std": pre_slope,
            "post_slope_noise_std": post_slope,
        }
    raise ValueError(f"Unknown mechanism: {mechanism}")


def _select_frozen(
    history,
    *,
    horizon: int,
    settings: dict,
    max_origins: int | None,
):
    return td.select_fixed_window_pure_smoothness(
        history,
        orders=tuple(settings["orders"]),
        windows=tuple(settings["windows"]),
        horizon=int(horizon),
        step=int(settings["inner_step"]),
        max_origins=max_origins,
        min_origins=2,
        log_bounds=tuple(settings["log_lambda_bounds"]),
        n_grid=int(settings["n_grid"]),
    ).best_


def run_configuration(
    *,
    seed: int,
    mechanism: str,
    path: str,
    horizon: int,
    settings: dict,
) -> list[dict]:
    params = _mechanism_parameters(mechanism, path)
    data = td.make_two_regime_local_linear_series(
        n_obs=int(settings["n_obs"]),
        regime_point=int(settings["regime_point"]),
        pre_slope_noise_std=params["pre_slope_noise_std"],
        post_slope_noise_std=params["post_slope_noise_std"],
        pre_observation_noise_std=params["pre_observation_noise_std"],
        post_observation_noise_std=params["post_observation_noise_std"],
        pre_ar1_phi=params["pre_phi"],
        post_ar1_phi=params["post_phi"],
        level_shift=0.0,
        slope_shift=0.0,
        random_state=int(seed),
    )

    rp = int(settings["regime_point"])
    pre_history = data.y[:rp]
    frozen_local = _select_frozen(
        pre_history,
        horizon=horizon,
        settings=settings,
        max_origins=int(settings["selector_max_inner_origins"]),
    )
    frozen_all_pre = _select_frozen(
        pre_history,
        horizon=horizon,
        settings=settings,
        max_origins=None,
    )

    adaptive = td.nested_rolling_pure_forecast(
        data.y,
        outer_initial_train=int(settings["outer_initial_train"]),
        horizon=int(horizon),
        outer_step=int(settings["outer_step"]),
        orders=tuple(settings["orders"]),
        windows=tuple(settings["windows"]),
        inner_step=int(settings["inner_step"]),
        max_inner_origins=int(settings["selector_max_inner_origins"]),
        min_inner_origins=2,
        log_bounds=tuple(settings["log_lambda_bounds"]),
        n_grid=int(settings["n_grid"]),
    )

    rows: list[dict] = []
    for record in adaptive.records:
        origin = int(record.origin)
        if origin < rp:
            continue

        history = data.y[:origin]
        observed = np.asarray(record.observed, dtype=float)
        adaptive_prediction = np.asarray(record.prediction, dtype=float)
        benchmark_prediction = np.asarray(record.benchmark_prediction, dtype=float)

        frozen_local_prediction = _fit_frozen_forecast(
            history,
            order=int(frozen_local.order),
            window=int(frozen_local.window),
            lambda_=float(frozen_local.lambda_),
            horizon=observed.size,
        )
        frozen_all_pre_prediction = _fit_frozen_forecast(
            history,
            order=int(frozen_all_pre.order),
            window=int(frozen_all_pre.window),
            lambda_=float(frozen_all_pre.lambda_),
            horizon=observed.size,
        )

        adaptive_mse, adaptive_rmse = _block_metrics(observed, adaptive_prediction)
        local_mse, local_rmse = _block_metrics(observed, frozen_local_prediction)
        all_pre_mse, all_pre_rmse = _block_metrics(
            observed,
            frozen_all_pre_prediction,
        )
        benchmark_mse, benchmark_rmse = _block_metrics(
            observed,
            benchmark_prediction,
        )

        relative_origin = origin - rp
        post_seen = max(0, relative_origin)
        adaptive_window = int(record.selected_window)

        rows.append(
            {
                "mechanism": mechanism,
                "path": path,
                "seed": int(seed),
                "horizon": int(horizon),
                "regime_point": rp,
                "outer_origin": origin,
                "relative_origin": relative_origin,
                "period": _period(relative_origin),
                **params,
                "adaptive_order": int(record.selected_order),
                "adaptive_window": adaptive_window,
                "adaptive_lambda": float(record.selected_lambda),
                "adaptive_smoothness": float(record.selected_smoothness),
                "adaptive_window_post_fraction": float(
                    min(adaptive_window, post_seen) / adaptive_window
                ),
                "frozen_local_order": int(frozen_local.order),
                "frozen_local_window": int(frozen_local.window),
                "frozen_local_lambda": float(frozen_local.lambda_),
                "frozen_local_smoothness": float(frozen_local.smoothness_),
                "frozen_local_n_origins": int(frozen_local.n_origins_),
                "frozen_all_pre_order": int(frozen_all_pre.order),
                "frozen_all_pre_window": int(frozen_all_pre.window),
                "frozen_all_pre_lambda": float(frozen_all_pre.lambda_),
                "frozen_all_pre_smoothness": float(frozen_all_pre.smoothness_),
                "frozen_all_pre_n_origins": int(frozen_all_pre.n_origins_),
                "adaptive_mse": adaptive_mse,
                "frozen_local_mse": local_mse,
                "frozen_all_pre_mse": all_pre_mse,
                "benchmark_mse": benchmark_mse,
                "adaptive_rmse": adaptive_rmse,
                "frozen_local_rmse": local_rmse,
                "frozen_all_pre_rmse": all_pre_rmse,
                "benchmark_rmse": benchmark_rmse,
                "adaptive_advantage_vs_frozen_local": local_mse - adaptive_mse,
                "adaptive_advantage_vs_frozen_all_pre": all_pre_mse - adaptive_mse,
            }
        )

    return rows


def _run_payload(payload) -> list[dict]:
    seed, mechanism, path, horizon, settings = payload
    return run_configuration(
        seed=int(seed),
        mechanism=str(mechanism),
        path=str(path),
        horizon=int(horizon),
        settings=settings,
    )


def _period_groups(group: pd.DataFrame):
    yield "all_post", group
    for period, part in group.groupby("period", dropna=False):
        yield str(period), part


def _seed_period_summary(frame: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for (mechanism, path, horizon, seed), group in frame.groupby(
        ["mechanism", "path", "horizon", "seed"],
        dropna=False,
    ):
        for period, part in _period_groups(group):
            rows.append(
                {
                    "mechanism": mechanism,
                    "path": path,
                    "horizon": int(horizon),
                    "seed": int(seed),
                    "period": period,
                    "n_blocks": int(len(part)),
                    "adaptive_mse": float(part["adaptive_mse"].mean()),
                    "frozen_local_mse": float(part["frozen_local_mse"].mean()),
                    "frozen_all_pre_mse": float(part["frozen_all_pre_mse"].mean()),
                    "benchmark_mse": float(part["benchmark_mse"].mean()),
                    "adaptive_advantage_vs_frozen_local": float(
                        part["adaptive_advantage_vs_frozen_local"].mean()
                    ),
                    "adaptive_advantage_vs_frozen_all_pre": float(
                        part["adaptive_advantage_vs_frozen_all_pre"].mean()
                    ),
                }
            )
    return pd.DataFrame(rows)


def _seed_excess_period(seed_period: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    keys = ["mechanism", "horizon", "seed", "period"]
    for direction, start_control, _ in PAIRING:
        transition = seed_period.loc[
            seed_period["path"].eq(direction),
            keys
            + [
                "adaptive_advantage_vs_frozen_local",
                "adaptive_advantage_vs_frozen_all_pre",
            ],
        ].copy()
        control = seed_period.loc[
            seed_period["path"].eq(start_control),
            keys
            + [
                "adaptive_advantage_vs_frozen_local",
                "adaptive_advantage_vs_frozen_all_pre",
            ],
        ].copy()
        transition = transition.rename(
            columns={
                "adaptive_advantage_vs_frozen_local": (
                    "transition_advantage_vs_frozen_local"
                ),
                "adaptive_advantage_vs_frozen_all_pre": (
                    "transition_advantage_vs_frozen_all_pre"
                ),
            }
        )
        control = control.rename(
            columns={
                "adaptive_advantage_vs_frozen_local": (
                    "control_advantage_vs_frozen_local"
                ),
                "adaptive_advantage_vs_frozen_all_pre": (
                    "control_advantage_vs_frozen_all_pre"
                ),
            }
        )
        paired = transition.merge(control, on=keys, validate="one_to_one")
        paired.insert(1, "direction", direction)
        paired.insert(2, "matched_control", start_control)
        paired["excess_advantage_vs_frozen_local"] = (
            paired["transition_advantage_vs_frozen_local"]
            - paired["control_advantage_vs_frozen_local"]
        )
        paired["excess_advantage_vs_frozen_all_pre"] = (
            paired["transition_advantage_vs_frozen_all_pre"]
            - paired["control_advantage_vs_frozen_all_pre"]
        )
        rows.extend(paired.to_dict("records"))
    return pd.DataFrame(rows)


def _tracking_path_stats(frame: pd.DataFrame) -> pd.DataFrame:
    keys = ["mechanism", "seed", "horizon", "relative_origin"]
    parts: list[pd.DataFrame] = []

    for direction, start_control, target_control in PAIRING:
        columns = keys + [
            "adaptive_order",
            "adaptive_window",
            "adaptive_smoothness",
            "adaptive_window_post_fraction",
        ]
        transition = frame.loc[frame["path"].eq(direction), columns].copy()
        start = frame.loc[frame["path"].eq(start_control), columns].copy()
        target = frame.loc[frame["path"].eq(target_control), columns].copy()

        rename = {
            "adaptive_order": "order",
            "adaptive_window": "window",
            "adaptive_smoothness": "smoothness",
            "adaptive_window_post_fraction": "window_post_fraction",
        }
        transition = transition.rename(
            columns={k: f"transition_{v}" for k, v in rename.items()}
        )
        start = start.rename(columns={k: f"start_{v}" for k, v in rename.items()})
        target = target.rename(columns={k: f"target_{v}" for k, v in rename.items()})

        paired = transition.merge(start, on=keys, validate="one_to_one")
        paired = paired.merge(target, on=keys, validate="one_to_one")
        paired["direction"] = direction
        paired["abs_smoothness_gap_to_target"] = np.abs(
            paired["transition_smoothness"] - paired["target_smoothness"]
        )
        paired["order_match_target"] = (
            paired["transition_order"] == paired["target_order"]
        ).astype(float)
        paired["window_match_target"] = (
            paired["transition_window"] == paired["target_window"]
        ).astype(float)
        paired["discrete_config_match_target"] = (
            (paired["transition_order"] == paired["target_order"])
            & (paired["transition_window"] == paired["target_window"])
        ).astype(float)
        parts.append(paired)

    paired = pd.concat(parts, ignore_index=True)
    stats = (
        paired.groupby(
            ["mechanism", "direction", "horizon", "relative_origin"],
            dropna=False,
        )
        .agg(
            n_pairs=("seed", "size"),
            transition_smoothness=("transition_smoothness", "mean"),
            start_smoothness=("start_smoothness", "mean"),
            target_smoothness=("target_smoothness", "mean"),
            mean_abs_smoothness_gap_to_target=(
                "abs_smoothness_gap_to_target",
                "mean",
            ),
            mean_transition_order=("transition_order", "mean"),
            mean_start_order=("start_order", "mean"),
            mean_target_order=("target_order", "mean"),
            mean_transition_window=("transition_window", "mean"),
            mean_start_window=("start_window", "mean"),
            mean_target_window=("target_window", "mean"),
            order_match_target_share=("order_match_target", "mean"),
            window_match_target_share=("window_match_target", "mean"),
            discrete_config_match_target_share=(
                "discrete_config_match_target",
                "mean",
            ),
            mean_transition_window_post_fraction=(
                "transition_window_post_fraction",
                "mean",
            ),
        )
        .reset_index()
    )
    return stats


def _batch_name(start_seed: int, end_seed: int) -> str:
    return f"batch_{start_seed:06d}_{end_seed:06d}"


def _batch_dir(run_dir: Path, start_seed: int, end_seed: int) -> Path:
    return run_dir / "batches" / _batch_name(start_seed, end_seed)


def _batch_complete(batch_dir: Path, design_hash: str, code_signature: str) -> bool:
    marker = batch_dir / ".complete.json"
    if not marker.exists():
        return False
    try:
        data = json.loads(marker.read_text(encoding="utf-8"))
    except Exception:
        return False
    return (
        data.get("design_hash") == design_hash
        and data.get("code_signature") == code_signature
        and (batch_dir / "grid.csv.gz").exists()
        and (batch_dir / "seed_period_summary.csv").exists()
        and (batch_dir / "seed_excess_period.csv").exists()
        and (batch_dir / "tracking_path_stats.csv").exists()
    )


def _expected_batches(target_seeds: int, batch_size: int) -> list[tuple[int, int]]:
    if target_seeds <= 0:
        raise ValueError("seeds must be positive.")
    if batch_size <= 0:
        raise ValueError("batch-size must be positive.")
    if target_seeds % batch_size != 0:
        raise ValueError(
            "For resumable/extensible final runs, --seeds must be a multiple "
            "of --batch-size."
        )
    return [
        (start, start + batch_size - 1)
        for start in range(0, target_seeds, batch_size)
    ]


def _batch_payloads(
    start_seed: int,
    end_seed: int,
    horizons: tuple[int, ...],
    settings: dict,
) -> list[tuple]:
    payloads = []
    for seed in range(start_seed, end_seed + 1):
        for mechanism in MECHANISMS:
            for path in PATHS:
                for horizon in horizons:
                    payloads.append(
                        (seed, mechanism, path, int(horizon), settings)
                    )
    return payloads


def _run_batch(
    *,
    run_dir: Path,
    start_seed: int,
    end_seed: int,
    horizons: tuple[int, ...],
    settings: dict,
    workers_requested: int,
    design_hash: str,
    code_signature: str,
) -> dict:
    batch_dir = _batch_dir(run_dir, start_seed, end_seed)
    if batch_dir.exists():
        shutil.rmtree(batch_dir)
    batch_dir.mkdir(parents=True, exist_ok=True)

    payloads = _batch_payloads(start_seed, end_seed, horizons, settings)
    workers = _resolve_workers(workers_requested, len(payloads))
    started = time.perf_counter()
    rows: list[dict] = []

    print(
        f"Batch {start_seed}-{end_seed}: {len(payloads)} configurations, "
        f"{workers} workers",
        flush=True,
    )

    if workers == 1:
        iterator = map(_run_payload, payloads)
        for i, result_rows in enumerate(iterator, start=1):
            rows.extend(result_rows)
            if i % max(1, len(payloads) // 10) == 0 or i == len(payloads):
                print(f"  {i}/{len(payloads)} configurations completed", flush=True)
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            iterator = executor.map(_run_payload, payloads, chunksize=1)
            for i, result_rows in enumerate(iterator, start=1):
                rows.extend(result_rows)
                if i % max(1, len(payloads) // 10) == 0 or i == len(payloads):
                    print(
                        f"  {i}/{len(payloads)} configurations completed",
                        flush=True,
                    )

    frame = pd.DataFrame(rows)
    seed_period = _seed_period_summary(frame)
    seed_excess = _seed_excess_period(seed_period)
    tracking = _tracking_path_stats(frame)

    grid_path = batch_dir / "grid.csv.gz"
    _atomic_csv_gzip(frame, grid_path)
    _atomic_csv(seed_period, batch_dir / "seed_period_summary.csv")
    _atomic_csv(seed_excess, batch_dir / "seed_excess_period.csv")
    _atomic_csv(tracking, batch_dir / "tracking_path_stats.csv")

    elapsed = time.perf_counter() - started
    marker = {
        "completed_at_utc": _utc_now(),
        "start_seed": int(start_seed),
        "end_seed": int(end_seed),
        "n_seeds": int(end_seed - start_seed + 1),
        "n_configurations": int(len(payloads)),
        "n_rows": int(len(frame)),
        "workers": int(workers),
        "elapsed_seconds": float(elapsed),
        "design_hash": design_hash,
        "code_signature": code_signature,
        "grid_sha256": _sha256_file(grid_path),
    }
    _atomic_json(batch_dir / ".complete.json", marker)
    return marker


def _weighted_mean(group: pd.DataFrame, value: str, weight: str) -> float:
    weights = group[weight].to_numpy(dtype=float)
    values = group[value].to_numpy(dtype=float)
    return float(np.sum(values * weights) / np.sum(weights))


def _aggregate_direct(seed_period: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    keys = ["mechanism", "path", "horizon", "period"]
    for key, group in seed_period.groupby(keys, dropna=False):
        mechanism, path, horizon, period = key
        total_blocks = int(group["n_blocks"].sum())
        adaptive = _weighted_mean(group, "adaptive_mse", "n_blocks")
        local = _weighted_mean(group, "frozen_local_mse", "n_blocks")
        all_pre = _weighted_mean(group, "frozen_all_pre_mse", "n_blocks")
        benchmark = _weighted_mean(group, "benchmark_mse", "n_blocks")
        rows.append(
            {
                "mechanism": mechanism,
                "path": path,
                "horizon": int(horizon),
                "period": period,
                "n_seeds": int(group["seed"].nunique()),
                "n_blocks": total_blocks,
                "adaptive_mse": adaptive,
                "frozen_local_mse": local,
                "frozen_all_pre_mse": all_pre,
                "benchmark_mse": benchmark,
                "adaptive_rmse_vs_frozen_local": float(np.sqrt(adaptive / local)),
                "adaptive_rmse_vs_frozen_all_pre": float(
                    np.sqrt(adaptive / all_pre)
                ),
                "adaptive_relative_rmsfe_vs_no_change": float(
                    np.sqrt(adaptive / benchmark)
                ),
                "frozen_all_pre_relative_rmsfe_vs_no_change": float(
                    np.sqrt(all_pre / benchmark)
                ),
            }
        )
    return pd.DataFrame(rows)


def _aggregate_excess(seed_excess: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    keys = ["mechanism", "direction", "matched_control", "horizon", "period"]
    for key, group in seed_excess.groupby(keys, dropna=False):
        mechanism, direction, control, horizon, period = key
        rows.append(
            {
                "mechanism": mechanism,
                "direction": direction,
                "matched_control": control,
                "horizon": int(horizon),
                "period": period,
                "n_seeds": int(group["seed"].nunique()),
                "mean_excess_advantage_vs_frozen_local": float(
                    group["excess_advantage_vs_frozen_local"].mean()
                ),
                "mean_excess_advantage_vs_frozen_all_pre": float(
                    group["excess_advantage_vs_frozen_all_pre"].mean()
                ),
                "median_excess_advantage_vs_frozen_all_pre": float(
                    group["excess_advantage_vs_frozen_all_pre"].median()
                ),
                "positive_seed_share_vs_frozen_all_pre": float(
                    (group["excess_advantage_vs_frozen_all_pre"] > 0.0).mean()
                ),
            }
        )
    return pd.DataFrame(rows)


def _combine_tracking(batch_tracking: pd.DataFrame) -> pd.DataFrame:
    metric_columns = [
        "transition_smoothness",
        "start_smoothness",
        "target_smoothness",
        "mean_abs_smoothness_gap_to_target",
        "mean_transition_order",
        "mean_start_order",
        "mean_target_order",
        "mean_transition_window",
        "mean_start_window",
        "mean_target_window",
        "order_match_target_share",
        "window_match_target_share",
        "discrete_config_match_target_share",
        "mean_transition_window_post_fraction",
    ]
    rows: list[dict] = []
    keys = ["mechanism", "direction", "horizon", "relative_origin"]
    for key, group in batch_tracking.groupby(keys, dropna=False):
        row = dict(zip(keys, key))
        row["n_pairs"] = int(group["n_pairs"].sum())
        for column in metric_columns:
            row[column] = _weighted_mean(group, column, "n_pairs")
        row["reference_smoothness_shift"] = (
            row["target_smoothness"] - row["start_smoothness"]
        )
        denom = float(row["reference_smoothness_shift"])
        row["smoothness_progress"] = (
            (row["transition_smoothness"] - row["start_smoothness"]) / denom
            if abs(denom) > 1e-8
            else float("nan")
        )
        rows.append(row)
    return pd.DataFrame(rows)


def _first_sustained_progress(
    path: pd.DataFrame,
    *,
    threshold: float,
    consecutive: int = 3,
) -> float:
    ordered = path.sort_values("relative_origin")
    values = ordered["smoothness_progress"].to_numpy(dtype=float)
    origins = ordered["relative_origin"].to_numpy(dtype=float)
    for i in range(0, len(values) - consecutive + 1):
        block = values[i : i + consecutive]
        if np.all(np.isfinite(block)) and np.all(block >= threshold):
            return float(origins[i])
    return float("nan")


def _tracking_summary(path: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for (mechanism, direction, horizon), group in path.groupby(
        ["mechanism", "direction", "horizon"],
        dropna=False,
    ):
        late = group.loc[group["relative_origin"].ge(72)]
        for threshold in (0.5, 0.8):
            rows.append(
                {
                    "mechanism": mechanism,
                    "direction": direction,
                    "horizon": int(horizon),
                    "threshold": threshold,
                    "adaptation_delay_observations": _first_sustained_progress(
                        group,
                        threshold=threshold,
                    ),
                    "mean_abs_reference_smoothness_shift": float(
                        np.mean(np.abs(group["reference_smoothness_shift"]))
                    ),
                    "late_order_match_target_share": float(
                        late["order_match_target_share"].mean()
                    ),
                    "late_window_match_target_share": float(
                        late["window_match_target_share"].mean()
                    ),
                    "late_discrete_config_match_target_share": float(
                        late["discrete_config_match_target_share"].mean()
                    ),
                }
            )
    return pd.DataFrame(rows)


def _convergence_tables(
    seed_period: pd.DataFrame,
    seed_excess: pd.DataFrame,
    target_seeds: int,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    checkpoints = sorted(
        {
            value
            for value in (*CONVERGENCE_CHECKPOINTS, int(target_seeds))
            if value <= target_seeds
        }
    )
    direct_parts = []
    excess_parts = []

    all_post = seed_period.loc[seed_period["period"].eq("all_post")]
    all_post_excess = seed_excess.loc[seed_excess["period"].eq("all_post")]

    for cutoff in checkpoints:
        direct = _aggregate_direct(all_post.loc[all_post["seed"].lt(cutoff)])
        direct.insert(0, "seed_cutoff", int(cutoff))
        direct_parts.append(direct)

        excess = _aggregate_excess(
            all_post_excess.loc[all_post_excess["seed"].lt(cutoff)]
        )
        excess.insert(0, "seed_cutoff", int(cutoff))
        excess_parts.append(excess)

    return (
        pd.concat(direct_parts, ignore_index=True),
        pd.concat(excess_parts, ignore_index=True),
    )


def _aggregate_run(
    run_dir: Path,
    expected_batches: list[tuple[int, int]],
    design_hash: str,
    code_signature: str,
    target_seeds: int,
) -> None:
    seed_period_parts = []
    seed_excess_parts = []
    tracking_parts = []

    for start_seed, end_seed in expected_batches:
        batch_dir = _batch_dir(run_dir, start_seed, end_seed)
        if not _batch_complete(batch_dir, design_hash, code_signature):
            raise RuntimeError(
                f"Cannot aggregate: incomplete batch {start_seed}-{end_seed}."
            )
        seed_period_parts.append(
            pd.read_csv(batch_dir / "seed_period_summary.csv")
        )
        seed_excess_parts.append(
            pd.read_csv(batch_dir / "seed_excess_period.csv")
        )
        tracking_parts.append(
            pd.read_csv(batch_dir / "tracking_path_stats.csv")
        )

    seed_period = pd.concat(seed_period_parts, ignore_index=True)
    seed_excess = pd.concat(seed_excess_parts, ignore_index=True)
    tracking_batches = pd.concat(tracking_parts, ignore_index=True)

    direct = _aggregate_direct(seed_period)
    excess = _aggregate_excess(seed_excess)
    tracking_path = _combine_tracking(tracking_batches)
    tracking_summary = _tracking_summary(tracking_path)
    convergence_direct, convergence_excess = _convergence_tables(
        seed_period,
        seed_excess,
        target_seeds,
    )

    final_dir = run_dir / "final"
    final_dir.mkdir(parents=True, exist_ok=True)

    _atomic_csv(direct, final_dir / "summary.csv")
    _atomic_csv(excess, final_dir / "paired_excess_summary.csv")
    _atomic_csv(
        seed_period.loc[seed_period["period"].eq("all_post")],
        final_dir / "seed_summary_all_post.csv",
    )
    _atomic_csv(
        seed_excess.loc[seed_excess["period"].eq("all_post")],
        final_dir / "seed_excess_all_post.csv",
    )
    _atomic_csv(tracking_path, final_dir / "target_tracking_path.csv")
    _atomic_csv(tracking_summary, final_dir / "target_tracking_summary.csv")
    _atomic_csv(
        convergence_direct,
        final_dir / "monte_carlo_convergence_direct.csv",
    )
    _atomic_csv(
        convergence_excess,
        final_dir / "monte_carlo_convergence_excess.csv",
    )
    _atomic_json(
        final_dir / "aggregate_metadata.json",
        {
            "created_at_utc": _utc_now(),
            "target_seeds": int(target_seeds),
            "n_batches": int(len(expected_batches)),
            "design_hash": design_hash,
            "code_signature": code_signature,
            "git_commit": git_short_sha(),
        },
    )


def _write_progress(
    run_dir: Path,
    expected_batches: list[tuple[int, int]],
    design_hash: str,
    code_signature: str,
) -> None:
    completed = []
    for start_seed, end_seed in expected_batches:
        batch_dir = _batch_dir(run_dir, start_seed, end_seed)
        if _batch_complete(batch_dir, design_hash, code_signature):
            marker = json.loads(
                (batch_dir / ".complete.json").read_text(encoding="utf-8")
            )
            completed.append(marker)

    _atomic_json(
        run_dir / "progress.json",
        {
            "updated_at_utc": _utc_now(),
            "expected_batches": len(expected_batches),
            "completed_batches": len(completed),
            "completed_seeds": int(sum(x["n_seeds"] for x in completed)),
            "completed_ranges": [
                [int(x["start_seed"]), int(x["end_seed"])] for x in completed
            ],
        },
    )


def main() -> None:
    args = parse_args()

    if args.preset == "smoke":
        target_seeds = 1 if args.seeds is None else int(args.seeds)
        batch_size = 1 if args.batch_size is None else int(args.batch_size)
        horizons = SMOKE_HORIZONS
        n_grid = 81 if args.n_grid is None else int(args.n_grid)
        default_run_id = "paper_mc_smoke"
    else:
        target_seeds = 1000 if args.seeds is None else int(args.seeds)
        batch_size = 10 if args.batch_size is None else int(args.batch_size)
        horizons = FINAL_HORIZONS
        n_grid = 321 if args.n_grid is None else int(args.n_grid)
        default_run_id = "paper_mc_v1"

    run_id = args.run_id or default_run_id
    settings = {
        "n_obs": int(args.n_obs),
        "regime_point": int(args.regime_point),
        "outer_initial_train": int(args.outer_initial_train),
        "outer_step": int(args.outer_step),
        "inner_step": int(args.inner_step),
        "selector_max_inner_origins": int(args.selector_max_inner_origins),
        "orders": [int(x) for x in args.orders],
        "windows": [int(x) for x in args.windows],
        "n_grid": int(n_grid),
        "log_lambda_bounds": [
            float(args.log_lambda_min),
            float(args.log_lambda_max),
        ],
    }

    if not settings["outer_initial_train"] < settings["regime_point"] < settings["n_obs"]:
        raise ValueError(
            "Require outer_initial_train < regime_point < n_obs."
        )
    if settings["selector_max_inner_origins"] <= 1:
        raise ValueError("selector-max-inner-origins must exceed 1.")

    expected_batches = _expected_batches(target_seeds, batch_size)
    design = {
        "experiment": "final_paper_scale_monte_carlo",
        "preset": args.preset,
        "mechanisms": list(MECHANISMS),
        "paths": list(PATHS),
        "horizons": list(horizons),
        "settings": settings,
        "mechanism_parameters": {
            mechanism: {
                path: _mechanism_parameters(mechanism, path)
                for path in PATHS
            }
            for mechanism in MECHANISMS
        },
        "storage_batch_size": int(batch_size),
        "primary_fixed_comparator": "frozen_all_pre",
        "secondary_fixed_comparator": "frozen_local_M20",
        "adaptive_method": "adaptive_M20",
        "external_benchmark": "no_change",
    }
    design_hash = _hash_json(design)
    code_signature = _code_signature()

    run_dir = (
        Path("results")
        / "forecast_optimal_smoothing"
        / run_id
    )
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = run_dir / "manifest.json"

    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("design_hash") != design_hash:
            raise RuntimeError(
                "Existing run-id has a different scientific/storage design. "
                "Use the original batch size/settings or choose a new --run-id."
            )
        if manifest.get("code_signature") != code_signature:
            raise RuntimeError(
                "Relevant trend-estimation code changed since this run began. "
                "To avoid mixing implementations, use a new --run-id."
            )
    else:
        _atomic_json(
            manifest_path,
            {
                "created_at_utc": _utc_now(),
                "created_git_commit": git_short_sha(),
                "run_id": run_id,
                "design": design,
                "design_hash": design_hash,
                "code_signature": code_signature,
            },
        )

    _write_progress(
        run_dir,
        expected_batches,
        design_hash,
        code_signature,
    )

    if not args.aggregate_only:
        for index, (start_seed, end_seed) in enumerate(expected_batches, start=1):
            batch_dir = _batch_dir(run_dir, start_seed, end_seed)
            if _batch_complete(batch_dir, design_hash, code_signature):
                print(
                    f"[{index}/{len(expected_batches)}] "
                    f"seed batch {start_seed}-{end_seed}: already complete",
                    flush=True,
                )
                continue

            marker = _run_batch(
                run_dir=run_dir,
                start_seed=start_seed,
                end_seed=end_seed,
                horizons=horizons,
                settings=settings,
                workers_requested=int(args.workers),
                design_hash=design_hash,
                code_signature=code_signature,
            )
            print(
                f"[{index}/{len(expected_batches)}] persisted seeds "
                f"{start_seed}-{end_seed}; rows={marker['n_rows']}",
                flush=True,
            )
            _write_progress(
                run_dir,
                expected_batches,
                design_hash,
                code_signature,
            )

    incomplete = [
        (start_seed, end_seed)
        for start_seed, end_seed in expected_batches
        if not _batch_complete(
            _batch_dir(run_dir, start_seed, end_seed),
            design_hash,
            code_signature,
        )
    ]
    if incomplete:
        print(
            f"Run remains resumable: {len(incomplete)} batches incomplete. "
            "Re-run the same command to continue.",
            flush=True,
        )
        return

    print("All requested batches complete; building cumulative summaries.", flush=True)
    _aggregate_run(
        run_dir,
        expected_batches,
        design_hash,
        code_signature,
        target_seeds,
    )
    _write_progress(
        run_dir,
        expected_batches,
        design_hash,
        code_signature,
    )
    print(f"Final outputs written to {run_dir / 'final'}", flush=True)


if __name__ == "__main__":
    main()
