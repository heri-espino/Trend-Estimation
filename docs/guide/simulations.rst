Simulations
===========

Synthetic data are part of the library because controlled experiments require a
known latent trend.

:func:`trend_estimation.make_local_linear_ar1_series` controls latent-trend
roughness, observation-noise scale, and AR(1) dependence separately.

:func:`trend_estimation.make_two_regime_local_linear_series` can change
roughness, noise scale, persistence, level, and slope at a known regime point.

When the latent trend is known,
:func:`trend_estimation.select_recovery_optimal_lambda` computes an oracle
recovery optimum. It is a simulation diagnostic, not a real-data tuning rule.
