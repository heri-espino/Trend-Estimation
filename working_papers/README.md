# Working papers

**Source-method replication separately:** the
[full-N Cortés-Toto 2^4 runner](../experiments/smoothness_cv/run_cortes_toto_replication.py)
reproduces the original *in-sample smoothness selection target* on
entire N=50/200 series. This is distinct from using the same 16 DGP
cells as **forecasting** stress cases in the extensive simulation
campaign.

## Start here — theory and current interfaces (2026-10-09)

**Research is theory-first.** Read
[THEORETICAL_CONTRIBUTIONS.md](THEORETICAL_CONTRIBUTIONS.md)
for **known results, our proposed integrations, proof obligations,
conjectures, scientific limitations and the GPU's supporting role**.
For implementation evidence and preliminary user-provided acceleration
numbers, use
[COMPUTATIONAL_IMPLEMENTATION.md](COMPUTATIONAL_IMPLEMENTATION.md).

**One canonical independent Streamlit app per paper:**
[Paper 1 pooled forecast-CV](../apps/pooled_forecast_cv.py),
[Paper 2 weighted-F dynamic branches](../apps/dynamic_branch_cv.py),
[Paper 3 numerical stationary points](../apps/numerical_methods.py).
Read [apps/README.md](../apps/README.md) for actual controls, data
provenance and historical/legacy traps.

The earlier \`apps/smoothness_lab.py\` and
\`apps/smoothness_lab_advanced.py\` implement a *different* Val1/Val2
algorithm and must never be presented as the current Paper 2.
New paper formulations and apps are not automatically synchronized
with the older LaTeX drafts or frozen CP01–CP08 evidence.

## Shared experimental evaluation

Both papers now have a single proposed [simulation and evaluation
protocol](SIMULATION_EVALUATION_PROTOCOL.md). It separately measures
**future observed-series forecasting**, **past latent-trend recovery**,
**future latent-trend forecasting**, and **selected normalized/raw
smoothness and EDF**. Experiment A reuses Cortés-Toto et al.'s 2^4
factorial design; Experiments B/C extend to polynomial degree,
nonlinear shapes, dependent noise and nonstationary branch behavior.
CV/GCV/AICc/BIC are **competing selection criteria**, not forecast
metrics. Fixed/ad-hoc S values, original pooled CV, weighted pooled
CV and matched tracked policies share identical outer evaluation.
**This is a plan, not completed new simulation results.**

## Shared prospective F-weighting method, different decisions

Papers 1 and 2 share the **same underlying PLS \(h\)-step historical
forecast-loss curves** and **method-dependent temporally weighted
surfaces** \(F_r^{(m,d,L,h)}(S)\), defined in
[WEIGHTED_SURFACE_PROTOCOL.md](WEIGHTED_SURFACE_PROTOCOL.md).

- **Paper 1 (Smoothness Cross Validation):** aggregate \(\ell_t(S)\)
  according to \(m\), then select the **global minimum of the latest
  complete** \(F_M^{(m,d,L,h)}(S)\). The original uniform mean
  remains the default baseline.
- **Paper 2 (Dynamic Branch Selection):** for each \((m,d,L,h)\),
  examine **all local minima of each** \(F_r^{(m,d,L,h)}\),
  track their branches chronologically, then apply a prespecified
  branch-selection and post-tracking smoothing rule (e.g. mean of
  last 3 minima). **No internal Val2 required.**
- **Numerical Methods:** supports both papers' numerical minimization
  and tracking diagnostics, but retains its own mathematical question.

The newest **prospective** algorithm is available in
[the weighted-surface experiment module](../experiments/smoothness_cv/weighted_surface_study.py).
Historical checkpoints and the old two-stage branch lab are preserved,
not rewritten or represented as new-method experiments. The existing
manuscripts are working drafts, not synchronized submission versions.

**Three active independent research manuscripts, in priority order:**

1. [Working Paper - Smoothness Cross Validation](Working%20Paper%20-%20Smoothness%20Cross%20Validation/)
2. [Working Paper - Dynamic Branch Selection](Working%20Paper%20-%20Dynamic%20Branch%20Selection/)
3. [Working Paper - Numerical Methods](Working%20Paper%20-%20Numerical%20Methods/)

Each paper has its own thesis, manuscript, bibliography,
experiments, research log and unresolved questions.
These are **not companion articles** and have independent
contributions and evidence.

New active studies use the folder convention
`working_papers/Working Paper - <Title>/`.
Unpromoted ideas and inactive/historical manuscript
snapshots belong under `ideas/`.

Reusable library components and shared datasets can be
used by any manuscript without tying their research claims together.

All paper/PDF builds are manual, not automatic CI jobs.
