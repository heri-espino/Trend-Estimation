> **RESEARCH STATUS UPDATE — 2026-10-08 (current; original checkpoint record preserved below).** The primary current statistical question is selection of normalized PLS smoothness (S\in[0,1]) by **chronological, horizon-matched future-block forecast MSE**, with an explicit polynomial continuation and mandatory final refit. The eigenstructure of the smoother, analytic derivatives, and reliable recovery of competing minima are central mathematical/numerical topics. The source of truth is [../notes/INDEX.md](../notes/INDEX.md), [../notes/mathematical_foundations.md](../notes/mathematical_foundations.md), and [../notes/research_log_2026-10.md](../notes/research_log_2026-10.md).
>
> **Archival status:** CP05 **has been completed** and is now an **optional/exploratory historical study** of tracked minimum branches, continuation-order stability, or maps (\phi(V_j)). The main pooled forecast-CV method does not require these branches. Preserve the mixed/negative comparisons with pooled CV and the original post-hoc/confirmation boundaries. Any “central method” or “next checkpoint” text below is historical, not the current program.

---

# Checkpoint 05 — Frozen external financial panel

**Status: COMPLETE — external panel run committed and analyzed.**

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


## Observed CP05 result

The frozen 64-series panel run is
`results/smoothness_cv/checkpoint_05/20261007T062356Z_panel_a400609`.

Primary external-panel result:

\[
\boxed{
\operatorname{gRMSFE}
(\text{recency-hl3}/\text{pooled CV})
=
1.6421
}
\]

with a descriptive series-cluster bootstrap interval
\([1.1678,\,2.7033]\).

Thus the CP04 confirmation advantage over pooled CV **did not generalize** to
the broad external financial panel.

The dynamic rule beat pooled CV in 46.5% of outer blocks and in 39.1% of
series on a series-aggregate basis.

Against the newest tracked minimum,

\[
\boxed{
\operatorname{gRMSFE}
(\text{recency-hl3}/\text{last})
=
0.5246
}
\]

with descriptive interval \([0.2001,\,0.9052]\). The recency average
therefore strongly stabilizes the newest-minimum rule on this panel even
though it does not outperform pooled CV.

By asset class, dynamic / pooled geometric ratios were:

- crypto: 1.098;
- ETF: 1.152;
- stock: 2.186.

No branch-continuation fallback was triggered.

## Post-hoc mechanism signal

The aggregate failure against pooled CV is concentrated in higher-order
continuations. Conditioning on the order selected by the frozen all-order
procedure gives approximately:

- `d=1`: 1.008 dynamic / pooled;
- `d=2`: 1.018;
- `d=3`: 1.249;
- `d=4`: 7.960.

The largest failures include `d=4` forecasts for Citigroup, IBM, Amazon, XLI,
MCD, MRK, SCHB, and SMH. In these cases the tracked smoothness can be only
moderately below one but the 60-step cubic continuation becomes extremely
large. Pooled CV often selects a value closer to one and remains much more
stable.

Removing the single worst dynamic/pooled outer block reduces the aggregate
geometric ratio from 1.642 to about 1.342; removing the worst five reduces it
to about 1.155. These are post-hoc diagnostics, not revised CP05 estimates.

The strong dynamic/last result is also partly explained by the same mechanism:
recency averaging frequently shrinks an even more extreme newest-minimum
forecast, so both tracked rules can be unstable while the average is less
unstable.

## Consequence

Do not retune CP05.

The next checkpoint is `CP06_ORDER_STABILITY.md`. It uses earlier historical
outer blocks, not the CP05 external-test blocks, to study whether the
instability frontier is specifically caused by allowing high-order polynomial
continuation.
