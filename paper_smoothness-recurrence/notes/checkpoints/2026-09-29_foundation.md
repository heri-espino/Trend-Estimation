# Checkpoint — Smoothness/Recurrence Paper Foundation

Date: 2026-09-29

## Why this paper exists

The broader adaptive paper expanded from smoothness selection into joint
adaptation of difference order, memory length, and smoothness across regimes.
That work is preserved, but it is not required for the original narrower idea.

This paper returns to

\[
S_h^\star=\arg\min_{S\in[0,1]}CV_h(S),
\]

then applies the selected trend to a financial recurrence question.

## Numerical direction

The older implementation could evaluate a dense grid over (S\in(0,1)),
especially quickly on GPU, identify local minima, and compare them.

The current library later moved to a coarse discovery grid in
(log\lambda), followed by Brent refinement.

The new target combines both:

- search on the natural compact smoothness domain (S\in[0,1]);
- retain analytic derivatives already available in (lambda);
- adaptively isolate multiple stationary points;
- refine roots numerically;
- compare all local minima and exact boundaries;
- keep the dense GPU grid only as a correctness benchmark.

## Financial direction

For each series/horizon, select (S_h^\star) by chronological CV. At untouched
origins, forecast the trend path and measure how long future prices take to
cross or re-enter a band around that frozen path.

\[
\boxed{
S_h^\star
\rightarrow
\widehat\tau_{T+k\mid T}
\rightarrow
g_{T,k}
\rightarrow
R_T.
}
\]

## Immediate next task

Implement and test the smoothness-domain numerical layer before new financial
experiments. Do not begin by tuning the asset universe or recurrence thresholds.
