# Proposed Study L — isolate numerical search from statistical smoothing selection

**Created 2026-10-19. Status: PROPOSED DESIGN ONLY. Not implemented or run by this checkpoint.** Must be reviewed/frozen before a manual comparison. This is not an extension of the executed 25-seed K.1 method table masquerading as new independent confirmation.

## 1. Scientific question and the necessary control

In [Study K.1](CORTES_TOTO_PAIRED_25_SEED_REPLAY_RESULTS_2026-10-19.md), the new `cv_joint` and old `existing__estimated_mu_fold_clean_pooled_loocv` minimize **the same mathematical joint-mean, observation-deletion score** at fixed lambda but differ in search algorithms. Their simulated latent-trend MSEs differ; that is an *effect on downstream reconstruction*, not a clean measurement of optimization quality.

**Primary question:** for one fixed statistical score on one fixed observed data pool, how often does a numerical solver find a lower score, at what computational cost, and how robust is it to search bounds and nearly flat/multimodal surfaces?

**Null/rival explanations:** (H0) the fixed CV surface is ordinarily unimodal and both solvers reach equivalent objective scores; (H1) some surfaces have multiple relevant minima or boundary solutions and a single local bounded search misses a better score; (H2) nominal score changes are numerical precision or incompatible budget effects. All are legitimate outcomes.

**Do not rank solvers by simulated true-trend MSE.** That is a secondary scientific consequence, not the objective each solver tries to minimize.

## 2. Mathematical object, fixed independently of solver

For comparable observed series `y_r`, fixed d and pooled common mean, with `p_t=choose(t,d)`, `T_lambda=Q(I+lambda Q)^(-1)`, `b=T_lambda p`, `k=p^T T_lambda p`, and `mu_hat=b^T ybar/k`, use

```math
e_{ri}^{(-i)}(\lambda)=\frac{(T_\lambda y_r)_i-b_i\widehat\mu_\lambda}
{(T_\lambda)_{ii}-b_i^2/(Rk)},
\qquad F_{\rm CV,joint}(\lambda)
=\frac{1}{RN}\sum_{r=1}^R\sum_{i=1}^N(e_{ri}^{(-i)}(\lambda))^2.
```

The held-out observation is excluded analytically through the full pooled hat diagonal. The score is **the same** for each solver arm. Test against direct deletion/refitting for small N and each d. Include exact `lambda=0` and `lambda=infinity` limits, handling the unidentifiable mu at `lambda=0` through its continuous fitted-trend/CV limit.

A separate **GCV** arm can use

```math
F_{\rm GCV,joint}(\lambda)
=\frac{\mathrm{RSS}(\lambda)/(RN)}
{[1-\mathrm{EDF}_{\mathrm{joint}}(\lambda)/(RN)]^2},
\qquad
\mathrm{EDF}_{\mathrm{joint}}
=R\mathrm{tr}(H_\lambda)+\lambda\frac{\|T_\lambda p\|_2^2}{p^T T_\lambda p}.
```

Never compare the *minimum CV score* with the *minimum GCV score* as if these have the same scale/objective. Compare algorithms **within one criterion at a time**. BIC based on unrestricted `log(RSS)` has no finite global minimizing lambda in this interpolating setting and is **excluded from primary solver rankings**; AICc has invalid domains near full EDF and should only be a secondary arm with explicit feasibility rules.

## 3. Actual current code paths must not be conflated

- `experiments/pooled_loocv_smoothness/cortes_optimality_criteria.py::choose(solver="bounded")` minimizes one score by SciPy bounded scalar minimization on log-lambda (plus admissible exact endpoints).
- The same `choose(solver="multibracket")` evaluates a finite **score grid** (41 scan values in the completed K.1 run) and Brent-refines brackets surrounding sampled score minima, plus endpoints.
- `experiments/pooled_loocv_smoothness/search.py::multibracket_brent` is a **different algorithm**, using a finite **derivative-sign scan** and root refinement, and currently takes the basic `PooledLOOCV` object, not necessarily the joint-mean score class. It cannot be presented as equivalent to the score-grid algorithm merely because both are named “multibracket.”
- `search.py::dense_reference` is a **finite reference**, not an exact global certificate. `sturm_exact.py` provides strictly restricted small rational-input exact-root isolation for supported score structures; do not silently apply the same tractability/guarantee to floating-point N=200 joint-mean cases.

Before running, implement one objective adapter and a unified method/result schema. If an analytic derivative for joint `mu` is introduced, derive and unit-test it against central differences in `log(lambda)` across typical, near-boundary and delicate high-order cases. Merely using finite differences to search sign flips gives no global certification.

## 4. Prospective design — paired datasets and controlled resources

**Primary same-sample comparisons:**
1. `bounded` single-start log-lambda scalar minimization.
2. `score_multibracket` with predeclared finite grid and local refinement.
3. `dense_grid` with an explicitly recorded larger number of points, labelled a *finite benchmark*.
4. Optional `derivative_multibracket` only once the exact **joint** derivative and all boundary cases are tested.
5. Optional restricted rational tiny-case root certificate only where symbolic assumptions are satisfied.

Proposed initial subset: same original Study J/K.1 observations for Gaussian iid and one heavy-tail regime; fixed d∈{1,2,4}, N∈{50,200}, observation SD∈{0.5,2}, nested R1/R3, `mu/sigma_epsilon=+1`, and the same 25 existing seeds in each selected stratum. This is a **paired numerical diagnostic/replay**, not new statistical replication. Once tests and diagnostics pass, enlarge the comparison to all previously saved J seed identities; do not needlessly launch a new huge Monte Carlo DGP. For `joint` mu, exact polynomial-shift equivariance means additional five mu shifts add no independent numerical evidence; verify the invariance once and state it explicitly.

**Fairness and budget reporting:** freeze log-lambda domain `[-20,35]`, exact endpoint checks, stopping tolerances, evaluation budgets, scipy/BLAS environment and precision. Compare at multiple fixed *cost tiers*, such as small/medium/large, rather than pretending 41 grid evaluations plus many Brent refinements costs the same as one bounded call. Track separately: score calls, derivative calls, linear algebra/factorization operations, wall time and numerical failures; compare time only on the same hardware with repeat timing and initialization/warm-cache effects documented.

**Primary outputs per data pool and criterion:**
- unique stratum, seed, R, d, N, noise distribution and input checksum/source reference;
- score function identity/version and a fixed data/score equality test;
- solver, bounds, scan/grid size, requested tolerance, actual score/derivative evaluations, wall clock;
- selected lambda (allowing 0 and infinity), normalized nominal S, boundary classification;
- **the same independently re-evaluated objective value** `F(estimated_lambda)` for every solver;
- paired score gaps `F(method)-min_solvers F` (within tested algorithms, not certified global), and gap to dense finite grid;
- numerical ties within declared absolute+relative tolerance, apparent multimodality/root diagnostics, rejected/unstable candidates;
- **secondary only:** realized latent reconstruction MSE, labelled ex-post to prevent winner selection by oracle true tau.

**Analysis:** paired per-seed score differences and failure frequencies *within* (law,d,N,eta,R); distinguish total cost and optimization accuracy Pareto trade-off. Do not pool R1 and R3 as independent; do not average raw MSE across changing orders and call it a universal statistical risk.

## 5. Acceptance tests before full simulation

- Numerical equality of `PenalizedCriteria(...,mean_mode="joint").score("cv",lambda)` and `JointMeanPooledLOOCV(...).score(lambda)` for randomly generated equal input; test zero/infinite limits and d=1..4.
- Explicit deleted-observation refit parity for small N, including pooled cross-series influence in the full `RN × RN` smoother; check the full joint EDF.
- Exact evaluation of the *same* objective after every method returns a candidate, with stable validation near log endpoints.
- Deterministic seeds, immutable shard outputs and complete row/source SHA manifests; no overwritten K.1 aggregate files.
- A robust treatment of candidate ties, numerical rank near d=4/N=200, and NaN/infinite objective scores.
- Validate the diagnostic aggregation on intentionally missing/duplicated/conflicting shard metadata and on a fixture with known multiple minima if one is actually found. Do **not** invent or assume multiple minima exist.

## 6. Interpretation and priorities

This study isolates the **numerical** axis. It does *not* establish that pooled observation CV is the optimal risk estimator or that Gaussian likelihood loses to CV. Study K.1 already supplies the **statistical** criterion comparison (exploratory 25 seed replay), Study H the stronger matched-Gaussian mean-estimation confirmation, and the future application to actual financial returns is different because the true stochastic trend is not observed.

**Next work order:** implement and unit-test fixed-score solver comparability; execute a small paired preflight manually; audit its saved objective gaps; only then decide whether an all-J-replay numerical experiment is worth the compute. If algorithms tie on score, document the negative result and redirect scientific effort to the estimation objective, dependence-aware validation, or statistical model specification rather than searching for a manufactured optimizer victory.

**No exact launcher command exists yet for Study L.** Do not direct a user to run a nonexistent module. Once implemented, update the study's status here and in the paper handoff, create a separately named result root, and use a new dated results/audit note.
