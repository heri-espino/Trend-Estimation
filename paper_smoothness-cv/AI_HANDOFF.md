# AI Handoff — Smoothness-CV paper

## Identity

This paper answers **what should be optimized**, not **how to optimize it quickly**.

\[
S^\star_{d,L,h}\in\arg\min_{S\in[0,1]}F_{d,L,h}(S),
\]
where \(F\) is chronological rolling future-block MSE from a finite-difference penalized trend plus its fixed continuation rule.

## Foundation

Start from Guerrero rather than Hart.

Guerrero supplies finite-difference PLS, controlled smoothness, and trend forecasting/extrapolation logic. The extension is to select the smoothness percentage from predictive performance rather than fixing it exogenously.

Hart is related-work evidence that predictive smoothing-parameter selection exists in another smoother family. It constrains novelty wording; it does not replace Guerrero as the main lineage.

## Do not import from the numerical paper

Do not make Brent, adaptive subdivision, derivative root finding, or Sturm the contribution here. A dense grid is acceptable.

Derivatives may appear as mathematical properties, but the solver belongs to Paper B.

## Mathematical chain

\[
y\xrightarrow{H_\lambda}\widehat\tau
\xrightarrow{G_{d,h}}\widehat z
\xrightarrow{\text{future error}}f(\lambda)
\xrightarrow{S\leftrightarrow\lambda}F(S).
\]

## Immediate tasks

1. formalize the forecast-CV criterion and information-set rule;
2. separate its target from recovery-optimal smoothing, GCV, likelihood, and exogenous smoothness;
3. design controlled simulations with known latent trend;
4. study dependence on horizon \(h\);
5. establish what is conditional on fixed \(d,L,h\);
6. perform targeted literature audit before any "first" claim;
7. draft around the Guerrero -> endogenous smoothness transition.

Do not turn this into the broad adaptive \((d,L,S)\) paper.
