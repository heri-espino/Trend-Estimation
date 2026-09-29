# Checkpoint — Frequency-Aware Real-Data Scale Sensitivity

Date: 2026-09-29

Status: **COMPLETED; scale mismatch mattered, but broad adaptive superiority is not supported**

Result:

`results/forecast_optimal_smoothing/20260929T195226Z_real-data-explore-frequency-aware_2586ef0/`

Result commit:

`148c34f` — `ran 20260929T195226Z_real-data-explore-frequency-aware_2586ef0`

## Purpose

The first real-data screen copied the simulation-scale policy

[
Lin{24,48,72},qquad M=20
]

to quarterly, monthly, and daily series. That screen was mostly negative.

The present run was pre-documented as a scale diagnostic using:

- quarterly GDP windows: ({12,24,48}), (M=48);
- monthly INDPRO windows: ({24,60,120}), (M=120);
- daily ETF/stock/crypto windows: ({63,126,252}), (M=51).

The data, universe, OOS fraction, horizons, model family, lambda domain, and
benchmarks remained otherwise unchanged.

## Run integrity

Completed:

- 16 series;
- 49 series/horizon cells;
- 10,160 OOS forecast blocks;
- 32 workers;
- 321-point discovery grid;
- frozen-all-pre primary comparator;
- no-change external benchmark.

## Class-level result

| class | observation-scale median A/F | frequency-aware median A/F | cells improved | frequency-aware wins |
|---|---:|---:|---:|---:|
| macro | 1.357 | 1.068 | 6/7 | 2/7 |
| ETF | 1.108 | 1.050 | 15/18 | 3/18 |
| stock | 1.122 | 1.022 | 17/18 | 5/18 |
| crypto | 1.100 | 1.003 | 6/6 | 2/6 |

Across all classes, **44 of 49 cells improved** relative to the literal
observation-scale transfer.

Thus the calendar-scale mismatch was a real design issue.

However, the median adaptive/frozen-all-pre ratio remains above one in every
class. Frequency-aware scaling converts many large losses into near-ties, but
it does not establish broad adaptive superiority.

## Frequency-aware positive cells

Cells with pooled adaptive/frozen-all-pre RMSFE below one include:

### Macro

- GDPC1 h=2: 0.935;
- GDPC1 h=4: 0.989.

### ETFs

- EEM h=1: 0.862;
- EEM h=5: 0.986;
- IWM h=20: 0.980.

### Stocks

- WMT h=1: 0.957;
- JPM h=1: 0.972;
- AAPL h=5: 0.977;
- WMT h=5: 0.985;
- MSFT h=5: 0.994.

### Crypto

- BTC h=1: 0.998;
- ETH h=7: 1.000 to three decimals.

These are development-panel observations, not final confirmatory findings.

## Near-tie structure

Many frequency-aware cells are close to one:

- macro: 3/7 within 2% of frozen-all-pre;
- ETFs: 7/18 within 2%;
- stocks: 9/18 within 2%;
- crypto: 5/6 within 2%.

The frequency-aware policy therefore substantially narrows the gap even where it
does not reverse the ranking.

## Selector stability

The frequency-aware policy also reduces selector turnover.

| class | old (d,L) turnover | new (d,L) turnover | new order turnover | new window turnover |
|---|---:|---:|---:|---:|
| macro | 0.325 | 0.129 | 0.016 | 0.122 |
| ETF | 0.460 | 0.400 | 0.058 | 0.378 |
| stock | 0.456 | 0.381 | 0.027 | 0.373 |
| crypto | 0.384 | 0.408 | 0.022 | 0.404 |

Macro and equity-like market series become materially more stable. Crypto
retains substantial window turnover even though order changes become rare.

Mean absolute smoothness changes between evaluated origins also fall sharply
relative to the first screen.

## Market-model boundary

Under the frequency-aware policy, adaptive selections overwhelmingly use
first-difference penalties:

- ETFs: d=1 at about 89.1% of OOS origins;
- stocks: d=1 at about 96.1%;
- crypto: d=1 at about 97.8%.

About 38--40% of market origins also select normalized smoothness below 0.01.

For the pure model, order d=1 with zero first-difference continuation produces
a constant future path. When lambda is near zero, the endpoint trend is also
near the observed endpoint, so the forecast approaches the no-change
benchmark.

The frozen-all-pre comparator shows this boundary especially clearly:

- stock median frozen/no-change RMSFE: approximately 1.000;
- crypto median frozen/no-change RMSFE: approximately 1.000;
- all 18 stock cells and all 6 crypto cells are within 1% of no-change.

Therefore the strong fixed selector often learns that the safest price-level
forecast is essentially no-change. Adaptive re-selection can lose when local
validation encourages a temporary departure from that conservative solution.

This is a substantive empirical boundary, not merely a tuning failure.

## Scientific conclusion

Two statements are simultaneously supported:

1. **Scale matters.** Calendar-aware estimator/selector memory materially
   improves transfer from simulation to real data.
2. **Adaptation is not broadly superior in observed price levels.** Even after
   the scale correction, frozen-all-pre/no-change remains difficult to beat on
   average.

The real-data evidence therefore sharpens the simulation result:

> adaptive forecast-optimal trend estimation can be valuable under genuine
> regime change, but local re-selection is not automatically beneficial when
> the observed process is close to a no-change price-level benchmark or when
> local regime evidence is weak.

## Data-snooping boundary and next step

The development panel has now informed the scale policy.

Do **not**:

- keep changing windows/M on this panel until adaptive wins;
- call a denser `paper` run on the same panel confirmatory;
- present isolated winning cells as general evidence.

The valid next step is to freeze the frequency-aware policy and evaluate it on
a **separate held-out replication panel** chosen before inspecting its results.

Macro remains separate: GDP/INDPRO require ALFRED vintage-correct replication
before any paper-final real-time macro claim.
