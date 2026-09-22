# Checkpoint — Explore-02 Verified; Boundary Sensitivity Prepared

Date: 2026-09-22

## Verified completed run

Commit: 71422ff (ran explore)

Run:

results/forecast_optimal_smoothing/20260922T185443Z_persistence-mechanism_explore_f6b9e0c/

Metadata:

- 30 seeds;
- 1,350 (seed, phi, h) configurations;
- 26,730 outer-origin rows;
- phi in {-0.8,-0.4,0,0.2,0.4,0.6,0.8,0.9,0.95};
- h in {1,2,3,6,12};
- old search domain log-lambda in [-10,16];
- 161 derivative-discovery grid points.

The aggregate smoothness pattern reproduces the previously documented
persistence/horizon mechanism. For example, averaging across seeds at
phi=0.8, h=1:

\[
S^\star_{\rm observed}\approx0.339,\quad
S^\star_{\rm AR}\approx0.593,\quad
S^\star_{\rm latent}\approx0.798,\quad
S^\star_{\rm recovery}\approx0.940.
\]

Across all persistence values, the observed/AR/latent forecasting optima move
toward higher smoothness as horizon increases.

## Remaining caveat

The completed Explore-02 run is not sufficient to close the mechanism result,
because a material fraction of optima hit the finite [-10,16] search
boundaries. This is a numerical-domain question, not a reason to discard the
scientific pattern.

## Next experiment prepared

Exploration 03 is documented in:

notes/experiments/03_search-boundary-sensitivity.md

Run:

~~~powershell
python experiments\forecast_optimal_smoothing\run_persistence_mechanism.py --preset boundary
~~~

This repeats the same Explore-02 grid/seeds while changing only:

\[
\log\lambda\in[-18,24],
\qquad
n_{\rm grid}=321.
\]

Row-level outputs now store all four selected lambda-star values and the
summary records lower/upper-boundary fractions by objective.

## Decision after the run

If the qualitative mechanism survives and the boundary behavior is resolved or
shown to be genuinely limiting, proceed immediately to the first within-series
regime-transition experiment tracking the full adaptive configuration

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h}).
\]

If the mechanism changes materially under the wider domain, diagnose objective
geometry/root discovery before proceeding.