# Checkpoint 04 — Dynamic branch decision rules

**Status: DESIGN / IMPLEMENTATION NEXT.**

Checkpoint 03 remains the frozen pooled forecast-CV baseline. CP04 introduces
the central dynamic method without altering CP03.

## Scientific question

Given tracked local-minimum branches

\[
V_j=[S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t}]_t,
\]

which branch should be used, and how should its historical smoothness trajectory
be converted into the smoothness used for the current forecast?

## Fixed decomposition

Branch selection:

\[
\widehat j_T=\psi(V_1,\ldots,V_J).
\]

Current smoothness:

\[
\widehat S_T=\phi(V_{\widehat j_T}).
\]

Final refit:

\[
\widehat\tau_T
=
H_{\lambda(\widehat S_T)}y_{T-L+1:T}.
\]

The outer future block is untouched until scoring.

## Branch selector baseline

Use the branch-selection logic already implemented in
`run_two_stage_order_validation.py` as the first baseline:

1. eligible branches must continue to the final pre-test origin;
2. if complete-support branches exist, compare only them;
3. otherwise compare the branches with maximum support;
4. choose the branch with the smallest mean historical Validation-2 loss;
5. deterministic tie-break by order and branch id.

Alternative `psi` rules are not introduced until this baseline has been
evaluated cleanly.

## Final-smoothness rules to compare

All rules receive the **same selected branch history**.

### 1. Last

\[
\phi_{\mathrm{last}}(V_j)=S_{j,T}.
\]

This is the currently implemented tracked-minima forecast rule.

### 2. Recent mean

\[
\phi_{\mathrm{mean},K}(V_j)
=
\frac1K\sum_{r=0}^{K-1}S_{j,T-r}.
\]

### 3. Recent median

\[
\phi_{\mathrm{median},K}(V_j)
=
\operatorname{median}\{S_{j,T-K+1},\ldots,S_{j,T}\}.
\]

### 4. Validation-2 weighted

\[
\phi_{\mathrm{V2}}(V_j)
=
\frac{\sum_t S_{j,t}/(\ell^{(2)}_{j,t}+\delta)}
{\sum_t 1/(\ell^{(2)}_{j,t}+\delta)}.
\]

### 5. Recency + Validation-2 weighted

\[
\phi_{\mathrm{recency+V2}}(V_j)
=
\frac{\sum_t \rho^{T-t}S_{j,t}/(\ell^{(2)}_{j,t}+\delta)}
{\sum_t \rho^{T-t}/(\ell^{(2)}_{j,t}+\delta)}.
\]

## Development-only tuning

`K`, `rho`, `delta`, and `track_epsilon` must be chosen without seeing the final
outer test. The initial experiment should use a small predeclared grid and a
nested chronological development split.

Do not choose different values per test series from its final test result.

## Required outputs

One row per outer origin, branch rule, and series/simulation case containing at
least:

- selected branch id;
- branch support;
- current/newest `S`;
- final `S_hat` produced by the rule;
- recent mean/median;
- historical Val2 branch score;
- final trend-fit window;
- outer forecast MSE/MAE;
- difference versus pooled forecast-CV;
- difference versus `phi_last`;
- oracle regret in simulations where latent future is known.

Also save the full branch matrices used for each decision.

## Primary comparisons

1. dynamic `last` versus pooled forecast-CV;
2. recent mean versus `last`;
3. recent median versus `last`;
4. Val2-weighted versus `last`;
5. recency+Val2-weighted versus `last`;
6. best frozen dynamic rule versus classical CV/GCV/AICc baselines.

## Numerical-method dependency

CP04 must consume a fixed local-minimum/branch-tracking interface. Changes to
the numerical search or branch matcher for numerical reasons belong to
`paper_numerical-methods/` and must be versioned separately.

## Stop rule

Before a paper-scale CP04 run, freeze:

- `track_epsilon`;
- branch birth/death policy;
- branch selector `psi`;
- candidate `phi` rules;
- `K` grid/final value;
- `rho` grid/final value;
- `delta` convention;
- outer origins;
- forecast horizons;
- primary metrics.

After the final dynamic run is observed, these choices may not be changed to
improve reported performance.
