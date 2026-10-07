# Checkpoint 07 — Dynamic roughness simulation

**Status: FROZEN BEFORE RUN.**

CP07 fixes d=2 so the experiment isolates smoothness selection from the separate instability of higher-order polynomial continuation.

The simulation compares the frozen dynamic rule `recency_hl3`, the newest tracked minimum `last`, and pooled forecast-CV under latent trends whose local roughness is either stationary or changes through time.

The primary question is whether temporal tracking adds value specifically when the forecast-optimal amount of smoothing is nonstationary.

## Frozen design

- d = 2
- L = 120
- horizon = 20
- 8 non-overlapping outer tests
- 30 historical paired Val1/Val2 origins
- tracking epsilon = 0.10
- candidate spacing = 0.02
- at most 5 initial branches
- frozen dynamic rule = `recency_hl3`
- branch selection uses historical log-RMSE on Val2

Latent log-level trends follow a local slope process with time-varying slope-innovation scale. Regimes are:

1. stationary smooth;
2. stationary rough;
3. abrupt smooth-to-rough switch;
4. abrupt rough-to-smooth switch;
5. gradual roughening;
6. gradual smoothing.

Observation noise levels are 0.01 and 0.03 on the log scale. The paper preset uses 100 seeds per regime/noise combination.

Primary comparison is dynamic versus pooled log-RMSE, reported separately for stationary and changing-roughness mechanisms. Secondary comparisons include dynamic versus last and distance to a simulation-only latent-future oracle smoothness.

No parameter is changed after the paper preset is observed.
