# Checkpoint 03 paper-scale simulation report

Source run: results/smoothness_cv/checkpoint_03/20261006T193636Z_paper_ab9a070

Preset: paper

Inference note: common random numbers are reused across trend mechanisms
within each seed. Confidence intervals therefore resample seeds, not
individual scenario rows.

## Primary paired forecast comparison

Geometric RMSFE ratio < 1 favors horizon-matched forecast-CV.

| noise_scope | comparator    | horizon | n_series | n_seeds | geometric_rmsfe_ratio | ci95_low | ci95_high | series_win_rate | series_tie_rate | median_rmsfe_ratio | median_s_difference |
| ----------- | ------------- | ------- | -------- | ------- | --------------------- | -------- | --------- | --------------- | --------------- | ------------------ | ------------------- |
| all         | aicc          | 1       | 3000     | 100     | 0.9947                | 0.9768   | 1.013     | 0.5337          | 0.013           | 0.9955             | 0.001944            |
| all         | aicc          | 3       | 3000     | 100     | 0.9242                | 0.903    | 0.9457    | 0.66            | 0.018           | 0.9788             | 0.01111             |
| all         | aicc          | 6       | 3000     | 100     | 0.8199                | 0.8007   | 0.8393    | 0.755           | 0.01333         | 0.9512             | 0.01111             |
| all         | aicc          | 12      | 3000     | 100     | 0.7015                | 0.6819   | 0.7205    | 0.8023          | 0.01433         | 0.9109             | 0.01194             |
| all         | cv            | 1       | 3000     | 100     | 0.925                 | 0.9022   | 0.9476    | 0.6303          | 0.008333        | 0.9703             | 0.02903             |
| all         | cv            | 3       | 3000     | 100     | 0.8324                | 0.8052   | 0.8616    | 0.7493          | 0.01467         | 0.9422             | 0.03417             |
| all         | cv            | 6       | 3000     | 100     | 0.7079                | 0.6827   | 0.7343    | 0.8087          | 0.01133         | 0.8719             | 0.03611             |
| all         | cv            | 12      | 3000     | 100     | 0.5741                | 0.5499   | 0.5969    | 0.8687          | 0.01            | 0.7503             | 0.03708             |
| all         | forecast_cv_1 | 1       | 3000     | 100     | 1                     | 1        | 1         | 0               | 1               | 1                  | 0                   |
| all         | forecast_cv_1 | 3       | 3000     | 100     | 0.9467                | 0.926    | 0.9674    | 0.5753          | 0.06233         | 0.9978             | 0.003889            |
| all         | forecast_cv_1 | 6       | 3000     | 100     | 0.8614                | 0.841    | 0.8804    | 0.6643          | 0.04067         | 0.9893             | 0.004722            |
| all         | forecast_cv_1 | 12      | 3000     | 100     | 0.7616                | 0.7399   | 0.783     | 0.717           | 0.03733         | 0.9821             | 0.005               |
| all         | gcv           | 1       | 3000     | 100     | 0.9121                | 0.8884   | 0.9356    | 0.643           | 0.008333        | 0.9665             | 0.03389             |
| all         | gcv           | 3       | 3000     | 100     | 0.8155                | 0.7868   | 0.8454    | 0.7557          | 0.013           | 0.933              | 0.03958             |
| all         | gcv           | 6       | 3000     | 100     | 0.6883                | 0.6608   | 0.7163    | 0.807           | 0.009333        | 0.8654             | 0.04028             |
| all         | gcv           | 12      | 3000     | 100     | 0.5539                | 0.5285   | 0.5799    | 0.8637          | 0.01033         | 0.7412             | 0.04042             |

## Horizon matching by noise model

| noise_scope | comparator    | horizon | n_series | n_seeds | geometric_rmsfe_ratio | ci95_low | ci95_high | series_win_rate | series_tie_rate | median_rmsfe_ratio | median_s_difference |
| ----------- | ------------- | ------- | -------- | ------- | --------------------- | -------- | --------- | --------------- | --------------- | ------------------ | ------------------- |
| all         | forecast_cv_1 | 3       | 3000     | 100     | 0.9467                | 0.926    | 0.9674    | 0.5753          | 0.06233         | 0.9978             | 0.003889            |
| all         | forecast_cv_1 | 6       | 3000     | 100     | 0.8614                | 0.841    | 0.8804    | 0.6643          | 0.04067         | 0.9893             | 0.004722            |
| all         | forecast_cv_1 | 12      | 3000     | 100     | 0.7616                | 0.7399   | 0.783     | 0.717           | 0.03733         | 0.9821             | 0.005               |
| ar1         | forecast_cv_1 | 3       | 1000     | 100     | 0.863                 | 0.8108   | 0.9154    | 0.663           | 0               | 0.8862             | 0.1626              |
| ar1         | forecast_cv_1 | 6       | 1000     | 100     | 0.6534                | 0.6118   | 0.6964    | 0.883           | 0               | 0.6731             | 0.1797              |
| ar1         | forecast_cv_1 | 12      | 1000     | 100     | 0.4595                | 0.4234   | 0.4998    | 0.967           | 0               | 0.4738             | 0.1847              |
| iid         | forecast_cv_1 | 3       | 1000     | 100     | 0.9881                | 0.9763   | 0.9963    | 0.561           | 0.101           | 0.9989             | 0.0005556           |
| iid         | forecast_cv_1 | 6       | 1000     | 100     | 0.9867                | 0.9773   | 0.9937    | 0.588           | 0.056           | 0.9979             | 0.0005556           |
| iid         | forecast_cv_1 | 12      | 1000     | 100     | 0.9753                | 0.9612   | 0.9869    | 0.627           | 0.05            | 0.997              | 0.0005556           |
| student_t   | forecast_cv_1 | 3       | 1000     | 100     | 0.9949                | 0.9901   | 0.9991    | 0.502           | 0.086           | 1                  | 0.0005556           |
| student_t   | forecast_cv_1 | 6       | 1000     | 100     | 0.9914                | 0.9838   | 0.9973    | 0.522           | 0.066           | 0.9997             | 0.0005556           |
| student_t   | forecast_cv_1 | 12      | 1000     | 100     | 0.986                 | 0.9769   | 0.9936    | 0.557           | 0.062           | 0.9989             | 0.0005556           |

## Smoothness and oracle targets

| noise_model | horizon | n_series | mean_s_proposed | mean_s_recovery | mean_s_forecast_oracle | oracle_interior_rate | median_abs_gap_proposed_oracle | median_abs_gap_recovery_oracle | median_scaled_latent_excess |
| ----------- | ------- | -------- | --------------- | --------------- | ---------------------- | -------------------- | ------------------------------ | ------------------------------ | --------------------------- |
| ar1         | 1       | 1000     | 0.783           | 0.9963          | 0.7871                 | 0.999                | 0.1122                         | 0.1942                         | 1.037                       |
| ar1         | 3       | 1000     | 0.9742          | 0.9963          | 0.8679                 | 0.965                | 0.09403                        | 0.1136                         | 0.4035                      |
| ar1         | 6       | 1000     | 0.9906          | 0.9963          | 0.8743                 | 0.968                | 0.09764                        | 0.09972                        | 0.3393                      |
| ar1         | 12      | 1000     | 0.9942          | 0.9963          | 0.8738                 | 0.96                 | 0.1029                         | 0.1043                         | 0.3626                      |
| iid         | 1       | 1000     | 0.9899          | 0.9933          | 0.7931                 | 0.998                | 0.1992                         | 0.2024                         | 0.06676                     |
| iid         | 3       | 1000     | 0.9935          | 0.9933          | 0.9092                 | 0.949                | 0.05736                        | 0.05611                        | 0.05972                     |
| iid         | 6       | 1000     | 0.9935          | 0.9933          | 0.9153                 | 0.953                | 0.05389                        | 0.05333                        | 0.0649                      |
| iid         | 12      | 1000     | 0.9936          | 0.9933          | 0.9126                 | 0.961                | 0.05819                        | 0.05694                        | 0.08369                     |
| student_t   | 1       | 1000     | 0.9903          | 0.9933          | 0.7982                 | 0.996                | 0.1814                         | 0.1843                         | 0.06384                     |
| student_t   | 3       | 1000     | 0.9934          | 0.9933          | 0.8995                 | 0.988                | 0.07042                        | 0.07139                        | 0.05827                     |
| student_t   | 6       | 1000     | 0.9934          | 0.9933          | 0.9064                 | 0.972                | 0.065                          | 0.06417                        | 0.06552                     |
| student_t   | 12      | 1000     | 0.9935          | 0.9933          | 0.906                  | 0.967                | 0.06583                        | 0.06556                        | 0.08638                     |

## Mechanism diagnostics

| trend_kind          | horizon | n_series | oracle_interior_rate | mean_s_oracle | median_abs_recovery_oracle_gap | median_abs_proposed_oracle_gap | median_scaled_latent_excess |
| ------------------- | ------- | -------- | -------------------- | ------------- | ------------------------------ | ------------------------------ | --------------------------- |
| linear              | 1       | 600      | 0.9967               | 0.7944        | 0.2053                         | 0.1633                         | 0.07622                     |
| linear              | 3       | 600      | 0.97                 | 0.899         | 0.08194                        | 0.07417                        | 0.06015                     |
| linear              | 6       | 600      | 0.9633               | 0.9042        | 0.07153                        | 0.06611                        | 0.06023                     |
| linear              | 12      | 600      | 0.9533               | 0.906         | 0.06986                        | 0.06611                        | 0.06763                     |
| oscillatory         | 1       | 600      | 1                    | 0.7887        | 0.1879                         | 0.1547                         | 0.1797                      |
| oscillatory         | 3       | 600      | 0.9917               | 0.8768        | 0.08736                        | 0.08042                        | 0.169                       |
| oscillatory         | 6       | 600      | 0.9933               | 0.8778        | 0.08014                        | 0.07861                        | 0.1921                      |
| oscillatory         | 12      | 600      | 0.9933               | 0.8702        | 0.09319                        | 0.09014                        | 0.2874                      |
| recent_slope_change | 1       | 600      | 0.9983               | 0.7924        | 0.1943                         | 0.1614                         | 0.1203                      |
| recent_slope_change | 3       | 600      | 0.9533               | 0.8961        | 0.07167                        | 0.06708                        | 0.1073                      |
| recent_slope_change | 6       | 600      | 0.945                | 0.9027        | 0.06389                        | 0.06097                        | 0.114                       |
| recent_slope_change | 12      | 600      | 0.9583               | 0.9014        | 0.06389                        | 0.06389                        | 0.1544                      |
| smooth_curve        | 1       | 600      | 0.9967               | 0.7932        | 0.1912                         | 0.16                           | 0.09643                     |
| smooth_curve        | 3       | 600      | 0.96                 | 0.8934        | 0.07819                        | 0.07667                        | 0.08176                     |
| smooth_curve        | 6       | 600      | 0.9633               | 0.9041        | 0.06653                        | 0.06458                        | 0.08672                     |
| smooth_curve        | 12      | 600      | 0.9567               | 0.9032        | 0.065                          | 0.06611                        | 0.1111                      |
| terminal_bend       | 1       | 600      | 0.9967               | 0.7953        | 0.1919                         | 0.1597                         | 0.08355                     |
| terminal_bend       | 3       | 600      | 0.9617               | 0.8957        | 0.07931                        | 0.07514                        | 0.07037                     |
| terminal_bend       | 6       | 600      | 0.9567               | 0.9048        | 0.06556                        | 0.06486                        | 0.07165                     |
| terminal_bend       | 12      | 600      | 0.9517               | 0.9066        | 0.06514                        | 0.06417                        | 0.08502                     |

## Fractional method win shares

| selector      | horizon | total_win_share | n_series | win_share_rate |
| ------------- | ------- | --------------- | -------- | -------------- |
| aicc          | 1       | 754.7           | 3000     | 0.2516         |
| aicc          | 3       | 465.5           | 3000     | 0.1552         |
| aicc          | 6       | 328.7           | 3000     | 0.1096         |
| aicc          | 12      | 296.7           | 3000     | 0.09889        |
| cv            | 1       | 489.5           | 3000     | 0.1632         |
| cv            | 3       | 303.2           | 3000     | 0.1011         |
| cv            | 6       | 175.7           | 3000     | 0.05857        |
| cv            | 12      | 159             | 3000     | 0.05301        |
| forecast_cv_1 | 1       | 693.5           | 3000     | 0.2312         |
| forecast_cv_1 | 3       | 765.4           | 3000     | 0.2551         |
| forecast_cv_1 | 6       | 639             | 3000     | 0.213          |
| forecast_cv_1 | 12      | 557.9           | 3000     | 0.186          |
| forecast_cv_h | 1       | 693.5           | 3000     | 0.2312         |
| forecast_cv_h | 3       | 1247            | 3000     | 0.4157         |
| forecast_cv_h | 6       | 1646            | 3000     | 0.5486         |
| forecast_cv_h | 12      | 1906            | 3000     | 0.6352         |
| gcv           | 1       | 368.7           | 3000     | 0.1229         |
| gcv           | 3       | 218.8           | 3000     | 0.07295        |
| gcv           | 6       | 210.9           | 3000     | 0.07029        |
| gcv           | 12      | 80.93           | 3000     | 0.02698        |

## Interpretation rules

- treat h=1 forecast_cv_h versus forecast_cv_1 as an identity check;
- emphasize paired ratios and seed-clustered intervals, not raw block counts;
- do not use the latent oracle as a feasible forecasting competitor;
- report iid, AR(1), and Student-t conditions separately when their conclusions differ;
- do not add or remove DGPs after seeing this paper-preset result;
- BIC remains outside the primary comparison because CP02 showed boundary degeneracy.
