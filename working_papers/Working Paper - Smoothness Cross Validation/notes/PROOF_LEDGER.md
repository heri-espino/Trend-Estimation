# Paper 1 · Registro de resultados matemáticos y demostraciones

**Estados:** [CLÁSICO] conocido, [DERIVADO] demostrado aquí pero no
necesariamente nuevo, [HIPÓTESIS] requerirá teoría/evidencia,
[PENDIENTE] no demostrado. Complementa
[mathematical_foundations.md](mathematical_foundations.md).
Cada resultado tiene suposiciones y consecuencia operativa.

## P1. ¿Por qué Q tiene exactamente d autovalores cero?
**[CLÁSICO, DERIVADO]** Sea \(1\le d<L\), \(D_d\) la matriz de
diferencias consecutivas de orden d sobre L puntos.
Sus L-d filas imponen L-d relaciones independientes: fijados
los primeros d valores, la recurrencia \(\Delta^d v=0\)
determina de forma única todos los demás. Por tanto
\(\dim\ker D_d=d\) y \(\operatorname{rank}D_d=L-d\).
Además
\[
v^\top D_d^\top D_dv=\|D_dv\|^2=0
\iff D_dv=0,
\]
de donde \(\ker Q=\ker D_d\), y Q simétrica
semidefinida positiva tiene exactamente d autovalores cero
(contando multiplicidades), el resto positivos.

**Significado:** al tomar \(\lambda\to\infty\), quedan
exactamente d grados de libertad polinomiales.

## P2. ¿Existe una tendencia óptima para lambda finito?
**[CLÁSICO, DERIVADO]** La función penalizada es
\(J(v)=\|x-v\|^2+\lambda v^\top Qv\).
\[
\nabla J(v)=2[(I+\lambda Q)v-x],\quad
\nabla^2 J(v)=2(I+\lambda Q).
\]
Para \(z\ne0\),
\(z^\top(I+\lambda Q)z=\|z\|^2+
\lambda\|D_dz\|^2>0\) si \(\lambda\ge0\).
Por tanto J es estrictamente convexa, tiene único
minimizador \(H_\lambda x\). Esto NO implica que
la pérdida externa F(S) sea convexa o unimodal.

## P3. ¿Cuáles son los límites de la suavidad?
**[CLÁSICO, DERIVADO]** Con
\(Q=U\operatorname{diag}(0_d,\delta_+)U^\top\),
\[
H_\lambda=U\operatorname{diag}
(1_d,(1+\lambda\delta_j)^{-1})U^\top.
\]
\(H_0=I\), y cuando \(\lambda\to\infty\) cada
\(\delta_j>0\) se suprime, mientras la dirección de
\(\ker Q\) conserva peso 1:
\(H_\infty=U_0U_0^\top\).
Es un proyector ortogonal de rango d, no matriz
invertible. Nunca aproximar este extremo usando un
lambda grande arbitrario si se puede evaluar exactamente.

## P4. ¿La coordenada S recorre la familia entera?
**[CLÁSICO, DERIVADO]** Definamos
\[
S(\lambda)=\frac{L-\sum_j(1+\lambda\delta_j)^{-1}}{L-d}.
\]
En los d modos cero no cambia el sumando 1. Para
lambda finito:
\[
S'(\lambda)=\frac1{L-d}\sum_{\delta_j>0}
\frac{\delta_j}{(1+\lambda\delta_j)^2}>0.
\]
Es continua, va de 0 en lambda=0 a 1
cuando lambda tiende a infinito; estrictamente
creciente y con inversa única en [0,1).
En d,L fijos \(\mathrm{edf}=L-(L-d)S\).
Por ello un minimizador **exacto** reparametrizado
produce idéntica curva y pronóstico en lambda y S.
La coordenada no cambia el estimador estadístico.

## P5. ¿Hay mínimo global de F(S)?
**[DERIVADO, existencia básica]** Supónganse
L,d,h y datos finitos, origen/ponderaciones fijos,
pesos no negativos con suma positiva. H(S) es
continua en [0,1] al incorporar su límite
proyector. Cada \(\ell_t(S)\), producto de matrices,
norma al cuadrado, es continua. La combinación
ponderada F es continua. Por Weierstrass alcanza
un mínimo global en el compacto [0,1].
**No demostramos unicidad, interioridad ni convexidad**.

Si dos S diferentes empatan, la implementación debe
establecer un criterio determinista, registrarlo y
considerar sensibilidad numérica.

## P6. ¿Cómo cambian H y F al variar lambda?
**[CLÁSICO, DERIVADO]** De
\((I+\lambda Q)H=I\) y regla del producto:
\(QH+(I+\lambda Q)H'=0\), luego
\[
H'=-HQH,\quad
H''=2HQHQH,\quad
H^{(n)}=(-1)^nn!H(QH)^n.
\]
A una ventana x corresponde \(p(\lambda)=GH_\lambda x\):
\[
p'=-GHQHx,\qquad p''=2GHQHQHx.
\]
Con \(r=z-p\), para cada pérdida de MSE:
\[
\ell'(\lambda)=-\tfrac2h r^\top p',
\quad
\ell''(\lambda)=\tfrac2h
\big(\|p'\|^2-r^\top p''\big).
\]
Cuando los pesos de F son **constantes respecto de S**,
\(F'=\sum\widetilde w_q\ell_q'\),
\(F''=\sum\widetilde w_q\ell_q''\). No derivar
los pesos si el método m los fijó de antemano.

Por regla de la cadena en el interior:
\[
F_S=\frac{F_\lambda}{S_\lambda},\qquad
F_{SS}=\frac{F_{\lambda\lambda}S_\lambda-
F_\lambda S_{\lambda\lambda}}{(S_\lambda)^3}.
\]
Esto NO demuestra multimodalidad o una raíz en particular,
pero permite investigar F sin diferencias finitas ruidosas.

## P7. ¿Qué puede probarse sobre promediar F?
**[DERIVADO]** Si todas las curvas \(\ell_q\) son
continuas, el promedio ponderado también. Si
\(\ell_q(S)=a_q(S)\) es diferenciable,
\(\frac{d}{dS}\sum_q w_q\ell_q(S)=\sum_qw_q\ell_q'(S)\)
para pesos constantes normalizados.

**Ojo:** en general
\[
\arg\min_S\sum_qw_q\ell_q(S)
\neq\sum_qw_q\arg\min_S\ell_q(S).
\]
Contraejemplo: \(\ell_1=(S-0)^2\),
\(\ell_2=100(S-1)^2\), con pesos 1/2;
el promedio de argmin es 1/2 y el argmin de
su suma es \(100/101\). Este ejemplo no es
una pérdida PLS concreta: ilustra una propiedad
general de la operación; construir contraejemplo
**dentro de la familia PLS** si se necesita
una afirmación más fuerte.

## P8. ¿Pronóstico vs reconstrucción tienen óptimos distintos?
**[HIPÓTESIS / POSIBLE CONTRAEJEMPLO]**
La recuperación optimiza
\(\sum\|\hat\tau(S)-\tau\|^2\);
el forecast optimiza
\(\sum\|G\hat\tau(S)-z\|^2\).
Ambos criterios usan matrices, objetivos y datos
de comparación diferentes. Nada de P1–P7
implica que compartan argmin.
Se requieren DGP controlados o construcción exacta
que ilustre divergencia; si se plantea un teorema
probabilístico de divergencia bajo ruido, especificar
el modelo, h y condiciones suficientes.
No se ha demostrado ventaja uniforme del segundo
fuera de muestra.

## P9. Propiedades estadísticas aún pendientes
**[PENDIENTE]** Consistencia de
\(\widehat S_T\) con dependencias temporales y
horizonte fijo; uniformidad de convergencia de F
en S; existencia de un óptimo de riesgo poblacional
y cuándo es identificable; regularidad bajo
ponderación reciente que da peso persistente a
pocas observaciones; estabilidad a d/L/h y cambios
de régimen. No fingir demostraciones generales
sin hipótesis de mezcla/ergodicidad/estacionariedad.

## Fuentes y precedencia

- Guerrero: suavización PLS, interpretación de S/EDF.
- Cortés-Toto, Guerrero y Reyes (2017):
  CV/GCV/AICc/BIC, índice clásico, factorial 2^4;
  **no adjudicarle forecasting h-step que no reportó**.
- Forecast cross-validation preexistente en otras clases
  de modelos/series: verificar precedentes cercanos de
  suavizado dependiente de h antes de reclamar prioridad.
- Los teoremas elementales de álgebra/optimización se
  atribuyen a matemáticas clásicas y se incluyen para
  hacer la exposición autocontenida.

**Control:** una demostración reproducida en este
documento no es automáticamente la contribución
original del artículo. El valor candidato está en
la formulación, teoría adicional y pruebas empíricas
bien delimitadas.
