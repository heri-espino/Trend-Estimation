# Smoothness and Financial Trend Recurrence

Working title:

**Numerical Selection of Forecast-Optimal Smoothness and Financial Trend Recurrence**

This directory is the self-contained research workspace for the compact
SMCCA-oriented paper. It is deliberately narrower than
`paper_forecast-optimal-smoothing/`.

## Read first

1. `notes/research_objective.md` — scientific source of truth.
2. `notes/roadmap.md` — execution order and stopping rules.
3. `notes/decisions.md` — frozen design decisions.
4. `notes/results.md` — results actually established for this paper.
5. latest file under `notes/checkpoints/` — chronological handoff.

## Core object

For a fixed paper protocol ((d,L)) and forecast horizon (h),

\[
S_h^\star=\arg\min_{S\in[0,1]}CV_h(S).
\]

The paper searches directly on normalized smoothness rather than treating
(lambda) as the scientific coordinate. The intended numerical method is

\[
\text{adaptive stationary-point isolation on }S
\to
\text{Brent refinement}
\to
\text{classify local minima}
\to
\text{compare all minima and endpoints}.
\]

A dense GPU smoothness grid is retained only as a validation benchmark.

## Financial application

At forecast origin (T), fit the trend using only information available through
(T), forecast the trend path, and freeze that path. Recurrence is measured
against future prices without re-estimating the reference trend using those
future observations.

Primary recurrence candidates are first crossing time, first entry into a
tolerance band, probability of recurrence by horizon, and censored
time-to-recurrence conditional on initial deviation.

Do not describe this automatically as mean reversion. Recurrence to a
time-varying forecast trend is a distinct empirical object.

## Repository boundaries

Reusable implementation belongs in `src/trend_estimation/`.
Paper-specific runners belong in `experiments/smoothness_recurrence/`.
Versioned outputs belong in `results/smoothness_recurrence/`.

## Build

~~~bash
latexmk -pdf -interaction=nonstopmode \
  -outdir=paper_smoothness-recurrence/build \
  paper_smoothness-recurrence/main.tex
~~~

The manual GitHub Actions paper builder also exposes target `recurrence`.
