from __future__ import annotations

from trend_estimation.models.penalized_trend import PenalizedTrend


class GuerreroTrend(PenalizedTrend):
    """Guerrero (2007) feasible penalized trend estimator.

    The default drift is the sample mean of the observed d-th differences,
    held fixed while lambda varies.
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


class IteratedDriftTrend(PenalizedTrend):
    """Historical variant with drift repeatedly re-estimated from the fitted trend."""

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
