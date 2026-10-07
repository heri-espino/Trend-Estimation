# Checkpoint 04 development report

Source run: results/smoothness_cv/checkpoint_04/20261007T011201Z_confirmation_6c0b548

This is a development-only comparison. The latest confirmation blocks
remain untouched and must not be inspected before the dynamic rule is
frozen.

## Dynamic-rule ranking

Geometric RMSFE ratios below one favor the dynamic rule over the named
baseline. Ranking is descriptive and is used only to freeze the later
confirmatory specification.

| development_rank | rule        | n_outer | geometric_rmsfe_vs_last | geometric_rmsfe_vs_pooled | win_rate_vs_last | win_rate_vs_pooled | median_abs_s_minus_current | mean_selected_s |
| ---------------- | ----------- | ------- | ----------------------- | ------------------------- | ---------------- | ------------------ | -------------------------- | --------------- |
| 1                | recency_hl3 | 16      | 0.8137                  | 0.692                     | 0.5625           | 0.8125             | 0.007397                   | 0.9834          |

## Baselines

| rule                  | n_outer | geometric_loss | mean_selected_s | median_selected_s |
| --------------------- | ------- | -------------- | --------------- | ----------------- |
| last                  | 16      | 326.1          | 0.9842          | 0.9873            |
| pooled_cv_same_config | 16      | 383.5          | 0.9817          | 0.9898            |

## By-series diagnostics

| series  | rule        | n_outer | geometric_rmsfe_vs_last | geometric_rmsfe_vs_pooled | win_rate_vs_last | win_rate_vs_pooled |
| ------- | ----------- | ------- | ----------------------- | ------------------------- | ---------------- | ------------------ |
| AAPL    | recency_hl3 | 4       | 0.4096                  | 0.4561                    | 0.75             | 1                  |
| BTC-USD | recency_hl3 | 4       | 1.028                   | 1.039                     | 0.5              | 0.75               |
| GDPC1   | recency_hl3 | 4       | 1.223                   | 0.8176                    | 0.5              | 0.75               |
| SPY     | recency_hl3 | 4       | 0.851                   | 0.5917                    | 0.5              | 0.75               |

## Freeze discipline

Do not run the reserved confirmation region yet. First inspect this
development run, choose the final K/half-life rule family, and record
that choice in CP04_DYNAMIC_BRANCH_RULES.md. The confirmation blocks
must then be evaluated once under that frozen specification.
