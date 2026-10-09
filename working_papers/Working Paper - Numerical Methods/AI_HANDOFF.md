# Paper 3 agent handoff — numerical minima and exact endpoints

**Current research scope 2026-10-09.** Read the
[theoretical charter](../THEORETICAL_CONTRIBUTIONS.md)
and [mathematical/claim boundaries](notes/assumptions_and_claim_boundaries.md).

**The objective is ONE fixed horizon-h forecast-loss function F(S)**,
conditioned on specified difference order d, training length L,
horizon h, validation-origin set and (optionally) prespecified
historical loss weights m. This paper concerns **finding and
comparing stationary and boundary candidates correctly**, NOT
following a branch of minima through multiple origins.

Model: pure, unweighted, zero-drift PLS with
\(H_\lambda=(I+\lambda D_d^\top D_d)^{-1}\),
\(S=(L-\mathrm{tr}H_\lambda)/(L-d)\in[0,1]\).
Matrix calculus identities \(H'_\lambda=-H_\lambda QH_\lambda\)
and \(H^{(n)}_\lambda=(-1)^n n!H_\lambda(QH_\lambda)^n\)
are known. Numerical analysis studies stability,
conditioning and derivative-root discovery in THIS structured
forecast objective. Changing to S coordinates requires chain-rule
derivatives; S=0/1 endpoints must be assessed exactly.

**Implemented building blocks:**
\`src/trend_estimation/selection/smoothness_numerical.py\`:
adaptive bracketing, stationary candidate classification, spacing;
\`src/trend_estimation/selection/sturm.py\`:
restricted rational finite-instance Sturm examples.
Adaptive grids and dense-reference comparisons do NOT imply
exhaustive root certification for all datasets.
240/240 adversarial, 2105/2105 synthetic and 473/473 financial
matches are **empirical matches to their tested references**, not
general mathematical theorems.

**Canonical app:**
\`streamlit run apps/numerical_methods.py\`. It evaluates a
declared completed historical weighted F(S), uses analytic
dF/dlambda and its S-chain-rule derivative, plots F and dF/dS,
shows candidate roots/endpoints, and exports samples. It does
not do historical branch matching or require Val2.
The earlier \`experiments/numerical_smoothness_selection/dashboard_tracked_minima.py\`
is a **legacy frozen-result display**, NOT the new numerical app.

**Potential theoretical advances (must be established, not assumed):**
derivative structure/spectral reduction of the forecast objective;
objective rationality and finite root structure for fixed data,
assuming algebraic lambda dependence; proof-based lower bounds or
isolation for restricted cases; numerical error and candidate
completeness guarantees **only under stated conditions**; sensitivity
of minima to declared horizon/order and endpoints. Exact algebraic
root counting is conditional on a finite rationalized input
instance, not arbitrary float input.

**Performance/GPU:** user-run float32 kernel CUDA measurements can be
reported in a brief *implementation* paragraph/table, after verifying
precision, metadata and repeatability. These are not by themselves
proofs of novel numerical algorithms and not full end-to-end speedups.
See [computational note](../COMPUTATIONAL_IMPLEMENTATION.md).

Manuscript \`main.tex\` remains an independent working draft, not
automatically synchronized with the new app or future results.
Heavy experiments and LaTeX builds remain manual.
