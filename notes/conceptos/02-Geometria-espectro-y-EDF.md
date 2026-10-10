---
tags: [matematicas, algebra-lineal, suavizamiento]
estado: demostrado-en-latex
---
# 02 · Núcleo, espectro y grados de libertad

**Pregunta.** ¿Por qué la matriz de penalización tiene exactamente $d$ autovalores nulos?

Sea $Q_d=D_d^\top D_d$ para $D_d\in\mathbb R^{(L-d)\times L}$, la matriz de diferencias finitas usual con $1\le d<L$.

## Demostración del núcleo

1. Una secuencia $u$ satisface $D_du=0$ si y sólo si sus diferencias de orden $d$ son cero.
2. Las secuencias $u_t=p(t)$ con $p$ polinomio de grado a lo más $d-1$ satisfacen esa ecuación, ya que cada diferencia reduce un grado.
3. Estas secuencias forman un espacio de dimensión $d$: los vectores de valores de $1,t,\ldots,t^{d-1}$ son linealmente independientes sobre $L\ge d$ puntos distintos.
4. La recurrencia de diferencias $D_du=0$ determina todos los términos posteriores a partir de los primeros $d$; no puede haber más de $d$ grados de libertad.

Por tanto

$$
\boxed{\dim\ker D_d=d.}
$$

Además,

$$
u^\top Q_du=\lVert D_du\rVert_2^2\ge0,
\qquad \ker Q_d=\ker D_d.
$$

Así, $Q_d$ es simétrica semidefinida positiva, $\operatorname{rank}Q_d=L-d$ y posee **exactamente $d$ autovalores cero**, contados con multiplicidad.

## Diagonalización y contracción

Por el teorema espectral, existe una matriz ortogonal $U$ tal que

$$
Q_d=U\operatorname{diag}(\delta_1,\dots,\delta_L)U^\top,
\quad \delta_i\ge0.
$$

Luego

$$
H_\lambda=(I+\lambda Q_d)^{-1}
=U\operatorname{diag}\left(\frac1{1+\lambda\delta_i}\right)U^\top.
$$

Sobre el núcleo el factor es $1$; sobre sus direcciones ortogonales está entre $0$ y $1$.

## Grados de libertad efectivos y suavidad

Para el estimador lineal $\widehat\tau=H_\lambda y$, definimos

$$
\operatorname{edf}(\lambda)=\operatorname{tr}H_\lambda
=d+\sum_{\delta_i>0}\frac1{1+\lambda\delta_i}.
$$

Para $\lambda$ finita y positiva: $d<\operatorname{edf}(\lambda)<L$; los límites en $0$ e infinito son $L$ y $d$, respectivamente.

La suavidad normalizada del proyecto es

$$
\boxed{
S_d(\lambda;L)=
\frac{L-\operatorname{edf}(\lambda)}{L-d},\qquad
\frac{dS}{d\lambda}=
\frac1{L-d}\sum_{\delta_i>0}
\frac{\delta_i}{(1+\lambda\delta_i)^2}>0.
}
$$

Por tanto la coordenada $\lambda\in[0,\infty]$ corresponde biunívocamente a $S\in[0,1]$ para $L>d$. La **pérdida de pronóstico** no tiene por qué ser inyectiva ni convexa.

Consultar [[key_results|resultados]], [[window_and_smoothness|dependencia de la ventana]] y la demostración extendida en [[notes_on_smoothnes/README|LaTeX]]. Siguiente: [[conceptos/03-Pronostico-y-CV-temporal|CV temporal]].
