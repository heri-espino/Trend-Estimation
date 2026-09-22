import numpy as np

import trend_estimation as td


def test_guerrero_default_matches_published_plugin_formula():
    y = np.array([0.2, 0.9, 1.7, 3.1, 4.6, 7.0, 10.1, 13.9], dtype=float)
    order = 2
    lambda_ = 3.5

    model = td.GuerreroTrend(order=order, lambda_=lambda_).fit(y)

    difference = td.difference_matrix(len(y), order)
    penalty = difference.T @ difference
    ones = np.ones(difference.shape[0], dtype=float)
    m_hat = float(np.mean(difference @ y))
    rhs = y + lambda_ * m_hat * (difference.T @ ones)
    expected = np.linalg.solve(np.eye(len(y)) + lambda_ * penalty, rhs)

    assert model.drift_mode_ == "data"
    assert np.isclose(model.m_hat_, m_hat)
    assert np.allclose(model.trend_, expected, rtol=1e-10, atol=1e-10)
    assert model.fit_result_.metadata_["model"] == "guerrero_plugin"


def test_iterated_drift_variant_is_explicitly_named():
    y = np.array([0.2, 0.9, 1.7, 3.1, 4.6, 7.0, 10.1, 13.9], dtype=float)
    plugin = td.GuerreroTrend(order=2, lambda_=8.0).fit(y)
    legacy = td.IteratedDriftTrend(order=2, lambda_=8.0).fit(y)

    assert plugin.drift_mode_ == "data"
    assert legacy.drift_mode_ == "iterated"
    assert not np.isclose(plugin.m_hat_, legacy.m_hat_)
