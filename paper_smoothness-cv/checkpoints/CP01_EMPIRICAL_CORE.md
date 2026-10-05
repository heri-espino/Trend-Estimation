# Checkpoint 01 — Empirical core for forecast-optimal smoothness

**Status: IMPLEMENTED — awaiting execution and result review.**

## Purpose

This checkpoint tests the empirical claims that must hold before the
Journal of Forecasting paper can be scaled up.

It is intentionally small enough to inspect before the final paper run.

## Questions

1. Does horizon-matched forecast-CV choose different smoothness from one-step tuning?
2. Does forecast-optimal smoothness differ from latent-trend recovery-optimal smoothness?
3. How do CV, GCV, AICc, and BIC compare in selected smoothness and later forecast error?
4. Are the proposed figure designs informative enough for the manuscript?
5. Are any selectors numerically unstable at the smoothness endpoints?

## Implemented code

Reusable library:
- src/trend_estimation/selection/classical.py
- src/trend_estimation/core/smoothness.py

Paper experiment:
- experiments/smoothness_cv/common.py
- experiments/smoothness_cv/run_checkpoint_01.py
- experiments/smoothness_cv/make_checkpoint_01_figures.py

Tests:
- tests/test_classical_smoothness_selection.py
- tests/test_smoothness_endpoints.py

## Selector definitions

### Proposed selector

For fixed \(d,L,h\),

\[
\widehat S_h
\in
\arg\min_{S\in[0,1]}
\frac{1}{Mh}
\sum_{m=1}^M
\left\|
z_{T_m}
-
G_{d,h}H_{\lambda(S)}x_{T_m}
\right\|^2.
\]

Checkpoint 01 evaluates this on a deterministic dense \(S\)-grid. This is
intentional: numerical efficiency belongs to the separate numerical-methods
paper.

### One-step comparator

\[
\widehat S_1
\]

is selected by one-step chronological forecast loss and then used to forecast
the operational horizon \(h\). This isolates the value of horizon matching.

### Classical PLS comparators

For the current fixed training window:
- ordinary leave-one-out CV;
- GCV;
- AICc;
- BIC.

The formulas match the PLS criteria summarized by Cortés-Toto, Guerrero, and
Reyes, up to constants that do not affect the minimizer.

### Simulation oracle

The recovery oracle selects

\[
S_{\mathrm{rec}}
\in
\arg\min_S
\|
\widehat\tau_S-\tau
\|^2
\]

on the current training window, using the known latent trend. It is not a
feasible method and is never presented as one. It exists to separate the
forecasting target from the historical trend-recovery target.

## Presets

### smoke

Very small diagnostic run:
- one seed;
- two latent trend mechanisms;
- iid noise;
- two horizons;
- 81-point smoothness grid.

### quick

Exploratory checkpoint:
- three seeds;
- four trend mechanisms;
- iid and AR(1) noise;
- two noise scales;
- horizons 1, 3, 6, and 12;
- 201-point smoothness grid.

### paper

Large provisional design:
- 30 seeds;
- four trend mechanisms;
- iid, AR(1), and Student-t noise;
- three noise scales;
- horizons 1, 3, 6, and 12;
- 801-point smoothness grid.

**Do not run the paper preset before CP01 review.** Its exact design is not yet
frozen.

## Required execution

From the repository root:

~~~bash
conda activate trend-estimation
pip install -e .
pytest
python experiments/smoothness_cv/run_checkpoint_01.py --preset smoke
python experiments/smoothness_cv/make_checkpoint_01_figures.py
~~~

If smoke succeeds:

~~~bash
python experiments/smoothness_cv/run_checkpoint_01.py --preset quick
python experiments/smoothness_cv/make_checkpoint_01_figures.py
~~~

## Required outputs to commit

Commit the complete generated run directory under

results/smoothness_cv/checkpoint_01/

including:
- results.csv;
- objective_curves.csv;
- series_examples.csv;
- horizon_matching.csv;
- summary.csv;
- run_metadata.json;
- paper_artifacts/figures/;
- paper_artifacts/tables/;
- artifact_manifest.json.

Also commit LATEST.txt.

## Review before Checkpoint 02

Do not interpret a single mean as sufficient evidence. Review:

- distributions of selected \(S\);
- endpoint-selection rates;
- matched versus one-step loss ratios;
- forecast versus recovery smoothness gaps;
- performance by trend mechanism;
- performance by noise model;
- performance by horizon;
- whether any classical score produces pathological endpoint concentration;
- whether representative \(F_h(S)\) curves actually move with horizon.

Only after that review should the paper-scale simulation design be frozen.

## Stop rule

The agent should not guess the outcome of CP01. Once the user has pushed the
smoke/quick outputs, inspect those exact files and decide what CP02 must change.
