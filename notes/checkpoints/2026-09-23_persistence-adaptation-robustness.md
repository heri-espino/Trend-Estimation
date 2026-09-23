# Checkpoint — Persistence Adaptation Value Robust to Selector Memory

Date: 2026-09-23

Status: **PASS; persistence mechanism closed for the exploratory stage**

M=30 robustness run:

`results/forecast_optimal_smoothing/20260923T234343Z_adaptive-value_explore_ebdc074/`

Commit containing the run: `6b274fd` (`ran`).

Reference M=20 run:

`results/forecast_optimal_smoothing/20260923T210337Z_adaptive-value_explore_296c581/`

## Direct adaptive versus frozen-pre result

The M=30 robustness run preserves the direct Level-III result. All eight
transition/horizon pooled RMSE ratios remain below one:

| direction | h=1 | h=3 | h=6 | h=12 |
|---|---:|---:|---:|---:|
| low_to_high, M=20 | 0.679 | 0.811 | 0.885 | 0.793 |
| low_to_high, M=30 | 0.768 | 0.863 | 0.942 | 0.943 |
| high_to_low, M=20 | 0.879 | 0.861 | 0.855 | 0.875 |
| high_to_low, M=30 | 0.884 | 0.879 | 0.906 | 0.864 |

Thus adaptive re-selection continues to outperform pre-regime hyperparameters
that are frozen at T0, even when the inner selector retains 30 origins.

The magnitude changes with selector memory, especially for low_to_high at
long horizons, but the sign of the direct result does not.

## Transition-specific excess adaptation value

The matched-control excess

\[
\Delta A
=
A_{transition}-A_{matched\ stable\ control}
\]

also preserves the exact sign pattern from M=20:

| direction | h=1 | h=3 | h=6 | h=12 |
|---|---:|---:|---:|---:|
| low_to_high, M=20 | +0.0829 | +0.0296 | -0.0260 | -0.0242 |
| low_to_high, M=30 | +0.0720 | +0.0197 | -0.0183 | -0.0343 |
| high_to_low, M=20 | +0.1129 | +0.0995 | +0.0707 | +0.0340 |
| high_to_low, M=30 | +0.0978 | +0.0932 | +0.0466 | +0.0359 |

Therefore the scientific interpretation is not an artifact of choosing M=20.

## Seed-level consistency for M=30

Using the 30 seed-level mean excess advantages and approximate two-sided t
intervals as Monte Carlo diagnostics:

| direction | h | mean Delta A | approx. 95% interval | positive seeds |
|---|---:|---:|---:|---:|
| low_to_high | 1 | +0.0720 | [0.0516, 0.0923] | 26/30 |
| low_to_high | 3 | +0.0197 | [0.0016, 0.0378] | 21/30 |
| low_to_high | 6 | -0.0183 | [-0.0406, 0.0040] | 8/30 |
| low_to_high | 12 | -0.0343 | [-0.0810, 0.0125] | 12/30 |
| high_to_low | 1 | +0.0978 | [0.0526, 0.1429] | 25/30 |
| high_to_low | 3 | +0.0932 | [0.0585, 0.1278] | 26/30 |
| high_to_low | 6 | +0.0466 | [0.0183, 0.0749] | 24/30 |
| high_to_low | 12 | +0.0359 | [-0.0188, 0.0906] | 20/30 |

The same cells that were clearly positive under M=20 remain clearly positive
under M=30: low_to_high at h=1,3 and high_to_low at h=1,3,6. The h=12
high_to_low mean remains positive but uncertain.

## Final persistence conclusion for this stage

Three claims now survive both M=20 and M=30:

1. persistence changes move the forecast-optimal configuration
   (d*, L*, S*);
2. adaptive re-selection beats frozen-pre configurations in pooled OOS RMSE
   across both transition directions and all studied horizons;
3. the extra value attributable specifically to a regime change is
   directional and horizon dependent.

Do not claim that every persistence change produces positive excess adaptation
value at every horizon.

## Decision

Close the persistence mechanism for the exploratory stage.

Next isolate **observation-noise scale** while holding persistence, latent
roughness, level, and slope-shift mechanisms fixed. Use the same paired
stable/transition architecture so the adaptation-value estimand remains
comparable.