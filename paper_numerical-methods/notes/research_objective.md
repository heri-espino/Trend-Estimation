# Canonical research objective — numerical methods

## Research question

Given a time-indexed sequence of potentially multimodal forecast-smoothness
objectives

\[
F_t(S),\qquad S\in[0,1],
\]

can we (i) recover the relevant local minima of each surface reliably with far
fewer evaluations than dense search, and (ii) maintain meaningful numerical
correspondence of those minima across neighboring chronological surfaces?

## Per-surface component

For each `t`, recover

\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\}.
\]

The frozen production method uses compact normalized-`S` search, analytic
derivatives, adaptive interval refinement, derivative-root bracketing, Brent
refinement, stationary-point classification, and exact endpoint comparison.

## Temporal component

Given `M_{t-1}` and `M_t`, assign minima to persistent branches. The current
baseline uses one-to-one nearest-neighbor continuation subject to

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon.
\]

The research problem is to characterize when this rule is reliable and when
more global assignment or additional local geometry is needed.

## Distinct numerical radii

`candidate_spacing` acts within one recovered surface after discovery.
`track_epsilon` acts across adjacent surfaces to define temporal continuation.
They are conceptually and algorithmically distinct.

## Input/output boundary with Paper A

`paper_smoothness-cv/` supplies the forecast-loss surfaces and uses the tracked
branches to make forecasting decisions. This numerical paper supplies local
minima and branch identities. It does not choose the forecasting functional
`phi(V_j)`.

## Stronger possible contribution

Certified polynomial/Sturm isolation may strengthen the per-surface recovery
problem. For temporal tracking, stronger candidates include globally optimal
bipartite assignment and branch-continuation diagnostics based on distance,
objective value, and curvature.
