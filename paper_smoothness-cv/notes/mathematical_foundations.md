# Mathematical foundations — forecast-CV on normalized smoothness

**Canonical technical notebook | 2026-10-08 | Working derivations, not a submission-ready theorem collection.**

Read [research_objective.md](research_objective.md) and [validation_semantics.md](validation_semantics.md) first. All notation here refers to the **forecasting paper alone**, regardless of which numerical algorithm evaluates the objective.

## 1. What we are estimating

Observed equally spaced levels \(y_1,\ldots,y_T\) are known at current forecast origin \(T\). Let \(L\) be the fitting-window length, \(1\le d<L\) the difference order, and \(h\ge1\) the **operational** forecasting horizon. For historical origins \(t\),

\[
x_t=(y_{t-L+1},\ldots,y_t)^\top\in\mathbb R^L,
\qquad z_t=(y_{t+1},\ldots,y_{t+h})^\top\in\mathbb R^h.
\]

The second vector exists **only at origins whose subsequent \(h\) observations are already in the historical record available at \(T\)**. We never know \(z_T\) when issuing the forecast at \(T\). Forecast-CV uses earlier observed pseudo-futures, not an oracle that knows the future.

The signal estimate for a fixed smoothing penalty is

\[
\widehat\tau_t(\lambda)
=\arg\min_{\tau\in\mathbb R^L}
\big\{\|x_t-\tau\|_2^2+\lambda\|D_d\tau\|_2^2\big\}
=H_\lambda x_t,
\quad H_\lambda=(I+\lambda Q)^{-1},\quad Q=D_d^\top D_d.
\]

Here \(D_d\) is the usual order-\(d\) finite-difference matrix. This is the *established* PLS family, not a newly invented smoother.

## 2. Why eigenvalues: geometry and fast computation

Because \(v^\top Qv=\|D_dv\|_2^2\ge0\), \(Q\) is symmetric positive semidefinite with rank \(L-d\). Orthogonal diagonalization gives

\[
Q=U\,\operatorname{diag}(
\underbrace{0,\ldots,0}_{d},\delta_1,\ldots,\delta_{L-d})U^\top,
\quad \delta_j>0,\quad U^\top U=I.
\]

Therefore,

\[
H_\lambda
=U\,\operatorname{diag}\left(
\underbrace{1,\ldots,1}_{d},
\frac1{1+\lambda\delta_1},\ldots,
\frac1{1+\lambda\delta_{L-d}}\right)U^\top.
\]

Interpretation: the \(d\) null-space polynomial directions are not penalized; every other eigendirection is shrunk by a scalar response \(a_j(\lambda)=(1+\lambda\delta_j)^{-1}\). With \(d=2\), the unpenalized subspace is intercept + linear time trend; with \(d=3\), it is quadratic. This is why the limiting trend becomes a least-squares polynomial.

**Computational point:** for fixed \((L,d)\), compute a symmetric eigendecomposition of \(Q\) **once**, reusing eigenvectors and eigenvalues across candidate \(S\), forecast origins, and horizons. For a candidate \(\lambda\): project \(c_t=U^\top x_t\), shrink its \(L-d\) penalizable coordinates, and reconstruct \(H_\lambda x_t=U(a(\lambda)\odot c_t)\). There is no need to invert \(I+\lambda Q\) separately at each trial \(\lambda\). A numerical implementation should compute or cache \(U^\top x_t\), \(GU\), and positive eigenvalues; check near-zero eigenvalues using a scale-sensitive tolerance, not an arbitrary exact-zero test. For large \(L\), compare spectral preprocessing against sparse/banded factorizations; full dense diagonalization is not automatically fastest.

At the compactified right endpoint,

\[
H_\infty=P_{\ker D_d}
=U_0U_0^\top,
\]

which must be evaluated as a **projection limit**, not by substituting a large guessed \(\lambda\). At \(\lambda=0\), \(H_0=I\).

## 3. Why optimize the index \(S\), not a truncated \(\lambda\) grid?

The Guerrero-type trace index, normalized to its attainable range, is

\[
S(\lambda)=1-\frac{1}{L-d}\sum_{j=1}^{L-d}\frac1{1+\lambda\delta_j}
=\frac{L-\operatorname{tr}(H_\lambda)}{L-d}.
\]

This is a **scalar measure of achieved smoothing**, not a new smoother. Its key properties:

\[
S(0)=0,\quad S(\infty)=1,
\quad S'(\lambda)=\frac1{L-d}\sum_j\frac{\delta_j}{(1+\lambda\delta_j)^2}>0,
\]

\[
S''(\lambda)=-\frac2{L-d}\sum_j\frac{\delta_j^2}{(1+\lambda\delta_j)^3}<0,
\qquad \operatorname{edf}(\lambda)=L-(L-d)S(\lambda).
\]

Consequently \(S:[0,\infty]\to[0,1]\) is continuous, strictly increasing, and invertible in the interior. It is useful because a **full, interpretable, bounded** search includes both limits and all interior smoothing regimes. An equally spaced grid in \(S\) is not an equally spaced grid in \(\lambda\): it samples the *amount of smoothing* rather than raw penalty magnitude. Numerically recover \(\lambda(S)\) using a monotone bracketed inverse; special-case endpoints. **Do not** claim that a one-to-one transform changes the globally optimal fitted trend, turns a multimodal loss convex, or independently constitutes a new statistical method. Near \(S=1\), inversion can be ill-conditioned since \(S'\to0\).

Define the smoother in the coordinate actually tuned:

\[
H(S)=
\begin{cases}
(I+\lambda(S)Q)^{-1},&0\le S<1,\\
P_{\ker D_d},&S=1.
\end{cases}
\]

## 4. What exactly is predicted?

Choose the deterministic continuation \(G_{d,h}\in\mathbb R^{h\times L}\) that sets *future \(d\)th differences to zero*. For fitted \(u=H(S)x_t\),

\[
\widehat \tau_{t+k\mid t}(S)
=\sum_{j=0}^{d-1}\binom{k+j-1}{j}(\nabla^ju)_L,\quad k=1,\ldots,h.
\]

- \(d=1\): constant forecast.
- \(d=2\): \(\widehat\tau_{t+k\mid t}=u_L+k(u_L-u_{L-1})\), a line.
- \(d=3\): \(\widehat\tau_{t+k\mid t}=u_L+k\nabla u_L+\tfrac{k(k+1)}2\nabla^2u_L\), a quadratic.

Thus \(\widehat z_t(S)=G_{d,h}H(S)x_t\). Altering \(S\) changes the terminal filtered differences and therefore the **coefficients** of the future polynomial. It does **not** choose the degree if \(d\) stays fixed; joint selection of \(d\) must be an explicit, separate experiment. This is forecast-directed selection of a trend, not merely retrospective visual smoothing.

## 5. MSE surface and its quadratic expansion

For each historical origin with completed validation block,

\[
F_t(S)=\frac1h\|z_t-GH(S)x_t\|_2^2,
\qquad
f_t(\lambda)=F_t(S(\lambda)).
\]

The same scalar objective admits a useful quadratic expansion:

\[
h f_t(\lambda)
=z_t^\top z_t-2z_t^\top GH_\lambda x_t
+x_t^\top H_\lambda G^\top GH_\lambda x_t.
\]

This is a quadratic **in the fitted forecast vector**, not necessarily a quadratic in \(S\) or \(\lambda\). It can have several local minima.

For historical origins \(t_m+h\le T\),

\[
F^{\mathrm{pool}}_{T,d,L,h}(S)=\frac1M\sum_{m=1}^M F_{t_m}(S),\qquad
\widehat S_{T,d,L,h}^{\mathrm{FCV}}\in
\arg\min_{S\in[0,1]}F^{\mathrm{pool}}_{T,d,L,h}(S).
\]

The pooled objective is one **aggregate** curve, not the same as taking the mean of origin-specific minimizing \(S\)'s. Its minimizers can differ from every individual historical minimum.

### Optional precomputation of the full curve

For fixed \((d,L,h)\), let \(A_m=GU\,\operatorname{diag}(U^\top x_{t_m})\) and \(w(\lambda)\) be the diagonal response vector of \(H_\lambda\). Then \(\widehat z_{t_m}=A_m w(\lambda)\). Precompute

\[
c=\frac1{Mh}\sum_m z_m^\top z_m,\quad
b=\frac1{Mh}\sum_m A_m^\top z_m,\quad
C=\frac1{Mh}\sum_m A_m^\top A_m.
\]

The **same** forecast CV objective is

\[
f^{\mathrm{pool}}(\lambda)
=c-2b^\top w(\lambda)+w(\lambda)^\top Cw(\lambda).
\]

This enables repeated loss/derivative evaluation after precomputation, avoiding a new fit for every candidate. It is an algebraic reformulation, not a claim that this optimization already has a measured speedup. Compare memory/time costs and the low rank of the forecast operator before choosing a production implementation.

## 6. Analytic derivatives: no finite differences required

Since \(H_\lambda(I+\lambda Q)=I\), differentiating gives

\[
H_\lambda'=-H_\lambda QH_\lambda,\qquad
H_\lambda''=2H_\lambda QH_\lambda QH_\lambda.
\]

Because \(Q\) commutes with its resolvent \(H_\lambda\),

\[
\frac{d^n H_\lambda}{d\lambda^n}
=(-1)^n n!\,H_\lambda(QH_\lambda)^n,\quad n=0,1,\ldots.
\]

Set \(r_t(\lambda)=z_t-GH_\lambda x_t\). For the **fixed** continuation operator \(G\),

\[
r_t'=GH_\lambda QH_\lambda x_t,\quad
r_t''=-2GH_\lambda QH_\lambda QH_\lambda x_t.
\]

Hence,

\[
f_t'(\lambda)=\frac2h\,r_t^\top GH_\lambda QH_\lambda x_t,
\]

\[
f_t''(\lambda)=\frac2h\|GH_\lambda QH_\lambda x_t\|_2^2
-\frac4h r_t^\top GH_\lambda QH_\lambda QH_\lambda x_t.
\]

Derivatives of the pooled objective are the averages of the origin-specific derivatives. By the chain rule,

\[
\frac{dF}{dS}=\frac{f'(\lambda)}{S'(\lambda)},\quad
\frac{d^2F}{dS^2}
=\frac{f''(\lambda)}{[S'(\lambda)]^2}
-\frac{f'(\lambda)S''(\lambda)}{[S'(\lambda)]^3}.
\]

For any **finite interior** stationary point \(f'(\lambda)=0\), the curvature sign is preserved. All formulas assume fixed \(G,d,L,h\) and a quadratic penalty; re-estimating another predictive model depending on \(S\) changes the derivatives. The endpoint \(S=1\) requires its own limit handling.

## 7. Multiple minima and numerical goals

The objective is continuous over compact \([0,1]\): a global minimum exists, but it need not be unique. We should search for multiple local minima, examine stationary maxima/flat roots where useful, compare \(S=0,1\), and report the **best** candidate according to the pooled historical future MSE.

- Earlier implementation: adaptive derivative sampling in \(S\), Brent refinement, endpoints. Practical but **not** a completeness proof.
- An algebraic route: for rational input data, \(f(\lambda)\) is rational and the numerator of \(f'(\lambda)\) is a polynomial. Exact Sturm sequences can count/isolate positive stationary roots of *small rationalized* problems. This involves \(\lambda\) as an algebraic auxiliary variable, with \(S\) as the reported decision coordinate. Do not call large-window or floating-point searches Sturm-certified, or claim that approximated loss rankings are rigorously globally certified.
- **Proposed, not decided:** compare modern search strategies, root-recovery accuracy, run time, and statistical stability before choosing the algorithm for the next experiments.

Tracking minima across historical origins is an optional further statistical **hypothesis**: individual curves \(F_t(S)\) can have several minima that move over time. Their temporal identity is ambiguous near crossings or births; it must be assessed, not assumed. The core pooled minimization requires **none** of that tracking.

## 8. What remains open

1. Which structural features of the historical forecast-loss curve are stable across different \((L,d,h)\)?
2. Does finding all local minima materially improve **selected pooled forecast MSE** versus a sufficiently dense/adaptive search?
3. How sensitive are forecasts to interpolation of \(S\), eigenvalue conditioning, and endpoint handling?
4. Can we obtain a computational improvement from spectral precomputation in real benchmark environments?
5. How different is \(S_{\mathrm{forecast}}\) from \(S_{\mathrm{recovery}}\), and under which DGPs?
6. Can tracking of *historical* minima improve forecasting, or is pooled CV a stronger and simpler baseline?

**Research discipline:** an exact derivative is a proven algebraic statement; a numerical root algorithm's completeness is a separate statement; predictive superiority is another, requiring genuinely untouched outer tests.
