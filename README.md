# Trend Estimation

trend_estimation is a library-first research repository for finite-difference penalized trend estimation, forecasting, chronological validation, and smoothness selection.

## Research map

As of 2026-10-05, the former mixed numerical-smoothness project is split into two linked papers because it contains two different scientific questions.

### Paper A — Smoothness selected by chronological forecast validation

Directory: paper_smoothness-cv/

Working idea: **Forecast-Optimal Smoothness for Finite-Difference Penalized Trend Estimation**

Primary target: **Journal of Forecasting**. The active Wiley manuscript is in `paper_smoothness-cv/manuscript/` and builds through `python paper_smoothness-cv/build.py`.

It asks:

> Given a fixed finite-difference trend family and forecast horizon, what level of smoothness should be selected when the criterion is future chronological forecast error rather than an exogenously chosen percentage or an in-sample/recovery criterion?

Core estimator:
\[
\widehat\tau_\lambda=(I+\lambda D_d^\top D_d)^{-1}y.
\]

Normalized smoothness:
\[
S(\lambda)=1-\frac{1}{N-d}\sum_{\delta_j>0}\frac{1}{1+\lambda\delta_j}.
\]

For rolling origins \(T\in\mathcal O\),
\[
F_{d,L,h}(S)=
\frac{1}{|\mathcal O|h}
\sum_{T\in\mathcal O}
\left\|z_T-G_{d,h}H_{\lambda(S)}x_T\right\|^2,
\]
and
\[
S^\star_{d,L,h}\in\arg\min_{S\in[0,1]}F_{d,L,h}(S).
\]

This paper owns the definition, interpretation, statistical motivation, and empirical behavior of forecast-optimal smoothness. It may use a dense grid because numerical efficiency is not its contribution.

The direct methodological foundation is Guerrero's penalized least-squares/controlled-smoothness framework. Hart (1994) is important related work showing predictive smoothing-parameter selection in a different kernel/TSCV setting, but it is not the same estimator, smoothness coordinate, continuation rule, or future-block criterion.

### Paper B — Numerical methods for the smoothness objective

Directory: paper_numerical-methods/

Working title: **Numerical Solution of Multimodal Forecast-Smoothness Selection Problems**

It asks:

> Once \(F(S)\) is defined, how can all relevant minima and the global optimum be located reliably and with far fewer evaluations than an exhaustive dense grid?

Current numerical method:

1. sparse deterministic evaluation in \(S\);
2. analytic \(F'\) and \(F''\);
3. adaptive subdivision of suspicious intervals;
4. bracketing roots of \(F'(S)\);
5. Brent refinement;
6. stationary-point classification;
7. comparison with exact endpoints \(S=0\) and \(S=1\).

Brent is a root refiner, not a global discovery method. The current production algorithm still uses adaptive evaluations to discover brackets.

A stronger certified direction is under study. For fixed \((d,L,h)\), the forecast loss has rational structure in \(\lambda\), so stationary points can be related to roots of a polynomial numerator. The existing Sturm experiment is a proof-of-concept only.

Frozen numerical evidence from the pre-split work remains part of Paper B: 240/240 adversarial relevant optima, 2105/2105 synthetic dense-reference interior minima over 1920 surfaces, and 473/473 financial geometry-stress interior minima over 384 surfaces.

## Other workspaces

- paper_forecast-optimal-smoothing/ — PARKED; broader adaptive joint selection of \((d,L,S)\).
- paper_smoothness-recurrence/ — PARKED; applied financial trend/recurrence comparison.
- paper_statistical-properties-penalized-trend/ — DRAFTING; statistical consequences of forecast-selected smoothness, with novelty/theorem claims not yet frozen.
- paper_penalized-trend-tutorial/ — tutorial companion.
- paper_bezier-trend/ — IDEA / NOVELTY AUDIT PENDING; Bernstein/Bézier control-space regularization and endpoint-aware trend forecasting, with P-splines as a mandatory rival.

The old paper_numerical-smoothness-selection/ directory is retained only as a pre-split historical snapshot. Do not edit it for new work.

## Canonical reading order for another AI agent

1. AI_HANDOFF.md
2. RESEARCH_MAP.md
3. paper_smoothness-cv/README.md
4. paper_smoothness-cv/AI_HANDOFF.md
5. paper_numerical-methods/README.md
6. paper_numerical-methods/AI_HANDOFF.md
7. paper_bezier-trend/README.md
8. paper_bezier-trend/notes/literature_positioning.md

Paper-specific notes override older root notes when scopes conflict.

## Stable implementation namespaces

Reusable methods remain under src/trend_estimation/.

For reproducibility, the existing experiment/result namespaces are intentionally not renamed yet:

- experiments/numerical_smoothness_selection/
- results/numerical_smoothness_selection/

Those names are historical implementation namespaces, not the current paper title.

## Install

~~~bash
conda env create -f environment.yml
conda activate trend-estimation
pip install -e .
pytest
~~~

## CI policy

Automatic CI stays lightweight. Paper/PDF compilation remains manual-only through workflow_dispatch.
