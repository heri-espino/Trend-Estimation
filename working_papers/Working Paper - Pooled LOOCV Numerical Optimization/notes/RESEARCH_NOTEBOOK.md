# Research notebook: pooled LOOCV and numerical optimization

**Date:** 2026-10-18. **Scientific status:** three distinct exploratory pilots have **executed and been committed**; the independent five-regime noise-misspecification robustness pilot **has now also executed and been committed** (200 nested pools, 1,000 per-method rows). See the [completed robustness audit](ROBUSTNESS_PILOT_AUDIT_2026-10-18.md), which distinguishes a strong AR(1) outcome from nearly equal mean results under iid Gaussian noise. See the source-authoritative [RESULTS_LEDGER.md](RESULTS_LEDGER.md), [variance-estimation pilot audit](VARIANCE_ESTIMATION_PILOT_AUDIT_2026-10-18.md) and [ROBUSTNESS_PROTOCOL.md](ROBUSTNESS_PROTOCOL.md). Neither overall numerical superiority nor a universal statistical method improvement has been established. The next tail stress pilot (not yet executed) crosses d=1,2,3 with centered skew-normal α=-6,-3,0,3,6 plus Student-t3, Gamma, jumps, GARCH, Gaussian and Cauchy. See [TAIL_NOISE_PROTOCOL.md](TAIL_NOISE_PROTOCOL.md).

## 1. Problem and terminology

Let R≥1 be the number of observed replicate series, N>d≥1 their common length and differencing order, \(y^{(r)}\in\mathbb R^N\) the observations, and \(D_d\in\mathbb R^{(N-d)\times N}\) the ordinary forward-difference matrix. In the main study take d=2, V=I, and mean of trend differences μ=0. The trend is the solution of

\[
\widehat\tau_\lambda^{(r)}
=\arg\min_\tau \bigl\{\|y^{(r)}-\tau\|^2+
\lambda\|D_d\tau\|^2\bigr\}
=(I+\lambda Q)^{-1}y^{(r)},\quad Q=D_d^\top D_d.
\]

A *leverage* \(h_{ii}(\lambda)\) is the ith diagonal of \(H_\lambda\); an *effective degree of freedom* is \(\mathrm{tr}(H_\lambda)\); an *interior stationary point* is a positive λ with \(F_R'(\lambda)=0\). A *global minimizer* must also be compared to both exact boundary limits. A *pool* is an aggregation across separate, comparable observed series, NOT across chronologically later target blocks.

## 2. Selection criterion

For λ>0,

\[
e_{ri}(\lambda)=
\frac{y_i^{(r)}-[H_\lambda y^{(r)}]_i}
{1-[H_\lambda]_{ii}},\qquad
F_R(\lambda)=\frac1{RN}\sum_{r,i}e_{ri}(\lambda)^2.
\]

Equivalently, with \(T_\lambda=Q(I+\lambda Q)^{-1}\),

\[
e_{ri}(\lambda)=\frac{[T_\lambda y^{(r)}]_i}
{[T_\lambda]_{ii}}.
\]

This exact identity enables evaluation at λ=0 by continuity. Define \(\lambda=\infty\) by the limiting nullspace projection and explicitly compare it. For each N,d, transform the same curve to normalized smoothness \(S=(N-\operatorname{tr} H_\lambda)/(N-d)\); the argmin is unchanged by this increasing reparameterization.

**Critical choice:** equal series weights R⁻¹, equal point weights N⁻¹. Statistical replication at fixed trend, seasonality and σ, with independently drawn noise, is a well-defined first pooled setting. Pools combining currencies, indices or σ without scale normalization can produce misleading weightings.

## 3. Numerical thesis and alternatives

**Candidate thesis:** structured derivative-root searches locate lower pooled LOOCV values or equivalent minima at fewer evaluations than a naive grid and one-shot local Brent, while exact small-rational Sturm instances permit a precise comparison of root counts.

**Rival explanations:** objective curves may be usually unimodal; GCV may be sufficient; a straightforward log-λ grid + bounded scalar minimization may be equally reliable; multi-bracket methods may miss tangencies or closely spaced extrema; high-degree symbolic polynomials may become infeasible.

We will *measure* frequency of non-unimodality before making stronger statements. A correct negative finding is an acceptable research outcome.

## 4. Mechanism to investigate

Differentiate \(T_\lambda=Q(I+\lambda Q)^{-1}\):

\[
T'_\lambda=-T_\lambda^2,\quad
a_{ri}=(T_\lambda y^{(r)})_i,\quad
b_i=(T_\lambda)_{ii}.
\]

Then

\[
e'_{ri}=\frac{a'_{ri}b_i-a_{ri}b_i'}{b_i^2},
\quad a'_{ri}=-(T_\lambda^2y^{(r)})_i,\quad
b'_i=-(T_\lambda^2)_{ii},
\]
\[
F_R'(\lambda)=\frac{2}{RN}\sum_{r,i}e_{ri} e'_{ri}.
\]

Test symbolic/numerical equivalence, derivative finite-difference agreement and sensitivity to log-λ parameterization. Identify positive stationary roots, classify candidate minima, and compare against both endpoints. Sturm counts exact positive roots of a cleared stationary polynomial only for small rational instances.

## 5. Meaning of the comparison with Guerrero and Cortés-Toto

Guerrero (2007) supplies the probabilistic PLS formulation and the smoothness index. Cortés-Toto et al. (2017) compared attained smoothness under CV, GCV, AICc, BIC in a 2^4 design, and their simulation is our replication baseline. Neither the trace index nor ordinary LOOCV is novel. We compare *numerical search algorithms and minimizer geometry*, not claim an invented statistical criterion. Guerrero's percentage of smoothness is **specified by the analyst**, not a universal competing optimum.

For single series (R=1), include original CV/GCV selectors. For R>1, report the shared pooled optimum, individual optima for descriptive comparison, and expected loss on independent synthetic replicate series only if an additional evaluation stage is predeclared; latent τ is available for reconstruction diagnostics, never used to select feasible λ.

## 6. Proposed manuscript structure

1. Introduction and existing LOOCV/GCV/global-optimization literature.
2. PLS, index, pooled LOOCV, endpoint identities.
3. Stationary derivative, Brent-based searches and exact restricted Sturm procedure.
4. Factorial simulation: numerical recovery vs runtime and effect of pooling.
5. Financial-series illustration: retrospective trend and error surface, not investment returns.
6. Discussion: numerical conditioning, competing literature, failure cases and limitations.

**Candidate, not result:** numerical structure and objective-specific global-search evidence may be sufficient for a short SMCCA paper. Do not make novelty/acceptance claims until literature and data support them.
