# Canonical Research Objective

Date established: 2026-09-29

This file is the first scientific source of truth for the
smoothness/financial-recurrence paper.

## One-sentence objective

> Select forecast-optimal normalized smoothness directly on its natural compact
> domain, using a numerical search for multiple local minima, and use the
> resulting forecast trend to study recurrence of financial prices toward that
> trend at multiple horizons.

## Mathematical object

For (y=(y_1,\ldots,y_N)^\top), difference order (d), and
(Q=D_d^\top D_d),

\[
\widehat\tau_\lambda=(I+\lambda Q)^{-1}y.
\]

For fixed ((N,d)), normalized smoothness is a monotone map

\[
S=S_d(\lambda;N)\in[0,1],
\]

with (S=0\leftrightarrow\lambda=0) and
(S=1\leftrightarrow\lambda=\infty) in the limiting sense.

For forecast horizon (h), define chronological CV loss (CV_h(S)). The
primary selection object is

\[
\boxed{S_h^\star=\arg\min_{S\in[0,1]}CV_h(S).}
\]

The numerical question is how to identify all relevant local minima without
evaluating a dense uniform grid over the full domain.

## Recurrence object

At untouched origin (T), use only (mathcal F_T) to obtain the selected
smoothness, fit the trend, and generate the frozen future path

\[
\widehat\tau_{T+k\mid T},\qquad k=1,\ldots,H.
\]

For log price (x_t=\log P_t), define

\[
g_{T,k}=x_{T+k}-\widehat\tau_{T+k\mid T}.
\]

Two primary recurrence definitions are

\[
R_T^{\mathrm{cross}}
=
\inf\{k\ge1:g_{T,k}g_{T,0}\le0\},
\]

and

\[
R_T^{\varepsilon}
=
\inf\{k\ge1:|g_{T,k}|\le\varepsilon_T\}.
\]

Events not recurring before a pre-specified (H_{\max}) are right-censored.

## Scientific questions

1. Can the optimal smoothness be found reliably with far fewer objective
   evaluations than a dense smoothness grid?
2. How does (S_h^\star) change with forecast horizon?
3. How is recurrence time related to initial distance from trend?
4. Are recurrence distributions different across ETFs, equities, and crypto?
5. Are conclusions robust to pre-specified definitions of distance and
   recurrence?

## Scope guardrails

The primary paper is **not** about adaptive joint selection of (d,L,S).
That is the separate adaptive paper.

For the main analysis:

- (d) and (L) are fixed before final evaluation;
- only (S) is the continuously optimized smoothing coordinate;
- no future observation may affect selection or the forecast trend at (T);
- the recurrence reference path is frozen at (T);
- recurrence to trend is not automatically a stationary mean-reversion claim;
- forecast accuracy is not evidence of trading profitability;
- the dense GPU grid is a numerical benchmark, not the proposed optimizer.
