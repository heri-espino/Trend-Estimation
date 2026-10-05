# Model and notation

At origin \(T\),
\[
x_T=(y_{T-L+1},\ldots,y_T)^\top\in\mathbb R^L,
\qquad
z_T=(y_{T+1},\ldots,y_{T+h})^\top\in\mathbb R^h.
\]

\(x_T\) is the fitting history; \(z_T\) is unseen future data used only for scoring.

## Difference operator

\[
D_d\in\mathbb R^{(L-d)\times L},
\qquad
Q=D_d^\top D_d\in\mathbb R^{L\times L}.
\]

\[
v^\top Qv=\|D_dv\|^2\ge0,
\]
so \(Q\) is symmetric positive semidefinite. For the usual operator, \(\operatorname{rank}(Q)=L-d\).

## Smoother

\[
H_\lambda=(I+\lambda Q)^{-1},
\qquad
\widehat\tau_T(\lambda)=H_\lambda x_T.
\]

\(H\) is a matrix and performs the smoothing.

## Smoothness index

\[
S(\lambda)=
1-\frac1{L-d}\sum_{j=1}^{L-d}\frac1{1+\lambda\delta_j}.
\]

\(S\) is a scalar measuring average suppression of penalizable spectral directions.

\[
H\text{ performs smoothing;}\qquad
S\text{ measures the amount of smoothing.}
\]

## Forecast operator

\[
\widehat z_T(\lambda)=G_{d,h}H_\lambda x_T.
\]

For zero drift:
- \(d=1\): constant continuation;
- \(d=2\): linear continuation;
- \(d=3\): quadratic continuation.

For \(d=2\):
\[
\tau_{T+1}=2\tau_T-\tau_{T-1},
\qquad
\tau_{T+2}=3\tau_T-2\tau_{T-1}.
\]

## Loss notation

\[
r_T(\lambda)=z_T-GH_\lambda x_T,
\qquad
f_T(\lambda)=\frac1h\|r_T(\lambda)\|^2.
\]

\[
f(\lambda)=\frac1M\sum_T f_T(\lambda),
\qquad
F(S)=f(\lambda(S)).
\]

Thus \(f\) and \(F\) are the same MSE under different parameterizations.
