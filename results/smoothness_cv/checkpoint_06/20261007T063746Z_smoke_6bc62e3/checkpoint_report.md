# Checkpoint 06 order-stability mechanism report

Source run: `results/smoothness_cv/checkpoint_06/20261007T063746Z_smoke_6bc62e3`

CP06 is explicitly post-hoc and explanatory. It uses earlier historical
outer blocks and does not rescore the four CP05 external-test blocks.

## Order-set comparison

| order_set | n_series | n_outer | geometric_ratio_vs_pooled | ci95_lo_vs_pooled | ci95_hi_vs_pooled | outer_win_rate_vs_pooled | series_win_rate_vs_pooled | ratio_gt_5_rate | ratio_gt_10_rate | ratio_gt_100_rate | max_ratio_vs_pooled | geometric_ratio_vs_last | ci95_lo_vs_last | ci95_hi_vs_last | outer_win_rate_vs_last | series_win_rate_vs_last | fallback_rate |
| --------- | -------- | ------- | ------------------------- | ----------------- | ----------------- | ------------------------ | ------------------------- | --------------- | ---------------- | ----------------- | ------------------- | ----------------------- | --------------- | --------------- | ---------------------- | ----------------------- | ------------- |
| d12       | 3        | 6       | 1.145                     | 1.092             | 1.232             | 0.3333                   | 0                         | 0               | 0                | 0                 | 1.324               | 1.007                   | 0.9191          | 1.118           | 0.3333                 | 0.6667                  | 0             |
| d1234     | 3        | 6       | 1.049                     | 1.001             | 1.092             | 0.5                      | 0                         | 0               | 0                | 0                 | 1.262               | 0.9463                  | 0.9191          | 0.9884          | 0.6667                 | 1                       | 0             |

## Direct effect of restricting orders on the dynamic forecast

| order_set | n_outer | geometric_dynamic_rmse_ratio_vs_d1234 | win_rate_vs_d1234_dynamic |
| --------- | ------- | ------------------------------------- | ------------------------- |
| d12       | 6       | 0.857                                 | 0.3333                    |

## Selected-order frequencies

| order_set | order | n_outer | selection_rate |
| --------- | ----- | ------- | -------------- |
| d12       | 1     | 3       | 0.5            |
| d12       | 2     | 3       | 0.5            |
| d1234     | 1     | 1       | 0.1667         |
| d1234     | 2     | 3       | 0.5            |
| d1234     | 3     | 2       | 0.3333         |

## By asset class

| order_set | asset_class | n_series | n_outer | geometric_ratio_vs_pooled | geometric_ratio_vs_last | win_rate_vs_pooled | win_rate_vs_last | ratio_gt_10_rate |
| --------- | ----------- | -------- | ------- | ------------------------- | ----------------------- | ------------------ | ---------------- | ---------------- |
| d12       | crypto      | 1        | 2       | 1.232                     | 1.118                   | 0                  | 0                | 0                |
| d12       | etf         | 1        | 2       | 1.116                     | 0.9926                  | 0.5                | 0.5              | 0                |
| d12       | stock       | 1        | 2       | 1.092                     | 0.9191                  | 0.5                | 0.5              | 0                |
| d1234     | crypto      | 1        | 2       | 1.001                     | 0.9884                  | 0.5                | 0.5              | 0                |
| d1234     | etf         | 1        | 2       | 1.056                     | 0.9329                  | 0.5                | 1                | 0                |
| d1234     | stock       | 1        | 2       | 1.092                     | 0.9191                  | 0.5                | 0.5              | 0                |

## Interpretation boundary

Use this checkpoint to identify whether high-order polynomial
continuation is the mechanism behind the CP05 tail failures. Do not
present a better-performing post-hoc order set as independently
validated. Any revised forecasting specification must next be frozen
and tested prospectively in controlled simulations or new data.
