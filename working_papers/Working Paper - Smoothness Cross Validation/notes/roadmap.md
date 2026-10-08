# Smoothness Cross Validation — research roadmap

**Independent active study.** Optimize pooled historical future-block
forecast MSE to choose one normalized smoothing index \(S\in[0,1]\)
for the latest refitted trend.

1. [x] Specify fixed \(d,L,h\), historical origins and loss pooling.
2. [x] Derive kernel/nullity, SPD uniqueness at finite penalty,
   exact polynomial projection at S=1, EDF and normalized index.
3. [x] Preserve completed CP01–CP03 design and frozen simulation evidence.
4. [ ] Compare numerical optimizers for the **same** pooled objective
   under reference accuracy, narrow minima, boundary cases and time.
5. [ ] Freeze a new independent, defensible simulation protocol.
6. [ ] Compare horizon-matched tuning against one-step CV,
   classical criteria and appropriate forecasting benchmarks.
7. [ ] Audit the specific scientific contribution against
   already-published predictive smoothing methods.
8. [ ] Produce the final self-contained manuscript after
   experiments, mathematical checks and formatting verification.

Historical artifacts are preserved. Planned or redefined
experiments must never be reported as if completed.
