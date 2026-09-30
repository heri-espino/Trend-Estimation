# Decisions Log

Design choices here should not be silently changed after results are inspected.

## D001 — Separate paper

**Date:** 2026-09-29  
**Status:** frozen.

This study is separate from `paper_forecast-optimal-smoothing/`.

## D002 — Smoothness is the scientific coordinate

**Date:** 2026-09-29  
**Status:** frozen.

The primary continuous parameter is (S\in[0,1]). (lambda) remains an
internal parameter because the estimator and existing derivatives are naturally
expressed in (lambda).

## D003 — Multiple local minima matter

**Date:** 2026-09-29  
**Status:** frozen.

Do not assume the CV objective is unimodal. Return and compare multiple local
minima plus endpoints.

## D004 — Dense grid is benchmark only

**Date:** 2026-09-29  
**Status:** frozen.

The old GPU dense smoothness grid is the numerical reference. The proposed
method is adaptive stationary-point discovery plus root refinement.

## D005 — Freeze recurrence reference at origin

**Date:** 2026-09-29  
**Status:** frozen.

At origin (T), construct (widehat\tau_{T+k\mid T}) using only
(mathcal F_T). Future prices are compared with this fixed forecast path.

## D006 — Keep the main numerical problem one-dimensional

**Date:** 2026-09-29  
**Status:** provisional until Phase 3.

The main paper optimizes (S). (d) and (L) are fixed by protocol.
Joint adaptive ((d,L,S)) selection belongs to the other paper.

## D007 — Recurrence is not automatically mean reversion

**Date:** 2026-09-29  
**Status:** frozen.

Use *recurrence to the forecast trend*, *first crossing*, and *time to trend*.
Do not infer stationarity or arbitrage from these statistics alone.


## D008 — Maximum five separated local minima

**Date:** 2026-09-29  
**Status:** frozen for the first numerical benchmark.

For each CV surface, first find all detected local minima. Candidate selection
then ranks them by CV and greedily keeps at most five. Once a minimum at
smoothness s is accepted, any remaining minimum inside

\[
[s-\varepsilon,\ s+\varepsilon]
\]

is suppressed. Thus \(\varepsilon=0.10\) denotes radius 0.10 and total
neighborhood width 0.20.

The initial sensitivity set is

\[
\varepsilon\in\{0,0.02,0.05,0.10,0.15\}.
\]

The spacing rule is applied after stationary-point discovery, so changing
epsilon does not change which stationary points the numerical solver finds.


## D009 — Separate smoothing from extrapolation

**Date:** 2026-09-29  
**Status:** frozen conceptually; exact forecast-method set remains to be frozen.

Estimating the historical trend and forecasting that trend h steps ahead are
different operations. Introduce a discrete forecast rule m and write the
selection objective as

\[
CV_h(d,L,m,S).
\]

The first comparison will include the native finite-difference continuation and
a small number of simple tail-extrapolation rules. Avoid a large forecasting
model zoo.

## D010 — Likelihood/state-space benchmark

**Date:** 2026-09-29  
**Status:** frozen.

The paper must compare forecast-selected smoothness with a likelihood-based
trend model. The likelihood model estimates stochastic variance/smoothing
parameters using ML/REML or marginal likelihood; its latent trend is then
obtained by Kalman filtering/smoothing and forecast through the state-space
model.

This benchmark is evaluated on the same validation and untouched test periods
as the proposed method. Likelihood selection itself must not use the final test
block.
