# Checkpoint 05 — Frozen external financial panel

**Status: FROZEN BEFORE RUN.**

CP04 produced a pre-specified confirmation result for the dynamic tracked-branch
rule `recency_hl3`. CP05 is a new external validation panel. It does not
retune the dynamic rule.

## Primary question

Does the already frozen dynamic rule

\[
\phi_{\mathrm{recency},H=3}
\]

retain a forecast advantage over (i) the newest tracked minimum and (ii) the
pooled forecast-CV selector on a much broader set of previously unused
financial series?

## Frozen panel inclusion rule

The data source is the repository snapshot manifest dated
`2026-09-29T21:40:44.625057+00:00`.

Include **every Yahoo snapshot series** satisfying all of:

1. asset class is `stock`, `etf`, or `crypto`;
2. at least 2060 observations are available;
3. the series was not used in CP04 development/confirmation.

Therefore AAPL, SPY, and BTC-USD are excluded. No series is selected using its
forecast performance.

The resulting frozen panel contains 64 series:

- 20 ETFs;
- 36 stocks;
- 8 cryptocurrencies.

Exact keys are hard-coded in `run_checkpoint_05.py` and the runner validates
the frozen snapshot-manifest timestamp.

## Forecast protocol

For every series use its most recent 2060 positive observations and evaluate
the four most recent non-overlapping 60-observation outer blocks.

For every outer block:

1. reserve the final 60 observations as untouched test;
2. reserve the preceding 60 observations as the final Validation-1 surface;
3. use only earlier history to choose one window for each `d=1,2,3,4`;
4. candidate windows are `63, 126, 252, 504`;
5. use step 5 and at most 30 historical origins;
6. recover up to five starting minima per order;
7. track with `track_epsilon = 0.10`;
8. use `candidate_spacing = 0.02` only within a surface;
9. select the persistent branch by the already frozen persistence + mean-Val2
   rule;
10. continue the selected branch to the final Val1 surface;
11. evaluate only the frozen dynamic rule `recency_hl3`, `last`, and
    `pooled_cv_same_config`;
12. freshly refit the trend on the newest selected window before forecasting
    the untouched test.

All three methods use the same selected `(d,L)` whenever a tracked branch
continues.

## Predeclared operational fallback

A broad panel can contain cases in which no historical branch continues to the
final Val1 surface. The forecasting method must remain defined.

If no branch continues:

- select `(d,L)` by the smallest historical aggregate Val1 loss among the
  already computed order/window candidates;
- compute pooled forecast-CV smoothness on that configuration;
- use that pooled forecast for all three named rules for this outer decision;
- mark `fallback_used = true`.

This fallback is deliberately conservative: a tracking failure contributes a
ratio of one rather than being dropped from the sample.

## Primary metrics

Primary:

\[
R_{\mathrm{pool}}
=
\exp\left[
\frac1N\sum_i
\log\frac{\mathrm{RMSE}_{\mathrm{recency},i}}
{\mathrm{RMSE}_{\mathrm{pooled},i}}
\right].
\]

Secondary:

\[
R_{\mathrm{last}}
=
\exp\left[
\frac1N\sum_i
\log\frac{\mathrm{RMSE}_{\mathrm{recency},i}}
{\mathrm{RMSE}_{\mathrm{last},i}}
\right].
\]

Report:

- geometric RMSE ratios;
- outer-block win rates;
- series-level geometric ratios and win shares;
- results by asset class;
- fallback rate;
- series-cluster bootstrap intervals using a fixed seed.

Because financial series share market shocks, bootstrap intervals are
sensitivity summaries rather than proof of cross-sectional independence.

## Frozen rule

No `K`, half-life, tracking radius, spacing radius, branch score, order set,
window set, or metric may be changed after CP05 results are observed.

The only primary dynamic rule is `recency_hl3`; CP05 is not another tuning
stage.

## Run sequence

~~~bash
git pull
pip install -e .
pytest

python experiments/smoothness_cv/run_checkpoint_05.py --preset smoke --jobs 8
python experiments/smoothness_cv/analyze_checkpoint_05.py

python experiments/smoothness_cv/run_checkpoint_05.py --preset panel --jobs 24
python experiments/smoothness_cv/analyze_checkpoint_05.py
python experiments/smoothness_cv/make_checkpoint_05_figures.py
~~~

Commit and push the complete `results/smoothness_cv/checkpoint_05/` directory.
