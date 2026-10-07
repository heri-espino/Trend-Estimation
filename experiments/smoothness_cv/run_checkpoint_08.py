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

os.environ['OMP_NUM_THREADS'] = '1'
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['NUMEXPR_NUM_THREADS'] = '1'

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from experiments.numerical_smoothness_selection import run_two_stage_order_validation as tracked
from experiments.smoothness_cv import run_checkpoint_04 as cp04
from experiments.smoothness_cv import run_checkpoint_06 as cp06
from experiments.smoothness_cv import run_checkpoint_07 as cp07
from experiments.smoothness_cv.dynamic_branch_rules import DEFAULT_RULES, TRAJECTORY_RULES, evaluate_rule_set


RESULT_ROOT = Path('results') / 'smoothness_cv' / 'checkpoint_08'
ORDER = 2
WINDOW = 120
HORIZON = 20
OUTER_BLOCKS = 8
STEP = 5
MAX_ORIGINS = 30
TRACK_EPSILON = 0.10
CANDIDATE_SPACING = 0.02
MAX_MINIMA = 5
BASELINE_RULES = tuple(
    spec for spec in DEFAULT_RULES if spec.name in {'last', 'recency_hl3'}
)
ALL_DYNAMIC_RULES = BASELINE_RULES + TRAJECTORY_RULES
TRAJECTORY_RULE_NAMES = tuple(spec.name for spec in TRAJECTORY_RULES)


@dataclass(frozen=True)
class CP08Preset:
    name: str
    seeds: tuple[int, ...]
    mechanisms: tuple[str, ...]
    observation_noise_sds: tuple[float, ...]


PRESETS = {
    'smoke': CP08Preset(
        name='smoke',
        seeds=(100, 101),
        mechanisms=('stationary_smooth', 'switch_to_rough'),
        observation_noise_sds=(0.02,),
    ),
    'development': CP08Preset(
        name='development',
        seeds=tuple(range(100, 200)),
        mechanisms=cp07.MECHANISMS,
        observation_noise_sds=(0.01, 0.03),
    ),
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description='CP08 development: forecast the selected smoothness branch trajectory.'
    )
    p.add_argument('--preset', choices=tuple(PRESETS), default='smoke')
    p.add_argument('--jobs', type=int, default=0)
    p.add_argument('--output-dir', type=Path, default=None)
    return p.parse_args()


def _git_short_sha() -> str:
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--short', 'HEAD'],
            check=True, capture_output=True, text=True,
        )
        return result.stdout.strip() or 'unknown'
    except Exception:
        return 'unknown'


def _resolve_jobs(requested: int) -> int:
    requested = int(requested)
    if requested < 0:
        raise ValueError('--jobs must be 0 or a positive integer.')
    if requested == 1:
        return 1
    cpu = int(os.cpu_count() or 1)
    if requested == 0:
        return max(1, min(16, cpu - 1 if cpu > 1 else 1))
    if os.name == 'nt' and requested > 61:
        raise ValueError('Windows ProcessPoolExecutor supports at most 61 workers.')
    return requested


def _default_run_dir(preset_name: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    return RESULT_ROOT / f'{stamp}_{preset_name}_{_git_short_sha()}'


def _register_key(key: str) -> None:
    cp07.applied.SERIES[key] = {
        'family': 'SIMULATION',
        'test_reserve': HORIZON,
        'step': STEP,
        'windows': (WINDOW,),
        'max_origins': MAX_ORIGINS,
    }


def _rule_frame(branch_history: pd.DataFrame, current_s: float) -> pd.DataFrame:
    return evaluate_rule_set(
        branch_history,
        current_s=float(current_s),
        val2_loss_column='val2_log_rmse',
        rules=ALL_DYNAMIC_RULES,
    )


def _run_scenario(task: tuple) -> list[dict]:
    seed, mechanism, noise_sd, preset_name = task
    key = 'CP08_SIM'
    _register_key(key)
    frame = cp07.simulate_log_series(
        mechanism=mechanism,
        observation_noise_sd=float(noise_sd),
        seed=int(seed),
    )
    stops = cp04._outer_stops(
        len(frame), horizon=HORIZON, development_blocks=OUTER_BLOCKS, holdout_blocks=0
    )
    rows: list[dict] = []

    for outer_number, outer_stop in enumerate(stops, start=1):
        case_frame = frame.iloc[:outer_stop].copy()
        history = case_frame.iloc[:-2 * HORIZON].copy()
        pretest = case_frame.iloc[:-HORIZON].copy()
        true_test = case_frame.iloc[-HORIZON:].copy()

        splits = tracked._paired_splits(
            len(history), window=WINDOW, horizon=HORIZON, step=STEP, max_origins=MAX_ORIGINS
        )
        tracks, _ = tracked._track_order_minima(
            key, history, order=ORDER, window=WINDOW, splits=splits,
            max_minima=MAX_MINIMA, track_epsilon=TRACK_EPSILON,
            candidate_spacing=CANDIDATE_SPACING,
        )
        summary = tracked._summarize_branches(tracks, selection_metric='log_rmse')
        continuations = cp06._final_continuations_subset(
            key, case_frame, summary, orders=(ORDER,)
        )

        fallback_used = False
        try:
            winner = cp04._select_branch(summary, continuations)
            branch_id = str(winner['branch_id'])
            current_s = float(winner['final_smoothness'])
            branch_history = tracks.loc[tracks['branch_id'].eq(branch_id)].copy()
            rules = _rule_frame(branch_history, current_s)
        except RuntimeError:
            fallback_used = True
            branch_id = 'fallback_pooled'
            current_s = np.nan
            rules = pd.DataFrame()

        pooled_s, pooled_score, _ = cp04._pooled_smoothness(
            key, pretest, order=ORDER, window=WINDOW, max_origins=MAX_ORIGINS
        )

        if fallback_used:
            rules = pd.DataFrame([
                {
                    'rule': name, 'rule_family': 'fallback_pooled',
                    'raw_selected_s': pooled_s, 'selected_s': pooled_s, 'clipped': False,
                }
                for name in ('last', 'recency_hl3', *TRAJECTORY_RULE_NAMES)
            ])

        rules = pd.concat([
            rules,
            pd.DataFrame([{
                'rule': 'pooled_cv_same_config',
                'rule_family': 'pooled_cv',
                'raw_selected_s': pooled_s,
                'selected_s': pooled_s,
                'clipped': False,
            }])
        ], ignore_index=True)

        oracle_s, oracle_latent_mse = cp07._oracle(pretest, true_test)
        common = {
            'seed': int(seed),
            'mechanism': mechanism,
            'mechanism_group': ('changing' if mechanism in cp07.CHANGING_MECHANISMS else 'stationary'),
            'observation_noise_sd': float(noise_sd),
            'outer_number': int(outer_number),
            'outer_stop': int(outer_stop),
            'order': ORDER,
            'window': WINDOW,
            'horizon': HORIZON,
            'branch_id': branch_id,
            'fallback_used': bool(fallback_used),
            'current_s': current_s,
            'pooled_cv_score': float(pooled_score),
            'oracle_s': float(oracle_s),
            'oracle_latent_rmse': float(np.sqrt(oracle_latent_mse)),
        }

        for _, rule in rules.iterrows():
            selected_s = float(rule['selected_s'])
            metrics, _ = cp04._fit_and_score(
                pretest, true_test, order=ORDER, window=WINDOW, smoothness=selected_s
            )
            rows.append({
                **common,
                'rule': str(rule['rule']),
                'rule_family': str(rule['rule_family']),
                'raw_selected_s': float(rule.get('raw_selected_s', selected_s)),
                'selected_s': selected_s,
                'clipped': bool(rule.get('clipped', False)),
                'abs_s_error_to_oracle': abs(selected_s - oracle_s),
                'latent_log_rmse': cp07._latent_rmse(
                    pretest, true_test, smoothness=selected_s
                ),
                **metrics,
            })

    return rows


def main() -> None:
    args = parse_args()
    preset = PRESETS[args.preset]
    jobs = _resolve_jobs(args.jobs)
    if preset.name == 'development' and (min(preset.seeds) < 100 or max(preset.seeds) >= 200):
        raise RuntimeError('CP08 development may use only seeds 100..199.')
    run_dir = args.output_dir or _default_run_dir(preset.name)
    run_dir.mkdir(parents=True, exist_ok=True)

    tasks = list(product(
        preset.seeds, preset.mechanisms, preset.observation_noise_sds, (preset.name,)
    ))
    print(
        f'CP08 preset={preset.name}: {len(tasks)} scenarios, '
        f'{len(tasks) * OUTER_BLOCKS} outer decisions, jobs={jobs}', flush=True
    )
    started = time.perf_counter()
    rows: list[dict] = []

    def consume(iterator):
        for completed, scenario_rows in enumerate(iterator, start=1):
            rows.extend(scenario_rows)
            if completed == 1 or completed % max(1, len(tasks)//50) == 0 or completed == len(tasks):
                elapsed = time.perf_counter() - started
                eta = elapsed / completed * (len(tasks) - completed)
                print(f'    [{completed}/{len(tasks)}] elapsed={elapsed/60:.1f}m eta={eta/60:.1f}m', flush=True)

    if jobs == 1:
        consume(map(_run_scenario, tasks))
    else:
        context = mp.get_context('spawn')
        with ProcessPoolExecutor(max_workers=jobs, mp_context=context) as executor:
            consume(executor.map(_run_scenario, tasks, chunksize=1))

    results = pd.DataFrame(rows).sort_values(
        ['seed','mechanism','observation_noise_sd','outer_number','rule']
    ).reset_index(drop=True)
    results.to_csv(run_dir / 'decision_results.csv.gz', index=False, compression='gzip')

    elapsed = time.perf_counter() - started
    metadata = {
        'created_at_utc': datetime.now(timezone.utc).isoformat(),
        'git_commit': _git_short_sha(),
        'checkpoint': '08',
        'preset': preset.name,
        'study_type': 'development_trajectory_rule_selection',
        'design_frozen_before_run': True,
        'preset_definition': asdict(preset),
        'development_seed_range': [100, 199],
        'reserved_confirmation_seed_range': [200, 399],
        'trajectory_rules': list(TRAJECTORY_RULE_NAMES),
        'baselines': ['recency_hl3','last','pooled_cv_same_config'],
        'order': ORDER, 'window': WINDOW, 'horizon': HORIZON,
        'track_epsilon': TRACK_EPSILON,
        'candidate_spacing': CANDIDATE_SPACING,
        'max_minima': MAX_MINIMA,
        'primary_development_group': 'changing',
        'primary_metric': 'observed log RMSE geometric ratio vs pooled CV',
        'n_scenarios': len(tasks),
        'n_outer_decisions': len(tasks) * OUTER_BLOCKS,
        'jobs': jobs,
        'elapsed_seconds': elapsed,
    }
    (run_dir / 'run_metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    latest = RESULT_ROOT / 'LATEST.txt'
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text(run_dir.as_posix() + '\n', encoding='utf-8')
    print(f'Checkpoint 08 complete: {run_dir}')
    print('Next: python experiments/smoothness_cv/analyze_checkpoint_08.py')


if __name__ == '__main__':
    main()
