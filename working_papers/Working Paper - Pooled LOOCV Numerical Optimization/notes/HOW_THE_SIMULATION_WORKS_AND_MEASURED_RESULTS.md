# Exact simulation methodology and measured results

**Canonical explanatory note, updated 2026-10-19.** This documents the *executed* fixed-\(d=2\) pilot as it actually ran, not a hypothetical method or an observed-stock backtest. Full source: [original 1,600-row CSV](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/method_comparison.csv), [executed manifest](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/manifest.json), [saved summary](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/summary.json), [dated audit](NONZERO_DIFFERENCE_MEAN_PILOT_AUDIT_2026-10-19.md), [original runner](../../../experiments/pooled_loocv_smoothness/run_nonzero_difference_mean.py).

## 1. Precisely what is being reconstructed?

We generate an **unobserved, realized stochastic trend** \(\tau^{(r)}\) for each independent pool member \(r\), then contaminate that trend with observational noise \(y^{(r)}=\tau^{(r)}+\eta^{(r)}\). **The target is the realized latent trajectory**, not its population expected polynomial, the arithmetic mean of the observed series, a Gaussian moving average, or a financial stock trend. The fitted methods receive \(y\) and never receive the realized \(\tau\) when tuning their parameters. The stored truth enters only *after* estimation, in error metrics.

At the analyst-chosen, fixed difference order \(d\), the stochastic trend DGP is

\[
D_d\tau^{(r)}=\mu\mathbf1+\varepsilon^{(r)},\qquad
\varepsilon_t^{(r)}\overset{\mathrm{iid}}{\sim}N(0,\sigma_\varepsilon^2),\quad
\eta_t^{(r)}\overset{\mathrm{iid}}{\sim}N(0,\sigma_\eta^2),
\]

with all innovations independent across components and across \(r\). For the **completed pilot \(d=2\)**, initialize \(\tau_0=0,\ \tau_1=0.02\). Subsequently,

\[
\tau_t=2\tau_{t-1}-\tau_{t-2}+\mu+\varepsilon_{t-2},\quad t=2,\ldots,N-1.
\]

Equivalently, with \(p_t=\binom{t}{2}\),

\[
\tau_t=0.02t+\mu p_t
      +\sum_{j=0}^{t-2}(t-1-j)\varepsilon_j.
\]

Consequently **\(E[\tau_t]=0.02t+\mu\binom{t}{2}\)** while the *reconstructed truth* is the entire realized curve including the accumulated innovation term. At \(\mu=0\), expected second differences vanish but the actual realized second differences do not; the expected trend remains linear with nonzero slope. At \(\mu\ne0\), expected trend curvature is nonzero. This does not mean we simply fit a quadratic: the noisy *realized* integrated trend must be recovered.

The source generator computes a common centered baseline trend for each seed, then adds \(\mu p\) and independent Gaussian observational noise. It reuses **the same innovations and measurement noise** at the five \(\mu\) treatments for each \((N,\sigma_\eta,\mathrm{seed})\). This is an intentional **paired intervention**, not five independent stochastic replications.

## 2. What actually varies in the completed experiment?

| Experimental axis | Executed values |
|---|---|
| Difference order | **\(d=2\) only**, chosen in advance by the analyst |
| \(N\) | 50, 200 |
| Observation noise SD \(\sigma_\eta\) | 0.5, 2 |
| Trend innovation SD \(\sigma_\varepsilon\) | 0.3 |
| \(\mu/\sigma_\varepsilon\) | \(-1,-0.25,0,+0.25,+1\), corresponding to \(\mu=-0.3,-0.075,0,+0.075,+0.3\) |
| Pool size \(R\) | 1 and 3; the first series of R3 is identical to R1 |
| Independent random seeds | 5 for each of four \((N,\sigma_\eta)\) settings, **20 independent R3 underlying shock draws total** |
| Repeated paired treatments | 5 \(\mu\)-values per shock draw; 100 primary R3 treatment evaluations (not 100 independent shock draws) |
| Total method records | 20 design cells × 5 replicates × 2 nested pool sizes × **8 selectors = 1,600** |
| RNG | \`numpy.random.default_rng\`, base seed 69000000, \`seed=base+N_index*10000+eta_index*1000+replicate\` |
| Code identity | Executed manifest SHA \`90521235df9dab729451fcceb2e5a001554e3e9a\`, written 2026-10-19 08:09:40 UTC |

For \(d=2\), the deterministic \(\mu\binom{t}{2}\) term grows quadratically. At the final index \(t=N-1\), \(\mu=0.3\) contributes **352.8 for N50** and **5910.3 for N200**, far larger than observation SD 0.5/2. These are deliberately strong mean-misspecification cases, not representative magnitudes calibrated to financial prices.

For \(R=3\), three independent stochastic latent trajectories have one shared \(\mu\), noise SDs, \(N,d\), and selected \(\lambda\), and three independent noise realizations. The analyst pools **loss functions**, NOT optimized individual smoothness values:

\[
F_d(\lambda)=\frac1R\sum_{r=1}^R\mathrm{LOOCV}_r(\lambda),\qquad
\hat\lambda_{\mathrm{CV}}=\arg\min_{\lambda\ge0} F_d(\lambda).
\]

A normalized smoothness coordinate \(S_d(\hat\lambda)\) is reported *after* choosing \(\hat\lambda\); it is not the mean of separately selected \(S_r\). A joint mean \(\mu\) is fitted across the pool for the mean-estimation methods; it is not known to the feasible estimators. The user retains \(d\) as a **chosen modeling assumption** rather than optimizing \(d\) from latent truth.

## 3. All eight methods (same y, same realized latent truth)

Put \(Q=D_d^\top D_d\), \(H_\lambda=(I+\lambda Q)^{-1}\), and \(p_j=\binom jd\), so \(D_dp=\mathbf1\). For fixed \(\mu\),

\[
\hat\tau_{\lambda,\mu}
=\mu p+H_\lambda(y-\mu p),\qquad
\lambda_G=\sigma_\eta^2/\sigma_\varepsilon^2.
\]

All methods ultimately reconstruct the trend using this family of smoothers or the corresponding pooled *jointly* estimated-\(\mu\) smoother, but choose \(\mu,\lambda\) differently.

| Stored name | Mean \(\mu\) | Penalty \(\lambda\) | Feasible from y alone? |
|---|---|---|---|
| \`known_mu_true_ratio_oracle\` | True simulation \(\mu\) | True ratio \(\lambda_G\) | **No, oracle** |
| \`zero_mu_gaussian_difference_ml\` | Artificially forced 0 | Gaussian difference-covariance likelihood | Yes; potentially misspecified |
| \`zero_mu_pooled_loocv\` | Artificially forced 0 | Ordinary pooled observed-series LOOCV | Yes; potentially misspecified |
| \`known_mu_estimated_variance_ml\` | True simulation \(\mu\) | Gaussian difference-covariance ML conditional on true mean | **No, mean oracle** |
| \`known_mu_pooled_loocv\` | True simulation \(\mu\) | Pooled CV on \(y-\mu p\) | **No, mean oracle** |
| \`pooled_guerrero_plugin_mu_plus_gaussian_ml\` | Pooled observed \(D_dy\) sample mean | Our conditional Gaussian covariance ML | Yes; this **hybrid is not Guerrero's published estimator** |
| \`estimated_mu_gaussian_gls_ml\` | Common GLS-profiled \(\mu\) of differenced observations | Simultaneously profiled Gaussian contrast likelihood \((\mu,\sigma_\eta^2,\sigma_\varepsilon^2)\) | Yes |
| \`estimated_mu_fold_clean_pooled_loocv\` | One common \(\mu_\lambda\) jointly profiled inside PLS | Minimize exact **observation-deletion PRESS that refits \(\mu\)** | Yes |

Guerrero (2007) already permits \(\mu\ne0\) and reports an observed-difference mean plug-in. The present research novelty, if any, must be supported by **new validated comparison methodology and findings**, not by claiming to invent mean differences or the affine penalty identity. The other repository working paper on **horizon-\(h\) forecasting** has a different objective and should not be confused with this retrospective observed-series LOOCV reconstruction experiment.

The Gaussian difference likelihood uses \(z=D_dy\) and

\[
z_r\sim N(\mu\mathbf1,\Sigma),\qquad
\Sigma=\sigma_\varepsilon^2I+
\sigma_\eta^2D_dD_d^\top.
\]

At fixed \(\Sigma\), the pooled mean is the GLS estimate

\[
\hat\mu(\Sigma)=
\frac{\sum_r\mathbf1^\top\Sigma^{-1}z_r}
{R\mathbf1^\top\Sigma^{-1}\mathbf1}.
\]

**Important validation boundary:** a PRESS calculation for an *all-data-estimated* GLS or sample-difference plug-in mean while keeping that \(\mu\) fixed is only a **diagnostic**; it leaks the deleted observation. The \`estimated_mu_fold_clean_pooled_loocv\` procedure uses an exact analytic PRESS that *refits the common \(\mu\) and trends under every deletion*. Its correctness is tested against direct deleted-observation refits.

## 4. Metrics: what does "better" mean?

For each estimator and pooled observed realization, the code computes

\[
\mathrm{MSE}_{\mathrm{trend}}
=\frac1{RN}\sum_{r=1}^R\sum_{t=1}^N
   (\hat\tau_{r,t}-\tau_{r,t})^2.
\]

The numerical reconstruction target is the realized unobservable \(\tau\), available only because we simulated it. This is **not** a forecast of \(y_{N+h}\), a financial portfolio loss, nor the LOOCV criterion's own noisy-target score.

The **observed LOOCV criterion** holds out noisy \(y_{r,t}\), using an analytic PRESS identity rather than refitting each \(\lambda\) at every leave-out point. These objectives differ, so a method with a lower observed LOOCV score need not have smaller latent reconstruction MSE. **True \(\tau\) is never used to select \(\lambda\) or estimate \(\mu\)**; oracles are explicitly labelled as exceptions relying on known DGP parameters (not the realized \(\tau\) path).

We save selected \(\lambda\), nominal smoothness \(S_d\), true and estimated \(\mu\), errors in \(\mu\), fitted variance components where defined, reconstruction MSE/MAE, reported PRESS and an explicit field distinguishing genuine fold-clean PRESS from the frozen-all-data-mean diagnostic. **Estimating \(\mu\) changes effective degrees of freedom**; the old \(S_d(\lambda)\) is a common *penalty coordinate*, not the EDF of the whole estimated-\(\mu\) procedure.

## 5. Complete *measured* findings from the committed pilot

All numbers below are calculated from the **executed source CSV**, R=3, averaged across the four \((N,\sigma_\eta)\) settings (five original random shock seeds each). **Five \(\mu\) settings share the same shocks**, so the five table rows are NOT five independent replications.

| True \(\mu/\sigma_\varepsilon\) | Wrong \(\mu=0\), Gaussian ML | Wrong \(\mu=0\), pooled LOOCV | Fitted common \(\mu\), Gaussian GLS-ML | Fitted common \(\mu\), fold-clean pooled LOOCV |
|---:|---:|---:|---:|---:|
| -1 | 0.461450 | 0.383661 | 0.359307 | **0.357713** |
| -.25 | 0.363456 | **0.355467** | 0.359307 | 0.357713 |
| 0 | 0.357095 | **0.355780** | 0.359307 | 0.357713 |
| +.25 | 0.368535 | 0.362628 | 0.359307 | **0.357713** |
| +1 | 0.462898 | 0.400765 | 0.359307 | **0.357713** |

For the two *extreme* treatments \(|\mu|/\sigma_\varepsilon=1\), imposing \(\mu=0\) gave mean trend MSE 0.462174 for Gaussian ML versus 0.359307 for fitted-mean Gaussian GLS-ML, and 0.392213 for zero-mean pooled LOOCV versus 0.357713 for fitted-mean pooled CV. **These are paired descriptive effects, not standard errors or independent replication results.** At the correctly specified zero mean, fitting an unnecessary extra parameter had a small observed cost.

Across all five paired \(\mu\) treatments, descriptive R3 mean trend MSEs for **all eight methods**:

| Estimator | Mean true-trend MSE |
|---|---:|
| True \(\mu\), true ratio **oracle** | **0.353328** |
| True \(\mu\), estimated Gaussian variances **mean oracle** | 0.357095 |
| True \(\mu\), pooled observed LOOCV **mean oracle** | 0.355780 |
| Forced \(\mu=0\), Gaussian covariance ML | 0.402687 |
| Forced \(\mu=0\), pooled LOOCV | 0.371660 |
| Pooled Guerrero-inspired observed-difference plug-in + **our** Gaussian ML | 0.363169 |
| Fitted \(\mu\), Gaussian GLS-ML | 0.359307 |
| Fitted \(\mu\), exact fold-clean pooled LOOCV | **0.357713** |

Observed mean absolute error when *estimating the common \(\mu\)*: pooled observed-difference plug-in 0.023000; Gaussian GLS 0.016419; pooled fold-clean CV estimate 0.016438. This does not prove universal ranking in finite samples.

### Why do estimated-\(\mu\) errors not change with \(\mu\)?

For a fixed random realization and a deterministic polynomial shift \(\mu p\),

\[
y_\mu=y_0+\mu p,\quad \tau_\mu=\tau_0+\mu p.
\]

The externally-known-mean and the fitted-mean approaches are **equivariant**:
\[
\hat\tau(y_0+\mu p)=\hat\tau(y_0)+\mu p,
\]
so their errors \(\hat\tau-\tau\) remain the same for **identical underlying random shocks**. The observed numerical near-invariance across the five \(\mu\) treatments (maximum MSE differences around \(10^{-8}\)) is therefore **a mathematical consequence of this experimental design**, not five independent confirmations. The forced-\(\mu=0\) methods lack this equivariance and can incur systematic curvature bias.

### Disaggregated R3 means, all five mu treatments (descriptive)

| N | Observation SD | Forced-zero ML | Forced-zero CV | Fitted GLS-ML | Fitted fold-clean CV |
|---:|---:|---:|---:|---:|---:|
| 50 | .5 | .079672 | .073400 | .071666 | **.071092** |
| 50 | 2 | .719013 | .674358 | .641769 | **.638453** |
| 200 | .5 | .088638 | .081870 | **.080931** | .081386 |
| 200 | 2 | .723424 | .657012 | .642863 | **.639919** |

These aggregate across \(\mu\) but preserve N and noise level. They each contain only five independent underlying Gaussian shock draws. Inference should therefore operate on **paired differences within seed** and report distinct \((N,\sigma_\eta)\) uncertainty.

## 6. Existing generated figures

- [Example fitted-minus-true trajectory errors](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/example_latent_trend_errors.png).
- [Exploratory R3 mean trend MSE versus true \(\mu/\sigma_\varepsilon\)](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/mean_shift_true_trend_mse_R3.png).

The figures are already committed as pilot evidence; do not recreate or overwrite them without documenting a new source hash. The second plot aggregates across N and noise scales; create separate panels/figures in analysis if doing statistical inference.

## 7. Next independent campaign: orders \(d=1,2,3,4\)

This is an **extension proposal**, not retrospective reinterpretation of the completed \(d=2\) pilot. The user requests **10,000 independent random shock seeds per \((d,N,\sigma_\eta)\) cell**, with all five \(\mu\) treatments **paired** on the exact same shock draw. This means \(4d\times2N\times2\sigma_\eta=16\) base cells × 10,000 independent seeds = **160,000 independent R3 shock pools**. Each shock pool generates five \(\mu\)-shifted treatments, each evaluated for nested R=1 and R=3 and the eight original parameter selectors: **1,600,000 pooled evaluations and 12,800,000 method rows** if we retain the complete original design. Do not interpret those 12.8 million rows as independent samples. This campaign requires **chunking, resumable sharding, fixed seeds, a numerical preflight and performance profiling**, and must remain manual; existing d2 source results must not be overwritten.

For general \(d\),

\[
\tau_t=0.02t+\mu\binom td+\underbrace{
\sum_{j=0}^{t-d}\binom{t-j-1}{d-1}\varepsilon_j}_{\text{integrated d-order noise}},
\quad t\ge d,
\]

with \(\tau_t=0.02t\) for \(t<d\). This exactly enforces \(D_d\tau=\mu+\varepsilon\). The expected polynomial order is \(d\): constant drift when d1, deterministic curvature when d2, cubic for d3, quartic for d4. **Larger d and longer N can produce enormous polynomial magnitudes** even at fixed \(\mu/\sigma_\varepsilon\); normalize/report per d and N and verify numerical rank and shift invariance before drawing inferences. Fix d within each run, do NOT select d using the known latent truth.

**Independent confirmatory seeds and non-Gaussian extension should remain separate stages.** A future Gaussian-restricted 10k-seed campaign tests mean-specification effects; the later non-Gaussian study must predeclare its extra noise laws, variance existence, dependence and proper target-specific risk summaries. In particular, Cauchy has no population noise variance or finite expected squared reconstruction risk, so Gaussian true-ratio oracle comparisons are undefined there.

**Reproduction and interpretation priority:** preserve original pilot; independently validate the generalized \(D_d p=1\), nested R1/R3, paired-\(\mu\) simulation, exact fold-clean PRESS for \(d=1,2,3,4\), and finite MSE. Pilot/large confirmation status must always be explicit in [RESULTS_LEDGER.md](RESULTS_LEDGER.md).
