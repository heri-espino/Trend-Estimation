# Instructions for coding/research agents

**Last updated: 2026-10-09. Read this file FIRST, then**
1. [AI_HANDOFF.md](AI_HANDOFF.md) — implementation state / what is NOT done;
2. [working_papers/THEORETICAL_CONTRIBUTIONS.md](working_papers/THEORETICAL_CONTRIBUTIONS.md)
   — authoritative claims, equations and mathematical priority;
3. [working_papers/WEIGHTED_SURFACE_PROTOCOL.md](working_papers/WEIGHTED_SURFACE_PROTOCOL.md)
   — shared canonical statistical decision protocol;
4. [working_papers/SIMULATION_EVALUATION_PROTOCOL.md](working_papers/SIMULATION_EVALUATION_PROTOCOL.md)
   — factorial DGPs, baselines, oracles, independent evaluation;
5. [apps/README.md](apps/README.md) — **one canonical Streamlit app per paper**;
6. [experiments/smoothness_cv/CAMPAIGN_README.md](experiments/smoothness_cv/CAMPAIGN_README.md)
   — manual extensive simulations, checkpointing and float32 GPU benchmark.

### Current 8-hour shared experiment across all three papers

Read [JOINT_FORMAL_8H_PROTOCOL.md](working_papers/JOINT_FORMAL_8H_PROTOCOL.md)
BEFORE proposing a publication-ready experiment. The
\`formal8h\` preset is **144** predeclared cells;
\`--time-budget-hours 8\` stops at a completed batch
(soft budget). The three papers share identical
DGPs, losses, selected S, and untouched outer
forecast origins. P1/P2 share the same weighted
F; a predeclared subsample of those F surfaces
is evaluated by Paper 3's grid, multibracket
Brent and adaptive derivatives, with exact
small-instance Sturm ONCE. Simple
naive/drift/seasonal-naive/OLS forecasts
are separate baselines, without fictional
smoothness indices. Results contain
past true-trend recovery and future
latent/observed forecast error, plus
predeclared equal-tau multi-noise PDFs.

**The time-stop DOES NOT manufacture a
completed balanced experiment.** Time-truncated
result tables are exploratory; independent
confirmatory seeds/tests are required
before a journal claim.

## PRIORITY UPDATE (2026-10-11): fourth paper, nonzero difference mean

**Read this before using the older "three papers" map.**
New lead:
[Trend Simulation and Mean-Difference Forecasting](working_papers/Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting/README.md).
The earlier three working papers remain preserved as independent
historical/parallel research, **NOT deleted**. Do not modify the
ongoing μ=0 CUDA 8-hour campaign or its results and pretend
it already tested the new μ≠0 model.

**Verified source Guerrero (2007)** introduced nonzero mean of
d-th differences and a data plug-in μ. Source already implemented
in \`core/solvers.py\`; \`forecasting/operators.py\` already handles
affine continuation. The NEW research extension implemented in
\`forecasting/mean_difference_cv.py\` analytically profiles one common
μ(S) from completed historical h-step forecast losses. This is
a **candidate research contribution, not verified publication
novelty or general forecasting improvement**.

Mandatory mathematical distinctions:
1. fixed μ: \(H x+\mu(I-H)p\), \(D_dp=1\);
2. Guerrero per-window plug-in μ from mean(D x);
3. common μ(S) chosen by completed forecast-CV, then S;
4. in-sample minimizing over BOTH τ,μ changes penalty matrix
   to \(D^\top(I-11^\top/(L-d))D\), with **d+1 nullity**.
Never conflate (3) with (4) or re-use pure-model EDF for
the complete data-selected μ procedure.
Source-grounded full derivations:
[Obsidian 06](notes/conceptos/06-Media-de-diferencias-Guerrero.md)
and [Obsidian 07](notes/conceptos/07-Perfilamiento-de-mu-en-CV.md).
Paper notes:
[proof ledger](working_papers/Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting/notes/PROOF_LEDGER.md)
and [simulation atlas](working_papers/Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting/notes/SIMULATION_ATLAS.md).

First new tests:
\`pytest tests/test_mean_difference_forecast_cv.py tests/test_mean_difference_pilot.py -q\`.
Pilot runner: \`python -m experiments.mean_difference_forecasting.run_pilot --dry-run\`.
**Not tested by this agent on user workstation; CUDA for the new
μ-extended problem is still NOT integrated.**
The existing three Streamlit apps remain specific to older papers;
the NEW fourth `apps/mean_difference_forecasting.py` calls the
shared nonzero-μ library for exploratory CV and trend visualization.
It has not yet been smoke-tested on the university environment.

## Research-note-first writing contract (2026-10-09)

Before editing \`manuscript/main.tex\` or claiming publication readiness,
read [NOTES_TO_MANUSCRIPT.md](working_papers/NOTES_TO_MANUSCRIPT.md)
and the three **Markdown note layers** within the relevant working
paper's \`notes/\` folder:

1. \`RESEARCH_NOTEBOOK.md\` — delimitation, theory motivation,
   exact forecasting algorithm, mathematical question and eventual
   journal-appropriate narrative.
2. \`PROOF_LEDGER.md\` — status-separated known identities, proved
   propositions, assumptions, counterexamples and genuinely open
   results. Never equate algebraic derivation with proven novelty.
3. \`SIMULATION_ATLAS.md\` — exact generator definitions and
   train/validation/outer semantics, \`y=tau+season+noise\`, diagrams
   of \`tau\` versus fitted and extrapolated trends at multiple noise
   levels, hypotheses, tables and **figures not yet generated**.

The first two papers share the 528-cell prospective simulation
campaign but ask **different scientific questions**. The numerical
paper has its own analytic known-root benchmarks and PLS F(S)
stress tests: do not interpret a simulated latent tau as the
ground-truth stationary roots of F. Historical results are
maintained with original scope; the new extensive run remains
prospective until verified.

## What research are we doing?

Three **independent** active papers, with common PLS infrastructure:

| Paper | Working folder | Canonical app | Central scientific decision |
| --- | --- | --- | --- |
| 1, horizon-matched pooled forecast-CV | \`working_papers/Working Paper - Smoothness Cross Validation/\` | \`apps/pooled_forecast_cv.py\` | Average **completed forecast-loss functions** using fixed temporal weights; choose global argmin of latest weighted F |
| 2, method-specific dynamic branches | \`working_papers/Working Paper - Dynamic Branch Selection/\` | \`apps/dynamic_branch_cv.py\` | Apply the **same time weights to F**, identify each local minimum, link branches across complete historical origins, choose a branch and operational S |
| 3, numerical methods | \`working_papers/Working Paper - Numerical Methods/\` | \`apps/numerical_methods.py\` | Reliably recover and compare stationary points and exact endpoints of **one fixed F(S)**; adaptive derivative search, rational/Sturm only under documented scope |

**Do not conflate** Paper 1's global minimization, Paper 2's temporal
correspondence, and Paper 3's one-function numerical root-search.
Do not call them compulsory companion papers: shared code does not
merge the independent scientific objectives.

## Non-negotiable statistical contract

At current origin \(T\), fit width \(L>d\), order \(d\), horizon \(h\):

- \(Q=D_d^\top D_d\), \(H_\lambda=(I+\lambda Q)^{-1}\),
  \(\widehat\tau=H_\lambda y\).
- **Spectral** \(H=U\mathrm{diag}((1+\lambda\delta_j)^{-1})U^\top\).
- Scalar normalized smoothness
  \(S=(L-\operatorname{tr}H)/(L-d)\in[0,1]\); **S is not H**.
  The source Guerrero scale is \(S_G=1-\operatorname{tr}H/L\).
- \(S=0\) means identity, \(S=1\) means the **exact rank-d nullspace
  projection**. Never approximate infinity by an arbitrary lambda.
- Prediction uses **h-step polynomial continuation \(G_{d,h}\)**,
  not simply the final row of H.
- \(\ell_{t}(S)=h^{-1}\|y_{t+1:t+h}-
  G_{d,h}H(S)y_{t-L+1:t}\|^2\).
- A historical loss may enter selection at \(T\) **only if \(t+h\le T\)**.
  Every validation target used for tuning must be completed and
  **external test targets must remain untouched**.
- The *method* \(m\) specifies chronological **weights on completed
  loss functions**: all-origin uniform, last-K uniform, linear,
  exponential, etc. It does NOT directly average S.
- \(F_r^{(m)}(S)=\sum_{q\le r}w^{(m)}_{r,q}\ell_{t_q}(S)/
  \sum_{q\le r}w^{(m)}_{r,q}\), with valid weights and completed origins.
- Paper 1 returns **global argmin of \(F_M^{(m)}\)**. Paper 2
  tracks the local minima of each \(F_r^{(m)}\), separately for each
  \((m,d,L,h)\). Only **AFTER** tracking does its \(\phi\) map (initially
  mean of last 3 local S minima of a selected branch) to operational S.
- Neither paper's current method requires a **second inner Val2**.
  Both require genuinely external h-step assessment.
- Refit the selected S on the last \(L\) observed data at operational
  origin \(T\), then forecast \(h\) steps. Never select a winner using
  an outer test and reuse those same test errors as independent proof.
- Preserve fixed d,L,h and weight scheme during a head-to-head
  comparison. A method selection over these settings needs its own
  inner historical selection layer or a new independent test.
- Window data are equally spaced index observations; economic or
  market irregular-calendar interpretation needs explicit care.

## Scope and originality: do NOT overclaim

**Known techniques**: PLS, eigen-decomposition of Q, EDF from its
eigenvalues, classical Guerrero index, simple [0,1] rescaling, standard
rolling time-series CV, conventional recency weights, analytic matrix
inverse derivatives, GPU matrix multiplication. None separately is
original here. The candidate contribution is a *specific
horizon-matched integration*, mathematical characterization and
measured out-of-sample behavior (Paper 1); temporal behavior/decision
value of method-dependent local-minimum branches (Paper 2); reliable
numerical search for structured forecast smoothness losses (Paper 3).
None is automatically a theorem or a published first.

**Prove/derive what is proven, label conjectures, do literature audit.**
Continuity/existence of a minimum ≠ uniqueness, convexity, stability
or global numerical certificate. Sparse/dense grids can miss minima.
Previously reported dense-reference matches cannot be promoted to
global completeness guarantees.

## Apps are distinct entrypoints, not copies

Run after installing \`.[dashboard,finance]\`:

~~~bash
streamlit run apps/pooled_forecast_cv.py
streamlit run apps/dynamic_branch_cv.py
streamlit run apps/numerical_methods.py
~~~

Keep formulas, controls, correct weighting semantics, visualization,
forecast origin and true/test distinction, matrix H, S/EDF, local
minima/candidates and reproducible downloads.

**Legacy trap:** \`apps/smoothness_lab.py\` and
\`apps/smoothness_lab_advanced.py\` are earlier Val1/Val2 designs.
Their contents and frozen CP04–CP08 are **not current Paper 2**.
Do not import those legacy apps into the current dynamic app.
Legacy analytical and manuscript material is retained for
reproducibility; don't rewrite frozen evidence to look contemporary.

### CUDA formal simulations (2026-10-09)

\`run_simulation_campaign.py --backend cuda\` is a **new,
one-GPU, batched loss-surface production backend**, not just a
benchmark. It computes float32 completed-origin forecast losses,
then uses the existing weighted-F minima/branch pipeline,
CPU classical comparators, vectorized selected-S outer refits
and SQLite storage. CPU eigendecomposition and S-to-lambda mapping
are still float64 and run on CPU. The numerical goal is to keep
the **same statistical estimator and same pretest chronology**.
No silent CPU fallback and no 32 competing CUDA processes.

**One-time** precision check: \`--preset smoke --backend cuda
--gpu-verify 2\`, in a distinct \`--run-dir\`.
**Formal run default**: \`--gpu-verify 0\` (no CPU/GPU
reference comparisons during batches). Expand to
\`--preset stress\` (720 new unusual cells) or \`--preset mega\`
(original 528 plus 720 = 1,248 cells) only after smoke and pilot.
See [CAMPAIGN_README.md](experiments/smoothness_cv/CAMPAIGN_README.md).
These additions remain *prospective experiments*, not results or
paper claims. GPU acceleration is secondary to theory.

## Experiments, computational workflow and limits

The prospective campaign has 528 factorial DGP cells (16 source-inspired
Cortés-Toto × 384 complexity × 128 regimes), with 100 requested
scenario–seed runs per cell = **52,800 simulation instances**,
not 52,800 statistically independent outcomes across all factors.
Within each DGP cell independent seeds are statistical replicates.
Compare all methods on paired series / same rolling outer origins.
Distinguish past latent recovery, future latent recovery and observed
future MSFE; make classical CV/GCV/AICc/BIC and fixed/ad-hoc S
*selectors*, not independent forecast performance metrics. Oracle
selectors using latent values are unavailable in practice.

Dedicated source reproduction uses **full series N=50/200** on
original 2^4 factorial, distinct from h-step forecast extension.
Keep historical CP01–CP08 records frozen; new code exists but
the extensive new campaign has **not been run / independently
validated in this repository**. Tests and actual GPU numerical
agreement still need to be checked on the university workstation.

A user-run float32 kernel benchmark on an RTX 4500 Ada reported
GPU/CPU32 speedups from 2.06x to 45.60x (transfer-inclusive).
This is **kernel performance**, not an end-to-end theoretical
contribution or proof of faster Monte Carlo campaigns. Preserve
hardware/data/precision metadata and comparison limitations before
adding a small implementation note to manuscripts.

**Heavy simulations, generation of figures, and PDF builds are manual
only** (\`workflow_dispatch\` if run in GitHub). Small CI/tests
should run automatically. Keep reproducibility manifests and
lightweight results in Git; do not accidentally commit giant SQLite
databases. All substantial simulations on the 32-thread university
machine are explicitly launched by the user; agents must not claim
to have executed a job they did not run.

## Before modifying research code or manuscripts

1. Identify the relevant paper's current vs legacy protocol.
2. State the mathematical research hypothesis and what is known.
3. Use shared \`src/\` and \`experiments/\` logic; app code only for
   interactive controls and plots.
4. Add tests for endpoint S=0/1, monotonic S mapping, forecast target
   isolation, chronology, weighting normalization, minima/branches,
   reproduction of old uniform pooled baseline, and numerical
   precision if replacing a CPU kernel with CUDA float32.
5. Preserve code and data provenance and do not overwrite historical
   checkpoints/manuscripts without explicit scope and validation.
6. Clearly report implemented vs tested vs simulated vs
   independently replicated vs mathematically proved.

**Priority order:** mathematical clarity > correct causal evaluation
> interpretable replicated evidence > app UX > speed optimization.

## Independent observed-series LOOCV paper (2026-10-18) — current branch policy

The independent classical **pooled observed-series LOOCV** working paper is at `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/`, **not** the earlier forecast-oriented numerical paper. Agents must first read `notes/RESULTS_LEDGER.md` and `notes/ROBUSTNESS_PROTOCOL.md` inside that paper before altering simulations or claiming a result. The ledger separates executed/committed pilots from smoke tests and unexecuted designs. Its stochastic-model extension compares known-ratio Guerrero, feasible Gaussian difference-likelihood variance-component estimation, NNLS moments and ordinary pooled LOOCV; do not attribute those proposed two-component estimators to Guerrero (2007).

**Explicit user Git policy for this work: no pull requests.** Commit edits **directly to the existing `paper/pooled-loocv-numerical-optimization` branch**, not `main`; do not open/reopen PRs, merge, force-push, or overwrite other agents' work. Keep full robustness/confirmatory Monte Carlo and figure generation **manual only**; ordinary small tests and smoke verification may use automatic CI. Use a new output folder for every independent DGP and preserve seeds, manifest, code SHA, per-pool CSV and research notes. The next robustness experiment includes Student-t noise, stationary AR1 observation errors and time-varying observation variance, with distinct confidence limits and no oracle claim for misspecified covariance.

### Independent heavy-tail stress safeguards (2026-10-18)

The next separate data-generator suite is `experiments/pooled_loocv_smoothness/run_tail_noise.py`, documented by `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/TAIL_NOISE_PROTOCOL.md`. It includes Student-t3 shocks, zero-mean centered Gamma (both skew signs), Gaussian jump mixtures, Student-t5 GARCH shocks, and Cauchy observation noise. Use **new pilot seeds** and output directory `results/pooled_loocv_smoothness/guerrero/tail_stress/pilot/`; do not overwrite or append rows to prior robustness pilots. Student-t3 has finite variance but infinite fourth moment. The Cauchy distribution has **no finite mean, variance or population expected squared-error risk**: its "noise_scale" is location-scale gamma rather than sigma_eta SD. Thus any Cauchy finite-sample `realized_true_trend_MSE` is a per-run diagnostic ONLY; summaries must emphasize medians and absolute-error quantiles and never claim a population risk or a true Guerrero ratio. This experiment models additive noise about simulated stochastic trends, not observed stock returns; empirical financial calibration requires a separate study. Keep 320-pool exploratory pilot and 6,400-pool confirmatory campaign manual-only. **No PRs; direct commits to the current independent paper branch.**

### 2026-10-18 pre-run design expansion

Before the next tail-stress **pilot** was run, the user requested more trend-difference orders and centered skew-normal noise. The runner `run_tail_noise.py` now must generate and fit matching `d=1,2,3`, and include five analytically population-centered skew-normal shapes `alpha=-6,-3,0,+3,+6`, in addition to the original eight noise settings. Final prospective pilot is **1560 nested pools / 4680 method rows**, not the obsolete 320/960 plan. Manual only. Never report means across d as if the different integrated-trend magnitudes were comparable; stratify by d and regime. Tests must verify (D_d\tau=\varepsilon) numerically for every d and that skew-normal population mean is zero and variance is fixed across alpha.

### Tail-stress experimental results checkpoint (uploaded 2026-10-18 local)

The version-2 pilot `results/pooled_loocv_smoothness/guerrero/tail_stress/pilot/` is **EXECUTED and COMMITTED**, not just a proposal: 156 scenarios, 5 replicate seeds, R=1 and nested R=3, **1,560 paired pools and 4,680 method rows**. Read `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/TAIL_NOISE_PILOT_AUDIT_2026-10-18.md` and `notes/RESULTS_LEDGER.md` within that paper before modifying its conclusions. The independent repeat audit is `python -m experiments.pooled_loocv_smoothness.audit_tail_noise`; optional figures are MANUAL with `--figures`.

Only 720 primary R=3 pools have finite population observation-noise variance (12 regimes × 3 d × 20). Gaussian contrast likelihood slightly reduced mean latent reconstruction MSE versus observed LOOCV in each **matched** d, but not uniformly or significantly established; cross-d average errors are not a valid order selection experiment. Cauchy has no population expected square risk, true variance ratio, or finite mean/variance: use robust error summaries. Seven primary R3 pools had multiple numerical derivative sign-change candidates but no bounded-Brent objective misses versus multibracket at 1e-7. **No global numerical superiority or realistic stock-return forecasting result has been established.** The next possible experiment must **hold the same generated latent truth fixed** while comparing fitted d choices without revealing truth to selection. Confirmatory presets remain unrun/manual; no PRs or merging.

### 2026-10-19 analyst-fixed order and historical finance calibration

User reaffirmed the original pooled-LOOCV experiment fixes difference order `d` **by analyst judgment**, then chooses ONE common lambda by minimizing **the average of the R LOOCV loss functions**. This is different from averaging each series' separately optimal S; do not misrepresent the tail-stress matched-d factorial as automatic d selection.

A new **unrun actual-market noise calibration** protocol lives in `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/EMPIRICAL_MARKET_BOOTSTRAP_PROTOCOL.md`, runner `experiments/pooled_loocv_smoothness/run_empirical_market_noise.py`, tests `tests/test_empirical_market_noise.py`. SPY adjusted daily returns 2015–2025 determine a demeaned empirical *marginal distribution* for synthetic additive observation noise; matched Gaussian, iid resampling and circular block (5/20) variants are compared on the SAME synthetic latent truth. The synthetic tau is the conditional mean; no real SPY price trend is labelled as known truth. The market snapshot is personal-use data saved under ignored `data/market_calibration/` and its SHA256 is retained in the research manifest. CI smoke must NEVER access Yahoo; full pilot/figures manual only. When results arrive, audit matched R=3 latent reconstruction error; direct Git branch only, no PRs.

### 2026-10-19 nonzero mean differences in independent pooled observed-LOOCV paper

Guerrero (2007) **already** models (D_d\tau=\mu\mathbf1+\varepsilon) for nonzero μ and gives an observed-difference mean plug-in. The *other fourth* `Working Paper - Trend Simulation and Mean-Difference Forecasting` already profiles μ against completed h-step forecast losses. **Do not conflate that forecasting study with this independent observed-series LOOCV sensitivity study**. User explicitly approved studying the impact of imposing μ=0 when the true mean is nonzero, fixing analyst order d=2.

New protocol `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/NONZERO_DIFFERENCE_MEAN_PROTOCOL.md`, code `experiments/pooled_loocv_smoothness/mean_difference_methods.py`, `run_nonzero_difference_mean.py`, tests `tests/test_nonzero_difference_mean_reconstruction.py`. A pooled analogue of Guerrero's observed difference mean is paired with our conditional Gaussian covariance ML as a hybrid baseline; it must NOT be called the exact Guerrero estimator. Fitted Gaussian difference-covariance contrast now has GLS-profiled μ and two unknown variances. Pooled observation LOOCV has **exact PRESS accounting for μ re-fitting inside each fold** (tested against explicit deleted-observation normal equations), NOT a frozen all-data μ. Joint μ increases effective degrees of freedom; do not interpret nominal S as full data-selected estimator EDF. New unrun pilot N50/200, sigma eta .5/2, epsilon SD .3, μ/epsilon SD=-1,-.25,0,.25,1, five shared-shock seeds per setting, nested R1/3: 200 treatment pools, 1600 method rows but only **20 distinct random-shock pool draws** repeated across 5 mu values. Cluster/compare by N, sigma eta and original seed for uncertainty. Source results will live under `results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/`. CI tiny smoke only; no PRs, direct branch commits; never overwrite earlier μ=0 datasets.

### 2026-10-19 executed mean-difference pilot: do not mistake as unrun

The exploratory `results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/` is **already executed and committed**, with 200 paired R1/R3 treatment pools / **1600 rows**, eight selectors and two genuine generated PNGs, source SHA `90521235df9dab729451fcceb2e5a001554e3e9a`. Read the [source-linked audit](working_papers/Working%20Paper%20-%20Pooled%20LOOCV%20Numerical%20Optimization/notes/NONZERO_DIFFERENCE_MEAN_PILOT_AUDIT_2026-10-19.md). 100 R3 treatment evaluations use only **20 independent random-shock pool draws** reused across five mu shifts, with R1 nested. Strict zero mu can harm trend MSE when true mu nonzero, especially for Gaussian variance ML; fitted mu methods nearly invariant across shifts **by algebra**, not independent evidence. The calculated PRESS of all-data mu plug-in/GLS fits is NOT fold-clean LOOCV, unlike the joint CV with exact deletion refitting. No independent confirmatory results; never reinterpret as a verified forecasting improvement, Gaussian MLE defeat, or new Guerrero model. No PRs.

### 2026-10-19 canonical methodology and *unexecuted* 10k-seed multorder confirmation

Read `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/HOW_THE_SIMULATION_WORKS_AND_MEASURED_RESULTS.md` before interpreting any Gaussian difference-mean results. It explicitly documents *executed fixed-d2 G pilot* (1,600 rows), simulation of realized stochastic tau (NOT just its expected polynomial), 8 methods/oracles, paired noise seeds, output metrics, all measured tables and source SHA. Source Guerrero itself already considers nonzero μ; do not invent novelty.

User requested four-order `d=1,2,3,4` manual confirmatory Gaussian campaign with **10,000 independent R3 shock draws in each of 16 (d,N,etaSD) strata**, 160k independent draws across strata, 5 paired μ-shifts and nested R1/3 => **1.6M treatment pools and 12.8M method rows**. Its protocol `notes/MULTIORDER_10000_SEED_CONFIRMATORY_PROTOCOL.md` (under paper's notes), new runner `run_nonzero_mean_multorder.py`, manual-only launcher `launch_nonzero_mean_multorder.py`, independent aggregator `aggregate_nonzero_mean_multorder.py`, tests `test_nonzero_mean_multorder.py`. **Code implemented but NO full 10k-seed confirmations executed or claimed**. Large runs only under explicit local `--execute`, resumable checksum-verified compressed shards (100 independent base seeds each), stable SVD/cached spectral basis for d4, and compact per-(d,N,noise,μ,R) paired reconstruction-MSE statistics. Be careful that `μ*binom(t,d)` at d4/N200 is huge; only compare within fixed d,N,noise and monitor numeric tolerances. Do NOT Git-add all 12.8M raw method rows; preserve backed-up shards locally and push compact aggregates with source provenance after completing validation. Non-Gaussian μ extension is a separate later experiment, never mix its tests with H. No PRs, no merging.

### 2026-10-19 ACTUAL completed 10k-seed Gaussian multorder confirmation (supersedes earlier unrun plan)

The large **Gaussian** mean-difference 4-order campaign **IS COMPLETED**, uploaded and independently audited. Exact measured findings (not claims from small d2 pilot): `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/MULTIORDER_10000_SEED_CONFIRMATORY_RESULTS_2026-10-19.md`. Original three compact files in `results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/audit_001/`; original run source SHA `070b363b7d8a8156f320c833539fa068b684fc7b`, 1,600 nonoverlapping and SHA-verified gzip shard references, 16 cells × 10k independent R3 shock pools each = 160k independent base draws / 1.6M paired/nested treatment pools / 12.8M method records. Actual source raw gzip shards remain user-local and MUST be backed up if machine disposed of. CI `audit_multorder_confirmatory.py` & `test_multorder_confirmatory_aggregate.py` inspect **saved compact data only**, not Monte Carlo.

**R3 findings:** at μ/σε=+1 wrongly forcing zero μ in Gaussian ML costs more latent-MSE than the fitted-μ GLS ML vs fold-clean CV loss gap in all 16 (d,N,eta) settings. Fitted-μ Gaussian ML has lower mean trend MSE in 15/16; exception d1/N50/etaSD2 where CV better. Gaussian DGP only. When μ=0 restriction correct, smaller finite-sample MSE than unrestricted μ fits in all R3 cells. **R1 has real high-noise small-N counterexamples** and must be separately reported. All 5 μ shifts use exactly the same shocks, so no sample-size inflation; d always analyst-fixed. Guerrero already treats nonzero mean; don't call it a new model. The distinct μ≠0 x non-Gaussian extension remains NOT DONE. No PRs, merges, force pushes, automatic massive reruns, or claiming stock forecasting.

### 2026-10-19 non-Gaussian × nonzero difference mean follow-up — planned, not run

Read `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/NONGAUSSIAN_NONZERO_MU_PROTOCOL_2026-10-19.md` BEFORE running or describing study J. It contains 12 distribution laws of **finite observation variance**, all generator constants inherited from `run_tail_noise.py`, matched fixed d1–4, N50/200, eta population SD .5/2, nested R1/3, five μ shifts with identical underlying noise draws. The 25-independent-seed pilot has 192 cells → 4,800 base shocks, 384,000 rows. **NOT EXECUTED** as of this checkpoint. Separate confirmatory has 10k NEW seeds/cell → 1.92M base draws/153.6M rows **NOT EXECUTED**. Distinct seed banks and separate paths; user explicitly launches `--workers 32 --execute`, no heavy CI. `run_nonzero_mu_nongaussian.py`, `launch_nonzero_mu_nongaussian.py`, `aggregate_nonzero_mu_nongaussian.py`, `tests/test_nonzero_mu_nongaussian.py` are the new source. Student t3: infinite fourth moment -> normal-approx squared-loss SE may be invalid. Cauchy excluded because true variance ratio and population MSE undefined; design robust-risk phase separately. GARCH-t5 observation noise is uncorrelated but conditionally heteroskedastic, so don't assert covariance structure is false merely due temporal volatility dependence. Check every source commit SHA and gzip digest before interpreting uploaded pilot; do not substitute the old 13-regime `mu=0` tail pilot. Raw shards ignored, compact aggregate trackable, no PR or merge.

### 2026-10-19 Study K: Cortés-Toto 2017 four statistical criteria vs mean and numerical search (not run at scale)

Read `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/CORTES_TOTO_CRITERIA_AND_NUMERICAL_COMPARISON_PROTOCOL_2026-10-19.md` before comparing selection methods. Source article **Cortés-Toto, Guerrero, Reyes (2017)** used **CV, GCV, AICc, BIC** for PLS (their simulated main d2 with μ0) and describes Guerrero's controlled S; AIC discussed but excluded from final experiment due numerical unreliability. The article credits Guerrero (2007) with nonzero mean; not novel here. Our extension pools R similar series and estimates a **single common μ** inside joint PLS. GCV/AICc/BIC must use exact pooled effective degrees-of-freedom (R\mathrm{tr}H_\lambda+\lambda\|b\|^2/(p^\top T p)), unlike fixed μ's (R\mathrm{tr}H); *numerical solvers* (Brent/multibracket) are separate factors, not methods of statistical selection. AICc is undefined if RN−EDF≤2; simple plug-in BIC with logRSS diverges to minus infinity as λ→0, so only **explicit finite-domain BIC** is implemented and globally optimal claims forbidden. `experiments/pooled_loocv_smoothness/cortes_optimality_criteria.py`, `run_cortes_criteria_case.py`, `tests/test_cortes_optimality_criteria.py` provide tested library and ONE-shock replay of existing non-Gaussian J pilot; **NO newly run 25- or 10000-seed full K simulation or manuscript result**. Avoid all-data mu leakage into fold-CV; exogenous true-mu fixed is an infeasible oracle. Study J source data are unchanged, no PRs, no merge, no heavy push-triggered run.

### 2026-10-19 Study K.1 26-method 25-seed J-pilot replay — implemented, unexecuted

User ran only ONE case with 18 Cortés-Toto/control policies and 8 prior comparators (Gaussian d2/N50/R3/μ/epsSD+1, seed 128000000): `cv_zero_multibracket` lowest **post-hoc latent MSE in that one draw**, not method dominance. Source protocol `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/CORTES_TOTO_PAIRED_25_SEED_REPLAY_PROTOCOL_2026-10-19.md` freezes a **paired replay of SAME prior Study J 25 independent RNG shock streams per each 192 (12 laws×4 d×2 N×2 eta) strata**, 4,800 REUSED R3 base shock draws, 5 paired mean shifts/nested R1/3 = 48k treatments, 26 procedures total (18 new criteria/mean modes and original 8), 1.248M compressed method rows. Core `run_cortes_criteria_pilot.py`; manual-only `launch_cortes_criteria_pilot.py --workers 32 --execute`; `aggregate_cortes_criteria_pilot.py` SHA256, source SHA/solver, disjoint original 25 seeds, parity of old-eight-method MSE with committed original J pilot; `tests/test_cortes_criteria_paired_pilot.py` fast CI only. **Code ready, full replay NOT RUN**. Avoid statistical sample inflation, leakage in frozen all-data mean CV, incorrect jointly fitted μ EDF, normal CI for Student-t3 infinite fourth moments, unconstrained BIC claims and cross-d comparison. No PR, no merge, no automatic full run on push. Gitignore raw shards; commit only compact audits and backup local gzip data.

### Completed K.1 source-matched 26-method non-Gaussian CV/GCV/AICc/BIC pilot (2026-10-19)

Study K.1 is now **EXECUTED AND UPLOADED**, superseding prior unrun plan. Authoritative report `working_papers/Working Paper - Pooled LOOCV Numerical Optimization/notes/CORTES_TOTO_PAIRED_25_SEED_REPLAY_RESULTS_2026-10-19.md`, compact original data `results/pooled_loocv_smoothness/guerrero/cortes_criteria_replay/audit_pilot_001/`, run SHA `1785889d7d64a77f548d8746d41a9ea786e3e588`. 192 cells × 25 exactly **REUSED prior Study J independent shocks**, 1.248M result rows, 49,920 method aggregates, 80,640 paired aggregates and exact 15,360-original-method parity MSE error 0.0. Independent compact-only audit `audit_cortes_criteria_confirmed_pilot.py` and tests `test_cortes_criteria_confirmed_aggregate.py` in dedicated CI; source gzip files remain user-local. At R3/μ/epsSD1: GLS quasi-ML mean reconstruction MSE lower in 179/192 than new CV, 180/192 than GCV, 178/192 than AICc. At R1 AICc/plug-in descriptively competitive or lower than GLS average. BIC logRSS chooses λ lower finite-domain boundary **4800/4800** underlying shocks at each R; show as criterion pathology, NOT generic BIC failure. Two variants of identical exact-fold CV optimize with different numerical search and yield DIFFERENT true MSE; next independent numerical solver protocol must compare identical CV score values and function-call costs at their λ selections, controlled search bounds, before attributing method superiority. **25 original seeds per scenario**: exploratory only, not new 10k confirmation. t3 infinite fourth moment, Cauchy omitted. Preserve source protocol history; no PR, no merge, no heavy CI.
