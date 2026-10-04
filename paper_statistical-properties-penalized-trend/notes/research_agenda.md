# Research Agenda — Statistical Properties and Inference

This is a parking document for a possible future paper. It records what can be
derived from the model, what is already standard or clearly connected to
existing smoothing literature, and which questions may be worth investigating
after the active numerical paper is finished.

The guiding rule is:

> Do not convert an algebraic property of a classical linear smoother into a
> novelty claim. First identify the corresponding result in
> Whittaker-Henderson, spline, ridge/Tikhonov, Hodrick-Prescott, Bayesian/GMRF,
> and state-space literature.

---

## 1. Base model

Start from the pure model used by the active numerical paper:

\[
\widehat\tau_\lambda
=
\arg\min_\tau
\left\{
\|y-\tau\|_2^2
+
\lambda\|D_d\tau\|_2^2
\right\},
\]

with

\[
Q=D_d^\top D_d,
\qquad
H_\lambda=(I+\lambda Q)^{-1},
\qquad
\widehat\tau_\lambda=H_\lambda y.
\]

The broader Guerrero formulation with \(V\neq I\) and/or \(\mu\neq0\) should
be treated as an extension, not silently mixed with the pure model.

---

## 2. Properties that follow immediately from the linear-smoother form

These are useful and interpretable, but most are likely classical.

### 2.1 Symmetry, positive semidefiniteness, and contraction

Since \(Q\succeq0\),

\[
H_\lambda
=
U\operatorname{diag}
\left(
\frac{1}{1+\lambda\delta_j}
\right)U^\top
\]

is symmetric positive semidefinite, with eigenvalues in \((0,1]\). Therefore

\[
\|H_\lambda x\|_2\le\|x\|_2.
\]

Increasing \(\lambda\) shrinks every penalized spectral direction.

Possible future use: characterize the regularization path through matrix order,
spectral shrinkage, condition numbers, and stability.

### 2.2 Exact reproduction of the null space

If \(x\in\ker(D_d)\), then

\[
Qx=0
\quad\Rightarrow\quad
H_\lambda x=x
\]

for every \(\lambda\).

For the standard finite-difference operator, the null space consists of
discrete polynomial sequences of degree at most \(d-1\). Thus the smoother
reproduces these components exactly.

Consequences to audit against the literature:

- \(d\ge1\): constants are preserved, so the sample sum/mean is preserved;
- \(d\ge2\): linear sequences are reproduced;
- more generally, polynomial components through degree \(d-1\) are unshrunk;
- \(\lambda\to\infty\) gives the least-squares projection onto this null space.

This is closely related to moment-preservation results in classical
Whittaker-Henderson smoothing and must not be presented as new without a
careful comparison.

### 2.3 Effective degrees of freedom

For fixed \(\lambda\),

\[
\boxed{
\operatorname{edf}(\lambda)=\operatorname{tr}(H_\lambda).
}
\]

Using the normalized smoothness coordinate,

\[
\boxed{
\operatorname{edf}
=
N-(N-d)S.
}
\]

Hence:

\[
S=0\Rightarrow \operatorname{edf}=N,
\qquad
S=1\Rightarrow \operatorname{edf}=d.
\]

This gives the most direct statistical interpretation currently available for
\(S\): it is a normalized loss of effective model flexibility.

Important caveat: after \(\lambda\) or \(S\) is selected from the data,
\(\operatorname{tr}(H_{\widehat\lambda})\) need not equal the effective degrees
of freedom of the **entire data-adaptive procedure**. Selection itself may add
complexity. That distinction is a promising future topic.

### 2.4 Influence and leverage

Because

\[
\frac{\partial\widehat\tau_i}{\partial y_j}
=
(H_\lambda)_{ij},
\]

the full matrix \(H_\lambda\) gives observation-to-fit influence.

Potential diagnostics:

- diagonal leverage \(H_{ii}\);
- row-wise influence profiles;
- boundary vs interior leverage;
- sensitivity of terminal level/slope to individual observations;
- influence on the eventual forecast
  \(G_{d,h}H_\lambda y\).

This could be especially useful for explaining outliers, endpoint behavior, and
regime changes.

---

## 3. Bias, variance, covariance, and risk

Under a simple stochastic model

\[
y=\tau+\varepsilon,
\qquad
E(\varepsilon)=0,
\qquad
\operatorname{Var}(\varepsilon)=\sigma^2I,
\]

and treating \(\lambda\) as fixed,

\[
E(\widehat\tau)=H_\lambda\tau,
\]

so the smoothing bias is

\[
\boxed{
\operatorname{Bias}(\widehat\tau)
=
(H_\lambda-I)\tau.
}
\]

Also,

\[
\boxed{
\operatorname{Var}(\widehat\tau)
=
\sigma^2H_\lambda^2.
}
\]

More generally, if

\[
\operatorname{Var}(\varepsilon)=\Sigma,
\]

then

\[
\operatorname{Var}(\widehat\tau)
=
H_\lambda\Sigma H_\lambda^\top.
\]

This leads immediately to pointwise and global bias-variance decompositions.

Future questions:

- characterize how bias and variance move monotonically with \(S\);
- study pointwise vs integrated risk;
- compare forecast-optimal \(S\) with estimation-risk-optimal \(S\);
- quantify boundary-specific bias;
- determine which results survive \(V\neq I\);
- account for \(\widehat S\) rather than pretending \(S\) is fixed.

Biessy (2025) explicitly discusses smoothing bias and Bayesian uncertainty for
Whittaker-Henderson smoothing, so the fixed-\(\lambda\) uncertainty problem is
not by itself a new contribution.

---

## 4. Inference for interpretable trend features

Rather than treating the whole fitted vector as the only target, study linear
functionals of the trend.

### Level

\[
\widehat\tau_t=e_t^\top H_\lambda y.
\]

### Local slope

\[
\widehat s_t
=
\Delta\widehat\tau_t.
\]

### Local curvature

\[
\widehat c_t
=
\Delta^2\widehat\tau_t.
\]

For any linear functional \(a^\top\widehat\tau\),

\[
\operatorname{Var}(a^\top\widehat\tau)
=
a^\top H_\lambda\Sigma H_\lambda^\top a.
\]

Possible future targets:

- standard errors for level, slope, and curvature;
- pointwise confidence/credible intervals;
- simultaneous bands;
- tests of zero local slope;
- tests of zero curvature;
- uncertainty for sign of slope;
- uncertainty for turning points;
- confidence sets for dates of trend reversals;
- uncertainty for maxima/minima of the fitted trend.

Major difficulty: smoothing bias and data-driven selection of \(S,d,L\).
Naive OLS-style p-values are not automatically valid.

A potentially useful paper would focus specifically on inference **after
forecast-based smoothness selection**, not merely inference conditional on a
fixed smoothing parameter.

---

## 5. Roughness, fit, and the regularization path

Define

\[
RSS(\lambda)=\|y-\widehat\tau_\lambda\|_2^2
\]

and

\[
R_d(\lambda)=\|D_d\widehat\tau_\lambda\|_2^2.
\]

In the spectral basis,

\[
R_d(\lambda)
=
\sum_{\delta_j>0}
\delta_j
\frac{c_j^2}{(1+\lambda\delta_j)^2},
\]

so roughness is non-increasing in \(\lambda\).

Likewise,

\[
RSS(\lambda)
=
\sum_{\delta_j>0}
\left(
\frac{\lambda\delta_j}{1+\lambda\delta_j}
\right)^2c_j^2,
\]

so in-sample residual sum of squares is non-decreasing in \(\lambda\).

Thus the entire path moves monotonically along the trade-off

\[
\text{fit}\longleftrightarrow\text{roughness}.
\]

Possible statistical/computational objects:

- exact Pareto frontier;
- L-curve interpretation;
- derivatives of fit and roughness with respect to \(S\);
- sensitivity of the frontier to \(d\);
- relation between \(S\), edf, and roughness;
- whether different \(d\) values can be compared on a common complexity scale.

This should be checked against Tikhonov/ridge/smoothing-spline literature.

---

## 6. Residuals and diagnostics

Residuals are

\[
e=(I-H_\lambda)y.
\]

Unlike the OLS hat matrix, \(H_\lambda\) is generally not idempotent:

\[
H_\lambda^2\neq H_\lambda.
\]

Therefore standard OLS residual formulas cannot simply be copied.

Questions to study:

- covariance of residuals;
- effective residual degrees of freedom;
- estimation of \(\sigma^2\) under smoothing bias;
- autocorrelation remaining after trend extraction;
- heteroskedasticity;
- standardized residuals;
- outlier/influence diagnostics;
- leave-one-out identities;
- diagnostics at boundaries;
- when residual structure indicates that \(V=I\) is inadequate.

A useful future result may be a diagnostic framework that explicitly separates
trend-model inadequacy from residual dependence.

---

## 7. Model-selection criteria and the meaning of complexity

Existing/related criteria include:

- GCV;
- AIC/AICc-type criteria;
- Mallows-\(C_p\)/SURE-style risk estimation;
- marginal likelihood / REML;
- Bayesian empirical-Bayes selection;
- chronological forecast validation.

The future question is not merely "which criterion wins?" but:

> What statistical object does each criterion optimize, and how do the selected
> trend, edf, bias, uncertainty, and forecast behavior differ?

Particularly interesting comparison:

\[
S_{\rm forecast}
\quad\text{vs}\quad
S_{\rm GCV}
\quad\text{vs}\quad
S_{\rm ML/REML}
\quad\text{vs}\quad
S_{\rm recovery}.
\]

The active numerical paper already establishes that the forecast-loss objective
can be multimodal. A later statistical paper could ask what those different
local minima mean in terms of edf, bias, roughness, and uncertainty.

---

## 8. Data-selected smoothness and post-selection inference

This is one of the strongest candidate directions because much classical
linear-smoother theory conditions on a fixed \(\lambda\), whereas this
repository deliberately selects smoothness from chronological forecast loss.

Potential questions:

- sampling distribution of \(\widehat S\);
- confidence sets for a forecast-optimal \(S^\star\);
- stability of \(\widehat S\) across rolling origins;
- effective degrees of freedom of the adaptive estimator
  \(H_{\widehat\lambda(y)}y\);
- optimism introduced by minimizing validation loss over multiple stationary
  points/configurations;
- bootstrap methods compatible with time dependence;
- selective/post-selection inference for trend level/slope after choosing
  \(S,d,L\);
- uncertainty due to local-minimum selection when the forecast-CV surface is
  multimodal.

Do not assume ordinary fixed-\(\lambda\) variance formulas remain valid after
selection.

---

## 9. Forecast uncertainty

For fixed \(d,h,\lambda\), the deterministic trend forecast is linear:

\[
\widehat z
=
G_{d,h}H_\lambda y.
\]

Thus, conditional on fixed parameters,

\[
\operatorname{Var}(\widehat z)
=
G_{d,h}H_\lambda\Sigma H_\lambda^\top G_{d,h}^\top.
\]

But that is only **estimation uncertainty in the extrapolated trend**. A full
predictive interval may also need future innovation/noise uncertainty.

Future decomposition:

\[
\text{forecast uncertainty}
=
\text{trend-estimation uncertainty}
+
\text{future observation/innovation uncertainty}
+
\text{hyperparameter-selection uncertainty}.
\]

Biessy (2025) already develops extrapolation credible intervals and explicitly
accounts for innovation error in a Whittaker-Henderson framework. Any future
work here should identify what remains different when smoothness is chosen for
forecasting and when \(d,L,S\) are selected chronologically.

---

## 10. High-order difference penalties and extrapolation stability

For the native zero-\(d\)-th-difference continuation,

\[
d=1\Rightarrow\text{constant},
\qquad
d=2\Rightarrow\text{linear},
\qquad
d=3\Rightarrow\text{quadratic},
\qquad
d=4\Rightarrow\text{cubic}.
\]

The highest-order forecast term grows as approximately

\[
O(h^{d-1}).
\]

Possible future theory:

- operator norm of \(G_{d,h}\);
- growth rate of forecast variance with \(h\) and \(d\);
- sensitivity of forecasts to terminal finite differences;
- probability/risk of explosive extrapolation;
- principled restrictions on \(d\) as a function of horizon;
- decoupling smoothing order \(d_{\rm smooth}\) from extrapolation order
  \(d_{\rm forecast}\);
- shrinkage/damping of higher-order terminal derivatives.

Biessy (2025) already notes that higher difference orders can create unstable
extrapolation and reports second-order penalties as a practical compromise.
The possible contribution here would have to be more specific, for example a
formal horizon-dependent stability analysis or a forecast-selection result.

---

## 11. Spectral/statistical interpretation

Writing

\[
c=U^\top y,
\]

the smoother acts componentwise:

\[
\widehat c_j
=
\alpha_j(\lambda)c_j,
\qquad
\alpha_j(\lambda)=\frac{1}{1+\lambda\delta_j}.
\]

Possible derived summaries:

- retained energy by spectral direction;
- suppressed energy;
- contribution of each direction to edf;
- contribution of each direction to bias and variance;
- contribution to the forecast at horizon \(h\);
- spectral explanation of why two local minima in forecast loss correspond to
  qualitatively different trend shapes.

This may provide a more interpretable analogue of regression coefficients:
there is no single slope coefficient, but there is a complete shrinkage profile
over orthogonal trend directions.

---

## 12. Equivalences and neighboring model classes to audit

Before any novelty claim, explicitly map the pure estimator to or compare it
with:

### Whittaker-Henderson smoothing

Very close to the current estimator; the weighted version replaces \(I\) in the
fit term by a weight matrix. This is likely the most direct statistical
literature.

### Hodrick-Prescott filter

The usual HP trend is a second-difference penalized least-squares problem, so it
is a special/closely related \(d=2\) case under its standard formulation.

### Tikhonov / ridge regularization

The estimator is a generalized ridge/Tikhonov problem with penalty operator
\(D_d\).

### Smoothing splines and P-splines

Closely related penalized smoothers with extensive theory for edf, GCV,
uncertainty, basis representations, and smoothing-parameter selection.

### Gaussian random walks / GMRFs / Bayesian priors

A quadratic difference penalty corresponds to a Gaussian prior/precision
structure, typically improper on the null space unless that component is
handled separately.

### State-space models

Under suitable Gaussian assumptions, difference-penalty trends have
state-space/random-walk interpretations. This connection should be derived
carefully rather than asserted loosely, especially when \(V\neq I\) or
\(\mu\neq0\).

### Demmler-Reinsch / spectral bases

The eigendecomposition used computationally is also the natural statistical
basis in which shrinkage, edf, bias, and variance decompose coordinatewise.

---

## 13. Candidate paper contributions after the literature audit

The following are **questions**, not current claims of novelty.

1. **Forecast-selected smoother inference.**
   Derive or approximate uncertainty for trend level/slope/curvature when
   \(S\) is selected by rolling forecast CV rather than fixed in advance.

2. **Selection-adjusted effective degrees of freedom.**
   Compare \(\operatorname{tr}(H_{\widehat\lambda})\) with an effective
   complexity measure for the full adaptive mapping
   \(y\mapsto H_{\widehat\lambda(y)}y\).

3. **Uncertainty of forecast-optimal smoothness.**
   Study the sampling/stability distribution of \(\widehat S\), especially
   under dependent rolling losses and multimodal validation objectives.

4. **Statistical meaning of multiple forecast-loss minima.**
   Characterize competing minima by edf, roughness, bias/variance,
   spectral content, terminal slope/curvature, and forecast geometry.

5. **Inference on trend derivatives after smoothing selection.**
   Develop intervals/tests for local slope, curvature, and turning points
   that account for smoothing bias and hyperparameter selection.

6. **Horizon-dependent extrapolation stability.**
   Formalize how the forecast operator amplifies terminal higher-order
   differences as \(d\) and \(h\) increase, and derive a statistical risk or
   stability criterion.

7. **Forecast-risk decomposition.**
   Separate estimation, future innovation, and hyperparameter-selection
   uncertainty for \(G_{d,h}H_{\widehat\lambda}y\).

8. **General covariance \(V\).**
   Extend the interpretable quantities above to Guerrero's
   \(V\neq I\) formulation and study the consequences of estimated
   heteroskedasticity/serial covariance.

9. **Common complexity scale across difference orders.**
   Determine whether edf / normalized \(S\) permits meaningful comparison
   across \(d\), and identify what remains order-specific because the null
   spaces differ.

10. **Diagnostics for adaptive trend models.**
    Build leverage, influence, residual, and boundary diagnostics that are
    appropriate for penalized trends selected for forecasting.

Any one of these could become the center of a statistical paper; the final
paper should not attempt to claim all of them.

---

## 14. What is already clearly not enough for a new paper

The following are useful to document and implement, but by themselves are
unlikely to constitute a new statistical contribution:

- \(\operatorname{edf}=\operatorname{tr}(H)\);
- fixed-\(\lambda\) bias and variance of a linear smoother;
- basic leverage from the diagonal of \(H\);
- a fixed-\(\lambda\) Gaussian credible interval;
- generic GCV/AIC calculations;
- the Bayesian interpretation of a quadratic penalty;
- the fact that \(d=2\) is related to HP/Whittaker smoothing;
- polynomial extrapolation from a difference penalty.

These should be treated as foundations and literature-connected properties.

---

## 15. Suggested future workflow

Do not begin this project until the numerical paper is substantially frozen.

When resumed:

1. perform a dedicated literature audit around Whittaker-Henderson, smoothing
   splines/P-splines, ridge/Tikhonov, HP, GMRF/Bayesian smoothing, state-space
   trends, selective inference, and data-adaptive smoother degrees of freedom;
2. make a theorem table with columns: property, already known?, exact source,
   assumptions, our extension;
3. derive all fixed-\(\lambda\) identities cleanly;
4. identify one genuinely nontrivial question involving forecast-based
   selection;
5. design simulation experiments specifically for coverage, bias, selection
   uncertainty, and dependent rolling validation;
6. only then choose a title, abstract, and statistical journal.

The likely useful distinction is:

\[
\boxed{
\text{classical fixed-smoother statistics}
\quad\text{vs}\quad
\text{statistics after forecast-driven adaptive selection}.
}
\]

That boundary should guide the future novelty search.
