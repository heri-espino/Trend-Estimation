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

The Guerrero (2007) source has now been checked directly. The paper first gives the known-drift estimator

\[
\widehat\tau_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}
\left(
y+
\lambda\widehat m_yD_d^\top\mathbf1
\right),
\]

and then, in equation (17), estimates the unknown drift from the observed differences:

\[
\boxed{
\widehat m_y
=
\frac{1}{N-d}\mathbf1^\top D_d y.
}
\]

Substitution gives equation (18):

\[
\boxed{
\widehat\tau_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}
\left(
y+
\lambda\widehat m_yD_d^\top\mathbf1
\right).
}
\]

With the observed sample fixed, \(\widehat m_y\) does not depend on \(\lambda\).

## C. Historical iterative library variant

The repository previously initialized a drift and repeatedly updated it from the fitted trend. That procedure is not Guerrero (2007) equation (18).

It is retained only for reproducibility under the explicit name:

**IteratedDriftTrend**

or equivalently `drift_mode="iterated"`.

**Library**

- `src/trend_estimation/core/solvers.py::GuerreroSpectralSolver`
- `src/trend_estimation/models/guerrero.py::IteratedDriftTrend`

The canonical `GuerreroTrend` now uses `drift_mode="data"` and implements model B.

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

Model B is now a literature-aligned extension available for robustness comparisons. Model C is historical/reproducibility only. Model D remains a separate possible methodological extension.

## Library mapping rule

Any implementation change to these models must update this note and `notes/key_results.md`. Any manuscript statement calling a model "Guerrero" must cite the exact estimator definition being used.
