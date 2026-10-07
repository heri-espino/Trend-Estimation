from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from itertools import product
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
from experiments.smoothness_cv import run_checkpoint_04 as cp04
from experiments.smoothness_cv import run_checkpoint_06 as cp06
from experiments.smoothness_cv.common import (
    fit_and_forecast,
    grid_argmin,
    latent_forecast_oracle_curve,
    smoothness_grid,
)
from experiments.smoothness_cv.dynamic_branch_rules import evaluate_rule_set


RESULT_ROOT = Path("results") / "smoothness_cv" / "checkpoint_07"
ORDER = 2
WINDOW = 120
HORIZON = 20
N_OBS = 720
OUTER_BLOCKS = 8
STEP = 5
MAX_ORIGINS = 30
TRACK_EPSILON = 0.10
CANDIDATE_SPACING = 0.02
MAX_MINIMA = 5
ORACLE_GRID = 201

MECHANISMS = (
    "stationary_smooth",
    "stationary_rough",
    "switch_to_rough",
    "switch_to_smooth",
    "gradual_roughening",
    "gradual_smoothing",
)
CHANGING_MECHANISMS = (
    "switch_to_rough",
    "switch_to_smooth",
    "gradual_roughening",
    "gradual_smoothing",
)


@dataclass(frozen=True)
class CP07Preset:
    name: str
    seeds: tuple[int, ...]
    mechanisms: tuple[str, ...]
    observation_noise_sds: tuple[float, ...]


PRESETS = {
    "smoke": CP07Preset(
        name="smoke",
        seeds=(0, 1),
        mechanisms=("stationary_smooth", "switch_to_rough"),
        observation_noise_sds=(0.02,),
    ),
    "paper": CP07Preset(
        name="paper",
        seeds=tuple(range(100)),
        mechanisms=MECHANISMS,
        observation_noise_sds=(0.01, 0.03),
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "CP07 prospective simulation: fixed d=2, fixed L=120, and "
            "time-varying latent trend roughness."
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


def roughness_scale(mechanism: str, n_obs: int = N_OBS) -> np.ndarray:
    low = 0.00030
    high = 0.00200
    n = int(n_obs)
    if mechanism == "stationary_smooth":
        return np.full(n, low)
    if mechanism == "stationary_rough":
        return np.full(n, high)
    if mechanism == "switch_to_rough":
        out = np.full(n, low)
        out[540:] = high
        return out
    if mechanism == "switch_to_smooth":
        out = np.full(n, high)
        out[540:] = low
        return out
    if mechanism in {"gradual_roughening", "gradual_smoothing"}:
        out = np.empty(n, dtype=float)
        start, stop = 440, 660
        alpha = np.clip((np.arange(n) - start) / (stop - start), 0.0, 1.0)
        if mechanism == "gradual_roughening":
            out[:] = low + (high - low) * alpha
        else:
            out[:] = high - (high - low) * alpha
        return out
    raise ValueError(f"Unknown mechanism: {mechanism}")


def simulate_log_series(
    *,
    mechanism: str,
    observation_noise_sd: float,
    seed: int,
) -> pd.DataFrame:
    rng = np.random.default_rng(int(seed))
    sigma_t = roughness_scale(mechanism)
    latent_log = np.empty(N_OBS, dtype=float)
    slope = np.empty(N_OBS, dtype=float)
    latent_log[0] = np.log(100.0)
    slope[0] = 0.001
    phi = 0.90
    mean_slope = 0.001

    innovations = rng.normal(size=N_OBS)
    for t in range(1, N_OBS):
        slope[t] = (
            mean_slope
            + phi * (slope[t - 1] - mean_slope)
            + sigma_t[t] * innovations[t]
        )
        latent_log[t] = latent_log[t - 1] + slope[t]

    observed_log = latent_log + rng.normal(
        0.0,
        float(observation_noise_sd),
        size=N_OBS,
    )
    level = np.exp(observed_log)
    dates = pd.date_range("2000-01-01", periods=N_OBS, freq="D")
    return pd.DataFrame(
        {
            "date": dates,
            "value": level,
            "observed_log": observed_log,
            "latent_log": latent_log,
            "roughness_scale": sigma_t,
        }
    )


def _register_simulation_key(key: str) -> None:
    applied.SERIES[key] = {
        "family": "SIMULATION",
        "test_reserve": HORIZON,
        "step": STEP,
        "windows": (WINDOW,),
        "max_origins": MAX_ORIGINS,
    }


def _pooled_s(
    key: str,
    pretest: pd.DataFrame,
) -> tuple[float, float, int]:
    return cp04._pooled_smoothness(
        key,
        pretest,
        order=ORDER,
        window=WINDOW,
        max_origins=MAX_ORIGINS,
    )


def _oracle(
    pretest: pd.DataFrame,
    true_test: pd.DataFrame,
) -> tuple[float, float]:
    observed_log_window = pretest["observed_log"].to_numpy(dtype=float)[-WINDOW:]
    latent_future = true_test["latent_log"].to_numpy(dtype=float)
    grid = smoothness_grid(ORACLE_GRID)
    curve = latent_forecast_oracle_curve(
        observed_log_window,
        latent_future,
        order=ORDER,
        s_grid=grid,
    )
    s, mse, _ = grid_argmin(grid, curve)
    return float(s), float(mse)


def _latent_rmse(
    pretest: pd.DataFrame,
    true_test: pd.DataFrame,
    *,
    smoothness: float,
) -> float:
    observed_log_window = pretest["observed_log"].to_numpy(dtype=float)[-WINDOW:]
    _, prediction, _, _ = fit_and_forecast(
        observed_log_window,
        order=ORDER,
        horizon=HORIZON,
        smoothness=float(smoothness),
    )
    error = true_test["latent_log"].to_numpy(dtype=float) - prediction
    return float(np.sqrt(np.mean(error * error)))


def _run_scenario(task: tuple) -> tuple[list[dict], list[dict]]:
    seed, mechanism, observation_noise_sd, preset_name = task
    key = "CP07_SIM"
    _register_simulation_key(key)
    frame = simulate_log_series(
        mechanism=mechanism,
        observation_noise_sd=float(observation_noise_sd),
        seed=int(seed),
    )
    stops = cp04._outer_stops(
        N_OBS,
        horizon=HORIZON,
        development_blocks=OUTER_BLOCKS,
        holdout_blocks=0,
    )

    rows: list[dict] = []
    branch_rows: list[dict] = []

    for outer_number, outer_stop in enumerate(stops, start=1):
        case_frame = frame.iloc[:outer_stop].copy()
        history = case_frame.iloc[:-2 * HORIZON].copy()
        pretest = case_frame.iloc[:-HORIZON].copy()
        true_test = case_frame.iloc[-HORIZON:].copy()

        splits = tracked._paired_splits(
            len(history),
            window=WINDOW,
            horizon=HORIZON,
            step=STEP,
            max_origins=MAX_ORIGINS,
        )
        tracks, _ = tracked._track_order_minima(
            key,
            history,
            order=ORDER,
            window=WINDOW,
            splits=splits,
            max_minima=MAX_MINIMA,
            track_epsilon=TRACK_EPSILON,
            candidate_spacing=CANDIDATE_SPACING,
        )
        summary = tracked._summarize_branches(
            tracks,
            selection_metric="log_rmse",
        )
        continuations = cp06._final_continuations_subset(
            key,
            case_frame,
            summary,
            orders=(ORDER,),
        )

        fallback_used = False
        try:
            winner = cp04._select_branch(summary, continuations)
            branch_id = str(winner["branch_id"])
            current_s = float(winner["final_smoothness"])
            branch_history = tracks.loc[
                tracks["branch_id"].eq(branch_id)
            ].copy()
            all_rules = evaluate_rule_set(
                branch_history,
                current_s=current_s,
                val2_loss_column="val2_log_rmse",
            )
            rules = all_rules.loc[
                all_rules["rule"].isin(["recency_hl3", "last"])
            ].copy()
        except RuntimeError:
            fallback_used = True
            branch_id = "fallback_pooled"
            current_s = np.nan
            branch_history = None
            rules = pd.DataFrame()

        pooled_s, pooled_score, _ = _pooled_s(key, pretest)
        if fallback_used:
            rules = pd.DataFrame(
                [
                    {
                        "rule": "recency_hl3",
                        "rule_family": "fallback_pooled",
                        "selected_s": pooled_s,
                    },
                    {
                        "rule": "last",
                        "rule_family": "fallback_pooled",
                        "selected_s": pooled_s,
                    },
                ]
            )

        rules = pd.concat(
            [
                rules,
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

        oracle_s, oracle_latent_mse = _oracle(pretest, true_test)
        common = {
            "seed": int(seed),
            "mechanism": mechanism,
            "mechanism_group": (
                "changing" if mechanism in CHANGING_MECHANISMS else "stationary"
            ),
            "observation_noise_sd": float(observation_noise_sd),
            "outer_number": int(outer_number),
            "outer_stop": int(outer_stop),
            "test_start_date": str(true_test["date"].iloc[0].date()),
            "test_end_date": str(true_test["date"].iloc[-1].date()),
            "order": ORDER,
            "window": WINDOW,
            "horizon": HORIZON,
            "branch_id": branch_id,
            "fallback_used": bool(fallback_used),
            "current_s": current_s,
            "pooled_cv_score": float(pooled_score),
            "oracle_s": oracle_s,
            "oracle_latent_rmse": float(np.sqrt(oracle_latent_mse)),
            "mean_test_roughness_scale": float(
                true_test["roughness_scale"].mean()
            ),
        }

        for _, rule in rules.iterrows():
            metrics, _ = cp04._fit_and_score(
                pretest,
                true_test,
                order=ORDER,
                window=WINDOW,
                smoothness=float(rule["selected_s"]),
            )
            selected_s = float(rule["selected_s"])
            rows.append(
                {
                    **common,
                    "rule": str(rule["rule"]),
                    "rule_family": str(rule["rule_family"]),
                    "selected_s": selected_s,
                    "abs_s_error_to_oracle": abs(selected_s - oracle_s),
                    "latent_log_rmse": _latent_rmse(
                        pretest,
                        true_test,
                        smoothness=selected_s,
                    ),
                    **metrics,
                }
            )

        branch_copy = tracks.copy()
        branch_copy["seed"] = int(seed)
        branch_copy["mechanism"] = mechanism
        branch_copy["observation_noise_sd"] = float(observation_noise_sd)
        branch_copy["outer_number"] = int(outer_number)
        branch_rows.extend(branch_copy.to_dict("records"))

    return rows, branch_rows


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    jobs = _resolve_jobs(args.jobs)
    run_dir = args.output_dir or _default_run_dir(preset.name)
    run_dir.mkdir(parents=True, exist_ok=True)

    tasks = [
        (seed, mechanism, noise_sd, preset.name)
        for seed, mechanism, noise_sd in product(
            preset.seeds,
            preset.mechanisms,
            preset.observation_noise_sds,
        )
    ]
    total_outer = len(tasks) * OUTER_BLOCKS
    print(
        f"CP07 preset={preset.name}: {len(tasks)} scenarios, "
        f"{total_outer} outer decisions, jobs={jobs}",
        flush=True,
    )

    rows: list[dict] = []
    branches: list[dict] = []
    started = time.perf_counter()

    def consume(iterator):
        for completed, result in enumerate(iterator, start=1):
            scenario_rows, branch_rows = result
            rows.extend(scenario_rows)
            branches.extend(branch_rows)
            if (
                completed == 1
                or completed % max(1, len(tasks) // 50) == 0
                or completed == len(tasks)
            ):
                elapsed = time.perf_counter() - started
                eta = (elapsed / completed) * (len(tasks) - completed)
                print(
                    f"    [{completed}/{len(tasks)}] "
                    f"elapsed={elapsed/60:.1f}m eta={eta/60:.1f}m",
                    flush=True,
                )

    if jobs == 1:
        consume(map(_run_scenario, tasks))
    else:
        context = mp.get_context("spawn")
        with ProcessPoolExecutor(
            max_workers=jobs,
            mp_context=context,
        ) as executor:
            consume(executor.map(_run_scenario, tasks, chunksize=1))

    results = pd.DataFrame(rows).sort_values(
        [
            "seed",
            "mechanism",
            "observation_noise_sd",
            "outer_number",
            "rule",
        ]
    ).reset_index(drop=True)
    branch_states = pd.DataFrame(branches).sort_values(
        [
            "seed",
            "mechanism",
            "observation_noise_sd",
            "outer_number",
            "branch_id",
            "origin_number",
        ]
    ).reset_index(drop=True)

    results.to_csv(
        run_dir / "decision_results.csv.gz",
        index=False,
        compression="gzip",
    )
    branch_states.to_csv(
        run_dir / "branch_states.csv.gz",
        index=False,
        compression="gzip",
    )

    elapsed = time.perf_counter() - started
    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_short_sha(),
        "checkpoint": "07",
        "preset": preset.name,
        "design_frozen_before_run": True,
        "preset_definition": asdict(preset),
        "order": ORDER,
        "window": WINDOW,
        "horizon": HORIZON,
        "n_obs": N_OBS,
        "outer_blocks": OUTER_BLOCKS,
        "step": STEP,
        "max_origins": MAX_ORIGINS,
        "track_epsilon": TRACK_EPSILON,
        "candidate_spacing": CANDIDATE_SPACING,
        "max_minima": MAX_MINIMA,
        "oracle_grid": ORACLE_GRID,
        "primary_metric": "observed log RMSE",
        "frozen_dynamic_rule": "recency_hl3",
        "mechanism_groups": {
            "stationary": [
                "stationary_smooth",
                "stationary_rough",
            ],
            "changing": list(CHANGING_MECHANISMS),
        },
        "n_scenarios": len(tasks),
        "n_outer_decisions": total_outer,
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
    print(f"Checkpoint 07 complete: {run_dir}")
    print(f"Decision rows: {len(results)}")
    print(
        "Next: python experiments/smoothness_cv/analyze_checkpoint_07.py "
        f"--run-dir {run_dir}"
    )


if __name__ == "__main__":
    main()
