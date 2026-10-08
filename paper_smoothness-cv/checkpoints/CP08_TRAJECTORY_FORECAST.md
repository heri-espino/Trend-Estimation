> **RESEARCH STATUS UPDATE — 2026-10-08 (current; original checkpoint record preserved below).** The primary current statistical question is selection of normalized PLS smoothness (S\in[0,1]) by **chronological, horizon-matched future-block forecast MSE**, with an explicit polynomial continuation and mandatory final refit. The eigenstructure of the smoother, analytic derivatives, and reliable recovery of competing minima are central mathematical/numerical topics. The source of truth is [../notes/INDEX.md](../notes/INDEX.md), [../notes/mathematical_foundations.md](../notes/mathematical_foundations.md), and [../notes/research_log_2026-10.md](../notes/research_log_2026-10.md).
>
> **Archival status:** CP08 **has been completed** and is now an **optional/exploratory historical study** of tracked minimum branches, continuation-order stability, or maps (\phi(V_j)). The main pooled forecast-CV method does not require these branches. Preserve the mixed/negative comparisons with pooled CV and the original post-hoc/confirmation boundaries. Any “central method” or “next checkpoint” text below is historical, not the current program.

---

# Checkpoint 08 — Forecast the tracked smoothness trajectory

**Status: COMPLETE — illustrative rule-family comparison (1,200 scenarios / 9,600 outer decisions).**

CP07 showed that backward-looking recency averaging stabilizes the newest
tracked minimum but does not beat pooled forecast-CV. CP08 tests the forward-
looking extension that motivated the branch-matrix formulation: predict the
next smoothness value from the selected branch trajectory.

CP08 is a **method-family demonstration**. It uses fresh simulation seeds
`100..199` to show that the tracked branch matrix supports several coherent
ways to construct the next smoothness value. The purpose is not to select a
universally best `phi` rule.

## Fixed forecasting environment

- `d = 2`;
- `L = 120`;
- horizon `h = 20`;
- 8 non-overlapping outer tests;
- 30 historical paired Val1/Val2 origins;
- `track_epsilon = 0.10`;
- `candidate_spacing = 0.02`;
- at most 5 initial local-minimum branches;
- branch selection by persistence plus historical Val2 log-RMSE;
- same six roughness mechanisms and two observation-noise levels as CP07.

Thus the only new object is the branch-to-smoothness functional `phi`.

## Candidate forward-looking rules

Let the selected branch values, including the current final-Val1 minimum, be

\[
S_1,\ldots,S_T.
\]

CP08 compares:

1. `linear_k3`: OLS line through the last 3 branch values, extrapolated one
   branch step;
2. `linear_k5`: same using the last 5;
3. `linear_k10`: same using the last 10;
4. `ew_linear_hl3`: exponentially weighted linear trend using all available
   branch values with half-life 3;
5. `ew_linear_hl5`: same with half-life 5;
6. `delta_hl3`: current S plus an exponentially weighted mean of historical
   branch increments, half-life 3;
7. `delta_hl5`: same with half-life 5.

All extrapolated values are clipped to `[0,1]`. The raw un-clipped value and
whether clipping occurred are saved for diagnostics.

Baselines are:

- `recency_hl3` from CP04--CP07;
- `last`;
- `pooled_cv_same_config`.

## Interpretation

The rules above are examples of admissible branch-to-smoothness maps

\[
\widehat S_T=\phi(V_j).
\]

CP08 reports how differently these functionals behave, including their selected
smoothness values, clipping frequency, forecast loss, and distance to the
simulation-only oracle. Relative performance is informative about their
behavior, but the paper does **not** define a competition whose goal is to find
one universally best rule.

The contribution is the branch representation and the resulting design space:
once a persistent branch has been summarized in \(V_j\), many decision rules
can be constructed from the same information without changing the underlying
trend estimator or the numerical minimum-tracking layer.

Accordingly, CP08 has no winner-selection step and no follow-up confirmation
stage tied to a selected trajectory rule.

## Observed CP08 demonstration

Source run: `results/smoothness_cv/checkpoint_08/20261007T072243Z_paper_be492a8/`.

The paper preset completed 1,200 scenarios and 9,600 outer forecast decisions.
Each decision used the same tracked branch while applying alternative maps
from historical branch information to the current smoothness.

| Example functional | Geometric observed-log RMSE / pooled CV | Clip rate |
| --- | ---: | ---: |
| Recency mean, half-life 3 | 1.0409 | 0.0% |
| Exponentially weighted linear, half-life 5 | 1.0627 | 10.8% |
| Linear extrapolation, 10 values | 1.0790 | 18.4% |
| Weighted-increment extrapolation, half-life 3 | 1.1103 | 22.3% |

All seven extrapolative examples and the recency mean had overall geometric
ratios above one against pooled forecast-CV. They do not support a
forecast-superiority claim.

The rules nevertheless produce different selected smoothness values and
boundary-clipping frequencies while using the same tracked minimum branch.
This demonstrates the flexibility of the representation, not its universal
forecasting benefit.

Generate three figures (PDF and PNG) using:

~~~bash
python experiments/smoothness_cv/make_checkpoint_08_figures.py
~~~

Figures show ratios by stationary/changing mechanism, clipping rates, and one
fixed illustrative seed/roughness scenario comparing alternative smoothness
choices from the same branch history. The illustrative scenario is fixed in
the script rather than selected by performance.

CP08 is closed. The next phase is visualization, manuscript synthesis, and
precise limits of the forecasting claims—not more winner-selection rounds.
