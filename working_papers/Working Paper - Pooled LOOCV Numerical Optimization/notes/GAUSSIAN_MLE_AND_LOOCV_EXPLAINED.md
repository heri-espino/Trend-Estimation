# Why Gaussian variance likelihood can beat observed LOOCV at latent-trend recovery

**Research explanation; current implementation, not a claim about Guerrero's published estimation algorithm.**

## 1. The stochastic model

For \(N\) observations, \(d=2\),

\[
 y=\tau+\eta,\qquad D_2\tau=\varepsilon,\qquad
 \eta\sim N(0,b I_N),\quad \varepsilon\sim N(0,a I_{N-2}),
\]

with independent components and independent series \(r=1,\dots,R\) of the same \(N,a,b\). Variance convention: \(a=\sigma_\varepsilon^2\) (stochastic trend's **second-difference variance**), \(b=\sigma_\eta^2\) (observation-noise variance). In the model, \(\lambda=b/a\). Under Gaussian assumptions the ratio is a natural model-informed PLS penalty, not a fixed LOOCV minimum in each realized dataset.

Let \(z_r=D_2 y_r\) and \(A=D_2D_2^\top\). Crucial identity:

\[
 z_r=\varepsilon_r+D_2\eta_r,\qquad
 \Sigma(a,b)=a I_{N-2}+b A.
\]

The finite-sample covariance is NOT diagonal after differencing: for d=2 the first three covariance lags are \(a+6b,-4b,b\). This is the information identifying the two unknown variances.

## 2. Actual Gaussian likelihood of DIFFERENCED DATA (not full y likelihood)

Let \(m=N-2\), \(\Sigma=aI+bA\). With centered normal contrasts,

\[
 -\log L(a,b)=\frac{R}{2}\log|\Sigma|+
 \frac12\sum_{r=1}^{R}z_r^\top\Sigma^{-1}z_r+\mathrm{constant}.
\]

The existing code \`variance_estimation.py::estimate_gaussian_differences\` diagonalizes \(A=U\,\mathrm{diag}(\alpha_j)\,U^\top\), and sets \(p\in[0,1]\), \(\bar\alpha=m^{-1}\sum_j\alpha_j\):

\[
 g_j(p)=(1-p)+p\,\frac{\alpha_j}{\bar\alpha},\quad
 \Sigma=v\,U\mathrm{diag}(g_j(p))U^\top.
\]

For fixed \(p\), define \(\bar q_j=R^{-1}\sum_r (u_j^\top z_r)^2\). Analytically profile the common scale

\[
 \widehat v(p)=\frac1m\sum_{j=1}^m\frac{\bar q_j}{g_j(p)}.
\]

Now minimize the one-dimensional profile negative log likelihood (up to constants)

\[
 J(p)=\frac12\left[\log\widehat v(p)
 +\frac1m\sum_{j=1}^m\log g_j(p)+1\right].
\]

The actual code uses a finite scan across \(p\in[0,1]\), bounded local minimization of detected basins, and compares both endpoints: NOT an exact general global certificate. Recover

\[
 \widehat a=\widehat v(1-\widehat p),\quad
 \widehat b=\frac{\widehat v\widehat p}{\bar\alpha},\quad
 \boxed{\widehat\lambda_\mathrm{ML}=\widehat b/\widehat a}.
\]

When \(\widehat a=0\), \(\widehat\lambda=+\infty\) and the smoother becomes the nullspace projection. No simulated latent \(\tau\) is read by this estimator. Under heavy-tailed or correlated noise, this is a **misspecified Gaussian contrast likelihood / quasi-ML**, not a genuine likelihood for the true DGP.

## 3. What is the reconstruction smoother?

Both feasible methods use exactly the same PLS operator once \(\lambda\) is selected:

\[
 H_\lambda=(I+\lambda D_2^\top D_2)^{-1},\qquad
 \widehat\tau_\lambda=H_\lambda y.
\]

Guerrero's known true ratio, the feasible fitted ratio, and observed LOOCV only differ by **how they select \(\lambda\)**; they are not three fundamentally different function classes or reconstruction operators.

## 4. What does ordinary pooled LOOCV MSE evaluate?

Let \(h_{ii}\) be diagonal elements of \(H_\lambda\). For \(R\) series,

\[
 \mathrm{LOOCV}(\lambda)=
 \frac1{RN}\sum_{r=1}^{R}\sum_{i=1}^N
 \left[\frac{y_{ri}-(H_\lambda y_r)_i}{1-h_{ii}}\right]^2
 =\frac1{RN}\sum_{r,i}
 (y_{ri}-\widehat y_{ri}^{(-i)}(\lambda))^2.
\]

The leave-one-out fitted value \(\widehat y_{ri}^{(-i)}\) is computed **without** the observed target \(y_{ri}\) in that fit. The expression above is the exact PRESS identity for this fixed-parameter linear smoother; the numerical code uses the algebraically equivalent \(T_\lambda=Q(I+\lambda Q)^{-1}\) representation to handle \(\lambda=0\) smoothly. CV optimizes agreement with **held-out noisy observations \(y\)**, not with the unknown \(\tau\). Autocorrelated errors violate the usual independence interpretation of point deletion.

## 5. How is true-trend MSE computed?

Simulation generates and stores \(\tau\) in memory before adding noise:

\[
 y=\tau+\eta.
\]

After a feasible method selects \(\widehat\lambda\) using only \(y\), it computes

\[
 \mathrm{TrendMSE}(\widehat\lambda)=
 \frac1{RN}\sum_{r,i}
 ((H_{\widehat\lambda}y_r)_i-\tau_{ri})^2.
\]

The true \(\tau\) is then a **held-out evaluation target**, not part of selection. In market data we do not observe a unique objective true price trend; without such a ground truth, *this* reconstruction MSE cannot be calculated directly. A smaller trend MSE means smaller **squared discrepancy from the generated latent signal**, not necessarily superior prediction of future returns/prices, trading value or volatility forecasting.

A method optimizing noisy targets can attain smaller LOOCV MSE while having larger latent-trend reconstruction MSE. This is no mathematical contradiction: the two loss functions evaluate distinct errors. Under iid additive observation noise, holding out \(y_i\) includes random measurement noise absent from latent truth; under serial correlation, the held-out noise can be partially guessed using neighboring noisy observations.

## 6. What the earlier executed robustness pilot showed

The uploaded 5-regime pilot (R=3, 20 pooled evaluations per regime) recorded:

| Noise type | Gaussian differenced-covariance ML true trend MSE | Ordinary LOOCV true trend MSE |
|---|---:|---:|
| Gaussian iid | 0.355507 | 0.355433 |
| t(5) measurement noise | 0.337182 | 0.352827 |
| t(5) second-difference trend innovations | 0.335247 | 0.336293 |
| AR(1) observation noise | 1.350641 | 1.704392 |
| Changing variance | 0.335961 | 0.354783 |

The large pooled advantage was dominated by the AR(1) mechanism. The original mathematical/numerical optimization paper does NOT become a new statistical MLE contribution merely because we compare these known estimators. The follow-up [TAIL_NOISE_PROTOCOL.md](TAIL_NOISE_PROTOCOL.md) stresses Student t(3), asymmetry, jumps, GARCH volatility and Cauchy without asserting which method will win.

## 7. Critical Cauchy warning

For \(X\sim\mathrm{Cauchy}(0,\gamma)\): \(\mathbb E[X]\), \(\operatorname{Var}(X)\), \(E[X^2]\), and excess kurtosis **do not exist as finite numbers**. Calling a Cauchy distribution "zero mean" is incorrect; its **median and location are zero**. Therefore:

- the Guerrero ratio \(\sigma_\eta^2/\sigma_\varepsilon^2\) is **undefined** if observation noise is Cauchy;
- Gaussian covariance likelihood estimates finite numeric *pseudo-parameters*, not the true noise variances;
- a finite simulated reconstruction MSE can be measured, but its population expectation is infinite for our nontrivial linear smoothers. Compare *medians* of per-pool realized errors and absolute-error quantiles for Cauchy; never claim a population MSE ranking.

Stock returns in general do not need a Cauchy assumption. Student-t with finite variance and GARCH-style volatility clustering are better primary stylized controls, while Cauchy is useful as a deliberate breakdown example.
