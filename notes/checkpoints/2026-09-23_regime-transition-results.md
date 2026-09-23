# Checkpoint — Within-Series Persistence Regime Transition Results

Date: 2026-09-23

Status: **PASS, with selector-memory follow-up required**

Run:

`results/forecast_optimal_smoothing/20260923T055447Z_regime-transition_explore_6623c55/`

Commit containing the run: `86f5deb` (`ran04`).

## Design

- 30 seeds;
- 4 paired paths: stable_low, low_to_high, high_to_low, stable_high;
- horizons h in {1,3,6,12};
- n=300, regime point T0=180;
- slope-noise std 0.01;
- observation-noise std 0.5;
- orders {1,2,3};
- windows {24,48,72};
- outer step 3;
- inner step 3;
- max inner origins 30;
- wide numerical domain log-lambda in [-18,24];
- 321 derivative-discovery points;
- 480 seed/transition/horizon configurations;
- 28,320 outer-origin rows;
- elapsed time about 1,895 s (31.6 min).

## Main result: the adaptive method moves toward the new regime

The experiment directly tracks

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h}).
\]

Before the regime point, each transition path is identical to its matched
start-regime control. After the change, both transition directions move toward
their matched target-regime controls.

### Smoothness adaptation delay

The aggregate 50% / 80% smoothness adaptation delays, measured in post-change
observations available at the forecast origin, are:

| direction | h | 50% | 80% |
|---|---:|---:|---:|
| high_to_low | 1 | 18 | 48 |
| high_to_low | 3 | 27 | 45 |
| high_to_low | 6 | 27 | 48 |
| high_to_low | 12 | 69 | 81 |
| low_to_high | 1 | 60 | 84 |
| low_to_high | 3 | 72 | 84 |
| low_to_high | 6 | 90 | 96 |
| low_to_high | 12 | 96 | 99 |

Adaptation is therefore strongly directional: high-to-low persistence
transitions are detected much faster than low-to-high transitions.

Longer horizons generally adapt more slowly, although the reference separation
between the stable-low and stable-high controls also becomes much smaller at
long horizons. The mean absolute reference smoothness separation is about
0.619 at h=1, 0.500 at h=3, 0.228 at h=6, and only 0.090 at h=12. Therefore
h=12 adaptation ratios should be interpreted more cautiously.

## The full configuration adapts, not only smoothness

Using relative origins >=72 as the late post-change phase:

- high_to_low average order-match-to-target share across horizons: ~0.87;
- low_to_high average order-match-to-target share: ~0.92;
- high_to_low average window-match-to-target share: ~0.68;
- low_to_high average window-match-to-target share: ~0.70;
- high_to_low average joint (order, window) target match: ~0.63;
- low_to_high average joint target match: ~0.67.

The late mean absolute smoothness gap to the matched target is about 0.015 for
high_to_low and 0.067 for low_to_high.

Thus all three coordinates show movement toward the new regime, although L is
less sharply identified than d and S.

## Window-length behavior

The selected estimation window does not simply shorten after every regime
change.

For low_to_high, shorter windows appear clearly at short/intermediate horizons:

- h=1: mean window ~47.7 pre-change, ~42.5 mid-transition, ~44.1 late;
- h=3: ~51.7 pre, ~39.3 mid, ~44.8 late;
- h=6: ~52.5 pre, ~44.5 mid, ~47.5 late.

For h=12 this shortening is weak or absent.

For high_to_low the window response is less monotone. Therefore the paper must
not claim a universal rule that regime changes imply shorter L.

## Forecast behavior relative to no-change

The adaptive smoother's pooled relative RMSFE versus the no-change forecast
shows a real transition cost.

For low_to_high at h=1:

- pre-change: ~0.80;
- early post-change: ~1.37;
- mid-transition: ~1.12;
- late: ~0.96.

So the method temporarily loses to no-change immediately after persistence
rises, then recovers as its configuration adapts.

For high_to_low at h=1:

- pre-change: ~1.03;
- early post-change: ~0.89;
- mid-transition: ~0.87;
- late: ~0.79.

The asymmetry is consistent with the much faster configuration adaptation in
the high_to_low direction.

At longer horizons the adaptive smoother is generally below the no-change
benchmark even during the transition, but the low_to_high path still performs
worse than its stable-low control during the adaptation period.

## Critical follow-up: selector memory

The experiment reveals that adaptation delay is not governed only by the
selected estimation window L.

The inner selector uses:

- max_inner_origins = 30;
- inner_step = 3.

Therefore its rolling validation objective can retain roughly 87-90
observations of historical validation origins.

With the current design, the first outer origin at which all retained inner
validation origins are post-regime occurs at approximately:

| h | all 30 inner origins post-regime |
|---:|---:|
| 1 | 90 observations after T0 |
| 3 | 90 |
| 6 | 93 |
| 12 | 99 |

This is strikingly close to the 80% low_to_high adaptation delays
(84, 84, 96, 99).

Thus the slow low_to_high response is plausibly driven in substantial part by
**selector-memory contamination**, not only by the final fitted window L.

This is not a flaw in chronological validation, but it is a methodological
parameter of the adaptive forecasting method that must be isolated before
claiming an intrinsic adaptation delay for (d,L,S).

## Decision

Exploration 04 passes the core scientific question: the forecast-optimal
configuration tracks a within-series persistence regime change.

However, do **not** move directly to adaptive-vs-fixed performance yet.

The next required experiment is a selector-memory sensitivity study that varies
the number of retained inner rolling origins while holding the DGP, seeds,
candidate (d,L), numerical domain, and outer evaluation fixed.

This will determine:

1. how much adaptation delay is protocol memory versus model memory;
2. whether shorter selector memory accelerates adaptation as expected;
3. how much forecast variance/performance is lost when the selector uses less
   historical validation data;
4. which selector-memory setting should be frozen before the final
   adaptive-vs-fixed experiment.