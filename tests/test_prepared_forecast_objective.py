import numpy as np

import trend_estimation as td


def test_prepared_rolling_objective_matches_direct_origin_average():
    x = np.arange(50, dtype=float)
    y = 0.02 * x**2 + 0.1 * np.sin(x / 3.0)
    splits = [
        td.RollingOriginSplit(slice(10, 30), slice(30, 33)),
        td.RollingOriginSplit(slice(14, 34), slice(34, 37)),
        td.RollingOriginSplit(slice(18, 38), slice(38, 41)),
    ]

    prepared = td.prepare_rolling_pure_forecast_objective(y, splits, order=2)

    for lambda_ in (0.01, 1.0, 100.0):
        fast = prepared.evaluate(lambda_)
        rows = [
            td.pure_forecast_loss_derivatives(
                y[split.train],
                y[split.validation],
                order=2,
                lambda_=lambda_,
            )
            for split in splits
        ]

        assert np.isclose(fast.value, np.mean([row.value for row in rows]), rtol=1e-11, atol=1e-11)
        assert np.isclose(fast.first, np.mean([row.first for row in rows]), rtol=1e-11, atol=1e-11)
        assert np.isclose(fast.second, np.mean([row.second for row in rows]), rtol=1e-11, atol=1e-11)


def test_cached_solver_is_reused():
    from trend_estimation.core.pure import cached_pure_solver

    assert cached_pure_solver(40, 2) is cached_pure_solver(40, 2)
