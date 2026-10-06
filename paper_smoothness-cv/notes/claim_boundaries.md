> **2026-10-06 override:** Dynamic tracking of local smoothness minima is now
> central to this paper. Any older statement below assigning time-varying
> smoothness to another paper is superseded. The numerical recovery/tracking
> algorithm belongs to `paper_numerical-methods/`; the forecasting decision
> from tracked branches belongs here.

# Claim boundaries

## Safe

- Forecast-optimal smoothness is conditional on estimator family, difference order, window, horizon, continuation rule, loss, and validation protocol.
- Normalized smoothness is a monotone reparameterization of penalty strength under stated assumptions.
- Forecast-optimal and recovery-optimal smoothness are different targets and may differ.
- Selected smoothness may depend on horizon and data-generating mechanism.
- Chronological scoring prevents future observations from entering the fit at the same origin.

## Not safe without additional work

- "First predictive smoothing-parameter selector."
- "First forecast-based smoothness method."
- Universal superiority over GCV/AIC/BIC/marginal likelihood.
- \(S^\star\) as a universal/population-optimal amount of smoothness.
- Forecast optimality outside the stated family/protocol.
- Causal interpretation.
- Financial predictability/economic value from illustrative price series.

## Scope discipline

If the paper starts jointly learning \(d,L,S\) by regime, it belongs to paper_forecast-optimal-smoothing/.

If it starts focusing on Brent, adaptive root discovery, Sturm, or evaluation counts, it belongs to paper_numerical-methods/.
