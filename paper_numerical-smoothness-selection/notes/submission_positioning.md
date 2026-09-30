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
- **Weinert / modern WH work:** efficient numerical computation for
  Whittaker-Henderson smoothing and smoothing-oriented criteria.
- **Biessy:** modern probabilistic WH formulation, marginal likelihood/LAML,
  numerical optimization, extrapolation, and an explicit example of a GCV
  profile with multiple local minima.
- **Franke et al.:** simulation-based data-driven calibration of HP smoothing
  parameters using known synthetic trends.
- **Tashman / Bergmeir-Benítez:** chronological forecast evaluation,
  rolling-origin designs, rolling windows, and recalibration.

Our target differs because the scalar objective is **rolling future forecast
loss**, not reconstruction CV/GCV, information criteria, marginal likelihood,
or user-fixed smoothness.

## Preferred novelty sentence

> We formulate smoothing-parameter selection as a horizon-specific rolling
> forecast optimization problem in normalized smoothness space and develop a
> numerical procedure to recover multiple relevant local minima efficiently.

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
