# Checkpoint 06 order-stability mechanism report

Source run: `results/smoothness_cv/checkpoint_06/20261007T063750Z_mechanism_6bc62e3`

CP06 is explicitly post-hoc and explanatory. It uses earlier historical
outer blocks and does not rescore the four CP05 external-test blocks.

## Order-set comparison

| order_set | n_series | n_outer | geometric_ratio_vs_pooled | ci95_lo_vs_pooled | ci95_hi_vs_pooled | outer_win_rate_vs_pooled | series_win_rate_vs_pooled | ratio_gt_5_rate | ratio_gt_10_rate | ratio_gt_100_rate | max_ratio_vs_pooled | geometric_ratio_vs_last | ci95_lo_vs_last | ci95_hi_vs_last | outer_win_rate_vs_last | series_win_rate_vs_last | fallback_rate |
| --------- | -------- | ------- | ------------------------- | ----------------- | ----------------- | ------------------------ | ------------------------- | --------------- | ---------------- | ----------------- | ------------------- | ----------------------- | --------------- | --------------- | ---------------------- | ----------------------- | ------------- |
| d12       | 64       | 512     | 1.073                     | 1.033             | 1.113             | 0.4473                   | 0.2812                    | 0.007812        | 0                | 0                 | 6.256               | 1.012                   | 0.9772          | 1.051           | 0.4727                 | 0.4531                  | 0             |
| d123      | 64       | 512     | 1.2                       | 1.131             | 1.277             | 0.4219                   | 0.2031                    | 0.04492         | 0.01953          | 0                 | 64.74               | 0.9485                  | 0.893           | 1.007           | 0.4902                 | 0.5938                  | 0             |
| d1234     | 64       | 512     | 1.353                     | 1.195             | 1.548             | 0.4277                   | 0.2031                    | 0.05469         | 0.0332           | 0.01562           | 3.06e+08            | 0.691                   | 0.4617          | 0.9303          | 0.4902                 | 0.625                   | 0             |
| d2        | 64       | 512     | 1.045                     | 1.008             | 1.086             | 0.4434                   | 0.375                     | 0.009766        | 0                | 0                 | 8.884               | 0.9942                  | 0.9555          | 1.035           | 0.5078                 | 0.4844                  | 0             |

## Direct effect of restricting orders on the dynamic forecast

| order_set | n_outer | geometric_dynamic_rmse_ratio_vs_d1234 | win_rate_vs_d1234_dynamic |
| --------- | ------- | ------------------------------------- | ------------------------- |
| d123      | 512     | 0.7314                                | 0.1543                    |
| d12       | 512     | 0.5818                                | 0.3613                    |
| d2        | 512     | 0.573                                 | 0.4609                    |

## Selected-order frequencies

| order_set | order | n_outer | selection_rate |
| --------- | ----- | ------- | -------------- |
| d12       | 1     | 105     | 0.2051         |
| d12       | 2     | 407     | 0.7949         |
| d123      | 1     | 86      | 0.168          |
| d123      | 2     | 228     | 0.4453         |
| d123      | 3     | 198     | 0.3867         |
| d1234     | 1     | 82      | 0.1602         |
| d1234     | 2     | 188     | 0.3672         |
| d1234     | 3     | 136     | 0.2656         |
| d1234     | 4     | 106     | 0.207          |
| d2        | 2     | 512     | 1              |

## By asset class

| order_set | asset_class | n_series | n_outer | geometric_ratio_vs_pooled | geometric_ratio_vs_last | win_rate_vs_pooled | win_rate_vs_last | ratio_gt_10_rate |
| --------- | ----------- | -------- | ------- | ------------------------- | ----------------------- | ------------------ | ---------------- | ---------------- |
| d12       | crypto      | 8        | 64      | 1.068                     | 0.9863                  | 0.4219             | 0.5156           | 0                |
| d12       | etf         | 20       | 160     | 1.067                     | 0.9874                  | 0.5062             | 0.4562           | 0                |
| d12       | stock       | 36       | 288     | 1.076                     | 1.033                   | 0.4201             | 0.4722           | 0                |
| d123      | crypto      | 8        | 64      | 1.12                      | 0.911                   | 0.4219             | 0.5781           | 0.01562          |
| d123      | etf         | 20       | 160     | 1.295                     | 0.9349                  | 0.4125             | 0.4437           | 0.025            |
| d123      | stock       | 36       | 288     | 1.168                     | 0.9648                  | 0.4271             | 0.4965           | 0.01736          |
| d1234     | crypto      | 8        | 64      | 0.9283                    | 0.6475                  | 0.4531             | 0.5938           | 0.01562          |
| d1234     | etf         | 20       | 160     | 1.502                     | 0.5713                  | 0.4188             | 0.4625           | 0.04375          |
| d1234     | stock       | 36       | 288     | 1.389                     | 0.7792                  | 0.4271             | 0.4826           | 0.03125          |
| d2        | crypto      | 8        | 64      | 1.067                     | 0.9512                  | 0.3906             | 0.5312           | 0                |
| d2        | etf         | 20       | 160     | 1.051                     | 0.9421                  | 0.4875             | 0.55             | 0                |
| d2        | stock       | 36       | 288     | 1.037                     | 1.034                   | 0.4306             | 0.4792           | 0                |

## Interpretation boundary

Use this checkpoint to identify whether high-order polynomial
continuation is the mechanism behind the CP05 tail failures. Do not
present a better-performing post-hoc order set as independently
validated. Any revised forecasting specification must next be frozen
and tested prospectively in controlled simulations or new data.
