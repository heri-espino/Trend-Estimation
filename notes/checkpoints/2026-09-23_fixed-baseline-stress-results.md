# Checkpoint — Fixed-Baseline Stress Test Results

Date: 2026-09-23

Status: **PASS; frozen-all-pre is adequate as the primary fixed comparator**

Run:

`results/forecast_optimal_smoothing/20260924T031631Z_fixed-baseline-stress_explore_9ae024d/`

Commit containing the run: `dffcb79` (`ran`).

## Design

The roughness transition experiment was repeated with three forecasting
methods:

1. adaptive-M20: re-select (d,L,lambda) at every outer origin using M=20;
2. frozen-local-M20: select once at T0 using the same most-recent 20 inner
   origins and then keep hyperparameters fixed;
3. frozen-all-pre: select once at T0 using every valid pre-T0 rolling origin
   at the same inner step, then keep hyperparameters fixed;
4. no-change remains the external benchmark.

The run used 30 seeds, 4 roughness paths, 4 horizons, and 18,720 post-T0
outer-origin rows.

## Baseline stabilization

`frozen-all-pre` removes the severe stationary-high-roughness fragility seen
with `frozen-local-M20`.

On `stable_high_roughness`, pooled adaptive/fixed RMSE ratios are:

| h | adaptive / frozen-local | adaptive / frozen-all-pre |
|---:|---:|---:|
| 1 | 0.578 | 1.003 |
| 3 | 0.574 | 0.987 |
| 6 | 0.606 | 0.991 |
| 12 | 0.711 | 1.051 |

The extreme apparent advantage of adaptive over frozen-local was caused by a
small number of catastrophic one-shot local selections. With all-pre
selection, the stationary control is approximately a tie, as desired for a
strong nonadaptive comparator.

Seed-level adaptive-minus-fixed MSE advantages on stable high roughness also
become centered near zero rather than being dominated by ~20-unit outliers.

## Smooth-to-rough transition survives the stronger comparator

For low-to-high roughness (slope-noise std 0.005 -> 0.02), pooled
adaptive/frozen-all-pre RMSE ratios are:

| h | ratio |
|---:|---:|
| 1 | 0.808 |
| 3 | 0.760 |
| 6 | 0.777 |
| 12 | 0.782 |

Thus adaptive re-selection still produces a large direct OOS gain against a
fixed method given substantially more pre-regime validation evidence.

The matched transition-minus-stable-control excess advantages versus
frozen-all-pre are:

| h | mean Delta A | positive seeds | approx. 95% seed-mean interval |
|---:|---:|---:|---:|
| 1 | +0.202 | 24/30 | [0.084, 0.320] |
| 3 | +0.265 | 24/30 | [0.091, 0.440] |
| 6 | +0.303 | 25/30 | [0.057, 0.549] |
| 12 | +0.530 | 18/30 | [0.008, 1.052] |

The effect is smaller than against frozen-local, as expected, but remains
positive at every studied horizon.

## Rough-to-smooth transition becomes a near tie

For high-to-low roughness (0.02 -> 0.005), adaptive/frozen-all-pre pooled
RMSE ratios are:

| h | ratio |
|---:|---:|
| 1 | 1.017 |
| 3 | 0.996 |
| 6 | 1.001 |
| 12 | 1.019 |

The matched-control excess advantages versus frozen-all-pre are approximately
-0.008, -0.007, -0.009, and +0.067. Seed-level intervals include zero at
every horizon.

This resolves the earlier paradox: the strongly negative pooled excess under
frozen-local was a baseline-instability artifact. Against a stable fixed
comparator, rough-to-smooth adaptation is essentially neutral at the studied
sample size.

## Comparator decision

For the final paper-scale simulation:

- **primary fixed comparator:** frozen-all-pre;
- **secondary diagnostic comparator:** frozen-local-M20;
- **adaptive method:** adaptive-M20;
- **external benchmark:** no-change.

Frozen-all-pre is deliberately advantaged by using more historical validation
origins than adaptive at T0. This makes it a stronger and less attackable
nonadaptive baseline.

No independently calibrated global fixed comparator is required before final
scale unless later evidence reveals another instability.

## Compute note

This result directory records `git_commit=9ae024d` and elapsed time ~1,988 s
(33.1 min). Therefore this particular run predates the later multiprocessing
and penalty-eigenvalue-cache patches. It is scientifically valid, but it does
not benchmark the new accelerated implementation.

## Decision

The exploratory simulation phase is complete. Freeze the scientific design and
move to the final paper-scale Monte Carlo experiment.