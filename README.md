# Trend Estimation

Research software for spectral finite-difference penalized least-squares
(PLS) trend estimation, horizon-matched forecast validation, numerical
smoothness optimization and temporal local-minimum tracking.

**Research priority: theoretical/statistical contributions first.**
Apps, large CPU simulations and the user's successful CUDA loss-kernel
benchmark are supporting computational infrastructure—not independently
new mathematical discoveries.

**For agents and collaborators: read [AGENTS.md](AGENTS.md),
[AI_HANDOFF.md](AI_HANDOFF.md), and
[THEORETICAL_CONTRIBUTIONS.md](working_papers/THEORETICAL_CONTRIBUTIONS.md)
before editing code or paper drafts.** These are the canonical current
research protocols; older experiment snapshots may use *different*
validation and branch-selection rules.

## Three independent working papers

| Paper | Working folder | Canonical Streamlit app | Primary scientific question |
| --- | --- | --- | --- |
| **1: Smoothness Cross Validation** | [Working Paper - Smoothness Cross Validation](working_papers/Working%20Paper%20-%20Smoothness%20Cross%20Validation/) | [pooled_forecast_cv.py](apps/pooled_forecast_cv.py) | Does minimizing a weighted average of **completed horizon-h historical forecast-loss curves** select useful trend smoothness? |
| **2: Dynamic Branch Selection** | [Working Paper - Dynamic Branch Selection](working_papers/Working%20Paper%20-%20Dynamic%20Branch%20Selection/) | [dynamic_branch_cv.py](apps/dynamic_branch_cv.py) | Do **histories of method-specific local minima** of the same weighted F add predictive information beyond its current global minimum? |
| **3: Numerical Methods** | [Working Paper - Numerical Methods](working_papers/Working%20Paper%20-%20Numerical%20Methods/) | [numerical_methods.py](apps/numerical_methods.py) | How reliably can an algorithm recover stationary points and endpoints of **one structured F(S)** using analytic derivatives, adaptive search and small-instance exact methods? |

They share statistical and numerical tools but retain **separate**
scientific questions, manuscripts, hypotheses and evidence.

## Exact shared setup

For \(1\le d<L\), \(h\ge1\), \(Q_d=D_d^\top D_d\),
\[
H_\lambda=(I+\lambda Q_d)^{-1}
=U\,\mathrm{diag}((1+\lambda\delta_j)^{-1})U^\top,\quad
S(\lambda)=\frac{L-\operatorname{tr}H_\lambda}{L-d}\in[0,1].
\]
The **matrix H** is spectral; **S is a scalar** index obtained from
the trace/EDF. This is classical PLS + a convenient normalized
Guerrero-type index, **not a new smoothing matrix**.
At \(S=1\), the exact limit is the polynomial null-space projection.

At historical origin \(t\), use the last \(L\) observations to forecast
the next **\(h\)** using the fixed continuation \(G_{d,h}\), then compute
\[
\ell_t(S)=\frac1h
\|y_{t+1:t+h}-G_{d,h}H(S)y_{t-L+1:t}\|^2.
\]
A completed historical validation block can contribute to selection
at \(T\) only if \(t+h\le T\).

**Paper 1** combines these *functions* with predeclared recency
weights \(m\), then minimizes the latest completed weighted F globally.
**Paper 2** tracks its local minima across historical updates and
converts the chosen branch to an operational S *after* tracking
(initially by mean of its last three S values). No extra Val2 is
required for either CURRENT method. Both refit on the last L
observations and evaluate forecasts on an untouched outer future.
**Paper 3** investigates numerical stationary-root discovery for a
single F (not branch persistence).

For full mathematics and non-overclaim rules, use
[THEORETICAL_CONTRIBUTIONS.md](working_papers/THEORETICAL_CONTRIBUTIONS.md)
and [WEIGHTED_SURFACE_PROTOCOL.md](working_papers/WEIGHTED_SURFACE_PROTOCOL.md).

## Streamlit research applications

From the repo root, after installation:

~~~powershell
streamlit run apps/pooled_forecast_cv.py
streamlit run apps/dynamic_branch_cv.py
streamlit run apps/numerical_methods.py
~~~

Launch **one app at a time** or use different Streamlit ports.
They provide synthetic trends/noise, Yahoo Finance (optional),
CSV import, fold/weighted-loss visualization, H/S/EDF explanations,
forecast displays and reproducible exports, as appropriate to
their respective scientific problem.

**Do not use the old Val1/Val2 apps as the current dynamic paper:**
\`apps/smoothness_lab.py\` and \`apps/smoothness_lab_advanced.py\`
are **legacy** retained for historical research reproduction.
See [apps/README.md](apps/README.md) for exact features and boundaries.

## Formal CUDA campaigns (new)

\`experiments/smoothness_cv/run_simulation_campaign.py --backend cuda\`
now computes *real* horizon-h rolling-origin forecast losses in
float32 batched on one GPU and passes them to the same Paper 1/Paper 2
pooled/branch selection and classical benchmarking pipeline.
Eigenanalysis, classical criteria, branch matching and outer scoring
remain on CPU. The formal default is **no repeated CPU-vs-GPU
benchmark/comparison** (\`--gpu-verify 0\`); perform one initial
precision smoke check with explicit \`--gpu-verify 2\`.

A new \`stress\` DGP includes **720** balanced difficult cells (jumps,
transient shocks, frequency changes, stochastic trends, contaminated
noise, seasonal interactions). The \`mega\` preset includes all
1,248 cells, or **124,800 scenario–seed runs at 100 seeds**.
These are **new implemented experiments, not completed results**.
See [formal CUDA commands](experiments/smoothness_cv/CAMPAIGN_README.md).
The numerical paper's adaptive/exact root solvers are still CPU.

## Simulation campaign and benchmarks

The [common simulation protocol](working_papers/SIMULATION_EVALUATION_PROTOCOL.md)
includes a source-faithful **2^4** Cortés-Toto full-sample reference
study, a broader polynomial/nonpolynomial trend-shape and noise
experiment, and a regime-change experiment specifically for branch
tracking. The prospective extensive preset includes **528 factorial
cells**, with **100 seeds per cell = 52,800 scenario-seed instances**,
not 52,800 globally independent statistical observations.

Measure genuinely unseen h-step observed forecast MSE, known latent
trend recovery and future latent-trend MSE, S, EDF, timing and
numerical failures. CV/GCV/AICc/BIC and fixed ad-hoc S are selectors
to compare under **identical outer forecasts**; oracle smoothness
uses known latent trend for research diagnostics only.
**The extensive new campaign has not yet been executed and confirmed.**
Historical CP01–CP08 outcomes refer to earlier designs and remain
frozen.

[CAMPAIGN_README.md](experiments/smoothness_cv/CAMPAIGN_README.md)
documents 32 logical CPU processes, persistent SQLite results,
resume, independent-seed aggregated reporting, and a float32
PyTorch CUDA **loss-kernel** benchmark. User-provided RTX 4500 Ada
timings show significant GPU improvements for batched matrix
contractions, but are **not an end-to-end simulation speedup** or
the central theoretical contribution. See detailed caveats in
[THEORETICAL_CONTRIBUTIONS.md](working_papers/THEORETICAL_CONTRIBUTIONS.md).

## Install (Windows / Conda)

~~~powershell
conda env create -f environment.yml
conda activate trend-estimation
python -m pip install -e ".[dev,docs,dashboard,finance,symbolic]"
python -m pytest
~~~

**Conda-first CUDA option:** where a CUDA-enabled PyTorch build is
available on the configured Conda channels, install it through the
environment's package manager. The optional CUDA benchmark needs
\`torch.cuda.is_available()==True\`; Streamlit and core scientific
research do **not** depend on GPU PyTorch.

~~~powershell
python -m experiments.smoothness_cv.benchmark_cpu_gpu --batch-sizes 1,32,256,1024 --jobs 32 --repeats 7 --warmup 3 --require-cuda
~~~

Manual long-running experiment examples:

~~~powershell
python -m experiments.smoothness_cv.run_simulation_campaign --preset smoke --jobs 2
python -m experiments.smoothness_cv.run_simulation_campaign --preset extensive --seeds 100 --jobs 32 --orders 2 --grid-points 161
~~~

**Lightweight tests/CI automated; large experiments, manuscript PDF
builds and derived figures manual only.** Never describe unexecuted
workflows or draft theoretical propositions as published results.

## Shared repository areas

- \`src/trend_estimation/\`: reusable PLS, spectra, forecast operators,
  derivative and numerical selection code.
- \`experiments/\`: numerical and statistical experiments including
  heavyweight reproducible campaign runners.
- \`results/\`: tracked lightweight frozen evidence / local large results
  and manifests; don't push huge SQLite archives to Git.
- \`apps/\`: **three current paper-specific interfaces**, legacy
  interfaces explicitly separated.
- \`working_papers/\`: three independent manuscripts, canonical
  research protocols, literature positions and scientific notes.
- \`data/\`, \`literature/\`, \`tests/\`, \`docs/\`, \`ideas/\`:
  data, references, regression checks, documentation and inactive ideas.
