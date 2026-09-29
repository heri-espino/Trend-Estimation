# Real-world external-validation data

The experiment entry point is:

```bash
python experiments/forecast_optimal_smoothing/run_real_data_validation.py
```

Raw snapshots are downloaded automatically into `snapshot/` on first use and
then reused without additional network requests.

These CSV files and `snapshot_manifest.json` are intentionally tracked by
**ordinary Git**, not Git LFS. They are small enough to version directly and
serve as a temporary research backup while the paper is being developed.

After the first successful download, commit and push the snapshot directory so
that the data do not exist only on one workstation.

Use `--refresh-data` only when intentionally replacing the tracked snapshot.
Every result run records the SHA-256 hash, first/last date, row count, and
source for each input series.

## Sources

- FRED current-vintage CSV snapshots: `GDPC1`, `INDPRO`.
- Yahoo Finance through the optional `yfinance` dependency for ETFs, stocks,
  BTC, and ETH.

## Snapshot policy

- normal Git, not Git LFS;
- do not overwrite the snapshot during ordinary experiment reruns;
- missing files are downloaded automatically;
- `--refresh-data` deliberately replaces the tracked files;
- review the Git diff before committing any refresh;
- do not delete the snapshot until the paper and its reproducibility archive
  are complete.

## Macro vintage warning

The first external-validation pass uses the current FRED history and is
therefore exploratory. Revised macroeconomic observations can contain
information that was unavailable at a historical forecast origin.

A paper-final macroeconomic backtest must repeat GDP/industrial-production
results using ALFRED real-time vintages so that each forecast origin sees only
the vintage available at that date.
