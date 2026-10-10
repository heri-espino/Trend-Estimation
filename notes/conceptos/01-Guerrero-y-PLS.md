---
tags: [matematicas, suavizamiento, derivacion]
estado: demostrado-en-latex
---
# 01 · De Guerrero a PLS

**Pregunta.** ¿Por qué una descomposición de señal y ruido lleva a mínimos cuadrados penalizados?

## Supuestos y notación

Sea $y,\tau\in\mathbb R^L$ y $D_d\in\mathbb R^{(L-d)\times L}$ el operador de diferencias de orden $d$, con $1\le d<L$.

$$
y=\tau+\eta,\qquad D_d\tau=\mu\mathbf 1+\varepsilon.
$$

En la formulación de Guerrero (2007): $\mathbb E(\eta)=0$, $\operatorname{Var}(\eta)=\sigma_\eta^2V$, $\mathbb E(\varepsilon)=0$, $\operatorname{Var}(\varepsilon)=\sigma_\varepsilon^2 I$, $\operatorname{Cov}(\eta,\varepsilon)=0$ y $V\succ0$. El cociente de varianzas es $\lambda=\sigma_\eta^2/\sigma_\varepsilon^2$.

## ¿Qué función se minimiza?

$$
J_G(u;\lambda)=
(y-u)^\top V^{-1}(y-u)
+\lambda\lVert D_du-\mu\mathbf1\rVert_2^2.
$$

La derivada respecto de $u$ es

$$
\nabla_uJ_G=
2(V^{-1}+\lambda D_d^\top D_d)u
-2(V^{-1}y+\lambda\mu D_d^\top\mathbf1).
$$

Igualando a cero:

$$
\boxed{
\widehat\tau_G=
(V^{-1}+\lambda D_d^\top D_d)^{-1}
(V^{-1}y+\lambda\mu D_d^\top\mathbf1).
}
$$

**¿Por qué es único?** Para cualquier $a\ne0$,

$$
a^\top(V^{-1}+\lambda D_d^\top D_d)a
=a^\top V^{-1}a+\lambda\lVert D_da\rVert_2^2>0
$$

porque $V^{-1}\succ0$ y $\lambda\ge0$. La Hessiana es definida positiva.

## Especialización del proyecto

Fijar **por decisión de modelado** $\mu=0$ y $V=I_L$ produce

$$
\boxed{\widehat\tau_\lambda
=(I_L+\lambda Q_d)^{-1}y,\qquad Q_d=D_d^\top D_d.}
$$

Esto no demuestra que las diferencias reales de toda tendencia tengan media cero. $V=I$ tampoco implica independencia de los errores sin supuestos adicionales.

La derivación completa del predictor LMMSE, su covarianza y la relación con la estimación de Guerrero están en [[notes_on_smoothnes/README|la clase LaTeX]], sección 1, y en [[model_definitions|la auditoría de variantes]]. Continuar con [[conceptos/02-Geometria-espectro-y-EDF|la geometría de $Q_d$]].

**Estado:** resultado algebraico, no evidencia de superioridad de pronóstico.
