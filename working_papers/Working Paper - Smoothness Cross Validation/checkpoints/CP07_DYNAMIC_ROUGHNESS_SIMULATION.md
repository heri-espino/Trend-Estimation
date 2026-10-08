> **RESEARCH STATUS UPDATE — 2026-10-08 (current; original checkpoint record preserved below).** The primary current statistical question is selection of normalized PLS smoothness (S\in[0,1]) by **chronological, horizon-matched future-block forecast MSE**, with an explicit polynomial continuation and mandatory final refit. The eigenstructure of the smoother, analytic derivatives, and reliable recovery of competing minima are central mathematical/numerical topics. The source of truth is [../notes/INDEX.md](../notes/INDEX.md), [../notes/mathematical_foundations.md](../notes/mathematical_foundations.md), and [../notes/research_log_2026-10.md](../notes/research_log_2026-10.md).
>
> **Archival status:** CP07 **has been completed** and is now an **optional/exploratory historical study** of tracked minimum branches, continuation-order stability, or maps (\phi(V_j)). The main pooled forecast-CV method does not require these branches. Preserve the mixed/negative comparisons with pooled CV and the original post-hoc/confirmation boundaries. Any “central method” or “next checkpoint” text below is historical, not the current program.

---

# Checkpoint 07 — Dynamic roughness simulation

**Status: COMPLETE — central recency-smoothing hypothesis not supported against pooled CV.**

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


## Observed CP07 result

The paper preset completed 1200 scenarios and 9600 outer forecast decisions.

The frozen recency rule did **not** beat pooled forecast-CV:

[
\operatorname{gRMSE}
(\text{recency-hl3}/\text{pooled})
=
1.037
]

overall. Under changing roughness the ratio was 1.028, compared with 1.056
under stationary roughness. The difference is directionally consistent with
the dynamic motivation, but it is not enough to produce a forecasting gain.

By mechanism, dynamic / pooled geometric RMSE ratios were approximately:

- gradual roughening: 1.050;
- gradual smoothing: 1.023;
- switch to rough: 1.037;
- switch to smooth: 1.001;
- stationary rough: 1.102;
- stationary smooth: 1.012.

Against the newest tracked minimum, recency averaging remained beneficial:

[
\operatorname{gRMSE}
(\text{recency-hl3}/\text{last})
=
0.945,
]

with similar gains in stationary and changing mechanisms.

Thus the evidence now supports a narrower statement: averaging along a tracked
branch stabilizes the newest local minimum, but a backward-looking average of
branch smoothness does not outperform pooled forecast-CV even when latent trend
roughness changes.

## Consequence

The next experiment does not retune the half-life on CP07. Instead it tests a
different branch functional that was part of the original research plan:
**forecast the smoothness trajectory itself**.

CP08 uses fresh simulation seeds and treats CP07 only as motivation. Candidate
rules extrapolate the tracked branch by recent linear trend or exponentially
weighted branch increments. A later, disjoint seed set will be reserved for
confirmation after one trajectory rule is frozen.
