# Experiment 11 — Held-Out Financial Replication

Date designed: 2026-09-29

Status: **protocol frozen before inspecting replication outcomes**

## Motivation

The development panel has already informed the move from literal
observation-count windows to a frequency-aware policy. It must therefore not
be used as a confirmatory test of that policy.

This experiment freezes a separate financial panel before its outcomes are
inspected.

## Frozen method

Use exactly the frequency-aware daily policy selected during development:

- orders: {1,2,3};
- windows: {63,126,252};
- selector memory: M=51;
- inner step: 5;
- log-lambda range: [-18,24];
- 321-point discovery grid;
- final 40% chronological OOS evaluation;
- primary comparator: frozen-all-pre;
- secondary comparator: frozen-local with the same M=51;
- external benchmark: no-change.

No candidate-grid changes are permitted after seeing replication results.

## Frozen replication universe

### ETFs

- VTI — total US equity market;
- XLK — technology sector;
- XLF — financial sector;
- XLE — energy sector;
- XLV — health-care sector;
- VNQ — real estate.

### Stocks

- KO;
- PG;
- CVX;
- BAC;
- CAT;
- HD.

### Crypto

- LTC-USD;
- XRP-USD.

None of these series appeared in the development panel.

## Horizons

- ETFs/stocks: h in {1,5,20} trading observations;
- crypto: h in {1,7,30} daily observations.

## Interpretation

The replication panel tests whether the development conclusion generalizes:

1. frequency-aware scaling should be treated as fixed;
2. broad adaptive superiority is not assumed;
3. near-ties and failures are scientifically valid outcomes;
4. the no-change boundary is central for price levels.

The main confirmatory quantities are pooled adaptive/frozen-all-pre and
adaptive/no-change RMSFE by series/horizon and class-level medians.

## Commands

Smoke:

```bash
python experiments/forecast_optimal_smoothing/run_real_data_validation.py --panel replication --preset smoke --scale-policy frequency-aware --workers 3
```

Replication run:

```bash
python experiments/forecast_optimal_smoothing/run_real_data_validation.py --panel replication --preset explore --scale-policy frequency-aware --workers 32
```

The runner downloads any missing replication series once and then reuses the
tracked snapshot.
