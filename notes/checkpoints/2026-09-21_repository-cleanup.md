# Checkpoint — Repository Cleanup and Library Documentation

Date: 2026-09-21

## Goal

Make `Trend-Estimation` behave like a real reusable Python library rather than
a collection of historical scripts and draft manuscript folders.

The supported development workflow is now:

```bash
pip install -e .
```

The pip distribution is `trend-estimation`; the import package is
`trend_estimation`; source code lives in `src/trend_estimation/`.

## Cleanup completed

The following historical/draft material was removed from `main`:

- `legacy/`;
- `reportes/`;
- the old generic `paper/` S&P 500 draft, including generated figures/data/tables;
- old copied experiments for multiple-minima and time-weighted validation;
- the old synthetic benchmark experiment;
- empty planned namespaces for multivariate, segmented, and noise models;
- unimplemented selector placeholders for CV/GCV/AICc/BIC;
- unused alias/wrapper modules.

Nothing was erased from Git history.

## Naming cleanup

Examples of names made explicit:

- `paper_forecast-optimal-smoothing/` — active manuscript;
- `paper_penalized-trend-tutorial/` — tutorial manuscript;
- `train_validation.py` instead of `train_val.py`;
- `test_pure_penalized.py` instead of `test_pure_penalized_v2.py`;
- public trend classes are explicit:
  `PurePenalizedTrend`, `GuerreroTrend`, `IteratedDriftTrend`,
  `HPTrend`, and `WhittakerTrend`;
- the configurable drift implementation is internal as
  `models/_drift_penalized.py`, not a vague public `PenalizedTrend`.

## Sphinx documentation

A new Sphinx site under `docs/` is now the canonical user-facing library
documentation.

Its root index links to:

- installation;
- quick start;
- repository structure;
- model guide;
- forecasting guide;
- smoothness-selection guide;
- simulation guide;
- API reference by subsystem;
- research-workflow explanation.

The API reference is generated from the public Python objects and their
docstrings, so a user does not need to search source files just to discover
function signatures or classes.

Build locally with:

```bash
pip install -e ".[dev,docs]"
sphinx-build -W -b html docs docs/_build/html
```

## Separation of documentation roles

There are now three intentionally different documentation layers:

1. `docs/` — public Sphinx documentation for using the library;
2. `notes/` — internal derivations, checkpoints, caveats, and research plan;
3. `paper_<short-title>/` — final manuscript argument and results.

This avoids mixing API documentation with derivation notebooks or paper prose.

## CI policy

Automatic CI remains lightweight. It checks:

- editable installation;
- public import/version;
- unit tests;
- Sphinx documentation build with warnings treated as errors.

Paper/PDF compilation remains manual-only via `workflow_dispatch`.

## Current clean top-level structure

```text
.github/
docs/
examples/
experiments/
literature/
notes/
paper_forecast-optimal-smoothing/
paper_penalized-trend-tutorial/
src/
tests/
.gitignore
AI_HANDOFF.md
LICENSE
README.md
environment.yml
pyproject.toml
```

## Next repository work

Repository architecture is no longer the bottleneck. Further changes should be
driven by actual library needs from the active research:

1. improve docstrings whenever a public object is touched;
2. add API pages only when new public subsystems are introduced;
3. avoid creating placeholder modules for hypothetical future work;
4. keep experiment-specific code outside `src/`;
5. keep reusable methods inside `src/trend_estimation/`;
6. preserve derivations in `notes/`;
7. keep generated outputs out of Git unless they are deliberately curated.

The next substantive work should return to numerical stress tests and controlled
simulations rather than adding more repository scaffolding.
