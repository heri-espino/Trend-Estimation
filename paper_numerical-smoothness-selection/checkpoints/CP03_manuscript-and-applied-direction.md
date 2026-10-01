# CP03 — Manuscript draft complete; applied interpretation is next

**Date:** 2026-09-30  
**Status:** current.

## 1. Current paper question

For fixed difference order (d), rolling-window length (L), and forecast
horizon (h):

> Can forecast-optimal smoothness in finite-difference penalized least squares
> be located accurately and economically when the rolling forecast-validation
> surface contains multiple local minima?

The numerical method is frozen. The paper is now moving from validation of the
search algorithm to **interpretation of the multiple-minimum phenomenon on
real series**.

## 2. Frozen numerical method

Primary search specification:

[
egin{aligned}
	ext{initial grid size} &= 9,\
	ext{endpoint refinement levels} &= 6,\
	ext{maximum adaptive depth} &= 8,\
	ext{minimum interval width} &= 10^{-3},\
	ext{derivative tolerance} &= 10^{-8},\
	ext{curvature tolerance} &= 10^{-8},\
	ext{near-zero derivative ratio} &= 0.2,\
	ext{Brent root tolerance} &= 10^{-10},\
	ext{interior boundary margin} &= 10^{-6}.
end{aligned}
]

Exact (S=0) and (S=1) are always evaluated.

Do not retune this specification from later applied examples.

## 3. Frozen primary evidence

- adversarial analytic objectives: **240/240** relevant known minima/boundary
  optima recovered;
- synthetic rolling forecast objectives: **2105/2105** dense-reference
  interior minima recovered over **1920** surfaces;
- financial geometry stress test: **473/473** dense-reference interior minima
  recovered over **384** surfaces;
- synthetic mean evaluation fraction: **1.57%** of the dense grid;
- financial mean evaluation fraction: **1.84%** of the dense grid;
- OFAT sensitivity completed;
- epsilon spacing classified as post-processing only.

These results establish the numerical-search claim. They do not establish
forecasting superiority or economic predictability.

## 4. Manuscript state

A complete SMCCA manuscript draft exists in `../main.tex`.

Current length: approximately 10 pages in the SMCCA template.

Current manuscript strengths:

- clear PLS formulation;
- normalized smoothness coordinate (Sin[0,1]);
- analytic derivative formulas;
- explicit adaptive-search algorithm;
- exact endpoint treatment;
- controlled adversarial, synthetic, and real-data numerical validation.

Current manuscript weakness:

> The reader sees that the optimizer works, but does not yet see clearly why
> multiple forecast-CV minima are substantively different smoothing choices.

The next addition should therefore be interpretive/applied rather than another
large benchmark.

## 5. New applied direction

Add a small set of **case studies** covering qualitatively different data:

1. quarterly macroeconomic series: real GDP (FRED `GDPC1`);
2. ETF: e.g. SPY or QQQ;
3. individual stock: e.g. AAPL or XOM;
4. cryptocurrency: e.g. BTC-USD or ETH-USD.

For each case, show:

- the rolling forecast-CV profile (F(S));
- all relevant local minima;
- the corresponding fitted trends on the same training data;
- the continuation/forecast implied by each minimum;
- an untouched final test block;
- test error for each candidate minimum;
- optionally a classical smoothing choice such as GCV as a reference, if
  implemented without changing the primary question.

The aim is **not** to identify a universally best asset-specific model. The aim
is to show that distinct minima correspond to distinct trend scales and future
paths.

## 6. Interpretation to develop

As (lambda) changes, the PLS smoother attenuates spectral/eigen components at
different rates through

[
alpha_j(lambda)=rac{1}{1+lambdadelta_j}.
]

The forecast operator then maps the resulting endpoint level, slope, and
higher-order finite-difference structure into the future.

Hence the rolling forecast loss need not change monotonically with smoothness:
different smoothing levels may suppress noise differently while preserving
different local slopes/curvatures. At a fixed forecast horizon, several such
trade-offs can become locally optimal.

This mechanism should become part of the paper's explanation of why multiple
minima occur.

## 7. What not to do

- Do not reopen the frozen numerical algorithm.
- Do not turn the paper into a model zoo.
- Do not select illustrative examples using final test error.
- Do not claim that a local minimum represents a true economic regime.
- Do not claim financial predictability.
- Do not mix this paper with recurrence/first-passage analysis.

## 8. Immediate next action

Implement a reproducible applied case-study experiment with a strictly untouched
test block and deterministic example-selection rules. Then regenerate a small
number of manuscript figures and revise the Introduction, Results, and
Discussion around the interpretation of multiple minima.
