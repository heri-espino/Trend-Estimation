# Checkpoint 01 diagnostic report

Source run: results/smoothness_cv/checkpoint_01/20261006T031348Z_quick_abb5c96

This report is descriptive only. It does not freeze CP02 or assert that
the proposed selector is superior.

## Selector summary

| selector              | horizon | n   | mean_s | median_s | endpoint_zero_rate | endpoint_one_rate | mean_mse | median_rel_rmsfe_gcv |
| --------------------- | ------- | --- | ------ | -------- | ------------------ | ----------------- | -------- | -------------------- |
| aicc                  | 1       | 192 | 0.8982 | 0.9225   | 0                  | 0.375             | 0.2305   | 1                    |
| aicc                  | 3       | 192 | 0.8982 | 0.9225   | 0                  | 0.375             | 0.3307   | 0.9976               |
| aicc                  | 6       | 192 | 0.8982 | 0.9225   | 0                  | 0.375             | 0.493    | 1                    |
| aicc                  | 12      | 192 | 0.8982 | 0.9225   | 0                  | 0.375             | 0.7265   | 1                    |
| bic                   | 1       | 192 | 0.005  | 0.005    | 0                  | 0                 | 1.287    | 1.918                |
| bic                   | 3       | 192 | 0.005  | 0.005    | 0                  | 0                 | 2.603    | 1.772                |
| bic                   | 6       | 192 | 0.005  | 0.005    | 0                  | 0                 | 7.034    | 1.82                 |
| bic                   | 12      | 192 | 0.005  | 0.005    | 0                  | 0                 | 21.4     | 1.996                |
| cv                    | 1       | 192 | 0.7164 | 0.785    | 0                  | 0.3802            | 0.3178   | 1                    |
| cv                    | 3       | 192 | 0.7164 | 0.785    | 0                  | 0.3802            | 0.6244   | 1                    |
| cv                    | 6       | 192 | 0.7164 | 0.785    | 0                  | 0.3802            | 1.497    | 1                    |
| cv                    | 12      | 192 | 0.7164 | 0.785    | 0                  | 0.3802            | 3.954    | 1                    |
| forecast_cv_1         | 1       | 192 | 0.9076 | 0.98     | 0                  | 0.2604            | 0.2512   | 1                    |
| forecast_cv_1         | 3       | 192 | 0.9076 | 0.98     | 0                  | 0.2604            | 0.3015   | 0.9706               |
| forecast_cv_1         | 6       | 192 | 0.9076 | 0.98     | 0                  | 0.2604            | 0.4779   | 0.9398               |
| forecast_cv_1         | 12      | 192 | 0.9076 | 0.98     | 0                  | 0.2604            | 0.8667   | 0.9899               |
| forecast_cv_h         | 1       | 192 | 0.9076 | 0.98     | 0                  | 0.2604            | 0.2512   | 1                    |
| forecast_cv_h         | 3       | 192 | 0.9856 | 0.995    | 0                  | 0.4479            | 0.2376   | 0.9868               |
| forecast_cv_h         | 6       | 192 | 0.9943 | 1        | 0                  | 0.5156            | 0.2622   | 0.9637               |
| forecast_cv_h         | 12      | 192 | 0.9933 | 0.995    | 0                  | 0.4427            | 0.2784   | 0.7831               |
| gcv                   | 1       | 192 | 0.7174 | 0.77     | 0                  | 0.3698            | 0.3026   | 1                    |
| gcv                   | 3       | 192 | 0.7174 | 0.77     | 0                  | 0.3698            | 0.5793   | 1                    |
| gcv                   | 6       | 192 | 0.7174 | 0.77     | 0                  | 0.3698            | 1.344    | 1                    |
| gcv                   | 12      | 192 | 0.7174 | 0.77     | 0                  | 0.3698            | 3.48     | 1                    |
| recovery_oracle_train | 1       | 192 | 0.9929 | 1        | 0                  | 0.5365            | 0.2288   | 1                    |
| recovery_oracle_train | 3       | 192 | 0.9929 | 1        | 0                  | 0.5365            | 0.2106   | 0.851                |
| recovery_oracle_train | 6       | 192 | 0.9929 | 1        | 0                  | 0.5365            | 0.2413   | 0.7037               |
| recovery_oracle_train | 12      | 192 | 0.9929 | 1        | 0                  | 0.5365            | 0.2683   | 0.7216               |

## Horizon-matched versus one-step tuning

| horizon | n   | median_mse_ratio | mean_mse_ratio | win_rate_h | tie_rate | mean_s_difference | median_abs_s_difference |
| ------- | --- | ---------------- | -------------- | ---------- | -------- | ----------------- | ----------------------- |
| 1       | 192 | 1                | 1              | 0          | 1        | 0                 | 0                       |
| 3       | 192 | 1                | 0.9178         | 0.4844     | 0.2031   | 0.07805           | 0.015                   |
| 6       | 192 | 0.9962           | 0.8652         | 0.5208     | 0.1927   | 0.08672           | 0.015                   |
| 12      | 192 | 0.9673           | 0.7668         | 0.5729     | 0.1823   | 0.08573           | 0.015                   |

## Forecast-optimal versus recovery-optimal smoothness

| horizon | n   | mean_s_forecast | mean_s_recovery | median_abs_s_gap | rate_abs_gap_gt_010 | median_forecast_mse_ratio_to_recovery |
| ------- | --- | --------------- | --------------- | ---------------- | ------------------- | ------------------------------------- |
| 1       | 192 | 0.9076          | 0.9929          | 0.02             | 0.3438              | 1                                     |
| 3       | 192 | 0.9856          | 0.9929          | 0.0075           | 0.04167             | 1                                     |
| 6       | 192 | 0.9943          | 0.9929          | 0.005            | 0                   | 1                                     |
| 12      | 192 | 0.9933          | 0.9929          | 0.005            | 0                   | 1                                     |

## Per-block method wins

| selector      | horizon | wins | total_blocks | win_rate |
| ------------- | ------- | ---- | ------------ | -------- |
| forecast_cv_h | 1       | 78   | 192          | 0.4062   |
| aicc          | 1       | 52   | 192          | 0.2708   |
| cv            | 1       | 37   | 192          | 0.1927   |
| bic           | 1       | 16   | 192          | 0.08333  |
| gcv           | 1       | 9    | 192          | 0.04688  |
| forecast_cv_h | 3       | 97   | 192          | 0.5052   |
| aicc          | 3       | 29   | 192          | 0.151    |
| forecast_cv_1 | 3       | 27   | 192          | 0.1406   |
| bic           | 3       | 24   | 192          | 0.125    |
| cv            | 3       | 14   | 192          | 0.07292  |
| gcv           | 3       | 1    | 192          | 0.005208 |
| forecast_cv_h | 6       | 105  | 192          | 0.5469   |
| forecast_cv_1 | 6       | 33   | 192          | 0.1719   |
| aicc          | 6       | 25   | 192          | 0.1302   |
| cv            | 6       | 14   | 192          | 0.07292  |
| bic           | 6       | 12   | 192          | 0.0625   |
| gcv           | 6       | 3    | 192          | 0.01562  |
| forecast_cv_h | 12      | 115  | 192          | 0.599    |
| forecast_cv_1 | 12      | 35   | 192          | 0.1823   |
| cv            | 12      | 20   | 192          | 0.1042   |
| aicc          | 12      | 17   | 192          | 0.08854  |
| gcv           | 12      | 4    | 192          | 0.02083  |
| bic           | 12      | 1    | 192          | 0.005208 |

## Forecast-CV smoothness by mechanism

| trend_kind    | noise_model | horizon | n  | mean_s | median_s | mean_mse |
| ------------- | ----------- | ------- | -- | ------ | -------- | -------- |
| linear        | ar1         | 1       | 24 | 0.8287 | 0.835    | 0.215    |
| linear        | ar1         | 3       | 24 | 0.9796 | 0.9975   | 0.1735   |
| linear        | ar1         | 6       | 24 | 0.9967 | 1        | 0.2022   |
| linear        | ar1         | 12      | 24 | 0.9975 | 0.9975   | 0.2196   |
| linear        | iid         | 1       | 24 | 0.9975 | 1        | 0.2888   |
| linear        | iid         | 3       | 24 | 1      | 1        | 0.2928   |
| linear        | iid         | 6       | 24 | 0.9996 | 1        | 0.3065   |
| linear        | iid         | 12      | 24 | 0.9996 | 1        | 0.3216   |
| low_frequency | ar1         | 1       | 24 | 0.8287 | 0.835    | 0.2134   |
| low_frequency | ar1         | 3       | 24 | 0.9762 | 0.99     | 0.1828   |
| low_frequency | ar1         | 6       | 24 | 0.9942 | 0.995    | 0.2223   |
| low_frequency | ar1         | 12      | 24 | 0.9921 | 0.9925   | 0.2515   |
| low_frequency | iid         | 1       | 24 | 0.9933 | 1        | 0.2886   |
| low_frequency | iid         | 3       | 24 | 0.9944 | 0.995    | 0.3102   |
| low_frequency | iid         | 6       | 24 | 0.994  | 0.995    | 0.3217   |
| low_frequency | iid         | 12      | 24 | 0.99   | 0.99     | 0.3382   |
| slope_change  | ar1         | 1       | 24 | 0.8198 | 0.835    | 0.2062   |
| slope_change  | ar1         | 3       | 24 | 0.9767 | 0.9925   | 0.1764   |
| slope_change  | ar1         | 6       | 24 | 0.9942 | 1        | 0.2065   |
| slope_change  | ar1         | 12      | 24 | 0.995  | 1        | 0.2093   |
| slope_change  | iid         | 1       | 24 | 0.9923 | 0.9925   | 0.2889   |
| slope_change  | iid         | 3       | 24 | 0.9946 | 0.9975   | 0.2863   |
| slope_change  | iid         | 6       | 24 | 0.9935 | 0.995    | 0.3068   |
| slope_change  | iid         | 12      | 24 | 0.9923 | 0.9925   | 0.3194   |
| smooth_curve  | ar1         | 1       | 24 | 0.8115 | 0.82     | 0.2112   |
| smooth_curve  | ar1         | 3       | 24 | 0.9721 | 0.9875   | 0.1806   |
| smooth_curve  | ar1         | 6       | 24 | 0.9919 | 0.99     | 0.2118   |
| smooth_curve  | ar1         | 12      | 24 | 0.9917 | 0.99     | 0.2343   |
| smooth_curve  | iid         | 1       | 24 | 0.9888 | 0.99     | 0.2975   |
| smooth_curve  | iid         | 3       | 24 | 0.9915 | 0.995    | 0.2985   |
| smooth_curve  | iid         | 6       | 24 | 0.9904 | 0.99     | 0.3196   |
| smooth_curve  | iid         | 12      | 24 | 0.9883 | 0.99     | 0.3332   |

## Required human/agent review before CP02

- inspect endpoint selection rates;
- inspect objective curves rather than only aggregate scores;
- inspect results by trend mechanism and noise dependence;
- verify whether horizon-matched gains, if any, are broad or driven by a few cases;
- verify whether the recovery-versus-forecast gap is scientifically interpretable;
- do not run the paper preset until those checks are complete.
