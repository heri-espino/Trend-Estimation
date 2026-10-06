# Checkpoint 01 diagnostic report

Source run: results/smoothness_cv/checkpoint_01/20261006T025812Z_smoke_d9630b5

This report is descriptive only. It does not freeze CP02 or assert that
the proposed selector is superior.

## Selector summary

| selector              | horizon | n | mean_s | median_s | endpoint_zero_rate | endpoint_one_rate | mean_mse | median_rel_rmsfe_gcv |
| --------------------- | ------- | - | ------ | -------- | ------------------ | ----------------- | -------- | -------------------- |
| aicc                  | 1       | 6 | 0.9688 | 0.9938   | 0                  | 0.5               | 0.0195   | 1.101                |
| aicc                  | 6       | 6 | 0.9688 | 0.9938   | 0                  | 0.5               | 0.08653  | 0.9839               |
| bic                   | 1       | 6 | 0.0125 | 0.0125   | 0                  | 0                 | 1.36     | 4.158                |
| bic                   | 6       | 6 | 0.0125 | 0.0125   | 0                  | 0                 | 13.11    | 5.607                |
| cv                    | 1       | 6 | 0.9542 | 0.975    | 0                  | 0.5               | 0.02192  | 1                    |
| cv                    | 6       | 6 | 0.9542 | 0.975    | 0                  | 0.5               | 0.09778  | 1                    |
| forecast_cv_1         | 1       | 6 | 0.9917 | 0.9938   | 0                  | 0.5               | 0.1253   | 1.094                |
| forecast_cv_1         | 6       | 6 | 0.9917 | 0.9938   | 0                  | 0.5               | 0.1014   | 0.9816               |
| forecast_cv_h         | 1       | 6 | 0.9917 | 0.9938   | 0                  | 0.5               | 0.1253   | 1.094                |
| forecast_cv_h         | 6       | 6 | 0.9958 | 1        | 0                  | 0.6667            | 0.1018   | 1                    |
| gcv                   | 1       | 6 | 0.9417 | 0.925    | 0                  | 0.3333            | 0.02082  | 1                    |
| gcv                   | 6       | 6 | 0.9417 | 0.925    | 0                  | 0.3333            | 0.09267  | 1                    |
| recovery_oracle_train | 1       | 6 | 0.9938 | 1        | 0                  | 0.6667            | 0.1059   | 1.878                |
| recovery_oracle_train | 6       | 6 | 0.9938 | 1        | 0                  | 0.6667            | 0.08369  | 0.9829               |

## Horizon-matched versus one-step tuning

| horizon | n | median_mse_ratio | mean_mse_ratio | win_rate_h | tie_rate | mean_s_difference | median_abs_s_difference |
| ------- | - | ---------------- | -------------- | ---------- | -------- | ----------------- | ----------------------- |
| 1       | 6 | 1                | 1              | 0          | 1        | 0                 | 0                       |
| 6       | 6 | 1                | 1.032          | 0          | 0.6667   | 0.004167          | 0                       |

## Forecast-optimal versus recovery-optimal smoothness

| horizon | n | mean_s_forecast | mean_s_recovery | median_abs_s_gap | rate_abs_gap_gt_010 | median_forecast_mse_ratio_to_recovery |
| ------- | - | --------------- | --------------- | ---------------- | ------------------- | ------------------------------------- |
| 1       | 6 | 0.9917          | 0.9938          | 0.0125           | 0                   | 0.8153                                |
| 6       | 6 | 0.9958          | 0.9938          | 0.00625          | 0                   | 1                                     |

## Per-block method wins

| selector      | horizon | wins | total_blocks | win_rate |
| ------------- | ------- | ---- | ------------ | -------- |
| forecast_cv_h | 1       | 3    | 6            | 0.5      |
| cv            | 1       | 2    | 6            | 0.3333   |
| gcv           | 1       | 1    | 6            | 0.1667   |
| forecast_cv_1 | 6       | 2    | 6            | 0.3333   |
| forecast_cv_h | 6       | 2    | 6            | 0.3333   |
| aicc          | 6       | 1    | 6            | 0.1667   |
| cv            | 6       | 1    | 6            | 0.1667   |

## Forecast-CV smoothness by mechanism

| trend_kind   | noise_model | horizon | n | mean_s | median_s | mean_mse |
| ------------ | ----------- | ------- | - | ------ | -------- | -------- |
| linear       | iid         | 1       | 3 | 0.9958 | 1        | 0.103    |
| linear       | iid         | 6       | 3 | 1      | 1        | 0.07974  |
| smooth_curve | iid         | 1       | 3 | 0.9875 | 0.9875   | 0.1476   |
| smooth_curve | iid         | 6       | 3 | 0.9917 | 0.9875   | 0.1239   |

## Required human/agent review before CP02

- inspect endpoint selection rates;
- inspect objective curves rather than only aggregate scores;
- inspect results by trend mechanism and noise dependence;
- verify whether horizon-matched gains, if any, are broad or driven by a few cases;
- verify whether the recovery-versus-forecast gap is scientifically interpretable;
- do not run the paper preset until those checks are complete.
