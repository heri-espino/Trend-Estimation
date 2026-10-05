# Numerical Smoothness Selection

**Status: ACTIVE — manuscript drafting and review.**

Working title:

**Numerical Selection of Forecast-Optimal Smoothness in Penalized Trend Estimation**

This is the paper currently being developed. Until this paper is finished, the
other two research papers in this repository are parked: do not add experiments,
expand scope, or revise their claims unless a change is required to support this
paper.

## One-sentence objective

> Develop and validate an efficient numerical method for locating the relevant
> local minima of a forecast-validation objective over normalized smoothness
> \(S\in[0,1]\) in finite-difference penalized trend estimation.

## Core mathematical object

For
\[
\widehat\tau_\lambda=(I+\lambda D_d^\top D_d)^{-1}y,
\]
use the normalized smoothness coordinate
\[
S=S_d(\lambda;N)\in[0,1].
\]

For fixed discrete choices \((d,L,h)\), with the native finite-difference
continuation rule fixed, define
\[
F_{d,L,h}(S)=CV_h(d,L,S).
\]

The numerical problem is to identify the relevant local minima of \(F\) and
select
\[
S^\star_{d,L,h}
\in
\arg\min_{S\in[0,1]}F_{d,L,h}(S)
\]
without relying on an exhaustive dense grid.

## Main contribution

The contribution is numerical, not financial:

1. compactify the penalty domain with normalized smoothness \(S\in[0,1]\);
2. exploit analytic derivatives inherited from the \(\lambda\)-parameterization;
3. adaptively isolate stationary structure;
4. refine derivative roots with a bracketed solver;
5. classify stationary points and retain multiple local minima;
6. compare against exact/limiting boundaries;
7. validate against a very dense reference grid;
8. quantify optimum agreement, missed minima, objective regret, evaluation
   count, and runtime.

The paper must be useful even if the financial application is removed.

## Delimitation

### In scope

- penalized least-squares trend estimation;
- normalized smoothness \(S\);
- forecast-validation objectives;
- multiple local minima;
- exact treatment of \(S=0\) and limiting \(S=1\);
- adaptive stationary-point search;
- Brent/root-refinement diagnostics;
- spacing/suppression of nearby candidate minima;
- sensitivity to \(d\in\{1,2,3,4\}\), rolling-window length \(L\), and forecast horizon \(h\);
- synthetic and selected real-series surfaces used to stress the numerical
  method.

### Out of scope

- regime-adaptive joint \((d,L,S)\) modeling;
- a large financial forecasting model comparison;
- ARIMA/model-zoo benchmarking;
- MLE/state-space versus forecast-optimal trend as a substantive empirical
  question;
- financial recurrence, first-passage, survival, or trading claims;
- portfolio construction.

Those topics belong to the other two research papers.

## Current experimental status

The primary numerical protocol is frozen and the principal experiments are
complete:

- 240/240 relevant adversarial minima/boundary optima recovered;
- 2105/2105 synthetic dense-reference interior minima recovered across 1920
  forecast-validation surfaces;
- 473/473 financial dense-reference interior minima recovered across 384
  real-data geometry stress surfaces;
- one-factor sensitivity and epsilon post-processing sensitivity completed.

The remaining work is manuscript refinement, literature/claim audit, SMCCA
compilation, and referee-style review.

## Read first

1. notes/research_objective.md
2. notes/scope.md
3. notes/roadmap.md
4. notes/decisions.md
5. notes/submission_positioning.md

Reusable implementation belongs in src/trend_estimation/.

Paper-specific experiments should live in
experiments/numerical_smoothness_selection/, and versioned lightweight
outputs in results/numerical_smoothness_selection/.

## Build

The manuscript uses the SMCCA class copied into this directory. Compile from
the paper directory so that the class, figures, tables, and bibliography resolve
relative paths correctly:

~~~bash
cd paper_numerical-smoothness-selection
latexmk -pdf -interaction=nonstopmode -outdir=build main.tex
~~~

The repository's heavy paper-build workflow remains manual
(`workflow_dispatch`) with target `numerical`.


## Project navigation

For current research state and next actions:

1. `checkpoints/AI_HANDOFF.md`
2. `checkpoints/CP03_manuscript-and-applied-direction.md`
3. `todo/NEXT.md`

Supporting material:

- `notes/applied_case_studies.md` — design for GDP/ETF/stock/crypto examples;
- `notes/submission_positioning.md` — SMCCA fit and claim boundaries;
- `notes/results.md` — frozen numerical evidence;
- `notes/decisions.md` — frozen methodological decisions;
- `literature/dictionary/` — terminology and wording rules.

The numerical algorithm and confirmatory benchmark are frozen. The active
development task is the applied interpretation of multiple forecast-CV minima.
