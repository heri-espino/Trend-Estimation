# AI handoff — current Trend-Estimation research workspace

**Updated 2026-10-09. Read [AGENTS.md](AGENTS.md) FIRST and
[theoretical charter](working_papers/THEORETICAL_CONTRIBUTIONS.md)
before interpreting any old code, manuscript or checkpoint.**

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
