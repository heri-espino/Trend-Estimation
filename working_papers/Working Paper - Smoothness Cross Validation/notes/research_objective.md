# Canonical research objective — forecast-optimal normalized smoothness

**Current independent research objective | 2026-10-08.** The latest manuscript is a working document; completed research notes will eventually drive the final rewrite.

## Motivation: choosing a trend for an unknown future

We are not merely asking how to make a realized series look smoother. We want to know **which smoothing of today's observed series is most suitable for extrapolating its trend into an unknown future**.

The apparent paradox—how can the future determine present smoothness if the future is unknown?—is resolved through chronological cross-validation. At current origin \(T\), the actual future \(y_{T+1:T+h}\) is unavailable. But the *futures of previous forecast origins* are now observed. We can retrospectively generate forecasts at those past origins without leaking their later data into their training windows, score against their subsequently realized observations, and select the smoothness that historically forecast best. Then we refit the final trend at \(T\).

The object of interest is **normalized smoothness \(S\in[0,1]\)**. The penalty \(\lambda\) is an equivalent algebraic/numerical coordinate; in the scientific decision we choose \(S\).

## Mathematical definition

For fixed difference order \(d\), estimation length \(L\), and horizon \(h\), define

\[
Q=D_d^\top D_d,\quad H_\lambda=(I+\lambda Q)^{-1},
\quad H(S)=H_{\lambda(S)}\ (S<1),\quad H(1)=P_{\ker D_d}.
\]

The trace-based normalized smoothness index is

\[
S(\lambda)=1-\frac1{L-d}\sum_{j=1}^{L-d}(1+\lambda\delta_j)^{-1},
\quad S(0)=0,\quad S(\infty)=1.
\]

At historical origin \(t_m\) whose subsequent \(h\) observations are already available by \(T\), predict through the fixed continuation operator \(G_{d,h}\):

\[
\widehat z_{t_m}(S)=G_{d,h}H(S)y_{t_m-L+1:t_m}.
\]

Select smoothness via **pooled chronological future-block MSE**:

\[
\widehat S^{\mathrm{FCV}}_{T,d,L,h}\in\arg\min_{S\in[0,1]}
\frac1{Mh}\sum_{m=1}^M
\left\|y_{t_m+1:t_m+h}
-G_{d,h}H(S)y_{t_m-L+1:t_m}\right\|_2^2,\quad t_m+h\le T.
\]

The selected value is then used to **refit** \(H(\widehat S_T)y_{T-L+1:T}\) and forecast \(y_{T+1:T+h}\). Do not average old historical fitted trends. Do not use the unknown future to tune the current smoothing parameter.

## What the method is / is not

- **Is:** a horizon-targeted choice of PLS smoothing, evaluated by forecasts of observations that were future at past origins.
- **Is:** a compact \(S\)-space optimization that searches between the unsmoothed and limiting polynomial trends.
- **Is:** a selected **future polynomial extrapolation** (degree at most \(d-1\) when \(d\) is fixed), whose coefficients change when \(S\) changes.
- **Is not:** post-hoc historical fit optimization, oracle access to today's unknown future, or selection of the polynomial degree itself.
- **Is not:** an invention of PLS, of Guerrero's controlled-smoothness index, or of predictive cross-validation.
- **Is not proven:** the first exact use of this specific criterion or a universally best forecasting approach.

## Mathematics we must understand and keep

1. PSD penalty \(Q=D_d^\top D_d\) and orthogonal eigenvalue decomposition.
2. Reusable spectral form of \(H_\lambda\), null space and exact endpoints.
3. Why \(S(\lambda)\) is strictly monotone and compact and how it relates to effective degrees of freedom.
4. Definition and interpretation of \(G_{d,h}\) and how smoothing changes the coefficients of future polynomial continuation.
5. Quadratic expansion of forecast MSE, analytic \(H',H'',H^{(n)}\), analytic \(F',F''\), and the \(S\)-chain rule.
6. Multimodality: all competing minima and endpoints must be considered; numerical completeness is not automatic.
7. Why the pooled minimum is not the average of the per-fold smoothness minimizers.

Full mathematics: [mathematical_foundations.md](mathematical_foundations.md).

## Current hypotheses, not settled results

- Direct \(h\)-step CV may select different \(S\) from ordinary CV/GCV, one-step CV, or latent-trend-recovery criteria.
- The forecast horizon may materially affect optimal smoothing and future MSE.
- Spectral reuse and analytic derivatives may improve reliable and efficient evaluation relative to repeated matrix inversions.
- The pooled surface can be multimodal, requiring robust detection and ranking of minima.

## Evidence and writing policy

CP01–CP03 were **actually run** and are preserved as the historical evidence of this working paper. Their existing results are informative historical observations, not automatically the future submission's final evidence. A changed numerical root-finding method may justify a same-objective comparison and a separately frozen new simulation, but cannot retroactively invalidate or overwrite the old results.

For now, **notes are authoritative; the current CSSC-oriented LaTeX manuscript is a dated working draft**. Once the numerical approach, comparative experiments, and prior-art audit settle, reconstruct the final paper from verified notes and reproducible results. Keep this paper independent of other manuscripts; do not define its contribution by the existence of another paper.
