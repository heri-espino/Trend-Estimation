# AI Handoff — Dynamic smoothness-CV paper

## Identity

This paper now studies **dynamic forecast-optimal smoothness**.

The older pooled selector

\[
\widehat S^{\mathrm{pool}}_{T,h}
\in\arg\min_S F^{\mathrm{pool}}_{T,h}(S)
\]

remains a primary baseline, but it is no longer the whole research question.

The central object is a time sequence of local minima of forecast-loss surfaces
and the persistent branches they form.

Read `notes/dynamic_tracked_smoothness.md` before changing the method,
experiments, or manuscript.

## Canonical dynamic object

At each chronological origin `t`, recover

\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\}.
\]

A current minimum may continue a previous branch if

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon,
\]

with one-to-one matching.

Each branch is represented by

\[
V_j=
\begin{pmatrix}
S_{j,t_1} & \ell^{(1)}_{j,t_1} & \ell^{(2)}_{j,t_1}\\
\vdots & \vdots & \vdots
\end{pmatrix}.
\]

`ell1` is Validation-1 loss on the surface where the local minimum is found.
`ell2` is Validation-2 forecast loss after refitting through Validation 1 with
the same `d,L,S`.

The decision has two layers:

\[
\widehat j_T=\psi(V_1,\ldots,V_J),
\qquad
\widehat S_T=\phi(V_{\widehat j_T}).
\]

`psi` selects a persistent branch using historical information only.
`phi` turns the selected branch history into the smoothness used today.

Minimum `phi` comparison set:

- last local minimum;
- recent mean;
- recent median;
- pure recency-weighted mean, with exponentially larger weight on newer smoothness values;
- Validation-2 weighted mean;
- recency + Validation-2 weighted mean;
- later: explicit forecast of the smoothness trajectory.

Do not silently choose one rule as final before it is evaluated out of sample.

## Non-negotiable validation semantics

At an outer forecast origin `T`, no observation after `T` may affect branch
selection, the final smoothness rule, or the trend fit.

After `S_hat_T` is produced, discard all historical fold-specific trend fits and
perform a fresh fit on

\[
y_{T-L+1:T}.
\]

Then forecast the untouched future block. We may average losses or values of
`S` when a declared `phi` rule requires it; **we never average old trend fits**.

## Current implementation mapping

`experiments/numerical_smoothness_selection/run_two_stage_order_validation.py`
already implements:

- local-minimum recovery at each rolling origin;
- epsilon branch tracking;
- one-to-one branch continuation;
- Validation-1 loss;
- refit through Validation 1;
- Validation-2 loss;
- persistence summaries;
- branch selection by historical Validation-2 loss;
- final `last` local-minimum rule;
- untouched-test scoring.

It also records branch mean/median and recent-five mean/median as diagnostics.
Those summaries are not yet competing final `phi` methods.

## Relationship to CP03

CP01--CP03 belong to the simpler pooled-selector baseline. CP03 remains frozen
and should not be changed after results are observed. It becomes baseline
evidence, not the final dynamic method.

The next smoothness-CV checkpoint must compare dynamic `phi(V_j)` rules using
identical branch histories and identical untouched test blocks.

## Paper boundary

`paper_smoothness-cv/` owns the forecasting/statistical decision rule:
`V_j`, `psi`, `phi`, validation design, and forecast evidence.

`paper_numerical-methods/` owns recovery of the multiple local minima and the
numerical correspondence/tracking problem across surfaces.

Only these two papers are active.

## Primary target

Journal of Forecasting.

## Claim rule

Do not claim the first predictive smoothing selector or universal superiority.
Any novelty claim about tracked minima must be audited against the literature
before submission.

## Current execution checkpoint — CP04

CP03 pooled paper-scale results have been committed. CP04 is now implemented
as the development experiment for dynamic tracked-branch rules.

Run `run_checkpoint_04.py --preset smoke` first, then `--preset refine` if
smoke passes. The refine preset uses six development outer blocks per series
while reserving the newest four non-overlapping blocks for later confirmation.

After refine, push the result bundle and stop. Do not inspect the reserved
confirmation region until `phi`, K/half-life, and the confirmation protocol
have been frozen in `checkpoints/CP04_DYNAMIC_BRANCH_RULES.md`.


## Frozen CP04 confirmation specification

The development rerun is complete. `recency_hl3` is frozen as the primary
dynamic rule before inspecting the reserved confirmation blocks.

Development result:
- geometric RMSFE vs `last`: 0.7989;
- geometric RMSFE vs `pooled_cv_same_config`: 1.0491.

The latter means the dynamic rule did not beat the pooled baseline on aggregate
development data; confirmation is therefore genuinely informative rather than
a formality.

The confirmation preset evaluates only:
- `recency_hl3`;
- `last`;
- `pooled_cv_same_config`.

Frozen parameters: level RMSE, track epsilon 0.10, candidate spacing 0.02,
max minima 5. Run `run_checkpoint_04.py --preset confirmation` exactly once,
then analyze and push the result.


## CP04 completed confirmation result

CP04 is complete. The frozen `recency_hl3` rule was evaluated once on the
reserved confirmation blocks.

Confirmation geometric RMSE ratios:
- vs pooled forecast-CV: **0.6920**, wins 13/16;
- vs newest tracked minimum: **0.8137**, wins 9/16.

The pooled comparison favors the dynamic rule in aggregate for AAPL, GDPC1,
and SPY; BTC-USD is slightly above one. Leave-one-series-out dynamic/pooled
ratios all remain below one.

Do not retune CP04.

The active next checkpoint is `checkpoints/CP05_EXTERNAL_PANEL.md`, a frozen
64-series external Yahoo panel excluding AAPL, SPY, and BTC-USD. The only
dynamic rule is still `recency_hl3`.


## CP05 completed external-panel result

CP05 is complete on 64 previously unused Yahoo series.

Frozen `recency_hl3` versus pooled forecast-CV:
- geometric RMSE ratio: **1.6421**;
- descriptive series-cluster interval: **[1.1678, 2.7033]**;
- outer-block win rate: 46.5%;
- series-level win rate: 39.1%.

Therefore the CP04 pooled-CV advantage did **not** generalize.

Frozen `recency_hl3` versus newest tracked minimum:
- geometric RMSE ratio: **0.5246**;
- descriptive interval: **[0.2001, 0.9052]**.

The tracked recency average strongly stabilizes `last`, but this does not make
it better than pooled CV overall.

Post-hoc mechanism diagnostics point strongly to high-order continuation:
dynamic/pooled geometric ratios are roughly 1.008 for d=1, 1.018 for d=2,
1.249 for d=3, and 7.960 for d=4. Several d=4 cubic extrapolations become
astronomically large.

The active next checkpoint is `checkpoints/CP06_ORDER_STABILITY.md`, a
post-hoc mechanism study on earlier historical outer blocks. It must not be
described as independent confirmation.


## CP07 completed dynamic-roughness result

CP07 fixed d=2 and isolated time-varying latent roughness from high-order
continuation instability.

Frozen recency_hl3 versus pooled forecast-CV:
- all mechanisms: gRMSE ratio 1.037;
- changing roughness: 1.028;
- stationary roughness: 1.056.

Frozen recency_hl3 versus newest tracked minimum:
- all mechanisms: 0.945.

Therefore backward-looking recency averaging stabilizes a tracked minimum but
does not beat pooled forecast-CV, even in the prospective changing-roughness
simulation.

The next experiment is CP08. It uses fresh seeds and tests the original
forward-looking extension: predict/extrapolate the selected branch's smoothness
trajectory rather than averaging it backward.

CP08 is **not** a competition to find a universally best \(\phi\). Its role is
to demonstrate that the branch matrix \(V_j\) supports many coherent
branch-to-smoothness rules: means, medians, recency weighting, loss weighting,
linear extrapolation, weighted trend extrapolation, and increment
extrapolation. Their empirical differences are reported as behavior of the
design space, not as a winner-selection exercise.
