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


## First numerical benchmark

Start with:

~~~bash
conda activate trend-estimation
pip install -e .
python experiments/smoothness_recurrence/benchmark_smoothness_search.py --preset smoke
~~~

Then the first broader check is:

~~~bash
python experiments/smoothness_recurrence/benchmark_smoothness_search.py --preset quick
~~~

The default candidate policy keeps at most five local minima and evaluates

~~~text
epsilon = 0.00, 0.02, 0.05, 0.10, 0.15
~~~

where epsilon is a radius in smoothness. For epsilon=0.10, a selected minimum
suppresses worse minima inside a total-width 0.20 neighborhood.

Outputs are written under
`results/smoothness_recurrence/<run-id>/` as
`search_summary.csv`, `candidate_sweep.csv`, and `run_metadata.json`.
