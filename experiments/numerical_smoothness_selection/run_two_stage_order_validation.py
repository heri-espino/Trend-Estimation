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
from matplotlib.colors import to_rgb
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd

import trend_estimation as td

import run_applied_case_studies as applied


RESULT_ROOT = Path("results") / "numerical_smoothness_selection"
ORDERS = (1, 2, 3, 4)
MODE_EPSILON = 0.10

# Matplotlib-compatible colors matching the familiar "deep" palette.
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
        "windows": {
            "GDPC1": (40,),
        },
    },
    "paper": {
        "series": ("GDPC1", "SPY", "AAPL", "BTC-USD"),
        "windows": {},
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Exploratory two-stage order/smoothness selection. Stage 1 first "
            "chooses L per order from aggregate rolling forecast CV, then "
            "recovers the local smoothness minima preferred at each rolling "
            "origin. Nearby S values are grouped into recurring modes. Stage 2 "
            "scores every mode on a contiguous pseudo-test validation block. "
            "Only after that is the winning (d, mode) refit and evaluated on "
            "the untouched final test."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="paper")
    parser.add_argument(
        "--selection-metric",
        choices=("level_rmse", "log_rmse"),
        default="level_rmse",
        help="Metric used on Validation 2 to choose the final candidate.",
    )
    parser.add_argument(
        "--mode-representative",
        choices=("median", "mean"),
        default="median",
        help=(
            "Representative S used for each recurring rolling-origin mode. "
            "Median is safer when a mode contains skewed or boundary values."
        ),
    )
    parser.add_argument(
        "--mode-epsilon",
        type=float,
        default=MODE_EPSILON,
        help="Maximum gap in normalized smoothness used to group nearby minima.",
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
    return RESULT_ROOT / f"{stamp}_two-stage-order-{preset}_{_git_short_sha()}"


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


def _fit_and_forecast(
    train: pd.DataFrame,
    future: pd.DataFrame,
    *,
    order: int,
    window: int,
    smoothness: float,
) -> tuple[pd.DataFrame, np.ndarray]:
    fit_train = train.tail(window).copy()
    train_log = np.log(fit_train["value"].to_numpy(dtype=float))
    model = td.PurePenalizedTrend(
        order=int(order),
        smoothness=float(smoothness),
    ).fit(train_log)
    fitted_level = _safe_levels(np.asarray(model.trend_, dtype=float))
    forecast_log = np.asarray(model.forecast(len(future)), dtype=float)
    forecast_level = _safe_levels(forecast_log)

    fitted = fit_train[["date", "value"]].copy()
    fitted["candidate_path"] = fitted_level
    return fitted, forecast_level


def _choose_window_per_order(
    key: str,
    inner_development: pd.DataFrame,
    *,
    windows: tuple[int, ...],
) -> tuple[pd.DataFrame, dict[int, list]]:
    """Choose L for each order using the ordinary aggregate rolling-CV objective."""

    spec = applied.SERIES[key]
    horizon = int(spec["test_reserve"])
    inner_log = np.log(inner_development["value"].to_numpy(dtype=float))

    selected_rows: list[dict] = []
    selected_splits: dict[int, list] = {}

    for order in ORDERS:
        rows: list[dict] = []
        payloads: dict[int, list] = {}

        for window in windows:
            if window + horizon > len(inner_log):
                continue

            prepared, splits = applied._make_prepared_objective(
                inner_log,
                order=int(order),
                window=int(window),
                horizon=horizon,
                step=int(spec["step"]),
                max_origins=int(spec["max_origins"]),
            )
            search, candidates, n_evaluations = applied._search_candidates(
                prepared,
                order=int(order),
                window=int(window),
            )
            best = candidates[0]
            rows.append(
                {
                    "series": key,
                    "family": spec["family"],
                    "order": int(order),
                    "window": int(window),
                    "horizon": horizon,
                    "aggregate_cv_error": float(best["cv_error"]),
                    "aggregate_best_smoothness": float(best["smoothness"]),
                    "aggregate_best_source": str(best["source"]),
                    "n_rolling_origins": int(len(splits)),
                    "adaptive_evaluations": int(n_evaluations),
                    "n_stationary_points": int(len(search.points_)),
                    "n_representative_candidates": int(len(candidates)),
                }
            )
            payloads[int(window)] = splits

        if not rows:
            raise RuntimeError(
                f"No valid Stage-1 window configuration for {key}, d={order}."
            )

        selected = (
            pd.DataFrame(rows)
            .sort_values(
                ["aggregate_cv_error", "window"],
                ascending=[True, True],
            )
            .iloc[0]
            .to_dict()
        )
        selected_rows.append(selected)
        selected_splits[int(order)] = payloads[int(selected["window"])]

    return (
        pd.DataFrame(selected_rows).sort_values("order").reset_index(drop=True),
        selected_splits,
    )


def _rolling_origin_minima(
    key: str,
    inner_development: pd.DataFrame,
    window_selection: pd.DataFrame,
    splits_by_order: dict[int, list],
) -> pd.DataFrame:
    """Recover all representative local minima for each individual rolling origin."""

    inner_log = np.log(inner_development["value"].to_numpy(dtype=float))
    rows: list[dict] = []

    for _, selected in window_selection.iterrows():
        order = int(selected["order"])
        window = int(selected["window"])
        splits = splits_by_order[order]

        for origin_number, split in enumerate(splits, start=1):
            prepared = td.prepare_rolling_pure_forecast_objective(
                inner_log,
                [split],
                order=order,
            )
            _, candidates, _ = applied._search_candidates(
                prepared,
                order=order,
                window=window,
            )

            validation_start = inner_development["date"].iloc[
                split.validation.start
            ]
            validation_end = inner_development["date"].iloc[
                split.validation.stop - 1
            ]

            for candidate in candidates:
                rows.append(
                    {
                        "series": key,
                        "family": applied.SERIES[key]["family"],
                        "order": order,
                        "window": window,
                        "origin_number": origin_number,
                        "validation_start_date": validation_start,
                        "validation_end_date": validation_end,
                        "origin_cv_rank": int(candidate["cv_rank"]),
                        "smoothness": float(candidate["smoothness"]),
                        "lambda": float(candidate["lambda"]),
                        "origin_cv_error": float(candidate["cv_error"]),
                        "source": str(candidate["source"]),
                    }
                )

    minima = pd.DataFrame(rows)
    if minima.empty:
        raise RuntimeError(f"No rolling-origin minima recovered for {key}.")
    return minima


def _cluster_order_minima(
    order_minima: pd.DataFrame,
    *,
    epsilon: float,
    representative: str,
) -> pd.DataFrame:
    """Group nearby S values into recurring one-dimensional modes."""

    if order_minima.empty:
        return pd.DataFrame()

    values = (
        order_minima.sort_values(
            ["smoothness", "origin_number", "origin_cv_rank"]
        )
        .reset_index(drop=True)
    )

    clusters: list[list[int]] = []
    current: list[int] = []

    for idx, row in values.iterrows():
        s = float(row["smoothness"])
        if not current:
            current = [idx]
            continue

        current_values = values.loc[current, "smoothness"].to_numpy(dtype=float)
        center = float(np.median(current_values))
        if abs(s - center) <= epsilon:
            current.append(idx)
        else:
            clusters.append(current)
            current = [idx]

    if current:
        clusters.append(current)

    rows: list[dict] = []
    n_origins = int(order_minima["origin_number"].nunique())

    for raw_cluster_id, indices in enumerate(clusters, start=1):
        cluster = values.loc[indices].copy()
        s_values = cluster["smoothness"].to_numpy(dtype=float)

        # An origin can contribute more than one nearby minimum. Support counts
        # distinct rolling origins, while point_count preserves the raw amount.
        support = int(cluster["origin_number"].nunique())
        s_mean = float(np.mean(s_values))
        s_median = float(np.median(s_values))
        s_used = s_median if representative == "median" else s_mean

        rows.append(
            {
                "series": str(cluster["series"].iloc[0]),
                "family": str(cluster["family"].iloc[0]),
                "order": int(cluster["order"].iloc[0]),
                "window": int(cluster["window"].iloc[0]),
                "raw_mode_id": raw_cluster_id,
                "origin_support": support,
                "origin_support_fraction": support / max(n_origins, 1),
                "point_count": int(len(cluster)),
                "smoothness_min": float(np.min(s_values)),
                "smoothness_max": float(np.max(s_values)),
                "smoothness_mean": s_mean,
                "smoothness_median": s_median,
                "smoothness_used": float(s_used),
                "mean_origin_cv_error": float(cluster["origin_cv_error"].mean()),
                "median_origin_cv_error": float(
                    cluster["origin_cv_error"].median()
                ),
            }
        )

    modes = pd.DataFrame(rows)
    modes = modes.sort_values(
        [
            "origin_support",
            "mean_origin_cv_error",
            "smoothness_used",
        ],
        ascending=[False, True, True],
    ).reset_index(drop=True)
    modes["mode_rank_within_order"] = np.arange(1, len(modes) + 1)
    modes["mode_id"] = [
        f"d{int(row.order)}_m{int(row.mode_rank_within_order)}"
        for row in modes.itertuples()
    ]
    return modes


def _build_modes(
    minima: pd.DataFrame,
    *,
    epsilon: float,
    representative: str,
) -> pd.DataFrame:
    frames = []
    for order in ORDERS:
        order_minima = minima.loc[minima["order"].eq(order)].copy()
        modes = _cluster_order_minima(
            order_minima,
            epsilon=epsilon,
            representative=representative,
        )
        if modes.empty:
            raise RuntimeError(f"No smoothness modes recovered for d={order}.")
        frames.append(modes)
    return pd.concat(frames, ignore_index=True)


def _evaluate_validation2(
    key: str,
    inner_development: pd.DataFrame,
    validation2: pd.DataFrame,
    modes: pd.DataFrame,
    *,
    selection_metric: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows: list[dict] = []
    path_rows: list[dict] = []

    validation_level = validation2["value"].to_numpy(dtype=float)
    validation_log = np.log(validation_level)

    for _, mode in modes.iterrows():
        order = int(mode["order"])
        window = int(mode["window"])
        smoothness = float(mode["smoothness_used"])

        fitted, forecast_level = _fit_and_forecast(
            inner_development,
            validation2,
            order=order,
            window=window,
            smoothness=smoothness,
        )
        forecast_log = np.log(np.clip(forecast_level, 1e-300, None))

        rows.append(
            {
                **mode.to_dict(),
                "validation2_level_rmse": _rmse(
                    validation_level,
                    forecast_level,
                ),
                "validation2_log_rmse": _rmse(
                    validation_log,
                    forecast_log,
                ),
            }
        )

        for date, observed, predicted in zip(
            fitted["date"],
            fitted["value"],
            fitted["candidate_path"],
        ):
            path_rows.append(
                {
                    "series": key,
                    "mode_id": str(mode["mode_id"]),
                    "order": order,
                    "window": window,
                    "smoothness": smoothness,
                    "segment": "inner_train",
                    "date": date,
                    "observed": float(observed),
                    "candidate_path": float(predicted),
                }
            )

        for date, observed, predicted in zip(
            validation2["date"],
            validation2["value"],
            forecast_level,
        ):
            path_rows.append(
                {
                    "series": key,
                    "mode_id": str(mode["mode_id"]),
                    "order": order,
                    "window": window,
                    "smoothness": smoothness,
                    "segment": "validation2",
                    "date": date,
                    "observed": float(observed),
                    "candidate_path": float(predicted),
                }
            )

    result = pd.DataFrame(rows)
    metric_column = (
        "validation2_level_rmse"
        if selection_metric == "level_rmse"
        else "validation2_log_rmse"
    )
    result["validation2_global_rank"] = (
        result[metric_column].rank(method="first", ascending=True).astype(int)
    )
    result["validation2_rank_within_order"] = (
        result.groupby("order")[metric_column]
        .rank(method="first", ascending=True)
        .astype(int)
    )
    result["best_mode_within_order"] = result[
        "validation2_rank_within_order"
    ].eq(1)
    result["selected_global"] = result["validation2_global_rank"].eq(1)

    return (
        result.sort_values(
            ["validation2_global_rank", "order", "mode_rank_within_order"]
        ).reset_index(drop=True),
        pd.DataFrame(path_rows),
    )


def _evaluate_true_test(
    key: str,
    pretest_development: pd.DataFrame,
    true_test: pd.DataFrame,
    candidates: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows: list[dict] = []
    path_rows: list[dict] = []

    test_level = true_test["value"].to_numpy(dtype=float)
    test_log = np.log(test_level)

    for _, candidate in candidates.iterrows():
        order = int(candidate["order"])
        window = int(candidate["window"])
        smoothness = float(candidate["smoothness_used"])
        mode_id = str(candidate["mode_id"])

        fitted, forecast_level = _fit_and_forecast(
            pretest_development,
            true_test,
            order=order,
            window=window,
            smoothness=smoothness,
        )
        forecast_log = np.log(np.clip(forecast_level, 1e-300, None))

        rows.append(
            {
                "series": key,
                "mode_id": mode_id,
                "order": order,
                "true_test_level_rmse": _rmse(
                    test_level,
                    forecast_level,
                ),
                "true_test_log_rmse": _rmse(
                    test_log,
                    forecast_log,
                ),
            }
        )

        for date, observed, predicted in zip(
            fitted["date"],
            fitted["value"],
            fitted["candidate_path"],
        ):
            path_rows.append(
                {
                    "series": key,
                    "mode_id": mode_id,
                    "order": order,
                    "window": window,
                    "smoothness": smoothness,
                    "segment": "final_train",
                    "date": date,
                    "observed": float(observed),
                    "candidate_path": float(predicted),
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
                    "mode_id": mode_id,
                    "order": order,
                    "window": window,
                    "smoothness": smoothness,
                    "segment": "true_test",
                    "date": date,
                    "observed": float(observed),
                    "candidate_path": float(predicted),
                }
            )

    return pd.DataFrame(rows), pd.DataFrame(path_rows)


def _order_color(order: int, smoothness: float) -> tuple[float, float, float]:
    rgb = np.asarray(to_rgb(ORDER_COLORS[int(order)]), dtype=float)
    smoothness = float(np.clip(smoothness, 0.0, 1.0))
    white_fraction = 0.34 * (1.0 - smoothness)
    mixed = rgb * (1.0 - white_fraction) + white_fraction
    return tuple(float(value) for value in mixed)


def _observed(frame: pd.DataFrame) -> pd.DataFrame:
    return (
        frame.loc[:, ["date", "observed"]]
        .drop_duplicates("date")
        .sort_values("date")
        .reset_index(drop=True)
    )


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


def _line_style(candidate: pd.Series) -> tuple[float, float, int]:
    if bool(candidate["selected_global"]):
        return 0.94, 2.55, 5
    if bool(candidate["best_mode_within_order"]):
        return 0.42, 1.55, 4

    support = float(candidate["origin_support_fraction"])
    alpha = 0.10 + 0.20 * min(max(support, 0.0), 1.0)
    return alpha, 0.95, 2


def _plot(
    selections: pd.DataFrame,
    paths: pd.DataFrame,
    output_dir: Path,
    *,
    selection_metric: str,
    mode_representative: str,
    dpi: int,
) -> None:
    series_order = [
        key
        for key in ("GDPC1", "SPY", "AAPL", "BTC-USD")
        if key in set(selections["series"])
    ]
    fig, axes = plt.subplots(
        len(series_order),
        3,
        figsize=(15.2, max(3.6, 3.35 * len(series_order))),
        squeeze=False,
    )

    for row_idx, key in enumerate(series_order):
        ax_val2, ax_fit, ax_test = axes[row_idx]
        case_selection = selections.loc[
            selections["series"].eq(key)
        ].copy()
        case_paths = paths.loc[paths["series"].eq(key)].copy()

        winner = case_selection.loc[
            case_selection["selected_global"]
        ].iloc[0]
        chosen_order = int(winner["order"])
        chosen_mode = str(winner["mode_id"])

        inner_train = case_paths.loc[
            case_paths["segment"].eq("inner_train")
        ]
        validation2 = case_paths.loc[
            case_paths["segment"].eq("validation2")
        ]
        final_train = case_paths.loc[
            case_paths["segment"].eq("final_train")
        ]
        true_test = case_paths.loc[
            case_paths["segment"].eq("true_test")
        ]

        obs_inner = _observed(inner_train)
        obs_val2 = _observed(validation2)
        obs_final = _observed(final_train)
        obs_test = _observed(true_test)

        history_n = min(
            len(obs_inner),
            max(24 if key == "GDPC1" else 120, 2 * len(obs_val2)),
        )
        val_context = pd.concat(
            [obs_inner.tail(history_n), obs_val2],
            ignore_index=True,
        ).drop_duplicates("date").sort_values("date")

        # Column 1: every recurring S-mode is scored on Validation 2.
        ax_val2.plot(
            val_context["date"],
            val_context["observed"],
            color=OBSERVED_COLOR,
            linewidth=1.50,
            alpha=0.96,
            zorder=8,
        )
        for _, candidate in case_selection.sort_values(
            ["order", "mode_rank_within_order"]
        ).iterrows():
            mode_id = str(candidate["mode_id"])
            order = int(candidate["order"])
            train_path = (
                inner_train.loc[inner_train["mode_id"].eq(mode_id)]
                .sort_values("date")
                .tail(history_n)
            )
            val_path = validation2.loc[
                validation2["mode_id"].eq(mode_id)
            ].sort_values("date")
            combined = pd.concat(
                [
                    train_path[["date", "candidate_path"]],
                    val_path[["date", "candidate_path"]],
                ],
                ignore_index=True,
            ).sort_values("date")

            alpha, linewidth, zorder = _line_style(candidate)
            ax_val2.plot(
                combined["date"],
                combined["candidate_path"],
                color=_order_color(
                    order,
                    float(candidate["smoothness_used"]),
                ),
                linewidth=linewidth,
                alpha=alpha,
                zorder=zorder,
            )

        ax_val2.axvline(
            obs_val2["date"].iloc[0],
            color="0.25",
            linewidth=0.9,
            linestyle="--",
            alpha=0.65,
        )
        ax_val2.set_ylim(*_padded_limits(val_context["observed"]))
        metric_label = (
            "level RMSE"
            if selection_metric == "level_rmse"
            else "log RMSE"
        )
        ax_val2.set_title(
            f"Validation 2 → {chosen_mode} ({metric_label})"
        )
        ax_val2.set_ylabel(
            applied.SERIES[key]["family"],
            fontweight="bold",
        )

        # Column 2: refit all modes through Validation 2.
        ax_fit.plot(
            obs_final["date"],
            obs_final["observed"],
            color=OBSERVED_COLOR,
            linewidth=1.40,
            alpha=0.96,
            zorder=8,
        )
        for _, candidate in case_selection.sort_values(
            ["order", "mode_rank_within_order"]
        ).iterrows():
            mode_id = str(candidate["mode_id"])
            order = int(candidate["order"])
            order_fit = final_train.loc[
                final_train["mode_id"].eq(mode_id)
            ].sort_values("date")
            alpha, linewidth, zorder = _line_style(candidate)
            ax_fit.plot(
                order_fit["date"],
                order_fit["candidate_path"],
                color=_order_color(
                    order,
                    float(candidate["smoothness_used"]),
                ),
                linewidth=linewidth,
                alpha=alpha,
                zorder=zorder,
            )
        ax_fit.set_ylim(*_padded_limits(obs_final["observed"]))
        ax_fit.set_title(
            f"Refit through Validation 2; selected d={chosen_order}"
        )

        # Column 3: untouched final test.
        ax_test.plot(
            obs_test["date"],
            obs_test["observed"],
            color=OBSERVED_COLOR,
            linewidth=1.60,
            marker="o",
            markersize=2.0,
            alpha=0.96,
            zorder=8,
        )
        for _, candidate in case_selection.sort_values(
            ["order", "mode_rank_within_order"]
        ).iterrows():
            mode_id = str(candidate["mode_id"])
            order = int(candidate["order"])
            order_test = true_test.loc[
                true_test["mode_id"].eq(mode_id)
            ].sort_values("date")
            alpha, linewidth, zorder = _line_style(candidate)
            ax_test.plot(
                order_test["date"],
                order_test["candidate_path"],
                color=_order_color(
                    order,
                    float(candidate["smoothness_used"]),
                ),
                linewidth=linewidth,
                alpha=alpha,
                zorder=zorder,
            )
        ax_test.set_ylim(*_padded_limits(obs_test["observed"]))
        ax_test.set_title("Untouched true test")

        for ax in (ax_val2, ax_fit, ax_test):
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
            label="Validation-2 winner",
        ),
        Line2D(
            [0],
            [0],
            color="0.45",
            linewidth=1.0,
            alpha=0.22,
            label="Other rolling-CV modes",
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
        (
            "Rolling-origin smoothness modes → Validation 2 selection → "
            f"true test  (mode S = {mode_representative})"
        ),
        y=0.998,
        fontsize=14,
    )
    fig.tight_layout(rect=[0.02, 0.02, 0.98, 0.955])

    fig.savefig(
        output_dir / "two_stage_order_validation.png",
        dpi=dpi,
        bbox_inches="tight",
    )
    fig.savefig(
        output_dir / "two_stage_order_validation.pdf",
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    args = parse_args()
    if args.mode_epsilon <= 0.0:
        raise ValueError("--mode-epsilon must be positive.")

    preset = PRESETS[args.preset]
    output_dir = (
        args.output_dir
        if args.output_dir is not None
        else _default_run_directory(args.preset)
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    started = time.perf_counter()
    window_frames: list[pd.DataFrame] = []
    minima_frames: list[pd.DataFrame] = []
    selection_frames: list[pd.DataFrame] = []
    path_frames: list[pd.DataFrame] = []
    snapshot_meta: dict[str, dict] = {}

    for key in preset["series"]:
        spec = applied.SERIES[key]
        frame = applied._load_series(key)
        reserve = int(spec["test_reserve"])
        if len(frame) <= 2 * reserve:
            raise RuntimeError(
                f"{key} does not have enough observations for Validation 2 "
                "plus the untouched true test."
            )

        inner_development = frame.iloc[: -2 * reserve].copy()
        validation2 = frame.iloc[-2 * reserve : -reserve].copy()
        pretest_development = frame.iloc[:-reserve].copy()
        true_test = frame.iloc[-reserve:].copy()

        window_selection, splits_by_order = _choose_window_per_order(
            key,
            inner_development,
            windows=_windows_for(key, preset),
        )
        minima = _rolling_origin_minima(
            key,
            inner_development,
            window_selection,
            splits_by_order,
        )
        modes = _build_modes(
            minima,
            epsilon=float(args.mode_epsilon),
            representative=args.mode_representative,
        )
        stage2, validation_paths = _evaluate_validation2(
            key,
            inner_development,
            validation2,
            modes,
            selection_metric=args.selection_metric,
        )
        test_metrics, test_paths = _evaluate_true_test(
            key,
            pretest_development,
            true_test,
            stage2,
        )

        merged = stage2.merge(
            test_metrics,
            on=["series", "mode_id", "order"],
            how="left",
            validate="one_to_one",
        )
        merged["inner_development_start_date"] = (
            inner_development["date"].iloc[0]
        )
        merged["inner_development_end_date"] = (
            inner_development["date"].iloc[-1]
        )
        merged["validation2_start_date"] = validation2["date"].iloc[0]
        merged["validation2_end_date"] = validation2["date"].iloc[-1]
        merged["true_test_start_date"] = true_test["date"].iloc[0]
        merged["true_test_end_date"] = true_test["date"].iloc[-1]

        window_frames.append(window_selection)
        minima_frames.append(minima)
        selection_frames.append(merged)
        path_frames.append(
            pd.concat([validation_paths, test_paths], ignore_index=True)
        )

        snapshot_path = Path(spec["path"])
        snapshot_meta[key] = {
            "path": str(snapshot_path),
            "sha256": _sha256(snapshot_path),
            "rows_loaded": int(len(frame)),
            "inner_development_rows": int(len(inner_development)),
            "validation2_rows": int(len(validation2)),
            "true_test_rows": int(len(true_test)),
        }

    windows = pd.concat(window_frames, ignore_index=True)
    minima = pd.concat(minima_frames, ignore_index=True)
    selections = pd.concat(selection_frames, ignore_index=True)
    paths = pd.concat(path_frames, ignore_index=True)

    windows.to_csv(output_dir / "order_window_selection.csv", index=False)
    minima.to_csv(output_dir / "rolling_origin_minima.csv", index=False)
    selections.to_csv(
        output_dir / "two_stage_order_selection.csv",
        index=False,
    )
    paths.to_csv(output_dir / "two_stage_order_paths.csv", index=False)

    _plot(
        selections,
        paths,
        output_dir,
        selection_metric=args.selection_metric,
        mode_representative=args.mode_representative,
        dpi=int(args.dpi),
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "suite": "two_stage_order_validation",
        "preset": args.preset,
        "series": list(preset["series"]),
        "selection_metric": args.selection_metric,
        "mode_representative": args.mode_representative,
        "mode_epsilon": float(args.mode_epsilon),
        "selection_uses_true_test": False,
        "protocol": {
            "stage_1a_window_selection": (
                "Inside the inner development region, the standard aggregate "
                "rolling forecast-CV objective selects L separately for each "
                "d in {1,2,3,4}."
            ),
            "stage_1b_originwise_minima": (
                "At the selected L for each d, the same rolling origins are "
                "reused individually. All representative local smoothness "
                "minima are recovered at every origin."
            ),
            "stage_1c_mode_aggregation": (
                "Nearby originwise minima are grouped in normalized-smoothness "
                "space. Each recurring mode is represented by the requested "
                "mean or median S; support records the number of rolling "
                "origins contributing to the mode."
            ),
            "stage_2_validation": (
                "Every recurring (d, S-mode) candidate forecasts the following "
                "contiguous Validation-2 block. The candidate with the smallest "
                "specified RMSE is selected globally."
            ),
            "final_refit": (
                "All candidates are refit through Validation 2 with frozen "
                "d, L and mode representative S. The winner is emphasized in "
                "the plot; all other candidates remain visible at lower alpha."
            ),
            "true_test": (
                "The final reserve remains untouched until all selection is "
                "complete. True-test metrics are diagnostic only."
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
        winner = selections.loc[
            selections["series"].eq(key)
            & selections["selected_global"]
        ].iloc[0]
        metric = (
            winner["validation2_level_rmse"]
            if args.selection_metric == "level_rmse"
            else winner["validation2_log_rmse"]
        )
        print(
            f"{key}: selected {winner['mode_id']} "
            f"(d={int(winner['order'])}, "
            f"L={int(winner['window'])}, "
            f"S={float(winner['smoothness_used']):.6f}, "
            f"support={int(winner['origin_support'])}, "
            f"validation2_{args.selection_metric}={float(metric):.6g})"
        )


if __name__ == "__main__":
    main()
