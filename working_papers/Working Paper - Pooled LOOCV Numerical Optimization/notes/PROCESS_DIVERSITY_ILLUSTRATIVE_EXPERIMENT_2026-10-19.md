# Process diversity: nine illustrative DGPs rather than more seeds

**2026-10-19 — IMPLEMENTED, NOT EXECUTED.** This note describes the experimental contract of [run_process_examples.py](../../../experiments/pooled_loocv_smoothness/run_process_examples.py). The compact fixture tests are [test_pooled_process_examples.py](../../../tests/test_pooled_process_examples.py). Neither a test fixture nor an authored protocol is evidence of completed Monte Carlo.

## Question and distinction from existing work

Study H already evaluated eight methods on 160,000 independent Gaussian base draws. Studies J/K.1 already tested 12 non-Gaussian error laws, including heavy tails, skewness and GARCH, with 25 reused seeds in each of 192 strata, including 26 selection policies. Instead of reproducing that entire factorial with more random seeds, this new gallery asks **which failures are caused by signal shape, temporal observation dependence, or invalid pooled-series assumptions?**

We use a single fixed random base sample for all case-specific transformations. The fitted difference order is d=2; default length N=80, R=1 or 3, base seed 20261019. R=1 is the *first series from R=3*, not an independent replicate. Baseline:
\[
D_2\tau^{(r)}=\mu\mathbf1+\varepsilon^{(r)},\quad
y^{(r)}=\tau^{(r)}+\eta^{(r)},\qquad
\mu=0.04,\ \sigma_\varepsilon=0.12,\ \sigma_\eta=0.80.
\]
Innovations are Gaussian and independent in the baseline. The realized trend includes accumulated innovations, not merely its expectation.

## Nine processes and their diagnostic purpose

| Case | Changed structure | Question |
|---|---|---|
| gaussian_reference | Correct Gaussian d=2 model | Baseline performance with correctly specified covariance and mean |
| smooth_cycle | Add 3 sin(2 pi t / 24) to the latent trend | Does smoothing remove genuine curvature? |
| slope_break | Add 0.75 max(t-floor(N/2),0) to the latent trend | How do methods handle a change in slope? |
| level_jump | Add a genuine +7 latent level shift halfway through | Can a global squared-roughness penalty preserve a true discontinuity? |
| observation_outliers | Add measurement outliers of ±8 to observed y but not tau | Is a noise outlier falsely incorporated into estimated trend? |
| ar1_observation | Replace eta by marginally SD-matched stationary Gaussian AR(1), phi=0.85 | Does ordinary leave-one-observation-out CV leak information through serial dependence? |
| variance_regime | Observation-noise multiplier 0.45 then 1.35 | Does heteroskedasticity distort inferred smoothness? |
| heterogeneous_pool | R=3 series with eta SD 0.25, 0.80 and 1.50 | Can one common lambda work for differently noisy series? |
| shared_observation_shock | Cross-series observation-noise correlation 0.70 | How much of pooling's apparent gain survives dependent replicates? |

Signal-perturbation examples use *exactly the same observation shocks* as the reference; observation-noise examples use the *same realized latent trend*. All comparisons are conditional on a shared random basis. Except for the specifically named mechanism, do not change the smoother or its fitted order. The 2017 Cortés-Toto factorial differs; this is NOT a reproduction of their published experiment.

## Exactly eleven feasible estimators

The runner fits the existing CV, GCV and AICc scores with either fixed mu=0 or joint fitted mu (six policies); Gaussian differenced-covariance GLS mean/covariance ML; the pooled observed-difference plug-in plus our covariance ML; forced-zero-mu covariance ML; and exogenously preset normalized smoothness S=0.5 or 0.8 with fitted joint mu (two policies). That is 11 feasible policies per example. No simulation-true-mu or true-variance **oracle** is included. The fixed-smoothness policies are not data-selected optima; Gaussian ML is a quasi-likelihood outside its covariance assumptions. The joint-mu CV reestimates mu fold-honestly and joint GCV/AICc use full RN-dimensional EDF.

For criterion-based selection the same existing score-grid multibracket method is used with 31 points and its original positive-lambda range plus allowable exact endpoints. This is *not* the separate Study L numerical-optimization comparison. Different statistical scores have different scales and MUST NOT be compared by their raw score numbers.

## Running the focused contrasts manually on the existing branch

PowerShell, from repository root:

1. conda activate trend-estimation
2. git switch paper/pooled-loocv-numerical-optimization
3. git pull --ff-only
4. python -m pytest tests/test_pooled_process_examples.py tests/test_cortes_optimality_criteria.py -q
5. python -m experiments.pooled_loocv_smoothness.run_process_examples --cases gaussian_reference,level_jump,observation_outliers --out-dir results/pooled_loocv_smoothness/process_examples/contrast_jump_001

For all nine cases, replace the last command with:

    python -m experiments.pooled_loocv_smoothness.run_process_examples --out-dir results/pooled_loocv_smoothness/process_examples/gallery_001

Outputs: manifest.json with seed/source/version and scope; method_comparison.csv with selected lambda, normalized nominal S, fitted mu, EDF when available, method-specific criterion score, and **ex-post simulated latent-trend MSE and MAE**; illustrative_winners.csv describing the minimum realized MSE in THAT ONE synthetic realization; and one plot per case/R showing tau, observed y and a fixed list of five selected methods. No winner is selected from latent tau during fitting. The script refuses an existing nonempty output directory. Default scale: nine mechanisms × two nested R sizes × 11 policies = **198 method rows**, but these are NOT 198 independent statistical repetitions. Heavy/full Monte Carlo remains manual-only, and this gallery requires no additional seed grid.

## Scientific interpretation contract

This is a collection of **counterexamples or illustrations**, not a new confirmatory risk study. A method winning one seeded realization proves no stochastic dominance. Measure how the chosen lambda/S and fitted mu shift across matched perturbations. Compare observed true jumps with observation-only outliers; compare reference iid noise with the identical trend under serially correlated or heteroskedastic eta; inspect R=1 vs R=3 without pretending they are independent populations. Never infer actual financial trend truth from observed prices.

Under an abrupt structural trend break, smoothing may trade bias against noise differently; neither CV nor AICc nor Gaussian quasi-ML is guaranteed to win. Under autocorrelation, ordinary observation-deletion CV may be optimistic, but an iid covariance-based likelihood is ALSO misspecified. With a contaminated observation, all the current quadratic criteria can be sensitive; none is a robust M-estimator. With heterogeneous or correlated pools, the effective benefit of combining series depends on covariance/weights, not simply R.

**Not yet executed:** no CSVs, plots or winners have been produced by this authored change. After the user runs the script and commits compact results, write a dated source-linked RESULTS note before changing any scientific claim in the paper. Update RESULTS_LEDGER.md, DECISIONS.md, the current-state handoff and the paper/root handoffs. Do not add more scenarios or seeds automatically.

Potential future processes only when motivated by gallery findings: time-varying difference mean, mean-reverting latent state, local-to-unity dependence, fractional/long-memory innovations, fitted-versus-generating order mismatch, irregular time spacing (requires changing D), or multivariate common latent factors.
