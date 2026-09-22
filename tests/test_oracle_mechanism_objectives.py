import numpy as np

import trend_estimation as td


def test_latent_target_objective_changes_targets_not_fit_series():
    x = np.arange(40, dtype=float)
    latent = 0.02 * x**2
    y = latent + 0.2 * np.sin(x)
    splits = [
        td.RollingOriginSplit(slice(5, 25), slice(25, 28)),
        td.RollingOriginSplit(slice(8, 28), slice(28, 31)),
    ]

    observed = td.prepare_rolling_pure_forecast_objective(
        y,
        splits,
        order=2,
    ).evaluate(3.0)
    latent_target = td.prepare_rolling_pure_forecast_objective(
        y,
        splits,
        order=2,
        target_series=latent,
    ).evaluate(3.0)

    assert observed.n_scored == latent_target.n_scored
    assert not np.isclose(observed.value, latent_target.value)


def test_oracle_ar_objective_matches_manual_forecasts():
    rng = np.random.default_rng(5)
    y = np.cumsum(rng.normal(size=50))
    splits = [
        td.RollingOriginSplit(slice(10, 30), slice(30, 33)),
        td.RollingOriginSplit(slice(14, 34), slice(34, 37)),
    ]
    phi = 0.7
    lambda_ = 2.5

    prepared = td.prepare_rolling_pure_forecast_objective(
        y,
        splits,
        order=2,
        residual_ar_phi=phi,
    ).evaluate(lambda_)

    errors = []
    for split in splits:
        train = y[split.train]
        future = y[split.validation]
        model = td.PurePenalizedTrend(
            order=2,
            smoothness=None,
            lambda_=lambda_,
        ).fit(train)
        trend_forecast = model.forecast(len(future))
        last_residual = train[-1] - model.trend_[-1]
        powers = phi ** np.arange(1, len(future) + 1)
        prediction = trend_forecast + powers * last_residual
        errors.extend((future - prediction) ** 2)

    assert np.isclose(prepared.value, np.mean(errors), rtol=1e-11, atol=1e-11)


def test_prepared_recovery_matches_direct_average():
    x = np.arange(45, dtype=float)
    latent = 0.01 * x**2
    y = latent + 0.1 * np.cos(x)
    splits = [
        td.RollingOriginSplit(slice(5, 25), slice(25, 28)),
        td.RollingOriginSplit(slice(10, 30), slice(30, 33)),
    ]
    lambda_ = 4.0

    prepared = td.prepare_rolling_pure_recovery_objective(
        y,
        latent,
        splits,
        order=2,
    ).evaluate(lambda_)

    errors = []
    for split in splits:
        model = td.PurePenalizedTrend(
            order=2,
            smoothness=None,
            lambda_=lambda_,
        ).fit(y[split.train])
        errors.extend((latent[split.train] - model.trend_) ** 2)

    assert np.isclose(prepared.value, np.mean(errors), rtol=1e-11, atol=1e-11)
