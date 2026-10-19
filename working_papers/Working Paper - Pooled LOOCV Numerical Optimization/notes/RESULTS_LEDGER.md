# Results and simulation provenance ledger — independent pooled observed-series paper

**Maintained as of 2026-10-18 local.** This table answers: *what was simulated, what was actually run, where is each result saved, how can we reproduce it, and what is not yet evidence?*

Keep different DGPs and estimands separate, even when they share `PooledLOOCV`. Never replace an earlier committed result silently with a newly generated run. The source manifest's `git_sha` is the code version of the executed run; current branch tip may be later.

| Study | Simulation mechanism / scientific question | Experimental size and run status | Stored artifacts and authoritative note |
|---|---|---|---|
| **A. Original deterministic-trend pooled LOOCV** | Cortés-Toto-inspired 16-factor cells: linear/nonlinear signal, seasonality no/yes, observation SD 0.5/2, N=50/200, Gaussian measurement noise; pool identical *deterministic* truth with independent noisy replicas. Focus = numerical minima of LOOCV. | **EXECUTED/COMMITTED** 16 cells × 5 seeds × nested R1/3 = **160 pools / 480 method rows** | `results/pooled_loocv_smoothness/pilot/`; [pilot audit](PILOT_AUDIT_2026-10-18.md), runner `experiments/pooled_loocv_smoothness/run.py`. |
| **B. Guerrero DGP, true known variance ratio** | **Stochastic** \(D_2\tau=\varepsilon\), \(y=\tau+\eta\), iid Gaussian shocks with known standard deviations; compare \(\lambda_G=\sigma_\eta^2/\sigma_\varepsilon^2\) against bounded/multibracket/grid observed LOOCV. Evaluates LOOCV and latent true-trend MSE separately. | **EXECUTED/COMMITTED** 12 cells × 5 seeds × nested R1/3 = **120 pools / 480 method rows** | `results/pooled_loocv_smoothness/guerrero/pilot/`; [known-ratio pilot audit](GUERRERO_RATIO_PILOT_AUDIT_2026-10-18.md), generator/runner `guerrero_ratio.py`. |
| **C. Guerrero DGP, both variances estimated** | Same 12 stochastic Gaussian cells: estimate the two variances from \(D_2y\) using (a) Gaussian differenced-covariance likelihood; (b) nonnegative quadratic moments. Compare with *true-ratio oracle* and LOOCV. True latent trend used only for final MSE evaluation. | **EXECUTED/COMMITTED** 12 cells × 5 seeds × nested R1/3 = **120 pools / 480 method rows** | `results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/`; [estimated-variance pilot audit](VARIANCE_ESTIMATION_PILOT_AUDIT_2026-10-18.md), code `variance_estimation.py` and `run_variance_estimation.py`. |
| **D. Robustness: noise-model misspecification** | Five regimes: iid Gaussian, Student-t observation, Student-t trend innovation, Gaussian AR1 observation, Gaussian half-sample heteroskedastic observation; fixed \(\sigma_\varepsilon=0.3\), eta SD 0.5/2, N50/200. Identical fitted PLS smoother; compare Gaussian-difference ML, observed LOOCV Brent, multibracket, moments, and *nominal* ratio. | **IMPLEMENTED / TESTABLE**: tiny **CI smoke** has five regimes, N24, **10 nested pools / 50 method rows**. Full pilot **NOT YET COMMITTED AS EXECUTED**: 20 cells × 5 seeds × R1/3 = **200 nested pools / 1000 rows**. | Expected manual outputs `results/pooled_loocv_smoothness/guerrero/robustness/pilot/`; [locked protocol](ROBUSTNESS_PROTOCOL.md), runner `run_robustness.py`. |

### A/B/C design and seeds, not interchangeable

- A manifest: `results/pooled_loocv_smoothness/pilot/manifest.json`, independent seed offset **100000**, difference order 2, log penalty domain [-20,35], R=1,3, 401-point grid and 101-point derivative scan. Simulation was originally run with NumPy 2.4.6, SciPy 1.17.1 and Python 3.11.16. Verified **160** pooled cases.
- B manifest: `results/pooled_loocv_smoothness/guerrero/pilot/manifest.json`, seed base **20262000**, `seed = seed_base + 10000*scenario_id + replicate`, N=50/200, sigma_eta=0.5/2, sigma_epsilon=0.1/0.3/1.0, d=2. For each pool, independent latent stochastic trajectories across r and independent Gaussian observation errors. `lambda_G` uses **true** simulation variances. Verified **120** pooled cases.
- C manifest: `results/pooled_loocv_smoothness/guerrero/estimated_variances/pilot/manifest.json`, seed base **20262000**, identical stochastic Gaussian generator and matching scenario order to B; a *methodological extension using the same simulated data*, not independent replication of B. The method-of-moments zero trend-innovation variance is retained even if this makes lambda infinite. Verified **120** pooled cases.
- D seed base **30610000** for smoke/pilot and **31610000** for future confirmatory simulations, with the scenario-order formula in [ROBUSTNESS_PROTOCOL.md](ROBUSTNESS_PROTOCOL.md). R1 and R3 intentionally share the first generated observation series. **Do not combine nested R1/R3 as independent seed outcomes.** D differs from B/C both by new seed baseline and DGP regimes.

### What our logs actually preserve

1. **Explicit DGP equations and parameter grid:** documented mathematical trend recurrence, stochastic error laws, variance factors and noise correlation; source code is the executable specification.
2. **Randomness:** declared base seed, formula, per-scenario `seed` in per-method CSV, NumPy PCG-backed `default_rng`, deterministic R1/R3 pairing.
3. **Software and implementation:** Python, NumPy, SciPy versions, source commit SHA, fixed difference order and search bounds/scans in each run manifest.
4. **Experimental outputs:** per-method \(\widehat\lambda\), smoothness \(S\), observed LOOCV MSE, simulated latent reconstruction MSE when available, selected methods and failure diagnostics, aggregated JSON, small explanatory figures.
5. **Audit status:** reports distinguish **planned**, **CI smoke**, **executed/committed pilot**, **independent confirmatory**, and **mathematically certified**. None of the executed pilots establishes general superiority of a new optimization technique.

### Limits and safeguards

- Some runs store **generated outputs and exact regeneration settings** rather than full time-series arrays; to reproduce raw \(y,\tau\), use the original `git_sha` and explicit seeds. Re-running on a later changed branch should not be silently called a byte-for-byte reproduction.
- Hardware and exact CPU BLAS build are not fully specified for past runs; elapsed times are not portable comparisons. The stochastic Monte Carlo study is numerical, not a financial experiment.
- The nominal known-variance ratio is **not an oracle** for AR1 or heteroskedastic covariance regimes. Differenced Gaussian likelihood is an **extension**, *not an estimation technique claimed to have been introduced by Guerrero (2007)*.
- No extrapolation or future horizon enters this independent observed-series paper. Correlated errors may violate ordinary LOOCV's statistical interpretation.
- Store lightweight experiment results/notes in Git on branch `paper/pooled-loocv-numerical-optimization`. **Do not open PRs or merge**. Automatic CI may run only small validation smoke; full pilots, confirmatory campaigns, large figures, and document builds remain **manual-only**.

### Remaining decisions

After D's manual pilot is uploaded, audit paired **R=3** latent true-MSE differences by regime, sigma_eta and N; plot failures and objective-vs-reconstruction tradeoffs; check if Gaussian ML's slight earlier advantage survives misspecification. Before interpreting uncorrected LOOCV under AR1 as a predictive method, construct a separate covariance-aware or blocked-validation benchmark. New *independent* confirmatory seeds should only be run after this design and its inference are finalized.
