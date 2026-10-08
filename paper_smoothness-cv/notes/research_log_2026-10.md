# Research log and decisions — October 2026

**Purpose:** preserve changes of direction without erasing actual completed experiments. The source of truth for the *current* aim is [research_objective.md](research_objective.md); mathematical derivations are in [mathematical_foundations.md](mathematical_foundations.md).

## What we initially thought

We began with controlled-smoothness PLS for historical trend estimation, then asked whether smoothness could be chosen for *future extrapolation*. We also explored more elaborate time-varying rules based on tracking local minima of forecast-error curves. The latter required branch histories \(V_j\), the choice \(\psi\) of which branch to follow, and a functional \(\phi\) converting its history to a current \(S\).

There were phases when documentation called the dynamic branch method the central contribution. **That statement is superseded as a research priority.** It remains a possible extension and a way to study loss-surface geometry, not a requirement of the core method.

## Current conviction, carefully stated

We are interested in *how the smoothing of a trend is chosen when the trend will be projected into the future*. Not retrospectively asking which fit looks smoothest or reconstructs a latent trend, but searching a scalar normalized smoothness \(S\in[0,1]\) that historically produces good **out-of-sample-like future-block predictions**.

This is possible without seeing the genuinely unknown future at \(T\): simulate earlier decisions \(t\), wait until their future observations have entered the historical record, score their forecasts, pool those historical errors, choose \(S\), refit at \(T\), forecast \(T+1,\ldots,T+h\). A different horizon may imply a different selected \(S\).

The eigenstructure of \(Q=D_d^\top D_d\), smoothing matrix \(H(S)\), extrapolator \(G_{d,h}\), analytic derivatives, and search for competing minima are essential to understand and compute this criterion. Their individual mathematical components are largely established; their combination into a precisely specified, horizon-matched forecast-tuning procedure is what we are investigating.

## Literature boundary (not a verified originality theorem)

- Guerrero (2007/2008): PLS trend and percentage smoothness; prior art.
- Cortés-Toto, Guerrero & Reyes (2017), *Communications in Statistics—Simulation and Computation*: smoothing criterion comparisons; very close methodological precedent.
- Islas, Guerrero & Silva (2019) and Islas Camargo & Zumaya Galván (2025): controlled-smoothness **used for forecasting**, so we must not claim this is the first such application.
- Hart (1994) and Vilar-Fernández & Cao (2007): forecast-based smoothing/CV precedents. The general concept is not new.
- Franke, Kukacka & Sacht (2026): calibrate HP smoothing for *latent-trend recovery*, different loss target.
- Biessy (2026): Whittaker–Henderson parameter selection and extrapolation, adjacent research.

**Open novelty question:** has this **specific** finite-difference PLS, normalized-index, direct \(h\)-step trend-continuation forecast-CV objective already appeared? This needs a focused prior-art audit, not a “first-ever” claim in notes or manuscript.

## Completed work: preserve it, do not silently call it final

| Stage | Historical role | Today |
| --- | --- | --- |
| CP01–CP02 | Initial simulations, diagnosis, DGP selection and protocol refinement | Completed historical development; do not present as new confirmatory evidence |
| CP03 | Frozen 3,000-scenario simulation, 72,000 outer-origin/horizon evaluations, compares horizon-matched FCV against one-step CV, CV, GCV, AICc and simulation oracles | Results **exist**, but no longer guaranteed to be the main/final experimental design after the planned numerical-method revision |
| CP04 | Development/confirmation of a recency-weighted tracked-minimum rule on four series | Historical exploratory branch results; favorable on a small confirmation |
| CP05 | External financial panel of 64 series | Historical exploratory branch results; pooled CV wins overall |
| CP06 | Post-hoc investigation of high-order continuation instability | Explanatory, not independent confirmation |
| CP07 | Time-varying roughness simulation with \(d=2\) | Historical negative result for recency versus pooled |
| CP08 | Distinct seed set and multiple \(\phi(V_j)\) mapping demonstrations | Optional methods family; no universal winner |

Do not overwrite result CSVs or mislabel them as unexecuted. The previous CP03 ratios to one-step forecast-CV were 1.000, 0.947, 0.861, 0.762 at horizons 1, 3, 6, 12. They are **historical frozen findings**, not promised outcomes for a new solver or redesigned protocol. A numerically more accurate optimizer **might** change comparisons, but this must be tested. A solver change that merely reparameterizes the same exact global objective should not mathematically change its true global minimizer; observed differences would reflect computational approximation, tie-breaking, or a changed objective/protocol.

## 2026-10-08 decision about writing

We are **researching first and writing the final article last**. The current CSSC-oriented LaTeX manuscript is a **dated working draft**, not the authoritative last version of the research. Notes and verified artifacts retain the assumptions, derivations, choices, failed attempts, and conclusions. After numerical-method decisions and new matched-protocol experiments, the manuscript should be rewritten from the completed notes rather than patched indefinitely.

The journal currently under consideration is *Communications in Statistics—Simulation and Computation*; this is a venue target, not a scientific premise. The older *Journal of Forecasting* notes are archived positioning exercises.

## Policy for future experiments

1. State precisely what mathematical/statistical algorithm changed.
2. Preserve original CP03 data, code, seeds, figures, and results unchanged.
3. Run a **same-input, same-objective** old-vs-new solver comparison before claiming a changed forecasting conclusion.
4. Separately design and preregister a new statistical experiment if the CV criterion, continuation rule, data generation, or allowed \((d,L,h)\) changes.
5. For all re-runs report numerical performance (missed minima, objective regret, endpoint choices, runtime) separately from outer forecast performance.
6. Never inspect outer future outcomes while deciding the solver, hyperparameters, or \(\phi\) rules.

This is an evolving research idea, not a completed theorem of universal forecast optimality.
