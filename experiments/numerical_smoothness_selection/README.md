# Numerical smoothness selection experiments

This directory belongs to the **active** paper_numerical-smoothness-selection/ paper.
Reusable numerical logic stays in src/trend_estimation/.

## Experimental order

Start with synthetic series. The numerical paper needs controlled objective surfaces before any financial stress test.

The sequence is:

1. synthetic smoke run;
2. inspect disagreements/minima;
3. synthetic quick run across more d, L, h configurations and regimes;
4. harden the stationary-point search if needed;
5. freeze numerical defaults;
6. only then use selected financial series as real-objective stress tests.

Financial forecasting comparisons and recurrence analysis belong to the parked applied paper, not this experiment namespace.

## Synthetic benchmark

~~~bash
python experiments/numerical_smoothness_selection/run_synthetic_benchmark.py --preset smoke
~~~

The smoke preset contains 8 cases:

- seed: 0;
- scenario: baseline local-linear trend + AR(1) noise;
- d in {1,2};
- L in {63,126};
- h in {1,5};
- dense reference: 401 points on the exact domain S in [0,1].

It compares the adaptive stationary-point search against a dense reference and explicitly compares the exact endpoints S=0 and S=1.

After inspecting smoke results, run:

~~~bash
python experiments/numerical_smoothness_selection/run_synthetic_benchmark.py --preset quick
~~~

The quick preset expands to:

- seeds 0, 1, 2;
- baseline and persistent-noise scenarios;
- d in {1,2,3,4};
- L in {63,126,252};
- h in {1,5,20};
- dense reference: 2001 points.

Do **not** run the paper preset before smoke and quick results have been inspected.

## Outputs

Each run writes to:

~~~text
results/numerical_smoothness_selection/<timestamp>_synthetic-<preset>_<sha>/
~~~

with:

- search_summary.csv — one row per numerical surface;
- candidate_sweep.csv — epsilon-separated interior minima;
- run_metadata.json — full reproducibility metadata.

Important summary columns include:

- adaptive_best_s / dense_best_s;
- adaptive_best_source (interior, S=0, or S=1);
- best_s_abs_error;
- objective_regret;
- adaptive_evaluations / dense_evaluations;
- dense interior minima matched/missed;
- adaptive_seconds / dense_seconds.

Commit the result directory after each scientifically relevant run so it can be inspected from another machine.
