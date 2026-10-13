# AI handoff — current Trend-Estimation research workspace

**Updated 2026-10-09. Read [AGENTS.md](AGENTS.md) FIRST and
[theoretical charter](working_papers/THEORETICAL_CONTRIBUTIONS.md)
before interpreting any old code, manuscript or checkpoint.**

## Frozen-campaign statistical audit — ready to execute (2026-10-12)

The user explicitly requested starting the audit of the
**already completed** 100,848 independent Monte Carlo replicates.
Do not run or suggest rerunning the \`formal8h\` simulation campaign.

New dedicated audit runner:
\`python -m experiments.smoothness_cv.audit_frozen_evidence
--report-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact
--frozen-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN\`

It reads the existing report CSVs and frozen SQLite **mode=ro**,
checks manifest/coverage/ratio/pair identity, runs independent
scenario-specific seed-level paired Student t diagnostics,
adjusts via Holm across the *full* P1/P2 families,
identifies tails and heterogeneity by shape/noise/study/
horizon/sigma/seasonality; analyzes all existing P3 numerical
JSON records WITHOUT recomputing F or forecasting.
S/EDF and branch metrics are sourced from the local
\`paper1_2_method_scenario.csv\`, not invented from
public paired-only exports.

Outputs under \`reports/frozen_compact/audit/\`.
Upload small review through
\`python -m experiments.smoothness_cv.publish_frozen_audit
--audit-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit --push\`.

Scientific protocol/limitations:
[JOINT_FORMAL_8H_AUDIT_PROTOCOL.md](working_papers/JOINT_FORMAL_8H_AUDIT_PROTOCOL.md).
Code committed but audit **NOT YET RUN** on the user's
frozen 31.47-GiB local database at time of this entry.
Do not claim numerical conclusions from audit outputs
until they are actually generated and published.

## Scientific interpretation completed (2026-10-12)

Read [JOINT_FORMAL_8H_RETROSPECTIVE_2026-10-12.md](working_papers/JOINT_FORMAL_8H_RETROSPECTIVE_2026-10-12.md)
before proposing a paper merger or additional experiments.
It derives a **carefully qualified** research priority from the
published 100,848-task frozen report:
- P1 horizon-matched forecast-CV broadly beats in-window
  CV/GCV/BIC across predeclared simulated DGPs; AICc is
  comparatively closer. Extreme BIC values require validation.
- P2 tracked recent exponential minima are often better than
  pooled under the **same** weighting. The decision rule also
  averages last K S values, so the observed gain does NOT yet
  establish that branch persistence itself beats simple temporal
  smoothing of global minimizers. No ablation has been run.
- P3 numerical (only h=3, 50,424 records) favours refinement/
  adaptive search against a finite dense grid, not a proven global
  optimum; outer forecast changes are small and algorithms known.
- ALL old experiment results use \`mu=0\` and are not evidence
  for the new mean-difference \`mu !=0\` working paper.

The user explicitly requests **no more Monte Carlo runs**.
Focus on interpretation, already saved tables and mathematical
arguments. For auditing the original model, reference SHA
\`21bd563146e04eb545cae56b46393d93a9d98212\`.

## Analysis-only frozen results, postprocess then curated Git upload

The university workstation has an original old \`formal8h\` SQLite
with **100,848/144,000 completed scenario-seed tasks**,
**65,877,504 model rows**, 50,424 numerical cases and
6,274,048 baseline rows. All 144 predeclared scenarios
are represented; 0 failures recorded. Original manifest
uses Git SHA \`21bd563146e04eb545cae56b46393d93a9d98212\`.

**User explicitly wants zero more Monte Carlo runs.**
Use only \`experiments/smoothness_cv/finalize_frozen_study.py\`
(which can also finalize an existing \`.sqlite.incomplete\`
Windows backup). Its main engine
\`analyze_frozen_compact.py\` reads the huge SQLite
once in primary-key order and aggregates seed-level
matched P1/P2 methods with honest inferential units.
\`plot_frozen_compact.py\` creates four charts and
\`REPORT_BRIEF.md\` from ACTUAL stored metrics, no
series regeneration. New tests
\`tests/test_analyze_frozen_compact.py\` and
\`tests/test_recover_campaign.py\` should pass
before running it.

Curated small GitHub sharing:
\`python -m experiments.smoothness_cv.publish_frozen_review
--report-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact --push\`.
The publisher refuses large SQLite/raw data, unknown
changes/staged items or >32MiB allowed files.
Only after GitHub review of the actual compact reports
may scientific conclusions be formulated. Current
evidence remains time-truncated/exploratory.

## Historical CUDA data recovery — DO NOT RESTART

A user's university workstation ran a long
\`--preset formal8h --backend cuda\` Monte Carlo campaign.
After shutdown / Git changes, re-running the same command
reported \`Existing manifest has a different design/code
version\`. This occurs because the manifest fingerprint
includes \`git_revision\`; it does **not** prove data
are lost, and \`_checked_manifest\` stops before
Monte Carlo iterations start.

User expressly requests **NO MORE SIMULATIONS**: inspect
and recover existing committed results ONLY.

Original expected path:
\`results/smoothness_cv/joint_formal_8h_v1/outcomes.sqlite\`
and its \`manifest.json\`; historical total exact count
must be measured, not inferred from progress logs.
Use \`experiments/smoothness_cv/recover_campaign.py\`
with \`--run-dir\` and a NEW outside \`--snapshot-dir\`.
It opens the original WAL-backed SQLite in read-only
mode, counts atomic \`completed\`, produces a
SQLite-online-backup snapshot and copies unchanged
manifest. On the snapshot, the joint analyzer's
\`--allow-partial\` permits retrospective results
without matching current git_revision. Do NOT edit
the original manifest, run a new campaign or
silently substitute a new directory for it.

See [recovery guide](experiments/smoothness_cv/CAMPAIGN_README.md).

## Top-priority NEW working paper (2026-10-11)

A fourth working paper has been created:
[Trend Simulation and Mean-Difference Forecasting](working_papers/Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting/README.md).
**It is currently the lead research hypothesis.** Its own
[notes](working_papers/Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting/notes/INDEX.md)
track derivations, assumptions and simulation proposals.
Obsidian [Guerrero derivation](notes/conceptos/06-Media-de-diferencias-Guerrero.md)
and [forecast-CV profiling](notes/conceptos/07-Perfilamiento-de-mu-en-CV.md)
are detailed step-by-step backgrounds.

Prior three papers' code/results ARE NOT DELETED.
The university's already-running μ=0 CUDA simulation
does not evaluate the new extension. This new research line adds
a separate \`src/trend_estimation/forecasting/mean_difference_cv.py\`
API (zero / Guerrero plug-in / analytically profiled common μ),
new tests and a separate \`experiments/mean_difference_forecasting/\`
pilot. No new dataset/result has yet been tested/confirmed by
this editing agent. Manuscript LaTeX is an empty scaffold,
not a paper ready for journal submission.

## Newly added fourth canonical Streamlit app

\`streamlit run apps/mean_difference_forecasting.py\`
now opens the new paper's exploratory interface, sharing
the source-level CV-profile selector. It contrasts μ=0,
per-window Guerrero μ and historical forecast-profiled μ(S),
shows F(S) and true (synthetic) past/future trend diagnostics,
and exports reproducible data. The interface is not a
publication experiment; do not use synthetic latent tau
or reserved external test to choose parameters.
Fourth app unit checks live in
\`tests/test_current_paper_apps.py\`.


## Notes before manuscript — mandatory handoff

**New 2026-10-09:** publication writing proceeds **from complete
Markdown research notes to LaTeX only after proof and evidence gates**.
See [NOTES_TO_MANUSCRIPT.md](working_papers/NOTES_TO_MANUSCRIPT.md).
Each active paper now has three canonical notes inside \`notes/\`:
\`RESEARCH_NOTEBOOK.md\` (delimitation, algorithm, motivation),
\`PROOF_LEDGER.md\` (proofs, assumptions, known vs open statements),
and \`SIMULATION_ATLAS.md\` (DGPs, true tau vs noisy y and estimated
trends, forecast steps, planned figures/tables).
Read the relevant paper's index/README before coding or drafting.
None of the figures or new 528-cell results described as plans should
be silently presented as already generated.

## Formal three-paper eight-hour research screen

**New common scientific protocol:**
[JOINT_FORMAL_8H_PROTOCOL.md](working_papers/JOINT_FORMAL_8H_PROTOCOL.md).
The \`formal8h\` DGP preset contains **144 interpretable factorial
cells** including the original 2^4 Cortés-Toto generating laws
and three noise amplitudes for the same latent B trend.
A \`--time-budget-hours 8\` soft stop preserves SQLite and
round-robins scenario/seed waves; incomplete results are
EXPLORATORY. Optional \`--with-baselines\` saves naive/drift/
seasonal-naive/linear OLS forecasts on the same untouched
outer origins. \`--numerical-every 8\` measures Brent
multibracket and analytic adaptive root searches on a
predeclared subsample of the very same weighted F surfaces,
including the effect of chosen S on observed future and
true latent past/future trend; \`--sturm-once\` executes a
tiny exact rational fixture only once. No repeated CPU/GPU
benchmark in the formal simulation.

Run and report through
[CAMPAIGN_README.md](experiments/smoothness_cv/CAMPAIGN_README.md).
This new software has NOT been run on the university machine
and no scientific superiority claims are established.

## Research objective and status



Three independent active papers:

1. [Paper 1 — Smoothness Cross Validation](working_papers/Working%20Paper%20-%20Smoothness%20Cross%20Validation/):
   choose S to minimize a predeclared **weighted aggregate of completed
   h-step rolling-origin forecast-MSE curves F**. Uniform all-origin
   mean is the original baseline. Global argmin of latest complete
   weighted F; **no tracking**.
2. [Paper 2 — Dynamic Branch Selection](working_papers/Working%20Paper%20-%20Dynamic%20Branch%20Selection/):
   for each fixed weighting method, difference order and horizon,
   detect and match **all grid-candidate local minima across
   consecutive weighted F functions**; choose an active branch using
   completed history, then map the branch to operational S (initial
   policy: mean of last three local S minima). **No internal Val2**.
3. [Paper 3 — Numerical Methods](working_papers/Working%20Paper%20-%20Numerical%20Methods/):
   analytic derivatives and numerical recovery of stationary/local
   minima and exact endpoints for **one fixed F**; adaptive sampling
   and limited rational/Sturm examples. No cross-origin branch
   tracking is needed.

The statistical definitions, normalizations, theoretical results,
**priority of theoretical contribution over performance engineering**
and exact claim boundaries are in
[THEORETICAL_CONTRIBUTIONS.md](working_papers/THEORETICAL_CONTRIBUTIONS.md).
Cortés-Toto/Guerrero-type PLS trace smoothness and its spectral
formulation are established; **do not imply we invented them**.
The project studies a horizon-matched integration of existing
techniques and specific theoretical/statistical implications.

## Canonical Streamlit apps — do not confuse with legacy

- \`streamlit run apps/pooled_forecast_cv.py\` — actual Paper 1 pooled
  selection and temporal weighting on completed F, including the
  original equal-weight baseline.
- \`streamlit run apps/dynamic_branch_cv.py\` — **new** weighted-F
  temporal branch tracking, separate from the historic two-stage
  method.
- \`streamlit run apps/numerical_methods.py\` — analytic derivatives,
  stationary candidate search, exact S=0/1 endpoints, one F.

[apps/README.md](apps/README.md) explains inputs, plots, and data
leakage boundaries. **Legacy:** \`apps/smoothness_lab.py\`,
\`apps/smoothness_lab_advanced.py\` and earlier numerical-tracks
dashboard show Val1/Val2 workflows / frozen files, not current Paper 2.
Before 2026-10-09 the dynamic launcher inadvertently pointed to
the old app; its implementation has been replaced. Preserve old
tests/checkpoints without rebranding them as contemporary results.

## Shared mathematical and evaluation invariants

\[
H_\lambda=(I+\lambda D_d^\top D_d)^{-1}
=U\,\mathrm{diag}((1+\lambda\delta_j)^{-1})U^\top,\qquad
S=\frac{L-\mathrm{tr}H_\lambda}{L-d}\in[0,1].
\]
S=1 is exact degree-(d-1) polynomial projector limit. For
horizon h at historical origin t,
\(\ell_t(S)=\|y_{t+1:t+h}-G_{d,h}H(S)y_{t-L+1:t}\|^2/h\),
and a historical future must satisfy \(t+h\le T\) to be used
in selecting at T. Method m weights **functions**, not S. After
selection refit on last L observations; score genuinely unseen
outer h steps only afterward.

The common protocol:
[WEIGHTED_SURFACE_PROTOCOL.md](working_papers/WEIGHTED_SURFACE_PROTOCOL.md).
Experimental/metric protocol:
[SIMULATION_EVALUATION_PROTOCOL.md](working_papers/SIMULATION_EVALUATION_PROTOCOL.md).

### Formal CUDA production path — current implementation, not measured campaign

\`experiments/smoothness_cv/cuda_simulation.py\` and
\`run_simulation_campaign.py --backend cuda\` now batch the REAL
chronological PLS forecast-loss matrices for many seeds in
float32 CUDA. All paper methods share the same selection code.
Default is **no per-batch CPU/GPU comparison** (\`--gpu-verify 0\`);
a single smoke precision audit uses \`--gpu-verify 2\`.
The old loss-kernel benchmark remains a historical engineering
measurement, not a procedure used repeatedly during formal runs.

New Study D has 720 rare-shape/noise/seasonal factorial
cells, and \`--preset mega\` combines all 528 original
cells with D = 1,248 cells (124,800 scenario–seed
instances with 100 seeds). The new CUDA code and added stress
protocol are not yet tested on the university GPU, nor are
final results recorded; execute smoke/pilot first, and retain
the independent latent-trend / outer-forecast evaluation contract.

## Current implementation and unfinished scientific work

New implementation exists:
\`experiments/smoothness_cv/weighted_surface_study.py\`;
simulation DGPs, 32-worker resumable SQLite Monte Carlo runner,
paired evaluation, factor reports and case inspection in
\`experiments/smoothness_cv/\`.
**The 528-cell extensive campaign is prepared but NOT yet reported
as run or independently verified**, nor are its outcomes available in
these commits. Historical CP01–CP08 results remain frozen and come
from partially different methods. Manuscript LaTeX files remain
working drafts predating the new framework; do not label them
submission-ready revisions.

The university workstation has 32 logical CPU processors and was
described as having an RTX 4500 Ada GPU. User executed a float32
CPU/GPU spectral PLS **loss kernel** benchmark, reporting
transfer-inclusive GPU acceleration 2.06x, 17.83x, 45.60x, 9.83x
for batch sizes 1, 32, 256, 1024 respectively. **Unverified here**:
numerical error/selected-S differences, hardware JSON,
reproducibility of the timings and total-campaign speedup.
One GPU process batching independent series is a possible future
design; 32 independent CUDA processes are not the intended default.
These timings can support a cautious computational subsection
*only after further checks*. Theoretical novelty takes precedence.

## Immediate next actions

1. Run tests for the current three apps and the weighted/simulation
   engines in the user's Conda environment; fix failures before a
   large campaign.
2. Review/verify theoretical claims, derive propositions or
   counterexamples and complete a closest-literature audit.
3. Validate root/minimum detection resolution and the branch
   correspondence scheme; preserve negative cases.
4. Run source-faithful full-N 2^4 factorial separately from
   rolling-origin forecast extension; run pilot, then interpretable
   extensive DGP benchmark with truly untouched testing.
5. Only then revise manuscript theory/results. Automated CI must
   remain lightweight; heavy simulations and PDF builds manual.

**Do not promise background execution from a chat.** This handoff
documents code and protocols, not autonomous ongoing GPU jobs.
