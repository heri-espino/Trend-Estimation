# Theory-first research charter — three independent working papers

**Updated 2026-10-09. This is the primary scientific contract for new agents.**
The research prioritizes defensible *mathematical/statistical* contributions.
Apps, large simulations, CPU parallelism and the GPU are supporting
implementation/evidence, **not independently novel theory**. Never rewrite
legacy checkpoints as new-method evidence.

## Model and notation (common, not newly discovered)

For observed \(y_{1:T}\), fit width \(L>d\ge1\), declared future
horizon \(h\ge1\), and consecutive order-d difference matrix \(D_d\),
use pure, zero-drift PLS with \(V=I\) and \(\mu=0\):
\[
\widehat\tau_\lambda=(I_L+\lambda Q_d)^{-1}x=H_\lambda x,\qquad
Q_d=D_d^\top D_d=U\,\mathrm{diag}(\delta_j)U^\top.
\]
\(Q_d\succeq0\), \(\mathrm{rank}(Q_d)=L-d\), and exactly \(d\) eigenvalues
are zero. \(I+\lambda Q_d\) and \(H_\lambda\) are positive definite for
*finite* \(\lambda\ge0\). The limiting \(H_\infty=U_0U_0^\top\) is
instead a rank-d projection onto the discrete polynomials of degree
at most \(d-1\). \(H_0=I\).

The established **spectral** representation is
\[
H_\lambda
=U\,\mathrm{diag}\big((1+\lambda\delta_j)^{-1}\big)U^\top,\quad
\mathrm{edf}(\lambda)=\mathrm{tr}H_\lambda
=\sum_{j=1}^L(1+\lambda\delta_j)^{-1}.
\]
**\(U\mathrm{diag}(\cdot)U^\top\) computes matrix \(H\); it is not scalar
smoothness \(S\).** Normalize the established Guerrero trace index:
\[
S(\lambda)=\frac{L-\mathrm{edf}(\lambda)}{L-d}\in[0,1],
\quad S_G=1-\frac{\mathrm{edf}}L=\frac{L-d}{L}S.
\]
The rescaling is useful and monotone, but **not a new smoothing family,
an original eigenvalue identity, or a new historical discovery**.
For finite \(\lambda>0\),
\[
\frac{dS}{d\lambda}
=\frac1{L-d}\sum_{\delta_j>0}
\frac{\delta_j}{(1+\lambda\delta_j)^2}>0.
\]
Hence the finite \(\lambda\) / interior S mapping is one-to-one at
fixed \((L,d)\); the endpoint \(S=1\) means \(\lambda=\infty\) and must
be evaluated exactly.

The forecast extrapolator \(G_{d,h}\), not \(H\) alone, turns the last
estimated trend into **h-step predictions**, using zero future d-th
differences (constant for d=1, linear d=2, quadratic d=3, cubic d=4).
For historical completed origin \(t\), define
\[
x_t=y_{t-L+1:t},\quad z_t=y_{t+1:t+h},\quad
\ell_t^{(d,L,h)}(S)=h^{-1}\|z_t-G_{d,h}H(S)x_t\|_2^2.
\]
A loss can be used at operational origin \(T\) **only when \(t+h\le T\)**.
Refit on \(y_{T-L+1:T}\) *after selecting S* and evaluate the future
\(y_{T+1:T+h}\) only as untouched external test.
Overlapping rolling-origin losses are dependent.

### Classical facts versus research questions

- Classical: PLS and forecast continuation, orthogonal diagonalization,
  trace/EDF, Guerrero smoothness, rolling-origin CV, weighted averages,
  \(H'_\lambda=-H_\lambda QH_\lambda\) and
  \(H_\lambda^{(n)}=(-1)^n n!H_\lambda(QH_\lambda)^n\);
  analytic first/second loss derivatives by the chain rule.
- Derivable and prove explicitly under stated assumptions:
  \(S\)'s endpoint mapping and strict interior monotonicity, continuity
  of the forecast loss on compact \([0,1]\), existence (not uniqueness)
  of at least one global minimizer. A monotonically reparameterized
  *exact* objective has identical trend fits and optimal predictions.
- **Not proved**: convexity/unimodality of \(F\), uniqueness of S*, an
  optimizer's statistical consistency, complete numerical recovery
  of arbitrary minima, and superior forecasting of any proposed rule.
- Originality of any proposed *combination* must be checked against
  closest smoothing, GCV and forecasting CV literature. An integration
  alone is not proof of novelty.

## Paper 1: horizon-matched weighted pooled forecast loss

**Decision/problem formulation** (fixed \(m,d,L,h\)):
\[
F_r^{(m,d,L,h)}(S)=
\frac{\sum_{q\in I_m(r)}w^{(m)}_{r,q}\ell_{t_q}^{(d,L,h)}(S)}
{\sum_{q\in I_m(r)}w^{(m)}_{r,q}},\qquad q\le r,\quad w_{r,q}\ge0,
\]
with nonzero total weight, and
\[
\boxed{\widehat S_T^{\rm pooled}
\in\arg\min_{S\in[0,1]}F_M^{(m,d,L,h)}(S).}
\]
**Average entire functions F first, then minimize. NOT average
fold-wise minimizers and not follow minima between origins.**
Weighting methods \(m\): all-origin uniform (the historical baseline),
last-K uniform, recency-linear, recency-exponential. The paper asks
when horizon-matched forecast-directed smoothness differs from
reconstruction-directed smoothing, how weights interact with
nonstationarity, and what is established mathematically and empirically.
Recency weighting is a prospective extension, not previously frozen CP03
results. No universal superiority claim.

## Paper 2: temporal local-minimum branches of precisely the SAME F

**Fix \(m,d,L,h\) first** and construct \(F_1,\ldots,F_M\) with
**completed** historical losses only. For each \(r\), detect admissible
interior and endpoint local minima
\(\mathcal M_r=\mathrm{LocalMin}(F_r)\). Link minima from *adjacent*
surfaces one-to-one when their normalized S positions are within a
predeclared tracking radius \(\epsilon\). A new unmatched local minimum
starts a branch; lost minima retire. Identity can be ambiguous at
crossings, bifurcations and ties. Multiple minima/branches are possible,
**not guaranteed for every m,d or simulated series**.

Track
\[
V_j=\{(r,t_r,S^*_{j,r},F_r(S^*_{j,r}))\}_{r\in\mathcal T_j}.
\]
Choose active branch \(\widehat j=\psi(V,\text{completed past F})\),
then map to operational S using \(\phi\), initially **the mean of
the last three S minima of the chosen branch** (fewer for young
branches), and refit before h-step forecasting:
\[
\boxed{\widehat S_T^{\rm track}=\phi(V_{\widehat j}).}
\]
**Weight F before finding minima. Mean S after tracking as a decision
rule; never feed an average of prior S back into F.**
Branch scoring based on already-observed weighted F is a heuristic
requiring an **external test**. No compulsory internal Val2.
Historical CP04–CP08 *did* use a different Val1/Val2 transformed-S
approach and cannot validate this revised method.

Theory agenda: investigate how branch existence and stability depend
on curvature and chronological perturbations to F, when an implicit
function/continuation result is applicable under *simple stationary
point plus positive curvature* assumptions, and what happens at
folds/collisions/endpoint minima. These are **proposed research
directions**, not proved general theorems.

A clean ablation compares tracked S with global argmin of **the very
same weighted F**, same \(m,d,L,h\), same outer origins/forecasts.

## Paper 3: numerical minima of a single fixed forecast F(S)

Study numerical recovery, differentiability/conditioning,
stationary points, endpoint limits, derivative-root bracketing, Brent,
and rational-polynomial/Sturm **for restricted small instances**.
The numerical paper need not perform branch correspondence over time.
A dense grid or adaptive root sampler is not an unrestricted proof
of finding *all* stationary roots. Preserve published-scope distinction:
numerical search/computational complexity is a possible theoretical
contribution when justified; plain GPU matrix batching alone is not.

## Theory + reproducible evidence workflow

1. State a precise assumption/theorem/conjecture or decision criterion.
2. Differentiate rigorously what is known from what this project adds,
   supported by explicit source references and citation audit.
3. Prove a proposition or find counterexamples; record negative and
   degenerate cases rather than selecting favorable plots.
4. Test implementation invariants (spectral endpoints, weights, chronology,
   derivative finite-difference checks, branch matches, no outer leakage).
5. Use matched simulations: source-inspired 2^4 factorial, polynomial
   (linear/quadratic/cubic/quartic) and nonpolynomial trends, regimes/noise,
   outer forecast MSE, past/future latent-trend MSE, S/EDF, fixed S and
   CV/GCV/AICc/BIC, oracle-only diagnostic targets.
6. Analyze independent *seed-level* paired differences; outer origins and
   multiple horizons within one generated series are dependent observations.
7. Only after methodological evidence, update the LaTeX manuscripts and
   clearly label what has actually been proved or run.

Reference protocols:
[WEIGHTED_SURFACE_PROTOCOL.md](WEIGHTED_SURFACE_PROTOCOL.md) and
[SIMULATION_EVALUATION_PROTOCOL.md](SIMULATION_EVALUATION_PROTOCOL.md).
Simulation implementation and frozen-result rules:
[CAMPAIGN_README.md](../experiments/smoothness_cv/CAMPAIGN_README.md).

## Performance and GPU — engineering evidence, not central theorem

A user-run **float32 spectral PLS loss-kernel** benchmark on
2026-10-09 (GPU device described as RTX 4500 Ada, Windows, 32 CPU
workers) reported CUDA **including transfers** versus a 32-process
NumPy pool:

| Batch (series) | CPU32 seconds | CUDA+transfer seconds | CPU32/CUDA |
| --: | --: | --: | --: |
| 1 | 0.00043 | 0.00021 | 2.06x |
| 32 | 0.02068 | 0.00116 | 17.83x |
| 256 | 0.09485 | 0.00208 | 45.60x |
| 1024 | 0.05157 | 0.00524 | 9.83x |

These are **self-reported timings** from
\`python -m experiments.smoothness_cv.benchmark_cpu_gpu\`,
**not independently reproduced by the agent**, and not yet checked
against saved error/selected-S columns in
\`results/smoothness_cv/gpu_benchmark/timings_float32.csv\`.
The nonmonotone CPU32 timing from 256 to 1024 suggests scheduling,
cache, noise, or measurement effects requiring repeated confirmation.
The figures measure the **loss kernel**, *not* the entire
Monte Carlo campaign, full optimization, or proven end-to-end speedup.
Use a short *Computational implementation* paragraph/table only after
saving hardware metadata, deterministic timing repeats and verifying
numerical selection equivalence. Do not cite 45.60x as a global
algorithm speedup.

Future architecture (not implemented): one or a small number of
GPU-batching workers consuming tasks prepared by CPU producers; avoid
32 independent GPU processes contending for one device. Select batch
size and CPU/GPU allocation only from representative end-to-end tests.
Float32 **kernel arithmetic** does not imply the existing eigenvalue
preparation/S-to-lambda inversion is also float32. This distinction
must remain explicit.

## Interfaces and historical separation

One **canonical Streamlit app per working paper** is required:
- \`apps/pooled_forecast_cv.py\`: Paper 1, weighted F aggregation,
  global minimization; no branches.
- \`apps/dynamic_branch_cv.py\`: Paper 2, local minima of the *same
  weighted F*, tracked branches and after-tracking decision; no Val2.
- \`apps/numerical_methods.py\`: Paper 3, one F, derivatives, local
  minima, endpoints, conditioning and numerical method comparisons.

**Historical** \`apps/smoothness_lab.py\` and
\`apps/smoothness_lab_advanced.py\` use old Val1/Val2 logic and must be
explicitly labelled legacy and not imported by the new dynamic launcher.
Apps are an experimental user-facing layer, **not numerical sources of
truth**; call shared library functions. Never pass outer targets to a
selector or describe an all-series retrospective fit as a forecast.

This charter is the priority when older READMEs/legacy comments
contradict current protocols. Correct misleading entrypoints and
outdated documentation, preserve historical code/results.
