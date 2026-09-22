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
