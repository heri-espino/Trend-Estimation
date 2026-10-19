# New finite-difference mean experiment: nonzero \(\mu\) in pooled observed-series reconstruction

**Date:** 2026-10-19 (America/Mexico_City). **Status:** code and mathematical protocol implemented on independent branch; **NO full pilot executed, NO empirical results claimed**. Tiny CI tests/smoke separate. This working paper studies **observed-series LOOCV and retrospective latent trend reconstruction**, NOT completed \(h\)-step forecast losses and NOT the fourth mean-difference forecasting paper.

## Source attribution and nonduplication

**Guerrero (2007) already allows nonzero** \(\mu=E[D_d\tau_t]\) and proposes a sample difference-mean *plug-in*, \(\widehat\mu_G=(N-d)^{-1}\mathbf1^\top D_d y\) (eqs. 17–18 as documented by the project's [source-based Obsidian note](../../../notes/conceptos/06-Media-de-diferencias-Guerrero.md)). Do **not** claim introducing nonzero \(\mu\) is novel. Our Gaussian **differenced-data mean/covariance MLE** and **fold-clean pooled observation-LOOCV fitting a common \(\mu\)** are explicit *extensions/comparators*, not estimators published by Guerrero.

The repo also already contains `working_papers/Working Paper - Trend Simulation and Mean-Difference Forecasting/` focused on **forecast** targets \(h\) and an analytically profiled \(\mu(S)\). This is a *different estimand*. Do not merge code, datasets, or originality claims between them; reuse of the same well-known affine identity is conceptual background.

## 1. DGP and assumptions

The analyst **chooses and fixes \(d=2\)**, as in the original pooled observed-LOOCV paper, and assumes comparable equal-length independent series. For each \(r=1,\ldots,R\) and all t,

\[
y^{(r)}=\tau^{(r)}+\eta^{(r)},\quad
D_d\tau^{(r)}=\mu\mathbf1+\varepsilon^{(r)},\quad
E[\varepsilon^{(r)}]=0,\quad E[\eta^{(r)}]=0,
\]
\[
\varepsilon^{(r)}\overset{\rm iid}\sim N(0,aI_{N-d}),\quad
\eta^{(r)}\overset{\rm iid}\sim N(0,bI_N),\qquad
a=\sigma_\varepsilon^2,\quad b=\sigma_\eta^2,\quad
\lambda_G=b/a.
\]

One common \(\mu\) and \(\lambda\) across a pool; independent realized innovations and observation noise across pool members. True initial level 0, true initial slope 0.02. The first R=1 member is nested within R=3. Across the five \(\mu\) values at the same \((N,\sigma_\eta,\text{replicate})\), the **identical random epsilon and eta draws** are reused, and only the deterministic \(\mu p\) signal is added. This intentionally isolates the mean violation, but \(\mu\) groups are therefore **paired, not independent**. The simulated true latent trend is **used for evaluation only**.

For \(p_j=\binom jd\), \(j=0,\ldots,N-1\), \(D_dp=\mathbf1\), hence \(\tau_\mu=\tau_0+\mu p\) with \(D_d\tau_0=\varepsilon\). That precisely controls nonzero difference mean without changing noise.

The five effects are \(\mu/\sigma_\varepsilon\in\{-1,-0.25,0,0.25,1\}\), with \(\sigma_\varepsilon=0.3\). They induce deterministic degree-2 growth for \(d=2\); for N200 the curvature can be very large. Always stratify by N and report relative/paired errors, not just pooled raw means.

## 2. Fixed-\(\mu\) PLS and endpoints

Let \(D=D_d\), \(Q=D^\top D\), \(H_\lambda=(I+\lambda Q)^{-1}\). For externally known \(\mu\), penalize differences toward that mean:

\[
\widehat\tau_{\lambda,\mu}
=\arg\min_{\tau}\left\{\|y-\tau\|^2+
\lambda\|D\tau-\mu\mathbf1\|^2\right\}
=H_\lambda y+\mu(I-H_\lambda)p
=\mu p+H_\lambda(y-\mu p).
\]

These identities are **classical** and proven in Obsidian note 06. At \(\lambda=\infty\), \(D\widehat\tau_{\infty,\mu}=\mu\mathbf1\), so an oracle known-\(\mu\) \(d=2\) smoother approaches a **quadratic** trend with the correct specified second difference, not a linear trend. With falsely fixed \(\mu=0\), the limiting trend is linear and can be very biased when the DGP has nonzero curvature.

With known fixed \(\mu\), pooled LOOCV on *shifted observations* \(y_r-\mu p\) exactly implements fold deletion while keeping exogenous \(\mu\) fixed. These known-\(\mu\) runs are **oracles** because \(\mu\) is the simulated truth.

## 3. Gaussian differenced-data likelihood jointly estimating \(\mu,a,b\)

For \(z_r=D y_r\), \(A=DD^\top\), \(m=N-d\),

\[
z_r\sim N(\mu\mathbf1,\Sigma),\quad \Sigma=aI_m+bA.
\]

With a fixed candidate covariance \(\Sigma\), the common GLS mean is

\[
\widehat\mu(\Sigma)=
\frac{\sum_{r=1}^R \mathbf1^\top\Sigma^{-1}z_r}
{R\,\mathbf1^\top\Sigma^{-1}\mathbf1}.
\]

The implementation diagonalizes \(A=U\operatorname{diag}(\alpha_j)U^\top\), parameterizes
\(\Sigma=vU\operatorname{diag}(g_j(p))U^\top\) with
\(g_j(p)=(1-p)+p\alpha_j/\bar\alpha\), \(p\in[0,1]\),
and profiles out both \(\mu\) and scale \(v\) for each p. A 61-point candidate scan and bounded local refinement plus endpoints supplies a **numerical solution, not proof of exact global optimality**. The same MLE routine can hold externally supplied true \(\mu\) fixed for an oracle isolation comparison.

This is a Gaussian contrast likelihood for differenced observations \(D y\), **not** a complete likelihood for y given diffuse or known initial state, not a claim about Guerrero's published MLE procedure, and not the Gaussian prior/posterior distribution for trajectories.

## 4. Jointly fitted mean within *observation*-LOOCV, without deletion leakage

An attractive but **INVALID** procedure would compute \(\widehat\mu\) once using **all data**, shift \(y-\widehat\mu p\), and then call ordinary fixed-mean PRESS while advertising it as leave-one-out validation. The deleted target would already have influenced \(\widehat\mu\).

Instead define, at each fixed \(\lambda\), a **single common pooled parameter** \(\mu\) by joint in-sample penalized least squares:

\[
(\widehat\tau_1,\ldots,\widehat\tau_R,\widehat\mu)
=\arg\min_{\tau_1,\ldots,\tau_R,\mu}
\sum_{r=1}^R\left[
\|y_r-\tau_r\|^2+\lambda\|D\tau_r-\mu\mathbf1\|^2\right].
\]

For \(\lambda>0\), put \(T_\lambda=Q(I+\lambda Q)^{-1}\),
\(b_\lambda=T_\lambda p\), \(k_\lambda=p^\top T_\lambda p>0\).
Completing the square, the full-data fitted common mean is

\[
\boxed{\widehat\mu_\lambda=
\frac{b_\lambda^\top\overline y}{k_\lambda}},
\qquad
\overline y=R^{-1}\sum_r y_r.
\]

The within-series full-data smoother block has diagonal
\[
h_{ri,ri}=(H_\lambda)_{ii}+
\frac{\lambda\,b_{\lambda,i}^2}{R k_\lambda},
\]
therefore the **exact leave-one-observation-out residual that re-fits \(\mu\) and \(\tau\) after deletion** is

\[
\boxed{e_{ri}(\lambda)=
\frac{(T_\lambda y_r)_i-
      b_{\lambda,i}\widehat\mu_\lambda}
{(T_\lambda)_{ii}-
 b_{\lambda,i}^2/(R k_\lambda)}}.
\]

Our implementation computes this ratio spectrally and evaluates the \(\lambda=0\) and \(\lambda=\infty\) **continuous endpoints** without dividing by numerically near-zero lambda. At infinity, scaled \(T\) tends to the projection onto \((\ker D)^\perp\). The R=1 limit has one extra unpenalized degree; with R independent series, the joint \(\mu\) estimator introduces one **global** free degree: the effective limiting fit space is dimension \(R\,d+1\), rather than \(R\,d\) for externally fixed \(\mu\). Accordingly, **the old \(S(\lambda)\) based on fixed-\(\mu\) \(H_\lambda\) is only a nominal penalty coordinate**, not the true EDF of the full data-selected-\(\mu\) procedure.

**Critical differentiation:** the pooled joint fitted \(\widehat\mu_\lambda\) is not Guerrero's simple observed-difference plug-in except in a special limit, and not the completed-origin \(h\)-step forecast-CV profiler from the fourth working paper. Dedicated regression tests compare this PRESS formula numerically to **explicit deletion and refitting of every trend and the common \(\mu\)**.

## 5. Eight comparisons, five feasible in practice

| Name in result CSV | \(\mu\) used | \(\lambda\) selection | Status |
|---|---|---|---|
| `known_mu_true_ratio_oracle` | true simulation \(\mu\) | true \(b/a\) | full model oracle |
| `zero_mu_gaussian_difference_ml` | forced zero | Gaussian difference likelihood for a,b | feasible but misspecified if true mu !=0 |
| `zero_mu_pooled_loocv` | forced zero | pooled ordinary observation LOOCV | feasible but misspecified if true mu !=0 |
| `known_mu_estimated_variance_ml` | true simulation \(\mu\) | Gaussian differenced ML for a,b given true mu | known-mean oracle |
| `known_mu_pooled_loocv` | true simulation \(\mu\) | pooled CV of shifted observed series | known-mean oracle |
| `estimated_mu_gaussian_gls_ml` | GLS profile \(\widehat\mu\) | joint Gaussian differenced ML of a,b,mu | feasible, full-data fit |
| `estimated_mu_fold_clean_pooled_loocv` | common pooled jointly penalized \(\widehat\mu_\lambda\) | optimize **exact fold-reestimated** PRESS over lambda | feasible, honest LOOCV selector |

**Important metric boundary:** true latent reconstruction MSE is computed identically for all eight methods and directly comparable within the *same simulated pool*. For the full-data GLS \(\widehat\mu\), a PRESS score computed while freezing that *all-data-estimated* mean is **NOT a valid fully refitted LOOCV score**. The results label that score `frozen_full_data_estimated_mu_PRESS_diagnostic_NOT_CV`; never use it to claim one method has lower honest CV. The exact fold-clean score for the `estimated_mu_fold_clean_pooled_loocv` method is separately marked `exact_fold_reestimated_mu_PRESS`. The oracle supplied mean is external/fixed and legitimately remains the same within folds. The pooled Guerrero-style plug-in estimates μ using ALL data and then fits covariance-ML conditional on μ; any frozen-μ PRESS shown for this hybrid is **diagnostic, not deletion-honest**, just like the full-data GLS mean's diagnostic.

## 6. Locked exploratory campaign

- **Automatic CI tiny smoke only:** N=24, eta SD 0.5, eps SD 0.3, mean factors -1/0/+1, one seed, nested R1/3: **6 pools × 8 = 48 method rows**. Smoke includes exact-fold-vs-direct-refit verification tests. The CI must NEVER run the pilot/confirmatory datasets automatically.
- **Manual exploratory pilot:** N∈{50,200}, eta SD∈{0.5,2.0}, eps SD 0.3, mean factors \(-1,-0.25,0,0.25,1\), five seeds per cell, nested R1/3: **20 scenarios ×5 seeds ×2 R=200 pools, 1,600 method rows**, 100 R3 treatment evaluations, but **only 20 distinct underlying random-innovation draws** (4 N×noise groups × five replicate seeds), reused across the five μ treatments; R1 nested. Each different mu factor shares underlying innovation/error noise at the same N, eta, seed.
- **Prospective confirmatory (NOT run):** same 20 cells with 100 new independent random seeds each, 4,000 nested pools, 32,000 method rows. Run only after auditing pilot, fixing comparisons, uncertainty method and computational costs.

`numpy.random.default_rng` base seed 69000000 for smoke/pilot, base 70000000 for fresh confirmatory, seed formula `base+N_index*10000+sigma_eta_index*1000+replicate`. Each scenario's N, noise SDs, d, true mu, true ratio, seed and selected variance estimates are retained in manifest and per-method CSV. Results **not** committed until user executes the full exploratory pilot.

Primary contrasts: on *paired* R3 pools, compare zero-mean restriction vs feasible fitted mean, Gaussian vs fold-clean CV, oracle mu vs estimated mu, and GLS mean estimation error by true standardized mu and N. Critical checks: boundary smoothing, effective degree change, mean-profile identifiability, whether model misspecification differs for small and large N. Do not aggregate raw MSE across dramatically different mu, N without stratification.

## 7. Reproducibility

From repository root:

    conda activate trend-estimation
    git switch paper/pooled-loocv-numerical-optimization
    git pull --ff-only
    python -m pytest tests/test_nonzero_difference_mean_reconstruction.py -q
    python -m experiments.pooled_loocv_smoothness.run_nonzero_difference_mean --preset smoke
    python -m experiments.pooled_loocv_smoothness.run_nonzero_difference_mean --preset pilot --dry-run
    python -m experiments.pooled_loocv_smoothness.run_nonzero_difference_mean --preset pilot

Results under `results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/{smoke,pilot}/`: executed `manifest.json`, `method_comparison.csv`, `summary.json`. Stage only `pilot/` result files after verifying them; the user has many unrelated untracked runs and partial WAL data in other results directories—**never use `git add .`**. Code, mathematical note, tests and prose are committed directly to branch `paper/pooled-loocv-numerical-optimization`, never PR/main.

## 8. What may be said in the paper now?

The formulas above are *derived mathematical identities and software verifications*, not empirical superiority results and not a claimed novelty over Guerrero's original nonzero-mean method. The experiment is **precommitted/design complete but not yet empirically run**. After the user pushes real results, update `RESULTS_LEDGER.md`, write a source-linked dated results audit, add the *measured* table and interpretation to the LaTeX manuscript. Keep the nonzero-\(\mu\) experiment clearly separate from completed \(\mu=0\) pilots and the distinct mean-difference **forecasting** paper.


### Figures produced on execution (not yet generated for the full pilot)

The runner generates `example_latent_trend_errors.png` (the first predeclared positive-μ example: actual simulated fitted-minus-true errors for oracle, zero-μ LOOCV, pooled plug-in, GLS μ-ML and joint fold-clean μ-LOOCV) and `mean_shift_true_trend_mse_R3.png` (log-scale **descriptive** means of true reconstruction MSE by standardized true μ). Both figures are generated only when executing the actual pilot; neither exists as paper empirical evidence just because its code is committed. The second figure averages over N and noise SD and must not be used for a strong inference without per-cell paired analysis.
