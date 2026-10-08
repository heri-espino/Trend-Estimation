# Roadmap — forecast-optimal smoothness CV with optional adaptation

**Intended target:** Communications in Statistics—Simulation and Computation.

## Phase 0 — Baseline criterion

- [x] Define normalized smoothness `S`.
- [x] Define chronological future-block forecast loss.
- [x] Implement pooled forecast-CV selector.
- [x] Separate forecast optimality from recovery optimality.
- [x] Freeze fit-select-refit information semantics.

## Phase 1 — Pooled-selector evidence

- [x] CP01 exploratory simulation.
- [x] CP02 refined simulation design.
- [x] Freeze CP03 pooled-selector paper-scale design.
- [ ] Finish/push CP03 paper-scale results.

CP03 is the primary, frozen horizon-matched forecast-CV experiment.
Do not retune it based on optional extension results.

## Phase 2 — Dynamic tracked minima

- [x] Define local-minimum sets `M_t`.
- [x] Define epsilon one-to-one branch continuation.
- [x] Define branch matrix `V_j = [S, Val1 loss, Val2 loss]`.
- [x] Existing tracked-minima experiment implements branch histories and `last`.
- [ ] Freeze branch-selection rule `psi`.
- [ ] Implement final-smoothness rules `phi(V_j)` on identical branch histories.
- [ ] Compare `last`, recent mean, recent median, Val2-weighted, and
  recency+Val2-weighted rules.
- [ ] Decide/freeze `K`, `epsilon`, `rho`, and numerical stabilizer `delta` using
  development data only.
- [x] Evaluate frozen `recency_hl3` once on the reserved CP04 confirmation blocks.

## Phase 2B — External financial validation

- [x] Freeze `recency_hl3` from CP04 development.
- [x] Confirm it once on the four-series CP04 holdout.
- [x] Freeze an objective 64-series external Yahoo panel excluding CP04 financial series.
- [x] Implement CP05 runner, analyzer, figures, and conservative no-continuation fallback.
- [x] Run CP05 smoke.
- [x] Run CP05 full panel.
- [x] Report overall, stock, ETF, and crypto results without retuning.

## Phase 2C — Order-stability mechanism

- [x] Diagnose CP05 failures by selected difference order.
- [x] Freeze a post-hoc mechanism study on earlier historical blocks.
- [x] Compare order sets `{1,2,3,4}`, `{1,2,3}`, `{1,2}`, and `{2}`.
- [x] Run CP06 smoke.
- [x] Run CP06 full mechanism study.
- [x] Decide that the next prospective simulation must isolate smoothness dynamics from high-order continuation.
## Phase 2D — Dynamic roughness simulation

- [x] Freeze CP07 with d=2, L=120, h=20.
- [x] Run CP07 smoke.
- [x] Run CP07 paper preset.
- [x] Analyze CP07 paper results.
- [x] Conclude that backward-looking recency averaging does not beat pooled CV even under changing roughness.

## Phase 2E — Forecast the smoothness trajectory

- [x] Freeze CP08 rule-family demonstration on fresh seeds 100--199.
- [x] Implement recent-linear, exponentially weighted linear, and increment extrapolation rules.
- [x] Run CP08 smoke.
- [x] Run CP08 paper demonstration.
- [x] Summarize how the different \(\phi(V_j)\) rules behave; do not select a universal winner.

## Phase 2F — Representation figures and manuscript consolidation

- [x] Generate CP08 explanatory figures from the frozen results.
- [ ] Illustrate origin-specific minima, tracked branches, and branch matrix V_j.
- [ ] Show several phi(V_j) maps acting on the same branch history.
- [ ] Separate methodological flexibility from claims of forecasting superiority.
- [x] Integrate frozen CP03--CP08 results into the manuscript.
- [ ] Compile and visually inspect the updated Wiley manuscript PDF.

## Phase 3 — Main dynamic simulation

- [ ] Construct DGPs where forecast-optimal smoothness is stable, drifting,
  switching, or intermittently multimodal.
- [ ] Measure branch recovery/persistence separately from forecast performance.
- [ ] Compare dynamic rules with pooled forecast-CV, CV, GCV, AICc, and
  simple last-minimum selection.
- [ ] Report forecast loss, selected `S`, branch support, switching frequency,
  and regret to simulation-only forecast oracle.

## Phase 4 — Public real-data panel

- [ ] Freeze a heterogeneous public panel.
- [ ] Use chronological Val1/refit/Val2/outer-test logic.
- [ ] No manual per-series choice of branch rule.
- [ ] Compare dynamic tracked rules with pooled forecast-CV and classical
  selectors.

## Phase 5 — Manuscript

- [x] Existing manuscript contains the pooled criterion and PLS foundation.
- [x] Reframe the abstract/introduction around the primary pooled forecast-CV criterion.
- [x] Separate tracked branches into an optional extension in the manuscript.
- [ ] Add only results actually observed.
- [x] Distinguish existing PLS, index, and predictive CV precedents from
  the specific horizon-matched forecast-MSE construction.

## Canonical notes

- `notes/dynamic_tracked_smoothness.md` — optional adaptation layer.
- `notes/validation_semantics.md` — information/refit invariant.
- `notes/research_objective.md` — formal research question.

## Active papers

This forecasting manuscript is maintained as an independent article.
