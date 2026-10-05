# Numerical methods for forecast-smoothness selection

**Status: ACTIVE — numerical companion paper after the 2026-10-05 split.**

Working title: **Numerical Solution of Multimodal Forecast-Smoothness Selection Problems**

## Objective

Given the forecast-smoothness objective \(F(S)\) defined in paper_smoothness-cv/, develop and validate methods for locating all relevant stationary minima and the global optimum efficiently and reliably on \(S\in[0,1]\).

## What this paper assumes

Paper A defines
\[
S^\star\in\arg\min_{S\in[0,1]}F(S).
\]

Paper B starts there and asks how to solve it.

## Current production method

1. sparse deterministic evaluation in \(S\);
2. analytic first/second derivatives;
3. adaptive interval subdivision;
4. derivative sign-change brackets;
5. Brent root refinement;
6. stationary-point classification;
7. exact/limiting endpoint comparison;
8. optional post-discovery spacing of nearby minima.

Brent does not discover all roots globally. It refines a root once a bracket is identified.

## Analytic derivatives

\[
H'=-HQH,\qquad H''=2HQHQH.
\]

With
\[
r_T=z_T-GHx_T,\quad
a_T=GHQHx_T,\quad
b_T=GHQHQHx_T,
\]
\[
f'_T=\frac{2}{h}r_T^\top a_T,
\]
\[
f''_T=\frac{2}{h}\left(\|a_T\|^2-2r_T^\top b_T\right).
\]

\[
F'(S)=\frac{f'(\lambda)}{S'(\lambda)},
\]
\[
F''(S)=
\frac{f''(\lambda)}{[S'(\lambda)]^2}
-
\frac{f'(\lambda)S''(\lambda)}{[S'(\lambda)]^3}.
\]

## Stronger algebraic direction

\[
f(\lambda)=\frac{P(\lambda)}{D(\lambda)^2},
\qquad
f'(\lambda)=\frac{R(\lambda)}{D(\lambda)^3}.
\]

This creates a possible route to certified stationary-point isolation via polynomial-root methods such as Sturm sequences, followed by Brent refinement.

Current status: the Sturm mini-check is a proof-of-concept, not the production solver and not a general certification theorem.

## Frozen benchmark evidence

- 240/240 relevant adversarial minima/boundary optima;
- 2105/2105 synthetic dense-reference interior minima across 1920 surfaces;
- 473/473 financial dense-reference interior minima across 384 geometry-stress surfaces;
- mean evaluation fractions about 1.57% synthetic and 1.84% financial.

These are empirical benchmark results.

## Migration note

This folder was copied from paper_numerical-smoothness-selection/ so the manuscript, figures, tables, checkpoints, and historical notes remain available.

Some copied files still reflect the old combined-paper framing. Canonical current sources are:

1. AI_HANDOFF.md
2. notes/research_objective.md
3. notes/paper_split_2026-10-05.md
4. notes/submission_positioning.md
5. notes/results.md
6. notes/sturm_minicheck.md

The experiment/result namespaces remain experiments/numerical_smoothness_selection/ and results/numerical_smoothness_selection/ for reproducibility.
