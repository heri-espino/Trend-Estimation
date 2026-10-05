# Smoothness-CV paper experiments

This directory contains paper-specific empirical code for paper_smoothness-cv/.

Reusable estimator mathematics remains in src/trend_estimation/. This folder
owns only the experimental design, frozen presets, paper-specific outputs, and
figure/table construction.

## Current checkpoint

### Checkpoint 01 — empirical core

Goal:

1. compare horizon-matched forecast-CV with one-step forecast-CV;
2. compare both with CV, GCV, AICc, and BIC;
3. compare forecast-optimal smoothness with a latent-trend recovery oracle in simulation;
4. generate the first manuscript figures and comparison tables.

The baseline paper configuration is intentionally fixed at a given
difference order d, window length L, and horizon h. This experiment does
not jointly tune (d, L, S).

## Run order

From the repository root:

~~~bash
conda activate trend-estimation
pip install -e .
pytest
~~~

First run the smoke checkpoint:

~~~bash
python experiments/smoothness_cv/run_checkpoint_01.py --preset smoke
~~~

Then build its figures and tables:

~~~bash
python experiments/smoothness_cv/make_checkpoint_01_figures.py
~~~

If the smoke run passes, run the exploratory quick design:

~~~bash
python experiments/smoothness_cv/run_checkpoint_01.py --preset quick
python experiments/smoothness_cv/make_checkpoint_01_figures.py
~~~

Do not run the paper preset yet unless the checkpoint has been reviewed.
The paper preset is intentionally much larger and should be frozen only after
the smoke/quick outputs are inspected.

## Output location

Each run creates a versioned directory:

~~~text
results/smoothness_cv/checkpoint_01/
└── <timestamp>_<preset>_<git-sha>/
    ├── results.csv
    ├── objective_curves.csv
    ├── series_examples.csv
    ├── horizon_matching.csv
    ├── summary.csv
    ├── run_metadata.json
    └── paper_artifacts/
        ├── artifact_manifest.json
        ├── figures/
        └── tables/
~~~

LATEST.txt points to the most recent run.

Results are intentionally versionable. After a successful checkpoint run, push
the complete run directory to the repository so another agent can inspect the
exact outputs without asking for local files.

## Selectors in Checkpoint 01

- forecast_cv_h — proposed horizon-matched future-block criterion;
- forecast_cv_1 — one-step rolling forecast criterion, then forecast at h;
- cv — ordinary leave-one-out linear-smoother CV;
- gcv — generalized cross-validation;
- aicc — corrected Akaike criterion in the PLS form used by Cortés-Toto et al.;
- bic — Bayesian information criterion in the same PLS comparison;
- recovery_oracle_train — simulation-only oracle minimizing latent-trend recovery MSE on the current training window.

The classical selector formulas live in
src/trend_estimation/selection/classical.py and are reusable/tested library
code.

## Checkpoint 01 figures

The artifact builder currently creates:

1. fig01_s_lambda — normalized smoothness versus penalty;
2. fig01b_edf_s — exact effective-degrees-of-freedom interpretation;
3. fig02_objective_curves — representative horizon-specific forecast-loss curves;
4. fig03_selected_s_by_horizon — distribution of selected smoothness versus horizon;
5. fig04_forecast_vs_recovery — forecast-optimal versus recovery-optimal smoothness;
6. fig05_method_comparison — forecast error relative to GCV;
7. fig06_horizon_matching — horizon-matched versus one-step tuning.

These are checkpoint figures, not automatically final manuscript figures.
After reviewing the quick run, we will decide which displays survive into the
Journal of Forecasting submission.

## Frozen information rule

At outer forecast origin T:

- fitting uses only observations at or before T;
- all inner forecast-CV origins lie strictly inside the historical information set;
- future observations are used only for scoring;
- latent-trend information is used only by the simulation oracle, never by the proposed selector;
- final test performance must not be used to retune the experiment design.

## Stop condition

After smoke or quick completes, stop and push the outputs. The next
checkpoint should be chosen only after inspecting:

- whether all selectors return sensible smoothness values;
- whether horizon-matched and one-step tuning actually differ;
- whether forecast-optimal and recovery-optimal smoothness separate in useful scenarios;
- whether the classical selector comparison is numerically stable;
- whether the proposed figures expose the intended mechanisms.

Do not scale to the paper preset before that review.
