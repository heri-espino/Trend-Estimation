# Current state — Statistical-properties paper

Last updated: 2026-10-05

## Status

A first full main.tex draft now exists. The paper has a clear identity but does
not yet have a frozen theorem-level novelty claim.

## Established foundation

\[
\widehat\tau_\lambda=H_\lambda y,
\qquad
H_\lambda=(I+\lambda Q)^{-1}.
\]

For fixed \(\lambda\),
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
H_\lambda\Sigma H_\lambda^\top,
\]
and
\[
\operatorname{edf}(\lambda)
=
\operatorname{tr}(H_\lambda)
=
N-(N-d)S.
\]

The project also has analytic \(H'\), \(H''\), \(S'\), \(S''\), forecast-loss
derivatives, a forecast operator \(G_{d,h}H_\lambda\), and evidence that
forecast-CV surfaces can be multimodal.

## What changes after selection

The smoothness-CV paper produces
\[
\widehat S=\arg\min_S F(S).
\]

This paper studies
\[
\widehat\tau_{\widehat S}
=
H_{\lambda(\widehat S(y))}y,
\]
which is generally not a fixed linear smoother.

## Main unknowns

- distribution/stability of \(\widehat S\);
- effective complexity of the full adaptive map;
- bias/variance after selection;
- post-selection coverage for trend level/slope/curvature;
- selection uncertainty under multimodal \(F(S)\);
- propagation of smoothness uncertainty into forecasts;
- rigorous local approximations and their failure at boundaries/minimum switches.

## Immediate next steps

1. Literature audit on generalized degrees of freedom, smoothing-parameter
   uncertainty, post-selection inference, and tuning by dependent/forecast CV.
2. Build a theorem table: result, assumptions, known source, what remains new.
3. Choose one primary contribution rather than trying to solve all open items.
4. Derive the simplest case first: Gaussian noise, fixed \(d,L,h\), unique
   interior forecast-optimal \(S^\star\).
5. Design coverage simulations before real-data applications.

Until the audit is complete, open items are research questions, not novelty
claims.
