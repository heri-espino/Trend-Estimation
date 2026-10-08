# Dynamic branch selection — canonical *weighted-F* method

**Redesigned prospective protocol | 2026-10-08.** This is the **new**
definition of Paper 2. The previous Val1/Val2 transformed-surface design
and completed CP04–CP08 results are **historical**; do not relabel them
as tests of this procedure.

Canonical common formulation:
[working_papers/WEIGHTED_SURFACE_PROTOCOL.md](../../WEIGHTED_SURFACE_PROTOCOL.md).

## 1. Fix method m, difference order d, window L, horizon h

For each \((m,d,L,h)\), predefine **before outer testing**:

- \(m\): weighting of completed **forecast-loss curves** (equal,
  last-K equal, linear recent, exponential recent);
- \(d\), \(L>d\), and the same operational forecast horizon \(h\);
- origin stride and maximum historical origins;
- local-minimum detection tolerance and tracking radius \(\varepsilon\);
- branch eligibility and selection policy \(\psi\);
- branch-to-smoothness policy \(\phi\), initially the **mean of last 3
  minima in the selected branch** (or fewer when the branch is younger).

Methods are *not* post-hoc transformations of S within the objective.

## 2. Weighted historical forecast surfaces

At a completed historical origin \(t_q\), the *raw* future-block forecast
MSE for PLS smoothing \(S\) is

\[
\ell_{t_q}^{(d,L,h)}(S)=\frac1h
\|y_{t_q+1:t_q+h}-G_{d,h}H_{d,L}(S)y_{t_q-L+1:t_q}\|_2^2.
\]

For each completed update \(r\) and preregistered \(m\), aggregate only
losses at \(q\le r\):

\[
\boxed{
F_r^{(m,d,L,h)}(S)
=\frac{\sum_{q\in I_m(r)}w^{(m)}_{r,q}\ell_{t_q}(S)}
{\sum_{q\in I_m(r)}w^{(m)}_{r,q}}.
}
\]

The method-specific **rolling weighted surfaces** are what the paper
tracks. A different \(m\) or \(d\) may create a different number and
geometry of minima and branches. Note that changing \(d\) also changes
the trend continuation \(G_{d,h}\).

## 3. Detect minima and match to branches

At each \(r\), including candidate **boundary minima**,
\[
\mathcal M_r^{(m,d,L,h)}
=\operatorname{LocalMin}_{S\in[0,1]}F_r^{(m,d,L,h)}(S).
\]

Connect adjacent updates with **one-to-one matching** where the
locations are at most \(\varepsilon_{\mathrm{track}}\) apart. Prefer
maximum-cardinality/minimum-distance feasible matching to a greedy
local nearest-neighbor rule. Unmatched new minima start new branches;
unmatched previous minima retire. No globally unique branch
identity is guaranteed near crossings, births, or deaths.

The current pilot uses a **grid detector**; its minima are candidates,
not certified roots. Do not present them as mathematical completeness.

For each method and order, retain
\[
V_j^{(m,d)}=[(r,t_r,S^*_{j,r},F_r(S^*_{j,r}))]_{r\in\mathcal T_j}.
\]

There is **no compulsory second validation block** in this data
structure. The historical Val1/Val2 \(V_j\) schema from CP04–08
belongs to the old design.

## 4. A decision at the operational origin T

Two distinct decisions are required:

**Branch selection:** \(\widehat j_T=\psi(V_1,\ldots,V_J)\), based
*only* on completed historical curves, branch support, and a
predeclared loss score. A proposed pilot policy requires enough
consecutive branch history and ranks active branches by recent
historical weighted-\(F\) evaluated at the smoothness produced by
their own policy \(\phi\). Missing eligible branches use an explicit
fallback; this ranking is a heuristic with potential selection bias
and must be tested externally.

**Operational smoothness:** after choosing \(j\), compute
\[
\widehat S_T=\phi(V_{\widehat j_T}),\quad
\phi_{\mathrm{mean3}}(V_j)
=\frac{1}{\min(3,n_j)}
\sum_{k=0}^{\min(3,n_j)-1}S^*_{j,\mathrm{last}-k}.
\]

**Mean-three is not used to generate the losses or the local minima.**
It is a post-tracking action on the chosen branch. One can examine
last-S, median-three, or branch forecasting as separately
predeclared extensions, but these do not change the definition of
method \(m\) as **weighting F**.

Refit \(H_{d,L}(\widehat S_T)\) on the most recent length-\(L\)
observations at \(T\), extrapolate \(h\) periods and **only afterward**
score the untouched outer future block.

## 5. Why this is distinct from Paper 1

Paper 1 globally minimizes the **last complete weighted surface**:
\[
\widehat S_T^{\mathrm{pool}}=
\arg\min_S F_M^{(m,d,L,h)}(S).
\]

Paper 2 tracks **all detected local minima** through the sequence
\((F_1,\ldots,F_M)\), then selects a branch and uses its
last-three mean. The two can use the **same weighting methods and raw
validation observations**, and still produce different smoothing
choices.

## 6. Evaluation and provenance

The current manual comparison entrypoint is

~~~bash
python -m experiments.smoothness_cv.run_weighted_surface_study --quick
~~~

Code: \`experiments/smoothness_cv/weighted_surface_study.py\`.
It evaluates both decision rules over the same completed historical
folds and scores final forecasts against an **untouched external**
holdout. Its output from **one** outer block is a diagnostic, *not*
a robust comparative experiment. For model/method/order selection
and publication claims, use time-respecting nested or otherwise
independent outer evaluations.

Historical work remains available:
- [Prior two-stage branch notes](tracked_minimum_smoothness_selection_legacy.tex).
- [Original tracking correspondence questions](temporal_minima_tracking.md).
- [Completed CP04–CP08 evidence](results_and_boundaries.md).

Do not claim that CP04–08 demonstrate performance for the new
weighted-F method; the earlier two-stage transformed-loss protocol
performed inconsistently against pooled forecast-CV.
