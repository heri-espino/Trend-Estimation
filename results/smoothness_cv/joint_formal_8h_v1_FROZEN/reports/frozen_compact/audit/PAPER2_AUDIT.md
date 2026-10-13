# Paper 2 — retrospective evidence audit

**Exploratory; source: existing frozen mu=0 Monte Carlo only.**
Ratios are sqrt(mean method MSE / mean comparator MSE) inside a DGP scenario. Significance uses seed-level paired MSFE contrasts (Student t), Holm-corrected across every tested 2 scenario/method/order/horizon contrast; one outer origin is NOT an independent experiment.

| d | h | Method | Comparator | Cells | Median ratio | Share ratio <1 | Share Holm significant (method) |
|---:|---:|---|---|---:|---:|---:|---:|
| 2 | 1 | tracked_recent_exp_20 | pooled_recent_exp_20 | 144 | 0.9846 | 86.8% | 7.6% |
| 2 | 1 | tracked_recent_exp_8 | pooled_recent_exp_8 | 144 | 0.9422 | 86.1% | 61.8% |
| 2 | 1 | tracked_recent_linear_8 | pooled_recent_linear_8 | 144 | 0.9471 | 85.4% | 61.1% |
| 2 | 1 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 144 | 0.9681 | 84.0% | 22.9% |
| 2 | 1 | tracked_uniform_all | pooled_uniform_all | 144 | 0.9981 | 77.8% | 2.8% |
| 2 | 3 | tracked_recent_exp_20 | pooled_recent_exp_20 | 144 | 0.9916 | 94.4% | 11.8% |
| 2 | 3 | tracked_recent_exp_8 | pooled_recent_exp_8 | 144 | 0.9709 | 95.8% | 48.6% |
| 2 | 3 | tracked_recent_linear_8 | pooled_recent_linear_8 | 144 | 0.9724 | 95.8% | 55.6% |
| 2 | 3 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 144 | 0.9849 | 95.8% | 20.8% |
| 2 | 3 | tracked_uniform_all | pooled_uniform_all | 144 | 0.9990 | 79.2% | 4.2% |
| 2 | 6 | tracked_recent_exp_20 | pooled_recent_exp_20 | 136 | 0.9957 | 88.2% | 35.3% |
| 2 | 6 | tracked_recent_exp_8 | pooled_recent_exp_8 | 136 | 0.9847 | 94.1% | 52.2% |
| 2 | 6 | tracked_recent_linear_8 | pooled_recent_linear_8 | 136 | 0.9848 | 96.3% | 47.8% |
| 2 | 6 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 136 | 0.9914 | 93.4% | 40.4% |
| 2 | 6 | tracked_uniform_all | pooled_uniform_all | 136 | 0.9992 | 81.6% | 15.4% |
| 2 | 12 | tracked_recent_exp_20 | pooled_recent_exp_20 | 136 | 0.9966 | 86.8% | 29.4% |
| 2 | 12 | tracked_recent_exp_8 | pooled_recent_exp_8 | 136 | 0.9911 | 91.9% | 28.7% |
| 2 | 12 | tracked_recent_linear_8 | pooled_recent_linear_8 | 136 | 0.9917 | 91.2% | 25.7% |
| 2 | 12 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 136 | 0.9946 | 86.8% | 14.7% |
| 2 | 12 | tracked_uniform_all | pooled_uniform_all | 136 | 0.9991 | 78.7% | 19.1% |
| 3 | 1 | tracked_recent_exp_20 | pooled_recent_exp_20 | 144 | 0.9829 | 91.0% | 6.9% |
| 3 | 1 | tracked_recent_exp_8 | pooled_recent_exp_8 | 144 | 0.9353 | 92.4% | 49.3% |
| 3 | 1 | tracked_recent_linear_8 | pooled_recent_linear_8 | 144 | 0.9370 | 94.4% | 59.0% |
| 3 | 1 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 144 | 0.9709 | 90.3% | 20.1% |
| 3 | 1 | tracked_uniform_all | pooled_uniform_all | 144 | 0.9983 | 76.4% | 4.2% |
| 3 | 3 | tracked_recent_exp_20 | pooled_recent_exp_20 | 144 | 0.9909 | 90.3% | 16.0% |
| 3 | 3 | tracked_recent_exp_8 | pooled_recent_exp_8 | 144 | 0.9654 | 95.1% | 54.2% |
| 3 | 3 | tracked_recent_linear_8 | pooled_recent_linear_8 | 144 | 0.9671 | 93.8% | 54.9% |
| 3 | 3 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 144 | 0.9813 | 91.7% | 25.0% |
| 3 | 3 | tracked_uniform_all | pooled_uniform_all | 144 | 0.9988 | 82.6% | 8.3% |
| 3 | 6 | tracked_recent_exp_20 | pooled_recent_exp_20 | 136 | 0.9931 | 95.6% | 77.9% |
| 3 | 6 | tracked_recent_exp_8 | pooled_recent_exp_8 | 136 | 0.9760 | 83.8% | 48.5% |
| 3 | 6 | tracked_recent_linear_8 | pooled_recent_linear_8 | 136 | 0.9773 | 86.8% | 45.6% |
| 3 | 6 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 136 | 0.9849 | 91.9% | 30.9% |
| 3 | 6 | tracked_uniform_all | pooled_uniform_all | 136 | 0.9974 | 91.9% | 46.3% |
| 3 | 12 | tracked_recent_exp_20 | pooled_recent_exp_20 | 136 | 0.9962 | 86.0% | 32.4% |
| 3 | 12 | tracked_recent_exp_8 | pooled_recent_exp_8 | 136 | 0.9893 | 75.7% | 38.2% |
| 3 | 12 | tracked_recent_linear_8 | pooled_recent_linear_8 | 136 | 0.9890 | 80.1% | 23.5% |
| 3 | 12 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 136 | 0.9935 | 71.3% | 19.9% |
| 3 | 12 | tracked_uniform_all | pooled_uniform_all | 136 | 0.9987 | 73.5% | 21.3% |

## Heterogeneity and failures

The median may hide large outliers. Inspect \`group_heterogeneity.csv\` and \`extreme_cases.csv\` for the negative cases, noise families, trend shapes and horizons; no scenario outcomes are removed.

## Mechanism warning: branch selection versus S averaging

Operational tracking chooses a persistent historical local-minimum branch and **averages its latest K S positions**. This experiment does not include a moving-average-of-global-S control. Significant gains against matched pooled do NOT isolate the contribution of branch identity from temporal variance reduction.
The local-minimum/EDF diagnostics below can identify whether competing branches are generally present but cannot substitute for the missing ablation.
