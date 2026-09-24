# Exploration 07 — Latent-Trend Roughness Adaptation

## Scientific question

After persistence and observation-noise scale, isolate a third regime factor:
the local roughness of the latent trend itself.

The adaptive object remains

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h}).
\]

## Isolation

Change only the standard deviation of slope innovations:

\[
\sigma_{\Delta slope}:0.005\leftrightarrow0.02.
\]

Hold fixed:

- observation-noise std: 0.5;
- AR(1) phi: 0;
- level shift: 0;
- slope shift: 0;
- n=300;
- regime point T0=180.

The fourfold roughness change is large enough to separate regimes without
turning either side into an almost deterministic or explosively rough trend.

## Paired paths

- stable_low_roughness: 0.005 -> 0.005;
- low_to_high_roughness: 0.005 -> 0.02;
- high_to_low_roughness: 0.02 -> 0.005;
- stable_high_roughness: 0.02 -> 0.02.

For a fixed seed, each transition and its matched start control are identical
before T0.

## Forecast protocol

Use the same exploratory protocol as Exploration 06:

- 30 seeds;
- selector memory M=20;
- horizons {1,3,6,12};
- orders {1,2,3};
- estimation windows {24,48,72};
- inner step 3;
- outer step 3;
- log-lambda in [-18,24];
- 321 discovery points.

## Outputs and estimands

The runner mirrors Exploration 06 and records both:

1. **configuration tracking** toward matched stationary target controls;
2. **forecast value** of adaptive re-selection relative to frozen-pre.

Tracking outputs include:

- smoothness path and absolute target gap;
- order/window/joint target matches;
- selected-window post-regime fraction;
- 50%/80% progress diagnostics when the stationary control separation is
  numerically large enough to interpret.

Forecast-value outputs include:

\[
R_{A/F}
=
\sqrt{\frac{\sum e_A^2}{\sum e_F^2}}
\]

and the matched-control excess

\[
\Delta A
=
A_{transition}-A_{matched\ stable\ control}.
\]

## Expected mechanism, not an imposed rule

A rougher latent trend should generally make aggressive smoothing less
attractive and may favor shorter estimation memory. Conversely, a smoother
latent trend may support stronger smoothing and longer memory.

Those are hypotheses only. The experiment evaluates the joint
forecast-optimal response and should retain any non-monotone behavior.

## Command

First:

~~~powershell
python experiments\forecast_optimal_smoothing\run_roughness_adaptation.py --preset smoke
~~~

If successful:

~~~powershell
python experiments\forecast_optimal_smoothing\run_roughness_adaptation.py --preset explore
~~~

## Outputs

- roughness_adaptation_grid.csv;
- roughness_adaptive_value_summary.csv;
- roughness_paired_adaptation_value.csv;
- roughness_paired_adaptation_value_summary.csv;
- roughness_adaptive_value_seed_summary.csv;
- roughness_paired_adaptation_value_seed_summary.csv;
- roughness_target_tracking.csv;
- roughness_target_tracking_path.csv;
- roughness_target_tracking_summary.csv;
- run_metadata.json.

## Decision after this experiment

If roughness also moves the full configuration toward target controls, the
paper will have three distinct simulated mechanisms:

1. serial dependence;
2. observation-noise scale;
3. latent-trend roughness.

At that point stop adding isolated factors unless a specific scientific gap
remains. The next priority should be freezing the paper-scale simulation
design and moving toward external macroeconomic evidence.