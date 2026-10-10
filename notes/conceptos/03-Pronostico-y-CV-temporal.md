---
tags: [forecasting, validacion-temporal, suavizamiento]
estado: definido-en-protocolos
---
# 03 · ¿Qué queremos pronosticar?

**Pregunta.** ¿Por qué escoger $\lambda$ mediante el MSE de reconstrucción no resuelve nuestro problema?

El objetivo científico del primer working paper es seleccionar suavidad por errores de predicción genuinamente futuros, no por ajuste dentro de la muestra.

## Información disponible en cada origen

Fijemos el orden $d$, la ventana $L$, el horizonte $h$ y un origen histórico $r$. Sea

$$
x_r=y_{r-L+1:r}\in\mathbb R^L,\qquad
z_r=y_{r+1:r+h}\in\mathbb R^h.
$$

Ajustamos únicamente con $x_r$:

$$
\widehat\tau_r(\lambda)=H_\lambda x_r.
$$

El operador lineal $G_{d,h}$ extrapola $h$ pasos mediante **diferencia futura de orden $d$ igual a cero**. Por ejemplo, $d=1$ continúa constante y $d=2$ continúa lineal. La predicción es

$$
\widehat z_r(\lambda)=G_{d,h}H_\lambda x_r.
$$

Definimos la pérdida observada cuando el futuro se revela:

$$
\boxed{\ell_r(\lambda)=
\frac1h\lVert z_r-G_{d,h}H_\lambda x_r\rVert_2^2.}
$$

## ¿Cómo evitar la fuga temporal?

Al elegir una suavidad operativa en el instante $T$, sólo se admiten orígenes **completados**:

$$
\boxed{r+h\le T.}
$$

Con pesos predeclarados $w_{T,r}\ge0$ y $\sum_rw_{T,r}=1$, la superficie agregada es

$$
F_T(S)=\sum_{r:\,r+h\le T}
w_{T,r}\,\ell_r\bigl(\lambda(S)\bigr).
$$

Se minimiza la **función agregada**, no el promedio de $\arg\min\ell_r$. El pronóstico operativo se construye después, usando la ventana más reciente, sin observar el bloque futuro externo.

## Tres objetos que no hay que confundir

- Estimar $H_\lambda x_r$: suavizar el pasado.
- Elegir $S$ o $\lambda$ por $F_T$: seleccionar un hiperparámetro usando pronósticos históricos ya evaluables.
- Medir $y_{T+1:T+h}$: evaluación externa; esos datos no pueden intervenir en la elección en $T$.

Ver [[nested_validation|evaluación anidada]], [[derivative|derivadas existentes]] y [[conceptos/04-Derivadas-y-optimizacion|derivación siguiente]]. Los protocolos vigentes del primer working paper están [fuera del vault en GitHub](https://github.com/heri-espino/Trend-Estimation/tree/main/working_papers/Working%20Paper%20-%20Smoothness%20Cross%20Validation).
