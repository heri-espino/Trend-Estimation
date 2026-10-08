# CP04 — Applied multiple-minima results

**Date:** 2026-09-30  
**Status:** current.

## Run

Frozen result directory:

results/numerical_smoothness_selection/20261001T022610Z_applied-paper_72b8aaa/

The run used tracked snapshots only and preserved the development/test split.
The metadata records selection_uses_test=false and test_role=diagnostic_only.

## Main result

The applied experiment supports a more nuanced statement than “forecast CV is
always multimodal.”

Across the pre-specified 64 configurations per series:

- GDPC1: 0 configurations with two or more epsilon-separated candidate minima;
- SPY: 7 configurations with two or more candidates;
- AAPL: 10 configurations with two or more candidates;
- BTC-USD: 9 configurations with two or more candidates, including 3 with
  three candidates.

Thus multimodality is data- and configuration-dependent rather than universal.

## Selected development-only cases

### GDPC1

Selected contrast case:

- d=1, L=40, h=1;
- one representative minimum;
- S=0.38030;
- no validation-test rank reversal.

GDP therefore serves as a useful unimodal contrast rather than a multiple-minimum
example.

### SPY

Selected case:

- d=1, L=126, h=60;
- CV-1: S=0.95639, CV MSE=0.00177070;
- CV-2: S=0, CV MSE=0.00195813.

The alternative candidate is about 10.6% worse in rolling CV, but on the
untouched test block:

- CV-1 test MSE=0.00093985, test rank 2;
- CV-2 test MSE=0.00066164, test rank 1.

This is a validation-test rank reversal. The candidate selected by rolling CV
does not have the smallest test error among the frozen candidates.

This does not justify selecting CV-2 after seeing test. It is evidence that
distinct local minima can encode materially different smoothing choices whose
relative ordering changes on later observations.

### AAPL

Selected case:

- d=2, L=252, h=1;
- CV-1: S=0.62901;
- CV-2: S=0.99733.

CV-2 has substantially larger validation error and also larger test error.
There is no rank reversal.

The case still demonstrates that a second local minimum can correspond to a
very different smoothing regime without being a competitive alternative.

### BTC-USD

Selected case:

- d=2, L=504, h=1;
- three representative minima:
  - CV-1: S=0.84463;
  - CV-2: S=0.02908;
  - CV-3: S=0.99786.

CV-2 is only about 13.9% worse than CV-1 in rolling validation error, but its
test MSE is about 14.7 times that of CV-1. CV-3 is much worse in validation and
also worse in test.

There is no rank reversal in the selected BTC case, but the example shows that
nearby validation performance can coexist with sharply different future
behavior when the smoothness regimes are far apart.

## Interpretation

The strongest applied message is not that every series has several plausible
minima. Instead:

1. some series/configurations are effectively unimodal;
2. others contain multiple well-separated local minima;
3. those minima correspond to different smoothing scales and forecast paths;
4. the validation ordering among frozen candidates need not persist on a later
   test block.

The SPY reversal is the clearest case for the manuscript. GDP is a useful
counterexample to any universal multimodality claim.

## Manuscript implication

The applied section should not be written as a benchmark of assets.

It should present:

- GDP as a contrast case with one representative minimum;
- SPY as the key rank-reversal example;
- AAPL and BTC as examples of multiple minima with stable validation/test
  ordering but very different candidate quality.

The paper should explicitly say that the test-best candidate is diagnostic only
and is never fed back into selection.
