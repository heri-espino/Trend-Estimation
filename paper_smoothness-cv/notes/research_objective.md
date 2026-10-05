# Canonical research objective

## Research question

Can the percentage of smoothness in finite-difference penalized least-squares trend estimation be selected endogenously from chronological forecast performance rather than specified ex ante?

## Estimator

For \(x_T\in\mathbb R^L\),
\[
\widehat\tau_T(\lambda)=H_\lambda x_T,\qquad
H_\lambda=(I+\lambda Q)^{-1},\qquad
Q=D_d^\top D_d.
\]

## Smoothness coordinate

\[
S(\lambda)=
1-\frac1{L-d}\sum_{\delta_j>0}\frac1{1+\lambda\delta_j}.
\]

Under the usual finite-difference operator, \(S\) is continuous and strictly increasing, with
\[
S(0)=0,\qquad S(\infty)=1.
\]

## Forecast criterion

Let \(G_{d,h}\) map the fitted historical trend to the \(h\)-step continuation implied by the fixed finite-difference forecast family.

\[
\widehat z_T(S)=G_{d,h}H_{\lambda(S)}x_T.
\]

For rolling origins \(T_1,\ldots,T_M\),
\[
F_{d,L,h}(S)=
\frac1{Mh}
\sum_{j=1}^M
\left\|
z_{T_j}-G_{d,h}H_{\lambda(S)}x_{T_j}
\right\|^2.
\]

Define
\[
S^\star_{d,L,h}\in\arg\min_{S\in[0,1]}F_{d,L,h}(S).
\]

## Intended contribution

Formulate and study this smoothness-selection target inside the finite-difference PLS/controlled-smoothness framework.

The paper should distinguish it from analyst-chosen smoothness, recovery optimality, in-sample fit, GCV/AIC/BIC/marginal-likelihood selection, and kernel-bandwidth TSCV.

Efficient multimodal optimization belongs to paper_numerical-methods/. Joint adaptive selection of \(d,L,S\) belongs to paper_forecast-optimal-smoothing/.
