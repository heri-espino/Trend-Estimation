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
