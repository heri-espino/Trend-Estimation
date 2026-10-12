# Proof ledger · Medio de diferencia y suavidad de pronóstico

**Estado:** [FUENTE] publicado por Guerrero; [DERIVADO] demostrado
aquí con álgebra clásica; [PROPUESTA] nuevo objetivo de decisión;
[ABIERTO] pendiente. Demostraciones extensas y pasadas a Obsidian:
\`notes/conceptos/06-Media-de-diferencias-Guerrero.md\` y
\`07-Perfilamiento-de-mu-en-CV.md\`.

## T1. [FUENTE/DERIVADO] Solución única de PLS para μ fijo

Para \(\lambda\ge0\), \(1\le d<L\):
\[
\nabla_\tau J=2[(I+\lambda D^\top D)\tau-x-
\lambda\mu D^\top\mathbf1].
\]
Su Hessiana \(2(I+\lambda D^\top D)\succ0\)
pues \(v^\top(I+\lambda Q)v=\|v\|^2+\lambda\|Dv\|^2>0\).
Hay un único minimizador:
\[
\widehat\tau_{\lambda,\mu}
=H_\lambda x+\mu\lambda H_\lambda D^\top\mathbf1.
\]
Conocido de Guerrero 2007, NO un teorema propio original.

## T2. [DERIVADO] Transformación particular estable

Tomar \(p_j=\binom jd\) y usar
\(\Delta \binom j d=\binom j{d-1}\) repetidamente.
Entonces \(Dp=\mathbf1\), \(Qp=D^\top\mathbf1\),
\(\lambda HQ=I-H\) para \(\lambda\) finito.
Por sustitución:
\[
\boxed{\widehat\tau=H x+\mu(I-H)p.}
\]
La segunda expresión extiende continuamente el
ajuste a \(S=1\) e impone \(D\widehat\tau=\mu\mathbf1\).

## T3. [DERIVADO] Futura diferencia igual a μ

Si los últimos d estados de la tendencia están
fijos y continuamos imponiendo \(\Delta^d\tau=\mu\),
la recurrencia lineal produce:
\[
\widehat z=G\widehat\tau+\mu g,\quad
g(k)=\binom{k+d-1}{d},\qquad k\ge1.
\]
Para d=1: \(g(k)=k\); d=2: \(g(k)=k(k+1)/2\).
En particular, \(S=1\) es un **polinomio de grado d**
si μ no es cero, no grado d−1.

## T4. [DERIVADO/PROPUESTA] Perfilado de μ sobre F histórica

\(F(S,\mu)=\sum_q\widetilde w_q h^{-1}
\|r_q(S)-\mu b(S)\|^2\) con pesos fijos
no negativos normalizados y pseudo-futuros COMPLETADOS.
Definir:
\[
A=\sum_q\widetilde w_q\|r_q\|^2/h,\quad
C=\sum_q\widetilde w_q b^\top r_q/h,\quad
B=\|b\|^2/h.
\]
Expandiendo cada cuadrado:
\(F=A-2\mu C+\mu^2 B\).
Si B>0, \(F_\mu=-2C+2\mu B=0\) da el
único minimizador \(\mu^*=C/B\) (ya que \(F_{\mu\mu}=2B>0\)).
Completar el cuadrado:
\[
F=B(\mu-\mu^*)^2+A-C^2/B,\quad
\boxed{\widetilde F(S)=A-C^2/B.}
\]
Si B=0, μ no está identificada. Que \(\widetilde F(S)
\le F(S,0)\) **en los folds usados para seleccionar**
NO es prueba de riesgo futuro menor.

## T5. [DERIVADO] Fórmula exacta de curvatura perfilada

Suponer F dos veces continuamente diferenciable,
S interior, \(F_\mu(S,\mu^*)=0\), \(F_{\mu\mu}>0\).
La identidad derivada de la FOC es:
\[
\mu^{*\prime}=-F_{S\mu}/F_{\mu\mu}.
\]
Envolvente:
\(\widetilde F'=F_S+F_\mu\mu^{*\prime}=F_S\).
Derivar de nuevo y sustituir:
\[
\boxed{\widetilde F''=
F_{SS}-F_{S\mu}^2/F_{\mu\mu}.}
\]
Esto es cálculo/Schur complement conocido; no garantiza
convexidad, unicidad ni alguna mejoría de pronóstico.

## T6. [DERIVADO] Traza del operador de ajuste plug-in

\(\mu_G=c^\top x\) con
\(c=D^\top\mathbf1/(L-d)\), y sea \(b=(I-H)p\).
Entonces \(\widehat\tau_G=(H+bc^\top)x\). Por la
linealidad de traza y \(\operatorname{tr}(bc^\top)=c^\top b\):
\[
\operatorname{edf}_G=\operatorname{tr}H+c^\top b.
\]
**No atribuir automáticamente este EDF** al
modelo con μ elegida por CV histórico o al selector
completo que también optimiza S.

## T7. [DERIVADO] Estimar μ dentro de penalización es OTRO modelo

Para \(\min_{\tau,\mu}\|x-\tau\|^2+
\lambda\|D\tau-\mu\mathbf1\|^2\),
FOC en μ:
\(\mu=\mathbf1^\top D\tau/(L-d)\).
Proyector \(P=I-\mathbf1\mathbf1^\top/(L-d)\).
Eliminar μ da \(Q_*=D^\top PD\), con
\(\ker Q_*=\{\tau:D\tau=c\mathbf1\}\).
Si D es la matriz usual de orden d,
el núcleo tiene dimensión d+1.
No confundir con perfilado de μ para CV:
tienen diferente información y diferente Q.

## T8. [ABIERTO] Existencia, identificabilidad y mínimos

Para B(S)>0 y continuidad de los objetos,
\(\widetilde F(S)\) es continua en vecindario;
en el dominio compacto puede haber situaciones
de degeneración de B que requieren análisis
separado. El mismo modelo puede producir
muchos mínimos locales, empates y cambios
de geometría frente al caso μ=0.
Demostrar condiciones globales para existencia
y estabilidad numérica; no asumir unicidad.

## T9. [ABIERTO] Riesgo y comparación causal

La superioridad de μ perfilada sobre Guerrero, μ=0
y pronósticos naive/drift/OLS es HIPÓTESIS.
Hay que medir errores de la misma réplica/semilla
y no mirar test para escoger método/h.
Si se aprende μ sobre pocos folds recientes,
la varianza puede aumentar incluso cuando el
historial de validación mejora.

## T10. [ABIERTO] Extensiones de ramas/Sturm

Por álgebra espectral finita,
la F(S,μ) del modelo fijo es una
función estructurada y el perfilado
cambia su geometría. Buscar derivadas
de \(\widetilde F\), propiedades
racionales cuando datos exactos, y
tracking por método m, siempre
separando casos degenerados y
certificados pequeños de Sturm.
No reciclar sin rehacer las
afirmaciones numéricas del caso μ=0.
