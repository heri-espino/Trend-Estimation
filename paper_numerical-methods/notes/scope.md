> **2026-10-06 override:** Temporal correspondence of local minima across
> forecast origins is now in scope for this numerical paper. Forecasting
> decisions from the resulting branch matrices remain in
> `paper_smoothness-cv/`. Any older ownership statements below are historical.

# Scope and Boundaries

## This paper owns

- the \(S\leftrightarrow\lambda\) numerical mapping;
- derivatives \(S'(\lambda)\) and \(S''(\lambda)\);
- forecast-loss derivatives used by the smoothness search;
- stationary-point discovery on \(S\in[0,1]\);
- exact/limiting endpoint handling;
- local-minimum classification;
- epsilon-separated candidate sets;
- dense-reference benchmarking;
- comparison with the existing log-\(\lambda\) search;
- numerical robustness and stopping rules.

## This paper may vary discretely

To demonstrate that the numerical method is not tied to one arbitrary setup, it
may run the search for a controlled collection of
\[
d\in\{1,2,3,4\},
\]
several estimation windows \(L\), several forecast horizons \(h\), and a small
number of simple trend-continuation rules \(m\).

These are benchmark dimensions, not the paper's substantive contribution. The
paper does not propose an adaptive joint optimizer over \((d,L,S)\).

## This paper does not own

### Adaptive regimes

Time-varying selection
\[
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C)
\]
belongs to paper_forecast-optimal-smoothing/.

### Comparative financial trend forecasting and recurrence

AR/ARIMA, likelihood/state-space trend models, GCV-selected trends, residual AR
models, recurrence distributions, first-passage times, survival/hazard models,
and cross-asset financial interpretation belong to
paper_smoothness-recurrence/.

## Anti-scope-creep rule

A new experiment belongs here only if it helps answer at least one of:

1. Did the numerical search find the relevant minima?
2. How accurately did it locate the optimum?
3. How many evaluations/time did it require?
4. Under what surface geometry does it fail or become inefficient?
5. Are conclusions sensitive to numerical tolerances, endpoints, or
   epsilon-spacing?

If not, defer it.
