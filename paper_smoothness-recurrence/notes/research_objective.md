# Canonical Research Objective

**Status:** parked.

## Research question

How do alternative, established definitions of a forecast trend change both
out-of-sample forecast performance and the measured recurrence of financial
prices toward that trend?

## Forecast path

For method \(m\), origin \(T\), and only information available through \(T\),
construct
\[
\widehat\tau^{(m)}_{T+k\mid T}.
\]

The path is frozen at \(T\). Future observations may score the forecast and
determine recurrence, but may not redefine the reference path.

## Recurrence

Let
\[
g^{(m)}_{T,k}
=
x_{T+k}
-
\widehat\tau^{(m)}_{T+k\mid T}.
\]

Primary outcomes include:

\[
H_T^{(m),\mathrm{cross}}
=
\inf\{k\ge1:
g^{(m)}_{T,k}g^{(m)}_{T,0}\le0\},
\]

band-entry recurrence, probability of recurrence by a fixed horizon,
censored time-to-event summaries, and recurrence conditional on initial
standardized distance.

## Scientific questions

1. Which trend/forecasting definitions perform best on untouched future data?
2. Does the preferred method depend on forecast horizon?
3. Is measured recurrence robust to the trend definition?
4. How does recurrence depend on the initial distance from trend?
5. Are these relationships stable across ETFs, equities, and crypto?

## Methodological role of forecast-optimal PLS

Forecast-optimal PLS is one competitor. Its numerical smoothness-selection
algorithm is developed and validated in the separate
paper_numerical-smoothness-selection/ paper and is imported here as a finished
method.

This paper does not claim novelty for AR, ARIMA, GCV, state-space likelihood, or
other standard forecasting methods individually.
