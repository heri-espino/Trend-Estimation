# Estimating the two variance components instead of treating their ratio as known

**Created:** 2026-10-18. **Paper:** independent pooled observed-series LOOCV numerical optimization. This is a separate feasible-estimation experiment, not a retrospective reinterpretation of the Cortés-Toto (2017) deterministic-trend factorial.

## 1. Scientific question and source boundary

Guerrero (2007), *Time series smoothing by penalized least squares*, uses the stochastic model

\[
y=\tau+\eta,\qquad D_d\tau=\mu{\bf1}+\varepsilon,
\]
with \(\operatorname{Var}(\eta)=\sigma_\eta^2 V\) and \(\operatorname{Var}(\varepsilon)=\sigma_\varepsilon^2 I\). Under \(V=I,\mu=0\), the classical model-motivated penalty is

\[
\lambda_G=\frac{\sigma_\eta^2}{\sigma_\varepsilon^2}.
\]

**Source boundary:** Guerrero (2007) does not supply the *particular two-component moment estimator or the particular difference-Gaussian likelihood procedure implemented here*. Those are our proposed feasible computational comparators. Guerrero's published practical emphasis is choosing a **smoothness percentage**, not claiming that the sample knows the two true innovation variances. We retain the actual \(\lambda_G\) as a model-informed **oracle** that is supplied with true simulation variances.

## 2. Why simply taking the variance of differences is wrong

Set \(z=D_dy\). The model implies

\[
z=\varepsilon+D_d\eta,\qquad
\boxed{\operatorname{Cov}(z)=aI+bA,\quad A=D_dD_d^\top,\quad
a=\sigma_\varepsilon^2,\ b=\sigma_\eta^2.}
\]

The noise produced by differencing \(\eta\) is correlated. For second differences,
the diagonal of \(A\) is 6 and its first and second off-diagonals are \(-4\) and \(1\). Thus \(\operatorname{Var}(z_t)=a+6b\) (interior for standard consecutive indices), while \(\operatorname{Cov}(z_t,z_{t+1})=-4b\) and \(\operatorname{Cov}(z_t,z_{t+2})=b\). Estimating only \(\operatorname{Var}(z)\) cannot identify both variance components.

With \(N>d+1\) and \(A\not\propto I\), both components are identifiable from the whole covariance model. **Identifiable in principle** does not imply precise for a short or highly noisy single realization.

## 3. Estimator A — two quadratic moments with nonnegative constraints

Let \(m=N-d\). Define

\[
u=\frac{\operatorname{tr}A}{m},\quad
v=\frac{\operatorname{tr}A^2}{m},\quad
M_0=\frac1{Rm}\sum_{r=1}^R \|z^{(r)}\|^2,\quad
M_1=\frac1{Rm}\sum_{r=1}^R (z^{(r)})^\top A z^{(r)}.
\]

Then the **classical quadratic expectation identity** gives

\[
\mathbb E\begin{pmatrix}M_0\\M_1\end{pmatrix}
=\begin{pmatrix}1&u\\u&v\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix}.
\]

Invert the 2×2 matrix to get unconstrained method-of-moments estimates, if \(v-u^2>0\). When an estimate is negative, use **nonnegative least squares on these two moment equations** rather than treating a negative value as a variance. Denote the result \((\hat a_{\mathrm{mom}},\hat b_{\mathrm{mom}})\).

**Known risk:** nonnegative least squares may select \(\hat a_{\mathrm{mom}}=0\), yielding \(\hat\lambda=\infty\) and a polynomial trend fit. For an actually stochastic integrated trend, this may cause **catastrophically high latent trend reconstruction error**. This failure should be preserved in experiments, not silently clipped to a convenient positive floor.

## 4. Estimator B — profiled marginal Gaussian likelihood of observed differences

Under independent Gaussian noises and independent stochastic trends across r,

\[
z^{(r)}\sim N(0,aI+bA).
\]

Let \(A=U\operatorname{diag}(\alpha_j)U^\top\), and write

\[
\mathcal L(a,b)\propto\sum_{j=1}^{m}
\left[\log(a+b\alpha_j)
+\frac{q_j}{a+b\alpha_j}\right],
\quad
q_j=\frac1R\sum_{r=1}^{R}(U^\top z^{(r)})_j^2.
\]

To estimate stably, set

\[
\bar\alpha=\frac1m\sum_j\alpha_j,\quad
a=v(1-p),\quad
b=\frac{vp}{\bar\alpha},\qquad 0\le p\le1.
\]

For each \(p\), define \(g_j(p)=(1-p)+p\alpha_j/\bar\alpha\), and analytically profile scale:

\[
\hat v(p)=\frac1m\sum_j\frac{q_j}{g_j(p)},\quad
\ell_{\rm prof}(p)=\log\hat v(p)+\frac1m\sum_j\log g_j(p).
\]

Numerically minimize this **one-dimensional** profile over [0,1], including boundaries, using coarse candidate detection and local bounded refinements. Then recover \(\hat a=\hat v(1-\hat p)\), \(\hat b=\hat v\hat p/\bar\alpha\) and \(\widehat\lambda_{\rm ML}=\hat b/\hat a\).

This is **marginal ML for z=D_dy**, not complete ML for y given deterministic initial trend conditions. It does not require knowing the simulated \(\tau\), or calculating LOOCV first. Its finite optimizer is not claimed to produce a rigorously certified global minimum for every possible dataset.

## 5. Four-way test at the same observed-series DGP

1. **Known true ratio (oracle):** \(\lambda_G=b/a\).
2. **Feasible difference-Gaussian ML:** \(\hat\lambda_{\rm ML}\).
3. **Feasible constrained method-of-moments:** \(\hat\lambda_{\rm MoM}\) (fragile failure-case control).
4. **Pooled LOOCV:** ordinary single-start Brent over the existing pooled reconstruction LOOCV objective.

Every selected \(\lambda\) uses the same \(H_\lambda\) estimator. Each method is scored on **both** realized pooled LOOCV MSE and realized latent trend MSE, the latter only possible in simulation. The variance estimators additionally report both estimated variance components and their errors.

The numerical dimension is unchanged (\(d=2\)); continue to distinguish these methods from the prior separate global-root-search question. Here, our main novelty question is **statistical sensitivity to estimated variance**, not a claim about a better optimizer.

## 6. Different levels versus different ratios

The existing Guerrero pilot contains 12 settings:

- \(N\in\{50,200\}\)
- \(\sigma_\eta\in\{0.5,2\}\) (observation noise)
- \(\sigma_\varepsilon\in\{0.1,0.3,1.0\}\) (trend innovation noise)
- \(R\in\{1,3\}\) (pool size)
- 5 replicates per setting, each paired across R sizes (seed baseline 20262000)

This yields **120 nested pools**, four methods per pool, 480 method rows. Its known ratios are \(0.25,2.777\ldots,25,4,44.444\ldots,400\), with multiple combinations repeated at both N values.

**Also** use an exact common-scale check \(y\mapsto cy,\tau\mapsto c\tau\), \(c\in\{0.5,1,2\}\), keeping the *same* base noise realization. This is not a second independent Monte Carlo campaign. Equivariant estimators should satisfy

\[
\hat a(cy)=c^2\hat a(y),\quad
\hat b(cy)=c^2\hat b(y),\quad
\hat\lambda(cy)=\hat\lambda(y).
\]

For any \(\lambda\), both realized LOOCV MSE and latent trend MSE should scale by \(c^2\). Normalized selected smoothness is invariant under this common scaling. **Increasing only one variance** changes the ratio and should change the target smoothness: observation noise increases should favor larger λ; trend-innovation noise increases should favor smaller λ, but any finite-sample estimator can deviate.

## 7. Reproduce and limitations

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_guerrero_variance_estimation.py -q
python -m experiments.pooled_loocv_smoothness.run_variance_estimation --preset smoke
python -m experiments.pooled_loocv_smoothness.run_variance_estimation --preset pilot
```

Outputs go to results/pooled_loocv_smoothness/guerrero/estimated_variances/{smoke,pilot}, separate from all previous experiments, including a pair of CSVs, manifest, scale consistency table, summary JSON and plot.

**Interpretation:** five seeds per scenario permit exploratory findings only; a confirmatory run must use independent seeds and preregister a feasible primary comparator. R=1 and R=3 are **nested** and not two independent trials. Financial series and model misspecification require a separate robustness design. Do not copy licensed PDFs into Git or imply variance estimates are explicitly proposed by Guerrero (2007).
