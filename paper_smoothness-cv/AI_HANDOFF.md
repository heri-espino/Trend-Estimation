# AI Handoff — Smoothness-CV paper

## Identity

This paper answers **what amount of smoothness should be selected for forecasting?**

Its central object is

\[
S^\star_{d,L,h}
\in
\arg\min_{S\in[0,1]}
F_{d,L,h}(S),
\]

where \(F\) is chronological rolling future-block MSE from a finite-difference penalized trend plus its fixed continuation rule.

## Primary target

**Journal of Forecasting.**

The active Wiley NJDv5 manuscript is in manuscript/main.tex and is configured with

\[
\text{journal}=\text{Journal of Forecasting}.
\]

The template bundle lives under vendor/wiley_njd_v5/. Build through build.py rather than editing the vendor class.

## Foundation and literature story

Start from Guerrero, not Hart.

Guerrero supplies:
- finite-difference PLS;
- the trace-based controlled-smoothness idea;
- the mapping between smoothness and penalty;
- trend continuation/forecasting.

The extension is to choose smoothness from chronological forecast performance rather than specifying it exogenously.

Hart (1994) is a conceptual precedent for predictive smoothing selection in a different kernel-smoothing problem. It limits novelty wording but is not the same estimator.

For Journal of Forecasting positioning, the manuscript now also uses:
- Taylor (2004): smoothing parameters estimated/updated for forecasting;
- Zafar et al. (2022): trend filtering judged by forecast performance;
- Staněk (2023): rolling/fixed pseudo-out-of-sample loss and model selection;
- Wolff and Echterling (2024): forecast-error tuning of regularization/hyperparameters;
- Franjic and Schweikert (2025): cross-validation linked directly to nowcast error;
- Xu et al. (2025): bandwidth/smoothing choice affecting forecasts.

## Do not import the numerical paper

Do not make Brent, adaptive subdivision, derivative root finding, rational stationary polynomials, or Sturm the contribution here. A dense grid is acceptable for Paper A if it evaluates the scientific criterion transparently.

The numerical solver belongs to paper_numerical-methods/.

## Do not import the statistical-properties paper

Fixed-\(S\) effective degrees of freedom are useful here because

\[
\operatorname{edf}
=
L-(L-d)S.
\]

But post-selection bias, variance, uncertainty, and inference for

\[
H_{\lambda(\widehat S)}y
\]

belong to paper_statistical-properties-penalized-trend/.

## Manuscript status

The paper was rewritten on 2026-10-05 for Journal of Forecasting. The accidentally copied WTI/Journal of Futures Markets manuscript text has been removed.

The current draft contains:
1. journal-facing introduction;
2. literature positioning;
3. finite-difference PLS and normalized smoothness;
4. the forecast-optimal smoothness criterion;
5. basic mathematical properties;
6. a prespecified evaluation protocol;
7. scope and interpretation;
8. conclusion.

There are deliberately no invented result numbers.

## Immediate next task

The next scientific task is experiments, not more general prose.

Run and freeze:
1. forecast-CV versus CV/GCV/AICc/BIC;
2. forecast-optimal versus latent-trend recovery-optimal \(S\);
3. one-step versus horizon-matched tuning;
4. a public heterogeneous forecasting panel;
5. paper-final real-time macro vintages if macro examples are retained.

Do not use revised current-vintage macro history as if it were available at historical forecast origins.

## Build

Check structure:

python paper_smoothness-cv/build.py --check

Compile:

python paper_smoothness-cv/build.py

Or use the manual GitHub Actions target smoothness-cv.

## Claim rule

Safe current wording:

> Building on controlled-smoothness finite-difference penalized trend estimation, we define the smoothness percentage endogenously through a horizon-specific chronological future-block forecast criterion.

Do not claim the first predictive smoothing selector, the first forecast-based tuning method, or universal superiority over classical selectors.

## Current execution checkpoint

The active stop point is `checkpoints/CP01_EMPIRICAL_CORE.md`. Empirical code is implemented under `experiments/smoothness_cv/`. Do not invent CP01 conclusions. Wait for the user to run smoke/quick and push the exact result bundle before freezing CP02.

## Current stop point

CP01 quick has been reviewed. The active execution handoff is `checkpoints/CP02_REFINE_SIMULATION_DESIGN.md`. CP02 is implemented; wait for its smoke/refine outputs before freezing CP03.
