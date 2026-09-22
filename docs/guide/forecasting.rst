Forecasting
===========

Chronological invariant
-----------------------

At forecast origin :math:`T`, fitting and hyperparameter selection may use
only observations available through :math:`T`. Future observations may score
a forecast but may not construct it.

Finite-difference continuation
------------------------------

The fitted trend is extrapolated by imposing a constant finite difference of
the fitted order. The package exposes both the recursive implementation and its
equivalent affine operator.

For the pure model,

.. math::

   \widehat y_{T+1:T+h\mid T}=H\widehat t_\lambda.

Forecast-loss derivatives
-------------------------

For

.. math::

   r_T(\lambda)=y_{T+1:T+h}-H S_\lambda y_{\mathrm{past}},

the library implements the forecast MSE and its first two derivatives.

See :func:`trend_estimation.pure_forecast_loss_derivatives`.
