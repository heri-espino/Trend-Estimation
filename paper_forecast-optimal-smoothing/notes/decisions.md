# Decisions Log

## A001 — Adaptive paper is parked

**Date:** 2026-09-30  
**Status:** frozen until the numerical paper is complete.

Do not run new adaptive-paper experiments while
paper_numerical-smoothness-selection/ is active.

## A002 — Adaptive object remains joint and state-dependent

The paper remains centered on
\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

Do not collapse this paper into a smoothness-only numerical study.

## A003 — Numerical solver may be imported later

When resumed, the adaptive paper may reuse the finished normalized-smoothness
solver, but the solver's standalone numerical novelty belongs to the numerical
paper.

## A004 — Recurrence belongs elsewhere

Comparative trend forecasting and financial recurrence belong to
paper_smoothness-recurrence/.
