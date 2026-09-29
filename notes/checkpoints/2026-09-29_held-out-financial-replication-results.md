# Checkpoint — Held-Out Financial Replication

Date: 2026-09-29

Status: **COMPLETED; held-out replication confirms the real-market boundary**

Result:

`results/forecast_optimal_smoothing/20260929T212901Z_real-data-replication-explore-frequency-aware_96fe7f3/`

Result commit:

`0b76072`

## Frozen protocol

The replication panel was committed before outcomes were inspected.

- daily windows: {63,126,252};
- selector memory: M=51;
- inner step: 5;
- horizons: {1,5,20} for ETFs/stocks and {1,7,30} for crypto;
- final 40% chronological OOS evaluation;
- frozen-all-pre primary comparator;
- no-change external benchmark;
- 321-point lambda discovery grid with continuous Brent refinement.

Panel:

- 6 ETFs;
- 6 stocks;
- 2 crypto assets;
- 42 series/horizon cells;
- 8,247 OOS forecast blocks.

## Confirmatory result

| class | median adaptive/frozen-all-pre RMSFE | adaptive beats fixed | median adaptive/no-change RMSFE | adaptive beats no-change |
|---|---:|---:|---:|---:|
| ETF | 1.034 | 4/18 | 1.039 | 4/18 |
| stock | 1.016 | 1/18 | 1.012 | 2/18 |
| crypto | 1.082 | 0/6 | 1.074 | 0/6 |

The pre-frozen replication therefore confirms the development-panel conclusion:
frequency-aware adaptive local re-selection does **not** broadly outperform a
strong historical fixed selector or no-change for financial price levels.

## Interpretation

The result is stronger than the development screen because the frequency-aware
policy was frozen before this panel was inspected.

The replication does not imply that adaptation is useless. It establishes a
boundary:

> The controlled-simulation gains require a sufficiently coherent,
> forecast-relevant regime shift. In observed financial price levels, local
> re-selection often adds estimation/selection noise relative to the
> conservative configuration learned from a long historical record.

The main paper should preserve this negative external result rather than tune
the same panel further.

## Next robustness stage

Because the replication is already inspected, any subsequent expansion is
**robustness/exploration**, not another pristine confirmatory test.

The most informative expansion is breadth rather than a finer lambda discovery
grid:

1. many more pre-specified financial series;
2. denser OOS origins (paper preset, step 5);
3. unchanged frequency-aware hyperparameter policy;
4. retain 321 lambda discovery points because Brent solves bracketed stationary
   points continuously.

A 1025-point discovery-grid rerun can later be used as a numerical sensitivity
check. It should not be treated as a new model or tuned for better forecast
performance.
