# Completed robustness pilot — estimated Gaussian variance likelihood vs pooled observed LOOCV

**Audit date:** 2026-10-18 America/Mexico_City (run created 2026-10-19 UTC). **Status: COMPLETED AND COMMITTED PILOT; exploratory, not independent confirmatory evidence.**

## 1. Provenance and exact simulation

Original committed experimental artifacts:

- [executed manifest](../../../results/pooled_loocv_smoothness/guerrero/robustness/pilot/manifest.json)
- [saved 1,000-method-row CSV](../../../results/pooled_loocv_smoothness/guerrero/robustness/pilot/method_comparison.csv)
- [saved original grouped summary](../../../results/pooled_loocv_smoothness/guerrero/robustness/pilot/summary.json)

Read the prespecified [ROBUSTNESS_PROTOCOL.md](ROBUSTNESS_PROTOCOL.md) before interpreting results. Generator is \`experiments/pooled_loocv_smoothness/run_robustness.py\`, with seeded \`numpy.random.default_rng\`. Source manifest says **seed base 30610000**, with \`seed = 30610000 + 10000*scenario_id + replicate\`. Series length \(N\in\{50,200\}\), \(d=2\), observation-noise SD \(\sigma_\eta\in\{0.5,2\}\), trend-innovation SD \(\sigma_\varepsilon=0.3\), five independent seeds for each setting, \(R=1\) and \(R=3\) nested. The five error regimes are Gaussian iid, Student-t(5) observations, Student-t(5) innovations, stationary Gaussian AR(1) observation noise with \(\phi=0.65\), and two-segment Gaussian heteroskedastic observations with variances \(0.25\sigma_\eta^2\) and \(1.75\sigma_\eta^2\).

**Execution coverage:** 5 regimes × 2 lengths × 2 observation noise SD × 5 seeds × 2 nested R = **200 pools**, five methods each = **1,000 per-method rows**. Primary display below is 100 \(R=3\) pool evaluations (20 per regime: 4 DGP cells × five independent seeds). R=1 reuses the first series of the R=3 pool for a common scenario and seed: these are **not 200 independent Monte Carlo replications**. Every selected smoother uses the same \(H_\lambda\); latent truth is used only to calculate the true-trend MSE, never in feasible selection.

**Exact nomenclature:** \`estimated_gaussian_difference_ml\` is our feasible Gaussian **difference-covariance likelihood extension** for \(D_2y\), not an estimator prescribed by Guerrero (2007). \`nominal_known_ratio\` uses the declared *marginal* \(\sigma_\eta^2/\sigma_\varepsilon^2\), and is **not an oracle** when the observation covariance is serially correlated or nonstationary. Student-t noises are variance-standardized to keep their second moments comparable, but the Gaussian distribution is no longer correct.

## 2. Five-regime comparison — R=3, actual uploaded results

| DGP noise | Gaussian ML true-trend MSE | Ordinary pooled LOOCV true-trend MSE | Paired ML lower true MSE | Relative mean true-MSE reduction vs LOOCV | Nominal-ratio reference true-MSE |
|---|---:|---:|---:|---:|---:|
| iid Gaussian | 0.355507 | **0.355433** | 15/20 | -0.02% | 0.349790 |
| Student-t observation noise | **0.337182** | 0.352827 | 13/20 | +4.43% | 0.340791 |
| Student-t trend innovations | **0.335247** | 0.336293 | 12/20 | +0.31% | 0.334483 |
| AR(1) observation noise (\(\phi=0.65\)) | **1.350641** | 1.704392 | **20/20** | **+20.76%** | 0.955715* |
| Changing observation variance | **0.335961** | 0.354783 | **16/20** | +5.31% | 0.335740* |

\* *Nominal scalar variance ratios in the AR(1) and changing-variance models are not the covariance-correct optimal estimator. They are descriptive fixed-parameter references, not statistical oracles.*

**All R=3 pools equally weighted:** mean true-trend MSE **0.542908 Gaussian ML** vs **0.620746 LOOCV**, a **12.54% reduction** in the pooled arithmetic means. Gaussian ML attained lower true-trend MSE in **76/100** paired pools, while ordinary LOOCV attained the smaller *observed CV* mean (2.225872 vs Gaussian ML 2.261620). The nominal fixed-ratio mean trend MSE was 0.463304, but it is NOT an oracle across these five regimes.

**Heterogeneity is critical:** the AR(1) group accounts for roughly **91% of the total equal-regime-mean absolute CV-minus-ML trend-MSE difference**. A headline 12.5% aggregate improvement alone would strongly obscure this mechanism. Within the correctly specified iid Gaussian group, the two feasible selectors' *mean* true-MSE scores were essentially tied, even though ML won on the realized true MSE in 15/20 pools. This is a reminder that wins, means and median differences capture different aspects of finite samples.

For AR(1), even though direct LOOCV minimized its recorded CV objective (mean observed CV score **0.913917** vs Gaussian ML **1.035299**), it selected smoother parameters yielding much higher latent-trend MSE. A held-out observation remains correlated with neighboring training observations; standard one-point leave-out does not validate an independent prediction target. Gaussian difference ML **also has a misspecified covariance model**, so its observed relative improvement is not a general guarantee. A covariance-aware state-space/GLS or dependence-aware validation comparator is required before drawing statistical conclusions about this regime.

## 3. R=1 sensitivity and genuine counterexample

Across all 100 single-series pools, mean true-trend MSE was **0.591485** for Gaussian ML vs **0.735484** for LOOCV, with ML lower in 68/100 and its own 3/100 infinite smoothing selections. Because R=1 uses the first member of R=3, those are **nested sensitivity checks**, not independent external replications.

The **Student-t innovation regime at R=1** is an important adverse average counterexample:

- Gaussian ML mean true-trend MSE: **0.392287**.
- Ordinary LOOCV mean true-trend MSE: **0.324086**.
- Thus Gaussian ML had **21.0% higher mean MSE** despite winning on true-trend MSE in **11/20** individual pools.

This is consistent with a few large errors contributing disproportionately to the mean and demonstrates that Gaussian ML is **not uniformly more accurate** when assumptions are violated. It needs an explicit tail/failure audit, not only a count of pairwise wins.

## 4. Numerical optimization and unstable moments

- Across all **100 R=3** pools, the derivative-sign scan found exactly **one** stationary candidate per pool. These are *numerical sign-change candidates*, not a certified proof of unique stationary points or unique local minima.
- The usual single-start bounded Brent objective **never exceeded** the multibracket Brent LOOCV objective by more than **1e-7** in those 100 cases. The approaches returned effectively identical CV minima; the more elaborate solver **did not demonstrate numerical benefit** on this robustness pilot.
- At R=1, finite scan root-candidate counts were: one candidate in **92/100**, two in 4/100, three in 3/100, four in 1/100. Do not equate 3 or 4 roots with 3 or 4 strict local minima.
- The nonnegative quadratic-moment estimator produced **30/100** \(R=3\) and **29/100** \(R=1\) cases with zero estimated trend-innovation variance and \(\lambda=\infty\). Its mean R=3 true-trend MSE was **361.858**, median **0.9483**: severe boundary failures dominate its mean. This is a failure of **this particular constrained moment procedure**, not proof that all moments estimators are necessarily invalid.
- Gaussian ML had **0/100** R=3 infinite penalties and **3/100** R=1 infinite penalties.

## 5. Mathematical/statistical boundaries

The exact target in this independent paper is **retrospective reconstruction of the simulated latent trend**, not forecasting. True latent trend recovery uses knowledge of \(\tau\) *only for evaluating* selected parameters, and ordinary CV minimizes observed left-out squared errors rather than latent reconstruction error.

Under the heavy-tailed Student-t settings, covariance second moments continue to match the iid covariance model even though the Gaussian likelihood is misspecified; thus Gaussian ML can operate as a Gaussian *quasi-likelihood*. The AR(1) and heteroskedastic settings alter the covariance structure, making both \(\lambda_{\mathrm{nominal}}\) and the fitted scalar variance-ratio model incomplete for optimal smoothing.

Only **five independent seed replicates per DGP cell** were run. Do not compute naive confidence intervals treating 1,000 method rows, 200 nested pools, or 5 series per pool as independent statistical units. These are exploratory pilot findings and should not be presented as broadly replicated robustness.

## 6. Deterministic audit of the committed results

After pulling this branch, run:

    python -m pytest tests/test_guerrero_robustness_audit.py -q
    python -m experiments.pooled_loocv_smoothness.audit_robustness

This **only reads** the committed 1,000-row method comparison CSV. It validates all five methods on paired pools, the nested R/seed layout, and writes:

- \`results/pooled_loocv_smoothness/guerrero/robustness/pilot/audit/paired_pool_differences.csv\`
- \`.../audit/R3_scenario_summary.csv\`
- \`.../audit/audit_summary.json\`

To create **two figures manually**, run the same module with \`--figures\`. Do not treat figures not yet committed as existing evidence. Heavy analysis should not launch during ordinary Git pushes.

## 7. Research conclusion and the next valid question

**Supported by this pilot:** under serially correlated errors, direct observed-series LOOCV gave substantially worse *latent reconstruction* than the fitted Gaussian difference-likelihood selector on the matched cases; under iid Gaussian errors the two feasible methods' *means* essentially tied; with heavy-tailed trends and R=1 there is a counterexample on mean latent MSE. Neither finite LOOCV solver established a global numerical improvement here.

**Next methodological priority:** Add a correctly covariance-aware state-space or generalized least-squares smoother/variance estimation and a dependence-aware validation baseline for the AR(1) regime, preserving the same simulated latent trajectories across competitors. This separates (i) ordinary LOOCV's dependence leakage, (ii) wrong Gaussian difference-likelihood covariance, and (iii) target mismatch of observed CV versus latent truth. Do not jump straight to 100 new seeds without auditing whether the comparison is correctly specified or fairly budgeted.

**Workflow:** all code, protocol, notes, and user-run results are committed **directly to** \`paper/pooled-loocv-numerical-optimization\`. **Do not open PRs or merge.**
