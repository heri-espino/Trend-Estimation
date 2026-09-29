# Real-world external-validation data

The experiment entry point is:

```bash
python experiments/forecast_optimal_smoothing/run_real_data_validation.py
```

Raw snapshots are downloaded automatically into `cache/` on first use and
then reused without network requests. The cache is intentionally ignored by
Git because market-data redistribution is not part of this repository.

Use `--refresh-data` only when intentionally replacing the local snapshot.
Every result run records the SHA-256 hash, first/last date, row count, and
source for each cached series.

## Sources

- FRED current-vintage CSV snapshots: `GDPC1`, `INDPRO`.
- Yahoo Finance through the optional `yfinance` dependency for ETFs, stocks,
  BTC, and ETH.

## Macro vintage warning

The first external-validation pass uses the current FRED history and is
therefore exploratory. Revised macroeconomic observations can contain
information that was unavailable at a historical forecast origin.

A paper-final macroeconomic backtest must repeat GDP/industrial-production
results using ALFRED real-time vintages so that each forecast origin sees only
the vintage available at that date.
