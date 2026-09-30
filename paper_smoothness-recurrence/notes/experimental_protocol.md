> **Historical pre-split note (2026-09-29).** This file predates the separation into three research papers. It is preserved for provenance but is **not** the current source of truth. For the applied paper use README.md, notes/research_objective.md, notes/scope.md, notes/roadmap.md, and notes/decisions.md. Numerical smoothness-search material belongs to ../paper_numerical-smoothness-selection/.

# Experimental Protocol

Status: draft; values must be frozen in `decisions.md` before final runs.

## 1. Information-set rule

At forecast origin (T),

\[
\mathcal F_T=\sigma(y_1,\ldots,y_T).
\]

Every fitted trend, selected smoothness, scale estimate, and forecast path used
at (T) must be measurable with respect to (mathcal F_T). Future
observations may only score a forecast or determine recurrence/censoring.

## 2. Suggested primary scale

Leading candidate:

\[
x_t=\log P_t.
\]

This makes additive deviations more comparable across assets with different
nominal prices. Price level remains a robustness option.

## 3. Smoothness selection

For fixed pre-specified (d,L) and horizon (h),

\[
S_h^\star=\arg\min_{S\in[0,1]}CV_h(S).
\]

Preferred clean design:

- development period: choose (S_h^\star) for each series/horizon;
- evaluation period: freeze (S_h^\star);
- at each evaluation origin, refit using the frozen smoothness and only allowed
  history.

This estimates a series/horizon-specific optimum without turning the paper into
the adaptive-regime project.

## 4. Forecast trend

At evaluation origin (T),

\[
\widehat\tau_{T+k\mid T},
\qquad k=0,1,\ldots,H_{max}.
\]

This path is frozen at (T). Do not replace it with a trend re-estimated at
(T+k) when computing recurrence.

## 5. Initial deviation

\[
g_{T,0}=x_T-\widehat\tau_{T\mid T}.
\]

For cross-asset comparison,

\[
z_T=\frac{g_{T,0}}{\widehat\sigma_T},
\]

where (widehat\sigma_T) uses only pre-(T) information. Candidate scales
include residual SD, MAD-based scale, or realized volatility; freeze one before
final evaluation.

## 6. Recurrence outcomes

Crossing:

\[
R_T^{cross}=\inf\{k\ge1:g_{T,k}g_{T,0}\le0\}.
\]

Band recurrence:

\[
R_T^\varepsilon
=
\inf\{k\ge1:|g_{T,k}|\le\varepsilon_T\}.
\]

Use a relative/standardized band rather than one fixed dollar threshold across
assets. If recurrence does not occur before (H_{max}), record right
censoring.

## 7. Dependence between origins

Daily rolling origins create overlapping future paths. Before inferential
claims, use spaced origins, block/bootstrap uncertainty, clustered inference,
or another dependence-aware method. Do not report iid standard errors for
heavily overlapping events.

## 8. Numerical benchmark

For each CV surface compare the adaptive search against a dense smoothness
reference:

- selected (S^\star);
- minimum CV loss;
- local minima detected;
- evaluation count;
- runtime.

GPU acceleration is allowed for the dense reference.

## 9. Financial panel policy

Use a progression:

1. broad ETFs/indices;
2. separately held-out equities;
3. crypto stress test.

Reuse tracked snapshots when they satisfy the protocol. Universe changes after
outcome inspection are exploratory.


## 10. Forecasting the estimated trend

Smoothness estimation and trend extrapolation are separate design choices.
For a fitted trend \(\widehat\tau_{1:T}\), denote the forecast rule by
\(m\). The validation object becomes

\[
CV_h(d,L,m,S).
\]

The first comparison should remain small and interpretable:

1. **native finite-difference continuation**: continue the fitted trend by
   imposing the order-\(d\) difference rule already used by the library;
2. **local linear tail extrapolation**: fit a line to a pre-specified number of
   final fitted-trend points and extrapolate it;
3. **local quadratic tail extrapolation**: same idea with degree two;
4. **no-change forecast**: simple external baseline.

For each discrete \((d,L,m,h)\) configuration, search the smoothness domain for
multiple local minima and retain up to five epsilon-separated candidates.

The forecast method is selected using development/validation data only. The
final test block remains untouched until the full protocol is frozen.

## 11. Likelihood-based benchmark

A likelihood comparison is required because difference-penalty smoothing has a
probabilistic Gaussian/state-space interpretation.

Use a Gaussian state-space trend model corresponding as closely as possible to
the same difference order. Estimate its variance/smoothing parameters by
maximum or restricted/marginal likelihood, obtain latent-trend estimates with
the Kalman smoother, and generate h-step state-space forecasts.

The comparison must distinguish two questions:

- **forecast-selected PLS**: choose smoothness by chronological forecast error;
- **likelihood-selected trend**: choose variance/smoothing parameters by
  likelihood.

Both are evaluated on the same validation origins and then on the same untouched
test period.

Do not call the comparator merely "MLE of the trend": maximum likelihood
estimates the probabilistic model/variance parameters; the latent trend itself
is obtained from the fitted state-space model (filter/smoother).
