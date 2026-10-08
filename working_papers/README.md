# Working papers

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
