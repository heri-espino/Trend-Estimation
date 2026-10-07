# Checkpoint 08 trajectory-rule family demonstration

CP08 is not a winner-selection experiment. It demonstrates several
branch-to-smoothness functionals that can be constructed from the same
tracked branch matrix.

## Rule behavior summary

| rule          | changing_g_ratio_vs_pooled | changing_win_rate_vs_pooled | stationary_g_ratio_vs_pooled | all_g_ratio_vs_pooled | all_g_ratio_vs_last | clipping_rate | mean_abs_s_error_to_oracle |
| ------------- | -------------------------- | --------------------------- | ---------------------------- | --------------------- | ------------------- | ------------- | -------------------------- |
| delta_hl3     | 1.102                      | 0.427                       | 1.127                        | 1.11                  | 1                   | 0.2234        | 0.1475                     |
| delta_hl5     | 1.101                      | 0.4253                      | 1.127                        | 1.11                  | 0.9997              | 0.2141        | 0.1474                     |
| ew_linear_hl3 | 1.061                      | 0.4598                      | 1.08                         | 1.067                 | 0.9618              | 0.1164        | 0.1469                     |
| ew_linear_hl5 | 1.058                      | 0.4628                      | 1.073                        | 1.063                 | 0.9575              | 0.1076        | 0.1467                     |
| linear_k10    | 1.075                      | 0.4559                      | 1.088                        | 1.079                 | 0.9721              | 0.1843        | 0.1473                     |
| linear_k3     | 1.111                      | 0.4217                      | 1.134                        | 1.119                 | 1.008               | 0.189         | 0.1479                     |
| linear_k5     | 1.087                      | 0.437                       | 1.113                        | 1.096                 | 0.9872              | 0.1397        | 0.1478                     |
| recency_hl3   | 1.033                      | 0.4852                      | 1.058                        | 1.041                 | 0.9378              | 0             | 0.1451                     |

## Interpretation

Forecast ratios, clipping rates, and oracle-distance diagnostics describe
how the rules behave. They are not used to declare one universally best
smoothness-selection rule.
