import numpy as np

from trend_estimation.core.smoothness import effective_degrees_of_freedom


def test_effective_degrees_of_freedom_handles_infinite_penalty_endpoint():
    assert effective_degrees_of_freedom(np.inf, n_obs=20, order=2) == 2.0
    assert effective_degrees_of_freedom(np.inf, n_obs=20, order=1) == 1.0
    assert effective_degrees_of_freedom(np.inf, n_obs=20, order=0) == 0.0
