from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd

import trend_estimation as td

import run_applied_case_studies as applied


RESULT_ROOT = Path("results") / "numerical_smoothness_selection"
ORDERS = (1, 2, 3, 4)

# Matplotlib-compatible colors from the familiar "deep" palette.
OBSERVED_COLOR = "#4C72B0"
ORDER_COLORS = {
    1: "#C44E52",  # red
    2: "#55A868",  # green
    3: "#8172B3",  # purple
    4: "#DD8452",  # orange
}

PRESETS = {
    "smoke": {
        "series": ("GDPC1",),
        "windows": {"GDPC1": (40,)},
        "max_origins_override": 6,
    },
    "paper": {
        "series": ("GDPC1", "SPY", "AAPL", "BTC-USD"),
        "windows": {},
        "max_origins_override": None,
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Track local smoothness minima through nearby rolling windows. "
            "At each origin, Validation 1 defines the smoothness objective; "
            "its local minima are continued from the previous origin in a "
            "small S-neighborhood. Each tracked minimum is then refit through "
            "Validation 1 and scored on the immediately following Validation 2 "
            "block. Historical Validation-2 scores select a persistent branch; "
            "the final untouched test is diagnostic only."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="paper")
    parser.add_argument(
        "--selection-metric",
        choices=("level_rmse", "log_rmse"),
        default="level_rmse",
        help="Historical Validation-2 metric used to select a tracked branch.",
    )
    parser.add_argument(
        "--max-minima",
        type=int,
        default=5,
        help="Maximum number of local-minimum branches initialized per order.",
    )
    parser.add_argument(
        "--track-epsilon",
        type=float,
        default=0.10,
        help=(
            "Maximum |S_t-S_(t-1)| allowed when continuing a local-minimum "
            "branch to the next rolling window."
        ),
    )
    parser.add_argument(
        "--candidate-spacing",
        type=float,
        default=0.02,
        help="Minimum S separation used to deduplicate minima on one surface.",
    )
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--dpi", type=int, default=220)
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
    return RESULT_ROOT / f"{stamp}_tracked-minima-{preset}_{_git_short_sha()}"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _windows_for(key: str, preset: dict) -> tuple[int, ...]:
    override = preset["windows"].get(key)
    if override is not None:
        return tuple(int(value) for value in override)
    return tuple(int(value) for value in applied.SERIES[key]["windows"])


def _safe_levels(log_values: np.ndarray) -> np.ndarray:
    return np.exp(np.clip(np.asarray(log_values, dtype=float), -700.0, 700.0))


def _rmse(observed: np.ndarray, predicted: np.ndarray) -> float:
    observed = np.asarray(observed, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    return float(np.sqrt(np.mean((observed - predicted) ** 2)))


def _paired_splits(
    n_obs: int,
    *,
    window: int,
    horizon: int,
    step: int,
    max_origins: int,
):
    """Return rolling splits whose Validation 1 has a full Validation 2 after it."""

    splits = td.rolling_origin_splits(
        n_obs,
        initial_train=window,
        horizon=horizon,
        step=step,
        expanding=False,
        train_window=window,
    )
    paired = [
        split
        for split in splits
        if split.validation.stop + horizon <= n_obs
    ]
    paired = paired[-max_origins:]
    if not paired:
        raise ValueError(
            f"No paired validation origins for L={window}, h={horizon}."
        )
    return paired


def _surface_candidates(
    prepared,
    *,
    order: int,
    window: int,
    spacing: float,
) -> tuple[list[dict], int]:
    """Recover distinct local minima on one Validation-1 objective surface."""

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
        **applied.FROZEN_SEARCH,
    )

    pool: list[dict] = []
    for point in result.points_:
        if point.kind_ != "minimum":
            continue
        pool.append(
            {
                "smoothness": float(point.smoothness_),
                "lambda": float(point.lambda_),
                "val1_loss": float(point.objective_),
                "source": "interior",
            }
        )

    endpoint_values = {
        0.0: float(evaluate_lambda(0.0).value),
        1.0: float(evaluate_lambda(float("inf")).value),
    }
    lower_probe = td.smoothness_to_lambda(
        applied.BOUNDARY_PROBE,
        n_obs=window,
        order=order,
    )
    upper_probe = td.smoothness_to_lambda(
        1.0 - applied.BOUNDARY_PROBE,
        n_obs=window,
        order=order,
    )
    lower_probe_value = float(evaluate_lambda(lower_probe).value)
    upper_probe_value = float(evaluate_lambda(upper_probe).value)

    if endpoint_values[0.0] <= lower_probe_value:
        pool.append(
            {
                "smoothness": 0.0,
                "lambda": 0.0,
                "val1_loss": endpoint_values[0.0],
                "source": "S=0",
            }
        )
    if endpoint_values[1.0] <= upper_probe_value:
        pool.append(
            {
                "smoothness": 1.0,
                "lambda": float("inf"),
                "val1_loss": endpoint_values[1.0],
                "source": "S=1",
            }
        )

    if not pool:
        pool = [
            {
                "smoothness": 0.0,
                "lambda": 0.0,
                "val1_loss": endpoint_values[0.0],
                "source": "S=0",
            },
            {
                "smoothness": 1.0,
                "lambda": float("inf"),
                "val1_loss": endpoint_values[1.0],
                "source": "S=1",
            },
        ]

    # Deduplicate numerical copies of the same basin, but do not collapse
    # genuinely separate minima. Keep the lower-loss representative first.
    ordered = sorted(
        pool,
        key=lambda row: (row["val1_loss"], row["smoothness"]),
    )
    distinct: list[dict] = []
    for candidate in ordered:
        if any(
            abs(candidate["smoothness"] - kept["smoothness"]) < spacing
            for kept in distinct
        ):
            continue
        distinct.append(candidate)

    distinct.sort(key=lambda row: row["smoothness"])
    return distinct, len(cache)


def _select_window_per_order(
    key: str,
    history: pd.DataFrame,
    *,
    windows: tuple[int, ...],
    max_origins: int,
) -> tuple[pd.DataFrame, dict[int, list]]:
    """Choose L per d from aggregate Validation-1 rolling loss only."""

    spec = applied.SERIES[key]
    horizon = int(spec["test_reserve"])
    history_log = np.log(history["value"].to_numpy(dtype=float))

    rows: list[dict] = []
    selected_splits: dict[int, list] = {}

    for order in ORDERS:
        order_rows: list[dict] = []
        payloads: dict[int, list] = {}

        for window in windows:
            if window + 2 * horizon > len(history_log):
                continue

            splits = _paired_splits(
                len(history_log),
                window=int(window),
                horizon=horizon,
                step=int(spec["step"]),
                max_origins=max_origins,
            )
            prepared = td.prepare_rolling_pure_forecast_objective(
                history_log,
                splits,
                order=int(order),
            )
            search, candidates, n_evaluations = applied._search_candidates(
                prepared,
                order=int(order),
                window=int(window),
            )
            best = candidates[0]
            order_rows.append(
                {
                    "series": key,
                    "family": spec["family"],
                    "order": int(order),
                    "window": int(window),
                    "horizon": horizon,
                    "aggregate_val1_loss": float(best["cv_error"]),
                    "aggregate_best_smoothness": float(best["smoothness"]),
                    "n_origins": int(len(splits)),
                    "adaptive_evaluations": int(n_evaluations),
                    "n_stationary_points": int(len(search.points_)),
                }
            )
            payloads[int(window)] = splits

        if not order_rows:
            raise RuntimeError(
                f"No valid rolling window for {key}, d={order}."
            )

        selected = (
            pd.DataFrame(order_rows)
            .sort_values(
                ["aggregate_val1_loss", "window"],
                ascending=[True, True],
            )
            .iloc[0]
            .to_dict()
        )
        rows.append(selected)
        selected_splits[int(order)] = payloads[int(selected["window"])]

    return (
        pd.DataFrame(rows).sort_values("order").reset_index(drop=True),
        selected_splits,
    )


def _match_branches(
    previous_s: dict[str, float],
    candidates: list[dict],
    *,
    epsilon: float,
) -> tuple[dict[str, tuple[int, float]], set[int]]:
    """Greedy one-to-one nearest-neighbor continuation in normalized S."""

    pairs: list[tuple[float, str, int]] = []
    for branch_id, s_prev in previous_s.items():
        for candidate_idx, candidate in enumerate(candidates):
            distance = abs(float(candidate["smoothness"]) - float(s_prev))
            pairs.append((distance, branch_id, candidate_idx))

    matches: dict[str, tuple[int, float]] = {}
    used_candidates: set[int] = set()

    for distance, branch_id, candidate_idx in sorted(pairs):
        if distance > epsilon:
            continue
        if branch_id in matches or candidate_idx in used_candidates:
            continue
        matches[branch_id] = (candidate_idx, float(distance))
        used_candidates.add(candidate_idx)

    return matches, used_candidates


def _score_validation2(
    history: pd.DataFrame,
    split,
    *,
    horizon: int,
    order: int,
    window: int,
    smoothness: float,
) -> tuple[float, float, pd.DataFrame]:
    """Refit through Validation 1, then forecast the immediately following block."""

    val2 = history.iloc[
        split.validation.stop : split.validation.stop + horizon
    ].copy()
    refit = history.iloc[: split.validation.stop].tail(window).copy()

    model = td.PurePenalizedTrend(
        order=order,
        smoothness=float(smoothness),
    ).fit(np.log(refit["value"].to_numpy(dtype=float)))
    forecast_log = np.asarray(model.forecast(horizon), dtype=float)
    forecast_level = _safe_levels(forecast_log)

    observed_level = val2["value"].to_numpy(dtype=float)
    observed_log = np.log(observed_level)
    path = val2[["date", "value"]].copy()
    path = path.rename(columns={"value": "observed"})
    path["candidate_path"] = forecast_level
    return (
        _rmse(observed_level, forecast_level),
        _rmse(observed_log, forecast_log),
        path,
    )


def _track_order_minima(
    key: str,
    history: pd.DataFrame,
    *,
    order: int,
    window: int,
    splits: list,
    max_minima: int,
    track_epsilon: float,
    candidate_spacing: float,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Initialize local minima once, then continue each branch locally in time."""

    history_log = np.log(history["value"].to_numpy(dtype=float))
    horizon = int(applied.SERIES[key]["test_reserve"])

    branch_last_s: dict[str, float] = {}
    initialized_branch_ids: list[str] = []
    rows: list[dict] = []
    validation_path_rows: list[dict] = []

    for origin_number, split in enumerate(splits, start=1):
        prepared = td.prepare_rolling_pure_forecast_objective(
            history_log,
            [split],
            order=order,
        )
        candidates, evaluations = _surface_candidates(
            prepared,
            order=order,
            window=window,
            spacing=candidate_spacing,
        )

        if origin_number == 1:
            # Maximum five starting basins, preferring lower Validation-1 loss
            # if the surface contains more than requested.
            initial = sorted(
                candidates,
                key=lambda row: (row["val1_loss"], row["smoothness"]),
            )[:max_minima]
            initial.sort(key=lambda row: row["smoothness"])

            for branch_number, candidate in enumerate(initial, start=1):
                branch_id = f"d{order}_b{branch_number}"
                initialized_branch_ids.append(branch_id)
                branch_last_s[branch_id] = float(candidate["smoothness"])

            matches = {
                branch_id: (
                    next(
                        idx
                        for idx, candidate in enumerate(candidates)
                        if abs(
                            float(candidate["smoothness"])
                            - branch_last_s[branch_id]
                        )
                        < 1e-12
                    ),
                    0.0,
                )
                for branch_id in initialized_branch_ids
            }
        else:
            matches, _ = _match_branches(
                branch_last_s,
                candidates,
                epsilon=track_epsilon,
            )

        matched_count = len(matches)
        surface_minima_count = len(candidates)
        val1_start = history["date"].iloc[split.validation.start]
        val1_end = history["date"].iloc[split.validation.stop - 1]
        val2_start = history["date"].iloc[split.validation.stop]
        val2_end = history["date"].iloc[
            split.validation.stop + horizon - 1
        ]

        for branch_id in initialized_branch_ids:
            if branch_id not in matches:
                rows.append(
                    {
                        "series": key,
                        "family": applied.SERIES[key]["family"],
                        "order": order,
                        "window": window,
                        "branch_id": branch_id,
                        "origin_number": origin_number,
                        "status": "missing_local_minimum",
                        "smoothness": np.nan,
                        "lambda": np.nan,
                        "val1_loss": np.nan,
                        "val2_level_rmse": np.nan,
                        "val2_log_rmse": np.nan,
                        "delta_s": np.nan,
                        "surface_minima_count": surface_minima_count,
                        "matched_branch_count": matched_count,
                        "objective_evaluations": evaluations,
                        "val1_start_date": val1_start,
                        "val1_end_date": val1_end,
                        "val2_start_date": val2_start,
                        "val2_end_date": val2_end,
                    }
                )
                continue

            candidate_idx, distance = matches[branch_id]
            candidate = candidates[candidate_idx]
            s = float(candidate["smoothness"])
            (
                val2_level_rmse,
                val2_log_rmse,
                val2_path,
            ) = _score_validation2(
                history,
                split,
                horizon=horizon,
                order=order,
                window=window,
                smoothness=s,
            )

            rows.append(
                {
                    "series": key,
                    "family": applied.SERIES[key]["family"],
                    "order": order,
                    "window": window,
                    "branch_id": branch_id,
                    "origin_number": origin_number,
                    "status": "matched",
                    "smoothness": s,
                    "lambda": float(candidate["lambda"]),
                    "val1_loss": float(candidate["val1_loss"]),
                    "val2_level_rmse": val2_level_rmse,
                    "val2_log_rmse": val2_log_rmse,
                    "delta_s": float(distance),
                    "surface_minima_count": surface_minima_count,
                    "matched_branch_count": matched_count,
                    "objective_evaluations": evaluations,
                    "val1_start_date": val1_start,
                    "val1_end_date": val1_end,
                    "val2_start_date": val2_start,
                    "val2_end_date": val2_end,
                }
            )
            for _, path_row in val2_path.iterrows():
                validation_path_rows.append(
                    {
                        "series": key,
                        "family": applied.SERIES[key]["family"],
                        "order": order,
                        "window": window,
                        "branch_id": branch_id,
                        "origin_number": origin_number,
                        "smoothness": s,
                        "date": path_row["date"],
                        "observed": float(path_row["observed"]),
                        "candidate_path": float(path_row["candidate_path"]),
                        "val2_level_rmse": val2_level_rmse,
                        "val2_log_rmse": val2_log_rmse,
                    }
                )

            branch_last_s[branch_id] = s

    return pd.DataFrame(rows), pd.DataFrame(validation_path_rows)


def _summarize_branches(
    tracks: pd.DataFrame,
    *,
    selection_metric: str,
) -> pd.DataFrame:
    metric_column = (
        "val2_level_rmse"
        if selection_metric == "level_rmse"
        else "val2_log_rmse"
    )
    rows: list[dict] = []

    for (series, order, branch_id), group in tracks.groupby(
        ["series", "order", "branch_id"],
        sort=False,
    ):
        matched = group.loc[group["status"].eq("matched")].sort_values(
            "origin_number"
        )
        n_possible = int(len(group))
        n_matched = int(len(matched))
        recent = matched.tail(min(5, n_matched))

        rows.append(
            {
                "series": series,
                "family": str(group["family"].iloc[0]),
                "order": int(order),
                "window": int(group["window"].iloc[0]),
                "branch_id": branch_id,
                "n_possible_origins": n_possible,
                "n_matched_origins": n_matched,
                "support_fraction": n_matched / max(n_possible, 1),
                "mean_val2_level_rmse": float(
                    matched["val2_level_rmse"].mean()
                ),
                "median_val2_level_rmse": float(
                    matched["val2_level_rmse"].median()
                ),
                "mean_val2_log_rmse": float(
                    matched["val2_log_rmse"].mean()
                ),
                "median_val2_log_rmse": float(
                    matched["val2_log_rmse"].median()
                ),
                "selection_score": float(matched[metric_column].mean()),
                "smoothness_first": float(matched["smoothness"].iloc[0]),
                "smoothness_last": float(matched["smoothness"].iloc[-1]),
                "smoothness_mean": float(matched["smoothness"].mean()),
                "smoothness_median": float(matched["smoothness"].median()),
                "smoothness_recent5_mean": float(recent["smoothness"].mean()),
                "smoothness_recent5_median": float(
                    recent["smoothness"].median()
                ),
                "max_abs_delta_s": float(
                    matched["delta_s"].fillna(0.0).max()
                ),
            }
        )

    return pd.DataFrame(rows)


def _final_validation_split(
    pretest: pd.DataFrame,
    *,
    window: int,
    horizon: int,
):
    splits = td.rolling_origin_splits(
        len(pretest),
        initial_train=len(pretest) - horizon,
        horizon=horizon,
        step=1,
        expanding=False,
        train_window=window,
    )
    exact = [
        split
        for split in splits
        if split.validation.stop == len(pretest)
    ]
    if not exact:
        raise RuntimeError(
            f"Could not construct final Validation-1 split for L={window}."
        )
    return exact[-1]


def _continue_to_final_validation(
    key: str,
    frame: pd.DataFrame,
    summaries: pd.DataFrame,
    *,
    track_epsilon: float,
    candidate_spacing: float,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Continue every historical branch once more on the final pre-test Val1."""

    spec = applied.SERIES[key]
    horizon = int(spec["test_reserve"])
    pretest = frame.iloc[:-horizon].copy()
    true_test = frame.iloc[-horizon:].copy()
    pretest_log = np.log(pretest["value"].to_numpy(dtype=float))

    result_rows: list[dict] = []
    path_rows: list[dict] = []

    for order in ORDERS:
        order_summary = summaries.loc[
            summaries["order"].eq(order)
        ].copy()
        if order_summary.empty:
            continue

        window = int(order_summary["window"].iloc[0])
        split = _final_validation_split(
            pretest,
            window=window,
            horizon=horizon,
        )
        prepared = td.prepare_rolling_pure_forecast_objective(
            pretest_log,
            [split],
            order=order,
        )
        candidates, _ = _surface_candidates(
            prepared,
            order=order,
            window=window,
            spacing=candidate_spacing,
        )
        previous = {
            str(row["branch_id"]): float(row["smoothness_last"])
            for _, row in order_summary.iterrows()
        }
        matches, _ = _match_branches(
            previous,
            candidates,
            epsilon=track_epsilon,
        )

        for _, summary in order_summary.iterrows():
            branch_id = str(summary["branch_id"])
            if branch_id not in matches:
                result_rows.append(
                    {
                        "series": key,
                        "branch_id": branch_id,
                        "order": order,
                        "final_continuation": False,
                        "final_smoothness": np.nan,
                        "final_val1_loss": np.nan,
                        "true_test_level_rmse": np.nan,
                        "true_test_log_rmse": np.nan,
                    }
                )
                continue

            candidate_idx, distance = matches[branch_id]
            candidate = candidates[candidate_idx]
            final_s = float(candidate["smoothness"])

            final_train = pretest.tail(window).copy()
            model = td.PurePenalizedTrend(
                order=order,
                smoothness=final_s,
            ).fit(np.log(final_train["value"].to_numpy(dtype=float)))
            forecast_log = np.asarray(model.forecast(horizon), dtype=float)
            forecast_level = _safe_levels(forecast_log)

            observed_level = true_test["value"].to_numpy(dtype=float)
            observed_log = np.log(observed_level)

            result_rows.append(
                {
                    "series": key,
                    "branch_id": branch_id,
                    "order": order,
                    "final_continuation": True,
                    "final_smoothness": final_s,
                    "final_delta_s": float(distance),
                    "final_val1_loss": float(candidate["val1_loss"]),
                    "true_test_level_rmse": _rmse(
                        observed_level,
                        forecast_level,
                    ),
                    "true_test_log_rmse": _rmse(
                        observed_log,
                        forecast_log,
                    ),
                }
            )

            for date, observed, predicted in zip(
                true_test["date"],
                true_test["value"],
                forecast_level,
            ):
                path_rows.append(
                    {
                        "series": key,
                        "branch_id": branch_id,
                        "order": order,
                        "smoothness": final_s,
                        "date": date,
                        "observed": float(observed),
                        "candidate_path": float(predicted),
                    }
                )

    return pd.DataFrame(result_rows), pd.DataFrame(path_rows)


def _select_winner(
    summary: pd.DataFrame,
    final_results: pd.DataFrame,
) -> pd.DataFrame:
    merged = summary.merge(
        final_results,
        on=["series", "branch_id", "order"],
        how="left",
        validate="one_to_one",
    )
    merged["selected_branch"] = False

    for series, group in merged.groupby("series"):
        eligible = group.loc[group["final_continuation"].fillna(False)].copy()
        if eligible.empty:
            raise RuntimeError(
                f"No tracked branch continued to the final validation for {series}."
            )

        complete = eligible.loc[
            np.isclose(eligible["support_fraction"], 1.0)
        ].copy()
        if not complete.empty:
            pool = complete
        else:
            max_support = float(eligible["support_fraction"].max())
            pool = eligible.loc[
                np.isclose(eligible["support_fraction"], max_support)
            ].copy()

        winner_idx = pool.sort_values(
            ["selection_score", "order", "branch_id"],
            ascending=[True, True, True],
        ).index[0]
        merged.loc[winner_idx, "selected_branch"] = True

    return merged


def _padded_limits(values: pd.Series, fraction: float = 0.08) -> tuple[float, float]:
    array = values.to_numpy(dtype=float)
    array = array[np.isfinite(array)]
    low = float(np.min(array))
    high = float(np.max(array))
    span = high - low
    if span <= 0.0:
        span = max(abs(high), 1.0) * 0.10
    pad = fraction * span
    return low - pad, high + pad


def _date_axis(ax: plt.Axes) -> None:
    locator = mdates.AutoDateLocator(minticks=3, maxticks=6)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))


def _plot(
    tracks: pd.DataFrame,
    final_selection: pd.DataFrame,
    final_paths: pd.DataFrame,
    output_dir: Path,
    *,
    selection_metric: str,
    dpi: int,
) -> None:
    series_order = [
        key
        for key in ("GDPC1", "SPY", "AAPL", "BTC-USD")
        if key in set(final_selection["series"])
    ]
    fig, axes = plt.subplots(
        len(series_order),
        3,
        figsize=(15.4, max(3.6, 3.35 * len(series_order))),
        squeeze=False,
    )

    metric_column = (
        "val2_level_rmse"
        if selection_metric == "level_rmse"
        else "val2_log_rmse"
    )

    for row_idx, key in enumerate(series_order):
        ax_s, ax_loss, ax_test = axes[row_idx]
        case_tracks = tracks.loc[tracks["series"].eq(key)].copy()
        case_selection = final_selection.loc[
            final_selection["series"].eq(key)
        ].copy()
        winner = case_selection.loc[
            case_selection["selected_branch"]
        ].iloc[0]
        winner_id = str(winner["branch_id"])

        # Column 1: local minima tracked through nearby rolling windows.
        for branch_id, branch in case_tracks.groupby("branch_id"):
            branch = branch.sort_values("origin_number")
            matched = branch.loc[branch["status"].eq("matched")]
            if matched.empty:
                continue
            order = int(branch["order"].iloc[0])
            selected = branch_id == winner_id
            ax_s.plot(
                pd.to_datetime(matched["val1_start_date"]),
                matched["smoothness"],
                color=ORDER_COLORS[order],
                linewidth=2.45 if selected else 1.0,
                alpha=0.95 if selected else 0.22,
                marker="o" if selected else None,
                markersize=2.4 if selected else 0.0,
                zorder=5 if selected else 2,
            )

        ax_s.set_ylim(-0.03, 1.03)
        ax_s.set_title("Tracked local minima $S_{j,t}$")
        ax_s.set_ylabel(applied.SERIES[key]["family"], fontweight="bold")
        ax_s.set_xlabel("Validation-1 origin")

        # Column 2: each branch's out-of-sample Validation-2 score through time.
        for branch_id, branch in case_tracks.groupby("branch_id"):
            branch = branch.sort_values("origin_number")
            matched = branch.loc[branch["status"].eq("matched")]
            if matched.empty:
                continue
            order = int(branch["order"].iloc[0])
            selected = branch_id == winner_id
            ax_loss.plot(
                pd.to_datetime(matched["val2_start_date"]),
                matched[metric_column],
                color=ORDER_COLORS[order],
                linewidth=2.45 if selected else 1.0,
                alpha=0.95 if selected else 0.22,
                marker="o" if selected else None,
                markersize=2.4 if selected else 0.0,
                zorder=5 if selected else 2,
            )

        ax_loss.set_title(
            "Validation-2 RMSE by tracked minimum"
            if selection_metric == "level_rmse"
            else "Validation-2 log-RMSE by tracked minimum"
        )
        ax_loss.set_xlabel("Validation-2 origin")

        # Column 3: final untouched test. Every continuing branch is shown.
        case_paths = final_paths.loc[
            final_paths["series"].eq(key)
        ].copy()
        observed = (
            case_paths[["date", "observed"]]
            .drop_duplicates("date")
            .sort_values("date")
        )
        ax_test.plot(
            pd.to_datetime(observed["date"]),
            observed["observed"],
            color=OBSERVED_COLOR,
            linewidth=1.65,
            marker="o",
            markersize=2.2,
            alpha=0.97,
            zorder=8,
        )

        for branch_id, branch_path in case_paths.groupby("branch_id"):
            branch_meta = case_selection.loc[
                case_selection["branch_id"].eq(branch_id)
            ].iloc[0]
            order = int(branch_meta["order"])
            selected = branch_id == winner_id
            branch_path = branch_path.sort_values("date")
            ax_test.plot(
                pd.to_datetime(branch_path["date"]),
                branch_path["candidate_path"],
                color=ORDER_COLORS[order],
                linewidth=2.55 if selected else 1.0,
                alpha=0.95 if selected else 0.18,
                zorder=5 if selected else 2,
            )

        ax_test.set_ylim(*_padded_limits(observed["observed"]))
        ax_test.set_title(
            f"Untouched test; selected {winner_id}, "
            f"S={float(winner['final_smoothness']):.3f}"
        )

        for ax in (ax_s, ax_loss, ax_test):
            ax.grid(alpha=0.16)
            _date_axis(ax)

    handles = [
        Line2D(
            [0],
            [0],
            color=OBSERVED_COLOR,
            linewidth=2.2,
            label="Observed",
        ),
        *[
            Line2D(
                [0],
                [0],
                color=ORDER_COLORS[order],
                linewidth=2.0,
                alpha=0.80,
                label=f"d={order}",
            )
            for order in ORDERS
        ],
        Line2D(
            [0],
            [0],
            color="0.15",
            linewidth=2.5,
            alpha=0.95,
            label="Selected persistent branch",
        ),
        Line2D(
            [0],
            [0],
            color="0.45",
            linewidth=1.0,
            alpha=0.22,
            label="Other tracked minima",
        ),
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.987),
        ncol=7,
        frameon=False,
        fontsize=8.1,
    )
    fig.suptitle(
        "Local-minimum tracking: Validation 1 → Validation 2 → true test",
        y=0.998,
        fontsize=14,
    )
    fig.tight_layout(rect=[0.02, 0.02, 0.98, 0.955])

    fig.savefig(
        output_dir / "tracked_minima_validation.png",
        dpi=dpi,
        bbox_inches="tight",
    )
    fig.savefig(
        output_dir / "tracked_minima_validation.pdf",
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    args = parse_args()
    if args.max_minima < 1 or args.max_minima > 5:
        raise ValueError("--max-minima must be between 1 and 5.")
    if not 0.0 < args.track_epsilon <= 1.0:
        raise ValueError("--track-epsilon must be in (0, 1].")
    if not 0.0 < args.candidate_spacing <= 1.0:
        raise ValueError("--candidate-spacing must be in (0, 1].")

    preset = PRESETS[args.preset]
    output_dir = (
        args.output_dir
        if args.output_dir is not None
        else _default_run_directory(args.preset)
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    started = time.perf_counter()
    window_frames: list[pd.DataFrame] = []
    track_frames: list[pd.DataFrame] = []
    validation_path_frames: list[pd.DataFrame] = []
    selection_frames: list[pd.DataFrame] = []
    path_frames: list[pd.DataFrame] = []
    snapshot_meta: dict[str, dict] = {}

    for key in preset["series"]:
        spec = applied.SERIES[key]
        frame = applied._load_series(key)
        horizon = int(spec["test_reserve"])

        if len(frame) <= 3 * horizon:
            raise RuntimeError(
                f"{key} does not have enough observations for repeated "
                "Validation-1/Validation-2 pairs, final Validation 1, and test."
            )

        # The last H observations are the true test. The H observations before
        # that are the final Validation-1 block used only to update the already
        # selected branch to its newest nearby local minimum. All historical
        # branch scoring happens strictly before those two blocks.
        history = frame.iloc[: -2 * horizon].copy()

        max_origins = (
            int(preset["max_origins_override"])
            if preset["max_origins_override"] is not None
            else int(spec["max_origins"])
        )
        window_selection, splits_by_order = _select_window_per_order(
            key,
            history,
            windows=_windows_for(key, preset),
            max_origins=max_origins,
        )
        window_frames.append(window_selection)

        series_tracks: list[pd.DataFrame] = []
        for _, selected in window_selection.iterrows():
            order = int(selected["order"])
            track, validation_paths = _track_order_minima(
                key,
                history,
                order=order,
                window=int(selected["window"]),
                splits=splits_by_order[order],
                max_minima=int(args.max_minima),
                track_epsilon=float(args.track_epsilon),
                candidate_spacing=float(args.candidate_spacing),
            )
            series_tracks.append(track)
            if not validation_paths.empty:
                validation_path_frames.append(validation_paths)

        tracks = pd.concat(series_tracks, ignore_index=True)
        summary = _summarize_branches(
            tracks,
            selection_metric=args.selection_metric,
        )
        final_results, final_paths = _continue_to_final_validation(
            key,
            frame,
            summary,
            track_epsilon=float(args.track_epsilon),
            candidate_spacing=float(args.candidate_spacing),
        )
        final_selection = _select_winner(summary, final_results)

        track_frames.append(tracks)
        selection_frames.append(final_selection)
        path_frames.append(final_paths)

        snapshot_path = Path(spec["path"])
        snapshot_meta[key] = {
            "path": str(snapshot_path),
            "sha256": _sha256(snapshot_path),
            "rows_loaded": int(len(frame)),
            "historical_tracking_rows": int(len(history)),
            "final_validation1_rows": horizon,
            "true_test_rows": horizon,
            "max_origins": max_origins,
        }

    windows = pd.concat(window_frames, ignore_index=True)
    tracks = pd.concat(track_frames, ignore_index=True)
    validation_paths = (
        pd.concat(validation_path_frames, ignore_index=True)
        if validation_path_frames
        else pd.DataFrame()
    )
    final_selection = pd.concat(selection_frames, ignore_index=True)
    final_paths = pd.concat(path_frames, ignore_index=True)

    windows.to_csv(output_dir / "order_window_selection.csv", index=False)
    tracks.to_csv(output_dir / "rolling_minimum_tracks.csv", index=False)
    validation_paths.to_csv(
        output_dir / "rolling_validation_paths.csv",
        index=False,
    )
    final_selection.to_csv(
        output_dir / "tracked_branch_selection.csv",
        index=False,
    )
    final_paths.to_csv(
        output_dir / "tracked_branch_test_paths.csv",
        index=False,
    )

    _plot(
        tracks,
        final_selection,
        final_paths,
        output_dir,
        selection_metric=args.selection_metric,
        dpi=int(args.dpi),
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "suite": "tracked_local_minima_two_validation",
        "preset": args.preset,
        "series": list(preset["series"]),
        "selection_metric": args.selection_metric,
        "selection_uses_true_test": False,
        "max_minima": int(args.max_minima),
        "track_epsilon": float(args.track_epsilon),
        "candidate_spacing": float(args.candidate_spacing),
        "protocol": {
            "window_selection": (
                "For each d, choose L from aggregate rolling Validation-1 loss "
                "inside the historical tracking region only."
            ),
            "first_origin": (
                "Find up to five distinct local minima of the Validation-1 "
                "smoothness objective and initialize one branch per minimum."
            ),
            "continuation": (
                "Move the rolling window by the series step. Recompute the "
                "Validation-1 objective and match each existing branch one-to-one "
                "to a new local minimum within track_epsilon in normalized S."
            ),
            "validation_2": (
                "For every matched minimum, refit through Validation 1 with the "
                "same d, L, S and score the immediately following Validation-2 "
                "block. Store both the score and full forecast path for that "
                "branch and repeat."
            ),
            "branch_selection": (
                "Select among persistent branches using mean historical "
                "Validation-2 loss. If complete-support branches exist, only "
                "they are eligible; otherwise use the branches with maximum "
                "support. The true test is not used."
            ),
            "final_update": (
                "Before the true test, continue every branch one final time on "
                "the reserved pre-test Validation-1 block. The selected branch "
                "uses that newest nearby local minimum S for the final refit."
            ),
            "true_test": (
                "The last reserve is untouched until branch selection and final "
                "local-minimum continuation are complete. Test scores are "
                "diagnostic only."
            ),
        },
        "snapshot": snapshot_meta,
        "elapsed_seconds": time.perf_counter() - started,
    }
    (output_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    print(f"Wrote: {output_dir}")
    for key in preset["series"]:
        winner = final_selection.loc[
            final_selection["series"].eq(key)
            & final_selection["selected_branch"]
        ].iloc[0]
        print(
            f"{key}: selected {winner['branch_id']} "
            f"(d={int(winner['order'])}, "
            f"L={int(winner['window'])}, "
            f"historical mean Val2={float(winner['selection_score']):.6g}, "
            f"support={int(winner['n_matched_origins'])}/"
            f"{int(winner['n_possible_origins'])}, "
            f"final S={float(winner['final_smoothness']):.6f})"
        )


if __name__ == "__main__":
    main()
