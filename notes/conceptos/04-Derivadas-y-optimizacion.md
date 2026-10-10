---
tags: [matematicas, derivacion, optimizacion]
estado: demostrado-en-latex
---
# 04 · Derivadas del suavizador y del pronóstico

**Pregunta.** ¿Cómo calcular la sensibilidad de la pérdida de pronóstico frente a $\lambda$ sin diferencias finitas?

Sean $Q=D_d^\top D_d$ y $H_\lambda=(I+\lambda Q)^{-1}$. El operador $G_{d,h}$ es fijo respecto de $\lambda$ para un modelo de continuación determinado.

## Derivar una inversa matricial

De $(I+\lambda Q)H_\lambda=I$ se obtiene, por regla del producto:

$$
QH_\lambda+(I+\lambda Q)H_\lambda'=0.
$$

Multiplicando por $H_\lambda$:

$$
\boxed{H_\lambda'=-H_\lambda QH_\lambda.}
$$

La segunda derivada usa de nuevo el producto:

$$
H_\lambda''=
-H_\lambda'QH_\lambda-H_\lambda QH_\lambda'
=2H_\lambda QH_\lambda QH_\lambda.
$$

Como $Q$ conmuta con cualquier función racional de sí misma, la inducción da

$$
\boxed{
\frac{d^kH_\lambda}{d\lambda^k}
=(-1)^kk!\,H_\lambda(QH_\lambda)^k.
}
$$

## Derivadas de un MSE futuro

Fijemos un origen y escribamos $x=x_r$, $z=z_r$, $G=G_{d,h}$ y $e(\lambda)=z-GH_\lambda x$.

$$
e'=GH_\lambda QH_\lambda x,\qquad
e''=-2GH_\lambda QH_\lambda QH_\lambda x.
$$

Con $\ell(\lambda)=h^{-1}e^\top e$:

$$
\boxed{
\ell'(\lambda)=\frac2h\,
e^\top GH_\lambda QH_\lambda x.
}
$$

Y otra derivación por producto proporciona

$$
\boxed{
\ell''(\lambda)=\frac2h\left[
\lVert GH_\lambda QH_\lambda x\rVert_2^2-
2e^\top GH_\lambda QH_\lambda QH_\lambda x
\right].
}
$$

La curvatura $\ell''$ no tiene signo fijo: el MSE futuro **no** es necesariamente convexo en $\lambda$.

Al cambiar a la coordenada $S(\lambda)$, para puntos interiores

$$
\frac{dF}{dS}=
\frac{df/d\lambda}{dS/d\lambda},\qquad
f(\lambda)=F(S(\lambda)).
$$

Los extremos $S=0,1$ requieren tratamiento por límites y comparación directa.

Véanse [[derivative|las derivaciones implementadas]], [[numerical_selection|el buscador numérico]] y [[conceptos/05-Tres-problemas-de-investigacion|la separación de los tres papers]].
