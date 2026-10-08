# Submission positioning — numerical-methods paper

## Identity

This is a scientific-computing/numerical-analysis paper.

The criterion \(F(S)\) is defined in the companion paper_smoothness-cv/ workspace. This manuscript should introduce only enough of that criterion to be self-contained.

## Core question

> How can the potentially multimodal scalar objective \(F(S)\), \(S\in[0,1]\), be solved reliably while avoiding exhaustive dense evaluation?

## Contribution hierarchy

Primary:
- derivative-aware stationary-point search;
- exact endpoint semantics;
- multiple-minimum recovery/classification;
- controlled benchmarking.

Stronger extension under investigation:
- exploit rational structure in \(\lambda\);
- construct the stationary polynomial numerator;
- isolate nonnegative real roots with certified algebraic tools;
- refine isolated roots numerically.

## Not novel by itself

Do not claim novelty for PLS smoothing, controlled smoothness, rolling validation, Brent, cross-validation, multiple minima, or dense-grid benchmarking.

## Safe current claim

> For the structured forecast-smoothness objectives studied here, a derivative-aware endpoint-aware search recovered all relevant reference minima in the frozen benchmark suites while using a small fraction of the dense-reference objective evaluations.

This is empirical, not a universal theorem.

## Sturm language

Safe:
- "proof-of-concept exact root-isolation experiment";
- "suggests a route toward certified stationary-point enumeration."

Not safe yet:
- "the algorithm certifies all minima";
- "no grid is required in all practical cases";
- "Sturm validates the production solver globally."
