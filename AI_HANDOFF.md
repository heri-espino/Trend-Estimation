# AI Handoff

Last updated: 2026-10-06

## Highest-priority instruction

There are exactly **two active papers** in this repository:

1. `paper_smoothness-cv/`
2. `paper_numerical-methods/`

Do not start or continue research work in other paper directories unless the user explicitly reactivates them.

## Paper A — dynamic smoothness-CV

Primary target: **Journal of Forecasting**.

The central research direction is no longer only the pooled selector

\[
\widehat S^{\mathrm{pool}}_{T,h}
\in
\arg\min_S F^{\mathrm{pool}}_{T,h}(S).
\]

That pooled criterion remains an important baseline.

The central object is now the temporal evolution of the **local minima** of origin-specific forecast-loss surfaces:

\[
\mathcal M_t
=
\{S_{1,t},\ldots,S_{K_t,t}\}.
\]

Nearby minima are tracked through time as data-driven branches using one-to-one continuation under

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon.
\]

Each branch stores at least

\[
V_j
=
[S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t}]_t,
\]

where \(\ell^{(1)}\) is Validation-1 forecast loss and \(\ell^{(2)}\) is Validation-2 loss after refitting through Validation 1.

The forecasting decision is explicitly two-stage:

\[
\widehat j_T
=
\psi(V_1,\ldots,V_J),
\qquad
\widehat S_T
=
\phi(V_{\widehat j_T}).
\]

The first dynamic \(\phi\) methods to compare are:

- newest/last tracked local minimum;
- recent mean;
- recent median;
- pure recency-weighted mean;
- Validation-2 weighted mean;
- recency + Validation-2 weighted mean.

A direct forecast of the smoothness trajectory may be studied later.

Read first:

1. `paper_smoothness-cv/AI_HANDOFF.md`
2. `paper_smoothness-cv/notes/dynamic_tracked_smoothness.md`
3. `paper_smoothness-cv/notes/validation_semantics.md`
4. `paper_smoothness-cv/notes/research_objective.md`

### Non-negotiable refit rule

Validation folds and branch histories select the hyperparameter; they do not supply the final trend fit.

After \(\widehat S_T\) is chosen, discard temporary historical fits and refit on the newest full window:

\[
\widehat\tau_T
=
H_{\lambda(\widehat S_T)}
y_{T-L+1:T}.
\]

Then forecast the untouched future block.

We may average **losses** or **smoothness values** when a declared \(\phi\) rule requires it. We never average historical fitted trends.

## Paper B — numerical methods

This paper owns two numerical layers:

1. recover all relevant local minima of each multimodal \(F_t(S)\);
2. track/correspond those minima across adjacent chronological surfaces.

The frozen per-surface method remains:

1. adaptive evaluation in normalized \(S\);
2. analytic derivatives;
3. adaptive interval subdivision;
4. derivative-root bracketing;
5. Brent refinement;
6. stationary-point classification;
7. exact endpoint comparison.

The temporal baseline is one-to-one nearest-neighbor matching under `track_epsilon`.

Do not confuse:

- `candidate_spacing`: within-surface post-discovery separation;
- `track_epsilon`: across-time branch continuation radius.

Read first:

1. `paper_numerical-methods/AI_HANDOFF.md`
2. `paper_numerical-methods/notes/research_objective.md`
3. `paper_numerical-methods/notes/temporal_minima_tracking.md`
4. `paper_numerical-methods/notes/decisions.md`

## Ownership boundary

`paper_numerical-methods/` returns local minima and branch identities.

`paper_smoothness-cv/` decides how a tracked branch is scored and converted into the current smoothness through \(\psi\) and \(\phi\), and evaluates forecasting performance.

Do not merge these contributions.

## Frozen numerical evidence

The existing per-surface solver has frozen empirical evidence:

- adversarial: 240/240 relevant known minima/boundary optima;
- synthetic: 2105/2105 dense-reference interior minima across 1920 surfaces;
- financial geometry stress: 473/473 dense-reference interior minima across 384 surfaces;
- mean evaluation fractions about 1.57% synthetic and 1.84% financial.

These results validate the tested **per-surface search**, not yet the temporal branch-matching layer.

## Repository policy

Reusable algorithms live in `src/trend_estimation/`. Heavy paper builds and large experiments remain manual-only.

## Immediate execution state

CP03 pooled forecast-CV paper run is committed. The active next experiment is
`paper_smoothness-cv/checkpoints/CP04_DYNAMIC_BRANCH_RULES.md`.

CP04 compares multiple `phi(V_j)` rules on repeated development-only outer
tests while reserving the newest four blocks of every tracked real series for
a later one-shot confirmation. Do not run or inspect that confirmation region
until the development rule is frozen.


## CP04 confirmation now frozen

The dynamic-rule development stage is complete. The primary rule is frozen as
`recency_hl3`: exponential recency weighting of the selected branch with a
three-origin half-life.

Development geometric RMSFE ratio:
- vs newest-minimum `last`: 0.7989;
- vs pooled forecast-CV: 1.0491.

The four reserved latest blocks per real series remain the one-shot
confirmation sample. The confirmation run may evaluate only
`recency_hl3`, `last`, and `pooled_cv_same_config` under the frozen
tracking specification.


## Immediate next run — CP05

CP04 confirmation is complete and audited. Frozen `recency_hl3` achieved
geometric RMSE ratio 0.6920 vs pooled forecast-CV and 0.8137 vs `last` on
the 16 reserved confirmation decisions.

The next run is CP05, an external 64-series financial panel selected
mechanically from the frozen Yahoo snapshot. AAPL, SPY, and BTC-USD are
excluded because they were used in CP04. No CP05 tuning is allowed.

Run smoke first, then the full panel; see
`paper_smoothness-cv/checkpoints/CP05_EXTERNAL_PANEL.md`.


## CP05 result and immediate CP06

The frozen 64-series external financial panel is complete.

`recency_hl3` did not beat pooled forecast-CV overall:
- geometric RMSE ratio = **1.6421**.

It did strongly beat the newest tracked minimum:
- geometric RMSE ratio = **0.5246**.

The broad-panel failure against pooled CV is concentrated in high-order native
continuation, especially d=4 cubic extrapolation. This is now a boundary of
the method, not something to hide or retune away.

The next active experiment is
`paper_smoothness-cv/checkpoints/CP06_ORDER_STABILITY.md`.
It compares nested order sets on earlier historical outer blocks that precede
all CP05 external-test blocks. It is a post-hoc mechanism study, not a new
confirmation test.


## CP07 result and CP08 trajectory forecasting

CP07 fixed d=2 and prospectively tested the frozen backward-looking recency
average under stationary and changing latent roughness.

Results:
- all mechanisms: dynamic / pooled gRMSE = 1.037;
- changing roughness: 1.028;
- stationary roughness: 1.056;
- dynamic / newest-minimum = 0.945 overall.

Therefore recency averaging stabilizes the newest tracked minimum but does not
outperform pooled forecast-CV even when roughness changes.

CP08 now demonstrates a different, forward-looking use of the branch matrix:
forecast the smoothness trajectory itself. Candidate rules include recent
linear extrapolation, exponentially weighted linear extrapolation, and
exponentially weighted branch-increment extrapolation.

The paper's objective is **not** to identify one universally best way to choose
\(S\). The central contribution is that tracking local-minimum branches creates
a reusable state \(V_j\) from which many legitimate decision rules
\(\phi(V_j)\) can be constructed and studied. CP08 is therefore a
rule-family demonstration, not a tuning/confirmation tournament.


## CP08 complete — rule-family illustration

The CP08 paper preset completed 1,200 simulated scenarios and 9,600 outer
decisions. It demonstrates that a tracked branch state supports multiple
maps from V_j to a current smoothness value S, including moving averages,
weighted averages, extrapolation of trends, and extrapolation of increments.

The purpose is NOT to discover one best phi. Its measured forecast ratios
and clipping rates characterize different rule behavior. All tested CP08
rules are above one relative to pooled CV on aggregate geometric log-RMSE,
so no unconditional forecast-superiority claim is supported.

Next: reproducible CP08 figures, manuscript synthesis, explicit claim limits.

## Manuscript integration after CP08

The frozen CP08 run has three committed figure pairs (PDF/PNG) explaining
selected S across a fixed scenario, how often raw extrapolations need
clipping to [0,1], and predictive-error behavior by roughness regime.

The manuscript now has a completed `07_empirical_evidence.tex` integrating
CP03--CP08 evidence and includes all three figures. Its abstract,
evaluation protocol, scope, introduction, and conclusion were updated to
present the framework as a **family of branch-based smoothness decisions**
without claiming superiority to pooled forecast-CV.

Run `python paper_smoothness-cv/build.py --check` and then
`python paper_smoothness-cv/build.py` on a machine with XeLaTeX and BibTeX,
inspect page layout, commit the generated PDF, and push.

## Numerical-methods paper update: tracking evidence and benchmark

The numerical manuscript (`paper_numerical-methods/main.tex`) has been
updated without changing the frozen per-surface optimizer. It now contains
a separate temporal-correspondence formulation, an explicit greedy matching
counterexample, and a figure and descriptive tracking counts from the
frozen four-series run (924 matched and 468 missing rows among 1392
initialized branch-origin states). These are not ground-truth identity
success rates.

A controlled CP05 benchmark has been implemented at
`experiments/numerical_smoothness_selection/run_tracking_correspondence_benchmark.py`
to compare greedy with exact pairwise max-cardinality/minimum-displacement
matching on known minima and 5 path mechanisms, including crossings and
birth/death. The benchmark has not yet been run. It conditions each
step on known previous labels, not cumulative tracking.

Next: run smoke and paper presets, commit their reports, inspect the
outcomes, then add measured tracking comparisons to the manuscript.
Rebuild numerical PDF with `paper_numerical-methods/build-paper.bat`.

 
## Five-panel forecasting workflow figure

The first (`paper_smoothness-cv`) manuscript now references a new full-width
five-horizontal-panel tutorial figure. Its script is
`experiments/smoothness_cv/make_workflow_tutorial_figure.py`.
It uses the frozen CP07 synthetic example (seed 100, switch_to_rough,
noise_sd 0.01, outer number 8), and explicitly keeps final Validation-1
loss distinct from the untouched test loss.

Output is committed by the user after running the generator:
`paper_smoothness-cv/manuscript/figures/fig_workflow_tutorial.pdf`,
`.png`, and `.json`. The manuscript and `build.py` are already updated
to include/check the PDF. Tests cover index chronology.
Run generator before `python paper_smoothness-cv/build.py --check`,
then compile and visually inspect the resulting Wiley PDF.


## Workflow figure audit: compiled PDF still needs update

At 2026-10-07 latest user push 88bf9065 added the five-panel workflow
figure as PDF/PNG/JSON. The figure was visually inspected in chat.
Minor Panel A label overlap was fixed in code. The main forecasting
manuscript PDF was last committed in 81a2030, before the tutorial
figure was generated; its newer compilation is unverified.

Run `paper_smoothness-cv/build-workflow-paper.ps1` via PowerShell after
pulling. This is a fail-fast test/generate/preflight/compile workflow
that refuses to report success if the compiled PDF is missing/stale.
Then commit and push the updated figure and the main manuscript PDF.
