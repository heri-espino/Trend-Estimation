import numpy as np

import trend_estimation as td


def test_recovery_loss_derivatives_match_finite_differences():
    rng = np.random.default_rng(19)
    true_trend = np.linspace(0.0, 3.0, 30) ** 1.4
    y = true_trend + rng.normal(0.0, 0.4, size=true_trend.size)

    order = 2
    lambda_ = 3.0
    step = 1e-4

    analytic = td.pure_recovery_loss_derivatives(
        y,
        true_trend,
        order=order,
        lambda_=lambda_,
    )

    f_plus = td.pure_recovery_loss_derivatives(
        y,
        true_trend,
        order=order,
        lambda_=lambda_ + step,
    ).value
    f_minus = td.pure_recovery_loss_derivatives(
        y,
        true_trend,
        order=order,
        lambda_=lambda_ - step,
    ).value

    first_fd = (f_plus - f_minus) / (2.0 * step)
    second_fd = (f_plus - 2.0 * analytic.value + f_minus) / (step * step)

    assert np.isclose(analytic.first, first_fd, rtol=2e-5, atol=2e-7)
    assert np.isclose(analytic.second, second_fd, rtol=2e-3, atol=2e-5)


def test_recovery_selector_returns_positive_lambda_and_valid_smoothness():
    data = td.make_local_linear_ar1_series(
        n_obs=60,
        slope_noise_std=0.01,
        observation_noise_std=0.4,
        ar1_phi=0.3,
        random_state=3,
    )

    result = td.select_recovery_optimal_lambda(
        data.y,
        data.true_trend,
        order=2,
        log_bounds=(-6.0, 8.0),
        n_grid=61,
    )

    assert result.lambda_ > 0.0
    assert 0.0 <= result.smoothness_ < 1.0
    assert result.objective_ >= 0.0
