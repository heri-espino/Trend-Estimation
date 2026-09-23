# Checkpoint — Selector-Memory Sensitivity Results

Date: 2026-09-23

Status: **PASS; freeze M=20 for the next adaptive-value experiment**

Run:

`results/forecast_optimal_smoothing/20260923T121051Z_selector-memory_explore_a42d446/`

Commit containing the run: `6351f38` (`ran`).

## Design

The study repeated the paired within-series persistence-transition experiment
while changing only the number of retained inner rolling validation origins:

\[
M\in\{5,10,20,30\}.
\]

With inner step 3, these correspond to nominal validation spans of roughly
12, 27, 57, and 87 observations.

The full run used:

- 30 seeds;
- four paired paths: stable_low, low_to_high, high_to_low, stable_high;
- horizons {1,3,6,12};
- 1,920 seed/memory/transition/horizon configurations;
- 113,280 outer-origin rows;
- wide log-lambda domain [-18,24] with 321 discovery points;
- elapsed time about 7,151 s (119.2 min).

## Main result: selector memory explains a large share of adaptation delay

For low_to_high, the 80% smoothness adaptation delay changes as follows:

| M | h=1 | h=3 | h=6 | h=12 |
|---:|---:|---:|---:|---:|
| 5 | 12 | 18 | 21 | 63 |
| 10 | 27 | 33 | 33 | 36 |
| 20 | 54 | 60 | 81 | 87 |
| 30 | 84 | 84 | 96 | 99 |

For high_to_low:

| M | h=1 | h=3 | h=6 | h=12 |
|---:|---:|---:|---:|---:|
| 5 | 15 | 9 | 15 | 18 |
| 10 | 15 | 27 | 27 | 27 |
| 20 | 30 | 39 | 48 | 45 |
| 30 | 48 | 45 | 48 | 81 |

Thus the slow response in Exploration 04 was not an intrinsic property of the
selected estimation window L alone. Inner-selector memory M is a major source
of adaptation inertia.

The directional asymmetry remains: low_to_high is generally slower than
high_to_low even after shortening M, especially at longer horizons.

## Forecast-skill tradeoff

Short selector memory adapts quickly but materially degrades untouched OOS
forecast accuracy on stationary controls.

Pooled relative RMSFE across stable_low and stable_high is:

| M | h=1 | h=3 | h=6 | h=12 |
|---:|---:|---:|---:|---:|
| 5 | 0.975 | 0.885 | 0.775 | 0.612 |
| 10 | 0.896 | 0.824 | 0.729 | 0.580 |
| 20 | 0.858 | 0.793 | 0.699 | 0.555 |
| 30 | 0.846 | 0.784 | 0.686 | 0.544 |

Relative to M=30, the stable-control RMSFE penalty for M=20 is only:

- +1.46% at h=1;
- +1.09% at h=3;
- +1.91% at h=6;
- +2.12% at h=12.

By comparison, M=10 is about 5.0-6.7% worse than M=30 and M=5 is about
12.5-15.3% worse.

On the transition paths themselves, M=20 stays within about 0.1-2.0% of M=30
across all horizons, while substantially reducing adaptation delay.

## Protocol decision

For the next experiment, freeze

\[
\boxed{M=20}
\]

as the exploratory selector-memory protocol.

Decision rule:

> choose the shortest tested selector memory whose pooled stable-control
> relative RMSFE remains within approximately 2.5% of the M=30 reference at
> every horizon.

M=20 is the only shortened memory satisfying that rule. It offers a material
adaptation-speed gain without the much larger forecast-skill penalty seen at
M=10 and M=5.

This is a **protocol choice for the next stage**, not a universal scientific
claim that M=20 is optimal. M=30 should remain a robustness setting in the
final design.

## Scientific interpretation

The project should keep estimator memory and selector memory conceptually
separate:

\[
L=\text{observations used to fit the trend model},
\]

whereas

\[
M=\text{historical forecast-validation origins retained by the selector}.
\]

M remains a validation-protocol parameter rather than a fourth coordinate of
the canonical adaptive object.

## Next experiment

With M=20 fixed, test the **value of adaptation** directly.

At each seed/series/horizon compare after T0:

1. adaptive: re-select (d,L,S) at every outer origin using M=20;
2. frozen-pre: select (d,L,S) once at T0 using only pre-change data, then keep
   those hyperparameters fixed while continuing to refit on newly observed
   data;
3. no-change forecast.

Run the same comparison on stable_low and stable_high controls. The stable
controls measure the cost/benefit of repeated re-selection when no regime
change occurs, while transition-minus-control comparisons isolate value that is
specific to adaptation.