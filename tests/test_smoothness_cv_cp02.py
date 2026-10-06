import numpy as np

from experiments.smoothness_cv.common import (
    latent_forecast_oracle_curve,
    latent_trend,
    smoothness_grid,
)


def test_cp02_trend_mechanisms_are_finite_and_length_preserving():
    names = (
        "quadratic",
        "turning_point",
        "recent_slope_change",
        "oscillatory",
        "terminal_bend",
    )
    for name in names:
        trend = latent_trend(120, name)
        assert trend.shape == (120,)
        assert np.all(np.isfinite(trend))


def test_latent_forecast_oracle_curve_is_finite():
    n = 80
    trend = latent_trend(n, "quadratic")
    rng = np.random.default_rng(0)
    observed = trend + rng.normal(0.0, 0.2, size=n)

    grid = smoothness_grid(31)
    values = latent_forecast_oracle_curve(
        observed[:60],
        trend[60:66],
        order=2,
        s_grid=grid,
    )

    assert values.shape == grid.shape
    assert np.all(np.isfinite(values))
    assert np.min(values) >= 0.0
