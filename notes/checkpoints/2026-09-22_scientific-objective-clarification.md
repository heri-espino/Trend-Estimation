# Checkpoint — Scientific Objective Clarification

Date: 2026-09-22

## Why this checkpoint exists

A review of the current repository and all 24 papers presently available under
\`literature/extracted/\` revealed a semantic risk in the project
documentation: recent persistence experiments could be mistaken for the
project's central objective.

That interpretation is incorrect.

## Canonical objective

The active paper is:

> **Forecast-optimal trend estimation as an adaptive forecasting method, where
> smoothness, memory length and difference order depend on horizon and local
> regime.**

The canonical formal object is now

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

## Correct hierarchy

1. Forecast optimality versus recovery optimality defines the target
   distinction.
2. Persistence/horizon is one mechanism study explaining part of the target
   behavior.
3. Within-series regime transition and adaptive OOS skill are the next central
   empirical questions.
4. Macro, index/ETF, equity, and crypto evidence are external validation
   stages.

## Literature status

The target manifest contains 40 references. At this checkpoint, 24 are
available under \`literature/extracted/\`. Therefore the literature audit is
substantial but not complete, and final novelty claims remain blocked.

## Repository action

A new canonical note, \`notes/research_objective.md\`, records the objective,
formal object, scientific hierarchy, persistence-study role, open claims,
literature status, and anti-drift rules. Other canonical documentation is
updated to point to it.

No directory-level refactor was required: the existing library/notes/paper
separation is sound. The necessary refactor is semantic, creating one explicit
source of truth and removing objective ambiguity across handoff, roadmap,
manuscript, and experiment notes.

## Immediate experimental order

1. widen the persistence search domain and densify root discovery;
2. verify the qualitative persistence/horizon mechanism away from artificial
   boundaries;
3. run within-series regime-transition experiments;
4. estimate adaptation delay and joint movement in \((d,L,S)\);
5. test adaptive versus fixed OOS forecast skill;
6. only then freeze the final large simulation design and move to real data.
