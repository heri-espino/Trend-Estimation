# Smoothness/Recurrence Experiments

Executable entry points for `paper_smoothness-recurrence/`.

Reusable estimator, smoothness, derivative, validation, and recurrence
primitives belong in `src/trend_estimation/`.

## Planned runners

1. `benchmark_smoothness_search.py`
   - adaptive stationary-point search vs. dense GPU/reference grid;
   - correctness, missed roots, regret, evaluation count, runtime.

2. `run_financial_recurrence.py`
   - frozen development/evaluation protocol;
   - select (S_h^\star);
   - forecast frozen trend paths;
   - measure crossing/band recurrence with censoring.

3. `summarize_recurrence.py`
   - paper tables and figure-ready summaries.

## Output policy

Write auditable runs under

`results/smoothness_recurrence/<timestamp>_<experiment>_<git-sha>/`

with raw event-level data, summaries, and `run_metadata.json`.

Expensive experiments remain manual-only, not ordinary push-triggered CI.
