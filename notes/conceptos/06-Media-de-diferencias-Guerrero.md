---
title: "06 · Guerrero: media no nula de diferencias y extrapolación"
tags: [trend-estimation, Guerrero-2007, PLS, differences, background, proof]
status: derived-from-source-and-classical-algebra
source: "Guerrero (2007), Statistics & Probability Letters 77, 1225–1234, ecuaciones (2), (3), (12), (16)–(18)"
---
# 06 · ¿Qué ocurre si las diferencias de la tendencia tienen media distinta de cero?

> [!source] Fuente verificada
> Guerrero, V. M. (2007), *Time series smoothing by penalized least squares*, **Statistics & Probability Letters** 77, 1225–1234, DOI 10.1016/j.spl.2007.03.006. Aquí se separa fielmente su **estimador de media plug-in** de nuestra **nueva propuesta forecast-CV para esa media**. No atribuir el perfilamiento por CV a Guerrero.

## 1. Pregunta: ¿cuál es el modelo anterior y qué simplificamos?

Sea un tramo observado de longitud $L$:

$$
x=(y_{t-L+1},\ldots,y_t)^\top,\qquad 1\le d<L.
$$

Con diferencias consecutivas $D_d\in\mathbb R^{(L-d)\times L}$, el problema usual **puro** era:

$$
\widehat\tau_{\lambda,0}
=\arg\min_{\tau\in\mathbb R^L}
\left\{\|x-\tau\|^2+\lambda\|D_d\tau\|^2\right\}.
$$

Guerrero (2007), eq. (2), permite un **nivel de referencia $\mu$** para las diferencias; eq. (3) interpreta $\Delta^d\tau_t=\mu+\varepsilon_t$, bajo sus supuestos probabilísticos. El funcional con $V=I$ es:

$$
\boxed{
J(\tau;\lambda,\mu)=
\|x-\tau\|^2+\lambda\|D_d\tau-\mu\mathbf1\|^2.
}
$$

$\mu$ significa media/referencia **de las diferencias de la tendencia**, NO la media de las observaciones $y$, NO la media de $\widehat\tau$ y NO la selección de suavidad $S$.

## 2. ¿Por qué hay que diferenciar dos parámetros?

- $d$ fija el orden de las diferencias y el tipo de continuación.
- $\lambda$ fija la fuerza de penalización respecto de $\mu$.
- $\mu$ fija el centro de las diferencias de orden $d$.
- $S$ reexpresa monotónicamente $\lambda$ para $L,d$ fijos; NO es otra matriz.

El problema **con $\mu$ fijo** sigue siendo cuadrático estrictamente convexo en $\tau$. Si se estima $\mu$ de los datos o de validación, ese procedimiento introduce una segunda fuente de flexibilidad que no puede ignorarse al interpretar EDF.

## 3. Demostración paso a paso del estimador con $\mu$ fijo

Escribimos $Q=D_d^\top D_d$. Expandiendo los productos:

$$
\begin{aligned}
J(\tau)
&=(x-\tau)^\top(x-\tau)
+\lambda(D_d\tau-\mu\mathbf1)^\top(D_d\tau-\mu\mathbf1)\\
&=x^\top x-2x^\top\tau+\tau^\top\tau\\
&\quad+\lambda\tau^\top Q\tau
-2\lambda\mu\mathbf1^\top D_d\tau
+\lambda\mu^2(L-d).
\end{aligned}
$$

Las derivadas respecto al **vector** $\tau$ son:

$$
\nabla_\tau J=-2x+2\tau+2\lambda Q\tau
-2\lambda\mu D_d^\top\mathbf1,
$$

$$
\nabla_\tau^2J=2(I+\lambda Q).
$$

Como para $v\ne0$ y $\lambda\ge0$:

$$
v^\top(I+\lambda Q)v=\|v\|^2+\lambda\|D_dv\|^2>0,
$$

la Hessiana es positiva definida. El único minimizador satisface:

$$
(I+\lambda Q)\widehat\tau=x+\lambda\mu D_d^\top\mathbf1,
$$

y, poniendo $H_\lambda=(I+\lambda Q)^{-1}$,

$$
\boxed{
\widehat\tau_{\lambda,\mu}
=H_\lambda x+\lambda\mu H_\lambda D_d^\top\mathbf1.
}
$$

**Guerrero ya estudió esta forma**. Nuestro proyecto no debe venderla como original.

## 4. ¿Podemos escribir el término de $\mu$ sin multiplicar por lambda?

Sí, y esta identidad es útil para el extremo $S=1$. Definimos para $j=0,\ldots,L-1$:

$$
p_j=\binom{j}{d}.
$$

Por la identidad de Pascal, $\Delta\binom jd=\binom j{d-1}$; al repetir $d$ diferencias se obtiene:

$$
D_dp=\mathbf1.
$$

Por tanto $Qp=D_d^\top D_dp=D_d^\top\mathbf1$. Al multiplicar por $H_\lambda$:

$$
\lambda H_\lambda Q
=H_\lambda[(I+\lambda Q)-I]
=I-H_\lambda.
$$

Luego:

$$
\boxed{
b_\lambda:=\lambda H_\lambda D_d^\top\mathbf1
=(I-H_\lambda)p.
}
$$

**Resultado derivado (no novedoso por sí mismo)**:

$$
\boxed{
\widehat\tau_{\lambda,\mu}
=H_\lambda x+\mu (I-H_\lambda)p
=\mu p+H_\lambda(x-\mu p).
}
$$

Interpretación: se resta el componente polinomial particular $\mu p$, se suaviza el residuo y se devuelve $\mu p$.

## 5. ¿Qué pasa en los dos extremos de suavidad?

Si $\lambda=0$, entonces $H_0=I$ y $(I-H_0)p=0$:

$$
\widehat\tau_{0,\mu}=x.
$$

Si $\lambda\to\infty$, el límite del suavizador es el proyector $P_0$ sobre $\ker D_d$, por lo que

$$
\boxed{
\widehat\tau_{\infty,\mu}
=P_0x+\mu(I-P_0)p.
}
$$

Apliquemos $D_d$:

$$
D_dP_0x=0,\qquad D_d(I-P_0)p=D_dp=\mathbf1.
$$

Entonces

$$
\boxed{D_d\widehat\tau_{\infty,\mu}=\mu\mathbf1.}
$$

**Cuidado:** en el caso $\mu\ne0$, el límite NO es solamente el polinomio de grado $d-1$; pertenece a una familia **afín** de polinomios de grado $d$. El límite corresponde a mínimos cuadrados sujeto a diferencias $d$-ésimas constantes e iguales a $\mu$.

## 6. La media plug-in de Guerrero: ¿de dónde sale?

Guerrero propone, eq. (17), usar la media **observada** de las diferencias:

$$
\boxed{
\widehat\mu_{\rm G}(x)=
\frac{1}{L-d}\mathbf1^\top D_dx.
}
$$

Para $d=1$, $\sum_{i=2}^L(y_i-y_{i-1})=y_L-y_1$, por lo que

$$
\widehat\mu_{\rm G}(x)=\frac{y_L-y_1}{L-1}.
$$

En $d=2$, la suma telescópica produce la diferencia entre la última y primera **pendiente discreta**:

$$
\widehat\mu_{\rm G}(x)
=\frac{(y_L-y_{L-1})-(y_2-y_1)}{L-2}.
$$

**La media plug-in se recalcula dentro de cada ventana** del forecast-CV; no se puede estimar con observaciones del bloque de test exterior.

## 7. ¿Cómo cambian realmente los grados de libertad?

Con $\mu$ **externo y fijo**, el Jacobiano del ajuste respecto de x es $H_\lambda$; sus EDF lineales son $\operatorname{tr}(H_\lambda)$.

Si $\widehat\mu_G=c^\top x$, con

$$
c=\frac{D_d^\top\mathbf1}{L-d},
$$

entonces

$$
\widehat\tau_G=(H_\lambda+b_\lambda c^\top)x.
$$

El operador de ajuste **plug-in** es

$$
\boxed{
A_{\lambda,G}=H_\lambda+b_\lambda c^\top,
\qquad
\operatorname{edf}_G
=\operatorname{tr}(H_\lambda)+c^\top b_\lambda.
}
$$

La segunda igualdad sale de $\operatorname{tr}(bc^\top)=c^\top b$.
El índice $S=(L-\operatorname{tr}H_\lambda)/(L-d)$ sigue siendo una **coordenada de penalización**, pero NO mide sin corrección los EDF del estimador con $\widehat\mu$ estimada de x. Si $\mu$ se ajusta con CV sobre muchas ventanas y se optimiza además S, no basta esta fórmula para asignarle EDF al selector no lineal completo.

## 8. Pronosticar: ¿cómo entra la media futura?

El operador implementado en \`forecasting/operators.py\` es **afín**:

$$
\widehat z_{t,h}(S,\mu)
=G_{d,h}\widehat\tau_t(S,\mu)+\mu g_{d,h}.
$$

El vector $g$ proviene de exigir **en el futuro** $\Delta^d\tau=\mu$; para los pasos $k=1,\ldots,h$,

$$
g_{d,h}(k)=\binom{k+d-1}{d}.
$$

Con $d=1$: $\widehat\tau_{t+k}=\widehat\tau_t+k\mu$.
Con $d=2$: $\widehat\tau_{t+k}=(k+1)\widehat\tau_t-k\widehat\tau_{t-1}+\binom{k+1}{2}\mu$.

Sustituyendo el ajuste:

$$
\widehat z_{t,h}(S,\mu)
=\underbrace{G_{d,h}H(S)x_t}_{a_t(S)}
+\mu\underbrace{[G_{d,h}(I-H(S))p+g_{d,h}]}_{b(S)}.
$$

Por eso el pronóstico depende **afínmente** de $\mu$ para cada S fijo.

## 9. Tres problemas que NO deben mezclarse

1. **Fijo:** elegir un $\mu$ externo y minimizar penalización en $\tau$.
2. **Guerrero plug-in:** estimar $\mu$ como media de $D_dx$ **dentro de cada ventana** y después suavizar; eqs. (17)–(18) del autor.
3. **Perfilado forecast-CV (propuesta):** elegir $\mu$ para minimizar errores **de pronóstico históricos completados**, compartiendo un solo $\mu$ entre orígenes para una configuración $(d,L,h,m,S)$ dada.

Un cuarto problema distinto sería minimizar la penalización **sobre $\tau$ y $\mu$ usando la misma ventana in-sample**. Si eliminamos $\mu$ de esa penalización, la matriz cambia (ver [[07-Perfilamiento-de-mu-en-CV|nota 07]]). NO llamarlo modelo 3.

## 10. Mapeo exacto al código y preguntas abiertas

- Guerrero publicado: \`src/trend_estimation/core/solvers.py::GuerreroSpectralSolver\` (ya existía antes).
- Pronóstico afín: \`src/trend_estimation/forecasting/operators.py\` (ya existía antes).
- Nueva identidad estable en el extremo y selector CV: \`src/trend_estimation/forecasting/mean_difference_cv.py\`.
- Derivaciones sobre el perfilado: [[07-Perfilamiento-de-mu-en-CV|nota 07]].
- Nuevo paper: [[08-Nuevo-paper-tendencia-y-media|nota 08]].

> [!warning] Alcance de los resultados
> Son identidades algebraicas y una hipótesis estadística de mejora, NO evidencia de que pronosticar con $\mu$ perfilada supere en promedio a Guerrero, al caso $\mu=0$ o a naive/drift/OLS. No alterar retrospectivamente las semillas ni la definición de métodos de la campaña GPU que está en marcha.
