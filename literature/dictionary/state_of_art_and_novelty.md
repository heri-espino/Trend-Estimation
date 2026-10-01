# State of the art and novelty map

## Purpose

This file is the canonical literature-positioning note for the active numerical
paper.

It is based on the local \`literature/bundle.md\` corpus. Its purpose is to
separate:

1. ideas that are already established in the literature;
2. the closest predecessors to the active paper;
3. combinations that were **not found in the bundle**;
4. wording that is safe for the manuscript.

Important limitation:

> **“Not found in the bundle” is not the same as “first in the literature.”**

The bundle is the citation base for the paper, but any eventual “first” claim
would require a separate targeted external literature audit.

---

# 1. What is already established

## 1.1 Penalized least-squares trend smoothing is old

Whittaker (1923) and the Whittaker--Henderson tradition already formulate
quadratic smoothing as a trade-off between fidelity to observations and a
smoothness penalty.

Guerrero (2007) develops the finite-difference penalized least-squares (PLS)
formulation for time-series trend estimation. In the notation of the active
paper,

\[
\widehat\tau_\lambda
=
(I+\lambda D_d^\top D_d)^{-1}y.
\]

Therefore the estimator itself is not new.

**Use for citations:** Whittaker (1923), Guerrero (2007), Weinert (2007),
Biessy (2025/2026).

---

## 1.2 Smoothness indices and controlled smoothness are established

Guerrero (2007, 2008) introduces the controlled-smoothness perspective: rather
than choosing \(\lambda\) directly, the analyst can specify a desired amount or
percentage of smoothness through a trace-based smoothness index.

Cortés-Toto, Guerrero, and Reyes (2017) write the index for \(d\ge 1\) as

\[
S_d(\lambda;N)
=
1-
\frac{
\operatorname{tr}
\left[
(I_N+\lambda K_d^\top K_d)^{-1}
\right]
}{N},
\]

with

\[
S_d(\lambda;N)\to0
\quad\text{as}\quad
\lambda\to0,
\]

and

\[
S_d(\lambda;N)\to1-\frac dN
\quad\text{as}\quad
\lambda\to\infty.
\]

The active paper's

\[
S(\lambda)
=
1-
\frac{1}{N-d}
\sum_{j=1}^{N-d}
\frac{1}{1+\lambda\delta_j}
\]

is therefore a **normalization of an established trace-based smoothness idea**,
chosen so that the attainable interval is exactly \([0,1]\).

Do not present the concept of a smoothness index as new.

**Use for citations:** Guerrero (2007, 2008); Cortés-Toto et al. (2017).

---

## 1.3 Selecting a smoothing parameter by CV/GCV is established

Craven and Wahba (1979) introduce GCV for spline smoothing.

Cortés-Toto et al. (2017) explicitly implement

- CV,
- GCV,
- AICc,
- BIC,

inside the PLS trend-smoothing framework to choose the smoothing parameter and
then study the smoothness attained by each criterion.

Their CV/GCV criteria are smoothing/reconstruction criteria. They are not the
same chronological rolling future-block forecast objective used in the active
paper.

Therefore:

> **Using CV to choose \(\lambda\) in PLS is not new.**

**Use for citations:** Craven and Wahba (1979); Cortés-Toto et al. (2017).

---

# 2. The closest conceptual predecessor: Hart (1994)

Hart (1994), *Automated Kernel Smoothing of Dependent Data by Using Time Series
Cross-Validation*, is the most important novelty boundary in the bundle.

Hart studies time-series trend estimation with a kernel smoother and chooses
the bandwidth using **time series cross-validation (TSCV)**.

The defining idea is predictive:

- construct the trend estimate using past data;
- produce a one-step-ahead prediction;
- choose the smoothing parameter to minimize prediction error.

Hart explicitly describes TSCV as seeking a good one-step-ahead predictor based
on past data.

This means:

> **Choosing trend smoothness by chronological predictive performance is not
> new.**

That claim must not appear in the paper.

Hart also emphasizes an important distinction for dependent data: a smoothing
choice that is good for estimating the historical trend need not coincide with
a smoothing choice that is good for prediction.

## How Hart differs from the active paper

Hart:

- uses kernel regression smoothing;
- selects a bandwidth;
- focuses on one-step-ahead prediction;
- explicitly models the serial correlation of the errors;
- aims primarily at smoothing-parameter/bandwidth selection;
- does not formulate the finite-difference PLS problem in normalized Guerrero
  smoothness;
- does not make recovery of multiple relevant local minima the numerical
  target studied in our paper.

The active paper:

- uses finite-difference quadratic PLS;
- searches a normalized smoothness coordinate \(S\in[0,1]\);
- allows fixed \(h\)-step future blocks;
- uses rolling windows / rolling forecast origins;
- derives analytic derivatives of the pooled forecast-validation objective;
- explicitly searches for multiple relevant local minima and exact boundary
  optima.

Hart should be cited whenever the manuscript motivates **predictive
smoothing-parameter selection**.

---

# 3. Chronological forecast evaluation is established

## Tashman (2000)

Tashman distinguishes:

- fit and test periods;
- fixed versus rolling forecast origins;
- forecast horizon;
- updating versus recalibration;
- fixed versus rolling windows;
- single versus multiple test periods.

He argues that out-of-sample evaluation should reproduce the real forecasting
environment and warns that looking at held-out observations during model
selection contaminates the evaluation.

This is the main source for the temporal logic of the active protocol.

## Bergmeir and Benítez (2012)

Bergmeir and Benítez systematize forecast-evaluation designs including:

- fixed-origin evaluation;
- rolling-origin recalibration;
- rolling-origin update;
- rolling-window evaluation.

They also emphasize that forecast horizon matters and that averaging across
different horizons can hide important differences.

Therefore:

> **Rolling-origin and rolling-window forecast evaluation are not new.**

The active paper uses these established evaluation ideas as the structure of
its smoothing-selection objective.

**Use for citations:** Tashman (2000); Bergmeir and Benítez (2012).

---

# 4. Cross-validation for dependent data is established

The bundle also contains a broader literature on CV under dependence.

Burman, Chow, and Nolan develop block-based CV ideas for stationary dependent
sequences, motivated by prediction-error estimation when ordinary
leave-one-out CV can be distorted by dependence.

The Bergmeir review discusses blocked, h-block, hv-block, last-block, and
rolling-origin alternatives.

This literature matters because the active paper should never imply that
ordinary random-fold CV is the natural default for time-series smoothing.

Our paper instead uses chronological future blocks at explicit forecast
origins.

---

# 5. Multiple minima in smoothing-parameter criteria are not new

Biessy (2025/2026) provides an especially important precedent.

In a Whittaker--Henderson smoothing example, the GCV profile has **two local
minima**. One is aligned with the marginal-likelihood solution while the global
GCV minimum produces an implausibly complex fit.

Therefore:

> **The observation that a smoothing-parameter criterion can have multiple
> local minima is not new.**

This is another claim we must not make.

What remains different is that our paper makes **recovery of multiple local
minima of a rolling forecast-validation objective** the central numerical
problem.

**Use for citations:** Biessy (2025/2026).

---

# 6. Numerical computation for penalized smoothing is established

Weinert (2007) develops efficient algorithms for Whittaker--Henderson smoothing
and for computation of its GCV score by exploiting matrix structure.

Biessy studies several numerical algorithms and optimization strategies for
marginal likelihood / LAML smoothing-parameter selection, together with banded
matrix and reduced-rank acceleration.

Therefore:

> **Efficient numerical computation of penalized smoothers and numerical
> optimization of smoothing criteria are not new by themselves.**

Our numerical claim has to be narrower: it concerns adaptive recovery of
multiple minima of our specific forecast-validation objective in normalized
smoothness space.

**Use for citations:** Weinert (2007); Biessy (2025/2026).

---

# 7. Data-driven HP smoothing-parameter calibration is established

Franke, Kukacka, and Sacht (2026) construct artificial data with a known trend
and use Monte Carlo experiments to determine HP smoothing parameters that best
approximate that true trend.

They also inspect the shape of the parameter-to-distance objective and
explicitly discuss the possibility of multiple local minima.

Their target is **distance to a known simulated trend**, not chronological
future forecast error.

Therefore the paper is relevant as evidence that:

- data-driven smoothing-parameter choice remains an active research topic;
- objective geometry in smoothing-parameter selection can matter;
- multiple minima can arise outside GCV as well.

It is not a predecessor of our exact rolling forecast-CV formulation.

---

# 8. Forecasting filtered/controlled-smoothness trends is established

The Islas-Camargo / Guerrero line of work uses controlled-smoothness trend
estimates in forecasting applications such as remittances and exchange rates,
including Markov-switching models fitted to the estimated trend.

These papers establish that:

- filtering/smoothing a series before forecasting can be a substantive modeling
  choice;
- controlled smoothness has been used in applied economic forecasting;
- trend estimation and forecasting can be treated as linked but distinct
  stages.

Their smoothing parameter is not selected by the active paper's rolling
future-block objective. The papers use controlled-smoothness/data-based
guidelines and then forecast the resulting trend with a separate model.

Therefore:

> **Forecasting a controlled-smoothness trend is not new.**

Our contribution is not “using a smoothed trend for forecasting.”

---

# 9. Extrapolation of penalized smoothers is established

Biessy explicitly studies extrapolation of Whittaker--Henderson smoothing.

The active paper's finite-difference continuation rule is therefore not
presented as the invention of trend extrapolation.

Its role in our paper is narrower:

- the continuation operator is fixed;
- because it is affine/linear in the fitted trend, analytic derivatives of the
  rolling forecast loss remain tractable;
- this permits the numerical study of smoothness selection.

---

# 10. What the bundle does **not** show

The following combination was **not found in the local bundle**.

This is the provisional novelty boundary of the active paper.

## 10.1 Formulation contribution

For finite-difference PLS, define a horizon-specific chronological objective

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

with:

- fixed difference order \(d\);
- fixed rolling-window length \(L\);
- explicit forecast horizon \(h\);
- refitting at chronological forecast origins;
- a normalized smoothness coordinate \(S\in[0,1]\).

The bundle contains the ingredients separately, but not this exact formulation
as the central smoothing-selection problem.

## 10.2 Numerical contribution

The bundle does not show a method that, for the objective above:

1. derives analytic first and second derivatives;
2. transports them through the monotone \(\lambda\leftrightarrow S\) map;
3. treats recovery of **multiple relevant local minima** as the target;
4. uses adaptive subdivision to find derivative-root brackets;
5. adds deterministic endpoint-aware refinement because compactification
   compresses large-\(\lambda\) structure near \(S=1\);
6. refines brackets with Brent's method;
7. classifies stationary points;
8. compares the interior minima with the exact limiting models \(S=0\) and
   \(S=1\).

This is the strongest numerical novelty in the current paper.

## 10.3 Interpretation contribution

The bundle also does not show the following applied diagnostic built around the
multiple-minimum set:

- discover and rank smoothing candidates using development-region forecast CV;
- freeze those candidates;
- show the distinct fitted trends and extrapolations induced by the minima;
- evaluate the frozen candidates on an untouched final block;
- report whether their validation ordering persists or undergoes a
  validation--test rank reversal.

This should be framed as **selection sensitivity**, not as test-set model
selection or statistical uncertainty.

---

# 11. Novelty hierarchy for the manuscript

## Primary contribution

> We study the numerical problem of recovering multiple relevant minima of a
> horizon-specific rolling forecast-validation criterion for finite-difference
> penalized trend estimation.

## Enabling formulation

> We express the search in a normalized smoothness coordinate
> \(S\in[0,1]\), with exact limiting estimators at the two boundaries, while
> retaining analytic derivatives through the original smoothing parameter.

The normalization itself is not the main scientific claim; it is the coordinate
that makes the numerical treatment and endpoint semantics clean.

## Applied interpretation

> The recovered minima form a finite set of distinct smoothing choices whose
> validation ranking may or may not persist on later unseen observations.

This motivates why recovering several minima can matter beyond simply locating
the global minimum.

---

# 12. Claims we must NOT make

Do not write:

- “We introduce cross-validation for trend smoothness.”
- “We are the first to choose smoothness by prediction error.”
- “We introduce time-series cross-validation for smoothing.”
- “We discover that smoothing criteria can have multiple local minima.”
- “We introduce rolling-origin validation.”
- “We introduce the idea of forecasting a smoothed trend.”
- “We introduce numerical optimization of the smoothing parameter.”

All of these are contradicted or substantially predated by sources in the
bundle.

---

# 13. Safe novelty wording

## Recommended short version

> Building on predictive smoothing-parameter selection and rolling-origin
> forecast evaluation, we focus on a numerical problem that has received less
> attention: recovering multiple relevant local minima of a horizon-specific
> forecast-validation criterion for finite-difference penalized trends.

## Recommended fuller version

> Predictive selection of a smoothing parameter is not new: time-series
> cross-validation has long been used to choose smoothing bandwidths from
> one-step-ahead predictive performance. Our contribution is instead the
> numerical treatment of the resulting selection landscape for
> finite-difference penalized least squares. We formulate a rolling
> \(h\)-step-ahead forecast-validation criterion in normalized smoothness
> space, derive analytic derivatives, and develop an endpoint-aware adaptive
> procedure that recovers and classifies multiple relevant local minima rather
> than returning a single scalar solution.

## Strongest wording currently justified by the bundle

> The local literature corpus contains the ingredients separately—penalized
> trend smoothing, predictive cross-validation, rolling-origin evaluation,
> smoothness indices, multiple-minimum smoothing criteria, and scalar numerical
> optimization—but does not contain their combination as a multi-minimum
> numerical search problem for rolling forecast-optimal finite-difference PLS.

Do not replace “the local literature corpus does not contain” with “the
literature does not contain” without a targeted external novelty search.

---

# 14. Citation map for writing the paper

| Manuscript point | Primary bundle citation(s) | What the source supports |
|---|---|---|
| Quadratic finite-difference smoothing / PLS | Whittaker (1923); Guerrero (2007) | Estimator family and fit-smoothness trade-off |
| Controlled smoothness / smoothness index | Guerrero (2007, 2008); Cortés-Toto et al. (2017) | Trace-based smoothness interpretation |
| CV/GCV selection of smoothing parameter | Craven & Wahba (1979); Cortés-Toto et al. (2017) | Classical smoothing-parameter selection; PLS implementation |
| Predictive CV for trend smoothness | **Hart (1994)** | One-step-ahead TSCV used to select kernel bandwidth |
| Dependence-aware CV | Burman et al.; Bergmeir & Benítez (2012) | Why time-series CV design matters |
| Rolling-origin / rolling-window evaluation | Tashman (2000); Bergmeir & Benítez (2012) | Forecast-origin, recalibration, fixed/rolling windows, horizon |
| Multiple minima in smoothing criteria | **Biessy (2025/2026)** | GCV example with two local minima |
| Numerical efficiency in WH smoothing | Weinert (2007); Biessy (2025/2026) | Structured computation and numerical parameter optimization |
| Data-driven HP parameter choice | Franke et al. (2026) | Simulation-based calibration to known trend; objective-shape discussion |
| Controlled-smoothness trend forecasting | Islas-Camargo et al. (2019); related exchange-rate work | Applied forecasting using smoothed/controlled-smoothness trends |
| Extrapolation of WH smoothing | Biessy (2025/2026) | Smoothing and extrapolation as distinct operations |
| Brent root refinement | Brent (1971) | Bracketed scalar root refinement |

---

# 15. Closest-source comparison matrix

| Source | Smoother | How smoothness is selected | Chronological predictive criterion? | Multiple minima central? | Multi-minimum numerical search? |
|---|---|---|---:|---:|---:|
| Craven & Wahba (1979) | smoothing spline | GCV | No | No | No |
| Guerrero (2007/2008) | finite-difference PLS | controlled/user-chosen smoothness | No | No | No |
| Hart (1994) | kernel trend smoother | one-step-ahead TSCV | **Yes** | No | No |
| Cortés-Toto et al. (2017) | finite-difference PLS | CV/GCV/AICc/BIC | No | No | No |
| Weinert (2007) | Whittaker--Henderson | GCV | No | No | No |
| Biessy (2025/2026) | Whittaker--Henderson | marginal likelihood/LAML; comparison with GCV | No | **Observed** | Not the target |
| Franke et al. (2026) | HP / modified HP | simulated true-trend distance | No | Discussed | No |
| Active paper | finite-difference PLS | rolling \(h\)-step forecast CV | **Yes** | **Yes** | **Yes** |

The final row is the paper's contribution **relative to the bundle**, not a
universal priority claim.

---

# 16. Practical writing rule

When describing novelty, always move through this sequence:

\[
\text{existing smoothing}
\rightarrow
\text{existing smoothing-parameter selection}
\rightarrow
\text{existing predictive TSCV}
\rightarrow
\text{existing rolling-origin evaluation}
\rightarrow
\text{known possibility of multiple minima}
\rightarrow
\boxed{\text{our multi-minimum numerical formulation and search}}.
\]

That sequence makes the novelty smaller than “forecast CV for smoothing,” but
much more defensible and technically clearer.
