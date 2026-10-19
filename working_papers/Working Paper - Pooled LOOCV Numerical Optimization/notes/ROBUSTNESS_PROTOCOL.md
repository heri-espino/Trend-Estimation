# Independent robustness extension: misspecified noise in observed-series trend smoothing

**Prepared on 2026-10-18 (America/Mexico_City).** Experiment code: [run_robustness.py](../../../experiments/pooled_loocv_smoothness/run_robustness.py). **Status:** prespecified simulation design. Do not describe the pilot as executed until its committed manifest and CSV exist. Small CI smoke tests are distinct from the research pilot.

## 1. Question and inferential objects

Earlier, with correctly specified Gaussian \(D_2\tau=\varepsilon\) and \(y=\tau+\eta\), the estimated-Gaussian-difference-likelihood selector approximated Guerrero's known-variance benchmark for true trend reconstruction, while directly minimizing observed LOOCV yielded a smaller observed LOOCV score. To test robustness, **hold the PLS estimator family and mean-zero integrated trend structure fixed**, but alter the error distributions/covariance so the fitted iid-Gaussian likelihood is misspecified.

Separate three questions:

1. How stable are Gaussian differenced-data likelihood parameter estimates when its distribution or covariance assumptions fail?
2. Which *feasible selector* gives lower **simulated latent trend reconstruction MSE**, Gaussian likelihood or pooled ordinary LOOCV?
3. Does a multibracket search materially improve numerical minimization of the same LOOCV surface over one-start Brent?

The numerical search result must not be conflated with superiority of one statistical smoothing criterion, and measured reconstruction error must not be conflated with forecasting.

## 2. Mathematical generator

For each independently drawn member \(r\) of a pool:

\[
D_2\tau^{(r)}=\varepsilon^{(r)},\quad
\tau_1=0,\quad \tau_2=0.02,\qquad
y^{(r)}=\tau^{(r)}+\eta^{(r)}.
\]

Same \((N,\sigma_\eta,\sigma_\varepsilon)\) across the \(R\) series in a pool. Independent latent trajectories and measurement errors across series, independent innovation noise and measurement noise. \(R=1\) reuses **exactly the first member** of the \(R=3\) pool with the same scenario and seed, to allow paired interpretation. The initial two coefficients are fixed, not a diffuse prior.

Five prespecified regimes:

| Label | Innovation \(\varepsilon\) | Observation noise \(\eta\) | Misspecification |
|---|---|---|---|
| \`gaussian_iid\` | iid Gaussian | iid Gaussian | None, correctly specified covariance benchmark |
| \`student_t_observation\` | iid Gaussian | iid Student-t(5), rescaled to SD \(\sigma_\eta\) | Gaussian observation distribution wrong; second moments unchanged |
| \`student_t_innovation\` | iid Student-t(5), rescaled to SD \(\sigma_\varepsilon\) | iid Gaussian | Gaussian trend-difference distribution wrong; second moments unchanged |
| \`ar1_observation\` | iid Gaussian | stationary Gaussian AR(1) with \(\phi=0.65\) | Observation serial dependence ignored by ML and ordinary LOOCV |
| \`heteroskedastic_observation\` | iid Gaussian | independent Gaussian observation noise, first-half variance \(0.25\sigma_\eta^2\), second-half variance \(1.75\sigma_\eta^2\) | Measurement noise variance changes within the series |

Student-t(5) draws are multiplied by \(\sqrt{(5-2)/5}\) for **unit population variance**. AR(1) recursion is

\[
\eta_1\sim N(0,\sigma_\eta^2),\quad
\eta_t=0.65\eta_{t-1}+\sigma_\eta\sqrt{1-0.65^2}\,u_t,
\quad u_t\sim N(0,1),
\]

so the marginal observation noise variance is exactly \(\sigma_\eta^2\), while temporal dependence is nonzero. Heteroskedastic regime's average *population observation variance over the grid* is \(\sigma_\eta^2\) (N always even); it cannot be captured by a single constant measurement variance.

### Why the nominal variance-ratio benchmark must be relabeled

The recorded nominal ratio is

\[
\lambda_{\rm nominal}=\sigma_\eta^2/\sigma_\varepsilon^2.
\]

For the iid Gaussian regime this is the classical model-informed Guerrero penalty. Under Student-t noise the *second moments* still match the white-noise model, so the ratio remains a covariance-motivated **linear-smoothing** reference, but the exact Gaussian conditional-mean interpretation does **not** generally carry over. Under AR(1) or heteroskedastic observation error, **the scalar ratio is not an optimal parameter justified by the actual noise covariance**, and must not be called an oracle.

The fitted ML method nevertheless assumes

\[
z=D_2y\sim N(0,\ aI+bD_2D_2^\top),
\]

with unknown \(a=\sigma_\varepsilon^2,\ b=\sigma_\eta^2\). Under misspecification, fitted \(a,b\) can be **pseudo-parameters**. We label it \`estimated_gaussian_difference_ml\`, not “Guerrero's MLE.” The method of moments with NNLS is included as a **failure-mode control**, not a primary method.

## 3. Five selections applied to identical observed pools

1. **Nominal known marginal variance ratio** (not a valid model oracle in the two correlated/nonstationary covariance regimes).
2. **Gaussian difference-likelihood estimated ratio**, using only observed \(D_2y\) and the existing \`estimate_gaussian_differences\`.
3. **Pooled observed LOOCV, single-start bounded Brent**.
4. **Pooled observed LOOCV, multibracket derivative Brent** (finite scan; not a completeness certificate).
5. **NNLS two-moment estimated ratio**, recording \(\widehat\sigma_\varepsilon^2=0\) and infinite penalty explicitly.

All five produce \(\widehat\tau_\lambda=H_\lambda y\) using exactly the **same** trend-smoother operator. Truth \(\tau\) is never used to choose \(\lambda\). For each method record \(\lambda\), normalized \(S\), observed pooled LOOCV MSE, and *realized* latent trend MSE. For variance estimators record both estimated components and whether the process-innovation component is zero.

Ordinary leave-one-observation-out CV on autocorrelated noise may be statistically optimistic; this experiment evaluates it as a **fixed observed-series criterion**, not valid independent holdout forecasting. Do not claim that minimizing LOOCV under AR1 estimates independent predictive risk.

## 4. Locked pilot design and independent seeds

**Smoke only (CI):** 5 regimes × N=24 × observation SD 0.5 × innovation SD 0.3 × one seed × R=1 and R=3 = **10 pools**, five methods per pool = **50 method rows**. CI-generated outputs under temporary paths do not constitute committed pilot evidence.

**Pilot (manual):** 5 regimes × N∈{50,200} × observation SD∈{0.5,2} × innovation SD fixed at 0.3 = **20 DGP cells**. Five independent seeds per cell and R∈{1,3}: **200 nested pools, 1000 method rows**. There are **100 independent three-series pools**, and 100 nested corresponding single-series evaluations.

**Prospective confirmatory (manual-only, NOT execute yet):** same 20 DGP cells × 100 independent *new* seeds per cell × R1/3 = **4000 nested pools**, 20,000 method rows. Scientific conclusions need scenario-stratified uncertainty, not a pseudo-sample size of 20,000.

\[
\mathrm{seed}=\mathrm{seed\_base}+10{,}000\times\mathrm{scenario\_id}
+\mathrm{replicate}.
\]

Pilot seed base: **30610000**, confirmatory: **31610000**. Source: \`numpy.random.default_rng\`. Scenario ordering and exact parameter tuples are written in every manifest. Because R1/R3 share a generated first series, never treat both as independent estimates of a treatment effect. Within every pool, all methods use the same observed data and latent evaluation truth.

Do not confuse pilot seeds with the prior variance-estimation pilot (\`20262000\`) or original Cortés-Toto source-inspired pilot (\`100000\`).

## 5. Hypotheses and analysis before looking at pilot outcomes

- Under iid Gaussian disturbances, the fitted Gaussian variance-likelihood selector should approach the model-informed ratio as available data increase; LOOCV minimizes its own reconstruction CV score.
- Student-t noise may challenge Gaussian likelihood via outliers; both the ML and CV selectors can be sensitive. Tail behavior (not only means) matters.
- For autocorrelated observation errors, **both** the independence Gaussian likelihood and ordinary LOOCV use misspecified noise assumptions/validation interpretation; either may fail. Do not assume LOOCV wins automatically.
- Under time-varying noise, a single global constant variance ratio is intrinsically limited; neither selector addresses the correctly specified heteroskedastic covariance structure.
- Expect more unstable NNLS moment-variance estimates when innovation variance is hard to distinguish from observation noise; record failure rates rather than trimming them.
- Multibracket may find alternative LOOCV minima, especially under misspecification; evaluate objective improvements and endpoints **separately** from true trend performance.

**Primary descriptive comparison:** Gaussian difference ML vs single-start LOOCV on *paired latent-trend MSE* within each \(R=3\) scenario/seed. Secondary: multibracket vs one-start LOOCV objective gap; relative variance-component estimation error when a stationary interpretation exists; \(\lambda=\infty\) frequency; median/upper-tail trend MSE; sensitivity by regime, N, and \(\sigma_\eta\). If multiple settings are compared, use scenario-level summaries rather than a pooled raw mean alone.

**Publication boundary:** even after the pilot, no superiority claim without external source novelty audit, independent confirmatory seeds, correctly specified reference methods where appropriate, and robust interval estimates with the Monte Carlo replicate as statistical unit.

## 6. Reproducibility and output expectations

From repository root in PowerShell:

    conda activate trend-estimation
    git switch paper/pooled-loocv-numerical-optimization
    git pull --ff-only
    python -m pip install -e ".[dev,symbolic]"
    python -m pytest tests/test_guerrero_robustness.py -q
    python -m experiments.pooled_loocv_smoothness.run_robustness --preset smoke
    python -m experiments.pooled_loocv_smoothness.run_robustness --preset pilot --dry-run
    python -m experiments.pooled_loocv_smoothness.run_robustness --preset pilot

Distinct output root: \`results/pooled_loocv_smoothness/guerrero/robustness/{smoke,pilot}/\` with \`method_comparison.csv\`, \`summary.json\`, \`manifest.json\` and \`robustness_true_trend_mse_R3.png\`. All software versions, random seeds, exact scenario grid, noise mechanisms and code SHA are retained. All large simulations and figure production remain **manual** rather than triggered by every commit. Only tiny smoke/test validation belongs in automatic CI.

After inspection, explicitly \`git add\` the relevant small CSV/JSON/PNG results, \`git commit\` and \`git push\` on the **same branch**. Do not open a PR or merge into main.
