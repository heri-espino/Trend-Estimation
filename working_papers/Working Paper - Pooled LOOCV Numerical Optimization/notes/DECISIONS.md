# Research decisions and unresolved issues

## D001 — 2026-10-18 — Independent manuscript
**Decision:** new stand-alone working paper. Neither a section of the older Numerical Methods working paper nor an extension of the horizon-matched forecast CV paper. No forecasting language or objectives.

## D002 — 2026-10-18 — Exact selection target
**Decision:** first average LOOCV MSE scores over R comparable series *at a common smoothing parameter*, then minimize the pooled function. Do not average argmins. R=1 is the non-pooled classical comparator.

## D003 — 2026-10-18 — Index semantics
**Decision:** optimize in λ or log λ numerically, report normalized S∈[0,1], and present original Guerrero index separately. Fixed d and N within pools. Evaluate endpoint λ=0,∞ exactly, not by epsilon surrogates.

## D004 — 2026-10-18 — Numerical honesty
**Decision:** bounded Brent = local; multibracket derivative Brent = uncertified sign-changing-root search; exact Sturm = small rational inputs only. Dense grid = finite numerical reference. Classification and numerical completeness still need validation.

## D005 — 2026-10-18 — Source-inspired design
**Decision:** preserve the four primary factors of Cortés-Toto et al. (2017); treat R pooling as a transparent additional factor. Use independent seeds and preserve simulated latent trend exclusively for descriptive reconstruction/oracle diagnostics, never feasible tuning.

## D006 — 2026-10-18 — Financial example
**Decision:** potentially include an index and an exchange rate with documented adjusted-price/source/preprocessing and no forecasting or investment-return claim. Do not download unlicensed/raw market data into the repository automatically.

## Open decisions
- Is there a genuine improvement over existing *global* CV optimization algorithms?
- Which score scaling permits economically sensible multi-asset pooling?
- Whether derivative-sign-only bracketing is insufficient; consider certified interval methods if empirical misses are material.
- Whether the journal scope should emphasize computational algorithms or statistical simulation.
- Whether experiments favor LOOCV, GCV, or no difference: negative results must be documented.

## D007 — 2026-10-18 — Evidence provenance ledger and DGP separation
**Decision:** Maintain [RESULTS_LEDGER.md](RESULTS_LEDGER.md) to identify exactly which simulations were generated, seed formulas, output manifests/CSVs, and whether each campaign is *implemented*, *CI smoke*, *executed and committed*, or *independent confirmatory*. The original deterministic-trend factorial, stochastic known-ratio benchmark, and estimated-variance experiment are **distinct**. R=1 pools are nested within R=3 at the same seed; never report nested outcomes as independent evidence.

## D008 — 2026-10-18 — Feasible fitted variance-ratio extension
**Decision:** Fit Gaussian likelihood of differenced observations `D_2y` and nonnegative two-moment variance estimates as **extensions**, not algorithms proposed by Guerrero (2007). Known true noise ratio is an informational oracle under the iid model. Under correctly specified Gaussian simulation, fitted Gaussian covariance likelihood came close to oracle true trend MSE; direct LOOCV minimized observed LOOCV; the constrained-moment estimator had catastrophic zero-innovation-variance boundaries. Record that failure instead of deleting it.

## D009 — 2026-10-18 — Locked robustness mechanisms
**Decision:** Keep noise model as the experimental factor while the smoother and trend-reconstruction target remain fixed. Prespecify five mechanisms (Gaussian baseline, Student-t measurement noise, Student-t trend innovations, Gaussian AR1 measurement noise, changing observation variance), pilot 20 scenarios × 5 seeds × nested R=1/3, then only **after auditing** choose an independent confirmatory design. In covariance-misspecified regimes, the true marginal variance ratio is a *nominal reference*, **not** a valid statistical optimality oracle. See [ROBUSTNESS_PROTOCOL.md](ROBUSTNESS_PROTOCOL.md).

## D010 — 2026-10-18 — Git workflow explicitly requested by user
**Decision:** **No PRs** for this project. Commit directly to the existing `paper/pooled-loocv-numerical-optimization` branch and push there. Do not merge or force-push. All substantial Monte Carlo campaigns are manual-only; automatic CI runs only lightweight tests and tiny smoke checks.

## D011 — 2026-10-18 — Completed five-regime robustness pilot and research boundary
**Observation after results, not a predeclared assumption:** the locked five-regime pilot was executed; its per-method CSV and manifest were committed. For R=3, Gaussian difference-likelihood true-trend MSE averaged **0.542908** versus **0.620746** for observed pooled LOOCV (76/100 paired wins), with roughly **91% of their aggregate equal-regime-mean absolute MSE gap due to AR(1)**. The iid Gaussian group was approximately tied on mean MSE; R=1 with Student-t trend innovations reversed the mean ordering. Single-start and multibracket reached equivalent LOOCV objectives at tolerance 1e-7 in all R=3 pools. See [ROBUSTNESS_PILOT_AUDIT_2026-10-18.md](ROBUSTNESS_PILOT_AUDIT_2026-10-18.md).

**Scientific decision:** do not use the pooled five-regime mean to claim broad Gaussian MLE superiority. AR(1) dependence leakage from ordinary observation-level LOOCV, and misspecification of both covariance models, require an explicit covariance-aware/dependence-aware comparator before confirmatory runs.

## D012 — 2026-10-18 — Heavy-tail robustness and Cauchy evaluation contract
**Decision:** implement a new independent **8-regime**, manual-only simulated noise campaign without modifying the completed Gaussian/robustness pilots. Include Student-t(3) observation or trend innovations, centered Gamma with positive and negative skew, rare Gaussian mixture shocks, Student-t(5) GARCH conditional-volatility shocks, a Gaussian iid control, and Cauchy noise as an *extreme mathematical stress test*. Store seed formula, noise laws, shape parameters, per-method selected lambda and both loss types when their target is defined. Research plan: [TAIL_NOISE_PROTOCOL.md](TAIL_NOISE_PROTOCOL.md). Full pilot = 32 cells × 5 seeds × nested R1/3 = 320 pools, three feasible selectors = 960 method rows. **Not run or interpreted until results exist.**

**Mathematical boundary:** a centered Gamma is a shifted Gamma (not a standard positive Gamma); Cauchy has zero *median* but **undefined mean/variance**, so Gaussian fitted components are pseudo-values and Guerrero's true variance ratio is not defined. For Cauchy do NOT treat finite realized sample mean squared error as an estimate of finite expected risk; report median per-pool MSE and absolute-error quantiles. The closest stock-market motivation is heavy-tailed and asymmetric *return* distributions and conditional volatility clustering, but our synthetic (y=	au+eta) cannot be called a calibrated stock-return generator. Mathematical derivation: [GAUSSIAN_MLE_AND_LOOCV_EXPLAINED.md](GAUSSIAN_MLE_AND_LOOCV_EXPLAINED.md). 

## D013 — 2026-10-18 — Revision before any heavy-tail pilot: d levels and skew-normal
**Decision before running:** expand the original proposed d=2, eight-regime noise stress study to **matched true and fitted d∈{1,2,3}** and **five population-centered skew-normal shape values α=-6,-3,0,3,6**. Generator enforces (D_d\tau=\varepsilon) via binomial-coefficient recursion and verifies it with dedicated tests. The skew-normal distribution is centered by its population analytic mean and rescaled by its population variance, **not** per realization. All methods in a cell fit with the same d that generated the trend. This is NOT a misspecified-order experiment.

The exploratory study now contains 13 distribution settings × 3 orders × 2 N × 2 noise scales = **156 cells**, 5 seeds, R1/3 nested: **1,560 pools, 4,680 method rows**. Primary reported comparisons must be stratified by **d**, noise family and scale because integrated trend magnitudes differ substantially across d. The prospective confirmatory 31,200-pool study is manual-only and unexecuted. This amendment was recorded **before seeing any v2 pilot results**; prior results are intact. Details in [TAIL_NOISE_PROTOCOL.md](TAIL_NOISE_PROTOCOL.md).

## D014 — 2026-10-18 — Uploaded expanded tail-stress pilot; cautious conclusions

**Status:** user ran and pushed the full version-2 tail-stress simulation, **156 scenarios × 5 replicates × nested R1/3 = 1,560 paired pools, 4,680 method rows**. Complete source CSV, summary and manifest are committed, source SHA in manifest `c215089c4adb737e5e8ed67ce91237d8961adad9`, base seed `47800000`. The independently computed findings and all caveats are in [TAIL_NOISE_PILOT_AUDIT_2026-10-18.md](TAIL_NOISE_PILOT_AUDIT_2026-10-18.md).

Among 720 finite-variance R3 pools, Gaussian difference likelihood had lower realized latent trend MSE in 427, with overall mean **0.322573** vs LOOCV **0.329322**. Stratified by matched d, ML / LOOCV means were d1 **0.207687 / 0.208839**, d2 **0.338310 / 0.348313**, d3 **0.421723 / 0.430813**. These **do not rank d**, because true generator changed with d. Cauchy observation noise requires separate treatment: Gaussian fitted pseudo-variances do not describe true finite noise variances, and Gaussian ML produced lower realized trend MSE in only **18/60** R3 Cauchy pools. Brent methods found equivalent observed LOOCV optima within `1e-7` across 780 R3 pools, despite multiple derivative sign-change candidates in seven.

**Decisions:** preserve all raw Monte Carlo errors, including Cauchy and infinite-lambda boundary estimates; report d-stratified means only for finite-variance noise and median per-pool robust absolute errors for Cauchy. Do not claim general ML superiority, stock-market calibration, or multibracket numerical improvements. The next *distinct* scientific experiment should hold the SAME latent data fixed and compare fitted d candidates fairly, ideally including a feasible method for selecting d without knowledge of the true trend; run only after defining the validation criterion and fresh seeds. Maintain user preference for direct branch commits and no PRs.

## D015 — 2026-10-19 — Keep analyst-fixed d; test empirical return-shaped noise without claiming market trend truth

**User clarification:** for the pooled observed-LOOCV paper, select d on statistical/modeling grounds as an analyst assumption, then pool losses (F_d(\lambda)=R^{-1}\sum_r CV_r(\lambda)) and find its common minimizing lambda/S. **Do not automatically optimize d** merely because the controlled matched-order sensitivity factorial happened to examine d=1,2,3. Nor treat mean of per-series optimum S as a substitute for minimization of mean losses.

**New independent empirical-noise pilot F is CODE ONLY, not yet actually executed on market data:** use SPY adjusted closes from 2015–2025, converted to daily log returns with empirical shape calibrated by population centering/SD. Compare matched Gaussian, iid historical-return resampling, and moving circular blocks (5/20). Generate artificial known latent trend \(\tau\) and (Y=\tau+\eta), so \(\tau_t\) is exactly the conditional expectation of the synthetic observed data, *not* the market stock-price mean or a privileged real price trend. Use common seed for the same latent tau across mode and scale comparisons, fixed d=2, and nested R1/R3. Keep source returns local under .gitignore; hashes/dates and independent Monte Carlo artifacts stored in run manifest. Full protocol: [EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md](EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md).

**Scientific prediction to test, not assume:** correctly specified Gaussian *density* may be efficient under normality, but Gaussian **quasi-likelihood** can still estimate variance ratios effectively for non-Gaussian independent finite-variance errors because the covariance equations remain correct. Dependence may matter more than marginal skewness. Five-seed pilot is exploratory; a proper distribution-sensitive robust comparator would be needed to demonstrate optimality outside Gaussian models.

## D016 — 2026-10-19 — Literal return-mean control remains separate

The market-calibrated Monte Carlo now also supports `--trend-kind constant_mean`, setting the true synthetic conditional mean at every date to the empirical historical daily log-return mean `rbar`. This is an explicit additional **boundary-case** experiment with (D_d\tau=0), zero process-innovation variance and a mathematically infinite nominal variance ratio, unlike the default stochastic-trend study. For a natural constant-mean fit, analyst picks `--d 1`. Its output root contains `constant_mean/` to prevent overwriting the main financial-noise pilot. Neither design asserts stock prices have known latent trends; both use real financial log-return noise shapes with separately generated synthetic conditional means. See [EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md](EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md).

## D017 — 2026-10-19 — Nonzero difference mean, honest CV and proper Guerrero attribution

**Decision after user approval:** preserve analyst-selected (d=2) and fixed common pooled LOOCV parameter (λ); introduce an **independent**, manually run simulation with (Δ^2\tau=\mu+\varepsilon), (μ/\sigma_\varepsilon\in\{-1,-.25,0,.25,1\}). Seven selectors separate wrong zero mean, externally known mean, jointly estimated common mean, and known-variance oracle. Estimating μ with all data then calling ordinary frozen-mean PRESS is **not deletion-honest**. Added an analytically derived exact joint pooled PRESS for a common μ estimated from training observations, and Gaussian differenced-data GLS-profile likelihood for μ,a,b. Tests compare full PRESS residuals to explicit deletion-refitting of both latent trends and μ.

**Attribution:** Guerrero (2007) already allows μ≠0 and a data plug-in; the [existing independent mean-difference forecasting paper](../../Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting/README.md) also profiles μ for completed historical h-step forecast loss. Neither is our current observed-series LOOCV criterion and no novelty claim follows from affine PLS or Gaussian profiling algebra. Estimating μ changes EDF/nullity of pooled penalty; original smoothness S remains only a nominal scalar penalty coordinate. Full pilot NOT YET RUN: 20 design cells, 5 shared-shock seeds and nested R=1/3, 200 pools/1400 method rows. Full source-aware protocol in [NONZERO_DIFFERENCE_MEAN_PROTOCOL.md](NONZERO_DIFFERENCE_MEAN_PROTOCOL.md). No PR, no merge, no automatic heavy simulations.
