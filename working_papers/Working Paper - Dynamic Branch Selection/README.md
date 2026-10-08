# Working Paper 2 — Dynamic Branch Selection

**Status:** independent, exploratory methodological working paper.
**Prospective algorithm redesign:** 2026-10-08.
**Working title:** *Dynamic Branch Tracking for Horizon-Matched Forecast-Loss Surfaces*.

## Central question

For a fixed forecast horizon \(h\), does tracking persistent local
minima of **temporally weighted historical forecast-loss functions**
help select a useful PLS smoothing parameter, beyond choosing the
global minimum of the latest aggregate (Paper 1)?

## Simulation study and matched Paper 1 comparison

Use the identical DGPs, external origins and baseline selectors
defined in the [shared simulation protocol](../SIMULATION_EVALUATION_PROTOCOL.md).
The decisive comparison is **tracked branches versus the global
minimum of the same method-specific weighted F**, conditional on
the same \((m,d,L,h)\). Include stationary mechanisms as negative
controls, curvature/slope changes as adaptation tests, and
compare external observed forecast MSE, latent-trend error,
smoothness, EDF, and branch stability. The new experiments
**have not been run**.

## Current proposed method

For each predeclared weighting method \(m\), difference order \(d\),
fit window \(L\), and horizon \(h\), compute the raw historical
forecast-loss curves

\[
\ell_t^{(d,L,h)}(S)
=\frac1h\|y_{t+1:t+h}-G_{d,h}H_{d,L}(S)y_{t-L+1:t}\|^2.
\]

For each completed historical update \(r\), weight the **functions**
rather than the smoothing levels:

\[
F_r^{(m,d,L,h)}(S)
=\frac{\sum_{q\in I_m(r)}w_{r,q}^{(m)}\ell_{t_q}(S)}
{\sum_{q\in I_m(r)}w_{r,q}^{(m)}},
\qquad q\le r,\quad t_r+h\le T.
\]

**Paper 2 then detects and tracks all admissible local minima of
each \(F_r\), for each method and order independently.**
One-to-one matches within a declared radius continue a branch;
unmatched minima start or end branches. A predeclared selector
\(\psi\) chooses an active branch from its **completed historical**
losses and support. A separate rule \(\phi\), initially the average
of the **last three minimizing S values** of that branch, yields
the current operational \(\widehat S_T\).

There is **no required second inner Val2**. The mean-of-three
decision is applied **after branch tracking**, not inside the
loss objective. The selected S is used to refit the final
length-\(L\) PLS trend and issue a truly unseen \(h\)-step forecast.
An **untouched outer test** remains mandatory to evaluate performance.

## Difference from Paper 1

- Paper 1: take the **global minimum of the latest complete**
  weighted \(F_M^{(m,d,L,h)}\).
- Paper 2: track **all detected local minima across the sequence**
  \(\{F_r^{(m,d,L,h)}\}\), select a branch, then map it to S.

The raw forecast losses, weighting schemes, spectral smoother, window
and horizon definitions can be **identical**. The statistical decisions
are different.

## Current implementation

- [Shared mathematical protocol](../WEIGHTED_SURFACE_PROTOCOL.md).
- [Current branch-tracking method](notes/dynamic_tracked_smoothness.md).
- [Prospective research objective](notes/research_objective.md).
- [Numerical matching issues](notes/temporal_minima_tracking.md).
- [Runnable shared implementation](../../experiments/smoothness_cv/weighted_surface_study.py).

Manual pilot, from the repository root:

~~~bash
python -m experiments.smoothness_cv.run_weighted_surface_study --quick
~~~

This produces candidate decisions and a single independent outer
holdout for comparison, **not publication-ready statistical results**.
The grid-detected minima are not numerically certified. Before
publication, use verified root-search strategies and a repeated
untouched rolling-outer test protocol.

## Historical research and provenance

The existing [manuscript](manuscript/main.tex), frozen
[CP04–CP08 checkpoints](checkpoints/), old
[Val1/Val2 two-stage notes](notes/tracked_minimum_smoothness_selection_legacy.tex),
and [recorded evidence](notes/results_and_boundaries.md) remain
available. They describe earlier and partially **different**
algorithms. Their mixed results include cases where branch tracking
was worse than pooled CV; **none should be presented as evidence
for the new weighted-\(F\) approach without rerunning it**.

Paper/PDF builds and substantial experiments remain manual.

## Build the dated draft

~~~bash
python "working_papers/Working Paper - Dynamic Branch Selection/build.py" --check
python "working_papers/Working Paper - Dynamic Branch Selection/build.py"
~~~

Building this draft does not imply that its methodology or
experiments have been updated to the newly defined protocol.
