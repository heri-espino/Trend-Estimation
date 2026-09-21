# Nested Rolling-Origin Forecast Evaluation

## Question

How do we estimate genuine out-of-sample performance after using the past to
select difference order \(d\), window length \(L\), and smoothing penalty
\(\lambda\)?

A single train/validation split is not sufficient for the active paper because
it can make the selected smoothness depend on one historical episode. Using
future outer observations during tuning would also create look-ahead bias.

## Outer/inner separation

At outer origin \(T\), define the available information as

\[
\mathcal I_T=\{y_1,\ldots,y_T\}.
\]

The inner selector receives only \(\mathcal I_T\). It selects

\[
(d_T^\star,L_T^\star,\lambda_T^\star)
\]

using rolling forecast errors wholly contained inside \(\mathcal I_T\).

Only after selection is complete do we fit the selected model on

\[
y_{T-L_T^\star+1:T}
\]

and produce

\[
\widehat y_{T+1:T+h\mid T}.
\]

The outer future block

\[
y_{T+1:T+h}
\]

is then revealed solely for scoring.

Therefore the information flow is

\[
\boxed{
y_{1:T}
\;\longrightarrow\;
\text{inner selection}
\;\longrightarrow\;
\text{outer forecast}
\;\longrightarrow\;
\text{reveal }y_{T+1:T+h}
\;\longrightarrow\;
\text{score}.
}
\]

## Why inner windows are fixed-width

For a candidate window \(L\), all inner origins fit exactly \(L\)
observations. This keeps the mapping

\[
\lambda
\longleftrightarrow
S_d(\lambda;L)
\]

consistent across the inner objective.

See `notes/window_and_smoothness.md`.

## Outer benchmark

For a price-level or persistence-like series, the basic no-change benchmark is

\[
\widehat y^{(0)}_{T+k\mid T}=y_T,
\qquad k=1,\ldots,h.
\]

The pooled relative forecast error is reported as

\[
\boxed{
RMSFE_{rel}
=
\frac{RMSFE_{method}}
{RMSFE_{no-change}}.
}
\]

For price-level experiments, a value below one means lower pooled RMSFE than
the no-change forecast. It does not by itself imply economic profitability.

## Library mapping

- `src/trend_estimation/selection/forecast_optimal.py`:
  inner fixed-window selection.
- `src/trend_estimation/validation/nested_forecast.py`:
  outer chronological evaluation.
- `src/trend_estimation/benchmarks/naive.py`:
  no-change benchmark.
- `src/trend_estimation/forecasting/objectives.py`:
  inner future-block forecast objective.
- `src/trend_estimation/validation/rolling_origin.py`:
  temporal split generation.

## Tests

`tests/test_nested_forecast.py` contains a direct leakage-invariance check:
two series with identical history but deliberately different outer future
values must produce exactly the same selected hyperparameters and forecast at
that origin.

## Status

- inner selector: implemented;
- outer nested evaluator: implemented;
- no-change benchmark: implemented;
- leakage-invariance test: added;
- multi-horizon experimental grid: pending;
- return/trend-change targets: pending;
- formal predictive-accuracy inference: pending.
