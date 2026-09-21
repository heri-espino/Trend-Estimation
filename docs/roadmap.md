# Library Roadmap

This file tracks library engineering. The active paper's scientific roadmap is `notes/roadmap.md`.

## Implemented

- finite-difference operators;
- pure penalized trend;
- Guerrero (2007) observed-difference plug-in estimator;
- explicitly named historical iterated-drift variant;
- spectral solution machinery;
- smoothness/lambda conversion;
- analytic first and second derivatives for the pure trend;
- train-validation selection;
- multiple-local-minimum diagnostics;
- time-weighted validation;
- rolling-origin split generation;
- log-lambda bounded minimization and Newton utilities;
- forecasting/extrapolation helpers;
- metrics, plotting, synthetic datasets, and benchmarks.

## Active library work for forecast-optimal smoothing

- differentiable future-block forecast objective;
- pooled rolling-origin objective derivatives;
- bracketed stationary-point search with Brent in log-lambda space;
- tests against finite differences and known multimodal objectives;
- nested rolling-origin selector for \((d,L,\lambda)\);
- robust random-walk/no-change forecast benchmark utilities.

## Later library work

- GCV/AICc/BIC selectors where scientifically useful;
- blocked CV for smoothing/reconstruction studies;
- trend-filtering and state-space baselines;
- richer regime/simulation generators;
- AR/ARMA/ARIMA noise models;
- multivariate or segmented smoothness only if motivated by the active research.

Portfolio/decision modules are paused until explicitly reactivated.
