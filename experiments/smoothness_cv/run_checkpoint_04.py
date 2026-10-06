from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
import multiprocessing as mp
import os
from pathlib import Path
import subprocess
import sys
import time

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import trend_estimation as td
from experiments.numerical_smoothness_selection import (
    run_applied_case_studies as applied,
)
from experiments.numerical_smoothness_selection import (
    run_two_stage_order_validation as tracked,
)
from experiments.smoothness_cv.dynamic_branch_rules import evaluate_rule_set


RESULT_ROOT = Path("results") / "smoothness_cv" / "checkpoint_04"


@dataclass(frozen=True)
class CP04Preset:
    name: str
    series: tuple[str, ...]
    development_outer_blocks: int
    confirmation_holdout_blocks: int
    max_origins_override: int | None
    windows_override: dict[str, tuple[int, ...]]


PRESETS = {
    "smoke": CP04Preset(
        name="smoke",
        series=("GDPC1",),
        development_outer_blocks=2,
        confirmation_holdout_blocks=1,
        max_origins_override=6,
        windows_override={"GDPC1": (40,)},
    ),
    "refine": CP04Preset(
        name="refine",
        series=("GDPC1", "SPY", "AAPL", "BTC-USD"),
        development_outer_blocks=6,
        confirmation_holdout_blocks=4,
        max_origins_override=None,
        windows_override={},
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Checkpoint 04 development experiment: compare branch-to-smoothness "
            "rules on repeated chronological outer tests while reserving the "
            "latest blocks for a later confirmatory run."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument(
        "--selection-metric",
        choices=("level_rmse", "log_rmse"),
        default="level_rmse",
    )
    parser.add_argument("--track-epsilon", type=float, default=0.10)
    parser.add_argument("--candidate-spacing", type=float, default=0.02)
    parser.add_argument("--max-minima", type=int, default=5)
    parser.add_argument(
        "--jobs",
        type=int,
        default=0,
        help="0=auto (all but one logical CPU, capped at 16); 1=serial.",
    )
    parser.add_argument("--output-dir", type=Path, default=None)
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


def _default_run_dir(preset: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return RESULT_ROOT / f"{stamp}_{preset}_{_git_short_sha()}"


def _resolve_jobs(requested: int) -> int:
    if requested < 0:
        raise ValueError("--jobs must be 0 or a positive integer.")
    if requested == 1:
        return 1
    cpu = int(os.cpu_count() or 1)
    if requested == 0:
        return max(1, min(16, cpu - 1 if cpu > 1 else 1))
    if os.name == "nt" and requested > 61:
        raise ValueError("Windows ProcessPoolExecutor supports at most 61 workers.")
    return requested


def _windows_for(key: str, preset: CP04Preset) -> tuple[int, ...]:
    if key in preset.windows_override:
        return tuple(int(v) for v in preset.windows_override[key])
    return tuple(int(v) for v in applied.SERIES[key]["windows"])


def _outer_stops(
    n_obs: int,
    *,
    horizon: int,
    development_blocks: int,
    holdout_blocks: int,
) -> list[int]:
    latest_development_stop = n_obs - holdout_blocks * horizon
    stops = [
        latest_development_stop - offset * horizon
        for offset in range(development_blocks - 1, -1, -1)
    ]
    if not stops or min(stops) <= 3 * horizon:
        raise ValueError("Insufficient history for requested CP04 outer blocks.")
    return stops


def _final_continuations(
    key: str,
    case_frame: pd.DataFrame,
    summaries: pd.DataFrame,
    *,
    track_epsilon: float,
    candidate_spacing: float,
) -> pd.DataFrame:
    """Continue branches on final Val1 without evaluating the outer test."""

    horizon = int(applied.SERIES[key]["test_reserve"])
    pretest = case_frame.iloc[:-horizon].copy()
    pretest_log = np.log(pretest["value"].to_numpy(dtype=float))
    rows: list[dict] = []

    for order in tracked.ORDERS:
        order_summary = summaries.loc[summaries["order"].eq(order)].copy()
        if order_summary.empty:
            continue
        window = int(order_summary["window"].iloc[0])
        split = tracked._final_validation_split(
            pretest,
            window=window,
            horizon=horizon,
        )
        prepared = td.prepare_rolling_pure_forecast_objective(
            pretest_log,
            [split],
            order=order,
        )
        candidates, evaluations = tracked._surface_candidates(
            prepared,
            order=order,
            window=window,
            spacing=candidate_spacing,
        )
        previous = {
            str(row["branch_id"]): float(row["smoothness_last"])
            for _, row in order_summary.iterrows()
        }
        matches, _ = tracked._match_branches(
            previous,
            candidates,
            epsilon=track_epsilon,
        )

        for _, summary in order_summary.iterrows():
            branch_id = str(summary["branch_id"])
            if branch_id not in matches:
                rows.append(
                    {
                        "series": key,
                        "branch_id": branch_id,
                        "order": order,
                        "window": window,
                        "final_continuation": False,
                        "final_smoothness": np.nan,
                        "final_delta_s": np.nan,
                        "final_val1_loss": np.nan,
                        "final_objective_evaluations": evaluations,
                    }
                )
                continue
            candidate_idx, distance = matches[branch_id]
            candidate = candidates[candidate_idx]
            rows.append(
                {
                    "series": key,
                    "branch_id": branch_id,
                    "order": order,
                    "window": window,
                    "final_continuation": True,
                    "final_smoothness": float(candidate["smoothness"]),
                    "final_delta_s": float(distance),
                    "final_val1_loss": float(candidate["val1_loss"]),
                    "final_objective_evaluations": evaluations,
                }
            )
    return pd.DataFrame(rows)


def _select_branch(
    summary: pd.DataFrame,
    continuations: pd.DataFrame,
) -> pd.Series:
    merged = summary.merge(
        continuations,
        on=["series", "branch_id", "order", "window"],
        how="left",
        validate="one_to_one",
    )
    eligible = merged.loc[merged["final_continuation"].fillna(False)].copy()
    if eligible.empty:
        raise RuntimeError("No branch continues to the current pre-test surface.")
    complete = eligible.loc[np.isclose(eligible["support_fraction"], 1.0)].copy()
    if not complete.empty:
        pool = complete
    else:
        max_support = float(eligible["support_fraction"].max())
        pool = eligible.loc[np.isclose(eligible["support_fraction"], max_support)]
    return pool.sort_values(
        ["selection_score", "order", "branch_id"],
        ascending=[True, True, True],
    ).iloc[0]


def _fit_and_score(
    pretest: pd.DataFrame,
    true_test: pd.DataFrame,
    *,
    order: int,
    window: int,
    smoothness: float,
) -> tuple[dict, pd.DataFrame]:
    train = pretest.tail(window).copy()
    model = td.PurePenalizedTrend(
        order=order,
        smoothness=float(smoothness),
    ).fit(np.log(train["value"].to_numpy(dtype=float)))
    forecast_log = np.asarray(model.forecast(len(true_test)), dtype=float)
    forecast_level = tracked._safe_levels(forecast_log)
    observed_level = true_test["value"].to_numpy(dtype=float)
    observed_log = np.log(observed_level)
    level_error = observed_level - forecast_level
    log_error = observed_log - forecast_log
    metrics = {
        "level_mse": float(np.mean(level_error**2)),
        "level_rmse": float(np.sqrt(np.mean(level_error**2))),
        "level_mae": float(np.mean(np.abs(level_error))),
        "log_mse": float(np.mean(log_error**2)),
        "log_rmse": float(np.sqrt(np.mean(log_error**2))),
        "log_mae": float(np.mean(np.abs(log_error))),
    }
    path = true_test[["date", "value"]].copy()
    path = path.rename(columns={"value": "observed"})
    path["forecast"] = forecast_level
    return metrics, path


def _pooled_smoothness(
    key: str,
    pretest: pd.DataFrame,
    *,
    order: int,
    window: int,
    max_origins: int,
) -> tuple[float, float, int]:
    spec = applied.SERIES[key]
    horizon = int(spec["test_reserve"])
    values = np.log(pretest["value"].to_numpy(dtype=float))
    splits = td.rolling_origin_splits(
        len(values),
        initial_train=window,
        horizon=horizon,
        step=int(spec["step"]),
        expanding=False,
        train_window=window,
    )
    splits = splits[-max_origins:]
    if not splits:
        raise RuntimeError("No pooled forecast-CV origins are available.")
    prepared = td.prepare_rolling_pure_forecast_objective(
        values,
        splits,
        order=order,
    )
    _, candidates, evaluations = applied._search_candidates(
        prepared,
        order=order,
        window=window,
    )
    best = candidates[0]
    return float(best["smoothness"]), float(best["cv_error"]), int(evaluations)


def _run_outer_task(task: tuple) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    (
        key,
        outer_number,
        outer_stop,
        preset_name,
        selection_metric,
        track_epsilon,
        candidate_spacing,
        max_minima,
    ) = task
    preset = PRESETS[preset_name]
    spec = applied.SERIES[key]
    horizon = int(spec["test_reserve"])
    frame = applied._load_series(key)
    case_frame = frame.iloc[: int(outer_stop)].copy()
    if len(case_frame) <= 3 * horizon:
        raise RuntimeError(f"Outer origin too early for {key}: {outer_stop}")

    history = case_frame.iloc[: -2 * horizon].copy()
    pretest = case_frame.iloc[:-horizon].copy()
    true_test = case_frame.iloc[-horizon:].copy()
    max_origins = (
        int(preset.max_origins_override)
        if preset.max_origins_override is not None
        else int(spec["max_origins"])
    )

    window_selection, splits_by_order = tracked._select_window_per_order(
        key,
        history,
        windows=_windows_for(key, preset),
        max_origins=max_origins,
    )

    track_frames: list[pd.DataFrame] = []
    for _, selected in window_selection.iterrows():
        order = int(selected["order"])
        track, _ = tracked._track_order_minima(
            key,
            history,
            order=order,
            window=int(selected["window"]),
            splits=splits_by_order[order],
            max_minima=int(max_minima),
            track_epsilon=float(track_epsilon),
            candidate_spacing=float(candidate_spacing),
        )
        track_frames.append(track)
    tracks = pd.concat(track_frames, ignore_index=True)
    summary = tracked._summarize_branches(
        tracks,
        selection_metric=selection_metric,
    )
    continuations = _final_continuations(
        key,
        case_frame,
        summary,
        track_epsilon=track_epsilon,
        candidate_spacing=candidate_spacing,
    )
    winner = _select_branch(summary, continuations)
    branch_id = str(winner["branch_id"])
    order = int(winner["order"])
    window = int(winner["window"])
    current_s = float(winner["final_smoothness"])

    branch_history = tracks.loc[tracks["branch_id"].eq(branch_id)].copy()
    val2_column = (
        "val2_level_rmse"
        if selection_metric == "level_rmse"
        else "val2_log_rmse"
    )
    rules = evaluate_rule_set(
        branch_history,
        current_s=current_s,
        val2_loss_column=val2_column,
    )

    pooled_s, pooled_score, pooled_evaluations = _pooled_smoothness(
        key,
        pretest,
        order=order,
        window=window,
        max_origins=max_origins,
    )
    rules = pd.concat(
        [
            rules,
            pd.DataFrame(
                [
                    {
                        "rule": "pooled_cv_same_config",
                        "rule_family": "pooled_cv",
                        "k": np.nan,
                        "half_life": np.nan,
                        "selected_s": pooled_s,
                        "n_history_used": max_origins,
                        "includes_current_s": True,
                        "delta": np.nan,
                        "rho": np.nan,
                    }
                ]
            ),
        ],
        ignore_index=True,
    )

    common = {
        "series": key,
        "family": spec["family"],
        "outer_number": int(outer_number),
        "outer_stop": int(outer_stop),
        "test_start_date": str(true_test["date"].iloc[0].date()),
        "test_end_date": str(true_test["date"].iloc[-1].date()),
        "horizon": horizon,
        "selected_branch": branch_id,
        "order": order,
        "window": window,
        "branch_support_fraction": float(winner["support_fraction"]),
        "branch_n_matched": int(winner["n_matched_origins"]),
        "branch_n_possible": int(winner["n_possible_origins"]),
        "branch_selection_score": float(winner["selection_score"]),
        "current_s": current_s,
        "current_val1_loss": float(winner["final_val1_loss"]),
        "pooled_cv_score": pooled_score,
        "pooled_objective_evaluations": pooled_evaluations,
    }

    decision_rows: list[dict] = []
    forecast_rows: list[dict] = []
    for _, rule in rules.iterrows():
        metrics, path = _fit_and_score(
            pretest,
            true_test,
            order=order,
            window=window,
            smoothness=float(rule["selected_s"]),
        )
        row = {
            **common,
            "rule": str(rule["rule"]),
            "rule_family": str(rule["rule_family"]),
            "selected_s": float(rule["selected_s"]),
            "s_minus_current": float(rule["selected_s"] - current_s),
            "k": rule.get("k", np.nan),
            "half_life": rule.get("half_life", np.nan),
            "n_history_used": int(rule.get("n_history_used", 0)),
            "includes_current_s": bool(rule.get("includes_current_s", False)),
            "delta": rule.get("delta", np.nan),
            "rho": rule.get("rho", np.nan),
            **metrics,
        }
        decision_rows.append(row)
        for _, p in path.iterrows():
            forecast_rows.append(
                {
                    **{k: common[k] for k in (
                        "series", "family", "outer_number", "outer_stop",
                        "test_start_date", "test_end_date", "horizon",
                        "selected_branch", "order", "window"
                    )},
                    "rule": str(rule["rule"]),
                    "selected_s": float(rule["selected_s"]),
                    "date": str(pd.Timestamp(p["date"]).date()),
                    "observed": float(p["observed"]),
                    "forecast": float(p["forecast"]),
                }
            )

    track_records = tracks.copy()
    track_records["outer_number"] = int(outer_number)
    track_records["outer_stop"] = int(outer_stop)
    track_records["test_start_date"] = common["test_start_date"]
    track_records["test_end_date"] = common["test_end_date"]

    window_records = window_selection.copy()
    window_records["outer_number"] = int(outer_number)
    window_records["outer_stop"] = int(outer_stop)

    return (
        decision_rows,
        forecast_rows,
        track_records.to_dict("records"),
        window_records.to_dict("records"),
    )


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    if not 0.0 < args.track_epsilon <= 1.0:
        raise ValueError("--track-epsilon must be in (0, 1].")
    if not 0.0 < args.candidate_spacing <= 1.0:
        raise ValueError("--candidate-spacing must be in (0, 1].")
    if args.max_minima < 1 or args.max_minima > 5:
        raise ValueError("--max-minima must be between 1 and 5.")

    jobs = _resolve_jobs(args.jobs)
    run_dir = args.output_dir or _default_run_dir(preset.name)
    run_dir.mkdir(parents=True, exist_ok=True)

    tasks: list[tuple] = []
    outer_manifest: list[dict] = []
    for key in preset.series:
        frame = applied._load_series(key)
        horizon = int(applied.SERIES[key]["test_reserve"])
        stops = _outer_stops(
            len(frame),
            horizon=horizon,
            development_blocks=preset.development_outer_blocks,
            holdout_blocks=preset.confirmation_holdout_blocks,
        )
        for outer_number, stop in enumerate(stops, start=1):
            tasks.append(
                (
                    key,
                    outer_number,
                    stop,
                    preset.name,
                    args.selection_metric,
                    float(args.track_epsilon),
                    float(args.candidate_spacing),
                    int(args.max_minima),
                )
            )
            outer_manifest.append(
                {
                    "series": key,
                    "outer_number": outer_number,
                    "outer_stop": stop,
                    "horizon": horizon,
                    "confirmation_holdout_blocks": preset.confirmation_holdout_blocks,
                }
            )

    print(
        f"CP04 preset={preset.name}: {len(tasks)} outer decisions, jobs={jobs}",
        flush=True,
    )
    started = time.perf_counter()
    decision_rows: list[dict] = []
    forecast_rows: list[dict] = []
    track_rows: list[dict] = []
    window_rows: list[dict] = []

    if jobs == 1:
        iterator = map(_run_outer_task, tasks)
        for completed, result in enumerate(iterator, start=1):
            d, p, t, w = result
            decision_rows.extend(d)
            forecast_rows.extend(p)
            track_rows.extend(t)
            window_rows.extend(w)
            print(f"    [{completed}/{len(tasks)}]", flush=True)
    else:
        context = mp.get_context("spawn")
        with ProcessPoolExecutor(max_workers=jobs, mp_context=context) as executor:
            iterator = executor.map(_run_outer_task, tasks, chunksize=1)
            for completed, result in enumerate(iterator, start=1):
                d, p, t, w = result
                decision_rows.extend(d)
                forecast_rows.extend(p)
                track_rows.extend(t)
                window_rows.extend(w)
                if completed == 1 or completed % max(1, len(tasks) // 20) == 0 or completed == len(tasks):
                    elapsed = time.perf_counter() - started
                    rate = elapsed / completed
                    eta = rate * (len(tasks) - completed)
                    print(
                        f"    [{completed}/{len(tasks)}] elapsed={elapsed/60:.1f}m "
                        f"eta={eta/60:.1f}m",
                        flush=True,
                    )

    decisions = pd.DataFrame(decision_rows).sort_values(
        ["series", "outer_number", "rule"]
    ).reset_index(drop=True)
    forecasts = pd.DataFrame(forecast_rows).sort_values(
        ["series", "outer_number", "rule", "date"]
    ).reset_index(drop=True)
    tracks = pd.DataFrame(track_rows).sort_values(
        ["series", "outer_number", "order", "branch_id", "origin_number"]
    ).reset_index(drop=True)
    windows = pd.DataFrame(window_rows).sort_values(
        ["series", "outer_number", "order"]
    ).reset_index(drop=True)

    decisions.to_csv(run_dir / "decision_results.csv", index=False)
    forecasts.to_csv(run_dir / "forecast_paths.csv.gz", index=False, compression="gzip")
    tracks.to_csv(run_dir / "branch_states.csv.gz", index=False, compression="gzip")
    windows.to_csv(run_dir / "window_selection.csv", index=False)
    pd.DataFrame(outer_manifest).to_csv(run_dir / "outer_manifest.csv", index=False)

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "checkpoint": "04",
        "stage": "development_rule_refinement",
        "preset": preset.name,
        "preset_definition": asdict(preset),
        "selection_metric": args.selection_metric,
        "track_epsilon": float(args.track_epsilon),
        "candidate_spacing": float(args.candidate_spacing),
        "max_minima": int(args.max_minima),
        "jobs": jobs,
        "rule_set": [
            "last",
            "mean_k3",
            "mean_k5",
            "median_k3",
            "median_k5",
            "val2_weighted",
            "recency_val2_hl3",
            "recency_val2_hl5",
            "recency_val2_hl10",
            "pooled_cv_same_config",
        ],
        "confirmation_region_used": False,
        "confirmation_holdout_blocks": preset.confirmation_holdout_blocks,
        "weighted_rule_note": (
            "Loss-weighted rules use only completed historical Validation-2 "
            "rows. The current local minimum has no Val2 weight because its "
            "following block is the untouched outer test."
        ),
        "n_outer_decisions": len(tasks),
        "elapsed_seconds": time.perf_counter() - started,
    }
    (run_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )
    latest = RESULT_ROOT / "LATEST.txt"
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text(run_dir.as_posix() + "\n", encoding="utf-8")

    print("")
    print(f"Checkpoint 04 development run complete: {run_dir}")
    print(f"Outer decisions: {len(tasks)}")
    print("Latest confirmation blocks remain untouched.")
    print(
        "Next: python experiments/smoothness_cv/analyze_checkpoint_04.py "
        f"--run-dir {run_dir}"
    )


if __name__ == "__main__":
    main()
