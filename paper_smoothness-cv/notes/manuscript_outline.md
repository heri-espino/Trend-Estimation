# Manuscript outline

## Provisional title

Forecast-Optimal Smoothness for Finite-Difference Penalized Trend Estimation

## Abstract logic

1. Penalized trend estimators require a smoothing choice.
2. Controlled-smoothness work makes smoothing interpretable but treats the target as externally specified.
3. Define an endogenous smoothness target by minimizing chronological future-block forecast error.
4. Express the criterion on normalized \(S\in[0,1]\).
5. Study how forecast-optimal smoothness differs from recovery-oriented smoothing and changes with horizon/mechanism.
6. Leave efficient multimodal optimization to the companion numerical paper.

## Sections

1. Introduction
2. Finite-difference PLS and controlled smoothness
3. From exogenous to forecast-optimal smoothness
4. Chronological future-block criterion
5. Mathematical properties
6. Controlled simulations
7. Empirical illustrations
8. Relation to predictive smoothing selection
9. Discussion and limitations
10. Conclusion

## Core equation

\[
\boxed{
S^\star_{d,L,h}
\in
\arg\min_{S\in[0,1]}
\frac1{Mh}
\sum_{j=1}^M
\left\|
z_{T_j}-G_{d,h}H_{\lambda(S)}x_{T_j}
\right\|^2
}
\]
