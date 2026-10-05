# Scope

## This paper owns

- scalar trend representations using Bernstein/Bézier or piecewise Bernstein/Bézier bases;
- penalties on control coefficients/control-polygon geometry;
- comparison with sampled-trend finite-difference penalties;
- terminal level/slope/curvature representation;
- endpoint-aware continuation rules;
- chronological forecast tuning for the Bézier/control representation;
- matched comparisons with P-splines, smoothing splines, finite-difference PLS, and trend filtering.

## This paper does not own

- the original idea of Bézier smoothing;
- Bernstein regression;
- P-splines;
- generic smoothing-parameter selection;
- the forecast-optimal smoothness criterion already owned by paper_smoothness-cv/;
- the adaptive numerical solver already owned by paper_numerical-methods/;
- generic financial forecasting with neural networks;
- a claim that Bézier curves are intrinsically superior.

## Important representation distinction

For scalar time-series trend estimation, prefer a graph/function representation

\[
\tau(u)=\sum_j\beta_j B_{j,K}(u)
\]

or a piecewise version with fixed temporal parameterization.

Do not casually switch to a free 2D parametric curve \((x(u),y(u))\), because then time itself becomes a fitted coordinate and the statistical problem changes.

## Stop condition

Stop or merge this project into a comparative note if a full audit shows that the proposed estimator plus continuation is exactly an existing P-spline/spline forecasting method up to a basis transformation and there is no distinct empirical or theoretical endpoint result.
