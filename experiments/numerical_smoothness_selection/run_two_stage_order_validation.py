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
OBSERVED_COLOR = "#1f77b4"
ORDER_COLORS = {
    1: "#d62728",  # red
    2: "#2ca02c",  # green
    3: "#9467bd",  # purple
    4: "#ff7f0e",  # orange
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
            "Exploratory two-stage order selection. Stage 1 uses rolling "
            "forecast CV inside an inner development region to select L and S "
            "for each d. Stage 2 uses a contiguous pseudo-test validation block "
            "to select d by RMSE. Only then are all candidates refit through "
            "that second validation block and forecast into the untouched "
            "final test."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="paper")
    parser.add_argument(
        "--selection-metric",
        choices=("level_rmse", "log_rmse"),
        default="level_rmse",
        help="Metric used on validation 2 to choose the polynomial order.",
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
) -> tuple[np.ndarray, np.ndarray]:
    fit_train = train.tail(window).copy()
    train_log = np.log(fit_train["value"].to_numpy(dtype=float))
    model = td.PurePenalizedTrend(
        order=int(order),
        smoothness=float(smoothness),
    ).fit(train_log)
    fitted_level = _safe_levels(np.asarray(model.trend_, dtype=float))
    forecast_log = np.asarray(model.forecast(len(future)), dtype=float)
    forecast_level = _safe_levels(forecast_log)
    return fitted_level, forecast_level


def _stage1_select_per_order(
    key: str,
    inner_development: pd.DataFrame,
    *,
    windows: tuple[int, ...],
) -> pd.DataFrame:
    spec = applied.SERIES[key]
    horizon = int(spec["test_reserve"])
    inner_log = np.log(inner_development["value"].to_numpy(dtype=float))
    rows: list[dict] = []

    for order in ORDERS:
        order_rows: list[dict] = []
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
            order_rows.append(
                {
                    "series": key,
                    "family": spec["family"],
                    "order": int(order),
                    "window": int(window),
                    "horizon": horizon,
                    "smoothness": float(best["smoothness"]),
                    "lambda": float(best["lambda"]),
                    "source": str(best["source"]),
                    "inner_cv_error": float(best["cv_error"]),
                    "inner_cv_origins": int(len(splits)),
                    "adaptive_evaluations": int(n_evaluations),
                    "n_stationary_points": int(len(search.points_)),
                    "n_representative_candidates": int(len(candidates)),
                }
            )

        if not order_rows:
            raise RuntimeError(
                f"No valid Stage-1 configuration for {key}, d={order}."
            )

        best_order = (
            pd.DataFrame(order_rows)
            .sort_values(
                ["inner_cv_error", "window", "smoothness"],
                ascending=[True, True, True],
            )
            .iloc[0]
            .to_dict()
        )
        rows.append(best_order)

    return pd.DataFrame(rows).sort_values("order").reset_index(drop=True)


def _evaluate_validation2(
    key: str,
    inner_development: pd.DataFrame,
    validation2: pd.DataFrame,
    selections: pd.DataFrame,
    *,
    selection_metric: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows: list[dict] = []
    path_rows: list[dict] = []
    validation_level = validation2["value"].to_numpy(dtype=float)
    validation_log = np.log(validation_level)

    for _, selected in selections.iterrows():
        order = int(selected["order"])
        window = int(selected["window"])
        smoothness = float(selected["smoothness"])
        train = inner_development.tail(window).copy()

        fitted_level, forecast_level = _fit_and_forecast(
            inner_development,
            validation2,
            order=order,
            window=window,
            smoothness=smoothness,
        )
        forecast_log = np.log(np.clip(forecast_level, 1e-300, None))
        level_rmse = _rmse(validation_level, forecast_level)
        log_rmse = _rmse(validation_log, forecast_log)

        rows.append(
            {
                **selected.to_dict(),
                "validation2_level_rmse": level_rmse,
                "validation2_log_rmse": log_rmse,
            }
        )

        for date, observed, fitted in zip(
            train["date"],
            train["value"],
            fitted_level,
        ):
            path_rows.append(
                {
                    "series": key,
                    "order": order,
                    "window": window,
                    "smoothness": smoothness,
                    "segment": "inner_train",
                    "date": date,
                    "observed": float(observed),
                    "candidate_path": float(fitted),
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
    result["validation2_rank"] = (
        result[metric_column].rank(method="first", ascending=True).astype(int)
    )
    result["selected_order"] = result["validation2_rank"].eq(1)
    return result.sort_values("order").reset_index(drop=True), pd.DataFrame(path_rows)


def _evaluate_true_test(
    key: str,
    pretest_development: pd.DataFrame,
    true_test: pd.DataFrame,
    selections: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows: list[dict] = []
    path_rows: list[dict] = []
    test_level = true_test["value"].to_numpy(dtype=float)
    test_log = np.log(test_level)

    for _, selected in selections.iterrows():
        order = int(selected["order"])
        window = int(selected["window"])
        smoothness = float(selected["smoothness"])
        train = pretest_development.tail(window).copy()

        fitted_level, forecast_level = _fit_and_forecast(
            pretest_development,
            true_test,
            order=order,
            window=window,
            smoothness=smoothness,
        )
        forecast_log = np.log(np.clip(forecast_level, 1e-300, None))
        level_rmse = _rmse(test_level, forecast_level)
        log_rmse = _rmse(test_log, forecast_log)

        rows.append(
            {
                "series": key,
                "order": order,
                "true_test_level_rmse": level_rmse,
                "true_test_log_rmse": log_rmse,
            }
        )

        for date, observed, fitted in zip(
            train["date"],
            train["value"],
            fitted_level,
        ):
            path_rows.append(
                {
                    "series": key,
                    "order": order,
                    "window": window,
                    "smoothness": smoothness,
                    "segment": "final_train",
                    "date": date,
                    "observed": float(observed),
                    "candidate_path": float(fitted),
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
    white_fraction = 0.45 * (1.0 - smoothness)
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


def _plot(
    selections: pd.DataFrame,
    paths: pd.DataFrame,
    output_dir: Path,
    *,
    selection_metric: str,
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
        figsize=(15.0, max(3.6, 3.25 * len(series_order))),
        squeeze=False,
    )

    for row_idx, key in enumerate(series_order):
        ax_val2, ax_fit, ax_test = axes[row_idx]
        case_selection = selections.loc[selections["series"].eq(key)].copy()
        case_paths = paths.loc[paths["series"].eq(key)].copy()
        chosen_order = int(
            case_selection.loc[case_selection["selected_order"], "order"].iloc[0]
        )

        inner_train = case_paths.loc[case_paths["segment"].eq("inner_train")]
        validation2 = case_paths.loc[case_paths["segment"].eq("validation2")]
        final_train = case_paths.loc[case_paths["segment"].eq("final_train")]
        true_test = case_paths.loc[case_paths["segment"].eq("true_test")]

        obs_inner = _observed(inner_train)
        obs_val2 = _observed(validation2)
        obs_final = _observed(final_train)
        obs_test = _observed(true_test)

        # Column 1: second validation block that actually chooses d.
        history_n = min(
            len(obs_inner),
            max(24 if key == "GDPC1" else 120, 2 * len(obs_val2)),
        )
        val_context = pd.concat(
            [obs_inner.tail(history_n), obs_val2],
            ignore_index=True,
        ).drop_duplicates("date").sort_values("date")
        ax_val2.plot(
            val_context["date"],
            val_context["observed"],
            color=OBSERVED_COLOR,
            linewidth=1.45,
            alpha=0.95,
            zorder=5,
        )
        for _, selected in case_selection.sort_values("order").iterrows():
            order = int(selected["order"])
            is_chosen = order == chosen_order
            order_train = (
                inner_train.loc[inner_train["order"].eq(order)]
                .sort_values("date")
                .tail(history_n)
            )
            order_val = validation2.loc[
                validation2["order"].eq(order)
            ].sort_values("date")
            combined = pd.concat(
                [
                    order_train[["date", "candidate_path"]],
                    order_val[["date", "candidate_path"]],
                ],
                ignore_index=True,
            ).sort_values("date")
            ax_val2.plot(
                combined["date"],
                combined["candidate_path"],
                color=_order_color(order, float(selected["smoothness"])),
                linewidth=2.25 if is_chosen else 1.05,
                alpha=0.88 if is_chosen else 0.20,
                zorder=4 if is_chosen else 2,
            )

        ax_val2.axvline(
            obs_val2["date"].iloc[0],
            color="0.25",
            linewidth=0.9,
            linestyle="--",
            alpha=0.65,
        )
        ax_val2.set_ylim(*_padded_limits(val_context["observed"]))
        metric_label = "level RMSE" if selection_metric == "level_rmse" else "log RMSE"
        ax_val2.set_title(f"Validation 2 selects d={chosen_order} ({metric_label})")
        ax_val2.set_ylabel(applied.SERIES[key]["family"], fontweight="bold")

        # Column 2: refit every Stage-1 candidate through validation 2.
        ax_fit.plot(
            obs_final["date"],
            obs_final["observed"],
            color=OBSERVED_COLOR,
            linewidth=1.35,
            alpha=0.95,
            zorder=5,
        )
        for _, selected in case_selection.sort_values("order").iterrows():
            order = int(selected["order"])
            is_chosen = order == chosen_order
            order_fit = final_train.loc[
                final_train["order"].eq(order)
            ].sort_values("date")
            ax_fit.plot(
                order_fit["date"],
                order_fit["candidate_path"],
                color=_order_color(order, float(selected["smoothness"])),
                linewidth=2.25 if is_chosen else 1.05,
                alpha=0.88 if is_chosen else 0.20,
                zorder=4 if is_chosen else 2,
            )
        ax_fit.set_ylim(*_padded_limits(obs_final["observed"]))
        ax_fit.set_title("Refit through Validation 2")

        # Column 3: untouched final test. Selection is already frozen.
        ax_test.plot(
            obs_test["date"],
            obs_test["observed"],
            color=OBSERVED_COLOR,
            linewidth=1.55,
            marker="o",
            markersize=2.0,
            alpha=0.95,
            zorder=5,
        )
        for _, selected in case_selection.sort_values("order").iterrows():
            order = int(selected["order"])
            is_chosen = order == chosen_order
            order_test = true_test.loc[
                true_test["order"].eq(order)
            ].sort_values("date")
            ax_test.plot(
                order_test["date"],
                order_test["candidate_path"],
                color=_order_color(order, float(selected["smoothness"])),
                linewidth=2.40 if is_chosen else 1.05,
                alpha=0.92 if is_chosen else 0.18,
                zorder=4 if is_chosen else 2,
            )
        ax_test.set_ylim(*_padded_limits(obs_test["observed"]))
        ax_test.set_title("Untouched true test")

        for ax in (ax_val2, ax_fit, ax_test):
            ax.grid(alpha=0.18)
            _date_axis(ax)

    handles = [
        Line2D([0], [0], color=OBSERVED_COLOR, linewidth=2.2, label="Observed"),
        *[
            Line2D(
                [0],
                [0],
                color=ORDER_COLORS[order],
                linewidth=2.0,
                alpha=0.75,
                label=f"d={order}",
            )
            for order in ORDERS
        ],
        Line2D(
            [0],
            [0],
            color="0.15",
            linewidth=2.4,
            label="Validation-2 winner: high alpha",
        ),
        Line2D(
            [0],
            [0],
            color="0.45",
            linewidth=1.1,
            alpha=0.25,
            label="Other Stage-1 choices: low alpha",
        ),
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.987),
        ncol=7,
        frameon=False,
        fontsize=8.2,
    )
    fig.suptitle(
        "Exploratory two-stage selection: rolling CV → pseudo-test RMSE → true test",
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
    preset = PRESETS[args.preset]
    output_dir = (
        args.output_dir
        if args.output_dir is not None
        else _default_run_directory(args.preset)
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    started = time.perf_counter()
    selection_frames: list[pd.DataFrame] = []
    path_frames: list[pd.DataFrame] = []
    snapshot_meta: dict[str, dict] = {}

    for key in preset["series"]:
        spec = applied.SERIES[key]
        frame = applied._load_series(key)
        reserve = int(spec["test_reserve"])
        if len(frame) <= 2 * reserve:
            raise RuntimeError(
                f"{key} does not have enough observations for validation 2 "
                "plus the untouched true test."
            )

        inner_development = frame.iloc[: -2 * reserve].copy()
        validation2 = frame.iloc[-2 * reserve : -reserve].copy()
        pretest_development = frame.iloc[:-reserve].copy()
        true_test = frame.iloc[-reserve:].copy()

        stage1 = _stage1_select_per_order(
            key,
            inner_development,
            windows=_windows_for(key, preset),
        )
        stage2, validation_paths = _evaluate_validation2(
            key,
            inner_development,
            validation2,
            stage1,
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
            on=["series", "order"],
            how="left",
            validate="one_to_one",
        )

        merged["inner_development_start_date"] = inner_development["date"].iloc[0]
        merged["inner_development_end_date"] = inner_development["date"].iloc[-1]
        merged["validation2_start_date"] = validation2["date"].iloc[0]
        merged["validation2_end_date"] = validation2["date"].iloc[-1]
        merged["true_test_start_date"] = true_test["date"].iloc[0]
        merged["true_test_end_date"] = true_test["date"].iloc[-1]

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

    selections = pd.concat(selection_frames, ignore_index=True)
    paths = pd.concat(path_frames, ignore_index=True)

    selections.to_csv(output_dir / "two_stage_order_selection.csv", index=False)
    paths.to_csv(output_dir / "two_stage_order_paths.csv", index=False)

    _plot(
        selections,
        paths,
        output_dir,
        selection_metric=args.selection_metric,
        dpi=int(args.dpi),
    )

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "suite": "two_stage_order_validation",
        "preset": args.preset,
        "series": list(preset["series"]),
        "selection_metric": args.selection_metric,
        "selection_uses_true_test": False,
        "protocol": {
            "stage_1": (
                "Within the inner development region, rolling forecast CV at "
                "the full reserve horizon selects L and the best smoothness "
                "candidate separately for each d in {1,2,3,4}."
            ),
            "stage_2": (
                "The immediately following contiguous block, with the same "
                "length as the final test reserve, acts as Validation 2. "
                "Its RMSE selects d among the four Stage-1 choices."
            ),
            "final_refit": (
                "After d is selected, all four Stage-1 choices are refit using "
                "their frozen d/L/S through Validation 2. The selected order "
                "is emphasized; the alternatives are retained only for "
                "diagnostic comparison."
            ),
            "true_test": (
                "The final reserve remains untouched until the order choice "
                "and all hyperparameters are frozen. True-test metrics are "
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
        chosen = selections.loc[
            selections["series"].eq(key) & selections["selected_order"]
        ].iloc[0]
        metric = (
            chosen["validation2_level_rmse"]
            if args.selection_metric == "level_rmse"
            else chosen["validation2_log_rmse"]
        )
        print(
            f"{key}: selected d={int(chosen['order'])}, "
            f"L={int(chosen['window'])}, "
            f"S={float(chosen['smoothness']):.6f}, "
            f"validation2_{args.selection_metric}={float(metric):.6g}"
        )


if __name__ == "__main__":
    main()
