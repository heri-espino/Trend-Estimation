# AI Handoff

Last updated: 2026-10-05

## Highest-priority instruction

The repository now has TWO linked active methodological papers. Do not merge their contributions back together.

### Paper A — paper_smoothness-cv/

Question: **what smoothness criterion should be optimized?**

\[
S^\star_{d,L,h}\in\arg\min_{S\in[0,1]}F_{d,L,h}(S),
\]
where \(F\) is chronological rolling future-block forecast MSE.

This paper is conceptually closest to Guerrero's controlled-smoothness PLS framework. Guerrero lets the analyst specify a smoothness percentage and maps it to a penalty. This paper asks whether that percentage can instead be selected endogenously from future forecast performance.

Hart (1994) must be cited as an important predictive-smoothing precedent, but do not present Hart's kernel/TSCV method as the same problem.

Paper A may use a dense smoothness grid. Efficient root finding is not its contribution.

Read first:
1. paper_smoothness-cv/README.md
2. paper_smoothness-cv/AI_HANDOFF.md
3. paper_smoothness-cv/notes/research_objective.md
4. paper_smoothness-cv/notes/literature_positioning.md
5. paper_smoothness-cv/notes/roadmap.md

### Paper B — paper_numerical-methods/

Question: **given \(F(S)\), how do we solve all relevant minima/global optimum efficiently and reliably?**

Current production design:
1. sparse/adaptive evaluation in \(S\);
2. derivative/curvature diagnostics;
3. bracket roots of \(F'(S)\);
4. Brent refinement;
5. classify stationary points;
6. compare local minima and exact endpoints.

Brent is NOT a global-discovery algorithm.

The rational/Sturm direction is stronger but not yet production-certified. The current Sturm mini-check is evidence of feasibility only.

Read first:
1. paper_numerical-methods/README.md
2. paper_numerical-methods/AI_HANDOFF.md
3. paper_numerical-methods/notes/research_objective.md
4. paper_numerical-methods/notes/paper_split_2026-10-05.md
5. paper_numerical-methods/notes/results.md
6. paper_numerical-methods/notes/sturm_minicheck.md

## Shared equations

\[
H_\lambda=(I+\lambda Q)^{-1},\quad Q=D_d^\top D_d,\quad
\widehat\tau_\lambda=H_\lambda y.
\]

\[
S(\lambda)=1-\frac1{N-d}\sum_{\delta_j>0}\frac1{1+\lambda\delta_j}.
\]

\[
\widehat z_T(\lambda)=G_{d,h}H_\lambda x_T,\qquad
F(S)=f(\lambda(S)).
\]

\[
H'=-HQH,\qquad H''=2HQHQH.
\]

\[
F'(S)=\frac{f'(\lambda)}{S'(\lambda)}.
\]

\[
F''(S)=
\frac{f''(\lambda)}{[S'(\lambda)]^2}
-
\frac{f'(\lambda)S''(\lambda)}{[S'(\lambda)]^3}.
\]

## Frozen numerical evidence

- adversarial: 240/240 relevant known minima/boundary optima;
- synthetic: 2105/2105 dense-reference interior minima across 1920 surfaces;
- financial geometry stress: 473/473 dense-reference interior minima across 384 surfaces;
- mean evaluation fractions about 1.57% and 1.84% of dense references in synthetic and financial suites.

These are benchmark results, not a theorem.

## Legacy directory

paper_numerical-smoothness-selection/ is a historical pre-split snapshot. Do not add new work there. The complete snapshot was copied to paper_numerical-methods/.

## Stable experiment namespaces

Do not rename experiments/numerical_smoothness_selection/ or results/numerical_smoothness_selection/ casually. Tests, frozen metadata, manuscript paths, and reproducibility records depend on those names.

## Other papers

paper_forecast-optimal-smoothing/ is PARKED and owns adaptive joint \((d,L,S)\) selection.

paper_smoothness-recurrence/ is PARKED and owns applied model comparison/recurrence.

paper_statistical-properties-penalized-trend/ is DRAFTING as a linked theory paper. It owns fixed-smoother statistical foundations and, especially, post-selection properties of the forecast-selected estimator. Its novelty audit and theorem agenda are not yet frozen.

paper_bezier-trend/ is an IDEA / NOVELTY AUDIT PENDING. It studies Bernstein/Bézier control-space regularization and endpoint geometry for trend forecasting. Do not claim that Bézier smoothing, Bernstein regression, penalized Bézier fitting, P-spline forecasting, or financial Bézier filtering are new. Read its literature audit before implementing large experiments.

## Validation invariant

At origin \(T\), nothing after \(T\) may influence the fitted trend, hyperparameter choice, or forecast path. Future observations are revealed only for scoring.

## Repository policy

Reusable algorithms live in src/trend_estimation/. Heavy paper builds stay manual-only.
