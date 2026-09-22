from __future__ import annotations

from ._drift_penalized import _DriftPenalizedTrend


class WhittakerTrend(_DriftPenalizedTrend):
    """Zero-drift Whittaker-Henderson-style quadratic trend baseline.

    Parameters
    ----------
    order : int
        Difference order in the roughness penalty.
    lambda_ : float or None
        Penalty parameter. Larger values imply smoother trends.
    smoothness : float or None
        Optional normalized smoothness level used when lambda_ is omitted.
    """

    def __init__(
        self,
        order: int = 2,
        lambda_: float | None = None,
        smoothness: float | None = 0.75,
    ):
        super().__init__(
            order=order,
            smoothness=smoothness,
            lambda_=lambda_,
            drift_mode="zero",
        )

    def get_params(self):
        return {
            "order": self.order,
            "lambda_": self.lambda_,
            "smoothness": self.smoothness,
        }
