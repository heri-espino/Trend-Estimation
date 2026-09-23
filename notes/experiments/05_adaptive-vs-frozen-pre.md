# Exploration 05 — Value of Adaptation: Adaptive vs Frozen-Pre

## Scientific role

This is the first experiment that directly tests Level III of the active paper:

\[
\text{does adapting }
\Theta^\star_{T,h}=(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
\text{ improve untouched OOS forecasts?}
\]

Explorations 01–04B established target dependence, persistence/horizon
mechanisms, numerical robustness, within-series adaptation, and the role of
inner-selector memory. Exploration 04B freezes the exploratory selector
protocol at

\[
M=20
\]

inner rolling origins.

## Methods compared

### Adaptive

At every outer origin T, use only y[:T] and re-select

\[
(d,L,\lambda)
\]

by the chronological inner forecast objective with M=20.

Then refit on the selected last L observations and forecast the untouched
future block.

### Frozen-pre

At the known simulation regime point T0, select

\[
(d_0,L_0,\lambda_0)
\]

once using only pre-change data y[:T0].

For every later outer origin, keep these three hyperparameters fixed but refit
the trend model on the most recent L0 observations before forecasting.

This comparison isolates **hyperparameter adaptation**. Frozen-pre is not a
completely frozen fitted model: its state is updated with new data, but its
method configuration is not re-selected.

Because d and L remain fixed, freezing lambda is equivalent to freezing the
corresponding normalized smoothness S for that configuration.

### No-change

Retain the no-change level forecast as the external benchmark.

## DGP and pairing

Use exactly the paired persistence design from Exploration 04:

- stable_low: 0 -> 0;
- low_to_high: 0 -> 0.8;
- high_to_low: 0.8 -> 0;
- stable_high: 0.8 -> 0.8.

Use:

- 30 seeds;
- n=300;
- T0=180;
- horizons {1,3,6,12};
- slope-noise std 0.01;
- observation-noise std 0.5;
- candidate orders {1,2,3};
- candidate windows {24,48,72};
- M=20 inner origins;
- inner step 3;
- outer step 3;
- log-lambda in [-18,24];
- 321 discovery points.

For a fixed seed, stable_low and low_to_high have identical data before T0,
and stable_high and high_to_low likewise. Therefore their frozen-pre
configuration is exactly matched at T0.

## Primary estimand

For each transition, horizon, and period, compare adaptive and frozen-pre by

\[
R_{A/F}
=
\sqrt{
\frac{\sum e^2_{\rm adaptive}}
{\sum e^2_{\rm frozen}}
}.
\]

Interpretation:

- R_A/F < 1: adaptive re-selection improves RMSE;
- R_A/F = 1: no practical difference;
- R_A/F > 1: repeated adaptation hurts.

Do not average blockwise relative RMSE values; use pooled squared errors.

## Stable-control correction

Repeated re-selection can help or hurt even when the regime does not change.
Therefore the transition result alone does not identify the value of regime
adaptation.

For each transition, use its matched stationary control and calculate the
adaptive MSE advantage

\[
A_T
=
\operatorname{MSE}_{\rm frozen}
-
\operatorname{MSE}_{\rm adaptive}.
\]

Then compare

\[
\Delta A
=
A_{\rm transition}
-
A_{\rm matched\ stable\ control}.
\]

Positive Delta A means the adaptive method gains more after the regime change
than it gains merely from continuing to re-select in a stationary series.

The runner stores this comparison at matched seed/horizon/relative-origin
level and also aggregates it by early, mid, late, and all-post periods.

## Periods

Post-change origins are divided into:

- early: 0 <= T-T0 < 36;
- mid: 36 <= T-T0 < 72;
- late: T-T0 >= 72;
- all_post: all origins after T0.

These bins align with the transition timescale observed in Explorations 04 and
04B without using future outcomes to alter the model.

## Questions

1. Does adaptive re-selection beat frozen-pre after an actual regime change?
2. Is any gain larger than the gain/cost of re-selection on the matched
   stationary control?
3. Is the value concentrated in early/mid transition periods or only after the
   selector has largely adapted?
4. Is the result asymmetric for low_to_high versus high_to_low?
5. How does adaptation value change with forecast horizon?
6. Does adaptive beat frozen-pre while also remaining competitive with the
   no-change benchmark?

## Command

First run:

~~~powershell
python experiments\forecast_optimal_smoothing\run_adaptive_value.py --preset smoke
~~~

If successful:

~~~powershell
python experiments\forecast_optimal_smoothing\run_adaptive_value.py --preset explore
~~~

The default selector memory is M=20. A robustness run can later use:

~~~powershell
python experiments\forecast_optimal_smoothing\run_adaptive_value.py --preset explore --selector-max-inner-origins 30
~~~

## Outputs

- adaptive_value_grid.csv;
- adaptive_value_summary.csv;
- paired_adaptation_value.csv;
- paired_adaptation_value_summary.csv;
- run_metadata.json.

## Decision after this experiment

If adaptive re-selection shows transition-specific OOS value beyond the stable
controls, the project has direct evidence for Level III: adaptation value.

Then repeat isolated transition/value experiments for observation-noise scale
and latent-trend roughness before freezing the final paper-scale simulation
design.

If adaptive does not beat frozen-pre, do not hide that result. The scientific
conclusion would instead be that forecast-optimal configurations move with
regime but re-selection is not automatically valuable at the studied sample
sizes and horizons.