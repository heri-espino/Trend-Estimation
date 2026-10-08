# Dynamic forecast-optimal smoothness by chronological validation

**Status: ACTIVE.**

**Primary target journal:** *Journal of Forecasting*.

**Working title:** *Dynamic Forecast-Optimal Smoothness for Penalized Trend Estimation*.

## Central scientific question

For a finite-difference penalized trend, how can local minima of chronological
forecast-loss surfaces be represented as persistent temporal branches, and
which distinct smoothness-decision functionals can be defined on the resulting
branch histories? Whether a particular rule improves forecasts relative to
pooled forecast-CV is an empirical question, not a property of the framework.

The paper now distinguishes two objects.

### Static pooled baseline

For fixed `d,L,h`,

\[
F^{\mathrm{pool}}_{T,h}(S)
=
\frac1M\sum_{m=1}^{M}\ell_{m,h}(S),
\]

and

\[
\widehat S^{\mathrm{pool}}_{T,h}
\in
\arg\min_{S\in[0,1]}F^{\mathrm{pool}}_{T,h}(S).
\]

This asks which single smoothness has the lowest average historical forecast
loss.

### Dynamic tracked-minimum formulation

At each chronological origin `t`, compute the local minima

\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\}.
\]

Track minima across adjacent origins using a one-to-one continuation rule

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon.
\]

Each persistent branch stores

\[
V_j=
\begin{pmatrix}
S_{j,t_1} & \ell^{(1)}_{j,t_1} & \ell^{(2)}_{j,t_1}\\
\vdots & \vdots & \vdots
\end{pmatrix},
\]

where `ell1` is Validation-1 forecast loss and `ell2` is the immediately
following Validation-2 forecast loss after refitting through Validation 1.

The forecasting decision is separated into

\[
\widehat j_T=\psi(V_1,\ldots,V_J)
\]

for branch selection and

\[
\widehat S_T=\phi(V_{\widehat j_T})
\]

for the current smoothness extracted from the selected branch.

Examples of `phi` include the newest minimum, recent mean/median,
Validation-2 weighted smoothness, recency-plus-Validation-2 weighting,
and extrapolation of the smoothness trajectory using recent linear trends
or historical smoothness increments. These are demonstrations of a design
family, not contestants for one universal winner.

Canonical formulation: `notes/dynamic_tracked_smoothness.md`.

## Core estimator

\[
\widehat\tau_\lambda=H_\lambda y,
\qquad
H_\lambda=(I+\lambda D_d^\top D_d)^{-1}.
\]

Normalized smoothness:

\[
S(\lambda)
=
1-\frac1{L-d}
\sum_{\delta_j>0}\frac1{1+\lambda\delta_j}.
\]

At an outer origin `T`, once a final `S_hat_T` is chosen by either the pooled
baseline or a tracked-branch rule, all temporary validation fits are discarded.
The trend is refit on the newest `L` observations:

\[
\widehat\tau_T
=
H_{\lambda(\widehat S_T)}y_{T-L+1:T},
\]

then forecast with the native finite-difference continuation operator:

\[
\widehat y_{T+1:T+h\mid T}=G_{d,h}\widehat\tau_T.
\]

**We average validation losses or smoothness values only when a rule explicitly
requires it. We never average historical fitted trends.**

## Direct lineage

The methodological lineage remains

\[
\text{Guerrero controlled smoothness}
\longrightarrow
\text{forecast-selected smoothness}
\longrightarrow
\text{dynamic tracked forecast smoothness}.
\]

Hart (1994) remains an important predictive-smoothing precedent, but it is not
the same estimator or tracked-minimum problem.

## Paper ownership

This paper owns:

- the forecasting interpretation of tracked smoothness branches;
- the branch state matrix `V_j`;
- branch selection `psi` using historical information;
- the final smoothness rule `phi(V_j)`;
- the pooled forecast-CV selector as a baseline;
- chronological Validation-1 / refit / Validation-2 semantics;
- untouched outer-test forecasting evaluation;
- comparisons among last/mean/median/weighted/predicted smoothness rules.

`paper_numerical-methods/` owns:

- locating all relevant local minima of each `F_t(S)` surface;
- adaptive subdivision, derivative diagnostics, Brent refinement, and exact
  endpoint handling;
- numerical branch correspondence/tracking across nearby surfaces;
- possible certified root isolation using rational/Sturm structure.

Do not merge those contributions.

## Completed empirical evidence

- CP03: frozen 3,000-scenario, 72,000-block simulation of horizon-matched
  pooled forecast-CV and classical smoothness benchmarks.
- CP04: 16 reserved outer tests from four heterogeneous time series;
  frozen recency branch rule / pooled CV gRMSE = 0.692.
- CP05: 64 previously unused financial series, 256 outer tests;
  frozen recency / pooled CV gRMSE = 1.642. Broad-panel superiority
  was not established.
- CP06: post-hoc continuation-order diagnostics identify high-order
  extrapolation as a major source of unstable forecast paths.
- CP07: 1,200 controlled roughness scenarios, 9,600 outer decisions;
  recency / pooled CV observed-log-RMSE = 1.037 overall.
- CP08: fresh 1,200-scenario demonstration of several maps
  \(\phi(V_j)\) from identical branch histories, including three
  reproducible figures and boundary-clipping diagnostics.

CP08 closes the rule-family demonstration stage; no universally best
functional is claimed. The next step is to compile and review the
manuscript, including the completed empirical section and illustrations.


## Read first

1. `AI_HANDOFF.md`
2. `notes/dynamic_tracked_smoothness.md`
3. `notes/validation_semantics.md`
4. `notes/research_objective.md`
5. `notes/roadmap.md`
6. `manuscript/main.tex`

## Build

~~~bash
python paper_smoothness-cv/build.py --check
python paper_smoothness-cv/build.py
~~~


## Five-panel workflow tutorial

The forecasting manuscript includes a full-width pedagogical figure,
`fig_workflow_tutorial.pdf`, at the end of its evaluation-design section.
The five horizontal panels show:

- a historical Train/Validation-1/Validation-2 pair, followed by a
  **separate current/final Validation-1 block** and an untouched outer test;
- fresh penalized trend fits on the latest window for pooled CV, the newest
  tracked minimum, and the recency-weighted mean;
- the three forecasts against the subsequently observed outer test;
- the **current Validation-1 forecast-loss curve** (never the test-loss
  curve), recovered minima, and all three smoothness decisions;
- historical tracked minimum branches and the final branch-to-smoothness
  maps \(\phi(V_j)\).

The figure uses a deterministic example: CP07 switch-to-rough simulation,
seed 100, observation-noise SD 0.01, outer decision 8. It is not selected
using test performance. The script writes PDF, PNG, and machine-readable
provenance directly to `manuscript/figures/`.

From the repository root, in this order:

~~~powershell
python experiments/smoothness_cv/make_workflow_tutorial_figure.py
python paper_smoothness-cv/build.py --check
python paper_smoothness-cv/build.py
~~~

`build.py --check` intentionally reports a missing figure if the generator
has not been run. `build.py` stages the manuscript source (including its
`figures/` folder) and the separately frozen CP08 figures.
