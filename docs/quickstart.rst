Quick start
===========

Fit a penalized trend
---------------------

.. code-block:: python

   import trend_estimation as td

   data = td.make_local_linear_ar1_series(
       n_obs=200,
       observation_noise_std=0.4,
       ar1_phi=0.3,
       random_state=7,
   )

   model = td.PurePenalizedTrend(order=2, lambda_=10.0).fit(data.y)
   forecast = model.forecast(5)

Select forecast-optimal smoothness
----------------------------------

.. code-block:: python

   selection = td.select_fixed_window_pure_smoothness(
       data.y,
       orders=(1, 2, 3),
       windows=(24, 48, 72),
       horizon=3,
   )

   print(selection.best_)

Nested rolling evaluation
-------------------------

.. code-block:: python

   result = td.nested_rolling_pure_forecast(
       data.y,
       outer_initial_train=120,
       horizon=3,
       outer_step=3,
       orders=(1, 2, 3),
       windows=(24, 48, 72),
   )

   print(result.rmse)
   print(result.relative_rmsfe)
