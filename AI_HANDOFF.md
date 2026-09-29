# AI Handoff

## Read this first — scientific source of truth

Before interpreting the latest experiment or changing the paper story, read
`notes/research_objective.md`.

Canonical objective:

> **Forecast-optimal trend estimation as an adaptive forecasting method, where
> smoothness, memory length and difference order depend on horizon and local
> regime.**

The central object is the full forecasting-method configuration

[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
]

Do **not** redefine the project around the latest mechanism result.
In particular, the persistence/AR(1) study is one diagnostic explaining part
of the behavior of (S^\star); it is not the paper's objective and
persistence is not synonymous with regime.

## Repository role

`Trend-Estimation` is a **library-first research repository**.

Reusable mathematics, estimators, forecasting, validation, optimization,
simulations, metrics, and plotting belong under `src/trend_estimation/`.
Papers and experiments must import the installed package rather than copy
library logic.

The maintainer owns the repository and has explicitly allowed structural
refactors. Historical draft material is intentionally removed from `main`;
Git history is the archive.

The supported local development install is:

~~~bash
pip install -e .
~~~

The pip distribution is `trend-estimation` and the Python import is
`trend_estimation`.

## Documentation

`docs/` is the canonical Sphinx documentation for the public library API.
Do not add ad-hoc Markdown files under `docs/`.

`notes/` is the internal scientific notebook for derivations, checkpoints,
research decisions, and the active roadmap.

`literature/pdfs/` and `literature/extracted/` are intentionally versioned
in Git. The maintainer wants the original PDFs used by the project, together
with extracted text, preserved in the repository while the paper is active.
Do not add ignore rules for these directories or delete their contents as
"local-only" artifacts.

When a public function or class changes, update its docstring and Sphinx API
page. When a mathematical result changes, update the relevant note first.

## Active paper

Only this research paper is active:

`paper_forecast-optimal-smoothing/`

Working title:

**Adaptive Forecast-Optimal Trend Estimation under Changing Time-Series Regimes**

The decision-aware/portfolio project is paused.

The research object is

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

Here (d) is difference order, (L) is finite-memory window length, and (S)
is normalized smoothness. The scientific target is future forecast loss, not
historical trend-recovery loss.

The empirical progression is controlled simulations, mechanism studies,
within-series regime transitions, adaptive-versus-fixed OOS evaluation,
macroeconomic series, indices/ETFs, equities, and crypto. Do not reduce regime
to volatility or persistence alone.

## Core analytic model

For the pure smoother,

\[
\widehat t_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}y.
\]

Let \(Q=D_d^\top D_d\) and \(S_\lambda=(I+\lambda Q)^{-1}\). Then

\[
S_\lambda'=-S_\lambda Q S_\lambda,
\]

\[
\widehat t_\lambda'=-S_\lambda Q\widehat t_\lambda,
\qquad
\widehat t_\lambda''=2S_\lambda Q S_\lambda Q\widehat t_\lambda.
\]

The detailed derivation is in `notes/derivative.md`.

## Forecast loss

For a causal forecast origin \(T\),

\[
r_T(\lambda)
=
y_{T+1:T+h}
-
H S_\lambda y_{\mathrm{past}}.
\]

The implemented derivatives are

\[
f_T'(\lambda)
=
\frac{2}{h}
r_T^\top H S_\lambda Q S_\lambda y_{\mathrm{past}},
\]

and

\[
f_T''(\lambda)
=
\frac{2}{h}
\left[
\|H S_\lambda Q S_\lambda y_{\mathrm{past}}\|_2^2
-
2r_T^\top H S_\lambda Q S_\lambda Q S_\lambda y_{\mathrm{past}}
\right].
\]

## Numerical selection

Work in \(\theta=\log\lambda\). The active robust search is:

1. coarse derivative scan in log-lambda;
2. bracket sign changes;
3. Brent root solve;
4. classify stationary points;
5. compare local minima and search boundaries.

Newton is a refinement/benchmark, not the sole global method.

## Validation invariant

At outer origin \(T\), no observation after \(T\) may influence fitting or
hyperparameter selection.

Use:

- `select_fixed_window_pure_smoothness` for inner \((d,L,\lambda)\) selection;
- `nested_rolling_pure_forecast` for untouched outer evaluation.

Candidate windows are compared on identical inner forecast origins.

## Model naming

`PurePenalizedTrend` is the zero-drift quadratic model used for the current
analytic work.

`GuerreroTrend` implements the Guerrero (2007) observed-difference plug-in
drift

\[
\widehat m_y=(N-d)^{-1}\mathbf1^\top D_dy.
\]

`IteratedDriftTrend` preserves the repository's old iterative drift procedure
for reproducibility and must not be described as Guerrero (2007) equation (18).

## Current implementation checkpoint

Implemented:

- pure penalized smoother and analytic trend derivatives;
- explicit forecast continuation operator;
- forecast-loss first/second derivatives;
- derivative-root stationary-point search;
- fixed-window forecast-optimal selection;
- common validation origins across candidate windows;
- nested rolling evaluation with leakage-invariance tests;
- no-change benchmark and relative RMSFE;
- local-linear AR(1) and two-regime simulations;
- oracle recovery-optimal lambda for simulations;
- first active simulation driver.

Next:

1. controlled simulation is complete at 1,000 seeds;
2. the development and pre-frozen held-out real-data panels are complete and
   establish a qualified financial boundary;
3. the 64-series large-robustness panel is also complete at **explore**
   temporal density; read
   `notes/checkpoints/2026-09-29_large-universe-financial-results.md`;
4. combined frequency-aware evidence now covers 92 distinct financial series
   (32 ETFs, 48 stocks, 12 crypto); class medians adaptive/frozen-all-pre remain
   above one while frozen-all-pre remains approximately no-change;
5. the large-panel run was accidentally/implicitly `preset=explore`, so the
   next clean sensitivity is the same panel at denser paper origins:
   `python experiments/forecast_optimal_smoothing/run_real_data_validation.py --panel large-robustness --preset paper --scale-policy frequency-aware --workers 32`;
6. do not change windows, M, horizons, or the 321 discovery grid for that run;
7. after paper-density results are inspected, run the numerical discovery-grid
   sensitivity:
   `python experiments/forecast_optimal_smoothing/run_real_data_validation.py --panel large-robustness --preset paper --scale-policy frequency-aware --n-grid 1025 --workers 32`;
8. treat 321 vs 1025 as numerical root-discovery robustness, not model tuning;
   Brent already refines bracketed roots continuously;
9. any expansion of the discrete candidate windows/orders is a separate
   exploratory model-expansion study and must preserve all previous results;
10. macro remains separate: implement ALFRED vintage-correct GDP/INDPRO before
    paper-final macro claims; continue the literature novelty audit.

## Canonical internal notes

Read before changing research logic:

- `notes/research_objective.md` — first scientific source of truth;
- `notes/current_state.md` — chronological status, interpretations, and next actions;
- `notes/key_results.md`
- `notes/derivative.md`
- `notes/numerical_selection.md`
- `notes/model_definitions.md`
- `notes/window_and_smoothness.md`
- `notes/nested_validation.md`
- `notes/roadmap.md`

## CI policy

Push/pull-request CI is lightweight: editable install, tests, and Sphinx
validation.

Paper/PDF compilation is manual-only via `workflow_dispatch` and uploaded as
artifacts; generated paper outputs are not auto-committed.
