# Research notes index — forecast-optimal smoothness CV

**Updated 2026-10-08. This folder is the canonical living research record.** The current LaTeX manuscript is a dated working draft; it will be reconsidered **after** the algorithm and experiments are settled. Previous checkpoint outputs are preserved, not discarded.

## Read in this order

1. [Research objective](research_objective.md) — central question, hypotheses, and information boundary.
2. [Mathematical foundations](mathematical_foundations.md) — PLS eigendecomposition, \(S\), forecast operator, MSE, analytic derivatives, multimodality and computation.
3. [Validation semantics](validation_semantics.md) — what a historical pseudo-future is; tuning/outer-test separation; mandatory final refit.
4. [Claim boundaries](claim_boundaries.md) — what is known, evidenced, hypothesized, and not yet verified.
5. [Research log](research_log_2026-10.md) — previous directions and frozen checkpoint outcomes without treating them as future promises.
6. [Next experiments](next_experiments.md) — numerical correctness, speed, horizon matching, recovery/forecast targets, and tracking.
7. [Literature](literature_positioning.md) — closest related research and open originality questions.
8. [Manuscript outline](manuscript_outline.md) — proposed final CSSC article structure after the new results.
9. [Roadmap](roadmap.md) — executable phases and decision gates.
10. [Dynamic minima](dynamic_tracked_smoothness.md) — optional \(V_j,\psi,\phi\), not the central method.

Additional implementation guide:

- [Pooled-only Streamlit app](POOLED_APP.md) — independent visualization of every F, pooled F, validation matrix, CV controls, forecasts and exports.

Secondary/historical documents:

- [Old empirical plan](empirical_roadmap.md) — archived CP01–03 development design, superseded schedule.
- [Former Journal of Forecasting positioning](journal_of_forecasting_positioning.md) — historical venue analysis, not current editorial target.
- [AI handoff](../AI_HANDOFF.md) — short continuity guide for new assistants.
- [Checkpoint histories](../checkpoints/) — original complete experiment records and frozen evidence.
- [CSSC literature audit](../LITERATURE_AUDIT_2026-10.md) and [submission checklist](../SUBMISSION_READINESS_CSSC_2026-10.md) — literature and formatting records, not an instruction to submit now.

## One-paragraph research summary

Given a historical training window, smooth it by finite-difference PLS, use the monotone trace-based index \(S\in[0,1]\) as the parameter, continue the fitted terminal differences as an \(h\)-step future polynomial trend, and choose \(S\) by minimizing MSE over **previously completed historical future blocks**. Then refit at the current origin and forecast the genuinely unknown future. Understanding the eigenstructure of \(Q\), efficiently computing \(H(S)\) and its analytic derivatives, and handling all candidate minima are key numerical ingredients. Whether the **specific** method is novel, which root search to adopt, and how robustly it outperforms established alternatives remain active research questions.
