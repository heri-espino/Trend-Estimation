# Decisions Log

## R001 — Applied paper is parked

**Date:** 2026-09-30  
**Status:** frozen.

No new experiments are run for this paper until
paper_numerical-smoothness-selection/ is finished.

## R002 — Numerical method is external to this paper

Forecast-optimal smoothness may be used here, but its algorithmic development
and validation belong to the numerical paper.

## R003 — Trend path is frozen at forecast origin

At origin \(T\), every method constructs its reference path using only
\(\mathcal F_T\). Future observations score the path and determine recurrence;
they do not update it retrospectively.

## R004 — Keep the model set small

AR/ARIMA, GCV, likelihood/state-space, forecast-optimal PLS, residual-AR, and
no-change are candidate principles. The goal is not a large model zoo.

## R005 — Recurrence is not automatically mean reversion

Use first-passage/recurrence language unless stationarity or mean-reversion
claims are separately established.

## R006 — Test is untouched

Model/hyperparameter choices use development/validation data. Final test data
are used only once the protocol is frozen.
