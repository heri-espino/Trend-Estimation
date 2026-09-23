# Exploration 06 — Observation-Noise-Scale Adaptation

## Scientific question

Persistence is now closed for the exploratory stage. The next isolated
mechanism asks whether the forecast-optimal configuration and the value of
re-selection respond to a change in **observation-noise scale** when serial
dependence and latent-trend roughness are held fixed.

The adaptive object remains

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h}).
\]

## Isolation

Change only

\[
\sigma_\varepsilon:0.25\leftrightarrow0.75.
\]

Hold fixed:

- AR(1) persistence: phi = 0;
- latent slope-noise std: 0.01;
- level shift: 0;
- slope shift: 0;
- n=300;
- regime point T0=180.

The 0.25/0.75 pair gives a threefold change in observation-noise standard
deviation without simultaneously introducing predictable AR residuals. It is
large enough for a mechanism study but less extreme than a near-degenerate
clean/noisy comparison.

## Paired paths

- stable_low_noise: 0.25 -> 0.25;
- low_to_high_noise: 0.25 -> 0.75;
- high_to_low_noise: 0.75 -> 0.25;
- stable_high_noise: 0.75 -> 0.75.

For a fixed seed, each transition and its matched start control are identical
before T0.

## Forecast protocol

Use the exploratory selector-memory protocol

\[
M=20
\]

with:

- 30 seeds;
- horizons {1,3,6,12};
- orders {1,2,3};
- estimation windows {24,48,72};
- inner step 3;
- outer step 3;
- log-lambda in [-18,24];
- 321 numerical discovery points.

## Combined design

Unlike the earlier persistence sequence, this runner records both scientific
levels in one pass.

### Configuration tracking

For each transition, compare the adaptive configuration at the same
seed/horizon/origin with:

1. the matched stationary start-regime control;
2. the matched stationary target-regime control.

Track:

- smoothness progress;
- absolute smoothness gap to target;
- order match to target;
- window match to target;
- joint (d,L) match to target;
- selected-window post-regime fraction;
- 50% and 80% sustained smoothness adaptation delays.

### Adaptation value

Compare:

- adaptive: re-select (d,L,lambda) every outer origin;
- frozen-pre: select once at T0 using only pre-change data, then refit with
  those hyperparameters as data arrive;
- no-change benchmark.

The direct metric is

\[
R_{A/F}
=
\sqrt{\frac{\sum e_A^2}{\sum e_F^2}}.
\]

The regime-specific metric remains

\[
\Delta A
=
A_{transition}-A_{matched\ stable\ control},
\qquad
A=MSE_{frozen}-MSE_{adaptive}.
\]

## Expected mechanism, not a required result

Higher observation noise should generally make stronger smoothing more
attractive, but the experiment must not assume a monotone rule for all
(h,d,L). The goal is to measure the joint forecast-optimal response rather
than impose it.

## Command

First:

~~~powershell
python experiments\forecast_optimal_smoothing\run_noise_scale_adaptation.py --preset smoke
~~~

If successful:

~~~powershell
python experiments\forecast_optimal_smoothing\run_noise_scale_adaptation.py --preset explore
~~~

## Outputs

- noise_adaptation_grid.csv;
- noise_adaptive_value_summary.csv;
- noise_paired_adaptation_value.csv;
- noise_paired_adaptation_value_summary.csv;
- noise_adaptive_value_seed_summary.csv;
- noise_paired_adaptation_value_seed_summary.csv;
- noise_target_tracking.csv;
- noise_target_tracking_path.csv;
- noise_target_tracking_summary.csv;
- run_metadata.json.

## Decision rule

If the transition paths move toward their target controls and adaptive
re-selection shows direct or transition-specific OOS value, observation-noise
scale becomes a second demonstrated regime mechanism.

If the configuration moves but adaptation value is weak, retain that
distinction explicitly. A changing forecast-optimal configuration does not by
itself imply economically or statistically meaningful value from re-selection.

After this experiment, the next isolated factor is latent-trend roughness.