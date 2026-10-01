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

## Frozen-search sensitivity benchmark

The primary adaptive search is frozen under Decision N009. Sensitivity runs are
therefore robustness analyses only; they must not retune the primary method.

Run:

~~~bash
python experiments/numerical_smoothness_selection/run_search_sensitivity.py --preset paper
~~~

The analysis varies one factor at a time around the frozen specification:

- initial grid size;
- maximum adaptive depth;
- endpoint refinement levels;
- minimum interval width;
- near-zero derivative ratio.

Each alternative is evaluated on the same synthetic surfaces and against the
same dense reference. The primary specification appears once as a control.

Outputs:

~~~text
results/numerical_smoothness_selection/<timestamp>_sensitivity-paper_<sha>/
├── sensitivity_summary.csv
├── sensitivity_cases.csv
└── run_metadata.json
~~~

The main robustness endpoints are missed minima, positive-regret cases,
selected-\(S\) error, evaluation count, and runtime. A sensitivity setting is
not allowed to replace the frozen primary specification after seeing these
results.

## Financial geometry stress test

After the frozen synthetic/adversarial validation and OFAT sensitivity analysis,
the final external geometry check uses only tracked financial snapshots.

Run:

~~~bash
python experiments/numerical_smoothness_selection/run_financial_stress_test.py --preset paper
~~~

The frozen panel contains six daily series:

- SPY and QQQ (ETFs);
- AAPL and XOM (stocks);
- BTC-USD and ETH-USD (crypto).

The experiment uses the final 2000 positive observations of each tracked
adjusted-price snapshot and transforms prices as

\[
x_t=\log P_t.
\]

For every series it evaluates

\[
d\in\{1,2,3,4\},\qquad
L\in\{63,126,252,504\},\qquad
h\in\{1,5,20,60\},
\]

using the frozen adaptive search and a 5001-point dense reference. This produces
384 real-data objective surfaces.

This is **not** a financial forecasting model comparison. It asks only whether
the numerical search continues to recover the relevant minima on objective
surfaces generated by real market data.

The runner never downloads data. It reads the versioned snapshots under
data/external/real_world/snapshot/yahoo and records SHA-256 hashes in the run
metadata.

Outputs:

~~~text
results/numerical_smoothness_selection/<timestamp>_financial-stress-paper_<sha>/
├── search_summary.csv
├── stationary_points.csv
└── run_metadata.json
~~~

## Generate frozen manuscript evidence

After all principal numerical experiments are complete, generate the manuscript
tables and figures directly from the frozen result directories:

~~~bash
python experiments/numerical_smoothness_selection/generate_paper_evidence.py
~~~

This writes into the active paper directory:

~~~text
paper_numerical-smoothness-selection/
├── tables/
│   ├── benchmark_summary.csv
│   ├── benchmark_summary.tex
│   ├── sensitivity_summary.csv
│   └── sensitivity_summary.tex
└── figures/
    ├── evaluation_efficiency.pdf
    ├── optimum_agreement.pdf
    └── sensitivity_tradeoff.pdf
~~~

The generator intentionally references the exact frozen adversarial, synthetic,
sensitivity, and financial result directories. If any frozen input is missing,
it fails rather than silently substituting another run.



## Applied multiple-minima case studies

After the numerical search is frozen, interpret the local forecast-CV minima on
four pre-specified tracked series: GDPC1, SPY, AAPL, and BTC-USD.

Run:

~~~bash
python experiments/numerical_smoothness_selection/run_applied_case_studies.py --preset paper
~~~

After an updated applied run has created the long-horizon diagnostic CSVs,
presentation-only changes can be regenerated from that run without repeating
selection:

~~~bash
python experiments/numerical_smoothness_selection/run_applied_case_studies.py \
  --figures-from-run results/numerical_smoothness_selection/<updated-applied-run>
~~~

Older applied runs created before the long-horizon diagnostic was added do not
contain those CSVs and therefore need one fresh `--preset paper` run first.

The experiment reserves the final test block before any configuration or
candidate search: 8 quarters for GDP and 60 observations for daily market
series.

All \((d,L,h)\) scanning, local-minimum discovery, candidate spacing, and
example selection use development data only. The final test block is diagnostic
only.

Outputs:

~~~text
results/numerical_smoothness_selection/<timestamp>_applied-paper_<sha>/
├── case_selection.csv
├── configuration_scan.csv
├── candidate_results.csv
├── objective_profiles.csv
├── applied_paths.csv
├── long_horizon_order_selection.csv
├── long_horizon_order_candidates.csv
├── long_horizon_order_paths.csv
├── temporal_split_protocol.csv
├── temporal_split.pdf
├── applied_case_studies.pdf
└── run_metadata.json
~~~

`temporal_split.pdf` shows the full chronology for each applied series. The
development region and final refit window are shaded separately, every rolling
validation block is represented in a narrow protocol strip with its forecast
origin marked, and the final reserved test block is kept visually distinct.
Because validation is rolling-origin, it is deliberately not drawn as one
fixed validation interval. `temporal_split_protocol.csv` records the exact
date boundaries used to construct the figure.

The main applied figure remains a 4-by-3 panel. Its first two columns retain
the selected forecast-CV profile and the fitted trends implied by its recovered
minima. The third column is now a long-horizon visual diagnostic over
`d=1,2,3,4`: for each order, the full pre-reserved test length is used as the
forecast horizon, the training window is chosen by development-only rolling CV,
and up to three epsilon-separated smoothness candidates are plotted. Observed
training and test values are always blue; forecasts use red for `d=1`, green
for `d=2`, purple for `d=3`, and orange for `d=4`. Within each order,
larger smoothness is rendered with a more saturated version of the same hue.

The third-column vertical limits are computed only from the displayed observed
training tail and observed test block. Forecasts that diverge for large
difference orders are therefore clipped by the plotting window rather than
compressing the observed series into an unreadable scale.

The validation ranking is the actual selection ranking. The test ranking and
all long-horizon test paths are retrospective diagnostic information only. They
do not permit selecting an order, window, or smoothness from the test block.

The candidate set is a selection-sensitivity diagnostic, not a confidence
interval or probability distribution over smoothness.
