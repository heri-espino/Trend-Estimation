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
