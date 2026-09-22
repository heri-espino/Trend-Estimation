import numpy as np

import trend_estimation as td


def test_local_linear_ar1_series_is_reproducible_and_has_known_trend():
    a = td.make_local_linear_ar1_series(
        n_obs=80,
        slope_noise_std=0.01,
        observation_noise_std=0.5,
        ar1_phi=0.6,
        random_state=7,
    )
    b = td.make_local_linear_ar1_series(
        n_obs=80,
        slope_noise_std=0.01,
        observation_noise_std=0.5,
        ar1_phi=0.6,
        random_state=7,
    )

    assert np.allclose(a.y, b.y)
    assert np.allclose(a.true_trend, b.true_trend)
    assert a.y.shape == a.true_trend.shape == (80,)
    assert a.metadata["ar1_phi"] == 0.6


def test_two_regime_generator_changes_parameters_independently():
    data = td.make_two_regime_local_linear_series(
        n_obs=100,
        regime_point=60,
        pre_slope_noise_std=0.0,
        post_slope_noise_std=0.0,
        pre_observation_noise_std=0.2,
        post_observation_noise_std=0.8,
        pre_ar1_phi=0.0,
        post_ar1_phi=0.7,
        level_shift=2.0,
        slope_shift=0.1,
        random_state=11,
    )

    assert data.metadata["regime_point"] == 60
    assert data.metadata["pre_observation_noise_std"] == 0.2
    assert data.metadata["post_observation_noise_std"] == 0.8
    assert data.metadata["pre_ar1_phi"] == 0.0
    assert data.metadata["post_ar1_phi"] == 0.7

    no_shift = td.make_two_regime_local_linear_series(
        n_obs=100,
        regime_point=60,
        pre_slope_noise_std=0.0,
        post_slope_noise_std=0.0,
        pre_observation_noise_std=0.2,
        post_observation_noise_std=0.8,
        pre_ar1_phi=0.0,
        post_ar1_phi=0.7,
        level_shift=0.0,
        slope_shift=0.1,
        random_state=11,
    )
    assert np.isclose(
        data.true_trend[60] - no_shift.true_trend[60],
        2.0,
    )


def test_ar1_phi_requires_stationarity():
    for phi in (-1.0, 1.0, 1.2):
        try:
            td.make_local_linear_ar1_series(ar1_phi=phi)
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError for nonstationary AR(1) coefficient.")
