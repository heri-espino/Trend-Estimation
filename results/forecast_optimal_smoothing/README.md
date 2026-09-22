# Forecast-optimal smoothing results

This directory contains **lightweight, reproducible numerical outputs** from the
active forecast-optimal-smoothing study.

Each run is stored in its own directory:

```text
<timestamp>_<preset>_<git-sha>/
├── simulation_grid.csv
├── summary.csv
└── run_metadata.json
```

## What should be committed

Commit CSV/JSON outputs that are needed to audit, compare, or write the paper.
These files are intentionally small enough to review through GitHub.

Do not commit large caches, serialized Python objects, environment folders, or
generated binary artifacts here. If a future experiment produces large raw
objects, keep those outside Git and commit only the analysis-ready tabular
result plus metadata.

## Reproducibility rule

A result is considered interpretable only if its run directory includes
`run_metadata.json`. The metadata identifies the code commit and all principal
experiment arguments.

## Analysis workflow

After a school/lab machine finishes a run:

```bash
git status
git add results/forecast_optimal_smoothing
git commit -m "results: add forecast-optimal smoothing run"
git push
```

Once pushed, collaborators can inspect the exact output from GitHub without
moving files through another channel.
