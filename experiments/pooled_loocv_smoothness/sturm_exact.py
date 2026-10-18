"""Optional exact rational Sturm mini-check for pooled LOOCV.

Requires 'pip install -e ".[symbolic]"'. Does not scale to large n.
No unrestricted global floating-point certification is claimed.
"""

from __future__ import annotations

import argparse
import json
from math import comb


def exact_sturm(series, order: int = 2, eps_denominator: int = 100000):
    """Build exact stationary polynomial and isolate positive roots.

    Parameters
    ----------
    series: list of lists of int or fractions.Fraction or SymPy Rational
        Each series must have the same n and all inputs must be exact
        rational numbers; Python floats are rejected.
    order: int
        Forward-differencing order.
    """
    try:
        import sympy as sp
    except ImportError as exc:
        raise ImportError('install exact dependencies with pip install -e ".[symbolic]"') from exc
    if not series or not series[0]:
        raise ValueError("provide at least one series")
    n = len(series[0])
    if n > 7 or n < order + 2 or any(len(s) != n for s in series):
        raise ValueError("tiny exact examples require order+2 <= n <= 7 and same n")
    y = []
    for s in series:
        row = []
        for val in s:
            if isinstance(val, float):
                raise TypeError("float inputs cannot provide an exact rational certificate")
            item = sp.sympify(val)
            if not item.is_Rational:
                raise TypeError("every datum must be exactly rational")
            row.append(item)
        y.append(sp.Matrix(row))
    d = sp.zeros(n - order, n)
    for i in range(n - order):
        for j in range(order + 1):
            d[i, i + j] = (-1) ** (order - j) * comb(order, j)
    q = d.T * d
    lam = sp.Symbol("lam", nonnegative=True)
    t = q * (sp.eye(n) + lam * q).inv()
    terms = []
    for row in y:
        ty = t * row
        for i in range(n):
            terms.append(sp.cancel(ty[i] / t[i, i]) ** 2)
    loss = sp.cancel(sum(terms) / len(terms))
    num, den = sp.cancel(sp.diff(loss, lam)).as_numer_denom()
    poly = sp.Poly(num, lam, domain="QQ")
    if poly.is_zero:
        return {"constant_objective": True, "positive_stationary_roots": "all"}
    intervals = []
    for (a, b), multiplicity in poly.intervals(eps=sp.Rational(1, eps_denominator)):
        if b <= 0:
            continue
        intervals.append({"lower": str(max(a, 0)), "upper": str(b),
                          "multiplicity": int(multiplicity)})
    return {
        "constant_objective": False,
        "polynomial_degree": int(poly.degree()),
        "positive_stationary_roots": int(poly.count_roots(0, sp.oo)),
        "isolating_intervals": intervals,
        "exact_input_series_count": len(series),
        "n": n, "order": order,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, default=2)
    args = parser.parse_args()
    # Tiny rational illustrative instance; no theorem about all series.
    result = exact_sturm([[0, 3, -1, 5, 1]], order=args.order)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
