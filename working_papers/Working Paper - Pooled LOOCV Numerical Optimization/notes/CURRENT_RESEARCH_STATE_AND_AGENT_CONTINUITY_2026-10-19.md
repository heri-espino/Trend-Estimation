# Current research state and agent continuity — 2026-10-19

> **Newer request (2026-10-19, Study M.2):** The user confirmed **local** success of Study M.1's nine-mechanism gallery (198 method rows, CSVs/PNG not yet available on GitHub), then asked for many seeds as the run was quick. This supersedes the dated *no extra seeds now* preference. [Study M.2 preregistration and manual commands](STUDY_M2_PROCESS_DIVERSITY_INDEPENDENT_SEEDS_2026-10-19.md); [resumable source](../../../experiments/pooled_loocv_smoothness/run_process_monte_carlo.py); [deterministic small tests](../../../tests/test_pooled_process_monte_carlo.py). Source+tests committed and dedicated CI passes, **no M.2 actual campaign results yet**. Design: 1000 new base seeds, original 9 common-shock perturbations, 11 feasible selectors, R1 nested in R3, 198,000 method records; report paired risks (all 990 pairwise comparisons, global Holm), common-first-series pooling deltas (99), backups of ignored raw shards. This is retrospective synthetic reconstruction, not h-step forecasts or method novelty evidence. Only user-local manually run heavy simulation. No PR/merge/main.



> **Latest request / Study M update (2026-10-19):** The user prefers *different process mechanisms and concrete illustrations* rather than more seeds or immediate numerical Study L. [Process gallery protocol](PROCESS_DIVERSITY_ILLUSTRATIVE_EXPERIMENT_2026-10-19.md); [runner](../../../experiments/pooled_loocv_smoothness/run_process_examples.py); and [tests](../../../tests/test_pooled_process_examples.py) are **IMPLEMENTED, NOT RUN**. Nine processes × nested R1/R3 × eleven feasible policies = 198 **illustrative** rows once manually executed; no new confirmatory Monte Carlo and no method-winner claim until saved results are audited. Include signal shape, outliers, temporal dependence and cross-series pooling assumptions. Study L remains a prospective, lower-priority numerical design.


**Branch:** `paper/pooled-loocv-numerical-optimization`. **Scope:** the *independent, retrospective observed-series reconstruction* paper, not the separate horizon-`h` forecast-CV paper. This is a navigation checkpoint derived from inspected branch files, saved manifests, source code, and the already-written result audits. Initial inspected branch head: `16184b51e7e223dcdb9fbedc804018002127e39c`; this checkpoint itself is subsequently committed and therefore changes the head. The per-experiment **source SHA in each manifest** takes precedence over the branch head for reproducibility.

## 0. Read this before running or editing anything

1. Repository [AGENTS.md](../../../AGENTS.md), [AI_HANDOFF.md](../../../AI_HANDOFF.md) and [working_papers/README.md](../../README.md). The older root handoff covers other papers and is not a current result ledger for this one.
2. [This paper's README](../README.md) and [AI_HANDOFF.md](../AI_HANDOFF.md). **Some older chronological sections say “not run”; these are historical at the time they were written**. A later dated executed-results note and the corresponding committed manifest override those statements.
3. [RESULTS_LEDGER.md](RESULTS_LEDGER.md), [RESEARCH_NOTEBOOK.md](RESEARCH_NOTEBOOK.md), [PROOF_LEDGER.md](PROOF_LEDGER.md), [SIMULATION_ATLAS.md](SIMULATION_ATLAS.md), [DECISIONS.md](DECISIONS.md), [LITERATURE_POSITIONING.md](LITERATURE_POSITIONING.md).
4. Read the source for the particular study before changing it: `experiments/pooled_loocv_smoothness/{objective,search,mean_difference_methods,cortes_optimality_criteria}.py`; then its runner, audit, and tests. Read the working-paper manuscript `manuscript/main.tex` *after* the notes; it is an older draft and not a complete rendering of the latest experiments.
5. For the latest experiments, read [Gaussian H confirmation](MULTIORDER_10000_SEED_CONFIRMATORY_RESULTS_2026-10-19.md), [non-Gaussian J protocol](NONGAUSSIAN_NONZERO_MU_PROTOCOL_2026-10-19.md), [Cortés-Toto K criteria mathematics](CORTES_TOTO_CRITERIA_AND_NUMERICAL_COMPARISON_PROTOCOL_2026-10-19.md), and especially [K.1 completed results](CORTES_TOTO_PAIRED_25_SEED_REPLAY_RESULTS_2026-10-19.md).
6. Read [proposed next numerical design](STUDY_L_SAME_OBJECTIVE_NUMERICAL_COMPARISON_DESIGN_2026-10-19.md) before coding or launching another comparison.

**Work policy:** the owner has asked for direct commits to the **existing branch only**, **no PRs, no merge, no force push**. Large Monte Carlo, figures and PDFs are manual-only; CI may perform lightweight tests/fixture smoke checks. Do not stage raw or licensed PDFs, giant gzip shards or personal financial data. Back up the original local gzip shards before deleting/reimaging a workstation.

## 1. Definitions and separation of three axes

Let `R` comparable observed series have `N` observations and a preselected order `1 <= d < N`. Let `D=D_d` denote forward differences, `Q=D^T D`, `lambda >= 0` the regularization parameter, and `H_lambda=(I+lambda Q)^(-1)` the zero/fixed-mean smoother. Let `p_t=binom(t,d)` for zero-based indices, so `Dp=1`.

The generating model in the stochastic mean-shift simulations is
$$
D_d\tau^{(r)} = \mu\mathbf 1 + \varepsilon^{(r)},\quad
y^{(r)} = \tau^{(r)} + \eta^{(r)}.
$$
The true *realized* `tau` (including accumulated innovations) exists in synthetic experiments, not in actual financial datasets. Choosing a penalty by noisy-observation CV is not equivalent to minimizing unobserved true-trend reconstruction risk. All comparisons must separate:

- **Statistical selection target:** ordinary pooled leave-one-observation-out CV, GCV, corrected AIC, restricted plug-in BIC, Gaussian contrast ML/quasi-ML, or externally preset smoothness. Controlled smoothness `S=0.5/0.8` is a predeclared policy, **not** optimized likelihood/CV.
- **Treatment of difference mean:** wrong forced `mu=0`, externally known `mu` *oracle*, pooled observed-difference plug-in plus **our** Gaussian variance ML, common GLS-profile fitted `mu`, or joint common `mu` fitted within the PLS objective and refitted within each LOOCV deletion. Never label a held-out-leaking frozen all-data plug-in as genuine LOOCV.
- **Numerical algorithm:** one bounded Brent-like search, score-grid multistart refinement, derivative-sign root scans, finite dense grids, restricted exact rational/Sturm isolation. A better *score minimizer* need not have better realized latent MSE.

For R series with jointly fitted one common `mu`, let `T_lambda=QH_lambda`, `b_lambda=T_lambda p`, and `k_lambda=p^T T_lambda p`. The exact total effective degrees of freedom, at finite positive lambda, are
$$
\operatorname{EDF}_{\mathrm{joint}}(\lambda)
=R\operatorname{tr}(H_\lambda)
+\lambda\|b_\lambda\|_2^2/k_\lambda .
$$
Its infinite-penalty limit is `Rd+1`, versus `Rd` with externally fixed `mu`. The *nominal* normalized smoothness `S=(N-tr H)/(N-d)` is a monotone coordinate for lambda, **not the full pooled joint-model EDF**. Guerrero (2007) already treats `mu != 0`; this is not a discovery of nonzero-difference trends.

## 2. Executed versus not executed: authoritative provenance

| Study | Current verified research status | Exact scale and evidence |
| --- | --- | --- |
| A–E earlier observed-series, variance-ratio, variance-estimation, robustness and tail stress | **Executed, committed exploratory pilots** | See [RESULTS_LEDGER](RESULTS_LEDGER.md), audits A–E, original individual manifests; original factorial A is not a perfect replication of the original authors' computational script. |
| F real-market return histogram / block-bootstrap calibration | **Implemented, not executed with real market data** | [EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md](EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md). A synthetic test fixture is not the SPY pilot; simulated tau would not be a market-observed true price trend. |
| G fixed d=2, nonzero difference-mean pilot | **Executed and committed** | 20 base shock draws across four N/noise groups; five shared-shock mu shifts, nested R1/R3, 1,600 method rows; [G audit](NONZERO_DIFFERENCE_MEAN_PILOT_AUDIT_2026-10-19.md). |
| H independent Gaussian d=1..4 confirmation | **Executed, aggregated and committed** | 16 strata x 10,000 **base independent** R3 draws = 160,000 base draws; 5 paired mu shifts and nested R1/R3 imply 1.6M treatment pools and 12.8M method results, **not independent 12.8M seeds**. Run SHA `070b363b7d8a8156f320c833539fa068b684fc7b`. [Manifest and compact data](../../../results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/audit_001/campaign_manifest.json), [H audit](MULTIORDER_10000_SEED_CONFIRMATORY_RESULTS_2026-10-19.md). |
| J finite-variance, non-Gaussian, nonzero mean **pilot** | **Executed and committed**; older protocol's “NOT RUN” is historical and superseded | 12 regimes x d1–4 x N50/200 x eta SD .5/2 = 192 strata, 25 independent new J shocks per stratum; original 4,800 shocks. [J manifest](../../../results/pooled_loocv_smoothness/guerrero/nonzero_mu_nongaussian/audit_pilot_001/campaign_manifest.json) status `COMPLETE_PILOT`, run SHA `33c8eef425e56c6e17b9a5f3d331869e2af99c30`. Its 10,000/new-seed confirmatory phase is **not executed**. |
| K one-shock demonstration | **Executed**, diagnostic only | `gaussian_iid,d2,N50,etaSD=.5,R3,mu/sigma_epsilon=1`; 18 new policies + 8 original; cannot rank methods from this shock. |
| K.1 Cortés-Toto 26-method comparison replay | **Executed, aggregated and committed** | Reuses J's **same** 25 shocks per 192 strata, not new confirmation. 4,800 reused base draws, 48,000 paired/nested treatments, 1,248,000 method records; 49,920 means, 80,640 paired contrasts. Run SHA `1785889d7d64a77f548d8746d41a9ea786e3e588`; manifest status `COMPLETE_25_SEED_PAIRED_REPLAY_EXPLORATORY`. Eight-method original parity: 15,360 aggregate cells, max absolute mean-MSE difference **0.0**. [K.1 manifest](../../../results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001/campaign_manifest.json), [K.1 results](CORTES_TOTO_PAIRED_25_SEED_REPLAY_RESULTS_2026-10-19.md). |
| K.1 independent **new** 10k-per-cell confirmation | **Not executed** | Never label matched J replay as independent confirmation. |
| L controlled numerical solver study | **Proposed only; not coded/run by this checkpoint** | [Study L design](STUDY_L_SAME_OBJECTIVE_NUMERICAL_COMPARISON_DESIGN_2026-10-19.md). |

**Data audit boundary:** the original huge compressed shards and independent-run gzip SHA256 checking happened on the user's machine, according to the committed manifests. GitHub currently stores checked **compact aggregate reports**, not raw 1.248M/12.8M individual records. A compact-only audit can check internal arithmetic and recorded provenance; it cannot recompute all per-seed statistics or independently re-hash absent gzip inputs.

## 3. What the actual results support (and do not support)

- **H under Gaussian R=3:** at substantial nonzero mu the cost of forcing zero mu is large; correctly fitted Gaussian GLS ML has lower mean simulated latent MSE than fitted-mu CV in **15/16** (d,N,noise) strata. For R1 there are meaningful counterexamples. Five deterministic mu shifts share each seed and do not constitute extra independent replication.
- **K.1 at mu/sigma_epsilon=+1:** for R3, descriptive equally weighted across 192 *heterogeneous* cells: GLS-MLE `0.373341`, plug-in `0.375077`, joint GCV `0.379396`, new joint CV `0.381325`, joint AICc `0.381327`, old joint CV `0.382295` mean latent MSE. For R1: joint AICc `0.389669` and plug-in `0.392452` versus GLS `0.429410`; a ranking flips with pool size/conditions. These 192 cell-averages are *not* 192 replications from one DGP or a legitimate choice of d. Results are exploratory (25 J seeds per cell), not an independent confirmatory K campaign.
- **Important bookkeeping correction identified in the K.1 result prose:** of 26 total policies, there are **nine simulation oracles** (six new fixed-true-mu policies and three original known-parameter/mean policies), so **17** feasible policies under the simulation information contract. The text calling the feasible subset “23 methods” while excluding all nine oracle policies is arithmetically inconsistent. Source `audit_cortes_criteria_confirmed_pilot.py` explicitly excludes all nine and therefore really ranks **17** feasible candidates; do not echo the mistaken 23 count. The aggregate outcomes are unaffected by the prose typo.
- **Naive residual BIC pathology:** `log(RSS)` tends to minus infinity as lambda decreases toward zero because the PLS smoother interpolates data; a finite lower log-lambda cutoff merely truncates an unbounded objective. In K.1 `bic_joint` hits this imposed lower bound on 4,800 of 4,800 base draws for each R at mu=+1. Do not infer all information criteria are inferior.
- **One statistical objective, two algorithms:** `cv_joint` in Study K.1 and the original `existing__estimated_mu_fold_clean_pooled_loocv` are the same *exact deletion-honest score* for fixed lambda but have different numerical searches. Their latent MSE differs (R3 `0.381325` vs `0.382295`; R1 `0.415654` vs `0.424964`). This says nothing decisive about *which reached the better CV objective value* until score/solver controls are run on identical individual observations.
- **Non-Gaussian limits:** Gaussian ML is quasi-ML in non-Gaussian regimes. Student-t(3) has finite variance but infinite fourth moment; ordinary normal intervals for averages of squared errors are not generally justified. Cauchy is excluded from J/K finite-variance MSE comparisons; its variance and expected squared risk are undefined. AR(1) observational dependence makes ordinary observation-deletion CV suspect as a proxy for predicting independent future noise.
- **No forecasting claim:** All A–K present study outcomes are retrospective observed-series reconstruction, not h-step forecast performance, out-of-sample trading results, or proof of publication novelty. The LaTeX manuscript is behind these completed analyses and should only be revised from verified evidence.

## 4. Tests and read-only reproduction (no new simulations)

From the repository root on the correct branch:

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only

python -m pytest tests/test_cortes_optimality_criteria.py tests/test_cortes_criteria_paired_pilot.py tests/test_cortes_criteria_confirmed_aggregate.py tests/test_multorder_confirmatory_aggregate.py -q
python -m experiments.pooled_loocv_smoothness.audit_cortes_criteria_confirmed_pilot
python -m experiments.pooled_loocv_smoothness.audit_multorder_confirmatory
```

These commands are suggested based on the inspected source and prior committed audits, **not newly executed by this documentation-only review**. Do not re-run `launch_cortes_criteria_pilot --execute` on existing audited outputs.

## 5. Required documentation workflow for every future agent

Before implementation: read this checkpoint and the target protocol; write down `question -> hypotheses -> estimand -> DGP -> randomization unit -> fixed methods/solvers -> primary loss -> failure modes -> predeclared outputs`. Mark explicitly **PROPOSED**, **IMPLEMENTED / NOT EXECUTED**, **EXECUTED / UNVERIFIED**, **AUDITED / EXPLORATORY**, or **INDEPENDENTLY CONFIRMED**.

After any code change: add tests for formulas, deletion honesty, endpoints, numeric limits, information leakage, and the relevant statistical unit; record a source commit SHA. Do not claim that a passing fixture is a Monte Carlo campaign.

After a manual run: retain manifests (seed formula, code SHA, software versions, solver bounds/budgets, distribution parameters, per-shard checksums) and compact paired aggregate tables. Preserve source gzip outside Git with an independent backup. Run an audit from saved data **without quietly resimulating**. Record negative results, infinities, failure counts and method reversals, not only victories. Write a dated `notes/*RESULTS*.md` linking exact artifacts and their independently verified status; then update [RESULTS_LEDGER.md](RESULTS_LEDGER.md), [DECISIONS.md](DECISIONS.md), this continuity note or its dated successor, and both paper-level and root handoffs if operational priorities change.

Do not turn the paper's working assumptions into claims about all time-series smoothers. An algebraic derivation is not priority/novelty evidence; finite grids and finite derivative scans are not unrestricted global certificates. Leave main untouched unless the user explicitly changes this branch-only workflow.
