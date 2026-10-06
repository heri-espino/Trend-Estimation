# Checkpoint 03 paper-scale simulation report

Source run: results/smoothness_cv/checkpoint_03/20261006T191618Z_smoke_a29e1a7

Preset: smoke

Inference note: common random numbers are reused across trend mechanisms
within each seed. Confidence intervals therefore resample seeds, not
individual scenario rows.

## Primary paired forecast comparison

Geometric RMSFE ratio < 1 favors horizon-matched forecast-CV.

| noise_scope | comparator    | horizon | n_series | n_seeds | geometric_rmsfe_ratio | ci95_low | ci95_high | series_win_rate | series_tie_rate | median_rmsfe_ratio | median_s_difference |
| ----------- | ------------- | ------- | -------- | ------- | --------------------- | -------- | --------- | --------------- | --------------- | ------------------ | ------------------- |
| all         | aicc          | 1       | 6        | 1       | 0.9759                | 0.9759   | 0.9759    | 0.8333          | 0               | 0.9671             | 0.03333             |
| all         | aicc          | 6       | 6        | 1       | 1.002                 | 1.002    | 1.002     | 0.3333          | 0               | 1.022              | 0.125               |
| all         | aicc          | 12      | 6        | 1       | 0.7054                | 0.7054   | 0.7054    | 1               | 0               | 0.7631             | 0.1271              |
| all         | cv            | 1       | 6        | 1       | 0.9653                | 0.9653   | 0.9653    | 0.5             | 0               | 1.007              | 0.1292              |
| all         | cv            | 6       | 6        | 1       | 0.9626                | 0.9626   | 0.9626    | 0.8333          | 0               | 0.9705             | 0.2187              |
| all         | cv            | 12      | 6        | 1       | 0.6369                | 0.6369   | 0.6369    | 1               | 0               | 0.6713             | 0.2208              |
| all         | forecast_cv_1 | 1       | 6        | 1       | 1                     | 1        | 1         | 0               | 1               | 1                  | 0                   |
| all         | forecast_cv_1 | 6       | 6        | 1       | 1.044                 | 1.044    | 1.044     | 0.1667          | 0               | 1.06               | 0.09167             |
| all         | forecast_cv_1 | 12      | 6        | 1       | 0.7437                | 0.7437   | 0.7437    | 1               | 0               | 0.8133             | 0.09375             |
| all         | gcv           | 1       | 6        | 1       | 1.016                 | 1.016    | 1.016     | 0.5             | 0               | 1.067              | 0.1375              |
| all         | gcv           | 6       | 6        | 1       | 0.9615                | 0.9615   | 0.9615    | 0.8333          | 0               | 0.9664             | 0.2271              |
| all         | gcv           | 12      | 6        | 1       | 0.6452                | 0.6452   | 0.6452    | 1               | 0               | 0.6827             | 0.2292              |

## Horizon matching by noise model

| noise_scope | comparator    | horizon | n_series | n_seeds | geometric_rmsfe_ratio | ci95_low | ci95_high | series_win_rate | series_tie_rate | median_rmsfe_ratio | median_s_difference |
| ----------- | ------------- | ------- | -------- | ------- | --------------------- | -------- | --------- | --------------- | --------------- | ------------------ | ------------------- |
| all         | forecast_cv_1 | 6       | 6        | 1       | 1.044                 | 1.044    | 1.044     | 0.1667          | 0               | 1.06               | 0.09167             |
| all         | forecast_cv_1 | 12      | 6        | 1       | 0.7437                | 0.7437   | 0.7437    | 1               | 0               | 0.8133             | 0.09375             |
| ar1         | forecast_cv_1 | 6       | 3        | 1       | 1.037                 | 1.037    | 1.037     | 0.3333          | 0               | 1.07               | 0.1875              |
| ar1         | forecast_cv_1 | 12      | 3        | 1       | 0.5671                | 0.5671   | 0.5671    | 1               | 0               | 0.5786             | 0.1875              |
| iid         | forecast_cv_1 | 6       | 3        | 1       | 1.051                 | 1.051    | 1.051     | 0               | 0               | 1.055              | 0.0125              |
| iid         | forecast_cv_1 | 12      | 3        | 1       | 0.9752                | 0.9752   | 0.9752    | 1               | 0               | 0.9772             | 0.0125              |

## Smoothness and oracle targets

| noise_model | horizon | n_series | mean_s_proposed | mean_s_recovery | mean_s_forecast_oracle | oracle_interior_rate | median_abs_gap_proposed_oracle | median_abs_gap_recovery_oracle | median_scaled_latent_excess |
| ----------- | ------- | -------- | --------------- | --------------- | ---------------------- | -------------------- | ------------------------------ | ------------------------------ | --------------------------- |
| ar1         | 1       | 3        | 0.8125          | 0.9986          | 0.6056                 | 1                    | 0.2042                         | 0.3917                         | 1.668                       |
| ar1         | 6       | 3        | 0.9931          | 0.9986          | 0.9236                 | 0.3333               | 0.0125                         | 0.004167                       | 0.2437                      |
| ar1         | 12      | 3        | 0.9944          | 0.9986          | 0.9333                 | 0.3333               | 0.008333                       | 0.004167                       | 0.2924                      |
| iid         | 1       | 3        | 0.9778          | 0.9903          | 0.8875                 | 1                    | 0.09583                        | 0.1083                         | 0.2669                      |
| iid         | 6       | 3        | 0.9917          | 0.9903          | 0.9708                 | 0.3333               | 0.01667                        | 0.004167                       | 0.1789                      |
| iid         | 12      | 3        | 0.9917          | 0.9903          | 0.9722                 | 0.6667               | 0.0125                         | 0                              | 0.2284                      |

## Mechanism diagnostics

| trend_kind          | horizon | n_series | oracle_interior_rate | mean_s_oracle | median_abs_recovery_oracle_gap | median_abs_proposed_oracle_gap | median_scaled_latent_excess |
| ------------------- | ------- | -------- | -------------------- | ------------- | ------------------------------ | ------------------------------ | --------------------------- |
| linear              | 1       | 2        | 1                    | 0.75          | 0.25                           | 0.15                           | 0.8952                      |
| linear              | 6       | 2        | 0                    | 1             | 0                              | 0                              | 0                           |
| linear              | 12      | 2        | 0                    | 1             | 0                              | 0                              | 0                           |
| oscillatory         | 1       | 2        | 1                    | 0.7396        | 0.2521                         | 0.1458                         | 0.9852                      |
| oscillatory         | 6       | 2        | 0                    | 0.9917        | 0.004167                       | 0.01458                        | 0.346                       |
| oscillatory         | 12      | 2        | 0.5                  | 0.9896        | 0.002083                       | 0.01042                        | 0.5464                      |
| recent_slope_change | 1       | 2        | 1                    | 0.75          | 0.2417                         | 0.15                           | 0.9672                      |
| recent_slope_change | 6       | 2        | 1                    | 0.85          | 0.1417                         | 0.15                           | 0.2113                      |
| recent_slope_change | 12      | 2        | 1                    | 0.8688        | 0.1229                         | 0.1312                         | 0.2604                      |

## Fractional method win shares

| selector      | horizon | total_win_share | n_series | win_share_rate |
| ------------- | ------- | --------------- | -------- | -------------- |
| aicc          | 1       | 1               | 6        | 0.1667         |
| aicc          | 6       | 0               | 6        | 0              |
| aicc          | 12      | 0               | 6        | 0              |
| cv            | 1       | 0               | 6        | 0              |
| cv            | 6       | 0               | 6        | 0              |
| cv            | 12      | 0               | 6        | 0              |
| forecast_cv_1 | 1       | 1               | 6        | 0.1667         |
| forecast_cv_1 | 6       | 5               | 6        | 0.8333         |
| forecast_cv_1 | 12      | 0               | 6        | 0              |
| forecast_cv_h | 1       | 1               | 6        | 0.1667         |
| forecast_cv_h | 6       | 1               | 6        | 0.1667         |
| forecast_cv_h | 12      | 6               | 6        | 1              |
| gcv           | 1       | 3               | 6        | 0.5            |
| gcv           | 6       | 0               | 6        | 0              |
| gcv           | 12      | 0               | 6        | 0              |

## Interpretation rules

- treat h=1 forecast_cv_h versus forecast_cv_1 as an identity check;
- emphasize paired ratios and seed-clustered intervals, not raw block counts;
- do not use the latent oracle as a feasible forecasting competitor;
- report iid, AR(1), and Student-t conditions separately when their conclusions differ;
- do not add or remove DGPs after seeing this paper-preset result;
- BIC remains outside the primary comparison because CP02 showed boundary degeneracy.
