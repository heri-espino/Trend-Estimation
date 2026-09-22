Models
======

Pure penalized trend
--------------------

The main analytic model is

.. math::

   \widehat t_{\lambda,d}
   =
   \arg\min_t
   \left\{
   \|y-t\|_2^2+\lambda\|D_dt\|_2^2
   \right\}.

Use :class:`trend_estimation.PurePenalizedTrend`.

Guerrero plug-in trend
----------------------

:class:`trend_estimation.GuerreroTrend` implements the Guerrero (2007)
feasible plug-in drift estimator used by this project.

The old iterative drift procedure is retained explicitly as
:class:`trend_estimation.IteratedDriftTrend` for reproducibility.

Baseline models
---------------

HP, Whittaker, moving-average, exponential-smoothing, and polynomial-trend
baselines are documented in :doc:`../api/models`.
