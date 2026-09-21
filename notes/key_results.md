# Key Results

This file is the short canonical list of mathematical results currently used by the active research program. Detailed derivations live in separate notes.

## 1. Pure penalized trend

Let

\[
Q=D_d^\top D_d,
\qquad
S_\lambda=(I+\lambda Q)^{-1}.
\]

Then

\[
\boxed{
\widehat t_\lambda=S_\lambda y
}
\]

solves

\[
\min_t\;\|y-t\|_2^2+\lambda\|D_dt\|_2^2.
\]

**Library mapping**

- `src/trend_estimation/core/pure.py`
- `src/trend_estimation/models/pure_penalized.py`

**Status:** implemented and tested.

## 2. Smoother sensitivity

\[
\boxed{
S_\lambda'=-S_\lambda Q S_\lambda
}
\]

and therefore

\[
\boxed{
\widehat t_\lambda'=-S_\lambda Q\widehat t_\lambda
}
\]

and

\[
\boxed{
\widehat t_\lambda''
=
2S_\lambda Q S_\lambda Q\widehat t_\lambda.
}
\]

**Library mapping**

- `src/trend_estimation/core/derivatives.py::pure_trend_derivatives`

**Status:** implemented and tested against centered finite differences.

## 3. Forecast residual at origin T

For forecast horizon \(h\), let \(H\) denote the linear continuation operator used by the pure model and let

\[
r_T(\lambda)
=
y_{T+1:T+h}
-
H S_\lambda y_{\mathrm{past}}.
\]

Then

\[
\boxed{
r_T'(\lambda)
=
H S_\lambda Q S_\lambda y_{\mathrm{past}}.
}
\]

**Library mapping**

- continuation logic: `src/trend_estimation/forecasting/extrapolation.py`
- forecast-loss derivative: `src/trend_estimation/forecasting/objectives.py`

**Status:** derived; implementation is the active numerical objective.

## 4. Forecast MSE derivatives

With

\[
f_T(\lambda)=\frac{1}{h}r_T(\lambda)^\top r_T(\lambda),
\]

we obtain

\[
\boxed{
f_T'(\lambda)
=
\frac{2}{h}
r_T^\top
H S_\lambda Q S_\lambda y_{\mathrm{past}}.
}
\]

Also,

\[
\boxed{
f_T''(\lambda)
=
\frac{2}{h}
\left[
\|H S_\lambda Q S_\lambda y_{\mathrm{past}}\|_2^2
-
2r_T^\top
H S_\lambda Q S_\lambda Q S_\lambda y_{\mathrm{past}}
\right].
}
\]

**Library mapping**

- generic MSE derivative identity:
  `src/trend_estimation/core/derivatives.py::mse_from_prediction_derivatives`
- forecast objective:
  `src/trend_estimation/forecasting/objectives.py`

**Status:** derived; tested numerically in the library.

Detailed derivation: `notes/derivative.md`.

## 5. Rolling-origin aggregate objective

For forecast origins \(T_1,\ldots,T_M\),

\[
\boxed{
CV(\lambda)
=
\frac{\sum_j h_j f_{T_j}(\lambda)}
{\sum_j h_j}.
}
\]

The same pooling applies to the derivatives:

\[
\boxed{
CV'(\lambda)
=
\frac{\sum_j h_j f_{T_j}'(\lambda)}
{\sum_j h_j},
\qquad
CV''(\lambda)
=
\frac{\sum_j h_j f_{T_j}''(\lambda)}
{\sum_j h_j}.
}
\]

**Library mapping**

- splits: `src/trend_estimation/validation/rolling_origin.py`
- aggregate objective: `src/trend_estimation/forecasting/objectives.py`

**Status:** derived and implemented for the pure penalized trend.

## 6. Log-lambda transformation

Set

\[
\theta=\log\lambda,
\qquad
g(\theta)=f(e^\theta).
\]

Then

\[
\boxed{
g'(\theta)=\lambda f'(\lambda)
}
\]

and

\[
\boxed{
g''(\theta)
=
\lambda f'(\lambda)+\lambda^2f''(\lambda).
}
\]

Thus stationary points are unchanged for \(\lambda>0\):

\[
g'(\theta)=0
\iff
f'(\lambda)=0.
\]

**Library mapping**

- `src/trend_estimation/selection/numerical.py`

**Status:** implemented.

## 7. Robust stationary-point strategy

On a bounded log-penalty domain:

\[
\boxed{
\text{coarse log-grid}
\rightarrow
\text{bracket sign changes in }g'
\rightarrow
\text{Brent roots}
\rightarrow
\text{classify}
\rightarrow
\text{evaluate minima and boundaries}.
}
\]

This avoids assuming that the cross-validation objective is unimodal.

**Library mapping**

- `src/trend_estimation/selection/numerical.py::find_stationary_points_log_lambda`

**Status:** implementation target for the active paper; compare against grid and Newton.

Detailed note: `notes/numerical_selection.md`.

## 8. Active scientific object

The primary empirical object is not raw \(\lambda^\star\) alone. We want to study

\[
\boxed{
S^\star_{T,h}
=
g(h,L,\mathcal R_T,\text{series class})
}
\]

together with out-of-sample forecast skill.

**Library mapping**

This is an experiment-level object built from reusable library components. No paper-specific estimator logic should be added to the manuscript directory.

**Status:** active research question.
