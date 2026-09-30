# Canonical Research Objective

**Status:** active source of truth.

## Research question

Can forecast-optimal normalized smoothness for finite-difference penalized trend
estimation be selected reliably and efficiently when the chronological
forecast-loss surface may contain multiple local minima?

## Estimator

For \(y\in\mathbb R^N\), difference order \(d\), and
\(Q=D_d^\top D_d\),
\[
\widehat\tau_\lambda=(I+\lambda Q)^{-1}y.
\]

Let \(S_d(\lambda;N)\in[0,1]\) be the normalized smoothness index. For
\(d\ge1\), using the positive eigenvalues \(\delta_j\) of \(Q\),
\[
S(\lambda)
=
1-
\frac{1}{N-d}
\sum_{j=1}^{N-d}
\frac{1}{1+\lambda\delta_j}.
\]

It is strictly increasing, so the penalty domain
\([0,\infty]\) is represented by the compact smoothness domain \([0,1]\).

## Forecast objective

For a frozen chronological validation protocol, discrete configuration
\((d,L,h)\), and continuation rule \(m\), define
\[
F(S)=CV_h(d,L,S).
\]

The primary continuous selection problem is
\[
S^\star\in\arg\min_{S\in[0,1]}F(S).
\]

The method must not assume that \(F\) is unimodal.

## Numerical idea

If \(f(\lambda)=F(S(\lambda))\), then
\[
F'(S)=\frac{f'(\lambda)}{S'(\lambda)}.
\]

Because \(S'(\lambda)>0\), the interior stationary points are preserved:
\[
F'(S)=0
\iff
f'(\lambda)=0.
\]

At a stationary point,
\[
F''(S^\star)
=
\frac{f''(\lambda^\star)}
{[S'(\lambda^\star)]^2},
\]
so local minimum/maximum classification is also preserved.

The proposed algorithm therefore searches the compact \(S\)-domain while
reusing stable analytic derivatives in \(\lambda\).

## Scientific claims this paper may establish

- compact smoothness coordinates improve interpretability of the search domain;
- derivative-aware adaptive search can recover the relevant minima with fewer
  objective evaluations than a dense reference grid;
- multimodality is empirically relevant for at least some forecast-validation
  surfaces;
- epsilon-separated candidate selection provides a controlled way to summarize
  nearby minima.

The paper must not claim guaranteed discovery of every stationary point of an
arbitrary smooth objective unless such a theorem is actually proved.
