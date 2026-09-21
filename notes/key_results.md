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

**Library mapping:** `core/pure.py`, `models/pure_penalized.py`.

**Status:** implemented and tested.

## 2. Smoother sensitivity

\[
\boxed{
S_\lambda'=-S_\lambda Q S_\lambda
}
\]

\[
\boxed{
\widehat t_\lambda'=-S_\lambda Q\widehat t_\lambda
}
\]

\[
\boxed{
\widehat t_\lambda''
=
2S_\lambda Q S_\lambda Q\widehat t_\lambda.
}
\]

**Library mapping:** `core/derivatives.py::pure_trend_derivatives`.

**Status:** implemented and tested against centered finite differences.

## 3. Forecast residual at origin T

For horizon \(h\), let \(H\) denote the linear continuation operator used by the pure model:

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

**Library mapping:** `forecasting/extrapolation.py`, `forecasting/objectives.py`.

**Status:** derived and implemented.

## 4. Forecast MSE derivatives

With

\[
f_T(\lambda)=\frac{1}{h}r_T(\lambda)^\top r_T(\lambda),
\]

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

**Library mapping:** `core/derivatives.py::mse_from_prediction_derivatives`, `forecasting/objectives.py::pure_forecast_loss_derivatives`.

**Status:** implemented with finite-difference tests.

Detailed derivation: `notes/derivative.md`.

## 5. Rolling-origin aggregate objective

For origins \(T_1,\ldots,T_M\),

\[
\boxed{
CV(\lambda)
=
\frac{\sum_j h_j f_{T_j}(\lambda)}
{\sum_j h_j}.
}
\]

and

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

**Library mapping:** `validation/rolling_origin.py`, `forecasting/objectives.py::rolling_pure_forecast_loss_derivatives`.

**Status:** implemented and tested against explicit weighted aggregation.

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

Thus

\[
g'(\theta)=0
\iff
f'(\lambda)=0.
\]

**Library mapping:** `selection/numerical.py`.

**Status:** implemented.

## 7. Bracketed stationary-point strategy

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
\text{evaluate stationary points and boundaries}.
}
\]

**Library mapping:** `selection/numerical.py::find_stationary_points_log_lambda`.

**Status:** implemented and tested on a known multimodal objective.

**Important limitation:** a finite discovery grid can miss multiple roots inside one interval or a tangential root with no sign change. Dense/adaptive diagnostic scans remain part of validation.

Detailed note: `notes/numerical_selection.md`.

## 8. Active scientific object

The primary empirical object is not raw \(\lambda^\star\) alone:

\[
\boxed{
S^\star_{T,h}
=
g(h,L,\mathcal R_T,\text{series class})
}
\]

together with out-of-sample forecast skill.

**Library mapping:** experiment-level object assembled from reusable library components.

**Status:** active research question.
