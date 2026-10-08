# Model, notation, and computation at a glance

**Updated: 2026-10-08.** See [mathematical_foundations.md](mathematical_foundations.md) for step-by-step derivations and hypotheses.

At outer forecast origin \(T\), only \(y_{1:T}\) is known. Use \(L\) observations for fitting, \(d<L\) for the penalty order, \(h\ge1\) for future forecast length:

\[
x_t=(y_{t-L+1},\ldots,y_t)^\top\in\mathbb R^L,\qquad
z_t=(y_{t+1},\ldots,y_{t+h})^\top\in\mathbb R^h.
\]

At a historical validation origin \(t\), \(z_t\) is already realized by the current \(T\) only if \(t+h\le T\). At \(t=T\), \(z_T\) is unknown until the outer test has concluded.

## Difference penalty and eigensystem

\[
D_d\in\mathbb R^{(L-d)\times L},\quad Q=D_d^\top D_d,\quad
v^\top Qv=\|D_dv\|^2\ge0.
\]

For the usual finite differences, \(\operatorname{rank}(Q)=L-d\). Let

\[
Q=U\operatorname{diag}(0,\ldots,0,\delta_1,\ldots,\delta_{L-d})U^\top,
\qquad\delta_j>0.
\]

The \(d\)-dimensional kernel consists of discrete polynomials of degree at most \(d-1\). Eigenvectors diagonalize the *smoothing action*; one decomposition for fixed \(L,d\) can be reused.

**Structural facts (standard consecutive differences, \(1\le d<L\)):**
\[
\operatorname{nullity}(D_d)=\operatorname{nullity}(Q)=d,\quad
\operatorname{rank}(D_d)=\operatorname{rank}(Q)=L-d.
\]
The first \(d\) values determine every sequence with \(D_dx=0\) (rank-nullity). Equality of the kernels follows since \(Qx=0\Rightarrow x^\top Qx=\|D_dx\|^2=0\Rightarrow D_dx=0\); the converse is immediate.

For every **finite** \(\lambda\ge0\), \(A_\lambda=I+\lambda Q\succ0\) because \(v^\top A_\lambda v=\|v\|^2+\lambda\|D_dv\|^2>0\) for all \(v\ne0\). Thus \(H_\lambda=A_\lambda^{-1}\succ0\) is invertible, and the PLS criterion has a unique minimizer. At the exact **\(S=1\)** limit, \(H(1)=U_0U_0^\top\) is a **singular projection** of rank \(d\), nullity \(L-d\); the fitted trend is nevertheless the unique constrained least-squares polynomial. No artificial \(1-\varepsilon\) endpoint is needed.



## Smoother and scalar smoothness

\[
H_\lambda=(I+\lambda Q)^{-1}
=U\operatorname{diag}\left(1,\ldots,1,
\frac1{1+\lambda\delta_1},\ldots,\frac1{1+\lambda\delta_{L-d}}\right)U^\top,
\quad \widehat\tau_t=H_\lambda x_t.
\]

\[
S(\lambda)=\frac{L-\operatorname{tr}H_\lambda}{L-d}
=1-\frac1{L-d}\sum_{j=1}^{L-d}\frac1{1+\lambda\delta_j}.
\]

\(H\) is a **matrix that performs smoothing**. \(S\) is a **scalar measuring how much smoothing** was achieved. \(\lambda\) is the original penalty strength and an algebraically convenient auxiliary coordinate. We **select/report \(S\in[0,1]\)**; \(\lambda(S)\) is inverted as needed.

\[
H(0)=I,\quad H(1)=P_{\ker D_d},\quad
\operatorname{edf}=L-(L-d)S.
\]

## Forecast continuation and loss

\(G_{d,h}\in\mathbb R^{h\times L}\) continues fitted terminal differences by assuming zero future \(d\)th difference. For \(d=1,2,3\), this gives constant, linear, and quadratic continuations respectively. **Fixing \(d\) fixes maximum polynomial degree**; searching \(S\) adjusts the coefficients.

\[
\widehat z_t(S)=G_{d,h}H(S)x_t,\qquad
F_t(S)=\frac1h\|z_t-\widehat z_t(S)\|_2^2.
\]

\[
F^{\mathrm{pool}}_{T,d,L,h}(S)=\frac1M\sum_{t_m+h\le T}F_{t_m}(S),
\quad
\widehat S_T\in\arg\min_{S\in[0,1]}F^{\mathrm{pool}}_{T,d,L,h}(S).
\]

The sum has \(M\) selected eligible historical origins, not necessarily *every* eligible origin; all training and test splits must be declared before the outer forecast.

## Derivatives in one line

\[
H'_\lambda=-H_\lambda QH_\lambda,\quad
H''_\lambda=2H_\lambda QH_\lambda QH_\lambda,\quad
H_\lambda^{(n)}=(-1)^n n!\,H_\lambda(QH_\lambda)^n.
\]

Let \(r=z-GH_\lambda x\). Then

\[
f'(\lambda)=\frac2h r^\top GH_\lambda QH_\lambda x,\quad
f''(\lambda)=\frac2h\|GH_\lambda QH_\lambda x\|^2
-\frac4h r^\top GH_\lambda QH_\lambda QH_\lambda x.
\]

For \(F(S)=f(\lambda(S))\):

\[
F'(S)=\frac{f'(\lambda)}{S'(\lambda)},\qquad
F''(S)=\frac{f''(\lambda)}{S'(\lambda)^2}
-\frac{f'(\lambda)S''(\lambda)}{S'(\lambda)^3}.
\]

**Multiple stationary points are possible.** No guaranteed unique minimum follows from this calculus. A global decision compares all recovered minima and **both limits**.

## Research status

The eigendecomposition, index identities, resolvent derivatives, and continuation are mathematical facts for this model. Which optimizer is most reliable/efficient at large \(L\), and whether the chosen \(S\) improves outer forecasts under revised simulations, are still open experimental questions. Archived CP03 results are not erased, but are not yet the final redesigned evidence.
