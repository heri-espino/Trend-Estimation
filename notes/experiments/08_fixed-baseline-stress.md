# Exploration 08 — Fixed-Baseline Stress Test

## Why this experiment exists

Exploration 07 established latent-trend roughness as a third configuration
mechanism, but it also exposed a weakness in the current nonadaptive
comparator.

`frozen-pre` selects (d,L,lambda) once at T0 using only the most recent M=20
inner origins. Under high latent roughness, a few seeds make that one-time
choice extremely poor even on the stationary high-roughness control.

Those rare failures can dominate pooled mean excess-adaptation statistics.

Before the final paper-scale simulation, test whether the adaptation result
survives a stronger fixed comparator that uses more pre-regime validation
evidence.

## Methods

Keep the same roughness DGP as Exploration 07:

- slope-noise std 0.005 <-> 0.02;
- observation-noise std 0.5;
- phi=0;
- T0=180;
- n=300;
- 30 seeds;
- horizons {1,3,6,12};
- orders {1,2,3};
- windows {24,48,72};
- inner step 3;
- outer step 3;
- log-lambda [-18,24];
- 321 discovery points.

Compare:

### Adaptive

Re-select (d,L,lambda) at every outer origin using M=20 inner origins.

### Frozen-local-M20

Current baseline: select once at T0 using the same capped M=20 inner origins
and keep hyperparameters fixed thereafter.

### Frozen-all-pre

Select once at T0 using **all valid pre-T0 rolling origins** at the same inner
step (`max_origins=None`), then keep the selected hyperparameters fixed while
continuing to refit the trend state as observations arrive.

This gives the fixed method more historical validation evidence and should
reduce one-shot selection variance.

### No-change

Keep the no-change forecast as the external benchmark.

## Primary questions

1. Does `frozen-all-pre` remove or materially reduce the catastrophic
   stationary-high-roughness failures seen under frozen-local-M20?
2. Does adaptive still beat the stronger fixed baseline on the
   smooth-to-rough transition?
3. Does the rough-to-smooth transition-specific excess become stable once the
   fixed baseline is less noisy?
4. Which fixed comparator should be carried into the paper-scale simulation?

## Command

First:

~~~powershell
python experiments\forecast_optimal_smoothing\run_fixed_baseline_stress.py --preset smoke
~~~

If successful:

~~~powershell
python experiments\forecast_optimal_smoothing\run_fixed_baseline_stress.py --preset explore
~~~

## Outputs

- baseline_stress_grid.csv;
- baseline_stress_summary.csv;
- baseline_stress_paired.csv;
- baseline_stress_paired_summary.csv;
- baseline_stress_seed_summary.csv;
- baseline_stress_seed_excess.csv;
- run_metadata.json.

## Decision after this experiment

If `frozen-all-pre` is materially more stable, include both fixed baselines in
the final paper-scale simulation and treat frozen-all-pre as the stronger
primary nonadaptive comparator.

If it remains fragile, introduce a calibration-panel global fixed
configuration before scaling. Do not proceed to the final large experiment
with only a demonstrably unstable one-time baseline.