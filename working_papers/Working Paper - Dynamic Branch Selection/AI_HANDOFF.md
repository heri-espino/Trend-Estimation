# Paper 2 agent handoff — dynamic branches of weighted F

**Current prospective design 2026-10-09.** See
[shared exact decision protocol](../WEIGHTED_SURFACE_PROTOCOL.md)
and [theoretical research charter](../THEORETICAL_CONTRIBUTIONS.md).

## Critical distinction from archived Val1/Val2 algorithm

The earlier CP04–CP08 experiments and
\`apps/smoothness_lab.py\` / \`apps/smoothness_lab_advanced.py\`
used **Val1/Val2** and variants where prior S could be transformed
inside the loss. These are **legacy**. They include negative
outcomes and should not be relabelled as tests of the current method.
Before 2026-10-09, the \`apps/dynamic_branch_cv.py\` launcher
erroneously invoked the legacy app; now it contains a **new, dedicated**
weighted-F branch interface.

## Exact CURRENT mathematical operation

At current forecast origin T and fixed weighting method m, order d,
fit length L, horizon h:

1. Build raw h-step historical prediction losses
   \(\ell_{t_q}(S)=h^{-1}\|y_{t_q+1:t_q+h}
   -G_{d,h}H(S)y_{t_q-L+1:t_q}\|^2\);
   every \(t_q+h\le T\).
2. For each historical update r, construct **method-weighted
   completed forecast-loss functions**:
   \(F_r^{(m,d,L,h)}(S)=\sum_{q\in I_m(r)}w_{r,q}\ell_{t_q}(S)/
   \sum_{q\in I_m(r)}w_{r,q}\).
   The method \`m\` specifies weighting **F / losses**, NOT S.
3. Find admissible interior AND boundary local minima of each
   \(F_r(S)\). **Grid-detected minima** in current code are
   approximate valleys, not certified stationary roots.
4. Match candidate minima between **adjacent historical F surfaces**
   one-to-one under fixed S-radius epsilon. Unmatched minima
   begin/end branches. Crossings and ties make branch identity
   potentially ambiguous. Multiple branches are not guaranteed.
5. Represent branch \(V_j=\{(r,t_r,S^*_{j,r},F_r(S^*_{j,r}))\}\).
   Use a predeclared selector \(\psi\) based ONLY on completed
   historical weighted F + support to choose an active branch.
6. **AFTER tracking**, use \(\phi(V_j)\), initially mean of the
   last 3 S minima (or available fewer), to obtain operational S.
   This mean is NOT substituted into F when computing its minima.
7. Fit the newest L points with that S, forecast h, score an
   untouched external test. **NO mandatory internal Val2**.

Everything depends on the particular \((m,d,L,h)\). Different methods
may have different F geometry and different branch counts.

## Central theoretical questions

- Local persistence and continuation when stationary minima are
  simple (\(F'_r(S)=0,F''_r(S)>0\)) and successive F perturbations
  are small; this is a **potential theorem under assumptions**,
  not a globally proven persistence result.
- Branch birth/death, intersection, coalescence, endpoints, nonunique
  matching and discontinuity of a selection policy.
- Selection information: whether tracking history offers truly new
  predictive value beyond the global minimum of the **exact same F**,
  in stationary and nonstationary regimes.
- False positives from numerical grid resolution and matching-radius
  sensitivity; do not confuse numerical continuity with physical
  trend persistence.

## Implementation, evidence and app

- **Current app:** \`streamlit run apps/dynamic_branch_cv.py\`
  with synthetic/CSV/Yahoo input, all/last-K uniform/linear/
  exponential F weights, tracked branches, loss matrices, H,
  forecast and exports; \`apps/README.md\` documents exact controls.
- **Shared engine:** \`experiments/smoothness_cv/weighted_surface_study.py\`.
- **New experiment:** 528-cell prospective simulation DGP campaign
  and matched Paper 1 global-argmin baseline; **NOT run/validated
  as completed**.
- **Old evidence:** CP04–CP08 with older method, some unfavorable
  out-of-sample results. Preserve frozen results and acknowledge them.
- **Manuscript:** \`manuscript/main.tex\` is a dated working draft;
  it has not been rewritten to claim new results.
- **GPU note:** secondary matrix-calculation engineering, not a
  theorem about branch persistence; see
  [computational note](../COMPUTATIONAL_IMPLEMENTATION.md).
