# Smoothness selected by chronological forecast validation

**Status: ACTIVE — methodological paper created by the 2026-10-05 split.**

Working title: **Forecast-Optimal Smoothness for Finite-Difference Penalized Trend Estimation**

## Objective

Define and study an endogenous smoothness level for finite-difference penalized trend estimation by choosing normalized smoothness \(S\) to minimize chronological future-block forecast error.

## Why this is a separate paper

The former project mixed two questions:

1. What should smoothness mean and how should it be selected for forecasting?
2. How should the resulting one-dimensional objective be optimized efficiently when multimodal?

This folder owns question 1. Numerical root discovery, Brent, adaptive subdivision, rational-polynomial structure, and Sturm/root isolation belong to paper_numerical-methods/.

## Direct methodological lineage

The closest foundation is Guerrero's controlled-smoothness penalized least-squares framework: finite-difference PLS, a trace-based smoothness index, analyst-specified smoothness percentages, and trend extrapolation.

The new step is
\[
S_{\text{chosen by analyst}}
\longrightarrow
S^\star_{\text{chosen by chronological forecast error}}.
\]

Hart (1994) is important related work because TSCV chooses a kernel bandwidth using predictive performance. It is not the same estimator or criterion.

## Core model

\[
\widehat\tau_\lambda=H_\lambda y,\qquad
H_\lambda=(I+\lambda D_d^\top D_d)^{-1}.
\]

\[
S(\lambda)=
1-\frac1{N-d}
\sum_{\delta_j>0}\frac1{1+\lambda\delta_j}\in[0,1].
\]

For origin \(T\),
\[
\widehat z_T(S)=G_{d,h}H_{\lambda(S)}x_T.
\]

Define
\[
F_{d,L,h}(S)=
\frac1{Mh}\sum_{j=1}^M
\left\|z_{T_j}-G_{d,h}H_{\lambda(S)}x_{T_j}\right\|^2,
\]
then
\[
S^\star_{d,L,h}\in\arg\min_{S\in[0,1]}F_{d,L,h}(S).
\]

This is the central object.

## What this paper should establish

- why normalized smoothness is a useful coordinate;
- why chronological future-block error is a different target from recovery-oriented or in-sample criteria;
- how selected smoothness depends on forecast horizon and continuation family;
- when the criterion is stable or multimodal;
- whether forecast-optimal and recovery-optimal smoothness differ under controlled mechanisms;
- relation to Guerrero, Hart/TSCV, classical smoothing-parameter criteria, and rolling-origin evaluation.

A dense grid is acceptable for the main scientific experiments. Numerical efficiency is not the contribution.

## Scope

The baseline paper fixes \(d,L,h\) for each continuous smoothness problem. Joint adaptation of \(d,L,S\) belongs to paper_forecast-optimal-smoothing/.

The baseline estimator uses the zero-drift, identity-weight finite-difference PLS family already implemented. General Guerrero \(\mu\neq0\) and non-identity covariance weighting are extensions.

## Read first

1. AI_HANDOFF.md
2. notes/research_objective.md
3. notes/model_and_notation.md
4. notes/literature_positioning.md
5. notes/claim_boundaries.md
6. notes/roadmap.md
7. notes/manuscript_outline.md
