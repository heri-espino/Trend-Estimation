# Nonzero trend-difference mean — completed pooled LOOCV exploratory pilot

**Audited 19 October 2026. STATUS: EXECUTED, uploaded, independently read from all 1,600 CSV rows.** Study G, distinct from the earlier \(\mu=0\) Guerrero pilots and the separate horizon-\(h\) forecast-mean paper. **Exploratory only:** do not infer general statistical superiority or novelty from this small paired test.

## Source and provenance

- [Executed manifest](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/manifest.json), [complete method-level CSV](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/method_comparison.csv), and [original summary](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/summary.json).
- [Actual generated example reconstruction-error figure](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/example_latent_trend_errors.png) and [actual mean-MSE-by-mu figure](../../../results/pooled_loocv_smoothness/guerrero/nonzero_difference_mean/pilot/mean_shift_true_trend_mse_R3.png). Both figures are already in Git, not merely prospective.
- Original run source SHA **90521235df9dab729451fcceb2e5a001554e3e9a**, manifest written **2026-10-19T08:09:40.286063Z**, Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1. Base seed **69000000**; seed `base+N_index*10000+eta_index*1000+replicate`.
- Full factorial: \(d=2\) fixed by analyst, \(N=50,200\), \(\sigma_\eta=0.5,2\), \(\sigma_\varepsilon=0.3\), \(\mu/\sigma_\varepsilon=-1,-0.25,0,0.25,1\), five seeds. **20 scenarios, 200 complete pool evaluations (R1 and R3), 8 methods per pool = 1,600 CSV rows**; 100 R3 treatment pools. No missing method per pool and no nonfinite recorded realized trend MSE.
- **Actual independent random-shock unit: 20 R3 draws, not 100.** Each (N, noise SD, seed) generates one set of three stochastic trends and errors reused under all five deterministic μ-shifts. R1 reuses the first series of corresponding R3. Statistical inference must respect this reuse; there are only five independently seeded draws for each N × noise SD.

## 1. Principal results (primary R3 pools)

These are **actual realized latent-trend reconstruction MSEs**, not observed LOOCV scores or stock-return forecast errors. Smaller is better.

| True \(\mu/\sigma_\varepsilon\) | Incorrect zero-μ Gaussian contrast ML | Incorrect zero-μ pooled LOOCV | Estimated-μ Gaussian GLS ML | Fold-clean estimated-μ pooled LOOCV |
|---:|---:|---:|---:|---:|
| -1 | 0.461450 | 0.383661 | 0.359307 | **0.357713** |
| -0.25 | 0.363456 | **0.355467** | 0.359307 | 0.357713 |
| 0 | 0.357095 | **0.355780** | 0.359307 | 0.357713 |
| +0.25 | 0.368535 | 0.362628 | 0.359307 | **0.357713** |
| +1 | 0.462898 | 0.400765 | 0.359307 | **0.357713** |

For the 40 extreme treatments \(\mu/\sigma_\varepsilon=\pm1\) (but just 20 distinct stochastic shock draws), restricting μ to zero gives **0.462174** mean trend MSE for Gaussian ML against **0.359307** for estimated-μ GLS ML (28.6% higher relative to estimated-μ ML). Zero-μ LOOCV gives **0.392213** versus **0.357713** for estimated-μ fold-clean LOOCV (9.65% higher relative to fold-clean CV). The magnitude and pattern depend on N and noise SD; report these as descriptive paired sensitivity results, not significance tests.

At \(\mu=0\), the restriction is correct: 0.357095 zero-μ ML versus 0.359307 fitted-μ ML, and 0.355780 zero-μ CV versus 0.357713 fitted-μ CV. This is a real small finite-sample cost of estimating an unnecessary mean. The weak ±0.25 shifts show mixed outcomes, so allowing μ to vary is NOT guaranteed to improve recovery for each process and shift.

### Full eight-method benchmark at R3 (descriptive averages over all five μ perturbations)

| Comparison | Mean true trend MSE | Notes |
|---|---:|---|
| **Known μ, known variance ratio oracle** | **0.353328** | Infeasible benchmark; best mean here, not necessarily best for each realized simulation |
| **Known μ, estimated variances ML** | 0.357095 | Oracle true μ, feasible variance fit conditional on oracle |
| **Known μ, pooled LOOCV** | 0.355780 | Oracle true μ, observed-series CV for λ |
| **Zero μ, Gaussian variance ML** | 0.402687 | Feasible but wrong when μ≠0 |
| **Zero μ, pooled LOOCV** | 0.371660 | Feasible but wrong when μ≠0 |
| **Pooled Guerrero-style plug-in μ + OUR conditional Gaussian ML** | 0.363169 | Feasible hybrid **NOT equivalent to source Guerrero's per-series plug-in** |
| **Estimated common μ, Gaussian GLS profile ML** | 0.359307 | Feasible Gaussian differenced-data contrast |
| **Estimated common μ, exact fold-clean pooled LOOCV** | **0.357713** | Feasible pooled training-fold adjusted-mean PRESS |

The last two feasible fitted-μ methods have **very close** realized error: 0.359307 ML versus 0.357713 LOOCV, a difference of ~0.001595 (0.44%). This exploratory sample does **not** establish general LOOCV superiority over Gaussian ML. All methods use the **same Gaussian true DGP**; this experiment isolates mean specification, not non-Gaussian distributional robustness.

### Mean estimation itself

Mean absolute error in estimated μ, primary R3:
- **Pooled Guerrero-style difference plug-in:** 0.023000.
- **Gaussian differenced-data GLS-profile ML:** 0.016419.
- **Fold-clean CV common fitted μ evaluated on full pool after selecting λ:** 0.016438.

GLS reduces **absolute μ estimation error** by ~28.6% relative to the pooled sample-difference plug-in in these matched draws, but the result is not independent across five μ-shifts. At \(\mu=0\), fixing μ=0 trivially has zero estimation error but this cannot be treated as a fair estimator when μ is unknown.

## 2. Subgroups show why raw pooled average is insufficient

These figures aggregate over μ treatments for presentation and hence **reuse the same shocks at all five shifts**. Each (N, noise SD) group has only five independent random-shock draws.

| N | Observation SD | Zero-μ ML | Zero-μ LOOCV | Fitted-μ GLS ML | Fold-clean fitted-μ LOOCV |
|---:|---:|---:|---:|---:|---:|
| 50 | 0.5 | 0.079672 | 0.073400 | 0.071666 | **0.071092** |
| 50 | 2.0 | 0.719013 | 0.674358 | 0.641769 | **0.638453** |
| 200 | 0.5 | 0.088638 | 0.081870 | **0.080931** | 0.081386 |
| 200 | 2.0 | 0.723424 | 0.657012 | 0.642863 | **0.639919** |

For \(|\mu|/\sigma_\varepsilon=1\), misspecified zero-μ Gaussian ML selected smaller typical λ values, e.g. for (N50, noise SD 2) its median λ was about 5–7 while estimated-μ GLS ML's median was **64.25**. This illustrates confounding of deterministic difference drift with stochastic innovation/variance, but is not a general theoretical proof of direction of bias.

## 3. A structural insight: perfect shift invariance for correctly modeled μ

For matched innovations and noise, \(y_\mu=y_0+\mu p\), \(\tau_\mu=\tau_0+\mu p\), \(D_2p=\mathbf1\). Every studied fitted-μ or externally-known-μ method with affine shift equivariance has

\[
\widehat\mu(y_0+\mu p)=\widehat\mu(y_0)+\mu,\quad
\widehat\tau(y_0+\mu p)=\widehat\tau(y_0)+\mu p,
\]

so for the SAME shocks

\[
\|\widehat\tau(y_\mu)-\tau_\mu\|^2
=\|\widehat\tau(y_0)-\tau_0\|^2.
\]

This is **algebraic invariance by construction, not five statistically independent empirical successes**. A direct independent scan of saved R3 CSV showed maximum discrepancy of the equivariant estimators' MSE across the five μ treatments of approximately **9.5×10⁻⁹**, compatible with floating-point and search tolerances. Thus nearly constant MSE rows are **expected**, not an unexplained discovery. Zero-μ fits cannot absorb these shifts correctly, and are the intended sensitivity contrast.

## 4. Honest model comparison: observed CV versus post-selection truth

The reported source `reported_press_kind` identifies a crucial distinction:
- Zero-μ ordinary LOOCV and **oracle externally fixed μ** have their appropriate fixed-mean PRESS.
- **Joint estimated-μ LOOCV** uses a derived exact within-fold refitting PRESS formula; tests independently confirmed agreement with explicit leave-one-observation-deleted re-fitting of μ and trends.
- For **full-data-estimated GLS μ and pooled Guerrero-style plug-in μ**, the stored PRESS score freezes an estimate that already used all observations. It is explicitly `frozen_full_data_estimated_mu_PRESS_diagnostic_NOT_CV`. **Do NOT compare this diagnostic to genuine leave-one-out values or claim it is held-out validation.**

Only compare **latent reconstruction MSE** across these eight methods when evaluating their realized accuracy. No selected λ or μ was tuned against simulated latent τ. The true \(\sigma_\eta,\sigma_\varepsilon,\mu\) supplied to oracle benchmarks are privileged simulation information, not deployable procedures.

## 5. Source attribution, evidence status and next priorities

**Guerrero (2007) already models nonzero expected differences and provides a data plug-in mean.** Our pooled analogue plus conditional fitted covariance, GLS mean likelihood, and fold-clean pooled CV are implementation/comparison extensions, not attribution to his original estimator and not verified novel research. The other repository paper's horizon-\(h\) forecast mean profiling is a different target and does not become evidence for this study.

**Limits:** only 20 distinct primary R3 noise replicates; exactly Gaussian centered innovation and observation shocks, independent errors; fixed d=2; raw pooled loss not an external forecast evaluation; no independent confirmatory seeds. High deterministic \( \mu\binom j2 \) curvature for N200 is an intentional sensitivity case. The current MSE differences are promising exploratory findings rather than reliable confidence intervals or general method dominance.

**Next:** (i) present the core table and true source attribution in the paper; (ii) create paired contrasts by N and noise SD for the 20 independent shock units, with cluster-aware uncertainty or fresh larger campaign if warranted; (iii) only then combine mean misspecification and financial-style dependent/heavy-tailed noise. Do **not** rerun any frozen older campaign, overwrite current pilot, open a PR, or merge to main.
