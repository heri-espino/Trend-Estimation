# Exploration 04B — Inner-Selector Memory Sensitivity

## Why this follow-up is required

Exploration 04 established that the selected forecasting configuration

\[
\Theta^\star_{T,h}=(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
\]

moves toward the new persistence regime after a within-series change.

However, the observed adaptation delay is partly confounded by the memory of
the **inner rolling validation objective**.

The Explore-04 selector retained 30 inner origins with inner step 3. Those
origins span roughly 87 observations, and the last pre-regime validation
origins do not leave the selector until roughly 90-99 observations after T0
depending on horizon. This closely matches the slow low_to_high adaptation
delays.

Before interpreting adaptation delay as a property of (d,L,S), isolate the
selector-memory effect.

## Status of selector memory

Selector memory is a **validation-protocol parameter**, not currently a fourth
coordinate of the canonical scientific object. The point of this experiment
is to determine whether it can be fixed at a defensible value before the
adaptive-versus-fixed forecast comparison.

If the evidence shows that selector memory itself must adapt to regime, the
canonical object can be reconsidered later. Do not expand the main notation
prematurely.

## Design

Repeat the exact paired persistence-transition design from Exploration 04:

- stable_low: 0 -> 0;
- low_to_high: 0 -> 0.8;
- high_to_low: 0.8 -> 0;
- stable_high: 0.8 -> 0.8;
- 30 seeds;
- n=300;
- T0=180;
- horizons {1,3,6,12};
- orders {1,2,3};
- windows {24,48,72};
- log-lambda in [-18,24];
- 321 derivative-discovery points.

Change only

\[
M=\text{max inner origins}
\in\{5,10,20,30\}.
\]

With inner step 3, the nominal validation-origin spans are approximately:

| M | nominal span |
|---:|---:|
| 5 | 12 observations |
| 10 | 27 |
| 20 | 57 |
| 30 | 87 |

The row-level output records the actual earliest/latest inner origin and the
fraction of retained inner validation origins that are post-regime, so the
analysis need not rely only on the nominal span.

## Primary questions

1. Does smoothness adaptation delay scale with selector memory M?
2. Does the directional asymmetry high_to_low versus low_to_high persist at
   short M?
3. How much target-regime tracking is gained by shortening M?
4. Does short selector memory make d, L, and S materially noisier on the two
   stationary controls?
5. What forecast-accuracy cost is paid for faster adaptation?
6. Is there a selector-memory value that gives a useful adaptation/variance
   tradeoff across horizons?

## Critical comparison

For low_to_high in Exploration 04, the 80% adaptation delays were

\[
(84,84,96,99)
\]

for h=(1,3,6,12).

Under M=30, all retained inner validation origins become post-regime at
approximately (90,90,93,99) observations after T0. The near-coincidence is the
main motivation for this sensitivity study.

If the low_to_high delays collapse roughly with the shorter M values, that
will show that the previous delay primarily measured validation-memory
inertia. If they remain long even for M=5 or 10, then the fitted-window/model
dynamics are doing more of the work.

## Forecast-accuracy tradeoff

Faster adaptation is not automatically better. Short M uses fewer validation
blocks to choose (d,L,S), so the selected configuration may have larger
variance.

The experiment therefore reports pooled relative RMSFE versus no-change by:

- selector memory;
- transition path;
- horizon;
- pre / early / mid / late phase.

The preferred protocol must be based on both adaptation and untouched OOS
forecast behavior, not on adaptation speed alone.

## Outputs

The runner writes:

- memory_transition_grid.csv;
- memory_paired_controls.csv;
- memory_adaptation_path.csv;
- memory_adaptation_summary.csv;
- memory_skill_summary.csv;
- run_metadata.json.

## Command

First a smoke run:

~~~powershell
python experiments\forecast_optimal_smoothing\run_selector_memory_sensitivity.py --preset smoke
~~~

Then the full exploration:

~~~powershell
python experiments\forecast_optimal_smoothing\run_selector_memory_sensitivity.py --preset explore
~~~

## Decision after this experiment

Freeze a selector-memory protocol only after comparing adaptation speed with
stationary-control stability and OOS loss.

Then run the adaptive-value experiment:

- adaptive: re-select (d,L,S) at each outer origin;
- frozen-pre: select (d,L,S) at T0 using only pre-change information and keep
  those hyperparameters fixed while continuing to refit on new observations;
- no-change benchmark;
- paired stable-regime controls.

The transition-minus-stable-control comparison will isolate value attributable
to adaptation rather than generic repeated hyperparameter estimation.