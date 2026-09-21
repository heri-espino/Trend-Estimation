import numpy as np

import trend_estimation as td


def test_guerrero_default_matches_published_plugin_formula():
    y = np.array([0.2, 0.9, 1.7, 3.1, 4.6, 7.0, 10.1, 13.9], dtype=float)
    order = 2
    lambda_ = 3.5

    model = td.GuerreroTrend(order=order, lambda_=lambda_).fit(y)

    D = td.difference_matrix(len(y), order)
    Q = D.T @ D
    ones = np.ones(D.shape[0], dtype=float)
    m_hat = float(np.mean(D @ y))
    rhs = y + lambda_ * m_hat * (D.T @ ones)
    expected = np.linalg.solve(np.eye(len(y)) + lambda_ * Q, rhs)

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


def test_legacy_estimate_drift_boolean_remains_reproducible():
    y = np.linspace(0.0, 4.0, 15) ** 2

    model = td.PenalizedTrend(
        order=2,
        lambda_=2.0,
        estimate_drift=True,
    ).fit(y)
    assert model.drift_mode_ == "iterated"

    zero = td.PenalizedTrend(
        order=2,
        lambda_=2.0,
        estimate_drift=False,
    ).fit(y)
    assert zero.drift_mode_ == "zero"
