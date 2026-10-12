# Scientific reading of the recovered formal8h CUDA results (2026-10-12)

> **Status:** completed RETROSPECTIVE REVIEW of a **partial exploratory campaign**, not a confirmatory experiment or publication-ready superiority claim. **0 new Monte Carlo runs.** All statements below refer to the previous **mu=0** PLS forecast design; the newer nonzero-difference-mean paper is independent.

## Data provenance

Public numerical outputs:
- [REPORT_BRIEF.md](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/REPORT_BRIEF.md)
- [ANALYSIS_MANIFEST.json](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/ANALYSIS_MANIFEST.json)
- [P1 complete scenario contrast CSV](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/paper1_forecast_cv_vs_classical.csv)
- [P2 matched contrast CSV](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/paper2_tracking_vs_matched_pooled.csv)
- [P3 numerical summary CSV](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/paper3_numerical_summary_compact.csv)
- [P1 PDF](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/paper1_classical_relative_rmse.pdf)
- [P2 PDF](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/paper2_matched_tracking_relative_rmse.pdf)
- [P3 PDF](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/paper3_numerical_regret.pdf)

Original manifest Git revision: \`21bd563146e04eb545cae56b46393d93a9d98212\`. Actual completed scenario/seed tasks: **100,848 / 144,000** (70.03%). **144/144** DGP cells represented, **696–704** completed independent seeds per cell. **65,877,504** stored method-evaluation rows, **50,424** numerical case records, 0 recorded failures. Reporting runtime **12.44 minutes** with no new simulations. The full 31.47-GiB SQLite snapshot remains on the user's local machine, not published in GitHub.

Comparisons are **paired on the same scenario, seed, outer origin, order and horizon**. Outer forecasts overlap and must not be counted as independent units. Pointwise nominal CIs in full scenario CSVs are computed from independent seed-averaged MSFE differences **within** scenario. Median relative RMSE below is descriptive across heterogeneous DGP cells:
\[
r_{\rm cell}=
\sqrt{\frac{\text{mean observed MSFE of method in cell}}
{\text{mean observed MSFE of comparator in same cell}}}.
\]
A median of cell ratios is **not** the grand-sample RMSE ratio and has no pooled significance level automatically.

## Paper 1 — forecast-CV against classical reconstruction criteria

Comparison: **pooled_uniform_all**, forecast-CV at the same operational $h$, against CV/GCV/AICc/BIC computed on the **current fit window**. This is NOT proof of superiority against every time-weighted pooled method; compare precisely these decision rules.

Selected scenario-level medians (ratio = classical / pooled, lower is better for method in numerator):
| d | h | CV | GCV | AICc | BIC |
| -: | -: | -: | -: | -: | -: |
| 2 | 1 | 1.0480 | 1.0624 | **1.0080** | 2.2514 |
| 2 | 3 | 1.1030 | 1.1345 | **1.0293** | 3.5755 |
| 2 | 12 | 1.4289 | 1.6200 | **1.0811** | 9.4212 |
| 3 | 1 | 1.1261 | 1.1716 | **1.0372** | 4.0306 |
| 3 | 3 | 1.3871 | 1.7272 | **1.0944** | 11.5150 |
| 3 | 12 | 4.6676 | 7.9542 | **1.8098** | 83.9803 |

Every reported median ratio exceeds 1: pooled forecast-CV is preferable on this **median-cell metric**. The gap is particularly large with higher order and longer horizon. However, substantial BIC divergence deserves an independent mathematical/code sanity check (penalty normalization, S endpoints, EDF, polynomial extrapolation), not automatic attribution to a new discovery. AICc is generally the nearest classical comparator.

For pooled_uniform_all against naive, report gives median relative RMSE of **0.7677** at d=2,h=1 (88.2% of 144 cells with ratio <1), but **0.8489** at d=3,h=12 (69.1% of 136 cells). These are descriptive; method performance varies by scenario.

## Paper 2 — tracking compared fairly at identical weighting

Each tracked selector is matched with **pooled_[same weighting]** on the very same historical forecast surfaces. This is the strongest empirical lead so far, **subject to a mechanism audit**.

| d | h | tracked_recent_exp_8 / pooled_recent_exp_8 (median cell RMSE) | cells with ratio <1 |
| -: | -: | -: | -: |
| 2 | 1 | **0.9422** | 86.1% of 144 |
| 2 | 3 | **0.9709** | 95.8% of 144 |
| 2 | 6 | **0.9847** | 94.1% of 136 |
| 2 | 12 | **0.9911** | 91.9% of 136 |
| 3 | 1 | **0.9353** | 92.4% of 144 |
| 3 | 3 | **0.9654** | 95.1% of 144 |
| 3 | 6 | **0.9760** | 83.8% of 136 |
| 3 | 12 | **0.9893** | 75.7% of 136 |

The improvement is larger at short horizons; at h=12 medians approach 1. Pooled/track uniform_all ratios are typically very close to 1 (e.g. d=2,h=1, 0.9981). These trends suggest **temporal regularization of the chosen S** may be valuable.

### Necessary ablation: branch tracking vs simple smoothing of S

The current \`select_tracked_branch\` implementation:
1. Identifies and connects local-minimum branches across consecutive *historical* F(S) curves;
2. Requires recent support/persistence;
3. Chooses active branch using recent values of historical F;
4. Outputs **the average of the last K local-minimum S positions** within the selected branch.

Therefore the observed improvement may arise from (i) actual identification/persistence of different local minima, (ii) **averaging S over time** (variance reduction), or both. Do not claim the branch mechanism is necessary without a control that averages the last K **global** argmin values or otherwise stabilizes pooled S with no branch search. Such an ablation **was not present** in the frozen campaign. We respect the user's decision **not to run more simulations**: label this distinction an open scientific limitation, not a secretly established conclusion.

Source implementation: \`experiments/smoothness_cv/weighted_surface_study.py::select_tracked_branch\`, which only uses completed historical F; outer test is used for scoring after selection.

## Paper 3 — numerical global/near-global optimization on F(S)

**Only h=3** is covered by the published P3 summary, grouped into **120 groups** across study, shape, d and method, with 50,424 numerical case records. Thus do **not** extrapolate results to h=1,6,12 without corresponding numeric records.

Median across the 120 diagnostic groups (loss = F(S) versus 401-point dense grid as **discrete numerical reference**):
- 161-point coarse grid regret: **+0.000335**;
- bracketed Brent regret: **+0.00000233**;
- adaptive stationary-point regret: **−0.0000651** (negative is possible because the dense grid is NOT a certified global minimum).

Approximate median across diagnostic group-average times in the available \`paper3_numerical_summary_compact.csv\`:
- bracketed Brent: **0.00112 s**;
- adaptive stationary-root search: **0.01084 s**;
- dense grid: **0.04867 s**.

Method timing comparisons should use matched per-case distributions, not treat these group medians as a formally controlled speedup experiment. Brent/adaptive techniques are well-known; demonstrating lower regret against a finite reference is not, by itself, a major new mathematical theorem. In the stored diagnostic groups, numerical differences in **outer observed MSFE** appear small compared with average error levels. Scientific interest may lie in characterizing stationary roots, branch geometry and *certified* small examples, not promising large forecasting gains.

In particular, the **negative adaptive regret** indicates the dense reference can be improved by points between grid knots; it is not evidence of a bug, not proof of global optimality, and must never be described as performance "better than the true optimum."

## Editorial decision: current recommendation, not a proven novelty verdict

- **Highest potential as independent paper:** Paper 2 *if* the temporal branch component is shown to be necessary beyond a simple moving average of S; results are strong but its mechanism is not isolated.
- **Strong empirical contextual result:** Paper 1; optimizing h-step forecasting errors instead of in-sample reconstruction errors explains a plausible large gain. Need closest-literature audit, compare to AICc and the best practical forecast baselines, and avoid implying criterion selection for prediction is itself original.
- **Least compelling as independent forecasting contribution:** Paper 3; useful numerical/theoretical appendix to P1/P2 unless it develops substantive results about stationary roots, reliable coverage/certificates, computational complexity or branch stability.
- **New lead nonzero-mean-difference study:** mathematically separate. These 100,848 historical \`mu=0\` Monte Carlo tasks do not evaluate Guerrero's plug-in or forecast-profiled mu; do NOT port the measured improvements to the fourth paper.

## Audits still needed before submission, WITHOUT inventing new data

1. Inspect **paired scenario CIs, negative-result cells and extreme outliers** in the public full P1/P2 contrast CSVs; determine which shape/noise families account for the gains. This review is based on the published brief and numerical aggregated summary; it does NOT independently verify every one of the large multi-MB paired CSV rows.
2. Examine severe BIC degradation, especially d=3,h=12; verify normalization, effective df, edge S=1 and polynomial continuation against the original code SHA.
3. Document the difference between a **median of scenario RMSE ratios**, a pooled RMSE ratio, and average paired MSFE improvement. Prefer seed-level paired CIs per scenario and report full heterogeneity.
4. Avoid selecting one winning weighting/method/d after viewing the common outer test and then calling the same test independently confirmatory.
5. If producing a future study is disallowed, explicitly acknowledge that the branch-vs-S-smoothing ablation is missing. Raw original SQLite is unnecessary for existing summary plots, but required for novel origin-level calculations.
6. Keep the frozen results archived, including the exact original manifest/SHA, while all new code changes to reporting stay versioned independently.

**Status:** descriptive scientific interpretation of **existing** retrospective outputs; no additional Monte Carlo and no claim of journal acceptance.
