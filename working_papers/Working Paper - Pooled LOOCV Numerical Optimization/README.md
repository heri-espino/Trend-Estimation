# Working Paper — Numerical Optimization of Pooled LOOCV Smoothness

**Status:** independent working paper, initiated 2026-10-18; Gaussian 160k-draw fixed-order/mean-difference reconstruction confirmation completed 2026-10-19; non-Gaussian joint-mean extension remains prospective.  
**Prospective venue:** SMCCA (journal scope and submission requirements must be verified before submission).  
**Working title:** *Numerical Optimization of Penalized Trend Smoothness by Pooled Leave-One-Out Cross-Validation*.

## Central question

Can numerical stationary-point searches, including multibracket Brent root refinement and *restricted exact* Sturm isolation, reliably locate the global minimum of a pooled leave-one-out cross-validation (LOOCV) loss for classical penalized least-squares (PLS) trends?

The statistical basis is **Cortés-Toto, Guerrero and Reyes (2017)**, especially their PLS/CV experiment. We study **observed-series reconstruction only**. NO forecasting horizons, forecast-origin splits, out-of-sample forecast claims, or dynamic tracking of branches. A **distinct, completed sensitivity experiment** additionally compares fixed/estimated nonzero trend-difference means within pooled retrospective observed-series reconstruction; it is not the separate horizon-h forecast-mean project.

## Independent scope

For R observed, equally long series (same N, same penalty order d), compute the ordinary PLS smoother

\[
H_\lambda=(I_N+\lambda D_d^\top D_d)^{-1}.
\]

For series r, define the exact LOOCV score at positive finite λ:

\[
C_r(\lambda)=\frac1N\sum_{i=1}^N
\left[\frac{y_i^{(r)}-(H_\lambda y^{(r)})_i}
{1-(H_\lambda)_{ii}}\right]^2 .
\]

**Pool the functions, not their minimizing parameters:**

\[
F_R(\lambda)=\frac1R\sum_{r=1}^R C_r(\lambda),\qquad
\widehat\lambda\in\arg\min_{\lambda\in[0,\infty]}F_R(\lambda).
\]

Report the common normalized index

\[
S(\lambda)=\frac{N-\operatorname{tr}(H_\lambda)}{N-d}\in[0,1].
\]

For R=1 this reduces to traditional single-series LOOCV. Group only statistically comparable series; standardize first if their units or scales differ. Exact limits are used at S=0 (λ=0) and S=1 (λ=∞). Guerrero's original index is \(S_G=(N-d)S/N\); the normalized S here is a reparameterization, **not a new index**.

## Starting point and limits on novelty

- **Established:** PLS smoothing, Guerrero's smoothness index (2007), ordinary LOOCV and GCV, Cortés-Toto et al.'s (2017) 2^4 experiment, Brent's optimization/root finding, and Sturm's theorem.
- **Existing optimization prior art:** Mohammadzadeh and Kent, *Global Optimization of the Generalized Cross-Validation Criterion* (provided reference, check complete bibliographic metadata). Do not claim the first global CV optimizer.
- **Potential contribution to evaluate:** a well-defined, efficient *pooled LOOCV* objective; its rational stationary-point structure; robust interior/boundary candidate recovery; tested algorithms with explicit failure and certification conditions.
- Standard Brent in a bounded interval is **local**; finite derivative scans can miss even-multiplicity roots; exact Sturm certification is limited to small exact-rational cases. No universal global certificate is claimed for general floating-point simulations.

## Research-first files

1. [Research notebook](notes/RESEARCH_NOTEBOOK.md) — question, assumptions and proposed narrative.
2. [Proof ledger](notes/PROOF_LEDGER.md) — exact derivations, degenerate cases and proof gaps.
3. [Simulation atlas](notes/SIMULATION_ATLAS.md) — original 2017 factorial and experimental contrasts.
4. [Literature and novelty audit](notes/LITERATURE_POSITIONING.md).
5. [Decision log](notes/DECISIONS.md).
6. [Completed first pilot audit](notes/PILOT_AUDIT_2026-10-18.md) — 160 observed pools, numerical caveats.
7. [Guerrero variance-ratio benchmark](notes/GUERRERO_VARIANCE_RATIO_PROTOCOL.md) — a separate stochastic-trend experiment comparing known noise ratio with true trend MSE.
8. [Guerrero ratio CI smoke findings](notes/GUERRERO_RATIO_SMOKE_2026-10-18.md) — verified first comparison of observed LOOCV and latent MSE (8 tiny pools).
9. [Completed Guerrero ratio pilot audit](notes/GUERRERO_RATIO_PILOT_AUDIT_2026-10-18.md) — 120 uploaded pools, two loss definitions, independent R=3 analysis and numerical limits.
10. [Estimated-variance pilot audit](notes/VARIANCE_ESTIMATION_PILOT_AUDIT_2026-10-18.md) — completed 120 pools, likelihood estimates, catastrophic moments boundaries and variance-level breakdown.
11. [Results and reproducibility ledger](notes/RESULTS_LEDGER.md) — actual executed campaigns, exact simulation generators, fixed seeds, evidence boundaries.
12. [Locked robustness protocol](notes/ROBUSTNESS_PROTOCOL.md) — heavy-tailed, autocorrelated and changing-variance simulated errors, with independent pilot seeds.
13. [Completed robustness pilot audit](notes/ROBUSTNESS_PILOT_AUDIT_2026-10-18.md) — five noise regimes, 1,000 saved method rows, exploratory R=3 paired evidence.
14. [Gaussian MLE and LOOCV explained](notes/GAUSSIAN_MLE_AND_LOOCV_EXPLAINED.md) — stepwise likelihood derivation and true-trend MSE distinction.
15. [Heavy-tail noise protocol](notes/TAIL_NOISE_PROTOCOL.md) — Cauchy, Student-t3, centered Gamma skew, Gaussian jump mixtures, and GARCH-type clustering.
16. [Completed d=1–3 tail-noise pilot audit](notes/TAIL_NOISE_PILOT_AUDIT_2026-10-18.md) — 4,680 result rows, matched-order comparisons, Cauchy limits, skew-normal and detected roots.
17. [Empirical market-return Monte Carlo protocol](notes/EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md) — SPY return histogram, iid versus block resampling, fixed analyst d and observed pooled LOOCV.
18. [Nonzero mean of trend differences](notes/NONZERO_DIFFERENCE_MEAN_PROTOCOL.md) — exact GLS mean profiling and deletion-safe pooled observation LOOCV, including known-mean oracles.
19. [Executed nonzero-mean pilot audit](notes/NONZERO_DIFFERENCE_MEAN_PILOT_AUDIT_2026-10-19.md) — 1,600 saved method rows, paired observed mean-shift effects, eight baselines and two committed figures.
20. [Exact simulation and measured results](notes/HOW_THE_SIMULATION_WORKS_AND_MEASURED_RESULTS.md) — actual latent trend recursion, eight estimators, independent-shock grouping and original pilot statistics.
21. [10,000-seed multorder confirmatory protocol](notes/MULTIORDER_10000_SEED_CONFIRMATORY_PROTOCOL.md) — d=1,2,3,4; shard control; code SHA, paired Monte Carlo inference and numerical preflights.
22. [Completed Gaussian 160k-draw confirmatory audit](notes/MULTIORDER_10000_SEED_CONFIRMATORY_RESULTS_2026-10-19.md) — per-(d,N,noise) paired MSE, 95% Monte Carlo intervals and single-series exceptions.
23. [Full eight-method breakdown for all 160 confirmed scenarios](notes/EIGHT_METHODS_BY_SCENARIO_160.md) — no averaging across N, noise, order, mu or pool size; [wide downloadable CSV](../../results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/audit_001/eight_methods_all_160_scenarios.csv).
24. [New non-Gaussian + nonzero-mean Monte Carlo protocol](notes/NONGAUSSIAN_NONZERO_MU_PROTOCOL_2026-10-19.md) — 12 noise distributions, 4 difference orders, mean shifts and moment-aware interpretation; pilot unrun.
25. [Cortés-Toto criteria versus Gaussian MLE, with a common estimated μ and numerical search](notes/CORTES_TOTO_CRITERIA_AND_NUMERICAL_COMPARISON_PROTOCOL_2026-10-19.md) — original CV/GCV/AICc/BIC, pooled joint EDF, controlled smoothness, source-aware search caveats; large comparison **not run**.
26. [Study K.1 exact 25-seed paired 26-method replay](notes/CORTES_TOTO_PAIRED_25_SEED_REPLAY_PROTOCOL_2026-10-19.md) — 32-worker manual, full same-seed J baseline checks, 192 cells and 1.248M per-method rows, **NOT RUN**.
27. [Completed matched 25-seed exploratory 26-method results](notes/CORTES_TOTO_PAIRED_25_SEED_REPLAY_RESULTS_2026-10-19.md) — 192 strata, R1/R3, 12 noise laws, BIC-boundary pathology, original estimator parity and solver confound.
28. [Agent handoff](AI_HANDOFF.md).

## Runnable independent pilot

Run from the repository root with the project's existing NumPy/SciPy/matplotlib dependencies:

    python -m experiments.pooled_loocv_smoothness.run --preset smoke --out-dir results/pooled_loocv_smoothness/smoke
    python -m pytest tests/test_pooled_loocv_smoothness.py -q

Preview the larger predeclared plan without running it:

    python -m experiments.pooled_loocv_smoothness.run --preset pilot --dry-run

For small rational input, separately:

    python -m experiments.pooled_loocv_smoothness.sturm_exact

The smoke and first 16-cell **pilot were executed and pushed** on 2026-10-18. See the [pilot audit](notes/PILOT_AUDIT_2026-10-18.md) for descriptive results and limitations. The confirmatory campaign, financial application, theorem/counterexample verification, and manuscript refinement remain prospective.

## Independent Guerrero (2007) benchmark

We separately simulate `D_2 tau = epsilon` and `y = tau + eta`, so the ratio `lambda_G = sigma_eta^2 / sigma_epsilon^2` is **known**. We compare it to Brent-selected pooled LOOCV and record both LOOCV MSE and true latent-trend MSE. The known ratio uses oracle simulation parameters and is not a variance estimator for market series.

An eight-pool [Guerrero ratio smoke](notes/GUERRERO_RATIO_SMOKE_2026-10-18.md) has run successfully in isolated GitHub CI. Run `python -m experiments.pooled_loocv_smoothness.guerrero_ratio --preset smoke` locally to save its artifacts. The [benchmark protocol](notes/GUERRERO_VARIANCE_RATIO_PROTOCOL.md) defines a separate 12-scenario pilot (120 pools). The **pilot has now been executed and pushed**: see the [pilot audit](notes/GUERRERO_RATIO_PILOT_AUDIT_2026-10-18.md). It does not overwrite the completed 2017-inspired 16-cell pilot.

## Variances estimated rather than known

The [variance-estimation protocol](notes/VARIANCE_ESTIMATION_PROTOCOL.md) compares the known (oracle) Guerrero ratio with **feasible Gaussian difference-covariance likelihood**, nonnegative quadratic moments, and LOOCV. The 12-scenario **pilot is executed and pushed**. See the [measured pilot audit](notes/VARIANCE_ESTIMATION_PILOT_AUDIT_2026-10-18.md); Gaussian ML approached the known-ratio mean true trend MSE for R=3, but the moment method had severe boundary failures. **Neither feasible procedure is claimed to be an estimator prescribed by Guerrero (2007).** The exploratory results are not a global numerical-optimizer novelty claim.

`python -m experiments.pooled_loocv_smoothness.audit_variance_estimation` generates per-scenario diagnostics and three figures manually, using the saved uploaded CSV. The ordinary lightweight CI checks the audit without regenerating those charts.

## Next experiment: robustness to misspecified noise

We have now **implemented** a fifth independent experimental campaign, without rerunning or overwriting prior results. It compares the fitted Gaussian difference-likelihood variance ratio, pooled observed LOOCV (single-start and multibracket), constrained moments, and a nominal known-variance ratio under **five data-generating regimes**: correctly specified iid Gaussian; Student-t observations; Student-t trend innovations; AR(1) observations; and time-varying observation variance. Under the last two regimes the nominal ratio is *not a valid oracle* because the covariance structure differs.

The [locked design](notes/ROBUSTNESS_PROTOCOL.md) calls for 20 scenarios × 5 seeds × nested R=1/3 = **200 pools**, 1000 method-level observations. The full pilot **has now been executed and committed**, with a [detailed observed-results audit](notes/ROBUSTNESS_PILOT_AUDIT_2026-10-18.md). Run `python -m experiments.pooled_loocv_smoothness.run_robustness --preset smoke` for the tiny check and `--preset pilot` for the manually initiated experiment. Read the [results ledger](notes/RESULTS_LEDGER.md) for the exact independent seeds, executed status, numerical limitations and output paths. An independent CSV audit is provided by `python -m experiments.pooled_loocv_smoothness.audit_robustness`; use `--figures` for manual plots.

**Repository action policy:** commit directly to `paper/pooled-loocv-numerical-optimization`; no PR creation, no merging into main, and no automatic heavy Monte Carlo.

## Heavy-tailed and asymmetric noise (new separate campaign)

We implemented a new **13-distribution-setting, three-difference-order research stress test** of noise distribution assumptions, with **no changes to existing committed experimental outputs**. The Gaussian difference-likelihood selector, one-start LOOCV, and multibracket LOOCV are compared on the same generated data. Student-t3 has finite variance but infinite fourth moment; centered Gamma has mean 0 and skew; GARCH-t5 introduces volatility clustering; Cauchy has **undefined variance and expected squared-error risk** (report robust quantiles instead). The [revised, unrun protocol](notes/TAIL_NOISE_PROTOCOL.md) crosses d∈{1,2,3}, five population-centered skew-normal shapes α=-6,-3,0,3,6, and the original eight regimes: **156 scenarios × 5 seeds × nested R1/3 = 1,560 pools, 4,680 method rows**. The **expanded pilot has now been run and uploaded**. Its findings and limitations are documented in the [completed tail-noise pilot audit](notes/TAIL_NOISE_PILOT_AUDIT_2026-10-18.md). Confirmatory research remains unrun; CI stays lightweight.

`python -m experiments.pooled_loocv_smoothness.run_tail_noise --preset pilot` runs the exploratory pilot manually and saves CSV/JSON/manifest under `results/pooled_loocv_smoothness/guerrero/tail_stress/pilot/`. The [results ledger](notes/RESULTS_LEDGER.md) identifies the executed pilot and source SHA; the new saved-data re-audit uses `python -m experiments.pooled_loocv_smoothness.audit_tail_noise` without regenerating the simulations. No PRs; commit only to the existing independent paper branch.

## Next independent experiment: financial return histogram as synthetic noise

The user correctly specifies **analyst-fixed difference order d**, followed by pooling **LOOCV losses** to choose a common penalty; this differs from averaging series-by-series best smoothness percentages. See [the financial Monte Carlo protocol](notes/EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md) for the exact mathematical distinction.

The **implemented but unexecuted** market-calibrated study uses actual adjusted SPY daily prices (2015–2025) only to infer the **marginal shape of historical log-return shocks**, not a true stock-price trend. It compares matched Gaussian, empirical return bootstrap, and circular block lengths 5/20 on **new synthetic trend-plus-shock series with known conditional mean τ**, R1/3, d=2, N50/200, two standardized noise scales, five seeds: 160 pools, 320 method rows. A second optional **literal mean baseline** is `--trend-kind constant_mean --d 1`: the synthetic return process has fixed conditional mean equal to the historical mean log return, and true trend-innovation variance is zero (a boundary model). It is saved separately, never mixed with the stochastic-trend results. A local cached return snapshot is ignored by Git but hashed in the manifest. A histogram and return/squared-return dependence plot are generated when the user runs the pilot. CI uses only a synthetic fixture. No PR.

`python -m experiments.pooled_loocv_smoothness.run_empirical_market_noise --preset pilot --ticker SPY` is the manual experiment; `python -m pytest tests/test_empirical_market_noise.py -q` verifies the code offline.

## New independent study: allowing a nonzero mean of trend differences

The previous experiments set (E[D_d\tau]=0); [Guerrero (2007) already permits and estimates nonzero difference means](notes/NONZERO_DIFFERENCE_MEAN_PROTOCOL.md). We implemented and executed an **exploratory sensitivity study** for **fixed analyst d=2** with (D_2\tau=\mu\mathbf1+\varepsilon). It compares zero-mean constraints against Gaussian GLS estimation of mu and a fold-clean common-mu pooled LOOCV criterion, and includes oracle true-mu and true-variance comparators. Fitting mu adds effective degrees of freedom; we reestimate it in each training deletion using an exact derived PRESS expression.

Pilot: 20 cells, five seeds per N×noise group, nested R1/3, **200 treatment pools (20 independent underlying shock streams), 1,600 per-method rows**, eight selectors. The new DGP shares the same random shocks across μ shifts, preserving paired comparison. **The full pilot is uploaded**; see the [measured analysis](notes/NONZERO_DIFFERENCE_MEAN_PILOT_AUDIT_2026-10-19.md). Manual reproducibility command: `python -m experiments.pooled_loocv_smoothness.run_nonzero_difference_mean --preset pilot`. Run `tests/test_nonzero_difference_mean_reconstruction.py` and tiny smoke first if needed; CI never reruns the full pilot. Its two PNG figures have already been generated and committed. No PRs or merging. This is **retrospective observed-series reconstruction**, not the distinct nonzero-μ horizon-h forecast paper.

## Next registered multorder confirmation — NOT YET EXECUTED

The user requested documenting the exact process and actual measured `d=2` five-seed results, then expanding **without rewriting old results** to fitted/generating orders `d=1,2,3,4`, with **10,000 independent Monte Carlo seeds per (d,N,observation SD)**. This is 16 independent base cells, **160,000 underlying independent R3 shock draws**, five **paired** mu shifts and nested R1/R3, or **1.6 million treatment-pool evaluations / 12.8 million method rows**. These numbers now describe a **completed manual Gaussian run**, source SHA `070b363b7d8a8156f320c833539fa068b684fc7b`; original per-seed gzip files are local and the compact verified aggregates are committed. Details: [canonical methodology/results note](notes/HOW_THE_SIMULATION_WORKS_AND_MEASURED_RESULTS.md) and [frozen confirmatory protocol](notes/MULTIORDER_10000_SEED_CONFIRMATORY_PROTOCOL.md).

The new sharded `run_nonzero_mean_multorder.py` records deterministic seed intervals, original source SHA and compressed CSV SHA256, avoids overlarge in-memory results and exploits exact affine-shift equivariance. `launch_nonzero_mean_multorder.py` is **plan-only by default**; only `--execute` starts local jobs, with `--workers` and safe resume. `aggregate_nonzero_mean_multorder.py` rejects overlapping seed intervals, mixed source commits and false completeness; it keeps the **paired true-MSE differences per seed** and outputs compact per-(d,N,eta,mu,R) statistics for legitimate uncertainty assessment. Earlier d2 1,600-row pilot results remain untouched; no PR/merge/main. Measured [16-cell confirmatory audit](notes/MULTIORDER_10000_SEED_CONFIRMATORY_RESULTS_2026-10-19.md) distinguishes both R3 dominance pattern and R1 counterexamples. Non-Gaussian mu-shift extension is **separately prospective**, after Gaussian numerical validation.

## Next experiment J — non-Gaussian mean-shift Monte Carlo (implemented; NOT RUN)

The independently verified 160k Gaussian base-shock campaign motivates a **separate finite-variance distributional stress study**: 12 regimes including Gaussian control, t3 observation/innovations, centered Gamma ±, rare Gaussian jumps, GARCH-t5 and five skew-normal shapes. Keep analyst-fixed d=1,2,3,4, N=50/200, observation population SD=.5/2, common `mu/sigma_epsilon` shifts [-1,-.25,0,.25,1], nested R1/3 and the eight existing fitting procedures. `gaussian_difference` MLE is **quasi-ML** outside normality. Exact statistical and reproducibility rules: [locked experiment J protocol](notes/NONGAUSSIAN_NONZERO_MU_PROTOCOL_2026-10-19.md).

**Status:** 25-seed ×192-cell pilot = **4,800 new independent base R3 shock draws and 384,000 method rows**, **NOT YET RUN**. New 10k/cell confirmation (1.92M base draws / 153.6M rows) is **future**, not silently launched. Run `python -m experiments.pooled_loocv_smoothness.launch_nonzero_mu_nongaussian --phase pilot --workers 32` to preview; append `--execute` for an explicitly authorized manual run on the user's own PC. `aggregate_nonzero_mu_nongaussian` checks SHA256 and all 192 strata. Cauchy is **intentionally separated** because population variance and squared risk are undefined. Student t3 has finite variance but infinite fourth moment, so mean-loss normal error bars need caution. Original Gaussian and historical tail pilots are unchanged.

## Study K — Cortés-Toto criterion family × mean model × numerical solver

The user requested a wider method comparison anchored in **Cortés-Toto, Guerrero and Reyes (2017)**, rather than only GLS-Gaussian (quasi-)MLE and joint fold-clean pooled LOOCV. Their actual four simulated selectors were **ordinary CV, GCV, AICc and BIC**, with (d=2,mu=0); their article also describes Guerrero's controlled smoothness and mentions AIC but excludes it from its final comparative experiment because of unreliable numerical behavior. Our [source-verified Study K protocol](notes/CORTES_TOTO_CRITERIA_AND_NUMERICAL_COMPARISON_PROTOCOL_2026-10-19.md) separates:
- **Statistical criteria:** CV/GCV/AICc/BIC; Gaussian difference-covariance ML/quasi-ML; and **predeclared** controlled-smoothness targets (not optimized criteria).
- **Mean treatment:** zero forced, known true μ (infeasible oracle), or common μ fitted jointly *inside PLS* and refitted on leave-one-observation-out folds. A pooled observed-difference plug-in plus our conditional ML remains a distinct old baseline, never naïvely frozen within supposed CV.
- **Numerical methods:** bounded versus multiple-bracket Brent and exact applicable endpoints with diagnostic scores/calls. These are solver choices for identical objectives, **not extra statistical criteria**; no global guarantee.

The new `cortes_optimality_criteria.py` implements the published criterion expressions, stable spectral endpoints, and our **new generalization** to R-series pooled joint-μ EDF (R\operatorname{tr}H_\lambda+\lambda\|b\|^2/k). Exact pooled CV remains the established tested class. **WARNING:** straightforward log(RSS) BIC diverges to −∞ as λ↓0 under interpolation; BIC is deliberately limited to explicitly reported finite positive λ bounds and cannot claim an unrestricted optimum. AICc is excluded where degrees-of-freedom denominator is nonpositive. `run_cortes_criteria_case.py` exactly replays **one** prior Study J non-Gaussian Gaussian/shock seed, reporting 18 selector choices plus original eight baselines (simulation latent MSE only for post-hoc evaluation). `tests/test_cortes_optimality_criteria.py` mathematically checks exact GCV/AICc/BIC EDF via the full RN×RN linear smoother. **No large K experiment executed;** reproduce one diagnostic first, then freeze a paired replay plan.

## Study K.1 implemented: 26 methods under exactly the SAME J pilot shocks

A *single* user-executed shock for d2/N50/etaSD.5/R3, Gaussian, `mu/epsSD=+1` returned `cv_zero_multibracket` as the **lowest realized synthetic latent-MSE new feasible policy ON THAT ONE DRAW ONLY**; this is not a statistically valid winner or evidence that incorrectly zero mean improves expected reconstruction. Next independent step is a **paired replay**, NOT fresh independent seeds.

The new `run_cortes_criteria_pilot.py`, `launch_cortes_criteria_pilot.py`, `aggregate_cortes_criteria_pilot.py` and `tests/test_cortes_criteria_paired_pilot.py` implement an optional manual **192 strata × exactly the same 25 J pilot shock draws per stratum**: 4,800 **previously used** independent base shocks, 48,000 nested R/paired-mu treatments, **26 methods = 18 new selector policies + eight old J estimators**, **1,248,000 compressed method rows**. Reuse the exact J original generator/seed convention, affine shift-equivariant selectors evaluated once per underlying draw/R, all 26 methods compared on identical y and known stochastic latent truth after selection. Fixed true mu modes explicitly labelled infeasible oracles; controlled smoothness presets not selected using latent truth. Numerical **multibracket** search held constant for new criteria; do not mistake it for global certification. The aggregator validates saved raw gzip SHA256, 25-seed cell completeness, mixed-code/solver rejection, and **exact same original eight-method average MSE** as the previous committed J pilot, guarding against accidental generator drift. Raw source shards ignored by git, compact aggregates remain trackable.

**NOT YET RUN:** Run `python -m experiments.pooled_loocv_smoothness.launch_cortes_criteria_pilot --workers 32` for plan only; explicit `--execute` starts it. Do small preflights under separate roots first, as documented in [exact paired replay protocol](notes/CORTES_TOTO_PAIRED_25_SEED_REPLAY_PROTOCOL_2026-10-19.md). Do not claim 4,800 new independent shock draws, confidence with only 25 seeds/cell, valid normal CIs for Student t3, unrestricted BIC optimality, or outcome superiority by `cv_zero_multibracket` from one seed.

## Latest K.1 exploratory results (completed and uploaded)

The 26-method 192-cell **same-original-J-25-seed** criterion replay has now **been executed** and compact results pushed (`results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001/`), source SHA `1785889d7d64a77f548d8746d41a9ea786e3e588`; original 8 method mean-MSE parity **exact at all 15,360 mean cells (maximum 0.0)**. 4,800 ORIGINAL seeded R3 shock draws, paired μ changes, nested R1/3 → 1,248,000 method records, 49,920 method aggregates and 80,640 paired. This is **EXPLORATORY ONLY**, not a new 4,800-seed independent cohort, nor 10k confirmatory evidence. Full source-aware [observed report and scenario tables](notes/CORTES_TOTO_PAIRED_25_SEED_REPLAY_RESULTS_2026-10-19.md).

At R3 and μ/epsSD=1: Gaussian GLS ML beats new joint fitted-mean CV/GCV/AICc on mean true trend MSE in 179/180/178 of 192 separate 25-seed strata respectively. At R1, joint AICc and pooled Guerrero-style plug-in are competitive or descriptively superior on equal-cell means. `bic_joint` ALWAYS selects the artificial positive-domain lower penalty limit (4,800 original shocks at each R); this naive BIC is not a meaningful unrestricted selector. Exact fold-clean old/new joint CV uses same mathematical criterion but DIFFERENT numerical optimizers; MSE differences motivate a controlled matched-score solver study before claiming criterion benefits. Do not infer significance from 25-seed cells or usual normal MSE CIs under t3.

## Separation contract

This paper owns this folder and experiments/pooled_loocv_smoothness/ with corresponding isolated tests. Do not modify existing forecasting manuscripts, old frozen checkpoints, their simulations, or the shared PLS interfaces merely to launch this study. Shared references and standard formulas may be cited but **cannot substitute for a self-contained paper**. No licensed PDF duplication is required.
