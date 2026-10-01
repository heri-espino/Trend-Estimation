# Literature Dictionary

This directory is the terminology and wording reference for the Trend Estimation
research program.

It is intentionally **literature-first**: terminology is taken from the local
literature corpus and original PDFs, then adapted only when the active numerical
paper needs a precise distinction that the source literature does not make.

## Files

- [concepts.md](concepts.md) — canonical concepts, mathematical meaning,
  notation guidance, and source anchors.
- [wording.md](wording.md) — preferred manuscript wording, discouraged wording,
  and distinctions that should remain consistent across the paper.
- [state_of_art_and_novelty.md](state_of_art_and_novelty.md) — bundle-based
  citation map, closest predecessors, novelty boundary, and safe novelty wording.

## Source policy

Primary terminology was checked against:

- the complete `literature/bundle.md` corpus;
- Guerrero (2007), *Time series smoothing by penalized least squares*;
- Cortés-Toto, Guerrero, and Reyes (2017), *Trend smoothness achieved by
  penalized least squares with the smoothing parameter chosen by optimality
  criteria*;
- the internal validation-MSE derivative report used by this project.

The wider bundle was used especially for terminology around forecast
evaluation, Whittaker-Henderson smoothing, GCV, marginal likelihood,
out-of-sample evaluation, endpoint behavior, and numerical root finding.

## Editorial rule

When a manuscript phrase conflicts with this dictionary, prefer the dictionary
unless the manuscript is deliberately quoting or discussing a source that uses
different terminology.

Project-specific terms are explicitly marked as such. They should not be
presented as established literature terminology.
