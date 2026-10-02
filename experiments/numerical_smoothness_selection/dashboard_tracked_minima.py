from __future__ import annotations

import json
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import streamlit as st

import trend_estimation as td


REPO_ROOT = Path(__file__).resolve().parents[2]
RESULT_ROOT = REPO_ROOT / "results" / "numerical_smoothness_selection"

SERIES_ORDER = ("GDPC1", "SPY", "AAPL", "BTC-USD")
SERIES_LABELS = {
    "GDPC1": "GDP",
    "SPY": "ETF",
    "AAPL": "Stock",
    "BTC-USD": "Crypto",
}
OBSERVED_COLOR = "#4C72B0"
ORDER_COLORS = {
    1: "#C44E52",
    2: "#55A868",
    3: "#8172B3",
    4: "#DD8452",
}

REQUIRED_FILES = (
    "order_window_selection.csv",
    "rolling_minimum_tracks.csv",
    "rolling_validation_paths.csv",
    "tracked_branch_selection.csv",
    "tracked_branch_test_paths.csv",
    "run_metadata.json",
)


def _compatible_runs() -> list[Path]:
    if not RESULT_ROOT.exists():
        return []
    runs = []
    for path in RESULT_ROOT.glob("*_tracked-minima-*"):
        if path.is_dir() and all((path / name).exists() for name in REQUIRED_FILES):
            runs.append(path)
    return sorted(runs, key=lambda item: item.name, reverse=True)


@st.cache_data(show_spinner=False)
def _load_run(run_dir_text: str) -> dict[str, object]:
    run_dir = Path(run_dir_text)

    windows = pd.read_csv(run_dir / "order_window_selection.csv")
    tracks = pd.read_csv(
        run_dir / "rolling_minimum_tracks.csv",
        parse_dates=[
            "val1_start_date",
            "val1_end_date",
            "val2_start_date",
            "val2_end_date",
        ],
    )
    validation_paths = pd.read_csv(
        run_dir / "rolling_validation_paths.csv",
        parse_dates=["date"],
    )
    selection = pd.read_csv(run_dir / "tracked_branch_selection.csv")
    test_paths = pd.read_csv(
        run_dir / "tracked_branch_test_paths.csv",
        parse_dates=["date"],
    )
    metadata = json.loads(
        (run_dir / "run_metadata.json").read_text(encoding="utf-8")
    )

    for column in ("selected_branch", "final_continuation"):
        if column in selection:
            text = selection[column].astype(str).str.lower()
            selection[column] = text.map({"true": True, "false": False})

    return {
        "windows": windows,
        "tracks": tracks,
        "validation_paths": validation_paths,
        "selection": selection,
        "test_paths": test_paths,
        "metadata": metadata,
    }


@st.cache_data(show_spinner=False)
def _load_snapshot(path_text: str) -> pd.DataFrame:
    path = Path(path_text)
    if not path.is_absolute():
        path = REPO_ROOT / path
    frame = pd.read_csv(path, parse_dates=["date"])
    frame["value"] = pd.to_numeric(frame["value"], errors="coerce")
    return (
        frame.dropna(subset=["date", "value"])
        .sort_values("date")
        .drop_duplicates("date")
        .reset_index(drop=True)
    )


def _date_axis(ax: plt.Axes, *, max_ticks: int = 5) -> None:
    locator = mdates.AutoDateLocator(minticks=2, maxticks=max_ticks)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))


def _padded_limits(values: pd.Series, fraction: float = 0.08) -> tuple[float, float]:
    array = values.to_numpy(dtype=float)
    array = array[np.isfinite(array)]
    if array.size == 0:
        return 0.0, 1.0
    low = float(np.min(array))
    high = float(np.max(array))
    span = high - low
    if span <= 0.0:
        span = max(abs(high), 1.0) * 0.10
    pad = fraction * span
    return low - pad, high + pad


def _robust_error_limits(
    values: pd.Series,
    *,
    upper_quantile: float,
    pad_fraction: float = 0.08,
) -> tuple[float, float]:
    """Bound a nonnegative loss axis using the bulk of finite observations."""

    array = values.to_numpy(dtype=float)
    array = array[np.isfinite(array)]
    if array.size == 0:
        return 0.0, 1.0

    upper_quantile = float(np.clip(upper_quantile, 0.50, 1.0))
    upper = float(np.quantile(array, upper_quantile))
    if upper <= 0.0:
        upper = float(np.max(array))
    if upper <= 0.0:
        upper = 1.0
    return 0.0, upper * (1.0 + pad_fraction)


def _safe_level(log_values: np.ndarray) -> np.ndarray:
    return np.exp(np.clip(np.asarray(log_values, dtype=float), -700.0, 700.0))


def _fit_window(
    train: pd.DataFrame,
    *,
    order: int,
    smoothness: float,
    steps: int,
) -> tuple[np.ndarray, np.ndarray]:
    model = td.PurePenalizedTrend(
        order=int(order),
        smoothness=float(smoothness),
    ).fit(np.log(train["value"].to_numpy(dtype=float)))
    fitted = _safe_level(np.asarray(model.trend_, dtype=float))
    forecast = _safe_level(np.asarray(model.forecast(int(steps)), dtype=float))
    return fitted, forecast


def _historical_origin_context(
    series: str,
    tracks: pd.DataFrame,
    winner_id: str,
    metadata: dict,
    origin_number: int,
) -> dict[str, object]:
    row = tracks.loc[
        tracks["branch_id"].eq(winner_id)
        & tracks["origin_number"].eq(origin_number)
        & tracks["status"].eq("matched")
    ]
    if row.empty:
        raise RuntimeError(
            f"No matched row for {series}, {winner_id}, origin={origin_number}."
        )
    row = row.iloc[0]

    frame = _load_snapshot(str(metadata["snapshot"][series]["path"]))
    val1_start = pd.Timestamp(row["val1_start_date"])
    val1_end = pd.Timestamp(row["val1_end_date"])

    start_matches = frame.index[frame["date"].eq(val1_start)].tolist()
    end_matches = frame.index[frame["date"].eq(val1_end)].tolist()
    if not start_matches or not end_matches:
        raise RuntimeError(f"Could not locate Validation 1 dates for {series}.")

    start_idx = int(start_matches[0])
    end_idx = int(end_matches[-1])
    window = int(row["window"])
    order = int(row["order"])
    smoothness = float(row["smoothness"])

    train = frame.iloc[start_idx - window : start_idx].copy()
    val1 = frame.iloc[start_idx : end_idx + 1].copy()
    fitted, val1_forecast = _fit_window(
        train,
        order=order,
        smoothness=smoothness,
        steps=len(val1),
    )
    return {
        "train": train,
        "val1": val1,
        "fitted": fitted,
        "val1_forecast": val1_forecast,
        "order": order,
        "smoothness": smoothness,
        "window": window,
    }


def _final_context(
    series: str,
    winner: pd.Series,
    metadata: dict,
) -> dict[str, object]:
    frame = _load_snapshot(str(metadata["snapshot"][series]["path"]))
    horizon = int(metadata["snapshot"][series]["true_test_rows"])
    window = int(winner["window"])
    order = int(winner["order"])
    smoothness = float(winner["final_smoothness"])

    pretest = frame.iloc[:-horizon].copy()
    test = frame.iloc[-horizon:].copy()
    train = pretest.tail(window).copy()
    fitted, forecast = _fit_window(
        train,
        order=order,
        smoothness=smoothness,
        steps=horizon,
    )
    return {
        "train": train,
        "test": test,
        "fitted": fitted,
        "forecast": forecast,
        "order": order,
        "smoothness": smoothness,
        "window": window,
    }


def _winner(case_selection: pd.DataFrame) -> pd.Series:
    selected = case_selection.loc[case_selection["selected_branch"].eq(True)]
    if selected.empty:
        raise RuntimeError("No selected branch found in tracked_branch_selection.csv.")
    return selected.iloc[0]


def _observed_from_paths(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame(columns=["date", "observed"])
    return (
        frame[["date", "observed"]]
        .drop_duplicates("date")
        .sort_values("date")
        .reset_index(drop=True)
    )


def _series_slice(
    series: str,
    data: dict[str, object],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    tracks = data["tracks"]
    validation_paths = data["validation_paths"]
    selection = data["selection"]
    test_paths = data["test_paths"]
    return (
        tracks.loc[tracks["series"].eq(series)].copy(),
        validation_paths.loc[validation_paths["series"].eq(series)].copy(),
        selection.loc[selection["series"].eq(series)].copy(),
        test_paths.loc[test_paths["series"].eq(series)].copy(),
    )


def _plot_chronology(ax: plt.Axes, series: str, metadata: dict) -> None:
    snapshot = metadata["snapshot"][series]
    frame = _load_snapshot(str(snapshot["path"]))

    history_rows = int(snapshot["historical_tracking_rows"])
    final_val_rows = int(snapshot["final_validation1_rows"])
    true_test_rows = int(snapshot["true_test_rows"])

    tail_total = history_rows + final_val_rows + true_test_rows
    if len(frame) > tail_total:
        frame = frame.tail(tail_total).reset_index(drop=True)

    history_end = history_rows - 1
    final_val_start = history_rows
    final_val_end = history_rows + final_val_rows - 1
    test_start = history_rows + final_val_rows

    ax.plot(
        frame["date"],
        frame["value"],
        color=OBSERVED_COLOR,
        linewidth=1.0,
        alpha=0.92,
    )
    if history_rows > 0:
        ax.axvspan(
            frame["date"].iloc[0],
            frame["date"].iloc[history_end],
            color="#DCE6F1",
            alpha=0.40,
        )
    ax.axvspan(
        frame["date"].iloc[final_val_start],
        frame["date"].iloc[final_val_end],
        color="#F2CF63",
        alpha=0.32,
    )
    ax.axvspan(
        frame["date"].iloc[test_start],
        frame["date"].iloc[-1],
        color="#E6A0A0",
        alpha=0.28,
    )
    ax.set_title("Chronology")
    _date_axis(ax)


def _plot_smoothness(
    ax: plt.Axes,
    tracks: pd.DataFrame,
    winner_id: str,
    *,
    faint_alpha: float,
) -> None:
    for branch_id, branch in tracks.groupby("branch_id"):
        matched = branch.loc[branch["status"].eq("matched")].sort_values(
            "origin_number"
        )
        if matched.empty:
            continue
        order = int(matched["order"].iloc[0])
        selected = branch_id == winner_id
        ax.plot(
            matched["val1_start_date"],
            matched["smoothness"],
            color=ORDER_COLORS[order],
            linewidth=2.2 if selected else 0.9,
            alpha=0.96 if selected else faint_alpha,
            marker="o" if selected else None,
            markersize=2.1 if selected else 0.0,
        )
    ax.set_ylim(-0.03, 1.03)
    ax.set_title("Tracked smoothness")
    _date_axis(ax)


def _plot_minima_count(ax: plt.Axes, tracks: pd.DataFrame) -> None:
    counts = (
        tracks[
            [
                "order",
                "origin_number",
                "val1_start_date",
                "surface_minima_count",
                "matched_branch_count",
            ]
        ]
        .drop_duplicates(["order", "origin_number"])
        .sort_values(["order", "origin_number"])
    )
    for order, group in counts.groupby("order"):
        ax.plot(
            group["val1_start_date"],
            group["surface_minima_count"],
            color=ORDER_COLORS[int(order)],
            linewidth=1.2,
            alpha=0.80,
            marker="o",
            markersize=2.0,
        )
    ax.set_ylim(bottom=0)
    ax.set_title("# local minima")
    _date_axis(ax)


def _plot_loss(
    ax: plt.Axes,
    tracks: pd.DataFrame,
    winner_id: str,
    *,
    column: str,
    title: str,
    faint_alpha: float,
    robust_quantile: float,
) -> None:
    for branch_id, branch in tracks.groupby("branch_id"):
        matched = branch.loc[
            branch["status"].eq("matched") & branch[column].notna()
        ].sort_values("origin_number")
        if matched.empty:
            continue
        order = int(matched["order"].iloc[0])
        selected = branch_id == winner_id
        date_column = "val1_start_date" if column == "val1_loss" else "val2_start_date"
        ax.plot(
            matched[date_column],
            matched[column],
            color=ORDER_COLORS[order],
            linewidth=2.2 if selected else 0.9,
            alpha=0.96 if selected else faint_alpha,
        )
    finite_values = tracks.loc[
        tracks["status"].eq("matched") & tracks[column].notna(),
        column,
    ]
    ax.set_ylim(
        *_robust_error_limits(
            finite_values,
            upper_quantile=robust_quantile,
        )
    )
    ax.set_title(f"{title} (ylim q{int(round(100 * robust_quantile))})")
    _date_axis(ax)


def _plot_smoothed_origin(
    ax: plt.Axes,
    series: str,
    tracks: pd.DataFrame,
    winner_id: str,
    metadata: dict,
    *,
    origin_number: int,
) -> None:
    context = _historical_origin_context(
        series,
        tracks,
        winner_id,
        metadata,
        origin_number,
    )
    train = context["train"]
    val1 = context["val1"]
    order = int(context["order"])

    ax.plot(
        train["date"],
        train["value"],
        color=OBSERVED_COLOR,
        linewidth=1.0,
        alpha=0.68,
        label="Observed train",
    )
    ax.plot(
        train["date"],
        context["fitted"],
        color=ORDER_COLORS[order],
        linewidth=2.0,
        alpha=0.94,
        label="Smoothed trend",
    )
    ax.plot(
        val1["date"],
        val1["value"],
        color=OBSERVED_COLOR,
        linewidth=1.25,
        alpha=0.95,
    )
    ax.plot(
        val1["date"],
        context["val1_forecast"],
        color=ORDER_COLORS[order],
        linewidth=1.45,
        linestyle="--",
        alpha=0.88,
        label="Val. 1 forecast",
    )
    ax.axvline(
        val1["date"].iloc[0],
        color="0.30",
        linewidth=0.8,
        linestyle=":",
        alpha=0.60,
    )
    observed = pd.concat(
        [train["value"], val1["value"]],
        ignore_index=True,
    )
    ax.set_ylim(*_padded_limits(observed))
    ax.set_title("Smoothed series + Val. 1")
    _date_axis(ax)


def _plot_final_smooth_to_test(
    ax: plt.Axes,
    series: str,
    winner: pd.Series,
    metadata: dict,
) -> None:
    context = _final_context(series, winner, metadata)
    train = context["train"]
    test = context["test"]
    order = int(context["order"])

    history_n = min(
        len(train),
        max(
            len(test) * 2,
            24 if series == "GDPC1" else 120,
        ),
    )
    train_tail = train.tail(history_n)
    fitted_tail = np.asarray(context["fitted"])[-history_n:]

    ax.plot(
        train_tail["date"],
        train_tail["value"],
        color=OBSERVED_COLOR,
        linewidth=1.0,
        alpha=0.68,
    )
    ax.plot(
        train_tail["date"],
        fitted_tail,
        color=ORDER_COLORS[order],
        linewidth=2.0,
        alpha=0.94,
    )
    ax.plot(
        test["date"],
        test["value"],
        color=OBSERVED_COLOR,
        linewidth=1.55,
        marker="o",
        markersize=1.8,
        alpha=0.97,
        zorder=7,
    )
    ax.plot(
        test["date"],
        context["forecast"],
        color=ORDER_COLORS[order],
        linewidth=2.25,
        alpha=0.95,
        zorder=6,
    )
    ax.axvline(
        test["date"].iloc[0],
        color="0.25",
        linewidth=0.9,
        linestyle="--",
        alpha=0.65,
    )

    observed = pd.concat(
        [train_tail["value"], test["value"]],
        ignore_index=True,
    )
    ax.set_ylim(*_padded_limits(observed))
    ax.set_title("After final validation → true test")
    _date_axis(ax)


def _plot_recent_validation_continuations(
    ax: plt.Axes,
    validation_paths: pd.DataFrame,
    winner_id: str,
    *,
    recent_origins: int,
) -> None:
    branch = validation_paths.loc[
        validation_paths["branch_id"].eq(winner_id)
    ].copy()
    if branch.empty:
        ax.text(0.5, 0.5, "No validation paths", ha="center", va="center")
        ax.set_title("Val. 2 continuation")
        return

    origins = sorted(branch["origin_number"].unique())[-recent_origins:]
    branch = branch.loc[branch["origin_number"].isin(origins)].copy()
    observed = _observed_from_paths(branch)

    ax.plot(
        observed["date"],
        observed["observed"],
        color=OBSERVED_COLOR,
        linewidth=1.4,
        alpha=0.95,
        zorder=5,
    )
    order = int(branch["order"].iloc[0])
    for idx, origin in enumerate(origins, start=1):
        path = branch.loc[branch["origin_number"].eq(origin)].sort_values("date")
        alpha = 0.28 + 0.62 * idx / max(len(origins), 1)
        ax.plot(
            path["date"],
            path["candidate_path"],
            color=ORDER_COLORS[order],
            linewidth=1.25,
            alpha=alpha,
        )

    ax.set_ylim(*_padded_limits(observed["observed"]))
    ax.set_title("Val. 2 continuation")
    _date_axis(ax)


def _plot_true_test(
    ax: plt.Axes,
    test_paths: pd.DataFrame,
    selection: pd.DataFrame,
    winner_id: str,
    *,
    faint_alpha: float,
) -> None:
    observed = _observed_from_paths(test_paths)
    if observed.empty:
        ax.text(0.5, 0.5, "No test paths", ha="center", va="center")
        ax.set_title("True test")
        return

    ax.plot(
        observed["date"],
        observed["observed"],
        color=OBSERVED_COLOR,
        linewidth=1.5,
        marker="o",
        markersize=1.8,
        alpha=0.97,
        zorder=8,
    )

    for branch_id, path in test_paths.groupby("branch_id"):
        meta = selection.loc[selection["branch_id"].eq(branch_id)]
        if meta.empty:
            continue
        order = int(meta["order"].iloc[0])
        selected = branch_id == winner_id
        path = path.sort_values("date")
        ax.plot(
            path["date"],
            path["candidate_path"],
            color=ORDER_COLORS[order],
            linewidth=2.4 if selected else 0.9,
            alpha=0.96 if selected else faint_alpha,
            zorder=5 if selected else 2,
        )

    ax.set_ylim(*_padded_limits(observed["observed"]))
    ax.set_title("Untouched true test")
    _date_axis(ax)


def _story_matrix(
    data: dict[str, object],
    *,
    metric: str,
    faint_alpha: float,
    recent_origins: int,
    robust_quantile: float,
) -> plt.Figure:
    metadata = data["metadata"]
    selection = data["selection"]
    present = [
        series
        for series in SERIES_ORDER
        if series in set(selection["series"].astype(str))
    ]

    fig, axes = plt.subplots(
        len(present),
        9,
        figsize=(35.0, max(3.0, 3.1 * len(present))),
        squeeze=False,
    )

    for row_idx, series in enumerate(present):
        tracks, validation_paths, case_selection, test_paths = _series_slice(
            series,
            data,
        )
        winner = _winner(case_selection)
        winner_id = str(winner["branch_id"])

        _plot_chronology(axes[row_idx, 0], series, metadata)
        _plot_smoothness(
            axes[row_idx, 1],
            tracks,
            winner_id,
            faint_alpha=faint_alpha,
        )
        _plot_minima_count(axes[row_idx, 2], tracks)
        _plot_loss(
            axes[row_idx, 3],
            tracks,
            winner_id,
            column="val1_loss",
            title="Validation 1 loss",
            faint_alpha=faint_alpha,
            robust_quantile=robust_quantile,
        )
        _plot_loss(
            axes[row_idx, 4],
            tracks,
            winner_id,
            column=(
                "val2_level_rmse"
                if metric == "level_rmse"
                else "val2_log_rmse"
            ),
            title=(
                "Validation 2 RMSE"
                if metric == "level_rmse"
                else "Validation 2 log-RMSE"
            ),
            faint_alpha=faint_alpha,
            robust_quantile=robust_quantile,
        )

        winner_origins = sorted(
            int(value)
            for value in tracks.loc[
                tracks["branch_id"].eq(winner_id)
                & tracks["status"].eq("matched"),
                "origin_number",
            ].unique()
        )
        latest_origin = winner_origins[-1]

        _plot_smoothed_origin(
            axes[row_idx, 5],
            series,
            tracks,
            winner_id,
            metadata,
            origin_number=latest_origin,
        )
        _plot_recent_validation_continuations(
            axes[row_idx, 6],
            validation_paths,
            winner_id,
            recent_origins=recent_origins,
        )
        _plot_final_smooth_to_test(
            axes[row_idx, 7],
            series,
            winner,
            metadata,
        )
        _plot_true_test(
            axes[row_idx, 8],
            test_paths,
            case_selection,
            winner_id,
            faint_alpha=faint_alpha,
        )

        axes[row_idx, 0].set_ylabel(
            SERIES_LABELS.get(series, series),
            fontweight="bold",
        )
        for col_idx in range(9):
            axes[row_idx, col_idx].grid(alpha=0.13)
            if row_idx < len(present) - 1:
                axes[row_idx, col_idx].tick_params(labelbottom=False)

    handles = [
        Line2D([0], [0], color=OBSERVED_COLOR, linewidth=2.0, label="Observed"),
        *[
            Line2D(
                [0],
                [0],
                color=ORDER_COLORS[order],
                linewidth=1.8,
                label=f"d={order}",
            )
            for order in (1, 2, 3, 4)
        ],
        Line2D(
            [0],
            [0],
            color="0.15",
            linewidth=2.4,
            alpha=0.95,
            label="Selected branch",
        ),
        Line2D(
            [0],
            [0],
            color="0.45",
            linewidth=1.0,
            alpha=faint_alpha,
            label="Other branches",
        ),
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        ncol=7,
        frameon=False,
        fontsize=8.4,
        bbox_to_anchor=(0.5, 0.995),
    )
    fig.suptitle(
        "Tracked-minimum story matrix: rolling validation to true test",
        y=1.015,
        fontsize=15,
    )
    fig.tight_layout(rect=[0.01, 0.01, 0.995, 0.975])
    return fig


def _detail_figure(
    series: str,
    data: dict[str, object],
    *,
    metric: str,
    faint_alpha: float,
    origin_number: int,
    robust_quantile: float,
) -> plt.Figure:
    tracks, validation_paths, selection, test_paths = _series_slice(series, data)
    winner = _winner(selection)
    winner_id = str(winner["branch_id"])

    fig, axes = plt.subplots(2, 4, figsize=(23.0, 9.0))
    _plot_smoothness(
        axes[0, 0],
        tracks,
        winner_id,
        faint_alpha=faint_alpha,
    )
    _plot_loss(
        axes[0, 1],
        tracks,
        winner_id,
        column="val1_loss",
        title="Validation 1 loss",
        faint_alpha=faint_alpha,
        robust_quantile=robust_quantile,
    )
    _plot_loss(
        axes[0, 2],
        tracks,
        winner_id,
        column=(
            "val2_level_rmse"
            if metric == "level_rmse"
            else "val2_log_rmse"
        ),
        title=(
            "Validation 2 RMSE"
            if metric == "level_rmse"
            else "Validation 2 log-RMSE"
        ),
        faint_alpha=faint_alpha,
        robust_quantile=robust_quantile,
    )
    _plot_smoothed_origin(
        axes[0, 3],
        series,
        tracks,
        winner_id,
        data["metadata"],
        origin_number=origin_number,
    )
    _plot_minima_count(axes[1, 0], tracks)

    origin_paths = validation_paths.loc[
        validation_paths["origin_number"].eq(origin_number)
    ].copy()
    observed = _observed_from_paths(origin_paths)
    if not observed.empty:
        axes[1, 1].plot(
            observed["date"],
            observed["observed"],
            color=OBSERVED_COLOR,
            linewidth=1.6,
            marker="o",
            markersize=2.0,
            alpha=0.97,
            zorder=8,
        )
        for branch_id, path in origin_paths.groupby("branch_id"):
            meta = selection.loc[selection["branch_id"].eq(branch_id)]
            if meta.empty:
                continue
            order = int(meta["order"].iloc[0])
            selected = branch_id == winner_id
            path = path.sort_values("date")
            axes[1, 1].plot(
                path["date"],
                path["candidate_path"],
                color=ORDER_COLORS[order],
                linewidth=2.3 if selected else 0.95,
                alpha=0.96 if selected else faint_alpha,
            )
        axes[1, 1].set_ylim(*_padded_limits(observed["observed"]))
    axes[1, 1].set_title(f"Validation 2 continuation: origin {origin_number}")
    _date_axis(axes[1, 1])

    _plot_final_smooth_to_test(
        axes[1, 2],
        series,
        winner,
        data["metadata"],
    )
    _plot_true_test(
        axes[1, 3],
        test_paths,
        selection,
        winner_id,
        faint_alpha=faint_alpha,
    )

    for ax in axes.ravel():
        ax.grid(alpha=0.14)

    fig.suptitle(
        f"{SERIES_LABELS.get(series, series)} - {series}: branch-level diagnostic",
        y=1.01,
        fontsize=14,
    )
    fig.tight_layout()
    return fig


def _selection_table(selection: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "selected_branch",
        "branch_id",
        "order",
        "window",
        "support_fraction",
        "n_matched_origins",
        "n_possible_origins",
        "selection_score",
        "smoothness_first",
        "smoothness_last",
        "smoothness_mean",
        "smoothness_median",
        "smoothness_recent5_mean",
        "smoothness_recent5_median",
        "final_smoothness",
        "true_test_level_rmse",
        "true_test_log_rmse",
    ]
    available = [column for column in columns if column in selection.columns]
    return selection[available].sort_values(
        ["selected_branch", "selection_score"],
        ascending=[False, True],
    )


def _bytes_csv(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False).encode("utf-8")


def main() -> None:
    st.set_page_config(
        page_title="Tracked minima dashboard",
        layout="wide",
    )
    st.markdown(
        """
        <style>
        .block-container {
            max-width: 2800px;
            padding-top: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Tracked local-minimum forecasting dashboard")
    st.caption(
        "Validation 1 finds and tracks local smoothness minima; Validation 2 "
        "scores each branch; the final reserve is untouched until selection is complete."
    )

    runs = _compatible_runs()
    if not runs:
        st.error(
            "No compatible tracked-minima run was found. Run the tracked-minima "
            "experiment with preset paper first."
        )
        st.stop()

    with st.sidebar:
        st.header("Run")
        selected_run = st.selectbox(
            "Result directory",
            options=runs,
            format_func=lambda path: path.name,
        )
        metric = st.selectbox(
            "Displayed Validation-2 metric",
            options=("level_rmse", "log_rmse"),
            format_func=lambda value: (
                "Level RMSE" if value == "level_rmse" else "Log RMSE"
            ),
        )
        faint_alpha = st.slider(
            "Alpha for non-selected branches",
            min_value=0.05,
            max_value=0.45,
            value=0.18,
            step=0.01,
        )
        recent_origins = st.slider(
            "Recent Validation-2 continuations in overview",
            min_value=1,
            max_value=8,
            value=3,
            step=1,
        )
        robust_quantile = st.slider(
            "Upper quantile for validation-error y-limits",
            min_value=0.80,
            max_value=1.00,
            value=0.95,
            step=0.01,
            help=(
                "Validation-loss panels ignore extreme upper-tail explosions "
                "when setting their visible y-range. The data are not removed."
            ),
        )

    data = _load_run(str(selected_run))
    metadata = data["metadata"]
    selection = data["selection"]

    run_metric = metadata.get("selection_metric", "unknown")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Run", selected_run.name)
    c2.metric("Selection metric used by run", str(run_metric))
    c3.metric("Tracking epsilon", str(metadata.get("track_epsilon", "-")))
    c4.metric("Max initialized minima / d", str(metadata.get("max_minima", "-")))

    st.subheader("Full story matrix")
    st.caption(
        "Rows are GDP, ETF, Stock, and Crypto. Columns follow the whole story: "
        "chronology, tracked smoothness, number of minima, Validation-1 loss, "
        "Validation-2 loss, the selected smoothed series, rolling Validation-2 "
        "continuations, the final smoothed fit carried into the test, and the "
        "untouched-test branch comparison. Validation-error axes use a robust "
        "upper quantile so isolated explosions do not flatten the rest."
    )
    overview = _story_matrix(
        data,
        metric=metric,
        faint_alpha=faint_alpha,
        recent_origins=recent_origins,
        robust_quantile=robust_quantile,
    )
    st.pyplot(overview, use_container_width=True)
    plt.close(overview)

    present_series = [
        series
        for series in SERIES_ORDER
        if series in set(selection["series"].astype(str))
    ]
    st.subheader("Series drill-down")
    tabs = st.tabs(
        [
            f"{SERIES_LABELS.get(series, series)} - {series}"
            for series in present_series
        ]
    )

    for tab, series in zip(tabs, present_series):
        with tab:
            tracks, validation_paths, case_selection, _ = _series_slice(
                series,
                data,
            )
            winner = _winner(case_selection)

            metrics = st.columns(7)
            metrics[0].metric("Selected branch", str(winner["branch_id"]))
            metrics[1].metric("d", int(winner["order"]))
            metrics[2].metric("L", int(winner["window"]))
            metrics[3].metric(
                "Support",
                f"{int(winner['n_matched_origins'])}/"
                f"{int(winner['n_possible_origins'])}",
            )
            metrics[4].metric(
                "Historical Val. 2 score",
                f"{float(winner['selection_score']):.5g}",
            )
            metrics[5].metric(
                "Final S",
                f"{float(winner['final_smoothness']):.4f}",
            )
            test_metric = (
                "true_test_level_rmse"
                if metric == "level_rmse"
                else "true_test_log_rmse"
            )
            metrics[6].metric(
                "True-test diagnostic",
                f"{float(winner[test_metric]):.5g}",
            )

            origins = sorted(
                int(value)
                for value in tracks.loc[
                    tracks["branch_id"].eq(str(winner["branch_id"]))
                    & tracks["status"].eq("matched"),
                    "origin_number",
                ].unique()
            )
            origin_number = st.select_slider(
                "Validation-2 origin to inspect",
                options=origins,
                value=origins[-1],
                key=f"origin-{series}",
            )

            detail = _detail_figure(
                series,
                data,
                metric=metric,
                faint_alpha=faint_alpha,
                origin_number=int(origin_number),
                robust_quantile=robust_quantile,
            )
            st.pyplot(detail, use_container_width=True)
            plt.close(detail)

            st.markdown("**Branch summary**")
            st.dataframe(
                _selection_table(case_selection),
                use_container_width=True,
                hide_index=True,
            )

            with st.expander("Rolling minima table"):
                st.dataframe(
                    tracks.sort_values(["order", "branch_id", "origin_number"]),
                    use_container_width=True,
                    hide_index=True,
                )

            with st.expander("Validation-2 forecast paths"):
                st.dataframe(
                    validation_paths.sort_values(
                        ["origin_number", "order", "branch_id", "date"]
                    ),
                    use_container_width=True,
                    hide_index=True,
                )

            d1, d2, d3 = st.columns(3)
            d1.download_button(
                "Download branch summary CSV",
                data=_bytes_csv(case_selection),
                file_name=f"{series}_tracked_branch_selection.csv",
                mime="text/csv",
                key=f"download-summary-{series}",
            )
            d2.download_button(
                "Download rolling tracks CSV",
                data=_bytes_csv(tracks),
                file_name=f"{series}_rolling_minimum_tracks.csv",
                mime="text/csv",
                key=f"download-tracks-{series}",
            )
            d3.download_button(
                "Download validation paths CSV",
                data=_bytes_csv(validation_paths),
                file_name=f"{series}_rolling_validation_paths.csv",
                mime="text/csv",
                key=f"download-valpaths-{series}",
            )

    st.divider()
    st.caption(
        "Exploratory dashboard only. It reads frozen result files and does not "
        "change model selection or manuscript outputs."
    )


if __name__ == "__main__":
    main()
