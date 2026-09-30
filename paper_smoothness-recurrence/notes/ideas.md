# Ideas and Open Questions

Items here are not part of the paper until promoted into the roadmap and
decisions log.

## Numerical

- Adaptive subdivision on (S\in[0,1]) using derivative sign, near-zero
  derivative, and curvature.
- Warm-start (lambda(S)) inversion from neighboring evaluations.
- Spectral caching by ((N,d)).
- Compare adaptive isolation with multi-start Newton/Halley.
- Investigate derivative bounds that could certify root-free intervals.
- Use the dense GPU grid to estimate empirical missed-root probability.
- Treat the number/depth of local minima as a property of the CV surface.

## Statistical

- Primary scale likely log price.
- Standardized displacement
  (z_T=(x_T-\widehat\tau_T)/\widehat\sigma_T).
- Estimate (P(R_T\le k\mid z_T)).
- Survival curves for censored recurrence times.
- Hazard as a function of distance, trend slope, volatility, and horizon.
- Separate positive and negative deviations.
- Study whether (h\mapsto S_h^\star) has a smooth term structure.

## Financial extensions

- ETFs/indices as primary application.
- Individual equities as robustness.
- Crypto as stress test.
- Price-trend vs. return-trend recurrence as separate analyses.
- Event-study future returns after large trend deviations.
- Trading interpretation only in future work with costs and a pre-specified
  strategy.

## Possible figures

1. (S\mapsto CV_h(S)) with all local minima.
2. Adaptive evaluation points over dense reference curve.
3. Runtime/evaluation counts: adaptive vs. dense.
4. (h\mapsto S_h^\star).
5. Forecast trend and first crossing examples.
6. Recurrence probability vs. standardized distance.
7. Survival curves by distance bin or asset class.
