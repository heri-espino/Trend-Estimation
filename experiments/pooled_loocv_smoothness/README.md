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
