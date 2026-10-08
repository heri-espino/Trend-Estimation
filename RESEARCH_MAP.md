# Research map

**Updated 2026-10-08.** Exactly **three active independent working papers**.

## 1. Smoothness Cross Validation

[Workspace](working_papers/Working%20Paper%20-%20Smoothness%20Cross%20Validation/)

Question: for fixed order d, fitting window L and forecast horizon h,
which normalized smoothing parameter S minimizes historical,
horizon-matched pooled future-block MSE?

The decision minimizes the full pooled forecast-loss curve,
not the average of individual folds' minimizing values.
The selected S is refitted at the latest forecast origin.
CP01–CP03 contain previously completed pooled evidence.

## 2. Numerical Methods

[Workspace](working_papers/Working%20Paper%20-%20Numerical%20Methods/)

Question: for a specified single potentially multimodal
forecast-loss function F(S), how can stationary points, local
minima and exact endpoints be recovered and ranked reliably?
Includes adaptive derivative-root discovery, Brent refinement
and small rational Sturm examples. Empirical recovery benchmarks
do not prove global completeness on arbitrary large problems.

## 3. Dynamic Branch Selection

[Workspace](working_papers/Working%20Paper%20-%20Dynamic%20Branch%20Selection/)

Question: can matched chronological minima histories
V_j support a useful future smoothing decision through
branch-selection and branch-to-smoothness mappings?
This question has distinct tracking assumptions and outer-test
evidence, including recorded unsuccessful broad comparisons.
CP04–CP08 and the unrun correspondence proposal are retained
with honest result status.

## Repository policy

Each working paper has an independent question, manuscript,
bibliography, notes, results and limitations. Do not refer
to any as a companion paper. Shared Python packages,
experiments and results remain outside the manuscript folders
for reproducibility. Inactive work belongs under [ideas/](ideas/).
