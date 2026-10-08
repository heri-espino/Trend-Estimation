"""Make the five-panel workflow figure for the forecasting manuscript.

A single fixed, reproducible simulated example illustrates:
  A. chronological train -> historical Val1 -> historical Val2 ->
     current Val1 -> untouched outer test;
  B. final refits with three smoothness decisions;
  C. outer-test forecasts (revealed only for display/scoring);
  D. the current Val1 objective and its minima, never an outer-test loss;
  E. tracked historical minima and the final phi(V_j) decisions.

Run from repository root:
    python experiments/smoothness_cv/make_workflow_tutorial_figure.py

Output:
    paper_smoothness-cv/manuscript/figures/fig_workflow_tutorial.pdf
    paper_smoothness-cv/manuscript/figures/fig_workflow_tutorial.png
    paper_smoothness-cv/manuscript/figures/fig_workflow_tutorial.json

The scenario and outer test are fixed by *indices*, not chosen for
favorable performance. This is a pedagogical figure, not a new experiment.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import trend_estimation as td
from experiments.smoothness_cv import run_checkpoint_04 as cp04
from experiments.smoothness_cv import run_checkpoint_06 as cp06
from experiments.smoothness_cv import run_checkpoint_07 as cp07
from experiments.smoothness_cv.dynamic_branch_rules import evaluate_rule_set
from experiments.numerical_smoothness_selection import (
    run_two_stage_order_validation as tracked,
)

FIGURES_DIR = ROOT / "paper_smoothness-cv" / "manuscript" / "figures"
NAME = "fig_workflow_tutorial"
KEY = "CP07_SIM"
SEED = 100
MECHANISM = "switch_to_rough"
NOISE_SD = 0.01
OUTER_NUMBER = 8  # fixed before inspecting the test, among the 8 CP07 origins
ORDER = cp07.ORDER
WINDOW = cp07.WINDOW
HORIZON = cp07.HORIZON
STEP = cp07.STEP
MAX_ORIGINS = cp07.MAX_ORIGINS
MAX_MINIMA = cp07.MAX_MINIMA
TRACK_EPSILON = cp07.TRACK_EPSILON
CANDIDATE_SPACING = cp07.CANDIDATE_SPACING

RULES = ("pooled_cv_same_config", "last", "recency_hl3")
LABELS = {
    "pooled_cv_same_config": "Pooled CV",
    "last": "Latest minimum",
    "recency_hl3": "Recency mean",
}
COLORS = {
    "pooled_cv_same_config": "#4477aa",
    "last": "#cc8844",
    "recency_hl3": "#228877",
}
BLOCK_SHADE = {
    "train": "#ededed",
    "val1": "#dfeaf4",
    "val2": "#f8e8d5",
    "current": "#e3f1e8",
    "test": "#f4dfe1",
}


def _positions(n: int, split) -> dict[str, tuple[int, int]]:
    """Partition a fixed case by *observed* index, without overlapping data."""
    val1_start, val1_end = int(split.validation.start), int(split.validation.stop)
    out = {
        "train": (val1_start - WINDOW, val1_start),
        "val1": (val1_start, val1_end),
        "val2": (val1_end, val1_end + HORIZON),
        "current": (n - 2 * HORIZON, n - HORIZON),
        "test": (n - HORIZON, n),
    }
    for start, end in out.values():
        if not (0 <= start < end <= n):
            raise ValueError("Invalid chronological region.")
    for first, second in zip(out.values(), list(out.values())[1:]):
        if first[1] > second[0]:
            raise ValueError("Train / Val1 / Val2 / final Val1 / test overlap.")
    return out


def _load_example() -> dict:
    cp07._register_simulation_key(KEY)
    frame = cp07.simulate_log_series(
        mechanism=MECHANISM, observation_noise_sd=NOISE_SD, seed=SEED,
    )
    stops = cp04._outer_stops(
        len(frame), horizon=HORIZON,
        development_blocks=cp07.OUTER_BLOCKS, holdout_blocks=0,
    )
    case = frame.iloc[:int(stops[OUTER_NUMBER - 1])].copy()
    history = case.iloc[:-2 * HORIZON].copy()
    pretest = case.iloc[:-HORIZON].copy()
    test = case.iloc[-HORIZON:].copy()

    splits = tracked._paired_splits(
        len(history), window=WINDOW, horizon=HORIZON,
        step=STEP, max_origins=MAX_ORIGINS,
    )
    tracks, _ = tracked._track_order_minima(
        KEY, history, order=ORDER, window=WINDOW,
        splits=splits, max_minima=MAX_MINIMA,
        track_epsilon=TRACK_EPSILON,
        candidate_spacing=CANDIDATE_SPACING,
    )
    summary = tracked._summarize_branches(tracks, selection_metric="log_rmse")
    continuations = cp06._final_continuations_subset(
        KEY, case, summary, orders=(ORDER,),
    )
    selected = cp04._select_branch(summary, continuations)
    selected_branch = str(selected["branch_id"])
    current_s = float(selected["final_smoothness"])
    branch_rows = tracks.loc[tracks["branch_id"].eq(selected_branch)].copy()
    rule_frame = evaluate_rule_set(
        branch_rows, current_s=current_s, val2_loss_column="val2_log_rmse",
    )
    rule_frame = rule_frame.loc[
        rule_frame["rule"].isin(("last", "recency_hl3"))
    ]
    pooled_s, pooled_score, _ = cp04._pooled_smoothness(
        KEY, pretest, order=ORDER, window=WINDOW, max_origins=MAX_ORIGINS,
    )
    decisions = {"pooled_cv_same_config": float(pooled_s)}
    for _, row in rule_frame.iterrows():
        decisions[str(row["rule"])] = float(row["selected_s"])
    if set(decisions) != set(RULES):
        raise RuntimeError("Expected pooled/last/recency smoothness decisions missing.")
    if not np.isclose(decisions["last"], current_s):
        raise RuntimeError("Latest minimum must equal the continued final Val1 minimum.")

    example_split = splits[-1]
    regions = _positions(len(case), example_split)
    test_start = regions["test"][0]
    if not (int(regions["val2"][1]) <= int(regions["current"][0]) <= test_start):
        raise RuntimeError("Validation is not strictly before test.")

    # Historical Val1 and Val2 example. S is taken from a matched minimum
    # of that historical origin, with no use of the later outer-test data.
    candidates = tracks.loc[
        tracks["origin_number"].eq(len(splits)) &
        tracks["status"].eq("matched")
    ].sort_values(["val1_loss", "smoothness"])
    if candidates.empty:
        raise RuntimeError("Illustrative historical origin has no matched local minimum.")
    historical_s = float(candidates.iloc[0]["smoothness"])

    # The final current-Val1 loss curve uses only pretest data. In particular,
    # the observed *test* path is NEVER an input to the objective.
    split_final = tracked._final_validation_split(
        pretest, window=WINDOW, horizon=HORIZON,
    )
    prepared = td.prepare_rolling_pure_forecast_objective(
        np.log(pretest["value"].to_numpy(dtype=float)),
        [split_final], order=ORDER,
    )
    minima, _ = tracked._surface_candidates(
        prepared, order=ORDER, window=WINDOW, spacing=CANDIDATE_SPACING,
    )

    return {
        "case": case, "history": history, "pretest": pretest, "test": test,
        "splits": splits, "regions": regions, "tracks": tracks,
        "summary": summary, "branch_id": selected_branch,
        "current_s": current_s, "decisions": decisions,
        "historical_s": historical_s, "prepared": prepared,
        "final_minima": minima, "pooled_cv_score": float(pooled_score),
    }


def _trend_and_forecast(values: np.ndarray, smoothness: float, horizon: int):
    model = td.PurePenalizedTrend(
        order=ORDER, smoothness=float(smoothness),
    ).fit(np.log(np.asarray(values, dtype=float)))
    return (
        np.asarray(model.trend_, dtype=float),
        np.asarray(model.forecast(horizon), dtype=float),
    )


def _historical_forecasts(example: dict) -> tuple[np.ndarray, np.ndarray]:
    hist = example["history"]
    regions = example["regions"]
    val1_start, val1_end = regions["val1"]
    _, val2_end = regions["val2"]
    s = example["historical_s"]
    _, forecast1 = _trend_and_forecast(
        hist["value"].iloc[val1_start - WINDOW:val1_start].to_numpy(), s,
        HORIZON,
    )
    _, forecast2 = _trend_and_forecast(
        hist["value"].iloc[val1_end - WINDOW:val1_end].to_numpy(), s,
        HORIZON,
    )
    if not (len(forecast1) == len(forecast2) == HORIZON):
        raise RuntimeError("Unexpected historical validation length.")
    if val2_end > len(hist):
        raise RuntimeError("Validation 2 would use unavailable history.")
    return forecast1, forecast2


def _objective_values(prepared, grid: np.ndarray) -> np.ndarray:
    results = []
    for s in grid:
        lam = (
            float("inf") if s >= 1.0
            else td.smoothness_to_lambda(float(s), n_obs=WINDOW, order=ORDER)
        )
        results.append(float(prepared.evaluate(lam).value))
    return np.asarray(results, dtype=float)


def _style_ax(ax, label: str, title: str):
    ax.set_title(f"{label}  {title}", loc="left", fontsize=10.5, pad=7)
    ax.grid(axis="y", alpha=0.16)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)


def _date_axis(ax):
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=4, maxticks=8))
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))


def _panel_a(ax, ex: dict):
    case = ex["case"]
    dates = pd.to_datetime(case["date"])
    y = np.log(case["value"].to_numpy())
    areas = ex["regions"]
    labels = [
        ("train", "Train"), ("val1", "Val1"),
        ("val2", "Val2"), ("current", "Final Val1"),
        ("test", "Test"),
    ]
    for code, label in labels:
        i, j = areas[code]
        ax.axvspan(dates.iloc[i], dates.iloc[j - 1], color=BLOCK_SHADE[code], alpha=0.82)
        ax.text(
            dates.iloc[(i + j - 1) // 2], 0.94, label,
            ha="center", va="top", transform=ax.get_xaxis_transform(),
            fontsize=7.7,
        )
        ax.axvline(dates.iloc[i], linewidth=0.7, linestyle=":", color="0.6")
    lower = areas["train"][0]
    ax.plot(dates.iloc[lower:], y[lower:], color="#292929", lw=1.25, label="Observed")
    forecast1, forecast2 = _historical_forecasts(ex)
    for region, path, label, style in [
        ("val1", forecast1, "Historical Val1 forecast", "#4477aa"),
        ("val2", forecast2, "Refitted Val2 forecast", "#cc8844"),
    ]:
        i, j = areas[region]
        ax.plot(
            dates.iloc[i:j], path, lw=1.35, linestyle="--",
            color=style, label=label,
        )
    ax.legend(loc="lower left", ncol=3, frameon=False, fontsize=7.5)
    ax.set_ylabel("Log level")
    ax.set_xlim(dates.iloc[lower], dates.iloc[-1])
    _style_ax(ax, "A", "Chronology: historical validation, current Val1, outer test")
    _date_axis(ax)


def _panel_b(ax, ex: dict):
    pretest = ex["pretest"]
    training = pretest.tail(WINDOW)
    dates = pd.to_datetime(training["date"])
    observed = np.log(training["value"].to_numpy())
    ax.plot(dates, observed, color="#303030", lw=1.0, alpha=0.58, label="Observed")
    for rule in RULES:
        s = ex["decisions"][rule]
        trend, _ = _trend_and_forecast(training["value"].to_numpy(), s, HORIZON)
        ax.plot(
            dates, trend, color=COLORS[rule], lw=1.7,
            label=f"{LABELS[rule]} ($S={s:.3f}$)",
        )
    ax.set_ylabel("Log level")
    ax.legend(ncol=2, frameon=False, fontsize=7.8, loc="upper left")
    _style_ax(ax, "B", "Fresh trend fit on the last L observations")
    _date_axis(ax)


def _panel_c(ax, ex: dict):
    pretest, test = ex["pretest"], ex["test"]
    recent = pretest.tail(2 * HORIZON)
    dx = pd.to_datetime(recent["date"])
    dy = pd.to_datetime(test["date"])
    observed = np.log(recent["value"].to_numpy())
    truth = np.log(test["value"].to_numpy())
    ax.plot(dx, observed, color="#303030", lw=1.3, label="Observed before test")
    ax.plot(dy, truth, color="#303030", lw=1.5, marker=".", ms=3.5, label="Test realization")
    ax.axvspan(dy.iloc[0], dy.iloc[-1], color=BLOCK_SHADE["test"], alpha=0.75)
    ax.axvline(dy.iloc[0], color="0.45", lw=0.9, linestyle=":")
    for rule in RULES:
        _, forecast = _trend_and_forecast(
            pretest["value"].tail(WINDOW).to_numpy(),
            ex["decisions"][rule], HORIZON,
        )
        ax.plot(dy, forecast, color=COLORS[rule], lw=1.75, label=LABELS[rule])
    ax.set_ylabel("Log level")
    ax.legend(loc="upper left", ncol=3, frameon=False, fontsize=7.4)
    _style_ax(ax, "C", "Test forecasts: same data, different smoothness decisions")
    _date_axis(ax)


def _panel_d(ax, ex: dict):
    grid = np.linspace(0.0, 1.0, 301)
    values = _objective_values(ex["prepared"], grid)
    ax.plot(grid, values, color="#353535", lw=1.55, label="Current Val1 loss")
    minima = ex["final_minima"]
    for j, candidate in enumerate(minima):
        s = float(candidate["smoothness"])
        ax.plot(
            s, _objective_values(ex["prepared"], np.asarray([s]))[0],
            "o", ms=5, mfc="white", mec="0.3", mew=1.0,
            label="Detected local minimum" if j == 0 else None,
        )
    for rule in RULES:
        s = ex["decisions"][rule]
        ax.axvline(
            s, color=COLORS[rule], linestyle="--", lw=1.2,
            label=f"{LABELS[rule]}: {s:.3f}",
        )
    ax.set_xlim(0, 1)
    ax.set_xlabel("Normalized smoothness $S$")
    ax.set_ylabel("Val1 MSE (log)")
    ax.legend(loc="best", frameon=False, ncol=2, fontsize=7.4)
    _style_ax(ax, "D", "Final Val1 objective (test observations excluded)")


def _panel_e(ax, ex: dict):
    tracks = ex["tracks"]
    winner = ex["branch_id"]
    for branch_id, group in tracks.groupby("branch_id", sort=False):
        matched = group.loc[group["status"].eq("matched")].sort_values("origin_number")
        if matched.empty:
            continue
        primary = str(branch_id) == winner
        ax.plot(
            matched["origin_number"], matched["smoothness"],
            lw=2.0 if primary else 1.05,
            color="#7755a5" if primary else "#bdbdbd",
            marker="o" if primary else ".", ms=3.5 if primary else 2.5,
            alpha=0.95 if primary else 0.65,
            label="Selected historical branch" if primary else None,
        )
    end = int(tracks["origin_number"].max())
    ax.plot(
        end + 1, ex["current_s"], "*", ms=11,
        color="#7755a5", label="Continued current minimum",
    )
    for i, rule in enumerate(RULES):
        ax.scatter(
            end + 2 + 0.18 * i, ex["decisions"][rule],
            s=45, marker="D", color=COLORS[rule], label=LABELS[rule],
            zorder=4,
        )
    ax.axvline(end + 0.5, lw=0.8, linestyle=":", color="0.5")
    ax.set_xlim(1, end + 4)
    ax.set_ylim(-0.035, 1.045)
    ax.set_xlabel("Historical paired origin  →  final decision")
    ax.set_ylabel("Smoothness $S$")
    ax.legend(loc="best", ncol=2, frameon=False, fontsize=7.3)
    _style_ax(ax, "E", "Tracked minima and maps $\\phi(V_j)$ to current $S$")


def make_figure(output_dir: Path = FIGURES_DIR) -> dict:
    ex = _load_example()
    output_dir.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9.0,
        "axes.linewidth": 0.75, "savefig.facecolor": "white",
    })
    fig, axes = plt.subplots(
        5, 1, figsize=(8.6, 10.4),
        gridspec_kw={"height_ratios": (1.5, 1.15, 1.15, 1.1, 1.25)},
    )
    _panel_a(axes[0], ex)
    _panel_b(axes[1], ex)
    _panel_c(axes[2], ex)
    _panel_d(axes[3], ex)
    _panel_e(axes[4], ex)
    fig.subplots_adjust(
        left=0.12, right=0.985, top=0.975, bottom=0.055, hspace=0.47,
    )
    pdf = output_dir / f"{NAME}.pdf"
    png = output_dir / f"{NAME}.png"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=240, bbox_inches="tight")
    plt.close(fig)

    regions = {
        key: [int(a), int(b)] for key, (a, b) in ex["regions"].items()
    }
    info = {
        "figure": NAME,
        "role": "pedagogical fixed-case example, not rule selection",
        "source": "CP07 synthetic DGP; CP04/CP06/CP07 frozen evaluation helpers",
        "seed": SEED, "mechanism": MECHANISM, "noise_sd": NOISE_SD,
        "outer_number": OUTER_NUMBER,
        "horizon": HORIZON, "order": ORDER, "window": WINDOW,
        "track_epsilon": TRACK_EPSILON,
        "candidate_spacing": CANDIDATE_SPACING,
        "outer_test_used_for_selection": False,
        "historical_val1_val2_example_s": ex["historical_s"],
        "selected_branch_id": ex["branch_id"],
        "current_val1_smoothness": ex["current_s"],
        "rules_selected_s": ex["decisions"],
        "regions_half_open_index": regions,
        "explanation": (
            "Historical Val1 and Val2 are paired; the current/final Val1 "
            "is later and updates the chosen branch before the untouched test. "
            "Panel D displays only final Val1 loss, never test loss."
        ),
    }
    (output_dir / f"{NAME}.json").write_text(
        json.dumps(info, indent=2), encoding="utf-8"
    )
    print(f"Figure: {pdf}")
    print(f"Preview: {png}")
    print(f"Provenance: {output_dir / (NAME + '.json')}")
    print("S decisions:", ex["decisions"])
    return info


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=FIGURES_DIR)
    args = parser.parse_args()
    make_figure(args.output_dir)


if __name__ == "__main__":
    main()
