# Frozen formal8h audit — three papers

- Original Git revision: `21bd563146e04eb545cae56b46393d93a9d98212`.
- Completed independent scenario/seed tasks: **100,848** / 144,000.
- Distinct DGP cells: **144**; min/max complete seeds per cell: 696/704.
- No new generated observations, Monte Carlo, CUDA or refits.
- All inference is **exploratory** after a truncated run; multiple methods compared on one common external test panel.

## Integrity

- Every scenario cell has one coverage row; summed seeds equal the completed-task manifest.
- Method/comparator pairs are the expected predeclared matching rules; stored relative RMSE equals sqrt(method MSFE / comparator MSFE).
- Underlying comparisons use within-seed matched outer origins, and independent Monte Carlo seeds within a DGP form each standard-error sample.
- Statistical cells: P1=10,080; P2=5,600. Holm FWER corrections applied separately over ALL predeclared scenario contrasts within each paper.

## Key caveats

- The tests audit consistency of stored aggregated values; they do **not** independently regenerate raw forecast errors from the original time series.
- Holm-adjusted p-values on a post hoc explored dataset do not turn this into an independent confirmation study.
- The strong BIC anomalies may reflect horizon-amplified polynomial extrapolation, score normalization or boundary selection; inspect existing S/EDF tables, not only the RMSE ratio.
- Tracking includes temporal mean-K of branch S, so the unrun global-S moving-average control remains necessary to attribute the gains uniquely to branch identities.
- P3 diagnostics compare with a **finite dense numerical grid**, not an exact global minimum. Negative regret is permitted.

## Existing S and EDF diagnostics

The local scenario/method table was found and 48 summaries of S, EDF, local-minimum count and branch support were written to smoothing_edf_diagnostics.csv. These are scenario-level medians of values already averaged over seeds and origins; they cannot measure single-origin boundary hit rates.

## Numerical audit

{
  "cases": 50424,
  "groups": 120,
  "horizons": [
    3
  ],
  "weighting_methods": [
    "recent_exp_8",
    "uniform_all"
  ],
  "fraction_adaptive_F_below_dense_grid": 0.6974853244486753,
  "fraction_adaptive_outer_msfe_below_grid": 0.3550690147548786
}

## Details

Read `PAPER1_AUDIT.md`, `PAPER2_AUDIT.md` and `PAPER3_AUDIT.md`, plus `comparison_tests.csv`, `group_heterogeneity.csv`, `extreme_cases.csv`, `smoothing_edf_diagnostics.csv` if available, and `numerical_paired_summary.csv` if the local frozen SQLite snapshot was supplied.
