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

## 2A. Why the nullity is exactly d, why fitting is always solvable, and why S=1 is exact

**Assumptions for all claims here:** the usual consecutive finite-difference operator \(D_d\in\mathbb R^{(L-d)\times L}\), \(1\le d<L\), real-valued observations, the *pure* PLS penalty \(Q=D_d^\top D_d\), and \(\lambda\ge0\). Different constraints, penalty matrices, boundary conditions, or negative penalties need their own proofs.

### A. Rank-nullity and the d free initial observations

The null space of \(D_d\) is the set of vectors satisfying \(D_dx=0\), or equivalently a homogeneous recurrence of order \(d\), \(\Delta^d x_t=0\). The coefficient multiplying the newest unknown value \(x_{t+d}\) is nonzero, so choosing \(x_1,\ldots,x_d\) freely determines every subsequent value uniquely. There are **exactly \(d\) free scalar choices**, not \(L-d\). Consequently,

\[
\dim\ker(D_d)=d,\qquad
\operatorname{rank}(D_d)=L-d
\]

by the rank-nullity theorem \(\operatorname{rank}(A)+\operatorname{nullity}(A)=\text{number of columns of }A\). The rank equals the number of *rows* here only because the consecutive-difference rows are independent; this equality does **not** hold for arbitrary matrices. These null-space sequences are discrete polynomial sequences of degree at most \(d-1\), with basis \(1,t,\ldots,t^{d-1}\).

**Concrete example:** for \(L=4,d=2\),

\[
D_2=\begin{pmatrix}1&-2&1&0\\0&1&-2&1\end{pmatrix},\qquad
D_2x=0\iff
x=a(1,1,1,1)^\top+b(0,1,2,3)^\top.
\]

Two freely chosen coefficients \(a,b\) give nullity 2. The notion is the **dimension of a subspace**, not a claim that the kernel itself is the number 2.

### B. Why Q inherits exactly the same kernel

One inclusion is immediate: \(D_dx=0\) implies \(Qx=D_d^\top(D_dx)=0\). The converse is the subtle direction; we cannot simply *cancel* \(D_d^\top\). If \(Qx=0\), premultiply by \(x^\top\):

\[
0=x^\top Qx
=x^\top D_d^\top D_dx
=(D_dx)^\top(D_dx)
=\|D_dx\|_2^2.
\]

A sum of squares of **real** numbers can equal zero only if each summand is zero. Thus \(D_dx=0\). Both inclusions hold, hence

\[
\boxed{\ker(Q)=\ker(D_d),\quad
\operatorname{nullity}(Q)=d,\quad
\operatorname{rank}(Q)=L-d.}
\]

Because \(Q\) is symmetric PSD, this means exactly \(d\) zero eigenvalues (counted with multiplicity), not that \(H_\lambda\) has \(d\) zero eigenvalues.

### C. Existence and uniqueness for every finite penalty

Let \(A_\lambda=I+\lambda Q\). For each **nonzero** \(v\in\mathbb R^L\) and finite \(\lambda\ge0\),

\[
v^\top A_\lambda v
=v^\top v+\lambda v^\top Qv
=\|v\|_2^2+\lambda\|D_dv\|_2^2
>0.
\]

The strict inequality comes from \(\|v\|^2>0\), even if \(v\in\ker(D_d)\). Thus \(A_\lambda\) is **symmetric positive definite (SPD)**, not merely PSD, and therefore invertible. Its inverse \(H_\lambda=A_\lambda^{-1}\) is SPD and invertible as well.

The objective

\[
J_\lambda(\tau)=\|x-\tau\|_2^2+\lambda\|D_d\tau\|_2^2
\]

has gradient \(2(I+\lambda Q)\tau-2x\) and Hessian \(2(I+\lambda Q)\succ0\). It is strictly convex and coercive: a finite, **unique global minimizer always exists** for each finite \(\lambda\ge0\) and every observed vector \(x\), namely \(\widehat\tau_\lambda=H_\lambda x\). This result holds even though \(Q\) itself is singular.

For the spectral eigenvalues, \(\delta_1=\cdots=\delta_d=0\), \(\delta_j>0\) otherwise, we have

\[
\operatorname{eig}(A_\lambda)=1+\lambda\delta_j\ge1,\qquad
\operatorname{eig}(H_\lambda)=(1+\lambda\delta_j)^{-1}\in(0,1].
\]

Therefore, for **finite** \(\lambda\), \(\ker(H_\lambda)=\{0\}\): the \(d\) zero eigenvalues of \(Q\) become \(d\) eigenvalues **equal to one**, not zero, in \(H_\lambda\).

**Numerical nuance:** invertibility is not the same as good conditioning. When \(d\ge1\), \(\kappa_2(A_\lambda)=1+\lambda\,\delta_{\max}\) and can grow without bound as \(\lambda\) increases, even though every finite \(A_\lambda\) is invertible. Reusing a spectral factorization or solving a structured linear system is preferable to explicitly constructing an unstable matrix inverse.

### C2. Why the smoother always has real eigenvalues and real eigenvectors

**Scope:** real consecutive-difference \(\displaystyle D_d\), \(1\le d<L\), pure zero-drift PLS, and finite \(\lambda\ge0\). We are discussing **the smoothing matrix** \(H_\lambda\), not the generally rectangular forecast continuation operator \(G_{d,h}\). The source code's forecasting module has also used the name `H` for a continuation matrix; use \(G_{d,h}\) in this manuscript to avoid a symbol collision.

1. \(Q=D_d^\top D_d\) is **real symmetric**, since \(Q^\top=Q\), and **PSD**, since \(v^\top Qv=\|D_dv\|^2\ge0\). The real symmetric **spectral theorem** guarantees an orthonormal basis \(u_1,\ldots,u_L\in\mathbb R^L\) with **real**, nonnegative eigenvalues \(\delta_j\):
   \[
   Qu_j=\delta_j u_j,\qquad U^\top U=I.
   \]
   Nonnegativity also follows from \(\delta_j\|u_j\|^2=\|D_du_j\|^2\ge0\).

2. Hence
   \[
   (I+\lambda Q)u_j=(1+\lambda\delta_j)u_j.
   \]
   Since \(1+\lambda\delta_j\ge1>0\), inversion is valid. Therefore the **same real orthonormal eigenvectors** diagonalize \(H_\lambda\), with
   \[
   \boxed{H_\lambda u_j=\mu_j(\lambda)u_j,\qquad
   \mu_j(\lambda)=\frac{1}{1+\lambda\delta_j}\in(0,1].}
   \]
   In particular, \(H_\lambda=H_\lambda^\top\succ0\) for finite \(\lambda\ge0\); it has a complete real eigenbasis and **only real positive eigenvalues**.

3. Exactly \(d\) eigenvalues of \(Q\) are zero; they become **eigenvalues equal to one**, not zero, in \(H_\lambda\). As \(\lambda\to\infty\), the remaining \(L-d\) eigenvalues converge to zero. The exact endpoint \(H_\infty=U_0U_0^\top\) remains real symmetric and PSD but **not** strictly positive definite or invertible. Its eigenvalues are exactly \(d\) ones and \(L-d\) zeros.

4. Each response factor \(\mu_j(\lambda)\) measures the retained weight of a spectral direction, so
   \[
   \operatorname{edf}(\lambda)=\operatorname{tr}(H_\lambda)
   =\sum_{j=1}^{L}\mu_j(\lambda),\qquad
   S=\frac{L-\operatorname{edf}}{L-d}.
   \]
   Thus the EDF need **not** be an integer: partial spectral shrinkage gives fractional model complexity; at \(d=2\), its minimum is **2**, corresponding to a least-squares line (not 1 EDF). \(\lambda=0\) gives \(L\) EDF; \(S=1\) gives \(d\) EDF.

**Important limitations:** these real-spectral guarantees rely on the symmetric pure PLS smoother. They do not automatically transfer to an arbitrary non-symmetric fitting operator, a forecast operator \(G_{d,h}\in\mathbb R^{h\times L}\), or a modified penalty without its own assumptions. This is a statement about eigenvalues of **matrices**, distinct from whether the forecast-MSE objective \(F(S)\) is convex or has a unique optimum.

**Numerical implementation:** `src/trend_estimation/core/pure.py` uses `np.linalg.eigh` to diagonalize \(Q\) (real symmetric), and `src/trend_estimation/core/smoothness.py` uses the resulting eigenvalues to compute EDF. This is **spectral diagonalization**, not Cholesky factorization. Cholesky could alternatively solve \((I+\lambda Q)\widehat\tau=y\) for valid \(d\), since the coefficient matrix is SPD, but would not by itself provide the spectral response \(\mu_j(\lambda)\).

### D. The exact limiting model S=1 does NOT need an epsilon

The equality \(S=1\) is reached only in the limit \(\lambda\to\infty\), never by finite \(\lambda\), because the \(L-d\) positive-eigenvalue shrinkage terms are strictly positive at finite penalty. The expression \((I+\infty Q)^{-1}\) is **not** an ordinary matrix inversion. Instead take the spectral limit, letting \(U_0\in\mathbb R^{L\times d}\) contain an orthonormal basis of \(\ker(D_d)\):

\[
\boxed{H(1)=H_\infty=\lim_{\lambda\to\infty}H_\lambda
=U_0U_0^\top=P_{\ker(D_d)}.}
\]

\(H_\infty\) is symmetric PSD, idempotent, **rank \(d\)**, and **nullity \(L-d\)**. It is singular (for \(1\le d<L\)), but that does **not** mean the fitted trend ceases to exist.

At the endpoint the right optimization problem is the **unique constrained least-squares fit**

\[
\boxed{\widehat\tau_\infty
=\underset{\tau:\,D_d\tau=0}{\arg\min}\|x-\tau\|_2^2
=U_0U_0^\top x.}
\]

**Proof of uniqueness:** every feasible \(\tau=U_0a\); minimizing \(\|x-U_0a\|^2\) in \(a\) gives the unique solution \(a=U_0^\top x\), since \(U_0^\top U_0=I_d\). So \(H_\infty\) is a *singular operator with a uniquely determined output*; we are not trying to invert it.

With \(d=2\), this is simply the ordinary least-squares line fitted to the \(L\) observations. There is no reason to replace \(S=1\) by \(1-\varepsilon\). Such a replacement is an approximation and may miss a global forecast-loss minimum at the true endpoint.

### E. What exactly is guaranteed for the forecast-CV paper?

1. **Unique fitted trend:** for each fixed \(S\in[0,1]\), the fit \(H(S)x\) is uniquely defined (finite penalty or exact constrained endpoint).
2. **Existence of an optimal selected smoothness:** \(H(S)\) extends continuously to \(S=1\); consequently, every fixed finite-fold pooled forecast-MSE function \(F^{\mathrm{pool}}(S)\) is continuous on compact \([0,1]\) and **attains a global minimum** (Weierstrass theorem).
3. **NOT guaranteed:** a unique optimal \(S\), a convex/unimodal forecast-loss surface, numerically complete discovery of all minima, or superior out-of-sample forecasting. Existence is not the same as these stronger properties.

Finally, the \(d\) unshrunk eigen-directions imply

\[
\operatorname{edf}(\lambda)=\operatorname{tr}(H_\lambda)\in[d,L],\quad
S_{\mathrm{raw}}=1-\frac{\operatorname{edf}}L\in[0,1-d/L].
\]

Rescaling to the **attainable** range produces

\[
\boxed{S=\frac{S_{\mathrm{raw}}}{1-d/L}
=\frac{L-\operatorname{edf}}{L-d}\in[0,1].}
\]

This normalized index is an equivalent coordinate for a known smoother, **not a new estimator or a change to its exact optimal trend**. The matrix facts justify why the denominator is \(L-d\) and why both endpoints are mathematically admissible.

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
