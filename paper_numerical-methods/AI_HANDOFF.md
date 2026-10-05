# AI Handoff — Numerical-methods paper

## Identity

This paper answers **how to optimize the forecast-smoothness objective**.

Do not re-claim the definition of forecast-optimal smoothness as the main numerical contribution; that belongs to paper_smoothness-cv/.

## Input problem

\[
F(S),\qquad S\in[0,1],
\]
with
\[
S^\star\in\arg\min_{S\in[0,1]}F(S),
\]
without assuming unimodality.

## Current solver

- adaptive discovery over \(S\);
- evaluate \(F,F',F''\);
- bracket sign-changing roots of \(F'\);
- refine with Brent;
- classify roots;
- include \(S=0\) and \(S=1\);
- compare all candidate minima.

Flat/tangential roots remain a numerical edge case; do not claim generic certification.

## Why \(S\) is legitimate

\[
F'(S)=0\iff f'(\lambda)=0
\]
because \(S'(\lambda)>0\).

At a nondegenerate stationary point,
\[
\operatorname{sign}F''(S^\star)
=
\operatorname{sign}f''(\lambda^\star).
\]

## Rational/Sturm direction

Do not say "we removed the grid" unless production discovery is actually replaced.

Today:
- adaptive sampling discovers brackets;
- Brent refines;
- Sturm exists only as a mini-check.

## Benchmark interpretation

Dense grids are reference approximations, not mathematical ground truth.

Financial series are objective-geometry stress tests, not evidence of predictability or trading value.

## Copied material

main.tex and several notes were copied from the former mixed paper. When they conflict with this handoff or notes/research_objective.md, the new split documents win.
