# Proof ledger — observed-series PLS/LOOCV numerical paper

Status key: **[CLASSICAL]**, **[DERIVED]**, **[OPEN]**, **[HYPOTHESIS]**. Algebraic derivation does not establish research novelty.

## P1. Nullspace and compact index [CLASSICAL / DERIVED]

For forward differences d on N>d equally spaced indices, rank(D_d)=N-d. Its kernel consists of sampled polynomials of degree at most d−1 and has dimension d. \(Q=D_d^\top D_d\succeq0\) has precisely d zero eigenvalues.

Let positive eigenvalues be q_j and set \(H_\lambda=(I+\lambda Q)^{-1}\). Then \(\operatorname{tr}H_\lambda=d+\sum_{q_j>0}(1+\lambda q_j)^{-1}\), whence

\[
S(\lambda)=\frac{1}{N-d}\sum_{q_j>0}\frac{\lambda q_j}{1+\lambda q_j},
\quad S'(\lambda)=\frac1{N-d}\sum_{q_j>0}
\frac{q_j}{(1+\lambda q_j)^2}>0.
\]

Thus finite λ>0 bijects with 0<S<1; λ=0 maps to S=0 and the λ→∞ limit maps to S=1. \(H_\infty=P_{\ker Q}\), an orthogonal projection of rank d. Guerrero's unnormalized index \(S_G=1-\operatorname{tr}H_\lambda/N=(N-d)S/N\). Note Cortés-Toto's source index/logit definition when reproducing their statistical tables.

## P2. LOOCV identity and finite endpoints [CLASSICAL / DERIVED]

For linear smoother H and positive finite λ, the leave-one-out residual is

\[
e_i^{(-i)}=\frac{y_i-(Hy)_i}{1-H_{ii}}.
\]

Since \(I-H_\lambda=\lambda Q(I+\lambda Q)^{-1}=\lambda T_\lambda\), cancellation gives \(e_i=(T_\lambda y)_i/(T_\lambda)_{ii}\). For every λ≥0 finite, \(T_\lambda\succeq0\), and \((T_\lambda)_{ii}>0\) because Q is positive semidefinite and the coordinate vector \(e_i\notin\ker Q\) for ordinary differences with N>d. Therefore no denominator vanishes in this representation.

At λ=0,

\[
e_i(0)=\frac{(Qy)_i}{Q_{ii}},
\]

which is the *continuous extension* of LOOCV (do not evaluate the 0/0 original H expression). At λ=∞, \(H_\infty=P\); because \(1-P_{ii}>0\), the exact endpoint is

\[
e_i(\infty)=\frac{[(I-P)y]_i}{1-P_{ii}}.
\]

**Implementation test:** verify endpoints against the limiting finite-λ curves at well-conditioned moderate N.

## P3. Derivative of the pooled criterion [DERIVED]

\(H'=-HQH\). Since Q commutes with H, \(T=QH\) has derivative \(T'=-T^2\). Write \(a_{ri}=(Ty^{(r)})_i\) and \(b_i=T_{ii}\). Quotient rule yields

\[
e'_{ri}=\frac{-(T^2y^{(r)})_i b_i+a_{ri}(T^2)_{ii}}{b_i^2},
\quad
F_R'=\frac{2}{RN}\sum_{r,i}e_{ri}e'_{ri}.
\]

For positive finite λ, \(F_R\) is continuously differentiable. Compare this derivative numerically with central differences in log λ, including near boundaries.

## P4. Rationality and exact root isolation [DERIVED with restricted hypotheses]

If all y values and difference coefficients are rational, entries of \((I+\lambda Q)^{-1}\) and T are rational functions over \(\mathbb Q(\lambda)\). The cancellation representation shows \(F_R(\lambda)\in\mathbb Q(\lambda)\) with no poles for λ≥0. Differentiate and reduce \(F'_R=A/B\) to coprime polynomials. If A is nonzero, there are finitely many positive real stationary roots. Exact Sturm sequences count distinct real roots of A in rational intervals and, after isolation, allow classification and comparison with endpoints. If A≡0, \(F_R\) is constant and *every* interior λ is stationary: an essential degenerate case.

**Limit:** floating-point noise, large N and high-degree exact numerators do not inherit computationally tractable certification. Brent sign scans can miss even-multiplicity roots and unresolved narrow extrema.

## P5. Existence, not uniqueness [CLASSICAL / DERIVED]

The endpoint limits exist and \(F_R\) is continuous on the compactified half-line [0,∞], equivalently on S∈[0,1]; by Weierstrass it has at least one global minimizer. This does NOT imply uniqueness or that a finite grid finds every minimum. A complete exact certificate needs all real positive stationary roots and exact boundary comparisons, or an independently justified global lower-bounding method.

## P6. Open research questions [OPEN / HYPOTHESIS]

- Are there practical, nondegenerate pools whose LOOCV curve has multiple *strict local minima*? Produce and certify examples; quantify prevalence under the 2017 factorial.
- How does independent replication R affect the number and separation of minima? It may remove, retain or generate structures; there is no declared monotonic theorem.
- Is adaptive derivative bracketing materially more accurate/efficient than tuned multistart bounded Brent under a fair budget?
- Can validated interval arithmetic or safe lower bounds extend complete positive-root searches beyond small exact inputs?
- How do pool heterogeneity, correlated errors and financial structural breaks affect the objective?
- What algorithmic improvement, if any, remains after comparison with pre-existing global GCV optimization?

**Do not use the simulated latent trend as a certificate of the objective's roots.** It permits a separate reconstruction-error diagnostic only.
