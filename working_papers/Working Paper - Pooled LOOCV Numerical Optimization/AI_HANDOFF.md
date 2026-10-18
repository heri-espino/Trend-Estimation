# Independent paper — agent handoff (2026-10-18)

## Read order

1. This README.md.
2. notes/RESEARCH_NOTEBOOK.md.
3. notes/PROOF_LEDGER.md.
4. notes/SIMULATION_ATLAS.md.
5. notes/LITERATURE_POSITIONING.md.
6. notes/DECISIONS.md.
7. experiments/pooled_loocv_smoothness/README.md and code.
8. Existing repository AGENTS.md and AI_HANDOFF.md for shared operational rules.

## Non-negotiable identity

**This is NOT the existing forecast-oriented Numerical Methods paper.** It deliberately changes the scientific object to classical *observed-series LOOCV for PLS trend reconstruction*. No future-block loss, no h, no rolling forecast validation, no branches or regime forecasting.

Primary output: full pooled loss curve; roots/local minima and endpoints; verified lowest candidate; computation, accuracy and failure analysis. Treat R=1 as an essential classical control.

## Implementation notes

- Pool LOOCV **scores at a common λ or normalized S first**, then minimize.
- Same N, d within each pool. Recompute H and the mapping when N changes between factorial cells.
- At λ=0 use the analytic LOOCV limit, not a small arbitrary positive λ.
- At λ=∞ use the exact projection onto ker(D_d).
- For finite λ>0, recover LOOCV via T=Q(I+λQ)^{-1}: held-out residual e_i=(Ty)_i/T_ii; analytic derivative uses T'=-T².
- Brent bracketing based on sign changes is numerical *evidence*, not a proof that every stationary point has been captured.
- Sturm sequences require exact rational inputs and a nonzero stationary polynomial; only small demonstrators are supported.
- Do not publish synthetic output figures as empirical market results.

## Stage and next work

Current stage: research plan and minimal reproducible computational scaffold. Investigate objective landscapes and ascertain if there is a *nontrivial numerical contribution* beyond published global CV methods; results may refute that thesis. Determine publication guidelines directly before final formatting.

Do not claim a theorem or experimental superiority before the required tests and evidence are recorded. Commit reproducible CSV/PNG/manifest for intentionally launched runs; note hardware, seed, git SHA, tolerances, and method configurations. Keep heavy results outside ordinary Git.
