# Checkpoint — Observation-Noise-Scale Adaptation Results

Date: 2026-09-23

Status: **PASS as a second regime mechanism; adaptation value is strongly directional**

Run:

`results/forecast_optimal_smoothing/20260924T002720Z_noise-scale-adaptation_explore_45e9c08/`

Commit containing the run: `4e43662` (`ran`).

## Design

- 30 paired seeds;
- observation-noise std transitions 0.25 <-> 0.75;
- fixed AR(1) phi = 0;
- fixed latent slope-noise std = 0.01;
- no level or slope shifts;
- selector memory M=20;
- horizons {1,3,6,12};
- 18,720 post-T0 outer-origin rows;
- elapsed time about 1,821 s (30.4 min).

## Configuration response

The stationary high-noise control generally selects slightly higher normalized
smoothness than the low-noise control. Across post-regime origins, the mean
absolute start-to-target smoothness separation is only about 0.025-0.031,
depending on horizon.

Despite that small separation, both transition directions move toward their
matched target controls in the full configuration.

Late target-match shares (relative origin >=72) are:

| direction | h | order | window | joint (d,L) |
|---|---:|---:|---:|---:|
| low_to_high_noise | 1 | 0.960 | 0.933 | 0.917 |
| low_to_high_noise | 3 | 0.965 | 0.927 | 0.902 |
| low_to_high_noise | 6 | 0.960 | 0.936 | 0.911 |
| low_to_high_noise | 12 | 0.956 | 0.882 | 0.867 |
| high_to_low_noise | 1 | 0.940 | 0.881 | 0.869 |
| high_to_low_noise | 3 | 0.981 | 0.873 | 0.858 |
| high_to_low_noise | 6 | 0.956 | 0.836 | 0.824 |
| high_to_low_noise | 12 | 0.946 | 0.815 | 0.779 |

Thus observation-noise scale is a second demonstrated mechanism that changes
the forecast-optimal joint configuration, not only lambda or S.

## Caveat on smoothness adaptation delays

The runner reports 50%/80% smoothness-progress delays, but those ratios divide
by the start-to-target smoothness separation. Because that separation is small
and occasionally changes sign at individual relative origins, the progress
ratio can become numerically unstable or very large.

Therefore do **not** make a substantive timing claim from the noise-scale
50%/80% delay table. For this mechanism, prefer:

- absolute smoothness gap to the target control;
- late order/window/joint target-match shares;
- direct adaptive-versus-frozen forecast loss.

## Direct adaptive versus frozen-pre value

Pooled RMSE ratios

\[
R_{A/F}=\sqrt{\frac{\sum e_A^2}{\sum e_F^2}}
\]

are:

| direction | h=1 | h=3 | h=6 | h=12 |
|---|---:|---:|---:|---:|
| low_to_high_noise | 1.009 | 0.972 | 0.966 | 0.943 |
| high_to_low_noise | 0.577 | 0.616 | 0.624 | 0.591 |

The high-to-low-noise transition shows a large adaptive advantage at every
horizon.

The low-to-high-noise transition is qualitatively different: adaptive is
slightly worse at h=1 and only modestly better than frozen-pre at h=3,6,12.

## Transition-specific excess adaptation value

Matched-control excess

\[
\Delta A=A_{transition}-A_{matched\ stable\ control}
\]

is:

| direction | h=1 | h=3 | h=6 | h=12 |
|---|---:|---:|---:|---:|
| low_to_high_noise | -0.0405 | +0.0060 | +0.0055 | +0.0112 |
| high_to_low_noise | +0.0583 | +0.0400 | +0.0578 | +0.0767 |

Seed-level Monte Carlo diagnostics give:

| direction | h | mean Delta A | approx. 95% interval | positive seeds |
|---|---:|---:|---:|---:|
| low_to_high_noise | 1 | -0.0405 | [-0.0686, -0.0123] | 9/30 |
| low_to_high_noise | 3 | +0.0060 | [-0.0175, 0.0295] | 15/30 |
| low_to_high_noise | 6 | +0.0055 | [-0.0275, 0.0386] | 13/30 |
| low_to_high_noise | 12 | +0.0112 | [-0.0703, 0.0927] | 13/30 |
| high_to_low_noise | 1 | +0.0583 | [0.0275, 0.0892] | 26/30 |
| high_to_low_noise | 3 | +0.0400 | [0.0248, 0.0551] | 26/30 |
| high_to_low_noise | 6 | +0.0578 | [0.0361, 0.0795] | 26/30 |
| high_to_low_noise | 12 | +0.0767 | [0.0241, 0.1292] | 24/30 |

Thus the transition-specific value is strongly asymmetric.

## Scientific conclusion

Observation-noise scale changes the forecast-optimal configuration, but
configuration movement does **not** imply that re-selection must improve
forecast loss in both directions.

The strongest result is the high-to-low-noise case: once the series becomes
cleaner, retaining a configuration chosen under high noise is costly, and
adaptive re-selection substantially improves OOS forecasts.

When noise rises, the configuration still moves toward the high-noise control,
but frozen-pre is already competitive and repeated re-selection adds little or
no transition-specific value at the studied sample size.

This strengthens the paper's intended boundary condition:

> forecast-optimal configurations are regime dependent, while the practical
> value of adaptation is itself regime-direction and horizon dependent.

## Decision

Count observation-noise scale as the second demonstrated regime mechanism.

Proceed to the third isolated factor: latent-trend roughness. Hold observation
noise and serial dependence fixed, and use the same paired tracking plus
adaptive-versus-frozen architecture.