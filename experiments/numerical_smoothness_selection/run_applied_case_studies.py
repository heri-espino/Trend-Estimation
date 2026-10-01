from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import trend_estimation as td


RESULT_ROOT = Path("results") / "numerical_smoothness_selection"
SNAPSHOT_ROOT = Path("data") / "external" / "real_world" / "snapshot"

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

CANDIDATE_SPACING_EPSILON = 0.10
MAX_CANDIDATES = 3
BOUNDARY_PROBE = 0.002

SERIES = {
    "GDPC1": {
        "path": SNAPSHOT_ROOT / "fred" / "GDPC1.csv",
        "label": "U.S. real GDP",
        "family": "GDP",
        "asset_class": "macroeconomic",
        "tail_observations": 248,
        "test_reserve": 8,
        "orders": (1, 2, 3, 4),
        "windows": (40, 60, 80, 120),
        "horizons": (1, 2, 4, 8),
        "step": 1,
        "max_origins": 24,
    },
    "SPY": {
        "path": SNAPSHOT_ROOT / "yahoo" / "SPY.csv",
        "label": "SPDR S&P 500 ETF",
        "family": "ETF",
        "asset_class": "etf",
        "tail_observations": 2060,
        "test_reserve": 60,
        "orders": (1, 2, 3, 4),
        "windows": (63, 126, 252, 504),
        "horizons": (1, 5, 20, 60),
        "step": 5,
        "max_origins": 30,
    },
    "AAPL": {
        "path": SNAPSHOT_ROOT / "yahoo" / "AAPL.csv",
        "label": "Apple",
        "family": "Stock",
        "asset_class": "stock",
        "tail_observations": 2060,
        "test_reserve": 60,
        "orders": (1, 2, 3, 4),
        "windows": (63, 126, 252, 504),
        "horizons": (1, 5, 20, 60),
        "step": 5,
        "max_origins": 30,
    },
    "BTC-USD": {
        "path": SNAPSHOT_ROOT / "yahoo" / "BTC_USD.csv",
        "label": "Bitcoin / USD",
        "family": "Crypto",
        "asset_class": "crypto",
        "tail_observations": 2060,
        "test_reserve": 60,
        "orders": (1, 2, 3, 4),
        "windows": (63, 126, 252, 504),
        "horizons": (1, 5, 20, 60),
        "step": 5,
        "max_origins": 30,
    },
}

PRESETS = {
    "smoke": {
        "series": ("GDPC1",),
        "config_override": {
            "GDPC1": {
                "orders": (2,),
                "windows": (40,),
                "horizons": (4,),
            }
        },
        "profile_grid_size": 201,
    },
    "paper": {
        "series": ("GDPC1", "SPY", "AAPL", "BTC-USD"),
        "config_override": {},
        "profile_grid_size": 2001,
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Interpret multiple rolling forecast-CV smoothness minima on "
            "pre-specified real series using a development-only selection "
            "stage and an untouched final test block."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument("--profile-grid-size", type=int, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument(
        "--figures-from-run",
        type=Path,
        default=None,
        help=(
            "Regenerate the applied figures from an existing result directory "
            "without rerunning configuration or smoothness selection."
        ),
    )
    return parser.parse_args()


def _git_short_sha() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def _default_run_directory(preset: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return RESULT_ROOT / f"{stamp}_applied-{preset}_{_git_short_sha()}"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_series(key: str) -> pd.DataFrame:
    spec = SERIES[key]
    path = Path(spec["path"])
    if not path.exists():
        raise FileNotFoundError(
            f"Tracked snapshot is missing: {path}. "
            "This experiment never downloads data."
        )

    frame = pd.read_csv(path, parse_dates=["date"])
    frame["value"] = pd.to_numeric(frame["value"], errors="coerce")
    frame = (
        frame.dropna(subset=["date", "value"])
        .sort_values("date")
        .drop_duplicates("date")
    )
    frame = frame.loc[frame["value"] > 0.0].copy()

    tail = int(spec["tail_observations"])
    if len(frame) < tail:
        raise ValueError(
            f"{key} has only {len(frame)} positive observations; "
            f"{tail} are required by the frozen case-study protocol."
        )
    return frame.tail(tail).reset_index(drop=True)


def _effective_grid(key: str, preset: dict) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    spec = SERIES[key]
    override = preset["config_override"].get(key, {})
    orders = tuple(override.get("orders", spec["orders"]))
    windows = tuple(override.get("windows", spec["windows"]))
    horizons = tuple(override.get("horizons", spec["horizons"]))
    return orders, windows, horizons


def _make_prepared_objective(
    development_log: np.ndarray,
    *,
    order: int,
    window: int,
    horizon: int,
    step: int,
    max_origins: int,
):
    splits = td.rolling_origin_splits(
        len(development_log),
        initial_train=window,
        horizon=horizon,
        step=step,
        expanding=False,
        train_window=window,
    )
    splits = splits[-max_origins:]
    if not splits:
        raise ValueError(
            f"No rolling origins for d={order}, L={window}, h={horizon}."
        )
    prepared = td.prepare_rolling_pure_forecast_objective(
        development_log,
        splits,
        order=order,
    )
    return prepared, splits


def _search_candidates(
    prepared,
    *,
    order: int,
    window: int,
) -> tuple[object, list[dict], int]:
    cache: dict[float, object] = {}

    def evaluate_lambda(lambda_: float):
        key = float(lambda_)
        if key not in cache:
            cache[key] = prepared.evaluate(key)
        return cache[key]

    def callback(lambda_: float):
        result = evaluate_lambda(lambda_)
        return result.value, result.first, result.second

    result = td.find_stationary_points_smoothness(
        callback,
        n_obs=window,
        order=order,
        **FROZEN_SEARCH,
    )

    pool: list[dict] = []
    for point in result.points_:
        if point.kind_ != "minimum":
            continue
        pool.append(
            {
                "smoothness": float(point.smoothness_),
                "lambda": float(point.lambda_),
                "cv_error": float(point.objective_),
                "source": "interior",
            }
        )

    endpoint_values = {
        0.0: float(evaluate_lambda(0.0).value),
        1.0: float(evaluate_lambda(float("inf")).value),
    }
    lower_probe_lambda = td.smoothness_to_lambda(
        BOUNDARY_PROBE,
        n_obs=window,
        order=order,
    )
    upper_probe_lambda = td.smoothness_to_lambda(
        1.0 - BOUNDARY_PROBE,
        n_obs=window,
        order=order,
    )
    lower_probe_value = float(evaluate_lambda(lower_probe_lambda).value)
    upper_probe_value = float(evaluate_lambda(upper_probe_lambda).value)

    if endpoint_values[0.0] <= lower_probe_value:
        pool.append(
            {
                "smoothness": 0.0,
                "lambda": 0.0,
                "cv_error": endpoint_values[0.0],
                "source": "S=0",
            }
        )
    if endpoint_values[1.0] <= upper_probe_value:
        pool.append(
            {
                "smoothness": 1.0,
                "lambda": float("inf"),
                "cv_error": endpoint_values[1.0],
                "source": "S=1",
            }
        )

    all_global = list(pool)
    if not all_global:
        all_global.extend(
            [
                {
                    "smoothness": 0.0,
                    "lambda": 0.0,
                    "cv_error": endpoint_values[0.0],
                    "source": "S=0",
                },
                {
                    "smoothness": 1.0,
                    "lambda": float("inf"),
                    "cv_error": endpoint_values[1.0],
                    "source": "S=1",
                },
            ]
        )
    else:
        best_pool = min(all_global, key=lambda row: row["cv_error"])
        best_endpoint = min(
            (
                {
                    "smoothness": 0.0,
                    "lambda": 0.0,
                    "cv_error": endpoint_values[0.0],
                    "source": "S=0",
                },
                {
                    "smoothness": 1.0,
                    "lambda": float("inf"),
                    "cv_error": endpoint_values[1.0],
                    "source": "S=1",
                },
            ),
            key=lambda row: row["cv_error"],
        )
        if best_endpoint["cv_error"] < best_pool["cv_error"]:
            all_global.append(best_endpoint)

    ordered = sorted(
        all_global,
        key=lambda row: (row["cv_error"], row["smoothness"]),
    )

    representatives: list[dict] = []
    for candidate in ordered:
        if any(
            abs(candidate["smoothness"] - kept["smoothness"])
            < CANDIDATE_SPACING_EPSILON
            for kept in representatives
        ):
            continue
        representatives.append(candidate)
        if len(representatives) >= MAX_CANDIDATES:
            break

    if not representatives:
        raise RuntimeError("Candidate search unexpectedly returned no representatives.")

    for rank, candidate in enumerate(representatives, start=1):
        candidate["cv_rank"] = rank

    return result, representatives, len(cache)


def _scan_configurations(
    key: str,
    development_log: np.ndarray,
    *,
    preset: dict,
) -> tuple[pd.DataFrame, dict]:
    spec = SERIES[key]
    orders, windows, horizons = _effective_grid(key, preset)

    rows: list[dict] = []
    payloads: dict[tuple[int, int, int], dict] = {}

    for order, window, horizon in itertools.product(orders, windows, horizons):
        if window + horizon > len(development_log):
            continue

        prepared, splits = _make_prepared_objective(
            development_log,
            order=order,
            window=window,
            horizon=horizon,
            step=int(spec["step"]),
            max_origins=int(spec["max_origins"]),
        )
        search, candidates, n_evaluations = _search_candidates(
            prepared,
            order=order,
            window=window,
        )

        if len(candidates) >= 2:
            separation = abs(
                candidates[0]["smoothness"] - candidates[1]["smoothness"]
            )
        else:
            separation = -1.0

        key_tuple = (int(order), int(window), int(horizon))
        payloads[key_tuple] = {
            "prepared": prepared,
            "splits": splits,
            "search": search,
            "candidates": candidates,
        }
        rows.append(
            {
                "series": key,
                "order": int(order),
                "window": int(window),
                "horizon": int(horizon),
                "n_representative_candidates": int(len(candidates)),
                "selection_score": float(separation),
                "best_cv_error": float(candidates[0]["cv_error"]),
                "best_smoothness": float(candidates[0]["smoothness"]),
                "adaptive_evaluations": int(n_evaluations),
                "n_stationary_points": int(len(search.points_)),
            }
        )

    frame = pd.DataFrame(rows)
    if frame.empty:
        raise RuntimeError(f"No valid configurations for {key}.")

    eligible = frame.loc[frame["n_representative_candidates"] >= 2].copy()
    if eligible.empty:
        eligible = frame.copy()
        eligible["selection_score"] = eligible["n_representative_candidates"].astype(
            float
        )

    selected = (
        eligible.sort_values(
            [
                "selection_score",
                "order",
                "window",
                "horizon",
            ],
            ascending=[False, True, True, True],
        )
        .iloc[0]
    )
    selected_key = (
        int(selected["order"]),
        int(selected["window"]),
        int(selected["horizon"]),
    )
    frame["selected"] = (
        (frame["order"] == selected_key[0])
        & (frame["window"] == selected_key[1])
        & (frame["horizon"] == selected_key[2])
    )
    return frame, payloads[selected_key]


def _evaluate_frozen_candidates(
    key: str,
    frame: pd.DataFrame,
    development: pd.DataFrame,
    test: pd.DataFrame,
    *,
    order: int,
    window: int,
    horizon: int,
    candidates: list[dict],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    train = development.tail(window).copy()
    train_log = np.log(train["value"].to_numpy(dtype=float))
    test_used = test.head(horizon).copy()
    test_log = np.log(test_used["value"].to_numpy(dtype=float))

    rows: list[dict] = []
    path_rows: list[dict] = []

    for candidate in candidates:
        model = td.PurePenalizedTrend(
            order=order,
            smoothness=float(candidate["smoothness"]),
        ).fit(train_log)
        forecast_log = np.asarray(model.forecast(horizon), dtype=float)
        test_mse = float(np.mean((test_log - forecast_log) ** 2))

        rows.append(
            {
                "series": key,
                "family": SERIES[key]["family"],
                "asset_class": SERIES[key]["asset_class"],
                "order": order,
                "window": window,
                "horizon": horizon,
                "cv_rank": int(candidate["cv_rank"]),
                "smoothness": float(candidate["smoothness"]),
                "lambda": float(candidate["lambda"]),
                "source": candidate["source"],
                "cv_error": float(candidate["cv_error"]),
                "test_mse": test_mse,
            }
        )

        for date, observed, fitted in zip(
            train["date"],
            train["value"],
            np.exp(model.trend_),
        ):
            path_rows.append(
                {
                    "series": key,
                    "family": SERIES[key]["family"],
                    "cv_rank": int(candidate["cv_rank"]),
                    "smoothness": float(candidate["smoothness"]),
                    "segment": "train",
                    "date": date,
                    "observed": float(observed),
                    "candidate_path": float(fitted),
                }
            )

        for date, observed, predicted in zip(
            test_used["date"],
            test_used["value"],
            np.exp(forecast_log),
        ):
            path_rows.append(
                {
                    "series": key,
                    "family": SERIES[key]["family"],
                    "cv_rank": int(candidate["cv_rank"]),
                    "smoothness": float(candidate["smoothness"]),
                    "segment": "test",
                    "date": date,
                    "observed": float(observed),
                    "candidate_path": float(predicted),
                }
            )

    result = pd.DataFrame(rows).sort_values("cv_rank").reset_index(drop=True)
    result["test_rank"] = (
        result["test_mse"].rank(method="first", ascending=True).astype(int)
    )
    result["delta_cv"] = result["cv_error"] - result["cv_error"].min()
    result["delta_test"] = result["test_mse"] - result["test_mse"].min()
    test_best_cv_rank = int(
        result.loc[result["test_rank"].idxmin(), "cv_rank"]
    )
    rank_reversal = test_best_cv_rank != 1
    result["validation_test_rank_reversal"] = bool(rank_reversal)

    return result, pd.DataFrame(path_rows)


def _objective_profile(
    key: str,
    prepared,
    search,
    *,
    order: int,
    window: int,
    horizon: int,
    grid_size: int,
) -> pd.DataFrame:
    grid = np.linspace(0.0, 1.0, grid_size)
    rows: list[dict] = []
    sampled = set(round(float(x), 12) for x in search.sampled_smoothness_)

    for smoothness in grid:
        lambda_ = td.smoothness_to_lambda(
            float(smoothness),
            n_obs=window,
            order=order,
        )
        value = float(prepared.evaluate(lambda_).value)
        rows.append(
            {
                "series": key,
                "family": SERIES[key]["family"],
                "order": order,
                "window": window,
                "horizon": horizon,
                "smoothness": float(smoothness),
                "cv_error": value,
                "is_adaptive_sample": round(float(smoothness), 12) in sampled,
            }
        )

    return pd.DataFrame(rows)


def _temporal_protocol(selections: pd.DataFrame) -> pd.DataFrame:
    """Reconstruct the exact rolling-validation chronology for selected cases.

    The final test reserve is never part of any rolling-origin split.  Each row
    describes one development-region validation block for the selected
    (d, L, h) configuration and repeats the final refit/test boundaries needed
    to make the plotting protocol auditable.
    """

    rows: list[dict] = []
    for _, selection in selections.iterrows():
        key = str(selection["series"])
        spec = SERIES[key]
        frame = _load_series(key)

        test_reserve = int(
            selection.get("test_reserve", spec["test_reserve"])
        )
        development = frame.iloc[:-test_reserve].copy()
        test = frame.iloc[-test_reserve:].copy()

        window = int(selection["window"])
        horizon = int(selection["horizon"])
        step = int(spec["step"])
        max_origins = int(spec["max_origins"])

        splits = td.rolling_origin_splits(
            len(development),
            initial_train=window,
            horizon=horizon,
            step=step,
            expanding=False,
            train_window=window,
        )
        splits = splits[-max_origins:]
        if not splits:
            raise RuntimeError(
                f"No rolling validation splits for selected case {key}."
            )

        final_train = development.tail(window)
        scored_test = test.head(horizon)

        for split_number, split in enumerate(splits, start=1):
            rows.append(
                {
                    "series": key,
                    "family": spec["family"],
                    "order": int(selection["order"]),
                    "window": window,
                    "horizon": horizon,
                    "split_number": split_number,
                    "train_start_date": development["date"].iloc[
                        split.train.start
                    ],
                    "train_end_date": development["date"].iloc[
                        split.train.stop - 1
                    ],
                    "validation_start_date": development["date"].iloc[
                        split.validation.start
                    ],
                    "validation_end_date": development["date"].iloc[
                        split.validation.stop - 1
                    ],
                    "development_start_date": development["date"].iloc[0],
                    "development_end_date": development["date"].iloc[-1],
                    "final_train_start_date": final_train["date"].iloc[0],
                    "final_train_end_date": final_train["date"].iloc[-1],
                    "test_start_date": test["date"].iloc[0],
                    "test_end_date": test["date"].iloc[-1],
                    "scored_test_start_date": scored_test["date"].iloc[0],
                    "scored_test_end_date": scored_test["date"].iloc[-1],
                }
            )

    protocol = pd.DataFrame(rows)
    date_columns = [column for column in protocol if column.endswith("_date")]
    for column in date_columns:
        protocol[column] = pd.to_datetime(protocol[column])
    return protocol


def _build_temporal_split_figure(
    selections: pd.DataFrame,
    protocol: pd.DataFrame,
    output_path: Path,
) -> None:
    """Plot the full case-study chronology and its nonstandard temporal split."""

    series_order = selections["series"].tolist()
    fig, axes = plt.subplots(
        len(series_order),
        1,
        figsize=(12.0, max(4.0, 2.25 * len(series_order))),
        squeeze=False,
    )

    for row_idx, key in enumerate(series_order):
        ax = axes[row_idx, 0]
        selection = selections.loc[selections["series"].eq(key)].iloc[0]
        case_protocol = protocol.loc[protocol["series"].eq(key)].copy()
        frame = _load_series(key)

        development_start = pd.Timestamp(
            case_protocol["development_start_date"].iloc[0]
        )
        development_end = pd.Timestamp(
            case_protocol["development_end_date"].iloc[0]
        )
        final_train_start = pd.Timestamp(
            case_protocol["final_train_start_date"].iloc[0]
        )
        final_train_end = pd.Timestamp(
            case_protocol["final_train_end_date"].iloc[0]
        )
        test_start = pd.Timestamp(case_protocol["test_start_date"].iloc[0])
        test_end = pd.Timestamp(case_protocol["test_end_date"].iloc[0])

        ax.axvspan(
            development_start,
            development_end,
            color="#dbeafe",
            alpha=0.35,
            label="Development region",
            zorder=0,
        )
        ax.axvspan(
            final_train_start,
            final_train_end,
            color="#60a5fa",
            alpha=0.38,
            label=f"Final training window (L={int(selection['window'])})",
            zorder=1,
        )
        ax.axvspan(
            test_start,
            test_end,
            color="#fecaca",
            alpha=0.45,
            label="Untouched test reserve",
            zorder=0,
        )

        # Validation is not one fixed block.  Draw every future block only in a
        # narrow protocol strip at the bottom and mark its forecast origin.
        for _, split in case_protocol.iterrows():
            ax.axvspan(
                pd.Timestamp(split["validation_start_date"]),
                pd.Timestamp(split["validation_end_date"]),
                ymin=0.0,
                ymax=0.075,
                color="#1d4ed8",
                alpha=0.12,
                zorder=2,
            )

        origin_dates = pd.to_datetime(
            case_protocol["validation_start_date"]
        ).drop_duplicates()
        ax.scatter(
            mdates.date2num(origin_dates),
            np.full(len(origin_dates), 0.038),
            marker="|",
            s=55,
            color="#1d4ed8",
            transform=ax.get_xaxis_transform(),
            label=f"Rolling validation origins (n={len(origin_dates)})",
            zorder=5,
        )

        ax.plot(
            pd.to_datetime(frame["date"]),
            frame["value"],
            color="#3f3f46",
            linewidth=1.0,
            label="Observed series",
            zorder=4,
        )
        ax.axvline(
            test_start,
            color="#991b1b",
            linewidth=0.9,
            linestyle="--",
            zorder=3,
        )

        ax.set_title(
            f"{SERIES[key]['family']}: selected "
            f"d={int(selection['order'])}, "
            f"L={int(selection['window'])}, "
            f"h={int(selection['horizon'])}"
        )
        ax.set_ylabel("Level")
        ax.grid(alpha=0.18)
        locator = mdates.AutoDateLocator()
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))

        if row_idx == 0:
            ax.legend(
                frameon=False,
                fontsize=7.2,
                ncol=3,
                loc="upper left",
            )

    axes[-1, 0].set_xlabel("Date")
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def _write_applied_figures(
    run_dir: Path,
    selections: pd.DataFrame,
    candidates: pd.DataFrame,
    profiles: pd.DataFrame,
    paths: pd.DataFrame,
) -> None:
    _build_figure(
        selections,
        candidates,
        profiles,
        paths,
        run_dir / "applied_case_studies.pdf",
    )
    protocol = _temporal_protocol(selections)
    protocol.to_csv(run_dir / "temporal_split_protocol.csv", index=False)
    _build_temporal_split_figure(
        selections,
        protocol,
        run_dir / "temporal_split.pdf",
    )


def _replot_existing_run(run_dir: Path) -> None:
    required = {
        "case_selection.csv",
        "candidate_results.csv",
        "objective_profiles.csv",
        "applied_paths.csv",
    }
    missing = sorted(name for name in required if not (run_dir / name).exists())
    if missing:
        raise FileNotFoundError(
            f"Cannot replot {run_dir}; missing: {', '.join(missing)}"
        )

    selections = pd.read_csv(run_dir / "case_selection.csv")
    candidates = pd.read_csv(run_dir / "candidate_results.csv")
    profiles = pd.read_csv(run_dir / "objective_profiles.csv")
    paths = pd.read_csv(run_dir / "applied_paths.csv")
    _write_applied_figures(
        run_dir,
        selections,
        candidates,
        profiles,
        paths,
    )


def _build_figure(
    selections: pd.DataFrame,
    candidates: pd.DataFrame,
    profiles: pd.DataFrame,
    paths: pd.DataFrame,
    output_path: Path,
) -> None:
    series_order = selections["series"].tolist()
    n_rows = len(series_order)
    fig, axes = plt.subplots(
        n_rows,
        3,
        figsize=(12.0, max(3.0, 2.9 * n_rows)),
        squeeze=False,
    )

    for row_idx, key in enumerate(series_order):
        selection = selections.loc[selections["series"].eq(key)].iloc[0]
        case_candidates = candidates.loc[candidates["series"].eq(key)].copy()
        profile = profiles.loc[profiles["series"].eq(key)]
        case_paths = paths.loc[paths["series"].eq(key)].copy()

        ax = axes[row_idx, 0]
        ax.plot(profile["smoothness"], profile["cv_error"], linewidth=1.2)
        for _, candidate in case_candidates.iterrows():
            ax.scatter(candidate["smoothness"], candidate["cv_error"], s=35)
            ax.annotate(
                f"CV-{int(candidate['cv_rank'])}",
                (candidate["smoothness"], candidate["cv_error"]),
                xytext=(4, 4),
                textcoords="offset points",
                fontsize=8,
            )
        ax.set_xlim(0.0, 1.0)
        ax.set_xlabel("Normalized smoothness $S$")
        ax.set_ylabel("Rolling CV MSE")
        ax.set_title(
            f"{SERIES[key]['family']}: d={int(selection['order'])}, "
            f"L={int(selection['window'])}, h={int(selection['horizon'])}"
        )
        ax.grid(alpha=0.2)

        ax = axes[row_idx, 1]
        first_rank = int(case_candidates["cv_rank"].min())
        observed_train = case_paths.loc[
            (case_paths["segment"].eq("train"))
            & (case_paths["cv_rank"].eq(first_rank))
        ]
        ax.plot(
            pd.to_datetime(observed_train["date"]),
            observed_train["observed"],
            linewidth=1.0,
            label="Observed",
        )
        for _, candidate in case_candidates.iterrows():
            candidate_train = case_paths.loc[
                (case_paths["segment"].eq("train"))
                & (case_paths["cv_rank"].eq(int(candidate["cv_rank"])))
            ]
            ax.plot(
                pd.to_datetime(candidate_train["date"]),
                candidate_train["candidate_path"],
                linewidth=1.3,
                label=f"CV-{int(candidate['cv_rank'])}",
            )
        ax.set_title("Same data, different CV minima")
        ax.set_ylabel("Level")
        ax.legend(frameon=False, fontsize=7)
        ax.grid(alpha=0.2)

        ax = axes[row_idx, 2]
        train_tail_n = min(60, int(selection["window"]))
        observed_tail = observed_train.tail(train_tail_n)
        ax.plot(
            pd.to_datetime(observed_tail["date"]),
            observed_tail["observed"],
            linewidth=1.0,
            label="Observed train",
        )
        first_test = case_paths.loc[
            (case_paths["segment"].eq("test"))
            & (case_paths["cv_rank"].eq(first_rank))
        ]
        ax.plot(
            pd.to_datetime(first_test["date"]),
            first_test["observed"],
            marker="o",
            markersize=2.5,
            linewidth=1.0,
            label="Untouched test",
        )
        for _, candidate in case_candidates.iterrows():
            rank = int(candidate["cv_rank"])
            candidate_test = case_paths.loc[
                (case_paths["segment"].eq("test"))
                & (case_paths["cv_rank"].eq(rank))
            ]
            test_rank = int(candidate["test_rank"])
            ax.plot(
                pd.to_datetime(candidate_test["date"]),
                candidate_test["candidate_path"],
                linewidth=1.3,
                label=f"CV-{rank} / test-{test_rank}",
            )
        reversal = bool(case_candidates["validation_test_rank_reversal"].iloc[0])
        ax.set_title(
            "Forecast vs untouched test"
            + (" — rank reversal" if reversal else "")
        )
        ax.legend(frameon=False, fontsize=6.8)
        ax.grid(alpha=0.2)

        for panel in axes[row_idx, 1:]:
            panel.xaxis.set_major_locator(mdates.AutoDateLocator())
            panel.xaxis.set_major_formatter(
                mdates.ConciseDateFormatter(panel.xaxis.get_major_locator())
            )

    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = parse_args()

    if args.figures_from_run is not None:
        run_dir = Path(args.figures_from_run)
        _replot_existing_run(run_dir)
        print(
            f"Regenerated applied figures from frozen results in {run_dir}",
            flush=True,
        )
        return

    preset = PRESETS[args.preset]
    profile_grid_size = int(
        args.profile_grid_size
        if args.profile_grid_size is not None
        else preset["profile_grid_size"]
    )
    if profile_grid_size < 51:
        raise ValueError("profile-grid-size must be at least 51.")

    run_dir = args.output_dir or _default_run_directory(args.preset)
    run_dir.mkdir(parents=True, exist_ok=True)

    selection_rows: list[dict] = []
    scan_frames: list[pd.DataFrame] = []
    candidate_frames: list[pd.DataFrame] = []
    profile_frames: list[pd.DataFrame] = []
    path_frames: list[pd.DataFrame] = []
    snapshot_meta: dict[str, dict] = {}

    started = time.perf_counter()

    for index, key in enumerate(preset["series"], start=1):
        spec = SERIES[key]
        frame = _load_series(key)
        test_reserve = int(spec["test_reserve"])
        development = frame.iloc[:-test_reserve].copy()
        test = frame.iloc[-test_reserve:].copy()
        development_log = np.log(development["value"].to_numpy(dtype=float))

        print(
            f"[{index}/{len(preset['series'])}] {key}: "
            f"development={len(development)} test_reserve={len(test)}",
            flush=True,
        )

        scan, payload = _scan_configurations(
            key,
            development_log,
            preset=preset,
        )
        selected = scan.loc[scan["selected"]].iloc[0]
        order = int(selected["order"])
        window = int(selected["window"])
        horizon = int(selected["horizon"])
        candidates = payload["candidates"]

        candidate_result, path_result = _evaluate_frozen_candidates(
            key,
            frame,
            development,
            test,
            order=order,
            window=window,
            horizon=horizon,
            candidates=candidates,
        )
        profile = _objective_profile(
            key,
            payload["prepared"],
            payload["search"],
            order=order,
            window=window,
            horizon=horizon,
            grid_size=profile_grid_size,
        )

        reversal = bool(candidate_result["validation_test_rank_reversal"].iloc[0])
        test_best_rank = int(
            candidate_result.loc[
                candidate_result["test_rank"].eq(1),
                "cv_rank",
            ].iloc[0]
        )

        selection_rows.append(
            {
                "series": key,
                "label": spec["label"],
                "family": spec["family"],
                "asset_class": spec["asset_class"],
                "order": order,
                "window": window,
                "horizon": horizon,
                "n_representative_candidates": len(candidates),
                "selection_score": float(selected["selection_score"]),
                "cv_selected_s": float(candidate_result.iloc[0]["smoothness"]),
                "test_best_cv_rank": test_best_rank,
                "validation_test_rank_reversal": reversal,
                "development_start_date": str(development["date"].iloc[0].date()),
                "development_end_date": str(development["date"].iloc[-1].date()),
                "test_start_date": str(test["date"].iloc[0].date()),
                "test_end_date": str(test["date"].iloc[-1].date()),
                "test_reserve": test_reserve,
            }
        )

        scan_frames.append(scan)
        candidate_frames.append(candidate_result)
        profile_frames.append(profile)
        path_frames.append(path_result)

        path = Path(spec["path"])
        snapshot_meta[key] = {
            "path": str(path).replace("\\", "/"),
            "sha256": _sha256(path),
            "rows_loaded": int(len(frame)),
            "development_rows": int(len(development)),
            "test_reserve_rows": int(len(test)),
        }

        print(
            f"    selected d={order} L={window} h={horizon}; "
            f"candidates={len(candidates)}; "
            f"rank_reversal={reversal}",
            flush=True,
        )

    selections = pd.DataFrame(selection_rows)
    scans = pd.concat(scan_frames, ignore_index=True)
    candidates = pd.concat(candidate_frames, ignore_index=True)
    profiles = pd.concat(profile_frames, ignore_index=True)
    paths = pd.concat(path_frames, ignore_index=True)

    selections.to_csv(run_dir / "case_selection.csv", index=False)
    scans.to_csv(run_dir / "configuration_scan.csv", index=False)
    candidates.to_csv(run_dir / "candidate_results.csv", index=False)
    profiles.to_csv(run_dir / "objective_profiles.csv", index=False)
    paths.to_csv(run_dir / "applied_paths.csv", index=False)

    _write_applied_figures(
        run_dir,
        selections,
        candidates,
        profiles,
        paths,
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "suite": "applied_multiple_minima",
        "preset": args.preset,
        "series": list(preset["series"]),
        "data_policy": "tracked_snapshot_only",
        "transform": "natural_log_level",
        "selection_uses_test": False,
        "test_role": "diagnostic_only",
        "candidate_spacing_epsilon": CANDIDATE_SPACING_EPSILON,
        "max_candidates": MAX_CANDIDATES,
        "boundary_probe": BOUNDARY_PROBE,
        "frozen_search": FROZEN_SEARCH,
        "selection_rule": (
            "Among development-only configurations with at least two "
            "epsilon-separated candidates, maximize the smoothness separation "
            "between the two lowest-CV candidates; break ties by ascending "
            "(d,L,h). If no configuration has two candidates, fall back to "
            "the largest candidate count with the same deterministic tie rule."
        ),
        "test_protocol": (
            "Reserve the final max-horizon block before configuration search. "
            "After the development-only candidate set is frozen, refit each "
            "candidate at the development endpoint and score the first h "
            "observations of the untouched test block."
        ),
        "profile_grid_size": profile_grid_size,
        "snapshot": snapshot_meta,
        "elapsed_seconds": time.perf_counter() - started,
    }
    (run_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    print(
        f"Wrote applied case studies to {run_dir}; "
        f"rank reversals={int(selections['validation_test_rank_reversal'].sum())}/"
        f"{len(selections)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
