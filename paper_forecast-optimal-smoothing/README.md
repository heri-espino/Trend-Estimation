# Adaptive Forecast-Optimal Trend Smoothing

**Status: PARKED until the numerical-smoothness paper is finished.**

Working title:

**Adaptive Forecast-Optimal Trend Estimation under Changing Time-Series Regimes**

This is the broad adaptive paper. It is one of three research papers in the
repository, but it is not the current focus.

## Canonical objective

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

The paper asks whether the full forecast-optimal configuration changes
systematically with horizon and local regime, and whether adapting the
configuration improves untouched out-of-sample forecasts relative to strong
fixed methods.

## Delimitation

### In scope

- time-varying/adaptive selection of \(d,L,S\);
- local regime/state descriptors \(X_T\);
- mechanism studies such as persistence, volatility, roughness, breaks, and
  horizon;
- adaptive-versus-fixed nested chronological evaluation;
- adaptation delay after regime changes.

### Out of scope

- developing the normalized-\(S\) stationary-point search as a standalone
  numerical contribution;
- broad ARIMA/MLE/GCV trend-model comparison for financial recurrence;
- first-passage/survival analysis as the main endpoint.

The standalone numerical method belongs to
paper_numerical-smoothness-selection/. Comparative financial recurrence belongs
to paper_smoothness-recurrence/.

## Status rule

Do not run new adaptive-paper experiments or expand this manuscript until
paper_numerical-smoothness-selection/ is complete.

## Read first when resumed

1. notes/research_objective.md
2. notes/scope.md
3. notes/roadmap.md
4. the detailed historical notes under ../notes/
