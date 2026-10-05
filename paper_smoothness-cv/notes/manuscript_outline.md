# Manuscript outline — Journal of Forecasting

## Title

**Forecast-Optimal Smoothness for Penalized Trend Estimation**

## Journal-facing abstract logic

1. Trend forecasts require a smoothing choice.
2. Guerrero's controlled-smoothness framework makes that choice interpretable as a percentage rather than an opaque penalty.
3. Forecasting research already selects smoothing/bandwidth/hyperparameters through predictive loss.
4. Define the controlled smoothness percentage endogenously by chronological future-block forecast error.
5. Put the complete penalty path on normalized \(S\in[0,1]\).
6. Establish monotonicity, endpoint semantics, effective degrees of freedom, and equivalence of optimization in \(S\) and \(\lambda\).
7. Test whether horizon-matched forecast smoothness differs from conventional PLS selectors and from recovery-optimal smoothness.
8. Leave efficient multimodal root recovery to the numerical companion paper.

## Active manuscript sections

1. Introduction
2. Related work and positioning
3. Finite-difference penalized trend estimation
4. Forecast-optimal smoothness
5. Basic properties
6. Evaluation protocol
7. Scope, interpretation, and implications
8. Conclusion

## Core equation

\[
\boxed{
S^\star_{d,L,h}
\in
\arg\min_{S\in[0,1]}
\frac{1}{Mh}
\sum_{j=1}^M
\left\|
z_{T_j}
-
G_{d,h}H_{\lambda(S)}x_{T_j}
\right\|^2
}
\]

## Main empirical figure/table logic after experiments

The paper should remain small enough that every display answers a forecasting question.

Likely figures:
1. the \(S\leftrightarrow\lambda\) path and endpoint interpretation;
2. representative simulated \(F_h(S)\) curves showing horizon dependence;
3. forecast-optimal versus recovery-optimal smoothness across controlled mechanisms;
4. held-out relative forecast loss across public series.

Likely tables:
1. simulation design and frozen comparison rules;
2. aggregate held-out forecast performance of forecast-CV versus CV/GCV/AICc/BIC;
3. horizon-matching comparison;
4. robustness summaries.

Do not fill the manuscript with the numerical paper's derivative/root-search diagnostics.
