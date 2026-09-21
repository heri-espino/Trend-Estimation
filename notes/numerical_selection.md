# Numerical Selection of Forecast-Optimal Smoothness

## Question

The validation/forecast objective can contain several local extrema. How should we find a global optimum without assuming unimodality?

## Why not rely on golden-section minimization?

Golden-section search is a local one-dimensional minimizer that is most useful when the objective is unimodal on the supplied interval. If the validation curve contains several local minima, a single global golden-section call can converge to the wrong basin or rely on an assumption we have not established.

A dense grid can reveal the global shape, but using the grid itself as the final optimizer is inefficient and makes the selected value depend on grid resolution.

## Work in log-lambda

Let

\[
\theta=\log\lambda,
\qquad
\lambda=e^\theta,
\qquad
g(\theta)=CV(e^\theta).
\]

Then

\[
g'(\theta)=\lambda CV'(\lambda).
\]

Because \(\lambda>0\),

\[
g'(\theta)=0
\iff
CV'(\lambda)=0.
\]

Log space is natural because useful penalties commonly span many orders of magnitude and positivity is automatic.

## Intended algorithm

Choose a bounded search interval

\[
\theta\in[\theta_{\min},\theta_{\max}].
\]

Then:

1. evaluate \(g'(\theta)\) on a coarse diagnostic grid;
2. whenever adjacent values change sign, bracket a root;
3. solve each bracket with Brent's root method;
4. deduplicate roots that were bracketed twice;
5. classify each root using local derivative signs or \(g''\);
6. evaluate the original objective at every local minimum;
7. also evaluate both domain boundaries;
8. choose the smallest objective value among these candidates.

Symbolically,

\[
\boxed{
\text{scan}
\to
\text{bracket}
\to
\text{Brent root}
\to
\text{classify}
\to
\text{global comparison}.
}
\]

## Classification

At an interior stationary point,

\[
CV'(\lambda^\star)=0.
\]

A practical classification is:

- \(CV''(\lambda^\star)>0\): local minimum;
- \(CV''(\lambda^\star)<0\): local maximum;
- curvature near zero: flat/degenerate stationary point requiring additional inspection.

Equivalently, inspect the sign of the first derivative on both sides:

\[
-\to+ \quad\Rightarrow\quad \text{minimum},
\]

\[
+\to- \quad\Rightarrow\quad \text{maximum}.
\]

## Newton's method

Newton in log space uses

\[
\theta_{k+1}
=
\theta_k-
\frac{g'(\theta_k)}{g''(\theta_k)}
=
\theta_k-
\frac{CV'(\lambda)}
{CV'(\lambda)+\lambda CV''(\lambda)}.
\]

This is useful for refinement and as a computational benchmark. It is not sufficient as the only global search because the result depends on initialization when several stationary points exist.

## Important limitation

A finite sign-change scan cannot mathematically guarantee discovery of every stationary point of an arbitrary smooth function. In particular, it can miss:

- two roots inside the same coarse interval;
- a root where the derivative touches zero without changing sign;
- an extremely narrow feature between grid points.

Therefore the root-based search must be validated against dense diagnostic scans on simulations, and the grid should be adaptively refinable where the derivative varies sharply or is close to zero.

This limitation should be stated in the paper rather than claiming that Brent itself "finds all roots." Brent robustly solves a root **after it has been bracketed**.

## Library mapping

- existing bounded minimization and Newton:
  `src/trend_estimation/selection/numerical.py`
- bracketed stationary-point search:
  `src/trend_estimation/selection/numerical.py::find_stationary_points_log_lambda`
- forecast objective and derivatives:
  `src/trend_estimation/forecasting/objectives.py`
- rolling origins:
  `src/trend_estimation/validation/rolling_origin.py`

## Paper comparison

The numerical experiment should compare at least:

- fixed/dense grid search;
- bounded scalar minimization in log-\(\lambda\);
- derivative-root Brent search;
- Newton in log-\(\lambda\).

Record:

- selected \(\lambda\) and normalized smoothness;
- objective gap relative to the best verified candidate;
- number of objective/derivative evaluations;
- runtime;
- failure or boundary cases;
- number and type of stationary points found.

The purpose is not to claim that root solving is automatically faster in every setting, but to determine when analytic derivative information gives a more reliable or efficient selection procedure.
