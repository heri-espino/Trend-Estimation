# Research Map

Last updated: 2026-10-05

This file is the conceptual map of the repository so that a new researcher or AI agent can reconstruct the project without chat history.

## 1. Common mathematical foundation

\[
\widehat\tau_\lambda=H_\lambda y,\qquad
H_\lambda=(I+\lambda Q)^{-1},\qquad
Q=D_d^\top D_d.
\]

Because
\[
x^\top Qx=x^\top D_d^\top D_dx=\|D_dx\|_2^2\ge0,
\]
\(Q\) is symmetric positive semidefinite. Under the usual \(d\)-th difference operator it has \(d\) zero eigenvalues and \(N-d\) positive eigenvalues.

If
\[
Q=U\operatorname{diag}(0,\ldots,0,\delta_1,\ldots,\delta_{N-d})U^\top,
\]
then
\[
H_\lambda=
U\operatorname{diag}\left(
1,\ldots,1,
\frac1{1+\lambda\delta_1},\ldots,\frac1{1+\lambda\delta_{N-d}}
\right)U^\top.
\]

## 2. Normalized smoothness

\[
S(\lambda)=
1-\frac1{N-d}\sum_{j=1}^{N-d}\frac1{1+\lambda\delta_j}.
\]

Hence
\[
S(0)=0,\qquad \lim_{\lambda\to\infty}S(\lambda)=1,
\]
and
\[
S'(\lambda)=
\frac1{N-d}\sum_j\frac{\delta_j}{(1+\lambda\delta_j)^2}>0.
\]

So \(S\) is a strictly increasing reparameterization of \(\lambda\in[0,\infty]\) onto \(S\in[0,1]\).

Interpretation: \(H_\lambda\) performs smoothing; \(S(\lambda)\) measures how much penalizable spectral flexibility has been suppressed.

## 3. Forecasting

Smoothing alone does not forecast. For the active zero-drift finite-difference family, define a continuation matrix \(G_{d,h}\):
\[
\widehat z_T(\lambda)=G_{d,h}H_\lambda x_T.
\]

For zero drift, \(d=1\) gives constant continuation, \(d=2\) linear continuation, and \(d=3\) quadratic continuation.

## 4. Paper A: smoothness-CV

At origin \(T\),
\[
r_T(\lambda)=z_T-GH_\lambda x_T,\qquad
f_T(\lambda)=\frac1h\|r_T(\lambda)\|^2.
\]

Across rolling origins,
\[
f(\lambda)=\frac1M\sum_j f_{T_j}(\lambda).
\]

The same loss in smoothness coordinates is
\[
F(S)=f(\lambda(S)).
\]

The proposal is
\[
S^\star\in\arg\min_{S\in[0,1]}F(S).
\]

Paper A owns this definition and its scientific interpretation.

The direct lineage is: Whittaker/finite-difference PLS -> Guerrero controlled smoothness -> endogenous forecast-based selection of the smoothness percentage.

Hart's TSCV is relevant because it selects smoothing from predictive performance, but it uses a different kernel smoother, bandwidth, error-model construction, and one-step prediction problem.

## 5. Paper B: numerical methods

\[
H'_\lambda=-H_\lambda QH_\lambda,\qquad
H''_\lambda=2H_\lambda QH_\lambda QH_\lambda.
\]

Let
\[
a_T=GHQHx_T,\qquad b_T=GHQHQHx_T.
\]

Then
\[
f'_T(\lambda)=\frac{2}{h}r_T^\top a_T,
\]
and
\[
f''_T(\lambda)=
\frac{2}{h}\left(\|a_T\|^2-2r_T^\top b_T\right).
\]

Because \(F(S)=f(\lambda(S))\),
\[
F'(S)=\frac{f'(\lambda)}{S'(\lambda)},
\]
\[
F''(S)=
\frac{f''(\lambda)}{[S'(\lambda)]^2}
-
\frac{f'(\lambda)S''(\lambda)}{[S'(\lambda)]^3}.
\]

At a stationary point the second term vanishes. Since \(S'>0\), stationary candidates and nondegenerate min/max classification correspond between \(\lambda\) and \(S\).

The production solver uses adaptive discovery plus Brent refinement. Brent alone is not global.

## 6. Rational structure and Sturm direction

For fixed \(d,L,h\),
\[
\widehat z_T(\lambda)=
c_0+\sum_{j=1}^r\frac{c_j}{1+\lambda\delta_j}.
\]

Therefore
\[
f(\lambda)=\frac{P(\lambda)}{D(\lambda)^2},\qquad
f'(\lambda)=\frac{R(\lambda)}{D(\lambda)^3}.
\]

Since \(D(\lambda)>0\) for \(\lambda\ge0\), interior stationary points correspond to nonnegative roots of \(R\), except degenerate cases.

The repository contains a Sturm mini-check showing exact polynomial root isolation is feasible in a small controlled case. It is not yet a production certification theorem.

## 7. Paper ownership

paper_smoothness-cv/ owns the definition and interpretation of forecast-optimal smoothness.

paper_numerical-methods/ owns optimization derivatives, multimodal search, Brent refinement, endpoints, benchmarks, rational structure, and possible Sturm certification.

paper_forecast-optimal-smoothing/ owns joint/time-varying \((d,L,S)\) adaptation.

paper_smoothness-recurrence/ owns applied model comparison and recurrence.

paper_statistical-properties-penalized-trend/ owns broader inference/statistical properties.

## 8. Claim discipline

Do not claim PLS, controlled smoothness, predictive smoothing selection, rolling-origin validation, Brent, or multiple minima are individually new.

Do not say the current adaptive-Brent algorithm guarantees every stationary point.

Do not say the Sturm mini-check certifies all production cases.

Do not equate forecast-optimal smoothness with recovery-optimal smoothness or a universal population optimum.
