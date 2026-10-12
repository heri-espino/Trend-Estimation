# Retrospective Monte Carlo results — three previous papers

**EXPLORATORY, NOT CONFIRMATORY.** This report is generated from the frozen, historically completed mu=0 CUDA experiment. It is NOT a result for the new nonzero-mean-difference paper.

- **Completed scenario/seed tasks:** 100,848 / 144,000.
- **Originally stored method rows analyzed:** 65,877,504.
- **Historical numerical cases:** 50,424.
- **No new Monte Carlo or GPU tasks performed** during analysis.

Every ratio below is sqrt(mean method MSE / mean comparator MSE) **inside one predeclared DGP cell**. Values summarized across cells are *medians* and proportions, not confidence intervals. For scenario-specific paired MSFE confidence intervals, consult the full compact CSVs.

## Paper 1 — Classical CV/GCV/AICc/BIC versus pooled uniform forecast-CV

| d | h | Method | Matched comparator | DGP cells | Median relative RMSE | Share of cells with ratio below 1 |
|---:|---:|---|---|---:|---:|---:|
| 2 | 1 | classical_aicc | pooled_uniform_all | 144 | 1.0080 | 27.8% |
| 2 | 1 | classical_bic | pooled_uniform_all | 144 | 2.2514 | 0.0% |
| 2 | 1 | classical_cv | pooled_uniform_all | 144 | 1.0480 | 2.1% |
| 2 | 1 | classical_gcv | pooled_uniform_all | 144 | 1.0624 | 1.4% |
| 2 | 3 | classical_aicc | pooled_uniform_all | 144 | 1.0293 | 14.6% |
| 2 | 3 | classical_bic | pooled_uniform_all | 144 | 3.5755 | 0.0% |
| 2 | 3 | classical_cv | pooled_uniform_all | 144 | 1.1030 | 2.8% |
| 2 | 3 | classical_gcv | pooled_uniform_all | 144 | 1.1345 | 2.1% |
| 2 | 6 | classical_aicc | pooled_uniform_all | 136 | 1.0463 | 11.0% |
| 2 | 6 | classical_bic | pooled_uniform_all | 136 | 5.6841 | 0.0% |
| 2 | 6 | classical_cv | pooled_uniform_all | 136 | 1.1992 | 2.2% |
| 2 | 6 | classical_gcv | pooled_uniform_all | 136 | 1.2654 | 2.2% |
| 2 | 12 | classical_aicc | pooled_uniform_all | 136 | 1.0811 | 11.8% |
| 2 | 12 | classical_bic | pooled_uniform_all | 136 | 9.4212 | 0.0% |
| 2 | 12 | classical_cv | pooled_uniform_all | 136 | 1.4289 | 2.9% |
| 2 | 12 | classical_gcv | pooled_uniform_all | 136 | 1.6200 | 2.2% |
| 3 | 1 | classical_aicc | pooled_uniform_all | 144 | 1.0372 | 4.2% |
| 3 | 1 | classical_bic | pooled_uniform_all | 144 | 4.0306 | 0.0% |
| 3 | 1 | classical_cv | pooled_uniform_all | 144 | 1.1261 | 0.7% |
| 3 | 1 | classical_gcv | pooled_uniform_all | 144 | 1.1716 | 0.7% |
| 3 | 3 | classical_aicc | pooled_uniform_all | 144 | 1.0944 | 9.7% |
| 3 | 3 | classical_bic | pooled_uniform_all | 144 | 11.5150 | 0.0% |
| 3 | 3 | classical_cv | pooled_uniform_all | 144 | 1.3871 | 0.0% |
| 3 | 3 | classical_gcv | pooled_uniform_all | 144 | 1.7272 | 0.0% |
| 3 | 6 | classical_aicc | pooled_uniform_all | 136 | 1.2500 | 2.9% |
| 3 | 6 | classical_bic | pooled_uniform_all | 136 | 29.5982 | 0.0% |
| 3 | 6 | classical_cv | pooled_uniform_all | 136 | 2.0239 | 0.0% |
| 3 | 6 | classical_gcv | pooled_uniform_all | 136 | 3.2239 | 0.0% |
| 3 | 12 | classical_aicc | pooled_uniform_all | 136 | 1.8098 | 2.9% |
| 3 | 12 | classical_bic | pooled_uniform_all | 136 | 83.9803 | 0.0% |
| 3 | 12 | classical_cv | pooled_uniform_all | 136 | 4.6676 | 0.0% |
| 3 | 12 | classical_gcv | pooled_uniform_all | 136 | 7.9542 | 0.0% |

## Paper 2 — Tracking versus pooled under the same temporal weighting

| d | h | Method | Matched comparator | DGP cells | Median relative RMSE | Share of cells with ratio below 1 |
|---:|---:|---|---|---:|---:|---:|
| 2 | 1 | tracked_recent_exp_8 | pooled_recent_exp_8 | 144 | 0.9422 | 86.1% |
| 2 | 1 | tracked_recent_linear_8 | pooled_recent_linear_8 | 144 | 0.9471 | 85.4% |
| 2 | 1 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 144 | 0.9681 | 84.0% |
| 2 | 1 | tracked_uniform_all | pooled_uniform_all | 144 | 0.9981 | 77.8% |
| 2 | 3 | tracked_recent_exp_8 | pooled_recent_exp_8 | 144 | 0.9709 | 95.8% |
| 2 | 3 | tracked_recent_linear_8 | pooled_recent_linear_8 | 144 | 0.9724 | 95.8% |
| 2 | 3 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 144 | 0.9849 | 95.8% |
| 2 | 3 | tracked_uniform_all | pooled_uniform_all | 144 | 0.9990 | 79.2% |
| 2 | 6 | tracked_recent_exp_8 | pooled_recent_exp_8 | 136 | 0.9847 | 94.1% |
| 2 | 6 | tracked_recent_linear_8 | pooled_recent_linear_8 | 136 | 0.9848 | 96.3% |
| 2 | 6 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 136 | 0.9914 | 93.4% |
| 2 | 6 | tracked_uniform_all | pooled_uniform_all | 136 | 0.9992 | 81.6% |
| 2 | 12 | tracked_recent_exp_8 | pooled_recent_exp_8 | 136 | 0.9911 | 91.9% |
| 2 | 12 | tracked_recent_linear_8 | pooled_recent_linear_8 | 136 | 0.9917 | 91.2% |
| 2 | 12 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 136 | 0.9946 | 86.8% |
| 2 | 12 | tracked_uniform_all | pooled_uniform_all | 136 | 0.9991 | 78.7% |
| 3 | 1 | tracked_recent_exp_8 | pooled_recent_exp_8 | 144 | 0.9353 | 92.4% |
| 3 | 1 | tracked_recent_linear_8 | pooled_recent_linear_8 | 144 | 0.9370 | 94.4% |
| 3 | 1 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 144 | 0.9709 | 90.3% |
| 3 | 1 | tracked_uniform_all | pooled_uniform_all | 144 | 0.9983 | 76.4% |
| 3 | 3 | tracked_recent_exp_8 | pooled_recent_exp_8 | 144 | 0.9654 | 95.1% |
| 3 | 3 | tracked_recent_linear_8 | pooled_recent_linear_8 | 144 | 0.9671 | 93.8% |
| 3 | 3 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 144 | 0.9813 | 91.7% |
| 3 | 3 | tracked_uniform_all | pooled_uniform_all | 144 | 0.9988 | 82.6% |
| 3 | 6 | tracked_recent_exp_8 | pooled_recent_exp_8 | 136 | 0.9760 | 83.8% |
| 3 | 6 | tracked_recent_linear_8 | pooled_recent_linear_8 | 136 | 0.9773 | 86.8% |
| 3 | 6 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 136 | 0.9849 | 91.9% |
| 3 | 6 | tracked_uniform_all | pooled_uniform_all | 136 | 0.9974 | 91.9% |
| 3 | 12 | tracked_recent_exp_8 | pooled_recent_exp_8 | 136 | 0.9893 | 75.7% |
| 3 | 12 | tracked_recent_linear_8 | pooled_recent_linear_8 | 136 | 0.9890 | 80.1% |
| 3 | 12 | tracked_recent_uniform_8 | pooled_recent_uniform_8 | 136 | 0.9935 | 71.3% |
| 3 | 12 | tracked_uniform_all | pooled_uniform_all | 136 | 0.9987 | 73.5% |

## Paper 3 — Numerical search on the same F(S) surfaces

| h | Diagnostic groups | Median grid regret | Median bounded-Brent regret | Median adaptive regret |
|---:|---:|---:|---:|---:|
| 3 | 120 | 0.000334971 | 2.3311e-06 | -6.50825e-05 |

## Reference comparison with naive

| d | h | DGP cells | Median pooled/naive RMSE | Share of cells with ratio below 1 |
|---:|---:|---:|---:|---:|
| 2 | 1 | 144 | 0.7677 | 88.2% |
| 2 | 3 | 144 | 0.7628 | 87.5% |
| 2 | 6 | 136 | 0.7652 | 92.6% |
| 2 | 12 | 136 | 0.7784 | 86.8% |
| 3 | 1 | 144 | 0.7811 | 87.5% |
| 3 | 3 | 144 | 0.7831 | 83.3% |
| 3 | 6 | 136 | 0.7973 | 77.9% |
| 3 | 12 | 136 | 0.8489 | 69.1% |

## Limits

- The experiment was stopped before its full seed allocation. 144 DGP cells have 696–704 finished seeds each; full cell-level detail is in coverage CSV.
- All retained findings are exploratory. Testing many methods and declaring a winner after seeing this external panel would need a NEW independent confirmation study.
- Confidence intervals for **paired MSFE differences** are computed across independently generated seeds **within each cell**; medians and win-shares across heterogeneous DGP cells are descriptive, not joint inferential confidence bands.
- Classical CV/GCV/AICc/BIC and P2 tracking do not model the new nonzero mean of differences; claims about that new estimator must await its independent pilot.
- Grid/Brent/adaptive minima are numerical comparisons; the dense-grid reference is not a universal global proof.
