# CP05 — Controlled numerical correspondence of smoothness minima

**Status: DESIGN/IMPLEMENTATION COMPLETE; CONTROLLED BENCHMARK NOT YET RUN.**

## Goal

Separate recovery of local minima on one forecast-loss surface from the
numerical ambiguity of matching them across successive surfaces.

The frozen single-surface derivative/root solver is not modified.
Known synthetic minima are fed to the existing one-to-one greedy matcher
and an exactly enumerated pairwise maximum-cardinality, minimum-distance
matcher. Ground-truth identities are known in the synthetic constructions.

## Controlled mechanisms

- separated branches;
- gradually drifting branches;
- near-merger of two branches;
- two genuinely crossing branches;
- branch birth and death.

Each path has 42 observation times and one of 100 random seeds. Candidate
locations are perturbed by reproducible small noise. A common eps grid
`{0.03, 0.06, 0.10, 0.15}` is tested. Paper scale:
`100 * 5 * 4 * 41 * 2 = 164000` method-transition rows.

Matching is one-to-one. Greedy uses the exact existing implementation.
The exact comparator enumerates all admissible **pairwise** assignments
with priority (a) maximum number of links and then (b) minimum sum of
absolute smoothness distances. It is not a global multi-time assignment.

**Crucial information boundary:** For each adjacent-origin transition,
the previous candidates are reset to their true labeled states. Therefore
this benchmark measures one-step correspondence conditional on accurate
previous states. It does *not* validate a full end-to-end tracking system
with accumulated identity errors or birth initialization.

The recorded metrics are number of admissible matches, fraction of true
surviving identities correctly matched, mismatched identities, birth/death
counts, and distance per match. At a genuine crossing, identical or nearly
identical locations may be insufficient to identify the correct branch.

## Deterministic greedy counterexample

Previous minima: branch A at 0.40 and B at 0.48.
Current minima: A at 0.34 and B at 0.43. At tracking radius 0.10,
the greedy shortest edge A -> 0.43 has distance 0.03. It leaves B with
no admissible unused successor. The admissible global pairwise assignment
A -> 0.34 (distance 0.06) and B -> 0.43 (distance 0.05) preserves both
branches. Thus greedy is not guaranteed to maximize continuation count,
even on the unit interval and without crossing.

## Commands

~~~powershell
python experiments/numerical_smoothness_selection/run_tracking_correspondence_benchmark.py --preset smoke
python experiments/numerical_smoothness_selection/run_tracking_correspondence_benchmark.py --preset paper
~~~

## Reporting constraint

Do not add performance percentages to the numerical paper before the
paper preset has been run, reviewed, and committed. Afterward report
results honestly, including situations where the global pairwise
objective cannot recover true temporal identity. Existing financial
tracked-branch illustrations are observational diagnostics, not
ground-truth tracking-validation experiments.
