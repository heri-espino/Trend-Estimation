# Canonical research objective — dynamic smoothness-CV

## Research question

Can local minima of a chronological forecast-loss surface for penalized trend
smoothness be tracked through time, and can their historical trajectories be
used to choose the current smoothness more effectively than a single pooled
forecast-CV optimum?

## Estimator

For the most recent `L` observations at outer origin `T`,

\[
\widehat\tau_T(S)=H_{\lambda(S)}y_{T-L+1:T},
\qquad
H_\lambda=(I+\lambda D_d^\top D_d)^{-1}.
\]

## Normalized smoothness

\[
S(\lambda)
=
1-\frac1{L-d}\sum_{\delta_j>0}\frac1{1+\lambda\delta_j},
\qquad S\in[0,1].
\]

## Static pooled baseline

For historical forecast origins inside the information set available at `T`,

\[
F^{\mathrm{pool}}_{T,h}(S)
=
\frac1M\sum_{m=1}^{M}\ell_{m,h}(S),
\]

with baseline selector

\[
\widehat S^{\mathrm{pool}}_{T,h}
\in\arg\min_S F^{\mathrm{pool}}_{T,h}(S).
\]

## Dynamic local-minimum process

At each chronological origin `t`, define the local-minimum set

\[
\mathcal M_t^{(d,L,h)}
=
\{S_{1,t},\ldots,S_{K_t,t}\}.
\]

Track minima through time by one-to-one continuation inside

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon.
\]

A tracked branch stores

\[
V_j=
\{(S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t})\}_{t\in\mathcal T_j}.
\]

The final decision is

\[
\widehat j_T=\psi(V_1,\ldots,V_J),
\qquad
\widehat S_T=\phi(V_{\widehat j_T}).
\]

`psi` selects a persistent branch from historical Validation-2 performance and
support. `phi` determines how the branch history is converted into today's
smoothness.

## Candidate final-smoothness rules

The initial comparison set is:

\[
\phi_{\mathrm{last}},\
\phi_{\mathrm{mean},K},\
\phi_{\mathrm{median},K},\
\phi_{\mathrm{V2}},\
\phi_{\mathrm{recency+V2}}.
\]

A simple time-series forecast of `S_{j,t}` is a later extension.

## Final refit

Once `S_hat_T` is chosen, the trend is refit with all currently available data
in the fixed final window:

\[
\widehat\tau_T
=
H_{\lambda(\widehat S_T)}y_{T-L+1:T},
\qquad
\widehat y_{T+1:T+h\mid T}=G_{d,h}\widehat\tau_T.
\]

## Intended contribution

The paper studies the **forecasting value of temporal persistence in local
smoothness optima**. It compares dynamic branch-based rules with the simpler
pooled forecast-CV optimum and conventional smoothness selectors.

Efficient recovery and numerical tracking of local minima belong to
`paper_numerical-methods/`.
