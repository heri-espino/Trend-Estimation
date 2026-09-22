# Checkpoint — First Paper-Scale Simulation Run

Date: 2026-09-21

Run directory:

`results/forecast_optimal_smoothing/20260922T034447Z_paper_21682bd/`

## Run identity

This was not a smoke or quick run. It was the full current `paper` preset.

- Git commit: `21682bd`
- seeds: 30
- observations per simulated series: 240
- stochastic grid:
  - slope-noise standard deviation: 0.002, 0.01, 0.03
  - observation-noise standard deviation: 0.2, 0.5, 1.0
  - AR(1) coefficient: 0.0, 0.4, 0.8
  - horizon: 1, 3, 6
- candidate orders: 1, 2, 3
- candidate windows: 24, 48, 72
- configurations: 2,430
- outer-origin rows: 48,600
- elapsed time: 1,839.32 s (about 30.7 min)

The run is large enough to expose systematic structure, but it should still be
treated as a first paper-scale diagnostic because the lambda-boundary behavior
below requires follow-up.

## First empirical pattern: forecast-optimal and recovery-optimal smoothing differ

Across all 48,600 outer-origin rows:

[
overline S^star_{mathrm{forecast}}approx 0.779,
qquad
overline S^star_{mathrm{recovery}}approx 0.954,
]

so the average gap is

[
overline{
S^star_{mathrm{forecast}}
-
S^star_{mathrm{recovery}}
}
approx -0.174.
]

This confirms that latent-trend recovery and forecasting the observed process
are not interchangeable objectives in this simulation design.

## Horizon pattern

Aggregating across the stochastic grid and seeds:

| horizon | mean forecast smoothness | mean recovery smoothness | mean gap | pooled relative RMSFE |
|---:|---:|---:|---:|---:|
| 1 | 0.678 | 0.946 | -0.268 | 0.850 |
| 3 | 0.790 | 0.955 | -0.164 | 0.749 |
| 6 | 0.870 | 0.960 | -0.091 | 0.617 |

The gap between forecast-optimal and recovery-optimal smoothing shrinks as the
forecast horizon grows.

## AR(1) persistence is the strongest first-run mechanism

The cleanest pattern is obtained by conditioning on the observation-noise
AR(1) coefficient.

### Independent observation noise: phi = 0

| h | forecast smoothness | recovery smoothness | gap | pooled relative RMSFE |
|---:|---:|---:|---:|---:|
| 1 | 0.939 | 0.957 | -0.018 | 0.776 |
| 3 | 0.959 | 0.959 | +0.001 | 0.694 |
| 6 | 0.958 | 0.959 | ~0.000 | 0.570 |

For horizons 3 and 6, the forecast and recovery optima are essentially the same
on average.

### Moderate persistence: phi = 0.4

| h | forecast smoothness | recovery smoothness | gap | pooled relative RMSFE |
|---:|---:|---:|---:|---:|
| 1 | 0.715 | 0.942 | -0.227 | 0.924 |
| 3 | 0.902 | 0.959 | -0.057 | 0.778 |
| 6 | 0.937 | 0.964 | -0.026 | 0.626 |

### Strong persistence: phi = 0.8

| h | forecast smoothness | recovery smoothness | gap | pooled relative RMSFE |
|---:|---:|---:|---:|---:|
| 1 | 0.380 | 0.939 | -0.559 | 0.936 |
| 3 | 0.510 | 0.946 | -0.436 | 0.800 |
| 6 | 0.714 | 0.959 | -0.245 | 0.664 |

This is the most important first scientific result.

A plausible mechanism is that persistent observation error contains short-run
predictive information about future observations. A recovery-optimal smoother
tries to remove that component in order to estimate the latent trend. A
forecast-optimal smoother can benefit from retaining some of it, especially at
short horizons. As the horizon increases, the predictive contribution of an
AR(1) component decays approximately with powers of phi, and the
forecast-optimal smoothness moves toward the recovery-optimal smoothness.

This mechanism is consistent with the simulation design, but it remains an
interpretation to be tested explicitly rather than a final causal claim.

## Order selection changes with persistence

Across all outer origins:

- order 1: 15,734 selections
- order 2: 29,656 selections
- order 3: 3,210 selections

For phi = 0 and h = 3 or 6, order 2 is selected about 79% of the time.

For phi = 0.8:

- h = 1: order 1 about 62.7%
- h = 3: order 1 about 58.0%
- h = 6: order 2 about 55.6%

Thus the selected difference order is itself state/horizon dependent in these
simulations.

## Window selection

Across all outer origins:

- L = 24: 15,685
- L = 48: 15,148
- L = 72: 17,767

There is no universal winning window. Longer windows become more common at
longer horizons for phi = 0 and 0.4, while strongly persistent noise produces a
more mixed window-selection pattern.

This supports keeping L as an explicit part of the research object rather than
fixing it in advance.

## Important numerical diagnostic: many lambda selections hit search boundaries

The forecast lambda search currently uses

[
loglambdain[-10,16].
]

Among the 48,600 outer-origin selections:

- 3,468 (about 7.1%) hit the lower lambda boundary;
- 6,916 (about 14.2%) hit the upper lambda boundary;
- about 14.2% have normalized smoothness above 0.999.

Roughly one fifth of selections are therefore on a lambda boundary.

This does **not** invalidate the run, but it means the current bounds cannot yet
be treated as innocuous numerical limits. Before freezing paper results we
should determine whether these are genuine near-zero/near-infinite smoothing
optima or artifacts of a search interval that is too narrow.

Required follow-up:

1. rerun a targeted subset with substantially wider log-lambda bounds;
2. identify which stochastic regimes produce lower/upper-bound selections;
3. inspect objective/derivative curves for representative boundary cases;
4. decide whether the paper should represent boundary solutions explicitly
   rather than by a large finite lambda.

## Important metric correction: do not average blockwise relative RMSFE

The first summary file contains means/medians of

[
rac{RMSE_{mathrm{method,block}}}
{RMSE_{mathrm{benchmark,block}}}.
]

This ratio can explode whenever a particular no-change benchmark block has
near-zero error. Some first-run rows show exactly this behavior.

The primary aggregate metric should instead pool squared errors first and then
form the ratio:

[
oxed{
RMSFE_{mathrm{rel,pooled}}
=
sqrt{
rac{
sum e_{mathrm{method}}^2
}{
sum e_{mathrm{benchmark}}^2
}
}.
}
]

All relative-RMSFE values reported in this checkpoint use the pooled
construction, not the arithmetic mean of blockwise ratios.

The experiment writer has been updated so future `summary.csv` files contain
`pooled_relative_rmsfe` explicitly. Existing raw results remain unchanged for
reproducibility.

## Current interpretation

The first full run supports the central research direction:

[
oxed{
S^star_{mathrm{forecast}}

eq
S^star_{mathrm{recovery}}
}
]

in important stochastic regimes, and the difference depends strongly on both
forecast horizon and residual persistence.

The strongest pattern is not simply "more volatility implies more/less
smoothing." Instead, serial dependence in the observation error materially
changes the amount of variation that is useful to retain for forecasting.

That is much closer to the intended paper question:

[
S^star
=
S^star(
h,
L,
	ext{persistence},
	ext{noise scale},
	ext{trend roughness}
).
]

## Next experiments

Before interpreting the paper-scale grid as final:

1. perform the lambda-boundary stress test;
2. add a direct AR(1)-mechanism diagnostic, including the decay with horizon;
3. inspect trend-roughness and observation-noise interactions after controlling
   for phi;
4. add the two-regime within-series experiment;
5. regenerate paper-scale results only if the stress tests imply a numerical
   design change.

This run should be preserved as the first complete paper-scale checkpoint.
