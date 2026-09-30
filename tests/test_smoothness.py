import numpy as np

import trend_estimation as td


def test_smoothness_round_trip():
    lam = td.smoothness_to_lambda(0.5, 40, 2)
    s = td.lambda_to_smoothness(lam, 40, 2)
    assert abs(s - 0.5) < 1e-6


def test_smoothness_derivatives_match_finite_differences():
    lambda_ = 3.0
    n_obs = 40
    order = 2
    first, second = td.smoothness_derivatives(lambda_, n_obs, order)

    step = 1e-4
    s_minus = td.lambda_to_smoothness(lambda_ - step, n_obs, order)
    s_zero = td.lambda_to_smoothness(lambda_, n_obs, order)
    s_plus = td.lambda_to_smoothness(lambda_ + step, n_obs, order)
    first_fd = (s_plus - s_minus) / (2.0 * step)
    second_fd = (s_plus - 2.0 * s_zero + s_minus) / (step * step)

    assert np.isclose(first, first_fd, rtol=1e-5, atol=1e-8)
    assert np.isclose(second, second_fd, rtol=2e-3, atol=1e-6)


def test_exact_smoothness_endpoints_map_to_zero_and_infinity():
    assert td.smoothness_to_lambda(0.0, 40, 2) == 0.0
    assert np.isinf(td.smoothness_to_lambda(1.0, 40, 2))
    assert td.lambda_to_smoothness(np.inf, 40, 2) == 1.0
