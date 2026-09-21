# Roadmap: Forecast-Optimal Trend Smoothing

This is the canonical active-paper roadmap. It records both **what** we are doing and **why**.

## Scientific objective

We want to determine whether forecast-optimal trend smoothness is stable or instead changes systematically with forecast horizon, estimation-window length, and local time-series regime.

The empirical object is

\[
S^\star_{T,h}
=
g(h,L,\mathcal R_T,\text{series class}),
\]

together with out-of-sample forecast skill.

The paper is not "a new way to choose lambda by cross-validation." Cross-validation and automatic smoothing selection have substantial prior literature. The intended contribution is the interaction among penalized trend smoothing, forecast horizon/window, local regime, and cross-asset/series behavior, supported by a derivative-aware numerical selection method.

---

## Phase 0 — Repository architecture

**Status:** in progress / largely complete.

### What

- treat `trend_estimation` as the reusable research library;
- use `paper_<short-title>/` manuscript names;
- maintain internal derivations under `notes/`;
- maintain literature metadata/RAG inputs under `literature/`;
- keep legacy manuscript assets separate from canonical papers.

### Why

Several papers can arise from the same mathematical machinery. Reusable methods should be tested once in the library and then consumed by manuscripts rather than copied.

### Deliverables

- [x] active paper renamed to `paper_forecast-optimal-smoothing/`;
- [x] tutorial renamed to `paper_penalized-trend-tutorial/`;
- [x] root `notes/` structure;
- [x] literature manifest workflow;
- [x] library-first repository policy documented.

---

## Phase 1 — Mathematical model audit

**Status:** active.

### What

Precisely distinguish:

1. pure quadratic penalized trend;
2. published Guerrero plug-in drift estimator;
3. current iterative Guerrero-style implementation;
4. possible jointly estimated drift variant.

### Why

The derivative formulas and statistical interpretation depend on the exact estimator. A paper cannot claim a derivative for one model while code fits another.

### Deliverables

- [x] pure model definition fixed;
- [x] pure first/second derivatives derived and implemented;
- [ ] verify Guerrero (2007) drift estimator directly from the paper;
- [ ] decide whether the current iterative solver is retained, renamed, replaced, or supplemented;
- [ ] add tests demonstrating the distinction.

Reference: `notes/model_definitions.md`.

---

## Phase 2 — Correct forecast-loss derivative

**Status:** active.

### What

Use a causal future-block forecast objective:

\[
r_T(\lambda)
=
y_{T+1:T+h}
-
H S_\lambda y_{\mathrm{past}}.
\]

Derive and implement \(f_T'\) and \(f_T''\), then pool them over rolling origins.

### Why

The active paper concerns forecasting. A derivative of an in-sample smoother residual selected by a matrix \(R\) is not the same object as the derivative of a genuine future forecast loss.

### Deliverables

- [x] derivation recorded in `notes/derivative.md`;
- [ ] implementation in `forecasting/objectives.py`;
- [ ] finite-difference tests;
- [ ] rolling-origin pooled derivative tests.

---

## Phase 3 — Numerical lambda selection

**Status:** active.

### What

Implement and benchmark:

- diagnostic grid;
- bounded scalar minimization in log-\(\lambda\);
- bracket + Brent root solving on the derivative;
- Newton in log-\(\lambda\).

### Why

The validation objective may have several local extrema. A single unimodal minimizer or one Newton initialization is not a robust global procedure.

### Deliverables

- [ ] `find_stationary_points_log_lambda`;
- [ ] local minimum/maximum classification;
- [ ] boundary handling;
- [ ] synthetic multimodal tests;
- [ ] adaptive-bracketing sensitivity check;
- [ ] benchmark evaluation counts and runtime.

Reference: `notes/numerical_selection.md`.

---

## Phase 4 — Temporal validation design

**Status:** partial: rolling split generator exists.

### What

Create nested chronological selection for

\[
(d,L,\lambda).
\]

- outer rolling origins evaluate generalization;
- inner chronological origins choose hyperparameters;
- no future value enters the fit or tuning for its own forecast.

### Why

One 60/20/20 split can make \(\lambda^\star\) depend heavily on one historical episode. Repeated forecast origins let us study time variation in optimal smoothing.

### Deliverables

- [x] `rolling_origin_splits`;
- [ ] nested rolling selector;
- [ ] expanding-window mode;
- [ ] fixed-length rolling-window mode;
- [ ] horizon-specific configuration;
- [ ] leakage tests.

---

## Phase 5 — Controlled simulations

**Status:** planned.

### What

Generate series

\[
y_t=\tau_t+\varepsilon_t
\]

while controlling:

- observation-noise variance;
- trend innovation/roughness;
- AR dependence;
- structural breaks;
- regime switches;
- sample size;
- forecast horizon.

### Why

Real data have no observed "true trend." Simulations let us separate trend-recovery quality from forecast quality and test when their optimal smoothing levels differ.

### Key questions

- Does \(\lambda^\star_{\rm recovery}\neq\lambda^\star_{\rm forecast}\)?
- How does \(S^\star\) react to signal-to-noise ratio?
- What does autocorrelation do to selected smoothness?
- What happens near structural breaks/endpoints?
- When does the root-based optimizer outperform or fail relative to a dense grid?

---

## Phase 6 — Macroeconomic data

**Status:** planned.

### What

Begin with lower-frequency economic series such as real GDP and industrial production, then possibly CPI or related series.

### Why

These provide a comparatively clear low-frequency trend setting and connect naturally to the HP/filtering literature.

### Required comparisons

- random walk/no-change where meaningful;
- HP and related penalized smoothers;
- simple extrapolation benchmarks;
- rolling-origin skill;
- horizon dependence.

---

## Phase 7 — Market index / ETF and equity data

**Status:** pilot assets already exist for S&P 500; full design planned.

### What

Move from aggregate market series to:

- broad index / ETF;
- selected individual equities spanning different empirical conditions.

### Why

This tests whether the smoothness/horizon relationship survives in noisier financial data.

### Important evaluation rule

Do not interpret low level-price RMSE alone as strong predictability. At minimum compare against

\[
\widehat P_{T+h|T}^{RW}=P_T
\]

and report relative forecast error/skill.

Also evaluate log returns or trend changes when scientifically appropriate.

---

## Phase 8 — Crypto

**Status:** planned.

### What

Use BTC and ETH first; add more assets only if they add distinct regimes rather than volume.

### Why

Crypto provides a higher-volatility, continuously traded setting with different dependence and regime behavior. It should not be treated merely as "equity with larger variance."

---

## Phase 9 — Regime relation

**Status:** planned.

### What

For each forecast origin construct local descriptors such as:

\[
X_T=
(
\widehat\sigma_T,
\widehat\rho_{1,T},
\text{trend strength},
\text{break indicators},
\ldots
).
\]

Study

\[
S^\star_{T,h}=g(X_T,h,L)
\]

and

\[
\operatorname{Skill}_{T,h}=q(X_T,S^\star_{T,h},h,L).
\]

### Why

The substantive question is whether forecast-optimal smoothing adapts systematically to the state of the process.

Do not define "regime" as volatility alone unless the data support that simplification.

---

## Phase 10 — Statistical forecast comparison

**Status:** planned.

### What

Use formal predictive-accuracy inference where appropriate, including literature such as Diebold-Mariano and conditional predictive ability.

### Why

A lower sample RMSE is not by itself sufficient evidence that one forecasting rule is systematically better.

---

## Phase 11 — Paper synthesis

**Status:** skeleton created.

### Paper story

1. penalized trend model;
2. forecast-optimal smoothness;
3. analytic forecast-loss derivatives;
4. robust numerical stationary-point selection;
5. chronological/nested validation;
6. simulations;
7. macro-to-equity-to-crypto empirical study;
8. regime dependence and limitations.

### What is explicitly not in this paper

- portfolio optimization;
- trading utility as the primary objective;
- `lambda_forecast` versus `lambda_decision`.

Those remain possible future papers built on the same library.

---

## Literature workflow

The literature set is tracked in `literature/manifest.csv`. For each high-priority paper, create a structured note or extracted representation answering:

- research question;
- estimator;
- how smoothness/\(\lambda\) is selected;
- validation protocol;
- forecasting versus smoothing objective;
- forecast horizon/window;
- data;
- regimes considered;
- main result;
- limitations;
- closest overlap with our paper;
- what remains different;
- useful equations and exact pages.

The literature audit must happen before making novelty claims.

---

## Definition of "ready to draft results"

Do not write a results section around the main claim until all are true:

- [ ] estimator definitions audited;
- [ ] forecast derivatives pass numerical checks;
- [ ] stationary-point search passes synthetic multimodal tests;
- [ ] nested chronological validation implemented;
- [ ] random-walk/no-change financial benchmark included;
- [ ] simulation design frozen;
- [ ] literature overlap table completed;
- [ ] empirical datasets and horizons frozen.
