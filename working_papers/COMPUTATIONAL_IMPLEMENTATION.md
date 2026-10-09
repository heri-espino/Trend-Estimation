# Computational implementation — supporting evidence, NOT primary novelty

**Status 2026-10-09: preliminary user-reported GPU kernel benchmark.**
Read [theory-first charter](THEORETICAL_CONTRIBUTIONS.md) before
including any hardware result in a manuscript.
This note is a **draft for a short implementation or reproducibility
subsection**, not an independently verified final benchmark.

## Why the algebra can be batched

For fixed difference order d and window length L,
\[
Q=D_d^\top D_d=U\,\mathrm{diag}(\delta_j)U^\top,\qquad
H_\lambda=U\,\mathrm{diag}(\alpha_j(\lambda))U^\top,
\quad\alpha_j=(1+\lambda\delta_j)^{-1}.
\]
At a historical origin, denote the spectral projection
\(c_t=U^\top y_{t-L+1:t}\) and precomputed continuation
\(B=G_{d,h}U\). Then
\[
\widehat z_{t,h}(S)=B\big(\alpha(S)\odot c_t\big).
\]
These are ordinary batched matrix products/contractions. The same
fixed \((L,d)\) spectral basis and candidate S-to-lambda filter
can be reused across many origins and simulated series.
For batches of B replicated series, M completed origins and K
candidate smoothness values, the loss tensor has shape
\(B\times M\times K\):
\[
\mathcal L_{b,m,k}
=\frac1h\sum_{j=1}^h
\left(y_{b,t_m+j}
-\big[G_{d,h}H(S_k)x_{b,t_m}\big]_j\right)^2.
\]
Weights over completed origins then produce method-specific
\(F^{(m,d,L,h)}\), as prescribed by **Paper 1**; the *same*
weighted surfaces enter **Paper 2's** branch-minimum detection.
The GPU does not change either statistical objective.

**What is currently on CPU:** the NumPy/SciPy spectral
eigendecomposition, S-to-lambda inversion, full simulation framework,
root refinements and branch matching. **What is benchmarked on CUDA:**
batched \`float32\` matrix contraction for the predictive losses.
Eigenvalues and normalized-smoothness mapping are preprocessed in
\`float64\` before casting to \`float32\` for measured arithmetic.
That is not full end-to-end float32 or CUDA implementation.

## Preliminary measured timings (user-run, not independently audited)

Environment described by the user: a university Windows workstation,
32 logical CPU processors and NVIDIA RTX 4500 Ada. Executed:

~~~powershell
python -m experiments.smoothness_cv.benchmark_cpu_gpu --batch-sizes 1,32,256,1024 --jobs 32 --repeats 7 --warmup 3 --require-cuda
~~~

Reported median times for a **single loss kernel**:

| Batch | CPU32 (seconds) | CUDA resident (seconds) | CUDA with transfers (seconds) | GPU with transfers speedup over CPU32 |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0.00043 | 0.00008 | 0.00021 | 2.06× |
| 32 | 0.02068 | 0.00030 | 0.00116 | 17.83× |
| 256 | 0.09485 | 0.00065 | 0.00208 | 45.60× |
| 1,024 | 0.05157 | 0.00295 | 0.00524 | 9.83× |

**Caveats mandatory in all presentations:**

1. This is **not the full Monte Carlo study**, solver/minimum search,
   SQLite work, Python simulation loop, or end-to-end wall-time.
2. Comparison CPU32 process pool includes process communication,
   which may differ from scenario-per-worker CPU implementation.
3. The **CPU32 batch 1,024 time being lower than batch 256**
   deserves repeated investigation. Speedups are not monotonically
   increasing, so quote measured conditions rather than claiming
   asymptotic advantage or 45.60× in general.
4. GPU+transfer timings include transfer in the benchmark, but
   preparation/eigendecomposition and full input-generation overhead
   are separate. For the final engineering choice, time complete runs.
5. We have not inspected the workstation-generated
   \`timings_float32.csv\` for the accuracy fields
   \`max_absolute_loss_error\`, \`max_scaled_loss_error\`
   and \`different_selected_s_count\`; do so **before** accepting
   \`float32\` as a numerically equivalent selection method.
6. Hardware/driver/library versions from
   \`results/smoothness_cv/gpu_benchmark/hardware.json\` have
   not been independently reviewed. Save these metadata, new
   repeated timings, seed, K/L/h and \`--kernel\` variant.
7. "GPU parallelism" means independent series/origins/S points can
   be **batched in GPU matrix operations**. Do **not** assume
   32 distinct CUDA workers will outperform one larger-batch GPU
   worker on a single physical device.

## Possible scalable architecture (NOT YET implemented)

- CPU producer pool: independent DGP generation, numerical/spectral
  preprocessing, historical windows and validation masks.
- A bounded queue and one **batching GPU consumer** (or a tuned
  small number of streams) send batches of compatible
  \((L,d,h,K)\) cases through the CUDA forecast-loss kernel.
- CPU postprocessor: weighted aggregation of F, refinement of
  local stationary candidates, branch matching/decision, classical
  CV/GCV/AICc/BIC selectors, external scoring and SQLite output.
- Independent test harness: compare CPU reference and GPU exactly
  for fold-matrices, weighted F, selected S, branch identities and
  external score; near-degenerate minima require additional
  double-precision reference diagnostics.
- Benchmark throughput, GPU peak memory, CPU/GPU wait time and
  total elapsed wall-time for equivalent **complete** scenario
  workloads; retain a pure CPU fallback and objective invariance.

The user prefers using the university workstation's cores and GPU,
but **only if the end-to-end integration is demonstrably correct and
faster**. Before implementing CUDA in the main campaign, freeze
the statistical algorithm so computational variations do not
silently become methodological variations.

## Appropriate publication placement

- **Paper 1:** one reproducibility or computational-implementation
  subsection after the mathematical estimator. Describe reuse
  of spectral factors and batched forecast losses; supply verified
  hardware/timings in an appendix or supplement. Do not use hardware
  to justify novelty of the CV rule.
- **Paper 2:** briefly say the same forecast-loss surfaces can
  be batched; note that root detection and branch matching are
  separate costs and might dominate after GPU acceleration.
- **Paper 3:** discuss complexity of spectral evaluation and
  numerical minima detection separately; GPU contraction is
  an optional empirical implementation comparison, not a new
  theoretical solver, unless a genuinely novel algorithm and
  rigorous complexity analysis are added.

### Manuscript-ready paragraph — DRAFT, pending verification

> The finite-difference penalized least-squares smoother admits a
> reusable spectral representation at fixed window length and
> differencing order. The horizon-specific forecast-loss functions
> can consequently be evaluated by batching spectral projections,
> diagonal shrinkage, and continuation across candidate smoothing
> levels and historical origins. We implemented a float32 CUDA
> evaluation of this loss kernel and compared it with NumPy CPU
> implementations at several batch sizes. These experiments assess
> computational scalability; they leave the smoothing family, the
> cross-validation criterion, and the branch-selection rules
> unchanged. The reported kernel times should not be interpreted
> as end-to-end speedups of the Monte Carlo experiments.

**Do not add a numeric speedup to this draft paragraph until the
float32 selected-S agreement, full hardware metadata and repeated
benchmark are checked.**

## Reproduce

~~~powershell
python -m pytest tests/test_benchmark_cpu_gpu.py -q
python -m experiments.smoothness_cv.benchmark_cpu_gpu --kernel gemm --batch-sizes 1,32,256,1024 --jobs 32 --repeats 7 --warmup 3 --require-cuda
python -m experiments.smoothness_cv.benchmark_cpu_gpu --kernel einsum --batch-sizes 1,32,256,1024 --jobs 32 --repeats 7 --warmup 3 --require-cuda --output results/smoothness_cv/gpu_benchmark_einsum
~~~

Do not run the heavy CPU Monte Carlo campaign at the same time as
a hardware benchmark; resource contention would bias the timings.
