# Canonical research objective — numerical methods

**Status: active source of truth after the 2026-10-05 split.**

## Research question

Given a potentially multimodal one-dimensional forecast-smoothness objective \(F(S)\) on \(S\in[0,1]\), can its relevant local minima and global optimum be located reliably with substantially fewer objective evaluations than exhaustive dense search?

## Input from Paper A

paper_smoothness-cv/ defines the scientific criterion. For fixed \(d,L,h\),
\[
F(S)=CV_h(S).
\]

This paper treats \(F\) as the object to solve.

## Derivative structure

Let \(f(\lambda)=F(S(\lambda))\). Since \(S'(\lambda)>0\),
\[
F'(S)=\frac{f'(\lambda)}{S'(\lambda)},
\]
so
\[
F'(S)=0\iff f'(\lambda)=0.
\]

At stationary points,
\[
F''(S^\star)=
\frac{f''(\lambda^\star)}{[S'(\lambda^\star)]^2},
\]
so nondegenerate min/max classification is preserved.

## Current numerical contribution

- compact \(S\in[0,1]\) search;
- analytic derivatives;
- adaptive interval refinement;
- derivative-root bracketing;
- Brent refinement;
- stationary-point classification;
- exact endpoint comparison;
- controlled dense-reference benchmarking.

The method does not prove discovery of every stationary point of an arbitrary smooth objective.

## Stronger possible contribution

Exploit rational structure in \(\lambda\). If the polynomial numerator of \(f'\) can be constructed stably for practical configurations, use certified real-root isolation to produce all relevant nonnegative stationary-root brackets, then use Brent only for numerical refinement.

That would change "adaptive discovery + Brent" into "certified isolation + Brent." It remains a future extension until generalized and benchmarked.
