# Study K.1 completed: 26 penalized-trend selection policies, source-matched 25-seed replay

**2026-10-19 — EXECUTED / EXPLORATORY ONLY.** The entire 192-stratum study is complete and uploaded, with exact replication of the original eight methods. All scientific claims here are about **reconstructing simulated realized stochastic latent trends**, NOT forecast accuracy, empirical price-trend truth, or a statistically validated ranking with 10,000 new independent draws. No confirmation has been run for this 26-method extension.

## 1. Exact original observations, not reconstructed hypothetical results

The user ran `aggregate_cortes_criteria_pilot --require-complete --verify-digests` and pushed the three compact outputs:

- [Completed campaign manifest](../../../results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001/campaign_manifest.json), `status=COMPLETE_25_SEED_PAIRED_REPLAY_EXPLORATORY`, actual execution source SHA **`1785889d7d64a77f548d8746d41a9ea786e3e588`**, search solver `multibracket` with **41** initial grid points, 192 unique original source shard references and gzip SHA256 digests.
- [Full **1,920-scenario × 26-method wide CSV**](../../../results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001/wide_all_26_methods_by_1920_scenarios.csv), deterministically pivoted from the committed aggregate means: every `law × d × N × ηSD × R × μ` row is separately retained with **25 original reused seeds**, every method including oracles, and the post-hoc best feasible method label (not a valid selection rule when latent τ is unknown).
- [49,920 per-method aggregate cells](../../../results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001/by_regime_d_N_eta_R_mu_26_methods.csv), with mean realized latent-trend MSE, MAE, sample SD and sample SE, infinite-λ counts, BIC lower-search-domain counts.
- [80,640 matched-seed paired MSE contrasts](../../../results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001/paired_criterion_vs_original_MLE_LOOCV_plugin.csv), each using original same 25 seeds within its stratum, including differences against Gaussian GLS-(quasi-)MLE, exact original fold-clean pooled CV and Guerrero-inspired pooled observed-mean + our covariance MLE hybrid.
- [Original Study J non-Gaussian pilot](../../../results/pooled_loocv_smoothness/guerrero/nonzero_mu_nongaussian/audit_pilot_001/campaign_manifest.json), run source SHA `33c8eef425e56c6e17b9a5f3d331869e2af99c30`, supplies the same underlying shocks.

**Crucial acceptance result:** the user-side checker compared the same **15,360 method×scenario mean MSEs** for the eight original methods against the earlier uploaded Study J file and found **maximum absolute difference exactly `0.0`**. Consequently the new criterion comparisons truly share the pre-existing Monte Carlo sample, not another random draw. The 192 original gzip shards were SHA256-verified by the user-side aggregator, but the individual raw files remain local and are NOT on GitHub. Our independent `audit_cortes_criteria_confirmed_pilot.py` cross-checks compact manifest, factor/method coverage, paired arithmetic and t3 moment flags. **This independent compact-data audit does not re-hash the inaccessible raw gzip shards.**

Sample definition: **12 noise regimes × four fixed d=1–4 × N=50/200 × η population SD=.5/2** = 192 base strata. In each, **25 old independently seeded three-series noise/innovation shock draws are REPLAYED**, not 25 new independent replications. Five different \(\mu/\sigma_\varepsilon\in\{-1,-.25,0,.25,1\}\) mean treatments use *the identical stochastic realizations*, and R=1 is nested in R=3. This yields **4,800 reused base draws**, 48,000 paired mean/pool treatments and **1,248,000 per-method records** (26 methods). Each reported \((\mathrm{law},d,N,\sigma_\eta,R,\mu)\) mean MSE has exactly **25 independent shock realizations**, not 4,800. Stratify comparisons; don't count the 26 choices, five μ shifts, or nested R as additional independent data.

## 2. All 26 methods retained

The **18 new policies** are \(\{\mathrm{CV,GCV,AICc,restricted\ BIC,controlled\ }S=0.5,0.8\}\times\{\mu=0,\text{joint estimated }\mu,\text{externally known true }\mu\}\). The latter known-true-mean policies are **infeasible oracles** and must not compete in feasible rankings. Controlled S is an **exogenous preset level**, not a data-optimal smoothing selector. The **eight old methods**, especially Gaussian GLS (quasi-)MLE with estimated mean, the earlier exact fold-clean pooled LOOCV, and pooled Guerrero-style observed-mean plug-in + **our** conditional covariance MLE, are included byte-for-byte in the saved means (same true-trend MSEs). The simulated true \(\tau\) is used only for ex post reconstruction evaluation, not to pick \(\lambda\) in a feasible selector.

Every new data-driven criterion is optimized with the same multibracket candidate search; the older eight algorithms retain their earlier internal numerical search, so a comparison of a new method to the old eight can combine *criterion* with *solver*. See [full source-prior experimental protocol](CORTES_TOTO_PAIRED_25_SEED_REPLAY_PROTOCOL_2026-10-19.md) and [mathematical criterion/EDF specification](CORTES_TOTO_CRITERIA_AND_NUMERICAL_COMPARISON_PROTOCOL_2026-10-19.md). The pooled EDF in GCV/AICc/BIC correctly accounts for one jointly estimated common μ across R series. The original 2017 Cortés-Toto study's primary criteria were CV/GCV/AICc/BIC under d2,μ0; our grouped estimated-μ d1–4 stochastic simulation is a separate extension, not a reproduction of its factorial DGP.

## 3. Main exploratory result by pool size (substantial mean shift)

For **\(\mu/\sigma_\varepsilon=+1\)**, equal-cell descriptive mean of the 192 separate law × d × N × ηSD mean MSEs:

| Feasible selector, fitted/common μ unless specified | R=3 mean realized trend MSE | R=1 mean realized trend MSE |
|---|---:|---:|
| Gaussian GLS (quasi-)MLE of μ and variances | **0.373341** | 0.429410 |
| Pooled Guerrero-style observed-mean plug-in + our variance MLE | 0.375077 | 0.392452 |
| GCV, joint μ | 0.379396 | 0.419622 |
| CV, joint μ, NEW multibracket search | 0.381325 | 0.415654 |
| AICc, joint μ | 0.381327 | **0.389669** |
| Earlier exact fold-clean pooled CV, its ORIGINAL numerical search | 0.382295 | 0.424964 |
| Controlled nominal S=0.8, joint μ, preset policy | 0.422192 | 0.423388 |
| CV with μ incorrectly forced zero | 0.415386 | 0.451006 |
| AICc with μ incorrectly forced zero | 0.412498 | 0.418619 |
| BIC, joint μ, **finite positive-domain** search | 2.122526 | 2.111128 |

This is a **descriptive equal weighting of heterogeneous simulation cells**, NOT a risk valid across distinct d and law families; do not use these numbers to pick the optimal d or claim 192 independent replications of one DGP. Differences may be small relative to 25-seed Monte Carlo noise in many individual cells. Student-t3 in innovations or observations has **infinite fourth moment**, invalidating naive normal-Monte-Carlo confidence-interval arguments for quadratic losses.

**R3 nuanced outcome:**
- Under true \(\mu/\sigma_\varepsilon=1\), the 192 **cell-average comparisons** favor Gaussian GLS quasi-MLE over the new joint CV in **179/192** cells; GLS versus new GCV in **180/192**; GLS versus AICc in **178/192**. These are 192 different DGP cells and each has only 25 seeds: **NOT inferential counts of 192 independently confirmed victories**.
- Among the **feasible** 23 methods (excluding all three original true-mean/true-covariance oracles and six new true-mean fixed-policy oracles), the lowest observed cell-average MSE occurs for **pooled plug-in** in **84/192**, GLS MLE in **82/192**, joint AICc in **13/192**, preset controlled S=.8 in **10/192**, joint CV in **2/192**, and joint GCV in **1/192**. The method that wins by observing synthetic true τ *after the fact* is **not a legitimate data-driven real-market selector**.
- The plug-in hybrid is materially competitive: it has slightly lower mean risk in some law/parameter subgroups, even though GLS has the lowest broad descriptive R3 average.

**R1 reversals:**
- R1 total averages of joint AICc **0.389669** and feasible plug-in **0.392452** are below GLS **0.429410**. AICc often strongly changes the selected penalty at small N and high η noise; that is a descriptive numerical pattern, not proof of AICc population superiority at each cell.
- Among the same 23 feasible procedures, the pilot's minimum within individual R1 cells belongs to plug-in **83/192**, GLS **40/192**, preset S=.8 **38/192**, AICc **28/192**, joint GCV **2/192**, and the earlier CV **1/192**.
- The R1 mean is especially influenced by \(N=50,\sigma_\eta=2\) scenarios; see the individual cell CSV from `audit_cortes_criteria_confirmed_pilot.py` before interpreting a broad ranking.
- Some single-series noise/t3 scenarios are extremely variable, making a 25-seed mean unreliable.

## 4. Main criterion patterns separated by distribution

For \(R=3,\ \mu/\sigma_\varepsilon=+1\), all numbers are **descriptive equal averages across four d × two N × two ηSD cells** per law (each cell itself has exactly 25 reused shock draws).

| Law | GLS ML | Plug-in | New CV | GCV | AICc | BIC restricted |
|---|---:|---:|---:|---:|---:|---:|
| Gaussian iid | **0.37332** | 0.37582 | 0.38068 | 0.38031 | 0.38131 | 2.1212 |
| Student-t3 observation | **0.35825** | 0.36079 | 0.36725 | 0.36560 | 0.36624 | 2.0302 |
| Student-t3 innovation | **0.37518** | 0.37843 | 0.38275 | 0.37978 | 0.38305 | 2.1391 |
| Gamma centered right | **0.36742** | 0.36919 | 0.37904 | 0.37414 | 0.37731 | 2.1196 |
| Gamma centered left | **0.37682** | 0.37788 | 0.38388 | 0.38179 | 0.38435 | 2.1385 |
| Gaussian jump mixture | **0.37573** | 0.37823 | 0.38905 | 0.39022 | 0.38303 | 2.1792 |
| GARCH-t5 observation | 0.36251 | **0.36038** | 0.37199 | 0.36717 | 0.37284 | 2.0949 |
| Skew-normal -6 | **0.38677** | 0.39021 | 0.39154 | 0.39045 | 0.39494 | 2.1442 |
| Skew-normal -3 | 0.38292 | **0.38241** | 0.38859 | 0.38741 | 0.39391 | 2.1336 |
| Skew-normal 0 | **0.37665** | 0.38098 | 0.38413 | 0.38329 | 0.38421 | 2.1257 |
| Skew-normal +3 | **0.37523** | 0.37681 | 0.38348 | 0.38015 | 0.38125 | 2.1279 |
| Skew-normal +6 | **0.36932** | 0.36979 | 0.37352 | 0.37245 | 0.37349 | 2.1162 |

For \(R=1\), the comparable exploratory means are:

| Law | GLS ML | Plug-in | New CV | GCV | AICc |
|---|---:|---:|---:|---:|---:|
| Gaussian iid | 0.45259 | **0.38516** | 0.43961 | 0.44444 | 0.38959 |
| Student-t3 observation | 0.40346 | **0.34874** | 0.37014 | 0.36604 | 0.35744 |
| Student-t3 innovation | 0.40905 | 0.40778 | 0.42051 | 0.43001 | **0.39004** |
| Gamma centered right | 0.40661 | **0.38642** | 0.39742 | 0.39217 | 0.38742 |
| Gamma centered left | 0.48277 | 0.39573 | 0.40629 | 0.42099 | **0.39261** |
| Gaussian jump mixture | 0.42794 | 0.37894 | 0.38796 | 0.39397 | **0.37616** |
| GARCH-t5 observation | 0.43623 | 0.40149 | 0.42192 | 0.42765 | **0.39239** |
| Skew-normal -6 | 0.42360 | 0.40467 | 0.41994 | 0.44171 | **0.40031** |
| Skew-normal -3 | 0.41571 | **0.40487** | 0.44214 | 0.43716 | 0.40530 |
| Skew-normal 0 | 0.42779 | **0.39911** | 0.43817 | 0.44256 | 0.40546 |
| Skew-normal +3 | 0.42597 | 0.39565 | 0.41454 | 0.41175 | **0.38804** |
| Skew-normal +6 | 0.44121 | 0.40087 | 0.42921 | 0.42703 | **0.39127** |

These tables show why **mean estimation must be explicitly modeled** and why a single averaged superiority claim about Gaussian likelihood is not justified. The "best" in each row is the smallest descriptive average among the selected columns, *not necessarily the lowest of all 23 feasible method policies*; in some individual cells controlled S or a zero-mean restriction can win by chance or conditional bias–variance behavior.

## 5. BIC and numerical optimization: two scientifically essential findings

### 5.1 The plug-in BIC failure is systematic under this implementation

The implemented \( \operatorname{BIC}(\lambda)=\log[\mathrm{RSS}(\lambda)/(RN)]+\mathrm{EDF}(\lambda)\log(RN)/(RN)\) is **not a legitimate unrestricted global smoothing optimum** for PLS interpolation: \(\mathrm{RSS}(\lambda)\to0\) as \(\lambda\downarrow0\), hence its logarithmic residual term tends to \(-\infty\). A finite constrained domain \(\log\lambda\in[-20,35]\) only truncates that pathology.

**Measured:** in all **4,800/4,800** original R3 shock draw treatments at \(\mu/\sigma_\varepsilon=+1\), and likewise all **4,800/4,800** original R1 draws, `bic_joint` picked the **positive-domain lower bound**. The mean trend MSE rose to ≈2.12, versus ≈0.37–0.38 for the more meaningful fitting methods. The same pattern is visible for forced-zero BIC. **Do not claim "BIC is fundamentally inferior"**; claim that **this naive BIC formula is unbounded and fails in this PLS interpolation setting**. To compare information criteria properly, consider derivations with an explicit residual likelihood/covariance model or a differently constrained effective model class; do not invent a fix from an arbitrary cutoff.

### 5.2 Two implementations of exactly pooled leave-one-out CV can differ substantially

`cv_joint` and the old `existing__estimated_mu_fold_clean_pooled_loocv` use the same mathematical deletion-clean observed-CV objective with one common μ fitted from retained observations; they were tested to agree **at fixed λ**. They have DIFFERENT numerical search procedures (multibracket vs the old bounded-optimizer strategy).

**Measured on the identical 25 shocks:** for R3, the new multibracket's equal-cell descriptive mean trend MSE is **0.381325**, vs old CV **0.382295**; for R1 new multibracket **0.415654**, vs old CV **0.424964**. Their scenario mean true-trend-MSE differences are heterogeneous, sometimes substantial in R1, with some individual R1 cell mean absolute differences >0.1. **Do not automatically attribute a lower *latent trend MSE* to a better *CV optimizer***: the CV criterion is noisy-observation risk, whereas evaluation is latent reconstruction loss. To tell whether multibracket found better minima, recompute and compare the **ACTUAL identical observed-CV objective scores** at both selected λ values for each paired seed, under matched numerical budgets and recorded boundary conditions. Only that measures numerical optimization quality; latent MSE measures the effect of selecting a different λ on reconstructing the simulated τ.

This solver-control comparison is the **next methodological priority** before claiming that any of the new AICc/GCV versus old CV patterns purely reflect a different statistical criterion.

## 6. Recommended next protocol and safeguards

1. **Numerical isolation first:** run bounded vs multibracket vs dense-grid/derivative-stationarity root candidate search **on the SAME CV and GCV objective, same paired Study J seeds**. Save every selected λ, criterion objective, number of criterion evaluations, search bounds, boundary hits and true latent reconstruction loss. A "solver winner" must be decided by minimizing its *own* fixed score under comparable budgets, NOT by observing latent truth at selection time.
2. **Investigate the BIC functional form**, rather than launching millions of seeds in an unbounded/ill-posed comparison. Keep the recorded BIC arm as a diagnostic example of an interpolation-boundary problem, not a serious potential winner.
3. Study **N=50/ηSD=2/R1** separately: it disproportionately influences cross-scenario averaged MSE and the mean-parameter estimation uncertainty.
4. Add Student-t3 robust inference summaries (median/win fractions/tail quantiles) before any ordinary normal-approximation confidence interval claims. With 25 seeds per stratum, no full method-ranking certainty is warranted.
5. Only **after** numerical controls and a locked study plan should a 10,000 NEW seeds-per-cell confirmatory campaign be contemplated. The present reuse of prior pilot seeds is not a new independent cohort.
6. Preserve all raw compressed original Study K.1 shards off Git with independent backups; only compact validated result tables and source SHA belong in the shared repository.

### Reproducible compact-only independent audit

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_cortes_criteria_confirmed_aggregate.py -q
python -m experiments.pooled_loocv_smoothness.audit_cortes_criteria_confirmed_pilot
# Optional: export scenario-wide all-26-method columns for R1 and R3 at mu=+1
python -m experiments.pooled_loocv_smoothness.audit_cortes_criteria_confirmed_pilot --out-dir results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_review_001
```

This audit reads ONLY the already committed compact GitHub results, **not** the 1.248M raw records. It checks all 192 source seed intervals, all 26-method/42-contrast cells and arithmetic agreement between paired differences and method-level MSE. No stock-market trading/forecast claim is supported by these simulation outputs.
