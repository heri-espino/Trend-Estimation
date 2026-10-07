# Checkpoint 04 development report

Source run: results/smoothness_cv/checkpoint_04/20261007T001422Z_smoke_60e6786

This is a development-only comparison. The latest confirmation blocks
remain untouched and must not be inspected before the dynamic rule is
frozen.

## Dynamic-rule ranking

Geometric RMSFE ratios below one favor the dynamic rule over the named
baseline. Ranking is descriptive and is used only to freeze the later
confirmatory specification.

| development_rank | rule              | n_outer | geometric_rmsfe_vs_last | geometric_rmsfe_vs_pooled | win_rate_vs_last | win_rate_vs_pooled | median_abs_s_minus_current | mean_selected_s |
| ---------------- | ----------------- | ------- | ----------------------- | ------------------------- | ---------------- | ------------------ | -------------------------- | --------------- |
| 1                | recency_val2_hl3  | 2       | 0.8177                  | 0.9276                    | 1                | 1                  | 0.02231                    | 0.9747          |
| 2                | recency_val2_hl5  | 2       | 0.8191                  | 0.9292                    | 1                | 1                  | 0.02237                    | 0.9742          |
| 3                | recency_val2_hl10 | 2       | 0.82                    | 0.9302                    | 1                | 1                  | 0.02242                    | 0.9737          |
| 4                | val2_weighted     | 2       | 0.8206                  | 0.9309                    | 1                | 1                  | 0.02247                    | 0.9733          |
| 5                | median_k3         | 2       | 0.8379                  | 0.9505                    | 1                | 1                  | 0.02087                    | 0.9764          |
| 6                | median_k5         | 2       | 0.839                   | 0.9518                    | 1                | 1                  | 0.02078                    | 0.9765          |
| 7                | recency_hl10      | 2       | 0.8982                  | 1.019                     | 0.5              | 0                  | 0.01793                    | 0.9762          |
| 8                | mean_k5           | 2       | 0.8991                  | 1.02                      | 0.5              | 0                  | 0.01697                    | 0.9781          |
| 9                | recency_hl5       | 2       | 0.9061                  | 1.028                     | 0.5              | 0                  | 0.01721                    | 0.9768          |
| 10               | recency_hl3       | 2       | 0.9165                  | 1.04                      | 0.5              | 0                  | 0.0162                     | 0.9777          |
| 11               | mean_k3           | 2       | 0.9168                  | 1.04                      | 0.5              | 0                  | 0.01502                    | 0.9796          |

## Baselines

| rule                  | n_outer | geometric_loss | mean_selected_s | median_selected_s |
| --------------------- | ------- | -------------- | --------------- | ----------------- |
| last                  | 2       | 651.1          | 0.9862          | 0.9862            |
| pooled_cv_same_config | 2       | 573.9          | 0.9907          | 0.9907            |

## By-series diagnostics

| series | rule              | n_outer | geometric_rmsfe_vs_last | geometric_rmsfe_vs_pooled | win_rate_vs_last | win_rate_vs_pooled |
| ------ | ----------------- | ------- | ----------------------- | ------------------------- | ---------------- | ------------------ |
| GDPC1  | mean_k3           | 2       | 0.9168                  | 1.04                      | 0.5              | 0                  |
| GDPC1  | mean_k5           | 2       | 0.8991                  | 1.02                      | 0.5              | 0                  |
| GDPC1  | median_k3         | 2       | 0.8379                  | 0.9505                    | 1                | 1                  |
| GDPC1  | median_k5         | 2       | 0.839                   | 0.9518                    | 1                | 1                  |
| GDPC1  | recency_hl10      | 2       | 0.8982                  | 1.019                     | 0.5              | 0                  |
| GDPC1  | recency_hl3       | 2       | 0.9165                  | 1.04                      | 0.5              | 0                  |
| GDPC1  | recency_hl5       | 2       | 0.9061                  | 1.028                     | 0.5              | 0                  |
| GDPC1  | recency_val2_hl10 | 2       | 0.82                    | 0.9302                    | 1                | 1                  |
| GDPC1  | recency_val2_hl3  | 2       | 0.8177                  | 0.9276                    | 1                | 1                  |
| GDPC1  | recency_val2_hl5  | 2       | 0.8191                  | 0.9292                    | 1                | 1                  |
| GDPC1  | val2_weighted     | 2       | 0.8206                  | 0.9309                    | 1                | 1                  |

## Freeze discipline

Do not run the reserved confirmation region yet. First inspect this
development run, choose the final K/half-life rule family, and record
that choice in CP04_DYNAMIC_BRANCH_RULES.md. The confirmation blocks
must then be evaluated once under that frozen specification.
