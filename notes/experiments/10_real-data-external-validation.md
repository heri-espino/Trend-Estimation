# Experiment 10 — Real-Data External Validation

Date designed: 2026-09-29

Status: **implementation ready; exploratory run next**

## Purpose

The 1,000-seed controlled Monte Carlo established that forecast-optimal
((d,L,S)) is regime- and horizon-dependent and that adaptive re-selection can
have positive, neutral, or negative value depending on mechanism and
direction.

This experiment asks the external-validity question:

> Does the same adaptive forecasting object produce useful and interpretable
> behavior in observed macroeconomic, broad-market, equity, and crypto series
> whose data-generating process is not controlled by the experimenter?

This is an application/external-validation stage, not a new simulation
mechanism search.

## Frozen initial universe

### Macroeconomic primary application

- `GDPC1`: US real GDP, quarterly;
- `INDPRO`: US industrial production, monthly.

The initial run uses current-vintage FRED snapshots only as an exploratory
screen. Paper-final macro results require ALFRED vintage-correct replication.

### Broad-market / ETF application

- SPY;
- QQQ;
- IWM;
- DIA;
- EFA;
- EEM.

These are the main financial-market application because they provide broad
exposure and reduce the temptation to select individual stocks based on
outcomes.

### Individual-stock robustness panel

Frozen before seeing results:

- AAPL;
- MSFT;
- JPM;
- XOM;
- JNJ;
- WMT.

This small panel is intentionally cross-sector and is a robustness/stress
sample, not a claim about the full US equity cross-section.

### Crypto stress test

- BTC-USD;
- ETH-USD.

## Transformation

For every positive level or adjusted price,

[
y_t=log P_t.
]

For macro series, (P_t) denotes the positive published level/index rather
than a traded price.

This keeps the active object as trend forecasting on levels. Returns are not
the primary target in this experiment.

## Horizons

- GDP: (hin{1,2,4}) quarters;
- INDPRO: (hin{1,3,6,12}) months;
- ETFs/stocks: (hin{1,5,20}) trading observations;
- crypto: (hin{1,7,30}) daily observations.

## Candidate configuration

To preserve continuity with the simulation study:

- (din{1,2,3});
- (Lin{24,48,72}) observations;
- (M=20) selector origins;
- log-lambda range ([-18,24]);
- 321-point discovery grid for explore/paper presets.

## Chronology

Each series uses an initial chronological training segment followed by untouched
OOS evaluation. The exploratory default reserves the final 40% of observations
for OOS forecasting.

At the first OOS origin:

- `frozen-all-pre` selects ((d,L,lambda)) once using every valid earlier
  rolling origin;
- `frozen-local-M20` selects once using only the latest 20 validation origins.

At every later OOS origin:

- adaptive-M20 re-selects ((d,L,lambda)) causally;
- fixed comparators keep their hyperparameters but refit their trend state with
  newly observed data;
- no-change uses the last observed log level.

No future observation may influence the configuration selected at an origin.

## Data snapshots

The runner downloads missing series once into

`data/external/real_world/snapshot/`

and then reuses that exact snapshot. The CSV files are small and are tracked by
ordinary Git, not Git LFS, so the paper's working data are backed up in the
repository rather than existing only on one workstation.

Network access occurs only for a missing snapshot file or when the user
explicitly passes `--refresh-data`. A refresh intentionally replaces tracked
data and should be reviewed as a Git diff before committing.

Result metadata records hashes and date ranges for every input snapshot.

## Presets

### Smoke

Uses GDPC1, SPY, and BTC with one horizon each, a sparse outer step, and an
81-point lambda discovery grid.

### Explore

Uses the full frozen universe. Daily financial/crypto series are evaluated
about every 20 observations while macro series use every observation. This is
the first scientific screen.

### Paper

Uses the same frozen universe but a denser five-observation outer step for
daily series. Run only after inspecting the exploratory results and completing
the ALFRED macro design.

## Primary outputs

For each series/horizon:

[
R_{A/F}
=
sqrt{
rac{sum e_A^2}
{sum e_{mathrm{frozen-all-pre}}^2}
},
]

and

[
R_{A/RW}
=
sqrt{
rac{sum e_A^2}
{sum e_{mathrm{no-change}}^2}
}.
]

Also retain the complete selected ((d,L,S)) path and simple local descriptors:

- local first-difference scale;
- lag-one correlation of first differences;
- second-/first-difference roughness ratio.

These descriptors will support the later empirical study of

[
Theta^star_{T,h}=G(h,X_T,mathcal C).
]

## Interpretation rules

- Do not claim financial predictability merely because adaptive beats a fixed
  smoother.
- The no-change benchmark is mandatory for market-price levels.
- Do not cherry-pick assets after seeing results.
- A failure in stocks/crypto is scientifically informative and can define a
  boundary of usefulness.
- Current-vintage GDP/INDPRO results are exploratory until ALFRED replication.

## Post-screen scale diagnostic

The first completed exploratory screen used the literal simulation-scale
candidate set `L={24,48,72}` and `M=20` for every frequency. That run is
preserved and documented in
`notes/checkpoints/2026-09-29_real-data-exploratory-results.md`.

Because the calendar meaning of an observation differs sharply across
quarterly, monthly, and daily data, the runner now supports two explicit
policies:

### `--scale-policy observation`

Reproduces the first screen:

- windows: 24, 48, 72 observations;
- selector memory: M=20.

### `--scale-policy frequency-aware`

Pre-documented scale sensitivity:

- quarterly: windows 12, 24, 48;
- monthly: windows 24, 60, 120;
- daily: windows 63, 126, 252;
- selector memory:
  `max(20, ceil(L_max / inner_step))`.

Thus the selector-history span is approximately one longest candidate
estimation window rather than a fixed number of validation origins.

This is a diagnostic of scale transfer, not a post-hoc search over arbitrary
grids. The negative observation-scale result remains part of the evidence.

Run:

~~~bash
python experiments/forecast_optimal_smoothing/run_real_data_validation.py --preset explore --scale-policy frequency-aware --workers 32
~~~

