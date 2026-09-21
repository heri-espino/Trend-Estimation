import numpy as np

import trend_estimation as td


def test_pure_forecast_loss_derivatives_match_finite_differences():
    y_past = np.array([0.1, 0.7, 1.8, 3.2, 5.1, 7.4, 10.2, 13.5], dtype=float)
    y_future = np.array([17.2, 21.4, 26.0], dtype=float)
    order = 2
    lambda_ = 2.5
    step = 1e-4

    analytic = td.pure_forecast_loss_derivatives(
        y_past,
        y_future,
        order=order,
        lambda_=lambda_,
    )

    f_plus = td.pure_forecast_loss_derivatives(
        y_past,
        y_future,
        order=order,
        lambda_=lambda_ + step,
    ).value
    f_minus = td.pure_forecast_loss_derivatives(
        y_past,
        y_future,
        order=order,
        lambda_=lambda_ - step,
    ).value

    first_fd = (f_plus - f_minus) / (2.0 * step)
    second_fd = (f_plus - 2.0 * analytic.value + f_minus) / (step * step)

    assert np.isclose(analytic.first, first_fd, rtol=2e-5, atol=2e-7)
    assert np.isclose(analytic.second, second_fd, rtol=2e-3, atol=2e-5)


def test_rolling_forecast_derivatives_equal_observation_weighted_pool():
    y = np.arange(24, dtype=float) ** 1.25
    splits = td.rolling_origin_splits(
        len(y),
        initial_train=12,
        horizon=3,
        step=4,
    )
    order = 2
    lambda_ = 4.0

    pooled = td.rolling_pure_forecast_loss_derivatives(
        y,
        splits,
        order=order,
        lambda_=lambda_,
    )

    pieces = [
        td.pure_forecast_loss_derivatives(
            y[split.train],
            y[split.validation],
            order=order,
            lambda_=lambda_,
        )
        for split in splits
    ]
    weights = np.array(
        [split.validation.stop - split.validation.start for split in splits],
        dtype=float,
    )

    assert pooled.n_origins == len(splits)
    assert pooled.n_scored == int(weights.sum())
    assert np.isclose(pooled.value, np.average([p.value for p in pieces], weights=weights))
    assert np.isclose(pooled.first, np.average([p.first for p in pieces], weights=weights))
    assert np.isclose(pooled.second, np.average([p.second for p in pieces], weights=weights))
