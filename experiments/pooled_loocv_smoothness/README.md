# Pooled observed-series LOOCV experiments

Independent computational companion to [the working paper](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/README.md).

## Setup and commands

From repository root:

    python -m pip install -e ".[dev,symbolic]"
    python -m pytest tests/test_pooled_loocv_smoothness.py -q
    python -m experiments.pooled_loocv_smoothness.run --preset smoke --dry-run
    python -m experiments.pooled_loocv_smoothness.run --preset smoke --out-dir results/pooled_loocv_smoothness/smoke
    python -m experiments.pooled_loocv_smoothness.run --preset pilot --dry-run
    python -m experiments.pooled_loocv_smoothness.sturm_exact

After inspecting smoke results, opt in manually to a run of the 16-cell pilot:

    python -m experiments.pooled_loocv_smoothness.run --preset pilot --out-dir results/pooled_loocv_smoothness/pilot

The 100-replicate confirmatory preset is intentionally not launched here; launch only when pilot code/novelty/audit are reviewed.

## Artifacts written on actual execution

- solver_comparison.csv: per-scenario/replicate/pool/method selected normalized S and λ, score, method evaluations and runtime.
- manifest.json: preset, seeds, algorithm budgets, versions, git commit and execution metadata.
- example_signal_and_objective.png: explanatory source-inspired signal/trend and pooled LOOCV landscape.
- example_loss_curve.csv: corresponding finite sampled curve for independent inspection.

Solver comparisons use the **same observed pool**. Methods do not include forecasting, and their numerical reference is a finite dense grid, not ground-truth root completeness. The optional exact rational script counts/isolate positive stationary roots for **tiny instances only**.

## Decisions

- Factorial baseline from Cortés-Toto et al. (2017): shape, seasonality, σ, N. Fixed d=2.
- R=1 is classical ordinary CV; R=3 adds cross-series pooling. Same latent signal within each pool; independent Gaussian errors conditional on it.
- λ optimized numerically (in log λ) and transformed to normalized S∈[0,1]; both exact endpoints included.
- No change to any existing forecast method or manuscript.


## Optional retrospective financial series example

Supply a local CSV containing a column of prices or an index level. The script **does not download data**, and never predicts future values:

    python -m experiments.pooled_loocv_smoothness.finance_case --csv data/local_prices.csv --columns close --date-column date --transform log-level --out-dir results/pooled_loocv_smoothness/finance

For comparable pooled **separate** financial series with different levels or currencies, standardize explicitly:

    python -m experiments.pooled_loocv_smoothness.finance_case --csv data/local_prices.csv --columns index1 fx_rate --date-column date --transform log-level --standardize --out-dir results/pooled_loocv_smoothness/finance_pooled

Available transformations are level, log-level and log-return. The latter changes the *target* to the return series. Rows with missing values in any chosen column are dropped before pooling. Consecutive observations are treated as equally spaced **trading observations**, not calendar days. Financial series can have autocorrelated errors, outliers, holidays and breaks; classical LOOCV is an exploratory reconstruction criterion, not proof of an appropriate trading or forecasting model. Output includes financial_case.json, financial_loss_curve.csv and financial_reconstruction.png; original CSV data are never copied into the results directory.


## Audit the saved pilot

Once `solver_comparison.csv` is present from an actual run or GitHub pull, compute a deterministic paired summary:

    python -m experiments.pooled_loocv_smoothness.audit_pilot --csv results/pooled_loocv_smoothness/pilot/solver_comparison.csv --out results/pooled_loocv_smoothness/pilot/audit_summary.json

Read the [2026-10-18 pilot audit](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/PILOT_AUDIT_2026-10-18.md) before selecting heavier experiments; its detected root counts are **not exact** and not an automatic count of distinct minima.


## New Guerrero known variance-ratio benchmark (separate stochastic DGP)

Unlike the original 2017-inspired deterministic-trend simulation, this experiment generates independent **stochastic** integrated trends from `D_2 tau = epsilon` with known process noise variance and observations `y = tau + eta` with known observation noise variance. The Guerrero known-parameter benchmark chooses `lambda_G = sigma_eta^2 / sigma_epsilon^2`. Compare it with pooled LOOCV selected by Brent, multibracket Brent, and a dense-grid reference; evaluate both observed LOOCV and true latent-trend MSE. Read the [source-grounded protocol](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/GUERRERO_VARIANCE_RATIO_PROTOCOL.md).

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_guerrero_ratio_pooled_loocv.py -q
python -m experiments.pooled_loocv_smoothness.guerrero_ratio --preset smoke
python -m experiments.pooled_loocv_smoothness.guerrero_ratio --preset pilot --dry-run
python -m experiments.pooled_loocv_smoothness.guerrero_ratio --preset pilot
```

Smoke: 8 pools × 4 methods = 32 saved rows. Pilot: 12 settings × 5 independent seeds × 2 nested pool sizes = **120 pools**, 480 saved rows. Results go under `results/pooled_loocv_smoothness/guerrero/{smoke,pilot}/`, separate from the completed Cortés-Toto pilot. Outputs: `guerrero_solver_comparison.csv`, `summary.json`, `manifest.json`, `guerrero_example.png`, `guerrero_example_curves.csv`. The 100-seed confirmatory preset is manual, and no forecasts are used.


## Reproduce the completed Guerrero pilot audit and figures

The first Guerrero 12-scenario pilot was executed and uploaded on 2026-10-18 local date. The observed scores were audited in [the paper's dedicated pilot analysis](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/GUERRERO_RATIO_PILOT_AUDIT_2026-10-18.md). This does **not** re-run simulations:

```powershell
python -m experiments.pooled_loocv_smoothness.audit_guerrero_pilot
```

It reads the saved per-method CSV and writes `paired_pool_contrasts.csv`, `scenario_by_R_summary.csv`, `audit_summary.json`, and two figures into `results/pooled_loocv_smoothness/guerrero/pilot/audit/`. It keeps R=1 and R=3 separately because their first series is shared and reports 12 scenarios with only five independent seeds each. The charts show per-scenario true trend reconstruction MSE and paired changes in the two fundamentally different loss functions. No multiple-minimum claim is inferred from a stationary-root count.


## Completed feasible variance-estimation pilot (2026-10-18)

The distinct 12-cell **estimated** noise-variance pilot was executed and committed. See the [detailed audit](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/VARIANCE_ESTIMATION_PILOT_AUDIT_2026-10-18.md). In particular, distinguish four methods: Guerrero's known-variance ratio (oracle), our Gaussian ML estimator on differenced observations, our NNLS quadratic-moment estimator, and bounded-Brent observed LOOCV.

A lightweight test checks the complete uploaded CSV, while the three figure outputs are intentionally **manual-only**:

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_estimated_variance_audit.py -q
python -m experiments.pooled_loocv_smoothness.audit_variance_estimation
git status
```

The manual audit writes under `results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/audit/`: a structured summary JSON, R=3 scenario CSV, comparison figure, moment-failure figure and ML variance-component-error figure. Do not interpret the 120 nested pool evaluations as 120 independent seeds; the primary descriptive comparison uses 60 R=3 pools.

Important empirical boundary: the constrained moments method reached innovation variance zero, and hence lambda=+infinity, in 16/60 R=3 and 19/60 R=1 pools. These are preserved failures, not silently regularized.
