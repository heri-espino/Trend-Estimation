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
