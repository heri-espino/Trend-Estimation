---
title: "07 · Minimizacion analitica de mu en forecast-CV"
tags: [trend-estimation, profile-optimization, forecast-cv, proof, obsidian]
status: derived-and-new-empirical-question
---
# 07 · ¿Podemos optimizar S y la media de diferencias sin una búsqueda bidimensional?

**Prerequisito:** [[06-Media-de-diferencias-Guerrero|modelo de Guerrero con media no nula]].

## 1. Objetivo: pronosticar, no ajustar diferencias al pasado

A tiempo T disponemos solamente de $y_{1:T}$. Fijamos la longitud L, orden d, horizonte h y método de ponderación temporal m. Sea $t_q$ una sucesión **creciente** de orígenes históricos con $t_q+h\le T$; sus futuros son pasados *al seleccionar en T*.

Para cada origen $q$ y S, el pronóstico afín es

$$
\widehat z_q(S,\mu)=a_q(S)+\mu b(S).
$$

Los vectores se construyen exclusivamente a partir de $x_q=y_{t_q-L+1:t_q}$ y los operadores fijos $G,H$; $a_q$ depende de x y S, mientras que $b$ depende de $(d,L,h,S)$ y **no de q** cuando todas las ventanas tienen la misma longitud. Definimos $z_q=y_{t_q+1:t_q+h}$ y $r_q(S)=z_q-a_q(S)$.

Con pesos históricos predefinidos $\widetilde w_q\ge0$, $\sum\widetilde w_q=1$:

$$
\boxed{
F_T(S,\mu)=\sum_q\widetilde w_q\,
\frac1h\|r_q(S)-\mu b(S)\|^2.
}
$$

## 2. Expande el cuadrado sin saltar pasos

Para vectores $r,b$:

$$
\begin{aligned}
\|r-\mu b\|^2
&=(r-\mu b)^\top(r-\mu b)\\
&=r^\top r-r^\top(\mu b)-(\mu b)^\top r+\mu^2b^\top b\\
&=\|r\|^2-2\mu b^\top r+\mu^2\|b\|^2.
\end{aligned}
$$

Sustituimos dentro de la suma:

$$
F_T(S,\mu)=
\underbrace{\sum_q\frac{\widetilde w_q}{h}\|r_q(S)\|^2}_{A(S)}
-2\mu\underbrace{\sum_q\frac{\widetilde w_q}{h}b(S)^\top r_q(S)}_{C(S)}
+\mu^2\underbrace{\frac{\|b(S)\|^2}{h}}_{B(S)}.
$$

El último término no requiere suma explícita porque los pesos están normalizados. Por tanto

$$
\boxed{F_T(S,\mu)=A(S)-2C(S)\mu+B(S)\mu^2.}
$$

## 3. ¿Cómo resolvemos mu para S fijo?

Derivamos en $\mu$:

$$
\frac{\partial F}{\partial\mu}=-2C+2B\mu,
\qquad
\frac{\partial^2F}{\partial\mu^2}=2B.
$$

Si $B(S)>0$, la derivada se anula **en un único punto**:

$$
\boxed{\widehat\mu(S)=\frac{C(S)}{B(S)}
=\frac{\sum_q\widetilde w_q\,b(S)^\top[z_q-a_q(S)]}
{\|b(S)\|^2}.}
$$

Como $F_{\mu\mu}=2B>0$, es el minimizador global en $\mu$ (para S fijo).

Si $B=0$, el pronóstico no depende de $\mu$ en ese S: **no identificamos $\mu$** y registrar $\mu=0$ es solo una convención reproducible, no una estimación científica.

## 4. Completar el cuadrado: ¿cuánto cambia la pérdida?

$$
\begin{aligned}
F_T(S,\mu)
&=A-2C\mu+B\mu^2\\
&=A-\frac{C^2}{B}
+B\left(\mu-\frac{C}{B}\right)^2.
\end{aligned}
$$

Con $B>0$:

$$
\boxed{
\widetilde F_T(S)
:=\min_\mu F_T(S,\mu)
=A(S)-\frac{C(S)^2}{B(S)}.
}
$$

De aquí se sigue $\widetilde F_T(S)\le F_T(S,0)$ **en el historial usado para elegir**. ¡No se sigue que el riesgo fuera de muestra disminuya! Al estimar un parámetro adicional, podemos sobreajustar los pseudo-futuros.

La selección final vuelve a ser unidimensional:

$$
\boxed{\widehat S_T\in\arg\min_{S\in[0,1]}\widetilde F_T(S),
\qquad
\widehat\mu_T=\widehat\mu(\widehat S_T).}
$$

Después reajustamos **una sola vez** sobre los últimos L datos disponibles, con ese mismo $(\widehat S_T,\widehat\mu_T)$, y pronosticamos h periodos. La observación $y_{T+1:T+h}$ se reserva para evaluación.

## 5. ¿Y si se quiere usar exactamente Guerrero?

Para cada origen q, la media de Guerrero es

$$
\widehat\mu_q^{G}
=\frac{\mathbf1^\top D_dx_q}{L-d}.
$$

Su función de evaluación es

$$
F_T^{G}(S)=\sum_q\widetilde w_q\,
\frac1h\|z_q-a_q(S)-\widehat\mu_q^G b(S)\|^2.
$$

En el origen final T debemos utilizar $\widehat\mu_T^G$ calculado de $x_T$, **no** las $\widehat\mu_q$ y **no** $\widehat\mu(S)$ del modelo perfilado.

**Distinción:** el perfilado supone un único $\mu$ compartido a través de los orígenes de validación, mientras Guerrero tiene un estimador plug-in distinto por ventana. Deben compararse explícitamente, no tratarse como la misma regla.

## 6. Derivadas de la función concentrada: demostración completa

Supongamos $F(S,\mu)$ dos veces continuamente diferenciable para $S$ interior, $B(S)>0$, y sea $\mu^*(S)$ su mínimo, de modo que $F_\mu(S,\mu^*)=0$. Definimos

$$
\widetilde F(S)=F(S,\mu^*(S)).
$$

**Primera derivada: regla de la cadena**

$$
\begin{aligned}
\widetilde F'(S)
&=F_S(S,\mu^*(S))
+F_\mu(S,\mu^*(S))\,\mu^{*\prime}(S)\\
&=F_S(S,\mu^*(S)),
\end{aligned}
$$

pues $F_\mu=0$ en el óptimo interior.

**Derivamos la condición de primer orden:** 

$$
0=\frac{d}{dS}F_\mu(S,\mu^*(S))
=F_{S\mu}+F_{\mu\mu}\mu^{*\prime}(S).
$$

Entonces, si $F_{\mu\mu}>0$,

$$
\boxed{
\mu^{*\prime}(S)=-\frac{F_{S\mu}}{F_{\mu\mu}}.
}
$$

**Segunda derivada de la función concentrada:**

$$
\begin{aligned}
\widetilde F''(S)
&=\frac{d}{dS}F_S(S,\mu^*(S))\\
&=F_{SS}+F_{S\mu}\mu^{*\prime}(S)\\
&=\boxed{F_{SS}-\frac{F_{S\mu}^2}{F_{\mu\mu}}}.
\end{aligned}
$$

La curvatura perfilada es la **complementación de Schur escalar** de la curvatura conjunta. Para una matriz hessiana conjunta evaluada en el óptimo de $\mu$, explica por qué optimizar $\mu$ puede aplanar o modificar los valles de la función en S. **No garantiza** que aparezcan nuevos mínimos ni que mejore la predicción.

## 7. ¡Cuidado! Otro problema: optimización de mu dentro de la penalización

Si en lugar de forecast-CV optimizamos simultáneamente $\tau,\mu$ sobre UNA ventana:

$$
\min_{\tau,\mu}\left\{
\|x-\tau\|^2+\lambda\|D_d\tau-\mu\mathbf1\|^2
\right\},
$$

la primera condición en $\mu$ produce

$$
\widehat\mu(\tau)=\frac{\mathbf1^\top D_d\tau}{L-d}.
$$

Definimos $P_\perp=I_{L-d}-\mathbf1\mathbf1^\top/(L-d)$, proyector sobre vectores de diferencias de media cero. Sustituyendo,

$$
\|D_d\tau-\widehat\mu(\tau)\mathbf1\|^2
=\|P_\perp D_d\tau\|^2.
$$

De aquí obtenemos un NUEVO problema de suavizado:

$$
\boxed{
\widehat\tau=
\left[I+\lambda D_d^\top P_\perp D_d\right]^{-1}x.
}
$$

El núcleo ahora son las secuencias con $D_d\tau$ constante: polinomios discretos hasta grado d; su dimensión es **d+1**, no d (cuando $1\le d<L$). Esto **no es** ni la media de Guerrero ni el perfilado de forecast-CV anterior. Hay que tratarlo como un cuarto procedimiento distinto, con otra definición de EDF y S si se investiga.

## 8. Posibles trampas estadísticas y cómo evitarlas

- Un μ compartido puede fallar si hay cambios de régimen; estudiar versión local/reciente después de comprobar el caso simple.
- No elegir d/L/h/m/rango de S mirando el test exterior y volver a llamar ese test "independiente".
- Las pérdidas overlapping de h pasos están correlacionadas; inferir a nivel serie/semilla.
- Si $\mu^*(S)$ crece demasiado cuando $B(S)$ es pequeño, medir **identificabilidad**/estabilidad y considerar límites *predeclarados*; no truncar sin informar.
- Reportar recuperación pasada de $\tau$, forecast de $\tau$ futura y forecast de y futuro, incluso si muestran conclusiones diferentes.
- El mínimo de $\widetilde F$ puede no ser único ni unimodal; el Paper numérico deberá revisitar raíces/Brent/Sturm bajo la nueva función, no asumir que conserva sus raíces.
- El score S basado en $\operatorname{tr}H$ no es automáticamente el EDF efectivo del selector con μ estimada.

## 9. ¿Qué implementamos y qué está pendiente?

**Ya implementado en código fuente:** \`src/trend_estimation/forecasting/mean_difference_cv.py\` con los tres modos, extremo S=1 exacto, validación de orígenes completados y mínimos cuadrados analíticos de μ(S).

**Pendiente:** validación en el entorno real, estudio Monte Carlo nuevo, derivadas numéricas de $\widetilde F$, certificación/contaje de raíces de la función concentrada para instancias pequeñas, tracking temporal de sus mínimos, y evidencia de novedad bibliográfica.

Sigue [[08-Nuevo-paper-tendencia-y-media|plan editorial del nuevo paper]].
