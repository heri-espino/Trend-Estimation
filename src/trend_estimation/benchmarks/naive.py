from __future__ import annotations

import numpy as np

from trend_estimation.utils.arrays import as_1d_float_array


def no_change_forecast(y_history, steps: int) -> np.ndarray:
    """Forecast a level series by repeating its latest observed value.

    This is the random-walk/no-change point forecast used as a mandatory
    reference for financial price-level experiments.
    """

    y_history = as_1d_float_array(y_history)
    steps = int(steps)
    if y_history.size == 0:
        raise ValueError("y_history must not be empty.")
    if steps < 0:
        raise ValueError("steps must be nonnegative.")
    return np.full(steps, float(y_history[-1]), dtype=float)
