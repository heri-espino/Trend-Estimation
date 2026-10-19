# Working Paper — Numerical Optimization of Pooled LOOCV Smoothness

**Status:** independent working paper, initiated 2026-10-18; theory and experiments in preparation.  
**Prospective venue:** SMCCA (journal scope and submission requirements must be verified before submission).  
**Working title:** *Numerical Optimization of Penalized Trend Smoothness by Pooled Leave-One-Out Cross-Validation*.

## Central question

Can numerical stationary-point searches, including multibracket Brent root refinement and *restricted exact* Sturm isolation, reliably locate the global minimum of a pooled leave-one-out cross-validation (LOOCV) loss for classical penalized least-squares (PLS) trends?

The statistical basis is **Cortés-Toto, Guerrero and Reyes (2017)**, especially their PLS/CV experiment. We study **observed-series reconstruction only**. NO forecasting horizons, forecast-origin splits, out-of-sample forecast claims, dynamic tracking of branches, or joint mean-difference estimation.

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
13. [Agent handoff](AI_HANDOFF.md).

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

The [locked design](notes/ROBUSTNESS_PROTOCOL.md) calls for 20 scenarios × 5 seeds × nested R=1/3 = **200 pools**, 1000 method-level observations. The full pilot **has not yet been run/committed**. Run `python -m experiments.pooled_loocv_smoothness.run_robustness --preset smoke` for the tiny check and `--preset pilot` for the manually initiated experiment. Read the [results ledger](notes/RESULTS_LEDGER.md) before inferring that implementing a runner has produced empirical findings.

**Repository action policy:** commit directly to `paper/pooled-loocv-numerical-optimization`; no PR creation, no merging into main, and no automatic heavy Monte Carlo.

## Separation contract

This paper owns this folder and experiments/pooled_loocv_smoothness/ with corresponding isolated tests. Do not modify existing forecasting manuscripts, old frozen checkpoints, their simulations, or the shared PLS interfaces merely to launch this study. Shared references and standard formulas may be cited but **cannot substitute for a self-contained paper**. No licensed PDF duplication is required.
