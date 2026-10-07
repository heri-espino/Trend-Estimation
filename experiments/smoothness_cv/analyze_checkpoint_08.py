from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from experiments.smoothness_cv.run_checkpoint_08 import TRAJECTORY_RULE_NAMES


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description='Analyze CP08 trajectory-rule development results.')
    p.add_argument('--run-dir', type=Path, default=None)
    return p.parse_args()


def _resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path('results/smoothness_cv/checkpoint_08/LATEST.txt')
    if not latest.exists():
        raise FileNotFoundError('No completed CP08 run found.')
    return Path(latest.read_text(encoding='utf-8').strip())


def _geomean(values: pd.Series) -> float:
    x = values.to_numpy(dtype=float)
    x = x[np.isfinite(x) & (x > 0.0)]
    if x.size == 0:
        return np.nan
    return float(np.exp(np.mean(np.log(x))))


def _paired(decisions: pd.DataFrame) -> pd.DataFrame:
    keys = ['seed','mechanism','mechanism_group','observation_noise_sd','outer_number']
    pooled = decisions.loc[
        decisions['rule'].eq('pooled_cv_same_config'),
        keys + ['log_rmse','selected_s'],
    ].rename(columns={'log_rmse':'rmse_pooled','selected_s':'s_pooled'})
    last = decisions.loc[
        decisions['rule'].eq('last'),
        keys + ['log_rmse','selected_s'],
    ].rename(columns={'log_rmse':'rmse_last','selected_s':'s_last'})
    rows = []
    for rule in [*TRAJECTORY_RULE_NAMES, 'recency_hl3']:
        current = decisions.loc[
            decisions['rule'].eq(rule),
            keys + ['log_rmse','selected_s','raw_selected_s','clipped','abs_s_error_to_oracle'],
        ].rename(columns={
            'log_rmse':'rmse_rule',
            'selected_s':'s_rule',
            'raw_selected_s':'raw_s_rule',
            'clipped':'clipped_rule',
            'abs_s_error_to_oracle':'s_error_rule',
        })
        current = current.merge(pooled, on=keys, validate='one_to_one')
        current = current.merge(last, on=keys, validate='one_to_one')
        current['rule'] = rule
        current['ratio_vs_pooled'] = current['rmse_rule'] / current['rmse_pooled']
        current['ratio_vs_last'] = current['rmse_rule'] / current['rmse_last']
        rows.append(current)
    return pd.concat(rows, ignore_index=True)


def _rule_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for rule, frame in paired.groupby('rule', sort=False):
        changing = frame.loc[frame['mechanism_group'].eq('changing')]
        stationary = frame.loc[frame['mechanism_group'].eq('stationary')]
        rows.append({
            'rule': rule,
            'changing_g_ratio_vs_pooled': _geomean(changing['ratio_vs_pooled']),
            'changing_win_rate_vs_pooled': float(np.mean(changing['ratio_vs_pooled'] < 1.0)),
            'stationary_g_ratio_vs_pooled': _geomean(stationary['ratio_vs_pooled']),
            'all_g_ratio_vs_pooled': _geomean(frame['ratio_vs_pooled']),
            'all_g_ratio_vs_last': _geomean(frame['ratio_vs_last']),
            'clipping_rate': float(np.mean(frame['clipped_rule'].astype(bool))),
            'mean_abs_s_error_to_oracle': float(frame['s_error_rule'].mean()),
        })
    out = pd.DataFrame(rows)
    return out.sort_values(
        ['rule']
    ).reset_index(drop=True)


def _mechanism_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (rule, mechanism), frame in paired.groupby(['rule','mechanism'], sort=True):
        rows.append({
            'rule': rule,
            'mechanism': mechanism,
            'n_outer': int(len(frame)),
            'g_ratio_vs_pooled': _geomean(frame['ratio_vs_pooled']),
            'win_rate_vs_pooled': float(np.mean(frame['ratio_vs_pooled'] < 1.0)),
            'clipping_rate': float(np.mean(frame['clipped_rule'].astype(bool))),
        })
    return pd.DataFrame(rows)


def _markdown_table(frame: pd.DataFrame, digits: int = 4) -> str:
    if frame.empty:
        return '_No rows._'
    clean = frame.copy()
    for column in clean.select_dtypes(include=[np.number]).columns:
        clean[column] = clean[column].map(
            lambda x: '' if pd.isna(x) else f'{float(x):.{digits}g}'
        )
    headers = [str(c) for c in clean.columns]
    rows = [[str(v) for v in row] for row in clean.to_numpy()]
    widths = [max(len(headers[j]), *(len(row[j]) for row in rows)) for j in range(len(headers))]
    header = '| ' + ' | '.join(headers[j].ljust(widths[j]) for j in range(len(headers))) + ' |'
    divider = '| ' + ' | '.join('-' * widths[j] for j in range(len(headers))) + ' |'
    body = ['| ' + ' | '.join(row[j].ljust(widths[j]) for j in range(len(headers))) + ' |' for row in rows]
    return '\n'.join([header, divider, *body])


def main() -> None:
    args = parse_args()
    run_dir = _resolve_run_dir(args.run_dir)
    metadata = json.loads((run_dir / 'run_metadata.json').read_text(encoding='utf-8'))
    if metadata.get('study_type') != 'trajectory_rule_family_demonstration':
        raise RuntimeError('CP08 analyzer expects the rule-family demonstration.')

    decisions = pd.read_csv(run_dir / 'decision_results.csv.gz')
    paired = _paired(decisions)
    rules = _rule_summary(paired)
    mechanisms = _mechanism_summary(paired)
    diagnostics = run_dir / 'diagnostics'
    diagnostics.mkdir(parents=True, exist_ok=True)
    paired.to_csv(diagnostics / 'paired_rule_results.csv.gz', index=False, compression='gzip')
    rules.to_csv(diagnostics / 'rule_summary.csv', index=False)
    mechanisms.to_csv(diagnostics / 'mechanism_summary.csv', index=False)

    report = [
        '# Checkpoint 08 trajectory-rule family demonstration',
        '',
        'CP08 is not a winner-selection experiment. It demonstrates several',
        'branch-to-smoothness functionals that can be constructed from the same',
        'tracked branch matrix.',
        '',
        '## Rule behavior summary',
        '',
        _markdown_table(rules),
        '',
        '## Interpretation',
        '',
        'Forecast ratios, clipping rates, and oracle-distance diagnostics describe',
        'how the rules behave. They are not used to declare one universally best',
        'smoothness-selection rule.',
        '',
    ]
    (run_dir / 'checkpoint_report.md').write_text('\n'.join(report), encoding='utf-8')
    print(rules.to_string(index=False))
    print('CP08 summarizes rule behavior; no winner is selected.')


if __name__ == '__main__':
    main()
