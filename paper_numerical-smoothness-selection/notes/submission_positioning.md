# Submission positioning — SMCCA

## Target venue

**Boletín Sociedad Mexicana de Computación Científica y sus Aplicaciones
(SMCCA), Vol. 12 (2026).**

The venue explicitly targets original research in applied mathematics and
scientific computing. This paper should therefore be presented primarily as a
**numerical method for a structured one-dimensional optimization problem**, not
as a financial forecasting paper.

## Paper question

For fixed difference order (d), rolling-window length (L), and forecast
horizon (h):

> Can forecast-optimal smoothness in finite-difference penalized least squares
> be located accurately and with substantially fewer objective evaluations
> than a dense search when the rolling forecast-validation surface contains
> multiple local minima?

The active paper does **not** ask whether PLS is the best forecasting model,
whether financial prices are predictable, or whether (d,L,S) should adapt
jointly over time.


## Zero-drift scope and forecasting interpretation

The active numerical paper deliberately studies the **pure zero-drift PLS
smoother**

[
\widehat{\tau}_{\lambda,d}
=
\arg\min_\tau
\left\{
\|y-\tau\|_2^2
+
\lambda\|D_d\tau\|_2^2
\right\},
]

which is the special case (V=I) and (mu=0) of the broader Guerrero
formulation. The manuscript must say this explicitly; it should not describe
the estimator as the full Guerrero (2007) model.

This is a modeling restriction, not merely an algebraic convenience. Setting
(mu=0) means that the (d)-th finite difference is penalized toward zero.
For the native continuation rule used in the paper, it also determines the
forecast class beyond the origin:

- (d=1): zero first difference, hence constant continuation;
- (d=2): zero second difference, hence linear continuation;
- (d=3): zero third difference, hence quadratic continuation;
- in general, (d) defines the polynomial-like null-space continuation of
  degree (d-1).

The rolling validation criterion does **not** assert that the true
(d)-th-difference mean is zero. It asks, for a fixed ((d,L,h)), which
smoothing level within this zero-drift forecasting family minimizes future
validation error. If zero drift is a poor approximation, validation may reduce
(lambda) and therefore weaken the penalty, but changing (lambda) cannot
change the continuation class itself.

This distinction matters when interpreting difference order. Increasing (d)
is not equivalent to estimating a nonzero drift (mu). It changes the
null space of the penalty and therefore the family of trends and forecasts that
are left unpenalized. Consequently:

- (d) should be interpreted as a **structural/continuation-order choice**;
- (mu) is a **drift/reference level for the (d)-th difference**;
- (lambda) controls **how strongly deviations from that reference structure
  are penalized**.

For the numerical paper, keeping (mu=0) is acceptable because the
contribution is the efficient recovery and comparison of minima of the rolling
forecast-loss surface for a clearly defined smoother. Brent refinement itself
does not require (mu=0); only the current closed-form derivative formulas are
for the zero-drift estimator. A Guerrero plug-in-drift version can therefore be
studied later as a robustness extension without changing the central numerical
question.

Do not preprocess a series solely to force the (d)-th differences to have
mean zero. If a later study needs nonzero drift, compare the zero-drift model
against the Guerrero plug-in estimator rather than using higher (d) merely to
make the mean vanish.

## Core contribution

The paper combines four pieces:

1. a normalized smoothness coordinate (S\in[0,1]) motivated by the
   controlled-smoothness literature but normalized to represent both limiting
   regimes exactly;
2. a chronological rolling future-block forecast objective;
3. analytic first and second derivatives with respect to the smoothing
   parameter, transported to the (S)-coordinate;
4. an adaptive stationary-point search with endpoint-aware refinement, Brent
   root refinement, classification of local minima, and exact evaluation of
   (S=0) and (S=1).

The contribution is the **combination and numerical treatment** of this
forecast-based selection problem. Do not claim that PLS, controlled smoothness,
rolling-origin evaluation, Brent's method, or smoothing-parameter selection are
individually new.

## State-of-the-art boundary

The closest literature in the project corpus separates into several strands:

- **Whittaker / PLS smoothing:** quadratic fidelity plus a finite-difference
  roughness penalty.
- **Guerrero controlled smoothness:** interpretable smoothness indices and
  user-chosen percentage of smoothness.
- **Cortés-Toto et al.:** CV, GCV, AICc, and BIC selection inside the PLS
  framework, followed by analysis of attained smoothness.
- **Hart (1994):** the closest conceptual predecessor. Time-series
  cross-validation chooses the bandwidth of a kernel trend smoother from
  one-step-ahead predictive performance using past data. Therefore predictive
  selection of trend smoothness is not our novelty.
- **Tashman / Bergmeir-Benítez:** chronological forecast evaluation,
  rolling-origin designs, rolling windows, recalibration, and explicit
  horizon-dependent evaluation.
- **Weinert / modern WH work:** efficient numerical computation for
  Whittaker-Henderson smoothing and smoothing-oriented criteria.
- **Biessy:** modern probabilistic WH formulation, marginal likelihood/LAML,
  numerical optimization, extrapolation, and an explicit GCV profile with
  multiple local minima. Therefore multiple minima in a smoothing criterion are
  not themselves our novelty.
- **Franke et al.:** simulation-based data-driven calibration of HP smoothing
  parameters using known synthetic trends, including discussion of
  parameter-objective geometry.

Our target is the **combination** not found in the local corpus: a
horizon-specific rolling future-block forecast objective for finite-difference
PLS, expressed in normalized smoothness space and treated as a
multiple-local-minimum numerical search problem with analytic derivatives and
exact boundary models.

## Preferred novelty sentence

> Building on predictive smoothing-parameter selection and rolling-origin
> forecast evaluation, we formulate a horizon-specific rolling forecast
> criterion for finite-difference PLS in normalized smoothness space and
> develop a numerical procedure to recover multiple relevant local minima and
> exact boundary optima efficiently.

Do not use “first” unless a later targeted literature audit establishes it.

## Primary evidence

Frozen confirmatory results:

- adversarial analytic objectives: **240/240** relevant known minima/boundary
  optima recovered;
- synthetic rolling forecast objectives: **2105/2105** dense-reference
  interior minima recovered over **1920** surfaces;
- real financial geometry stress test: **473/473** dense-reference interior
  minima recovered over **384** surfaces;
- mean evaluation fractions relative to dense search: **1.57%** synthetic and
  **1.84%** financial.

The financial panel is external geometry validation only. It is not evidence
of financial predictability or forecasting superiority.

## Claim boundaries

Safe:

- the tested forecast-validation objectives can contain multiple local minima;
- the frozen adaptive search recovered all relevant reference minima in the
  reported benchmark suites;
- exact smoothness endpoints matter empirically;
- endpoint-aware refinement is necessary in the tested upper-tail failure mode;
- evaluation counts are substantially lower than the dense references in the
  reported experiments.

Not safe:

- guaranteed recovery of every stationary point of an arbitrary smooth
  objective;
- dense grid as mathematical ground truth;
- universal superiority over GCV, marginal likelihood, AICc, BIC, or other
  smoothing criteria;
- universal speed-up independent of implementation/hardware;
- financial predictability or trading value.

## Manuscript emphasis

The paper should read as:

[
\text{PLS}
\rightarrow
S\in[0,1]
\rightarrow
\text{rolling forecast loss}
\rightarrow
\text{multiple minima}
\rightarrow
\text{adaptive numerical search}
\rightarrow
\text{controlled validation}.
]

Keep finance short. Keep the numerical mechanism, endpoint semantics,
derivatives, and controlled benchmark central.


## Canonical literature boundary

For the bundle-based citation map and the exact distinction between established
ideas and the active paper's provisional novelty, read:

`../../literature/dictionary/state_of_art_and_novelty.md`

This file is the canonical novelty reference. “Not found in the bundle” must
not be upgraded to a universal first-in-the-literature claim without a targeted
external audit.
