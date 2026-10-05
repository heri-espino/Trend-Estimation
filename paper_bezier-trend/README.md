# Forecast-oriented Bézier/Bernstein trend estimation

**Status: IDEA / NOVELTY AUDIT PENDING. Do not treat as an established contribution yet.**

Working title:

> **Forecast-Oriented Penalized Bézier Trend Estimation: Control-Point Regularization and Endpoint Geometry**

## Question

Can trend estimation for forecasting benefit from moving the smoothness penalty from sampled trend values to a Bernstein/Bézier control representation, especially at the forecast endpoint?

The paper is not about merely fitting a Bézier curve to a time series. That is not new.

The candidate contribution is the combination of:

1. a Bernstein/Bézier representation of a scalar trend;
2. explicit regularization of control coefficients/control-polygon geometry;
3. chronological forecast-based tuning;
4. explicit endpoint geometry for continuation;
5. controlled comparison with finite-difference PLS, P-splines, smoothing splines, and trend filtering.

## Baseline finite-difference estimator

For observations \(y\in\mathbb R^N\),

\[
\widehat\tau_\lambda
=
\arg\min_\tau
\left\{
\|y-\tau\|_2^2
+
\lambda\|D_d\tau\|_2^2
\right\},
\]

with

\[
\widehat\tau_\lambda
=
(I+\lambda D_d^\top D_d)^{-1}y.
\]

## Bernstein/Bézier coefficient-space analogue

Normalize time to \(u_t\in[0,1]\). For a Bernstein design matrix \(B_K\),

\[
\tau=B_K\beta.
\]

A quadratic control-coefficient penalty gives

\[
\widehat\beta_{\lambda,K,q}
=
\arg\min_\beta
\left\{
\|y-B_K\beta\|_2^2
+
\lambda\|D_q\beta\|_2^2
\right\}.
\]

Hence

\[
\widehat\beta_{\lambda,K,q}
=
(B_K^\top B_K+\lambda D_q^\top D_q)^{-1}B_K^\top y,
\]

and

\[
\widehat\tau_{\lambda,K,q}
=
H^{(B)}_{\lambda,K,q}y,
\]

where

\[
H^{(B)}_{\lambda,K,q}
=
B_K
(B_K^\top B_K+\lambda D_q^\top D_q)^{-1}
B_K^\top.
\]

The scientific question is **where regularization should act**, not whether quadratic regularization exists.

Important: this construction is close to penalized spline/P-spline methodology. It must not be advertised as novel without a literature-specific equivalence audit.

## Endpoint geometry

For a cubic scalar Bernstein/Bézier segment

\[
C(u)=
(1-u)^3\beta_0
+3(1-u)^2u\beta_1
+3(1-u)u^2\beta_2
+u^3\beta_3,
\]

the right endpoint satisfies

\[
C(1)=\beta_3,
\]

\[
C'(1)=3(\beta_3-\beta_2),
\]

and

\[
C''(1)=6(\beta_3-2\beta_2+\beta_1).
\]

Thus the final coefficients encode terminal level, slope, and curvature directly.

Candidate continuation rules:

- endpoint Taylor continuation from \(C(1),C'(1),C''(1)\);
- append a new Bézier segment with \(C^1\) continuity;
- append a new segment with \(C^2\) continuity;
- shrink endpoint slope/curvature toward zero;
- choose the continuation rule chronologically by forecast error.

Do not use naive out-of-domain Bézier extrapolation as the default without stress testing: the convex-hull interpretation applies only on the parameter interval.

## Central comparison

\[
\underbrace{\|D_d\tau\|_2^2}_{\text{sample-space roughness}}
\qquad\text{vs.}\qquad
\underbrace{\|D_q\beta\|_2^2}_{\text{control-space roughness}}.
\]

The paper should identify regimes in which these regularization geometries differ materially for endpoint trend forecasts, rather than claim universal dominance.

## Relationship to the other papers

- paper_smoothness-cv/ owns chronological forecast-based smoothness selection in the finite-difference PLS family.
- paper_numerical-methods/ owns efficient solution of multimodal smoothness objectives.
- paper_forecast-optimal-smoothing/ owns broader adaptive selection inside the finite-difference family.
- This workspace owns only the alternative Bernstein/Bézier representation, control-space regularization, endpoint geometry, and comparative evidence.

If the final result reduces mathematically to an already-known P-spline under a change of basis and offers no distinct forecasting result, this paper should be abandoned or reframed as a comparative/equivalence note.

## Read next

1. notes/research_objective.md
2. notes/literature_positioning.md
3. notes/literature_needed.md
4. notes/scope.md
5. notes/roadmap.md
6. notes/decisions.md
