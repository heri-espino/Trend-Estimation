"""Hyperparameter selection and numerical optimization."""

from .base import BaseSelectionCriterion, BaseTrendSelector, SelectionResult
from .forecast_optimal import (
    ForecastOptimalCandidate,
    ForecastOptimalSelection,
    select_fixed_window_pure_smoothness,
)
from .minima import find_all_local_minima, golden_local
from .numerical import (
    LambdaOptimizationResult,
    StationaryPoint,
    StationaryPointSearchResult,
    find_stationary_points_log_lambda,
    minimize_over_log_lambda,
    newton_stationary_log_lambda,
)
from .recovery import (
    PreparedRollingPureRecoveryObjective,
    RecoveryLossDerivatives,
    RecoveryOptimalSelection,
    prepare_rolling_pure_recovery_objective,
    pure_recovery_loss_derivatives,
    select_recovery_optimal_lambda,
)
from .time_weighted import TimeWeightedValidationSelector
from .train_validation import TrainValidationSelector

__all__ = [
    "BaseSelectionCriterion",
    "BaseTrendSelector",
    "SelectionResult",
    "TrainValidationSelector",
    "TimeWeightedValidationSelector",
    "golden_local",
    "find_all_local_minima",
    "LambdaOptimizationResult",
    "StationaryPoint",
    "StationaryPointSearchResult",
    "minimize_over_log_lambda",
    "newton_stationary_log_lambda",
    "find_stationary_points_log_lambda",
    "ForecastOptimalCandidate",
    "ForecastOptimalSelection",
    "select_fixed_window_pure_smoothness",
    "PreparedRollingPureRecoveryObjective",
    "RecoveryLossDerivatives",
    "RecoveryOptimalSelection",
    "prepare_rolling_pure_recovery_objective",
    "pure_recovery_loss_derivatives",
    "select_recovery_optimal_lambda",
]
