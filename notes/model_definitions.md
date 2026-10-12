# Model Definitions and Naming Audit

## Purpose

The repository contains closely related penalized smoothers. They must not be conflated in code, notes, or manuscripts.

## A. Pure penalized trend

$$
\widehat t_{\lambda,d}
=
\arg\min_t
\left\{
\|y-t\|_2^2+
\lambda\|D_dt\|_2^2
\right\}
=
(I+\lambda D_d^\top D_d)^{-1}y.
$$

This is the canonical model for the active derivative and numerical-optimization work.

**Library**

- `PurePenalizedSolver`
- `PurePenalizedTrend`
- `pure_trend_derivatives`

**Status:** definition, implementation, and derivative identities are internally consistent.


### Interpretation for forecast validation

For the active numerical paper, Model A is intentionally the **zero-drift**
special case of the Guerrero family: (V=I) and (mu=0). This should be
treated as a modeling choice, not as a claim that the true (d)-th differences
of the latent trend necessarily have mean zero.

The chronological validation objective selects (lambda) **within** a fixed
forecasting family. If the zero-drift penalty is locally inappropriate,
validation can prefer a smaller (lambda), reducing the influence of the
penalty, but (lambda) cannot change the native continuation class. Under the
current continuation rule (D_d\tau_{future}=0), (d=1) gives constant
continuation, (d=2) linear continuation, (d=3) quadratic continuation, and
so on.

Therefore, increasing (d) must not be described as a substitute for estimating
a nonzero (mu). The roles are distinct:

[
d = \text{structural / continuation order},\qquad
mu = \text{reference drift of the }d\text{-th difference},\qquad
lambda = \text{strength of penalization around that structure}.
]

For paper wording, say **zero-drift finite-difference PLS** or **the
(mu=0) special case of Guerrero (2007)**. The Brent-based numerical search is
not inherently tied to (mu=0); the present analytic derivative identities
are. A Guerrero plug-in-drift version is therefore a natural robustness
extension, not a prerequisite for the validity of the current numerical paper.

## B. Guerrero (2007) plug-in drift formulation

The Guerrero (2007) source has now been checked directly. The paper first gives the known-drift estimator

$$
\widehat\tau_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}
\left(
y+
\lambda\widehat m_yD_d^\top\mathbf1
\right),
$$

and then, in equation (17), estimates the unknown drift from the observed differences:

$$
\boxed{
\widehat m_y
=
\frac{1}{N-d}\mathbf1^\top D_d y.
}
$$

Substitution gives equation (18):

$$
\boxed{
\widehat\tau_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}
\left(
y+
\lambda\widehat m_yD_d^\top\mathbf1
\right).
}
$$

With the observed sample fixed, $\widehat m_y$ does not depend on $\lambda$.

## C. Historical iterative library variant

The repository previously initialized a drift and repeatedly updated it from the fitted trend. That procedure is not Guerrero (2007) equation (18).

It is retained only for reproducibility under the explicit name:

**IteratedDriftTrend**

or equivalently `drift_mode="iterated"`.

**Library**

- `src/trend_estimation/core/solvers.py::GuerreroSpectralSolver`
- `src/trend_estimation/models/guerrero.py::IteratedDriftTrend`

The canonical `GuerreroTrend` now uses `drift_mode="data"` and implements model B.

## D. Possible jointly estimated drift model

If we intentionally study

$$
\min_{t,m}
\left\{
\|y-t\|_2^2+
\lambda\|D_dt-m\mathbf1\|_2^2
\right\},
$$

then minimizing over $m$ gives

$$
m(t)=\frac{1}{N-d}\mathbf1^\top D_dt.
$$

Let

$$
P
=
I-
\frac{1}{N-d}\mathbf1\mathbf1^\top.
$$

Substitution yields the equivalent quadratic problem

$$
\min_t
\left\{
\|y-t\|_2^2+
\lambda\|P D_dt\|_2^2
\right\},
$$

with solution

$$
\widehat t
=
\left(
I+\lambda D_d^\top P D_d
\right)^{-1}y.
$$

This is mathematically attractive because it again has the pure quadratic form with a modified penalty matrix. However, it is a separate model and should receive its own name if we decide to implement it.

## Active-paper policy

The forecast-optimal-smoothing paper should begin with model A because its derivative and forecast objective can be stated exactly and tested cleanly.

Model B is now a literature-aligned extension available for robustness comparisons. Model C is historical/reproducibility only. Model D remains a separate possible methodological extension.

## E. Forecast-CV de media de diferencias (NEW — 2026-10-11)

Para cada S en el caso de Guerrero con centro fijo μ,
la identidad del término afín es
\[
\widehat\tau_{\lambda,\mu}
=H_\lambda x+\mu(I-H_\lambda)p,\qquad
p_j=\binom jd,\quad D_dp=\mathbf1.
\]
Se utiliza el operador de continuación afín:
\[
\widehat z_{t,h}(S,\mu)
=G_{d,h}\widehat\tau_{t}(S,\mu)+\mu g_{d,h}
=a_t(S)+\mu b(S).
\]

El **estimador de μ por errores h-step completados**,
introducido como propuesta separada, no es equivalente
a ninguna de las letras A–D anteriores:
\[
\widehat\mu(S)=
\frac{\sum_q \widetilde w_q
b(S)^\top(z_q-a_q(S))}
{\|b(S)\|^2},\qquad \|b(S)\|^2>0,
\]
y luego \(\widehat S=\arg\min_S F(S,\widehat\mu(S))\).

**Tres métodos del código nuevo:**
\`zero\` (modelo A),
\`guerrero\` (B, plug-in **por ventana**),
\`profile\` (nueva política h-step con μ común entre folds).
Modelo D (optimizar μ dentro de UNA penalización in-sample)
cambia el núcleo a dimensión d+1 y no debe confundirse
con \`profile\`.

**Advertencia EDF:** cuando μ_G=c'x, el operador es
H+b c' y sus EDF son tr(H)+c'b; la coordenada
S basada en tr(H) no es ya automáticamente
el EDF del procedimiento completo.

**Fuente de derivaciones Obsidian:**
\`conceptos/06-Media-de-diferencias-Guerrero.md\` y
\`conceptos/07-Perfilamiento-de-mu-en-CV.md\`.

**Mapping:**
\`src/trend_estimation/forecasting/mean_difference_cv.py\`,
\`experiments/mean_difference_forecasting/run_pilot.py\`,
\`tests/test_mean_difference_forecast_cv.py\`.
Paper nuevo:
\`working_papers/Working Paper - Trend Simulation and Mean-Difference Forecasting/\`.

**Estado:** planteamiento derivado e implementado en nueva ruta,
experimentos/test de usuario pendientes; no equivale a
un hallazgo de superioridad confirmado.

## Library mapping rule

Any implementation change to these models must update this note and `notes/key_results.md`. Any manuscript statement calling a model "Guerrero" must cite the exact estimator definition being used.
