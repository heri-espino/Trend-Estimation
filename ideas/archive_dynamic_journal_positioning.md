> **ARCHIVED VENUE NOTE — 2026-10-08.** This was written for the *former* Journal of Forecasting target and Wiley manuscript. It is not the present journal, research direction, execution state, or article template. The current working outlet is *Communications in Statistics—Simulation and Computation*. See [INDEX.md](INDEX.md) and [manuscript_outline.md](manuscript_outline.md).

---

# Journal of Forecasting positioning

Date: 2026-10-05

## Target

Primary target: **Journal of Forecasting**.

The manuscript uses the Wiley NJDv5 Harvard/Utopia two-column template bundled in this repository and is configured as a Journal of Forecasting research article.

## Why the journal fit is credible

The paper is not being targeted to Journal of Forecasting merely because it contains forecasts. Its core methodological question matches several themes already represented in the journal:

1. **Smoothing parameters as forecasting quantities.** Taylor (2004) treats smoothing-parameter adaptation as a forecasting problem and discusses estimation through forecast errors.

2. **Trend/filter choice judged by predictive consequences.** Zafar et al. (2022) develop and compare trend filters specifically through short-term forecast performance.

3. **Out-of-sample loss and rolling evaluation as methodological objects.** Staněk (2023) studies estimation of out-of-sample loss and distinguishes rolling from fixed forecast-evaluation schemes.

4. **Forecast-error hyperparameter selection.** Wolff and Echterling (2024) use time-series cross-validation to select regularization and model tuning parameters from validation prediction error.

5. **New forecast-linked cross-validation strategies.** Franjic and Schweikert (2025) propose a selection strategy based directly on nowcast errors.

6. **Smoothing/bandwidth selection affecting forecasts.** Xu et al. (2025) explicitly compare smoothing variables and bandwidth selectors in a forecasting model.

Our paper occupies the intersection of these forecasting practices with Guerrero's controlled-smoothness finite-difference PLS framework.

## What the paper should look like for this audience

The manuscript should lead with the forecasting decision, not with matrix algebra.

The narrative order should be:

\[
\text{forecasting requires a smoothing choice}
\rightarrow
\text{Guerrero makes smoothness interpretable}
\rightarrow
\text{forecasting literature selects tuning by predictive loss}
\rightarrow
\text{define }S^\star_{d,L,h}.
\]

The mathematical sections should support the forecasting contribution by proving:
- \(S\) is a bounded monotone reparameterization;
- the endpoints have exact forecasting-model interpretations;
- \(S\) has an effective-degrees-of-freedom interpretation;
- optimizing in \(S\) and \(\lambda\) is equivalent.

The manuscript should not become primarily a numerical-analysis paper. Brent, adaptive root discovery, rational stationary equations, and Sturm isolation belong to the companion numerical-methods paper.

## What the empirical package must show

For Journal of Forecasting, definition plus algebra is unlikely to be sufficient. The final paper should show, under a frozen protocol:

- when forecast-CV selects materially different smoothness from CV/GCV/AICc/BIC;
- whether those differences improve later held-out forecasts;
- how selected smoothness changes with horizon;
- when forecast-optimal smoothness differs from latent-trend recovery-optimal smoothness;
- results across heterogeneous public time series rather than only one illustrative series.

The most important experiment is probably:

\[
\text{one-step-selected }S
\quad\text{versus}\quad
\text{horizon-matched }S_h
\]

evaluated on a later untouched test block for several horizons.

## Submission claims to avoid

Do not say:
- predictive smoothing selection is new;
- cross-validation for dependent time series is new;
- forecast-error hyperparameter tuning is new;
- rolling-origin evaluation is new;
- the proposed criterion is universally superior;
- the selected smoothness is a universal property of the series.

## Current safe paper identity

**Forecast-Optimal Smoothness for Penalized Trend Estimation**

> A controlled-smoothness finite-difference trend is tuned by the same horizon-specific chronological forecast loss that defines its intended predictive use.

## Current manuscript state

The manuscript has been rewritten in paper_smoothness-cv/manuscript/ for this target journal. It contains theory and a frozen evaluation design, but no invented performance numbers. The next step is to generate the final empirical evidence under the prespecified protocol.
