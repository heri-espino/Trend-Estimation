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
