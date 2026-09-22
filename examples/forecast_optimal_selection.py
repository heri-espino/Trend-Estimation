import trend_estimation as td

data = td.make_local_linear_ar1_series(
    n_obs=180,
    slope_noise_std=0.01,
    observation_noise_std=0.5,
    ar1_phi=0.4,
    random_state=11,
)

selection = td.select_fixed_window_pure_smoothness(
    data.y,
    orders=(1, 2, 3),
    windows=(24, 48, 72),
    horizon=3,
)

print(selection.best_)
