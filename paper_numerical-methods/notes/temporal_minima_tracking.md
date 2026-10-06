# Temporal tracking of local forecast-smoothness minima

**Status: active numerical extension.**

This note defines the interface between `paper_numerical-methods/` and the
dynamic forecasting method in `paper_smoothness-cv/`.

## Per-surface problem

For each chronological forecast origin `t`, the forecasting paper supplies a
one-dimensional smoothness objective

\[
F_t(S),\qquad S\in[0,1].
\]

The numerical paper must recover the relevant local minima

\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\},
\]

including exact boundary optima where relevant.

The existing adaptive `S`-space search, analytic derivatives, Brent refinement,
and endpoint comparison solve this per-surface problem.

## Cross-surface correspondence problem

The new numerical question is how to assign local minima on adjacent surfaces
to persistent branches.

The current baseline matcher is one-to-one nearest-neighbor continuation in
normalized smoothness under

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon.
\]

This produces branch identities

\[
\mathcal B_j=(S_{j,t_1},S_{j,t_2},\ldots).
\]

The continuation radius is **not** the same as post-discovery candidate
spacing. Candidate spacing suppresses redundant minima on one surface.
Tracking epsilon connects minima across different surfaces.

These two epsilons must be named distinctly in code and prose whenever there
is risk of ambiguity:

- `candidate_spacing`: within-surface representative separation;
- `track_epsilon`: across-time branch continuation radius.

## Numerical output required by Paper A

For every matched branch/origin, the numerical layer should return at least:

- branch id;
- origin/date;
- local minimum `S`;
- implied `lambda`;
- objective/Validation-1 loss;
- continuation distance `delta_s`;
- number of local minima on the surface;
- whether the branch was successfully continued.

Forecasting-layer code then adds Validation-2 loss after the required refit.

## Reliability questions for the numerical paper

The branch-tracking extension should study:

1. sensitivity to `track_epsilon`;
2. branch births and deaths;
3. near-crossings where nearest-neighbor identity may be ambiguous;
4. whether one-to-one greedy matching differs from globally optimal bipartite
   matching;
5. robustness when two minima approach within numerical resolution;
6. whether curvature/objective value should be used as secondary matching
   information after smoothness distance.

The current greedy matcher is a transparent baseline, not yet a theorem or a
certified continuation algorithm.

## Paper boundary

`paper_numerical-methods/` owns:

- discovery of all relevant minima of each `F_t(S)`;
- exact boundary handling;
- numerical accuracy/efficiency;
- temporal correspondence of minima across surfaces.

`paper_smoothness-cv/` owns what to do with the tracked branches:

- Validation-2 scoring;
- branch-selection rule `psi`;
- branch matrix `V_j`;
- final smoothness rule `phi(V_j)`;
- forecast evaluation.

Do not move the decision rules into the numerical contribution.
