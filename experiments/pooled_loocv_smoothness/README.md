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


## Next, independent misspecified-noise robustness experiment

[Reproducibility ledger](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/RESULTS_LEDGER.md) lists each previous **executed and committed** campaign with its DGP, seeds, location and status. The [robustness protocol](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/ROBUSTNESS_PROTOCOL.md) specifies an **completed and committed exploratory full pilot** that holds the same PLS smoother fixed and tests:

- correctly specified Gaussian errors;
- Student-t(5) measurement noise (finite variance);
- Student-t(5) stochastic-trend innovations;
- stationary AR(1) measurement errors, phi=0.65;
- measurement-noise variance changing across the time series.

Each regime has N=50/200 and observation SD 0.5/2 with innovation SD 0.3, 5 seeds, nested pools R=1/3, for **200 pools and 1000 method rows**. Method pairs see identical observations. *Nominal ratio* is not called an oracle for AR1/heteroskedastic models.

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_guerrero_robustness.py -q
python -m experiments.pooled_loocv_smoothness.run_robustness --preset smoke
python -m experiments.pooled_loocv_smoothness.run_robustness --preset pilot --dry-run
python -m experiments.pooled_loocv_smoothness.run_robustness --preset pilot
```

**Save results for independent analysis:** `results/pooled_loocv_smoothness/guerrero/robustness/pilot/{manifest.json,method_comparison.csv,summary.json,robustness_true_trend_mse_R3.png}`. Inspect the exact pilot manifest and CSV before adding and pushing these specific lightweight files to the **same existing branch**. The pilot results were uploaded and analyzed: see [ROBUSTNESS_PILOT_AUDIT_2026-10-18.md](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/ROBUSTNESS_PILOT_AUDIT_2026-10-18.md). For independent reproducibility **without re-running any simulations**:

```powershell
python -m pytest tests/test_guerrero_robustness_audit.py -q
python -m experiments.pooled_loocv_smoothness.audit_robustness
# Optional manual generation of the two analysis figures
python -m experiments.pooled_loocv_smoothness.audit_robustness --figures
```

Generated audit CSV/JSON/figures are under `results/pooled_loocv_smoothness/guerrero/robustness/pilot/audit/`, and can be committed separately after inspection. Do not launch the 100-seed confirmatory preset or auto-generate heavyweight figures on push. No PRs.


## New extreme tails, centered Gamma, jumps, and GARCH volatility (manual pilot)

The complete [tail stress-test protocol](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/TAIL_NOISE_PROTOCOL.md) and [stepwise Gaussian MLE / LOOCV explanation](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/GAUSSIAN_MLE_AND_LOOCV_EXPLAINED.md) provide precise mathematics and distribution parameters. The new independent runner does **not** touch saved Gaussian or prior robustness campaigns.

It compares Gaussian difference-likelihood, single-start Brent LOOCV, and multibracket Brent LOOCV on **13 distribution settings**: the original eight (Gaussian, t3 observation/innovation, right/left centered Gamma, rare Gaussian jumps, GARCH-t5, Cauchy), plus five centered skew-normal levels **α=-6,-3,0,3,6**, each at matched d=1,2,3. Finite-variance regimes retain true-trend MSE evaluation. **Cauchy has infinite population MSE** and is evaluated using sample-error medians/quantiles, never assigned a Guerrero noise-variance ratio.

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_guerrero_tail_noise.py -q
python -m experiments.pooled_loocv_smoothness.run_tail_noise --preset smoke
python -m experiments.pooled_loocv_smoothness.run_tail_noise --preset pilot --dry-run
python -m experiments.pooled_loocv_smoothness.run_tail_noise --preset pilot
```

The full pilot is **1,560 nested pools × 3 methods = 4,680 rows**. Outputs to `results/pooled_loocv_smoothness/guerrero/tail_stress/pilot/{manifest.json,method_comparison.csv,summary.json}`. The pilot files have now been committed; see [measured audit](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/TAIL_NOISE_PILOT_AUDIT_2026-10-18.md). Run `python -m experiments.pooled_loocv_smoothness.audit_tail_noise` to independently recheck all saved data, or append `--figures` to create three manual order-stratified figures. The confirmatory preset is manual and intentionally unrun. No PRs or heavy Monte Carlo on push.


## Market-return histogram and block-bootstrap noise (new, manual real-data pilot)

The analyst chooses d (default 2) before running any simulation; a single lambda is selected by minimizing **the arithmetic mean of the R observed LOOCV loss functions**. It is not the mean of separately optimized lambda/S values. This project deliberately evaluates retrospective synthetic conditional-mean trend recovery; it does not treat a market price's sample mean as a known true stochastic trend.

The [complete market calibration protocol](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md) describes how actual historical adjusted SPY daily log returns calibrate the empirical zero-mean distribution, how iid histogram bootstrap differs from circular 5/20 trading-day block bootstrap, and why a matched Gaussian noise experiment remains relevant under nonnormal finite-second-moment distributions.

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pip install -e ".[dev,finance]"
python -m pytest tests/test_empirical_market_noise.py -q
python -m experiments.pooled_loocv_smoothness.run_empirical_market_noise --preset smoke
python -m experiments.pooled_loocv_smoothness.run_empirical_market_noise --preset pilot --dry-run
python -m experiments.pooled_loocv_smoothness.run_empirical_market_noise --preset pilot --ticker SPY
```

For the **literal constant historical mean** rather than a time-varying synthetic conditional mean, run a **separate** `python -m experiments.pooled_loocv_smoothness.run_empirical_market_noise --preset pilot --ticker SPY --trend-kind constant_mean --d 1`. This is a zero-trend-innovation boundary case with its own `SPY/d1/constant_mean/pilot/` directory. **Outputs only after the user actually executes the real-data pilot**: `results/pooled_loocv_smoothness/empirical_market_noise/SPY/d2/pilot/` stores `manifest.json`, `method_comparison.csv`, `summary.json`, `empirical_return_histogram_vs_gaussian.png`, `market_return_and_squared_return_acf.png`. Source raw return snapshot remains locally cached and ignored at `data/market_calibration/`; result manifest records its SHA256. Do not assume Yahoo can be reproduced byte-for-byte by later redownload. CSV source is supported via `--source returns_csv --csv ...` or `--source prices_csv --csv ...` for authorized local data. Full Monte Carlo manual-only; tiny synthetic-source smoke in CI. No PR.


## New nonzero-difference-mean simulation: fixed d=2 (unrun full pilot)

The [locked protocol and mathematical derivations](../../working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/NONZERO_DIFFERENCE_MEAN_PROTOCOL.md) compare eight selectors on (D_2\tau=\mu+\varepsilon, y=\tau+\eta), including known true mu and known true variances (ORACLES), two feasible forced-zero-mu selectors, estimated GLS Gaussian differenced-data contrast mean, and exact **fold-reestimated mu** pooled observation LOOCV.

The Gaussian-mean model has variance (aI+bD_2D_2^\top) and common mean (μ\mathbf1). Joint CV profiles one common mu from the data for each lambda; it must be refit within folds. **Guerrero (2007) itself already allows nonzero mean and a simple observed-difference plug-in**. The independent *forecast* mean-difference paper is not affected.

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_nonzero_difference_mean_reconstruction.py -q
python -m experiments.pooled_loocv_smoothness.run_nonzero_difference_mean --preset smoke
python -m experiments.pooled_loocv_smoothness.run_nonzero_difference_mean --preset pilot --dry-run
python -m experiments.pooled_loocv_smoothness.run_nonzero_difference_mean --preset pilot
```

Pilot writes `results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/{manifest.json,summary.json,method_comparison.csv,example_latent_trend_errors.png,mean_shift_true_trend_mse_R3.png}`. N=50/200; sigma eta=.5/2; sigma epsilon=.3; mu/sigma epsilon=-1,-.25,0,.25,1; a Guerrero-style **pooled observed-difference mean plug-in hybrid** included; 5 shared-shock seeds; nested R1/3 => 200 pools, 1600 method rows. Check carefully before adding only these three result files; do not use `git add .`. Full independent confirmatory preset remains manual/unrun.
