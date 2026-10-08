# AI Handoff — Statistical-properties paper

## Identity

This paper is not the smoothness-CV paper.

The companion criterion paper defines
\[
\widehat S
\in
\arg\min_{S\in[0,1]}F(S).
\]

This paper takes that selection rule as given and studies
\[
\widehat\tau_{\widehat S}
=
H_{\lambda(\widehat S(y))}y.
\]

The central issue is that fixed-\(S\) PLS is a linear smoother, while the full
forecast-selected estimator is a data-adaptive nonlinear procedure.

## Known fixed-smoother foundation

For fixed \(\lambda\),
\[
\widehat\tau_\lambda=H_\lambda y,
\qquad
H_\lambda=(I+\lambda Q)^{-1}.
\]

Under \(y=\tau+\varepsilon\), \(E\varepsilon=0\), and
\(\operatorname{Var}(\varepsilon)=\Sigma\),
\[
E(\widehat\tau_\lambda)=H_\lambda\tau,
\]
\[
\operatorname{Bias}(\widehat\tau_\lambda)=(H_\lambda-I)\tau,
\]
\[
\operatorname{Var}(\widehat\tau_\lambda)
=
H_\lambda\Sigma H_\lambda^\top.
\]

Also,
\[
\operatorname{edf}(\lambda)=\operatorname{tr}(H_\lambda)
=
N-(N-d)S.
\]

These formulas are foundations and likely classical in neighboring smoothing
literatures. Do not claim them as novel.

## Primary open problems

1. Sampling/stability distribution of \(\widehat S\).
2. Effective degrees of freedom of the full adaptive estimator.
3. Bias and variance after smoothness selection.
4. Validity of fixed-\(S\) confidence intervals after selection.
5. Selection-adjusted uncertainty for level/slope/curvature.
6. Propagation of \(\widehat S\) uncertainty to forecasts.
7. Statistical meaning of multiple near-optimal minima.
8. Boundary optima and minimum switching.

## Derivatives already available

\[
\frac{\partial\widehat\tau}{\partial\lambda}
=
-H_\lambda QH_\lambda y,
\]
\[
\frac{\partial\widehat\tau}{\partial S}
=
-\frac{H_\lambda QH_\lambda y}{S'(\lambda)}.
\]

For forecasts,
\[
\frac{\partial\widehat z}{\partial S}
=
-\frac{G_{d,h}H_\lambda QH_\lambda y}{S'(\lambda)}.
\]

These may support local sensitivity or delta-method approximations around a
stable interior optimum, but do not by themselves solve post-selection
inference.

## Scope boundary

Do not re-derive the forecast-CV criterion here as the novelty. That belongs to
../paper_smoothness-cv/.

Do not focus on Brent/Sturm/root discovery here. That belongs to
../paper_numerical-methods/.

Do not claim fixed-smoother edf/bias/variance as new without a literature audit.

## Current manuscript

main.tex is the canonical draft.
