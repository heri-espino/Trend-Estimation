from trend_estimation.datasets.synthetic import (
    SyntheticTrendData,
    make_polynomial_trend_series,
    make_noisy_trend_series,
    make_piecewise_trend_series,
    make_sinusoidal_trend_series,
    make_local_linear_trend_series,
    make_structural_break_series,
)

__all__ = [
    "SyntheticTrendData",
    "make_polynomial_trend_series",
    "make_noisy_trend_series",
    "make_piecewise_trend_series",
    "make_sinusoidal_trend_series",
    "make_local_linear_trend_series",
    "make_structural_break_series",
    "make_local_linear_ar1_series",
    "make_two_regime_local_linear_series",
]

from trend_estimation.datasets.regime import (
    make_local_linear_ar1_series,
    make_two_regime_local_linear_series,
)
