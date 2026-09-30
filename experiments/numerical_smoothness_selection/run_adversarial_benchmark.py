from __future__ import annotations

import argparse
import json
import math
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import trend_estimation as td
from trend_estimation.benchmarks.adversarial import (
    AdversarialSmoothnessCase,
    adversarial_smoothness_cases,
)


PRESETS = {
    "smoke": {
        "case_names": (
            "near_zero",
            "near_one",
            "close_pair",
            "flat_minimum",
            "boundary_zero",
            "boundary_one",
        ),
        "n_obs_values": (63,),
        "orders": (2,),
        "dense_grid_size": 1001,
        "log_grid_size": 257,
    },
    "quick": {
        "case_names": None,
        "n_obs_values": (63, 252),
        "orders": (1, 2, 3, 4),
        "dense_grid_size": 5001,
        "log_grid_size": 257,
    },
    "paper": {
        "case_names": None,
        "n_obs_values": (63, 126, 252, 504),
        "orders": (1, 2, 3, 4),
        "dense_grid_size": 20001,
        "log_grid_size": 257,
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare adaptive-S, log-lambda, and dense-grid searches on "
            "analytic adversarial smoothness objectives with known truth."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument("--dense-grid-size", type=int, default=None)
    parser.add_argument("--log-grid-size", type=int, default=None)
    parser.add_argument("--initial-grid-size", type=int, default=9)
    parser.add_argument("--max-depth", type=int, default=8)
    parser.add_argument("--min-interval", type=float, default=1e-3)
    parser.add_argument("--endpoint-refinement-levels", type=int, default=6)
    parser.add_argument("--boundary-margin", type=float, default=1e-6)
    parser.add_argument(
        "--log-s-lower",
        type=float,
        default=1e-6,
        help="Lower S used to construct finite log-lambda bounds.",
    )
    parser.add_argument(
        "--log-s-upper",
        type=float,
        default=0.9999,
        help="Upper S used to construct finite log-lambda bounds.",
    )
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser.parse_args()


def _git_short_sha() -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def _default_run_directory(preset: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return (
        Path("results")
        / "numerical_smoothness_selection"
        / f"{stamp}_adversarial-{preset}_{_git_short_sha()}"
    )


def _truth_global(case: AdversarialSmoothnessCase) -> tuple[float, tuple[float, ...]]:
    candidates = (
        tuple(case.true_minima)
        + tuple(case.true_flat_minima)
        + tuple(case.true_boundary_minima)
        + (0.0, 1.0)
    )
    values = np.asarray([case.value(s) for s in candidates], dtype=float)
    best_value = float(np.min(values))
    tolerance = 1e-10 * max(1.0, abs(best_value)) + 1e-12
    best_s = tuple(
        float(s)
        for s, value in zip(candidates, values)
        if abs(float(value) - best_value) <= tolerance
    )
    return best_value, tuple(sorted(set(best_s)))


def _distance_to_set(value: float, truth: tuple[float, ...]) -> float:
    if not truth:
        return float("nan")
    return float(min(abs(float(value) - target) for target in truth))


def _dedupe(values: list[float], tolerance: float = 1e-8) -> tuple[float, ...]:
    result: list[float] = []
    for value in sorted(float(x) for x in values):
        if not result or abs(value - result[-1]) > tolerance:
            result.append(value)
    return tuple(result)


def _adaptive_method(
    case: AdversarialSmoothnessCase,
    *,
    n_obs: int,
    order: int,
    args: argparse.Namespace,
) -> dict:
    callback = case.lambda_callback(n_obs=n_obs, order=order)
    start = time.perf_counter()
    result = td.find_stationary_points_smoothness(
        callback,
        n_obs=n_obs,
        order=order,
        initial_grid_size=args.initial_grid_size,
        max_depth=args.max_depth,
        min_interval=args.min_interval,
        endpoint_refinement_levels=args.endpoint_refinement_levels,
        boundary_margin=args.boundary_margin,
    )
    seconds = time.perf_counter() - start

    candidate_points = [
        point
        for point in result.points_
        if point.kind_ in {"minimum", "flat"}
    ]
    candidates = [
        (point.objective_, point.smoothness_, "stationary_" + point.kind_)
        for point in candidate_points
    ]
    candidates.extend(
        [
            (case.value(0.0), 0.0, "S=0"),
            (case.value(1.0), 1.0, "S=1"),
        ]
    )
    best_value, best_s, best_source = min(
        candidates,
        key=lambda row: (row[0], row[1]),
    )
    detected = tuple(point.smoothness_ for point in result.points_)
    return {
        "method": "adaptive_s",
        "best_s": float(best_s),
        "best_value": float(best_value),
        "best_source": best_source,
        "n_stationary_detected": len(result.points_),
        "n_minima_detected": sum(
            point.kind_ in {"minimum", "flat"} for point in result.points_
        ),
        "n_evaluations": int(result.n_evaluations_ + 2),
        "seconds": float(seconds),
        "detected_points": detected,
    }


def _log_lambda_method(
    case: AdversarialSmoothnessCase,
    *,
    n_obs: int,
    order: int,
    args: argparse.Namespace,
    log_grid_size: int,
) -> dict:
    raw_callback = case.lambda_callback(n_obs=n_obs, order=order)
    cache: dict[float, tuple[float, float, float]] = {}

    def callback(lambda_: float) -> tuple[float, float, float]:
        key = float(lambda_)
        if key not in cache:
            cache[key] = raw_callback(key)
        return cache[key]

    lambda_lo = td.smoothness_to_lambda(args.log_s_lower, n_obs, order)
    lambda_hi = td.smoothness_to_lambda(args.log_s_upper, n_obs, order)
    if not (0.0 < lambda_lo < lambda_hi < float("inf")):
        raise FloatingPointError("Invalid finite lambda bounds for log search.")
    log_bounds = (math.log(lambda_lo), math.log(lambda_hi))

    start = time.perf_counter()
    result = td.find_stationary_points_log_lambda(
        callback,
        log_bounds=log_bounds,
        n_grid=log_grid_size,
    )
    seconds = time.perf_counter() - start

    points = [
        (
            point.objective_,
            td.lambda_to_smoothness(point.lambda_, n_obs, order),
            "stationary_" + point.kind_,
        )
        for point in result.points_
        if point.kind_ in {"minimum", "flat"}
    ]
    points.extend(
        [
            (case.value(0.0), 0.0, "S=0"),
            (case.value(1.0), 1.0, "S=1"),
        ]
    )
    best_value, best_s, best_source = min(
        points,
        key=lambda row: (row[0], row[1]),
    )
    detected = tuple(
        td.lambda_to_smoothness(point.lambda_, n_obs, order)
        for point in result.points_
    )
    return {
        "method": "log_lambda",
        "best_s": float(best_s),
        "best_value": float(best_value),
        "best_source": best_source,
        "n_stationary_detected": len(result.points_),
        "n_minima_detected": sum(
            point.kind_ in {"minimum", "flat"} for point in result.points_
        ),
        "n_evaluations": int(len(cache) + 2),
        "seconds": float(seconds),
        "detected_points": detected,
        "log_lower": float(log_bounds[0]),
        "log_upper": float(log_bounds[1]),
    }


def _dense_method(
    case: AdversarialSmoothnessCase,
    *,
    dense_grid_size: int,
) -> dict:
    start = time.perf_counter()
    grid = np.linspace(0.0, 1.0, dense_grid_size)
    values = np.asarray([case.value(value) for value in grid], dtype=float)
    best_index = int(np.argmin(values))

    local_minima: list[float] = []
    for index in range(1, dense_grid_size - 1):
        if values[index] <= values[index - 1] and values[index] <= values[index + 1]:
            local_minima.append(float(grid[index]))
    if values[0] <= values[1]:
        local_minima.append(0.0)
    if values[-1] <= values[-2]:
        local_minima.append(1.0)

    seconds = time.perf_counter() - start
    return {
        "method": "dense",
        "best_s": float(grid[best_index]),
        "best_value": float(values[best_index]),
        "best_source": "grid",
        "n_stationary_detected": len(local_minima),
        "n_minima_detected": len(local_minima),
        "n_evaluations": int(dense_grid_size),
        "seconds": float(seconds),
        "detected_points": _dedupe(local_minima),
    }


def _detection_rows(
    case: AdversarialSmoothnessCase,
    result: dict,
    *,
    n_obs: int,
    order: int,
    dense_grid_size: int,
) -> list[dict]:
    method = result["method"]
    detected = tuple(float(x) for x in result["detected_points"])
    dense_step = 1.0 / max(1, dense_grid_size - 1)
    tolerance = (
        max(2.0 * dense_step, 1e-6)
        if method == "dense"
        else max(2.0 * dense_step, 5e-5)
    )

    rows: list[dict] = []
    for truth_s, truth_kind in case.truth_points():
        if truth_kind == "boundary_minimum":
            found = abs(result["best_s"] - truth_s) <= tolerance or any(
                abs(point - truth_s) <= tolerance for point in detected
            )
            error = 0.0 if found else _distance_to_set(truth_s, detected)
        else:
            errors = [abs(point - truth_s) for point in detected]
            error = min(errors) if errors else float("nan")
            found = bool(errors) and error <= tolerance
        rows.append(
            {
                "case": case.name,
                "n_obs": n_obs,
                "order": order,
                "method": method,
                "truth_s": float(truth_s),
                "truth_kind": truth_kind,
                "detected": bool(found),
                "abs_error": float(error),
                "tolerance": float(tolerance),
            }
        )
    return rows


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    dense_grid_size = int(
        args.dense_grid_size
        if args.dense_grid_size is not None
        else preset["dense_grid_size"]
    )
    log_grid_size = int(
        args.log_grid_size
        if args.log_grid_size is not None
        else preset["log_grid_size"]
    )
    if dense_grid_size < 3 or log_grid_size < 3:
        raise ValueError("Grid sizes must be at least 3.")
    if not 0.0 < args.log_s_lower < args.log_s_upper < 1.0:
        raise ValueError("log-s bounds must satisfy 0 < lower < upper < 1.")

    available = {case.name: case for case in adversarial_smoothness_cases()}
    names = preset["case_names"]
    cases = tuple(available[name] for name in names) if names else tuple(available.values())
    n_obs_values = tuple(int(value) for value in preset["n_obs_values"])
    orders = tuple(int(value) for value in preset["orders"])

    run_dir = args.output_dir or _default_run_directory(args.preset)
    run_dir.mkdir(parents=True, exist_ok=True)

    summaries: list[dict] = []
    detections: list[dict] = []
    manifests: list[dict] = []
    run_start = time.perf_counter()

    total = len(cases) * len(n_obs_values) * len(orders)
    index = 0
    for case in cases:
        truth_best_value, truth_best_s = _truth_global(case)
        manifests.append(
            {
                "case": case.name,
                "description": case.description,
                "true_minima": ";".join(map(str, case.true_minima)),
                "true_flat_minima": ";".join(map(str, case.true_flat_minima)),
                "true_boundary_minima": ";".join(map(str, case.true_boundary_minima)),
                "true_other_stationary": ";".join(map(str, case.true_other_stationary)),
                "true_global_value": truth_best_value,
                "true_global_s": ";".join(map(str, truth_best_s)),
            }
        )

        for n_obs in n_obs_values:
            for order in orders:
                if order >= n_obs:
                    continue
                index += 1
                print(
                    f"[{index}/{total}] case={case.name} n={n_obs} d={order}",
                    flush=True,
                )
                method_results = (
                    _adaptive_method(
                        case,
                        n_obs=n_obs,
                        order=order,
                        args=args,
                    ),
                    _log_lambda_method(
                        case,
                        n_obs=n_obs,
                        order=order,
                        args=args,
                        log_grid_size=log_grid_size,
                    ),
                    _dense_method(
                        case,
                        dense_grid_size=dense_grid_size,
                    ),
                )

                for result in method_results:
                    row = {
                        "case": case.name,
                        "n_obs": n_obs,
                        "order": order,
                        "method": result["method"],
                        "best_s": result["best_s"],
                        "best_value": result["best_value"],
                        "best_source": result["best_source"],
                        "true_best_value": truth_best_value,
                        "best_s_distance_to_true": _distance_to_set(
                            result["best_s"],
                            truth_best_s,
                        ),
                        "objective_regret": result["best_value"] - truth_best_value,
                        "n_stationary_detected": result["n_stationary_detected"],
                        "n_minima_detected": result["n_minima_detected"],
                        "n_evaluations": result["n_evaluations"],
                        "seconds": result["seconds"],
                    }
                    if "log_lower" in result:
                        row["log_lower"] = result["log_lower"]
                        row["log_upper"] = result["log_upper"]
                    summaries.append(row)
                    detections.extend(
                        _detection_rows(
                            case,
                            result,
                            n_obs=n_obs,
                            order=order,
                            dense_grid_size=dense_grid_size,
                        )
                    )

                print(
                    "    "
                    + " | ".join(
                        f"{result['method']}: S*={result['best_s']:.6f}, "
                        f"eval={result['n_evaluations']}"
                        for result in method_results
                    ),
                    flush=True,
                )

    elapsed = time.perf_counter() - run_start
    pd.DataFrame(summaries).to_csv(run_dir / "method_summary.csv", index=False)
    pd.DataFrame(detections).to_csv(run_dir / "stationary_detection.csv", index=False)
    pd.DataFrame(manifests).to_csv(run_dir / "case_manifest.csv", index=False)

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "suite": "adversarial_smoothness",
        "preset": args.preset,
        "endpoint_policy": "exact",
        "case_names": [case.name for case in cases],
        "n_obs_values": list(n_obs_values),
        "orders": list(orders),
        "dense_grid_size": dense_grid_size,
        "log_grid_size": log_grid_size,
        "adaptive_initial_grid_size": args.initial_grid_size,
        "adaptive_max_depth": args.max_depth,
        "adaptive_min_interval": args.min_interval,
        "adaptive_endpoint_refinement_levels": args.endpoint_refinement_levels,
        "adaptive_boundary_margin": args.boundary_margin,
        "log_s_lower": args.log_s_lower,
        "log_s_upper": args.log_s_upper,
        "elapsed_seconds": elapsed,
        "n_configurations": index,
        "n_method_rows": len(summaries),
    }
    (run_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote adversarial benchmark to {run_dir} in {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
