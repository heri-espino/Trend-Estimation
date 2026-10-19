# Independent paper — agent handoff (2026-10-18)

## Read order

1. This README.md.
2. notes/RESEARCH_NOTEBOOK.md.
3. notes/PROOF_LEDGER.md.
4. notes/SIMULATION_ATLAS.md.
5. notes/LITERATURE_POSITIONING.md.
6. notes/DECISIONS.md.
7. experiments/pooled_loocv_smoothness/README.md and code.
8. Existing repository AGENTS.md and AI_HANDOFF.md for shared operational rules.

## Read this research checkpoint first

1. `notes/RESULTS_LEDGER.md` — executed versus planned datasets, precise simulation DGPs, commits, seeds, outputs.
2. `notes/ROBUSTNESS_PROTOCOL.md` — five regimes and preregistered robustness study; only small smoke in automated CI.
3. `notes/VARIANCE_ESTIMATION_PILOT_AUDIT_2026-10-18.md` — measured Gaussian-ML/LOOCV and unstable moment results.
4. `experiments/pooled_loocv_smoothness/run_robustness.py` and dedicated tests.
5. **Direct branch-only Git changes.** User prohibits PRs: do not open new PRs or merge anything. Keep all substantial simulation campaigns manual and independent from frozen work.

## Current next requested work (2026-10-18)

User requested derivation of Gaussian difference likelihood, separation of observed LOOCV error from latent truth MSE, and exploring Cauchy and financial-style non-Gaussian tails. **Completed:** documented exact implementation in `notes/GAUSSIAN_MLE_AND_LOOCV_EXPLAINED.md`; committed new independent `run_tail_noise.py` with 13 prespecified distribution settings, generating and fitting orders d=1,2,3, and generator tests. **NOW completed:** the full 1,560-pool exploratory pilot has been executed and pushed; see `notes/TAIL_NOISE_PILOT_AUDIT_2026-10-18.md`. Cauchy is a distinct infinite-variance stress case, with Gaussian ML often at lambda=infinity and observed LOOCV having lower median per-pool median absolute trend error for d=1,2,3. **NOT done:** any independent confirmatory run or market return calibration. Its manual steps, finite-moment vs infinite-moment evaluation semantics and seed grid are in `notes/TAIL_NOISE_PROTOCOL.md`. Update `notes/RESULTS_LEDGER.md` and file a source-linked Markdown results audit after user runs the new pilot and pushes CSV/JSON manifests. Under **no circumstances open a PR** or merge; all edits go directly to branch `paper/pooled-loocv-numerical-optimization`.

## Latest user clarification: fixed d and separate real-market calibration experiment

The analyst chooses difference order `d` **before** computing a common pooled LOOCV penalty; the pooled score is mean of the R individual LOOCV loss functions, NOT arithmetic mean of independently optimized smoothness values. Preserve this decision; the d=1/2/3 tail pilot was a *sensitivity factorial*, not an automatic d-selection system. The complete descriptive distribution rankings remain in `notes/TAIL_NOISE_PILOT_AUDIT_2026-10-18.md`.

An independent **SPY adjusted daily log-return calibrated** experiment was implemented in `experiments/pooled_loocv_smoothness/run_empirical_market_noise.py`, mathematical contract `notes/EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md`, tests `tests/test_empirical_market_noise.py`. Its full SPY pilot is **NOT YET RUN OR PUSHED**. It uses real return data for noise shapes but new synthetic (Y=\tau+\eta) with known conditional expectation trend; it is NOT a true stock-price trend estimation or financial backtest. Four modes: iid matched normal, iid empirical shocks, circular blocks 5/20. Two separate analyst-selected trend kinds: default `stochastic` with known generated conditional mean path, or optional `constant_mean` with tau_t equal to the empirical historical mean log return; latter has zero true difference-innovation variance and outputs into its own `constant_mean/` folder. Do not pool these two DGPs or call the fitted Gaussian variance ratio a regular finite Guerrero ratio in the constant-mean case. Only the synthetic-labelled offline smoke runs in CI; raw returns saved locally under gitignored `data/market_calibration/`. Once executed on user's computer and results committed, analyze paired R3 latent MSE against the same generated tau across modes; check calibration SHA256 and source before making claims.

## 2026-10-19 next experiment: μ≠0 difference mean, mathematical correction

The user agreed to study (Δ^d\tau=\mu+\varepsilon) with nonzero μ, inside the **independent retrospective pooled observation-LOOCV paper**. The source Guerrero paper and the repository's other [Mean-Difference Forecasting paper](../../Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting/README.md) already accommodate nonzero μ and a plug-in; **do not present either as a newly invented model**. Carefully distinguish the *other paper's* horizon-h forecast mean profiling from this paper's *observation* leave-one-out CV with fold-clean jointly estimated common μ.

Read the [locked new protocol](notes/NONZERO_DIFFERENCE_MEAN_PROTOCOL.md). Code: `experiments/pooled_loocv_smoothness/mean_difference_methods.py` and `run_nonzero_difference_mean.py`; tests `tests/test_nonzero_difference_mean_reconstruction.py`. CI's tiny smoke verifies a 42-row case plus PRESS-vs-actual-deletion invariance tests. The **full 200-pool, 1400-row pilot is NOT YET RUN**. New seed base 69000000, μ levels -1,-.25,0,.25,1 times sigma epsilon, fixed d=2, different N and noise; R1 nested in R3, μ treatments paired across same random shock series. The EDF changes when μ is estimated; old S is nominal penalty coordinate only. The full-data GLS μ estimated by ML must NOT be treated as held-out-estimated in ordinary frozen-mu PRESS. No PRs, no heavy Monte Carlo on push.

## Non-negotiable identity

**This is NOT the existing forecast-oriented Numerical Methods paper.** It deliberately changes the scientific object to classical *observed-series LOOCV for PLS trend reconstruction*. No future-block loss, no h, no rolling forecast validation, no branches or regime forecasting.

Primary output: full pooled loss curve; roots/local minima and endpoints; verified lowest candidate; computation, accuracy and failure analysis. Treat R=1 as an essential classical control.

## Implementation notes

- Pool LOOCV **scores at a common λ or normalized S first**, then minimize.
- Same N, d within each pool. Recompute H and the mapping when N changes between factorial cells.
- At λ=0 use the analytic LOOCV limit, not a small arbitrary positive λ.
- At λ=∞ use the exact projection onto ker(D_d).
- For finite λ>0, recover LOOCV via T=Q(I+λQ)^{-1}: held-out residual e_i=(Ty)_i/T_ii; analytic derivative uses T'=-T².
- Brent bracketing based on sign changes is numerical *evidence*, not a proof that every stationary point has been captured.
- Sturm sequences require exact rational inputs and a nonzero stationary polynomial; only small demonstrators are supported.
- Do not publish synthetic output figures as empirical market results.

## Stage and next work

Current stage: **three executed, committed exploratory pilots** and an additional **executed and committed five-regime misspecified-noise robustness pilot** with dedicated tests; 200 nested pools, 1,000 method rows. Its independent **confirmatory** experiment remains unrun. Authoritative run-by-run status and seeds: [notes/RESULTS_LEDGER.md](notes/RESULTS_LEDGER.md). The five-regime robustness protocol is [notes/ROBUSTNESS_PROTOCOL.md](notes/ROBUSTNESS_PROTOCOL.md). Investigate objective landscapes and ascertain if there is a *nontrivial numerical contribution* beyond published global CV methods; results may refute that thesis. Determine publication guidelines directly before final formatting.

Do not claim a theorem or experimental superiority before the required tests and evidence are recorded. Commit reproducible CSV/PNG/manifest for intentionally launched runs; note hardware, seed, git SHA, tolerances, and method configurations. Keep heavy results outside ordinary Git.
