# Research Map

Last updated: 2026-10-06

This is the conceptual map for the **two active papers**.

## 1. Common estimator

\[
\widehat\tau_\lambda=H_\lambda y,
\qquad
H_\lambda=(I+\lambda Q)^{-1},
\qquad
Q=D_d^\top D_d.
\]

Normalized smoothness is

\[
S(\lambda)
=
1-\frac1{N-d}
\sum_{j=1}^{N-d}
\frac1{1+\lambda\delta_j},
\]

which maps \([0,\infty]\) monotonically to \([0,1]\).

Forecasting uses the native finite-difference continuation

\[
\widehat z_T(S)
=
G_{d,h}H_{\lambda(S)}x_T.
\]

## 2. Static pooled forecast-CV baseline

For historical forecast origins,

\[
F^{\mathrm{pool}}_{T,h}(S)
=
\frac1M\sum_{m=1}^{M}\ell_{m,h}(S),
\]

with

\[
\widehat S^{\mathrm{pool}}_{T,h}
\in
\arg\min_S F^{\mathrm{pool}}_{T,h}(S).
\]

This remains a baseline and is the object studied by smoothness-CV CP01--CP03.

## 3. Dynamic tracked-smoothness object

At each chronological origin \(t\), recover all relevant local minima

\[
\mathcal M_t
=
\{S_{1,t},\ldots,S_{K_t,t}\}.
\]

Connect minima across adjacent surfaces by one-to-one temporal continuation,

\[
|S_{j,t}-S_{j,t-1}|
\le
\varepsilon_{\mathrm{track}}.
\]

A tracked branch stores

\[
V_j
=
\{(S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t})\}_{t\in\mathcal T_j}.
\]

The forecasting decision is

\[
\widehat j_T
=
\psi(V_1,\ldots,V_J),
\qquad
\widehat S_T
=
\phi(V_{\widehat j_T}).
\]

Initial \(\phi\) rules are:

- last/newest local minimum;
- recent mean;
- recent median;
- Validation-2 weighted mean;
- recency + Validation-2 weighted mean.

A direct forecast of the smoothness trajectory is a later extension.

## 4. Mandatory final refit

Whatever rule selects \(\widehat S_T\), all temporary validation fits are
discarded. The operational estimator is refit using the newest full window:

\[
\widehat\tau_T
=
H_{\lambda(\widehat S_T)}
y_{T-L+1:T},
\]

then the untouched future is forecast.

We may average historical losses or smoothness values when a declared rule
requires it. We never average historical fitted trends.

## 5. Paper A ownership — `paper_smoothness-cv/`

Paper A owns the forecasting/statistical decision problem:

- branch matrix \(V_j\);
- branch selector \(\psi\);
- final smoothness functional \(\phi\);
- Validation-1/refit/Validation-2 chronology;
- comparison with pooled forecast-CV and classical selectors;
- untouched-test forecast performance.

Primary target: Journal of Forecasting.

## 6. Paper B ownership — `paper_numerical-methods/`

Paper B owns numerical support for the dynamic object:

- derivative-aware recovery of multiple local minima on each \(F_t(S)\);
- exact \(S=0\) and \(S=1\) handling;
- adaptive interval subdivision;
- Brent root refinement;
- possible rational/Sturm certification;
- temporal correspondence/tracking of minima across successive surfaces.

Per-surface derivatives remain

\[
H'_\lambda=-H_\lambda QH_\lambda,
\qquad
H''_\lambda=2H_\lambda QH_\lambda QH_\lambda,
\]

with

\[
F'(S)=\frac{f'(\lambda)}{S'(\lambda)}.
\]

The frozen per-surface benchmark evidence remains valid. Temporal tracking is a
new numerical layer and must be validated separately.

## 7. Two distinct radii

Do not conflate:

- `candidate_spacing`: within one surface, after minimum discovery;
- `track_epsilon`: across adjacent surfaces, for branch continuation.

## 8. Claim discipline

Do not claim that predictive smoothing selection, multiple minima, Brent, or
rolling validation are individually new.

Do not claim the current adaptive sampler certifies every stationary point.

Do not claim the current greedy branch matcher is globally optimal or
theoretically unique.

Any novelty claim about temporal tracking of smoothing optima must be audited
against the literature before submission.

## 9. Active-work policy

Only `paper_smoothness-cv/` and `paper_numerical-methods/` are active.
All other paper directories are inactive unless the user explicitly reactivates
one.
