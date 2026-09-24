# Checkpoint — Latent-Trend Roughness Adaptation Results

Date: 2026-09-23

Status: **PASS as a third configuration mechanism; fixed-baseline stress test required before final paper-scale simulation**

Run:

`results/forecast_optimal_smoothing/20260924T011516Z_roughness-adaptation_explore_42f5ac4/`

Commit containing the run: `67691cc` (`ran`).

## Design

- 30 paired seeds;
- latent slope-noise std transitions 0.005 <-> 0.02;
- fixed observation-noise std = 0.5;
- fixed AR(1) phi = 0;
- no level or slope shifts;
- selector memory M=20;
- horizons {1,3,6,12};
- 18,720 post-T0 outer-origin rows;
- elapsed time about 1,851 s (30.9 min).

## Configuration response

The stationary controls show the expected broad direction:

- higher latent roughness generally selects less normalized smoothing;
- lower latent roughness generally selects more smoothing.

Both transition directions move toward their matched target controls.

Late target-match shares (relative origin >=72) are:

| direction | h | order | window | joint (d,L) |
|---|---:|---:|---:|---:|
| low_to_high_roughness | 1 | 0.796 | 0.821 | 0.752 |
| low_to_high_roughness | 3 | 0.767 | 0.785 | 0.719 |
| low_to_high_roughness | 6 | 0.749 | 0.762 | 0.664 |
| low_to_high_roughness | 12 | 0.700 | 0.723 | 0.618 |
| high_to_low_roughness | 1 | 0.773 | 0.740 | 0.677 |
| high_to_low_roughness | 3 | 0.865 | 0.708 | 0.681 |
| high_to_low_roughness | 6 | 0.836 | 0.689 | 0.647 |
| high_to_low_roughness | 12 | 0.818 | 0.687 | 0.610 |

Late mean smoothness also moves toward the target control. For example, at
h=6:

- smooth-to-rough: transition S=0.942, target S=0.948, start S=0.988;
- rough-to-smooth: transition S=0.988, target S=0.988, start S=0.948.

Thus latent-trend roughness is a third distinct mechanism that changes the
forecast-optimal full configuration.

## Direct adaptive versus frozen-pre value

Pooled RMSE ratios

\[
R_{A/F}=\sqrt{\frac{\sum e_A^2}{\sum e_F^2}}
\]

are:

| direction | h=1 | h=3 | h=6 | h=12 |
|---|---:|---:|---:|---:|
| low_to_high_roughness | 0.603 | 0.608 | 0.645 | 0.706 |
| high_to_low_roughness | 0.948 | 0.927 | 0.928 | 0.909 |

The smooth-to-rough transition shows a large direct adaptive advantage at every
horizon. The rough-to-smooth transition shows only modest pooled gains.

## Matched-control excess and a newly exposed baseline problem

The mean matched-control excess

\[
\Delta A=A_{transition}-A_{matched\ stable\ control}
\]

is:

| direction | h=1 | h=3 | h=6 | h=12 |
|---|---:|---:|---:|---:|
| low_to_high_roughness | +0.623 | +0.601 | +0.629 | +0.812 |
| high_to_low_roughness | -0.704 | -0.724 | -0.757 | -0.780 |

The low-to-high result is positive at the seed level for 22/30, 25/30, 25/30,
and 21/30 seeds. Approximate t intervals for the seed-level mean excess remain
above zero at all four horizons.

The high-to-low mean excess is **not representative of a typical seed**.
A few stationary-high-roughness seeds produce catastrophic loss for the
one-time frozen-pre configuration and dominate the arithmetic mean.

Robust diagnostics for high-to-low roughness are:

| h | mean Delta A | median | 10% trimmed mean | positive seeds | minimum |
|---:|---:|---:|---:|---:|---:|
| 1 | -0.704 | -0.014 | -0.038 | 12/30 | -18.80 |
| 3 | -0.724 | +0.020 | +0.015 | 21/30 | -20.74 |
| 6 | -0.757 | +0.029 | +0.023 | 23/30 | -20.68 |
| 12 | -0.780 | +0.082 | +0.017 | 21/30 | -20.25 |

Therefore the negative pooled transition-specific excess is driven by a small
number of extreme stationary-control failures rather than a uniform
high-to-low disadvantage.

## Why frozen-pre is fragile here

`frozen-pre` chooses (d,L,lambda) once at T0 using the same capped M=20 inner
origins as the adaptive selector, then never revisits that choice.

Under high latent roughness, a single finite-sample choice at T0 can be poor.
Repeated re-selection can then produce a very large gain even on
`stable_high_roughness`, where no regime change occurs.

This means `frozen-pre` is useful as a realistic local one-time-tuning
baseline, but it is not strong enough to be the only nonadaptive comparator
in the final paper.

## Scientific conclusion

Roughness completes the exploratory mechanism triad:

1. serial dependence;
2. observation-noise scale;
3. latent-trend roughness.

The first scientific claim is now well supported:

> forecast-optimal (d,L,S) is regime dependent across several distinct
> mechanisms.

The adaptation-value claim remains deliberately narrower:

> adaptive re-selection can improve OOS forecasts, sometimes substantially,
> but the magnitude and transition-specific value depend on mechanism,
> direction, horizon, and the strength of the fixed comparator.

## Required next step before final scale

Do **not** add another isolated regime factor.

Instead strengthen the nonadaptive baseline. At minimum compare adaptive
selection against:

1. current `frozen-local-M20`: one selection at T0 using M=20 inner origins;
2. `frozen-all-pre`: one selection at T0 using **all available pre-T0 inner
   rolling origins** (`max_origins=None`), then keep the selected
   hyperparameters fixed while refitting the state;
3. no-change.

`frozen-all-pre` deliberately gives the fixed method more historical
validation evidence than the adaptive selector and should reduce one-shot
selection variance. If the main adaptive conclusions survive, the final
paper-scale experiment can include both fixed baselines confidently.

A calibration-panel global fixed configuration can be added later if needed,
but first test whether all-pre selection already resolves the fragility.