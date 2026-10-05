# Literature positioning

## Direct foundation: Guerrero

The paper should be narrated primarily as an extension of controlled-smoothness finite-difference PLS.

Guerrero provides the finite-difference trend family, a statistical interpretation, a trace-based smoothness index, analyst-chosen smoothness percentages, and trend forecasting/extrapolation examples.

Our conceptual change is
\[
S_{\text{chosen by analyst}}
\longrightarrow
S^\star_{\text{chosen by chronological forecast error}}.
\]

## Important but different: Hart (1994)

Hart's TSCV selects a kernel bandwidth using one-step-ahead predictive performance in dependent data.

This establishes that predictive smoothing-parameter selection is not new in general.

However Hart differs structurally:
- kernel smoother rather than finite-difference PLS;
- bandwidth rather than controlled-smoothness percentage;
- explicit time-series error model;
- one-step prediction rather than general future-block continuation.

Cite Hart as a conceptual precedent and novelty boundary, not as the direct mathematical foundation.

## Other strands to audit

- Whittaker/Henderson finite-difference smoothing;
- CV/GCV/AIC/AICc/BIC smoothing selection;
- smoothing splines/effective degrees of freedom;
- rolling-origin forecast evaluation;
- horizon-specific model selection;
- modern Whittaker-Henderson likelihood/Bayesian formulations.

The existing literature/ corpus and pre-split notes are source material. Re-audit specifically for Paper A before claiming universal novelty.

## Safe provisional wording

> We extend controlled-smoothness finite-difference penalized trend estimation by defining the smoothness percentage endogenously through a horizon-specific chronological future-block forecast criterion.

Do not use "first" without a targeted audit.
