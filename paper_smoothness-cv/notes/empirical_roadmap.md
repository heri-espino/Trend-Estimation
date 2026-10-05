# Empirical roadmap — Journal of Forecasting paper

Last updated: 2026-10-05.

This roadmap begins where the current theory/manuscript draft stops. Its purpose
is to produce the evidence, figures, and tables needed for a Journal of
Forecasting submission without contaminating the numerical-methods paper.

## Scientific hierarchy

The empirical section must answer three questions in this order:

1. **Does forecast-oriented tuning choose a different smoothness?**
2. **Does matching the tuning horizon to the forecast horizon matter?**
3. **When the selected smoothness differs, does it improve later held-out forecasts?**

Everything else is secondary.

The central comparison is therefore not merely

\[
\lambda_A \neq \lambda_B,
\]

but

\[
S^\star_{\mathrm{forecast},h}
\neq
S^\star_{\mathrm{recovery/classical}}
\]

together with an untouched later forecast evaluation.

## Figure roadmap

### Figure 1 — the smoothness coordinate

Purpose: explain the parameterization before showing empirical results.

Panel/display candidates:
- \(S(\lambda)\) on a log-\(\lambda\) axis;
- exact effective-degrees-of-freedom relation
  \(\operatorname{edf}=L-(L-d)S\).

This figure is theory-facing and can be generated without simulation results.

### Figure 2 — representative forecast-loss surfaces

Plot

\[
F_{d,L,h}(S)
\]

for the same simulated history and several horizons.

Purpose:
- show that the criterion has substantive geometry;
- show that its minimizer can move with \(h\);
- make possible non-unimodality visible without turning the paper into the
  numerical-methods paper.

Use only a few representative cases in the final manuscript.

### Figure 3 — selected smoothness versus horizon

Summarize

\[
h\mapsto S^\star_{d,L,h}
\]

across controlled simulations.

Purpose: establish that horizon dependence is empirically meaningful rather
than merely possible algebraically.

### Figure 4 — forecast-optimal versus recovery-optimal smoothness

Scatter

\[
S^\star_{\mathrm{recovery}}
\quad\text{against}\quad
S^\star_{\mathrm{forecast},h}
\]

with the 45-degree line.

Purpose: demonstrate directly that historical trend recovery and future
forecasting are different tuning targets.

### Figure 5 — method comparison

Compare held-out forecast performance of:
- horizon-matched forecast-CV;
- one-step forecast-CV;
- CV;
- GCV;
- AICc;
- BIC.

Primary display: relative RMSFE to GCV or another prespecified baseline.

Purpose: answer whether the proposed tuning target translates into later
forecast gains.

### Figure 6 — horizon matching

For \(h>1\), compare test MSE under:
- smoothness selected with one-step forecast loss;
- smoothness selected with the same \(h\)-step block used operationally.

Primary statistic:

\[
\frac{\operatorname{MSE}(\widehat S_h)}
     {\operatorname{MSE}(\widehat S_1)}.
\]

Purpose: isolate the paper's horizon-specific contribution.

### Figure 7 — public-data summary

After simulations are frozen, add one compact real-data display:
- relative forecast loss across series; or
- method ranks across series.

Only 2–3 individual series should be shown as illustrations.

## Table roadmap

### Table 1 — frozen simulation design

Include:
- latent trend mechanisms;
- noise models;
- noise levels;
- sample lengths;
- fixed \(d,L\);
- horizons;
- number of seeds;
- validation/test scheme.

### Table 2 — simulation forecast performance

Aggregate held-out MSFE/relative RMSFE for the six feasible selectors.

### Table 3 — horizon matching

Report selected \(S\), forecast loss, and win rate for \(S_h^\star\) versus
\(S_1^\star\).

### Table 4 — forecast versus recovery target

Report differences between forecast-optimal and recovery-optimal smoothness,
plus both recovery and forecast metrics.

### Table 5 — public-data forecasting panel

Keep this compact: MSFE/MAE or relative loss and average rank.

## Checkpoint sequence

### CP01 — empirical core: IMPLEMENTED, awaiting execution

Code:
- experiments/smoothness_cv/common.py
- experiments/smoothness_cv/run_checkpoint_01.py
- experiments/smoothness_cv/make_checkpoint_01_figures.py
- src/trend_estimation/selection/classical.py

Questions:
- Are the classical selectors stable?
- Does \(S_h^\star\) move with \(h\)?
- Does it differ from the recovery oracle?
- Do the proposed figures reveal the mechanisms clearly?

Run smoke first, then quick. Stop and push results.

### CP02 — refine and freeze simulation design

Depends on CP01 outputs.

Tasks:
- remove uninformative DGPs;
- add any missing mechanism suggested by CP01;
- freeze the exact paper grid;
- freeze seeds and test origins;
- decide whether heavy-tailed noise remains main text or robustness;
- decide whether \(d=1,3\) belongs to robustness.

No final paper-scale run before this checkpoint is frozen.

### CP03 — paper-scale controlled simulations

Run the frozen grid at substantially larger scale.

Outputs:
- final simulation result tables;
- final Figures 2–6;
- uncertainty summaries;
- sensitivity/robustness appendix material.

After this checkpoint, simulation design cannot be retuned using the final test
results.

### CP04 — public multi-series forecasting panel

Use a reproducible public forecasting dataset.

Requirements:
- chronological train/validation/test;
- fixed preprocessing;
- no per-series manual tuning;
- horizons fixed before results;
- same selector definitions as simulation.

Candidate panel: M4 or another stable public benchmark whose series frequency
can be handled cleanly.

### CP05 — real-time macro illustration

Optional but valuable for Journal of Forecasting.

If retained:
- use historical vintages for historical backtests;
- do not use current revised FRED histories as if they were available in real
  time;
- keep panel small and interpretable.

### CP06 — manuscript integration

- copy only frozen final figures into paper_smoothness-cv/manuscript/figures/;
- generate LaTeX tables from frozen result CSVs;
- replace evaluation-protocol prose with actual Results while preserving the
  prespecified design;
- update abstract/conclusion only with results actually observed;
- compile final Wiley manuscript.

### CP07 — submission audit

- literature/novelty pass;
- chronological leakage audit;
- code/data reproducibility audit;
- figure readability in two-column layout;
- black-and-white/print check;
- referee-style contribution review;
- freeze final commit and PDF.

## Current stop point

CP01 code is ready. The next required information is empirical output from the
user's machine.

Run:

~~~bash
python experiments/smoothness_cv/run_checkpoint_01.py --preset smoke
python experiments/smoothness_cv/make_checkpoint_01_figures.py
~~~

If that passes, run the quick preset and push the entire generated run directory.
Do not start CP02 from assumptions; CP02 must respond to the actual CP01 output.
