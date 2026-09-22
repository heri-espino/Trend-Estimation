Smoothness selection
====================

Log-penalty parameterization
----------------------------

The numerical routines work in

.. math::

   \theta=\log\lambda,

which enforces :math:`\lambda>0` and handles multiple orders of magnitude
naturally.

Stationary-point search
-----------------------

The validation objective is not assumed to be unimodal. The active search:

1. scans the derivative on a coarse log grid;
2. brackets sign changes;
3. solves bracketed roots with Brent's method;
4. classifies stationary points;
5. evaluates local minima and boundaries.

See :func:`trend_estimation.find_stationary_points_log_lambda`.

Window length
-------------

Normalized smoothness depends on fitted sample size. The active inner selector
therefore uses fixed-width candidate windows and scores all candidate windows
on the same forecast origins.

See :func:`trend_estimation.select_fixed_window_pure_smoothness`.

Nested evaluation
-----------------

Use :func:`trend_estimation.nested_rolling_pure_forecast` for genuine
out-of-sample evaluation after tuning order, window length, and penalty.
