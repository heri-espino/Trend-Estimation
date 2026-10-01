from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd


SERIES_ORDER = ("GDPC1", "SPY", "AAPL", "BTC-USD")
SERIES_LABELS = {
    "GDPC1": "GDP",
    "SPY": "SPY",
    "AAPL": "AAPL",
    "BTC-USD": "BTC-USD",
}

OBSERVED_COLOR = "#1f77b4"
ORDER_COLORS = {
    1: "#d62728",  # red
    2: "#2ca02c",  # green
    3: "#9467bd",  # purple
    4: "#ff7f0e",  # orange
}

DEFAULT_RESULTS_ROOT = Path("results/numerical_smoothness_selection")
REQUIRED_FILES = (
    "long_horizon_order_selection.csv",
    "long_horizon_order_paths.csv",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Plot an exploratory 4x3 diagnostic of long-horizon trend "
            "extrapolation across d=1,2,3,4. This script does not modify "
            "the manuscript."
        )
    )
    parser.add_argument(
        "--run-dir",
        type=Path,
        default=None,
        help=(
            "Applied-case result directory. If omitted, use the newest "
            "applied-paper run containing the long-horizon CSVs."
        ),
    )
    parser.add_argument(
        "--output-stem",
        default="long_horizon_orders_exploratory",
        help="Output filename stem written inside the selected run directory.",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=220,
        help="PNG resolution.",
    )
    return parser.parse_args()


def _latest_compatible_run(results_root: Path) -> Path:
    if not results_root.exists():
        raise FileNotFoundError(
            f"Results root does not exist: {results_root}"
        )

    candidates = []
    for path in results_root.glob("*_applied-paper_*"):
        if not path.is_dir():
            continue
        if all((path / name).exists() for name in REQUIRED_FILES):
            candidates.append(path)

    if not candidates:
        raise FileNotFoundError(
            "No compatible applied-paper run was found. Run "
            "run_applied_case_studies.py --preset paper first, or pass "
            "--run-dir explicitly."
        )

    return max(candidates, key=lambda item: item.name)


def _resolve_run_dir(run_dir: Path | None) -> Path:
    resolved = (
        _latest_compatible_run(DEFAULT_RESULTS_ROOT)
        if run_dir is None
        else run_dir
    )
    missing = [
        name for name in REQUIRED_FILES if not (resolved / name).exists()
    ]
    if missing:
        raise FileNotFoundError(
            f"Run directory {resolved} is missing: {', '.join(missing)}"
        )
    return resolved


def _order_color(base_color: str, smoothness: float) -> tuple[float, float, float]:
    """Use smoothness to control saturation while preserving the order hue."""

    rgb = np.asarray(to_rgb(base_color), dtype=float)
    smoothness = float(np.clip(smoothness, 0.0, 1.0))
    # Keep even S=0 visibly colored. Higher S remains more saturated.
    white_fraction = 0.45 * (1.0 - smoothness)
    mixed = rgb * (1.0 - white_fraction) + white_fraction
    return tuple(float(value) for value in mixed)


def _observed_path(frame: pd.DataFrame) -> pd.DataFrame:
    return (
        frame.loc[:, ["date", "observed"]]
        .drop_duplicates(subset=["date"])
        .sort_values("date")
        .reset_index(drop=True)
    )


def _padded_limits(values: pd.Series, fraction: float = 0.08) -> tuple[float, float]:
    array = values.to_numpy(dtype=float)
    array = array[np.isfinite(array)]
    if array.size == 0:
        raise ValueError("Cannot determine y-limits from an empty observed series.")

    low = float(np.min(array))
    high = float(np.max(array))
    span = high - low
    if span <= 0.0:
        span = max(abs(high), 1.0) * 0.10
    pad = fraction * span
    return low - pad, high + pad


def _configure_date_axis(ax: plt.Axes) -> None:
    locator = mdates.AutoDateLocator(minticks=3, maxticks=6)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))


def _metadata_text(selection: pd.DataFrame) -> str:
    lines = []
    for _, row in selection.sort_values("order").iterrows():
        lines.append(
            f"d={int(row['order'])}: "
            f"L={int(row['window'])}, "
            f"S={float(row['best_smoothness']):.3f}"
        )
    return "\n".join(lines)


def _plot_series_row(
    axes: np.ndarray,
    series: str,
    paths: pd.DataFrame,
    selection: pd.DataFrame,
) -> None:
    ax_fit, ax_full, ax_test = axes

    case_paths = paths.loc[paths["series"].eq(series)].copy()
    case_selection = selection.loc[selection["series"].eq(series)].copy()

    if case_paths.empty or case_selection.empty:
        for ax in axes:
            ax.axis("off")
        return

    # This exploratory plot compares the development-selected best candidate
    # for each order. Other local minima remain available in the source CSVs.
    rank_one = case_paths.loc[case_paths["cv_rank"].eq(1)].copy()
    train = rank_one.loc[rank_one["segment"].eq("train")].copy()
    test = rank_one.loc[rank_one["segment"].eq("test")].copy()

    observed_train = _observed_path(train)
    observed_test = _observed_path(test)
    if observed_train.empty or observed_test.empty:
        raise RuntimeError(f"Missing observed train/test path for {series}.")

    test_n = len(observed_test)
    if series == "GDPC1":
        history_n = min(len(observed_train), max(24, 3 * test_n))
    else:
        history_n = min(len(observed_train), max(120, 3 * test_n))

    observed_tail = observed_train.tail(history_n)
    observed_full = pd.concat(
        [observed_tail, observed_test],
        ignore_index=True,
    ).drop_duplicates(subset=["date"]).sort_values("date")

    # ------------------------------------------------------------------
    # Column 1: fitted trend in each order's final training window.
    # ------------------------------------------------------------------
    ax_fit.plot(
        observed_train["date"],
        observed_train["observed"],
        color=OBSERVED_COLOR,
        linewidth=1.35,
        alpha=0.95,
        zorder=5,
    )

    for order in sorted(case_selection["order"].astype(int).unique()):
        order_sel = case_selection.loc[
            case_selection["order"].eq(order)
        ].iloc[0]
        order_train = train.loc[train["order"].eq(order)].sort_values("date")
        if order_train.empty:
            continue

        color = _order_color(
            ORDER_COLORS[order],
            float(order_sel["best_smoothness"]),
        )
        ax_fit.plot(
            order_train["date"],
            order_train["candidate_path"],
            color=color,
            linewidth=1.55,
            alpha=0.62,
            zorder=3,
        )

    ax_fit.set_ylim(*_padded_limits(observed_train["observed"]))
    ax_fit.set_title("Final fitted trends")
    ax_fit.set_ylabel(SERIES_LABELS.get(series, series), fontweight="bold")
    ax_fit.text(
        0.02,
        0.98,
        _metadata_text(case_selection),
        transform=ax_fit.transAxes,
        va="top",
        ha="left",
        fontsize=7.2,
        bbox={
            "boxstyle": "round,pad=0.25",
            "facecolor": "white",
            "edgecolor": "0.80",
            "alpha": 0.78,
        },
    )

    # ------------------------------------------------------------------
    # Column 2: recent observed history plus the complete reserved test.
    # ------------------------------------------------------------------
    ax_full.plot(
        observed_full["date"],
        observed_full["observed"],
        color=OBSERVED_COLOR,
        linewidth=1.4,
        alpha=0.95,
        zorder=5,
    )

    for order in sorted(case_selection["order"].astype(int).unique()):
        order_sel = case_selection.loc[
            case_selection["order"].eq(order)
        ].iloc[0]
        order_train = (
            train.loc[train["order"].eq(order)]
            .sort_values("date")
            .tail(history_n)
        )
        order_test = test.loc[test["order"].eq(order)].sort_values("date")
        if order_test.empty:
            continue

        order_path = pd.concat(
            [
                order_train.loc[:, ["date", "candidate_path"]],
                order_test.loc[:, ["date", "candidate_path"]],
            ],
            ignore_index=True,
        ).sort_values("date")

        color = _order_color(
            ORDER_COLORS[order],
            float(order_sel["best_smoothness"]),
        )
        ax_full.plot(
            order_path["date"],
            order_path["candidate_path"],
            color=color,
            linewidth=1.55,
            alpha=0.62,
            zorder=3,
        )

    split_date = observed_test["date"].iloc[0]
    ax_full.axvline(
        split_date,
        color="0.25",
        linewidth=0.9,
        linestyle="--",
        alpha=0.65,
        zorder=2,
    )
    ax_full.set_ylim(*_padded_limits(observed_full["observed"]))
    ax_full.set_title("Train tail → full reserved test")

    # ------------------------------------------------------------------
    # Column 3: the untouched test only. Limits ignore forecasts.
    # ------------------------------------------------------------------
    ax_test.plot(
        observed_test["date"],
        observed_test["observed"],
        color=OBSERVED_COLOR,
        linewidth=1.55,
        marker="o",
        markersize=2.0,
        alpha=0.95,
        zorder=5,
    )

    for order in sorted(case_selection["order"].astype(int).unique()):
        order_sel = case_selection.loc[
            case_selection["order"].eq(order)
        ].iloc[0]
        order_test = test.loc[test["order"].eq(order)].sort_values("date")
        if order_test.empty:
            continue

        color = _order_color(
            ORDER_COLORS[order],
            float(order_sel["best_smoothness"]),
        )
        ax_test.plot(
            order_test["date"],
            order_test["candidate_path"],
            color=color,
            linewidth=1.65,
            alpha=0.62,
            zorder=3,
        )

    ax_test.set_ylim(*_padded_limits(observed_test["observed"]))
    ax_test.set_title(f"Reserved test only (h={test_n})")

    for ax in axes:
        ax.grid(alpha=0.18)
        _configure_date_axis(ax)


def plot_exploratory_panel(
    run_dir: Path,
    *,
    output_stem: str,
    dpi: int,
) -> tuple[Path, Path]:
    selection = pd.read_csv(run_dir / "long_horizon_order_selection.csv")
    paths = pd.read_csv(
        run_dir / "long_horizon_order_paths.csv",
        parse_dates=["date"],
    )

    present_series = tuple(
        series
        for series in SERIES_ORDER
        if series in set(selection["series"].astype(str))
    )
    if not present_series:
        raise RuntimeError("No recognized applied series are present in the run.")

    required_orders = {1, 2, 3, 4}
    for series in present_series:
        observed_orders = set(
            selection.loc[selection["series"].eq(series), "order"]
            .astype(int)
            .tolist()
        )
        missing = sorted(required_orders - observed_orders)
        if missing:
            raise RuntimeError(
                f"{series} is missing diagnostic orders: {missing}"
            )

    fig, axes = plt.subplots(
        nrows=len(present_series),
        ncols=3,
        figsize=(15.0, max(3.5, 3.2 * len(present_series))),
        squeeze=False,
    )

    for row_idx, series in enumerate(present_series):
        _plot_series_row(
            axes[row_idx],
            series,
            paths,
            selection,
        )

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
                alpha=0.70,
                label=f"d={order}",
            )
            for order in (1, 2, 3, 4)
        ],
        Line2D(
            [0],
            [0],
            color="0.25",
            linewidth=1.0,
            linestyle="--",
            label="Test begins",
        ),
    ]
    fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.986),
        ncol=6,
        frameon=False,
        fontsize=9,
    )
    fig.suptitle(
        "Exploratory long-horizon trend continuation across difference orders",
        y=0.998,
        fontsize=14,
    )
    fig.tight_layout(rect=[0.02, 0.02, 0.98, 0.955])

    png_path = run_dir / f"{output_stem}.png"
    pdf_path = run_dir / f"{output_stem}.pdf"
    fig.savefig(png_path, dpi=dpi, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    plt.close(fig)
    return png_path, pdf_path


def main() -> None:
    args = parse_args()
    run_dir = _resolve_run_dir(args.run_dir)
    png_path, pdf_path = plot_exploratory_panel(
        run_dir,
        output_stem=args.output_stem,
        dpi=args.dpi,
    )
    print(f"Using run: {run_dir}")
    print(f"Wrote: {png_path}")
    print(f"Wrote: {pdf_path}")


if __name__ == "__main__":
    main()
