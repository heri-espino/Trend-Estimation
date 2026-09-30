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
}

PRIMARY_SPEC = {
    "initial_grid_size": 9,
    "max_depth": 8,
    "min_interval": 1e-3,
    "endpoint_refinement_levels": 6,
    "derivative_tol": 1e-8,
    "curvature_tol": 1e-8,
    "near_zero_ratio": 0.2,
    "root_xtol": 1e-10,
    "boundary_margin": 1e-6,
}

SENSITIVITY_VALUES = {
    "initial_grid_size": (5, 7, 13),
    "max_depth": (4, 6, 10),
    "endpoint_refinement_levels": (0, 2, 4, 8),
    "min_interval": (5e-4, 2e-3, 5e-3),
    "near_zero_ratio": (0.1, 0.5),
}

PRESETS = {
    "smoke": {
        "seeds": (0,),
        "orders": (2, 4),
        "windows": (126,),
        "horizons": (5, 20),
        "scenarios": ("baseline",),
        "dense_grid_size": 1001,
        "max_cases": 2,
    },
    "quick": {
        "seeds": (0, 1, 2),
        "orders": (1, 2, 3, 4),
        "windows": (63, 126, 252),
        "horizons": (1, 5, 20),
        "scenarios": ("baseline", "persistent"),
        "dense_grid_size": 2001,
        "max_cases": 48,
    },
    "paper": {
        "seeds": (0, 1, 2),
        "orders": (1, 2, 3, 4),
        "windows": (63, 126, 252),
        "horizons": (1, 5, 20),
        "scenarios": ("baseline", "persistent"),
        "dense_grid_size": 5001,
        "max_cases": None,
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "One-factor-at-a-time sensitivity analysis for the frozen "
            "adaptive smoothness-search specification."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument("--n-obs", type=int, default=800)
    parser.add_argument("--max-origins", type=int, default=30)
    parser.add_argument("--step", type=int, default=5)
    parser.add_argument("--dense-grid-size", type=int, default=None)
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
        / f"{stamp}_sensitivity-{preset}_{_git_short_sha()}"
    )


def _specifications() -> list[tuple[str, str, bool, dict]]:
    rows: list[tuple[str, str, bool, dict]] = [
        ("primary", "frozen", True, dict(PRIMARY_SPEC))
    ]
    for parameter, values in SENSITIVITY_VALUES.items():
        for value in values:
            spec = dict(PRIMARY_SPEC)
            spec[parameter] = value
            rows.append((parameter, str(value), False, spec))
    return rows


def _dense_truth(prepared, *, window: int, order: int, n_grid: int):
    grid = np.linspace(0.0, 1.0, n_grid)
    values = np.empty(n_grid, dtype=float)
    for i, smoothness in enumerate(grid):
        lambda_ = td.smoothness_to_lambda(
            float(smoothness),
            n_obs=window,
            order=order,
        )
        values[i] = prepared.evaluate(lambda_).value

    minima = [
        float(grid[i])
        for i in range(1, n_grid - 1)
        if values[i] <= values[i - 1] and values[i] <= values[i + 1]
    ]
    best_idx = int(np.argmin(values))
    return grid, values, minima, float(grid[best_idx]), float(values[best_idx])


def _match_minima(
    truth: list[float],
    detected: list[float],
    *,
    tolerance: float,
) -> tuple[int, int]:
    matched = sum(
        any(abs(target - candidate) <= tolerance for candidate in detected)
        for target in truth
    )
    return int(matched), int(len(truth) - matched)


def _evaluate_spec(
    prepared,
    *,
    window: int,
    order: int,
    spec: dict,
    dense_minima: list[float],
    dense_best_s: float,
    dense_best_value: float,
    dense_step: float,
):
    cache: dict[float, object] = {}

    def evaluate(lambda_: float):
        key = float(lambda_)
        if key not in cache:
            cache[key] = prepared.evaluate(key)
        return cache[key]

    def callback(lambda_: float):
        result = evaluate(lambda_)
        return result.value, result.first, result.second

    started = time.perf_counter()
    search = td.find_stationary_points_smoothness(
        callback,
        n_obs=window,
        order=order,
        **spec,
    )
    minima = [
        point
        for point in search.points_
        if point.kind_ == "minimum"
    ]
    candidates = [
        (point.objective_, point.smoothness_)
        for point in minima
    ]
    endpoint_zero = evaluate(0.0)
    endpoint_one = evaluate(float("inf"))
    candidates.extend(
        [
            (endpoint_zero.value, 0.0),
            (endpoint_one.value, 1.0),
        ]
    )
    best_value, best_s = min(candidates, key=lambda row: (row[0], row[1]))
    seconds = time.perf_counter() - started

    matched, missed = _match_minima(
        dense_minima,
        [point.smoothness_ for point in minima],
        tolerance=max(2.0 * dense_step, 1e-6),
    )
    return {
        "matched_minima": matched,
        "missed_minima": missed,
        "best_s": float(best_s),
        "dense_best_s": dense_best_s,
        "best_s_abs_error": abs(float(best_s) - dense_best_s),
        "objective_regret": float(best_value) - dense_best_value,
        "n_evaluations": len(cache),
        "seconds": seconds,
    }


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    dense_grid_size = int(
        args.dense_grid_size
        if args.dense_grid_size is not None
        else preset["dense_grid_size"]
    )
    if dense_grid_size < 3:
        raise ValueError("dense-grid-size must be at least 3.")

    cases = list(
        itertools.product(
            preset["seeds"],
            preset["scenarios"],
            preset["orders"],
            preset["windows"],
            preset["horizons"],
        )
    )
    if preset["max_cases"] is not None:
        cases = cases[: int(preset["max_cases"])]

    specs = _specifications()
    run_dir = args.output_dir or _default_run_directory(args.preset)
    run_dir.mkdir(parents=True, exist_ok=True)

    case_rows: list[dict] = []
    started_all = time.perf_counter()

    for case_index, (seed, scenario_name, order, window, horizon) in enumerate(
        cases,
        start=1,
    ):
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
        )[-args.max_origins :]
        prepared = td.prepare_rolling_pure_forecast_objective(
            data.y,
            splits,
            order=order,
        )

        grid, dense_values, dense_minima, dense_best_s, dense_best_value = (
            _dense_truth(
                prepared,
                window=window,
                order=order,
                n_grid=dense_grid_size,
            )
        )
        dense_step = float(grid[1] - grid[0])

        print(
            f"[{case_index}/{len(cases)}] seed={seed} scenario={scenario_name} "
            f"d={order} L={window} h={horizon}",
            flush=True,
        )

        for parameter, setting, is_primary, spec in specs:
            result = _evaluate_spec(
                prepared,
                window=window,
                order=order,
                spec=spec,
                dense_minima=dense_minima,
                dense_best_s=dense_best_s,
                dense_best_value=dense_best_value,
                dense_step=dense_step,
            )
            case_rows.append(
                {
                    "seed": seed,
                    "scenario": scenario_name,
                    "order": order,
                    "window": window,
                    "horizon": horizon,
                    "parameter": parameter,
                    "setting": setting,
                    "is_primary": is_primary,
                    **result,
                }
            )

    cases_frame = pd.DataFrame(case_rows)
    cases_frame.to_csv(run_dir / "sensitivity_cases.csv", index=False)

    summary_rows: list[dict] = []
    for (parameter, setting, is_primary), group in cases_frame.groupby(
        ["parameter", "setting", "is_primary"],
        sort=False,
    ):
        positive_regret = group["objective_regret"] > 1e-12
        summary_rows.append(
            {
                "parameter": parameter,
                "setting": setting,
                "is_primary": bool(is_primary),
                "n_cases": int(len(group)),
                "matched_minima": int(group["matched_minima"].sum()),
                "missed_minima": int(group["missed_minima"].sum()),
                "cases_with_missed_minima": int(
                    (group["missed_minima"] > 0).sum()
                ),
                "positive_regret_cases": int(positive_regret.sum()),
                "max_positive_regret": float(
                    np.maximum(group["objective_regret"].to_numpy(), 0.0).max()
                ),
                "mean_abs_s_error": float(group["best_s_abs_error"].mean()),
                "max_abs_s_error": float(group["best_s_abs_error"].max()),
                "mean_evaluations": float(group["n_evaluations"].mean()),
                "median_evaluations": float(group["n_evaluations"].median()),
                "mean_seconds": float(group["seconds"].mean()),
            }
        )

    pd.DataFrame(summary_rows).to_csv(
        run_dir / "sensitivity_summary.csv",
        index=False,
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "suite": "search_design_sensitivity",
        "preset": args.preset,
        "primary_spec": PRIMARY_SPEC,
        "sensitivity_values": {
            key: list(values) for key, values in SENSITIVITY_VALUES.items()
        },
        "n_obs": args.n_obs,
        "dense_grid_size": dense_grid_size,
        "n_cases": len(cases),
        "n_specifications": len(specs),
        "elapsed_seconds": time.perf_counter() - started_all,
    }
    (run_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote sensitivity benchmark to {run_dir}", flush=True)


if __name__ == "__main__":
    main()
