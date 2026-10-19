# Simulation atlas — observed-series LOOCV only

**Status (2026-10-18):** the original factorial pilot **has been executed and committed**, along with two independent Guerrero-model pilots. The new misspecified-noise robustness study is **implemented but its full pilot has not yet been executed**. Run-by-run status and code/seed provenance: [RESULTS_LEDGER.md](RESULTS_LEDGER.md); new regime definitions: [ROBUSTNESS_PROTOCOL.md](ROBUSTNESS_PROTOCOL.md).

## Source-inspired 2^4 factorial: Cortés-Toto, Guerrero & Reyes (2017)

Their Section 3.1 and Table 1 define:

| Factor | Low | High |
|---|---|---|
| Trend | Linear \(\tau_t=4t/N\) | Nonlinear \(0.6\,\beta_{30,17}(u_t)+0.4\,\beta_{3,11}(u_t)\) |
| Seasonality | Absent | Quarterly pattern \(+1,-0.5,-2.5,+2\) repeating |
| Gaussian noise SD | 0.5 | 2 |
| Sample length N | 50 | 200 |

The nonlinear curve uses the Beta density \(\beta_{a,b}(u)=u^{a-1}(1-u)^{b-1}/B(a,b)\) on u∈[0,1]. Use \(u_t=(t-1)/(N-1)\), t=1,...,N, as a documented implementation grid. Note minor discretization conventions may differ from the original published R script; do **not** call it a perfect computational replication without checking the authors' implementation.

Define \(y_t^{(r)}=\tau_t+\xi_t+\epsilon_t^{(r)}\), independent \(\epsilon_t^{(r)}\sim N(0,\sigma^2)\), with the **same underlying τ and seasonality across r within a pool**. The original design compared CV, GCV, AICc and BIC on a *single series*. Our R>1 experiment is a novel **protocol choice**, not something attributed to the 2017 paper.

## Phased presets

- **Smoke:** short N for implementation checks, small seed count, R∈{1,3}. Not publishable and **not** one of the original 16 factorial cells.
- **Pilot:** all 16 factorial cells, R∈{1,3}, 5 independent pools per cell, N=50/200 as specified. Distinct random seeds across cells/pools.
- **Confirmatory (manual after review):** same 16 cells, R∈{1,3}, 100 independent pools/cell; seeds disjoint from pilot. Record multiplicity/selection issues before running.
- **Exact tiny-case:** rational observations, N≤6, R≤2, d=1 or 2; compare Sturm positive-root count and bounded-refinement results.
- **Financial illustration:** 1–3 fully specified historical time series, data snapshot/date/corporate actions/preprocessing, showing retrospective smoothing and score landscape ONLY. Do not blend incomparable price levels in a raw pooled MSE; standardization and economic interpretation are required.

No costly full campaign should run automatically. Only launch it deliberately and save outputs with run manifests. The long campaign should not be inferred from smoke completion.

## Methods, on identical generated data

1. Dense log-λ reference (finite grid, *not* certified global optimum).
2. One-shot bounded Brent-style minimization in log λ (local, possible bad basin).
3. Multiple derivative-sign brackets followed by Brent root refinement; evaluate all found stationary points and both analytic endpoints. This search is **not certified complete**.
4. Sturm sequence and exact root isolation on restricted rational examples. It is the *exact* reference only for those instances.
5. Classical GCV as an alternative *selection objective*, not an optimizer or a substitute for LOOCV.
6. Prespecified Guerrero smoothness percentages as interpretive benchmarks (no universally optimal Guerrero λ exists).

To avoid conflation, the main solver comparison must use the SAME pooled LOOCV objective for (1)–(4). If GCV is compared, clearly label it as a different criterion. Do not infer that lower LOOCV implies lower latent-trend error automatically.

## Outcomes and statistical units

Per pool record: scenario ID, seed, R, N, σ, trend, seasonality, d; min λ and S; F_min; F at both endpoints; number of sign-change roots; numerical objective gap relative to **finite-grid** reference; evaluations and wall time. Compare on paired instances, not separate random series per method.

Across independent seeds within each scenario, summarize paired differences and confidence intervals by **pool replicate**. The R observations within a pool are NOT R independent Monte Carlo outcome replicates for inference about that pool.

Report the frequency of multiple strict interior minima; near-flat regions; stationary roots close to endpoints; effect of R; runtime and failures. At least one grid resolution and derivative finite-difference sensitivity analysis is required.

## Source-inspired figures (original plan; check ledger for outputs already generated)

1. Same latent τ with low/high noise (one panel per σ); observations and fitted trend.
2. Pooled F(S) vs component C_r(S), minima, stationary roots, exact endpoints.
3. Dense-grid vs root-refinement mismatch/candidate histogram.
4. Factorial distribution of \(\widehat S\), R=1 vs R=3.
5. Runtime vs N and evaluation budget, exact tiny cases separately.
6. Financial series and its retrospective fitted trend, paired with LOOCV surface.

Every figure should be constructed from saved data, with captions documenting data-generation and solver configuration. Negative and degenerate examples must be retained.

## Risks / controls

- Standard LOOCV may under-smooth with serially correlated residuals; use a **separate** robustness experiment with an AR(1) noise process. This is not the original 2017 factorial.
- An optimized criterion should not be evaluated as if independently held out on the same data. Only claim selection geometry and computational precision without a separate performance target.
- A target d=2 fits locally linear trend; the nonlinear Beta mixture may have high curvature and seasonality intentionally breaks the model.
- No market profit, backtest, or forecast claims.
