# Concept Dictionary

This file defines the concepts that should remain stable across the active
numerical paper and its supporting notes.

## Core trend-estimation concepts

### Trend / trend component

**Preferred term:** *trend* or *trend component*.

A smooth underlying component used to represent the long-term or slowly varying
behavior of an observed time series. The literature also uses *signal* in the
unobserved-components interpretation.

Use *trend* by default. Use *signal* only when discussing the statistical
signal/noise interpretation explicitly.

**Source anchors:** Guerrero (2007); Guerrero (2008); Cortés-Toto et al. (2017).

---

### Penalized least squares (PLS)

**Preferred term:** *penalized least squares (PLS)*.

The estimator balances fidelity to the observations against a penalty for lack
of smoothness. In the notation of the active paper,

\[
\widehat\tau_\lambda
=
\arg\min_\tau
\left\{
\|y-\tau\|_2^2
+
\lambda\|D_d\tau\|_2^2
\right\}.
\]

The corresponding closed form is

\[
\widehat\tau_\lambda
=
(I+\lambda D_d^\top D_d)^{-1}y.
\]

Do not call this estimator *trend filtering* without qualification: in modern
statistics that phrase often refers to the \(\ell_1\)-penalized trend-filtering
literature.

**Source anchors:** Whittaker (1923); Guerrero (2007); Cortés-Toto et al. (2017);
Biessy (2025).

---

### Fidelity criterion

**Preferred term:** *fidelity to the data*, *fidelity criterion*, or *data-fit
term*.

The squared-error component

\[
\|y-\tau\|_2^2
\]

measures agreement between the fitted trend and the observed series.

The phrase *fidelity criterion* is especially consistent with the modern
Whittaker-Henderson literature.

---

### Smoothness criterion / roughness penalty

**Preferred terms:** *smoothness criterion*, *penalty for lack of smoothness*,
or *roughness penalty*.

For finite-difference PLS,

\[
\|D_d\tau\|_2^2
\]

penalizes variation in the \(d\)-th differences of the trend.

Use *penalty for lack of smoothness* when explaining the model intuitively;
use *roughness penalty* or *smoothness criterion* in technical sections.

---

### Smoothing parameter \(\lambda\)

**Preferred term:** *smoothing parameter*.

\(\lambda\ge0\) controls the trade-off between goodness of fit and trend
smoothness.

- \(\lambda\to0\): the trend approaches the observed series;
- \(\lambda\to\infty\): smoothness dominates and the trend approaches the
  null space implied by the difference penalty.

The literature also uses *smoothing constant*. Use *smoothing parameter*
consistently in the active paper.

*Penalty parameter* is acceptable when discussing numerical optimization, but
it is not the default manuscript term.

**Statistical interpretation:** under the unobserved-components formulation,
\(\lambda\) can be interpreted as a variance ratio. This is an interpretation
of the statistical model, not the definition required by the deterministic PLS
problem.

**Source anchors:** Guerrero (2007); Cortés-Toto et al. (2017).

---

### Difference order \(d\)

**Preferred term:** *difference order* or *order of the difference penalty*.

\(D_d\) denotes the matrix representation of the \(d\)-th finite-difference
operator.

The order is a structural modeling choice, distinct from the smoothing
parameter.

For the quadratic PLS formulation, the nullity of
\(D_d^\top D_d\) is exactly \(d\).

---

### Smoother matrix

**Preferred term:** *smoother matrix* or *smoothing matrix*.

The literature commonly denotes

\[
(I+\lambda D_d^\top D_d)^{-1}
\]

as a smoothing matrix.

**Notation rule for this project:** do **not** denote this matrix by
\(S_\lambda\) in the active paper because \(S\) is reserved for normalized
smoothness. Prefer \(H_\lambda\) for the matrix if a symbol is required:

\[
H_\lambda=(I+\lambda D_d^\top D_d)^{-1}.
\]

This notation choice is project-specific and exists only to avoid a collision
with the smoothness coordinate.

---

### Null space of the difference penalty

**Preferred term:** *null space of \(D_d\)* or *null space of the penalty*.

As \(\lambda\to\infty\), penalized components vanish and the fitted trend
approaches the component lying in the null space of \(D_d\).

For the standard finite-difference penalty this yields polynomial-like
behavior: constant for \(d=1\), linear for \(d=2\), and the corresponding
higher-order discrete polynomial structure for larger \(d\).

This concept is important for the exact \(S=1\) endpoint.

---

## Smoothness concepts

### Controlled smoothness approach

**Preferred term:** *controlled smoothness approach*.

The literature uses this phrase for choosing the smoothing parameter indirectly
by first fixing a desired amount or percentage of smoothness and then solving
for the corresponding \(\lambda\).

Do not use *controlled smoothing* as the default name when referring to the
Guerrero line of work; *controlled smoothness* is the established phrase in the
project corpus.

**Source anchors:** Guerrero (2007, 2008); Cortés-Toto et al. (2017).

---

### Smoothness index

**Preferred term:** *smoothness index*.

In the Guerrero/Cortés-Toto literature, a trace-based index connects
\(\lambda\), sample size, and the smoothing matrix, and is interpreted through
relative precision.

A commonly written form is

\[
S_d(\lambda;N)
=
1-
\frac{\operatorname{tr}\{(I+\lambda D_d^\top D_d)^{-1}\}}{N}.
\]

The precise finite-sample endpoint convention differs across presentations in
the literature, so the active paper should state its own normalization
explicitly instead of treating every historical \(S_d\) as identical.

**Source anchors:** Guerrero (2007, 2008); Cortés-Toto et al. (2017).

---

### Percentage of smoothness

**Preferred term:** *percentage of smoothness* only when discussing the
controlled-smoothness literature or an explicitly percentage-scaled index.

It is the literature's interpretation of a smoothness index in percentage
terms.

**Important:** do not automatically call the active paper's normalized
\(S\in[0,1]\) a *percentage of smoothness*. The paper uses a normalized
coordinate designed to have exact endpoints 0 and 1.

---

### Normalized smoothness coordinate \(S\)

**Project-specific preferred term:** *normalized smoothness coordinate*.

Also acceptable after first definition: *normalized smoothness*.

For the active numerical paper,

\[
S(\lambda)
=
1-
\frac{1}{N-d}
\sum_{j=1}^{N-d}
\frac{1}{1+\lambda\delta_j},
\]

where \(\delta_j>0\) are the positive eigenvalues of
\(D_d^\top D_d\).

This normalization gives

\[
S(0)=0,
\qquad
S(\lambda)\to1
\quad\text{as}\quad
\lambda\to\infty.
\]

The term *coordinate* is useful because the numerical contribution is a change
of optimization coordinate from the unbounded \(\lambda\)-domain to the
compact interval \([0,1]\).

Do not imply that this exact normalization is the original Guerrero index.

---

### Effective degrees of freedom

**Preferred term:** *effective degrees of freedom*.

For a linear smoother, trace-based quantities such as
\(\operatorname{tr}(H_\lambda)\) summarize the effective model dimension and
appear in GCV and information-criterion formulations.

Do not use simply *degrees of freedom* when the trace of a smoother is meant if
there is any risk of confusing it with literal sample-size differences such as
\(N-d\).

**Source anchors:** Craven and Wahba (1979); Golub et al. (1979);
Cortés-Toto et al. (2017); Biessy (2025).

---

## Forecast-validation concepts

### Forecast origin

**Preferred term:** *forecast origin*.

The last time point whose information is available when a forecast is issued.

If the available sample ends at \(T\), then \(T\) is the forecast origin for
predictions of \(T+h\).

**Source anchors:** Tashman (2000); Bergmeir and Benítez (2012).

---

### Forecast horizon \(h\)

**Preferred term:** *forecast horizon*.

The number of steps between the forecast origin and the target being evaluated.

Use *\(h\)-step-ahead forecast* when referring to a fixed horizon.

Do not average different horizons without making the aggregation explicit:
forecast errors at different horizons have different properties.

---

### Rolling-origin evaluation

**Preferred umbrella term:** *rolling-origin evaluation*.

The forecast origin advances sequentially through time.

If the model is re-estimated at every origin, call the design
*rolling-origin recalibration* or say explicitly that the model is refit at
each origin.

If the training sample retains constant length by dropping old observations,
call it *rolling-window evaluation*.

The active numerical benchmark with fixed \(L\) should be described as a
**rolling-window, rolling-origin forecast-validation design**.

**Source anchors:** Tashman (2000); Bergmeir and Benítez (2012).

---

### Rolling forecast-validation objective

**Project-specific preferred term:** *rolling forecast-validation objective*.

For fixed \((d,L,h)\), define

\[
F_{d,L,h}(S)=CV_h(d,L,S),
\]

where the loss is computed from genuinely future \(h\)-step forecasts at
chronological forecast origins.

Use this phrase rather than plain *cross-validation objective* when the
chronological forecasting structure matters.

This is distinct from ordinary leave-one-out CV or GCV used to assess
in-sample smoothing/reconstruction.

---

### Out-of-sample forecast evaluation

**Preferred term:** *out-of-sample forecast evaluation* when discussing the
general evaluation principle.

Use *rolling-origin* or *rolling-window* when describing the actual protocol.

Do not use *out-of-sample* for observations that were used, directly or
indirectly, to select the same forecast being scored.

---

### Trend forecasting / extrapolation

**Preferred terms:** *trend forecasting* and *trend extrapolation*.

The literature explicitly distinguishes estimation of the historical trend
from extrapolation beyond the observed sample.

In this project, the active numerical paper fixes the continuation rule to the
native finite-difference continuation. Do not mix this with the separate
smoothing operation.

**Source anchors:** Guerrero (2007, 2008); Biessy (2025).

---

## Numerical-search concepts

### Stationary point

**Preferred term:** *stationary point*.

A point where the derivative of the scalar objective with respect to the search
coordinate is zero.

A stationary point can be a local minimum, local maximum, or a flatter
stationary feature. Do not use *stationary point* as a synonym for *minimum*.

---

### Local minimum

**Preferred term:** *local minimum*.

The primary numerical target of the active paper, together with exact boundary
optima.

The paper does not claim certified recovery of every stationary root of an
arbitrary smooth objective.

---

### Multiple local minima

**Preferred term:** *multiple local minima* or *multi-minimum objective*.

Use *multimodal objective* sparingly and only when the meaning is obvious.
*Multiple local minima* is less ambiguous.

---

### Derivative root / root bracket

**Preferred terms:** *root of the derivative*, *sign-change bracket*, and
*bracketed root*.

The adaptive algorithm samples the derivative, identifies intervals that may
contain derivative roots, and refines sign-change brackets with a bracketing
root solver.

---

### Brent's method

**Preferred term:** *Brent's method* or *Brent root refinement*.

Use it for the bracketed scalar root-refinement stage. Do not describe the
entire adaptive algorithm as *Brent optimization*: Brent's method is only the
root-refinement component.

**Source anchor:** Brent (1971).

---

### Endpoint-aware refinement

**Project-specific preferred term:** *endpoint-aware refinement*.

A deterministic refinement of the first and last cells of the normalized
smoothness domain, introduced because the compact transformation can compress
objective structure near \(S=0\) and especially \(S=1\).

Always qualify which endpoint is meant; see the endpoint terminology below.

---

### Dense reference grid

**Preferred term:** *dense reference grid* or *dense-grid reference*.

A fine grid used to benchmark the adaptive method.

Do **not** call it *ground truth* or an *exact optimum*: it remains a discrete
reference approximation to the continuous objective.

---

### Objective regret

**Project-specific preferred term:** *objective regret*.

For an adaptive choice \(\widehat S\) and dense-reference choice
\(S_{\mathrm{ref}}\),

\[
\operatorname{regret}
=
F(\widehat S)-F(S_{\mathrm{ref}}).
\]

Negative values can occur when continuous root refinement locates a lower
objective value between dense-grid points. Therefore report *positive regret*
when counting meaningful failures against a dense reference.

---

### Missed minimum

**Preferred term:** *missed local minimum* or *missed reference minimum*.

A dense-reference local minimum for which no adaptive minimum lies within the
pre-specified matching tolerance.

Use *missed* rather than *undetected* when reporting benchmark counts; reserve
*detection* for the algorithmic procedure.

---

## Endpoint terminology

### Time-series endpoint

**Preferred term:** *time-series endpoint*, *sample endpoint*, or *end of the
sample*.

This refers to the first or last observations in the temporal sample and to the
well-known boundary behavior of two-sided smoothers.

**Source anchors:** Guerrero (2007); Mise et al. (2005).

---

### Smoothness-domain endpoint

**Preferred term:** *smoothness-domain endpoint* or *parameter-domain endpoint*.

This refers to \(S=0\) or \(S=1\).

Use *lower smoothness endpoint* and *upper smoothness endpoint* when needed.

Never write merely *endpoint problem* when the reader could confuse temporal
endpoints with \(S=0,1\).

---

## Related literature concepts

### Whittaker-Henderson smoothing

**Preferred term:** *Whittaker-Henderson (WH) smoothing* when discussing the
actuarial/general smoothing lineage.

Modern treatments describe WH smoothing as a fidelity criterion plus a
finite-difference smoothness criterion and connect it to penalized likelihood,
Bayesian interpretation, marginal likelihood, and extrapolation.

The active paper may mention WH smoothing as the broader historical/statistical
family, while using PLS for the specific time-series formulation.

**Source anchor:** Biessy (2025).

---

### Generalized cross-validation (GCV)

**Preferred term:** *generalized cross-validation (GCV)*.

A classical data-driven smoothing-parameter selection criterion based on a
linear smoother and its effective degrees of freedom.

Do not conflate GCV with the active paper's chronological rolling forecast
validation.

**Source anchors:** Craven and Wahba (1979); Golub et al. (1979);
Cortés-Toto et al. (2017).

---

### Marginal likelihood / LAML

**Preferred terms:** *marginal likelihood* and *Laplace approximation of the
marginal likelihood (LAML)*.

These are modern smoothing-parameter selection approaches in probabilistic or
penalized-likelihood formulations.

They are useful comparison points in the literature review, but they are not
the numerical objective optimized in the active paper.

**Source anchor:** Biessy (2025).
