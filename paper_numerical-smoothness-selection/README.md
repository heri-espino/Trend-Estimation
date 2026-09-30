# Numerical Smoothness Selection

**Status: ACTIVE — sole current research focus.**

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

For fixed discrete choices \((d,L,m,h)\), where \(m\) is a pre-specified trend
continuation rule, define
\[
F_{d,L,m,h}(S)=CV_h(d,L,m,S).
\]

The numerical problem is to identify the relevant local minima of \(F\) and
select
\[
S^\star_{d,L,m,h}
\in
\arg\min_{S\in[0,1]}F_{d,L,m,h}(S)
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
- sensitivity to \(d\in\{1,2,3,4\}\), a small set of \(L\), forecast horizon
  \(h\), and a small number of simple continuation rules;
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

## Success criteria

The paper is ready to write to completion when:

1. exact endpoint semantics are implemented;
2. the adaptive search matches the dense-reference global optimum to frozen
   tolerances across the benchmark suite;
3. missed-local-minimum behavior is measured and honestly characterized;
4. evaluation-count and runtime savings are quantified;
5. sensitivity to the epsilon-spacing rule is understood;
6. comparisons with the existing log-\(\lambda\) search are complete;
7. the numerical protocol is frozen and reproducible;
8. the manuscript states only claims supported by those experiments.

## Read first

1. notes/research_objective.md
2. notes/scope.md
3. notes/roadmap.md
4. notes/decisions.md

Reusable implementation belongs in src/trend_estimation/.

Paper-specific experiments should live in
experiments/numerical_smoothness_selection/, and versioned lightweight
outputs in results/numerical_smoothness_selection/.

## Build

~~~bash
latexmk -pdf -interaction=nonstopmode \
  -outdir=paper_numerical-smoothness-selection/build \
  paper_numerical-smoothness-selection/main.tex
~~~
