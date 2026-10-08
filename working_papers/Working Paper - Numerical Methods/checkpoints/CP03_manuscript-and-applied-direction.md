# CP03 — Manuscript draft complete; applied interpretation is next

**Date:** 2026-09-30  
**Status:** current.

## Current paper question

For fixed difference order \(d\), rolling-window length \(L\), and forecast
horizon \(h\):

> Can forecast-optimal smoothness in finite-difference penalized least squares
> be located accurately and economically when the rolling forecast-validation
> surface contains multiple local minima?

The numerical search is frozen. The active task is now to interpret what those
different local minima mean on real series and whether their validation ranking
persists on unseen data.

## Frozen numerical evidence

- 240/240 relevant known adversarial minima/boundary optima recovered;
- 2105/2105 synthetic dense-reference interior minima recovered across 1920
  surfaces;
- 473/473 financial dense-reference interior minima recovered across 384
  surfaces;
- mean evaluation fractions of 1.57% (synthetic) and 1.84% (financial);
- OFAT sensitivity completed;
- epsilon spacing fixed as post-processing only.

Do not retune the numerical search from later applied examples.

## Applied protocol now frozen

Series:

1. GDPC1 — GDP;
2. SPY — ETF;
3. AAPL — stock;
4. BTC-USD — crypto.

The final test block is reserved before any configuration search:

- GDP: 8 quarters;
- daily series: 60 observations.

Configuration and candidate selection use development data only. The final test
block is used only after the candidate set is frozen.

Representative candidate minima use the already frozen spacing
\(\varepsilon=0.10\), with at most three candidates.

The displayed configuration is chosen by development data only: among
configurations with at least two representative minima, maximize the
smoothness separation between the two lowest-CV candidates and break ties
lexicographically by \((d,L,h)\).

## Validation--test rank reversals

For the frozen candidate set

\[
\mathcal C=\{S_1,\ldots,S_K\},
\]

let

\[
k_{\mathrm{CV}}=\arg\min_k CV_k.
\]

After freezing the candidates, evaluate them on the untouched block and define
for diagnosis only

\[
k_{\mathrm{test}}=\arg\min_k E_k^{\mathrm{test}}.
\]

If

\[
k_{\mathrm{CV}}\neq k_{\mathrm{test}},
\]

report a validation--test rank reversal.

This is not test-set model selection. It is evidence that distinct local minima
of the same validation criterion can encode different smoothing/forecast
choices whose relative ordering is sample-dependent.

## Why this matters

The previous manuscript showed that the numerical search recovered minima
accurately. The applied section should now show that those minima can correspond
to visibly different trend scales and forecast paths.

A rank reversal is especially informative: it demonstrates that the minimum
with the smallest rolling-CV error need not be the candidate with the smallest
error on the later untouched block. The test result remains diagnostic and
must never be fed back into selection.

## Immediate next action

Run the paper preset of
experiments/numerical_smoothness_selection/run_applied_case_studies.py,
commit the result directory, inspect the four selected configurations and rank
reversals, then revise the manuscript around the applied interpretation.
