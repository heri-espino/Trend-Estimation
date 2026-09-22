from __future__ import annotations

from trend_estimation.validation.losses import TimeWeightedValidationLoss

from .train_validation import TrainValidationSelector


class TimeWeightedValidationSelector(TrainValidationSelector):
    """Chronological holdout selector with a time-weighted validation loss."""

    def __init__(
        self,
        orders=(1, 2, 3),
        smoothness_grid=None,
        *,
        weight_scheme: str = "exponential",
        decay: float = 0.95,
        custom_weights=None,
        **kwargs,
    ):
        loss = TimeWeightedValidationLoss(
            weight_scheme=weight_scheme,
            decay=decay,
            custom_weights=custom_weights,
        )
        super().__init__(
            orders=orders,
            smoothness_grid=smoothness_grid,
            loss=loss,
            **kwargs,
        )
        self.weight_scheme = weight_scheme
        self.decay = decay
        self.custom_weights = custom_weights
