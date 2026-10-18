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
