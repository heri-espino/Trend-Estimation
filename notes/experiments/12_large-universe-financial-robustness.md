# Experiment 12 — Large-Universe Financial Robustness

Date designed: 2026-09-29

Status: **panel frozen after held-out replication; robustness run next**

## Role

The pre-frozen held-out replication has already been inspected and confirmed
that adaptive re-selection does not broadly dominate frozen-all-pre/no-change
for financial price levels.

This experiment is therefore **not another confirmatory replication**. Its role
is to estimate how broadly that boundary persists across a much larger
cross-section while keeping the method unchanged.

## Frozen method

Use the development-selected frequency-aware policy without modification:

- orders: {1,2,3};
- daily windows: {63,126,252};
- selector memory: M=51;
- inner step: 5;
- log-lambda range: [-18,24];
- 321-point stationary-point discovery grid;
- Brent root refinement after discovery;
- final 40% chronological OOS evaluation;
- primary comparator: frozen-all-pre;
- secondary comparator: frozen-local with M=51;
- external benchmark: no-change.

Use the `paper` preset so daily outer origins are evaluated every 5
observations rather than every 20.

## Frozen robustness universe

64 new series, all distinct from both the development and held-out replication
panels.

### Equity ETFs — 20

IVV, SCHB, ITOT, VO, VB, VUG, VTV, IWF, IWD, MDY, IJH, IJR, XLY, XLP, XLI,
XLB, XLU, SMH, VEA, VWO.

### Stocks — 36

AMZN, GOOGL, META, NVDA, TSLA, ORCL, IBM, CSCO, CRM, ADBE, AVGO, AMD, PEP,
MCD, NKE, DIS, COST, TGT, MRK, PFE, ABBV, UNH, LLY, GS, MS, C, BLK, SLB, COP,
OXY, BA, GE, MMM, DE, UPS, FDX.

### Crypto — 8

SOL-USD, ADA-USD, DOGE-USD, BCH-USD, LINK-USD, XLM-USD, AVAX-USD, DOT-USD.

## Scale

Each series contributes three horizons, so the run contains 192
series/horizon tasks before outer-origin expansion.

Relative to the prior explore runs, `paper` makes the OOS origin grid four
times denser for daily data.

## Why not enlarge the lambda discovery grid in the main run?

The 321-point log-lambda grid is a **root-discovery device**, not the final
lambda discretization. Bracketed stationary points are refined continuously
with Brent.

Therefore a 1025-point rerun answers a numerical-stability question
("did 321 points miss brackets?") rather than a substantive model question.
Keep 321 for the main large-universe run.

If desired after the main run, use the exact same panel with
`--n-grid 1025` as a numerical sensitivity check. Do not select between 321
and 1025 based on forecast performance.

## Primary summaries

Report by class and horizon:

- pooled adaptive/frozen-all-pre RMSFE;
- pooled adaptive/no-change RMSFE;
- series-level distribution of those ratios;
- fraction of series where adaptive wins;
- median and interquartile range across series;
- selected d/L/S distributions;
- selector turnover.

Cross-series breadth is more informative here than simply multiplying
overlapping time origins.

## Command

~~~bash
python experiments/forecast_optimal_smoothing/run_real_data_validation.py --panel large-robustness --preset paper --scale-policy frequency-aware --workers 32
~~~

Optional later numerical sensitivity:

~~~bash
python experiments/forecast_optimal_smoothing/run_real_data_validation.py --panel large-robustness --preset explore --scale-policy frequency-aware --n-grid 1025 --workers 32
~~~
