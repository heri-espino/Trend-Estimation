# Simulation and evaluation protocol — Papers 1 and 2

**Design proposal, 2026-10-08. NOT executed.** No frozen results, performance
claim or final preregistration is implied by this document. The purpose is to
prevent a forecasting method from being judged solely by how much smoothness
it selects or by how small its **training** loss becomes.

Both papers use [the common weighted-F decision protocol](WEIGHTED_SURFACE_PROTOCOL.md)
and the same data-generating processes (DGPs), outer origins, forecast horizons,
noise realizations, and classical PLS competitors. Their **decisions** differ:
Paper 1 globally minimizes the newest complete weighted surface; Paper 2
tracks its historical local-minimum branches and selects a branch-specific S.

## 2026-10-09 addition — formal CUDA execution and new stress Study D

**Prospective study, not a result**. The same Paper 1 pooled and
Paper 2 branch algorithms now accept float32 CUDA-computed
**completed-origin forecast-loss matrices** through the formal runner.
The default formal GPU run does **not** compare to CPU at each batch.
Perform one small preflight with \`--gpu-verify 2\`, then
\`--preset mega --backend cuda --gpu-verify 0\` (0 is default).

**Study D** is a predeclared factorial stress/robustness extension:
12 latent-trend mechanisms (jumps, jump-recovery, a transient pulse,
frequency-changing oscillations/chirps, beating waves, plateau,
terminal spike, accelerating oscillations, double sigmoid, stochastic
level and stochastic slope), lengths N=300/600, noise scale
sigma=.25/.8/1.6, iid/AR(1)/Student-t5/heteroskedastic/4% contaminated
outlier noise, optional quarterly seasonality. This forms
\(12\times2\times3\times5\times2=720\) additional scenario cells.
The \`mega\` preset includes 528 A/B/C + 720 D = **1,248 cells**;
100 replicates/cell are **124,800 scenario–seed instances**.

The two stochastic trends are generated from an additional
seeded RNG (separate from observation noise) so the simulated
latent \(\tau_t\) remains available for *external* error measurement;
only y enters the selectors. As before, fixed \(V=I\) in the PLS
smoother is NOT an assertion that the actual DGP noise is iid.

**Paper 1 question:** when does recency-weighted global minimization
help/hurt near these irregular dynamics? **Paper 2 question:** does
local-minimum branch persistence improve future h-step forecasts
beyond the *same* weighted-F global argmin, or introduce spurious
instability? Paper 3 numerical solvers remain a separate
CPU/adaptive-root research workflow; the new CUDA production runner
does NOT yet accelerate arbitrary certified root isolation or Sturm.

Precise implementation, one-time precision audit, timing and commands:
[CAMPAIGN_README.md](../experiments/smoothness_cv/CAMPAIGN_README.md).
Do not claim the expanded study has already been run.

## 1. What the 2017 source actually did

Cortés-Toto, Guerrero and Reyes (2017, *Communications in Statistics—
Simulation and Computation*, Section 3, pp. 1498–1500) conducted a
**2^4 factorial simulation**, NOT two separate prospective forecasting
experiments. Its **two latent-trend shapes** were:

- Linear: \(\tau_t=4t/N\), with \(t=1,\ldots,N\).
- Nonlinear: \(\tau(u)=0.6\beta_{30,17}(u)+0.4\beta_{3,11}(u)\),
  where \(u\in[0,1]\) and \(\beta\) is the **Beta density** (not Gamma density).

Cross these with seasonal component **absent/present**, observation noise
standard deviation \(\sigma=0.5\) or \(2\), and \(N=50\) or \(200\).
The seasonal pattern has period 4 and values \((1,-0.5,-2.5,2)\).
The article used pure PLS with \(d=2,\mu=0\), and CV, GCV, AICc and BIC;
AIC was tried but discarded because its numerical results were unreliable
for some simulated series. They examined **attained smoothness** and
factorial effects, not a systematic comparison of genuinely unseen
\(h\)-step forecast MSE versus known latent-trend reconstruction MSE.

Its raw Guerrero index is
\(S_G=1-\operatorname{edf}/L\), maximum \(1-d/L\) for \(d\ge1\).
Our normalized index is
\(S=[L-\operatorname{edf}]/(L-d)\), maximum 1. Use **both** for comparisons
to article tables. Never interpret a difference due solely to normalization
as a scientific discrepancy.

### Operational separation of faithful reference and forecast extension

A **dedicated implemented full-sample factorial runner**
[\`run_cortes_toto_replication.py\`](../experiments/smoothness_cv/run_cortes_toto_replication.py)
scores CV/GCV/AICc/BIC on the **complete source-paper N-point data**,
\(d=2,\mu=0\), and computes raw \(S_G\) and normalized S. It is
separate from the main extensive forecast campaign, whose historical
training windows have length \(L\ne N\).
Run separately:

~~~bash
python -m experiments.smoothness_cv.run_cortes_toto_replication --seeds 100 --jobs 32 --grid-points 501
~~~

The source had one factorial simulation study with two trend shapes
rather than two full prospective forecasting studies. Our added
forecast and latent-recovery outcomes are explicitly new extensions.

### What "reproduce" means

- **Replication track (faithful):** same two signals, original 2^4
  conditions, \(d=2,\mu=0\), and selectors CV/GCV/AICc/BIC; report
  selected \(\lambda\), \(\operatorname{edf}\), \(S_G\), \(S\) and summaries
  of factor effects. Original paper's few replicates are not enough
  for precise Monte Carlo estimation, so use a larger predeclared
  count (initially 100; final count set after timing and precision
  pilot). Do not imply identical random draws or exact replication
  of every reported summary.
- **Prospective extension:** use *the same* DGPs to compare forecast
  selection and **new** targets, with a chronological outer test.
  Separately label this a new experiment, not a replication of their
  forecasting results (they did not report such results).
- Keep true latent \(\tau\), seasonal \(\xi\), and observed \(y\)
  in distinct arrays.

## 2. Model, information boundaries and two different losses

Generate for the full simulation span,
\[
y_t=\tau_t+\xi_t+\varepsilon_t,
\]
with the generating components separately recorded. Latent \(\tau_t\)
is known to the experiment analyst **only for scoring and oracle
diagnostics**. It is never supplied to a feasible selector.

At an external test origin \(T\), only \(y_{1:T}\) enters the method
(and all its candidate evaluations). Select \(\widehat S_T\) from
**completed historical \(h\)-step validation blocks**; refit the
last \(L\) values using \(H_{d,L}(\widehat S_T)\); produce
\(\widehat y_{T+1:T+h}=G_{d,h}H_{d,L}(\widehat S_T)y_{T-L+1:T}\).
Use the same continuation across competitors with the same \(d,L,h\).
Reserve \(y_{T+1:T+h}\) entirely for external scoring.
Methods/origins/hyperparameters must not be selected based on those
external scores subsequently presented as independent evidence.

### 2.1 Primary endpoint: future observed-series forecast

\[
\boxed{\mathrm{MSE}_{\mathrm{obs},T,h}
=\frac1h\sum_{k=1}^h
(y_{T+k}-\widehat y_{T+k\mid T})^2.}
\]

Report RMSE as **sqrt of aggregated MSE**, not average of replicate
RMSE; report pooled and per-lead \(k\) errors. Paired error differences
relative to the **equal-weight all-origin pooled baseline** are the
principal comparisons. For each replicate and outer origin use exactly
the same observations and train/test masks for all selectors.

### 2.2 Second endpoint: latent-trend recovery, past fit

\[
\boxed{\mathrm{MSE}_{\mathrm{trend,past},T,L}
=\frac1L\sum_{i=T-L+1}^{T}
(\widehat\tau_{i\mid T}-\tau_i)^2.}
\]

This is NOT \((\widehat\tau-y)^2\), since the observed series includes
noise and sometimes seasonality. Report original-data residual RSS/MSE
**only as a fit diagnostic**, not as "true trend accuracy".

### 2.3 Third endpoint: future *latent* trend

\[
\boxed{\mathrm{MSE}_{\mathrm{trend,future},T,h}
=\frac1h\sum_{k=1}^h
(\widehat y_{T+k\mid T}-\tau_{T+k})^2.}
\]

For the pure continuation used here, forecast notation
\(\widehat y\) is an extrapolation of the trend. This metric asks how
well it continues the **latent trend**, a different target from
\(\mathrm{MSE}_{\mathrm{obs}}\). If \(\xi\ne0\), score a *fourth*
diagnostic against the conditional signal \(\tau+\xi\) when appropriate,
since the extrapolation does **not** explicitly model seasonality.

For future IID zero-mean noise independent of fitted history, no
seasonality and constant variance, the **expected** observed forecast
risk is future latent-trend risk plus \(\sigma^2\). This identity
does not hold unchanged for dependent, heteroskedastic or seasonal
settings; do not subtract \(\sigma^2\) indiscriminately from realized
scores.

### 2.4 Fourth endpoint: smoothness selected, stability and cost

For every method, outer origin and DGP record:

- chosen \(S\in[0,1]\), **raw** \(S_G=1-\mathrm{edf}/L\),
  \(\lambda\), \(\mathrm{edf}=L-(L-d)S\), \(d,L,h,m\);
- mean, median, IQR, variance of chosen S across seeds/origins;
- temporal changes \(|S_T-S_{T-\Delta}|\), endpoint frequency
  \(S\approx0\) / \(S\approx1\), and forecast-vs-recovery tradeoff;
- computation time, objective evaluations, convergence/warnings,
  detection accuracy when a reference minimizer exists.

No *intrinsic* uniquely "correct smoothness" exists for an arbitrary
deterministic simulated \(\tau\). Define explicitly the target-dependent
oracle below rather than pretending the DGP gives a natural S%.

### 2.5 Oracle limits — diagnostics ONLY, NEVER actual selection

Define (using information unavailable to the real predictor):

- \(S^*_{\mathrm{rec},T}\): minimizes
  \(\mathrm{MSE}_{\mathrm{trend,past},T,L}(S)\) against known \(\tau\).
- \(S^*_{\mathrm{latent},T,h}\): minimizes the error of the
  **forecast continued trend** against \(\tau_{T+1:T+h}\).
- \(S^*_{\mathrm{future-y},T,h}\): hindsight minimizer against
  the *realized* outer \(y_{T+1:T+h}\). **Optimistic and noise-fitting**;
  NOT a feasible selector, NOT the true statistical optimum.

Report gaps \(|\widehat S-S^*_{\mathrm{rec}}|\) and
\(|\widehat S-S^*_{\mathrm{latent}}|\) only **with their oracle label**.
A more defensible forecast target is the **population** oracle that
minimizes expected out-of-sample risk under a fully specified DGP,
estimated via *independent additional Monte Carlo draws* rather than
a single future noise realization. Numerical regret and forecast
regret must never be mixed.

## 3. Three complementary experiments

### Experiment A — source-inspired reference 2^4 factorial

**Goal:** reproduce original attained-smoothness comparisons, then
independently extend them to recovery and genuine forecast outcomes.

- Latent shape: original **linear**, original **Beta-mixture**.
- Seasonal effect: original 4-period pattern **off/on**.
- IID Gaussian \(\sigma\): original **0.5/2**.
- Sample \(N\): original **50/200**.
- Keep original PLS \(d=2,\mu=0\). Reference CV, GCV, AICc,
  BIC implemented on **the identical discrete PLS \(H_\lambda\)**.
- On faithful replication: report \(S_G,S,\mathrm{edf}\) and factor
  effects; paper's reported summaries use the **raw** index.
- On forecast extension: add equal-weight pooled and recency-weighted
  forecast-CV using origins whose \(h\)-step outcomes have completed.
  Because \(N=50\) is short, preregister a *feasible smaller* \(L\),
  inner-fold count and short horizons (e.g., \(h=1,3\)).
  The \(N=200\) counterpart may include longer horizons.
  Do not confuse full sample length \(N\) with fitting-window length
  \(L\). Compare methods only on common valid outer origins.

**Status:** defined here as a plan; not yet rerun for the new framework.

### Experiment B — broader trend-shape / degree mismatch study

**Goal:** isolate trend shape, horizon and mismatch between true
degree/curvature and fitted continuation order.

Include these clearly labelled **new DGPs** (the exact coefficients,
signal-to-noise standardization, and time scaling will be frozen in a
machine-readable configuration before simulations):

1. **Linear** \(\tau(u)=a+bu\).
2. **Quadratic** \(\tau(u)=a+bu+cu^2\), including a turning-point case.
3. **Cubic** \(\tau(u)=a+bu+cu^2+eu^3\), including inflection.
4. **Smooth nonpolynomial**: a sine or Beta-mixture shape.
5. **Piecewise linear with a slope break** at a frozen change point.
6. **Smooth regime transition / terminal bend** (e.g. sigmoid or
   continuous quadratic bend).
7. Optionally **low-frequency oscillation** as an intentionally
   difficult extrapolation problem, outside main polynomial examples.

Scale these to comparable **latent dynamic ranges** before applying
noise, and predeclare whether noise SD means absolute \(\sigma\) or
a common signal-to-noise ratio. Fix the *underlying time path* across
sample-length and horizon comparisons: do not covertly change the
DGP because normalized time has been redefined after splitting.

**Primary ablation:** fix \(d=2\), \(L\), and horizon \(h\), so
differences between selectors can be interpreted fairly.
**Order-mismatch study:** separately evaluate \(d\in\{1,2,3,4\}\):
the maximally smooth limit of order \(d\) is a polynomial of degree
\(d-1\). Thus \(d=2\) can extend a line, \(d=3\) a quadratic,
\(d=4\) a cubic, but **higher order may explode in long-horizon
extrapolation**. Do not select d on test labels or conflate order
selection with smoothness selection.

Candidate horizons: \(h\in\{1,3,6,12\}\), with common outer origins
and completed inner validation blocks where feasible. Candidate noise
models: IID Gaussian main study, AR(1), Student-t(5), and
heteroskedastic robustness layers. Predeclare selected factorial
crosses rather than running an uncontrolled huge Cartesian product.

### Experiment C — changing regimes and local branch tracking

**Goal:** test specifically whether tracking historical minima provides
information *beyond* minimizing the newest weighted surface.

Use **the same** per-origin \(\ell_t(S)\), time-weighting \(m\),
\(d,L,h\), and external evaluation origins for both papers.
Freeze benchmark methods:

- Paper 1: equal-weight all-origin pooled;
- Paper 1: most recent K uniform;
- Paper 1: recent linear weights;
- Paper 1: recent exponential weights;
- Paper 2: each **same m** with tracked local minima, a fixed matching
  radius, a predeclared branch-selection policy, and last-three
  minima mean (with a documented young-branch fallback).
- Classical PLS LOOCV/GCV/AICc/BIC, and **fixed/ad-hoc S**
  baselines, on the same final fit and forecast continuation.

Main DGP conditions:
- **Stationary smoothness / stationary trend mechanism**: negative
  control, branches should not be assumed to have an advantage.
- **Sudden slope or curvature break**: adaptation versus oversmoothing.
- **Gradual change in latent curvature or innovation variance**.
- **Periodic or intermittent changes of underlying curvature**.
- **An initially stable regime followed by a late change**.
- Optional noise-only variance break and seasonality as diagnostic
  misspecification (avoid changing everything simultaneously).

For Paper 2 also record **branch-structure diagnostics** by \((m,d)\):
number of detected local minima, births/deaths, duration, percentage
of origins with multiple admissible minima, continuation distances,
assignment ambiguity, number of fallback decisions, selected branch
support, and sensitivity to grid resolution and matching radius.
Grid minima are **candidate valleys**; a separate numerical
benchmark must verify that they approximate true stationary/boundary
minima, and distinguish numerical tracking mistakes from statistical
performance. Branches may not exist in plural for every method/d.

The **legacy CP04–CP08 Val1/Val2 experiments are not evidence about
this new weighted-F branch algorithm**. Preserve them as frozen
historical work; do not silently combine their numbers with new runs.

## 4. Competitors: not all are forecast scores

| Selector (what selects S) | Why include | Independent evaluation |
| --- | --- | --- |
| PLS LOOCV | Reconstruct withheld in-sample points | same outer h-step test |
| PLS GCV | Approximate LOOCV using EDF/trace | same outer h-step test |
| PLS AICc | Penalized in-sample selection | same outer h-step test |
| PLS BIC | Penalized in-sample selection | same outer h-step test |
| PLS AIC (diagnostic) | Source tried it and reported numerical issues | separate, not headline unless stable |
| Fixed S: e.g. 0, 0.50, 0.80, 0.95, 1 | **ad-hoc** user-chosen controlled smoothness | same outer h-step test |
| Paper 1, equal-weight full | required primary pooled baseline | same outer h-step test |
| Paper 1, recent equal/linear/exponential | time-weighting ablation | same outer h-step test |
| Paper 2, same m/d and tracked branches | tests use of branch *history* | same outer h-step test |
| Latent recovery/forecast oracles | unattainable targets for interpretation | **never deploy or select by them** |

AICc, BIC, GCV and LOOCV are **smoothing parameter selection
criteria**, not measurements of external forecasting accuracy.
We may show their selected S and criterion values, but the
*head-to-head performance metric* is a common outer future MSE.
For fair comparisons use the same \(d,L,h\), training mask and
forecast extrapolation \(G_{d,h}\). If \((m,d)\) selection is itself
learned, use another chronological selection layer or a completely
independent evaluation; otherwise declare fixed alternatives.

## 5. Fixed/ad-hoc smoothness: define, do not dismiss

An analyst might pick \(S=0.8\) or \(0.95\) **without optimization**.
This is an essential comparator to distinguish the claimed benefit
of *data-driven smoothness selection* from merely using a fairly
smooth trend. Predeclare fixed levels and optionally add a
**calibration-selected constant S** learned from an independent
development set. A post-hoc best fixed S on the final test is an
oracle, not a valid achievable baseline.

Measure **how much and when** our S decisions differ from these
fixed choices, how EDF changes, how sensitive results are to \(N,L,d\)
and which fixed values remain surprisingly competitive.
The scalar S remains comparable on \([0,1]\) but equal S values at
different \(L,d\) do not imply identical spectral responses/EDF.

## 6. Experimental design, uncertainty, release gates

### Staging

1. **Correctness/smoke:** 1–3 seeds and a handful of cases. Check
   exact \(S=0,1\), fixed windows, identical folds, correct oracle
   isolation, stable spectrum and all expected output columns.
2. **Precision/timing pilot:** start with 20–30 seeds to estimate
   runtime, Monte Carlo uncertainty, and frequency of difficult
   minima. This is **not** the final test and should determine a
   predeclared affordable R.
3. **Frozen experiment:** initial target around 100 independent
   seeds per main cell (or increase until stated Monte Carlo
   precision is met), exact scenarios, seeds, order/horizon,
   weight schemes, search tolerances and report script frozen
   beforehand. Outer origins repeated through each series.
   Larger exploratory sweeps are separate from confirmatory
   comparisons and must be labeled.

### Independence and statistical inference

- Use common random numbers **within each seed across all competing
  methods**; different seeds are independent Monte Carlo units.
- Forecast errors for neighboring rolling origins are correlated,
  particularly when horizon blocks overlap. Prefer a main outer
  stride \(\ge h\) where feasible, and explicitly analyze overlapping
  sensitivity separately. That stride does **not** make entire
  histories statistically independent.
- Report paired differences in external MSE and relative RMSE,
  with confidence intervals **clustered by independent simulated
  series / seed**, not by every horizon step or every origin.
  Multiple scenario/horizon comparisons require clear primary
  outcomes and multiplicity-aware interpretation.
- Include win/loss and failure rates **by DGP**, not solely an
  averaged win rate that can conceal severe outlier losses.
- For final publication, keep a held-out set of independent seeds
  or an untouched study stage to avoid researcher-side overfitting
  after extensive method exploration.

### Suggested machine-readable output

One row per (study, scenario, seed, outer origin, d, L, h, method):

\`tau_dgp, seasonality, noise_family, sigma, regime_parameters,
 seed, T, d, L, h, method, weighting_scheme, lookback, decay,
 selected_S, selected_lambda, edf, raw_Guerrero_S, outer_obs_mse,
 outer_latent_trend_mse, past_latent_recovery_mse, rss_fit,
 branch_id, branch_support, n_local_minima, n_branches, runtime,
 selector_convergence, root_detection_method, git_sha\`.

Write full \(F_r(S)\) matrices and branch records in separate
artifacts with a manifest; don't duplicate wide matrices into each
result row. Record the simulated \(\tau,\xi,\varepsilon,y\) arrays
or reproducible generators/seeds for post-hoc diagnostics.
Only frozen outputs can be interpreted as completed research.

## 7. Predeclared questions that should appear in the papers

**Both:** Does selecting smoothness for horizon \(h\) beat classical
reconstruction-based criteria on the **same outer h-step forecast**?
Does this trade improved forecasting for worse/better latent trend
recovery? How do S and EDF respond to true trend shape, noise,
sample length and horizon? Is an optimized S materially better than
a fixed/ad-hoc smoothness?

**Paper 1:** Is equal pooling sufficient? Do recency weights help
adaptation to nonstationarity, and how costly are they when the
mechanism is stationary?

**Paper 2:** Are meaningful local-minimum branches stable,
reproducible and predictive after controlling for the choice of
weighted-F method? Does tracking help **over its paired global-argmin
counterpart using the exact same \(F_r^{(m,d,L,h)}\)**, or merely
create more selection variance and endpoint effects?

## 8. Current execution status and large factorial implementation

**2026-10-08 code prepared, NOT run:** the new high-throughput campaign
now has the following concrete files in the research repository:
- [DGPs](../experiments/smoothness_cv/simulation_dgps.py)
- [Paired evaluation](../experiments/smoothness_cv/simulation_evaluation.py)
- [32-worker resumable runner](../experiments/smoothness_cv/run_simulation_campaign.py)
- [Memory-bounded report](../experiments/smoothness_cv/analyze_simulation_campaign.py)
- [Single-case inspection](../experiments/smoothness_cv/inspect_simulation_case.py)
- [Full operational instructions](../experiments/smoothness_cv/CAMPAIGN_README.md)

**528 predeclared scenario cells in extensive preset**: 16 original
2^4 source-paper cells, 384 complexity/curvature cells, and 128
regime-change/robustness cells. With **100 seeds per cell**, the
main campaign contains **52,800 scenario–seed simulation instances**,
each evaluated at common outer origins and horizons, with multiple
methods measured on the same realized observations. Independent seeds **within each DGP cell**, not outer origins or
candidate methods, are the replication units; reusing the same seed
across different DGP cells may induce paired dependence across cells.
The runner can use **32 logical CPU processes**, one BLAS thread
per worker, with SQLite transactions and manifest-checked restart.
The RTX Ada GPU is not currently required or used.

The implemented design measures future observed MSE/MAE, latent
future trend MSE, past latent recovery, EDF/normalized and source
smoothness, classical CV/GCV/AICc/BIC, fixed S and privileged oracle
diagnostics. It separately records method-specific branch structure.

**Scientific gates that remain:** execute and debug smoke tests, pilot
throughput and memory, evaluate minimum-detection convergence,
freeze an independent confirmatory seed allocation, and run the
full experiment. Present implementation must NOT be mistaken for
completed evidence; external method/order choices from the same
test still require new untouched confirmation. The current pilot
does not yet implement a general nested selector over arbitrary
\(m,d,L\), nor a certified all-root search. The new manuscript must
await tested and independently confirmed results.

