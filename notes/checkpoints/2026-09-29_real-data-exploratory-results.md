# Checkpoint — First Real-Data External-Validation Screen

Date: 2026-09-29

Status: **COMPLETED; negative external-transfer result, followed by a scale-design diagnostic**

Result:

`results/forecast_optimal_smoothing/20260929T091259Z_real-data-explore_cc46a3f/`

Result commit:

`f38b9ad` — `results: add real-data exploratory validation`

## Run integrity

The exploratory screen completed:

- 16 observed series;
- 49 series/horizon cells;
- 10,160 untouched OOS forecast blocks;
- 32 workers;
- 321-point lambda discovery grid;
- primary fixed comparator: frozen-all-pre;
- secondary diagnostic comparator: frozen-local-M20;
- external benchmark: no-change;
- log-level target;
- final 40% of each history used for chronological OOS evaluation.

The data snapshot used by the experiment was subsequently preserved in Git.

## Main result

The direct transfer of the simulation protocol does **not** outperform the
strong fixed comparator broadly in observed data.

Class-level medians:

| class | median adaptive/frozen-all-pre RMSFE | cells adaptive < fixed | median adaptive/no-change RMSFE | cells adaptive < no-change |
|---|---:|---:|---:|---:|
| macro | 1.357 | 1/7 | 1.487 | 1/7 |
| ETF | 1.108 | 2/18 | 1.099 | 2/18 |
| stock | 1.122 | 1/18 | 1.122 | 1/18 |
| crypto | 1.100 | 0/6 | 1.100 | 0/6 |

This is a real external-validity boundary and must not be hidden.

## Positive cells

Only a small number of cells beat both frozen-all-pre and no-change:

- GDPC1, h=4 quarters:
  adaptive/fixed = 0.850, adaptive/no-change = 0.862;
- SPY, h=20 trading observations:
  adaptive/fixed = 0.989, adaptive/no-change = 0.965;
- EEM, h=5:
  adaptive/fixed = 0.989, adaptive/no-change = 0.989;
- JPM, h=1:
  adaptive/fixed = 0.911, adaptive/no-change = 0.911.

These isolated cells are not evidence of broad superiority and must not be
cherry-picked as the external conclusion.

## Time-split diagnostic

The negative market result is not driven by only one third of the OOS period.

For ETFs, stocks, and crypto, pooled adaptive/fixed ratios remain above one in
nearly every early/mid/late × horizon group.

Macro is more heterogeneous. In particular, long-horizon GDP has a favorable
late-period result, while pooled monthly industrial production strongly favors
the fixed/no-change alternatives.

## Selector-path diagnostic

The adaptive discrete configuration changes frequently between consecutive
evaluated origins:

| class | mean (d,L) turnover | order turnover | window turnover |
|---|---:|---:|---:|
| macro | 0.325 | 0.092 | 0.296 |
| ETF | 0.460 | 0.161 | 0.410 |
| stock | 0.456 | 0.134 | 0.411 |
| crypto | 0.384 | 0.107 | 0.339 |

For daily ETFs and stocks, almost half of evaluated origins change at least
one of (d,L), with window length responsible for most turnover.

This is consistent with a noisy local selector, but turnover alone does not
prove that selector instability causes the forecast losses.

The frozen-local-M20 comparator is also much less stable than frozen-all-pre in
several cells (for example long-horizon QQQ, WMT, INDPRO), which provides a
second diagnostic that short validation memory can be fragile in observed
series.

## Critical design issue discovered

The first real-data screen deliberately copied the simulation candidate set

[
Lin{24,48,72},qquad M=20
]

to every frequency.

That makes the *calendar meaning* of the adaptive object very different by
series class:

- GDP: 24--72 quarters = 6--18 years;
- INDPRO: 24--72 months = 2--6 years;
- daily markets: 24--72 observations is only about 1--3.5 trading months.

Likewise, M=20 inner origins spans very different effective history because the
inner step differs by class.

This matters because the scientific object is explicitly

[
Theta^star_{T,h}=G(h,X_T,mathcal C),
]

so the admissible scale of L can legitimately depend on series class
(mathcal C). Equal observation counts are not automatically equal scientific
scales across quarterly, monthly, and daily data.

## Next diagnostic: frequency-aware scale policy

Do **not** delete or supersede the first result.

Run a pre-documented scale sensitivity using:

- quarterly GDP windows: {12,24,48};
- monthly INDPRO windows: {24,60,120};
- daily ETF/stock/crypto windows: {63,126,252};
- selector-memory span approximately one longest candidate window:
  M=max(20, ceil(L_max / inner_step)).

This gives:

- GDP: M=48;
- INDPRO: M=120;
- daily series: M=51 with inner step 5.

The purpose is to test whether the negative transfer result is specific to an
observation-count scale inherited from simulation. It is **not** a license to
search candidate grids until adaptive wins.

The original observation-scale result remains part of the audit trail.

## Macro caveat

GDPC1 and INDPRO in this screen are current-vintage FRED histories. Their
results remain exploratory until repeated using ALFRED real-time vintages.

## Scientific interpretation so far

The controlled-simulation result does not automatically transfer to observed
series. Under the literal simulation-scale protocol, adaptive M20 is generally
worse than a strong frozen-all-pre configuration and often worse than
no-change.

The next valid question is whether this is:

1. a genuine external-validity failure of adaptive trend selection, or
2. partly a scale mismatch caused by applying identical observation-count
   windows and selector memory across very different sampling frequencies.

The frequency-aware diagnostic is designed to distinguish these explanations
without discarding the negative first screen.
