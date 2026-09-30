# Financial Trend Forecasting and Recurrence

**Status: PARKED until the numerical-smoothness paper is finished.**

Working title:

**Forecasting Financial Trends and Measuring Recurrence under Competing Trend Models**

This is the applied/financial paper. It is intentionally separate from the
numerical-method paper.

## One-sentence objective

> Compare several established ways to estimate and forecast a financial trend,
> evaluate them on chronological validation and untouched test data, and study
> how the resulting definition of trend changes observed recurrence/first-passage
> behavior.

## Core empirical object

At origin \(T\), each method \(m\) produces an ex-ante trend path
\[
\widehat\tau^{(m)}_{T+k\mid T},\qquad k\ge0,
\]
using only information available through \(T\).

For log price \(x_t\), define
\[
g^{(m)}_{T,k}
=
x_{T+k}-\widehat\tau^{(m)}_{T+k\mid T}.
\]

A crossing time is
\[
H_T^{(m)}
=
\inf\{k\ge1:
g^{(m)}_{T,k}g^{(m)}_{T,0}\le0\}.
\]

The paper compares recurrence summaries across competing trend definitions.

## Candidate method families

The final list must remain small and interpretable. Current candidates are:

- forecast-optimal penalized trend;
- GCV-selected penalized trend;
- likelihood/state-space trend;
- AR(\(p\)) / ARIMA forecasting benchmarks;
- penalized trend plus AR residual forecast;
- no-change/random-walk baseline.

The paper may also include a small number of literature-motivated trend
forecasting models if they add a genuinely different modeling principle.

## Main outputs

- validation and untouched-test forecast errors;
- probability of recurrence by horizon;
- median/restricted-mean recurrence time;
- survival and hazard summaries when censoring matters;
- recurrence versus initial standardized distance from trend;
- robustness of recurrence conclusions to the trend definition.

## Delimitation

### In scope

- comparative financial forecasting;
- chronological train/validation/test separation;
- multiple known trend/forecasting methods;
- frozen-origin trend paths;
- first-passage/recurrence analysis;
- cross-asset comparisons across ETFs, equities, and crypto;
- dependence-aware uncertainty.

### Out of scope

- inventing the smoothness search algorithm;
- proving numerical root-discovery properties;
- large adaptive regime modeling of \((d,L,S)\);
- claiming that recurrence automatically implies stationary mean reversion;
- portfolio/trading profitability unless a separate explicit design is added.

The numerical optimizer used by forecast-optimal PLS belongs to
paper_numerical-smoothness-selection/.

## Read first when this paper is resumed

1. notes/research_objective.md
2. notes/scope.md
3. notes/roadmap.md
4. notes/decisions.md

Do not resume this roadmap until paper_numerical-smoothness-selection/ is
finished.
