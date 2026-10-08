# Trend Estimation

trend_estimation is a library-first research repository for finite-difference penalized trend estimation, forecasting, chronological validation, and smoothness selection.

## Research map

As of 2026-10-06, there are exactly **two active papers**.

### Paper A — Dynamic forecast-optimal smoothness

Directory: `paper_smoothness-cv/`

Primary target: **Journal of Forecasting**.

The pooled chronological selector remains a baseline,

\[
\widehat S^{\mathrm{pool}}_{T,h}
\in\arg\min_S F^{\mathrm{pool}}_{T,h}(S),
\]

but the central research object is now the sequence of local minima of
origin-specific forecast-loss surfaces,

\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\}.
\]

Nearby minima are tracked through time as data-driven branches. Each branch
stores smoothness, Validation-1 loss, and subsequent Validation-2 loss,

\[
V_j=[S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t}]_t.
\]

The forecasting decision is

\[
\widehat j_T=\psi(V_1,\ldots,V_J),
\qquad
\widehat S_T=\phi(V_{\widehat j_T}).
\]

Paper A owns branch scoring, branch selection, final smoothness rules, refitting,
and forecast evaluation.

### Paper B — Numerical recovery and tracking of minima

Directory: `paper_numerical-methods/`

Paper B owns:

1. recovery of all relevant local minima of each multimodal forecast-loss surface;
2. exact endpoint handling;
3. adaptive derivative-aware search and Brent refinement;
4. temporal correspondence of minima across adjacent surfaces.

The current temporal baseline is one-to-one matching under

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon_{\mathrm{track}}.
\]

Do not confuse `track_epsilon` with within-surface `candidate_spacing`.

Frozen evidence for the per-surface solver remains 240/240 adversarial relevant
optima, 2105/2105 synthetic reference minima, and 473/473 financial geometry
stress minima.

## Interactive smoothness laboratory

The primary **live** Streamlit app now lives at `apps/smoothness_lab.py`.
It does not replace the separate frozen-results viewer at
`experiments/numerical_smoothness_selection/dashboard_tracked_minima.py`.

Install and launch from the repository root:

~~~bash
python -m pip install -e ".[dashboard,finance]"
streamlit run apps/smoothness_lab.py
~~~

The app provides synthetic functions with reproducible additive noise (including
AR(1), heavy-tailed and heteroskedastic variants), Yahoo Finance multi-ticker
downloads, and CSV uploads. For price levels, select level, log level, indexed
level, simple returns or log returns. It exposes rolling-window order `d`,
window `L`, horizon `h`, branch tracking radius and CP08 `phi(V_j)` rules.

You can inspect the forecast **Validation-1 MSE** surface heatmap (origin by
smoothness), the final local minima, the per-branch
`V_j = [S, Validation-1 loss, Validation-2 loss]` histories, the
Validation-2 MSE for each tracked branch, and the smoothing matrix
`H_lambda=(I+lambda D_d.T D_d)^-1`. Selected and pooled trend continuations
are shown alongside each other; manual smoothness and trend-view modes are
available. CSV exports include downloaded observations, branches, loss
surfaces, and the matrix.

**Validation contract:** The final test block is never used to choose a
smoothness, track a branch, or fit a trend. Validation-1 finds local minima;
Validation-2 is scored only after a fresh fit through Validation-1. Branch
selection uses support and historical Validation-2 RMSE, then the chosen
`phi(V_j)` selects smoothness for a **fresh pre-test fit**. The final test may
be revealed separately as a diagnostic. A lack of final branch continuation
is explicitly labeled and falls back to a coarse pooled-CV grid.

**Interpretation:** This is an *exploratory interactive companion*, not a new
checkpoint, a reproduction of every frozen preset, or a finding of universal
superiority. For responsiveness, its default derivative-search depth is 5,
versus 8 in the frozen numerical experiments. The pooled baseline in this app
is grid-based; the frozen paper implementation remains authoritative for
published quantitative comparisons. Large order `d=3,4` can yield unstable
polynomial forecast extensions. The app does not modify CP03–CP08 outputs.

Run the targeted pure-engine tests with:

~~~bash
python -m pytest tests/test_live_smoothness_lab.py
~~~

### Other directories

Other paper directories are historical, parked, tutorial, or idea workspaces.
They are **not active research tracks**. Do not add new research work to them
unless the user explicitly reactivates one.

The legacy `paper_numerical-smoothness-selection/` directory is a historical
pre-split snapshot and must not receive new work.

## Canonical reading order for another AI agent

1. `AI_HANDOFF.md`
2. `RESEARCH_MAP.md`
3. `paper_smoothness-cv/AI_HANDOFF.md`
4. `paper_smoothness-cv/notes/dynamic_tracked_smoothness.md`
5. `paper_smoothness-cv/notes/validation_semantics.md`
6. `paper_numerical-methods/AI_HANDOFF.md`
7. `paper_numerical-methods/notes/temporal_minima_tracking.md`

## Stable implementation namespaces

Reusable methods remain under src/trend_estimation/.

For reproducibility, the existing experiment/result namespaces are intentionally not renamed yet:

- experiments/numerical_smoothness_selection/
- results/numerical_smoothness_selection/

The active Journal of Forecasting criterion paper now has its own checkpointed empirical pipeline under `experiments/smoothness_cv/`, with versioned outputs under `results/smoothness_cv/`.

Those names are historical implementation namespaces, not the current paper title.

## Install

~~~bash
conda env create -f environment.yml
conda activate trend-estimation
pip install -e .
pytest
~~~

## CI policy

Automatic CI stays lightweight. Paper/PDF compilation remains manual-only through workflow_dispatch.
