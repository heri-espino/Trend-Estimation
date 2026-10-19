# Study M.2 — independent-seed replication of the nine process examples

**2026-10-19 — CODE IMPLEMENTED, MONTE CARLO NOT EXECUTED OR AUDITED.**
The user reports that the first nine-example gallery was successfully run **locally** (198 method rows), but the saved gallery is not yet available in this branch. The earlier study M.1 gallery is documented in [the single-realization protocol](PROCESS_DIVERSITY_ILLUSTRATIVE_EXPERIMENT_2026-10-19.md). The user now explicitly requests **many more seeds**, since the illustrative run was fast. This replaces, rather than contradicts, the previous preference for process diversity over merely increasing *old* Study J/K seeds.

## Target and rules frozen before seeing new results

Replicate **the exact existing nine generating mechanisms**, d=2, N=80, fixed baseline parameters and 11 feasible policies. Do not add methods or tune hyperparameters using the new simulation truth. Base pseudorandom seed 20261019; the gallery used replicate offset 0. New seed windows begin at replicate offset **1** so they do not reuse the displayed gallery outcome. For replicate index j, the generator uses seed 20261019+j. Each seed draws a new three-series base set, and all nine mechanisms are obtained by common-shock paired perturbations, with R=1 nested in R=3.

Within a seed, nine scenarios and R1/R3 comparisons are **dependent**. The independent statistical unit is the entire seed j, not the 198 method rows per seed. Across seeds, the pseudorandom draws are reproducibly independent by generator design.

Primary performance: mean squared reconstruction error of the actual simulated, realized latent trend (tau), averaged over the R fitted series and N observations. Secondary: mean absolute reconstruction error, median and upper-tail MSE, mean fitted mu, normalized S, full-model EDF **when available**, and ex-post method win frequencies. Win frequencies are descriptive and not a deployable model selector. A method's average reconstruction MSE may be driven by rare bad runs; always show both its mean and median and p90.

### Predeclared paired comparisons

1. For each mechanism and each R, rank the eleven methods by **mean MSE over distinct seeds**, not by their score values. The numerical criterion values CV/GCV/AICc/ML are incomparable across criterion types.
2. For each process/R, form per-seed **paired MSE differences** for every pair of the 11 methods (55 pairs). Report the across-seed mean, standard deviation, 95% Student t CI and the fraction of seeds A has lower MSE than B. Negative A-B means A wins.
3. 9 mechanisms x 2 R x 55 pairs = **990 comparisons** with pointwise confidence intervals and separately one exploratory **global Holm p adjustment** over all 990 paired t tests. Interpret with effect sizes; p values are not a guarantee of model correctness and the multiple comparison design remains exploratory.
4. Critically, compare R=3 and R=1 for the **same first observed series** (tau_1 and y_1 literally equal within seed). Report per-seed MSE(tau_1 reconstructed using R3) - MSE(tau_1 reconstructed using R1), with paired CI and pooling-benefit frequency for each case/method. Unlike pooled-average R3 versus one-series R1, this isolates the first series' benefit from parameter pooling; it does not prove a causal real-world pooling advantage.
5. Do **not** mistake fresh random seeds for fresh independent method development: the nine scenarios/eleven policies were selected after prior modeling work. Even many simulated seeds here establish conditional evidence for **these exact nine DGPs**, not universal dominance or guaranteed real-market performance.

All confidence intervals are **nominal** finite-seed approximations and may be less reliable for nonnormal loss differences. The normal-innovation generators here have finite variance and defined MSE, unlike the earlier Cauchy exclusion/t3 fourth-moment concern. The Holm correction is across every available A/B mean-MSE test from these scenarios/R; the pooling sensitivity CIs are explicitly pointwise rather than included in the same family.

## Manual code, sharding, and exact commands (PowerShell)

Runner: [run_process_monte_carlo.py](../../../experiments/pooled_loocv_smoothness/run_process_monte_carlo.py).
Regression checks: [test_pooled_process_monte_carlo.py](../../../tests/test_pooled_process_monte_carlo.py).

From the repository's **existing** paper/pooled-loocv-numerical-optimization branch:

    conda activate trend-estimation
    git switch paper/pooled-loocv-numerical-optimization
    git pull --ff-only
    python -m pytest tests/test_pooled_process_examples.py tests/test_pooled_process_monte_carlo.py -q

To verify the grid without simulation:

    python -m experiments.pooled_loocv_smoothness.run_process_monte_carlo --count 1000 --preview

To run **1000 new independent seeds** for all nine mechanisms, with atomic 25-seed chunks:

    python -m experiments.pooled_loocv_smoothness.run_process_monte_carlo --seed-start 1 --count 1000 --chunk-size 25 --out-dir results/pooled_loocv_smoothness/process_examples/seed_study_1000_v1

If interrupted, retry the exact same command with an appended --resume; existing complete chunks are skipped, then *all* compressed shards re-read/validated before final summaries. Change nothing about seed schedule, names, length or scan-points on resume.

For a **second nonoverlapping 1000-seed set**, to challenge preliminary patterns:

    python -m experiments.pooled_loocv_smoothness.run_process_monte_carlo --seed-start 1001 --count 1000 --chunk-size 25 --out-dir results/pooled_loocv_smoothness/process_examples/seed_study_1000_v2

These are two disjoint seed windows, not the same draws replayed. If more power is required later, continue with seed-start 2001. Do not pick the seed window after seeing surprising winners.

Outputs per run folder:
- manifest.json — exact seed window, commit SHA, versions, status, method/case lists, chunks and completion audit.
- rows_<first>_<last>.csv.gz — atomic, individually resumable *per-seed raw records*. Ignored by Git because potentially large; **keep a separate backup before deleting any VM**. The runner does not pretend to have pushed these to GitHub.
- risk_by_process_method.csv — 9 x 2 x 11 = **198 risk summary rows**, one each process/R/method, with CIs, MAE, median/p90 MSE, mean mu/S/EDF and ex-post win share.
- paired_method_mse_differences.csv — **990 independent-seed paired contrasts**, global Holm adjustment, confidence intervals and win fractions.
- paired_pooling_first_series.csv — 9 x 11 = **99 comparisons** of R3 vs R1 MSE for the exact same first series.

Default 1000 seeds entail **198,000 method rows**, but exactly 1000 independent underlying base innovations and 9 correlated mechanism transformations per seed. Methods fit only observed y; simulated true tau is for ex-post evaluation.

## Interpretation after actual execution and upload

Do not fabricate winners. Audit manifest.status COMPLETE and number of shards, verify independent integer seed windows, verify rows 198*count, and check for accidentally overlapping seed ids with Study M.1 if relevant. Parse summary CSV and identify:

- What wins in the correctly specified Gaussian reference, and by what expected-risk margin, not only a win count?
- Are sinusoidal trends reconstructed differently from true slope/level breaks? Is a discontinuity simply smoothed into a broad transition?
- Does the algorithm smooth over a **true tau jump** differently from **observation-only** outliers when paired observation shocks are the same?
- Does serially correlated error damage leave-one-out CV and Gaussian quasi-ML differently? Avoid asserting causation from loss rankings alone.
- Does changing observation noise across time change the preferred smoothness regime? Does heterogeneous pooling help or harm the low-noise first series?
- When a common observation factor is introduced, how large is the paired reduction (or increase) in reconstruction loss from R3 compared with R1 on **identical first-series data**?
- Which apparent advantages survive **global Holm correction**? If confidence intervals straddle zero, report uncertainty plainly. Note individual mean-MSE confidence intervals are pointwise and no true population ranking is certified.

After running, create a dated research note documenting actual findings, plots if useful, failures and unexpected results. Update RESULTS_LEDGER.md, DECISIONS.md, current-state handoff, paper and root AGENTS/AI_HANDOFF as needed. Raw gzip rows can remain local; commit only compact CSVs and manifest where reasonable, with the precise Git commit SHA recorded. No PR, no merge, do not change main.

## Status tracker

- [x] Study M.1 single-realization runner, tests, manuscript note created.
- [x] User confirmed local successful 9-case M.1 execution, 198 reported method rows; no results uploaded/audited on research branch yet.
- [x] Study M.2 independent-seed resumable runner, seed-pair comparisons, Holm adjusted reports, lightweight CI tests implemented.
- [ ] Study M.2 first independent 1000-seed window user run.
- [ ] Independent audit and results interpretation in dated paper note.
- [ ] Optional second nonoverlapping seed window, only as justified by observed uncertainty.
