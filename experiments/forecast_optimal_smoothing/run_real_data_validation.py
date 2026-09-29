from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import os
import subprocess
import time
import urllib.request
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

# Keep multiprocessing workers from spawning nested BLAS thread pools.
for _name in (
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ.setdefault(_name, "1")

import numpy as np
import pandas as pd

import trend_estimation as td

from run_adaptive_value import _block_metrics, _fit_frozen_forecast


SNAPSHOT_ROOT = Path("data") / "external" / "real_world" / "snapshot"
RESULT_ROOT = Path("results") / "forecast_optimal_smoothing"
ORDERS = (1, 2, 3)
OBSERVATION_WINDOWS = (24, 48, 72)
OBSERVATION_SELECTOR_MEMORY = 20
LOG_BOUNDS = (-18.0, 24.0)


@dataclass(frozen=True)
class SeriesSpec:
    key: str
    label: str
    asset_class: str
    source: str
    frequency: str
    horizons: tuple[int, ...]
    outer_step_explore: int
    outer_step_paper: int
    inner_step: int


DEVELOPMENT_SERIES: tuple[SeriesSpec, ...] = (
    SeriesSpec("GDPC1", "US real GDP", "macro", "fred", "quarterly", (1, 2, 4), 1, 1, 1),
    SeriesSpec(
        "INDPRO",
        "US industrial production",
        "macro",
        "fred",
        "monthly",
        (1, 3, 6, 12),
        1,
        1,
        1,
    ),
    SeriesSpec("SPY", "SPDR S&P 500 ETF", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("QQQ", "Invesco QQQ", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("IWM", "iShares Russell 2000 ETF", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("DIA", "SPDR Dow Jones Industrial Average ETF", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("EFA", "iShares MSCI EAFE ETF", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("EEM", "iShares MSCI Emerging Markets ETF", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("AAPL", "Apple", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("MSFT", "Microsoft", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("JPM", "JPMorgan Chase", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("XOM", "Exxon Mobil", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("JNJ", "Johnson & Johnson", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("WMT", "Walmart", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("BTC-USD", "Bitcoin / USD", "crypto", "yahoo", "daily", (1, 7, 30), 20, 5, 5),
    SeriesSpec("ETH-USD", "Ether / USD", "crypto", "yahoo", "daily", (1, 7, 30), 20, 5, 5),
)

REPLICATION_SERIES: tuple[SeriesSpec, ...] = (
    SeriesSpec("VTI", "Vanguard Total Stock Market ETF", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("XLK", "Technology Select Sector SPDR Fund", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("XLF", "Financial Select Sector SPDR Fund", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("XLE", "Energy Select Sector SPDR Fund", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("XLV", "Health Care Select Sector SPDR Fund", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("VNQ", "Vanguard Real Estate ETF", "etf", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("KO", "Coca-Cola", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("PG", "Procter & Gamble", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("CVX", "Chevron", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("BAC", "Bank of America", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("CAT", "Caterpillar", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("HD", "Home Depot", "stock", "yahoo", "daily", (1, 5, 20), 20, 5, 5),
    SeriesSpec("LTC-USD", "Litecoin / USD", "crypto", "yahoo", "daily", (1, 7, 30), 20, 5, 5),
    SeriesSpec("XRP-USD", "XRP / USD", "crypto", "yahoo", "daily", (1, 7, 30), 20, 5, 5),
)

SERIES: tuple[SeriesSpec, ...] = DEVELOPMENT_SERIES + REPLICATION_SERIES


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Real-data external validation for forecast-optimal trend adaptation. "
            "Data are downloaded once into a versioned snapshot and reused by default."
        )
    )
    parser.add_argument(
        "--preset",
        choices=("smoke", "explore", "paper"),
        default="explore",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help="Worker processes. 0 uses all logical CPUs.",
    )
    parser.add_argument(
        "--refresh-data",
        action="store_true",
        help=(
            "Replace tracked snapshot files with newly downloaded data. "
            "Review and commit the resulting data diff deliberately."
        ),
    )
    parser.add_argument(
        "--download-only",
        action="store_true",
        help="Populate/refresh the versioned snapshot, write the manifest, and stop.",
    )
    parser.add_argument(
        "--panel",
        choices=("development", "replication"),
        default="development",
        help=(
            "Series panel. 'development' reproduces the inspected 16-series "
            "screen; 'replication' uses a separate frozen financial panel."
        ),
    )
    parser.add_argument(
        "--asset-classes",
        nargs="+",
        choices=("macro", "etf", "stock", "crypto"),
        default=None,
        help="Optional subset within the selected panel.",
    )
    parser.add_argument(
        "--n-grid",
        type=int,
        default=None,
    )
    parser.add_argument(
        "--evaluation-fraction",
        type=float,
        default=None,
        help="Fraction reserved for chronological OOS evaluation.",
    )
    parser.add_argument(
        "--scale-policy",
        choices=("observation", "frequency-aware"),
        default="observation",
        help=(
            "Candidate-window/selector-memory scale. 'observation' reproduces "
            "the first external screen exactly; 'frequency-aware' uses "
            "calendar-interpretable windows and a selector span tied to the "
            "largest candidate window."
        ),
    )
    return parser.parse_args()


def git_short_sha() -> str:
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


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_key(key: str) -> str:
    return key.replace("^", "INDEX_").replace("/", "_").replace("-", "_")


def _snapshot_path(spec: SeriesSpec) -> Path:
    return SNAPSHOT_ROOT / spec.source / f"{_safe_key(spec.key)}.csv"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _download_fred(spec: SeriesSpec, path: Path) -> None:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={spec.key}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "trend-estimation-research/1.0"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = response.read()

    frame = pd.read_csv(io.BytesIO(payload))
    if frame.shape[1] != 2:
        raise RuntimeError(f"Unexpected FRED shape for {spec.key}: {frame.shape}")

    frame.columns = ["date", "value"]
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    frame["value"] = pd.to_numeric(frame["value"], errors="coerce")
    frame = frame.dropna().sort_values("date").drop_duplicates("date")
    if frame.empty:
        raise RuntimeError(f"FRED returned no usable rows for {spec.key}.")

    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)


def _download_yahoo(spec: SeriesSpec, path: Path) -> None:
    try:
        import yfinance as yf
    except ImportError as exc:
        raise RuntimeError(
            "Market/crypto snapshot is missing and yfinance is not installed. "
            'Run: pip install -e ".[finance]"'
        ) from exc

    frame = yf.Ticker(spec.key).history(
        period="max",
        auto_adjust=True,
        actions=False,
        raise_errors=True,
    )
    if frame.empty or "Close" not in frame.columns:
        raise RuntimeError(f"Yahoo/yfinance returned no usable Close data for {spec.key}.")

    values = pd.DataFrame(
        {
            "date": pd.to_datetime(frame.index, errors="coerce"),
            "value": pd.to_numeric(frame["Close"], errors="coerce").to_numpy(),
        }
    )
    if getattr(values["date"].dt, "tz", None) is not None:
        values["date"] = values["date"].dt.tz_localize(None)

    values = values.dropna().sort_values("date").drop_duplicates("date")
    values = values.loc[values["value"].gt(0.0)]
    if values.empty:
        raise RuntimeError(f"No positive price rows remain for {spec.key}.")

    path.parent.mkdir(parents=True, exist_ok=True)
    values.to_csv(path, index=False)


def _read_snapshot(spec: SeriesSpec) -> pd.DataFrame:
    path = _snapshot_path(spec)
    frame = pd.read_csv(path, parse_dates=["date"])
    frame["value"] = pd.to_numeric(frame["value"], errors="coerce")
    frame = frame.dropna().sort_values("date").drop_duplicates("date")
    return frame


def _ensure_snapshot(
    specs: tuple[SeriesSpec, ...],
    *,
    refresh: bool,
) -> dict[str, dict]:
    SNAPSHOT_ROOT.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, dict] = {}

    for i, spec in enumerate(specs, start=1):
        path = _snapshot_path(spec)
        if path.exists() and not refresh:
            action = "snapshot"
        else:
            action = "download"
            print(
                f"[data {i}/{len(specs)}] downloading {spec.key} ({spec.source})",
                flush=True,
            )
            if spec.source == "fred":
                _download_fred(spec, path)
            elif spec.source == "yahoo":
                _download_yahoo(spec, path)
            else:
                raise ValueError(f"Unknown source: {spec.source}")

        frame = _read_snapshot(spec)
        print(
            f"[data {i}/{len(specs)}] {spec.key}: {action}; "
            f"{len(frame)} rows, {frame['date'].min().date()} -> "
            f"{frame['date'].max().date()}",
            flush=True,
        )
        manifest[spec.key] = {
            "label": spec.label,
            "asset_class": spec.asset_class,
            "source": spec.source,
            "frequency": spec.frequency,
            "snapshot_path": str(path).replace("\\", "/"),
            "rows": int(len(frame)),
            "first_date": str(frame["date"].min().date()),
            "last_date": str(frame["date"].max().date()),
            "sha256": _sha256(path),
            "macro_vintage": (
                "current-vintage FRED snapshot; exploratory only until "
                "ALFRED vintage-correct replication"
                if spec.source == "fred"
                else None
            ),
        }

    manifest_path = SNAPSHOT_ROOT / "snapshot_manifest.json"
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "updated_at_utc": _utc_now(),
                "refresh_requested": bool(refresh),
                "series": manifest,
            },
            handle,
            indent=2,
        )
    return manifest


def _selected_specs(args: argparse.Namespace) -> tuple[SeriesSpec, ...]:
    specs = (
        DEVELOPMENT_SERIES
        if args.panel == "development"
        else REPLICATION_SERIES
    )
    if args.asset_classes:
        wanted = set(args.asset_classes)
        specs = tuple(spec for spec in specs if spec.asset_class in wanted)

    if args.preset == "smoke":
        smoke_keys = (
            {"GDPC1", "SPY", "BTC-USD"}
            if args.panel == "development"
            else {"VTI", "KO", "LTC-USD"}
        )
        specs = tuple(spec for spec in specs if spec.key in smoke_keys)

    if not specs:
        raise ValueError("No series remain after filtering.")
    return specs


def _resolve_workers(requested: int, n_tasks: int) -> int:
    if requested < 0:
        raise ValueError("workers must be >= 0.")
    logical = os.cpu_count() or 1
    chosen = logical if requested == 0 else requested
    return max(1, min(int(chosen), int(logical), int(n_tasks)))


def _design_for_spec(
    spec: SeriesSpec,
    scale_policy: str,
) -> tuple[tuple[int, ...], int]:
    if scale_policy == "observation":
        return OBSERVATION_WINDOWS, OBSERVATION_SELECTOR_MEMORY

    if scale_policy != "frequency-aware":
        raise ValueError(f"Unknown scale policy: {scale_policy}")

    if spec.frequency == "quarterly":
        windows = (12, 24, 48)
    elif spec.frequency == "monthly":
        windows = (24, 60, 120)
    elif spec.frequency == "daily":
        windows = (63, 126, 252)
    else:
        raise ValueError(f"Unsupported frequency: {spec.frequency}")

    selector_memory = max(
        20,
        int(math.ceil(max(windows) / max(1, int(spec.inner_step)))),
    )
    return windows, selector_memory


def _transform(frame: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    values = frame["value"].to_numpy(dtype=float)
    if np.any(values <= 0.0):
        raise ValueError("Real-data level transformation requires positive observations.")
    return frame["date"].to_numpy(), np.log(values)


def _local_descriptors(history: np.ndarray, window: int = 60) -> dict[str, float]:
    x = np.asarray(history[-window:], dtype=float)
    d1 = np.diff(x)
    d2 = np.diff(x, n=2)

    if d1.size >= 3 and np.std(d1[:-1]) > 0.0 and np.std(d1[1:]) > 0.0:
        ar1 = float(np.corrcoef(d1[:-1], d1[1:])[0, 1])
    else:
        ar1 = float("nan")

    diff_std = float(np.std(d1, ddof=1)) if d1.size >= 2 else float("nan")
    second_std = float(np.std(d2, ddof=1)) if d2.size >= 2 else float("nan")
    roughness_ratio = (
        second_std / diff_std
        if np.isfinite(diff_std) and diff_std > 0.0
        else float("nan")
    )
    return {
        "local_diff_std": diff_std,
        "local_diff_ar1": ar1,
        "local_roughness_ratio": roughness_ratio,
    }


def _period_label(relative_index: int, total_eval: int) -> str:
    if total_eval <= 0:
        return "all"
    frac = relative_index / total_eval
    if frac < 1.0 / 3.0:
        return "early"
    if frac < 2.0 / 3.0:
        return "mid"
    return "late"


def _selection(
    history: np.ndarray,
    *,
    horizon: int,
    inner_step: int,
    windows: tuple[int, ...],
    max_origins: int | None,
    n_grid: int,
):
    return td.select_fixed_window_pure_smoothness(
        history,
        orders=ORDERS,
        windows=windows,
        horizon=horizon,
        step=inner_step,
        max_origins=max_origins,
        min_origins=2,
        log_bounds=LOG_BOUNDS,
        n_grid=n_grid,
    ).best_


def _evaluate_task(payload) -> list[dict]:
    (
        spec,
        snapshot_path,
        horizon,
        preset,
        n_grid,
        evaluation_fraction,
        windows,
        selector_memory,
        scale_policy,
    ) = payload

    frame = pd.read_csv(snapshot_path, parse_dates=["date"])
    frame = frame.dropna().sort_values("date").drop_duplicates("date")
    dates, y = _transform(frame)

    n = len(y)
    if n < 180:
        raise RuntimeError(
            f"{spec.key} has only {n} usable observations; need at least 180."
        )

    train_fraction = 1.0 - float(evaluation_fraction)
    evaluation_start = max(120, int(math.floor(train_fraction * n)))
    evaluation_start = min(evaluation_start, n - int(horizon) - 8)

    if evaluation_start <= max(windows) + horizon:
        raise RuntimeError(
            f"{spec.key}: evaluation start leaves insufficient pre-OOS history."
        )

    if preset == "smoke":
        outer_step = 4 if spec.asset_class == "macro" else 60
    elif preset == "explore":
        outer_step = spec.outer_step_explore
    else:
        outer_step = spec.outer_step_paper

    frozen_all_pre = _selection(
        y[:evaluation_start],
        horizon=horizon,
        inner_step=spec.inner_step,
        windows=windows,
        max_origins=None,
        n_grid=n_grid,
    )
    frozen_local = _selection(
        y[:evaluation_start],
        horizon=horizon,
        inner_step=spec.inner_step,
        windows=windows,
        max_origins=selector_memory,
        n_grid=n_grid,
    )

    adaptive = td.nested_rolling_pure_forecast(
        y,
        outer_initial_train=evaluation_start,
        horizon=horizon,
        outer_step=outer_step,
        orders=ORDERS,
        windows=windows,
        inner_step=spec.inner_step,
        max_inner_origins=selector_memory,
        min_inner_origins=2,
        log_bounds=LOG_BOUNDS,
        n_grid=n_grid,
    )

    rows: list[dict] = []
    for record in adaptive.records:
        origin = int(record.origin)
        history = y[:origin]
        observed = np.asarray(record.observed, dtype=float)
        adaptive_prediction = np.asarray(record.prediction, dtype=float)
        benchmark_prediction = np.asarray(record.benchmark_prediction, dtype=float)

        all_pre_prediction = _fit_frozen_forecast(
            history,
            order=int(frozen_all_pre.order),
            window=int(frozen_all_pre.window),
            lambda_=float(frozen_all_pre.lambda_),
            horizon=observed.size,
        )
        local_prediction = _fit_frozen_forecast(
            history,
            order=int(frozen_local.order),
            window=int(frozen_local.window),
            lambda_=float(frozen_local.lambda_),
            horizon=observed.size,
        )

        adaptive_mse, _ = _block_metrics(observed, adaptive_prediction)
        all_pre_mse, _ = _block_metrics(observed, all_pre_prediction)
        local_mse, _ = _block_metrics(observed, local_prediction)
        benchmark_mse, _ = _block_metrics(observed, benchmark_prediction)
        descriptors = _local_descriptors(history)

        last_target = min(origin + observed.size - 1, n - 1)
        relative = origin - evaluation_start

        rows.append(
            {
                "series": spec.key,
                "label": spec.label,
                "asset_class": spec.asset_class,
                "frequency": spec.frequency,
                "scale_policy": scale_policy,
                "candidate_windows": "|".join(str(v) for v in windows),
                "selector_memory": int(selector_memory),
                "horizon": int(horizon),
                "outer_step": int(outer_step),
                "evaluation_start_index": int(evaluation_start),
                "evaluation_start_date": str(
                    pd.Timestamp(dates[evaluation_start]).date()
                ),
                "origin_index": origin,
                "origin_date": str(pd.Timestamp(dates[origin - 1]).date()),
                "target_end_date": str(pd.Timestamp(dates[last_target]).date()),
                "evaluation_period": _period_label(relative, n - evaluation_start),
                "adaptive_order": int(record.selected_order),
                "adaptive_window": int(record.selected_window),
                "adaptive_lambda": float(record.selected_lambda),
                "adaptive_smoothness": float(record.selected_smoothness),
                "frozen_all_pre_order": int(frozen_all_pre.order),
                "frozen_all_pre_window": int(frozen_all_pre.window),
                "frozen_all_pre_lambda": float(frozen_all_pre.lambda_),
                "frozen_all_pre_smoothness": float(frozen_all_pre.smoothness_),
                "frozen_all_pre_n_origins": int(frozen_all_pre.n_origins_),
                "frozen_local_order": int(frozen_local.order),
                "frozen_local_window": int(frozen_local.window),
                "frozen_local_lambda": float(frozen_local.lambda_),
                "frozen_local_smoothness": float(frozen_local.smoothness_),
                "adaptive_mse": adaptive_mse,
                "frozen_all_pre_mse": all_pre_mse,
                "frozen_local_mse": local_mse,
                "benchmark_mse": benchmark_mse,
                "adaptive_advantage_vs_frozen_all_pre": (
                    all_pre_mse - adaptive_mse
                ),
                **descriptors,
            }
        )

    return rows


def _summary(frame: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    keys = [
        "series",
        "label",
        "asset_class",
        "frequency",
        "scale_policy",
        "candidate_windows",
        "selector_memory",
        "horizon",
    ]

    for key, group in frame.groupby(keys, dropna=False):
        (
            series,
            label,
            asset_class,
            frequency,
            scale_policy,
            candidate_windows,
            selector_memory,
            horizon,
        ) = key
        a = float(group["adaptive_mse"].mean())
        fa = float(group["frozen_all_pre_mse"].mean())
        fl = float(group["frozen_local_mse"].mean())
        b = float(group["benchmark_mse"].mean())

        rows.append(
            {
                "series": series,
                "label": label,
                "asset_class": asset_class,
                "frequency": frequency,
                "scale_policy": scale_policy,
                "candidate_windows": candidate_windows,
                "selector_memory": int(selector_memory),
                "horizon": int(horizon),
                "n_origins": int(len(group)),
                "first_origin_date": str(group["origin_date"].min()),
                "last_origin_date": str(group["origin_date"].max()),
                "adaptive_mse": a,
                "frozen_all_pre_mse": fa,
                "frozen_local_mse": fl,
                "benchmark_mse": b,
                "adaptive_rmse_vs_frozen_all_pre": float(np.sqrt(a / fa)),
                "adaptive_rmse_vs_frozen_local": float(np.sqrt(a / fl)),
                "adaptive_relative_rmsfe_vs_no_change": float(np.sqrt(a / b)),
                "frozen_all_pre_relative_rmsfe_vs_no_change": float(
                    np.sqrt(fa / b)
                ),
                "mean_adaptive_advantage_vs_frozen_all_pre": float(
                    group["adaptive_advantage_vs_frozen_all_pre"].mean()
                ),
                "mean_adaptive_smoothness": float(
                    group["adaptive_smoothness"].mean()
                ),
                "mean_adaptive_window": float(group["adaptive_window"].mean()),
                "mean_adaptive_order": float(group["adaptive_order"].mean()),
            }
        )

    return pd.DataFrame(rows)


def _class_summary(summary: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for asset_class, group in summary.groupby("asset_class", dropna=False):
        rows.append(
            {
                "asset_class": asset_class,
                "n_series": int(group["series"].nunique()),
                "n_series_horizon_cells": int(len(group)),
                "median_adaptive_rmse_vs_frozen_all_pre": float(
                    group["adaptive_rmse_vs_frozen_all_pre"].median()
                ),
                "share_cells_adaptive_beats_frozen_all_pre": float(
                    (group["adaptive_rmse_vs_frozen_all_pre"] < 1.0).mean()
                ),
                "median_adaptive_relative_rmsfe_vs_no_change": float(
                    group["adaptive_relative_rmsfe_vs_no_change"].median()
                ),
                "share_cells_adaptive_beats_no_change": float(
                    (group["adaptive_relative_rmsfe_vs_no_change"] < 1.0).mean()
                ),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    args = parse_args()
    specs = _selected_specs(args)

    if args.preset == "smoke":
        default_grid = 81
        default_eval_fraction = 0.12
    else:
        default_grid = 321
        default_eval_fraction = 0.40

    n_grid = default_grid if args.n_grid is None else int(args.n_grid)
    evaluation_fraction = (
        default_eval_fraction
        if args.evaluation_fraction is None
        else float(args.evaluation_fraction)
    )
    if not 0.05 <= evaluation_fraction <= 0.60:
        raise ValueError("evaluation-fraction must be between 0.05 and 0.60.")

    print(
        "Data policy: use the tracked snapshot when present; network only for "
        "missing snapshot files or when --refresh-data is supplied.",
        flush=True,
    )
    snapshot_manifest = _ensure_snapshot(specs, refresh=bool(args.refresh_data))

    if args.download_only:
        print(f"Snapshot ready under {SNAPSHOT_ROOT}", flush=True)
        return

    payloads = []
    design_by_series: dict[str, dict] = {}
    for spec in specs:
        windows, selector_memory = _design_for_spec(spec, args.scale_policy)
        design_by_series[spec.key] = {
            "frequency": spec.frequency,
            "windows": list(windows),
            "selector_memory": int(selector_memory),
            "inner_step": int(spec.inner_step),
        }
        horizons = spec.horizons
        if args.preset == "smoke":
            horizons = horizons[:1]
        for horizon in horizons:
            payloads.append(
                (
                    spec,
                    str(_snapshot_path(spec)),
                    int(horizon),
                    args.preset,
                    int(n_grid),
                    float(evaluation_fraction),
                    windows,
                    int(selector_memory),
                    args.scale_policy,
                )
            )

    workers = _resolve_workers(int(args.workers), len(payloads))
    print(
        f"Execution: {len(payloads)} series/horizon tasks with {workers} workers",
        flush=True,
    )

    start = time.perf_counter()
    rows: list[dict] = []

    if workers == 1:
        iterator = map(_evaluate_task, payloads)
        for i, result_rows in enumerate(iterator, start=1):
            rows.extend(result_rows)
            print(f"[{i}/{len(payloads)}] completed", flush=True)
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            iterator = executor.map(_evaluate_task, payloads, chunksize=1)
            for i, result_rows in enumerate(iterator, start=1):
                rows.extend(result_rows)
                print(f"[{i}/{len(payloads)}] completed", flush=True)

    frame = pd.DataFrame(rows)
    summary = _summary(frame)
    class_summary = _class_summary(summary)
    elapsed = time.perf_counter() - start

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = RESULT_ROOT / (
        f"{stamp}_real-data-{args.panel}-{args.preset}-"
        f"{args.scale_policy}_{git_short_sha()}"
    )
    run_dir.mkdir(parents=True, exist_ok=True)

    frame.to_csv(run_dir / "real_data_forecast_blocks.csv", index=False)
    summary.to_csv(run_dir / "real_data_summary.csv", index=False)
    class_summary.to_csv(run_dir / "real_data_class_summary.csv", index=False)

    selected_snapshot = {
        key: snapshot_manifest[key]
        for key in sorted(snapshot_manifest)
    }
    metadata = {
        "created_at_utc": _utc_now(),
        "git_commit": git_short_sha(),
        "experiment": "real_data_external_validation",
        "panel": args.panel,
        "preset": args.preset,
        "workers": workers,
        "logical_cpus": os.cpu_count(),
        "n_grid": n_grid,
        "log_lambda_bounds": list(LOG_BOUNDS),
        "orders": list(ORDERS),
        "scale_policy": args.scale_policy,
        "series_design": design_by_series,
        "evaluation_fraction": evaluation_fraction,
        "transform": "natural log of positive level/adjusted price",
        "primary_fixed_comparator": "frozen_all_pre",
        "secondary_fixed_comparator": "frozen_local_same_selector_memory",
        "external_benchmark": "no_change",
        "macro_vintage_warning": (
            "GDPC1 and INDPRO are current-vintage FRED snapshots in this "
            "exploratory external-validation run. A paper-final macro result "
            "must be replicated with ALFRED real-time vintages to avoid revision "
            "look-ahead."
        ),
        "data_snapshot": selected_snapshot,
        "n_tasks": len(payloads),
        "n_forecast_blocks": int(len(frame)),
        "elapsed_seconds": float(elapsed),
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(f"Wrote results to {run_dir} in {elapsed:.1f}s", flush=True)


if __name__ == "__main__":
    main()
