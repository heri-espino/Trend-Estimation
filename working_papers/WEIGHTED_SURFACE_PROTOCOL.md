# Shared prospective protocol — weighted forecast-loss surfaces

**2026-10-08 | Current proposed method for Papers 1 and 2.**
This document defines one family of historical forecast-loss surfaces.
The two papers ask **different questions** about precisely the same family.
Historical CP01–CP08 experiments and manuscripts remain dated evidence;
they are **not** retroactively results for this redesigned algorithm.

## Information available at an outer origin T

Predeclare difference order \(d\), training-window length \(L>d\),
forecast horizon **\(h\)**, origin stride, weighting policy \(m\), and the
branch-matching and decision rules where applicable. At \(T\), only
\(y_1,\ldots,y_T\) are available. Each historical origin \(t\) used below must
satisfy \(t+h\le T\).

Use the pure PLS smoother and polynomial continuation:

\[
Q_d=D_d^\top D_d,\quad
H_{d,L}(S)=(I_L+\lambda(S)Q_d)^{-1},\quad
G_{d,h}\in\mathbb R^{h\times L},
\]
with the exact \(S=1\) endpoint defined as the projector onto
\(\ker(D_d)\). The normalized index is
\(S=[L-\operatorname{tr}H_{d,L}(S)]/(L-d)\in[0,1]\).

For each **completed** historical forecast origin, compute the same raw
future-block loss independently of any weighting method:

\[
\ell_t^{(d,L,h)}(S)
=\frac1h\left\|
y_{t+1:t+h}
-G_{d,h}H_{d,L}(S)y_{t-L+1:t}
\right\|_2^2.
\]

A **method \(m\)** is a prespecified temporal weighting rule over these
historical loss functions: equal weights over all available origins,
uniform weights over the last \(K\), linear recency weights, or exponential
recency weights. Later completed origins may be given more weight.
The lookback \(K\), decay, stride, and all tuning rules are selected without
using the current outer block.

For chronological completed origins \(t_1<\cdots<t_M\), let
\(I_m(r)\subseteq\{1,\ldots,r\}\) denote the **past/present only** origin
indices retained by method \(m\) at historical update \(r\).
Then

\[
\boxed{
F_r^{(m,d,L,h)}(S)=
\frac{\sum_{q\in I_m(r)} w_{r,q}^{(m)}
\ell_{t_q}^{(d,L,h)}(S)}
{\sum_{q\in I_m(r)} w_{r,q}^{(m)}},
\qquad w_{r,q}^{(m)}\ge0,
}
\]
with a positive total weight. **No later \(\ell_{t_q}\) with \(q>r\)**
is allowed to affect historical surface \(F_r\).

The weighted surface \(F_r\) is available only once all historical
validation outcomes that it uses have been realized; in this setup
the latest block completes at \(t_r+h\).

## Paper 1 — pooled / weighted forecast-CV

For fixed \((m,d,L,h)\), **minimize the latest complete weighted surface**:

\[
\boxed{\widehat S^{\mathrm{pool}}_{T,m,d,L,h}
\in\arg\min_{S\in[0,1]}F_M^{(m,d,L,h)}(S).}
\]

The equal-weight all-origin variant is the original pooled criterion.
Recency-weighted aggregation is an extension. Paper 1 does **not**
match local minima across time, average minimizing S values, or select a
historical fitted trend for reuse. The final forecast is built after
**refitting** the last available length-\(L\) window using the selected S.

## Paper 2 — method-and-order-specific local-minimum tracking

For the **same fixed method \(m\)** and \(d,L,h\), consider **every**
chronologically available weighted surface \(F_1,\ldots,F_M\).
At each update \(r\), detect all admissible local minima of \(F_r(S)\)
on \(S\in[0,1]\) (including feasible endpoint minima) and record their
location and loss.

Match minima one-to-one between *adjacent weighted surfaces* with a
predeclared normalized-S radius \(\varepsilon_{\mathrm{track}}\).
Unmatched new minima start **new branches**, while unmatched old branches
stop. Crossings/births/deaths make identification **model-dependent**.
A separate set of trajectories is generated for each \((m,d,L,h)\);
the numbers and trajectories of branches may differ.

For active branch \(j\), use a **decision rule specified beforehand**,
e.g. \(\phi_j=\text{mean of its last three local-minimum locations}\).
This rule is applied **after** tracking, **not inside** \(F_r(S)\).
In the first pilot, select the eligible active branch with the smallest
recent historical weighted-\(F\) score **evaluated at the smoothing value
actually delivered by its decision rule**. Require minimum branch support,
and use a specified fallback if none qualify. This is a historical
in-sample branch-ranking heuristic, not a proof of superior forecasting.

\[
\boxed{
\widehat j_T=\psi(\{V_{j,M}\};\,\text{past complete }F_r),
\qquad
\widehat S_T^{\mathrm{track}}=\phi(V_{\widehat j_T}).
}
\]

**No extra Val2 block is required to construct or choose these branches.**
The earlier two-stage Val1/Val2 branch protocol is an **archived,
different algorithm**, not the current proposed method.
An untouched **outer future block** is still mandatory to evaluate both
Paper 1 and Paper 2 honestly.

## Non-equivalence, evaluation and limitations

- Paper 1: **aggregate loss, then choose its global minimum**.
- Paper 2: **construct weighted surfaces, track their local minima,
  then choose a branch and operational smoothness**.
- A method \(m\) weights **loss functions** \(\ell_t(S)\), not S values.
  Averaging last-three local-minimum S values is a **separate branch
  decision rule**, applied only in Paper 2.
- At each outer origin \(T\), both methods use **only** previously
  completed validation folds. Their selected S is used to refit on the
  latest observed \(L\)-window; the unobserved future is used for
  scoring **only**.
- The pilot can compare *predeclared* (method, d) combinations but must
  **not pick a winning method or order using the same outer test**
  subsequently reported as independent evidence. Use separate
  historical model-selection or nested rolling evaluation.
- With overlapping forecast blocks, historical losses are dependent.
  Weighting recent folds trades stability for adaptation.
- A grid-based minimum detector is only approximate; the numerical
  methods working paper must assess resolution, roots, boundaries,
  and correspondence stability before claims of complete recovery.
- Historical CP04–CP08 tests of the old Val1/Val2 method **do not test**
  this replacement; their positive and negative findings remain in
  their original checkpoint records.

## Implementation and manual pilot

The common implementation, shared by **both papers**, is
[weighted_surface_study.py](../experiments/smoothness_cv/weighted_surface_study.py).
For the first pilot from the repo root:

~~~bash
python -m experiments.smoothness_cv.run_weighted_surface_study --quick
~~~

For user data with a numeric \`observed\` column:

~~~bash
python -m experiments.smoothness_cv.run_weighted_surface_study --csv my_series.csv --column observed --orders 2 --horizon 3 --lookback 8
~~~

The manual runner exports:
- \`decisions_and_outer_test.csv\`: pooled and tracked S and outer-test MSE
  for each predeclared \((m,d)\) pairing;
- \`tracked_local_minima.csv\`: tracked candidate history by branch;
- \`weighted_F_<method>_d<order>.csv\`: actual weighted surfaces;
- \`PROVENANCE.txt\`: parameters and diagnostic limitations.

The pilot is **not** the new paper's frozen experiment or a confirmation
of predictive performance. It is a testable starting point for designing
the final benchmark. Full simulations and LaTeX/PDF builds remain manual.
