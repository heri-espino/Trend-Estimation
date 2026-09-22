from __future__ import annotations

from ._drift_penalized import _DriftPenalizedTrend


class HPTrend(_DriftPenalizedTrend):
    """Hodrick-Prescott-style order-2 quadratic penalized trend baseline."""

    def __init__(self, lambda_: float = 1600.0):
        super().__init__(
            order=2,
            smoothness=None,
            lambda_=float(lambda_),
            drift_mode="zero",
        )

    def get_params(self):
        return {"lambda_": self.lambda_}
