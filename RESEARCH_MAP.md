# Research map — active theory-first program

**Updated 2026-10-09.** Exactly THREE independently publishable
working papers are active, but use shared mathematical and numerical
building blocks. For future agents, begin at [AGENTS.md](AGENTS.md),
[AI_HANDOFF.md](AI_HANDOFF.md) and
[THEORETICAL_CONTRIBUTIONS.md](working_papers/THEORETICAL_CONTRIBUTIONS.md).

## 1. Smoothness Cross Validation

[Paper folder](working_papers/Working%20Paper%20-%20Smoothness%20Cross%20Validation/)
· [Streamlit](apps/pooled_forecast_cv.py)
· [Paper-specific agent handoff](working_papers/Working%20Paper%20-%20Smoothness%20Cross%20Validation/AI_HANDOFF.md).

**Mathematical question:** given fixed order d, fit width L, h-step
extrapolator, and a prespecified method m for weighting completed
historical rolling-origin forecast-loss **functions**, choose the
global minimizer of latest weighted F(S). Original pooled objective
is the all-origin uniform special case. Ask how horizon-specific
forecast selection compares with latent recovery and classical
CV/GCV/AICc/BIC. Time-weighted extensions are prospective.

**Do NOT track minima. Do NOT average individual minimizing S's.**

## 2. Dynamic Branch Selection

[Paper folder](working_papers/Working%20Paper%20-%20Dynamic%20Branch%20Selection/)
· [Streamlit](apps/dynamic_branch_cv.py)
· [Paper-specific agent handoff](working_papers/Working%20Paper%20-%20Dynamic%20Branch%20Selection/AI_HANDOFF.md).

**Mathematical question:** for each fixed m,d,L,h, can local-minimum
histories of the **same weighted historical F** provide useful temporal
information beyond its latest global minimizer? Link extrema across
adjacent completed historical surfaces using one-to-one
distance-limited matching; select a branch using historical evidence;
only **after tracking** compute operational S (e.g. mean of last three
branch S minima).

No compulsory Val2 in the **current** algorithm. **Old CP04–CP08,
apps/smoothness_lab.py and apps/smoothness_lab_advanced.py use earlier
Val1/Val2 methods and must remain labelled legacy.**

## 3. Numerical Methods

[Paper folder](working_papers/Working%20Paper%20-%20Numerical%20Methods/)
· [Streamlit](apps/numerical_methods.py)
· [Paper-specific agent handoff](working_papers/Working%20Paper%20-%20Numerical%20Methods/AI_HANDOFF.md).

**Mathematical question:** derivative structure and robust numerical
recovery of minima, stationary roots and exact endpoints of
one fixed weighted or unweighted F(S). Adaptive root bracketing,
Brent refinement, rational/Sturm methods only under restricted finite
instance assumptions. No branch tracking required. Previous
dense-reference matches do NOT imply certified complete roots.

## Shared research contracts

[Weighted surface formulation](working_papers/WEIGHTED_SURFACE_PROTOCOL.md)
· [Simulation and evaluation](working_papers/SIMULATION_EVALUATION_PROTOCOL.md)
· [Computational implementation and preliminary GPU evidence](working_papers/COMPUTATIONAL_IMPLEMENTATION.md)
· [Apps entrypoints](apps/README.md).

**Priority:** theoretical claims and literature boundaries →
correct chronology/causal validation → interpretable simulation →
interface documentation → computational speedups. PLS spectral EDF,
Guerrero smoothness, simple normalization, TSCV and GPU batching
are established tools, not individual originality claims.

## Evidence and operations

The original source-inspired 2^4 simulation, the prospective 528
scenario-cell × 100 seed large design, and current batched float32
CPU/GPU loss benchmarks are defined in
[CAMPAIGN_README.md](experiments/smoothness_cv/CAMPAIGN_README.md).
The user-provided RTX 4500 Ada benchmark times show impressive
loss-kernel acceleration but **not end-to-end Monte Carlo speedup**,
and numeric selection agreement needs verification. New extensive
simulations are prepared, NOT represented as already executed.

Every paper has its own independent research claims and manuscript.
Shared src/, apps/, experiments/, data and results do NOT merge their
publication contributions. Large simulations, regenerated figures
and paper builds are manual only. Historical checkpoints must not be
silently rewritten to fit the new methods.
