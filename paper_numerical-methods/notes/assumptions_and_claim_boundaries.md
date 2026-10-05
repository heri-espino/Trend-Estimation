# Assumptions and Claim Boundaries — Numerical Smoothness-Selection Paper

Date added: 2026-10-03

This note separates **model assumptions**, **forecast-validation assumptions**,
**numerical-search assumptions**, and **claim boundaries** for the active SMCCA
paper. Future manuscript edits should preserve these distinctions.

## 1. Model actually studied

The active paper studies the pure finite-difference penalized least-squares
estimator

[
widehat{	au}_{lambda,d}
=
argmin_{	au}
left{
|y-	au|_2^2
+
lambda|D_d	au|_2^2
ight},
qquad
lambdage 0.
]

Relative to the broader Guerrero formulation, this is the special case

[
V=I,
qquad
mu=0.
]

These are genuine modeling restrictions, not merely algebraic shorthand.

### Assumption A1 — identity observation weighting: (V=I)

Under Guerrero's stochastic interpretation,

[
operatorname{Var}(eta)=sigma_Z^2 I.
]

This means equal marginal observation-error variance and zero covariance across
different time indices. It does **not** by itself imply statistical independence;
independence follows only under additional distributional assumptions such as
joint Gaussianity.

In the active numerical paper, (V=I) can also be read more modestly as an
unweighted Euclidean data-fit criterion. The numerical algorithm and derivative
identities do not require a Gaussian observation model.

Consequences:

- heteroskedasticity is not explicitly weighted;
- serial correlation in observation error is not explicitly modeled through
  (V);
- if such structure is present, the selected smoother may absorb some of it.

Do not claim that the paper estimates or corrects a general covariance matrix.

### Assumption A2 — zero drift in the penalized difference: (mu=0)

The penalty is centered at zero:

[
D_d	au approx 0.
]

Under a stochastic trend interpretation, this corresponds to centering the
(d)-th difference around zero. In the optimization-only interpretation, it is
simply the structural target of the regularizer; it need not be asserted as a
literal truth about the data-generating process.

This assumption fixes the native continuation family:

- (d=1): constant continuation;
- (d=2): linear continuation;
- (d=3): quadratic continuation;
- generally: polynomial-like continuation of degree (d-1).

Changing (lambda) can weaken or strengthen the penalty but cannot turn the
zero-drift continuation into the nonzero-drift Guerrero continuation.

### Assumption A3 — regular temporal indexing for finite differences

The standard finite-difference operator (D_d) treats adjacent indices as
equally spaced units. Therefore the direct interpretation of (D_d) as a time
difference assumes regularly spaced observations, or that the analyst has
already mapped observations to an appropriate regular index.

For irregular observation times, the current (D_d) is not automatically a
correct divided-difference operator.

### Assumption A4 — fixed (d,L,h) for the numerical optimization problem

The active numerical paper conditions on

[
(d,L,h)
]

and optimizes only smoothness:

[
S^star
in
argmin_{Sin[0,1]}
F_{d,L,h}(S).
]

Thus "forecast-optimal smoothness" means optimal **within the specified
zero-drift PLS family and the specified validation protocol**, not globally
optimal over all trend models, all window lengths, all orders, or all horizons.

The broader repository may treat (d,L), selector memory, and split sizes as
hyperparameters, but that is outside the narrow numerical claim of this paper.

### Assumption A5 — native zero-(d)-th-difference extrapolation

Forecasting is not produced by the smoother alone. The paper fixes a
continuation operator (G_{d,h}) that imposes zero (d)-th finite difference
beyond the forecast origin.

Therefore conclusions about forecast loss are conditional on this continuation
rule. Another extrapolator could produce a different objective surface and a
different selected smoothness.

## 2. Forecast-validation assumptions

### Assumption V1 — chronology is respected

At each forecast origin, only observations available by that origin are used.
Future blocks are used for validation only after the candidate is fitted.

This prevents look-ahead leakage.

### Assumption V2 — past forecast performance is informative for the target future

Chronological CV does not require global stationarity as a theorem, but using
past rolling forecast losses to choose a future configuration implicitly assumes
some degree of local persistence in the predictive environment.

If the data-generating regime changes sharply between validation and test,
validation-optimal smoothness need not remain test-optimal.

The paper already contains development/test rank reversals; these should be
presented as evidence of this limitation, not hidden.

### Assumption V3 — the loss function defines the meaning of "optimal"

The active objective is mean squared forecast error,

[
f_T(lambda)=rac1h|r_T(lambda)|_2^2.
]

For a fixed number of forecast errors, minimizing RMSE and minimizing MSE gives
the same minimizer because the square root is monotone. However, the analytic
derivatives in the paper are derivatives of the MSE objective.

Therefore manuscript wording should use **MSE** for the differentiated
criterion unless RMSE is explicitly introduced only as an equivalent reporting
scale.

### Assumption V4 — rolling losses are not independent observations

Overlapping training windows and overlapping future blocks induce dependence
between origin-specific losses. This does not invalidate their average as a
selection criterion, but it means naive i.i.d. standard errors or classical
independent-sample inference are not justified.

The current paper is primarily numerical and does not claim i.i.d.-based
statistical inference from rolling-origin losses.

### Assumption V5 — split sizes and origin design are part of the procedure

Window length, number of validation origins, spacing between origins, and
development/test block sizes affect the objective being optimized. They are not
innocent bookkeeping choices.

Claims should therefore be conditional on the stated protocol. In broader
ML-style work, these quantities may be treated as assumption-informed protocol
hyperparameters inside a properly nested design; an untouched outer test block
must not be tuned after inspection.

## 3. Numerical-search assumptions and limits

### Assumption N1 — one-dimensional smooth objective for fixed configuration

For fixed (d,L,h), the algorithm searches a scalar smoothness coordinate
(Sin[0,1]). Analytic derivatives follow from the closed-form linear smoother.

The method does not directly solve a high-dimensional joint
((d,L,S,ldots)) optimization problem.

### Assumption N2 — Brent is a refinement tool, not a global optimizer

Brent root refinement is applied after the adaptive procedure has bracketed a
derivative sign change. Brent does not by itself discover all stationary points.

The adaptive sampler, endpoint refinement, derivative/curvature diagnostics,
and exact endpoint checks are what turn local root refinement into the full
search procedure.

### Assumption N3 — structured finite-root objective, but no sampler certification yet

For fixed (d,L,h), the forecast-MSE objective is not an arbitrary smooth
function. It is a rational function of (lambda) with no poles on
(lambdage0), and its stationary points are roots of a finite-degree
polynomial numerator (except for degenerate cases). Thus pathological infinite
oscillation is not a relevant concern.

The remaining limitation is algorithmic: the current finite adaptive sampler
does not yet constitute a formal root-isolation proof. It can in principle miss
multiple roots inside one unresolved interval or an even-multiplicity root that
does not create a sign change.

Therefore the paper may report empirical recovery on the frozen benchmark
suite and may exploit the finite rational structure, but it should not claim
certified exhaustive stationary-point recovery until a formal isolation
argument or implementation is added.

### Assumption N4 — endpoint models are part of the candidate set

(S=0) and (S=1) are evaluated exactly, with (S=1) represented by the
null-space limit rather than by a large finite (lambda).

This is important because an optimum may occur at a boundary.

### Assumption N5 — dense grids are references, not truth

The synthetic and financial dense grids are numerical reference searches.
Except for adversarial analytic cases with known structure, they are not
mathematical ground truth.

Use wording such as "dense-reference minima" rather than "true minima."

## 4. Distributional assumptions we do *not* need for the numerical paper

The core optimization and derivative method does **not** require:

- Gaussian observation noise;
- independent observation errors;
- a correct probabilistic likelihood;
- that (lambda=sigma_Z^2/sigma_arepsilon^2);
- that the latent trend literally follows Guerrero's stochastic model.

Those statements become relevant only if we invoke the stronger statistical
interpretation of the PLS estimator.

If we claim the Guerrero variance-ratio interpretation

[
lambda=sigma_Z^2/sigma_arepsilon^2,
]

then we must state the associated stochastic assumptions instead of presenting
that identity as universally valid for any penalized smoother.

## 5. What the active paper can say

Supported wording:

- We study the zero-drift, identity-weighted finite-difference PLS smoother.
- For fixed (d,L,h), the chronological forecast-MSE surface can be
  multimodal.
- The proposed derivative-aware search recovered all relevant reference minima
  in the reported frozen benchmark suites.
- Exact smoothness endpoints can matter and should be compared explicitly.
- The method used substantially fewer objective evaluations than the stated
  dense references in the reported experiments.
- The selected (S^star) is forecast-optimal **relative to the chosen model
  family, loss, horizon, window, and validation design**.
- Multimodality is configuration-dependent, not universal.

## 6. What the active paper must not say

Do not claim:

- that (mu=0) or (V=I) is empirically true for all studied series;
- that observation errors are independent merely because (V=I);
- that the method estimates a general covariance structure;
- that the selected trend is the "true trend";
- that forecast-optimal smoothness is recovery-optimal smoothness;
- that the selected (S^star) is population-optimal outside the stated
  validation protocol;
- that Brent's method guarantees global optimization;
- that every stationary point of every smooth objective is recovered;
- that a dense grid provides mathematical truth;
- that the method universally outperforms GCV, AICc, BIC, marginal likelihood,
  or other smoothness selectors;
- that the financial geometry stress test establishes financial
  predictability, economic value, or trading profitability;
- that the current numerical paper jointly learns (d,L,S);
- causal interpretations of the selected hyperparameters or trend.

## 7. Recommended manuscript language

A concise rigorous description is:

> We study the zero-drift, identity-weighted special case of
> finite-difference penalized least squares. The identity weighting corresponds
> to an unweighted Euclidean data-fit criterion and, under a stochastic-error
> interpretation, to equal marginal observation-error variance with zero
> cross-time covariance. The zero-drift penalty centers the (d)-th finite
> difference at zero. These are modeling choices rather than empirically
> asserted truths. For fixed difference order, estimation-window length, and
> forecast horizon, we select smoothness by chronological future-block MSE and
> study the numerical problem of recovering all relevant minima of that
> one-dimensional objective.

This paragraph should appear in or immediately after the PLS model subsection
of the final manuscript.
