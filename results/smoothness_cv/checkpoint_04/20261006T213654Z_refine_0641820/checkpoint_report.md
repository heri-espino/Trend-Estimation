# Checkpoint 04 development report

Source run: results/smoothness_cv/checkpoint_04/20261006T213654Z_refine_0641820

This is a development-only comparison. The latest confirmation blocks
remain untouched and must not be inspected before the dynamic rule is
frozen.

## Dynamic-rule ranking

Geometric RMSFE ratios below one favor the dynamic rule over the named
baseline. Ranking is descriptive and is used only to freeze the later
confirmatory specification.

| development_rank | rule              | n_outer | geometric_rmsfe_vs_last | geometric_rmsfe_vs_pooled | win_rate_vs_last | win_rate_vs_pooled | median_abs_s_minus_current | mean_selected_s |
| ---------------- | ----------------- | ------- | ----------------------- | ------------------------- | ---------------- | ------------------ | -------------------------- | --------------- |
| 1                | recency_hl3       | 24      | 0.7989                  | 1.049                     | 0.5833           | 0.4167             | 0.005683                   | 0.943           |
| 2                | recency_hl5       | 24      | 0.85                    | 1.116                     | 0.4583           | 0.4167             | 0.004661                   | 0.9436          |
| 3                | val2_weighted     | 24      | 0.8636                  | 1.134                     | 0.5              | 0.4167             | 0.007442                   | 0.9428          |
| 4                | median_k5         | 24      | 0.8705                  | 1.143                     | 0.4583           | 0.4167             | 0.007799                   | 0.9485          |
| 5                | mean_k3           | 24      | 0.8857                  | 1.163                     | 0.5              | 0.4167             | 0.006507                   | 0.9414          |
| 6                | recency_hl10      | 24      | 0.8905                  | 1.169                     | 0.5417           | 0.3333             | 0.005067                   | 0.9433          |
| 7                | recency_val2_hl3  | 24      | 0.9489                  | 1.246                     | 0.4583           | 0.4167             | 0.007277                   | 0.947           |
| 8                | recency_val2_hl10 | 24      | 0.9588                  | 1.259                     | 0.625            | 0.375              | 0.005284                   | 0.9448          |
| 9                | mean_k5           | 24      | 0.9643                  | 1.266                     | 0.4583           | 0.4167             | 0.006868                   | 0.9437          |
| 10               | recency_val2_hl5  | 24      | 0.9817                  | 1.289                     | 0.5833           | 0.4167             | 0.006137                   | 0.9461          |
| 11               | median_k3         | 24      | 1.042                   | 1.369                     | 0.4583           | 0.4167             | 0.005307                   | 0.945           |

## Baselines

| rule                  | n_outer | geometric_loss | mean_selected_s | median_selected_s |
| --------------------- | ------- | -------------- | --------------- | ----------------- |
| last                  | 24      | 1.624e+05      | 0.9325          | 0.9839            |
| pooled_cv_same_config | 24      | 9.419e+04      | 0.8887          | 0.9966            |

## By-series diagnostics

| series  | rule              | n_outer | geometric_rmsfe_vs_last | geometric_rmsfe_vs_pooled | win_rate_vs_last | win_rate_vs_pooled |
| ------- | ----------------- | ------- | ----------------------- | ------------------------- | ---------------- | ------------------ |
| AAPL    | mean_k3           | 6       | 1.013                   | 1.001                     | 0.6667           | 0.3333             |
| AAPL    | mean_k5           | 6       | 1.256                   | 1.24                      | 0.5              | 0.3333             |
| AAPL    | median_k3         | 6       | 0.8484                  | 0.8381                    | 0.6667           | 0.5                |
| AAPL    | median_k5         | 6       | 0.9447                  | 0.9332                    | 0.5              | 0.5                |
| AAPL    | recency_hl10      | 6       | 1.27                    | 1.254                     | 0.5              | 0.1667             |
| AAPL    | recency_hl3       | 6       | 1.177                   | 1.163                     | 0.6667           | 0.1667             |
| AAPL    | recency_hl5       | 6       | 1.267                   | 1.251                     | 0.5              | 0.1667             |
| AAPL    | recency_val2_hl10 | 6       | 1.225                   | 1.21                      | 0.5              | 0.1667             |
| AAPL    | recency_val2_hl3  | 6       | 1.185                   | 1.171                     | 0.6667           | 0.3333             |
| AAPL    | recency_val2_hl5  | 6       | 1.255                   | 1.24                      | 0.5              | 0.3333             |
| AAPL    | val2_weighted     | 6       | 1.009                   | 0.9963                    | 0.5              | 0.3333             |
| BTC-USD | mean_k3           | 6       | 0.7338                  | 0.8958                    | 0.5              | 0.5                |
| BTC-USD | mean_k5           | 6       | 0.9608                  | 1.173                     | 0.5              | 0.3333             |
| BTC-USD | median_k3         | 6       | 0.9383                  | 1.145                     | 0.3333           | 0.3333             |
| BTC-USD | median_k5         | 6       | 0.751                   | 0.9168                    | 0.5              | 0.3333             |
| BTC-USD | recency_hl10      | 6       | 0.5506                  | 0.6721                    | 0.8333           | 0.5                |
| BTC-USD | recency_hl3       | 6       | 0.6278                  | 0.7663                    | 0.6667           | 0.6667             |
| BTC-USD | recency_hl5       | 6       | 0.5821                  | 0.7106                    | 0.5              | 0.6667             |
| BTC-USD | recency_val2_hl10 | 6       | 0.7418                  | 0.9056                    | 0.8333           | 0.8333             |
| BTC-USD | recency_val2_hl3  | 6       | 0.9798                  | 1.196                     | 0.1667           | 0.3333             |
| BTC-USD | recency_val2_hl5  | 6       | 0.867                   | 1.058                     | 0.8333           | 0.5                |
| BTC-USD | val2_weighted     | 6       | 0.608                   | 0.7422                    | 1                | 0.8333             |
| GDPC1   | mean_k3           | 6       | 0.9686                  | 0.9264                    | 0.3333           | 0.6667             |
| GDPC1   | mean_k5           | 6       | 1.303                   | 1.246                     | 0.3333           | 0.6667             |
| GDPC1   | median_k3         | 6       | 1.698                   | 1.624                     | 0.1667           | 0.5                |
| GDPC1   | median_k5         | 6       | 1.793                   | 1.715                     | 0.1667           | 0.3333             |
| GDPC1   | recency_hl10      | 6       | 1.239                   | 1.185                     | 0.1667           | 0.5                |
| GDPC1   | recency_hl3       | 6       | 0.9934                  | 0.95                      | 0.3333           | 0.5                |
| GDPC1   | recency_hl5       | 6       | 1.04                    | 0.9945                    | 0.1667           | 0.5                |
| GDPC1   | recency_val2_hl10 | 6       | 1.52                    | 1.453                     | 0.3333           | 0.3333             |
| GDPC1   | recency_val2_hl3  | 6       | 1.601                   | 1.531                     | 0.3333           | 0.5                |
| GDPC1   | recency_val2_hl5  | 6       | 1.582                   | 1.513                     | 0.3333           | 0.5                |
| GDPC1   | val2_weighted     | 6       | 1.437                   | 1.375                     | 0                | 0.3333             |
| SPY     | mean_k3           | 6       | 0.8547                  | 2.204                     | 0.5              | 0.1667             |
| SPY     | mean_k5           | 6       | 0.5502                  | 1.419                     | 0.5              | 0.3333             |
| SPY     | median_k3         | 6       | 0.873                   | 2.251                     | 0.6667           | 0.3333             |
| SPY     | median_k5         | 6       | 0.4516                  | 1.164                     | 0.6667           | 0.5                |
| SPY     | recency_hl10      | 6       | 0.7258                  | 1.871                     | 0.6667           | 0.1667             |
| SPY     | recency_hl3       | 6       | 0.5549                  | 1.431                     | 0.6667           | 0.3333             |
| SPY     | recency_hl5       | 6       | 0.6806                  | 1.755                     | 0.6667           | 0.3333             |
| SPY     | recency_val2_hl10 | 6       | 0.6118                  | 1.577                     | 0.8333           | 0.1667             |
| SPY     | recency_val2_hl3  | 6       | 0.4361                  | 1.124                     | 0.6667           | 0.5                |
| SPY     | recency_val2_hl5  | 6       | 0.5395                  | 1.391                     | 0.6667           | 0.3333             |
| SPY     | val2_weighted     | 6       | 0.631                   | 1.627                     | 0.5              | 0.1667             |

## Freeze discipline

Do not run the reserved confirmation region yet. First inspect this
development run, choose the final K/half-life rule family, and record
that choice in CP04_DYNAMIC_BRANCH_RULES.md. The confirmation blocks
must then be evaluated once under that frozen specification.
