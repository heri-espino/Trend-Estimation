# Checkpoint 04 frozen confirmation report

Source run: `results/smoothness_cv/checkpoint_04/20261007T011201Z_confirmation_6c0b548`

## Audit status

This is the one-shot confirmation run for the dynamic tracked-smoothness rule
frozen from the development stage.

The forecast outputs in `decision_results.csv` were not modified after the
run. A stale reporting/metadata path initially labeled this directory as a
development run and wrote `confirmation_region_used=false`. That provenance
field has been corrected after auditing `outer_manifest.csv` and the saved
decision rows.

The confirmation sample is exactly the four previously reserved latest,
non-overlapping outer blocks for each of GDPC1, SPY, AAPL, and BTC-USD. The
only evaluated forecasting rules are:

- `recency_hl3` — frozen primary dynamic rule;
- `last` — newest tracked minimum;
- `pooled_cv_same_config` — pooled forecast-CV baseline.

No alternative dynamic rule was selected using these confirmation outcomes.

## Primary confirmation result

Across the 16 confirmation outer tests,

[
\text{geometric RMSFE ratio: recency-hl3 / pooled CV}
=
\boxed{0.6920}.
]

Thus the frozen dynamic rule had about **30.8% lower geometric RMSE** than the
pooled forecast-CV baseline over these confirmation decisions.

It beat pooled CV in **13 of 16** outer tests (81.25%).

Against the simpler newest-minimum rule,

[
\text{geometric RMSFE ratio: recency-hl3 / last}
=
\boxed{0.8137},
]

corresponding to about **18.6% lower geometric RMSE** overall, with wins in
9 of 16 outer tests.

## By-series confirmation results

| Series | RMSFE ratio vs last | RMSFE ratio vs pooled CV | Wins vs pooled |
| --- | ---: | ---: | ---: |
| AAPL | 0.4096 | 0.4561 | 4/4 |
| BTC-USD | 1.0277 | 1.0391 | 3/4 |
| GDPC1 | 1.2233 | 0.8176 | 3/4 |
| SPY | 0.8510 | 0.5917 | 3/4 |

The pooled-CV comparison therefore favors the frozen dynamic rule on an
aggregate basis in three of four series. BTC-USD is the exception by geometric
ratio, although the dynamic rule still wins three of its four individual
confirmation blocks.

The comparison with `last` is less uniform. AAPL and SPY favor the recency
average on a series-aggregate basis, while BTC-USD is nearly neutral and GDPC1
favors the newest minimum.

## Robustness to one-series deletion

For the comparison with pooled CV, the aggregate geometric RMSFE ratio remains
below one after omitting any single series:

| Omitted series | Dynamic / pooled geometric RMSFE |
| --- | ---: |
| AAPL | 0.7951 |
| BTC-USD | 0.6043 |
| GDPC1 | 0.6545 |
| SPY | 0.7290 |

This makes the confirmation advantage over pooled CV less dependent on a
single series than the advantage over `last`. If AAPL is omitted, the
dynamic/last aggregate ratio becomes 1.0228.

A simple series-cluster bootstrap diagnostic over only four series gives a
95% empirical interval of approximately **[0.519, 0.922]** for the
dynamic/pooled geometric RMSFE ratio and **[0.516, 1.121]** for dynamic/last.
Because there are only four clusters, these intervals are descriptive
sensitivity diagnostics rather than strong asymptotic inference.

## Interpretation

The pre-specified confirmation result supports the specific claim that
**exponentially averaging smoothness values along a tracked local-minimum
branch with a three-origin half-life can outperform the pooled forecast-CV
selector in this four-series confirmation panel**.

It does not establish universal superiority. The panel is small, the
series/horizons are heterogeneous, and the dynamic advantage over simply using
the newest tracked minimum is materially less stable than the advantage over
pooled CV.

The next paper-scale experiment should therefore test the mechanism under
controlled dynamic simulations and then on a broader public series panel,
without retuning the already confirmed `recency_hl3` rule on these 16 blocks.
