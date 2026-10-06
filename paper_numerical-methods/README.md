# Numerical methods for multimodal forecast-smoothness selection

**Status: ACTIVE.**

**Working title:** *Numerical Solution and Tracking of Multimodal Forecast-Smoothness Minima*.

## Objective

The numerical paper now has two linked tasks.

### Task A — recover minima on one surface

Given

\[
F_t(S),\qquad S\in[0,1],
\]

recover all relevant local minima and the global optimum efficiently and
reliably, without assuming unimodality.

### Task B — track minima across time

For a sequence of neighboring forecast-loss surfaces, recover

\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\}
\]

and determine which minima belong to the same temporal branch.

The current baseline continuation rule is one-to-one nearest-neighbor matching
under

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon.
\]

Canonical tracking note: `notes/temporal_minima_tracking.md`.

## Current per-surface solver

1. sparse deterministic evaluation in normalized `S`;
2. analytic first/second derivatives;
3. adaptive interval subdivision;
4. derivative sign-change brackets;
5. Brent root refinement;
6. stationary-point classification;
7. exact/limiting endpoint comparison;
8. optional within-surface spacing of nearby representative minima.

Brent refines roots after a bracket is identified; it is not a global
root-discovery algorithm.

## Two different epsilon-like quantities

Do not conflate:

- `candidate_spacing`: post-discovery separation of redundant/nearby minima on
  the **same** surface;
- `track_epsilon`: maximum distance used to continue a minimum from one
  chronological surface to the **next** surface.

The dynamic forecasting paper uses the tracked branches downstream.

## Interface with `paper_smoothness-cv/`

The numerical paper returns the local minima and their branch identities.
The forecasting paper then augments each branch with Validation-2 forecast loss
and forms

\[
V_j=[S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t}]_t.
\]

The forecasting paper owns branch selection `psi(V_1,...,V_J)` and the final
smoothness rule `phi(V_j)`. This numerical paper does **not** claim those
decision rules as its contribution.

## Frozen numerical evidence

The existing per-surface solver remains frozen under the previous benchmark
protocol:

- 240/240 relevant adversarial minima/boundary optima;
- 2105/2105 synthetic dense-reference interior minima across 1920 surfaces;
- 473/473 financial dense-reference interior minima across 384 surfaces;
- mean evaluation fractions about 1.57% synthetic and 1.84% financial.

These validate the per-surface search empirically. They do not yet validate
temporal branch correspondence.

## New numerical work required

The temporal extension must evaluate:

- sensitivity to `track_epsilon`;
- branch birth/death;
- near-crossings and ambiguous matches;
- greedy one-to-one matching versus globally optimal bipartite matching;
- stability when minima become very close;
- possible use of curvature/objective information as secondary correspondence
  features.

Do not claim certified tracking until those cases are studied.

## Stronger algebraic direction

The rational/Sturm direction remains a possible route to certified per-surface
stationary-root isolation. It is still a proof-of-concept and does not solve
the cross-time correspondence problem by itself.

## Active papers

Only `paper_numerical-methods/` and `paper_smoothness-cv/` are active.
