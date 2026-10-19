# Frozen proposed Gaussian confirmation: orders 1–4, 10,000 independent seeds per cell

**Designed 2026-10-19. STATUS: IMPLEMENTED / NUMERICALLY TESTABLE; LARGE CAMPAIGN NOT EXECUTED.** Do not report a confirmation until all 16 cells reach 10,000 independent random-shock seeds each and the source SHA, shard manifests and completeness audit agree. This is for the **independent retrospective Pooled-LOOCV numerical optimization paper**, not the separate \(h\)-step forecast-CV paper.

## 1. What prompted this, and what is already known?

The executed fixed-d2 five-seed pilot gave evidence that forcing a wrong \(\mu=0\) when \(D_2\tau=\mu+\varepsilon\) can inflate latent trend reconstruction MSE, while correctly restricting \(\mu=0\) can slightly improve finite-sample recovery. A full explanation of the **actual trend generator, every estimation method, source versions, evaluation target and measured pilot values** is [HOW_THE_SIMULATION_WORKS_AND_MEASURED_RESULTS.md](HOW_THE_SIMULATION_WORKS_AND_MEASURED_RESULTS.md); detailed numerical results [NONZERO_DIFFERENCE_MEAN_PILOT_AUDIT_2026-10-19.md](NONZERO_DIFFERENCE_MEAN_PILOT_AUDIT_2026-10-19.md).

**Scientific hypothesis (not established):** under nonzero expected \(d\)-th differences, fitting the common difference mean \(\mu\) may matter more for realized retrospective reconstruction MSE than the choice between Gaussian covariance likelihood and pooled observed-data LOOCV. Conversely, when true \(\mu=0\), the added estimation degree may be unnecessary. This is a **relative loss comparison**, not a claim that Gaussian MLE is invalid outside normality or that a stock-price trend is observed.

Guerrero (2007) already covers nonzero difference mean and an observed sample-difference plug-in. The pooled plug-in hybrid, fitted Gaussian differenced-covariance GLS mean and exact fold-reestimated pooled CV are OUR research comparators; never attribute those algorithms to Guerrero.

## 2. Data-generating process for each fixed analyst order

For \(d\in\{1,2,3,4\}\), \(N\in\{50,200\}\), \(\sigma_\eta\in\{0.5,2\}\), \(R\in\{1,3\}\), and \(\sigma_\varepsilon=0.3\), generate independent standard normal trend innovations \(\varepsilon_t^{(r)}\) and observation errors \(\eta_t^{(r)}\). The analyst has **fixed d before fitting**; it is NOT tuned to minimize latent truth MSE. Each series in one pool has distinct shocks but shares the same \(N,d,\mu,\sigma_\varepsilon,\sigma_\eta\) and fitted common \(\lambda\).

\[
D_d\tau^{(r)}=\mu\mathbf1+\varepsilon^{(r)},\qquad
y^{(r)}=\tau^{(r)}+\eta^{(r)},\qquad
\varepsilon^{(r)}_t\overset{\mathrm{iid}}{\sim}N(0,0.3^2),\quad
\eta^{(r)}_t\overset{\mathrm{iid}}{\sim}N(0,\sigma_\eta^2).
\]

Initialize \(\tau_t=0.02t\), \(0\le t<d\); the true realized stochastic trajectory is

\[
\boxed{\tau_t=0.02t+\mu\binom td+
\sum_{j=0}^{t-d}\binom{t-j-1}{d-1}\varepsilon_j,\quad t\ge d.}
\]

This is **not** merely the polynomial mean, nor an observed financial return trend. The true *population expected* trend is \(0.02t+\mu\binom td\), but we reconstruct the actual stochastic trajectory including the integrated shocks. Both true trend and fitted penalty use the *same* d in each experiment. This ensures correct matched-order baseline, **not** an experiment in automatic order selection. The generalization retains the existing d2 five-seed pilot *unmodified*.

For all d, let \(p_t=\binom td\); \(D_dp=\mathbf1\). On one original random draw, set \(y_\mu=y_0+\mu p\), \(\tau_\mu=\tau_0+\mu p\). **The same centered innovations and observation errors are reused across all five** \(\mu/\sigma_\varepsilon\in\{-1,-0.25,0,0.25,1\}\). The first series of R3 is reused in R1. These correlations are **deliberate paired design**, not independent observations.

**Scale caveat:** \(\mu=0.3\) times \(\binom{199}{4}\) for d4/N200 creates a very large deterministic quartic signal. Do not compare raw MSE or absolute polynomial amplitude across d as if they represent the same inference difficulty. Interpret *within* fixed \((d,N,\sigma_\eta,\mu,R)\), and report relative paired reconstruction losses, S, boundary hits and numerical stability. Optional future calibrated-signal-scale factorial is **not part of this frozen design** and would need a new protocol/seed bank.

## 3. Parameter selectors and what is optimized

Keep exactly the **eight original procedure labels**:

1. Known true mean and true ratio \(\lambda_G\) (**oracle**, not feasible).
2. Wrongly forced \(\mu=0\), Gaussian differenced-covariance ML for the two variances.
3. Wrongly forced \(\mu=0\), pooled ordinary observed-series LOOCV for \(\lambda\).
4. True known mean with Gaussian differenced-covariance ML for variances (**mean oracle**).
5. True known mean with pooled observed-series LOOCV (**mean oracle**).
6. Pooled sample-mean of observed d-th differences (Guerrero-inspired) plus **our** fitted conditional Gaussian variance likelihood; feasible hybrid.
7. Common Gaussian GLS-profiled \(\mu\) and two variances via differenced-data contrast likelihood; feasible.
8. One common \(\mu\) fitted jointly with trends inside **fold-clean pooled observed-LOOCV**, minimizing the exact training-deletion PRESS; feasible.

All methods reconstruct \(\widehat\tau\) using penalized least squares; each pool selects one shared \(\lambda\) from the average observed LOOCV loss (not from averaging separately optimized \(S_r\)). The true latent trajectory is used **only after** selection to measure
\[
\mathrm{TrendMSE}=(RN)^{-1}\sum_{r,t}(\widehat\tau_{rt}-\tau_{rt})^2.
\]

Guerrero and Gaussian covariance methods also rely on a \(d\)-th difference mean and noise-covariance model; the fitted sample covariance \(\operatorname{Var}(D_d y)=aI+bD_dD_d^\top\) is correct under this Gaussian DGP. **Frozen all-data GLS/plugin-mean PRESS is not honest CV**; the joint-mean LOOCV method re-estimates the common mean inside each deletion. Estimating the mean changes effective degrees of freedom, so the saved original normalized S only parameterizes \(\lambda\), not complete EDF.

**Efficiency without redefining any estimator:** six methods are equivariant to shifts \(y\mapsto y+\mu p\) and need to be evaluated only **once at baseline \(\mu=0\)** for each independent (d,N,eta,seed,R). Their reconstructed MSE, observed PRESS and estimated variance ratios are mathematically invariant under these deterministic polynomial shifts. Only the two forced-\(\mu=0\) methods must actually be recomputed for every new \(\mu\). The fast path should be verified numerically against direct eight-method recomputation before executing any large run. This identity improves computation; it does not increase independent evidence.

## 4. The 10,000-seed sampling contract

**10,000 independently seeded base R3 pools per** \((d,N,\sigma_\eta)\), not 10,000 rows or 10,000 pooled method measurements. All 16 strata:

\[
4\ \text{orders}\times2\ \text{lengths}\times2\ \text{noise levels}
=16\ \text{base scenario groups}.
\]

Each has **10,000 independent shock-stream seeds** -> 160,000 independent R3 shock pool draws. Each base draw is examined under five μ interventions and two nested R values: \(160000\times5\times2=\mathbf{1,600,000}\) distinct pooled treatment evaluations. Eight procedures per treatment: **12,800,000 method records**. **Only the 160,000 base streams are independent; the five μ variants and R1/R3 nested versions are dependent.**

The new RNG seed bank starts **82100000** and never reuses the original pilot's base 69000000:

\[
\mathrm{seed}=82100000+10^6d+200000\,i_N+100000\,i_\eta+j,
\quad j=0,\ldots,9999,
\]

with \(i_N=0,1\) for N50/N200 and \(i_\eta=0,1\) for ηSD .5/2. Every base shock draw uses a distinct integer RNG initialization. Within each stratum, seed index \(j\) is the **independent statistical replication unit**. No inferential sample size inflation from R, μ or method rows.

**Execution source code**: `experiments/pooled_loocv_smoothness/run_nonzero_mean_multorder.py` for one disjoint shard, `launch_nonzero_mean_multorder.py` for optional parallel, resumable manual launch, and `aggregate_nonzero_mean_multorder.py` for source-checked aggregation and paired-difference uncertainty. The source commit SHA, seed interval, scheme, data SHA256, exact d/N/noise/methods, Python/NumPy/SciPy versions and source manifest are saved per shard.

## 5. Shards, execution cost, checkpointing, source hygiene

**At the default 100 base seeds per shard**, the complete design is 16 × (10,000/100) = **1,600 independent shard folders**, each containing 100 base draws × five μ values × two nested R × eight methods = **8,000 compressed CSV rows** (not 8,000 independent draws). The full completed campaign is **12.8 million rows** stored in sharded gzip CSV on the machine, likely substantial disk usage and nontrivial CPU demand.

This is a large project: **do not launch all 10,000 seeds automatically**, do not compile the manuscript or trigger heavy simulations on push, and do not treat the written protocol as completed experiment data. Performance and numerical rank for d4/N200 require explicit preflight; ordinary EVD of \(Q=D_d^\top D_d\) can numerically drop the tiny d4 modes. To avoid this, the library now caches spectral bases across equal N,d and uses an **SVD of \(D_d\)** to obtain the positive squared singular values for d4; similarly the contrast covariance uses D's SVD. Check full d4 fitted-mean and forced-zero methods, actual reconstruction MSE, fold refits and affine invariance before large confirmation.

Shards are **immutable**. Existing complete shards with matching source SHA and SHA256 are skipped by the launcher; incomplete or mismatched shards raise instead of overwriting. Resume by reissuing the SAME launch command after an interruption. If one shard was interrupted, diagnose/rename just its incomplete folder before restarting that interval; never delete completed results indiscriminately. Parallelism is controlled by `--workers`. Every worker can reuse cached spectral bases for repeated N,d. All large computations are **user-initiated on the local workstation/university machine**, not cloud background tasks in ChatGPT.

The aggregator consumes shard *summaries*, checks seed-range overlaps, a single source SHA, per-shard method coverage and optional original CSV SHA256; it computes group means, sample SD and SE, and **within-seed paired MSE difference** means/SD/SE separately at each \((d,N,\sigma_\eta,R,\mu)\). A run with even one missing of the 160,000 base seed draws is marked **INCOMPLETE_EXPLORATORY** and cannot be described as full confirmation. Never copy 12.8 million potentially licensed/large method rows indiscriminately into standard Git: keep raw gzip shards locally/backed up and commit **small aggregate CSVs/manifests plus source SHA/provenance** after manual audit. To reproduce raw rows, rerun the seeded code at the recorded commit (plus matching computational environment).

## 6. Execution recipes (root checkout)

### Strict smoke/preflight with one or two independent base seeds

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_nonzero_mean_multorder.py -q
# No simulation; only print design
python -m experiments.pooled_loocv_smoothness.launch_nonzero_mean_multorder --d 4 --n 200 --sigma-eta 2 --seed-stop 2
# Actually execute just 2 independent d4/N200/noise2 seeds; explicit opt-in
python -m experiments.pooled_loocv_smoothness.launch_nonzero_mean_multorder --d 4 --n 200 --sigma-eta 2 --seed-stop 2 --workers 1 --root results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/preflight_d4_N200 --execute
```

This tests d4's most ill-conditioned and largest-scale cell in an **isolated preflight directory**. Do not run a short interval under the default `confirmatory/` root: the full campaign later creates larger [0,100) shards and would overlap [0,2). The launcher now checks for such overlap and refuses to mix intervals. Inspect its manifest, compression digest, finite reconstructed loss, boundary λ and numeric invariance. The completed preflight is **not counted** in the full 10k-per-cell confirmatory root. Test at least one N50 and η=.5 cell before enabling larger jobs.

### Full campaign only AFTER preflight, manually opt in

```powershell
# PLAN ONLY: 1600 shards / 160000 independent base draws / 12800000 method rows
python -m experiments.pooled_loocv_smoothness.launch_nonzero_mean_multorder --workers 8

# One selected d first; 400 shards at 100 draws each, manually choose CPU worker count:
python -m experiments.pooled_loocv_smoothness.launch_nonzero_mean_multorder --d 2 --workers 8 --execute

# All four orders after numerical verification:
python -m experiments.pooled_loocv_smoothness.launch_nonzero_mean_multorder --workers 8 --execute

# Aggregate checked compact per-method and PAIRED MSE statistics:
python -m experiments.pooled_loocv_smoothness.aggregate_nonzero_mean_multorder --out-dir results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/audit_confirmatory_001 --require-complete --verify-digests
```

Only the **plan** is run by default; `--execute` launches jobs. On resume, completed matching shards are skipped; on a cross-code SHA mismatch it stops rather than silently mixing cohorts. Aggregator output directory must be new, preventing overwrite of a previous audit. `--require-complete` rejects incomplete runs; without it, aggregates are marked exploratory/incomplete.

Do not automatically stage the 1,600 compressed raw gzip shard files into GitHub. Back up the raw shards outside temporary university machines; use the saved campaign manifest, compact aggregate CSVs and reproducible independent seeds to preserve provenance. GitHub Actions runs **mathematical tests and a tiny 1–2-seed smoke only**, not the full confirmation.

## 7. Interpretation and staged future robustness

Our comparison is *retrospective reconstruction of artificially generated latent stochastic trends*. It is **not** about forecasting stock prices or estimating the unique 'true trend' of observed financial data. For each order the expected trend polynomial degree changes, and \(\mu\) is a nonzero expected d-th difference. The analyst chooses d in advance (no automatic cross-order selection), then pools **observed LOOCV losses** across independent same-length series.

After passing numerical tests and full independent-seed confirmation, assess the primary contrasts per cell, by \(\mu\), and report paired MSE effect sizes and Monte Carlo uncertainty (including large boundary errors). An insignificant difference cannot be declared proof of equivalence. *Then* create an **independent non-Gaussian extension** preserving the same d/N/noise-factor conventions. Consider standardized Student-t with finite variance, skew-normal or centered Gamma, contaminated Gaussian jump mixtures and Student-t GARCH-type dependence with well-defined marginal covariance. Cauchy has **undefined population variance and infinite/undefined squared-risk expectation**, so a Guerrero true finite-variance-ratio benchmark cannot be compared to it and robust finite-sample absolute errors require separate analysis. Never silently combine these two DGP phases.

**Research conclusion currently justified only by the executed five-seed pilot:** incorrectly imposing zero mean can be much more damaging than the tiny observed ML-versus-CV loss difference for some nonzero-\(\mu\) scenarios; there is a small price to estimating unnecessary \(\mu\) when it truly is zero. This *provisional* effect must withstand the new independent 10,000-seed-per-stratum analysis before a statistically defensible paper claim.
