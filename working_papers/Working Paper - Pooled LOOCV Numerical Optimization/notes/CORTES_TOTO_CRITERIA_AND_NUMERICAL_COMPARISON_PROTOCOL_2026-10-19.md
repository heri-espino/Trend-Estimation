# Study K: Cortés-Toto (2017) selector criteria vs Gaussian covariance MLE, with/without estimated μ

**Protocol and source audit 2026-10-19. IMPLEMENTED CORE CRITERION LIBRARY AND A ONE-SHOCK REPRODUCIBLE DEMONSTRATOR; LARGE PAIRED COMPARISON NOT RUN.** Study K extends the already committed *retrospective latent-trend* Study J without modifying its source results or misrepresenting a historical h-step forecast paper.

## 1. Primary literature actually read, rather than assumed

The locally supplied full text is:

Daniela **Cortés-Toto**, Víctor M. **Guerrero**, and Hortensia J. **Reyes** (2017), *Trend smoothness achieved by penalized least squares with the smoothing parameter chosen by optimality criteria*, **Communications in Statistics — Simulation and Computation**, 46(2), 1492–1507, DOI **10.1080/03610918.2015.1005236**; see its **§2, equations (9), (17), (18), (20)–(22), and §3**. A related source-grounded markdown extraction exists as `literature/.../Cortes-Toto_2017_trend-smoothness-optimality-criteria.md` in the project's bundled literature (check actual relative path before linking to it). Do not redistribute the licensed PDF or copy its full article text into Git.

The article considered four *final* penalty selectors on the classical penalized least squares (PLS) smoother with the *same* candidate order \(d=2\) and with \(\mu=0\): **ordinary leave-one-out Cross-Validation (CV), Generalized Cross-Validation (GCV), corrected Akaike criterion (AICc), and Bayesian Information Criterion (BIC)**. Their §2 also describes the **controlled-smoothness** approach from **Guerrero (2007)** and discusses **uncorrected AIC**, but the latter was **excluded from the authors' final simulation** because of unreliable numerical behavior. §3 compared **deterministic linear vs nonlinear trend**, seasonality, series variability and \(N=50\) vs \(200\), with their chief response being *attained smoothness*, not necessarily *realized stochastic latent-trend MSE*. Thus **our stochastic integrated-noise DGP is not a reproduction of their 2⁴ factorial simulation**, only a comparison of their four named criterion functions in our matched PLS framework.

**Crucially:** Their PLS §1 equation (2) explicitly includes a reference mean \(\mu\), and explicitly credits **Guerrero (2007)** for \(\mu\neq0\); the four-criterion experiment in the article itself is \(\mu=0\). Neither estimating \(\mu\) nor ordinary CV/GCV/AICc/BIC nor Theil/Guerrero's smoothness index is original to this project. **Our proposed generalization** is shared-mean profile estimation across multiple comparable series and its exact fold-clean CV and correct information-criterion EDF.

## 2. Three truly different methodological axes

**Criterion:** What are we *trying to minimize* when we choose penalty \(\lambda\)?
- Classical CV, GCV, AICc, BIC from Cortés-Toto (2017) §§2.2.1–2.2.2.
- Gaussian *contrast* maximum likelihood (ML)/quasi-ML, using differences \(z=D_d y\), with mean \(\mu\) either held at zero or jointly GLS-profiled with covariance scales. Gaussian contrast ML is a different objective from GCV/CV and not one of the four original paper experiment's selectors.
- Fixed controlled smoothness \(\lambda=\lambda(S_0)\) from the Guerrero index. **Predeclared \(S_0\)** is an exogenous smoothness *policy*, not an optimized data-dependent model selection criterion. It must be kept separate or given a training-only preselection design.

**Treatment of mean:** \(\mu=0\) (appropriate control only if justified); \(\mu=\mu_\mathrm{true}\) **infeasible oracle** (legitimate simulation comparator); \(\widehat\mu_{\mathrm{GLS}}\) estimated from all data (quasi-ML); \(\widehat\mu_{\mathrm{joint}}(\lambda)\) estimated jointly *within the PLS fitting criterion* and **re-estimated under each deletion for true ordinary CV**; and observed-mean Guerrero-style **pooled plug-in plus our covariance ML**. Do not compare a frozen all-data sample mean inside purported CV and call it deletion-honest. A plug-in mean can be a **separate feasible reconstruction benchmark** even though its *naive frozen-mean CV score* leaks information.

**Numerical solver:** Where does an algorithm search for its **given, fixed** criterion's minimizer? Bounded Brent in \(\log\lambda\) (possibly local), finite multibracket scan with local Brent refinement and exact relevant endpoints (not globally certified), dense log-lambda reference and later carefully restricted certified stationary-point isolation/Sturm (only when applicable). **Same objective** must be used across solver arms; comparing different criteria across different solver budgets confounds methodological and numerical effects.

## 3. Our exact formulas and extension with a pooled shared mean

For \(R\) equal-length observed series, each \(y_r\in\mathbb R^N\) with fixed analyst order \(1\le d<N\), denote \(D=D_d\), \(Q=D^\top D\), \(H_\lambda=(I+\lambda Q)^{-1}\), \(p_i=\binom{i}{d}\) and \(Dp=\mathbf1\). The fixed-exogenous-\(\mu\) trend is
\[
\widehat\tau_r=H_\lambda y_r+\mu(I-H_\lambda)p,\quad
\mathrm{EDF}_{\mu\mathrm{\ fixed}}=R\operatorname{tr}(H_\lambda).
\]
Use genuine \(RN\) observation loss and **one pooled \(\lambda\)**, not mean of \(R\) independently chosen lambdas.

For a fitted *common* mean through joint PLS,
\[
(\widehat\tau,\widehat\mu)
=\arg\min_{\tau_1,\ldots,\tau_R,\mu}
\sum_{r=1}^R \left[\|y_r-\tau_r\|^2+
\lambda\|D\tau_r-\mu\mathbf1\|^2\right].
\]
For \(\lambda>0\), set \(T_\lambda=Q(I+\lambda Q)^{-1}\), \(b_\lambda=T_\lambda p\), \(k_\lambda=p^\top T_\lambda p\), \(\bar y=R^{-1}\sum_r y_r\). Then
\[
\widehat\mu_\lambda=\frac{b_\lambda^\top\bar y}{k_\lambda},\qquad
\widehat\tau_r=H_\lambda y_r+\lambda b_\lambda\widehat\mu_\lambda .
\]
This linear smoother has within-series block \(H_\lambda+\lambda b_\lambda b_\lambda^\top/(Rk_\lambda)\) and cross-series block \(\lambda b_\lambda b_\lambda^\top/(Rk_\lambda)\) for different \(r\), giving **total EDF**
\[
\boxed{
\mathrm{EDF}_{\mathrm{joint}}(\lambda)
=R\,\operatorname{tr}(H_\lambda)
+\lambda\frac{\|b_\lambda\|_2^2}{k_\lambda}.
}
\]
Consequently EDF per series is \(\operatorname{tr}(H_\lambda)+\lambda\|b_\lambda\|^2/(R k_\lambda)\). The **endpoints** are \(RN\) at \(\lambda=0\) (continuous limit; μ unidentifiable exactly at \(\lambda=0\), but \(\tau=y\) well-defined) and \(Rd+1\) at \(\lambda\to\infty\), rather than \(Rd\) when μ fixed. Any generalized CV or information criterion that uses \(\operatorname{tr}H_\lambda\) alone when μ is estimated **under-penalizes model complexity**. The paper from 2017 did **not** derive this R-series joint-mean EDF; we do not attribute this identity to that paper.

With total EDF \(q_\lambda\) and pooled \(\mathrm{RSS}(\lambda)=\sum_{r,i}(y_{ri}-\widehat\tau_{ri})^2\), adapt the article's scores as follows (constant-in-\(\lambda\) scaling and offsets may be omitted without affecting the minimizer):
\[
\begin{aligned}
\mathrm{CV}(\lambda)&=\frac1{RN}\sum_{r,i}
\left(\frac{y_{ri}-\widehat\tau_{ri}}{1-A_{(r,i),(r,i)}(\lambda)}\right)^2,\\
\mathrm{GCV}(\lambda)&=\frac{\mathrm{RSS}(\lambda)/(RN)}
{\bigl(1-q_\lambda/(RN)\bigr)^2},\\
\mathrm{AICc}(\lambda)&=\log\!\left(\frac{\mathrm{RSS}(\lambda)}{RN}\right)
+\frac{2q_\lambda+1}{RN-q_\lambda-2},\qquad RN-q_\lambda>2,\\
\mathrm{BIC}(\lambda)&=\log\!\left(\frac{\mathrm{RSS}(\lambda)}{RN}\right)
+\frac{q_\lambda\log(RN)}{RN}.
\end{aligned}
\]
These use the exact published Cortés-Toto AICc/BIC *functional forms* with \(N\) replaced by total \(RN\), not a claim of their statistical derivation for the new jointly fitted mean across a pooled sample. The pooled-mean CV residual is exact and deletion-clean, already proven and tested in `JointMeanPooledLOOCV`.

**Important potential failure of naive BIC:** the PLS smoother interpolates \(y\) as \(\lambda\downarrow0\), so \(\mathrm{RSS}(\lambda)\to0\) and the simple plug-in log-residual **BIC tends to \(-\infty\)**. Thus unrestricted optimization over \([0,\infty)\) makes it unbounded and ill-defined as a smoothing selector! The article optimized over a numerical positive domain and did not provide a global guarantee. We therefore predeclare \(\log\lambda\in[-20,35]\) for BIC, report lower-domain boundary selection and explicitly **do not label this as a globally optimal BIC**. AICc is undefined where \(RN-q_\lambda\le2\) and must return \(+\infty\) rather than silently selecting a negative denominator near its pole. For CV/GCV, residual and denominator vanish as \(\lambda\to0\) but have stable finite *joint* continuous limits using the same spectral \(T_\lambda\) ratios.

**Guerrero smoothness:** article eq. (9) uses \(S_G(\lambda)=1-\operatorname{tr}H_\lambda/N\), with limiting maximum \(1-d/N\). Our established project uses a **normalized** \(S(\lambda)=[N-\operatorname{tr}H_\lambda]/(N-d)\in[0,1]\); therefore **\(S_G=(N-d)S/N\)**. These are different scales. The mean-estimated joint fit has a different EDF from fixed-\(\mu\) \(H_\lambda\); do not mislabel nominal normalized \(S(\lambda)\) as *joint* EDF or actual precision/smoothness.

## 4. Implemented source (verified mathematical vs exploratory status)

The new reusable module **`experiments/pooled_loocv_smoothness/cortes_optimality_criteria.py`** has:
- All four criterion scores (CV,GCV,AICc,BIC), exact finite \(\lambda\) spectral residuals, exact CV/GCV endpoints, explicit AICc invalid-domain behavior and BIC finite-domain constraint.
- Three clearly labeled mean modes: `zero` fixed, `fixed` with an *EXTERNALLY supplied* constant (the \(\mu_\text{true}\) oracle in simulation), and `joint`, re-estimating one shared \(\mu\) inside the penalized fit. GCV/AICc/BIC for joint μ use the **full RN×RN EDF**, not \(R\operatorname{tr}H\).
- `choose(...,solver="bounded"|"multibracket")` compares fixed criterion across numerical optimizers, returns actual score, \(\lambda\), normalized smoothness, estimated common μ, EDF, number of function evaluations and boundary flags. Neither algorithm certifies global optimality. Dense scans, derivative stationary roots and restricted exact-Sturm may be studied as **numerical** factors afterwards.
- `choose_fixed_smoothness(s)` inverts the *normalized* predeclared \(s\in[0,1]\), with separate paper-index conversion; example policies \(s=.5,.8\) only for illustrative control, **not optimized on test truth**.
- `tests/test_cortes_optimality_criteria.py` compares old exact CV and joint PRESS identities at all four orders and R1/R3, explicitly constructs the RN×RN joint hat matrix to check EDF, GCV, AICc and BIC, tests affine μ shift equivariance, and verifies endpoints and the BIC limitation.

The independent **single-case smoke** `python -m experiments.pooled_loocv_smoothness.run_cortes_criteria_case` exactly replays a specified Study J pilot seed (same deterministic noise law and same μ polynomial shift) and returns \(4\) criteria × \(\{0,\mathrm{joint},\mathrm{true\ fixed}\}\) (12 choices), \(2\) predeclared controlled smoothness policies × three mean modes (6) and the original **eight** comparator records, all scored on the *same simulated latent realized trend*. **This is 18 selector policies + eight original reference estimators for ONE seed, NOT a validated new Monte Carlo experiment.**

## 5. Proposed prospective controlled Monte Carlo and validation design

Do **not** immediately launch 10k seeds across every new axis. First validate one case and numerical behavior in the four orders, including the delicate \(d=4,N=200,\sigma_\eta=2\) with \(\mu\neq0\). Prespecify a small numerical solver benchmarking grid (same objective, \(\log\lambda\) bounds, max evaluations, endpoint rules, positive-domain BIC caveat) before claiming any method is globally better or faster.

**Pairing:** reuse Study J's exact already committed 25-seed \((\mathrm{regime},d,N,\sigma_\eta)\) pilot seed bank to evaluate **new criteria on the SAME generated y and latent τ**. Since the older eight methods are defined on the same shocks, the new criteria can be compared pairwise *without relabeling them as additional independent shocks*. This is **replay**, not a new confirmatory cohort. Keep \(d\), N, ηSD, \(R\) and μ separate in summaries. Source j law × d × N × η × seed remains the primary independent unit. The two fitted mean-treatment arms (zero, jointly estimated μ), plus three true-μ-oracle arms (reported separately), are sufficient for the first statistical comparison. A pooled **Guerrero-style plug-in** can be compared with existing MLE results, but applying naive fixed-μ CV to an all-data-observed plug-in **is not deletion-honest** and must not be mislabelled as such.

**Primary evaluation:** expected average **realized latent-trend reconstruction MSE**, plus MAE, selected \(\lambda\), original/normalized smoothness, boundary hit counts, EDF and solve time/criterion evaluations. Pair raw per-seed differences across methods in the *same* stratum. Different d imply different stochastic integrated trend classes and scales; no raw cross-d method ranking. Student-t3 infinite fourth moment -> usual variance-of-quadratic-loss SE may be infinite; report win frequencies, median and tail quantiles of per-seed paired loss, and avoid unjustified normal CIs. Cauchy remains outside MSE population comparisons.

**Preregistered credibility checks:**
1. Verify \(\widehat\mu_{\mathrm{joint}}\) and diagonal *full pooled hat* derivative by explicit linear algebra, not just selected MSE.
2. Compare numerical optimizers on **identical CV/GCV/AICc/BIC objective** with matched evaluation budgets and endpoints; distinguish local minima from criterion failure.
3. Investigate the open issue with **BIC's interpolating \(\lambda\to0\) divergence** before publishing a "BIC winner" comparison; same caution for AICc pole. AIC excluded source-aware.
4. Avoid comparing the "oracle known true μ" policies as implementable methods.
5. Verify that plug-in μ from entire y is not accidentally used inside purported fold-clean CV; nested μ joint CV is already implemented and tested.
6. Keep \(\mu\neq0\), and report what happens at \(\mu=0\) (correct restriction may improve finite-sample reconstruction).
7. Present the 2017 paper's **original simulation factors** (linear/nonlinear, seasonality, observation variability, N) as a possible separate *replication study* rather than claiming our integrated-stochastic-trend simulation reproduces it.

**No numerical results of any new criterion have yet been obtained at pilot or confirmatory scale.** Any subsequent full campaign requires a fixed protocol revision and explicit user-triggered local run, not automatically running on push. No PRs, no merge, no raw/credential/licensed-PDF uploads.

## 6. Single-shock commands (no large simulation)

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_cortes_optimality_criteria.py -q

# Exactly one old pilot seed, three series, nonzero mu, Gaussian control:
python -m experiments.pooled_loocv_smoothness.run_cortes_criteria_case --regime gaussian_iid --d 2 --n 50 --sigma-eta 0.5 --R 3 --replicate 0 --mu-factor 1 --solver multibracket

# Stress higher d and non-Gaussian observation tails:
python -m experiments.pooled_loocv_smoothness.run_cortes_criteria_case --regime student_t3_observation --d 4 --n 200 --sigma-eta 2 --R 3 --replicate 0 --mu-factor 1 --solver multibracket --scan-points 81
```

These commands re-generate only **one** synthetic shock at a time, use source-versioned J pilot seeds and print selected numerical diagnostics. No 25/10k-seed run occurs from them. The entire source article's empirical conclusion about seasonality and trend type is a separate question from whether a modern *joint-mu pooled LOOCV criterion* improves realized retrospective latent trend MSE.
