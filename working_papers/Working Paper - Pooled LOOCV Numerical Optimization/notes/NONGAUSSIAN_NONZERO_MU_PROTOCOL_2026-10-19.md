# Phase J — non-Gaussian observation / trend-innovation distributions with nonzero expected differences

**Locked exploratory protocol, 2026-10-19; CODE IMPLEMENTED, REAL PILOT AND LARGE CONFIRMATION NOT EXECUTED.** This is a new, distinct campaign on branch `paper/pooled-loocv-numerical-optimization`, not a rerun of the completed five-seed \(d=2\) mean-shift pilot or of the 160,000-draw Gaussian four-order confirmation. Heavy simulations are **manual only**. No PR or merge.

## 1. Research question and earlier evidence

The completed [160k Gaussian base-draw confirmation](MULTIORDER_10000_SEED_CONFIRMATORY_RESULTS_2026-10-19.md) found that for three-series pools with large true difference means, **wrongly imposing \(\mu=0\) can cost more latent reconstruction MSE than choosing between feasible fitted-mean Gaussian GLS likelihood and fold-clean pooled observed LOOCV** in all 16 Gaussian \((d,N,\sigma_\eta)\) cells. GLS-ML had lower mean reconstruction loss in 15/16 such cells, with genuine \(R=1\) exceptions. For small \(|\mu|/\sigma_\varepsilon=0.25\), that magnitude conclusion held only 5/16 R3 cells. Do not summarize this as uniform MLE superiority or a discovery of nonzero means: Guerrero (2007) already considers \(\mu\neq0\).

**New question:** Does this ranking or mean-misspecification cost persist when the *same correctly ordered stochastic latent trend reconstruction task* is exposed to non-Gaussian observation innovations, non-Gaussian trend differences, asymmetric contamination or conditionally heteroskedastic disturbances? Gaussian mean/covariance estimation is a **quasi-likelihood** outside the true normal density. Its covariance contrast remains mathematically valid for centered, uncorrelated finite-second-moment disturbances; lack of normality alone does NOT falsify \(\operatorname{Cov}(D_d y)=aI+bD_dD_d^\top\). In GARCH-t5, volatility changes over time and the errors are dependent but serially uncorrelated, so unconditional covariance structure is still compatible with the Gaussian contrast. Conditional volatility itself is not used by the Gaussian fitted contrast.

## 2. Same realized latent trend, four chosen orders

The analyst separately **fixes** \(d\in\{1,2,3,4\}\) *before fitting*; these are matched generating/fitted-order sensitivity studies, **not order selection**. At each independent seed, generate \(R=3\) trajectories (first shared with R1). For a common chosen \(d\),

\[
D_d\tau^{(r)}=\mu\mathbf 1+\varepsilon^{(r)},\quad
y^{(r)}=\tau^{(r)}+\eta^{(r)},\quad
\mu/\sigma_\varepsilon\in\{-1,-0.25,0,0.25,1\},
\]

with \(\sigma_\varepsilon=0.3,\;\sigma_\eta\in\{0.5,2\}\), and \(N\in\{50,200\}\). Initial \(\tau_t=0.02t\) for \(t<d\). The **realized** true latent trajectory includes its accumulated stochastic innovation; it is not merely its polynomial expectation:

\[
\tau_t=0.02t+\mu\binom td+
\sum_{j=0}^{t-d}\binom{t-j-1}{d-1}\varepsilon_j
\quad (t\ge d).
\]

The **same exact centered stochastic innovations and observational errors** generate the five paired \(\mu\)-treatments at each (regime,d,N,\(\sigma_\eta\),replicate), using \(\tau_\mu=\tau_0+\mu p\), \(y_\mu=y_0+\mu p\), \(p_t=\binom td\). R1 is nested in R3. These are paired comparisons, not five more independent seeds. For every distribution regime, fitted methods receive \(y\) only; the realized latent \(\tau\) is used strictly after selection to evaluate reconstruction errors. The known true mean/variance-ratio row is an **infeasible known-covariance linear-smoother benchmark** outside Gaussianity, not a general Bayes-optimal heavy-tailed conditional estimator.

## 3. Distributional choices inherited from the previous executed tail pilot

**Source of parameters:** [run_tail_noise.py](../../../experiments/pooled_loocv_smoothness/run_tail_noise.py), which was already implemented and piloted for \(d=1,2,3\). Here we reuse exactly its law parameters, add \(d=4\), enable nonzero \(\mu\) and the eight fitted-mean/zero-mean comparators, and use a NEW independent seed bank. The twelve finite-variance regimes are:

| Regime identifier | Changed innovation distribution | Definition and moment properties |
|---|---|---|
| `gaussian_iid` | Reference centered normal for ε and η | Identical law family to previous Gaussian confirmation, but with **new, independent seeds** |
| `student_t3_observation` | \(\eta\) | Standard Student-t(3) multiplied by \(\sqrt{(3-2)/3}\); exactly population mean zero and SD one before multiplying by \(\sigma_\eta\); **infinite fourth moment** |
| `student_t3_innovation` | \(\varepsilon\) | Same standardized Student-t(3), scaled by \(\sigma_\varepsilon\); observation η remains iid Gaussian; **infinite fourth moment** |
| `centered_gamma_right` | \(\eta\) | Shape **0.5** centered Gamma: \((G-0.5)/\sqrt{0.5}\), positive skew; finite moments |
| `centered_gamma_left` | \(\eta\) | Negative of the same centered standardized Gamma, negative skew |
| `gaussian_jump_mixture` | \(\eta\) | Gaussian SD multiplier **8** with probability **0.02**, SD 1 otherwise, divided by \(\sqrt{0.98+0.02(8)^2}\) to retain marginal variance 1; finite fourth moment |
| `garch_t5_observation` | \(\eta\) | Standardized Student-t(5) shocks with \(h_0=1\) and \(h_t=0.05+0.10 e_{t-1}^2+0.85 h_{t-1}\), \(e_t=\sqrt{h_t}\xi_t\), \(\xi_t\) variance 1; unconditional target variance 1 and volatility persistence |
| `skew_normal_m6` | \(\eta\) | Population-centered standardized Azzalini skew-normal \(\alpha=-6\) |
| `skew_normal_m3` | \(\eta\) | Same, \(\alpha=-3\) |
| `skew_normal_0` | \(\eta\) | Same, \(\alpha=0\), symmetric Gaussian marginal reference with a different random generator |
| `skew_normal_p3` | \(\eta\) | Same, \(\alpha=+3\) |
| `skew_normal_p6` | \(\eta\) | Same, \(\alpha=+6\) |

The skew-normal generator uses \(Z=\delta|U|+\sqrt{1-\delta^2}V\), \(\delta=\alpha/\sqrt{1+\alpha^2}\), subtracts the **analytical population** mean \(\delta\sqrt{2/\pi}\) and divides by the **analytical population** SD \(\sqrt{1-2\delta^2/\pi}\). Gamma is also analytically centered and standardized. **Never re-center a given simulated sample using its realized sample mean**; that would alter the noise assumptions, erase stochastic variation and leak data between observations. The GARCH-t5 process is conditionally heteroskedastic and serially uncorrelated (not independent), and is initialized at its unconditional target \(h_0=1\), not drawn from the stationary volatility distribution.

**Cauchy:** deliberately excluded from the twelve-regime **mean-square-risk** study. For \(\eta\) Cauchy, there is **no finite population mean or variance**: \(\sigma_\eta\) would become a *Cauchy scale parameter* rather than an SD, and \(\lambda_G=\sigma_\eta^2/\sigma_\varepsilon^2\) and expected squared reconstruction risk cannot be defined in the same sense. The earlier exploratory [tail pilot audit](TAIL_NOISE_PILOT_AUDIT_2026-10-18.md) already considered it **separately**. A future Cauchy-specific nonzero-μ stress test must use finite-realization median absolute error and quantiles/win rates, without false mean-MSE, normal standard-error, or oracle claims. Cauchy is **not silently treated as the thirteenth finite law**.

## 4. Eight methods and honest validation

As before, all eight comparison methods see the *same synthetic observed \(y\)* for each paired draw. They reconstruct the same realized latent \(\tau\) afterwards.

1. Known true \(\mu\) and **known marginal variance ratio** \(b/a\): infeasible **linear benchmark**, not optimal nonlinear smoothing under non-Gaussian errors.
2. \(\mu=0\) forced, Gaussian difference-covariance **quasi**-MLE for \(a,b\).
3. \(\mu=0\) forced, pooled observed-series LOOCV for common \(\lambda\).
4. True known \(\mu\), Gaussian difference-covariance quasi-MLE for \(a,b\): **mean oracle**.
5. True known \(\mu\), pooled observed LOOCV on observations shifted by true \(\mu p\): **mean oracle**.
6. Pooled observed difference-mean *Guerrero-style plug-in* \(\widehat\mu=\operatorname{average}_{r,t}(D_dy^{(r)})_t\) plus **our** fitted Gaussian variance contrast; this is our hybrid, not the source's full estimator.
7. Common \(\mu,a,b\) from Gaussian differenced-covariance GLS-profile **quasi**-likelihood, feasible.
8. One common \(\mu\) fitted jointly with all trends within **exact fold-reestimated observed LOOCV** for one pooled \(\lambda\); feasible.

Pooled LOOCV means **minimizing average held-out observation losses** across \(R\), not averaging the \(R\) independently selected smoothness percentages. The true stochastic trend is never used to select parameters. For fitted-mean Gaussian/Guerrero hybrid, any naive PRESS keeping an all-data estimated mean fixed is diagnostic, not deletion-honest CV; only method 8 has joint mean refitted in each leave-one-observation-out fold.

Source mathematical note: [HOW_THE_SIMULATION_WORKS_AND_MEASURED_RESULTS.md](HOW_THE_SIMULATION_WORKS_AND_MEASURED_RESULTS.md). Gaussian model assumption is a *working likelihood* outside normality, and proper pairwise latent-MSE comparisons need to be stratified by regime/d/N/noise/μ/R, not blindly averaged between unlike stochastic trends.

## 5. Paired simulation phases and independent seeds

There are **12 finite regimes × 4 d × 2 N × 2 observational SDs = 192 distinct base strata**. Each has:

- **Pilot**: **25 independent R3 base shock draws per stratum**, total **4,800 base draws**, five paired μ values and nested R1/R3 -> **48,000 treatment pools and 384,000 method rows**. Pilot is exploratory/preflight and will be checked prior to any confirmatory interpretation.
- **Confirmatory, manual and NOT EXECUTED**: **10,000 entirely NEW independent R3 base draws per stratum**, total **1,920,000 base draws**, five paired μ values and nested R1/R3 -> **19,200,000 treatment pools / 153,600,000 method rows**. That scale is much larger than the earlier Gaussian-only 160k-base-draw campaign; it is **not** implied to have been run by completing the pilot.

Seed formula, exactly as implemented:

\[
s=126000000+10^9 I[\mathrm{confirmatory}]+10^7\,i_{\rm regime}
+10^6d+200000\,i_N+100000\,i_\eta+j,
\]
with \(j=0,\ldots,24\) (pilot) or \(j=0,\ldots,9999\) (confirmatory), \(\mathrm{regime\ index}=0,\ldots,11\) in the exact order shown in section 3. This is a PRNG distinct-integer seed convention, not a formal probability proof of fully independent random-number streams; in the Monte Carlo design, each fresh initialized stream is treated as an independent replication. **Pilot and confirmatory seed banks are disjoint**; do not reuse the pilot's 25 replicates in a confirmatory interval.

This study retains the *same random shock paths under different μ* but does not claim observation shocks are directly paired across different distributional regimes. Within a regime/d/N/noise/seed, all eight methods see identical \(y\). Student t3 has **finite second moment but infinite fourth**: although mean squared reconstruction risk can be finite, the variance of per-pool squared loss can be infinite; *ordinary normal Monte Carlo CIs from mean-MSE sample SE may fail*. We save those sample SD/SE as labelled **diagnostics only** under t3, not validated asymptotic inference. Median/absolute-error and paired win proportions are safer descriptive complements; exact pooled medians may need analysis of the stored gzip raw records in a separate robust audit.

For GARCH-t5, the unconditional covariance is diagonal for its innovations despite dependence in squared shocks; do **not** assert all GARCH temporal dependence makes Gaussian covariance identity wrong. The question instead becomes whether better distribution-aware selection would outperform Gaussian quasi-likelihood under conditional heteroskedasticity.

## 6. Reproducible artifacts, resuming and human execution

Runner: `experiments/pooled_loocv_smoothness/run_nonzero_mu_nongaussian.py`. Parallel launcher: `launch_nonzero_mu_nongaussian.py`. SHA/interval-checking aggregator: `aggregate_nonzero_mu_nongaussian.py`. Test source: `tests/test_nonzero_mu_nongaussian.py`.

Each immutable shard has `method_comparison.csv.gz`, `summary.json`, `manifest.json` with exact seed interval, distribution parameters from original source, Python/NumPy/SciPy, code SHA, outcome target and compressed artifact SHA256. Completed matching shards are checksum-verified and reused by reissuing the exact launch command; corrupted/incomplete/mixed code or partially overlapping seed intervals stop rather than overwrite. A small preflight must use a **separate `--root`**, or the full pilot's [0,25) shards will overlap its [0,1)/(0,2) interval.

Default launcher **only prints the plan**. `--execute` explicitly launches real jobs, with `--workers 32` permitted. Restrict BLAS to one thread per worker, and adjust workers downward if CPU/memory oversubscribed. The 384k pilot and 153.6M-row confirmation may consume substantial disk space: default gzip shards are not intended for ordinary Git tracking. Only **compact, SHA-verified aggregate CSVs and provenance** should be added to the existing research branch. Back up raw gzip results outside transient university workstations/VMs before deleting anything. Non-Gaussian confirmation is a separate reproducibility cohort and must never overwrite the completed Gaussian `audit_001/`.

### Local PowerShell commands

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_nonzero_mu_nongaussian.py -q

# Plan only, no Monte Carlo
python -m experiments.pooled_loocv_smoothness.launch_nonzero_mu_nongaussian --phase pilot --workers 32

# Tiny numerical preflight on the most difficult order:
python -m experiments.pooled_loocv_smoothness.launch_nonzero_mu_nongaussian --phase pilot --regime student_t3_observation --d 4 --n 200 --sigma-eta 2 --seed-stop 2 --workers 1 --root results/pooled_loocv_smoothness/guerrero/nonzero_mu_nongaussian/preflight_t3_d4 --execute

# AFTER inspecting the preflight, run just 25 fresh pilot seeds per stratum:
$env:OPENBLAS_NUM_THREADS="1"
$env:MKL_NUM_THREADS="1"
$env:OMP_NUM_THREADS="1"
$env:NUMEXPR_NUM_THREADS="1"
python -m experiments.pooled_loocv_smoothness.launch_nonzero_mu_nongaussian --phase pilot --workers 32 --execute

# Verify all raw gzip digests; record compact pilot aggregates:
python -m experiments.pooled_loocv_smoothness.aggregate_nonzero_mu_nongaussian --phase pilot --require-complete --verify-digests --out-dir results/pooled_loocv_smoothness/guerrero/nonzero_mu_nongaussian/audit_pilot_001
```

**Pilot output expectation** in the compact audit: 192/192 strata, 4,800 independent base R3 shock draws, 48,000 paired/nested treatment pools and **384,000** method rows, code SHA fixed across all shards. The pilot is **NOT YET RUN** as of this protocol. **Do not start `--phase confirmatory --execute` solely because the code exists.** Confirm the pilot's numerics, interpretation and completeness, then freeze any changes and run the 10k-seed confirmatory phase with the **disjoint phase seed bank**. At default 100 base draws/shard for the confirmation there will be 19,200 compressed shards, potentially large disk/compute requirements; the raw output is explicitly excluded by Git.

### Later extension

Once finite-variance noise is validated, add a *separate* Cauchy (no MSE population risk), possibly contaminated/skewed trend innovations beyond Student t3, or actual empirical-return-shaped noise. These are new protocols, not proof that the observed trend of a real stock is known. The main scientific conclusion is conditional: *when and how does mean misspecification versus penalty selection affect stochastic latent trend reconstruction under non-Gaussian disturbances?* This experiment tests the question; it does **not** presuppose LOOCV must win.
