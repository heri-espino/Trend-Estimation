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
