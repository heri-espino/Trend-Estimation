# Roadmap: Forecast-Optimal Trend Smoothing

This is the canonical active-paper roadmap. It records both **what** we are doing and **why**.

## Scientific objective

The canonical source of truth is \`notes/research_objective.md\`.

The active paper studies:

> **Forecast-optimal trend estimation as an adaptive forecasting method, where
> smoothness, memory length and difference order depend on horizon and local
> regime.**

At forecast origin \(T\) and horizon \(h\), the full forecasting-method object
is

\[
\boxed{
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
}
\]

The three coordinates are:

- \(d^\star\): finite-difference order;
- \(L^\star\): finite-memory estimation-window length;
- \(S^\star\): normalized smoothness.

The local state \(X_T\) may include volatility, persistence, trend strength,
break evidence, local roughness, and other measurable conditions. Regime must
not be reduced to volatility alone or persistence alone without evidence.

The paper has three scientific levels:

1. **Target dependence:** forecast-optimal and trend-recovery-optimal
   configurations need not coincide.
2. **Mechanisms:** persistence, horizon, signal-to-noise, roughness, endpoints,
   and structural changes can explain why \(\Theta^\star\) moves.
3. **Adaptation value:** determine whether \(\Theta^\star_{T,h}\) tracks local
   regime in a useful way and whether adaptive selection improves untouched
   out-of-sample forecasts relative to strong fixed methods.

The persistence/AR(1) study is Level II only. It is a mechanism diagnostic,
not the paper's objective.

The paper is also not "a new way to choose lambda by cross-validation."
Cross-validation and automatic smoothing selection have substantial prior
literature. Chronological validation is a correctness requirement; the intended
contribution is the adaptive forecasting problem and its empirical behavior.

## Phase 0 — Repository architecture

**Status:** complete for the current stage.

- [x] library-first architecture documented;
- [x] `paper_forecast-optimal-smoothing/` is the active paper;
- [x] `paper_penalized-trend-tutorial/` is the tutorial companion;
- [x] `notes/` is the internal scientific notebook;
- [x] `literature/` contains the 40-paper manifest and RAG workflow;
- [x] obsolete reports, old S&P manuscript assets, copied legacy scripts, and placeholder modules removed from `main`;
- [x] editable package install standardized as `pip install -e .`;
- [x] public API cleaned around explicitly named models and selectors;
- [x] Sphinx documentation added with a root index, user guides, and API reference;
- [x] CI validates editable installation, tests, and the Sphinx build.

**Why:** several papers can share the same tested mathematical library.

## Phase 1 — Mathematical model audit

**Status:** complete for the current stage.

- [x] pure penalized model defined;
- [x] pure first/second derivatives derived and implemented;
- [x] Guerrero (2007) equations (17)--(18) checked directly;
- [x] canonical `GuerreroTrend` aligned with the observed-difference plug-in estimator;
- [x] historical iterative variant renamed `IteratedDriftTrend`;
- [x] direct formula/model-distinction tests added;
- [ ] derive/test Guerrero plug-in forecast-loss sensitivity only if it becomes necessary for the active experiments.

Reference: `notes/model_definitions.md`.

## Phase 2 — Correct forecast-loss derivative

**Status:** implemented for the pure model; validation ongoing.

- [x] causal future-block residual defined;
- [x] first derivative derived;
- [x] second derivative derived;
- [x] single-origin implementation in `forecasting/objectives.py`;
- [x] pooled rolling-origin implementation;
- [x] finite-difference test added;
- [x] pooled-aggregation test added;
- [ ] benchmark numerical stability over extreme \(\lambda\), \(d\), and window lengths.

Reference: `notes/derivative.md`.

## Phase 3 — Numerical lambda selection

**Status:** first implementation complete; robustness experiments pending.

- [x] direct bounded minimization in log-\(\lambda\) retained as benchmark;
- [x] Newton in log-\(\lambda\);
- [x] `find_stationary_points_log_lambda`;
- [x] Brent root solving on derivative sign-change brackets;
- [x] stationary-point classification from log-space curvature;
- [x] boundary comparison;
- [x] known multimodal unit test;
- [ ] adaptive refinement where the derivative changes rapidly or approaches zero;
- [ ] comparison against very dense diagnostic grids;
- [ ] evaluation-count and runtime benchmark;
- [ ] stress tests for nearly flat/tangential roots.

Reference: `notes/numerical_selection.md`.

## Phase 4 — Temporal validation design

**Status:** active; inner fixed-window selector implemented.

- [x] chronological rolling-origin split generator;
- [x] identify that fixed \(\lambda\) is not fixed normalized smoothness when \(N\) changes;
- [x] fixed-window inner selector for candidate \((d,L,\lambda)\);
- [x] convert selected \(\lambda\) to smoothness using the candidate window \(N=L\);
- [x] complete nested outer rolling evaluator;
- [x] no-change/random-walk level benchmark in the nested evaluator;
- [x] direct leakage-invariance test for the outer forecast;
- [ ] expanding-window robustness protocol;
- [ ] multiple forecast horizons in the outer experiment grid;

**Why:** one 60/20/20 split can make the selected smoothness depend on one historical episode. Fixed-width inner windows also give a clean interpretation of a shared \(\lambda\) as a shared smoothness level for each candidate \(L\).

Reference: `notes/window_and_smoothness.md`.

## Phase 5 — Controlled simulations

**Status:** infrastructure implemented; first factorial and persistence
mechanism runs completed; search-boundary robustness and adaptive-transition
experiments pending.

Generate

\[
y_t=\tau_t+\varepsilon_t
\]

while controlling noise variance, trend roughness, AR dependence, structural breaks, regimes, sample size, and horizon.

Implemented infrastructure:

- [x] local-linear latent trend with independently controlled trend roughness;
- [x] AR(1) observation noise with controlled marginal scale and persistence;
- [x] two-regime generator with separate changes in roughness, variance, persistence, level, and slope;
- [x] oracle latent-trend recovery objective and derivative-based lambda selection;
- [x] first factorial simulation driver under `experiments/forecast_optimal_smoothing/`;
- [x] run and inspect the first factorial simulation grid;
- [x] run a dedicated persistence/horizon mechanism study;
- [ ] run Exploration 03 with `--preset boundary`: same seeds/DGP grid as
  Exploration 02, but log-lambda bounds [-18,24] and 321 discovery points;
- [ ] add dedicated within-series regime-transition experiments after
  search-boundary robustness is established;
- [ ] track the joint path of
  ((d^star_{T,h},L^star_{T,h},S^star_{T,h})) and estimate adaptation
  delay after regime changes;
- [ ] compare adaptive selection with strong fixed configurations under
  untouched outer evaluation;
- [ ] freeze paper-scale parameter grid and seed count only after these checks;
- [ ] generate paper tables/figures only after design is frozen.

Key questions:

- Does (Theta^star_{m recovery}
eqTheta^star_{m forecast})?
- How do (d^star), (L^star), and (S^star) respond jointly to horizon
  and local state?
- How does optimal normalized smoothness respond to signal-to-noise ratio?
- What mechanisms are created by the sign and magnitude of autocorrelation?
- What happens near breaks/endpoints and after within-series regime changes?
- How quickly does the selected method adapt after a change?
- Does adaptive selection outperform strong fixed methods OOS?
- When does root-based lambda selection agree with or improve on grid/Newton
  methods?

## Phase 6 — Macroeconomic data

**Status:** planned.

Start with lower-frequency economic series such as real GDP and industrial production. Use the same estimator/selection machinery as later financial series.

**Why:** provides a clear low-frequency trend setting and anchors the work in classical filtering literature.

## Phase 7 — Market index / ETF and equity data

**Status:** new protocol not yet run. Historical S&P 500 draft assets were removed from `main` during repository cleanup and remain available through Git history.

Use broad index/ETF series and selected equities across different empirical conditions.

Minimum financial benchmark:

\[
\widehat P_{T+h|T}^{RW}=P_T.
\]

Do not interpret low level-price RMSE alone as evidence of exploitable predictability. Evaluate returns or trend changes separately when appropriate.

## Phase 8 — Crypto

**Status:** planned.

Start with BTC and ETH. Add further assets only if they contribute distinct regimes or structure.

**Why:** crypto is not simply "equity with larger variance"; its dependence and regime behavior may differ.

## Phase 9 — Regime relation

**Status:** planned.

Construct local descriptors

\[
X_T=
(
\widehat\sigma_T,
\widehat\rho_{1,T},
\text{trend strength},
\text{break indicators},
\text{local roughness},
\ldots
)
\]

and study

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(X_T,h,\mathcal C),
\]

together with

\[
\operatorname{Skill}_{T,h}
=
q(X_T,\Theta^\star_{T,h},h,\mathcal C).
\]

Do not define regime as volatility alone or persistence alone unless evidence
supports that simplification.

## Phase 10 — Statistical forecast comparison

**Status:** planned.

Add formal predictive-accuracy inference where appropriate, including Diebold-Mariano and conditional predictive-ability ideas from the literature audit.

## Phase 11 — Paper synthesis

**Status:** manuscript skeleton created.

Planned story:

1. penalized trend model;
2. forecast-optimal smoothness;
3. analytic forecast-loss derivatives;
4. bracketed numerical stationary-point selection;
5. nested chronological validation;
6. controlled simulations;
7. macro-to-equity-to-crypto evidence;
8. regime dependence and limitations.

Explicitly excluded from the active paper:

- portfolio optimization;
- trading utility as the primary objective;
- forecast-optimal versus decision-optimal smoothing.

These remain possible future papers built on the same library.

## Literature workflow

The 40-paper target set is in `literature/manifest.csv`. For high-priority papers, record research question, estimator, lambda-selection rule, validation protocol, horizon/window, data, regime definition, main result, limitations, overlap with our paper, remaining gap, useful equations, and exact pages.

As of 2026-09-22, the manifest contains 40 target references and 24 papers are
present in `literature/extracted/`. The extracted corpus has been reviewed,
but the target audit is not complete.

No novelty claim is final until the high-priority remainder of this audit is
complete.

## Definition of "ready to draft results"

- [x] estimator definitions audited for the pure model and Guerrero plug-in;
- [ ] derivative stability tests complete;
- [ ] root search stress-tested against dense diagnostics;
- [x] nested chronological validation implemented;
- [x] random-walk/no-change financial benchmark included;
- [ ] simulation design frozen;
- [ ] literature overlap table completed;
- [ ] empirical datasets and horizons frozen.
