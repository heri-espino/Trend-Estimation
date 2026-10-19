> **POST-EXECUTION 2026-10-19:** The source-matched **full 192-stratum, 25-reused-seed pilot IS NOW COMPLETE**, with 1,248,000 original per-method rows represented. User-side digest aggregator verified all 192 gzip shard hashes and exact mean-MSE parity across **15,360** previous method cells (**maximum deviation 0.0**). Actual source SHA `1785889d7d64a77f548d8746d41a9ea786e3e588`, 26 methods, 49,920 saved method aggregates, 80,640 paired contrasts; compact source files under `results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001/`. Read [CORTES_TOTO_PAIRED_25_SEED_REPLAY_RESULTS_2026-10-19.md](CORTES_TOTO_PAIRED_25_SEED_REPLAY_RESULTS_2026-10-19.md). The original prospective protocol below is preserved as an auditable historical pre-run specification; future-tense wording no longer describes completion status. The original J shocks are **reused, NOT NEW**. Do not infer 10k-seed confirmation or valid normal CIs for Student-t3.

# Study K.1 — Source-matched 25-seed paired criterion pilot (26 selectors)

**Protocol locked 2026-10-19. STATUS: CODE IMPLEMENTED, INITIAL ONE-SHOCK TEST PASSED, 192-STRATUM PAIRED REPLAY NOT EXECUTED.** This is an *exploratory replay of the exact 25 seeds already used in Study J* (non-Gaussian × nonzero difference mean). It is **not** a new independent 4,800-sample confirmation and must never be described as one. Study J's original code-source SHA was `33c8eef425e56c6e17b9a5f3d331869e2af99c30`; use its untouched aggregate for parity comparisons.

## Research question

How do the penalty-selection criteria **CV, GCV, AICc and domain-constrained BIC** studied by **Cortés-Toto, Guerrero and Reyes (2017)** compare against Gaussian contrast MLE/quasi-MLE and the new exact fold-clean pooled LOOCV when one varies (i) whether the \(d\)-th difference mean is zero, jointly estimated or supplied as an infeasible oracle, and (ii) the numerical solver on an identical criterion?

**Strong separation**: We compare criterion choice and mean handling first, keeping numerical optimizer **fixed to multibracket** for every new statistical criterion. The historical eight previous estimators keep their already specified internal searches; their differences therefore combine statistical and numerical procedure but make a useful faithfully reproduced practical baseline. A controlled solver-only arm with matched \(\log\lambda\) bounds, function budgets and exact endpoints must be a **separate experiment** before claiming which optimizer is best.

## Factorial protocol and actual independent units

We fix the original 12 finite-variance noise regimes (including Gaussian control and Student-t3/GARCH/skew/Gamma/jumps), \(d\in\{1,2,3,4\}\), \(N\in\{50,200\}\), \(\sigma_\eta\in\{0.5,2\}\), \(\sigma_\varepsilon=0.3\). This is **192 base strata**.

For each stratum we re-run `NoiseShard(...,phase="pilot")` with exactly the **same 25 base seed indices 0–24** as Study J. The originally simulated \(R=3\) shock pool is reused with five paired \(\mu/\sigma_\varepsilon\in\{-1,-0.25,0,0.25,1\}\) polynomial shifts and nested \(R\in\{1,3\}\). Thus **4,800 already existing, independently seeded R3 shock pools are replayed**, producing **48,000 paired/nested treatment-pool evaluations**; each has **26 reconstruction procedures**, totalling **1,248,000 per-method replay records**. They are *not* 1.248M independent observations, nor 4,800 new independent random streams.

Every row is scored by **MSE/MAE to the actual realized integrated stochastic latent trend**, unknown in financial data but available here for honest *post-selection simulation evaluation*. No feasible method chooses \(\lambda\), criterion, solver or \(\mu\) using that true trend.

## The 26 methods

**New criteria: 18** = \{CV, GCV, AICc, constrained BIC, controlled-S=0.5, controlled-S=0.8\} × three mean modes:
- `zero`: fix \(\mu=0\), may be wrong when true mean nonzero.
- `joint`: fit one shared \(\mu\) jointly with penalized \(R\) trends at each \(\lambda\). **Fold-clean** ordinary CV and **proper pooled total EDF \(R\operatorname{tr}H_\lambda+\lambda\|b_\lambda\|^2/k_\lambda\)** in GCV/AICc/BIC.
- `fixed`: use externally supplied true \(\mu\). **ORACLE only**, never a feasible estimator; retained to isolate the uncertainty cost of estimating the mean.

**Existing methods: eight** unmodified, `existing__...` labels. These include the known-true-parameters oracle, imposed-zero-mu Gaussian covariance ML/CV, known true mu and estimated variances/CV oracles, pooled Guerrero-style mean plug-in + OUR Gaussian covariance MLE hybrid, estimated common-mu GLS Gaussian ML and jointly estimated exact-fold-clean pooled LOOCV.

Controlled smoothness \(S\in\{0.5,0.8\}\) is chosen **before** observing true latent reconstruction errors, not optimized on the held-out simulation truth or fitted CV. AIC (uncorrected) was source-discussed but **excluded** from the cited paper's final comparison. Basic BIC based on \(\log(\mathrm{RSS})\) is **unbounded below** for this PLS interpolating smoother as \(\lambda\downarrow0\); the implemented \(\mathrm{BIC}\) is deliberately **numerically constrained to \(\log\lambda\in[-20,35]\)** and its lower-bound cases must be reported as such, not claimed globally optimal. AICc is invalid when \(RN-\mathrm{EDF}\le2\). All selector objective functions report exact endpoints when meaningful, without global optimality guarantees.

The original six μ shift-equivariant fitted-mean and known-mean new policies are **computed once for μ=0 per R and seed, then reused** across five μ interventions; the `zero` policies must be recomputed at every nonzero mean. This algebraic speedup is already validated for PLS but should be smoke-tested at high-order \(d=4\). It **does not create more statistically independent data**.

## Primary contrasts and method rankings

1. For each **fixed regime × d × N × observation SD × R × μ**, compare the six new **non-oracle joint-μ** criteria against the *same* original GLS-ML estimated μ, original fold-clean LOOCV estimated μ, and Guerrero pooled plug-in; use paired per-seed **MSE differences**.
2. Compare each joint-\(\mu\) criterion with its fixed-\(\mu=0\) counterpart to quantify mean misspecification under true nonzero μ. When true μ=0, examine the price of estimating one unnecessary mean parameter.
3. Within a fixed μ treatment compare CV versus GCV, AICc and constrained-BIC using the **same** fitted mean mode. Report per-seed win fractions, latent MSE/MAE, nominal smoothness, selected λ, EDF, criterion evaluations and boundary hits separately.
4. The fixed-true-μ group comprises oracles only; analyze them separately and never count them as feasible selections.
5. Compare `cv_joint` against `existing__estimated_mu_fold_clean_pooled_loocv` to check numerically that the common joint-μ CV criterion has the same mathematical target; any deviation is due to optimizer details.
6. For Student-t3 in observation errors or stochastic trend innovations, the squared loss can have **infinite fourth-moment sampling dispersion**, so usual normal 95% Monte Carlo mean-MSE confidence intervals may not be valid. **Do not** report ordinary normal CIs as proof. Include tail and win-frequency diagnostics. With only 25 independent shocks per base stratum, all conclusions are exploratory.

For the complete pilot there are **49,920 compact per-method aggregates** and **80,640 prespecified paired contrasts**, disaggregated by regime/d/N/noise/R/μ. The raw gzip replay files are preserved outside standard Git; only the compact checked aggregate CSVs, provenance and notes should be committed.

## Manual reproducibility on Windows/PowerShell

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only

python -m pytest tests/test_cortes_optimality_criteria.py tests/test_cortes_criteria_paired_pilot.py -q

# No simulation; show complete plan: 192 × 25 original shocks = 4800 replays, 1,248,000 rows.
python -m experiments.pooled_loocv_smoothness.launch_cortes_criteria_pilot --workers 32

# 1-seed numerical preflight, separate output root to avoid overlap with [0,25).
python -m experiments.pooled_loocv_smoothness.launch_cortes_criteria_pilot --regime gaussian_iid --d 2 --n 50 --sigma-eta 0.5 --stop 1 --workers 1 --solver multibracket --root results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/preflight_gaussian_d2 --execute

# High-order/large-signal numerical preflight (Student t3 obs, N200, d4):
python -m experiments.pooled_loocv_smoothness.launch_cortes_criteria_pilot --regime student_t3_observation --d 4 --n 200 --sigma-eta 2 --stop 1 --workers 1 --solver multibracket --root results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/preflight_t3_d4 --execute

# User-initiated full replay ONLY after the two preflights pass:
$env:OPENBLAS_NUM_THREADS = "1"
$env:MKL_NUM_THREADS = "1"
$env:OMP_NUM_THREADS = "1"
$env:NUMEXPR_NUM_THREADS = "1"
python -m experiments.pooled_loocv_smoothness.launch_cortes_criteria_pilot --workers 32 --solver multibracket --execute

# Summarize independently from saved raw shards; all 192 strata and 25 seeds required:
python -m experiments.pooled_loocv_smoothness.aggregate_cortes_criteria_pilot --require-complete --verify-digests --out-dir results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001
```

The aggregator checks every gzip SHA256, disjoint seed intervals, a **single code source SHA and identical numerical solver/scan budget**, all 26 methods and prespecified paired contrasts and **direct parity of the original eight methods against the previously committed Study J mean-MSE table**. If a later source change occurs mid-run, **do not merge shards across incompatible SHA**. Existing complete shard outputs can be resumed, never overwritten. Preflights MUST use isolated output roots.

Only **after** the `--require-complete` audit succeeds, stage the three files in `audit_pilot_001/` by exact path; do not `git add .` or upload 1.248M raw rows. Keep independent backups of compressed shards outside temporary university machines before any cleanup.

**Status as of writing:** only a one-shock demonstration with `cv_zero_multibracket` the *best feasible new criterion in that ONE simulated realization* has been executed by the user. That does not establish a best selector or evidence for restricting a true nonzero mean. The large paired 25-seed replay is **NOT YET EXECUTED**, and there are no 10,000-seed Study K results.
