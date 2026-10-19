# Completed Gaussian mean-difference confirmation: 10,000 independent seeds per (d, N, noise SD)

**Status: completed and uploaded on 2026-10-19, then independently audited from the exact GitHub aggregates.** This is the completed Gaussian matched-order, retrospective *latent stochastic trend reconstruction* confirmation. It is **not** real financial data, not horizon-h forecasting and not the still-unrun non-Gaussian extension. The previously completed five-seed d=2 pilot remains a **separate** simulation cohort.

## 1. Source traceability and completeness

- [Exact submitted campaign manifest](../../../results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/audit_001/campaign_manifest.json) — `status=complete_10000_independent_draws_per_cell`, source executable commit **070b363b7d8a8156f320c833539fa068b684fc7b**, 16 fully covered cells, 1,600 unique compressed source shard references, each with SHA256 and disjoint seed intervals. The **user's local aggregator** confirmed the original gzip SHA256s when producing the compact GitHub upload; source shards themselves are not committed.
- [Saved mean-MSE/SD/SE by d,N,noise,R,mu,method](../../../results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/audit_001/by_d_N_eta_R_mu_method.csv) — 1,280 aggregate rows.
- [Saved within-seed paired method-MSE differences with SE and win counts](../../../results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/audit_001/paired_MSE_contrasts_by_d_N_eta_R_mu.csv) — 640 aggregate rows.
- [Independent compact-data audit](../../../experiments/pooled_loocv_smoothness/audit_multorder_confirmatory.py) — independently verifies expected 1,280+640 aggregate cells; complete seed ranges per stratum, method/paired arithmetic consistency, and derives approximate paired 95% Monte Carlo intervals. [Regression tests](../../../tests/test_multorder_confirmatory_aggregate.py) prohibit silently accepting incomplete/conflicting manifest counts.

**Design, not just number of rows:** 4 analyst-fixed difference orders \(d=1,2,3,4\), 2 lengths \(N=50,200\), 2 observation error SDs \(\sigma_\eta=0.5,2\), 10,000 independent **R3 shock pools** for each of those 16 strata = **160,000 independent base shock pools**. Each pool is transformed into five *paired* \(\mu/\sigma_\varepsilon=-1,-0.25,0,+0.25,+1\) settings and two *nested* sizes R1 and R3. The eight common methods yield 1,600,000 method-comparison treatment pools and **12.8 million method rows represented**. **Neither μ variants nor R1/R3 are additional independent replications.**

User-side source code and statistical target: \(D_d\tau^{(r)}=\mu\mathbf1+\varepsilon^{(r)}\), \(y^{(r)}=\tau^{(r)}+\eta^{(r)}\), independent Gaussian mean-zero eps/eta with \(\sigma_\varepsilon=0.3\). Initial \(\tau_t=0.02t\) for \(t<d\); true latent stochastic trajectory includes all integrated innovations. The *analyst* fixes d for each scenario; no d selection. Details, including exactly what LOOCV observes and what the true-trend MSE evaluates, are in [HOW_THE_SIMULATION_WORKS_AND_MEASURED_RESULTS.md](HOW_THE_SIMULATION_WORKS_AND_MEASURED_RESULTS.md) and the [pre-run locked four-order protocol](MULTIORDER_10000_SEED_CONFIRMATORY_PROTOCOL.md).

The pilot's actual run code SHA must not be confused with this campaign's source SHA. Results are tabulated only from the actual committed aggregates, not reconstructed from the old pilot, not invented from fitted parametric assumptions, and not estimated by running new Monte Carlo in CI.

## 2. Principal R3 result by order (descriptive mean of four distinct N × noise-SD cells)

Below \(\mu/\sigma_\varepsilon=+1\). Each row averages four *equal-sized, but different* 10,000-base-seed strata; hence it is a descriptive equal-cell average. Do **not** use these pooled numbers for across-d model-order ranking or to compute confidence intervals by pretending all treatments have the same DGP.

| Fixed \(d\) | Gaussian ML wrongly forces \(\mu=0\) | Gaussian GLS ML estimates \(\mu\) | Pooled LOOCV re-estimates \(\mu\) inside folds | Excess mean MSE from wrongly fixed μ, Gaussian ML | Mean MSE (GLS ML − fitted-μ LOOCV) |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.369897 | 0.217522 | **0.216354** | **0.152376** | +0.001168 |
| 2 | 0.440161 | **0.347805** | 0.352994 | **0.092356** | −0.005188 |
| 3 | 0.508880 | **0.439738** | 0.449096 | **0.069142** | −0.009358 |
| 4 | 0.561674 | **0.506292** | 0.520423 | **0.055382** | −0.014130 |

**Interpretation:** with R=3 and a substantial true mean shift, fitting μ materially improves mean true-trend reconstruction versus imposing μ=0. In all 16 separate d/N/noise strata, the excess mean reconstruction error of forced-zero Gaussian ML exceeds the absolute Gaussian-GLS-ML versus fitted-μ LOOCV mean MSE gap. In 15/16 strata, correctly fitting the mean by Gaussian GLS ML gives lower mean reconstruction MSE than fitted-mean LOOCV; one exception is \(d=1,N=50,\sigma_\eta=2\). This confirms the importance of *mean specification*, NOT general LOOCV superiority. Gaussian ML is well specified in this Gaussian DGP.

At true \(\mu=0\), imposing zero mean (correctly) gives slightly lower mean MSE than estimating an unnecessary μ in **every one of the 16 R3 strata**, both for Gaussian ML and for pooled observed LOOCV. Thus an unrestricted mean can have a measurable finite-sample cost. It is not automatically best to estimate μ when the zero-mean assumption is justified in advance.

The constant mean-trend reconstruction-MSE values across the five μ shifts for GLS ML and fold-clean pooled CV are **algebraically inevitable** under the experiment's common-random-number affine shift \(y_\mu=y_0+\mu\binom{t}{d}\). The 10,000 *base* replications quantify Monte Carlo error; the five μ treatments do not quintuple information.

## 3. Complete R3 within-cell mean-shift cost and paired-method differences

All entries are for \(\mu/\sigma_\varepsilon=+1\), R3. Define
\(\Delta_{\mu,\mathrm{ML}}=\mathrm{MSE}(\text{incorrect forced-zero ML})-\mathrm{MSE}(\text{estimated-mean GLS ML})\);
\(\Delta_{\mu,\mathrm{CV}}=\mathrm{MSE}(\text{incorrect forced-zero CV})-\mathrm{MSE}(\text{fold-clean estimated-mean CV})\);
\(\Delta_{\mathrm{ML-CV}}=\mathrm{MSE}(\text{estimated-mean GLS ML})-\mathrm{MSE}(\text{fold-clean estimated-mean CV})\).
**Positive** \(\Delta_\mu\) means that fitting the true nonzero mean helps. **Negative** \(\Delta_{\mathrm{ML-CV}}\) means Gaussian ML has lower mean true-trend MSE.

| d | N | \(\sigma_\eta\) | \(\Delta_{\mu,\mathrm{ML}}\) | \(\Delta_{\mu,\mathrm{CV}}\) | \(\Delta_{\mathrm{ML-CV}}\) | Paired SE of ML−CV |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 50 | 0.5 | +0.061361 | +0.007605 | −0.002727 | 0.000131 |
| 1 | 50 | 2 | +0.220275 | +0.126868 | **+0.010804** | 0.001479 |
| 1 | 200 | 0.5 | +0.061661 | +0.001987 | −0.000478 | 0.000016 |
| 1 | 200 | 2 | +0.266205 | +0.062407 | −0.002929 | 0.000206 |
| 2 | 50 | 0.5 | +0.017827 | +0.005009 | −0.002035 | 0.000074 |
| 2 | 50 | 2 | +0.161555 | +0.081156 | −0.013934 | 0.001454 |
| 2 | 200 | 0.5 | +0.017755 | +0.001205 | −0.000377 | 0.000010 |
| 2 | 200 | 2 | +0.172287 | +0.030262 | −0.004407 | 0.000131 |
| 3 | 50 | 0.5 | +0.010324 | +0.004892 | −0.002450 | 0.000070 |
| 3 | 50 | 2 | +0.129615 | +0.072511 | −0.029342 | 0.001005 |
| 3 | 200 | 0.5 | +0.010204 | +0.001481 | −0.000446 | 0.000011 |
| 3 | 200 | 2 | +0.126426 | +0.025709 | −0.005195 | 0.000141 |
| 4 | 50 | 0.5 | +0.007578 | +0.004885 | −0.003410 | 0.000080 |
| 4 | 50 | 2 | +0.104850 | +0.067158 | −0.044825 | 0.001194 |
| 4 | 200 | 0.5 | +0.007367 | +0.002120 | −0.000654 | 0.000014 |
| 4 | 200 | 2 | +0.101731 | +0.030705 | −0.007632 | 0.000183 |

In all 16 cells, both \(\Delta_{\mu,\mathrm{ML}}\) and \(\Delta_{\mu,\mathrm{CV}}\) have strictly positive approximate 95% Monte Carlo confidence intervals based on their **10,000 independent, within-shock-paired differences**. All 16 paired ML−CV approximate 95% intervals exclude zero (15 negative, 1 positive). For example:

- \(d=2,N=50,\sigma_\eta=2\): estimated-μ Gaussian ML MSE **0.659534** versus fold-clean CV **0.673468**, paired \(\Delta_{\mathrm{ML-CV}}=-0.013934\), approximate 95% CI **[-0.016784, -0.011085]**.
- **Exception:** \(d=1,N=50,\sigma_\eta=2\): GLS ML 0.405154 vs fold-clean CV 0.394350; \(\Delta_{\mathrm{ML-CV}}=+0.010804\), approximate 95% CI **[+0.007905,+0.013703]**.
- For that same exceptional cell, mean misspecified-μ ML cost is **+0.220275** with approx 95% CI **[+0.216979,+0.223571]**; thus even where CV outperforms fitted-μ GLS ML, mean misspecification matters much more.

**Statistical limits:** these are Monte Carlo standard-error intervals for the expected realized loss difference under the **specified Gaussian data generator**; they do not establish effects in markets, financial crises or other DGPs. Intervals are marginal and unadjusted for multiple comparisons; effect sizes and cell robustness matter more than isolated significance labels.


## 3a. Effect size matters: weaker nonzero means do **not** always dominate selector choice

The preceding all-16 result is **specifically for a substantial** \(|\mu|/\sigma_\varepsilon=1\). The saved paired contrast CSV also permits a less dramatic sensitivity test. Across the **16 independent R3 (d,N,noise) groups**, the following counts refer to group **mean** latent reconstruction MSE, *not* 10,000 individual trials per group:

| Standardized true mean \(\mu/\sigma_\varepsilon\) | R3 cells where wrongly forcing zero raises Gaussian ML mean MSE | R3 cells where this rise exceeds \(\lvert\mathrm{MSE}_{\mathrm{GLS\,ML}}-\mathrm{MSE}_{\mathrm{fitted\,CV}}\rvert\) | R3 cells where wrongly forcing zero raises pooled CV MSE |
|---:|---:|---:|---:|
| -1 | 16/16 | 16/16 | 16/16 |
| -0.25 | 15/16 | **5/16** | 16/16 |
| 0 | 0/16 | 0/16 | 0/16 |
| +0.25 | 15/16 | **5/16** | 16/16 |
| +1 | 16/16 | 16/16 | 16/16 |

Thus **do not claim mean specification is more important than smoothing method for every nonzero mean**. Under small relative mean shifts (±0.25), the incorrect-zero model often has only a small extra MSE cost, which exceeds the ML-vs-CV gap in just 5/16 R3 cells. At true μ=0 the constraint is actually correct and decreases expected estimated-mean variance cost. This pattern is a key effect-size qualification.

The same within-scenario observation holds much less reliably for **R1**: at ±0.25, wrongly fixing zero raises Gaussian ML mean MSE in just 8/16 cells and exceeds the estimated-mean ML-versus-CV difference in **0/16**. At μ=+1, incorrectly zero-mean ML has higher R1 MSE in 13/16, and a larger MSE penalty than ML/CV choice in 11/16. This reinforces that pooled estimation and adequate mean-shift size are **essential conditions** of the strongest headline.

## 3b. All eight estimators retained

The full commit includes the three *mean/parameter oracles* plus five feasible/possibly misspecified methods, not just the four highlighted for the paper. Equal-weighted average R3 realized MSE across four (N,noise SD) groups under \(\mu/\sigma_\varepsilon=+1\):

| Estimator (true μ / true variance unavailable except oracle rows) | d1 | d2 | d3 | d4 |
|---|---:|---:|---:|---:|
| True μ and true variance ratio (oracle) | 0.199272 | 0.341395 | 0.436852 | 0.504091 |
| True μ and estimated Gaussian variances (mean oracle) | 0.212142 | 0.345552 | 0.439253 | 0.505950 |
| True μ and pooled observed CV (mean oracle) | 0.215028 | 0.352637 | 0.448844 | 0.519989 |
| Incorrect forced-zero Gaussian ML | 0.369897 | 0.440161 | 0.508880 | 0.561674 |
| Incorrect forced-zero pooled CV | 0.266070 | 0.382401 | 0.475245 | 0.546639 |
| Pooled observed-difference μ plug-in + **our** variance ML | 0.214198 | 0.346310 | 0.442250 | 0.513928 |
| Fitted common μ, Gaussian GLS profile ML | 0.217522 | 0.347805 | 0.439738 | 0.506292 |
| Fitted common μ, fold-clean pooled observed LOOCV | 0.216354 | 0.352994 | 0.449096 | 0.520423 |

The pooled Guerrero-style plug-in hybrid is a meaningful feasible baseline and **sometimes beats Gaussian GLS mean profile ML** (for example the descriptive d1/d2 averages above), while GLS is better for d3/d4 averages. Therefore, don't say GLS uniformly beats this plug-in; compare methods within cells and report the proper target. Oracles are **not** feasible data-only selection algorithms.


## 4. The result differs for single-series R1

The **same completed source data** includes R1 nested in R3. Do not infer R1 results from R3 averages: pooling itself influences variance-component estimation and mean estimation. For R1 and \(\mu/\sigma_\varepsilon=+1\):

| d | Equal-cell mean MSE (GLS ML − estimated-μ CV) | Equal-cell mean MSE (wrongly forced-zero Gaussian ML − fitted-μ GLS ML) |
|---:|---:|---:|
| 1 | −0.026838 | +0.140545 |
| 2 | +0.030081 | +0.012016 |
| 3 | +0.018113 | −0.001827 |
| 4 | −0.012574 | +0.007429 |

In **only 13/16** individual R1 strata does imposing the wrong zero mean increase Gaussian ML true MSE; in three small-\(N=50\), high-noise cells this incorrectly restrictive model has *lower finite-sample mean reconstruction error* than fitted-μ GLS ML. This is a meaningful **bias–variance/estimation-instability counterexample**, not a reason to ignore correctness of the assumed DGP. For R1 **Gaussian GLS ML has lower mean MSE than fitted-μ CV in 13/16 cells**, but the equal-cell averages reverse at d=2 and d=3 because a few high-noise cells exert large influence. This demonstrates why averages over heterogeneous noise conditions and sample lengths do not prove method dominance.

For R1, wrongly forced-zero **CV** has larger mean MSE than fitted-mean CV in all 16 strata at the positive large mean shift; the gain is nevertheless often much smaller for long N/low noise. Analyze R1 and R3 as distinct experimental designs rather than 20,000 independent observations per seed.

## 5. Three different reasons a method may look favorable

1. **Mean misspecification**: fixing \(\mu=0\) can confound smooth deterministic curvature with random difference innovations; Gaussian contrast likelihood may then select a different variance ratio and penalty.
2. **Mean estimation variance and smoothing degrees of freedom**: estimating one shared μ consumes a parameter, and its uncertainty differs for R1 versus R3. At \(\mu=0\), the restricted estimator is usually slightly better in this correctly specified simulation.
3. **Smoothing selection target**: Gaussian differenced-covariance likelihood estimates variance components and a mean under a model; observed-data pooled LOOCV minimizes held-out **noisy-observation** error. Neither method directly minimizes latent trend MSE. Their ranking varies with R, N and observation noise.

These are **not** evidence that Gaussian MLE only works for Gaussian noise; this confirmation is **entirely Gaussian**. Earlier non-Gaussian exploratory pilots remain separate and the planned Gaussian-with-nonzero-μ × heavy-tail/volatility experiment has **not yet been run**.

Guerrero already permits nonzero expected d-th differences; the pooled observed-difference plugin used in these comparisons is combined with **our** conditional Gaussian differenced-covariance likelihood and is not the exact published estimator. Nor does this Gaussian study prove novel global numerical optimization.

## 6. What to put in the paper and what remains

**Paper-worthy, source-supported result:** in the deliberately matched Gaussian trend-difference reconstruction model and at R3, wrongly imposing a zero mean under true nonzero μ costs more true-trend MSE than choosing between fitted-μ Gaussian likelihood and fitted-μ pooled observation CV, in each of 16 tested (d,N,noise) cells. When mean truly zero, imposing its correct value modestly improves finite-sample reconstruction. Correctly fitting μ by Gaussian likelihood gives lower mean latent reconstruction MSE in 15/16 R3 cells, but not all R1 cells and not under all possible DGPs.

**Additional mandatory verification before claiming broad applicability:** confirm important results under independent noise-law families and temporal dependence, with balanced reconstruction signal scales; note that higher d leads to very different stochastic trend amplitudes. Separate market-data calibration from true trend availability. Report paired within-seed Monte Carlo uncertainty, don't treat μ shifts as replications, and avoid using real price trends as if known.

### Reproduce only the compact GitHub evidence, no Monte Carlo

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pytest tests/test_multorder_confirmatory_aggregate.py -q
python -m experiments.pooled_loocv_smoothness.audit_multorder_confirmatory
# Optional extra CSVs for the exact 95%-interval tables, without simulating:
python -m experiments.pooled_loocv_smoothness.audit_multorder_confirmatory --out-dir results/pooled_loocv_smoothness/guerrero/nonzero_mean_multorder/audit_CI_001
```

The raw gzip shards remain on the user's original machine. Preserve an independent backup; the compact data include original per-shard source references and hashes, but cannot fully reconstruct individual draw distributions if the raw files are lost.
