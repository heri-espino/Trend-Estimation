# Executed 13-distribution × 3-difference-order tail-noise pilot: evidence audit

**Status: actually executed and committed on branch `paper/pooled-loocv-numerical-optimization`.** This is a **five-seeds-per-cell exploratory pilot**, not a separately powered confirmatory study, numerical global optimization proof, or financial-return backtest. Analysis on October 18, 2026 (Mexico City time); original manifest creation **2026-10-19T05:55:02Z**.

## Exact sources and recorded generator

- [Run manifest and 156-cell scenario grid](../../../results/pooled_loocv_smoothness/guerrero/tail_stress/pilot/manifest.json).
- [Individual 4,680 method results](../../../results/pooled_loocv_smoothness/guerrero/tail_stress/pilot/method_comparison.csv).
- [Original run summary](../../../results/pooled_loocv_smoothness/guerrero/tail_stress/pilot/summary.json).
- Source implementation [`run_tail_noise.py`](../../../experiments/pooled_loocv_smoothness/run_tail_noise.py), and [pre-run design](TAIL_NOISE_PROTOCOL.md). Exact manifest source SHA: `c215089c4adb737e5e8ed67ce91237d8961adad9`. Manifest Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1, `numpy.random.default_rng`, base seed **47800000** and `seed=base+10000*scenario_id+replicate`. Not a fresh random holdout in each method: all methods within a pool use the **same y and same latent truth**.

Verified by independently reading the entire saved 1,264,578-character CSV via GitHub Git blob: **4,680 rows, 1,560 paired (scenario,seed,R) pools, three complete method rows per pool, 156 distinct scenarios**, three difference orders, 13 distributions, both R1 and R3. Each combination (noise regime, d, N=50/200, noise scale 0.5/2) has five seeds. **780 independent primary R3 pools** (60 per noise regime, 20 for each d), plus 780 **nested** R1 evaluations reusing the first series. The source CSV has no nonfinite recorded realized trend MSE or observed LOOCV MSE values. A reproducible standalone saved-data audit and regression tests are in `audit_tail_noise.py` and `test_guerrero_tail_pilot_audit.py`.

The stochastic generator for each matched order is

\[
D_d\tau=\varepsilon,\qquad y=\tau+\eta,\qquad
\widehat\tau_{\lambda,d}=(I+\lambda D_d^\top D_d)^{-1}y.
\]

Here **both the underlying data generator and the fitted penalty order vary together**: d=1 implies constant limiting trends, d=2 linear, d=3 quadratic. We did NOT test one fixed latent DGP against incorrectly chosen fitted orders; nor did we select d jointly with lambda. \(\tau\) is revealed **only during the final latent reconstruction MSE calculation**, not in fitted Gaussian likelihood nor observed pooled LOOCV.

## 1. Principal paired results by d, R=3, **excluding Cauchy**

Cauchy observation errors have no finite variance or population expected squared-error risk and are analyzed separately. For the remaining 12 distribution settings, each difference order has **240 primary R3 pools**.

| True and fitted d | Mean realized latent-trend MSE: Gaussian differences ML | Mean latent-trend MSE: LOOCV bounded Brent | Relative decrease in means with ML | ML smaller realized MSE in |
|---:|---:|---:|---:|---:|
| **1** | **0.207687** | 0.208839 | 0.55% | 122/240 |
| **2** | **0.338310** | 0.348313 | 2.87% | 149/240 |
| **3** | **0.421723** | 0.430813 | 2.11% | 156/240 |
| **All d — DESCRIPTIVE only** | **0.322573** | 0.329322 | 2.05% | 427/720 |

Interpretation: the feasible Gaussian **differenced-data likelihood** estimate of the smoothing ratio gave slightly smaller mean **latent reconstruction error** for all three d in this particular set of realizations. The advantage **is modest**, especially d=1; the win counts vary and no universal ordering, interval, or significance claim follows from five independent seeds per cell.

**Do not interpret 0.2077 vs 0.4217 as proof that d=1 is a better smoothing order.** Different d values generate different stochastic latent-trend processes with very different accumulated low-frequency amplitudes; the reconstruction errors and their difficulty are not directly comparable. A genuine selection-of-d experiment would hold the **true** trend fixed and compare candidate fitted d while selecting lambda fairly.

The R3 Gaussian likelihood estimated \(\widehat\lambda=\infty\) in **11/720** finite-observation-variance pools, all at d=1; ordinary bounded LOOCV selected \(\lambda=\infty\) in **4/720**, all at d=1. These are actual boundary fits; keep them.

### Sample size and noise level (same d; 12 finite-variance distributions)

| d | N=50: ML vs LOOCV mean trend MSE | N=200: ML vs LOOCV mean trend MSE |
|---:|---:|---:|
| 1 | 0.225499 / 0.226507 | 0.189875 / 0.191170 |
| 2 | 0.360399 / 0.379285 | 0.316220 / 0.317342 |
| 3 | 0.424857 / 0.439944 | 0.418590 / 0.421683 |

At higher observation noise SD 2 (versus .5), absolute reconstruction MSE increases in every d as expected. Inferences should be made from within-cell matched differences rather than raw aggregation across noise scales.

## 2. Centered skew-normal results

Five population-centered and variance-standardized shapes \(\alpha\in\{-6,-3,0,3,6\}\) were included. By construction the **population mean is exactly zero** and the population SD is the same nominal value at every shape. These are not heavy-tailed in the sense of Student-t(3); they identify *asymmetry effects*.

The table below **aggregates d only for descriptive visibility** (20 R3 pools per d, 60 per alpha); comparisons across d must use the saved `by_difference_order_R3` and the independent audit's `by_d_and_regime_R3`.

| Skew shape \(\alpha\) | Mean latent trend MSE ML | Mean trend MSE LOOCV | ML lower MSE pools |
|---:|---:|---:|---:|
| -6 | **0.339486** | 0.343221 | 36/60 |
| -3 | **0.336722** | 0.336932 | 31/60 |
| 0 | **0.334225** | 0.339534 | 40/60 |
| +3 | **0.351735** | 0.354664 | 33/60 |
| +6 | **0.318019** | 0.327993 | 36/60 |

This does **not** demonstrate a monotone relation between alpha/skewness and MLE superiority. Each shape is allocated a different scenario ID/seed stream; although distributions are standardized, observed differences across alpha still contain Monte Carlo variation, and five seeds per cell cannot identify a subtle trend reliably.

### Selected scientifically useful regime contrasts (each has 20 R3 pools)

- **d=2, right-centered Gamma:** Gaussian ML true MSE **0.316759**, LOOCV **0.347861** (8.94% lower mean for ML; 15/20 pools).
- **d=2, left-centered Gamma:** Gaussian ML **0.346818**, LOOCV **0.344218** (LOOCV lower by about 0.76% in mean; Gaussian ML wins 12/20 individual pools). Asymmetry may matter, but streams are not matched sign-flips, so do **not** attribute this difference causally to skew sign.
- **d=2, GARCH-t5 observation noise:** Gaussian ML **0.320151**, LOOCV **0.366335** (12.61% lower mean for ML; 14/20 wins).
- **d=3, GARCH-t5:** Gaussian ML **0.402285**, LOOCV **0.445787** (9.76% lower mean for ML; 17/20 wins).
- **d=1, GARCH-t5:** Gaussian ML **0.208575**, LOOCV **0.204630** (LOOCV slightly better in mean; ML wins 10/20).
- **d=1, Student-t3 trend innovations:** ML **0.186873**, LOOCV **0.186269** (LOOCV slightly lower mean; ML wins only 8/20). Therefore "ML always wins under non-Gaussian shocks" is contradicted.

These are *uncertainty-limited exploratory contrasts*, not statistically confirmed effects or real-stock results.

## 3. Cauchy observation noise — distinct risk semantics

**CRITICAL:** A Cauchy variable has a finite location parameter and median, but no population mean, variance, kurtosis or finite expected squared-error risk. Its `noise_scale` is \(\gamma\), **not** \(\sigma_\eta\). There is no population Guerrero variance ratio \(b/a\) under Cauchy observation noise. Gaussian difference-likelihood estimates two **numerical pseudo-variance components** from the realized observations, not true Cauchy variances.

For the **60 independent primary R3 Cauchy pools**, Gaussian ML had lower *realized* trend MSE in **18/60**. A more appropriate descriptive comparison is the distribution of finite-sample robust absolute reconstruction errors:

| d | Median per-pool median absolute reconstruction error, ML | Same, LOOCV | ML \(\lambda=\infty\) count | LOOCV \(\lambda=\infty\) count |
|---:|---:|---:|---:|---:|
| 1 | 1.35765 | **1.22894** | 16/20 | 6/20 |
| 2 | 3.12537 | **3.10298** | 9/20 | 2/20 |
| 3 | 1.97628 | **1.83570** | 2/20 | 0/20 |

Thus the **ordinary LOOCV selector had smaller median per-pool median absolute error in all three Cauchy order groups** in this experiment, while Gaussian ML often chose the \(\lambda=\infty\) boundary. Cauchy extreme events make ordinary arithmetic Monte Carlo MSE *means* unreliable for comparing expected performance. Do not report a "percentage MSE reduction" under Cauchy as a scientific risk estimate; finite realized error remains a valid diagnostic.

Cauchy is a **deliberately extreme** stress test, not a recommended model of stock returns.

## 4. Numerical stationary candidates, NOT necessarily local minima

Across all **780 primary R3 pools**, **bounded single-start Brent versus multibracket Brent yielded no objective disagreement greater than \(10^{-7}\)**. This is directly checked from the paired per-method CV scores; both remain finite grid/numerical methods without mathematical global certificates.

There were **seven R3 pools with multiple sign-change stationary candidates**, **11 pools with zero** detected stationary candidates, and the remainder mostly one candidate:

- 7 cases at scenario IDs/replicates `(21,3)`, `(56,4)`, `(61,0)`, `(81,0)`, `(94,2)`, `(109,1)`, `(121,4)`. These span Student-t3 observation, Gamma-left, Gaussian jump, GARCH-t5, Cauchy, and two skew-normal groups. One 2-candidate case at `(61,0)` selected the infinite-boundary optimum; other multi-candidate cases had 3 sign-change candidates.
- Zero-candidate pools are mostly Cauchy and d=1, with many selecting infinite smoothing. A zero-candidate count does **not** imply optimizer malfunction; the optimal endpoint must be evaluated.
- The finite derivative scan can miss roots and may include nongenuine numerical sign changes; no exact root isolation or strict local minimum count follows.

**Numerical conclusion:** this large new pilot does **not** support claiming multibracket search is practically superior to bounded Brent on these DGPs. Existing separate deterministic-trend source-inspired experiments did uncover a few bounded misses; they must be interpreted as a different DGP and not combined silently.

## 5. Reproducible post-run analysis (new, no re-simulation)

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_guerrero_tail_pilot_audit.py -q
python -m experiments.pooled_loocv_smoothness.audit_tail_noise
# Optional manual plotting, by difference order:
python -m experiments.pooled_loocv_smoothness.audit_tail_noise --figures
```

The audit reads the committed CSV and manifest; outputs go to `results/pooled_loocv_smoothness/guerrero/tail_stress/pilot/audit/`:

- `audit_summary.json` — stratified statistics, all cells, Cauchy caveats, root-candidate IDs.
- `R3_by_d_distribution.csv` — 39 d×regime rows, excluding population MSE means for Cauchy.
- `R3_by_scenario.csv` — 156 cells with original N and scale.
- `paired_pool_diagnostics.csv` — every matched pool, preserving differences.
- Optional `tail_noise_R3_d1_finite_variance.png`, `...d2...`, `...d3...`.

The user has **not** yet generated or pushed these optional audit outputs; the original per-method source results are already committed. The CI audit tests are lightweight and should not run any Monte Carlo.

## 6. Next genuine research question

The results point toward a **model-order distinction** rather than merely "Gaussian MLE is always better" (it is not). Because the simulator intentionally matches generating d with fitted d, we still do not know whether **choosing d from observed y**, as opposed to knowing the correct d, improves or harms latent trend reconstruction. This is the next fair comparison: hold *one generated latent truth* fixed, compare \(d_\mathrm{fit}=1,2,3\) on exactly the same realized y, and optimize \(\lambda\) appropriately for each fitted d by Gaussian likelihood and LOOCV. A separate unobserved model-order selection rule must not use latent tau. Restrict this next extension to a small subset of finite-variance distributions first, then add other regimes.

For Cauchy, Gaussian variance likelihood lacks a correct covariance interpretation: a truly robust likelihood or bounded-influence loss is more principled than pushing the Gaussian pseudo-variance estimate through more replications. Other potential direction: a dependence-aware comparison for correlated observation noise. Treat novelty and statistical performance as distinct from numerical-global-optimization claims.

**Workflow rule:** commit directly to the existing `paper/pooled-loocv-numerical-optimization` branch. No PRs, no merge to main; new confirmatory simulations are manual-only.
