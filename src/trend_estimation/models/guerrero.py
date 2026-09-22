from __future__ import annotations

from trend_estimation.models._drift_penalized import _DriftPenalizedTrend


class GuerreroTrend(_DriftPenalizedTrend):
    """Guerrero (2007) feasible plug-in trend estimator.

    The drift is the sample mean of the observed d-th differences and is held
    fixed while the penalty parameter varies.
    """

    def __init__(
        self,
        order: int = 2,
        smoothness: float | None = 0.75,
        lambda_: float | None = None,
    ):
        super().__init__(
            order=order,
            smoothness=smoothness,
            lambda_=lambda_,
            drift_mode="data",
        )


class IteratedDriftTrend(_DriftPenalizedTrend):
    """Historical variant that re-estimates drift from the fitted trend."""

    def __init__(
        self,
        order: int = 2,
        smoothness: float | None = 0.75,
        lambda_: float | None = None,
    ):
        super().__init__(
            order=order,
            smoothness=smoothness,
            lambda_=lambda_,
            drift_mode="iterated",
        )
