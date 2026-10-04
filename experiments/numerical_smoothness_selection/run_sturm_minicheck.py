from __future__ import annotations

from math import comb

import numpy as np
from scipy.optimize import brentq

try:
    import sympy as sp
except ImportError as exc:
    raise SystemExit(
        'This diagnostic requires SymPy. Install with: '
        'python -m pip install -e ".[symbolic]"'
    ) from exc

from trend_estimation.forecasting.objectives import pure_forecast_loss_derivatives


def difference_matrix_exact(n_obs: int, order: int) -> sp.Matrix:
    """Exact integer finite-difference matrix used only for this diagnostic."""
    coeffs = [(-1) ** (order - k) * comb(order, k) for k in range(order + 1)]
    out = sp.zeros(n_obs - order, n_obs)
    for row in range(n_obs - order):
        for k, coeff in enumerate(coeffs):
            out[row, row + k] = coeff
    return out


def forecast_operator_exact(n_fit: int, order: int, steps: int) -> sp.Matrix:
    """Exact integer matrix matching finite_difference_forecast_operator for mu=0."""
    if order <= 0:
        return sp.zeros(steps, n_fit)

    d_eff = min(order, n_fit)
    state = sp.zeros(d_eff, n_fit)
    for i in range(d_eff):
        state[i, n_fit - d_eff + i] = 1

    coeffs = [(-1) ** (d_eff - k) * comb(d_eff, k) for k in range(d_eff)]
    out = sp.zeros(steps, n_fit)

    for i in range(steps):
        next_row = sp.zeros(1, n_fit)
        for k, coeff in enumerate(coeffs):
            next_row -= coeff * state[k, :]
        out[i, :] = next_row

        if d_eff > 1:
            for k in range(d_eff - 1):
                state[k, :] = state[k + 1, :]
        state[d_eff - 1, :] = next_row

    return out


def sign_variations(signs: list[int]) -> int:
    nonzero = [sign for sign in signs if sign != 0]
    return sum(left != right for left, right in zip(nonzero, nonzero[1:]))


def sign_int(value: sp.Expr) -> int:
    value = sp.sign(sp.simplify(value))
    if value == 1:
        return 1
    if value == -1:
        return -1
    if value == 0:
        return 0
    raise ValueError(f"Could not determine exact sign of {value!r}")


def main() -> None:
    lam = sp.symbols("lambda", nonnegative=True)

    # Deliberately tiny exact case. It contains three positive stationary points,
    # so it checks more than a trivially unimodal objective.
    n_fit = 6
    order = 2
    horizon = 2
    y_past = sp.Matrix([4, 0, -2, -1, 3, 1])
    y_future = sp.Matrix([0, 1])

    D = difference_matrix_exact(n_fit, order)
    Q = D.T * D
    A = sp.eye(n_fit) + lam * Q
    smoother = A.inv()
    G = forecast_operator_exact(n_fit, order, horizon)

    prediction = G * smoother * y_past
    residual = y_future - prediction
    loss = sp.cancel(sum(value**2 for value in residual) / sp.Integer(horizon))

    loss_num, loss_den = sp.fraction(loss)
    derivative = sp.cancel(sp.diff(loss, lam))
    derivative_num, _ = sp.fraction(derivative)
    derivative_poly = sp.Poly(derivative_num, lam)

    # Exact Sturm count on (0, +infinity).
    sturm = sp.sturm(derivative_poly.as_expr(), lam)
    signs_zero = [sign_int(poly.subs(lam, 0)) for poly in sturm]
    # For +infinity, a polynomial has the sign of its leading coefficient.
    signs_inf = [sign_int(sp.Poly(poly, lam).LC()) for poly in sturm]
    variations_zero = sign_variations(signs_zero)
    variations_inf = sign_variations(signs_inf)
    positive_root_count = variations_zero - variations_inf

    # Numerical roots are used only to print their locations/classification.
    numerical_roots = sorted(
        float(sp.re(root))
        for root in sp.nroots(derivative_poly, maxsteps=200)
        if abs(float(sp.im(root))) < 1e-10 and float(sp.re(root)) > 0.0
    )

    second = sp.diff(loss, lam, 2)
    classifications = [
        "minimum" if float(sp.N(second.subs(lam, root))) > 0.0 else "maximum"
        for root in numerical_roots
    ]

    # A standard sign-change scan + Brent should recover all three roots in this
    # deliberately small example because all three roots are simple.
    derivative_fn = sp.lambdify(lam, derivative, "numpy")
    grid = np.concatenate(([0.0], np.logspace(-4, 3, 2000)))
    values = np.asarray(derivative_fn(grid), dtype=float)
    brent_roots: list[float] = []
    for left, right, f_left, f_right in zip(
        grid[:-1], grid[1:], values[:-1], values[1:]
    ):
        if f_left * f_right < 0.0:
            root = float(brentq(derivative_fn, left, right))
            if not brent_roots or abs(root - brent_roots[-1]) > 1e-8:
                brent_roots.append(root)

    assert positive_root_count == 3
    assert len(numerical_roots) == 3
    assert np.allclose(numerical_roots, brent_roots, rtol=0.0, atol=1e-9)
    assert classifications == ["minimum", "maximum", "minimum"]

    # Verify that the exact symbolic construction is the same objective and
    # derivative implementation used by the production library.
    loss_fn = sp.lambdify(lam, loss, "numpy")
    first_fn = sp.lambdify(lam, derivative, "numpy")
    second_fn = sp.lambdify(lam, second, "numpy")
    y_past_np = np.asarray(y_past, dtype=float).ravel()
    y_future_np = np.asarray(y_future, dtype=float).ravel()

    for lambda_value in [0.0, 0.1, 1.0, 10.0, 100.0]:
        actual = pure_forecast_loss_derivatives(
            y_past_np,
            y_future_np,
            order=order,
            lambda_=lambda_value,
        )
        assert np.isclose(actual.value, float(loss_fn(lambda_value)), atol=1e-10)
        assert np.isclose(actual.first, float(first_fn(lambda_value)), atol=1e-10)
        assert np.isclose(actual.second, float(second_fn(lambda_value)), atol=1e-9)

    print("Sturm mini-check: PASS")
    print(f"n_fit={n_fit}, d={order}, h={horizon}")
    print(f"loss numerator degree: {sp.Poly(loss_num, lam).degree()}")
    print(f"loss denominator degree: {sp.Poly(loss_den, lam).degree()}")
    print(f"derivative numerator degree: {derivative_poly.degree()}")
    print(f"Sturm variations: V(0+)={variations_zero}, V(+inf)={variations_inf}")
    print(f"positive stationary roots: {positive_root_count}")
    for root, kind in zip(numerical_roots, classifications):
        print(f"  lambda={root:.12g} -> {kind}")
    print("Brent roots match the Sturm-certified positive-root count.")
    print("Symbolic objective/derivatives match production code at 5 lambda values.")


if __name__ == "__main__":
    main()
