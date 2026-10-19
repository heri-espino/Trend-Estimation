# Tail-shape, asymmetry, jump-mixture and clustered-volatility stress study

**Prepared 2026-10-18; revised to v2 before experiment execution. Full pilot NOT executed.** Distinct from the previously completed 5-regime robustness pilot. Executable: `experiments/pooled_loocv_smoothness/run_tail_noise.py`. Mathematical context: [MSE AND GAUSSIAN LIKELIHOOD EXPLANATION](GAUSSIAN_MLE_AND_LOOCV_EXPLAINED.md).

## Version 2 amendment — added **before running the pilot**

**Latest planned design (2026-10-18):** the earlier proposed d=2, eight-distribution experiment has been revised **before any full pilot is run**. The current executable experiment combines **three difference orders** \(d\in\{1,2,3\}\) with **13 distribution settings** (the eight original controls plus five centered skew-normal shape settings). All previous simulations and their artifacts remain unchanged. Any older counts below are superseded by the explicit numbers in this amendment.

**What is changed mathematically?** Each new scenario generates the true stochastic trend and fits the PLS smoother with the **same** order:

\[
D_d\tau=\varepsilon,\qquad
\widehat\tau_\lambda=(I+\lambda D_d^\top D_d)^{-1}y,
\qquad d\in\{1,2,3\}.
\]

The first d values of the trend are fixed at \(\tau_j=0.02(j-1)\), for \(j=1,\ldots,d\); subsequent values are recursively generated as

\[
\tau_{j+d}=\varepsilon_j-\sum_{k=0}^{d-1}
(-1)^{d-k}\binom{d}{k}\tau_{j+k}.
\]

This ensures exactly \(D_d\tau=\varepsilon\). The infinite-smoothing limit is constant for d=1, linear for d=2 and quadratic for d=3. Comparing fitted order versus a *different* generating order is a separate future misspecification study; this campaign only compares correctly matched orders. Higher-order integrated trends can have much larger low-frequency variation: **stratify by d**, never infer one method dominates from unstratified MSE averages across orders.

**Skew-normal with population mean zero.** Five levels \(\alpha\in\{-6,-3,0,+3,+6\}\) are included. Let \(\delta=\alpha/\sqrt{1+\alpha^2}\) and \(U,V\) be independent standard normals. Define

\[
Z=\delta |U|+\sqrt{1-\delta^2}\,V,\quad
\mu_Z=\delta\sqrt{2/\pi},\quad
s_Z^2=1-2\delta^2/\pi.
\]

Actual simulated noise is

\[
\boxed{\eta=\sigma_\eta\,\frac{Z-\mu_Z}{s_Z}}.
\]

Thus \(\mathbb E\eta=0\) and \(\operatorname{Var}(\eta)=\sigma_\eta^2\), **independently of skewness**. We use *analytic population* centering and scaling, not the mean/SD computed from each realization. At \(\alpha=0\) this is a Gaussian-in-distribution control. The five additional settings are \`skew_normal_m6\`, \`skew_normal_m3\`, \`skew_normal_0\`, \`skew_normal_p3\`, \`skew_normal_p6\`. Unlike a regular unshifted Gamma, these skew-normals can take both positive and negative values.

**Final unrun pilot grid:** \(13\) distribution settings × \(3\) orders × \(2\) lengths (N=50,200) × \(2\) noise scales (0.5,2) = **156 scenarios**. At five independent seeds per scenario and nested R=1/3, this is **1,560 pool evaluations, 4,680 method rows** (780 primary R=3 pools). The **tiny CI smoke** instead checks N=24, noise scale 0.5, one seed, 13×3×2 = **78 pools, 234 method rows**. The manual-only prospective confirmatory preset is 31,200 pools and 93,600 method rows (not run now). Pilot seeds remain fixed to base **47800000**, \`base+10000*scenario_id+replicate\`; the revised scenario order is recorded in the manifest. This pilot has **not been executed**.

**Risk semantics remain:** Cauchy scale gamma is not an SD; Cauchy has neither finite population variance nor expected squared-error risk. Report its median per-pool realized MSE and absolute-error quantiles, not an expected MSE or Guerrero variance ratio. Student-t3, skew-normal, centered Gamma, mixture, and GARCH regimes have finite observation variance, though distributional assumptions may be misspecified. The empirical financial-return motivation does not make additive-noise synthetic trends a calibrated stock-market DGP.

---

## 1. Original distribution definitions (retained)


The original d=2-only notation below is superseded by the **matched d=1,2,3** generator defined in the v2 amendment. The common synthetic data model remains

\[
 D_2\tau^{(r)}=\varepsilon^{(r)},\quad
 \tau_1^{(r)}=0,\ \tau_2^{(r)}=0.02,\quad
 y^{(r)}=\tau^{(r)}+\eta^{(r)},\quad r=1,\ldots,R.
\]

Do not describe this as actual equity/ETF returns or real market data: returns often exhibit heavy tails and volatility clustering, but a market log return need not be a smooth integrated trend plus additive independent measurement error. The goal here is to isolate *robustness of the statistical choice of a PLS smoothing penalty* in a controlled latent-trend experiment. A genuinely market-calibrated DGP and observed market evidence are separate studies.

Trend-innovation SD \(\sigma_\varepsilon=0.3\) unless overridden. \(\eta\) noise has nominal standard deviation \(\sigma_\eta\in\{0.5,2.0\}\) **except Cauchy**, where the number is its **scale \(\gamma\)**, not an SD. Two lengths \(N\in\{50,200\}\). Noise is centered and independent across observations *except* in the volatility-clustering regime; all latent innovation and observation-noise processes are independent of each other, and separate pool members are simulated independently.

Eight original DGP regimes (five additional skew-normal shapes are defined in the v2 amendment above) (NO silent truncation or winsorization):

| Regime | Construction | Moments and relevance |
|---|---|---|
| `gaussian_iid` | \(\eta=\sigma_\eta Z\), \(Z\sim N(0,1)\) | Correctly specified Gaussian baseline |
| `student_t3_observation` | \(\eta=\sigma_\eta\sqrt{(3-2)/3}\,T_3\) | Symmetric, excess kurtosis **undefined/infinite**; finite variance |
| `student_t3_innovation` | \(\varepsilon=\sigma_\varepsilon\sqrt{1/3}\,T_3\) | Heavy stochastic trend shocks; finite innovation variance, infinite fourth moment |
| `centered_gamma_right` | \(\eta=\sigma_\eta(G-k)/\sqrt{k}\), \(G\sim\Gamma(k,1)\), \(k=0.5\) | EXACT zero mean, SD \(\sigma_\eta\), right skew \(+2/\sqrt{k}\), excess kurtosis \(6/k=12\) |
| `centered_gamma_left` | \(\eta=-\sigma_\eta(G-k)/\sqrt{k}\) | EXACT zero mean, same SD and kurtosis, LEFT skew \( -2/\sqrt{k}\) |
| `gaussian_jump_mixture` | With probability 0.02 use Gaussian SD \(8\), else SD \(1\); divide by \(\sqrt{0.98+0.02(8^2)}\), multiply by \(\sigma_\eta\) | Finite-variance rare-shock contamination (leptokurtic), not structural jumps in latent tau |
| `garch_t5_observation` | Unit-variance standardized Student-t(5) shocks \(Z_t\); \(h_1=1\), \(h_t=0.05+0.10(\eta_{t-1}/\sigma_\eta)^2+0.85h_{t-1}\), \(\eta_t=\sigma_\eta\sqrt{h_t}Z_t\) | Heavy tails plus *conditional* heteroskedastic clustering. Deterministic \(h_1\) rather than random stationary volatility draw, explicitly disclosed |
| `cauchy_observation` | \(\eta=\gamma C\), \(C\sim\operatorname{Cauchy}(0,1)\) | Median 0, Cauchy scale \(\gamma\) (median absolute noise \(\gamma\)); **no finite mean, variance, kurtosis or MSE risk** |

**Important correction to informal phrase "zero-mean Gamma":** A standard Gamma variable has strictly positive mean. We use the *shifted centered Gamma*, which has a negative lower support bound and a long positive tail. Flipping its sign creates long negative returns-like outliers, but the supported data are still artificial trend measurement errors.

The Student-t3 and mixture distribution have finite *variance*, so the Gaussian difference likelihood can serve as a quasi-likelihood (though not a correctly specified density model). The Cauchy experiment is an **extreme robustness stress test**, not a realistic default model of stock returns. For Cauchy, estimates of \(\sigma_\eta^2\) are only pseudo-fitted numerical values: the parameter does not exist in the true law. Likewise \(\sigma_\eta^2/\sigma_\varepsilon^2\) cannot be supplied as a true Guerrero ratio.

## 2. What exactly is compared?

Three **feasible** selectors applied to *identical observed y* within each pool:

1. Gaussian likelihood of \(z=D_2y\) with \(\Sigma=aI+bD_2D_2^\top\), profiling scale and selecting a nonnegative ratio \(b/a\). This ML / quasi-ML selector sees **only y**.
2. Ordinary pooled observed-series LOOCV minimized by one bounded Brent search.
3. The **same pooled observed LOOCV objective** minimized by finite multibracket derivative-root Brent, for numerical-search diagnostics. It is not globally certified.

After selection, all methods use the **same PLS smoother**

\[
 \widehat\tau_\lambda=H_\lambda y,\qquad
 H_\lambda=(I+\lambda D_2^\top D_2)^{-1}.
\]

No optimizer tunes directly on true latent \(\tau\); truth is used **only to evaluate** reconstructions. The known-ratio oracle and NNLS moment estimator are excluded from this stress campaign, because the ratio is undefined under Cauchy and the previously observed NNLS boundary failures would distract from the main two feasible selectors.

Per pool/method save lambda, S, observed LOOCV MSE, realized latent-trend MSE, mean and median absolute latent reconstruction error, p90 absolute error, Gaussian fitted components if applicable, and number of **detected derivative sign-change candidates**. Sign-change candidate counts are not exact counts of distinct minima.

## 3. Why the Cauchy MSE result has a different interpretation

In each finite Monte Carlo realization, \(\frac1{RN}\|\widehat\tau-\tau\|_2^2\) is a real number and can be calculated. But the **population expected risk** \(\mathbb E[\frac1{RN}\|\widehat\tau-\tau\|_2^2]\) is not finite under Cauchy measurement noise for these nontrivial linear smoothers. A sample *mean* of those realized errors will not stabilize with increasing independent Monte Carlo replications. We should therefore highlight *median of per-pool realized MSE*, *median per-pool median absolute trend error* and upper-tail absolute error quantiles, rather than compare finite Monte Carlo means as convergent estimates of expected MSE.

No finite theoretical Cauchy standard deviation, no matching \(\lambda_G\), and no finite Cauchy kurtosis. Finite non-Gaussian tails (Student-t3, Gamma, mixture, GARCH-t5) make the conventional variance-ratio question meaningful, albeit potentially model-misspecified.

## 4. Statistical design and immutable seeds

- **Automated tiny smoke ONLY:** 13 settings × 3 orders × N24 × noise scale 0.5 × 1 seed × R1/3 = **78 nested pools** and **234 method rows**.
- **Exploratory pilot (manual, not automatically triggered):** 13 settings × 3 orders × 2 lengths × 2 noise scales = **156 scenario cells**, five independent replicate seeds, R1/3 nested = **1,560 pooled evaluations, 4,680 method rows**, 780 primary R3 pools (the R1 observations reuse series #1).
- **Prospective independent confirmation (manual only):** 156 cells × 100 fresh seeds × R1/3 = **31,200 nested pooled evaluations** and 93,600 method rows, only after pilot diagnostics.
- NumPy `default_rng`, seed base **47800000**, `seed=base+10000*scenario_id+replicate`. Independent confirmatory seed base **48800000**. Prior results and their seeds are not touched.

**Primary finite-second-moment estimand:** paired difference of true latent trend MSE between ML and bounded LOOCV for R=3 at fixed scenario/seed, report by **difference order**, regime, length and scale (not just pooled average).

**Cauchy primary estimand:** comparative distribution (quantiles) of *realized finite-sample robust absolute errors*, with *no population expected-MSE interpretation*. Report median rather than only mean, retain extreme realizations, and use common latent truth and noisy observations across methods.

Keep methods and scenario formulas fixed *before* examining the pilot output. Source manifest records git code SHA, RNG/seed formula, software versions, sample size, algorithm scan counts and distribution parameters. We store simulated data-generation information, not necessarily all raw simulated arrays; full raw-data regeneration requires checkout of the manifest commit.

## 5. Commands

From repository root:

    conda activate trend-estimation
    git switch paper/pooled-loocv-numerical-optimization
    git pull --ff-only
    python -m pytest tests/test_guerrero_tail_noise.py -q
    python -m experiments.pooled_loocv_smoothness.run_tail_noise --preset smoke
    python -m experiments.pooled_loocv_smoothness.run_tail_noise --preset pilot --dry-run
    python -m experiments.pooled_loocv_smoothness.run_tail_noise --preset pilot

Outputs under `results/pooled_loocv_smoothness/guerrero/tail_stress/{smoke,pilot}/`: `manifest.json`, `method_comparison.csv`, `summary.json`. Keep generated outputs distinct from five-regime completed robustness and older Guerrero variance-estimation pilot directories.

After a verified pilot, add the small generated files, commit and push to **the same branch**; no pull requests or merge into main. Large campaigns and figure generation remain manual only. Record all experimental analyses in source-linked Markdown notes, including negative results.

## 6. Literature positioning (not proof of a market calibration)

Rama Cont, *Empirical properties of asset returns: stylized facts and statistical issues*, Quantitative Finance 1(2), 223–236 (2001), DOI 10.1080/713665670: heavy tails, asymmetry, volatility clustering and nonlinear dependence are established stylized facts of returns. Student-t, skewed families, mixture and volatility dynamics are **motivated** by those properties; this study does **not** claim our 8 exact innovation laws match any specific stock index without a separate observed-return calibration exercise.

Theodossiou, *Financial Data and the Skewed Generalized T Distribution*, Management Science 44(12), 1650–1661 (1998), DOI 10.1287/mnsc.44.12.1650: a literature example treating asymmetry and heavy tails jointly; our centered Gamma is a cheap diagnostic control, **not** the skewed generalized-t estimator of that paper.
