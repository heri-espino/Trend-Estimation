# Roadmap — Bézier/Bernstein trend idea

**Do not begin paper-scale experiments yet.**

## Phase 0 — novelty audit

- [ ] Acquire/read Kim et al. (1999).
- [ ] Acquire/read Farouki (2012).
- [ ] Acquire/read Wang & Ghosh (2012).
- [ ] Acquire/read Lukoseviciute et al. (2018).
- [ ] Acquire/read Bak, Shin & Koo (2022/2023).
- [ ] Acquire/read the 2025 metal-futures Bézier-filtering paper.
- [ ] Acquire/read Currie, Durban & Eilers (2004).
- [ ] Acquire/read Ugarte et al. (2009).
- [ ] Acquire/read endpoint/margin P-spline work, including Blöchl (2014).
- [ ] Search specifically for penalized Bernstein regression and spline/Bernstein equivalence.
- [ ] Search specifically for Bézier endpoint continuation in time-series forecasting.
- [ ] Write an equivalence/non-equivalence memo before making novelty claims.

## Phase 1 — algebraic prototype

Implement only after Phase 0 has enough clarity:

1. Bernstein design matrix;
2. quadratic coefficient-difference penalty;
3. closed-form smoother;
4. effective degrees of freedom;
5. analytic derivative with respect to \(\lambda\);
6. cubic endpoint level/slope/curvature extraction;
7. at least two endpoint continuation rules.

Verify all formulas by numerical perturbation.

## Phase 2 — controlled equivalence experiment

For the same synthetic signals compare:

- finite-difference PLS;
- smoothing spline;
- P-spline;
- global Bernstein smoother;
- piecewise Bézier/Bernstein smoother;
- optionally l1 trend filtering.

Match complexity by effective degrees of freedom where possible.

Measure both:

- recovery error;
- chronological out-of-sample trend forecast error.

The purpose is to determine whether basis/control-space regularization changes anything after fair matching.

## Phase 3 — endpoint stress tests

DGP families:

- linear;
- quadratic;
- smooth nonlinear;
- local turning point near the endpoint;
- piecewise slope;
- stochastic local level/local linear trend.

Noise:

- iid Gaussian;
- AR(1);
- heteroskedastic;
- occasional outliers.

Vary:

- \(N\);
- forecast horizon \(h\);
- basis dimension \(K\);
- penalty order \(q\);
- distance from the endpoint to the latest turning point.

## Phase 4 — continuation comparison

Compare:

- zero-\(d\)-th-difference continuation from PLS;
- standard P-spline extrapolation;
- derivative/Taylor continuation from the final Bézier segment;
- appended \(C^1\) cubic segment;
- appended \(C^2\) cubic segment;
- shrinkage of terminal slope/curvature.

All continuation choices must be made without future leakage.

## Phase 5 — decision gate

Promote to an active paper only if at least one survives:

1. a nontrivial mathematical distinction from P-splines/smoothing splines;
2. a clear endpoint forecasting regime where control-space regularization is reproducibly different and useful;
3. a useful negative/equivalence result with enough generality to publish.

Otherwise archive as an explored idea.
