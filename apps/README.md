# Interactive research applications — exactly one canonical app per paper

**2026-10-09.** This directory intentionally contains three **canonical**
Streamlit entrypoints, one for each independent active working paper.
Two older dashboard scripts remain **legacy** for historical reproduction.
All apps are exploratory interfaces over real \`src/\` and
\`experiments/\` methods, **not a separate mathematical implementation**.

Read [AGENTS.md](../AGENTS.md) and the
[theory-first charter](../working_papers/THEORETICAL_CONTRIBUTIONS.md)
before changing an app.

## Canonical apps

| Paper | Run from repository root | Scientific object | Current features |
| --- | --- | --- | --- |
| 1 — Smoothness Cross Validation | \`streamlit run apps/pooled_forecast_cv.py\` | Historical raw forecast loss curves and their **weighted average F**; select **global minimum** | Original equal-weight pooled CV + weighted all/last-K uniform/linear/exponential, spectral H, S/EDF, historical fold heatmap, forecast and CSV/JSON exports |
| 2 — Dynamic Branch Selection | \`streamlit run apps/dynamic_branch_cv.py\` | **Local minima** of method-specific weighted historical F, matched into chronological branches | Independent m, fixed d,L,h, radius/support/K controls, one-to-one branch matching, mean-last-K S **after** branch choice, forecast and branch/weighted-F matrix exports |
| 3 — Numerical Methods | \`streamlit run apps/numerical_methods.py\` | Stationary points **of one fixed F(S)**, derivatives and exact endpoints | Adaptive derivative root brackets, F and first derivative plots, stationary candidate classifications, exact 0/1 checks, tabular exports, mathematical warnings |

All three support interactive synthetic input via a restricted numeric
expression and additional source modes; Paper 1 provides synthetic,
Yahoo Finance or CSV. Papers 2/3 also offer the original linear and
Beta-mixture Cortés-Toto DGPs directly. Paper 1 includes those within
its existing synthetic presets. Yahoo download requires network access
and optional \`yfinance\`.

Install from repository root:

~~~powershell
conda activate trend-estimation
python -m pip install -e ".[dashboard,finance,dev]"
streamlit run apps/pooled_forecast_cv.py
~~~

The user prefers Conda for large binary frameworks: optional **GPU
PyTorch is separately installed via Conda**, and is NOT required to run
Streamlit pages. Its benchmark belongs in
[CAMPAIGN_README.md](../experiments/smoothness_cv/CAMPAIGN_README.md),
not in the core statistical decision.

## What does each "F" mean?

Raw **completed** historical h-step loss at origin t:
\[
\ell_t(S)=\frac1h\|y_{t+1:t+h}
-G_{d,h}H(S)y_{t-L+1:t}\|^2,\qquad t+h\le T.
\]
Here \`d\` and \`L\` select the **PLS smoother** and \`h\` selects
the operational forecast **horizon**, all fixed for a comparison.
\`m\` names a historical **weighting of losses**, not of S:
\[
F_r^{(m)}(S)=
\frac{\sum_{q\in I_m(r)}w_{r,q}^{(m)}\ell_{t_q}(S)}
{\sum_{q\in I_m(r)}w_{r,q}^{(m)}}.
\]

Paper 1: \`argmin_S F_M^(m)(S)\`. **No temporal matching of local minima.**

Paper 2: for *each* method m, find **all grid-detected candidate local
minima** of \`F_r^(m)\`, link eligible adjacent minima with one-to-one
matching, score/select active branch based on historical completed F,
and apply operational S (initially mean of its last three minima).
**Never put mean-of-three S INSIDE F.** No internal Val2. Outer test
only after the smoothing choice.

Paper 3: fix a **single** F, compute derivative w.r.t lambda analytically
and transform to derivative w.r.t normalized S; examine adaptive
stationary search and endpoints. No temporal branch selection is needed.
The finite numerical sampler is not an exhaustive-root theorem.

## Streamlit input/output boundaries

- **Synthetic:** generated latent trend is allowed only in display
  and in explicitly labelled oracle-only simulation diagnostics. It
  cannot be supplied to a real-data selector.
- **Yahoo/CSV:** these are observed series. Financial prices/returns
  need appropriate unit/transform declarations before interpretation.
- **Holdout:** a reserved final h observations must not affect any
  historical selection or refit. An outer score exists only after
  forecasting those h points.
- **Full-series smooth:** retrospective use of all observations,
  including test, is descriptive and cannot be reported as outer
  forecast accuracy.
- **Spectral smoother:** \`H=Udiag((1+lambda delta)^(-1))U.T\`.
  Scalar \`S=(L-tr(H))/(L-d)\`, not \`H\` itself. Exact S=1 means
  polynomial null-space projection. The heatmap of H represents
  observation weights, while \`F\` heatmap represents validation MSE.
  Do not interchange them.
- **Downloads:** include the actual method/d/L/h, applied F weighting,
  selected S, and whether a matrix is grid-approximate or from a
  certified method.
- **Method selection:** a user inspecting many configurations and
  picking one based on the outer test has contaminated any independent
  generalization claim. One case/app plot is educational, not a paper
  benchmark.

## Historical interfaces — do NOT expose as the new method

- \`apps/smoothness_lab.py\`: old branch-rule / Val1/Val2 workflow.
- \`apps/smoothness_lab_advanced.py\`: an older advanced Val1/Val2 app.
- \`experiments/numerical_smoothness_selection/dashboard_tracked_minima.py\`:
  visualization of historical frozen files with older validation
  semantics (not the current numerical-paper canonical app).

**Do not alias \`apps/dynamic_branch_cv.py\` to either historical app.**
Preserve old scripts and their tests for reproducibility but clearly
label them "legacy" in navigation, comments and manuals.

## Code ownership

- Source of the current weighted-F and branch algorithm:
  \`experiments/smoothness_cv/weighted_surface_study.py\`.
- Original Paper 1 pooled infrastructure:
  \`experiments/smoothness_cv/pooled_lab.py\`.
- Numerical roots + derivative formulas:
  \`src/trend_estimation/selection/smoothness_numerical.py\` and
  \`src/trend_estimation/forecasting/objectives.py\`.
- Per-paper apps above should call these functions; do not change
  mathematical definitions inside plotting functions.
- New app regression tests:
  \`tests/test_current_paper_apps.py\` (compile and contract),
  plus numerical/rolling regression tests.
- The \`manuscript/main.tex\` and \`main.tex\` files are dated drafts.
  Updating an app does not imply the manuscript was updated.

## Immediate next milestones

1. Test all three apps using the actual \`trend-estimation\` Conda
   environment, and fix any Streamlit/Yahoo optional-dependency regressions.
2. Add repeated **external** rolling-origin evaluation to interactive
   app previews; the single holdout is not publication evidence.
3. Explore estimator geometry (nonuniqueness, multiple extrema and
   branch persistence), record proof attempts and counterexamples.
4. Run source-faithful 2^4 replication and then the large factorial
   DGP suite with matched forecasts and latent trend metrics.
5. If reporting GPU acceleration, verify the benchmark CSV's numerical
   error/selected-S differences, measure real end-to-end batches, and
   report hardware and float32 arithmetic. Performance is secondary
   to the theoretical claims.
