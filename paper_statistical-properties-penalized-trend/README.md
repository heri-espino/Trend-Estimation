# Statistical Properties of Penalized Trend Estimation

**Status: PARKED / future paper.**

This folder is intentionally separate from
\`paper_numerical-smoothness-selection/\`. The active numerical paper should
remain computational and applied: its contribution is the numerical selection
of forecast-optimal smoothness for fixed configurations. The material here is a
future statistical-methodology project and should not be allowed to expand the
scope of the active paper.

## Working title

**Statistical Properties and Inference for Finite-Difference Penalized Trend Estimation**

The title is provisional. No novelty claim is implied.

## Motivation

The pure finite-difference PLS estimator

\[
\widehat\tau_\lambda
=
H_\lambda y,
\qquad
H_\lambda=(I+\lambda D_d^\top D_d)^{-1},
\]

is a linear smoother. This means that many classical statistical ideas have
direct analogues:

- effective degrees of freedom;
- bias and variance;
- covariance of the fitted trend;
- leverage and influence;
- residual diagnostics;
- uncertainty for trend level, slope, and curvature;
- model-complexity criteria;
- Bayesian and state-space interpretations;
- spectral shrinkage;
- extrapolation uncertainty.

The purpose of a future paper would not be to rediscover properties already
known for Whittaker-Henderson smoothing, smoothing splines, P-splines, ridge /
Tikhonov regularization, the Hodrick-Prescott filter, or Gaussian
state-space/GMRF models. The first task must be a literature audit that separates
known results from genuinely useful extensions for the particular
forecast-selected finite-difference trend model studied in this repository.

## Immediate structural identity

For normalized smoothness \(S\),

\[
S
=
\frac{1-\operatorname{tr}(H_\lambda)/N}{1-d/N},
\]

so

\[
\boxed{
\operatorname{edf}(\lambda)
=
\operatorname{tr}(H_\lambda)
=
N-(N-d)S.
}
\]

Thus the normalized smoothness coordinate is exactly a normalized complement of
the effective degrees of freedom for the fixed-\(\lambda\) linear smoother.

This identity is algebraic and useful, but should not by itself be advertised
as a novel contribution without checking the literature.

## Research agenda

See \`notes/research_agenda.md\`.

## Literature already in this repository

The most important starting points include:

- \`literature/extracted/Guerrero_2007_time-series-smoothing-penalized-least-squares.md\`
- \`literature/extracted/Guerrero_2008_estimating-trends-percentage-smoothness.md\`
- \`literature/extracted/Biessy_2025_whittaker-henderson-smoothing-revisited.md\`
- \`literature/extracted/Biessy_2025_whittaker-henderson-smoothing-revisited-appendix.md\`
- \`literature/extracted/Golub_1979_generalized-cross-validation-ridge.md\`
- \`literature/extracted/Craven_1979_smoothing-noisy-data-spline-functions.md\`
- \`literature/extracted/Eilers_1996_flexible-smoothing-b-splines.md\`
- \`literature/extracted/Hodrick_1997_postwar-us-business-cycles.md\`

Biessy (2025) is especially important because it already treats modern
statistical properties of Whittaker-Henderson smoothing, including effective
degrees of freedom, smoothing bias, a Bayesian interpretation, credible
intervals, marginal-likelihood smoothing-parameter selection, computational
eigendecompositions, and extrapolation uncertainty. Any future paper here must
differentiate itself clearly from that work.

## Venue

Not selected. The target should be chosen only after the literature audit
clarifies whether the eventual contribution is primarily statistical
methodology, statistical computing, or applied time-series methodology.
