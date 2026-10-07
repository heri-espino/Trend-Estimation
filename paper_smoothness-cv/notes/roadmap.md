# Roadmap — Dynamic smoothness-CV paper

**Primary target:** Journal of Forecasting.

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

CP03 remains a valid baseline. Do not retune it because the central method has
expanded.

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
- [ ] Analyze CP07 paper results.
- [ ] Decide whether dynamic tracking helps specifically under changing roughness.

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
- [ ] Rewrite abstract/introduction after dynamic results exist.
- [ ] Make tracked branches the central method and pooled selector the baseline.
- [ ] Add only results actually observed.
- [ ] Audit novelty around dynamic smoothing-parameter tracking before claiming
  precedence.

## Canonical notes

- `notes/dynamic_tracked_smoothness.md` — central method.
- `notes/validation_semantics.md` — information/refit invariant.
- `notes/research_objective.md` — formal research question.

## Active papers

Only `paper_smoothness-cv/` and `paper_numerical-methods/` are active.
