# Completed pilot — feasible estimation of Guerrero's two variances

**Recorded:** October 18, 2026 (America/Mexico_City). **Status:** exploratory pilot, not independent confirmatory inference.

**Data read directly from committed GitHub branch** at:
- [Executed manifest](../../../results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/manifest.json)
- [Four-method summary](../../../results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/summary.json)
- [Paired method-level CSV](../../../results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/variance_estimator_comparison.csv)
- [Scenario breakdown](../../../results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/scenario_summary.csv)
- [Common-scale invariance check](../../../results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/common_noise_scale_invariance.csv)

Run metadata: created 2026-10-19T02:38:46Z, commit recorded as faed2982df59f1fdc7033603aa46a2bf8d5b5f04, Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1. The exact DGP and estimators are specified in [VARIANCE_ESTIMATION_PROTOCOL.md](VARIANCE_ESTIMATION_PROTOCOL.md). The saved data contain **12 scenario settings × 5 replicate seeds × two nested pool sizes (R=1/3) = 120 paired pools**, four methods each, **480 rows**.

**Critical source distinction:** Guerrero (2007) supplies the stochastic smoothing *variance ratio* \(\lambda=\sigma_\eta^2/\sigma_\varepsilon^2\) under his model; the particular Gaussian *difference-contrast likelihood* and nonnegative *quadratic moment estimator* are our **computational extensions**, not Guerrero's published estimators. His paper also advocates choosing a desired percentage of smoothness. The true-ratio comparison is an **oracle given known simulation variances**.

## 1. Primary R=3 results — completed, not a proposed result

All four methods use exactly the same PLS trend estimator \(H_\lambda y\); only the way \(\lambda\) is selected differs. Gaussian difference ML and quadratic moments observe **only y**, not latent \(\tau\). The true latent trend is used solely for retrospective *evaluation*.

| Method | Mean observed pooled LOOCV MSE ↓ | Mean true trend MSE ↓ | Median true trend MSE ↓ | \(\lambda=\infty\) hits |
|---|---:|---:|---:|---:|
| Guerrero known **true** variance ratio (oracle) | 2.697581 | **0.385673** | 0.165792 | 0/60 |
| **Feasible Gaussian difference ML** | 2.696789 | 0.387916 | 0.167952 | 0/60 |
| Pooled observed LOOCV, one-start Brent | **2.681409** | 0.394848 | 0.200955 | 0/60 |
| Nonnegative quadratic moments | 102.033035 | **96.127631** | 0.770187 | **16/60** |

- Among 60 paired R=3 pools, Gaussian difference ML has a **smaller true trend MSE than LOOCV in 37/60**, and a smaller true trend MSE than the oracle in **20/60**. The oracle is better on *average* by a small amount, not in every finite sample.
- Gaussian ML's mean true trend MSE is approximately **1.76% lower than LOOCV's** and **0.58% higher than the known-ratio oracle's**. Those differences are **not** a statistical significance claim.
- The corresponding observed LOOCV score was lower for Brent (2.681409) than Gaussian difference ML (2.696789). This is expected because Brent **selects by** observed LOOCV, whereas the fitted likelihood targets the stochastic-model covariance.
- **Do not present the moment estimator's huge mean as an ordinary small inefficiency.** It is a mixture with catastrophic finite-sample failures, which deserve an explicit *rate and severity* analysis.

The 60 R=3 pools arise from **12 different DGP settings, 5 independent three-series pools per setting**. Their average is an equal-weighted exploratory benchmark; high-noise cells contribute much more to raw mean MSE than low-noise cells. Do not attach a pooled standard error treating four method rows or nested R=1 and R=3 as independent replicates.

## 2. R=1 sensitivity and effect of pooling

| Method | R=1 mean true trend MSE | R=3 mean true trend MSE |
|---|---:|---:|
| Known variance ratio | 0.381850 | 0.385673 |
| Estimated Gaussian difference likelihood | 0.390560 | 0.387916 |
| Pooled observed LOOCV | 0.414164 | 0.394848 |
| Constrained moment estimator | **340.630007** | **96.127631** |

In R=1, Gaussian ML beats LOOCV in **38/60** pools and its mean trend MSE is approximately **5.7% smaller**. The observation-noise variance mean absolute *relative* estimation error is approximately 15.9% for R=1 vs **10.0% for R=3**; the trend-innovation variance error is 29.7% vs **18.3%**.

The median absolute logarithmic error of the estimated variance ratio \(\log(\widehat\lambda/\lambda_G)\) is **0.2884** for R=1 and **0.1758** for R=3, i.e. a typical multiplicative deviation of about 1.33× vs 1.19×. The single R=1 Gaussian boundary selection with \(\widehat\lambda=\infty\) is excluded from this *finite-log* median and must be counted separately.

R=1 uses the **first observation series of the corresponding R=3 pool**; therefore changes across R are **paired/nested**, not two unrelated independent samples.

## 3. Variance levels and sample size: what the data actually show

For **R=3**:

| Length | Pools | Gaussian relative abs. error in \(\sigma_\eta^2\) | Gaussian relative abs. error in \(\sigma_\varepsilon^2\) | Moment method \(\hat\sigma_\varepsilon^2=0\) |
|---|---:|---:|---:|---:|
| N=50 | 30 | **14.10%** | **24.21%** | 11/30 |
| N=200 | 30 | **5.86%** | **12.36%** | 5/30 |

The longer series gave substantially more accurate **variance-component estimates in this run** and fewer moment-method boundary failures, **but** its moment-method mean MSE could still be larger due to individual extremely bad reconstruction cases with accumulating stochastic-trend departures.

The **six true population ratios** \(\lambda_G\) are 0.25, 2.7778, 4, 25, 44.4444 and 400 (each at N=50 and 200). Their ratio is what controls the target smoothing parameter, not the absolute noise level alone. Within the 60 R=3 pools, observed Gaussian likelihood improvements over LOOCV depend on the noise configuration: it won on true MSE in 8/10 at \(\lambda_G=0.25\), 4/10 at 2.7778, 4/10 at 4, 7/10 at 25, 7/10 at 44.4444 and 7/10 at 400. With **only ten pools per ratio**, these counts are descriptive.

Crucial scale check: for exactly the same simulated series, rescale \(y,\tau\mapsto cy,c\tau\) for \(c=0.5,1,2\). The uploaded common_noise_scale_invariance.csv shows the selected \(\lambda\) unchanged (within numerical precision), fitted variances multiplied by \(c^2\), and both MSE scores multiplied by \(c^2\). **This is an algebraic equivariance check on one fixed dataset, not independent evidence about six new variance levels.** To separately investigate scale effects, use matched DGPs with common \(\lambda\) and differing common SD multiplier.

## 4. Catastrophic boundary-case diagnosis

The constrained moment estimator set the *trend innovation variance* to zero in **19/60 R=1 pools** and **16/60 R=3 pools**, implying \(\widehat\lambda=\infty\). With \(d=2\), the fitted trend then lies in \(\ker D_2\), namely the space of linear functions, even when the stochastic truth is not linear.

For R=3, the most extreme observed failure was scenario 10 (N=200, \(\sigma_\eta=2\), \(\sigma_\varepsilon=0.3\)), replicate 4: true trend MSE about **2594.34** with constrained moments vs **0.626** using the true ratio. This is a real recorded failure mode of the *specified moment procedure*, not a proof all possible moment methods are unreliable.

The difference-Gaussian ML profile was **much more stable**, with **0/60 boundary hits** in R=3 and 1/60 in R=1. It is not universally immune to boundary estimates or misspecification.

## 5. How to reproduce the descriptive audit with figures

From the branch root:

    conda activate trend-estimation
    git switch paper/pooled-loocv-numerical-optimization
    git pull --ff-only
    python -m experiments.pooled_loocv_smoothness.audit_variance_estimation

Outputs (manual analysis only):
- `results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/audit/variance_pilot_audit.json`
- `.../audit/R3_scenario_diagnostics.csv`
- `.../audit/R3_true_trend_mse_by_variance_scenario.png`
- `.../audit/R3_moment_boundary_failures.png`
- `.../audit/ML_variance_component_error_by_sample_size.png`

The audit reads uploaded source CSV without rerunning any DGP. It distinguishes each DGP/seed/R group; 2 sizes are nested; finite-\(\log\lambda\) ratio metrics separately count boundary estimates. No charts are committed as if a user had already generated them on their machine.

## 6. Research interpretation and next decisions

**Supported:** Under these correctly specified stochastic-trend DGPs, joint *Gaussian differenced-data covariance likelihood* is a feasible alternative to cross-validation: it estimated both variance components without latent-\(\tau\) access and approached the **known-variance** oracle's average latent-trend reconstruction error. Naive quadratic moments with NNLS were highly unstable because the innovation variance often hit a zero boundary. Direct LOOCV remains better on the *LOOCV objective* but does not necessarily minimize expected or realized trend reconstruction error.

**Not supported:** A claim that Guerrero (2007) proposed this specific two-variance ML procedure, that the Gaussian estimator is uniformly better than LOOCV, that we have a new globally certified numerical solver, or that these results carry over to market prices/returns under misspecified independent Gaussian errors.

**Next study:** prespecify Gaussian ML versus observed pooled LOOCV on \(R=3\) as primary; run a fresh independent larger confirmatory seed set after validating endpoints, likelihood shapes and computational budgets; include \(d\in\{1,2,3\}\) only as a separate extension; study non-Gaussian shocks and autocorrelated measurement noise. Report robust per-scenario paired mean/median differences, estimator boundary rates and ratios with uncertainty. Do not merge the preliminary 2017-inspired and stochastic DGP datasets into one undifferentiated table.
