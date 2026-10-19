# Known variance-ratio benchmark against pooled LOOCV

**Protocol recorded:** 2026-10-18.
**Status:** independently executable experiment; do not infer outcomes from source formulation or an unrun pilot.

## 1. Why this is a separate experiment

The original Cortés-Toto-style factorial constructed deterministic linear or nonlinear trends and added white noise. It therefore does **not** supply a latent trend-innovation variance parameter. Applying \(\lambda=\sigma_\eta^2/\sigma_\varepsilon^2\) to that earlier DGP without defining \(\varepsilon\) would be meaningless.

Guerrero (2007), *Time series smoothing by penalized least squares*, Section 2 and Proposition 1 (especially equations (3), (6)–(7), and (12)–(13)), instead specifies

\[
y_t=\tau_t+\eta_t,\quad
D_d\tau=\mu\boldsymbol1+\varepsilon,\quad
\mathbb E\eta=0,\quad \operatorname{Var}(\eta)=\sigma_\eta^2 V,\quad
\mathbb E\varepsilon=0,\quad\operatorname{Var}(\varepsilon)=\sigma_\varepsilon^2I,\quad
\operatorname{Cov}(\eta,\varepsilon)=0.
\]

With \(V=I\), \(\mu=0\), and \(\lambda_G=\sigma_\eta^2/\sigma_\varepsilon^2\), the source's model-informed optimal linear trend estimator reduces to

\[
\widehat\tau_G
=(I+\lambda_GD_d^\top D_d)^{-1}y.
\]

**Source distinction:** Guerrero's main operational recommendation is to **specify a target percentage of smoothness** using a trace-based index, rather than to estimate the two variances from arbitrary data. We label use of the **known true DGP ratio** as an oracle **model-informed benchmark**. We are not implementing a variance-component estimator from the 2007 paper, and cannot apply this oracle directly to empirical financial data.

## 2. Exact new simulation

For each independent series \(r=1,\ldots,R\) in a pool, independently draw

\[
\varepsilon_t^{(r)}\stackrel{\rm iid}{\sim}
N(0,\sigma_\varepsilon^2),\qquad
\eta_t^{(r)}\stackrel{\rm iid}{\sim}N(0,\sigma_\eta^2),
\]
with innovations independent of observation noise. Choose \(d=2\); use

\[
\tau^{(r)}_1=a,\quad
\tau^{(r)}_2=a+b,\quad
\tau^{(r)}_t=2\tau^{(r)}_{t-1}
-\tau^{(r)}_{t-2}+\varepsilon_{t-2}^{(r)}
\quad (t=3,\ldots,N),
\]

and \(y_t^{(r)}=\tau_t^{(r)}+\eta_t^{(r)}\). The recurrence ensures **exactly** \(D_2\tau=\varepsilon\). The initial intercept/slope are deterministic and constitute an unpenalized polynomial nullspace component. This is not an actual finite-variance diffuse-state prior simulation; the variance ratio remains the classical PLS benchmark and its unconditional MMSE interpretation must be qualified for this initialization.

Each pool shares known \(d,N,\sigma_\eta,\sigma_\varepsilon\), but its \(R\) stochastic latent trends and observation errors are drawn **independently**. This differs intentionally from the original deterministic-trend replication pool, where observations shared a common latent trend. Do **not** pool series with different true ratios in the same optimization.

## 3. Four selections, one fitted estimator

For each generated pool:

1. **Guerrero known ratio:** \(\lambda_G=\sigma_\eta^2/\sigma_\varepsilon^2\); this method *knows simulation variances*.
2. **Single-start bounded Brent:** numerical minimizer candidate of the pooled LOOCV objective.
3. **Multibracket derivative Brent:** finds sign-change roots, evaluates candidates and both exact endpoints.
4. **Finite dense grid:** reference sampled at declared 401 points (pilot) or 121 points (smoke), with exact endpoints. **Not a global certificate.**

All four use identical \(H_\lambda\) to compute fitted trends. Only the selection mechanism differs. Pool LOOCV before minimization:

\[
F_R(\lambda)=\frac1{RN}\sum_{r,i}
\left[\frac{y^{(r)}_i-(H_\lambda y^{(r)})_i}
{1-(H_\lambda)_{ii}}\right]^2.
\]

**Important: the Guerrero method is not supposed to minimize the realized LOOCV function.** Our expected pattern, rather than an advance claim, is that the multibracket procedure often achieves a no-greater observed LOOCV value but need not have smaller trend reconstruction error.

## 4. Two losses, explicitly different

After the parameter is selected, report both

\[
\mathrm{LOOCV}(\widehat\lambda)
=F_R(\widehat\lambda),
\quad
\mathrm{TrendMSE}(\widehat\lambda)
=\frac1{RN}\sum_{r,i}
(\widehat\tau_i^{(r)}(\widehat\lambda)-\tau_i^{(r)})^2.
\]

**True \(\tau\) must not influence the feasible LOOCV selection.**
The realized trend MSE is an *evaluation diagnostic*. It is not the LOOCV training error, not a forecast error, and not an oracle-tuned benchmark. We may optionally add the trend-MSE-minimizing oracle later, but it must be clearly labelled non-deployable.

## 5. Computational plan and predeclared endpoints

- **Smoke:** 2 settings \(N=24\); \(\sigma_\eta\in\{0.5,2\}\), \(\sigma_\varepsilon=0.25\); 2 independent seeds per setting; \(R\in\{1,3\}\): **8 pools × 4 methods = 32 rows**.
- **Pilot:** \(N\in\{50,200\}\), \(\sigma_\eta\in\{0.5,2\}\), \(\sigma_\varepsilon\in\{0.1,0.3,1.0\}\): **12 settings**, 5 seeds each, \(R=1\) and 3: **120 pools × 4 methods = 480 rows**.
- **Independent confirmatory:** same settings, 100 new independent seeds per setting, unique disjoint seed offset: **2400 pools × 4 methods**, manually run only after pilot validation.
- \(d=2\), λ scanned in \(\log\lambda\in[-20,35]\), with λ=0 and λ=∞ evaluated exactly. Fixed initial intercept 0 and slope 0.02.
- Comparison metrics: paired mean LOOCV MSE, paired mean latent trend MSE, winner frequency within identical pool, selected S vs known \(S(\lambda_G)\), boundary hits, candidate roots, and uncertainty by **independently generated pool replicate**. Nested \(R=1/R=3\) samples share the first observed series; preserve seed coupling for inference.
- Save **manifest**, per-method CSV, grouped summary JSON, visual reconstruction example, objective/latent MSE curves. Track code SHA, software version, seeds, algorithm budgets. Do not overwrite prior 2017-inspired experiment outputs.

## 6. Run commands

From the repository root after activating the existing Conda environment:

    python -m pytest tests/test_guerrero_ratio_pooled_loocv.py -q
    python -m experiments.pooled_loocv_smoothness.guerrero_ratio --preset smoke --out-dir results/pooled_loocv_smoothness/guerrero/smoke
    python -m experiments.pooled_loocv_smoothness.guerrero_ratio --preset pilot --dry-run
    python -m experiments.pooled_loocv_smoothness.guerrero_ratio --preset pilot --out-dir results/pooled_loocv_smoothness/guerrero/pilot

The confirmatory run must be independent, not simply pooled with pilot results:

    python -m experiments.pooled_loocv_smoothness.guerrero_ratio --preset confirmatory --out-dir results/pooled_loocv_smoothness/guerrero/confirmatory

**No result is a publication-ready assertion until independently audited.** A better Brent LOOCV score is a numerical objective observation; the Guerrero known-ratio benchmark addresses a different (model-based) statistical question.
