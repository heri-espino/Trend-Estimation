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


## Structural behavior of the forecast-loss function

The forecast-validation objective used in this project is **not an arbitrary
smooth black-box function**. For fixed \(d\), \(L\), and \(h\), it has a
finite-dimensional rational structure inherited from the PLS smoother.

Let

\[
Q=D_d^\top D_d
=
U\operatorname{diag}(\delta_1,\ldots,\delta_L)U^\top,
\]

with \(d\) zero eigenvalues and \(r\le L-d\) distinct positive eigenvalues
\(\delta_j>0\). Then

\[
S_\lambda=(I+\lambda Q)^{-1}
\]

acts spectrally through factors

\[
\alpha_j(\lambda)=\frac{1}{1+\lambda\delta_j}.
\]

For any fixed forecast origin, the linear forecast
\(H S_\lambda y_{\rm past}\) is therefore a finite linear combination of a
constant null-space component and terms of the form

\[
\frac{c_j}{1+\lambda\delta_j}.
\]

Using the common denominator

\[
D(\lambda)=\prod_{j=1}^{r}(1+\lambda\delta_j),
\]

each forecast component, residual component, and hence the origin-specific MSE
can be written as a rational function. The pooled rolling-origin objective has
the same denominator because \(d\) and \(L\) are fixed across origins:

\[
\boxed{
f(\lambda)
=
\frac{P(\lambda)}{D(\lambda)^2}
}
\]

for some polynomial \(P\) with degree at most \(2r\), before algebraic
cancellations.

Because \(\lambda\ge0\) and every \(\delta_j>0\),

\[
1+\lambda\delta_j>0,
\]

so the admissible domain contains no poles. Consequently the objective has:

- no jumps or discontinuities;
- no finite singularities;
- no infinite accumulation of oscillations analogous to pathological examples
  such as \(x\sin(1/x)\);
- only finitely many stationary points unless the derivative degenerates
  identically.

Differentiating the rational representation gives

\[
f'(\lambda)
=
\frac{
P'(\lambda)D(\lambda)-2P(\lambda)D'(\lambda)
}{
D(\lambda)^3
}.
\]

Hence the interior stationary points are precisely the nonnegative real roots
of the polynomial numerator

\[
\boxed{
R(\lambda)
=
P'(\lambda)D(\lambda)-2P(\lambda)D'(\lambda),
}
\]

provided \(R\not\equiv0\). Since
\(\deg(P)\le2r\) and \(\deg(D)=r\), a crude algebraic bound is

\[
\deg(R)\le 3r-1
\le
3(L-d)-1.
\]

Thus the number of isolated interior stationary points is finite and
algebraically bounded for each fixed configuration. This is a much stronger
description than merely saying that the objective is smooth.

The normalized smoothness change of variable does not create additional
interior stationary points. Since \(S'(\lambda)>0\),

\[
F'(S)=0
\iff
f'(\lambda)=0.
\]

### Consequence for the search algorithm

The current adaptive-Brent method should therefore be interpreted as exploiting
a **structured rational objective**, not as attempting global optimization of
an arbitrary smooth function.

Brent still does not by itself discover every root. The current implementation
first samples/adaptively refines the derivative, brackets sign changes, and then
uses Brent for accurate refinement. Multiple roots or even-multiplicity roots
of \(R\) need not produce a derivative sign change, so empirical discovery is
not yet a mathematical certification of exhaustive root recovery.

However, the rational structure suggests a stronger future extension:
construct or otherwise characterize \(R(\lambda)\), isolate all of its
nonnegative real roots using a certified polynomial-root method (for example,
Sturm-sequence/root-isolation techniques), and use Brent only to refine the
isolated roots numerically. Such an extension could potentially convert the
current empirical recovery statement into an exhaustive fixed-configuration
stationary-point result, subject to a formal derivation and numerically stable
implementation.

For the current paper, treat this rational representation and the finite-root
property as an important structural observation. Do **not** claim a certified
root-isolation theorem until the polynomial representation, degeneracies,
multiplicities, and numerical conditioning have been formally checked in the
implementation.

## Important limitation

For the structured rational objective above, the number of stationary points is finite and algebraically bounded. The remaining limitation is therefore not pathological infinite oscillation, but **root discovery by the finite sampler**. In particular, a sign-change scan can still miss:

- two or more roots inside the same sampled interval;
- an even-multiplicity stationary root where the derivative touches zero without changing sign;
- a sufficiently narrow pair of extrema between sampled points.

Therefore the current root-based search is validated against dense diagnostic references and uses adaptive refinement where the derivative or curvature indicates unresolved structure.

The paper should not say that Brent itself "finds all roots." Brent robustly refines a root **after it has been bracketed**. The stronger finite-rational structure should be stated explicitly, while exhaustive certification should be reserved for a future root-isolation implementation or a formal proof that the present sampler detects every admissible root pattern.

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
