# AI Handoff — Bézier/Bernstein trend paper idea

## Status

IDEA / NOVELTY AUDIT PENDING.

Do not run large experiments or draft a submission manuscript before the direct literature audit is complete.

## Candidate identity

Working title:

**Forecast-Oriented Penalized Bézier Trend Estimation: Control-Point Regularization and Endpoint Geometry**

The weak idea is:

> fit a Bézier curve to a time series.

That is already covered by prior statistical smoothing and forecasting work.

The stronger candidate is:

> compare finite-difference regularization of sampled trend values with regularization of Bernstein/Bézier control coefficients, tune both by chronological forecast performance, and study whether explicit endpoint geometry changes forecast behavior.

## Core equations

Finite-difference PLS:

\[
\widehat\tau=(I+\lambda D_d^\top D_d)^{-1}y.
\]

Bernstein coefficient-space smoother:

\[
\widehat\beta
=
(B^\top B+\lambda D_q^\top D_q)^{-1}B^\top y,
\]

\[
\widehat\tau
=
B(B^\top B+\lambda D_q^\top D_q)^{-1}B^\top y.
\]

Cubic endpoint:

\[
C'(1)=3(\beta_3-\beta_2),\qquad
C''(1)=6(\beta_3-2\beta_2+\beta_1).
\]

## Claim discipline

Known prior work already includes:

- statistical smoothing through Bézier curves;
- Bernstein-polynomial nonparametric regression;
- P-splines with difference penalties on basis coefficients;
- Bernstein-polynomial time-series forecasting;
- penalized Bézier smoothing;
- P-spline trend forecasting;
- piecewise cubic Bézier filtering in financial forecasting.

Therefore none of those phrases alone constitutes novelty.

The novelty audit must specifically test:

1. whether the proposed quadratic control-difference estimator is simply an existing penalized Bernstein/P-spline under another basis;
2. whether endpoint-aware Bézier continuation has already been studied for time-series trend forecasting;
3. whether chronological forecast-based joint selection of representation complexity and control-point smoothness already exists;
4. whether any theorem can distinguish sample-space and control-space regularization beyond basis reparameterization.

## Execution priority

Park this idea until the audit in notes/literature_needed.md is resolved. Small algebraic equivalence experiments are allowed; paper-scale Monte Carlo is not yet justified.
