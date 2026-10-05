# Research objective

## Primary question

For trend forecasting, does regularizing a low-dimensional Bernstein/Bézier control representation produce meaningfully different endpoint behavior from regularizing the sampled trend directly with finite differences?

## Formal candidate problem

Let

\[
y_t=\tau(t)+\varepsilon_t.
\]

### Model F — finite-difference trend

\[
\widehat\tau^{(F)}_\lambda
=
\arg\min_\tau
\|y-\tau\|^2
+
\lambda\|D_d\tau\|^2.
\]

### Model B — Bernstein/control trend

For a Bernstein basis \(B_K\),

\[
\widehat\beta_{\lambda,K,q}
=
\arg\min_\beta
\|y-B_K\beta\|^2
+
\lambda\|D_q\beta\|^2,
\]

\[
\widehat\tau^{(B)}
=
B_K\widehat\beta.
\]

The key scientific comparison is therefore

\[
\text{regularize in observation/trend space}
\quad\text{versus}\quad
\text{regularize in control-coefficient space}.
\]

## Forecasting layer

For each rolling origin \(T\), fit using only information available by \(T\).

Candidate Bézier forecast maps should use terminal derivatives or a new continuity-constrained segment, not unconstrained evaluation far outside the fitted interval.

Let \(J\) denote a continuation rule. Then

\[
\widehat z_T(\lambda,K,q,J)
=
G^{(B)}_{K,q,J,h}
\widehat\beta_{T,\lambda,K,q}.
\]

Select hyperparameters chronologically:

\[
(\lambda^\star,K^\star,q^\star,J^\star)
\in
\arg\min
\frac{1}{|\mathcal O|h}
\sum_{T\in\mathcal O}
\|z_T-\widehat z_T(\lambda,K,q,J)\|^2.
\]

This must obey the repository validation invariant: no information after origin \(T\) may enter fitting or tuning.

## Main empirical questions

1. When are finite-difference and control-space smoothers nearly equivalent?
2. When does endpoint geometry create materially different forecasts?
3. Does a low-dimensional control representation reduce endpoint variance at the cost of bias?
4. How sensitive are conclusions to \(K\), penalty order \(q\), horizon \(h\), and noise dependence?
5. Is any advantage specific to smooth deterministic trends, or does it persist under stochastic/local trends?
6. Are gains still present after comparison with P-splines and smoothing splines, rather than only HP/PLS?

## Null result that is scientifically acceptable

If the Bernstein/control smoother behaves indistinguishably from a suitably matched P-spline and offers no robust endpoint forecasting advantage, the correct conclusion is equivalence/redundancy, not a forced new method.
