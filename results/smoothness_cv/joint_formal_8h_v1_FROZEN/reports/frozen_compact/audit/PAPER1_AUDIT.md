# Paper 1 — retrospective evidence audit

**Exploratory; source: existing frozen mu=0 Monte Carlo only.**
Ratios are sqrt(mean method MSE / mean comparator MSE) inside a DGP scenario. Significance uses seed-level paired MSFE contrasts (Student t), Holm-corrected across every tested 1 scenario/method/order/horizon contrast; one outer origin is NOT an independent experiment.

| d | h | Method | Comparator | Cells | Median ratio | Share ratio <1 | Share Holm significant (method) |
|---:|---:|---|---|---:|---:|---:|---:|
| 2 | 1 | classical_aicc | pooled_uniform_all | 144 | 1.0080 | 27.8% | 13.2% |
| 2 | 1 | classical_bic | pooled_uniform_all | 144 | 2.2514 | 0.0% | 0.0% |
| 2 | 1 | classical_cv | pooled_uniform_all | 144 | 1.0480 | 2.1% | 2.1% |
| 2 | 1 | classical_gcv | pooled_uniform_all | 144 | 1.0624 | 1.4% | 1.4% |
| 2 | 1 | fixed_0 | pooled_uniform_all | 144 | 2.2580 | 0.0% | 0.0% |
| 2 | 1 | fixed_0.5 | pooled_uniform_all | 144 | 1.6623 | 0.0% | 0.0% |
| 2 | 1 | fixed_0.8 | pooled_uniform_all | 144 | 1.2309 | 12.5% | 11.8% |
| 2 | 1 | fixed_0.95 | pooled_uniform_all | 144 | 1.0246 | 20.8% | 6.9% |
| 2 | 1 | fixed_1 | pooled_uniform_all | 144 | 1.0240 | 36.1% | 11.1% |
| 2 | 3 | classical_aicc | pooled_uniform_all | 144 | 1.0293 | 14.6% | 6.2% |
| 2 | 3 | classical_bic | pooled_uniform_all | 144 | 3.5755 | 0.0% | 0.0% |
| 2 | 3 | classical_cv | pooled_uniform_all | 144 | 1.1030 | 2.8% | 0.0% |
| 2 | 3 | classical_gcv | pooled_uniform_all | 144 | 1.1345 | 2.1% | 0.7% |
| 2 | 3 | fixed_0 | pooled_uniform_all | 144 | 3.5902 | 0.0% | 0.0% |
| 2 | 3 | fixed_0.5 | pooled_uniform_all | 144 | 2.2825 | 0.0% | 0.0% |
| 2 | 3 | fixed_0.8 | pooled_uniform_all | 144 | 1.3973 | 0.7% | 0.7% |
| 2 | 3 | fixed_0.95 | pooled_uniform_all | 144 | 1.0380 | 22.2% | 10.4% |
| 2 | 3 | fixed_1 | pooled_uniform_all | 144 | 1.0055 | 44.4% | 6.9% |
| 2 | 6 | classical_aicc | pooled_uniform_all | 136 | 1.0463 | 11.0% | 5.9% |
| 2 | 6 | classical_bic | pooled_uniform_all | 136 | 5.6841 | 0.0% | 0.0% |
| 2 | 6 | classical_cv | pooled_uniform_all | 136 | 1.1992 | 2.2% | 1.5% |
| 2 | 6 | classical_gcv | pooled_uniform_all | 136 | 1.2654 | 2.2% | 2.2% |
| 2 | 6 | fixed_0 | pooled_uniform_all | 136 | 5.7106 | 0.0% | 0.0% |
| 2 | 6 | fixed_0.5 | pooled_uniform_all | 136 | 3.3276 | 0.0% | 0.0% |
| 2 | 6 | fixed_0.8 | pooled_uniform_all | 136 | 1.6715 | 0.0% | 0.0% |
| 2 | 6 | fixed_0.95 | pooled_uniform_all | 136 | 1.0691 | 16.2% | 9.6% |
| 2 | 6 | fixed_1 | pooled_uniform_all | 136 | 1.0061 | 41.9% | 12.5% |
| 2 | 12 | classical_aicc | pooled_uniform_all | 136 | 1.0811 | 11.8% | 8.8% |
| 2 | 12 | classical_bic | pooled_uniform_all | 136 | 9.4212 | 0.0% | 0.0% |
| 2 | 12 | classical_cv | pooled_uniform_all | 136 | 1.4289 | 2.9% | 1.5% |
| 2 | 12 | classical_gcv | pooled_uniform_all | 136 | 1.6200 | 2.2% | 1.5% |
| 2 | 12 | fixed_0 | pooled_uniform_all | 136 | 9.4681 | 0.0% | 0.0% |
| 2 | 12 | fixed_0.5 | pooled_uniform_all | 136 | 5.2331 | 0.0% | 0.0% |
| 2 | 12 | fixed_0.8 | pooled_uniform_all | 136 | 2.2505 | 0.7% | 0.0% |
| 2 | 12 | fixed_0.95 | pooled_uniform_all | 136 | 1.1088 | 16.2% | 10.3% |
| 2 | 12 | fixed_1 | pooled_uniform_all | 136 | 1.0012 | 49.3% | 33.1% |
| 3 | 1 | classical_aicc | pooled_uniform_all | 144 | 1.0372 | 4.2% | 1.4% |
| 3 | 1 | classical_bic | pooled_uniform_all | 144 | 4.0306 | 0.0% | 0.0% |
| 3 | 1 | classical_cv | pooled_uniform_all | 144 | 1.1261 | 0.7% | 0.0% |
| 3 | 1 | classical_gcv | pooled_uniform_all | 144 | 1.1716 | 0.7% | 0.0% |
| 3 | 1 | fixed_0 | pooled_uniform_all | 144 | 4.0475 | 0.0% | 0.0% |
| 3 | 1 | fixed_0.5 | pooled_uniform_all | 144 | 2.5413 | 0.0% | 0.0% |
| 3 | 1 | fixed_0.8 | pooled_uniform_all | 144 | 1.5123 | 0.7% | 0.0% |
| 3 | 1 | fixed_0.95 | pooled_uniform_all | 144 | 1.0854 | 20.1% | 6.2% |
| 3 | 1 | fixed_1 | pooled_uniform_all | 144 | 0.9930 | 61.8% | 11.1% |
| 3 | 3 | classical_aicc | pooled_uniform_all | 144 | 1.0944 | 9.7% | 3.5% |
| 3 | 3 | classical_bic | pooled_uniform_all | 144 | 11.5150 | 0.0% | 0.0% |
| 3 | 3 | classical_cv | pooled_uniform_all | 144 | 1.3871 | 0.0% | 0.0% |
| 3 | 3 | classical_gcv | pooled_uniform_all | 144 | 1.7272 | 0.0% | 0.0% |
| 3 | 3 | fixed_0 | pooled_uniform_all | 144 | 11.5778 | 0.0% | 0.0% |
| 3 | 3 | fixed_0.5 | pooled_uniform_all | 144 | 5.8304 | 0.0% | 0.0% |
| 3 | 3 | fixed_0.8 | pooled_uniform_all | 144 | 2.2057 | 0.7% | 0.7% |
| 3 | 3 | fixed_0.95 | pooled_uniform_all | 144 | 1.1520 | 13.2% | 10.4% |
| 3 | 3 | fixed_1 | pooled_uniform_all | 144 | 0.9957 | 70.8% | 22.2% |
| 3 | 6 | classical_aicc | pooled_uniform_all | 136 | 1.2500 | 2.9% | 0.7% |
| 3 | 6 | classical_bic | pooled_uniform_all | 136 | 29.5982 | 0.0% | 0.0% |
| 3 | 6 | classical_cv | pooled_uniform_all | 136 | 2.0239 | 0.0% | 0.0% |
| 3 | 6 | classical_gcv | pooled_uniform_all | 136 | 3.2239 | 0.0% | 0.0% |
| 3 | 6 | fixed_0 | pooled_uniform_all | 136 | 29.7753 | 0.0% | 0.0% |
| 3 | 6 | fixed_0.5 | pooled_uniform_all | 136 | 13.6480 | 0.0% | 0.0% |
| 3 | 6 | fixed_0.8 | pooled_uniform_all | 136 | 3.8462 | 0.0% | 0.0% |
| 3 | 6 | fixed_0.95 | pooled_uniform_all | 136 | 1.2842 | 10.3% | 10.3% |
| 3 | 6 | fixed_1 | pooled_uniform_all | 136 | 0.9967 | 74.3% | 32.4% |
| 3 | 12 | classical_aicc | pooled_uniform_all | 136 | 1.8098 | 2.9% | 0.0% |
| 3 | 12 | classical_bic | pooled_uniform_all | 136 | 83.9803 | 0.0% | 0.0% |
| 3 | 12 | classical_cv | pooled_uniform_all | 136 | 4.6676 | 0.0% | 0.0% |
| 3 | 12 | classical_gcv | pooled_uniform_all | 136 | 7.9542 | 0.0% | 0.0% |
| 3 | 12 | fixed_0 | pooled_uniform_all | 136 | 84.5111 | 0.0% | 0.0% |
| 3 | 12 | fixed_0.5 | pooled_uniform_all | 136 | 36.7331 | 0.0% | 0.0% |
| 3 | 12 | fixed_0.8 | pooled_uniform_all | 136 | 8.6369 | 0.0% | 0.0% |
| 3 | 12 | fixed_0.95 | pooled_uniform_all | 136 | 1.6525 | 6.6% | 5.9% |
| 3 | 12 | fixed_1 | pooled_uniform_all | 136 | 0.9912 | 82.4% | 54.4% |

## Heterogeneity and failures

The median may hide large outliers. Inspect `group_heterogeneity.csv` and `extreme_cases.csv` for the negative cases, noise families, trend shapes and horizons; no scenario outcomes are removed.

## BIC anomaly: mechanistic audit, NOT an automatic bug verdict

BIC in the original CUDA campaign revision chooses S using
`log(RSS/L) + EDF*log(L)/L` on the LAST L observed values. It is a reconstruction information criterion, not a horizon-h out-of-sample forecast criterion. Very small in-sample residuals can coexist with unstable order-d polynomial continuation, especially d=3 and h=12.

The published example d=3,h=12 has BIC/pooled median relative RMSE 83.9803. This statistic is a scenario median ratio, not a factor of 84 across every observation.
Use the local `paper1_2_method_scenario.csv` diagnostics (selected_s, edf, n_independent_seeds) and the original SHA 21bd563... before attributing the anomaly to overfitting, low S, boundary behavior or a specific implementation error.
