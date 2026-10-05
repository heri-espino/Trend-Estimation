# Paper split — 2026-10-05

## Why

The old paper_numerical-smoothness-selection/ workspace mixed two contributions:

1. a methodological definition of forecast-optimal smoothness;
2. a numerical method for solving the resulting potentially multimodal objective.

These should be reviewed against different literatures.

## New ownership

paper_smoothness-cv/:
- Guerrero-based controlled-smoothness foundation;
- normalized smoothness;
- forecast continuation;
- rolling future-block loss;
- definition/interpretation of \(S^\star\);
- comparison with recovery/in-sample/predictive-selection alternatives.

paper_numerical-methods/:
- derivatives for optimization;
- multimodal stationary-point search;
- adaptive discovery;
- Brent refinement;
- endpoints;
- benchmarks;
- rational structure;
- Sturm/root-isolation direction.

## Hart versus Guerrero

The literature story is asymmetric.

Guerrero is the direct foundation for Paper A because estimator, finite-difference penalty, smoothness interpretation, and trend extrapolation align structurally.

Hart is an important predictive-selection precedent but uses a different kernel smoother, bandwidth, one-step TSCV construction, and error-model setup. Hart constrains novelty wording; it does not replace Guerrero as the main lineage.

## Migration policy

The old mixed folder remains as a legacy snapshot.

The complete snapshot was copied into paper_numerical-methods/ because most implementation, benchmark evidence, figures, and manuscript machinery belong to the numerical paper.

Do not edit the old folder for new work.

The experiment/result names numerical_smoothness_selection are retained temporarily to avoid breaking tests, frozen metadata, and manuscript paths.
