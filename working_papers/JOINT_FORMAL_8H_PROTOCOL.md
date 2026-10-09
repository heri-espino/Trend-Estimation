# Shared 8-hour prospective simulation — three independent working papers

**Version: 2026-10-09. Status: design + code implemented, NOT executed
or scientifically confirmed on the university workstation.**
This is a fixed **time-budgeted exploratory screen**, NOT a completed
unbiased confirmatory factorial unless every declared cell receives the
same predeclared seed allocation. Do not describe its partial results
as evidence of universal superiority or successful publication.

The three papers share **the same historical h-step F, same generated
observations, same numerical candidates and same outer test**, but
answer distinct questions:

- **Paper 1**: does horizon-matched selection of normalized smoothness
  via global argmin of temporal weighted F improve forecasting?
- **Paper 2**: does tracking minima of EXACTLY that same F improve
  prediction over its global argmin, at fixed m,d,L,h?
- **Paper 3**: how reliably/efficiently do grid, bounded Brent
  refinement and adaptive analytic stationary-root search find
  minima of those same weighted F surfaces? What do differences
  in selected S do to outer forecast and latent trend recovery?
  Exact rational Sturm is a **separate tiny-instance control**:
  it cannot certify all roots in a large stochastic Monte Carlo case.

## 1. Literature-supported pieces vs proposed contributions

| Component | Status and source |
| --- | --- |
| PLS trace smoothness; CV, GCV, AICc and BIC | Preexisting; Cortés-Toto, Guerrero & Reyes (2017), doi:10.1080/03610918.2015.1005236 |
| Rolling-origin genuine out-of-sample forecast test and multistep h | Standard; Hyndman & Athanasopoulos, *Forecasting: Principles and Practice*, section on time-series CV: https://otexts.com/fpptr/tscv.html |
| Origin/rolling-window recalibration and multiple testing periods | Established evaluation design; Tashman (2000), doi:10.1016/S0169-2070(00)00065-0 |
| Naive, drift, seasonal naive | Standard simple forecasting references; FPP/forecasting textbooks (not invented here) |
| RMSE, MAE, paired relative risks; caution across heterogeneous scales | See Hyndman & Koehler (2006), doi:10.1016/j.ijforecast.2006.03.001 |
| Brent / bounded local minimization | Standard numerical analysis; SciPy \`minimize_scalar\` documentation. One bounded call is *not* a global multimodal solver. |
| Sturm exact positive-root count | Classical exact algebra for small rational instances; not a practical large-N Monte Carlo root solver. |
| Horizon-matched PLS weighted F optimization | New *proposed combination*; requires closest-literature novelty audit and substantive mathematical analysis. |
| Weighted-F local minima persistence and branch decision | Proposed dynamic policy; not an established universally better forecast rule. |

Prior literature does NOT prescribe our unusual DGP shapes, 144-cell
grid or eight-hour compute budget. These are **our preregistered
research choices**, inspired by standard design practice, not exact
reproductions of cited publications.

## 2. Simulated observations and accessible information

For each declared DGP cell and independent seed:
\[
y_t=\tau_t+\xi_t+\varepsilon_t.
\]
\(\tau_t\): latent signal/trend, \(\xi_t\): optional periodic component,
\(\varepsilon_t\): iid Gaussian, AR(1), heavy tail, variance change
or contaminated innovation depending on predeclared cell.

Only y up to the currently available time T enters S selection.
Neither **past true latent trend** nor **future observed/latent
test block** may be used for algorithmic tuning. The true latent
trend is reserved for *diagnostic evaluation and plots*.

At a historical completed fold \(t+h\le T\), the method first fits
\[
\widehat\tau_{t,L}(S)
=H_{d,L}(S)y_{t-L+1:t},\quad
H_\lambda=(I+\lambda D_d^\top D_d)^{-1},
\quad
S=\frac{L-\mathrm{tr}H_\lambda}{L-d}.
\]
Then it predicts the next **h** via order-d polynomial continuation
\(G_{d,h}\):
\[
\widehat y_{t+1:t+h|t}(S)
=G_{d,h}\widehat\tau_{t,L}(S),
\quad
\ell_t(S)=h^{-1}\sum_{k=1}^h
(y_{t+k}-\widehat y_{t+k|t}(S))^2.
\]
Fixed weighted aggregation across completed fold losses gives
\(F_r^{(m,d,L,h)}(S)\). **The weights apply to loss FUNCTIONS**;
mean-of-three S applies only AFTER tracking in Paper 2.

At each held-out **outer** origin T, S is chosen using history
completed by T, the model is refit on the last L *observations*,
and unseen \(y_{T+1:T+h}\) is evaluated. Even if h steps overlap
between outer tests, they remain dependent measurements of
the SAME seed; they are not independent replicates.

## 3. Time-bounded factorial scientific panel

**Preset \`formal8h\`: 144 predeclared DGP cells.**

| Block | Cells | Fixed/balanced factors | Role |
| --- | ---: | --- | --- |
| A. Cortés-Toto source-inspired | 16 | 2 shapes (linear/Beta), 2 N (50/200), 2 noise SD (.5/2), seasonal on/off; iid | Source comparability (note: **rolling forecast extension** != original full-N source evaluation) |
| B. Polynomial and nonlinear signal | 48 | 8 shapes (linear, convex/turning quadratic, cubic, quartic, slow sine, late break, Beta) × 2 N (180/360) × 3 SD (.25/.5/1); iid | Interpretation of noisy trend recovery, fit vs extrapolation and d mismatch |
| C. Regime dynamics | 32 | 8 shapes × 2 N (240/400) × 2 noise families (iid/AR1); sigma .5 | Recency weights and branch stability under changing regimes |
| D. Unusual stress | 48 | 12 unusual shapes × 2 N (300/600) × 2 noise families (iid/4%-contaminated Gaussian); sigma .8 | Robustness, spikes, latent stochastic trends; deliberately exploratory |

All groups are **separate factors**, not a single complete cross
of shapes/noises/seasonality. Cell-wise controls are paired on
the identical simulated observations and outer origins.

Default proposed comparison:
- \`d=2,3\` (assess linear versus quadratic continuation and order
  misspecification);
- \`h=1,3,6,12\` with automatic valid restriction \`h={1,3}\`
  for source N=50 where predeclared;
- \`L\` fixed by the DGP class in \`Scenario.window\`;
- 4 chronological outer origins per series;
- 32 completed inner rolling-origin folds, with stride h;
- 161 normalized-S grid candidates including exact S=0 and S=1;
- five fixed time-weighting methods (uniform all, last-8 uniform,
  last-8 linear, last-8 exp .8, last-20 exp .9);
- Paper 2 branch matching at predeclared radius .10,
  min support 3 and mean-last-3 S after matching;
- classic PLS CV/GCV/AICc/BIC; fixed/ad-hoc S={0,.5,.8,.95,1};
  privileged *oracle latent* selectors labelled NONDEPLOYABLE;
- **non-PLS external benchmark forecasts** naive, drift,
  seasonal-naive and OLS linear in a SEPARATE table
  (these forecasts have no chosen S or EDF).
- Paper 3 runs for every 8th seed within each scenario.
  It compares exact-F grid, refinement by multiple local bounded
  Brent brackets, and derivative-based adaptive stationary
  root search for **the same** uniform and exp-weighted F,
  using a dense 401-S numerical reference **not a root certificate**.
  Save selected S, F, min counts, numerical error, evaluation
  count, runtime, and each method's *actual external* observed
  forecast MSE, future latent forecast MSE, past latent recovery MSE.
- One tiny exact rational Sturm case (L=6,d=2,h=2) is run **once**
  for proof-of-concept; its exact count does not validate all P3 roots.

**Important caveat:** the first full (source-faithful) 2^4
Cortés-Toto *smoothing* replication uses all N data and therefore
is a distinct procedure from our rolling forecast extension.
Keep its own independent run and tables. The 8h screen can reuse
the same 16 generating laws but **cannot claim it reproduces the
source's numerical result table**.

## 4. What "track past and future trend" means

For each decision made at outer T, save (and aggregate by seed):

**Past latent trend recovery**
\[
R_{\mathrm{past}}=
\frac{1}{L}\sum_{i=T-L+1}^{T}
(\widehat\tau_{i|T}-\tau_i)^2.
\]

**Future latent trend forecasting**
\[
R_{\mathrm{latent},h}=
\frac{1}{h}\sum_{k=1}^{h}
(\widehat y_{T+k|T}-\tau_{T+k})^2.
\]

**Future observed forecasting (MAIN operational endpoint)**
\[
R_{\mathrm{obs},h}=
\frac{1}{h}\sum_{k=1}^{h}
(\widehat y_{T+k|T}-y_{T+k})^2.
\]

Plus future conditional-signal loss vs \(\tau+\xi\) (when seasonal),
per-lead squared errors, absolute error, S, EDF, boundary selection
frequency, and number/support of tracked branches. No "one true
optimal S" unless explicitly defined as a specific *oracle risk*.

The two forecast losses are **not identical**: the observation
includes noise/seasonality unmodeled by our polynomial continuation.

## 5. Computation: SOFT eight-hour wall-clock budget

From the repo root on the university CUDA workstation:

~~~powershell
conda activate trend-estimation
git pull --ff-only origin main
python -m pytest tests/test_joint_formal_eight_hour.py tests/test_cuda_simulation.py tests/test_simulation_campaign.py tests/test_weighted_surface_study.py -q
~~~

**Single formal eight-hour candidate command** (manual foreground):
~~~powershell
python -m experiments.smoothness_cv.run_simulation_campaign --backend cuda --preset formal8h --seeds 1000 --seed-wave 8 --gpu-batch-size 8 --orders 2,3 --horizons 1,3,6,12 --outer-count 4 --max-folds 32 --grid-points 161 --numerical-every 8 --numerical-dense-grid 401 --numerical-adaptive-depth 6 --with-baselines --sturm-once --time-budget-hours 8 --run-dir results/smoothness_cv/joint_formal_8h_v1
~~~

**\`--seeds 1000\` is the MAXIMUM declared horizon of tasks, NOT a
claim that 144,000 series will finish in eight hours.**
No fixed amount of work can guarantee an exact wall time because
hardware, I/O and numerical root complexity vary. The scheduler
admits tasks until a **soft monotonic-clock budget** expires,
finishes the active batch and commits atomically. It may end
slightly later than eight hours for a long active batch. It
does not sleep to fill unused time. If tasks remain, the database
is PARTIAL/EXPLORATORY.

**Wave order for balance:** visit A/B/C/D in round-robin by
scenario, processing 8 independent seeds per scenario per wave
instead of exhausting 1,000 seeds of the first scenario. A
time stop can still interrupt a wave; \`run_status.json\` declares
incompleteness and the report must not imply every condition has
equal sample size.

**GPU:** one batched CUDA context for the completed historical
loss matrix in float32; CPU float64 spectral setup and numerical
search, plus CPU classical selectors/branch linking/refit/SQLite.
The previous kernel benchmark is not an end-to-end wall-time
estimate. **No CPU-vs-GPU verification on every batch**
(\`--gpu-verify 0\` by default).
One initial short separate CUDA preflight, when required, can
use \`--gpu-verify 2\`. GPU speed is NOT the theoretical claim.

Exact Sturm needs SymPy in the active Conda environment.
If that dependency is missing, install it with Conda BEFORE
the eight-hour command and rerun the smoke. On failure the
one-time reference fails visibly rather than silently skipping P3.

The run is resumable from the exact same code+configuration by
repeating the command. For a different design/code revision, use
a **different run directory** to preserve provenance. The
budget is per invocation. Do not modify code during a running
frozen experiment. No heavyweight GitHub Actions schedule.

## 6. After a time-budget stop: reports and figures

~~~powershell
python -m experiments.smoothness_cv.analyze_joint_campaign --run-dir results/smoothness_cv/joint_formal_8h_v1 --allow-partial
python -m experiments.smoothness_cv.make_formal_figures --run-dir results/smoothness_cv/joint_formal_8h_v1
~~~

The first command builds the usual Paper 1/2 tables, paired
weighted-vs-uniform contrasts, seed-level CIs where enough
independent replications exist, and joint supplemental reports:

- \`reports/paper3_numerical_cases.csv.gz\`: exact-F Brent,
  adaptive, dense/grid comparisons, forecast recovery and cost;
- \`reports/paper3_numerical_summary.csv\`: group by shape/d/h/m;
- \`reports/forecast_baseline_scenario_summary.csv\`: naive,
  drift, seasonal naive, OLS (no invented S or EDF);
- \`reports/paired_vs_naive_scenario.csv\`: PLS methods vs
  naive matched by seed/outer origin, with nominal uncertainty;
- \`reports/THREE_PAPER_REPORT.md\`: source/status/provenance caveats.

The second command creates **predeclared** PDF/PNG figures for
\(\tau\), noisy observed \(y\), fitted past trend and future
h-step forecasts, for linear, quadratic-turn, cubic-S and
late slope break under Gaussian SD .25/.5/1,
**using same latent generator shape and fixed seed**.
It plots Paper 1 vs Paper 2 from the exact same exponential
weighted F (so any difference is due to tracking, not F).
The figure script reads the S selections from actual stored
outcomes; if a cell has not completed due to the time budget,
it is omitted and labelled missing—not fabricated.

## 7. What the eight-hour screen can and cannot prove

- A *completed balanced study* with enough independent seeds
  and held-out origins can support conditional empirical
  comparisons at those DGP cells.
- A **time-truncated** exploratory campaign is a screen to
  identify failures, robustness and feasible effect sizes,
  **not** an unbiased final confirmation across 144 cells.
- Picking a winning method/weight/d on these same outer
  observations creates selection bias. Freeze it, then run
  **new independent seed blocks/outer tests** for confirmatory
  publication evidence.
- With overlapping forecasting horizons, time errors are
  dependent; replicate-based SEs are over the full simulated
  series/seed, not over every forecast lead or test point.
- A dense grid is not a mathematical certificate of ALL
  stationary points. The one-time Sturm instance proves
  only its own exact finite polynomial root count.
- No single setup is "the standard literature factorial"
  for all three questions. We *borrow established baselines
  and validation principles*, then transparently declare
  our proposed integrated research design.

## 8. Routes to three journal-ready articles

**P1 Results:** observed forecast MSFE and confidence intervals vs
classical CV/GCV/AICc/BIC, fixed S, naive/drift/OLS, latent
past/future, h dependence and recency effects. Explain why
directed h-step risk differs from fit risk.

**P2 Results:** matched tracked-vs-global for the SAME weighted F,
branch cardinality/persistence, counterexamples, regime-change
effects, failure rates, sensitivity to tracking radius and grid.

**P3 Results:** numerical accuracy/cost of multi-bracket bounded Brent
and analytic root search vs dense grid on identical forecast objectives,
effect on outer forecast/latent recovery, finite small-instance Sturm
and explicit absence of a general exhaustive-root certificate.

Do not write journal-conclusion text until the relevant result,
provenance and limitations have been verified.
