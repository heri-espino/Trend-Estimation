# Derivative of the Forecast Loss

## Question

For the pure finite-difference penalized trend, how does the genuinely out-of-sample forecast MSE change with the smoothing penalty \(\lambda\)?

This is the derivative needed for the active forecasting paper. It is different from taking a fitted smoother over the full vector and then selecting "validation" entries from that same fitted vector.

## Assumptions and notation

At one forecast origin, let

- \(y\in\mathbb R^n\) be the observations available at the origin;
- \(z\in\mathbb R^h\) be the future block used only for scoring;
- \(D_d\) be the order-\(d\) finite-difference matrix;
- \(Q=D_d^\top D_d\);
- \(S_\lambda=(I+\lambda Q)^{-1}\);
- \(H\) be the linear forecast/continuation operator from the fitted in-sample trend to the next \(h\) values.

For the pure model,

\[
\widehat t_\lambda=S_\lambda y,
\qquad
\widehat z_\lambda=H S_\lambda y.
\]

The current pure continuation uses zero order-\(d\) future difference. In code we do not need to construct the matrix \(H\) explicitly; `forecast_trend(..., m_hat=0)` is linear, so it can be applied to a trend vector and to its derivative vectors.

## Step 1: derivative of the inverse

Let

\[
A(\lambda)=I+\lambda Q.
\]

For an invertible differentiable matrix,

\[
\frac{dA^{-1}}{d\lambda}
=
-A^{-1}A'A^{-1}.
\]

Since \(A'(\lambda)=Q\),

\[
\boxed{
S_\lambda'
=
-S_\lambda Q S_\lambda.
}
\]

This is the first key identity.

## Step 2: derivative of the fitted trend

Because \(y\) does not depend on \(\lambda\),

\[
\widehat t_\lambda'
=
S_\lambda' y
=
-S_\lambda Q S_\lambda y.
\]

Since \(\widehat t_\lambda=S_\lambda y\),

\[
\boxed{
\widehat t_\lambda'
=
-S_\lambda Q\widehat t_\lambda.
}
\]

Differentiate once more:

\[
\widehat t_\lambda''
=
-\left(S_\lambda'QS_\lambda
+
S_\lambda Q S_\lambda'\right)y.
\]

Substituting \(S_\lambda'=-S_\lambda Q S_\lambda\),

\[
\boxed{
\widehat t_\lambda''
=
2S_\lambda Q S_\lambda Q S_\lambda y.
}
\]

## Step 3: forecast derivatives

The forecast is

\[
\widehat z_\lambda
=
H S_\lambda y.
\]

Therefore

\[
\widehat z_\lambda'
=
-H S_\lambda Q S_\lambda y,
\]

and

\[
\widehat z_\lambda''
=
2H S_\lambda Q S_\lambda Q S_\lambda y.
\]

Define

\[
a_\lambda
=
H S_\lambda Q S_\lambda y,
\qquad
b_\lambda
=
H S_\lambda Q S_\lambda Q S_\lambda y.
\]

Then

\[
\widehat z_\lambda'=-a_\lambda,
\qquad
\widehat z_\lambda''=2b_\lambda.
\]

## Step 4: residual derivative

Define the genuinely future residual

\[
r_T(\lambda)
=
z-\widehat z_\lambda
=
z-HS_\lambda y.
\]

Then

\[
r_T'
=
-\widehat z_\lambda'
=
a_\lambda.
\]

Hence

\[
\boxed{
r_T'
=
H S_\lambda Q S_\lambda y.
}
\]

Differentiating again,

\[
r_T''
=
-\widehat z_\lambda''
=
-2b_\lambda.
\]

## Step 5: first derivative of forecast MSE

Let

\[
f_T(\lambda)
=
\frac1h r_T^\top r_T.
\]

Then

\[
f_T'
=
\frac1h
\left[
(r_T')^\top r_T+r_T^\top r_T'
\right]
=
\frac{2}{h}r_T^\top r_T'.
\]

Using \(r_T'=a_\lambda\),

\[
\boxed{
f_T'(\lambda)
=
\frac{2}{h}
r_T^\top
H S_\lambda Q S_\lambda y.
}
\]

This is the derivative whose roots determine interior stationary points of the single-origin forecast loss.

## Step 6: second derivative

Differentiate

\[
f_T'
=
\frac{2}{h}r_T^\top r_T'.
\]

Then

\[
f_T''
=
\frac{2}{h}
\left[
(r_T')^\top r_T'
+
r_T^\top r_T''
\right].
\]

Since \(r_T'=a_\lambda\) and \(r_T''=-2b_\lambda\),

\[
\boxed{
f_T''(\lambda)
=
\frac{2}{h}
\left[
\|H S_\lambda Q S_\lambda y\|_2^2
-
2r_T^\top
H S_\lambda Q S_\lambda Q S_\lambda y
\right].
}
\]

## Step 7: several rolling origins

For origins indexed by \(j\), possibly with different horizons \(h_j\), define the pooled validation objective

\[
CV(\lambda)
=
\frac{
\sum_j \|r_j(\lambda)\|_2^2
}{
\sum_j h_j
}.
\]

Equivalently,

\[
CV(\lambda)
=
\frac{
\sum_j h_j f_j(\lambda)
}{
\sum_j h_j
}.
\]

Linearity of differentiation gives

\[
\boxed{
CV'(\lambda)
=
\frac{
\sum_j h_j f_j'(\lambda)
}{
\sum_j h_j
},
}
\]

and

\[
\boxed{
CV''(\lambda)
=
\frac{
\sum_j h_j f_j''(\lambda)
}{
\sum_j h_j
}.
}
\]

The global hyperparameter search should operate on this aggregate objective when one shared \(\lambda\) is being selected across the rolling origins. We should not independently minimize each fold and then average the minimizers.

## Step 8: log-penalty parameter

Let

\[
\theta=\log\lambda,
\qquad
g(\theta)=CV(e^\theta).
\]

Then

\[
\boxed{
g'(\theta)
=
\lambda CV'(\lambda)
}
\]

and

\[
\boxed{
g''(\theta)
=
\lambda CV'(\lambda)
+
\lambda^2CV''(\lambda).
}
\]

Because \(\lambda>0\), the roots of \(g'\) and \(CV'\) correspond exactly.

## Library mapping

### Already implemented

- `src/trend_estimation/core/derivatives.py::pure_trend_derivatives`
  implements \(\widehat t_\lambda'\) and \(\widehat t_\lambda''\).
- `src/trend_estimation/core/derivatives.py::mse_from_prediction_derivatives`
  implements the generic MSE derivative identities.
- `src/trend_estimation/forecasting/extrapolation.py::forecast_trend`
  implements the continuation used by the pure estimator.
- `src/trend_estimation/validation/rolling_origin.py`
  generates chronological origins.

### Active implementation

- `src/trend_estimation/forecasting/objectives.py`
  combines the trend derivatives, continuation operator, and MSE derivatives into the single-origin and rolling-origin forecast objectives.
- `src/trend_estimation/selection/numerical.py`
  uses these derivatives for stationary-point search in log-\(\lambda\).

### Tests

- `tests/test_forecast_objective_derivatives.py`
  compares the analytic objective derivatives with finite differences.
- `tests/test_rolling_origin_and_numerical.py`
  checks the log-\(\lambda\) stationary-point machinery on a known multimodal objective.

## Scope

This derivation is for the **pure penalized trend**. Do not automatically reuse it for any model in which the right-hand side, drift, forecast operator, or other fitted quantity depends on \(\lambda\) in an additional way.

See `notes/model_definitions.md` for the Guerrero-model issue.
