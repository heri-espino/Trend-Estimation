# Frozen CUDA campaign — exploratory retrospective analysis

- **100,848 of 144,000** scenario-seed tasks retained; 144 DGP cells represented.
- Processed **65,877,504 original saved model rows** with no new Monte Carlo runs.
- Numerics: **50,424** recorded diagnostic cases (Brent, adaptive, dense grid; NOT an exhaustive certificate).
- The three papers here are the **previous mu=0 design**; this is NOT a result for the newer nonzero difference-mean method.

## Statistical protocol

1. First average correlated overlapping external origins inside each independent scenario/seed for each model/d/h.
2. Compute differences between methods for the **same origin, seed, order and horizon**; then average at seed level.
3. Across independent seeds **within a DGP scenario** compute mean, SD and nominal 95% CI of seed-averaged paired MSFE gaps.
4. Paper 2 tracked_* is compared with pooled_* of the **same historical weighting**; Paper 1 classical/fixed comparisons are against pooled_uniform_all. No oracle rows in usable comparisons.
5. Baselines naive, drift, seasonal_naive and linear_ols are genuine matched external forecasts; no artificial S or EDF.

## Reporting limitations

The time budget left unequal seed counts across the 144 cells; we did NOT impute missing experiments, rerun seeds, or turn overlapping forecast origins into independent replicates. Relative RMSE in a table is sqrt(mean method MSE / mean comparator MSE) within that cell; confidence intervals attach to the PAIRED MSFE difference, NOT to the RMSE ratio. Any model-selection conclusion made by inspecting this external panel is exploratory, not independent confirmation.

## Compact outputs

- paper1_2_method_scenario.csv: observed/latent/recovery MSE, S, EDF and branch diagnostics by scenario/d/h/selector.
- paper1_forecast_cv_vs_classical.csv: paired CV, GCV, AICc, BIC and fixed-S comparisons with pooled_uniform_all.
- paper2_tracking_vs_matched_pooled.csv: tracked versus pooled under the identical weighting rule.
- paired_vs_baselines_scenario.csv and baseline_scenario.csv: comparisons against standard time-series forecasters.
- paper3_numerical_summary_compact.csv: stored numerical diagnostics aggregated without interpreting dense grid as exact roots.
- coverage_by_scenario.csv and ANALYSIS_MANIFEST.json: reproducible partial-coverage inventory and analysis status.
