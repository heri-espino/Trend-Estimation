# Model Definitions and Naming Audit

## Purpose

The repository contains closely related penalized smoothers. They must not be conflated in code, notes, or manuscripts.

## A. Pure penalized trend

\[
\widehat t_{\lambda,d}
=
\arg\min_t
\left\{
\|y-t\|_2^2+
\lambda\|D_dt\|_2^2
\right\}
=
(I+\lambda D_d^\top D_d)^{-1}y.
\]

This is the canonical model for the active derivative and numerical-optimization work.

**Library**

- `PurePenalizedSolver`
- `PurePenalizedTrend`
- `pure_trend_derivatives`

**Status:** definition, implementation, and derivative identities are internally consistent.

## B. Guerrero (2007) plug-in drift formulation

The uploaded Guerrero paper must be treated as the authority when we describe the published estimator. The relevant plug-in structure is

\[
\widehat\tau_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}
\left(
y+
\lambda\widehat m_yD_d^\top\mathbf1
\right),
\]

where the literature audit should verify exactly how \(\widehat m_y\) is estimated from the observed series.

Our current working reading is that the paper's plug-in estimator computes the drift from observed differences rather than repeatedly re-estimating it from the fitted trend. This must be checked against the paper text before being stated as a final manuscript claim.

## C. Current iterative library variant

The existing `GuerreroSpectralSolver` initializes a drift and repeatedly updates it from the fitted trend. Therefore its current numerical definition is not automatically identical to model B.

Until the audit is complete, call this implementation:

**Guerrero-style iterative drift variant**

rather than asserting that it is exactly the published Guerrero (2007) estimator.

**Library**

- `src/trend_estimation/core/solvers.py::GuerreroSpectralSolver`
- `src/trend_estimation/models/guerrero.py::GuerreroTrend`

## D. Possible jointly estimated drift model

If we intentionally study

\[
\min_{t,m}
\left\{
\|y-t\|_2^2+
\lambda\|D_dt-m\mathbf1\|_2^2
\right\},
\]

then minimizing over \(m\) gives

\[
m(t)=\frac{1}{N-d}\mathbf1^\top D_dt.
\]

Let

\[
P
=
I-
\frac{1}{N-d}\mathbf1\mathbf1^\top.
\]

Substitution yields the equivalent quadratic problem

\[
\min_t
\left\{
\|y-t\|_2^2+
\lambda\|P D_dt\|_2^2
\right\},
\]

with solution

\[
\widehat t
=
\left(
I+\lambda D_d^\top P D_d
\right)^{-1}y.
\]

This is mathematically attractive because it again has the pure quadratic form with a modified penalty matrix. However, it is a separate model and should receive its own name if we decide to implement it.

## Active-paper policy

The forecast-optimal-smoothing paper should begin with model A because its derivative and forecast objective can be stated exactly and tested cleanly.

Models B/C/D can become robustness comparisons only after their definitions and relationship to the literature are resolved.

## Library mapping rule

Any implementation change to these models must update this note and `notes/key_results.md`. Any manuscript statement calling a model "Guerrero" must cite the exact estimator definition being used.
