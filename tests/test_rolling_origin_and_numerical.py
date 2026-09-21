import numpy as np

import trend_estimation as td


def test_rolling_origin_splits_are_chronological():
    splits = td.rolling_origin_splits(20, initial_train=10, horizon=3, step=2)
    assert len(splits) == 4
    for split in splits:
        assert split.train.stop <= split.validation.start
        assert split.validation.stop <= 20


def test_rolling_window_keeps_requested_width():
    splits = td.rolling_origin_splits(
        20,
        initial_train=8,
        horizon=2,
        step=3,
        expanding=False,
        train_window=5,
    )
    assert all((s.train.stop - s.train.start) == 5 for s in splits)


def test_log_lambda_minimization_recovers_positive_optimum():
    result = td.minimize_over_log_lambda(
        lambda lmb: (np.log(lmb) - np.log(3.0)) ** 2,
        log_bounds=(-5.0, 5.0),
    )
    assert result.converged_
    assert np.isclose(result.lambda_, 3.0, rtol=1e-5)


def test_bracketed_stationary_search_finds_multiple_extrema():
    # In theta = log(lambda), h(theta) = (theta^2 - 1)^2 has
    # minima at theta=-1,+1 and a maximum at theta=0.
    def value_grad_hess(lambda_):
        theta = np.log(lambda_)
        value = (theta * theta - 1.0) ** 2
        h1 = 4.0 * theta * (theta * theta - 1.0)
        h2 = 12.0 * theta * theta - 4.0
        grad = h1 / lambda_
        hess = (h2 - h1) / (lambda_ * lambda_)
        return value, grad, hess

    result = td.find_stationary_points_log_lambda(
        value_grad_hess,
        log_bounds=(-2.0, 2.0),
        n_grid=81,
    )

    minima = sorted(point.theta_ for point in result.points_ if point.kind_ == "minimum")
    maxima = sorted(point.theta_ for point in result.points_ if point.kind_ == "maximum")

    assert len(minima) == 2
    assert np.allclose(minima, [-1.0, 1.0], atol=1e-8)
    assert len(maxima) == 1
    assert np.allclose(maxima, [0.0], atol=1e-8)
    assert np.isclose(result.best_objective_, 0.0, atol=1e-12)
    assert np.isclose(abs(result.best_theta_), 1.0, atol=1e-8)
