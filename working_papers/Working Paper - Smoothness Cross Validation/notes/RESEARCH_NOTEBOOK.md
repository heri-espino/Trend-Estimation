# Paper 1 · Cuaderno científico: suavidad óptima para pronosticar a horizonte h

**Notas de investigación (2026-10-09), NO manuscrito terminado.**
Documento narrativo para que el futuro paper sea comprensible por sí
solo. Leer con [demostraciones](PROOF_LEDGER.md),
[atlas de simulación y figuras](SIMULATION_ATLAS.md),
[base matemática histórica](mathematical_foundations.md) y
[protocolo transversal](../../WEIGHTED_SURFACE_PROTOCOL.md).

## 0. Resumen intelectual en una pregunta

**Pregunta:** si estimamos una tendencia por penalización de
diferencias finitas, ¿cómo escoger su nivel de suavidad para
**pronosticar los siguientes h puntos**, en vez de escogerlo
únicamente para reproducir adecuadamente observaciones pasadas?

**Nuestra propuesta por investigar:** considerar cada suavidad
\(S\in[0,1]\) como un **procedimiento completo de pronóstico**:
ajustar PLS con una ventana L, extrapolar h periodos mediante una
regla de continuación fijada por d, medir los errores de pronósticos
históricos ya realizados, **agregar las funciones de pérdida**
con un método temporal prespecificado y minimizar esa agregación.
El peso temporal \(m\) podría ayudar ante cambios recientes,
pero podría empeorar el riesgo en series estables.

**No es:** una familia nueva de suavizadores, una invención de la
descomposición espectral ni una manera universalmente óptima
de predecir. Se investiga una *integración dirigida a horizonte*,
su caracterización y su evidencia fuera de muestra.

## 1. Alcance: ¿qué estudiamos y qué dejamos fuera?

Se observa una serie de niveles igualmente espaciados
\(y_1,\dots,y_T\), con \(T\) como origen operacional. En simulación,
\(y_t=\tau_t+\xi_t+\epsilon_t\), con tendencia \(\tau_t\),
estacionalidad opcional \(\xi_t\) y ruido \(\epsilon_t\).
En aplicaciones reales no conocemos \(\tau_t\).

El estimador es **PLS puro**, con pesos de observación \(V=I\)
y centro de penalización \(\mu=0\). No modelamos estacionalidad
explícitamente, no optimizamos una matriz general \(V\), no
reconstruimos retrospectivamente un trend usando el test,
no afirmamos causalidad ni pronosticamos volatilidad condicional.

Parámetros de diseño declarados: **orden \(d\), ancho \(L>d\),
horizonte \(h\), orígenes históricos y su separación, familia de
pesos temporales \(m\)**. Comparamos selectores de S fijando
estos factores. La elección entre valores de d/m/L exige
otro conjunto de validación estrictamente histórico o una
confirmación posterior distinta.

## 2. De Guerrero a nuestro caso puro: ¿qué regulariza PLS?

En una ventana \(x_t=y_{t-L+1:t}\), resolvemos
\[
\widehat\tau_\lambda=
\arg\min_{v\in\mathbb R^L}
\{\|x_t-v\|_2^2+\lambda\|D_dv\|_2^2\}.
\]
La condición de primer orden da
\((I+\lambda D_d^\top D_d)v=x_t\) y
\[
Q_d=D_d^\top D_d,\qquad H_\lambda=(I+\lambda Q_d)^{-1},
\qquad\widehat\tau_\lambda=H_\lambda x_t.
\]
Esta construcción es clásica. \(D_d\) anula secuencias con
polinomio discreto de grado menor a d. Por ello
\(\dim\ker Q_d=d\), con \(L-d\) direcciones penalizadas.

Como \(Q_d=U\operatorname{diag}(\delta_j)U^\top\), los filtros
son \(\alpha_j(\lambda)=1/(1+\lambda\delta_j)\).
La matriz \(H\) NO es el índice escalar S.

## 3. De \(\lambda\) a \(S\): ¿por qué normalizar?

Los grados efectivos de libertad son
\(\mathrm{edf}=\operatorname{tr}H_\lambda\).
En la formulación precedente de Guerrero se presenta el
índice \(S_G=1-\mathrm{edf}/L\). Para comparar el rango
completo de la misma familia a L y d fijados, usamos
\[
\boxed{S=\frac{L-\operatorname{tr}H_\lambda}{L-d}
=\frac{L}{L-d}S_G,\quad 0\le S\le1.}
\]
\(S=0\Leftrightarrow\lambda=0\): ajuste que interpola x.
\(S=1\Leftrightarrow\lambda\to+\infty\): proyección
ortogonal exacta sobre \(\ker D_d\), con edf=d.
En d=2 se obtiene tendencia lineal por mínimos cuadrados.
No se trunca la escala lambda en algún techo arbitrario.

Esta normalización es una reparametrización monotónica
conveniente, **no evidencia por sí sola de un mejor pronóstico**.

## 4. ¿Qué significa pronosticar con una tendencia?

No basta con aplicar H a los datos observados:
\(G_{d,h}\in\mathbb R^{h\times L}\) continúa los últimos
niveles de la tendencia estimada imponiendo diferencias futuras
de orden d iguales a cero:
\[
\boxed{\widehat y_{t+1:t+h\mid t}(S)
=G_{d,h}H_{d,L}(S)y_{t-L+1:t}.}
\]
- d=1: nivel constante.
- d=2: extrapolación lineal.
- d=3: cuadrática.
- d=4: cúbica.

**Ejemplo conceptual:** aunque la verdadera tendencia sea
cuadrática, con d=2 el suavizador puede recuperar curvatura
dentro de la ventana para S menor a 1, pero el pronóstico
es una continuación lineal de su frontera. No afirmar que
«S correcto» compensa siempre un d incorrecto.

## 5. ¿De dónde sale una función de pérdida F(S)?

En un origen histórico \(t\) cuyo bloque futuro ya
fue observado al llegar a T, \(t+h\le T\):
\[
\ell_t^{(d,L,h)}(S)=\frac1h
\|y_{t+1:t+h}-G_{d,h}H_{d,L}(S)y_{t-L+1:t}\|_2^2.
\]
Para cada S, esta es la pérdida de **pronóstico** de ese
origen, no el RSS in-sample. Guardamos toda la curva
\(\ell_t(S)\), no solamente su minimizador.

Elegimos de antemano el método temporal m:
- todos los orígenes con igual peso (criterio pooled clásico
  que venimos estudiando);
- últimos K con igual peso;
- últimos K con pesos lineales crecientes;
- últimos K con pesos exponenciales \(w\propto\rho^a\).

La función agregada al actualizar el origen histórico r es
\[
F_r^{(m,d,L,h)}(S)
=\frac{\sum_{q\in I_m(r)}w_{r,q}^{(m)}\ell_{t_q}(S)}
{\sum_{q\in I_m(r)}w_{r,q}^{(m)}},\quad q\le r,
\]
donde ningún bloque aún no realizado puede intervenir.
La decisión operativa del **Paper 1** es
\[
\boxed{\widehat S_T^{(m,d,L,h)}
\in\arg\min_{S\in[0,1]}F_M^{(m,d,L,h)}(S).}
\]
La media de minimizadores individuales, el último mínimo
histórico y el tracking son otras reglas: **NO son este paper**.

## 6. ¿Por qué podría tener sentido?

Las suavidades bajas preservan variaciones de alta frecuencia
que pueden ser ruido; las altas las suprimen, pero podrían
reaccionar demasiado lentamente a una pendiente que acaba de
cambiar. Un pronóstico a h=1 puede favorecer S diferente de
h=12 porque G amplifica de manera distinta errores en niveles,
pendientes y curvaturas. La ventana temporal m determina
cuánto pesa un episodio de régimen antiguo al seleccionar S.

Esto es una **motivación**, no un teorema de ganancia:
- Si la tendencia es realmente lineal y el ruido iid, una
  suavidad alta podría ser favorable.
- Si la pendiente cambia cerca del final, los orígenes antiguos
  pueden no representar el mecanismo futuro.
- Si m privilegia pocos folds, la estimación de F es más ruidosa.
- Si d es demasiado grande para h largo, extrapolar la
  curvatura estimada puede amplificar ruido.
Estos ejemplos fundamentan los DGP y las figuras previstas;
se contrastarán empíricamente sin seleccionar casos favorables.

## 7. Algoritmo desde datos disponibles hasta pronóstico

**Entrada:** \(y_{1:T},d,L,h\), regla de orígenes,
método m y parámetro K/decay elegidos **sin usar test exterior**.

1. Construir Q, diagonalizar una vez por pareja (L,d),
   construir espectro y \(G_{d,h}\).
2. Enumerar orígenes \(t_1<\cdots<t_M\) tales que
   \(t_q+h\le T\). Cada fold tiene la misma longitud L.
3. Para candidatos S (incluyendo exactamente 0 y 1),
   calcular pronósticos y toda \(\ell_{t_q}(S)\).
4. Agregar según m la **función** F_M(S).
5. Localizar su global argmin. La grilla con
   refinamiento no es garantía universal de recuperar todos
   los valles: separar precisión numérica del estimador ideal.
6. Con \(\widehat S_T\), **reajustar** \(\widehat\tau_T
   =H(\widehat S_T)y_{T-L+1:T}\), pronosticar \(G\widehat\tau_T\).
7. Evaluar contra \(y_{T+1:T+h}\) únicamente después de
   tomar la decisión. Repetir en varios orígenes exteriores.
8. Registrar S, EDF, MSFE observado y error frente a
   \(\tau\) simulado (solo diagnósticos), escenarios y semilla.

La extrapolación y los folds usados al final deben tener
h declarado igual al h del problema real. Un competidor h=1
que luego pronostica h>1 merece una ablación separada.

## 8. Qué compararemos para sustentar la idea

**Criterios clásicos** CV leave-one-out, GCV, AICc, BIC
seleccionan S reconstruyendo/ajustando datos; cada candidato
se evalúa después con el **mismo pronóstico y test h**.
Incluir S ad hoc fijos (0,.5,.8,.95,1) y oráculos **marcados como
imposibles para predicción real**.

Tres métricas distintas:
\[
\begin{aligned}
E_{\mathrm{obs}}&=h^{-1}\sum_{k=1}^h
(\widehat y_{T+k|T}-y_{T+k})^2,\\
E_{\mathrm{recover}}&=L^{-1}\sum_{i=T-L+1}^T
(\widehat\tau_{i|T}-\tau_i)^2,\\
E_{\mathrm{latent},h}&=h^{-1}\sum_{k=1}^h
(\widehat y_{T+k|T}-\tau_{T+k})^2.
\end{aligned}
\]
La tendencia \(\tau\) no se revela al selector. En escenarios
con estacionalidad, reportar también error frente a
\(\tau+\xi\): nuestro G extrapola tendencia, no componentes
estacionales separados.

## 9. Experimentos y visuales que deben figurar

Consultar [SIMULATION_ATLAS.md](SIMULATION_ATLAS.md):
Cortés-Toto original 2^4 (fuente recuperada: tendencia lineal y
mezcla beta, estacionalidad, sigma y N); extrapolación de
tendencias lineales/cuadráticas/cúbicas y polinomios mal
especificados; senos, curvas y cambios de pendiente; ruidos
iid, AR(1), t, heterocedástico.

**Figura indispensable:** para la MISMA \(\tau\), tres o más
realizaciones/niveles de ruido en columnas; mostrar
\(\tau\), \(y\), \(\widehat\tau\), límite T y
\(\widehat y_{T+1:T+h}\) frente al futuro realizado; reportar
qué método seleccionó S y el error de ese caso sin presentarlo
como conclusión poblacional. Complementar con resultados por
celdas y bandas de incertidumbre por semilla.

## 10. Límites y preguntas que no debemos ocultar

- ¿Existe una ventaja fuera de muestra de m reciente cuando
  el DGP es estacionario? Podría ser negativa.
- ¿Cuánta ganancia aparente se explica solo por un S fijo bien
  elegido o por el mayor costo de buscar varios m?
- ¿Difieren S óptimo de recuperación y S útil para pronóstico?
  No asignar «S verdadero» sin especificar riesgo/oráculo.
- ¿Qué pasa si F es multimodal y un minimizador numérico
  devuelve un mínimo local peor?
- ¿Qué parte del resultado depende de d, L, h, pesos m o ruido?
- ¿Se mantiene el resultado en datos observacionales donde
  no conocemos la tendencia latente?

## 11. Del cuaderno al manuscrito: estructura tentativa

1. Introducción: pronosticar la tendencia vs reconstruirla;
   literatura cercana y promesa empírica **condicional**.
2. PLS, extensión a h, coordenada S y propiedades necesarias
   (teoremas clásicos citados; derivaciones propias transparentes).
3. Criterio weighted pooled rolling-origin y protocolo causal.
4. Caracterización matemática / sensibilidad, solo lo probado.
5. Monte Carlo y referencia Cortés-Toto, DGP explícitos y figuras
   señal vs tendencia estimada a distintos ruidos.
6. Resultados pareados en MSFE, tendencia latente, S y EDF;
   efectos de h, d, forma, m y ruido; controles negativos.
7. Aplicaciones y limitaciones.
8. Apéndice de derivadas y pruebas numéricas; GPU solo si
   rendimiento y equivalencia se verifican.

La estructura exacta se adaptará al journal seleccionado,
sin atribuirle requisitos aún no consultados.

**Estado:** metodología y campaña extensiva implementadas como
propuestas; 528 celdas prospectivas NO equivalen a resultados
ejecutados y verificados. Los checkpoints antiguos permanecen
históricos. No redactar un abstract de hallazgos antes de
tener resultados externos auditables.
