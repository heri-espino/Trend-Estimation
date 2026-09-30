from __future__ import annotations

import argparse
import itertools
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import trend_estimation as td


SCENARIOS = {
    "baseline": {
        "slope_noise_std": 0.01,
        "observation_noise_std": 0.5,
        "ar1_phi": 0.3,
    },
    "persistent": {
        "slope_noise_std": 0.01,
        "observation_noise_std": 0.5,
        "ar1_phi": 0.8,
    },
    "rough": {
        "slope_noise_std": 0.03,
        "observation_noise_std": 0.5,
        "ar1_phi": 0.3,
    },
    "noisy": {
        "slope_noise_std": 0.01,
        "observation_noise_std": 1.0,
        "ar1_phi": 0.3,
    },
}

PRESETS = {
    "smoke": {
        "seeds": (0,),
        "orders": (1, 2),
        "windows": (63, 126),
        "horizons": (1, 5),
        "scenarios": ("baseline",),
        "dense_grid_size": 401,
    },
    "quick": {
        "seeds": tuple(range(3)),
        "orders": (1, 2, 3, 4),
        "windows": (63, 126, 252),
        "horizons": (1, 5, 20),
        "scenarios": ("baseline", "persistent"),
        "dense_grid_size": 2001,
    },
    "paper": {
        "seeds": tuple(range(10)),
        "orders": (1, 2, 3, 4),
        "windows": (63, 126, 252, 504),
        "horizons": (1, 5, 20, 60),
        "scenarios": ("baseline", "persistent", "rough"),
        "dense_grid_size": 5001,
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Benchmark adaptive smoothness stationary-point search on synthetic "
            "forecast-validation surfaces against an exact-endpoint dense reference."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument("--n-obs", type=int, default=800)
    parser.add_argument("--orders", type=int, nargs="+", default=None)
    parser.add_argument("--windows", type=int, nargs="+", default=None)
    parser.add_argument("--horizons", type=int, nargs="+", default=None)
    parser.add_argument(
        "--scenarios",
        nargs="+",
        choices=tuple(SCENARIOS),
        default=None,
    )
    parser.add_argument("--step", type=int, default=5)
    parser.add_argument("--max-origins", type=int, default=30)
    parser.add_argument("--initial-grid-size", type=int, default=9)
    parser.add_argument("--max-depth", type=int, default=8)
    parser.add_argument("--min-interval", type=float, default=1e-3)
    parser.add_argument("--endpoint-refinement-levels", type=int, default=6)
    parser.add_argument("--max-candidates", type=int, default=5)
    parser.add_argument(
        "--epsilons",
        type=float,
        nargs="+",
        default=list(td.DEFAULT_SPACING_EPSILONS),
    )
    parser.add_argument("--dense-grid-size", type=int, default=None)
    parser.add_argument(
        "--max-cases",
        type=int,
        default=None,
        help="Optional deterministic prefix of cases, useful for smoke/debug runs.",
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
        / f"{stamp}_synthetic-{preset}_{_git_short_sha()}"
    )


def _resolve_axis(
    args: argparse.Namespace,
    preset: dict,
    name: str,
) -> tuple:
    override = getattr(args, name)
    values = preset[name] if override is None else override
    return tuple(values)


def _dense_reference(
    prepared,
    *,
    window: int,
    order: int,
    n_grid: int,
) -> tuple[np.ndarray, np.ndarray, list[tuple[float, float]], list[tuple[float, float]]]:
    smoothness_grid = np.linspace(0.0, 1.0, int(n_grid))
    values = np.empty_like(smoothness_grid)

    for i, smoothness in enumerate(smoothness_grid):
        lambda_ = td.smoothness_to_lambda(
            float(smoothness),
            n_obs=window,
            order=order,
        )
        values[i] = prepared.evaluate(lambda_).value

    interior_minima: list[tuple[float, float]] = []
    for i in range(1, len(smoothness_grid) - 1):
        if values[i] <= values[i - 1] and values[i] <= values[i + 1]:
            interior_minima.append(
                (float(smoothness_grid[i]), float(values[i]))
            )

    boundary_minima: list[tuple[float, float]] = []
    if values[0] <= values[1]:
        boundary_minima.append((0.0, float(values[0])))
    if values[-1] <= values[-2]:
        boundary_minima.append((1.0, float(values[-1])))

    return smoothness_grid, values, interior_minima, boundary_minima


def _match_dense_minima(
    dense_minima: list[tuple[float, float]],
    adaptive_minima,
    *,
    grid_step: float,
) -> tuple[int, int]:
    tolerance = max(2.0 * float(grid_step), 1e-6)
    adaptive_s = [point.smoothness_ for point in adaptive_minima]
    matched = sum(
        any(abs(dense_s - adaptive_s_i) <= tolerance for adaptive_s_i in adaptive_s)
        for dense_s, _ in dense_minima
    )
    return int(matched), int(len(dense_minima) - matched)


def run_case(
    *,
    seed: int,
    scenario_name: str,
    order: int,
    window: int,
    horizon: int,
    args: argparse.Namespace,
    dense_grid_size: int,
) -> tuple[dict, list[dict]]:
    scenario = SCENARIOS[scenario_name]
    data = td.make_local_linear_ar1_series(
        n_obs=args.n_obs,
        slope_noise_std=scenario["slope_noise_std"],
        observation_noise_std=scenario["observation_noise_std"],
        ar1_phi=scenario["ar1_phi"],
        random_state=seed,
    )

    splits = td.rolling_origin_splits(
        args.n_obs,
        initial_train=window,
        horizon=horizon,
        step=args.step,
        expanding=False,
        train_window=window,
    )
    splits = splits[-args.max_origins :]
    if not splits:
        raise ValueError(
            f"No rolling origins for window={window}, horizon={horizon}, "
            f"n_obs={args.n_obs}."
        )

    prepared = td.prepare_rolling_pure_forecast_objective(
        data.y,
        splits,
        order=order,
    )

    adaptive_cache: dict[float, object] = {}

    def evaluate_lambda(lambda_: float):
        key = float(lambda_)
        if key not in adaptive_cache:
            adaptive_cache[key] = prepared.evaluate(key)
        return adaptive_cache[key]

    def value_grad_hess(lambda_: float):
        evaluated = evaluate_lambda(lambda_)
        return evaluated.value, evaluated.first, evaluated.second

    adaptive_start = time.perf_counter()
    search = td.find_stationary_points_smoothness(
        value_grad_hess,
        n_obs=window,
        order=order,
        initial_grid_size=args.initial_grid_size,
        max_depth=args.max_depth,
        min_interval=args.min_interval,
        endpoint_refinement_levels=args.endpoint_refinement_levels,
    )
    adaptive_minima = tuple(
        point for point in search.points_ if point.kind_ == "minimum"
    )

    endpoint_zero = evaluate_lambda(0.0)
    endpoint_one = evaluate_lambda(float("inf"))
    adaptive_candidates = [
        (
            "interior",
            point.smoothness_,
            point.lambda_,
            point.objective_,
        )
        for point in adaptive_minima
    ]
    adaptive_candidates.extend(
        [
            ("S=0", 0.0, 0.0, endpoint_zero.value),
            ("S=1", 1.0, float("inf"), endpoint_one.value),
        ]
    )
    adaptive_best_source, adaptive_best_s, adaptive_best_lambda, adaptive_best_value = min(
        adaptive_candidates,
        key=lambda row: (row[3], row[1]),
    )
    adaptive_seconds = time.perf_counter() - adaptive_start

    dense_start = time.perf_counter()
    dense_s, dense_values, dense_interior_minima, dense_boundary_minima = (
        _dense_reference(
            prepared,
            window=window,
            order=order,
            n_grid=dense_grid_size,
        )
    )
    dense_seconds = time.perf_counter() - dense_start

    dense_best_index = int(np.argmin(dense_values))
    dense_best_s = float(dense_s[dense_best_index])
    dense_best_value = float(dense_values[dense_best_index])
    grid_step = float(dense_s[1] - dense_s[0])
    matched, missed = _match_dense_minima(
        dense_interior_minima,
        adaptive_minima,
        grid_step=grid_step,
    )

    summary = {
        "seed": seed,
        "scenario": scenario_name,
        "slope_noise_std": scenario["slope_noise_std"],
        "observation_noise_std": scenario["observation_noise_std"],
        "ar1_phi": scenario["ar1_phi"],
        "horizon": horizon,
        "order": order,
        "window": window,
        "n_origins": len(splits),
        "n_adaptive_stationary_points": len(search.points_),
        "n_adaptive_local_minima": len(adaptive_minima),
        "n_dense_interior_minima": len(dense_interior_minima),
        "n_dense_boundary_minima": len(dense_boundary_minima),
        "n_dense_interior_minima_matched": matched,
        "n_dense_interior_minima_missed": missed,
        "adaptive_evaluations": len(adaptive_cache),
        "dense_evaluations": int(dense_grid_size),
        "adaptive_seconds": adaptive_seconds,
        "dense_seconds": dense_seconds,
        "dense_best_s": dense_best_s,
        "dense_best_cv": dense_best_value,
        "adaptive_best_s": float(adaptive_best_s),
        "adaptive_best_lambda": float(adaptive_best_lambda),
        "adaptive_best_cv": float(adaptive_best_value),
        "adaptive_best_source": adaptive_best_source,
        "best_s_abs_error": abs(float(adaptive_best_s) - dense_best_s),
        "objective_regret": float(adaptive_best_value) - dense_best_value,
    }

    candidate_rows: list[dict] = []
    for candidate_set in td.sweep_spaced_smoothness_minima(
        search.points_,
        epsilons=args.epsilons,
        max_candidates=args.max_candidates,
    ):
        for rank, point in enumerate(candidate_set.candidates_, start=1):
            candidate_rows.append(
                {
                    "seed": seed,
                    "scenario": scenario_name,
                    "order": order,
                    "window": window,
                    "horizon": horizon,
                    "epsilon": candidate_set.epsilon_,
                    "rank": rank,
                    "smoothness": point.smoothness_,
                    "lambda": point.lambda_,
                    "cv": point.objective_,
                    "curvature_smoothness": point.curvature_smoothness_,
                    "n_available_minima": candidate_set.n_available_minima_,
                    "n_removed": candidate_set.n_removed_,
                }
            )

    return summary, candidate_rows


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]

    seeds = tuple(int(x) for x in preset["seeds"])
    orders = tuple(int(x) for x in _resolve_axis(args, preset, "orders"))
    windows = tuple(int(x) for x in _resolve_axis(args, preset, "windows"))
    horizons = tuple(int(x) for x in _resolve_axis(args, preset, "horizons"))
    scenarios = tuple(str(x) for x in _resolve_axis(args, preset, "scenarios"))

    dense_grid_size = (
        int(args.dense_grid_size)
        if args.dense_grid_size is not None
        else int(preset["dense_grid_size"])
    )

    if args.n_obs <= 0:
        raise ValueError("n-obs must be positive.")
    if args.max_origins <= 0:
        raise ValueError("max-origins must be positive.")
    if args.step <= 0:
        raise ValueError("step must be positive.")
    if args.max_candidates <= 0:
        raise ValueError("max-candidates must be positive.")
    if dense_grid_size < 3:
        raise ValueError("dense-grid-size must be at least 3.")
    if any(order < 1 for order in orders):
        raise ValueError("orders must be positive.")
    if any(window <= 0 for window in windows):
        raise ValueError("windows must be positive.")
    if any(horizon <= 0 for horizon in horizons):
        raise ValueError("horizons must be positive.")
    if max(windows) >= args.n_obs:
        raise ValueError("Every window must be smaller than n-obs.")

    cases = list(
        itertools.product(
            seeds,
            scenarios,
            orders,
            windows,
            horizons,
        )
    )
    if args.max_cases is not None:
        if args.max_cases <= 0:
            raise ValueError("max-cases must be positive when provided.")
        cases = cases[: int(args.max_cases)]

    run_dir = args.output_dir or _default_run_directory(args.preset)
    run_dir.mkdir(parents=True, exist_ok=True)

    summaries: list[dict] = []
    candidates: list[dict] = []
    start = time.perf_counter()

    for i, (seed, scenario, order, window, horizon) in enumerate(cases, start=1):
        print(
            f"[{i}/{len(cases)}] scenario={scenario} seed={seed} "
            f"d={order} L={window} h={horizon}",
            flush=True,
        )
        summary, rows = run_case(
            seed=int(seed),
            scenario_name=str(scenario),
            order=int(order),
            window=int(window),
            horizon=int(horizon),
            args=args,
            dense_grid_size=dense_grid_size,
        )
        summaries.append(summary)
        candidates.extend(rows)
        print(
            "    "
            f"best={summary['adaptive_best_source']} "
            f"S*={summary['adaptive_best_s']:.6f} "
            f"dense={summary['dense_best_s']:.6f} "
            f"|dS|={summary['best_s_abs_error']:.3g} "
            f"missed={summary['n_dense_interior_minima_missed']} "
            f"eval={summary['adaptive_evaluations']}/{summary['dense_evaluations']}",
            flush=True,
        )

    elapsed = time.perf_counter() - start
    pd.DataFrame(summaries).to_csv(run_dir / "search_summary.csv", index=False)

    candidate_columns = [
        "seed",
        "scenario",
        "order",
        "window",
        "horizon",
        "epsilon",
        "rank",
        "smoothness",
        "lambda",
        "cv",
        "curvature_smoothness",
        "n_available_minima",
        "n_removed",
    ]
    pd.DataFrame(candidates, columns=candidate_columns).to_csv(
        run_dir / "candidate_sweep.csv",
        index=False,
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "preset": args.preset,
        "endpoint_policy": "exact",
        "n_obs": args.n_obs,
        "seeds": list(seeds),
        "orders": list(orders),
        "windows": list(windows),
        "horizons": list(horizons),
        "scenarios": list(scenarios),
        "scenario_parameters": {
            name: SCENARIOS[name] for name in scenarios
        },
        "step": args.step,
        "max_origins": args.max_origins,
        "initial_grid_size": args.initial_grid_size,
        "max_depth": args.max_depth,
        "min_interval": args.min_interval,
        "endpoint_refinement_levels": args.endpoint_refinement_levels,
        "max_candidates": args.max_candidates,
        "epsilons": list(args.epsilons),
        "dense_grid_size": dense_grid_size,
        "max_cases": args.max_cases,
        "elapsed_seconds": elapsed,
        "n_cases": len(cases),
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(f"Wrote benchmark to {run_dir} in {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
