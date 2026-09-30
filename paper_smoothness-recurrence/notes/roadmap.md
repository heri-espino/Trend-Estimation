# Roadmap

Last updated: 2026-09-29

The goal is a compact paper with one mathematical/numerical contribution and
one financial application. Do not expand the project until the current phase
passes its stopping criterion.

## Phase 0 — Separate the paper cleanly

**Status: complete.**

- [x] create a dedicated paper directory;
- [x] define a separate scientific source of truth;
- [x] keep the broader adaptive ((d,L,S)) paper intact;
- [x] reserve `experiments/smoothness_recurrence/`;
- [x] reserve `results/smoothness_recurrence/`.

## Phase 1 — Reparameterize by smoothness

**Status: next.**

- [ ] derive and test (S(\lambda)), (S'(\lambda)), (S''(\lambda));
- [ ] treat (S=0) and (S=1) as exact conceptual boundaries;
- [ ] implement robust interior inversion (lambda(S));
- [ ] expose (F(S)=CV(\lambda(S)));
- [ ] verify (F'(S)=0\iff CV'(\lambda)=0);
- [x] verify minimum/maximum classification is preserved;
- [ ] benchmark conditioning near both endpoints.

Stopping criterion: smoothness-domain evaluations reproduce existing
lambda-domain values/derivatives to numerical tolerance.

## Phase 2 — Multiple local minima without a dense grid

**Status: planned.**

Primary algorithm:

1. start from a small deterministic partition of (S\in[0,1]);
2. evaluate derivative information;
3. adaptively subdivide intervals with plausible stationary structure;
4. bracket derivative sign changes;
5. refine every bracket with Brent;
6. classify roots;
7. compare every local minimum plus both boundaries.

- [x] implement `find_stationary_points_smoothness`;
- [x] report all roots, types, objective values, and evaluation counts;
- [ ] refine near-zero/flat derivative regions;
- [ ] define deterministic stopping tolerances and max depth;
- [ ] cache eigenvalues and repeated inversion work;
- [x] add multimodal synthetic tests;
- [ ] compare with current log-lambda search;
- [x] add a reproducible dense-reference benchmark runner;\n- [ ] run and inspect the benchmark against the dense reference.

Without stronger assumptions, no finite adaptive sampler can certify discovery
of every root of an arbitrary smooth objective. The dense diagnostic grid will
measure empirical missed-root risk.

Stopping criterion: match the dense/reference global optimum to a frozen
tolerance with materially fewer evaluations.

## Phase 3 — Freeze forecasting/model-selection protocol

**Status: planned.**

Before final financial outcomes:

- [ ] choose primary scale, with log price as leading candidate;
- [ ] evaluate difference orders d in {1,2,3,4};
- [ ] freeze a small grid of estimation windows L;
- [ ] freeze forecast methods m;
- [ ] freeze CV history/origin spacing;
- [ ] freeze forecast horizons h;
- [ ] freeze loss;
- [ ] implement a likelihood/state-space benchmark;
- [ ] decide once-per-series vs. rolling selection.

For each discrete configuration (d,L,m,h), find multiple local minima in S and
retain at most five epsilon-separated candidates. Select the complete
configuration using development/validation data only:

\[
(d^\star,L^\star,m^\star,S_h^\star)
=
\arg\min CV_h(d,L,m,S).
\]

Then freeze the selected configuration and evaluate it once on the untouched
test block.

The likelihood benchmark is not tuned by forecast CV: its variance/smoothing
parameters are estimated by ML/REML or marginal likelihood and its forecasts
are scored on the same validation/test periods.

## Phase 4 — Freeze recurrence definition

**Status: planned.**

- [ ] implement frozen-origin trend forecasts;
- [ ] implement crossing recurrence;
- [ ] implement tolerance-band recurrence;
- [ ] define standardized initial deviation;
- [ ] freeze (H_{max}) and censoring;
- [ ] pre-specify bins or continuous models;
- [ ] address overlap/dependence between event origins.

Stopping criterion: leakage tests and synthetic known-crossing tests pass.

## Phase 5 — Numerical and stochastic validation

**Status: planned.**

Numerical benchmark:

- dense GPU/reference grid vs. adaptive search;
- (|S^*_{adaptive}-S^*_{dense}|);
- objective regret;
- evaluation count;
- runtime;
- local-minimum count.

Stochastic sanity checks use simple known-trend synthetic series. They validate
interpretation without reproducing the adaptive paper's large regime grid.

## Phase 6 — Financial application

**Status: planned.**

Progression:

1. broad ETFs/indices;
2. held-out individual equities;
3. crypto stress test.

For each series/horizon:

- estimate (S_h^\star) from development data;
- forecast the trend at untouched origins;
- record initial standardized deviation;
- record recurrence/censoring time;
- summarize recurrence probability and time-to-event.

Primary outputs include (h\mapsto S_h^\star), local-minimum counts,
numerical efficiency, recurrence probability vs. initial distance, survival
summaries, and cross-class comparisons.

## Phase 7 — Inference and robustness

- [ ] uncertainty for recurrence probabilities;
- [ ] survival/hazard model if censoring warrants it;
- [ ] block/bootstrap or cluster-aware uncertainty;
- [ ] price vs. log-price;
- [ ] (d=1) vs. (d=2);
- [ ] alternative fixed (L);
- [ ] alternative tolerance bands;
- [ ] non-overlapping event sampling.

Do not add robustness dimensions merely because the main result is unfavorable.

## Phase 8 — Manuscript synthesis

Target narrative:

1. penalized trend;
2. smoothness compactification;
3. derivative-based multiple-minimum search;
4. chronological CV selection;
5. frozen forecast-trend recurrence;
6. numerical benchmark;
7. financial evidence;
8. limitations.

For a short SMCCA-style paper, prefer one clean algorithm, a few precise
mathematical results, and a compact empirical section.
