# AI handoff — research workspace

**Current layout (2026-10-08):** exactly three independent active papers.

1. `working_papers/Working Paper - Smoothness Cross Validation/`
2. `working_papers/Working Paper - Numerical Methods/`
3. `working_papers/Working Paper - Dynamic Branch Selection/`

Each has its own stand-alone manuscript, research questions,
notes, claim boundaries and experimental protocol.
Do not call them companion papers or collapse their outcomes.

**Smoothness CV:** select normalized PLS S in [0,1] by
pooled historical, horizon-matched future-block MSE.
Refit the latest L-window before predicting. Q has
nullity d; I+lambda Q is SPD for finite lambda>=0;
S=1 is an exact polynomial projection with a unique
constrained least-squares fit. Pooled F is continuous
and has a minimum; the minimizing S need not be unique.
CP01–CP03 are historical runs, not final new-solver evidence.

**Numerical Methods:** one-surface multimodal stationary-root
recovery, derivatives, adaptive intervals, Brent, exact
endpoints and rational Sturm on short instances.
Previous 240/240, 2105/2105, 473/473 dense-reference
matches are empirical, not general mathematical guarantees.

**Dynamic Branch Selection:** model persistence of local minima
across completed forecast-CV origins; V_j, psi/phi, and
outer forecast tests. CP04 small confirmation favored
a recency rule but CP05 64-series and CP07–CP08 did
not confirm aggregate pooled-CV improvements. Proposed
controlled tracking correspondence CP05 is **not run**.

Reusable code resides in src/, experiments/; versioned
artifacts reside in results/. Historical paths there
are intentionally stable. Inactive drafts were moved
to ideas/. PDF builds are manual only.
