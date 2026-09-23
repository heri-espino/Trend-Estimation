# Checkpoint — Adaptive vs Frozen-Pre Persistence Results

Date: 2026-09-23

Status: **Level III supported directly; transition-specific value is conditional**

Run:

`results/forecast_optimal_smoothing/20260923T210337Z_adaptive-value_explore_296c581/`

Commit containing the run: `bbf7a2f` (`ran`).

## Design

- 30 paired seeds;
- selector memory M=20;
- persistence paths: stable 0, 0->0.8, 0.8->0, stable 0.8;
- horizons {1,3,6,12};
- frozen-pre selects (d,L,lambda) once at T0=180 using only y[:T0];
- adaptive re-selects at every outer origin;
- both methods refit on newly available observations;
- no-change remains the external benchmark;
- 18,720 post-T0 outer-origin rows;
- elapsed time about 2,127 s (35.5 min).

## Direct adaptive-versus-frozen result

Using pooled post-regime squared errors,

\[
R_{A/F}=\sqrt{\frac{\sum e_A^2}{\sum e_F^2}}.
\]

All eight transition/horizon comparisons have R_A/F < 1:

| direction | h=1 | h=3 | h=6 | h=12 |
|---|---:|---:|---:|---:|
| low_to_high | 0.679 | 0.811 | 0.885 | 0.793 |
| high_to_low | 0.879 | 0.861 | 0.855 | 0.875 |

Thus adaptive re-selection reduces RMSE relative to hyperparameters frozen at
T0 for every studied persistence transition and horizon.

Approximate RMSE reductions are:

- low_to_high: 32.1%, 18.9%, 11.5%, 20.7%;
- high_to_low: 12.1%, 13.9%, 14.5%, 12.5%.

This establishes the direct Level-III inequality for the studied persistence
transitions:

\[
E[L_{adaptive}] < E[L_{frozen-pre}]
\]

at the aggregate Monte Carlo level.

## Why the stable controls matter

Repeated re-selection can also improve forecasts when no regime change occurs.
For example, on stable_low the adaptive/frozen RMSE ratios are approximately
0.871, 0.872, 0.855, and 0.746 for h=1,3,6,12.

Therefore direct adaptive superiority is not sufficient to attribute the gain
specifically to regime adaptation.

Define the per-block adaptive MSE advantage

\[
A=MSE_{frozen}-MSE_{adaptive}
\]

and the paired transition-specific excess

\[
\Delta A=A_{transition}-A_{matched\ stable\ control}.
\]

## Transition-specific excess adaptation value

All-post mean Delta A:

| direction | h=1 | h=3 | h=6 | h=12 |
|---|---:|---:|---:|---:|
| low_to_high | +0.0829 | +0.0296 | -0.0260 | -0.0242 |
| high_to_low | +0.1129 | +0.0995 | +0.0707 | +0.0340 |

Using the 30 seed-level mean Delta A values and a simple two-sided t interval
(diagnostic only; no multiplicity correction), approximate 95% intervals are:

| direction | h | mean Delta A | approx. 95% interval | positive seeds |
|---|---:|---:|---:|---:|
| low_to_high | 1 | +0.0829 | [0.0599, 0.1059] | 28/30 |
| low_to_high | 3 | +0.0296 | [0.0059, 0.0532] | 19/30 |
| low_to_high | 6 | -0.0260 | [-0.0538, 0.0018] | 13/30 |
| low_to_high | 12 | -0.0242 | [-0.0889, 0.0404] | 14/30 |
| high_to_low | 1 | +0.1129 | [0.0617, 0.1642] | 24/30 |
| high_to_low | 3 | +0.0995 | [0.0509, 0.1480] | 25/30 |
| high_to_low | 6 | +0.0707 | [0.0306, 0.1107] | 20/30 |
| high_to_low | 12 | +0.0340 | [-0.0124, 0.0805] | 16/30 |

These intervals are a Monte Carlo diagnostic, not a final inferential
procedure for the paper.

## Time structure

The transition-specific value is strongest after the configuration has had
time to move:

- high_to_low shows positive late-period Delta A at h=1,3,6,12;
- low_to_high is strongly positive at h=1, moderately positive at h=3, but
  does not exceed the stable-low re-selection benefit at h=6 or h=12.

At long horizons the stable-low series already benefits strongly from repeated
re-selection, so the transition does not add extra value beyond that baseline.

## Scientific conclusion

The evidence supports two distinct statements:

1. **Direct adaptation value:** for the studied persistence transitions,
   adaptive (d,L,S) beats frozen-pre at every horizon.
2. **Regime-specific adaptation value:** the additional benefit attributable
   specifically to the regime change is directional and horizon dependent.

Do not collapse these into a universal claim that regime adaptation always
adds value beyond ordinary rolling re-selection.

## Required robustness

Before moving to a new regime factor, repeat the same Exploration-05 design
with M=30. This checks that the Level-III conclusion and the directional
transition-specific pattern are not artifacts of the exploratory M=20
protocol.

Command:

~~~powershell
python experiments\forecast_optimal_smoothing\run_adaptive_value.py --preset explore --selector-max-inner-origins 30
~~~

If the M=30 run preserves the qualitative conclusions, proceed to isolated
observation-noise-scale transitions, then latent-trend-roughness transitions.