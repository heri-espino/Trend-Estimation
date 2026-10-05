# Statistical Properties of Forecast-Selected Penalized Trend Estimators

**Status: DRAFTING / theory agenda active; novelty audit not yet complete.**

This paper is separate from paper_smoothness-cv/ and paper_numerical-methods/.

## The three-paper distinction

\[
\text{smoothness-CV: } y\rightarrow\widehat S
\]

\[
\text{numerical methods: solve the argmin defining }\widehat S
\]

\[
\text{this paper: }(y,\widehat S)
\rightarrow
\widehat\tau_{\widehat S}
\rightarrow
\text{bias, variance, complexity, and uncertainty}
\]

The smoothness-CV paper asks which smoothness level should be selected for
forecasting. This paper asks what happens statistically after that smoothness
level has been selected from the data.

## Core distinction

For fixed \(\lambda\),
\[
\widehat\tau_\lambda
=
H_\lambda y,
\qquad
H_\lambda=(I+\lambda D_d^\top D_d)^{-1},
\]
is a linear smoother.

After chronological forecast-CV selection,
\[
\widehat S=\arg\min_S F(S),
\]
and the actual estimator is
\[
\boxed{
\widehat\tau_{\widehat S}
=
H_{\lambda(\widehat S(y))}y.
}
\]

The full mapping is data-adaptive and generally nonlinear in \(y\).

## What we already know

For fixed smoothness, under
\[
y=\tau+\varepsilon,\qquad
E(\varepsilon)=0,\qquad
\operatorname{Var}(\varepsilon)=\Sigma,
\]
\[
E(\widehat\tau_\lambda)=H_\lambda\tau,
\]
\[
\operatorname{Bias}(\widehat\tau_\lambda)
=
(H_\lambda-I)\tau,
\]
\[
\operatorname{Var}(\widehat\tau_\lambda)
=
H_\lambda\Sigma H_\lambda^\top.
\]

Also,
\[
\boxed{
\operatorname{edf}(\lambda)
=
\operatorname{tr}(H_\lambda)
=
N-(N-d)S.
}
\]

For a fixed forecast operator,
\[
\widehat z_\lambda=G_{d,h}H_\lambda y,
\]
and
\[
\operatorname{Var}(\widehat z_\lambda)
=
G_{d,h}H_\lambda\Sigma H_\lambda^\top G_{d,h}^\top.
\]

These are foundations, not novelty claims.

## What we want to know

The main open questions are:

- sampling distribution and stability of \(\widehat S\);
- selection-adjusted effective degrees of freedom;
- bias and variance of \(H_{\lambda(\widehat S)}y\);
- valid uncertainty for level, slope, curvature, and turning points after
  smoothness selection;
- propagation of smoothness-selection uncertainty into forecasts;
- statistical meaning of multimodal forecast-CV surfaces;
- whether local delta-method approximations work around stable interior minima;
- what replaces them near boundaries or minimum switching.

## What is explicitly not enough for a paper

By themselves, the following are likely classical:

- \(\operatorname{edf}=\operatorname{tr}(H)\);
- fixed-\(\lambda\) bias/variance;
- leverage from \(H_{ii}\);
- fixed-\(\lambda\) Gaussian intervals;
- Bayesian interpretation of a quadratic penalty;
- relationships with Whittaker-Henderson, HP, ridge/Tikhonov, splines, GMRFs,
  and state-space trends.

The paper must center on a nontrivial consequence of forecast-driven,
data-dependent selection.

## Main draft

The first working manuscript is main.tex.

Read first:

1. main.tex
2. AI_HANDOFF.md
3. notes/research_agenda.md
4. notes/current_state.md

No final novelty claim should be made until the dedicated literature audit is
complete.
