# Research roadmap — normalized forecast cross-validation

**Current: 2026-10-08. Intended journal: Communications in Statistics—Simulation and Computation.** The current manuscript is a working draft. We will write the definitive paper from completed notes **after** testing the new numerical method and choosing a new statistical experiment.

## Stage 1: question and mathematics — established

- [x] Define the training-window PLS smoother \(H_\lambda=(I+\lambda D_d^\top D_d)^{-1}\).
- [x] Normalize the trace-based Guerrero smoothness index to \(S\in[0,1]\).
- [x] Derive the spectral form, exact limiting polynomial projection and effective degrees of freedom.
- [x] Define native \(h\)-step polynomial continuation \(G_{d,h}\), with degree \(d-1\) fixed by \(d\).
- [x] Minimize pooled **historical** future-block forecast MSE using only windows completed by the current origin, then refit at the current origin.
- [x] Derive the matrix-resolvent \(n\)th derivative, and the analytic forecast-loss gradient and curvature.
- [x] Recognize possible multiple interior minima and both endpoint candidates.
- [ ] Verify gradients, Hessians, spectral shortcuts, numerical conditioning, especially near \(S=1\).

See [mathematical_foundations.md](mathematical_foundations.md).

## Stage 2: preserve existing research — complete as historical evidence

- [x] CP01–CP02: initial simulations and design refinement.
- [x] CP03: **ran** frozen 3,000 scenarios / 72,000 outer origin–horizon decisions, with figures and comparison results.
- [x] CP04–CP08: **ran** exploratory dynamic branch/financial panel/roughness/trajectory studies.
- [x] Archived favorable and unfavorable results without removing them.

CP03 is **not automatically the definitive final experimental design**. Do not change its stored seeds, code, output, or frozen interpretations. Refer to [research_log_2026-10.md](research_log_2026-10.md).

## Stage 3: numerical revision — NEXT

- [ ] Create verified small examples with known minima, stationary inflections, flat regions and boundary winners.
- [ ] Compare old adaptive \(S\) search + Brent with potential replacement solvers on the **same numerical objective and observations**.
- [ ] Evaluate small exact-rational Sturm isolation separately from large-window floating-point algorithms; do not imply universal root certification.
- [ ] Precompute eigendecomposition, projections, and analytic derivatives where it helps; compare numerical precision, memory and wall time.
- [ ] Measure missed roots, selected \(S\), endpoint frequency, actual historical objective regret, and cost.
- [ ] Select and freeze an implementation only after correctness tests and explicitly distinguishing root completeness from global value ranking.

**Gate:** A changed search method applied to exactly the same mathematical objective should not change its exact global minimizer. If results change, examine approximation error, ties, or changed protocol before making a statistical claim.

## Stage 4: new predictive experiment — PLANNED

- [ ] Decide \(d,L,h\), chronology, trend/noise DGPs, number of seeds, and independent outer blocks *before* evaluating the new method.
- [ ] Pair horizon-matched forecast-CV against one-step CV, ordinary CV, GCV, AICc, and clear simulation-only oracles on a comparable optimization footing.
- [ ] Separate **trend reconstruction** from **future observations forecast** and possible latent future trend forecasting.
- [ ] Report aggregate ratios with seed-dependent uncertainty, failures by mechanism, selected \(S\), endpoint rates, and sensitivity to continuation degree.
- [ ] Preserve all new results and negative cases; never overwrite CP03/CP04–08 artifacts.

## Stage 5: optional historical minima and branches

- [ ] If scientifically useful, characterize the location, shape, number, and movement of historical single-origin forecast-loss minima.
- [ ] Tracking \(V_j,\psi,\phi\) is an additional hypothesis, not a requirement of the pooled criterion.
- [ ] Handle birth/death/crossing ambiguity and compare with pooled forecast-CV using frozen outer tests.
- [ ] Explicitly acknowledge CP04–CP08 mixed/negative evidence for recency and trajectory rules.

## Stage 6: literature and final writing — LATER

- [ ] Verify exactly whether direct multi-step forecast-MSE tuning for finite-difference PLS trends already exists.
- [ ] Compare Guerrero, Cortés-Toto, Islas, Hart, Vilar-Fernández/Cao, Franke, Biessy in depth.
- [ ] Once solver/protocol results settle, write the final independent CSSC manuscript from these notes, select figures from verified results, compile PDF and visually review.
- [ ] Current working LaTeX and CSSC submission checklist do not supersede this research agenda.

Start with [INDEX.md](INDEX.md), [research_objective.md](research_objective.md), [next_experiments.md](next_experiments.md).
