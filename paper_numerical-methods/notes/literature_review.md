> **Split note (2026-10-05):** This review was written before the project was separated into a criterion paper and a numerical-methods paper. Treat it as source material, not the current novelty statement. Paper A positioning is in ../../paper_smoothness-cv/notes/literature_positioning.md; the numerical paper's current positioning is in submission_positioning.md.

# Literature Review — Numerical Selection of Forecast-Optimal Smoothness

**Status:** working literature review for the active numerical paper.

**Purpose:** document what is already established, identify the closest predecessors,
and state precisely what the active paper does differently. This note is intended
to support the Introduction/Related Work sections and to prevent accidental
novelty overclaims.

**Scope warning:** this review is grounded in the literature currently collected
under \`literature/\`. A claim such as "not found in this corpus" is not equivalent
to "first in the literature." Any priority claim would require a targeted
external novelty audit.

---

## 1. The literature problem in one sentence

The active paper sits at the intersection of five established literatures:

\[
\boxed{
\text{penalized trend smoothing}
+
\text{smoothing-parameter selection}
+
\text{predictive time-series validation}
+
\text{numerical optimization}
+
\text{forecast extrapolation}
}
\]

None of those ingredients is new by itself. The paper's contribution is the
specific numerical treatment of a **horizon-specific rolling forecast-loss
surface for finite-difference penalized least squares when that surface can have
multiple local minima and relevant boundary optima**.

---

# 2. Historical foundation: penalized trend smoothing

## 2.1 Whittaker (1923)

Whittaker's graduation method is an early formulation of quadratic smoothing:
fit the observations while penalizing roughness in the fitted sequence. This is
the historical ancestor of Whittaker--Henderson smoothing and of the
finite-difference PLS estimator used in the active paper.

The key idea already present is the trade-off

\[
\text{fidelity to the data}
\quad\leftrightarrow\quad
\text{roughness of the fitted sequence}.
\]

### What this means for our paper

We do **not** claim to introduce quadratic penalized smoothing.

**Repository source:**
\`literature/extracted/Whittaker-1923-new_method_graduation.md\`.

---

## 2.2 Guerrero (2007)

Guerrero develops penalized least squares for time-series trend estimation using
finite differences. In the broader formulation, the observed series is written
as a trend plus noise and the \(d\)-th difference of the trend is modeled around
a drift \(\mu\).

The active numerical paper deliberately studies the simpler zero-drift,
identity-weighted case

\[
\widehat\tau_{\lambda,d}
=
\arg\min_\tau
\left\{
\|y-\tau\|_2^2
+
\lambda\|D_d\tau\|_2^2
\right\},
\]

with solution

\[
\widehat\tau_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}y.
\]

Guerrero also connects the smoothing parameter with a statistical
noise-to-signal interpretation under additional stochastic assumptions.

### What this means for our paper

The estimator is established. Our paper uses a special case because the
numerical contribution is easier to isolate and its derivatives are available in
closed form.

**Repository source:**
\`literature/extracted/Guerrero-2007-time_series_smoothing_penalized_least_squares.md\`.

---

# 3. Controlled smoothness and the meaning of lambda

## 3.1 Guerrero (2008)

Guerrero proposes choosing an interpretable percentage of smoothness rather than
working directly with the raw penalty \(\lambda\). The smoothness measure is
based on the trace of the smoothing matrix.

This is important because \(\lambda\) itself is not directly comparable across
sample lengths and smoothing orders.

For \(d\ge1\), the established Guerrero-style index can be written as

\[
S_G(\lambda;N)
=
1-
\frac{\operatorname{tr}(H_\lambda)}{N},
\qquad
H_\lambda=(I+\lambda D_d^\top D_d)^{-1}.
\]

Its attainable upper limit is

\[
1-\frac dN,
\]

not exactly one.

### What the active paper changes

We normalize the established index to

\[
\boxed{
S(\lambda)
=
\frac{S_G(\lambda;N)}{1-d/N}
}
\]

so that

\[
S(0)=0,
\qquad
S(\infty)=1.
\]

This normalization is useful because the two limiting models become exact
endpoints of a compact search domain.

This should be presented as a **numerically convenient normalization of an
established smoothness concept**, not as the invention of controlled
smoothness.

**Repository source:**
\`literature/extracted/Guerrero-2008-estimating_trends_percentage_smoothness.md\`.

---

# 4. Classical smoothing-parameter selection

## 4.1 Craven and Wahba (1979): CV and GCV

Cross-validation and generalized cross-validation are classical tools for
selecting smoothing parameters in spline smoothing. Their purpose is to balance
fit and effective model complexity without requiring the analyst to set the
smoothing parameter manually.

### Relevance

This establishes that **data-driven selection of a smoothing parameter is old**.

**Repository source:**
\`literature/extracted/Craven-1979-smoothing_noisy_data_spline_functions.md\`.

---

## 4.2 Cortés-Toto, Guerrero, and Reyes (2017)

This is one of the closest papers to our PLS setting.

They implement, inside penalized least squares,

- CV;
- GCV;
- AICc;
- BIC;

and study the amount of smoothness achieved by the parameter selected by each
criterion.

Their study emphasizes how attained smoothness changes with factors such as
sample size and trend type. In particular, the paper concludes that sample size
is a major determinant of the smoothness attained by the classical criteria.

### Difference from the active paper

Their primary question is:

> How much smoothness is produced when \(\lambda\) is chosen by established
> optimality criteria?

Our question is different:

> If smoothness is defined by **chronological future forecast error**, how do we
> solve the resulting numerical optimization problem reliably when the objective
> can contain several local minima?

Their CV/GCV criteria are not our rolling future-block forecast loss.

### Consequence for novelty

We cannot claim that selecting \(\lambda\) by CV inside PLS is new.

**Repository source:**
\`literature/extracted/Cortes_Toto-2017-trend_smoothness_optimality_criteria.md\`.

---

# 5. Predictive selection of trend smoothness already exists

## 5.1 Hart (1994): time-series cross-validation

Hart is the most important conceptual novelty boundary.

Hart studies kernel trend smoothing for dependent time-series data and selects
the smoothing bandwidth using one-step-ahead predictive performance based only
on observations available in the past.

Conceptually,

\[
\text{past data}
\rightarrow
\text{fit smoother}
\rightarrow
\text{one-step forecast}
\rightarrow
\text{prediction error}
\]

is repeated through time, and the bandwidth is selected by predictive error.

### Why Hart matters

Hart establishes that:

\[
\boxed{
\text{choosing trend smoothness by chronological prediction error is not new.}
}
\]

Therefore the active paper must not claim to introduce predictive
smoothing-parameter selection.

### How our paper differs

Hart:

- uses a kernel trend smoother;
- chooses a bandwidth rather than a finite-difference PLS penalty;
- focuses on one-step-ahead prediction;
- explicitly considers serial correlation in the error process;
- does not formulate the problem in normalized Guerrero smoothness;
- does not make exhaustive/reliable recovery of multiple local minima the
  numerical object of study.

Our paper:

- uses finite-difference PLS;
- works on \(S\in[0,1]\);
- permits explicit \(h\)-step future blocks;
- uses rolling windows and rolling origins;
- derives analytic first and second derivatives of the forecast loss;
- explicitly searches for multiple relevant minima and exact endpoints.

**Repository source:**
\`literature/extracted/Hart-1994-time_series_cross_validation.md\`.

---

# 6. Rolling-origin forecast evaluation is established

## 6.1 Tashman (2000)

Tashman systematizes out-of-sample forecast evaluation and distinguishes choices
such as:

- fixed versus rolling forecast origins;
- forecast horizon;
- updating/recalibration;
- fixed versus rolling windows;
- single versus repeated test periods.

The central principle is that evaluation should reproduce the information flow
available in an actual forecasting problem.

### Relevance

Our rolling validation design is methodologically standard and should be cited,
not presented as a novelty.

**Repository source:**
\`literature/extracted/Tashman-2000-out_of_sample_forecast_accuracy.md\`.

---

## 6.2 Bergmeir and Benítez (2012) and related work

The time-series cross-validation literature further systematizes rolling-origin,
rolling-window, blocked, and dependence-aware validation procedures.

### Relevance

The active paper borrows the chronological logic but uses it to construct a
specific scalar objective in smoothness space.

**Repository sources:**

- \`literature/extracted/Bergmeir-2012-cross_validation_time_series_predictors.md\`;
- \`literature/extracted/Bergmeir-2018-cross_validation_ar_time_series.md\`;
- \`literature/extracted/Burman-1994-cross_validatory_dependent_data.md\`.

---

# 7. Forecasting smoothed or controlled-smoothness trends is established

The Islas-Camargo / Guerrero applied line uses controlled-smoothness trend
estimates in economic forecasting applications, including remittances and
exchange-rate models.

Those works show that smoothing a series before fitting a forecasting model can
be substantively useful and that trend estimation and forecasting may be treated
as linked stages.

### Difference from the active paper

Those papers are not centered on numerically minimizing a rolling forecast-loss
surface over \(S\), nor on recovering multiple smoothness minima.

Our contribution is therefore not:

> "forecast a smoothed trend."

It is the numerical selection problem induced by forecast-based smoothness
choice.

**Repository sources:**

- \`literature/extracted/Islas_Camargo-2019-forecasting_remittances_mexico_rjef.md\`;
- \`literature/extracted/Islas_Camargo-2019-forecasting_remittances_mexico.md\`;
- \`literature/extracted/Islas_Camargo-2025-exchange_rate_predictability_controlled_smoothness.md\`.

---

# 8. Numerical computation for penalized smoothers is established

## 8.1 Weinert (2007)

Weinert develops efficient numerical computation for Whittaker--Henderson
smoothing, exploiting matrix structure and addressing efficient calculation of
smoothing criteria such as GCV.

### Relevance

Efficient implementation of a penalized smoother is not by itself our novelty.

**Repository source:**
\`literature/extracted/Weinert-2007-efficient_whittaker_henderson_smoothing.md\`.

---

## 8.2 Biessy (2025/2026)

Biessy places Whittaker--Henderson smoothing in a modern statistical and
computational framework. The paper covers, among other topics:

- effective degrees of freedom;
- Bayesian/statistical interpretations;
- marginal-likelihood/LAML smoothing-parameter selection;
- numerical optimization strategies;
- eigendecomposition / natural parameterization;
- reduced-rank computation;
- extrapolation and uncertainty.

Especially important for our novelty boundary, Biessy gives an example where a
GCV profile has **two local minima**.

The paper also compares numerical algorithms such as Newton, Brent,
Nelder--Mead, and generalized Fellner--Schall in its own smoothing-selection
setting.

### Consequences for the active paper

We cannot claim:

- that numerical optimization of a smoothing criterion is new;
- that Brent is new in smoothing-parameter selection;
- that multiple local minima in a smoothing criterion are newly discovered.

### Difference from our paper

Biessy's central target is not a rolling \(h\)-step future-block forecast-loss
surface for finite-difference PLS, and the recovery of all relevant minima of
that forecast objective is not the central numerical problem.

That distinction is one of the strongest reasons the active paper remains
defensible.

**Repository sources:**

- \`literature/extracted/Biessy-2025-whittaker_henderson_smoothing_revisited.md\`;
- \`literature/extracted/Biessy-2025-whittaker_henderson_smoothing_revisited_appendix.md\`.

---

# 9. Data-driven HP calibration is also active research

## Franke, Kukacka, and Sacht (2026)

Franke et al. revisit selection of the Hodrick--Prescott smoothing parameter
using artificial data with a known trend. They calibrate the smoothing
parameter according to how well the filtered trend recovers the synthetic true
trend and study the geometry of the parameter objective.

They also discuss that smoothing-parameter objectives can exhibit multiple local
minima.

### Difference from the active paper

Their target is approximately

\[
\text{distance to a known latent trend},
\]

which is available in simulation.

Our target is

\[
\text{chronological future forecast loss},
\]

which can be computed on observed time series without observing a latent true
trend.

This distinction is important:

\[
\boxed{
\text{recovery-optimal smoothness}
\neq
\text{forecast-optimal smoothness}
}
\]

in general.

**Repository source:**
\`literature/extracted/Franke-2026-data_driven_hp_smoothing_parameter.md\`.

---

# 10. Brent's method is a numerical component, not a contribution by itself

Brent (1971) gives a robust bracketed scalar root-finding algorithm.

In the active method Brent is applied only after the adaptive procedure has
found a bracket for a derivative root.

Thus:

\[
\boxed{
\text{adaptive discovery}
\rightarrow
\text{root bracket}
\rightarrow
\text{Brent refinement}
}
\]

Brent refines a root; it does not discover all roots globally.

### Consequence for writing

Never say "Brent finds all minima." The paper's contribution is the surrounding
discovery/classification/end-point procedure.

**Repository source:**
\`literature/extracted/Brent-1971-zero_finding_algorithm.md\`.

---

# 11. Where the active paper begins

After removing everything already established, the active paper's problem is:

For fixed \(d,L,h\), define

\[
F_{d,L,h}(S)
=
\frac{1}{|\mathcal O|}
\sum_{T\in\mathcal O}
\frac1h
\left\|
y_{T+1:T+h}
-
G_{d,h}H_{\lambda(S)}x_T
\right\|_2^2,
\]

where each forecast origin uses only its available rolling window.

Then solve

\[
\boxed{
S^\star
\in
\arg\min_{S\in[0,1]}
F_{d,L,h}(S)
}
\]

without assuming unimodality.

The key numerical pieces are:

1. compact normalized smoothness \(S\in[0,1]\);
2. exact endpoints \(S=0\) and \(S=1\);
3. analytic \(F'\) and \(F''\);
4. adaptive subdivision of regions with unresolved derivative structure;
5. derivative-root bracketing;
6. Brent refinement;
7. stationary-point classification;
8. global comparison of all detected minima and both limiting models.

The contribution is therefore not a new smoother. It is a numerical method for
a specific **forecast-optimal smoothness-selection landscape**.

---

# 12. Structural result discovered in the current project

For fixed \((d,L,h)\), the rolling forecast loss has more structure than a
generic smooth black-box objective.

Using the positive eigenvalues
\(\delta_1,\ldots,\delta_r\) of \(D_d^\top D_d\), define

\[
D(\lambda)
=
\prod_{j=1}^r
(1+\lambda\delta_j).
\]

Each forecast component is a finite combination of terms of the form

\[
\frac{1}{1+\lambda\delta_j},
\]

so the pooled forecast loss can be written as

\[
\boxed{
f(\lambda)
=
\frac{P(\lambda)}{D(\lambda)^2}
}
\]

for a polynomial \(P\), after accounting for possible cancellations.

Its derivative has the form

\[
\boxed{
f'(\lambda)
=
\frac{R(\lambda)}{D(\lambda)^3}
}
\]

where \(R\) is a polynomial. On \(\lambda\ge0\), the denominator is strictly
positive.

Consequently, except for degenerate cases, the interior stationary points are
roots of a finite-degree polynomial.

### Why this matters

This gives a theoretical explanation for why the relevant numerical difficulty
is **root discovery**, not pathological infinite oscillation.

It also motivates a possible stronger method:

\[
\text{polynomial root isolation}
\rightarrow
\text{Brent refinement}
\rightarrow
\text{classification/endpoints}.
\]

The repository already contains a small exact Sturm-sequence proof-of-concept.

### Current claim boundary

This structural result should be presented carefully. The current production
algorithm does not yet construct and isolate the general polynomial \(R\) for
all realistic cases. Therefore the paper can use the rational structure to
explain the geometry but should not yet claim certified exhaustive recovery for
all configurations.

This particular connection should receive a **targeted external literature
audit** before being described as novel.

---

# 13. Closest-predecessor comparison

| Work | Smoother / model | How smoothness is selected | Chronological forecast criterion? | Multiple minima discussed? | Multi-minimum numerical recovery is central? |
|---|---|---|---:|---:|---:|
| Whittaker (1923) | quadratic graduation / finite differences | fixed penalty | No | No | No |
| Craven & Wahba (1979) | smoothing spline | GCV | No | No | No |
| Guerrero (2007, 2008) | finite-difference PLS | variance-ratio / controlled percentage | No | No | No |
| Hart (1994) | kernel trend smoother | one-step-ahead TSCV | **Yes** | Not central | No |
| Weinert (2007) | Whittaker--Henderson | GCV / efficient computation | No | Not central | No |
| Cortés-Toto et al. (2017) | finite-difference PLS | CV, GCV, AICc, BIC | No | Not central | No |
| Islas-Camargo et al. | controlled-smoothness trend + forecasting model | controlled/data-guided smoothing | Forecasting application | No | No |
| Biessy (2025/2026) | Whittaker--Henderson | LAML / GCV / numerical optimization | No | **Yes** | No |
| Franke et al. (2026) | HP / related filtering | distance to known simulated trend | No | **Discussed** | No |
| **Active paper** | finite-difference PLS | rolling \(h\)-step future forecast MSE | **Yes** | **Yes** | **Yes** |

The last row describes the distinction relative to the current corpus. It is not
a universal priority claim.

---

# 14. What is genuinely different in the active paper

The most defensible distinction is the **combination** of the following:

### A. The criterion is explicitly forecast-optimal

We optimize future-block error rather than in-sample reconstruction, GCV,
information criteria, marginal likelihood, or distance to a latent trend:

\[
F_{d,L,h}(S)
=
\text{rolling future-block MSE}.
\]

### B. The horizon is explicit

The selected smoothness is conditional on \(h\). We do not collapse all
forecast horizons into one generic smoothing choice.

### C. The problem is treated as a multi-minimum numerical landscape

The method does not ask only for one scalar answer from a generic optimizer. It
tries to recover all **relevant** local minima before selecting the global best
candidate.

### D. The search domain has exact statistical/model endpoints

\[
S=0
\quad\leftrightarrow\quad
\lambda=0,
\]

and

\[
S=1
\quad\leftrightarrow\quad
\lambda=\infty
\]

are evaluated as exact limiting models rather than arbitrary large/small finite
penalties.

### E. Analytic derivatives are used for discovery and classification

The forecast objective is differentiated through the smoother and continuation
operator, giving direct information about stationary points and curvature.

### F. The benchmark evaluates missed minima, not only final objective value

The numerical study asks whether the algorithm recovers the relevant landscape,
how accurately it locates optima, and how many evaluations are required.

### G. The rational structure gives a stronger mathematical explanation

The current project shows that fixed-configuration forecast loss is rational in
\(\lambda\), with stationary points determined by a finite polynomial
numerator. This is a stronger statement than merely assuming a generic smooth
one-dimensional objective.

---

# 15. What the paper must not claim

The literature review directly rules out the following statements:

- "We introduce penalized trend smoothing."
- "We introduce a smoothness index."
- "We introduce data-driven smoothing-parameter selection."
- "We introduce CV/GCV for PLS."
- "We are the first to choose trend smoothness by prediction error."
- "We introduce rolling-origin validation."
- "We discover that smoothing criteria can be multimodal."
- "We introduce Brent/Newton optimization for smoothing parameters."
- "We introduce forecasting from a smoothed trend."
- "We prove the present adaptive sampler always finds every root."

---

# 16. Recommended novelty statement

A safe short formulation is:

> Building on predictive smoothing-parameter selection and rolling-origin
> forecast evaluation, we formulate a horizon-specific future-block forecast
> criterion for finite-difference penalized least squares in normalized
> smoothness space and develop an endpoint-aware derivative-based procedure for
> recovering and comparing multiple relevant local minima.

A somewhat stronger version, still conditional on the current corpus, is:

> The literature collected for this project contains the constituent ideas
> separately—penalized trend smoothing, controlled smoothness, predictive
> time-series cross-validation, rolling-origin evaluation, multiple-minimum
> smoothing criteria, and scalar numerical optimization—but does not contain
> their combination as a multi-minimum numerical search problem for
> horizon-specific forecast-optimal finite-difference PLS.

Do not replace "the literature collected for this project" with "the
literature" unless a targeted external audit supports the stronger statement.

---

# 17. Why the contribution is appropriate for the active SMCCA paper

The paper is best positioned as a scientific-computing contribution:

\[
\text{known statistical estimator}
\rightarrow
\text{newly isolated numerical problem}
\rightarrow
\text{structured derivatives/geometry}
\rightarrow
\text{adaptive algorithm}
\rightarrow
\text{controlled numerical validation}.
\]

The statistical model provides the structured objective; the main paper question
is computational:

> Can the relevant minima and boundary optima of the forecast-smoothness
> objective be located reliably with far fewer evaluations than a dense search?

This keeps the paper distinct from:

- the adaptive \((d,L,S)\) forecasting paper;
- the financial/recurrence paper;
- the future statistical-inference paper.

---

# 18. Literature gaps to audit before submission

Before using any absolute novelty language, perform targeted searches for:

1. finite-difference PLS with smoothing selected by rolling multi-step forecast
   loss;
2. derivative-based optimization of rolling forecast CV for penalized trends;
3. exhaustive/multi-root smoothing-parameter search rather than single-start
   minimization;
4. rational or polynomial characterizations of forecast-loss derivatives for
   Whittaker/HP/PLS smoothers;
5. Sturm/root-isolation methods applied to smoothing-parameter selection;
6. exact boundary treatment of \(\lambda=0\) and \(\lambda=\infty\) in
   forecast-optimal smoothing.

If a close predecessor is found, the paper can still survive by narrowing the
contribution to the exact structured algorithm and benchmark result. The
literature review should be updated rather than protecting a novelty claim.

---

# 19. Repository citation map

| Topic in manuscript | Main source(s) in repository |
|---|---|
| Historical quadratic smoothing | \`Whittaker-1923-new_method_graduation.md\` |
| Finite-difference PLS | \`Guerrero-2007-time_series_smoothing_penalized_least_squares.md\` |
| Controlled percentage of smoothness | \`Guerrero-2008-estimating_trends_percentage_smoothness.md\` |
| CV/GCV | \`Craven-1979-smoothing_noisy_data_spline_functions.md\` |
| PLS + CV/GCV/AICc/BIC | \`Cortes_Toto-2017-trend_smoothness_optimality_criteria.md\` |
| Predictive TSCV for trend smoothing | \`Hart-1994-time_series_cross_validation.md\` |
| Forecast-origin evaluation | \`Tashman-2000-out_of_sample_forecast_accuracy.md\` |
| Time-series CV designs | \`Bergmeir-2012-cross_validation_time_series_predictors.md\` |
| Efficient WH computation | \`Weinert-2007-efficient_whittaker_henderson_smoothing.md\` |
| Modern WH + multiple GCV minima + optimization | \`Biessy-2025-whittaker_henderson_smoothing_revisited.md\` |
| Data-driven HP calibration | \`Franke-2026-data_driven_hp_smoothing_parameter.md\` |
| Applied controlled-smoothness forecasting | \`Islas_Camargo-2019-forecasting_remittances_mexico_rjef.md\` |
| Brent root refinement | \`Brent-1971-zero_finding_algorithm.md\` |

---

## Bottom line

The literature does **not** support selling the paper as a new smoothing model,
a new cross-validation method, or the first predictive choice of smoothness.

The defensible paper is narrower:

\[
\boxed{
\text{forecast-defined smoothness objective}
+
\text{multi-minimum numerical geometry}
+
\text{derivative-aware endpoint-safe search}.
}
\]

That is the distinction the manuscript should preserve.
