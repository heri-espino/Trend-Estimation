# Final Paper-Scale Monte Carlo Design

Date frozen: 2026-09-23

Status: **scientific design frozen; implementation/performance benchmarking next**

## Scientific objective

Test the paper's central claim at paper scale:

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C),
\]

and quantify when adaptive re-selection improves untouched out-of-sample
forecast loss relative to strong fixed configurations.

## Replication scale

Use **1,000 Monte Carlo seeds per mechanism** as the main paper-scale target,
with the run designed so it can be extended to 3,000 seeds without repeating
completed work.

This produces 16,000 seed/path/horizon configurations per mechanism and 48,000
across the three mechanisms before outer-origin expansion.

## Three frozen regime mechanisms

Do not add more isolated factors to the main simulation.

### 1. Persistence

- low phi = 0.0;
- high phi = 0.8;
- observation-noise std = 0.5;
- latent slope-noise std = 0.01.

### 2. Observation-noise scale

- low observation-noise std = 0.25;
- high observation-noise std = 0.75;
- phi = 0.0;
- latent slope-noise std = 0.01.

### 3. Latent-trend roughness

- low slope-noise std = 0.005;
- high slope-noise std = 0.02;
- observation-noise std = 0.5;
- phi = 0.0.

For every mechanism use paired paths:

- stable-low;
- low-to-high;
- high-to-low;
- stable-high.

For each seed, the transition path and its matched start-regime stationary
control must be identical before T0.

## Common time-series design

- n = 300;
- regime point T0 = 180;
- initial outer training origin = 120;
- outer step = 3;
- inner step = 3;
- horizons h in {1,3,6,12};
- no level shift;
- no deterministic slope shift.

## Candidate adaptive configuration

- orders d in {1,2,3};
- windows L in {24,48,72};
- normalized smoothness obtained from numerical lambda optimization;
- log-lambda domain [-18,24];
- discovery grid = 321 points;
- adaptive selector memory M = 20 inner origins.

Exploration 04B chose M=20 as the shortest tested selector memory retaining
near-M30 stationary forecast skill. Persistence Exploration 05 also established
qualitative robustness to M=30.

## Forecasting methods

### Primary: adaptive-M20

At each outer origin, use only information available at that origin and
re-select (d,L,lambda) using the latest M=20 chronological inner origins.

### Primary fixed comparator: frozen-all-pre

At T0, select (d,L,lambda) once using **all valid pre-T0 inner rolling
origins** at inner step 3. Keep those hyperparameters fixed after T0 while
continuing to refit the trend state on newly observed data.

This is deliberately stronger than adaptive's local selector in the amount of
historical validation evidence available at T0.

### Secondary fixed diagnostic: frozen-local-M20

Select once at T0 using the same most-recent M=20 inner origins as adaptive.
This comparator is retained to connect with exploratory results and diagnose
one-shot local-selection variance, but it is not the primary fixed baseline.

### External benchmark: no-change

Use the last observed level as the mandatory external benchmark.

## Primary quantities

### Regime dependence / target tracking

For each transition, compare adaptive (d,L,S) to matched stationary start and
target controls at the same seed, horizon, and relative origin.

Report:

- smoothness paths and target gaps;
- order-match share;
- window-match share;
- joint (d,L)-match share;
- late-regime target tracking;
- adaptation delays only when stationary-control separation is sufficiently
  large for the normalized progress ratio to be numerically meaningful.

### Direct adaptation value

For each fixed comparator F, use pooled squared errors:

\[
R_{A/F}
=
\sqrt{\frac{\sum e_A^2}{\sum e_F^2}}.
\]

Never average blockwise relative RMSE.

### Transition-specific excess adaptation value

For each paired transition/control:

\[
A=MSE_F-MSE_A,
\qquad
\Delta A=A_{transition}-A_{matched\ stable\ control}.
\]

Primary excess comparisons use frozen-all-pre. Frozen-local-M20 is secondary.

### Monte Carlo stability

Retain seed-level summaries. Report means with Monte Carlo uncertainty together
with medians/trimmed summaries when heavy-tailed seed effects are present.

Do not allow a few catastrophic fixed-baseline seeds to stand in for the
typical paired behavior without explicitly reporting that tail structure.

## Period summaries

Retain:

- early: 0 <= T-T0 < 36;
- mid: 36 <= T-T0 < 72;
- late: T-T0 >= 72;
- all-post.

## Numerical and computational requirements

- preserve exact chronology and no-future-information constraints;
- use cached spectral/eigenvalue objects where valid;
- parallelize independent seed/path/horizon configurations with worker
  processes;
- make results independent of process scheduling;
- write enough metadata to reproduce the exact run;
- final runner uses atomic seed batches of 10 seeds by default; each completed
  batch is persisted before the next begins, so a machine restart loses at
  most the currently running batch;
- re-running the same run-id automatically skips completed batches;
- increasing the target from 1,000 to 3,000 seeds reuses the first 1,000;
- heavy final simulation runs locally, not automatically on push.

## Robustness already established outside the final main grid

- wide lambda domain [-18,24] does not alter the persistence mechanism;
- persistence adaptation-value signs are robust to M=20 versus M=30;
- selector-memory sensitivity M in {5,10,20,30} is documented;
- frozen-all-pre removes the major high-roughness baseline fragility found
  with frozen-local-M20.

These results should be used as supporting/appendix robustness rather than
multiplying the main 1,000-seed grid unnecessarily.

## Stop rule

The main simulation design is frozen. Do not add another mechanism, horizon,
window family, or selector-memory setting to the main grid unless a concrete
reviewer-level scientific gap is identified.