# Checkpoint 04 — Dynamic branch decision rules

**Status: DEVELOPMENT EXPERIMENT IMPLEMENTED — run smoke, then refine.**

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

## Implemented development protocol

Code:

- `experiments/smoothness_cv/dynamic_branch_rules.py`
- `experiments/smoothness_cv/run_checkpoint_04.py`
- `experiments/smoothness_cv/analyze_checkpoint_04.py`
- `experiments/smoothness_cv/make_checkpoint_04_figures.py`

The development experiment uses the tracked real-series panel already used
by the numerical work: GDPC1, SPY, AAPL, and BTC-USD.

For every series it constructs **repeated non-overlapping outer test blocks**.
The newest four blocks are reserved completely for a later confirmatory run.
The `refine` preset evaluates six earlier outer blocks per series and never
loads the reserved future into any individual outer decision.

At each outer origin the experiment:

1. chooses `L` separately for each `d=1,2,3,4` from historical Val1 only;
2. recovers and tracks local minima on historical Val1 surfaces;
3. refits through Val1 and stores Val2 error for every matched branch;
4. selects one persistent branch using the frozen baseline `psi`;
5. continues that branch to the final pre-test Val1 surface;
6. applies every candidate `phi` rule to the **same branch history**;
7. freshly refits the trend on the newest full window;
8. scores the same untouched outer test;
9. compares with pooled forecast-CV using the same selected `(d,L)`.

Development rule grid:

- `last`;
- `mean_k3`, `mean_k5`;
- `median_k3`, `median_k5`;
- `val2_weighted`;
- `recency_val2_hl3`, `recency_val2_hl5`, `recency_val2_hl10`;
- `pooled_cv_same_config` baseline.

For the weighted rules, the current final-Val1 minimum is deliberately not
given a Val2 weight because its following block is the untouched outer test.
The numerical stabilizer is scale-relative: `1e-8 * median(positive Val2 loss)`
with a floor of `1e-12`.

The `refine` run is development-only. It is allowed to choose the final
`K` / half-life specification. It is **not** the confirmation test.

## Run now

From the repository root:

~~~bash
git pull
pip install -e .
pytest

python experiments/smoothness_cv/run_checkpoint_04.py --preset smoke --jobs 8
python experiments/smoothness_cv/analyze_checkpoint_04.py
python experiments/smoothness_cv/make_checkpoint_04_figures.py
~~~

If smoke passes, run the development refinement. On the current 24-core /
32-logical-processor machine, use 24 workers:

~~~bash
python experiments/smoothness_cv/run_checkpoint_04.py --preset refine --jobs 24
python experiments/smoothness_cv/analyze_checkpoint_04.py
python experiments/smoothness_cv/make_checkpoint_04_figures.py
~~~

Then commit and push the complete `results/smoothness_cv/checkpoint_04/`
directory and stop. Do **not** evaluate the four reserved confirmation
blocks yet. The final dynamic rule must be frozen from the refine output
before a confirmation preset is implemented.
