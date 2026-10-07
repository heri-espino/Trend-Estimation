# Checkpoint 05 external financial panel

Source run: `results/smoothness_cv/checkpoint_05/20261007T062247Z_smoke_a400609`

The dynamic rule was frozen before this panel was evaluated:
`recency_hl3`. AAPL, SPY, and BTC-USD were excluded because they were
used in CP04. No CP05 series was selected from forecast performance.

## Primary result

Series-cluster geometric RMSE ratio versus pooled CV: **1.6285** 
(descriptive 95% series-cluster bootstrap interval 
[0.8381, 5.1155]).

Series-cluster geometric RMSE ratio versus the newest tracked minimum: 
**1.2830** 
(descriptive 95% interval 
[0.8381, 2.6545]).

## Overall and by asset class

| group  | n_series | n_outer | geometric_rmse_ratio_vs_pooled | cluster_ci95_lo_vs_pooled | cluster_ci95_hi_vs_pooled | outer_win_rate_vs_pooled | series_win_rate_vs_pooled | geometric_rmse_ratio_vs_last | cluster_ci95_lo_vs_last | cluster_ci95_hi_vs_last | outer_win_rate_vs_last | series_win_rate_vs_last | fallback_rate |
| ------ | -------- | ------- | ------------------------------ | ------------------------- | ------------------------- | ------------------------ | ------------------------- | ---------------------------- | ----------------------- | ----------------------- | ---------------------- | ----------------------- | ------------- |
| all    | 3        | 3       | 1.629                          | 0.8381                    | 5.115                     | 0.3333                   | 0.3333                    | 1.283                        | 0.8381                  | 2.655                   | 0.6667                 | 0.6667                  | 0             |
| crypto | 1        | 1       | 1.007                          | 1.007                     | 1.007                     | 0                        | 0                         | 0.9493                       | 0.9493                  | 0.9493                  | 1                      | 1                       | 0             |
| etf    | 1        | 1       | 5.115                          | 5.115                     | 5.115                     | 0                        | 0                         | 2.655                        | 2.655                   | 2.655                   | 0                      | 0                       | 0             |
| stock  | 1        | 1       | 0.8381                         | 0.8381                    | 0.8381                    | 1                        | 1                         | 0.8381                       | 0.8381                  | 0.8381                  | 1                      | 1                       | 0             |

## Series-level results

| asset_class | series  | n_outer | geometric_rmse_ratio_vs_last | geometric_rmse_ratio_vs_pooled | win_rate_vs_last | win_rate_vs_pooled | fallback_rate | mean_s_dynamic | mean_abs_s_change_from_last |
| ----------- | ------- | ------- | ---------------------------- | ------------------------------ | ---------------- | ------------------ | ------------- | -------------- | --------------------------- |
| crypto      | SOL-USD | 1       | 0.9493                       | 1.007                          | 1                | 0                  | 0             | 0.9943         | 0.001772                    |
| etf         | IVV     | 1       | 2.655                        | 5.115                          | 0                | 0                  | 0             | 0.9911         | 0.007722                    |
| stock       | AMZN    | 1       | 0.8381                       | 0.8381                         | 1                | 1                  | 0             | 0.9986         | 0.00135                     |

## Interpretation rule

This is an external validation stage, not a tuning stage. Do not change
the half-life, branch selector, epsilon, spacing, orders, windows, or
fallback rule based on these results. Financial series share common
market shocks, so cluster intervals are sensitivity summaries rather
than evidence of independent cross-sectional sampling.

Fallback rate: **0.00%**.

Frozen manifest timestamp: `2026-09-29T21:40:44.625057+00:00`.
