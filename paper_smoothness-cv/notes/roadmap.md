# Roadmap — Smoothness-CV paper

## Phase 0 — Identity

- [x] Split criterion and numerical-solver papers.
- [x] Define Paper A as the "what should be optimized?" contribution.
- [x] Make Guerrero the direct methodological foundation.
- [x] Keep Hart as an important but structurally different precedent.

## Phase 1 — Formal theory

- [ ] Freeze baseline assumptions: zero drift, identity weighting, regular spacing, fixed \(d,L,h\).
- [ ] Record monotonicity/endpoints of normalized \(S(\lambda)\).
- [ ] State the bijection \([0,\infty]\leftrightarrow[0,1]\).
- [ ] Define \(G_{d,h}\) formally.
- [ ] State the chronological information-set rule.
- [ ] Define \(F_{d,L,h}(S)\) and \(S^\star\).
- [ ] Clarify existence and possible nonuniqueness.

## Phase 2 — Literature audit

- [ ] Re-read Guerrero 2007/related controlled-smoothness work.
- [ ] Re-read Hart 1994 for novelty boundaries.
- [ ] Audit finite-difference PLS smoothing-selection papers.
- [ ] Audit horizon-specific/rolling forecast selection.
- [ ] Rewrite literature review around Guerrero -> endogenous smoothness.
- [ ] Avoid "first" claims until complete.

## Phase 3 — Controlled experiments

- [ ] Compare forecast-optimal vs recovery-optimal smoothness.
- [ ] Vary horizon with estimator family fixed.
- [ ] Study noise, latent roughness, residual persistence.
- [ ] Show representative \(F(S)\) curves including multimodality.
- [ ] Dense \(S\) grids are acceptable.

## Phase 4 — Empirical illustration

- [ ] Use a small number of carefully chosen real series.
- [ ] Treat them as illustrations, not universal superiority evidence.

## Phase 5 — Manuscript

- [ ] Draft introduction around controlled-smoothness gap.
- [ ] Present Hart/other predictive methods as related work.
- [ ] Keep numerical solver to a short implementation paragraph.
- [ ] Final claim audit.
