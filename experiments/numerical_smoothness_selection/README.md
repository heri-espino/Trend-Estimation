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
## Adversarial analytic benchmark

Before any larger paper run, use objectives whose stationary structure is known exactly:

~~~bash
python experiments/numerical_smoothness_selection/run_adversarial_benchmark.py --preset smoke
~~~

The adversarial suite includes:

- a minimum at S=0.001;
- a minimum at S=0.999;
- two minima separated by only 0.02;
- two upper-tail minima at 0.97 and 0.995;
- a quartic flat minimum;
- a stationary inflection where F'(S)=0 without a sign change;
- five separated minima;
- exact optima at S=0 and S=1.

The runner compares three methods on exactly the same objective:

1. adaptive_s — the proposed adaptive search on normalized smoothness;
2. log_lambda — the existing stationary-point search on a uniform log(lambda) grid;
3. dense — a dense S-grid reference.

The log-lambda method uses finite bounds induced by the same normalized smoothness range S in [1e-6, 0.9999]. Exact endpoints S=0 and S=1 are still compared explicitly for the global optimum.

After the smoke run is inspected, run:

~~~bash
python experiments/numerical_smoothness_selection/run_adversarial_benchmark.py --preset quick
~~~

The quick preset evaluates all adversarial cases at N in {63,252} and d in {1,2,3,4}, using a 5001-point dense reference and the existing 257-point log-lambda discovery grid.

Outputs:

~~~text
results/numerical_smoothness_selection/<timestamp>_adversarial-<preset>_<sha>/
├── method_summary.csv
├── stationary_detection.csv
├── case_manifest.csv
└── run_metadata.json
~~~

method_summary.csv reports global-optimum error/regret, evaluation count and runtime. stationary_detection.csv records whether each known minimum, flat minimum, boundary optimum or stationary inflection was detected.

Do not tune the proposed method after looking at a paper-scale run. The adversarial quick run is the intended dataset for diagnosing search-design weaknesses and freezing numerical defaults.

