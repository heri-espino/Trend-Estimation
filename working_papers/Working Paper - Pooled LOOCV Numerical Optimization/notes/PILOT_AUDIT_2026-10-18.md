# Pilot audit — pooled LOOCV numerical optimization

**Date of underlying run:** 2026-10-18 (manifest UTC 23:41:50).  
**Analysis recorded:** 2026-10-18.  
**Source files:** [pilot manifest](../../../../results/pooled_loocv_smoothness/pilot/manifest.json) · [pilot per-method CSV](../../../../results/pooled_loocv_smoothness/pilot/solver_comparison.csv).  
**Reproducibility:** run from repo root:

    python -m experiments.pooled_loocv_smoothness.audit_pilot --csv results/pooled_loocv_smoothness/pilot/solver_comparison.csv --out results/pooled_loocv_smoothness/pilot/audit_summary.json

## 1. Completed, not prospective

The new independent observed-series pilot **was executed and committed**. Its manifest records 16 Cortés-Toto-inspired factorial scenarios (trend linear/nonlinear; seasonality no/yes; σ=0.5/2; N=50/200), five seeds per scenario, and R∈{1,3} observations per pooled criterion: **160 paired solver cases**, **480 method rows**.

Experimental setting: pure μ=0, V=I PLS with difference order d=2; λ coordinate searched in log(λ)∈[-20,35], with exact comparison of λ=0 and λ=∞. Finite dense grid: 401 log-spaced points; multibracket derivative scan: 101 points. Manifest environment: Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1. Hardware was **not** included in the manifest. The two values of R are nested (the first single series is common to the R=3 pool); do not count them as independent experiments for a pooling-effect significance test.

## 2. Descriptive solver results — measured, not a theorem

All comparisons use the **same observed pool** for bounded Brent, multibracket derivative Brent and the finite dense-grid benchmark. An objective gap >10^-7 is used below for a practically visible difference, although even this is not a certified tolerance on the true mathematical optimum.

| Metric | Pilot result |
|---|---:|
| Paired pools | 160 |
| Single-start bounded Brent yields higher F than multibracket | **5 / 160** |
| Multibracket yields higher F than single-start bounded Brent | **0 / 160** |
| Multibracket beats the finite dense grid by >10^-7 | **86 / 160** |
| Bounded Brent beats the finite dense grid by >10^-7 | **81 / 160** |
| At least 3 numerically *detected stationary roots* | **33 / 160** |
| Zero numerically detected stationary roots | **38 / 160** |
| Multibracket selects exact S=1 boundary | **67 / 160** |
| Multibracket selects exact S=0 boundary | **1 / 160** |

The largest bounded-Brent disadvantage was **0.21635 absolute pooled LOOCV MSE**, **2.59%** of the lower multibracket score in that case. Maximum dense-grid objective disadvantage against multibracket was approximately **3.79e-4**; no finite-grid comparison differed by more than 0.001. These are finite numerical differences, not statistical test outcomes.

Cases in which multibracket materially improves on single-start bounded Brent:

| Scenario | Replicate | R | Trend | N | σ | Season | Bounded F | Multibracket F | Bounded S | Multibracket S |
|---:|---:|---:|---|---:|---:|---|---:|---:|---:|---:|
| 6 | 1 | 1 | linear | 50 | 2 | yes | 8.580270 | 8.363920 | 1.000000 | 0.955923 |
| 14 | 1 | 3 | nonlinear | 50 | 2 | yes | 7.265296 | 7.174770 | 0.992362 | 0.913403 |
| 10 | 4 | 1 | nonlinear | 50 | 2 | no | 4.956733 | 4.876461 | 1.000000 | 0.906167 |
| 10 | 4 | 3 | nonlinear | 50 | 2 | no | 5.672286 | 5.639817 | 0.984211 | 0.900486 |
| 1 | 1 | 1 | linear | 200 | 0.5 | no | 0.229706 | 0.227567 | 1.000000 | 0.964015 |

These five seeds should be saved as predeclared numerical **counterexamples to single-start global reliability**, subject to independent higher-precision re-evaluation. They do not certify that multibracket has located the *actual global* minimum.

## 3. Does pooling simplify the surface?

The current evidence does **not** support a simple monotonic statement that increasing R eliminates stationary points:

| Outcome | R=1 (80 pools) | R=3 (80 pools) |
|---|---:|---:|
| At least three detected stationary roots | 16 | 17 |
| Cases bounded Brent loses against multibracket | 3 | 2 |
| Mean multibracket-selected S | ~0.9432 | ~0.9600 |

Because R=1 and R=3 share one realization, use *paired within-seed* comparisons of individual outcomes. Five seeds per scenario are too few to establish general effects of pooling. Importantly the source paper's ordinary single-series CV and this new cross-series pooling are separate designs.

## 4. Shape and numerical warnings

- **33 cases with ≥3 detected derivative roots do not prove 33 multimodal objective surfaces.** The sign-change root scan does not classify roots as local minima/maxima, and floating-point behavior near λ≈exp(35) may produce questionable stationary points. Re-evaluate root neighborhoods, curvature and objective differences in higher precision before making any multimodality claim.
- The large frequency of selected S=1 (67/160) may be scientifically sensible for a low-degree trend with independent noise, but it also makes endpoint comparison and asymptotic conditioning essential.
- Linear scenarios selected S=1 more frequently (60/80) than nonlinear scenarios (7/80). This is **descriptive under the pilot design**, not an external validity claim.
- Across all 160 cases, mean runtimes from the CSV were approximately 1.49 ms (bounded), 8.68 ms (multibracket) and 15.93 ms (dense grid), on unreported hardware. Methods have different derivative/score evaluation costs and no repeated hardware timings; do **not** claim a portable speedup from these values.
- For simple known smoothers, apparent multiple roots can be severe near extremely large λ; different derivative coordinates and asymptotic expansions may be necessary.
- The minimum over methods is not an independent held-out criterion. Numerical objective evaluation is the target here; this experiment alone cannot show improved recovery of true latent τ.
- The original source reproduction is only source-inspired until parameterization and generator discretization are confirmed against Cortés-Toto et al. (2017).

## 5. Next experiment priorities — before scaling

1. **Recheck these five cases** with a much denser adaptive/local reference on finite regions and high-precision calculation near λ→∞. Save objective/derivative curves and full root neighborhoods, not only the winning S. Retain the original seeds and exact generator settings.
2. **Count actual local minima, not merely roots.** Check derivative sign on both sides, curvature where safe, and a robust endpoint comparison. Classify numerical vs real roots.
3. Compare at **matched numerical budgets**: one-shot Brent, multi-start Brent, derivative-root multibracket, a refined grid and (small rational) exact Sturm. Count derivative cost separately.
4. Only once we establish robust numerical phenomena and novelty relative to earlier global-CV optimization should we run independent **confirmatory** seeds and analyze the proposed financial illustration.
5. Do not advertise this pilot as certified global-optimization evidence or proof of the algorithm's novelty.

**Provisional conclusion:** an adaptive multi-candidate search has yielded lower objective values than one-shot bounded Brent in a nonzero number of pilot cases, but the current gain is **5/160**, not universal, while the additional computational cost is nontrivial. This is a useful direction for numerical analysis, not yet a publication-ready finding.
