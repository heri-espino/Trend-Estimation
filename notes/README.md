# Research Notes

This directory is the internal scientific notebook for `Trend-Estimation`.

It is intentionally separate from the manuscripts. Papers contain only the final argument and evidence; `notes/` records derivations, decisions, caveats, failed ideas, checkpoints, and implementation mappings so the research can be reconstructed later.

## Required structure for mathematical notes

Every note describing a mathematical result should include:

1. **Question** — what problem the result answers.
2. **Assumptions** — exact model and notation.
3. **Derivation** — enough steps to audit the result.
4. **Result** — boxed or otherwise clearly stated.
5. **Interpretation** — what the result means.
6. **Library mapping** — exact files/functions using the result.
7. **Status** — derived / implemented / tested / used in experiments.
8. **Open issues** — what remains uncertain.

## Current notes

- `research_objective.md` — **first scientific source of truth**: canonical
  objective, full adaptive object ((d,L,S)), experiment hierarchy, scope, and
  anti-drift rules.
- `key_results.md` — compact canonical result sheet.
- `derivative.md` — forecast-loss derivatives for the pure penalized trend.
- `numerical_selection.md` — stationary-point search in log-\(\lambda\).
- `model_definitions.md` — exact estimator definitions and Guerrero-model audit.
- `roadmap.md` — active-paper roadmap and rationale.
- `window_and_smoothness.md` — why fixed \(\lambda\) is not fixed smoothness when sample length changes.
- `nested_validation.md` — leakage-free outer/inner rolling evaluation and no-change benchmark.

When a result graduates into the public API, keep the note and update its library mapping rather than deleting the derivation.


## Checkpoints

- `checkpoints/2026-09-21_forecast-optimal-foundation.md` — foundation complete enough to begin controlled simulation runs.
- `checkpoints/2026-09-21_repository-cleanup.md` — library-first cleanup, naming, editable install, and Sphinx documentation.


- `checkpoints/2026-09-21_first-paper-simulation-run.md` — first full simulation grid, initial scientific patterns, and numerical diagnostics.

- `checkpoints/2026-09-21_first-paper-simulation-results.md` — first paper-scale simulation run and preliminary aggregate findings.

- `experiments/02_persistence-horizon-mechanism.md` — mechanism study separating observed forecasting, latent forecasting, AR-aware forecasting, and recovery.
- `experiments/03_search-boundary-sensitivity.md` — controlled wide-domain rerun that tests whether Explore-02 boundary optima are numerical truncation or genuine limiting choices.
- `experiments/04_within-series-persistence-regime-transition.md` — paired stationary controls and within-series persistence changes for measuring joint (d, L, S) adaptation.
- `experiments/04b_selector-memory-sensitivity.md` — isolates how inner rolling-validation memory controls adaptation delay and forecast variance.
- `experiments/05_adaptive-vs-frozen-pre.md` — tests whether repeated adaptation of (d, L, S) improves untouched OOS forecasts relative to hyperparameters frozen at T0.
- `experiments/06_observation-noise-scale-adaptation.md` — isolates observation-noise-scale changes while jointly measuring configuration tracking and adaptation value.
- `experiments/07_latent-trend-roughness-adaptation.md` — isolates latent slope roughness while jointly measuring configuration tracking and adaptation value.

- `checkpoints/2026-09-22_persistence-mechanism-results.md` — mechanism-study results, decomposition, and search-boundary caveat.
- `checkpoints/2026-09-22_scientific-objective-clarification.md` — records the
  correction from a persistence-centered reading to the full adaptive
  forecasting objective.
- `checkpoints/2026-09-22_boundary-sensitivity-prepared.md` — verifies the completed Explore-02 run and records the exact wide-domain diagnostic that comes next.
- `checkpoints/2026-09-22_search-boundary-sensitivity-results.md` — Exploration 03 PASS; the persistence/horizon mechanism survives the wider search domain.
- `checkpoints/2026-09-23_regime-transition-results.md` — Exploration 04 PASS; the full selected configuration tracks regime changes, with selector-memory sensitivity required next.
- `checkpoints/2026-09-23_selector-memory-results.md` — Exploration 04B PASS; M=20 is frozen for the next stage, with M=30 retained for robustness.
- `checkpoints/2026-09-23_adaptive-value-persistence-results.md` — Exploration 05: adaptive beats frozen-pre directly at every studied persistence transition/horizon; transition-specific excess value is conditional, with M=30 robustness next.
- `checkpoints/2026-09-23_persistence-adaptation-robustness.md` — M=30 preserves the M=20 persistence conclusion; persistence is closed for the exploratory stage.
- `checkpoints/2026-09-23_noise-scale-adaptation-results.md` — observation-noise scale is a second regime mechanism; configuration tracking is clear but forecast value is strongly directional.
