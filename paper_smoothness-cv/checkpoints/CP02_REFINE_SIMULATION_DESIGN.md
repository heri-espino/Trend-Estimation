> **RESEARCH STATUS UPDATE — 2026-10-08 (current; original checkpoint record preserved below).** The primary current statistical question is selection of normalized PLS smoothness (S\in[0,1]) by **chronological, horizon-matched future-block forecast MSE**, with an explicit polynomial continuation and mandatory final refit. The eigenstructure of the smoother, analytic derivatives, and reliable recovery of competing minima are central mathematical/numerical topics. The source of truth is [../notes/INDEX.md](../notes/INDEX.md), [../notes/mathematical_foundations.md](../notes/mathematical_foundations.md), and [../notes/research_log_2026-10.md](../notes/research_log_2026-10.md).
>
> **Archival status:** This checkpoint was **executed in the old program**, regardless of any stale “awaiting execution” line below. It remains developmental historical evidence, not a planned future task. The numerical solver may be revised; compare old/new solvers on *identical objectives* before designing/re-running a new statistical evaluation. **Do not rewrite frozen observations or retune old tests.**

---

# Checkpoint 02 — Refine the simulation design

**Status: IMPLEMENTED — awaiting execution.**

Checkpoint 01 passed both smoke and quick runs. Its quick output showed three
important facts that determine this checkpoint:

1. Horizon-matched forecast-CV improved relative to one-step tuning more clearly
   as the horizon increased.
2. The original CP01 trend mechanisms were too easy for the d=2 continuation:
   for h >= 3 both forecast-CV and the recovery oracle often selected S very
   close to 1.
3. The endpoint-inclusive global implementation of the published BIC score
   collapsed to the smallest positive smoothness grid value throughout CP01.
   BIC is therefore diagnostic-only in CP02 until its implementation domain is
   reconciled with the source paper.

CP02 is a design-refinement experiment, not the paper-scale simulation.

## Scientific goals

CP02 asks:

- Can we create controlled mechanisms where forecast-optimal smoothness is not
  trivially the maximally smooth d=2 limit?
- Does the optimal smoothness depend materially on the forecast horizon?
- Does recovery-optimal smoothness differ from future forecast-optimal smoothness?
- How close does feasible forecast-CV get to a simulation-only latent-future oracle?
- Does window length change these relationships?
- Does the BIC criterion remain pinned to its left finite boundary under a full
  score-curve audit?

## New latent mechanisms

In addition to control cases, CP02 includes:

- quadratic;
- turning_point;
- recent_slope_change;
- oscillatory;
- terminal_bend.

These were chosen before CP02 is run because CP01 revealed near-degeneracy at
S=1 under the milder mechanisms. They are not selected because of any observed
CP02 performance.

## New simulation oracle

For each outer block, CP02 computes a latent-future oracle

\[
S_{\mathrm{oracle},h}
\in
\arg\min_S
\left\|
\tau_{T+1:T+h}
-
G_{d,h}H_{\lambda(S)}y_{T-L+1:T}
\right\|^2.
\]

The historical fit still uses the noisy observations. Only the choice of S is
allowed to see the latent future. This is not a feasible forecasting method; it
is a benchmark for selection regret.

This gives three conceptually distinct quantities:

\[
S_{\mathrm{recovery}},
\qquad
\widehat S_{\mathrm{forecast-CV},h},
\qquad
S_{\mathrm{oracle},h}.
\]

## Window-length diagnostic

CP02 varies L while holding d=2 fixed. This is a robustness/design diagnostic,
not joint tuning of (d,L,S).

The refine preset uses:

\[
L\in\{36,60,96\}.
\]

If one window is clearly pathological or redundant, CP03 will freeze a smaller
set before the final simulation.

## BIC status

BIC is not a primary performance comparator in CP02.

The published score formula is still evaluated over the full S grid and saved
in classical_score_audit.csv. The purpose is to determine whether its global
minimum remains at the smallest finite S once the exact interpolation endpoint
is excluded.

If that behavior persists, the paper must either:

1. reproduce and justify the original paper's numerical search domain/constraint;
2. report BIC only as a source-paper comparison with that domain made explicit; or
3. omit BIC from the primary global-selector comparison.

Do not silently alter BIC to make it behave better.

## Code

- experiments/smoothness_cv/run_checkpoint_02.py
- experiments/smoothness_cv/analyze_checkpoint_02.py
- experiments/smoothness_cv/make_checkpoint_02_figures.py
- experiments/smoothness_cv/common.py

Tests:
- tests/test_smoothness_cv_cp02.py

## Execution

From the repository root:

~~~bash
git pull
pip install -e .
pytest
python experiments/smoothness_cv/run_checkpoint_02.py --preset smoke
python experiments/smoothness_cv/analyze_checkpoint_02.py
python experiments/smoothness_cv/make_checkpoint_02_figures.py
~~~

If the smoke run completes cleanly, run:

~~~bash
python experiments/smoothness_cv/run_checkpoint_02.py --preset refine
python experiments/smoothness_cv/analyze_checkpoint_02.py
python experiments/smoothness_cv/make_checkpoint_02_figures.py
~~~

Then commit and push the complete results/smoothness_cv/checkpoint_02/ tree.

## Stop rule

Do not create or run CP03 until the refine outputs have been inspected.

CP03 must be frozen from:
- which mechanisms produce informative non-boundary oracle smoothness;
- which window lengths materially change the problem;
- whether horizon matching remains useful beyond the AR(1)-heavy CP01 cases;
- how close forecast-CV comes to the latent forecast oracle;
- whether BIC remains a boundary criterion under global search.

The final paper-scale design must be smaller and more targeted than CP02.
