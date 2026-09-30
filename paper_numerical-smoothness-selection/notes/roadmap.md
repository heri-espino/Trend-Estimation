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
- [x] verify recovery of flat minima on an adversarial analytic suite;
- [ ] detect tangential non-minimum stationary roots if the manuscript needs a claim about all stationary points;
- [x] implement an adversarial analytic suite with known stationary points;
- [x] add deterministic endpoint-aware refinement for compactified boundary cells;
- [x] freeze derivative/curvature tolerances, endpoint refinement, and maximum depth;
- [ ] deduplicate roots robustly near numerical boundaries.

**Stop condition:** known synthetic stationary points are recovered within
frozen tolerances, including adversarial near-flat cases.

## Phase 3 — Dense-reference benchmark

- [x] create an initial reproducible benchmark runner;
- [x] replace the old mixed-paper runner with an active-paper runner under
  experiments/numerical_smoothness_selection/;
- [x] run smoke benchmark;
- [x] rerun quick benchmark after nullspace canonicalization;
- [x] rerun quick benchmark after endpoint-aware refinement;
- [x] inspect every disagreement in the post-nullspace quick run;
- [ ] run paper-scale benchmark.

Report:

- global-optimum \(S\) error;
- objective regret;
- local minima found/missed;
- number of objective/derivative evaluations;
- runtime;
- failure/ambiguity rate.

**Current pre-paper result:** 227/227 dense-reference interior minima matched across 216 synthetic surfaces, with zero positive objective regret. The primary search specification is frozen before the paper-scale run.

**Paper-scale result:** 2105/2105 dense-reference minima matched across 1920 synthetic surfaces; 240/240 relevant adversarial minima/boundary optima detected; zero meaningful positive regret.

**Stop condition: met.** Empirical accuracy and efficiency are characterized well enough to support a precise claim.

## Phase 4 — Search-design sensitivity

The primary settings are already frozen under Decision N009. The remaining
items are robustness checks and must not retune the primary specification.

- [x] compare initial grid sizes;
- [x] implement reproducible OFAT sensitivity runner;
- [x] compare max depths;
- [x] compare near-zero derivative heuristic;
- [x] compare with existing log-\(\lambda\) stationary search using the adversarial suite;
- [x] evaluate epsilon set
  \[
  \{0,0.02,0.05,0.10,0.15\};
  \]
- [x] decide that epsilon is candidate-summary post-processing only.

**Stop condition: met.** Sensitivity was characterized without changing the frozen primary protocol.

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
