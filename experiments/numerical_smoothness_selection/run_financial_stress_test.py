from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import trend_estimation as td


SNAPSHOT_ROOT = Path("data") / "external" / "real_world" / "snapshot" / "yahoo"
RESULT_ROOT = Path("results") / "numerical_smoothness_selection"

SERIES = {
    "SPY": {
        "file": "SPY.csv",
        "label": "SPDR S&P 500 ETF",
        "asset_class": "etf",
    },
    "QQQ": {
        "file": "QQQ.csv",
        "label": "Invesco QQQ",
        "asset_class": "etf",
    },
    "AAPL": {
        "file": "AAPL.csv",
        "label": "Apple",
        "asset_class": "stock",
    },
    "XOM": {
        "file": "XOM.csv",
        "label": "Exxon Mobil",
        "asset_class": "stock",
    },
    "BTC-USD": {
        "file": "BTC_USD.csv",
        "label": "Bitcoin / USD",
        "asset_class": "crypto",
    },
    "ETH-USD": {
        "file": "ETH_USD.csv",
        "label": "Ether / USD",
        "asset_class": "crypto",
    },
}

FROZEN_SEARCH = {
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

PRESETS = {
    "smoke": {
        "series": ("SPY",),
        "orders": (2,),
        "windows": (126,),
        "horizons": (5,),
        "dense_grid_size": 401,
        "tail_observations": 1000,
    },
    "paper": {
        "series": tuple(SERIES),
        "orders": (1, 2, 3, 4),
        "windows": (63, 126, 252, 504),
        "horizons": (1, 5, 20, 60),
        "dense_grid_size": 5001,
        "tail_observations": 2000,
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Stress-test the frozen adaptive smoothness search on tracked "
            "real financial price snapshots. This experiment evaluates search "
            "geometry only; it does not compare forecasting models."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument("--dense-grid-size", type=int, default=None)
    parser.add_argument("--tail-observations", type=int, default=None)
    parser.add_argument("--max-origins", type=int, default=30)
    parser.add_argument("--step", type=int, default=5)
    parser.add_argument(
        "--max-cases",
        type=int,
        default=None,
        help="Optional deterministic prefix for debugging/tests.",
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


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _default_run_directory(preset: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return RESULT_ROOT / (
        f"{stamp}_financial-stress-{preset}_{_git_short_sha()}"
    )


def _load_series(key: str, tail_observations: int) -> tuple[pd.DataFrame, Path]:
    spec = SERIES[key]
    path = SNAPSHOT_ROOT / spec["file"]
    if not path.exists():
        raise FileNotFoundError(
            f"Tracked snapshot is missing: {path}. "
            "This numerical stress test never downloads data."
        )

    frame = pd.read_csv(path, parse_dates=["date"])
    frame["value"] = pd.to_numeric(frame["value"], errors="coerce")
    frame = (
        frame.dropna(subset=["date", "value"])
        .sort_values("date")
        .drop_duplicates("date")
    )
    frame = frame.loc[frame["value"] > 0.0].copy()
    if len(frame) < tail_observations:
        raise ValueError(
            f"{key} has only {len(frame)} positive rows, fewer than "
            f"tail_observations={tail_observations}."
        )
    return frame.tail(tail_observations).reset_index(drop=True), path


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
        any(abs(dense_s - candidate) <= tolerance for candidate in adaptive_s)
        for dense_s, _ in dense_minima
    )
    return int(matched), int(len(dense_minima) - matched)


def _run_case(
    *,
    key: str,
    frame: pd.DataFrame,
    order: int,
    window: int,
    horizon: int,
    dense_grid_size: int,
    max_origins: int,
    step: int,
) -> tuple[dict, list[dict]]:
    y = np.log(frame["value"].to_numpy(dtype=float))
    splits = td.rolling_origin_splits(
        len(y),
        initial_train=window,
        horizon=horizon,
        step=step,
        expanding=False,
        train_window=window,
    )[-max_origins:]
    if not splits:
        raise ValueError(
            f"No rolling origins for {key}, d={order}, L={window}, h={horizon}."
        )

    prepared = td.prepare_rolling_pure_forecast_objective(
        y,
        splits,
        order=order,
    )
    cache: dict[float, object] = {}

    def evaluate(lambda_: float):
        key_lambda = float(lambda_)
        if key_lambda not in cache:
            cache[key_lambda] = prepared.evaluate(key_lambda)
        return cache[key_lambda]

    def callback(lambda_: float):
        result = evaluate(lambda_)
        return result.value, result.first, result.second

    adaptive_start = time.perf_counter()
    search = td.find_stationary_points_smoothness(
        callback,
        n_obs=window,
        order=order,
        **FROZEN_SEARCH,
    )
    adaptive_minima = tuple(
        point for point in search.points_ if point.kind_ == "minimum"
    )
    endpoint_zero = evaluate(0.0)
    endpoint_one = evaluate(float("inf"))
    candidates = [
        (point.objective_, point.smoothness_, "interior")
        for point in adaptive_minima
    ]
    candidates.extend(
        [
            (endpoint_zero.value, 0.0, "S=0"),
            (endpoint_one.value, 1.0, "S=1"),
        ]
    )
    adaptive_best_value, adaptive_best_s, adaptive_best_source = min(
        candidates,
        key=lambda row: (row[0], row[1]),
    )
    adaptive_seconds = time.perf_counter() - adaptive_start

    dense_start = time.perf_counter()
    dense_s, dense_values, dense_minima, dense_boundary_minima = _dense_reference(
        prepared,
        window=window,
        order=order,
        n_grid=dense_grid_size,
    )
    dense_seconds = time.perf_counter() - dense_start
    dense_best_index = int(np.argmin(dense_values))
    dense_best_s = float(dense_s[dense_best_index])
    dense_best_value = float(dense_values[dense_best_index])
    grid_step = float(dense_s[1] - dense_s[0])
    matched, missed = _match_dense_minima(
        dense_minima,
        adaptive_minima,
        grid_step=grid_step,
    )

    spec = SERIES[key]
    row = {
        "series": key,
        "label": spec["label"],
        "asset_class": spec["asset_class"],
        "first_date": str(frame["date"].iloc[0].date()),
        "last_date": str(frame["date"].iloc[-1].date()),
        "n_observations": int(len(frame)),
        "order": order,
        "window": window,
        "horizon": horizon,
        "n_origins": len(splits),
        "n_adaptive_stationary_points": len(search.points_),
        "n_adaptive_local_minima": len(adaptive_minima),
        "n_dense_interior_minima": len(dense_minima),
        "n_dense_boundary_minima": len(dense_boundary_minima),
        "n_dense_interior_minima_matched": matched,
        "n_dense_interior_minima_missed": missed,
        "adaptive_best_s": float(adaptive_best_s),
        "adaptive_best_cv": float(adaptive_best_value),
        "adaptive_best_source": adaptive_best_source,
        "dense_best_s": dense_best_s,
        "dense_best_cv": dense_best_value,
        "best_s_abs_error": abs(float(adaptive_best_s) - dense_best_s),
        "objective_regret": float(adaptive_best_value) - dense_best_value,
        "adaptive_evaluations": len(cache),
        "dense_evaluations": int(dense_grid_size),
        "adaptive_seconds": adaptive_seconds,
        "dense_seconds": dense_seconds,
    }

    point_rows = [
        {
            "series": key,
            "asset_class": spec["asset_class"],
            "order": order,
            "window": window,
            "horizon": horizon,
            "smoothness": point.smoothness_,
            "lambda": point.lambda_,
            "objective": point.objective_,
            "kind": point.kind_,
            "curvature_smoothness": point.curvature_smoothness_,
        }
        for point in search.points_
    ]
    return row, point_rows


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    dense_grid_size = int(
        args.dense_grid_size
        if args.dense_grid_size is not None
        else preset["dense_grid_size"]
    )
    tail_observations = int(
        args.tail_observations
        if args.tail_observations is not None
        else preset["tail_observations"]
    )
    if dense_grid_size < 3:
        raise ValueError("dense-grid-size must be at least 3.")
    if tail_observations <= max(preset["windows"]):
        raise ValueError("tail-observations must exceed the largest window.")
    if args.max_origins <= 0 or args.step <= 0:
        raise ValueError("max-origins and step must be positive.")

    loaded: dict[str, pd.DataFrame] = {}
    snapshot_metadata: dict[str, dict] = {}
    for key in preset["series"]:
        frame, path = _load_series(key, tail_observations)
        loaded[key] = frame
        snapshot_metadata[key] = {
            "path": str(path).replace("\\", "/"),
            "sha256": _sha256(path),
            "rows_used": int(len(frame)),
            "first_date": str(frame["date"].iloc[0].date()),
            "last_date": str(frame["date"].iloc[-1].date()),
        }

    cases = list(
        itertools.product(
            preset["series"],
            preset["orders"],
            preset["windows"],
            preset["horizons"],
        )
    )
    if args.max_cases is not None:
        if args.max_cases <= 0:
            raise ValueError("max-cases must be positive when supplied.")
        cases = cases[: args.max_cases]

    run_dir = args.output_dir or _default_run_directory(args.preset)
    run_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []
    point_rows: list[dict] = []
    started = time.perf_counter()

    for index, (key, order, window, horizon) in enumerate(cases, start=1):
        print(
            f"[{index}/{len(cases)}] {key} d={order} L={window} h={horizon}",
            flush=True,
        )
        row, points = _run_case(
            key=key,
            frame=loaded[key],
            order=int(order),
            window=int(window),
            horizon=int(horizon),
            dense_grid_size=dense_grid_size,
            max_origins=int(args.max_origins),
            step=int(args.step),
        )
        rows.append(row)
        point_rows.extend(points)
        print(
            "    "
            f"minima={row['n_adaptive_local_minima']}/"
            f"{row['n_dense_interior_minima']} "
            f"missed={row['n_dense_interior_minima_missed']} "
            f"S*={row['adaptive_best_s']:.6f}/"
            f"{row['dense_best_s']:.6f} "
            f"eval={row['adaptive_evaluations']}/{row['dense_evaluations']}",
            flush=True,
        )

    pd.DataFrame(rows).to_csv(run_dir / "search_summary.csv", index=False)
    pd.DataFrame(point_rows).to_csv(
        run_dir / "stationary_points.csv",
        index=False,
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "suite": "financial_geometry_stress",
        "preset": args.preset,
        "data_policy": "tracked_snapshot_only",
        "transform": "natural_log_price",
        "endpoint_policy": "exact",
        "forecast_continuation": "native_finite_difference",
        "frozen_search": FROZEN_SEARCH,
        "series": list(preset["series"]),
        "orders": list(preset["orders"]),
        "windows": list(preset["windows"]),
        "horizons": list(preset["horizons"]),
        "tail_observations": tail_observations,
        "max_origins": int(args.max_origins),
        "step": int(args.step),
        "dense_grid_size": dense_grid_size,
        "n_cases": len(cases),
        "snapshot": snapshot_metadata,
        "elapsed_seconds": time.perf_counter() - started,
        "interpretation": (
            "Numerical geometry stress test only; not a forecasting-model "
            "comparison and not evidence of financial predictability."
        ),
    }
    (run_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote financial stress test to {run_dir}", flush=True)


if __name__ == "__main__":
    main()
