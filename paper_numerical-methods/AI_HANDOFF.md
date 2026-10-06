# AI Handoff — Numerical-methods paper

## Identity

This paper answers two numerical questions:

1. how to recover the relevant local minima of each multimodal forecast-
   smoothness surface `F_t(S)`;
2. how to track/correspond those minima across adjacent chronological surfaces.

The forecasting interpretation of the resulting branches belongs to
`paper_smoothness-cv/`.

## Per-surface problem

\[
F_t(S),\qquad S\in[0,1],
\]

with local-minimum set

\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\}.
\]

Current frozen solver:

- adaptive discovery over `S`;
- evaluate `F,F',F''`;
- bracket sign-changing roots of `F'`;
- refine with Brent;
- classify roots;
- include exact `S=0` and `S=1`;
- compare all candidate minima.

Existing benchmark evidence applies to this per-surface task.

## Temporal correspondence problem

The dynamic forecasting method requires branch identities through time.
The current baseline matcher is one-to-one nearest-neighbor continuation:

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon.
\]

Read `notes/temporal_minima_tracking.md` before modifying tracking code.

Do not confuse:

- `candidate_spacing` = within-surface post-discovery separation;
- `track_epsilon` = across-time branch continuation radius.

The greedy matcher is currently a baseline. Do not claim it is globally
optimal or certified.

## Paper boundary

This paper owns:

- local-minimum discovery;
- derivative/root numerical methods;
- exact endpoints;
- numerical accuracy and efficiency;
- temporal correspondence/tracking of minima.

`paper_smoothness-cv/` owns:

- Validation-2 scoring;
- branch matrix `V_j` as a forecasting state;
- branch selector `psi`;
- final smoothness functional `phi(V_j)`;
- forecast comparisons.

## Rational/Sturm direction

Sturm remains a possible certified per-surface root-isolation extension. It
does not by itself solve temporal branch identity.

## Current next task

Keep the frozen per-surface solver unchanged. Build a controlled branch-
tracking benchmark around the existing tracked-minima experiment: branch
birth/death, crossings, epsilon sensitivity, and greedy versus bipartite
matching.

Only `paper_numerical-methods/` and `paper_smoothness-cv/` are active.
