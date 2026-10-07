from pathlib import Path
import argparse
import numpy as np
import pandas as pd


def _markdown_table(frame: pd.DataFrame, digits: int = 4) -> str:
    """Render a compact Markdown table without optional tabulate dependency."""
    if frame.empty:
        return "_No rows._"
    clean = frame.copy()
    for column in clean.select_dtypes(include=[np.number]).columns:
        clean[column] = clean[column].map(
            lambda x: "" if pd.isna(x) else f"{float(x):.{digits}g}"
        )
    headers = [str(col) for col in clean.columns]
    rows = [[str(value) for value in row] for row in clean.to_numpy()]
    widths = [
        max(len(headers[j]), *(len(row[j]) for row in rows))
        for j in range(len(headers))
    ]
    header = "| " + " | ".join(
        headers[j].ljust(widths[j]) for j in range(len(headers))
    ) + " |"
    divider = "| " + " | ".join(
        "-" * widths[j] for j in range(len(headers))
    ) + " |"
    body = [
        "| " + " | ".join(
            row[j].ljust(widths[j]) for j in range(len(headers))
        ) + " |"
        for row in rows
    ]
    return "\n".join([header, divider, *body])


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--run-dir', type=Path, default=None)
    a = p.parse_args()
    if a.run_dir is None:
        latest = Path('results/smoothness_cv/checkpoint_07/LATEST.txt')
        run_dir = Path(latest.read_text(encoding='utf-8').strip())
    else:
        run_dir = a.run_dir
    d = pd.read_csv(run_dir / 'decision_results.csv.gz')
    keys = ['seed','mechanism','mechanism_group','observation_noise_sd','outer_number']
    keep = keys + ['rule','log_rmse','selected_s','abs_s_error_to_oracle','fallback_used']
    wide = d[keep].pivot(index=keys, columns='rule')
    out = pd.DataFrame(index=wide.index).reset_index()
    out['dynamic_pooled'] = (
        wide['log_rmse']['recency_hl3'].to_numpy() /
        wide['log_rmse']['pooled_cv_same_config'].to_numpy()
    )
    out['dynamic_last'] = (
        wide['log_rmse']['recency_hl3'].to_numpy() /
        wide['log_rmse']['last'].to_numpy()
    )
    out['s_dynamic'] = wide['selected_s']['recency_hl3'].to_numpy()
    out['s_pooled'] = wide['selected_s']['pooled_cv_same_config'].to_numpy()
    out['s_last'] = wide['selected_s']['last'].to_numpy()
    rows = []
    groups = [('all', out)]
    groups += [(str(k), g) for k,g in out.groupby('mechanism_group')]
    groups += [(str(k), g) for k,g in out.groupby('mechanism')]
    for name,g in groups:
        rows.append({
            'group': name,
            'n': len(g),
            'g_ratio_dynamic_pooled': float(np.exp(np.mean(np.log(g['dynamic_pooled'])))),
            'win_rate_dynamic_pooled': float(np.mean(g['dynamic_pooled'] < 1)),
            'g_ratio_dynamic_last': float(np.exp(np.mean(np.log(g['dynamic_last'])))),
            'win_rate_dynamic_last': float(np.mean(g['dynamic_last'] < 1)),
            'mean_s_dynamic': float(g['s_dynamic'].mean()),
            'mean_s_pooled': float(g['s_pooled'].mean()),
            'mean_s_last': float(g['s_last'].mean()),
        })
    summary = pd.DataFrame(rows)
    diag = run_dir / 'diagnostics'
    diag.mkdir(parents=True, exist_ok=True)
    out.to_csv(diag / 'paired_outer_results.csv', index=False)
    summary.to_csv(diag / 'group_summary.csv', index=False)
    (run_dir / 'checkpoint_report.md').write_text(
        '# Checkpoint 07 dynamic roughness simulation\n\n' +
        _markdown_table(summary) + '\n',
        encoding='utf-8',
    )
    print(summary.to_string(index=False))

if __name__ == '__main__':
    main()
