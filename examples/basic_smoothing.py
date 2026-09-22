import trend_estimation as td

data = td.make_local_linear_ar1_series(
    n_obs=160,
    observation_noise_std=0.4,
    ar1_phi=0.3,
    random_state=7,
)

model = td.PurePenalizedTrend(order=2, lambda_=10.0).fit(data.y)

print("lambda:", model.lambda_)
print("forecast:", model.forecast(5))
