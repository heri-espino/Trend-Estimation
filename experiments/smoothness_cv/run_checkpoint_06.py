from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
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
from experiments.smoothness_cv import run_checkpoint_04 as cp04
from experiments.smoothness_cv import run_checkpoint_05 as cp05


RESULT_ROOT = Path("results") / "smoothness_cv" / "checkpoint_06"
HORIZON = 60
WINDOWS = (63, 126, 252, 504)
MAX_ORIGINS = 30
STEP = 5
TRACK_EPSILON = 0.10
CANDIDATE_SPACING = 0.02
MAX_MINIMA = 5

ORDER_SETS = {
    "d1234": (1, 2, 3, 4),
    "d123": (1, 2, 3),
    "d12": (1, 2),
    "d2": (2,),
}


@dataclass(frozen=True)
class CP06Preset:
    name: str
    series: tuple[str, ...]
    order_sets: tuple[str, ...]
    outer_blocks: int
    holdout_blocks: int
    max_origins: int
    windows: tuple[int, ...]


PRESETS = {
    "smoke": CP06Preset(
        name="smoke",
        series=("IVV", "AMZN", "SOL-USD"),
        order_sets=("d1234", "d12"),
        outer_blocks=2,
        holdout_blocks=4,
        max_origins=8,
        windows=(63, 252),
    ),
    "mechanism": CP06Preset(
        name="mechanism",
        series=cp05.PANEL_SERIES,
        order_sets=("d1234", "d123", "d12", "d2"),
        outer_blocks=8,
        holdout_blocks=4,
        max_origins=MAX_ORIGINS,
        windows=WINDOWS,
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Checkpoint 06 post-hoc order-stability mechanism study using "
            "historical outer blocks that precede all CP05 test blocks."
        )
    )
    parser.add_argument("--preset", choices=tuple(PRESETS), default="smoke")
    parser.add_argument("--jobs", type=int, default=0)
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


def _resolve_jobs(requested: int) -> int:
    requested = int(requested)
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


def _default_run_dir(preset_name: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return RESULT_ROOT / f"{stamp}_{preset_name}_{_git_short_sha()}"


def _select_window_per_order_subset(
    key: str,
    history: pd.DataFrame,
    *,
    orders: tuple[int, ...],
    windows: tuple[int, ...],
    max_origins: int,
) -> tuple[pd.DataFrame, dict[int, list]]:
    """Choose L separately for each allowed d using historical Val1 only."""

    spec = applied.SERIES[key]
    horizon = int(spec["test_reserve"])
    history_log = np.log(history["value"].to_numpy(dtype=float))
    rows: list[dict] = []
    selected_splits: dict[int, list] = {}

    for order in orders:
        order_rows: list[dict] = []
        payloads: dict[int, list] = {}
        for window in windows:
            if int(window) + 2 * horizon > len(history_log):
                continue
            splits = tracked._paired_splits(
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
            raise RuntimeError(f"No valid rolling window for {key}, d={order}.")

        selected = (
            pd.DataFrame(order_rows)
            .sort_values(["aggregate_val1_loss", "window"], ascending=[True, True])
            .iloc[0]
            .to_dict()
        )
        rows.append(selected)
        selected_splits[int(order)] = payloads[int(selected["window"])]

    return (
        pd.DataFrame(rows).sort_values("order").reset_index(drop=True),
        selected_splits,
    )


def _final_continuations_subset(
    key: str,
    case_frame: pd.DataFrame,
    summaries: pd.DataFrame,
    *,
    orders: tuple[int, ...],
) -> pd.DataFrame:
    """Continue tracked branches to final Val1 using only allowed orders."""

    horizon = int(applied.SERIES[key]["test_reserve"])
    pretest = case_frame.iloc[:-horizon].copy()
    pretest_log = np.log(pretest["value"].to_numpy(dtype=float))
    rows: list[dict] = []

    for order in orders:
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
            spacing=CANDIDATE_SPACING,
        )
        previous = {
            str(row["branch_id"]): float(row["smoothness_last"])
            for _, row in order_summary.iterrows()
        }
        matches, _ = tracked._match_branches(
            previous,
            candidates,
            epsilon=TRACK_EPSILON,
        )

        for _, summary in order_summary.iterrows():
            branch_id = str(summary["branch_id"])
            if branch_id not in matches:
                rows.append(
                    {
                        "series": key,
                        "branch_id": branch_id,
                        "order": int(order),
                        "window": window,
                        "final_continuation": False,
                        "final_smoothness": np.nan,
                        "final_delta_s": np.nan,
                        "final_val1_loss": np.nan,
                        "final_objective_evaluations": int(evaluations),
                    }
                )
                continue
            candidate_idx, distance = matches[branch_id]
            candidate = candidates[candidate_idx]
            rows.append(
                {
                    "series": key,
                    "branch_id": branch_id,
                    "order": int(order),
                    "window": window,
                    "final_continuation": True,
                    "final_smoothness": float(candidate["smoothness"]),
                    "final_delta_s": float(distance),
                    "final_val1_loss": float(candidate["val1_loss"]),
                    "final_objective_evaluations": int(evaluations),
                }
            )
    return pd.DataFrame(rows)


def _run_outer_task(task: tuple) -> tuple[list[dict], list[dict]]:
    key, order_set_name, outer_number, outer_stop, preset_name = task
    preset = PRESETS[preset_name]
    orders = ORDER_SETS[order_set_name]
    spec = cp05._register_series(key)
    frame = applied._load_series(key)
    case_frame = frame.iloc[: int(outer_stop)].copy()
    history = case_frame.iloc[:-2 * HORIZON].copy()
    pretest = case_frame.iloc[:-HORIZON].copy()
    true_test = case_frame.iloc[-HORIZON:].copy()

    window_selection, splits_by_order = _select_window_per_order_subset(
        key,
        history,
        orders=orders,
        windows=preset.windows,
        max_origins=preset.max_origins,
    )

    track_frames: list[pd.DataFrame] = []
    for _, selected_window in window_selection.iterrows():
        order = int(selected_window["order"])
        track, _ = tracked._track_order_minima(
            key,
            history,
            order=order,
            window=int(selected_window["window"]),
            splits=splits_by_order[order],
            max_minima=MAX_MINIMA,
            track_epsilon=TRACK_EPSILON,
            candidate_spacing=CANDIDATE_SPACING,
        )
        track_frames.append(track)
    tracks = pd.concat(track_frames, ignore_index=True)
    summary = tracked._summarize_branches(
        tracks,
        selection_metric="level_rmse",
    )
    continuations = _final_continuations_subset(
        key,
        case_frame,
        summary,
        orders=orders,
    )

    fallback_used = False
    fallback_reason = ""
    try:
        winner = cp04._select_branch(summary, continuations)
        branch_id = str(winner["branch_id"])
        order = int(winner["order"])
        window = int(winner["window"])
        current_s = float(winner["final_smoothness"])
        branch_history = tracks.loc[tracks["branch_id"].eq(branch_id)].copy()
        branch_support = float(winner["support_fraction"])
        branch_score = float(winner["selection_score"])
    except RuntimeError:
        fallback_used = True
        fallback_reason = "no_branch_continued_to_final_val1"
        row = window_selection.sort_values(
            ["aggregate_val1_loss", "order", "window"],
            ascending=[True, True, True],
        ).iloc[0]
        order = int(row["order"])
        window = int(row["window"])
        branch_id = "fallback_pooled"
        current_s = None
        branch_history = None
        branch_support = np.nan
        branch_score = np.nan

    pooled_s, pooled_score, pooled_evaluations = cp05._pooled_for_config(
        key,
        pretest,
        order=order,
        window=window,
        max_origins=preset.max_origins,
    )
    rules = cp05._make_rule_rows(
        branch_history=branch_history,
        current_s=current_s,
        pooled_s=pooled_s,
        fallback_used=fallback_used,
    )

    common = {
        "series": key,
        "asset_class": spec["asset_class"],
        "order_set": order_set_name,
        "outer_number": int(outer_number),
        "outer_stop": int(outer_stop),
        "test_start_date": str(true_test["date"].iloc[0].date()),
        "test_end_date": str(true_test["date"].iloc[-1].date()),
        "order": order,
        "window": window,
        "selected_branch": branch_id,
        "branch_support_fraction": branch_support,
        "branch_selection_score": branch_score,
        "current_s": np.nan if current_s is None else current_s,
        "pooled_cv_score": float(pooled_score),
        "pooled_objective_evaluations": int(pooled_evaluations),
        "fallback_used": bool(fallback_used),
        "fallback_reason": fallback_reason,
    }

    decision_rows: list[dict] = []
    for _, rule in rules.iterrows():
        metrics, _ = cp04._fit_and_score(
            pretest,
            true_test,
            order=order,
            window=window,
            smoothness=float(rule["selected_s"]),
        )
        decision_rows.append(
            {
                **common,
                "rule": str(rule["rule"]),
                "rule_family": str(rule["rule_family"]),
                "selected_s": float(rule["selected_s"]),
                **metrics,
            }
        )

    window_rows = window_selection.copy()
    window_rows["series"] = key
    window_rows["asset_class"] = spec["asset_class"]
    window_rows["order_set"] = order_set_name
    window_rows["outer_number"] = int(outer_number)
    window_rows["outer_stop"] = int(outer_stop)

    return decision_rows, window_rows.to_dict("records")


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    jobs = _resolve_jobs(args.jobs)
    cp05._load_frozen_manifest()

    run_dir = args.output_dir or _default_run_dir(preset.name)
    run_dir.mkdir(parents=True, exist_ok=True)

    tasks: list[tuple] = []
    manifest_rows: list[dict] = []
    for key in preset.series:
        spec = cp05._register_series(key)
        frame = applied._load_series(key)
        stops = cp04._outer_stops(
            len(frame),
            horizon=HORIZON,
            development_blocks=preset.outer_blocks,
            holdout_blocks=preset.holdout_blocks,
        )
        for order_set_name in preset.order_sets:
            for outer_number, stop in enumerate(stops, start=1):
                tasks.append(
                    (key, order_set_name, outer_number, stop, preset.name)
                )
                manifest_rows.append(
                    {
                        "series": key,
                        "asset_class": spec["asset_class"],
                        "order_set": order_set_name,
                        "outer_number": outer_number,
                        "outer_stop": stop,
                        "horizon": HORIZON,
                        "cp05_holdout_blocks_skipped": preset.holdout_blocks,
                    }
                )

    print(
        f"CP06 preset={preset.name}: {len(preset.series)} series, "
        f"{len(preset.order_sets)} order sets, {len(tasks)} tasks, jobs={jobs}",
        flush=True,
    )
    started = time.perf_counter()
    decision_rows: list[dict] = []
    window_rows: list[dict] = []

    def consume(iterator):
        for completed, result in enumerate(iterator, start=1):
            d, w = result
            decision_rows.extend(d)
            window_rows.extend(w)
            if completed == 1 or completed % max(1, len(tasks) // 40) == 0 or completed == len(tasks):
                elapsed = time.perf_counter() - started
                eta = (elapsed / completed) * (len(tasks) - completed)
                print(
                    f"    [{completed}/{len(tasks)}] elapsed={elapsed/60:.1f}m "
                    f"eta={eta/60:.1f}m",
                    flush=True,
                )

    if jobs == 1:
        consume(map(_run_outer_task, tasks))
    else:
        context = mp.get_context("spawn")
        with ProcessPoolExecutor(max_workers=jobs, mp_context=context) as executor:
            consume(executor.map(_run_outer_task, tasks, chunksize=1))

    decisions = pd.DataFrame(decision_rows).sort_values(
        ["asset_class", "series", "outer_number", "order_set", "rule"]
    ).reset_index(drop=True)
    windows = pd.DataFrame(window_rows).sort_values(
        ["asset_class", "series", "outer_number", "order_set", "order"]
    ).reset_index(drop=True)
    task_manifest = pd.DataFrame(manifest_rows).sort_values(
        ["asset_class", "series", "outer_number", "order_set"]
    ).reset_index(drop=True)

    decisions.to_csv(run_dir / "decision_results.csv.gz", index=False, compression="gzip")
    windows.to_csv(run_dir / "window_selection.csv.gz", index=False, compression="gzip")
    task_manifest.to_csv(run_dir / "task_manifest.csv", index=False)

    elapsed = time.perf_counter() - started
    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "checkpoint": "06",
        "preset": preset.name,
        "study_type": "post_hoc_mechanism_not_confirmation",
        "cp05_external_test_blocks_rescored": False,
        "cp05_holdout_blocks_skipped": preset.holdout_blocks,
        "order_sets": {name: list(ORDER_SETS[name]) for name in preset.order_sets},
        "frozen_dynamic_rule": "recency_hl3",
        "track_epsilon": TRACK_EPSILON,
        "candidate_spacing": CANDIDATE_SPACING,
        "max_minima": MAX_MINIMA,
        "windows": list(preset.windows),
        "max_origins": preset.max_origins,
        "step": STEP,
        "horizon": HORIZON,
        "n_series": len(preset.series),
        "n_tasks": len(tasks),
        "jobs": jobs,
        "elapsed_seconds": elapsed,
    }
    (run_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    latest = RESULT_ROOT / "LATEST.txt"
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text(run_dir.as_posix() + "\n", encoding="utf-8")

    print("")
    print(f"Checkpoint 06 complete: {run_dir}")
    print(f"Decision rows: {len(decisions)}")
    print(f"Elapsed: {elapsed/60:.1f} minutes")
    print(
        "Next: python experiments/smoothness_cv/analyze_checkpoint_06.py "
        f"--run-dir {run_dir}"
    )


if __name__ == "__main__":
    main()
