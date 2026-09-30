# AI Handoff

## Highest-priority instruction

This repository contains **three research papers**, but only one is active.

\[
\boxed{\text{ACTIVE: paper\_numerical-smoothness-selection/}}
\]

Work exclusively on the numerical smoothness-selection paper until its roadmap
is complete. Do not start new experiments, broaden claims, or add model
comparisons for the other two papers unless the user explicitly changes this
priority.

The other papers are parked, not abandoned. Preserve their existing results and
history.

## Research-paper map

### 1. ACTIVE — Numerical Selection of Forecast-Optimal Smoothness

Directory: paper_numerical-smoothness-selection/

Read in this order:

1. notes/research_objective.md
2. notes/scope.md
3. notes/roadmap.md
4. notes/decisions.md

Primary estimator:
\[
\widehat\tau_\lambda
=
(I+\lambda D_d^\top D_d)^{-1}y.
\]

Normalized smoothness:
\[
S(\lambda)
=
1-
\frac1{N-d}
\sum_{j=1}^{N-d}
\frac1{1+\lambda\delta_j}.
\]

Primary numerical object, for a fixed discrete configuration
\((d,L,m,h)\):
\[
F(S)=CV_h(d,L,m,S),
\qquad
S^\star\in\arg\min_{S\in[0,1]}F(S).
\]

The method must allow multiple local minima. Current numerical design:

1. sparse deterministic partition of \(S\);
2. derivative/curvature evaluation;
3. adaptive interval subdivision;
4. derivative sign-change bracketing;
5. Brent refinement;
6. stationary-point classification;
7. exact/limiting boundary comparison;
8. post-discovery epsilon spacing of representative minima.

Current epsilon sensitivity:
\[
\varepsilon\in\{0,0.02,0.05,0.10,0.15\}.
\]

Keep at most five representative local minima after discovery. Epsilon spacing
is post-processing and must not affect root discovery.

Important unfinished items:

- exact \(S=1\leftrightarrow\lambda=\infty\) handling;
- flat/tangential-root robustness;
- frozen tolerances/stopping rules;
- benchmark against dense reference;
- comparison with existing log-\(\lambda\) stationary search;
- controlled stress tests across \(d\in\{1,2,3,4\}\), several \(L\), \(h\),
  and a small number of simple continuation rules.

The contribution is numerical. Do not turn this paper into an ARIMA/MLE/GCV
model-comparison paper or a recurrence paper.

### 2. PARKED — Adaptive Forecast-Optimal Trend Estimation

Directory: paper_forecast-optimal-smoothing/

Core object:
\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

This paper owns time-varying regime/state adaptation, mechanism studies, and
adaptive-versus-fixed forecast evaluation. Detailed historical notes remain
under root notes/.

Do not resume it until the numerical paper is finished.

### 3. PARKED — Financial Trend Forecasting and Recurrence

Directory: paper_smoothness-recurrence/

This paper owns the applied comparison of trend/forecast definitions and their
financial recurrence implications.

Candidate principles include:

- forecast-optimal penalized trend;
- GCV-selected penalized trend;
- likelihood/state-space trend;
- AR(\(p\))/ARIMA;
- penalized trend + AR residual;
- no-change/random walk.

At origin \(T\), every reference trend path must be frozen using only
\(\mathcal F_T\). Future data may score the forecast and determine recurrence,
but may not update the reference path retrospectively.

This paper does not own the numerical \(S\)-search. Do not resume it until the
numerical paper is finished.

## Tutorial companion

paper_penalized-trend-tutorial/ is a tutorial companion, not a fourth research
track.

## Repository role

Trend-Estimation is library-first.

Reusable estimators, derivatives, optimizers, forecasting logic, simulations,
metrics, and plotting belong in src/trend_estimation/.

Paper-specific runners belong under experiments/<paper namespace>/.
Lightweight reproducible outputs belong under results/<paper namespace>/.

Do not duplicate reusable implementation inside paper folders.

## Active numerical implementation

Relevant existing implementation includes:

- src/trend_estimation/core/smoothness.py
  - lambda_to_smoothness
  - smoothness_derivatives
  - smoothness_to_lambda
- src/trend_estimation/selection/smoothness_numerical.py
  - find_stationary_points_smoothness
  - select_spaced_smoothness_minima
  - sweep_spaced_smoothness_minima
  - DEFAULT_SPACING_EPSILONS
- src/trend_estimation/selection/numerical.py
  - existing log-\(\lambda\) stationary search
- tests/test_smoothness.py
- tests/test_smoothness_numerical.py

Current smoothness_to_lambda behavior clips \(S\ge1\) to an interior value.
That is not acceptable as the final scientific treatment of the endpoint; the
active roadmap requires exact limiting semantics.

## Validation invariant

At forecast origin \(T\), no observation after \(T\) may influence fitting,
hyperparameter selection, or the forecast path.

Chronological future observations are revealed only for scoring.

## Documentation policy

docs/ is for public Sphinx API documentation.

Each research paper owns its scientific objective, scope, roadmap, and decisions
inside its own folder.

Root notes/ contains historical/detailed material for the adaptive paper and
must not override the active numerical paper's local source of truth.

## CI policy

Automatic CI remains lightweight: install, tests, and Sphinx.

Paper compilation is manual-only through workflow_dispatch. Do not make heavy
paper/results workflows run on ordinary push or pull request.
