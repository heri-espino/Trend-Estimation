# Guerrero known-variance-ratio pilot — observed CV versus true-trend error

**Source results committed by user:** [manifest](../../../results/pooled_loocv_smoothness/guerrero/pilot/manifest.json), [summary](../../../results/pooled_loocv_smoothness/guerrero/pilot/summary.json), [per-pool, per-method CSV](../../../results/pooled_loocv_smoothness/guerrero/pilot/guerrero_solver_comparison.csv).  
**Status:** [MEASURED PILOT], independently read back from GitHub. Not confirmatory or publication-ready. Analysis added 2026-10-18 local date.

## A. Scientific target

Different *selection mechanisms* for the same PLS trend estimator:

\[
H_\lambda=(I+\lambda D_2^\top D_2)^{-1},\qquad
\widehat\tau=H_\lambda y.
\]

Guerrero's model uses observations \(y=\tau+\eta\) and stochastic trend differences \(D_2\tau=\varepsilon\), where \(\operatorname{Var}\eta=\sigma_\eta^2 I\), \(\operatorname{Var}\varepsilon=\sigma_\varepsilon^2 I\), and \(\eta,\varepsilon\) are independent. The **model-informed oracle known-ratio parameter** is

\[
\lambda_G=\sigma_\eta^2/\sigma_\varepsilon^2.
\]

The pooled LOOCV selectors observe only y and minimize the **mean of R reconstruction LOOCV MSE functions** for a common λ. True latent \(\tau\) is used **only for evaluating estimated trends**:

\[
\operatorname{TrendMSE}(\lambda)
=\frac1{RN}\sum_{r=1}^{R}\|H_\lambda y^{(r)}-\tau^{(r)}\|^2.
\]

These are different objectives; a lower realized LOOCV score need not yield a lower trend MSE. The known ratio is not a feasible parameter estimate in ordinary market data unless variance components are actually identified and estimated.

## B. Provenance and design

Executed pilot manifest: 2026-10-19T01:57:10Z, Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1, git SHA 7fc208e18b74e45cfe1075eede9390a6f30f23b3. The original runner used \`d=2\`, \`N∈{50,200}\`, observation-noise SD \(\sigma_\eta\in\{0.5,2\}\), innovation SD \(\sigma_\varepsilon\in\{0.1,0.3,1\}\), **12 scenarios × five seeds × pool sizes R=1 and R=3 = 120 paired pools**, with four method rows each = 480 rows. R=1 is the **first** member of R=3 for a matching scenario/seed, so the 120 pools are not 120 statistically independent experimental draws for a pooling comparison.

Numerical methods: one bounded Brent in log lambda, multibracket derivative-sign Brent, and finite 401-point log-lambda grid; analytic endpoints λ=0 and λ→∞ are included. The multibracket scan has 101 points and does not certify complete stationary-root recovery. Guerrero selects the actual DGP-known variance ratio; it is not a competitor minimizing realized LOOCV.

## C. Measured whole-pilot means

| Selection | Mean observed pooled LOOCV MSE | Mean true latent TrendMSE | Mean normalized S |
|---|---:|---:|---:|
| Guerrero known DGP ratio | 2.667639 | **0.383761** | 0.756655 |
| One-shot bounded Brent | **2.642914** | 0.404506 | 0.758646 |
| Multibracket derivative Brent | **2.642914** | 0.404506 | 0.758646 |
| Finite dense grid | 2.643001 | 0.404297 | 0.758166 |

Means weight all predeclared *scenario–seed–pool-size* cases equally, not series or units across DGP settings; e.g. high-noise MSEs contribute larger absolute differences. Do not treat this pooled MSE mean as a universal cross-DGP error or derive sampling precision from 480 method rows.

**Descriptive pilot finding:** Guerrero has about **5.13% lower** average true trend MSE than multibracket (0.383761 versus 0.404506), despite achieving about 0.93% higher averaged realized LOOCV (2.667639 versus 2.642914). In the 120 paired evaluations Guerrero's true trend MSE is lower in **95/120**, and multibracket's realized LOOCV is lower in **120/120**. These are repeated/nested evaluation counts, **not 120 independent statistical successes**.

## D. Primary un-nested R=3 summary and R=1 sensitivity

Use **R=3** as a transparent primary display (60 pools: 12 independent DGP cells × five independently seeded three-series pools). Do not combine R=1 and R=3 as if independent.

| Pool R | Pools | Guerrero true MSE | Multibracket true MSE | Guerrero lower in | Guerrero LOOCV | Multibracket LOOCV |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 60 | 0.381850 | 0.414164 | 50/60 | 2.637698 | 2.604419 |
| **3** | **60** | **0.385673** | **0.394848** | **45/60** | **2.697581** | **2.681409** |

For R=3, the reduction in mean true MSE is approximately **2.32%** relative to multibracket's mean. Among the 12 R=3 scenario cells (each averaging only five replicates), Guerrero's mean true MSE is lower in **10/12**; the exceptions are N=50, observation SD 2, trend-difference SD 0.1 and 1.0. This makes the apparent effect heterogeneous and is **not** evidence of a universal gain.

For R=1 the mean true-MSE reduction is around 7.80%. Because R=1 is nested inside R=3, differences between these aggregated columns cannot by themselves be assigned an independent-samples confidence interval.

## E. Root-search geometry actually observed

The explicit saved field \`stationary_candidates_detected\` records numerically found derivative sign-change candidates, not proven minima.

- **R=3:** all 60 pools report **one** detected stationary candidate.
- **R=1:** 55 pools report 1 candidate, 3 report 2, 1 reports 3, and 1 reports 0.
- No pool has bounded Brent observed LOOCV worse than multibracket by >1e-7.
- Thus in this **correctly specified stochastic DGP**, there is **no measured numerical advantage** of multibracket over the single-start bounded solver at the reported tolerance, even though it is more complicated.
- This says nothing about global uniqueness: finite derivative scans can miss roots; narrow/tangent stationary roots require more stringent study.

Compare with the *different* prior Cortés-Toto-inspired deterministic-trend pilot, which contained five bounded-Brent misses among 160 pools. Do not pool those DGPs or treat evidence from one as confirmation for the other.

## F. Why this is scientifically valuable, and what it is not

1. **Important distinction:** Numerical minimization of an observed reconstruction CV criterion and statistically informed trend recovery do not coincide automatically.
2. **Model-informed advantage is expected**: Guerrero was given actual σ² values; this baseline has access to information unavailable to LOOCV and should not be promoted as a fair practical estimator comparison.
3. **Numerical thesis is conditional**: The more expensive multibracket optimizer did not improve the objective here. Therefore a paper claiming global practical numerical superiority needs *more difficult, genuinely multimodal* surfaces, accurate root verification and fair computation budgets.
4. **Finite initialization caveat**: Fixed intercept and slope in DGP are not a diffuse prior; avoid unconditional MMSE assertions without proof for this exact finite generator.
5. **Statistical uncertainty**: Five seeds per scenario is exploratory. Treat seed replicates within scenario as sampling units. A credible confirmatory plan should prespecify primary R=3 contrast, effect estimand, seed-stratified uncertainty and robustness cases, not just report a pooled win rate.
6. **Not financial forecasting**: These are independently generated synthetic observed series and retrospective trend fits; no market data or future outcomes enter.

## G. Recommendation and next precise experiments

Do **not** launch the 100-seed confirmatory campaign yet. First:

- Analyze the **one R=1 three-stationary-candidate** case and all cases with zero/two stationary candidates, verifying root neighborhoods, derivative signs, boundary conditioning and whether there are multiple distinct *minima*. Keep exact scenario and seed identifiers in the diagnostic.
- Add a per-scenario paired true-MSE comparison against Guerrero with uncertainty and stable random seeds; report both R sizes separately.
- Decide whether the paper's numerical claim concerns existing multimodal LOOCV *when it occurs*, rather than typical improvement under Guerrero's correctly specified model.
- Consider a new **feasible estimated variance-ratio** comparator only as a distinctly labeled extension; do not misrepresent known-ratio oracle as Guerrero's published practical smoothness-target procedure.
- Before journal claims: novelty audit versus existing global GCV optimization and new independent confirmatory seeds after method selection.

**Overall judgment:** the actual pilot supports an instructive statistical distinction but does **not** yet demonstrate a superior novel numerical optimizer.
