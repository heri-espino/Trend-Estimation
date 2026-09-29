# Current Project State

Last updated: 2026-09-29

This file is the shortest chronological handoff for the active
`Trend-Estimation` research program. It answers four questions:

1. What are we trying to establish?
2. What have we done?
3. What did the experiments show?
4. What should happen next?

For exact derivations and numbers, follow the linked notes/checkpoints rather
than treating this file as a substitute for them.

## 1. Scientific objective

The active paper studies:

> **Forecast-optimal trend estimation as an adaptive forecasting method, where
> smoothness, memory length and difference order depend on horizon and local
> regime.**

The central object is

[
Theta^star_{T,h}
=
(d^star_{T,h},L^star_{T,h},S^star_{T,h})
=
G(h,X_T,mathcal C).
]

The claim is intentionally conditional. The paper is not trying to show that
adaptive smoothing always wins.

Canonical source: `notes/research_objective.md`.

## 2. Mathematical and implementation foundation

Completed before the main experiments:

- pure penalized least-squares trend estimator;
- exact first/second smoother derivatives;
- exact forecast-loss derivatives;
- log-lambda stationary-point search using derivative scans + Brent roots;
- fixed-window forecast-optimal selection;
- nested chronological outer evaluation with direct leakage tests;
- normalized smoothness definition;
- no-change benchmark;
- oracle recovery-optimal target for simulations;
- Guerrero (2007) implementation audit and model naming cleanup.

Canonical compact summary: `notes/key_results.md`.

## 3. Controlled-simulation development

### First factorial

The first grid showed that forecast-optimal smoothness differs materially from
recovery-optimal smoothness and depends on horizon, noise, latent roughness,
and persistence.

This motivated mechanism studies rather than a claim about one universal
smoothness rule.

### Persistence mechanism

The persistence study showed that strong positive residual persistence at short
horizons can push the observed-series forecast optimum toward substantially
less smoothing than the latent/recovery optima.

A wider log-lambda search confirmed that this was not an artifact of the
original search boundary.

### Within-series regime transitions

Paired stationary controls and regime switches established that the full
selected configuration ((d,L,S)), not just lambda, moves toward the target
regime.

This also exposed two distinct memory concepts:

- (L): estimator memory;
- (M): selector/validation memory.

Selector memory materially controls adaptation delay.

### Adaptive versus frozen configurations

The first frozen comparator used only a local pre-transition selector history.
The latent-roughness experiments revealed that this baseline could itself be
fragile.

A stronger comparator was therefore defined:

- **primary:** frozen-all-pre;
- **secondary diagnostic:** frozen-local-M20;
- **adaptive:** adaptive-M20;
- **external benchmark:** no-change.

The fixed-baseline stress experiment showed that frozen-all-pre removes the
major stationary-high-roughness instability.

## 4. Final 1,000-seed controlled Monte Carlo

The paper-scale simulation completed 1,000 seeds for each of three mechanisms:

- persistence;
- observation-noise scale;
- latent-trend roughness.

It covered stable controls plus both transition directions and horizons
(hin{1,3,6,12}).

Main conclusion:

> Forecast-optimal ((d,L,S)) changes systematically with local regime and
> horizon, and adaptive re-selection can improve future forecasts relative to
> a strong fixed configuration, but the gain is mechanism-, direction-, and
> horizon-dependent.

Clearest positive transition-specific cases:

- persistence high-to-low at every studied horizon;
- observation-noise high-to-low at every studied horizon;
- latent roughness smooth-to-rough at every studied horizon.

Important boundaries:

- persistence low-to-high becomes negative at h=6 and h=12 after subtracting
  the matched stationary-control advantage;
- noise low-to-high is negative at h=1 and only modestly positive later;
- roughness rough-to-smooth has near-zero mean transition-specific excess;
- strong positive persistence at h=1 can still favor no-change over the
  adaptive trend forecast.

The Monte Carlo conclusions are stable enough at 1,000 seeds. Extending to
3,000 is optional precision work, mainly for the heavy-tailed smooth-to-rough
effect, not a required new experiment.

Full checkpoint:
`notes/checkpoints/2026-09-29_final-1000-seed-monte-carlo-results.md`.

## 5. First real-data external-validation screen

A unified real-data runner was added for:

- macro: GDPC1, INDPRO;
- broad ETFs: SPY, QQQ, IWM, DIA, EFA, EEM;
- stocks: AAPL, MSFT, JPM, XOM, JNJ, WMT;
- crypto: BTC-USD, ETH-USD.

The input snapshot is downloaded once, versioned, hashed, and reused so
repeated experiment runs do not silently change the data.

The first completed exploratory screen used the literal simulation-scale policy:

- windows (Lin{24,48,72}) for every frequency;
- selector memory (M=20).

Run size:

- 16 series;
- 49 series/horizon cells;
- 10,160 untouched OOS forecast blocks.

### Result

The direct simulation-scale transfer was mostly negative:

| class | median adaptive/frozen-all-pre RMSFE | cells adaptive < fixed |
|---|---:|---:|
| macro | 1.357 | 1/7 |
| ETF | 1.108 | 2/18 |
| stock | 1.122 | 1/18 |
| crypto | 1.100 | 0/6 |

The same basic failure also appears against no-change.

This result is preserved. It must not be hidden or replaced by a later
favorable sensitivity.

### Interpretation

The negative result appears throughout early/mid/late OOS subperiods for the
daily market classes.

The adaptive configuration also turns over frequently:

- macro: about 32% of evaluated origins;
- ETFs: about 46%;
- stocks: about 46%;
- crypto: about 38%.

Window changes account for most of the turnover.

This suggests selector instability may matter, but turnover alone does not
establish causality.

### Scale mismatch discovered

The literal (L={24,48,72}) policy means very different calendar memory:

- GDP: 6--18 years;
- INDPRO: 2--6 years;
- daily assets: roughly 1--3.5 trading months.

Because the theory explicitly contains series class (mathcal C), using the
same observation counts across frequencies is not automatically the correct
real-data design.

Full checkpoint:
`notes/checkpoints/2026-09-29_real-data-exploratory-results.md`.

## 6. Current next experiment

The next run is a **pre-documented frequency-aware scale sensitivity**, not a
search until the method wins.

Policy:

- quarterly GDP windows: {12,24,48};
- monthly INDPRO windows: {24,60,120};
- daily ETF/stock/crypto windows: {63,126,252};
- selector memory:
  `max(20, ceil(L_max / inner_step))`.

Command:

```bash
python experiments/forecast_optimal_smoothing/run_real_data_validation.py --preset explore --scale-policy frequency-aware --workers 32
```

The already inspected first panel means this is development work. Once the
real-data protocol is frozen, a separate held-out replication panel should be
used for the final financial external-validity claim.

## 7. Remaining work before a final manuscript claim

High priority:

1. run and interpret the frequency-aware real-data sensitivity;
2. freeze the real-data protocol after that diagnostic;
3. design a held-out replication panel for final financial validation;
4. replace current-vintage GDP/INDPRO evidence with ALFRED vintage-correct
   macro backtests;
5. complete the high-priority literature novelty audit, especially
   Guerrero/Cortés-Toto/Reyes (2018);
6. generate final simulation and real-data tables/figures;
7. add predictive-accuracy inference where appropriate;
8. finish the active manuscript.

## 8. Guardrails

- Preserve negative results.
- Do not tune real-data candidate grids repeatedly until adaptive wins.
- Do not call current-vintage macro backtests final.
- Do not interpret price-level RMSFE as trading profitability.
- Keep (d,L,S) together when describing the adaptive object.
- Keep selector memory (M) distinct from estimator memory (L).
- Do not make the final novelty claim before the literature audit is complete.
