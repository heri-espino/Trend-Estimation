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
- [ ] Evaluate all frozen rules on untouched outer test blocks.

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
