# Literature positioning — current CSSC research question

**Updated 2026-10-08.** The earlier Journal of Forecasting plan is historical. Current intended journal: *Communications in Statistics—Simulation and Computation* (CSSC). No “first-ever” novelty claim has been verified.

## Closest statistical and model foundations

- **Guerrero (2007, 2008):** finite-difference PLS, statistical interpretation, trace-based smoothness, a user-chosen smoothness percentage and penalty recovery. We did not invent the estimator or index.
- **Cortés-Toto, Guerrero and Reyes (2017), CSSC:** PLS smoothness achieved with CV, GCV, AICc, and BIC. Direct same-family comparator, although not the identical declared multi-step trend-continuation MSE.
- **Guerrero et al. (2018):** effects of autocorrelated noise on smoothness and PLS; a simulation with AR(1) errors is not itself a dependence-aware fitted covariance model.

## Using controlled trends in forecasts already occurred

- **Islas, Guerrero and Silva (2019):** a controlled-smoothness trend used for remittance forecasts with a Markov-switching model. Their chosen smoothness percentage differs from our explicit pooled future-block error criterion, but the use of such a trend for forecasting is plainly not novel.
- **Islas Camargo and Zumaya Galván (2025):** exchange-rate forecasting using a controlled-smoothness trend and Markov switching. Again, compare *what is tuned and with which loss*, not whether smoothing was previously used before forecasts.

## Predictive smoothing selection is also precedent

- **Hart (1994):** time-series cross-validation selecting kernel bandwidth from one-step-ahead predictions with dependent data. Direct precedent for historical pseudo-futures guiding smoothing.
- **Vilar-Fernández and Cao (2007), CSSC:** nonparametric time-series forecasting and smoothing parameter choice, another close journal precedent.
- **Bates et al. (1987), CSSC:** GCVPACK and numerical regularization selection.
- **Tashman (2000) and Bergmeir et al. (2012, 2018):** forecast-origin chronology and conditions for CV use.

## Different loss targets

- **Franke, Kukacka and Sacht (2026):** HP tuning from simulations with known latent trend, primarily recovery of that trend; not the same as historical future observation MSE.
- **Biessy (2026):** Whittaker–Henderson parameter selection, marginal likelihood and extrapolation. Its precise assumptions and criterion need explicit comparison.

## Possible research gap — not yet proven as priority

Investigate the joint statistical construction:

1. Full-range normalized smoothness \(S\in[0,1]\) as the tuning/reporting coordinate (with an algebraically equivalent \(\lambda\)).
2. \(H(S)\) estimated on each strictly historical fitting window.
3. A declared native finite-difference \(h\)-step continuation \(G_{d,h}\).
4. Direct MSE against **subsequently realized blocks of older forecast origins**, pooled at the intended horizon.
5. Final refit and truly unseen outer forecast; careful distinction from signal recovery.
6. Spectral and analytic derivative evaluation, competing minima, and exact endpoint handling.

The change of coordinate from \(\lambda\) to \(S\) does **not** change the globally optimal fitted trend for an identical objective. Novelty must instead be sought in the particular forecast-CV criterion, its numerical analysis/implementation, and robust evidence of consequences.

**Open:** was this exact PLS/HP multi-step forecast-tuning objective previously published? Conduct a focused full-text audit, including older HP forecasting and penalized-trend research. The uploaded PDFs and the literature bundle are primary reading inputs; missing original texts must not be marked as checked.

Preferred wording: “We investigate horizon-matched chronological forecast-MSE selection for normalized PLS trend smoothness.” Avoid universal uniqueness or performance claims.

[Research objective](research_objective.md) · [Mathematical foundations](mathematical_foundations.md) · [Claim boundaries](claim_boundaries.md)
