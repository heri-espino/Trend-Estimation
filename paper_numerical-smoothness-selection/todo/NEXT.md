# NEXT — Applied interpretation of multiple forecast-CV minima

## Priority 1 — Design the case studies

- [ ] Freeze the case-study series before inspecting final test performance:
  - [ ] FRED real GDP: `GDPC1`;
  - [ ] one broad ETF: `SPY` or `QQQ`;
  - [ ] one stock: `AAPL` or `XOM`;
  - [ ] one cryptocurrency: `BTC-USD` or `ETH-USD`.
- [ ] Define frequency-appropriate ((d,L,h)) values before opening the final
      test block.
- [ ] Define a final untouched test block for every series.
- [ ] Decide whether the case-study figures show all minima or at most the best
      3 epsilon-separated minima.
- [ ] Define a deterministic rule for selecting a representative origin/configuration
      when several have multiple minima.

## Priority 2 — Explain why multiple minima occur

- [ ] Add a short spectral explanation using
      (alpha_j(lambda)=1/(1+lambdadelta_j)).
- [ ] Explain how smoothing changes endpoint slope/curvature and therefore
      finite-difference continuation.
- [ ] Show at least one example where two local CV minima have similar
      validation loss but visibly different trends/forecasts.
- [ ] Show at least one example where the globally selected CV minimum is not
      the smoothest or roughest candidate.
- [ ] Avoid causal/economic interpretations of the minima.

## Priority 3 — Applied figure design

Target one multi-panel figure per data family or, preferably, one compact
figure with four rows:

1. GDP;
2. ETF;
3. stock;
4. crypto.

For each row/panel:

- left: (F(S)) with minima marked;
- center: observed training series plus trend estimates for the minima;
- right: forecast paths plus untouched test observations.

Potential visual encoding:

- candidate 1: best CV minimum;
- candidate 2/3: alternative local minima;
- optional dashed GCV reference if added later.

The figure must make the practical meaning of “multiple minima” visible without
requiring a table of dozens of numbers.

## Priority 4 — Optional comparator

Before submission, consider adding one compact comparison against an
off-the-shelf one-dimensional optimizer:

- [ ] bounded/golden-section scalar minimization as a unimodal baseline;
- [ ] multistart Brent or SHGO/DIRECT as a global baseline.

This comparison should answer the referee question:

> Why is a specialized multiple-minimum search needed for a one-dimensional
> objective?

Do not add a large optimizer zoo.

## Priority 5 — Manuscript revision

- [ ] Reframe the introduction around the practical ambiguity created by
      multiple forecast-CV minima.
- [ ] Add a subsection: “Why multiple forecast-optimal smoothness levels can
      arise.”
- [ ] Add a subsection: “Applied examples.”
- [ ] Reduce emphasis on the financial 384-surface benchmark once the applied
      examples are present.
- [ ] Replace or simplify the current sensitivity figure if page pressure
      increases.
- [ ] Revisit the abstract only after the applied section is frozen.
- [ ] Run a referee-style pass for novelty, scope, wording, and unnecessary
      numbers.
- [ ] Compile final SMCCA PDF and inspect every page.

## Submission boundary

The paper remains a numerical/applied-mathematics paper. The applied examples
exist to interpret the optimization geometry, not to claim forecasting
superiority, economic regimes, or trading value.
