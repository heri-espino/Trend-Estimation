# Checkpoint — Forecast-Optimal Smoothing Foundation

> **Scope note (2026-09-22):** This is a historical checkpoint. The canonical
> active objective is now stated in \`notes/research_objective.md\` as
> forecast-optimal trend estimation as an adaptive forecasting method with
> joint configuration
> \(\Theta^\star_{T,h}=(d^\star,L^\star,S^\star)\). Results in this checkpoint
> are evidence for parts of that program, not a replacement definition of it.


Date: 2026-09-21

## Scope

The repository is now being treated as a reusable trend-estimation research library. The only active research manuscript is:

**Forecast-Optimal Trend Smoothing under Changing Time-Series Regimes**

The portfolio/decision-optimal branch of the research program is paused.

## What is now established

### Repository structure

- active paper: `paper_forecast-optimal-smoothing/`;
- tutorial companion: `paper_penalized-trend-tutorial/`;
- internal derivations/checkpoints: `notes/`;
- literature/RAG manifest: `literature/`;
- reusable implementation: `src/trend_estimation/`;
- active experiments: `experiments/forecast_optimal_smoothing/`.

### Mathematical core

For the pure smoother,

\[
\widehat t_\lambda=(I+\lambda Q)^{-1}y,
\qquad Q=D_d^\top D_d,
\]

the first two lambda derivatives are implemented and checked by centered finite differences.

For genuine chronological forecast loss,

\[
r_T(\lambda)
=
y_{T+1:T+h}
-
H S_\lambda y_{\rm past},
\]

we derived and implemented

\[
f_T'(\lambda)
=
\frac{2}{h}
r_T^\top H S_\lambda Q S_\lambda y_{\rm past},
\]

and

\[
f_T''(\lambda)
=
\frac{2}{h}
\left[
\|H S_\lambda Q S_\lambda y_{\rm past}\|_2^2
-
2r_T^\top
H S_\lambda Q S_\lambda Q S_\lambda y_{\rm past}
\right].
\]

The explicit matrix/operator representation of \(H\) is now tested against the original recursive forecast implementation.

### Lambda optimization

The robust active method is:

\[
\theta=\log\lambda
\]

followed by derivative scanning, sign-change bracketing, Brent root solving, stationary-point classification, and objective comparison across all detected minima plus boundaries.

Newton remains a local benchmark/refinement.

### Guerrero model correction

The Guerrero (2007) source was checked directly. The canonical plug-in drift is

\[
\widehat m_y=(N-d)^{-1}\mathbf1^\top D_dy,
\]

not the old repository iteration based on fitted-trend differences.

The canonical model is now `GuerreroTrend`. The old behavior is retained explicitly as `IteratedDriftTrend`.

### Chronological selection

A fixed raw lambda is not a fixed normalized smoothness level when fitted sample size changes. Therefore the active inner selector compares candidate fixed windows \(L\), with all inner fits for a candidate using exactly \(L\) observations.

A second correction was made: competing window lengths are evaluated on the **same inner forecast origins**, so their losses are directly comparable.

The implemented nested procedure now has the information flow

\[
y_{1:T}
\to
(d,L,\lambda)\text{ selection}
\to
\text{outer forecast}
\to
\text{future revealed only for scoring}.
\]

A unit test changes the untouched future values while preserving the past and verifies that the selected hyperparameters and forecast do not change.

### Simulations

The library now has controlled generators that can vary separately:

- latent-trend roughness;
- observation-noise scale;
- AR(1) dependence;
- regime changes;
- level shifts;
- slope shifts.

Because the latent trend is known in simulation, an oracle recovery-optimal lambda is also implemented. This lets us compare

\[
S^\star_{\rm forecast}
\quad\text{with}\quad
S^\star_{\rm recovery}.
\]

The first factorial simulation driver is:

`experiments/forecast_optimal_smoothing/run_simulation_grid.py`.

## Validation status

Lightweight GitHub CI is enabled on push/pull request. Heavy paper compilation is separate and manual-only.

The current test suite has been passing after the nested-validation/import-cycle fixes. Re-check the latest CI run before using a new commit for experiments.

## What we should do next

1. run the quick simulation preset locally;
2. inspect whether selected smoothness, oracle recovery smoothness, and relative RMSFE behave sensibly;
3. stress-test the derivative/root finder against a very dense reference scan;
4. add a dedicated within-series two-regime transition experiment;
5. freeze simulation ranges, horizons, windows, orders, seeds, and log-lambda bounds;
6. only then run the paper-scale simulation study;
7. continue the literature audit before making a novelty claim;
8. after simulations are stable, move to macroeconomic real data.

## Why this ordering matters

The paper should not become a collection of exploratory outputs. The intended chain is:

\[
\boxed{
\text{derivation}
\to
\text{tested library}
\to
\text{controlled simulation}
\to
\text{real-data experiment}
\to
\text{paper claim}.
}
\]

This checkpoint is the handoff point between infrastructure/mathematical validation and the first substantive simulation results.
