# Checkpoint 05 external financial panel

Source run: `results/smoothness_cv/checkpoint_05/20261007T062356Z_panel_a400609`

The dynamic rule was frozen before this panel was evaluated:
`recency_hl3`. AAPL, SPY, and BTC-USD were excluded because they were
used in CP04. No CP05 series was selected from forecast performance.

## Primary result

Series-cluster geometric RMSE ratio versus pooled CV: **1.6421** 
(descriptive 95% series-cluster bootstrap interval 
[1.1678, 2.7033]).

Series-cluster geometric RMSE ratio versus the newest tracked minimum: 
**0.5246** 
(descriptive 95% interval 
[0.2001, 0.9052]).

## Overall and by asset class

| group  | n_series | n_outer | geometric_rmse_ratio_vs_pooled | cluster_ci95_lo_vs_pooled | cluster_ci95_hi_vs_pooled | outer_win_rate_vs_pooled | series_win_rate_vs_pooled | geometric_rmse_ratio_vs_last | cluster_ci95_lo_vs_last | cluster_ci95_hi_vs_last | outer_win_rate_vs_last | series_win_rate_vs_last | fallback_rate |
| ------ | -------- | ------- | ------------------------------ | ------------------------- | ------------------------- | ------------------------ | ------------------------- | ---------------------------- | ----------------------- | ----------------------- | ---------------------- | ----------------------- | ------------- |
| all    | 64       | 256     | 1.642                          | 1.168                     | 2.703                     | 0.4648                   | 0.3906                    | 0.5246                       | 0.2001                  | 0.9052                  | 0.6016                 | 0.6094                  | 0             |
| crypto | 8        | 32      | 1.098                          | 0.9511                    | 1.259                     | 0.4375                   | 0.5                       | 1.22                         | 1.087                   | 1.366                   | 0.4062                 | 0.125                   | 0             |
| etf    | 20       | 80      | 1.152                          | 0.9104                    | 1.492                     | 0.4875                   | 0.5                       | 0.6945                       | 0.4986                  | 0.9236                  | 0.7                    | 0.85                    | 0             |
| stock  | 36       | 144     | 2.186                          | 1.237                     | 5.269                     | 0.4583                   | 0.3056                    | 0.3721                       | 0.07042                 | 0.9399                  | 0.5903                 | 0.5833                  | 0             |

## Series-level results

| asset_class | series   | n_outer | geometric_rmse_ratio_vs_last | geometric_rmse_ratio_vs_pooled | win_rate_vs_last | win_rate_vs_pooled | fallback_rate | mean_s_dynamic | mean_abs_s_change_from_last |
| ----------- | -------- | ------- | ---------------------------- | ------------------------------ | ---------------- | ------------------ | ------------- | -------------- | --------------------------- |
| crypto      | ADA-USD  | 4       | 1.306                        | 1.382                          | 0.5              | 0.5                | 0             | 0.9933         | 0.01368                     |
| crypto      | AVAX-USD | 4       | 1.475                        | 0.9909                         | 0.5              | 0.5                | 0             | 0.9932         | 0.002343                    |
| crypto      | BCH-USD  | 4       | 1.507                        | 0.9688                         | 0                | 0.25               | 0             | 0.9902         | 0.006637                    |
| crypto      | DOGE-USD | 4       | 0.9854                       | 1.319                          | 0.75             | 0.5                | 0             | 0.9954         | 0.004481                    |
| crypto      | DOT-USD  | 4       | 1.221                        | 1.112                          | 0.25             | 0.5                | 0             | 0.9912         | 0.004925                    |
| crypto      | LINK-USD | 4       | 1.38                         | 1.444                          | 0                | 0.25               | 0             | 0.9874         | 0.00834                     |
| crypto      | SOL-USD  | 4       | 1.003                        | 0.7769                         | 0.75             | 0.75               | 0             | 0.9934         | 0.003173                    |
| crypto      | XLM-USD  | 4       | 1.018                        | 0.968                          | 0.5              | 0.25               | 0             | 0.9936         | 0.005271                    |
| etf         | IJH      | 4       | 0.4584                       | 1.564                          | 0.5              | 0.5                | 0             | 0.9884         | 0.005173                    |
| etf         | IJR      | 4       | 0.8396                       | 0.7277                         | 0.75             | 0.5                | 0             | 0.9921         | 0.01139                     |
| etf         | ITOT     | 4       | 0.5683                       | 0.5083                         | 0.75             | 0.75               | 0             | 0.9962         | 0.005438                    |
| etf         | IVV      | 4       | 0.6438                       | 0.9146                         | 1                | 0.75               | 0             | 0.9925         | 0.005729                    |
| etf         | IWD      | 4       | 0.8817                       | 1.179                          | 0.75             | 0.25               | 0             | 0.9853         | 0.002602                    |
| etf         | IWF      | 4       | 1.06                         | 1.371                          | 0.5              | 0.5                | 0             | 0.9758         | 0.03295                     |
| etf         | MDY      | 4       | 0.7309                       | 0.923                          | 0.75             | 0.75               | 0             | 0.9909         | 0.004567                    |
| etf         | SCHB     | 4       | 0.06322                      | 1.962                          | 1                | 0.5                | 0             | 0.9798         | 0.02013                     |
| etf         | SMH      | 4       | 1.159                        | 2.233                          | 0.5              | 0.25               | 0             | 0.9866         | 0.005733                    |
| etf         | VB       | 4       | 0.5241                       | 0.6264                         | 0.75             | 0.75               | 0             | 0.9909         | 0.003868                    |
| etf         | VEA      | 4       | 0.7994                       | 1.233                          | 1                | 0.5                | 0             | 0.9932         | 0.003805                    |
| etf         | VO       | 4       | 0.73                         | 1.158                          | 1                | 0.25               | 0             | 0.9934         | 0.003374                    |
| etf         | VTV      | 4       | 0.9309                       | 1.807                          | 0.5              | 0                  | 0             | 0.9848         | 0.01339                     |
| etf         | VUG      | 4       | 0.5176                       | 0.7052                         | 0.75             | 0.75               | 0             | 0.9913         | 0.005091                    |
| etf         | VWO      | 4       | 0.8426                       | 0.7515                         | 0.5              | 0.5                | 0             | 0.9946         | 0.004216                    |
| etf         | XLB      | 4       | 0.6555                       | 0.6489                         | 1                | 1                  | 0             | 0.9908         | 0.0124                      |
| etf         | XLI      | 4       | 3.784                        | 5.853                          | 0.25             | 0                  | 0             | 0.9625         | 0.02068                     |
| etf         | XLP      | 4       | 0.6233                       | 1.936                          | 1                | 0                  | 0             | 0.9787         | 0.009274                    |
| etf         | XLU      | 4       | 0.7248                       | 0.7886                         | 0.5              | 0.75               | 0             | 0.9852         | 0.0061                      |
| etf         | XLY      | 4       | 0.6963                       | 0.9927                         | 0.25             | 0.5                | 0             | 0.9861         | 0.009626                    |
| stock       | ABBV     | 4       | 0.7617                       | 0.8285                         | 0.5              | 0.5                | 0             | 0.9941         | 0.0119                      |
| stock       | ADBE     | 4       | 0.9746                       | 0.9694                         | 0.25             | 0.5                | 0             | 0.9892         | 0.006515                    |
| stock       | AMD      | 4       | 0.1741                       | 2.318                          | 0.5              | 0.25               | 0             | 0.9729         | 0.01251                     |
| stock       | AMZN     | 4       | 0.6762                       | 7.413                          | 1                | 0.5                | 0             | 0.9828         | 0.002084                    |
| stock       | AVGO     | 4       | 0.7642                       | 1.136                          | 0.75             | 0.5                | 0             | 0.9934         | 0.005479                    |
| stock       | BA       | 4       | 1.696                        | 1.277                          | 0.25             | 0.25               | 0             | 0.9887         | 0.007469                    |
| stock       | BLK      | 4       | 0.6129                       | 1.358                          | 0.75             | 0.25               | 0             | 0.9664         | 0.009586                    |
| stock       | C        | 4       | 7.575e-13                    | 3.24e+05                       | 1                | 0.5                | 0             | 0.9537         | 0.04199                     |
| stock       | COP      | 4       | 0.8879                       | 1.051                          | 1                | 0.5                | 0             | 0.9781         | 0.007576                    |
| stock       | COST     | 4       | 2.201                        | 2.193                          | 0.5              | 0.25               | 0             | 0.9896         | 0.005831                    |
| stock       | CRM      | 4       | 1.146                        | 1.265                          | 0.5              | 0.5                | 0             | 0.9961         | 0.005486                    |
| stock       | CSCO     | 4       | 0.9294                       | 0.7458                         | 0.5              | 0.75               | 0             | 0.992          | 0.004516                    |
| stock       | DE       | 4       | 1.889                        | 2.177                          | 0.5              | 0.25               | 0             | 0.981          | 0.008149                    |
| stock       | DIS      | 4       | 1.181                        | 1.016                          | 0.25             | 0.5                | 0             | 0.9758         | 0.01124                     |
| stock       | FDX      | 4       | 1.155                        | 1.22                           | 0.5              | 0.25               | 0             | 0.9928         | 0.007432                    |
| stock       | GE       | 4       | 1.003                        | 1.06                           | 0.5              | 0.75               | 0             | 0.9939         | 0.003399                    |
| stock       | GOOGL    | 4       | 0.08554                      | 1.128                          | 0.75             | 0.75               | 0             | 0.9793         | 0.03182                     |
| stock       | GS       | 4       | 0.6544                       | 2.261                          | 0.25             | 0                  | 0             | 0.9826         | 0.009968                    |
| stock       | IBM      | 4       | 0.1752                       | 388.7                          | 0.5              | 0.25               | 0             | 0.9855         | 0.001897                    |
| stock       | LLY      | 4       | 2.034                        | 2.461                          | 0.25             | 0.25               | 0             | 0.9699         | 0.01322                     |
| stock       | MCD      | 4       | 0.5239                       | 3.147                          | 1                | 0.5                | 0             | 0.9838         | 0.008667                    |
| stock       | META     | 4       | 1.377                        | 1.395                          | 0                | 0.25               | 0             | 0.9844         | 0.01258                     |
| stock       | MMM      | 4       | 0.5316                       | 0.9651                         | 0.75             | 0.5                | 0             | 0.993          | 0.004885                    |
| stock       | MRK      | 4       | 0.5372                       | 1.954                          | 0.75             | 0.5                | 0             | 0.9806         | 0.007122                    |
| stock       | MS       | 4       | 1.564                        | 1.752                          | 0.5              | 0                  | 0             | 0.9809         | 0.006156                    |
| stock       | NKE      | 4       | 1.084                        | 1.369                          | 0.5              | 0.25               | 0             | 0.9905         | 0.001757                    |
| stock       | NVDA     | 4       | 1.005                        | 0.8254                         | 0.75             | 0.75               | 0             | 0.97           | 0.005316                    |
| stock       | ORCL     | 4       | 0.6275                       | 0.9631                         | 0.75             | 0.5                | 0             | 0.9848         | 0.005764                    |
| stock       | OXY      | 4       | 0.967                        | 1.191                          | 0.75             | 0.75               | 0             | 0.9944         | 0.006185                    |
| stock       | PEP      | 4       | 0.6087                       | 1.022                          | 0.75             | 0.5                | 0             | 0.984          | 0.01985                     |
| stock       | PFE      | 4       | 1.112                        | 0.9152                         | 0.25             | 0.75               | 0             | 0.9788         | 0.02454                     |
| stock       | SLB      | 4       | 0.8318                       | 0.9049                         | 0.75             | 0.75               | 0             | 0.9912         | 0.009811                    |
| stock       | TGT      | 4       | 1.135                        | 0.8239                         | 0.5              | 0.75               | 0             | 0.991          | 0.007841                    |
| stock       | TSLA     | 4       | 0.6812                       | 0.8068                         | 1                | 0.5                | 0             | 0.9951         | 0.004428                    |
| stock       | UNH      | 4       | 1.148                        | 1.317                          | 0.5              | 0.5                | 0             | 0.989          | 0.003441                    |
| stock       | UPS      | 4       | 0.5844                       | 0.9069                         | 0.75             | 0.5                | 0             | 0.9722         | 0.005689                    |

## Interpretation rule

This is an external validation stage, not a tuning stage. Do not change
the half-life, branch selector, epsilon, spacing, orders, windows, or
fallback rule based on these results. Financial series share common
market shocks, so cluster intervals are sensitivity summaries rather
than evidence of independent cross-sectional sampling.

Fallback rate: **0.00%**.

Frozen manifest timestamp: `2026-09-29T21:40:44.625057+00:00`.
