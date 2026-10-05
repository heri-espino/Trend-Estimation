# Decisions

## BZ001 — Create a separate paper idea

**Date:** 2026-10-05

Keep the Bézier/Bernstein direction separate from the active smoothness-CV and numerical-method papers.

Reason: it changes the representation and regularization geometry, whereas the active papers assume the finite-difference PLS family.

## BZ002 — No generic novelty claim

**Date:** 2026-10-05

Do not claim novelty for Bézier smoothing, Bernstein regression, penalized Bézier fitting, Bernstein time-series forecasting, P-spline forecasting, or financial Bézier filtering.

Direct prior literature exists for all of these.

## BZ003 — Candidate contribution is comparative and endpoint-focused

**Date:** 2026-10-05

The candidate scientific object is the comparison

\[
\|D_d\tau\|^2
\quad\text{versus}\quad
\|D_q\beta\|^2
\]

under chronological forecast tuning, together with explicit terminal Bézier geometry and matched P-spline baselines.

## BZ004 — Audit before computation

**Date:** 2026-10-05

Do not spend paper-scale compute until the P0 direct literature is read and the equivalence with P-splines is understood.
