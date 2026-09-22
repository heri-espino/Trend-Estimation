import trend_estimation as td

data = td.make_local_linear_ar1_series(
    n_obs=220,
    slope_noise_std=0.01,
    observation_noise_std=0.5,
    ar1_phi=0.4,
    random_state=19,
)

result = td.nested_rolling_pure_forecast(
    data.y,
    outer_initial_train=120,
    horizon=3,
    outer_step=3,
    orders=(1, 2, 3),
    windows=(24, 48, 72),
)

print("RMSE:", result.rmse)
print("relative RMSFE:", result.relative_rmsfe)
