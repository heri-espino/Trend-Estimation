# Large simulation campaign — Paper 1 and Paper 2

## PRIORITY: 8-hour common experiment for Papers 1, 2 and 3 (2026-10-09)

The formal **time-bounded, shared** three-paper design is now
[JOINT_FORMAL_8H_PROTOCOL.md](../../working_papers/JOINT_FORMAL_8H_PROTOCOL.md).
It is more interpretable than arbitrarily truncating the 1,248-cell
\`mega\` stress grid: 144 predeclared cells with balanced
source/polynomial/regime/rare-shape coverage, three noise levels for
the same B latent trends, outer h-step forecast evaluation,
true past/future latent trend errors, classical PLS
CV/GCV/AICc/BIC and naive/drift/seasonal-naive/OLS baselines,
and **Paper 3 Brent/adaptive root diagnostics on a predeclared
subset of exactly the same F** with tiny exact Sturm once.

The runner supports a **soft eight-hour wall-clock budget** with
atomic SQLite checkpoints and \`--seed-wave\` round-robin study
scheduling. If incomplete, label results **exploratory**;
neither 8 hours nor a mega scenario count grants formal
confirmatory status. Do not repeat CPU/GPU kernel comparisons
during the formal study (\`--gpu-verify 0\` by default).

Test, run and analyze with **these** commands:

~~~powershell
python -m pytest tests/test_joint_formal_eight_hour.py tests/test_cuda_simulation.py tests/test_simulation_campaign.py tests/test_weighted_surface_study.py -q
python -m experiments.smoothness_cv.run_simulation_campaign --backend cuda --preset formal8h --seeds 1000 --seed-wave 8 --gpu-batch-size 8 --orders 2,3 --horizons 1,3,6,12 --outer-count 4 --max-folds 32 --grid-points 161 --numerical-every 8 --numerical-dense-grid 401 --numerical-adaptive-depth 6 --with-baselines --sturm-once --time-budget-hours 8 --run-dir results/smoothness_cv/joint_formal_8h_v1
python -m experiments.smoothness_cv.analyze_joint_campaign --run-dir results/smoothness_cv/joint_formal_8h_v1 --allow-partial
python -m experiments.smoothness_cv.make_formal_figures --run-dir results/smoothness_cv/joint_formal_8h_v1
~~~

These are **instructions, not assertions that the suite has already
passed or been run** on the user's workstation. Exact Sturm needs
SymPy in the Conda environment. A failure should be fixed before
the eight-hour run. The wall-clock stop happens **after** the
active batch and can exceed the nominal budget slightly.
The full bibliography/methodology and publication caveats are in
the linked protocol.



**Status: implemented prospective campaign, not executed in the repository.**
This is the **new** source-inspired + large synthetic study. It does not
overwrite CP01–CP08, does not claim a winning method, and does not
automatically run at a push/build.

## Why large *and interpretable*

The study is a balanced factorial design with **528 DGP cells** in
the extensive preset, not an unstructured search over arbitrary cases.
Each cell has independently replicated simulated series; **within a
replication**, *all compared methods see the same generated series*
and the same untouched outer forecast origins.

| Experiment | DGP cells | Factor design | Scientific role |
| --- | ---: | --- | --- |
| A (Cortés-Toto reproduction/extension) | 16 | two source shapes × seasonality on/off × sigma (.5,2) × N (50,200) | attained smoothness and recovery/forecast baseline |
| B (trend complexity) | 384 | 16 shapes × N (180,360) × SD (.25,.5,1) × 4 noise mechanisms | linear/quadratic/cubic, nonlinear and order mismatch |
| C (regime adaptation) | 128 | 8 regime shapes × N (240,400) × SD (.25,.8) × 4 noise mechanisms | stationarity controls, breaks and tracking |

At **100 independent seeds per DGP cell**, the extensive campaign
contains **52,800 scenario–seed simulation instances**.
Each of those is evaluated over multiple outer origins, forecast horizons,
candidate smoothness levels and methods; these additional evaluations are
*paired repeated measurements*, **NOT 52,800 times a misleading large
multiplier of independent replications**.

Each scenario cell has independently drawn seed replications; reusing seed IDs
across scenario cells can intentionally induce paired/common-random-number
dependence. Therefore the 52,800 instances are **not** globally
independent observations for statistical inference. The user may increase independent seeds (e.g. \`--seeds 200\` gives 105,600
scenario–seed instances). The previous experiments included thousands of outcomes, but
these new results have their **own** independent method/manifest identifier.

**Default compared methods:**
- Paper 1: uniform all folds, last-8 uniform, last-8 linear weights,
  last-8 exponential decay 0.8, last-20 exponential decay 0.9;
- Paper 2: **the same five method-specific weighted F histories**, with
  local-minimum tracking and mean of last three tracked S minima;
- classical CV, GCV, AICc and BIC on the **same PLS family**;
- fixed normalized S of 0, .5, .8, .95, 1;
- **clearly marked oracles** for past latent recovery and future latent
  trend, for research diagnostics only (never deployable selection).

**Reported outcomes:** future observed MSE/MAE and per-lead squared errors;
future true latent-trend MSE; past true latent-trend MSE; conditional
signal error when seasonality exists; selected S, lambda, EDF, original
Guerrero S; branch counts, detected local minima and selected support.

## Dedicated full-sample replication of Cortés-Toto et al. (2017)

**Important distinction:** in Experiment A of the rolling-forecast
campaign we recreate the original *generating mechanisms* but
select on historical fitting windows of length \(L\), not the
source-paper full sample \(N\). To reproduce the source paper's
**attained smoothness** comparison itself, use a **separate**
full-\(N\) replication that applies CV/GCV/AICc/BIC to
all \(N=50\) or \(200\) observations:

~~~bash
python -m experiments.smoothness_cv.run_cortes_toto_replication --seeds 100 --jobs 32 --grid-points 501 --run-dir results/smoothness_cv/source_factorial_v1
~~~

This independently resumable 2^4 design has **16 cells × 100 seeds =
1,600 complete simulated series**, with **four classical PLS
selectors**, and exports:
- \`reports/source_factorial_by_cell.csv\`: achieved raw Guerrero
  smoothness, our normalized smoothness, EDF and latent recovery;
- \`reports/main_effect_contrasts.csv\`: high-minus-low main factor
  effects across the original balanced 2^4 cells;
- \`reports/source_factorial_replicates.csv.gz\`: seed-level audit
  trail, with \`source_factorial.sqlite\` preserving atomic progress.

It is a close methodological replication with a finer/more systematic
grid and new random draws, not literal replication of their
particular R samples or significance levels. The new h-step forecast
comparisons are **reported separately**.

## Formal CUDA simulations: one-time validation, then GPU only (2026-10-09)

**CURRENT EXECUTABLE:** \`run_simulation_campaign.py\` supports
\`--backend cuda\`. This now executes **the actual completed-origin
h-step PLS loss tensor** for multiple independent simulated series
on one CUDA device in float32. It is NOT merely the old standalone
speed benchmark. The spectral decomposition and S-to-lambda inverse
still use CPU float64; classical CV/GCV/AICc/BIC, branch linking,
scoring and SQLite remain CPU computations. Only the expensive
batched loss calculation is implemented on the GPU. Therefore
**no end-to-end speedup is claimed yet**.

CUDA **does NOT repeatedly compare against CPU** during formal
simulations. The default \`--gpu-verify 0\` disables those comparison
calculations. Before running the formal study, perform **one**
small precision preflight (different run directory):

~~~powershell
git pull --ff-only origin main
python -m pytest tests/test_cuda_simulation.py tests/test_simulation_campaign.py tests/test_weighted_surface_study.py -q
python -m experiments.smoothness_cv.run_simulation_campaign --backend cuda --preset smoke --gpu-verify 2 --gpu-batch-size 2 --run-dir results/smoothness_cv/cuda_precision_preflight_v1
~~~

Then run the **formal GPU-only** campaign, with *NO*
\`--gpu-verify\` flag:

~~~powershell
python -m experiments.smoothness_cv.run_simulation_campaign --backend cuda --preset pilot --seeds 5 --gpu-batch-size 32 --run-dir results/smoothness_cv/campaign_pilot_cuda_v1
python -m experiments.smoothness_cv.analyze_simulation_campaign --run-dir results/smoothness_cv/campaign_pilot_cuda_v1
python -m experiments.smoothness_cv.run_simulation_campaign --backend cuda --preset mega --seeds 100 --orders 2 --grid-points 161 --gpu-batch-size 64 --run-dir results/smoothness_cv/campaign_mega_cuda_v1
~~~

These are separate **manual** foreground commands, not an automatic
combined launch. Smoke/pilot should pass first. The formal runner
has a **single CUDA context**; it does not launch 32 competing GPU
processes. \`--jobs\` only applies to the CPU backend.

**Additional DGP stress factor:** 720 new balanced scenario cells
(Study D): 12 latent shapes (terminal/double jumps, jump/recovery,
transient pulse, chirp, beating sinusoids, plateau, terminal spike,
accelerating oscillations, double sigmoid, stochastic random-walk
level and stochastic random-walk slope) × N {300,600} ×
sigma {.25,.8,1.6} × 5 noise laws (iid, AR1, t5, heteroskedastic,
and 4%-contaminated Gaussian outliers) × seasonal on/off.
\`--preset stress\` runs ONLY these 720; \`--preset mega\` combines
the original 528 A/B/C with all D scenarios = **1,248 cells**.
At 100 seeds/cell, \`mega\` has **124,800 scenario–seed instances**,
each assessed at shared horizons, outer origins and selectors.

**Statistical scope:** study D has rare and stochastic latent
processes but still fits the SAME PLS \(V=I,\mu=0\), so it tests
robustness / misspecification, not a hidden change to the estimator.
Only y is supplied to selectors; tau is withheld until external
scoring. Results are resumable in \`outcomes.sqlite\` and have
a method/code/backend-specific manifest. Preserve negative cases
and evaluate uncertainty by independent seeds **within each DGP
cell**.

**Hardware caveats:** The RTX 4500 Ada kernel benchmark already
showed substantial speedups. That measurement alone is not a
formal-campaign wall-time estimate. The main statistical
postprocessing (including classical selectors and branch linking)
still happens on CPU. Evaluate full pilot throughput before
assuming GPU acceleration of the whole scientific experiment.
Do not mix CUDA and CPU rows in the same manifest/run-dir. Use a
new run-dir if changing the scientific configuration or code revision.
For CUDA out-of-memory errors, use a smaller \`--gpu-batch-size\`
with a **new** run directory or preplan/restart carefully; current
manifests fingerprint the batch size for strict reproducibility.

**Progress:** \`--max-tasks 20\` processes up to 20 remaining
scenario–seed instances. The same command resumes committed tasks
if interrupted. \`--dry-run\` lists the planned factorial cells
without initializing CUDA or writing outputs. The GPU path and
stress design are committed, **not yet run/verified** on the
university machine by the agent.

## Recommended workflow on the university workstation

From the repository root, after \`git pull --ff-only\` and installation
of the existing environment:

**(1) Inspect the design, without running experiments**

~~~bash
python -m experiments.smoothness_cv.run_simulation_campaign --preset extensive --seeds 100 --jobs 32 --dry-run
~~~

**(2) Check correctness (fast automated tests)**

~~~bash
python -m pytest tests/test_weighted_surface_study.py tests/test_simulation_campaign.py -q
~~~

**(3) Execute a smoke run, and inspect the summary**

~~~bash
python -m experiments.smoothness_cv.run_simulation_campaign --preset smoke --jobs 2 --run-dir results/smoothness_cv/campaign_smoke
python -m experiments.smoothness_cv.analyze_simulation_campaign --run-dir results/smoothness_cv/campaign_smoke
~~~

**(4) Pilot with 36 factorial cells × 5 seeds**

~~~bash
python -m experiments.smoothness_cv.run_simulation_campaign --preset pilot --seeds 5 --jobs 16 --run-dir results/smoothness_cv/campaign_pilot_v1
python -m experiments.smoothness_cv.analyze_simulation_campaign --run-dir results/smoothness_cv/campaign_pilot_v1
~~~

**(5) Extensive campaign — all 32 logical processors**

~~~bash
python -m experiments.smoothness_cv.run_simulation_campaign --preset extensive --seeds 100 --jobs 32 --orders 2 --grid-points 161 --run-dir results/smoothness_cv/campaign_extensive_v1
~~~

The run is **foreground** and progress is printed while it is active.
A Ctrl+C / disconnection may stop it. All previously committed
replications remain in \`outcomes.sqlite\`; **run the same command again**
to resume only missing tasks. Do **not** change seed counts, orders,
grid precision, code revision or any other design setting while resuming
into the *same* folder. To run a different experiment, choose a new
\`--run-dir\`.

For a Windows PowerShell session, commands have the **same** syntax
as shown above (one command per line). Large full runs can consume
significant disk space and CPU hours/days; **benchmark your pilot**
rather than relying on an unsupported time estimate.

**Order mismatch follow-up (separate experiment/run directory):**

~~~bash
python -m experiments.smoothness_cv.run_simulation_campaign --preset extensive --seeds 100 --jobs 32 --orders 1,2,3,4 --grid-points 161 --run-dir results/smoothness_cv/campaign_orders_v1
~~~

The above multiplies the candidate estimator comparisons and computational
cost. It is separate because the primary d=2 analysis must remain
interpretable and not be confounded by best-order selection.

**Progressive execution:** \`--max-tasks 20\` processes at most
20 remaining scenario-seed replications, then exits normally. Omit it
when ready to continue. \`--continue-on-error\` records failures
and continues, but failed task keys remain incomplete for later retries.

## CPU versus GPU — measured float32 benchmark (run before GPU migration)

An optional **float32-only** benchmark now compares
the *same spectral PLS forecast-loss calculation* across:

1. A single NumPy CPU process with one BLAS thread.
2. **32 NumPy worker processes**, including subprocess communication.
3. PyTorch CUDA with tensors already resident in GPU memory.
4. PyTorch CUDA **including** CPU-to-GPU transfer and final result download.

**All measured matrix arithmetic is \`float32\`** on CPU and CUDA;
the existing PLS eigendecomposition and \`S -> lambda\` mapping
are prepared once in CPU double precision and then cast to float32
to retain stable spectral and endpoint semantics. These preprocessing
costs are reported separately as preparation time.
CUDA synchronizations prevent asynchronous launch timings from being
mistaken for actual execution times.

From repo root, with a CUDA-enabled PyTorch installed in the same
Python environment (see the official PyTorch install selector):

~~~powershell
python -m pytest tests/test_benchmark_cpu_gpu.py -q
python -m experiments.smoothness_cv.benchmark_cpu_gpu --batch-sizes 1,32,256,1024 --jobs 32 --repeats 7 --warmup 3 --require-cuda
~~~

The **default** \`--kernel gemm\` rewrites the same spectral
three-factor contraction as a matrix multiplication so both NumPy and
CUDA can use optimized GEMM. To also measure the **literal**
\`einsum\` implementation currently used in
\`all_grid_fold_losses\`, run a separate experiment:

~~~powershell
python -m experiments.smoothness_cv.benchmark_cpu_gpu --kernel einsum --batch-sizes 1,32,256,1024 --jobs 32 --repeats 7 --warmup 3 --require-cuda --output results/smoothness_cv/gpu_benchmark_einsum
~~~

Both routes use float32 for the measured arithmetic, and the tests
compare their full \`F_t(S)\` arrays and selected grid minima for
consistency. **GEMM is an algebraically equivalent contraction**, not
a change to the model or validation criterion.

Optional separate run that enables TF32 tensor-core precision
(subject to a numerical accuracy check):

~~~powershell
python -m experiments.smoothness_cv.benchmark_cpu_gpu --batch-sizes 1,32,256,1024 --jobs 32 --repeats 7 --warmup 3 --tf32 --require-cuda --output results/smoothness_cv/gpu_benchmark_tf32
~~~

**Artifacts:** \`results/smoothness_cv/gpu_benchmark/timings_float32.csv\`
and \`hardware.json\`. Columns include the CPU1/CPU32 times,
GPU-resident and transfer-inclusive times, CPU32-to-GPU speedup,
maximum loss differences, and the count of series where
the selected grid-minimum smoothness differs on CUDA.

**Interpretation:**
- For small batches, CPU may win due to kernel-launch and data-transfer
  overhead. GPU may win only after **batching many independent series**.
- Judge deployment using **GPU+transfers vs CPU worker pool**, rather than
  comparing a resident GPU kernel against an unbatched CPU process.
- CPU process-pool timing itself includes interprocess communication;
  the actual scenario-per-worker campaign avoids some of that copying.
  Hence this measures the *dominant loss kernel*, **not** total
  campaign speed. End-to-end GPU integration and another head-to-head
  run are required before changing the default experimental backend.
- A GPU win is acceptable only if computed losses and **selected
  smoothness levels** match the CPU within the predeclared numerical
  tolerance. Near-tied minima are particularly sensitive.
- CUDA not detected: tool reports \`unavailable\`; it does not claim
  GPU timings. Check \`python -c "import torch; print(torch.cuda.is_available())"\`.
- Do not launch the full expensive simulation campaign simultaneously
  with the hardware benchmark; it would corrupt comparative timing.

See the [float32 benchmark source](benchmark_cpu_gpu.py) and
[correctness tests](../../tests/test_benchmark_cpu_gpu.py).
**The benchmarks must be run on the actual university workstation**;
no speedup is asserted by committing the benchmark itself.

## User-run RTX 4500 Ada float32 loss-kernel benchmark (2026-10-09)

The user ran the default \`--kernel gemm\` loss-surface benchmark
with 32 CPU workers and one CUDA GPU. The provided console output
shows the following **preliminary timings**:

| Series per batch | CPU32 | CUDA resident | CUDA + transfers | CPU32 / CUDA + transfers |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0.00043 s | 0.00008 s | 0.00021 s | 2.06× |
| 32 | 0.02068 s | 0.00030 s | 0.00116 s | 17.83× |
| 256 | 0.09485 s | 0.00065 s | 0.00208 s | 45.60× |
| 1024 | 0.05157 s | 0.00295 s | 0.00524 s | 9.83× |

**These are user-provided measurements, not independently reproduced
by this repository-editing agent.** Performance must be interpreted
as **the spectral PLS loss kernel**, NOT full end-to-end Monte Carlo
acceleration. The CPU32 batch-size anomaly (1,024 faster than 256)
warrants repeated runs and full timing distribution, plus fair
scenario-per-worker CPU comparisons. Next validation must inspect
\`results/smoothness_cv/gpu_benchmark/timings_float32.csv\` and
\`hardware.json\`: dtype, CUDA build/device, loss error, and especially
the number of **different selected grid smoothness values**.
Saving that metadata is essential before presenting quantitative
engineering results in an article.

**Potential GPU/CPU parallel implementation (NOT implemented):**
CPU producer processes prepare/generate series and grouped spectral
inputs; a bounded batching queue feeds **one GPU inference process**
that handles the B×M×K float32 contractions; CPU postprocessors
handle global/local minima, branch matching, outer forecast scores
and SQLite transaction writes. Launching 32 independent CUDA
processes to contend for one GPU is not the proposed design.
Benchmark complete tasks before replacing the current CPU campaign.

**Scientific priority remains theoretical/statistical**:
[theoretical charter](../../working_papers/THEORETICAL_CONTRIBUTIONS.md).
For a manuscript-ready implementation paragraph and honest
comparison boundaries, see
[computational implementation note](../../working_papers/COMPUTATIONAL_IMPLEMENTATION.md).

## Hardware: 32 logical processors and RTX Ada GPU

The runner defaults to up to 32 logical CPU processes and explicitly
enforces **one OpenBLAS/MKL/OpenMP thread per process**. Do not set
\`--jobs 32\` together with multithreaded BLAS: oversubscription can
greatly reduce throughput. Using 32 logical threads is possible, but
may **not** be optimal on hardware with hyperthreading; compare
\`--jobs 16\`, \`24\` and \`32\` on the pilot and choose by throughput.

The current PLS spectral computations use NumPy/SciPy **on CPU**;
the RTX 4500 Ada GPU is deliberately not used. Dense eigensolvers for
many small, independent matrices frequently benefit from parallel
CPU workers and cached spectra. Implementing a GPU benchmark could
be a separate numerical research task; using the GPU merely because
it is available is not a sound speed claim.

## Results, interpretation and error bars

Saved *during* the run:
- \`manifest.json\`: immutable fingerprint of the actual scenario grid,
  parameters and Git commit;
- \`outcomes.sqlite\`: one row per scenario/seed/outer origin/order/horizon/
  selector, with complete outcomes;
- \`completed\` table: atomic per-replication checkpoints;
- \`failures\` table: error messages for failed trial keys.

**Only after complete (or with explicit exploratory override):**

~~~bash
python -m experiments.smoothness_cv.analyze_simulation_campaign --run-dir results/smoothness_cv/campaign_extensive_v1
~~~

If some tasks are incomplete, use \`--allow-partial\` for **exploratory**
summaries only. The analyzer produces \`reports/\` with:

- \`scenario_method_summary.csv\`: MSE, RMSE, recovery, smoothness,
  EDF and branch statistics for each DGP and method;
- \`paired_scenario_comparisons.csv\`: difference from
  \`pooled_uniform_all\` on *the same series, horizons and origins*,
  with independent-seed SE/nominal CIs;
- \`effects_by_shape.csv\`, \`effects_by_noise.csv\`,
  \`effects_by_h.csv\`, \`effects_by_sigma.csv\`,
  \`effects_by_d.csv\`, etc.: descriptive factorial summaries;
- \`worst_relative_rmse_cases.csv\` and
  \`best_relative_rmse_cases.csv\`: failure/success stress examples;
- \`oracles_diagnostic_only.csv\`: clearly non-deployable upper-bound
  comparisons; \`replicate_means.csv.gz\` and
  \`paired_replicate_differences.csv.gz\`: auditable independent
  replicate-level aggregates; \`README_RESULTS.md\` for caveats.

**Independent statistical units are seeds, not origins**. The standard
errors are computed after averaging each seed's correlated origins.
No selection of a winning method using those same external test scores
may subsequently be presented as independent performance confirmation.
For final publication, freeze a truly untouched confirmatory seed set.

## Reproduce and visualize a specific case

For a representative failure/winner found in the reports:

~~~bash
python -m experiments.smoothness_cv.inspect_simulation_case --preset pilot --scenario "B__cubic_s__N180__iid__sd0.5__seasonal0" --seed 0 --order 2 --horizon 3 --html
~~~

This exports the TRUE latent trend, seasonal/noise components,
method-specific weighted F matrices, individual branches, and a
case overview HTML (Plotly extra required). We can reproduce an
interesting scenario without storing every F array in the giant DB.

## Scientific limitations and release gates

1. The new simulated study is **not executed** just because code is committed.
2. Classical CV/GCV/AICc/BIC and fixed-S comparisons are fully
   paired using identical fitting windows; the oracle selectors are
   unavailable in real forecasting.
3. The current **global minimum and local minima are based on the
   candidate S grid**, not a certified complete root search.
   Before the final experimental freeze, run numerical sensitivity
   at e.g. 161/321/501 points; distinguish algorithm error from
   statistical gains. Pooled numerical refinement is separately
   supported in the interactive prototype.
4. Plot/calibrate experiment A against the original article's **raw**
   smoothness \(S_G\), not only the normalized S. Its 2^4 design
   is a source-inspired reproduction plus a novel forecasting
   extension, **not** two original forecast experiments.
5. The analyzer's CIs are nominal Monte Carlo CIs; for many scenarios/
   methods/horizons simultaneously, avoid interpreting unadjusted
   95% intervals as strong multiple-testing evidence.
6. The final benchmark needs **independently confirmed** winners:
   freeze methods/weights before untouched confirmation. Preserve
   negative cases and methods that lose to fixed smoothness.
7. The run directory should be excluded from regular Git commits
   due to size. Commit lightweight manifests/reports/checkpoint
   summaries only deliberately; version large databases elsewhere.

## Sharing research evidence through GitHub

The work station's SQLite database may become many gigabytes. **Do not**
blindly stage the whole campaign output folder. To make the results
available to collaborators for analysis, push the lightweight
\`manifest.json\` and \`reports/\` summary CSV/README outputs rather
than the raw SQLite file. For example after complete aggregation:

~~~bash
git add results/smoothness_cv/campaign_extensive_v1/manifest.json
git add results/smoothness_cv/campaign_extensive_v1/reports/
git status --short
git commit -m "results: frozen weighted-F large simulation summaries"
git push
~~~

Before committing, check \`git status\` and file sizes: certain
replicate-level compressed audit trails can themselves become large.
If necessary, leave those two \`*.csv.gz\` trails outside Git and
commit only:
\`scenario_method_summary.csv\`,
\`paired_scenario_comparisons.csv\`,
\`effects_by_*.csv\`,
\`worst_relative_rmse_cases.csv\`,
\`best_relative_rmse_cases.csv\`,
\`task_timing.csv\`, and \`README_RESULTS.md\`.
Keep the full database available locally and recoverable from the
frozen manifest/seeds/code. Git LFS or external institutional storage
is more appropriate for unusually large raw artifacts.

**Do not commit an incomplete or still-changing simulation summary
as though it were a completed frozen run.** Partial reports are only
exploratory.

## Module index

- \`simulation_dgps.py\`: source paper and extended scenario generators.
- \`simulation_evaluation.py\`: one independent paired replication.
- \`run_simulation_campaign.py\`: resumable process-pool SQLite runner.
- \`analyze_simulation_campaign.py\`: factor and paired-seed reports.
- \`inspect_simulation_case.py\`: regenerate case-level curves and branches.
- \`weighted_surface_study.py\`: shared pooled/branch algorithm.
- \`tests/test_simulation_campaign.py\`: inexpensive correctness tests.
- [Cross-paper statistical protocol](../../working_papers/SIMULATION_EVALUATION_PROTOCOL.md).
