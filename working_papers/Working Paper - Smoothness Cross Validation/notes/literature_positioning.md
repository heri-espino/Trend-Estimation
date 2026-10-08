# Literature positioning — current CSSC research question

**Updated 2026-10-08.** The earlier Journal of Forecasting plan is historical. Current intended journal: *Communications in Statistics—Simulation and Computation* (CSSC). No “first-ever” novelty claim has been verified.

## Closest statistical and model foundations

- **Guerrero (2007, 2008):** finite-difference PLS, statistical interpretation, trace-based smoothness, a user-chosen smoothness percentage and penalty recovery. We did not invent the estimator or index.
- **Cortés-Toto, Guerrero and Reyes (2017), CSSC:** PLS smoothness achieved with CV, GCV, AICc, and BIC. Direct same-family comparator, although not the identical declared multi-step trend-continuation MSE.
- **Guerrero et al. (2018):** effects of autocorrelated noise on smoothness and PLS; a simulation with AR(1) errors is not itself a dependence-aware fitted covariance model.

## Spectral smoothness: central technical representation, not a first-discovery claim

The pure finite-difference PLS smoother has \(Q=D_d^\top D_d\) real symmetric PSD, \(Q=U\operatorname{diag}(\delta_1,\ldots,\delta_L)U^\top\), and
\[
H_\lambda=(I+\lambda Q)^{-1}
=U\operatorname{diag}\bigl((1+\lambda\delta_j)^{-1}\bigr)U^\top,
\qquad
\operatorname{edf}(\lambda)
=\operatorname{tr}(H_\lambda)
=\sum_{j=1}^L(1+\lambda\delta_j)^{-1}.
\]
For \(1\le d<L\), the \(d\) null eigenvalues imply the normalized identity
\[
S(\lambda)
=\frac{L-\sum_{j=1}^L(1+\lambda\delta_j)^{-1}}{L-d}
=\frac{L-\operatorname{edf}(\lambda)}{L-d}.
\]

**Evidence that this is not intrinsically novel:** Cortés-Toto, Guerrero and Reyes (2017, discussion directly following their equation (9), p. 1495) explicitly state that their smoothness limit follows by expressing the trace in terms of the **eigenvalues** of \(K_d^\top K_d\), citing Eilers and Marx (1996). Earlier smoothing literature already writes effective degrees of freedom as spectral sums. Guerrero (2007) also precedes us in introducing the trace-based smoothness index. Our full-range normalization of this index is a straightforward reparameterization. We must **not** claim to be first to express PLS smoothness spectrally, first to compute EDF with eigenvalues, or first to choose smoothing based on EDF.

**Why the spectral representation matters to this particular paper:** a shared eigendecomposition can be reused for many candidate \(S\) values and forecast origins; the spectral weights supply exact limits at \(S=0,1\), analytic derivatives, and a computationally structured expression for pooled forecast-MSE. The research contribution, **if borne out**, must be defended in the specific horizon-matched forecast-selection criterion, its analysis and computation, and rigorously untouched out-of-sample comparisons with classical smoothness selectors. The spectral formula is an **enabling mathematical tool**, not a standalone priority claim.

**Suggested manuscript wording:** “We exploit the spectral representation of the established finite-difference PLS smoother to evaluate normalized smoothness, its derivatives, and a pooled horizon-specific forecast-validation objective.” Attribute the underlying smoothness index to Guerrero and cite Cortés-Toto et al. for the eigenvalue connection.

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

## Explicit synthesis-first positioning

We should present the research as a **synthesis designed for the forecasting decision at horizon \(h\)**: established PLS + spectral EDF/normalized smoothness + \(h\)-step continuation + fixed-window rolling-origin TSCV + pooled forecast-MSE selection and final refit. The unifying point is that **the choice of smoothness is evaluated against the future outcomes of historical origins at the *same declared horizon***. Neither the number of ingredients nor their individual mathematical familiarity is itself a contribution; relevance, any genuinely new analysis, prior-art comparison, and untouched test performance determine what can be claimed.

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
