# Checkpoint — Final 1,000-Seed Paper Monte Carlo

Date: 2026-09-29

Status: **PASS; main simulation conclusions are stable at 1,000 seeds**

Run:

`results/forecast_optimal_smoothing/paper_mc_v1/`

Result commit:

`2aa304e` — `results: add final 1000-seed paper Monte Carlo`

## Completion and design integrity

The run completed all **100/100** atomic batches:

- seeds: 0--999;
- 1,000 seeds per mechanism;
- three mechanisms: persistence, observation-noise scale, latent-trend roughness;
- four paths per mechanism: stable-low, low-to-high, high-to-low, stable-high;
- horizons: 1, 3, 6, 12;
- adaptive selector: M=20;
- primary fixed comparator: frozen-all-pre;
- secondary fixed comparator: frozen-local-M20;
- external benchmark: no-change;
- difference orders: 1, 2, 3;
- windows: 24, 48, 72;
- log-lambda domain: [-18,24];
- 321-point discovery grid.

The manifest and final aggregate share one design hash and one code signature.
No incomplete batch is present.

## 1. Direct adaptive value versus the strong fixed comparator

The table below reports pooled

[
R_{A/F}
=
sqrt{
rac{sum e_A^2}{sum e_{F,mathrm{all-pre}}^2}
}.
]

Values below one favor adaptive re-selection.

| Mechanism | Direction | h=1 | h=3 | h=6 | h=12 |
|---|---|---:|---:|---:|---:|
| persistence | high -> low | 0.859 | 0.863 | 0.882 | 0.876 |
| persistence | low -> high | 0.798 | 0.921 | 0.990 | 0.999 |
| noise scale | high -> low | 0.796 | 0.776 | 0.779 | 0.800 |
| noise scale | low -> high | 1.011 | 0.992 | 0.982 | 0.970 |
| roughness | high -> low | 0.995 | 0.981 | 0.971 | 0.954 |
| roughness | low -> high | 0.671 | 0.706 | 0.710 | 0.765 |

The largest direct gains occur when latent roughness increases
(smooth -> rough), followed by high -> low observation noise and high -> low
persistence.

## 2. Transition-specific adaptation value

For each transition and its matched stationary start-regime control, define

[
A=MSE_F-MSE_A,
qquad
Delta A=A_{mathrm{transition}}-A_{mathrm{control}}.
]

Primary results use frozen-all-pre.

### Persistence

| Direction | h | mean Delta A | approx. 95% MC interval | median | positive seeds |
|---|---:|---:|---:|---:|---:|
| low -> high | 1 | +0.0828 | [0.0778, 0.0878] | +0.0820 | 87.3% |
| low -> high | 3 | +0.0325 | [0.0285, 0.0365] | +0.0244 | 68.6% |
| low -> high | 6 | -0.0104 | [-0.0148, -0.0061] | -0.0137 | 39.2% |
| low -> high | 12 | -0.0341 | [-0.0432, -0.0250] | -0.0309 | 39.0% |
| high -> low | 1 | +0.1389 | [0.1309, 0.1470] | +0.1248 | 89.4% |
| high -> low | 3 | +0.1189 | [0.1106, 0.1272] | +0.1073 | 86.4% |
| high -> low | 6 | +0.0849 | [0.0773, 0.0926] | +0.0587 | 77.8% |
| high -> low | 12 | +0.0701 | [0.0597, 0.0804] | +0.0497 | 66.1% |

Thus the extra value caused by a persistence change is strongly directional.
High -> low is positive at every horizon. Low -> high is positive at short
horizons but becomes negative at h=6 and h=12.

### Observation-noise scale

| Direction | h | mean Delta A | approx. 95% MC interval | median | positive seeds |
|---|---:|---:|---:|---:|---:|
| low -> high | 1 | -0.0163 | [-0.0229, -0.0098] | -0.0251 | 37.4% |
| low -> high | 3 | +0.0079 | [0.0043, 0.0115] | +0.0054 | 53.7% |
| low -> high | 6 | +0.0238 | [0.0188, 0.0287] | +0.0170 | 59.2% |
| low -> high | 12 | +0.0503 | [0.0400, 0.0606] | +0.0411 | 61.3% |
| high -> low | 1 | +0.0451 | [0.0394, 0.0508] | +0.0449 | 75.2% |
| high -> low | 3 | +0.0363 | [0.0337, 0.0389] | +0.0360 | 82.8% |
| high -> low | 6 | +0.0450 | [0.0416, 0.0484] | +0.0445 | 80.2% |
| high -> low | 12 | +0.0683 | [0.0616, 0.0749] | +0.0550 | 74.7% |

High -> low noise has robust positive transition-specific adaptation value.
Low -> high noise is harmful at h=1, near-zero/small at h=3, and modestly
positive at longer horizons.

### Latent-trend roughness

| Direction | h | mean Delta A | approx. 95% MC interval | median | 10% trimmed | positive seeds |
|---|---:|---:|---:|---:|---:|---:|
| low -> high | 1 | +0.442 | [0.242, 0.642] | +0.075 | +0.144 | 73.0% |
| low -> high | 3 | +0.382 | [0.308, 0.456] | +0.103 | +0.163 | 85.3% |
| low -> high | 6 | +0.465 | [0.374, 0.556] | +0.110 | +0.188 | 76.8% |
| low -> high | 12 | +0.610 | [0.480, 0.740] | +0.067 | +0.193 | 60.2% |
| high -> low | 1 | -0.003 | [-0.010, 0.004] | +0.014 | +0.012 | 63.5% |
| high -> low | 3 | +0.000 | [-0.009, 0.009] | +0.022 | +0.021 | 76.8% |
| high -> low | 6 | +0.007 | [-0.008, 0.022] | +0.042 | +0.040 | 78.4% |
| high -> low | 12 | +0.009 | [-0.040, 0.057] | +0.107 | +0.108 | 76.7% |

Smooth -> rough remains the strongest demonstrated adaptation mechanism.
Its seed distribution is heavy-tailed: the mean is much larger than the
median and 10% trimmed mean. This tail structure must be reported rather than
summarized only by the mean.

Rough -> smooth has direct adaptive gains at longer horizons, but its
transition-specific mean is statistically near zero. The direct gain largely
reflects advantages that are also present in the matched stationary
high-roughness control.

## 3. No-change benchmark boundary

Adaptive re-selection beats the no-change benchmark in almost every transition
cell. The important exception is positive-persistence short-horizon forecasting:

- persistence low -> high, h=1: relative RMSFE = **1.134**;
- stable high persistence, h=1: relative RMSFE = **1.039**.

Therefore beating a fixed trend configuration does not imply beating the
no-change forecast. This is a useful validity boundary for the paper.

## 4. Configuration tracking

Late-regime joint (d,L) target-match shares remain high enough to establish
that the complete configuration moves with regime, not only smoothness.

Representative late joint match ranges:

- persistence: about 0.78--0.86;
- noise scale: about 0.80--0.90;
- roughness: about 0.57--0.79.

Persistence has the clearest smoothness separation between stationary regimes.
Its estimated 50%/80% adaptation delays are:

- high -> low: 18--30 / 39--51 observations across horizons;
- low -> high: 45--57 / 57--66 observations.

This confirms the directional adaptation asymmetry discovered in the
exploratory runs.

Noise-scale and roughness stationary smoothness shifts are much smaller
(roughly 0.018--0.031), so exact normalized delay ratios should remain
secondary to target gaps and discrete (d,L) match rates.

## 5. Monte Carlo convergence

The principal qualitative conclusions are already stable.

For persistence and noise-scale transition-specific excess effects, estimates
at 500 and 1,000 seeds differ only modestly.

Roughness smooth -> rough is the main exception in magnitude: its mean
transition-specific excess changes by roughly 0.045--0.057 between 500 and
1,000 seeds for several horizons. This is explained by the strongly
right-skewed seed distribution. The sign, median, trimmed mean, positive-seed
share, and direct adaptive/fixed RMSE ratio remain qualitatively stable.

Direct adaptive/frozen-all-pre ratios change only by a few hundredths between
500 and 1,000 seeds; the largest observed movement is about 0.03.

## 6. Decision on 3,000 seeds

**1,000 seeds are sufficient for the main paper-scale conclusions.**

An extension to 3,000 seeds is not required to determine the direction or
existence of the main effects. It would primarily improve precision for the
heavy-tailed magnitude of smooth -> rough roughness adaptation.

If compute is cheap and available, extending the same run-id to 3,000 is useful
as a Monte Carlo precision upgrade, but it should not be presented as a new
scientific experiment and should not delay the external-data stage.

## Scientific conclusion

The final simulation supports the central Level-II/Level-III claim in a
qualified form:

> Forecast-optimal (d,L,S) changes systematically with local regime and
> horizon. Adaptive re-selection can materially improve untouched future
> forecasts relative to a strong fixed configuration, but the value of
> adaptation is mechanism-, direction-, and horizon-dependent.

The paper must not claim universal superiority of adaptation.
