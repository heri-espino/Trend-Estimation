import numpy as np

import trend_estimation as td


def test_affine_forecast_operator_matches_recursive_forecast():
    rng = np.random.default_rng(20260921)

    for n_fit in (3, 8):
        trend = rng.normal(size=n_fit)
        for order in (0, 1, 2, 3):
            for steps in (1, 5):
                for m_hat in (0.0, 0.25):
                    operator = td.finite_difference_forecast_operator(
                        n_fit=n_fit,
                        order=order,
                        steps=steps,
                    )
                    matrix_forecast = operator.apply(trend, m_hat=m_hat)
                    recursive_forecast = td.forecast_trend(
                        trend,
                        order=order,
                        m_hat=m_hat,
                        steps=steps,
                    )
                    assert np.allclose(
                        matrix_forecast,
                        recursive_forecast,
                        rtol=1e-12,
                        atol=1e-12,
                    )


def test_pure_forecast_operator_is_linear():
    rng = np.random.default_rng(11)
    a = rng.normal(size=10)
    b = rng.normal(size=10)
    c1, c2 = 1.7, -0.4

    operator = td.finite_difference_forecast_operator(
        n_fit=10,
        order=2,
        steps=4,
    )
    lhs = operator.apply(c1 * a + c2 * b, m_hat=0.0)
    rhs = c1 * operator.apply(a, m_hat=0.0) + c2 * operator.apply(b, m_hat=0.0)

    assert np.allclose(lhs, rhs, rtol=1e-12, atol=1e-12)
