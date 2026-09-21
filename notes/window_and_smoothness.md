# Window Length, Lambda, and Comparable Smoothness

## Question

When we compare forecast-optimal smoothing across rolling origins, can we use one common penalty parameter \(\lambda\) if the fitted sample size changes?

The answer is: mathematically yes, but it no longer represents one common amount of normalized smoothness.

## Why sample size matters

For a finite-difference smoother,

\[
S_\lambda=(I+\lambda D_d^\top D_d)^{-1}.
\]

The Guerrero-style smoothness index used by this project is based on the effective degrees of freedom,

\[
\operatorname{tr}(S_\lambda),
\]

and is normalized using the sample size \(N\) and difference order \(d\).

The implemented normalized index is

\[
s_d(\lambda;N)
=
\frac{
1-N^{-1}\operatorname{tr}(S_\lambda)
}{
1-d/N
}.
\]

Therefore, in general,

\[
\boxed{
s_d(\lambda;N_1)
\neq
s_d(\lambda;N_2)
}
\]

for the same \(\lambda\) when \(N_1\neq N_2\).

The reason is not only the explicit normalization by \(N\). The spectrum of

\[
D_d^\top D_d
\]

also changes with the fitted sample length.

## Consequence for expanding-window CV

Suppose a rolling-origin objective uses expanding fits:

\[
1{:}T_1,
\quad
1{:}T_2,
\quad
\ldots
\]

and optimizes one shared \(\lambda\).

That objective is valid as a common-penalty objective, but the corresponding amount of normalized smoothness changes from origin to origin because \(N=T_j\) changes.

So the statement

> one common lambda was selected across expanding origins

is not equivalent to

> one common smoothness level was selected across expanding origins.

This distinction matters because the active paper is framed in terms of forecast-optimal **smoothness**, not raw \(\lambda\) alone.

## Active-paper design choice

When the scientific object is

\[
S^\star_{T,h,L},
\]

we explicitly include estimation-window length \(L\).

For a candidate fixed window \(L\), inner rolling-origin fits use

\[
T_j-L+1{:}T_j.
\]

Every inner fit therefore contains exactly \(L\) observations. For fixed \(d\),

\[
N=L
\]

is constant across those origins, so a common \(\lambda\) corresponds to one common normalized smoothness value.

This makes the interpretation clean:

\[
\boxed{
(d,L,\lambda)
\longleftrightarrow
(d,L,S_d(\lambda;L)).
}
\]

## Selector implemented for this design

The library now exposes

`select_fixed_window_pure_smoothness`

which, for each candidate \((d,L)\):

1. constructs fixed-width inner rolling-origin splits;
2. pools genuine future-block forecast loss;
3. optimizes \(\lambda\) with derivative-root search;
4. converts the selected \(\lambda\) to normalized smoothness using exactly \(N=L\);
5. compares candidate \((d,L)\) pairs by their inner forecast loss.

This is an **inner selector only**. The caller must pass only history available at the current outer forecast origin.

Outer performance must still be evaluated on a later untouched block.

## Alternative for expanding windows

If we later want a common smoothness target under expanding windows, a different parameterization is preferable:

\[
s
\mapsto
\lambda_j(s;N_j,d).
\]

That is, hold the normalized smoothness \(s\) fixed and convert it to a split-specific \(\lambda_j\).

The derivative of the aggregate objective with respect to \(s\) then requires the chain rule through \(\lambda_j(s)\). That is a separate derivation and is not required for the first active-paper implementation.

## Library mapping

- `src/trend_estimation/core/smoothness.py` — \(\lambda\leftrightarrow s_d(\lambda;N)\).
- `src/trend_estimation/validation/rolling_origin.py` — fixed or expanding chronological splits.
- `src/trend_estimation/selection/forecast_optimal.py` — fixed-window inner selector.
- `src/trend_estimation/forecasting/objectives.py` — pooled future-block loss and derivatives.

## Status

- mathematical issue identified;
- fixed-window design chosen for the main \(S^\star_{T,h,L}\) experiments;
- selector implemented;
- basic selector tests added;
- full nested outer evaluation still pending.
