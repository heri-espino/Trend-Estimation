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
7. [Agent handoff](AI_HANDOFF.md).

## Runnable independent pilot

Run from the repository root with the project's existing NumPy/SciPy/matplotlib dependencies:

    python -m experiments.pooled_loocv_smoothness.run --preset smoke --out-dir results/pooled_loocv_smoothness/smoke
    python -m pytest tests/test_pooled_loocv_smoothness.py -q

Preview the larger predeclared plan without running it:

    python -m experiments.pooled_loocv_smoothness.run --preset pilot --dry-run

For small rational input, separately:

    python -m experiments.pooled_loocv_smoothness.sturm_exact

The smoke and first 16-cell **pilot were executed and pushed** on 2026-10-18. See the [pilot audit](notes/PILOT_AUDIT_2026-10-18.md) for descriptive results and limitations. The confirmatory campaign, financial application, theorem/counterexample verification, and manuscript refinement remain prospective.

## Separation contract

This paper owns this folder and experiments/pooled_loocv_smoothness/ with corresponding isolated tests. Do not modify existing forecasting manuscripts, old frozen checkpoints, their simulations, or the shared PLS interfaces merely to launch this study. Shared references and standard formulas may be cited but **cannot substitute for a self-contained paper**. No licensed PDF duplication is required.
