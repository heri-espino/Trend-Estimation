# Roadmap — Smoothness-CV paper

Last updated: 2026-10-05.

**Primary target:** Journal of Forecasting.

## Phase 0 — Identity

- [x] Split criterion and numerical-solver papers.
- [x] Define Paper A as the "what should be optimized?" contribution.
- [x] Make Guerrero the direct methodological foundation.
- [x] Keep Hart as an important but structurally different predictive-selection precedent.
- [x] Freeze Journal of Forecasting as the primary target.
- [x] Replace the accidentally inherited WTI/JFM manuscript with the actual smoothness-CV paper.

## Phase 1 — Formal criterion and theory

- [x] Freeze baseline assumptions: zero drift, identity weighting, regular spacing, fixed \(d,L,h\).
- [x] Record monotonicity/endpoints of normalized \(S(\lambda)\).
- [x] State the bijection \([0,\infty]\leftrightarrow[0,1]\).
- [x] Define \(G_{d,h}\) and native zero-\(d\)th-difference continuation.
- [x] State the chronological information-set rule.
- [x] Define \(F_{d,L,h}(S)\) and \(S^\star\).
- [x] Prove the exact effective-degrees-of-freedom relation.
- [x] Clarify existence and possible nonuniqueness.
- [x] Separate forecast optimality from latent-trend recovery optimality.

## Phase 2 — Journal-facing literature audit

- [x] Re-read Guerrero 2007/controlled smoothness.
- [x] Position Hart 1994 as predictive-smoothing precedent rather than direct foundation.
- [x] Incorporate Cortés-Toto et al. on PLS selectors and induced smoothness.
- [x] Incorporate Taylor 2004 on forecast-oriented smoothing parameters.
- [x] Incorporate Zafar et al. 2022 on trend filtering for forecasting.
- [x] Incorporate Staněk 2023 on pseudo-out-of-sample/rolling loss.
- [x] Incorporate Wolff and Echterling 2024 on validation-based hyperparameter tuning.
- [x] Incorporate Franjic and Schweikert 2025 on nowcast-error cross-validation.
- [x] Incorporate Xu et al. 2025 on bandwidth/smoothing choices for forecasts.
- [ ] Broader final novelty audit before any universal "first" claim.

## Phase 3 — Controlled experiments

This is now the highest-priority phase.

- [ ] Implement/freeze the paper-specific experiment entry point.
- [ ] Compare forecast-CV with CV, GCV, AICc, and BIC.
- [ ] Compare forecast-optimal \(S\) with latent-trend recovery-optimal \(S\).
- [ ] Compare one-step-selected smoothness with horizon-matched \(h\)-step smoothness.
- [ ] Vary horizon with \(d,L\) fixed.
- [ ] Study noise scale, residual persistence, and latent trend roughness.
- [ ] Include linear, smoothly nonlinear, and structural-change mechanisms.
- [ ] Freeze seeds and test splits before inspecting final test results.
- [ ] Plot representative \(F(S)\) curves, but do not turn the paper into the numerical-methods study.

A dense deterministic \(S\)-grid is acceptable here because computational efficiency is not Paper A's contribution.

## Phase 4 — Public real-data forecasting panel

- [ ] Choose/freeze a heterogeneous public multi-series panel.
- [ ] Use genuinely chronological validation/test splits.
- [ ] Report forecast MSFE/MAE, selected \(S\), and implied effective degrees of freedom.
- [ ] If macroeconomic series are retained, replace exploratory current-vintage histories with real-time vintages for historical backtests.
- [ ] Keep any current-vintage FRED results explicitly exploratory.

## Phase 5 — Manuscript completion

- [x] Rewrite introduction for Journal of Forecasting.
- [x] Rewrite related work for the target audience.
- [x] Write the criterion and core propositions.
- [x] Write a frozen result-free evaluation protocol.
- [x] Configure Wiley NJDv5 for Journal of Forecasting.
- [x] Add a local build script and manual GitHub Actions target.
- [ ] Insert final frozen simulation results.
- [ ] Insert final public-data results.
- [ ] Add only figures/tables needed to answer the forecasting question.
- [ ] Final literature/claim audit.
- [ ] Referee-style pass for forecasting contribution, readability, and overclaiming.
- [ ] Compile submission PDF and freeze exact commit.
