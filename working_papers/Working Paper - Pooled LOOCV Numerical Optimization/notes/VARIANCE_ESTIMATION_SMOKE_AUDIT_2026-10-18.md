# Feasible variance-component estimation — first measured smoke

**Date of analysis:** 2026-10-18 local (CI execution UTC 2026-10-19).
**Source:** [Pooled LOOCV checks run 39190179377](https://github.com/heri-espino/Trend-Estimation/actions/runs/39190179377), specifically the executed step *Execute feasible variance estimator smoke and verify artifacts*. **Status:** exploratory smoke only, **not** an executed 12-scenario pilot or confirmatory analysis.

The CI tests and variance-estimation smoke completed successfully. Its generated CSV/figures were verified in temporary runner storage; they are **not** necessarily committed. Run locally with the documented commands and commit intended experiment outputs to retain them.

## What the methods actually mean

1. **Guerrero known ratio**: \(\lambda_G=\sigma_\eta^2/\sigma_\varepsilon^2\) supplied with true simulation variances. *Oracle, not deployable.*
2. **Estimated Gaussian differences**: estimate both components from \(z=D_2y\), using \(\operatorname{Var}(z)=aI+bD_2D_2^\top\). This is an **extension to Guerrero**, not the MLE proposed in his paper. The optimizer profiles likelihood of *differenced observations*, not the complete likelihood of \(y\).
3. **Estimated quadratic moments + NNLS**: another feasible extension recovering both variance components from two quadratic moments and constraining nonnegativity. May choose a zero variance and force \(\lambda=\infty\), severely oversmoothing an actually stochastic trend.
4. **LOOCV bounded Brent**: directly minimize observed-series reconstruction LOOCV, not estimating a two-variance model.

All procedures use the same PLS smoother after selecting \(\lambda\). Every trend MSE shown below evaluates a simulated latent truth, never used by the feasible methods.

## Tiny smoke: N=24, sigma_epsilon=0.25, sigma_eta 0.5 or 2.0

Two seeds per setting, nested R=1 and R=3 pools. **Only 4 R=3 pools** provide the primary display. No significance or model-performance claim is justified.

| Method | R=3 mean observed LOOCV MSE | R=3 mean true trend MSE | R=3 lambda=infinity selections |
|---|---:|---:|---:|
| Guerrero known variance ratio | 3.142535 | **0.270613** | 0 |
| Feasible Gaussian difference-likelihood | 3.033434 | 0.278373 | 1 |
| Feasible constrained quadratic moments | 3.776587 | 0.838703 | 2 |
| Feasible LOOCV bounded Brent | **2.996781** | 0.293249 | 0 |

**R=1 separately (4 pools):** mean true trend MSE was 0.321667 (known ratio), 0.335728 (Gaussian difference ML), 0.511812 (constrained moments) and 0.339630 (LOOCV). The Gaussian estimator chose lambda=infinity in one case; the moment method did so in two.

**Interpretation:** in these particular four three-series pools, feasible Gaussian variance estimation comes relatively close to the known-parameter oracle on true trend MSE, and is better on mean true trend MSE than LOOCV, but only as a small descriptive sample. The nonnegative moment method is much less stable and demonstrates a practical boundary failure: estimated innovation variance zero yields an infinite ratio and a fully polynomial trend. LOOCV continues to attain a lower *observed* CV score, which is a different target.

The smoke's mean absolute variance-component errors under R=3:
- Gaussian differences: observation-noise variance 0.648132; innovation-noise variance 0.040376.
- Constrained moments: observation-noise variance 0.787835; innovation-noise variance 0.037141.

Raw errors combine heterogeneous true variance levels; in the **pilot**, use relative errors, scenario-specific rows, boundary-hit rates and paired true trend MSE. Report both R sizes but never treat nested R1 and R3 as 8 independent draws.

## What to test next

The executable experiment already covers 12 scenario cells:
\(N\in\{50,200\}\), \(\sigma_\eta\in\{0.5,2\}\),
\(\sigma_\varepsilon\in\{0.1,0.3,1\}\), 5 seeds per cell and nested R=1/3,
giving 120 pools and 480 method rows. Run **manually** and commit results under
`results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/`.

Commands from repository root:

    conda activate trend-estimation
    git switch paper/pooled-loocv-numerical-optimization
    git pull --ff-only
    python -m pytest tests/test_guerrero_variance_estimation.py -q
    python -m experiments.pooled_loocv_smoothness.run_variance_estimation --preset pilot --dry-run
    python -m experiments.pooled_loocv_smoothness.run_variance_estimation --preset pilot

An additional exact **common scaling** experiment tests whether multiplying every simulated observed and latent series by c rescales both variance estimates by c², leaves lambda and normalized smoothness invariant, and multiplies LOOCV and latent MSE by c². This is an algebraic consistency check, not new independent evidence.

**Source distinction:** Guerrero (2007) derives the variance ratio from his stochastic signal-noise assumptions and provides a conditional observation-noise variance estimator for prescribed smoothing. He does **not** use our two proposed fitted-component procedures as his published primary smoothing-parameter selection method. His practical emphasis is a target percentage of smoothness. The inference in this experiment is a clearly labeled extension.
