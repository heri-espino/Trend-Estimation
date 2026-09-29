# Checkpoint — Large-Universe Financial Robustness

Date: 2026-09-29

Status: **COMPLETED at explore density; broad financial boundary reinforced**

Result:

`results/forecast_optimal_smoothing/20260929T220202Z_real-data-large-robustness-explore-frequency-aware_e84b38b/`

Result commit:

`89d3e52`

## Important execution detail

The run completed with:

- panel: large-robustness;
- preset: **explore**;
- scale policy: frequency-aware;
- 64 entirely new financial series;
- 192 series/horizon cells;
- 31,922 OOS forecast blocks;
- 32 workers;
- elapsed time: about 1,278 seconds;
- 321-point log-lambda discovery grid with Brent refinement.

The intended denser `paper` preset was not used in this run. Therefore this
result establishes cross-sectional breadth, while the denser temporal-origin
sensitivity remains open.

## Class-level result

| class | series | cells | median adaptive/frozen-all-pre | adaptive wins | median adaptive/no-change |
|---|---:|---:|---:|---:|---:|
| ETF | 20 | 60 | 1.027 | 14/60 | 1.030 |
| stock | 36 | 108 | 1.022 | 17/108 | 1.024 |
| crypto | 8 | 24 | 1.014 | 6/24 | 1.008 |

Again, class medians remain above one.

## Horizon structure

### ETFs

| horizon | median A/F | wins |
|---:|---:|---:|
| 1 | 1.043 | 5/20 |
| 5 | 1.032 | 4/20 |
| 20 | 1.020 | 5/20 |

### Stocks

| horizon | median A/F | wins |
|---:|---:|
| 1 | 1.021 | 8/36 |
| 5 | 1.008 | 8/36 |
| 20 | 1.037 | 1/36 |

The h=5 stock result is close to parity, while h=20 is a particularly clear
boundary.

### Crypto

| horizon | median A/F | wins |
|---:|---:|
| 1 | 1.081 | 1/8 |
| 7 | 1.001 | 3/8 |
| 30 | 1.038 | 2/8 |

The h=7 crypto horizon is approximately a tie, whereas h=1 is materially worse.

## Combined frequency-aware evidence

Combining the development, pre-frozen replication, and large robustness panels
gives **92 distinct financial series**:

- 32 ETFs;
- 48 stocks;
- 12 crypto assets.

Across all three panels:

| class | series | cells | median A/F | adaptive wins | median frozen/no-change |
|---|---:|---:|---:|---:|---:|
| ETF | 32 | 96 | 1.032 | 21/96 | ~1.000 |
| stock | 48 | 144 | 1.022 | 23/144 | ~1.000 |
| crypto | 12 | 36 | 1.014 | 8/36 | ~1.000 |

By horizon across all available financial panels:

- ETF h=1: median 1.036, wins 8/32;
- ETF h=5: median 1.039, wins 6/32;
- ETF h=20: median 1.028, wins 7/32;
- stock h=1: median 1.031, wins 11/48;
- stock h=5: median 1.007, wins 11/48;
- stock h=20: median 1.031, wins 1/48;
- crypto h=1: median 1.076, wins 2/12;
- crypto h=7: median 1.002, wins 4/12;
- crypto h=30: median 1.038, wins 2/12.

## Structural interpretation

The strong fixed comparator remains extremely close to no-change across a broad
cross-section. This is not restricted to a few hand-picked assets.

The empirical pattern is consistent with:

1. long-history forecast selection learning a conservative price-level forecast;
2. local adaptive re-selection occasionally finding useful departures;
3. those departures failing often enough that median OOS performance is worse;
4. the cost of local adaptation depending materially on horizon.

The result should not be summarized as "adaptive never works." Individual
series/horizons can show sizeable gains. The correct statement is that broad
unconditional adaptive superiority is not supported for financial price levels.

## Next computational checks

Two distinct questions remain and should not be conflated.

### A. Denser temporal origins

Repeat the same frozen 64-series panel with `preset=paper`, which changes the
daily outer step from 20 to 5 while keeping the method unchanged.

This tests whether the explore-origin subsample materially changes the pooled
results.

### B. Finer lambda root-discovery grid

Only after the paper-density run, repeat with `n_grid=1025`.

The lambda grid is not the final parameter discretization: Brent refines roots
continuously after brackets are discovered. Therefore 1025 points test numerical
root-discovery stability, not a richer forecasting model.

If "larger grid" means adding more candidate L or d values, that is a separate
post-confirmatory model-expansion study and must be labeled exploratory because
the existing panels have already been inspected.

## Decision

The cross-sectional evidence is already strong enough to preserve the
financial boundary in the manuscript.

Run the denser paper-origin version next, then the 1025 discovery-grid
sensitivity if computational cost is acceptable. Do not use either sensitivity
to discard the current negative result.
