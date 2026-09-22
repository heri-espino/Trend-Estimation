# Checkpoint — First Paper-Scale Simulation Run

Date: 2026-09-21

Run directory:

`results/forecast_optimal_smoothing/20260922T034447Z_paper_21682bd/`

## Run size

This was already the full `paper` preset, not a smoke/quick run.

- code commit: `21682bd`
- 30 seeds
- 3 trend-roughness levels
- 3 observation-noise levels
- 3 AR(1) persistence levels
- 3 horizons
- 2430 parameter configurations
- 20 outer origins per configuration
- 48,600 outer-origin rows
- elapsed time: 1839.32 s (about 30.7 minutes)

## First robust aggregate patterns

For each horizon, the pooled relative RMSFE is computed as

[
RMSFE_{m rel}
=
sqrt{
rac{overline{MSE}_{m method}}
{overline{MSE}_{m no-change}}
}.
]

This is preferable to averaging blockwise RMSFE ratios.

Across all stochastic regimes:

| horizon | mean forecast smoothness | mean recovery smoothness | mean gap | pooled relative RMSFE |
|---:|---:|---:|---:|---:|
| 1 | 0.678 | 0.946 | -0.268 | 0.850 |
| 3 | 0.790 | 0.955 | -0.164 | 0.749 |
| 6 | 0.870 | 0.960 | -0.091 | 0.617 |

The first major pattern is therefore:

[
S^star_{m forecast}
<
S^star_{m recovery}
]

on average, especially at short horizons, with the gap shrinking as the
forecast horizon grows.

## Persistence interaction

AR(1) persistence has a much stronger effect than a simple variance-only story.

At (phi=0), forecast-optimal and recovery-optimal smoothness are nearly the
same:

| phi | h | forecast S | recovery S | gap |
|---:|---:|---:|---:|---:|
| 0.0 | 1 | 0.939 | 0.957 | -0.018 |
| 0.0 | 3 | 0.959 | 0.959 | +0.001 |
| 0.0 | 6 | 0.958 | 0.959 | -0.000 |

At high persistence, (phi=0.8), the difference is large:

| phi | h | forecast S | recovery S | gap |
|---:|---:|---:|---:|---:|
| 0.8 | 1 | 0.380 | 0.939 | -0.559 |
| 0.8 | 3 | 0.510 | 0.946 | -0.436 |
| 0.8 | 6 | 0.714 | 0.959 | -0.245 |

A plausible interpretation to test, not yet a final claim, is that when the
observation noise is persistent, some of what a latent-trend recovery objective
would regard as noise contains short-horizon predictive information. A
forecast-optimal smoother may therefore deliberately smooth less so that the
fit retains part of this persistent component.

This gives a much sharper scientific distinction than “high variance requires
more or less smoothing.”

## Horizon effect

Mean selected window length and difference order also increase with horizon:

| h | mean order | mean window |
|---:|---:|---:|
| 1 | 1.68 | 47.18 |
| 3 | 1.73 | 49.07 |
| 6 | 1.82 | 50.84 |

Longer-horizon forecasts therefore tend to select slightly longer windows,
higher difference order, and substantially more smoothing.

## Trend roughness

Recovery-optimal smoothness behaves in the expected direction: rougher latent
trends require less smoothing.

For (h=1), mean recovery smoothness falls from about 0.967 at
(sigma_{m slope}=0.002) to 0.925 at (sigma_{m slope}=0.03).

Forecast-optimal smoothness does not follow the same monotone direction in the
marginal averages. That is scientifically useful rather than automatically a
problem: it reinforces that recovery-optimal and forecast-optimal smoothing are
different objectives. However, this must be checked conditionally on
persistence and noise scale before being written as a paper claim.

## Observation-noise scale

Recovery-optimal smoothness rises with observation-noise scale, as expected.

The marginal forecast-optimal smoothness at (h=1) instead decreases slightly
as observation-noise scale increases. This again suggests an interaction with
persistence/order/window selection and should not yet be interpreted in
isolation.

## Benchmark performance

Using pooled RMSFE rather than the mean of blockwise ratios, the smoother beats
the no-change benchmark on aggregate in all three horizon groups:

- h=1: 0.850
- h=3: 0.749
- h=6: 0.617

The relative advantage is larger at longer horizons in this simulated DGP.

## Metric caveat discovered

The current run's `summary.csv` contains `mean_relative_rmsfe`, which is the
arithmetic mean of per-block RMSFE ratios. That statistic can explode when the
benchmark happens to have nearly zero error in a particular block; values above
100 are present in some seed/configuration summaries.

For paper inference, do not use that column as the principal relative error.

Use the pooled ratio instead:

[
oxed{
RMSFE_{m rel,pooled}
=
sqrt{
rac{sum e_{m method}^2}
{sum e_{m benchmark}^2}
}.
}
]

The experiment writer has been updated so future `summary.csv` files include
`pooled_relative_rmsfe` explicitly and rename the old statistics as
`mean_block_relative_rmsfe` and `median_block_relative_rmsfe`.

## What this first run suggests

The strongest candidate result is not simply that optimal smoothness changes
with variance. It is the interaction

[
oxed{
S^star_{m forecast}
=
S^star(h,phi,	ext{trend roughness},	ext{noise scale},L,d)
}
]

and, in particular, the separation between forecast-optimal and
recovery-optimal smoothness under persistent disturbances.

The next analysis should therefore prioritize:

1. full interaction plots of (S^star_{m forecast}) versus (phi) and
   horizon;
2. the gap (S^star_{m forecast}-S^star_{m recovery});
3. order/window selection frequencies;
4. pooled relative RMSFE;
5. conditional effects of trend roughness and observation-noise scale;
6. boundary-selection diagnostics for lambda/smoothness;
7. a dedicated within-series regime-transition experiment.

No manuscript conclusion should be frozen until those diagnostics are done.
