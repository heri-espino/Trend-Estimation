# Literature positioning — Journal of Forecasting target

Last updated: 2026-10-05.

## Direct foundation: Guerrero

The paper is primarily an extension of controlled-smoothness finite-difference PLS.

Guerrero (2007, 2008) provides:
- the finite-difference penalized trend family;
- a statistical interpretation;
- a trace-based smoothness index;
- the idea of choosing a smoothness percentage and solving for the corresponding penalty;
- trend continuation/forecasting formulas.

Our conceptual change is

\[
S_{\text{chosen by analyst}}
\longrightarrow
S^\star_{\text{chosen by chronological forecast error}}.
\]

This is the cleanest direct lineage.

## Important but structurally different: Hart (1994)

Hart's time-series cross-validation selects a kernel bandwidth through one-step-ahead predictive performance under dependent errors.

This matters because predictive smoothing-parameter selection is therefore not new in general.

The present problem differs in four ways:
- finite-difference PLS rather than kernel regression;
- normalized controlled smoothness rather than bandwidth;
- the finite-difference model's own continuation rule;
- a general horizon-specific future block rather than only the Hart one-step construction.

Hart is a conceptual precedent and novelty boundary, not the direct model foundation.

## Journal of Forecasting literature now incorporated

The target journal already publishes work in the methodological neighborhood needed for this paper.

### Taylor (2004)

Smooth Transition Exponential Smoothing treats the smoothing parameter as a forecasting quantity and discusses estimation from one-step-ahead forecast errors. This supports the forecasting interpretation of smoothing-parameter choice.

### Zafar, Kellard, and Vinogradov (2022)

Multi-Stage Optimization Filter for Trend Based Short-Term Forecasting evaluates trend/filter choices by the forecasts they generate. This is the closest Journal of Forecasting precedent for the claim that trend extraction should be judged by predictive consequences.

### Staněk (2023)

Optimal Out-of-Sample Forecast Evaluation under Stationarity formalizes pseudo-out-of-sample loss, including rolling and fixed schemes, and emphasizes that forecast evaluation depends on the horizon and updating design. This is a direct foundation for the chronology of \(F_{d,L,h}(S)\).

### Wolff and Echterling (2024)

Stock Picking with Machine Learning uses validation forecast error and time-series cross-validation to select regularization/hyperparameters. It is evidence that the journal treats predictive tuning itself as a legitimate part of forecasting methodology.

### Franjic and Schweikert (2025)

Predictor Preselection for Mixed-Frequency Dynamic Factor Models proposes a new cross-validation procedure that links selection directly to nowcast performance. This is an especially useful journal-facing precedent for an endogenous forecast-error selection criterion.

### Xu, Aschakulporn, and Zhang (2025)

Modeling and Forecasting the CBOE VIX with the TVP-HAR Model studies bandwidth and smoothing-variable choices and their consequences for forecasting. It supports the importance of smoothing/tuning choices for predictive performance.

## How to state the gap

Avoid:

> No one has selected smoothing by forecast error before.

That is false.

Avoid:

> This is the first use of cross-validation to choose a smoothing parameter in time series.

Hart already prevents this claim.

Prefer:

> Existing work provides controlled-smoothness finite-difference PLS on one side and predictive tuning of smoothing, bandwidth, and model hyperparameters on the other. We connect these strands by defining the controlled smoothness percentage itself through a horizon-specific chronological future-block forecast criterion for finite-difference penalized trends.

This is narrower and defensible.

## Other literature strands

Keep the following in the background:
- Whittaker/Henderson finite-difference smoothing;
- CV/GCV/AIC/AICc/BIC smoothing selection;
- smoothing splines and effective degrees of freedom;
- rolling-origin forecast evaluation;
- horizon-specific model selection;
- modern Whittaker-Henderson likelihood/Bayesian formulations.

Cortés-Toto et al. is particularly important because it already asks how much smoothness standard optimality criteria induce in PLS. Our question is different: which induced smoothness is useful for later forecasting?

## Safe current contribution statement

> We extend controlled-smoothness finite-difference penalized trend estimation by selecting the normalized smoothness percentage endogenously from a horizon-specific chronological future-block forecast criterion, while preserving the trend family's native continuation rule.

No universal first claim should be made without a broader dedicated audit.
