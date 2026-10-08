"""Sturm isolation for small exact-rational forecast-smoothness problems.

This optional method is complete for the rationalized finite-sample objective.
For long windows use the existing adaptive S-domain solver: high-degree exact
polynomial arithmetic can be prohibitively expensive.
SymPy is optional: pip install -e ".[symbolic]"
"""
from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Sequence

import numpy as np

from trend_estimation.core.smoothness import lambda_to_smoothness


@dataclass(frozen=True)
class SturmRoot:
    lambda_interval: tuple[float, float]
    lambda_value: float
    smoothness: float
    forecast_mse: float
    kind: str
    multiplicity: int
    rational_interval: tuple[str, str] | None = None


@dataclass(frozen=True)
class SturmSearchResult:
    stationary_roots: tuple[SturmRoot, ...]
    certified_positive_root_count: int
    derivative_numerator_degree: int
    endpoint_mse: tuple[float, float]
    best_smoothness: float
    best_lambda: float
    best_mse: float
    sturm_variations: tuple[int, int]
    constant_loss: bool = False


def _exact_scalar(value, sp):
    """Convert a printed decimal to a rational, not its binary-float model."""
    if not np.isfinite(float(value)):
        raise ValueError("All inputs must be finite.")
    return sp.Rational(str(value))


def _difference_matrix(sp, n: int, d: int):
    matrix = sp.zeros(n - d, n)
    for row in range(n - d):
        for j in range(d + 1):
            matrix[row, row + j] = (-1) ** (d - j) * comb(d, j)
    return matrix


def _forecast_operator(sp, n: int, d: int, h: int):
    state = sp.zeros(d, n)
    for j in range(d):
        state[j, n - d + j] = 1
    result = sp.zeros(h, n)
    coeff = [(-1) ** (d - j) * comb(d, j) for j in range(d)]
    for k in range(h):
        row = -sum((coeff[j] * state[j, :] for j in range(d)), sp.zeros(1, n))
        result[k, :] = row
        for j in range(d - 1):
            state[j, :] = state[j + 1, :]
        state[d - 1, :] = row
    return result


def _variations(signs: Sequence[int]) -> int:
    nonzero = [v for v in signs if v]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


def sturm_forecast_smoothness(
    history,
    future,
    *,
    order: int,
    precision_digits: int = 12,
    max_window: int = 8,
) -> SturmSearchResult:
    """Isolate every positive stationary root in a small forecast-MSE objective.

    history and future accept 1D inputs (one validation origin) or
    2D inputs (pooled origins), with a common window and horizon.
    The exact objective uses the rationals written by the decimal
    representation of inputs; this does not certify a latent data process.

    We construct a rational loss function in lambda, use an exact
    Sturm sequence and rational intervals for distinct positive real
    zeros of its derivative numerator, and map isolated roots to S.
    Even-multiplicity stationary roots are included. Exact lambda=0
    and lambda=infinity limits are included in the global comparison.
    Root interval strings retain the exact rational enclosure; float
    endpoint coordinates are conveniences, not certified bounds.
    """
    try:
        import sympy as sp
    except ImportError as exc:
        raise ImportError(
            'Exact Sturm search requires SymPy; install with pip install -e ".[symbolic]"'
        ) from exc

    y = np.asarray(history)
    z = np.asarray(future)
    if y.ndim == 1:
        y = y[None, :]
    if z.ndim == 1:
        z = z[None, :]
    if y.ndim != 2 or z.ndim != 2 or y.shape[0] != z.shape[0]:
        raise ValueError("history and future must have matching origin counts.")
    m, n = y.shape
    h = z.shape[1]
    d = int(order)
    if m < 1 or h < 1 or n < 2 or not 1 <= d < n:
        raise ValueError("Require nonempty origins, horizon, and 1 <= order < window.")
    if n > int(max_window):
        raise ValueError(
            "Exact symbolic Sturm search exceeds max_window; "
            "use the scalable adaptive S-domain solver instead."
        )
    if not 4 <= precision_digits <= 30:
        raise ValueError("precision_digits must be between 4 and 30.")

    lam = sp.Symbol("lambda", real=True)
    D = _difference_matrix(sp, n, d)
    A = sp.eye(n) + lam * D.T * D
    H = A.inv()
    G = _forecast_operator(sp, n, d, h)
    projection = G * H
    error_sum = sp.S.Zero
    for i in range(m):
        x = sp.Matrix([_exact_scalar(v, sp) for v in y[i]])
        target = sp.Matrix([_exact_scalar(v, sp) for v in z[i]])
        residual = target - projection * x
        error_sum += sum((v * v for v in residual), sp.S.Zero)
    loss = sp.cancel(error_sum / (m * h))
    derivative = sp.cancel(sp.diff(loss, lam))
    numerator, denominator = sp.fraction(derivative)
    poly = sp.Poly(numerator, lam, domain="QQ")
    if poly.is_zero:
        loss0 = float(loss.subs(lam, 0))
        lossinf = float(sp.limit(loss, lam, sp.oo))
        if not np.isclose(loss0, lossinf, rtol=1e-12, atol=1e-12):
            raise ArithmeticError("Zero derivative with nonconstant endpoints.")
        return SturmSearchResult((), 0, -1, (loss0, lossinf),
                                 0.0, 0.0, loss0, (0, 0), constant_loss=True)

    # The rational derivative denominator cannot vanish for lambda>=0,
    # because I + lambda D.T D is positive definite there.
    sturm = sp.sturm(poly.sqf_part().as_expr(), lam)
    sign0 = [int(sp.sign(p.subs(lam, 0))) for p in sturm]
    sign_inf = [int(sp.sign(sp.Poly(p, lam).LC())) for p in sturm]
    v0, vinf = _variations(sign0), _variations(sign_inf)
    count = v0 - vinf
    if count < 0:
        raise ArithmeticError("Invalid positive-root count.")

    intervals = sp.intervals(poly, eps=sp.Rational(1, 10**precision_digits))
    positive = [(a, b, mult) for (a, b), mult in intervals if b > 0]
    if any(a < 0 < b for a, b, _ in positive):
        raise ArithmeticError(
            "An isolating interval straddles the lambda=0 boundary; "
            "increase precision_digits to separate the root."
        )
    if len(positive) != count:
        raise ArithmeticError(
            "Sturm variations disagree with the isolated positive roots."
        )

    roots = []
    for i, (a, b, mult) in enumerate(positive):
        previous_end = positive[i - 1][1] if i else sp.S.Zero
        following_start = positive[i + 1][0] if i + 1 < count else b + 2
        left = (previous_end + a) / 2
        right = (b + following_start) / 2
        if not left < a or not right > b:
            raise ArithmeticError("Root intervals are not separated.")
        left_sign = int(sp.sign(poly.eval(left) / denominator.subs(lam, left)))
        right_sign = int(sp.sign(poly.eval(right) / denominator.subs(lam, right)))
        if left_sign < 0 and right_sign > 0:
            kind = "minimum"
        elif left_sign > 0 and right_sign < 0:
            kind = "maximum"
        else:
            kind = "flat"
        midpoint = (a + b) / 2
        x = float(sp.N(midpoint, precision_digits + 5))
        mse = float(sp.N(loss.subs(lam, midpoint), 18))
        roots.append(
            SturmRoot(
                lambda_interval=(float(a), float(b)),
                lambda_value=x,
                smoothness=lambda_to_smoothness(x, n_obs=n, order=d),
                forecast_mse=mse,
                kind=kind,
                multiplicity=int(mult),
                rational_interval=(str(a), str(b)),
            )
        )

    mse0 = float(sp.N(loss.subs(lam, 0), 18))
    mseinf = float(sp.N(sp.limit(loss, lam, sp.oo), 18))
    candidates = [(mse0, 0.0, 0.0), (mseinf, 1.0, float("inf"))]
    candidates += [
        (p.forecast_mse, p.smoothness, p.lambda_value)
        for p in roots if p.kind == "minimum"
    ]
    best_mse, best_s, best_lam = min(candidates, key=lambda t: (t[0], t[1]))
    return SturmSearchResult(
        stationary_roots=tuple(roots),
        certified_positive_root_count=count,
        derivative_numerator_degree=poly.degree(),
        endpoint_mse=(mse0, mseinf),
        best_smoothness=best_s,
        best_lambda=best_lam,
        best_mse=best_mse,
        sturm_variations=(v0, vinf),
    )
