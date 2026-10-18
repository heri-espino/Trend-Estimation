"""Independent observed-series pooled LOOCV numerical experiment.

This package deliberately does not import forecasting modules.
"""

from .objective import PooledLOOCV, difference_matrix
from .search import bounded_brent, dense_reference, multibracket_brent

__all__ = ["PooledLOOCV", "difference_matrix", "bounded_brent", "dense_reference", "multibracket_brent"]
