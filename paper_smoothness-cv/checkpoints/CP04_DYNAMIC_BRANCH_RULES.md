# Checkpoint 04 — Dynamic branch decision rules

**Status: COMPLETE — frozen confirmation evaluated once and audited.**

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

### 4. Pure recency-weighted mean

Recent branch values may receive exponentially larger weights than older values:

\[
\phi_{\mathrm{recency}}(V_j)
=
\frac{\sum_{r=0}^{R} \rho^r S_{j,T-r}}
{\sum_{r=0}^{R} \rho^r},
\qquad 0<\rho<1.
\]

The newest value has weight one, the previous value has weight \(\rho\), and
so on. We parameterize \(\rho\) by a half-life \(H\),

\[
\rho=2^{-1/H},
\]

so after \(H\) tracked origins the weight is one half of the newest value.
CP04 compares half-lives 3, 5, and 10.

### 5. Validation-2 weighted

\[
\phi_{\mathrm{V2}}(V_j)
=
\frac{\sum_t S_{j,t}/(\ell^{(2)}_{j,t}+\delta)}
{\sum_t 1/(\ell^{(2)}_{j,t}+\delta)}.
\]

### 6. Recency + Validation-2 weighted

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
4. pure recency-weighted mean versus `last`;
5. Val2-weighted versus `last`;
6. recency+Val2-weighted versus `last`;
7. best frozen dynamic rule versus classical CV/GCV/AICc baselines.

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
- `recency_hl3`, `recency_hl5`, `recency_hl10`;
- `val2_weighted`;
- `recency_val2_hl3`, `recency_val2_hl5`, `recency_val2_hl10`;
- `pooled_cv_same_config` baseline.

Pure recency-weighted rules include the current final-Val1 minimum with the
largest weight and exponentially discount older tracked smoothness values.

For the Validation-2-weighted rules, the current final-Val1 minimum is
deliberately not given a Val2 weight because its following block is the
untouched outer test.
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


## Numerical-stability note after first refine run

The first CP04 refine execution exposed occasional warnings of the form

`overflow encountered in square`

inside the level-RMSE calculation for deliberately poor branch candidates.
The underlying forecast values were finite but could be astronomically large
after exponentiating a log-scale trend; direct squaring overflowed before the
square root was taken.

This is a numerical representation issue, not evidence that the local-minimum
search itself failed. The code now computes RMSE by scaling residuals before
squaring. CP04 analysis also compares methods directly on RMSE rather than
forming MSE and then taking square-root ratios.

The already committed first refine output contains no `inf` or `NaN` in
`decision_results.csv`, but because historical branch ranking can encounter
these extreme candidates, rerun smoke/refine after this patch before freezing
the final dynamic rule. The reserved confirmation blocks remain untouched.


## Development decision and frozen confirmation rule

The overflow-safe rerun reproduced the same development ranking as the first
refine execution.

Across the 24 development outer tests, the best dynamic rule was

[
oxed{phi_{mathrm{recency},H=3}}
]

implemented as `recency_hl3`.

Its development geometric RMSFE ratio was

[
0.7989
]

relative to the newest-minimum rule `last`, with a 58.3% outer-test win rate.
Relative to `pooled_cv_same_config`, its geometric RMSFE ratio was

[
1.0491,
]

so the development evidence does **not** establish superiority to the pooled
baseline. This is precisely what the reserved confirmation blocks must test
without further tuning.

The frozen confirmation specification is now:

- primary dynamic rule: `recency_hl3`;
- branch selector: existing persistence + historical mean-Val2 rule;
- selection metric: level RMSE;
- `track_epsilon = 0.10`;
- `candidate_spacing = 0.02`;
- `max_minima = 5`;
- all four difference orders remain eligible;
- window selection remains historical and order-specific;
- comparison baselines: `last` and `pooled_cv_same_config`;
- confirmation sample: the four previously reserved latest non-overlapping
  outer blocks of each of GDPC1, SPY, AAPL, and BTC-USD.

No alternative dynamic `phi` rule is evaluated in confirmation. The
confirmation preset enforces the frozen numerical parameters and will raise an
error if they are changed.

## Run the frozen confirmation once

~~~bash
git pull
pip install -e .
pytest

python experiments/smoothness_cv/run_checkpoint_04.py --preset confirmation --jobs 24
python experiments/smoothness_cv/analyze_checkpoint_04.py
python experiments/smoothness_cv/make_checkpoint_04_figures.py
~~~

After this run, commit and push the complete new CP04 confirmation directory.
Do not rerun confirmation to choose another rule. Any later method change must
be treated as a separate new study.


## Final CP04 confirmation outcome

The one-shot confirmation run is
`results/smoothness_cv/checkpoint_04/20261007T011201Z_confirmation_6c0b548`.

The saved outer manifest confirms that the run used exactly the four previously
reserved latest blocks per series. Only `recency_hl3`, `last`, and
`pooled_cv_same_config` were forecast on those blocks.

Primary confirmation:

[
\boxed{
\operatorname{gRMSFE}
(\text{recency-hl3}/\text{pooled CV})
=
0.6920
}
]

with wins in 13/16 outer blocks.

Against the newest tracked minimum:

[
\boxed{
\operatorname{gRMSFE}
(\text{recency-hl3}/\text{last})
=
0.8137
}
]

with wins in 9/16 outer blocks.

By series, the dynamic/pooled geometric ratios were:

- AAPL: 0.4561;
- BTC-USD: 1.0391;
- GDPC1: 0.8176;
- SPY: 0.5917.

The dynamic/pooled ratio remains below one after omitting any one of the four
series. The dynamic/last advantage is less stable and disappears when AAPL is
omitted.

A stale reporting path in the runner initially marked the saved confirmation
metadata as development-only. This was audited and corrected **without changing
any forecast output**. See the run's corrected `checkpoint_report.md` and
`run_metadata.json`.

CP04 is now closed. Do not retune `recency_hl3` using these blocks.

## Next checkpoint

Proceed to `CP05_EXTERNAL_PANEL.md`: a 64-series external financial panel
selected mechanically from the frozen repository snapshot, excluding the three
financial series used in CP04.
