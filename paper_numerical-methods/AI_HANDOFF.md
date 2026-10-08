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

## Current checkpoint: manuscript tracking integration and CP05 benchmark

The numerical manuscript has been updated to incorporate the existing tracked
minima demonstration (four series; 1392 initialized branch-origin states,
924 matched and 468 missing under epsilon 0.10), the distinct two radii,
and the limits of greedy correspondence.

The new controlled diagnostic is implemented at
`experiments/numerical_smoothness_selection/run_tracking_correspondence_benchmark.py`;
its frozen design is `checkpoints/CP05_TRACKING_CORRESPONDENCE.md`. It compares
the existing greedy one-to-one matcher with an exact maximum-cardinality,
minimum-distance **pairwise** assignment for labeled minima in five mechanisms.
The benchmark must be run before adding quantitative identity-accuracy claims
to the paper.

The diagnostic conditions each adjacent-origin step on known previous true
states. It does not validate an end-to-end tracker with label propagation or
birth initialization. The current real-world tracker initializes only the
first origin's minima and does not automatically initialize later births.

**Do not modify the frozen per-surface optimizer.** Do not infer tracking
accuracy from the 240/240, 2105/2105, or 473/473 per-surface recovery results.

Only `paper_numerical-methods/` and `paper_smoothness-cv/` are active.
