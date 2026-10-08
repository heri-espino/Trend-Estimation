# Chronological Smoothness-CV experiment infrastructure

Also see the [full-sample source-paper factorial runner](run_cortes_toto_replication.py):
the original Cortés-Toto 2^4 CV/GCV/AICc/BIC experiment is
reproduced on full N=50/200 sequences, **separately from new
rolling-window forecast experiments**, with seed-level reports and
raw/normalized smoothness.

## Prospective 2026-10-08 high-throughput simulation campaign

**New**: [CAMPAIGN_README.md](CAMPAIGN_README.md) documents 528
factorial scenario cells, reproducible DGPs, up to 32 CPU workers,
SQLite checkpoint/resume, memory-bounded reports and regeneration
of true trend/noise/weighted-F curves. This explicitly implements
the shared [two-paper simulation protocol](../../working_papers/SIMULATION_EVALUATION_PROTOCOL.md).
It has **not** been executed and does **not** alter historical CP01–CP08
results.



This versioned namespace holds both pooled-future-block experiments (historical CP01–CP03, now documented under `working_papers/Working Paper - Smoothness Cross Validation/`) and dynamic minimum/branch experiments (historical CP04–CP08, documented under `working_papers/Working Paper - Dynamic Branch Selection/`). Scientific claims, notes and manuscripts are independent; the same shared code is not evidence of a common research question.

Reusable estimator mathematics remains in src/trend_estimation/. This folder
owns only the experimental design, frozen presets, paper-specific outputs, and
figure/table construction.

## Critical fit-select-refit semantics

This experiment uses nested chronological logic:

1. inner rolling folds evaluate each candidate smoothness \(S\) using historical pseudo-out-of-sample forecast loss;
2. those losses are averaged and the minimizing \(\widehat S_{T,h}\) is selected;
3. fold-specific fits are discarded;
4. the trend is freshly refit on `history[-window:]`, i.e. the most recent \(L\) observations available at the current outer origin;
5. that refitted trend is extrapolated into the untouched outer future block.

The folds average losses, not trends. Never keep the last inner-fold trend as the outer forecast model. Never withhold information that is already available at the outer origin merely because it was previously used as validation data at an earlier origin.

Canonical explanation: `working_papers/Working Paper - Smoothness Cross Validation/notes/validation_semantics.md`.
## Current checkpoint

### Checkpoints 01–02 complete; Checkpoint 03 is the active frozen paper simulation

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
python experiments/smoothness_cv/analyze_checkpoint_01.py
~~~

Then build its figures and tables:

~~~bash
python experiments/smoothness_cv/make_checkpoint_01_figures.py
~~~

If the smoke run passes, run the exploratory quick design:

~~~bash
python experiments/smoothness_cv/run_checkpoint_01.py --preset quick
python experiments/smoothness_cv/analyze_checkpoint_01.py
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
