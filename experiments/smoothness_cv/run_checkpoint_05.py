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

from experiments.numerical_smoothness_selection import (
    run_applied_case_studies as applied,
)
from experiments.numerical_smoothness_selection import (
    run_two_stage_order_validation as tracked,
)
from experiments.smoothness_cv.dynamic_branch_rules import evaluate_rule_set
from experiments.smoothness_cv import run_checkpoint_04 as cp04


RESULT_ROOT = Path("results") / "smoothness_cv" / "checkpoint_05"
SNAPSHOT_MANIFEST = Path("data/external/real_world/snapshot/snapshot_manifest.json")
FROZEN_MANIFEST_UPDATED_AT = "2026-09-29T21:40:44.625057+00:00"

PANEL_ETFS = (
    "IJH", "IJR", "ITOT", "IVV", "IWD", "IWF", "MDY", "SCHB",
    "SMH", "VB", "VEA", "VO", "VTV", "VUG", "VWO", "XLB",
    "XLI", "XLP", "XLU", "XLY",
)

PANEL_STOCKS = (
    "ABBV", "ADBE", "AMD", "AMZN", "AVGO", "BA", "BLK", "C",
    "COP", "COST", "CRM", "CSCO", "DE", "DIS", "FDX", "GE",
    "GOOGL", "GS", "IBM", "LLY", "MCD", "META", "MMM", "MRK",
    "MS", "NKE", "NVDA", "ORCL", "OXY", "PEP", "PFE", "SLB",
    "TGT", "TSLA", "UNH", "UPS",
)

PANEL_CRYPTOS = (
    "ADA-USD", "AVAX-USD", "BCH-USD", "DOGE-USD", "DOT-USD",
    "LINK-USD", "SOL-USD", "XLM-USD",
)

PANEL_SERIES = PANEL_ETFS + PANEL_STOCKS + PANEL_CRYPTOS


@dataclass(frozen=True)
class CP05Preset:
    name: str
    series: tuple[str, ...]
    outer_blocks: int
    max_origins: int
    windows: tuple[int, ...]


PRESETS = {
    "smoke": CP05Preset(
        name="smoke",
        series=("IVV", "AMZN", "SOL-USD"),
        outer_blocks=1,
        max_origins=8,
        windows=(63, 252),
    ),
    "panel": CP05Preset(
        name="panel",
        series=PANEL_SERIES,
        outer_blocks=4,
        max_origins=30,
        windows=(63, 126, 252, 504),
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Checkpoint 05 frozen external financial panel for the already "
            "selected recency_hl3 dynamic smoothness rule."
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


def _load_frozen_manifest() -> dict:
    payload = json.loads(SNAPSHOT_MANIFEST.read_text(encoding="utf-8"))
    if payload.get("updated_at_utc") != FROZEN_MANIFEST_UPDATED_AT:
        raise RuntimeError(
            "Snapshot manifest changed after CP05 was frozen. "
            "Do not silently change the external panel."
        )
    return payload


def _register_series(key: str) -> dict:
    manifest = _load_frozen_manifest()
    entry = manifest["series"][key]
    if entry["source"] != "yahoo":
        raise RuntimeError(f"CP05 expected Yahoo source for {key}.")
    if entry["asset_class"] not in {"stock", "etf", "crypto"}:
        raise RuntimeError(f"Unexpected asset class for {key}: {entry['asset_class']}")
    if int(entry["rows"]) < 2060:
        raise RuntimeError(f"{key} has fewer than 2060 observations.")
    if key in {"AAPL", "SPY", "BTC-USD"}:
        raise RuntimeError(f"{key} belongs to CP04 and must not enter CP05.")

    spec = {
        "path": Path(entry["snapshot_path"]),
        "label": entry["label"],
        "family": entry["asset_class"].upper(),
        "asset_class": entry["asset_class"],
        "tail_observations": 2060,
        "test_reserve": 60,
        "orders": (1, 2, 3, 4),
        "windows": (63, 126, 252, 504),
        "horizons": (60,),
        "step": 5,
        "max_origins": 30,
    }
    applied.SERIES[key] = spec
    return spec


def _load_frame(key: str) -> pd.DataFrame:
    _register_series(key)
    return applied._load_series(key)


def _pooled_for_config(
    key: str,
    pretest: pd.DataFrame,
    *,
    order: int,
    window: int,
    max_origins: int,
) -> tuple[float, float, int]:
    return cp04._pooled_smoothness(
        key,
        pretest,
        order=order,
        window=window,
        max_origins=max_origins,
    )


def _fallback_config(window_selection: pd.DataFrame) -> tuple[int, int]:
    row = window_selection.sort_values(
        ["aggregate_val1_loss", "order", "window"],
        ascending=[True, True, True],
    ).iloc[0]
    return int(row["order"]), int(row["window"])


def _make_rule_rows(
    *,
    branch_history: pd.DataFrame | None,
    current_s: float | None,
    pooled_s: float,
    fallback_used: bool,
) -> pd.DataFrame:
    if fallback_used:
        return pd.DataFrame(
            [
                {"rule": "recency_hl3", "rule_family": "fallback_pooled", "selected_s": pooled_s},
                {"rule": "last", "rule_family": "fallback_pooled", "selected_s": pooled_s},
                {"rule": "pooled_cv_same_config", "rule_family": "pooled_cv", "selected_s": pooled_s},
            ]
        )

    assert branch_history is not None
    assert current_s is not None
    all_rules = evaluate_rule_set(
        branch_history,
        current_s=float(current_s),
        val2_loss_column="val2_level_rmse",
    )
    selected = all_rules.loc[
        all_rules["rule"].isin(["recency_hl3", "last"])
    ].copy()
    selected = pd.concat(
        [
            selected,
            pd.DataFrame(
                [
                    {
                        "rule": "pooled_cv_same_config",
                        "rule_family": "pooled_cv",
                        "selected_s": pooled_s,
                    }
                ]
            ),
        ],
        ignore_index=True,
    )
    return selected


def _run_outer_task(task: tuple) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    key, outer_number, outer_stop, preset_name = task
    preset = PRESETS[preset_name]
    spec = _register_series(key)
    frame = applied._load_series(key)
    horizon = 60
    case_frame = frame.iloc[: int(outer_stop)].copy()
    history = case_frame.iloc[:-2 * horizon].copy()
    pretest = case_frame.iloc[:-horizon].copy()
    true_test = case_frame.iloc[-horizon:].copy()

    window_selection, splits_by_order = tracked._select_window_per_order(
        key,
        history,
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
            max_minima=5,
            track_epsilon=0.10,
            candidate_spacing=0.02,
        )
        track_frames.append(track)
    tracks = pd.concat(track_frames, ignore_index=True)
    summary = tracked._summarize_branches(
        tracks,
        selection_metric="level_rmse",
    )
    continuations = cp04._final_continuations(
        key,
        case_frame,
        summary,
        track_epsilon=0.10,
        candidate_spacing=0.02,
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
        branch_id = "fallback_pooled"
        order, window = _fallback_config(window_selection)
        current_s = None
        branch_history = None
        branch_support = np.nan
        branch_score = np.nan

    pooled_s, pooled_score, pooled_evaluations = _pooled_for_config(
        key,
        pretest,
        order=order,
        window=window,
        max_origins=preset.max_origins,
    )
    rules = _make_rule_rows(
        branch_history=branch_history,
        current_s=current_s,
        pooled_s=pooled_s,
        fallback_used=fallback_used,
    )

    common = {
        "series": key,
        "label": spec["label"],
        "asset_class": spec["asset_class"],
        "outer_number": int(outer_number),
        "outer_stop": int(outer_stop),
        "test_start_date": str(true_test["date"].iloc[0].date()),
        "test_end_date": str(true_test["date"].iloc[-1].date()),
        "horizon": horizon,
        "selected_branch": branch_id,
        "order": order,
        "window": window,
        "branch_support_fraction": branch_support,
        "branch_selection_score": branch_score,
        "current_s": np.nan if current_s is None else current_s,
        "pooled_cv_score": pooled_score,
        "pooled_objective_evaluations": pooled_evaluations,
        "fallback_used": bool(fallback_used),
        "fallback_reason": fallback_reason,
    }

    decision_rows: list[dict] = []
    forecast_rows: list[dict] = []
    for _, rule in rules.iterrows():
        metrics, path = cp04._fit_and_score(
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
        for _, path_row in path.iterrows():
            forecast_rows.append(
                {
                    "series": key,
                    "asset_class": spec["asset_class"],
                    "outer_number": int(outer_number),
                    "rule": str(rule["rule"]),
                    "selected_s": float(rule["selected_s"]),
                    "date": str(pd.Timestamp(path_row["date"]).date()),
                    "observed": float(path_row["observed"]),
                    "forecast": float(path_row["forecast"]),
                }
            )

    tracks = tracks.copy()
    tracks["outer_number"] = int(outer_number)
    tracks["outer_stop"] = int(outer_stop)
    tracks["asset_class"] = spec["asset_class"]
    windows = window_selection.copy()
    windows["outer_number"] = int(outer_number)
    windows["outer_stop"] = int(outer_stop)
    windows["asset_class"] = spec["asset_class"]

    return (
        decision_rows,
        forecast_rows,
        tracks.to_dict("records"),
        windows.to_dict("records"),
    )


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    jobs = _resolve_jobs(args.jobs)
    _load_frozen_manifest()

    run_dir = args.output_dir or _default_run_dir(preset.name)
    run_dir.mkdir(parents=True, exist_ok=True)

    tasks: list[tuple] = []
    panel_manifest: list[dict] = []
    for key in preset.series:
        spec = _register_series(key)
        frame = applied._load_series(key)
        stops = cp04._outer_stops(
            len(frame),
            horizon=60,
            development_blocks=preset.outer_blocks,
            holdout_blocks=0,
        )
        panel_manifest.append(
            {
                "series": key,
                "label": spec["label"],
                "asset_class": spec["asset_class"],
                "n_snapshot_rows_used": len(frame),
                "n_outer_blocks": len(stops),
            }
        )
        for outer_number, stop in enumerate(stops, start=1):
            tasks.append((key, outer_number, stop, preset.name))

    print(
        f"CP05 preset={preset.name}: {len(preset.series)} series, "
        f"{len(tasks)} outer decisions, jobs={jobs}",
        flush=True,
    )
    started = time.perf_counter()
    decision_rows: list[dict] = []
    forecast_rows: list[dict] = []
    track_rows: list[dict] = []
    window_rows: list[dict] = []

    def consume(iterator):
        for completed, result in enumerate(iterator, start=1):
            d, p, t, w = result
            decision_rows.extend(d)
            forecast_rows.extend(p)
            track_rows.extend(t)
            window_rows.extend(w)
            if completed == 1 or completed % max(1, len(tasks) // 20) == 0 or completed == len(tasks):
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
        ["asset_class", "series", "outer_number", "rule"]
    ).reset_index(drop=True)
    forecasts = pd.DataFrame(forecast_rows).sort_values(
        ["asset_class", "series", "outer_number", "rule", "date"]
    ).reset_index(drop=True)
    tracks = pd.DataFrame(track_rows).sort_values(
        ["asset_class", "series", "outer_number", "order", "branch_id", "origin_number"]
    ).reset_index(drop=True)
    windows = pd.DataFrame(window_rows).sort_values(
        ["asset_class", "series", "outer_number", "order"]
    ).reset_index(drop=True)

    decisions.to_csv(run_dir / "decision_results.csv.gz", index=False, compression="gzip")
    forecasts.to_csv(run_dir / "forecast_paths.csv.gz", index=False, compression="gzip")
    tracks.to_csv(run_dir / "branch_states.csv.gz", index=False, compression="gzip")
    windows.to_csv(run_dir / "window_selection.csv.gz", index=False, compression="gzip")
    pd.DataFrame(panel_manifest).to_csv(run_dir / "panel_manifest.csv", index=False)

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "checkpoint": "05",
        "preset": preset.name,
        "design_frozen_before_run": True,
        "snapshot_manifest_updated_at": FROZEN_MANIFEST_UPDATED_AT,
        "excluded_cp04_series": ["AAPL", "SPY", "BTC-USD"],
        "frozen_primary_rule": "recency_hl3",
        "baselines": ["last", "pooled_cv_same_config"],
        "track_epsilon": 0.10,
        "candidate_spacing": 0.02,
        "max_minima": 5,
        "selection_metric": "level_rmse",
        "orders": [1, 2, 3, 4],
        "windows": list(preset.windows),
        "tail_observations": 2060,
        "horizon": 60,
        "outer_blocks": preset.outer_blocks,
        "max_origins": preset.max_origins,
        "step": 5,
        "fallback_policy": "pooled_equal_ratios_if_no_branch_continues",
        "panel_counts": {
            "etf": sum(k in PANEL_ETFS for k in preset.series),
            "stock": sum(k in PANEL_STOCKS for k in preset.series),
            "crypto": sum(k in PANEL_CRYPTOS for k in preset.series),
        },
        "n_series": len(preset.series),
        "n_outer_decisions": len(tasks),
        "jobs": jobs,
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
    print(f"Checkpoint 05 complete: {run_dir}")
    print(f"Series: {len(preset.series)}")
    print(f"Outer decisions: {len(tasks)}")
    print(
        "Next: python experiments/smoothness_cv/analyze_checkpoint_05.py "
        f"--run-dir {run_dir}"
    )


if __name__ == "__main__":
    main()
