# Canonical research objective — forecast-optimal smoothness CV

## Primary research question

Can we choose the normalized smoothness index of a finite-difference
penalized trend to minimize actual historical forecast MSE at the
intended horizon `h`, rather than the error of recovering a
historical trend or fitting contemporaneous observations?

## Statistical construction

At each historical origin `t`, fit the training window
`x_t` with the matrix

\[
H_\lambda=(I+\lambda D_d^\top D_d)^{-1},
\qquad \widehat\tau_t=H_\lambda x_t.
\]

Let `S(lambda)` be the normalized, monotone trace-based
smoothness coordinate; let `G_{d,h}` extrapolate the fitted
trend for `h` observations.

The proposed chronological cross-validation criterion is

\[
F^{\mathrm{pool}}_{d,L,h}(S)
=\frac1M\sum_{m=1}^{M}\frac1h
\|y_{t_m+1:t_m+h}-G_{d,h}H_{\lambda(S)}x_{t_m}\|_2^2.
\]

Choose

\[
\widehat S^{\mathrm{FCV}}_{T,d,L,h}
\in\arg\min_{S\in[0,1]}F^{\mathrm{pool}}_{d,L,h}(S).
\]

All validation blocks must be realized by the outer forecast
origin `T`. Then refit the trend on the latest available
window. Never average historical fitted trends into the
operational forecast.

## Contribution boundaries

1. **Forecasting paper:** definition and evaluation of this
   horizon-matched CV selection procedure over normalized PLS
   smoothness. CP03 is the central experimental evidence.
2. **Numerical-methods paper:** locating multiple minima in
   the forecast-MSE objective, derivative bracketing, Brent
   refinement and endpoint comparisons. Exact rational/Sturm
   isolation is still experimental; it is not a completed
   certified root solver.
3. **Optional forecasting extension:** represent historical
   local minima by chronological branch states
   `V_j=[S, Validation-1 loss, Validation-2 loss]`, and,
   subject to assumptions about regime persistence, use
   `psi` and `phi(V_j)` to produce a time-adaptive
   smoothness choice. The different maps are alternative
   modeling decisions, not a universal winning method.

Neither PLS itself, the original Guerrero index, nor the
general idea of selecting a tuning parameter by future-block
forecast error is independently claimed as new. The specific
horizon-matched PLS selection criterion is the primary
scientific object.
