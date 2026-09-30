> **Historical pre-split note (2026-09-29).** This file predates the separation into three research papers. It is preserved for provenance but is **not** the current source of truth. For the applied paper use README.md, notes/research_objective.md, notes/scope.md, notes/roadmap.md, and notes/decisions.md. Numerical smoothness-search material belongs to ../paper_numerical-smoothness-selection/.

# Results

Last updated: 2026-09-29

## Rule

Only results produced under this paper's documented protocol belong here.
Do not copy favorable numbers from the adaptive paper as recurrence-paper
results.

## Existing reusable infrastructure

The shared library already provides:

- pure finite-difference penalized trends;
- cached penalty eigenvalues and normalized smoothness conversion;
- chronological rolling-origin forecast objectives;
- analytic first/second forecast-loss derivatives in (lambda);
- Brent-based stationary-point refinement;
- dense-grid infrastructure from earlier work;
- tracked financial snapshots and reproducible result metadata.

These are implementation assets, not empirical findings of this paper.

## Paper-specific empirical results

**None yet.**

The first required result is numerical: show that the smoothness-domain
adaptive stationary-point search recovers the dense/reference optimum with
substantially fewer evaluations.

## Required result record

Each result must include:

- date;
- Git commit;
- command;
- data panel/date range;
- frozen protocol;
- result directory;
- main numerical/statistical result;
- caveats;
- whether it changes a paper claim.
