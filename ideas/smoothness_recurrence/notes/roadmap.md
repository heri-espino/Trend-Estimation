# Roadmap — Parked Applied Paper

**Do not execute this roadmap until
paper_numerical-methods/ is finished.**

## Phase 0 — Separation

**Status: complete.**

- [x] move numerical-method ownership to the numerical paper;
- [x] retain this paper as the applied comparison/recurrence track;
- [x] freeze this paper while numerical work is active.

## Phase 1 — Freeze data and information sets

- [ ] choose primary financial scale;
- [ ] freeze development/validation/test chronology;
- [ ] freeze asset panels;
- [ ] freeze forecast origins and horizons;
- [ ] freeze loss metrics.

## Phase 2 — Freeze model comparison

- [ ] forecast-optimal PLS from the finished numerical paper;
- [ ] GCV PLS;
- [ ] likelihood/state-space;
- [ ] AR(\(p\))/ARIMA;
- [ ] PLS + AR residual;
- [ ] no-change/random walk;
- [ ] remove redundant models before final runs.

## Phase 3 — Forecast comparison

Report validation and untouched-test performance using identical forecast
origins and losses. Validation may select model-specific hyperparameters; final
test outcomes never feed back into model selection.

## Phase 4 — Recurrence definitions

- [ ] crossing time;
- [ ] tolerance-band entry;
- [ ] standardized initial deviation;
- [ ] right censoring at frozen \(H_{\max}\);
- [ ] recurrence probabilities by horizon;
- [ ] median/restricted-mean time to recurrence;
- [ ] survival/hazard summaries if warranted.

## Phase 5 — Dependence and robustness

- [ ] non-overlapping/spaced origins;
- [ ] block/bootstrap or clustered uncertainty;
- [ ] positive versus negative deviations;
- [ ] asset-class comparisons;
- [ ] sensitivity to trend definition.

## Phase 6 — Manuscript

Target narrative:

1. competing definitions of forecast trend;
2. fair chronological comparison;
3. untouched forecast performance;
4. recurrence as a first-passage object;
5. robustness of recurrence to the trend definition;
6. limitations.

The paper is applied. Do not turn it back into a numerical-method paper.
