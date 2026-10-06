# Dynamic forecast-optimal smoothness by chronological validation

**Status: ACTIVE.**

**Primary target journal:** *Journal of Forecasting*.

**Working title:** *Dynamic Forecast-Optimal Smoothness for Penalized Trend Estimation*.

## Central scientific question

For a finite-difference penalized trend, can the local minima of a chronological
forecast-loss surface be tracked through time and used to choose the current
smoothness more effectively than a single pooled forecast-CV optimum?

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

Candidate `phi` rules include the newest local minimum, recent mean/median,
Validation-2 weighted smoothness, recency-plus-Validation-2 weighting, and
later a forecast of the smoothness trajectory itself.

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

## Current empirical status

CP01 and CP02 explored the simpler pooled selector. CP03 is a frozen
paper-scale run of that pooled baseline and should be retained as baseline
evidence even though the paper's central direction has now expanded.

The next experiment must compare dynamic branch rules on the **same tracked
branches and same untouched test blocks**. Do not retune CP03 after viewing its
results.

Existing `experiments/numerical_smoothness_selection/run_two_stage_order_validation.py`
already implements the core branch-tracking chronology and the `last` rule.
It also stores mean/median/recent smoothness summaries. The next smoothness-CV
checkpoint should formalize and compare `phi` rules without test leakage.

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
