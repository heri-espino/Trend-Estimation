# Applied case-study design

## Motivation

The numerical benchmark already establishes that the adaptive method can recover
the relevant minima of a multimodal rolling forecast-validation objective.

The applied section now asks:

> If several smoothness values are local minima of rolling forecast CV, what
> changes in the fitted trend and forecast path, and does their validation
> ranking persist on an untouched test block?

The protocol is strict:

- **development/validation discovers and ranks candidates;**
- **test evaluates those frozen candidates only.**

The test set is never used to discover minima, select the displayed
configuration, choose \(\varepsilon\), tune \(d,L,h\), or alter the numerical
algorithm.

## Frozen data families

The experiment uses four tracked snapshots:

1. FRED GDPC1 — U.S. real GDP, quarterly;
2. SPY — broad ETF;
3. AAPL — individual stock;
4. BTC-USD — cryptocurrency.

All positive levels are modeled on the natural-log scale.

## Development/test split

Reserve the final block before any configuration search:

- GDP: final 8 quarterly observations;
- daily market series: final 60 observations.

Everything before that block is development data.

For each series, search only over the pre-specified \((d,L,h)\) grid in the
experiment script. The final test block remains untouched until the candidate
set is frozen.

## Development-only example selection

For each pre-specified configuration:

1. compute the rolling forecast-CV objective on development data;
2. recover local minima with the frozen adaptive algorithm;
3. apply the already frozen \(\varepsilon=0.10\) spacing rule;
4. retain at most three representative candidates, ranked by validation error.

Among configurations with at least two representatives, choose the one with
the largest smoothness separation between its two lowest-CV candidates. Break
ties lexicographically by \((d,L,h)\).

This selects a visually informative multimodal example without using test
performance.

## Validation/test ranking

Let the frozen candidate set be

\[
\mathcal C=\{S_1,\ldots,S_K\}.
\]

For every candidate record

\[
CV_k=F_{d,L,h}(S_k).
\]

The validation-selected candidate is

\[
k_{\mathrm{CV}}=\arg\min_k CV_k.
\]

Only after the candidate set is frozen, refit every candidate at the final
development origin and score the first \(h\) observations of the untouched
test block:

\[
E_k^{\mathrm{test}}
=
\frac{1}{h}\sum_{j=1}^{h}
\left(y_{T+j}-\widehat y^{(k)}_{T+j|T}\right)^2.
\]

For diagnosis only,

\[
k_{\mathrm{test}}=\arg\min_k E_k^{\mathrm{test}}.
\]

A **validation--test rank reversal** occurs when

\[
k_{\mathrm{CV}}\neq k_{\mathrm{test}}.
\]

A reversal does not justify selecting on the test set. It shows that distinct
local minima of the same validation criterion can be ordered differently by a
later unseen block.

Also report

\[
\Delta CV_k=CV_k-\min_j CV_j
\]

and

\[
\Delta E_k^{\mathrm{test}}
=
E_k^{\mathrm{test}}-\min_j E_j^{\mathrm{test}}.
\]

## Why several minima can arise

With eigendecomposition

\[
Q=U\operatorname{diag}(\delta_j)U^\top,
\]

the smoother attenuates penalized components by

\[
\alpha_j(\lambda)=\frac{1}{1+\lambda\delta_j}.
\]

Different components disappear at different rates as \(\lambda\) increases.
The fitted endpoint level, slope, and higher-order finite differences change,
and the continuation operator maps those features into future values.

A rougher local optimum may preserve recent movement and extrapolate a stronger
local slope or curvature. A smoother local optimum may suppress that movement
and extrapolate a more stable low-frequency path. Across forecast origins,
their errors can cross, so the average forecast-validation objective need not
be convex or unimodal.

The candidate set is therefore a **selection-sensitivity diagnostic**, not a
confidence interval or a probability distribution over smoothness.

## Figure design

Use one compact figure with four rows, one per data family.

For each row:

1. left: \(F(S)\) with representative minima marked;
2. center: the same training observations with the trend estimates for
   CV-1, CV-2, and CV-3;
3. right: candidate forecasts with the untouched test observations.

Candidate labels preserve validation rank. If the test ranking differs, label
the paths as CV-2 / test-1; do not relabel the validation winner.

## Interpretation boundary

The applied examples interpret the numerical geometry and stability of
smoothness selection. They do not establish economic regimes, universal
forecasting superiority, financial predictability, or trading value.
