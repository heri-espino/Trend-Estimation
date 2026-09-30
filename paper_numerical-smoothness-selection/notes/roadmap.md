# Roadmap — Active Paper

The repository is currently focused **only** on this roadmap. Do not start new
experiments for the other research papers until this one reaches Phase 7.

## Phase 0 — Paper separation

**Status: complete.**

- [x] create a dedicated numerical-paper directory;
- [x] separate recurrence/model-comparison questions into their own paper;
- [x] mark the adaptive paper as parked;
- [x] make this the sole active research track.

## Phase 1 — Mathematical/numerical foundation

- [x] derive \(S'(\lambda)\) and \(S''(\lambda)\);
- [x] implement smoothness-domain stationary-point search;
- [x] establish stationary-point equivalence under reparameterization;
- [x] add synthetic multimodal tests;
- [x] implement exact \(S=1\leftrightarrow\lambda=\infty\) semantics;
- [x] verify exact \(S=0\) and limiting \(S=1\) objectives;
- [ ] benchmark numerical conditioning near both endpoints;
- [x] canonicalize the theoretical nullity of \(D_d^\top D_d\) to remove LAPACK/platform noise at large \(\lambda\).

**Stop condition:** endpoint behavior and interior derivatives are numerically
consistent to frozen tolerances.

## Phase 2 — Multiple-minimum search

- [x] start from a small deterministic \(S\)-partition;
- [x] adaptively subdivide suspicious intervals;
- [x] bracket derivative sign changes;
- [x] refine roots with Brent;
- [x] classify roots;
- [x] implement epsilon-separated candidate selection;
- [ ] strengthen flat/tangential stationary-point diagnostics;
- [x] implement an adversarial analytic suite with known stationary points;
- [ ] freeze derivative/curvature tolerances and maximum depth;
- [ ] deduplicate roots robustly near numerical boundaries.

**Stop condition:** known synthetic stationary points are recovered within
frozen tolerances, including adversarial near-flat cases.

## Phase 3 — Dense-reference benchmark

- [x] create an initial reproducible benchmark runner;
- [x] replace the old mixed-paper runner with an active-paper runner under
  experiments/numerical_smoothness_selection/;
- [x] run smoke benchmark;
- [ ] rerun quick benchmark after nullspace canonicalization (the first quick run is diagnostic/pre-fix);
- [ ] inspect every disagreement with the dense reference;
- [ ] run paper-scale benchmark.

Report:

- global-optimum \(S\) error;
- objective regret;
- local minima found/missed;
- number of objective/derivative evaluations;
- runtime;
- failure/ambiguity rate.

**Stop condition:** empirical accuracy and efficiency are characterized well
enough to support a precise claim.

## Phase 4 — Search-design sensitivity

- [ ] compare initial grid sizes;
- [ ] compare max depths;
- [ ] compare near-zero/curvature heuristics;
- [ ] compare with existing log-\(\lambda\) stationary search using the adversarial suite;
- [ ] evaluate epsilon set
  \[
  \{0,0.02,0.05,0.10,0.15\};
  \]
- [ ] decide whether epsilon is algorithmic output or only candidate-summary
  post-processing.

**Stop condition:** one default algorithm/protocol is frozen before final runs.

## Phase 5 — Controlled configuration breadth

Run the frozen numerical algorithm over a controlled set of:

- \(d\in\{1,2,3,4\}\);
- several \(L\);
- several \(h\);
- a small number of simple continuation rules.

The purpose is to stress different objective geometries, not to rank a large
forecasting model zoo.

**Stop condition:** conclusions are not artifacts of one \(d,L,h\) choice.

## Phase 6 — Reproducibility and manuscript evidence

- [ ] freeze random seeds and presets;
- [ ] version lightweight summary outputs;
- [ ] create final figures/tables directly from frozen results;
- [ ] write a limitations section covering missed-root risk;
- [ ] complete literature audit focused on numerical parameter selection;
- [ ] run all tests and documentation checks.

## Phase 7 — Finish the paper

- [ ] complete main.tex;
- [ ] compile through manual GitHub Actions;
- [ ] perform notation/claim consistency pass;
- [ ] referee-style novelty and readability review;
- [ ] freeze final results and checkpoint.

**Completion rule:** only after Phase 7 is complete do we resume either parked
research paper.
