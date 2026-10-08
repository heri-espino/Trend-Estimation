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

## Observed tracking interface

The committed paper run
`results/numerical_smoothness_selection/20261002T074706Z_tracked-minima-paper_8fe5437/`
contains 1392 initialized branch-origin states across four series and four
difference orders. Exactly 924 state rows were marked matched and 468
marked missing. These are algorithm outputs, NOT ground-truth correctness
rates. The implementation initializes its branches at the first origin
only; an unmatched later candidate does not automatically become a new branch.

The manuscript gives a concrete failure of greedy pairwise matching:
previous minima 0.40 and 0.48, current minima 0.34 and 0.43, radius 0.10.
Greedy takes 0.40 -> 0.43 and leaves one branch unmatched. A two-link
assignment 0.40 -> 0.34 and 0.48 -> 0.43 is feasible.

## Controlled CP05 correspondence benchmark

The frozen evaluation in `checkpoints/CP05_TRACKING_CORRESPONDENCE.md`
uses known true labels, five simulated trajectory mechanisms, and eps
values 0.03, 0.06, 0.10, 0.15. It directly compares the existing greedy
pairwise matcher and exact max-cardinality/minimum-distance pairwise
matching. It resets previous identities to the ground truth at each
transition, so it does not establish end-to-end identity accuracy.
