# Resultados de la auditoría de la campaña CUDA histórica

**Fecha:** 12 de octubre de 2026. **Estado:** análisis retrospectivo exploratorio de datos ya generados; **0 simulaciones nuevas**. Esta nota NO establece originalidad ni valida los modelos para series financieras reales.

## 1. Procedencia y alcance

La campaña `formal8h` original, correspondiente a los tres artículos iniciales con **media de diferencias \(\mu=0\)**, terminó con **100,848** de **144,000** réplicas de escenario/semilla, **144/144** celdas cubiertas y **696–704** semillas independientes por celda. Se archivaron **65,877,504** evaluaciones de método y **50,424** diagnósticos numéricos. No se detectaron fallos registrados. Código experimental original: commit `21bd563146e04eb545cae56b46393d93a9d98212`.

Fuentes de los resultados auditados:
- [Manifiesto](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit/AUDIT_MANIFEST.json).
- [Auditoría de Paper 1](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit/PAPER1_AUDIT.md).
- [Auditoría de Paper 2](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit/PAPER2_AUDIT.md).
- [Auditoría de Paper 3](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit/PAPER3_AUDIT.md).
- [Diagnósticos de suavidad y EDF](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit/smoothing_edf_diagnostics.csv).
- [Estratificación por DGP y ruido](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit/group_heterogeneity.csv).
- [Casos extremos, incluyendo fallos](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit/extreme_cases.csv).
- [Contrastes pareados corregidos por Holm](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit/comparison_tests.csv).
- [Diferencias numéricas pareadas](../results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit/numerical_paired_summary.csv).

Se promedian los orígenes externos dentro de cada semilla; la inferencia se basa en diferencias pareadas **entre semillas independientes de la misma celda**, no sobre pseudo-réplicas de orígenes superpuestos. Los porcentajes de escenarios y las medianas de cocientes de RMSE son **descriptivos entre DGP heterogéneos**, no intervalos de confianza para una población de DGP nuevos. Los tests \(t\) y el ajuste Holm por familias de Paper 1 (10,080 contrastes) y Paper 2 (5,600) siguen siendo retrospectivos, no confirmación independiente.

**Direcciones de las pruebas:** Paper 1 define `method=classical/fixed`, `comparator=pooled_uniform_all`; por tanto, 442 contrastes Holm significativamente favorables al primero y 7,791 al segundo. Paper 2 define `method=tracked`, `comparator=pooled` de la MISMA ponderación; 1,800 contrastes Holm significativamente favorables a tracking y 72 a pooled. Ninguno de estos cuatro recuentos debe traducirse a “número de semillas ganadoras”.

## 2. Paper 1: éxito contra criterios in-sample, pero S=1 limita la afirmación

Para el experimento `d=3,h=12`, la mediana por escenario de `classical_cv/pooled_uniform_all` es **4.6676**, de `classical_aicc/pooled_uniform_all` es **1.8098**, y de `classical_bic/pooled_uniform_all` es **83.9803**. El mensaje de valor es que el objetivo de ajuste histórico y el pronóstico de largo horizonte son objetivos diferentes. No obstante, hay **dos matices esenciales**:

### 2.1 BIC es un control prácticamente degenerado en este diseño

El [código histórico](../experiments/smoothness_cv/simulation_evaluation.py) usa
\[
\operatorname{BIC}(S)=\log(\operatorname{RSS}(S)/L)+\operatorname{EDF}(S)\frac{\log L}{L}.
\]
El reporte de auditoría muestra **mediana de \(S_\mathrm{BIC}=0.00625\) en todas las combinaciones \((d,h)\)**, y la fracción de celdas con promedio de \(S<0.01\) es 100%. Corresponde al **primer punto positivo** de una cuadrícula uniforme de 161 puntos. EDF mediano \(\approx71.56\) en ventanas largas, casi interpolación (para comparadores forecast-CV \(S\) es generalmente \(\approx0.96\)–\(0.997\)).

**Explicación matemática:** para \(\lambda\to0^+\), \(H_\lambda=(I+\lambda Q)^{-1}=I-\lambda Q+O(\lambda^2)\). De aquí,
\[
x-H_\lambda x=\lambda Qx+O(\lambda^2),
\qquad
\operatorname{RSS}(\lambda)=\lambda^2\|Qx\|^2+O(\lambda^3).
\]
Con \(\|Qx\|>0\), \(\log(\operatorname{RSS}(\lambda)/L)\to-\infty\), mientras EDF tiende a \(L\) y su penalización queda acotada. **El criterio no tiene mínimo interior bien regularizado en este espacio de suavizadores cuando la varianza del ruido se estima sin restricciones por RSS.** El código excluye la interpolación exacta cuando RSS es numéricamente cero, por lo que selecciona el punto inmediatamente siguiente. Es un **efecto del dominio/criterio de comparación**, no prueba de que un BIC apropiadamente definido para otra clase de modelos pronostique 84 veces peor.

**Acción editorial:** NO sustentar la contribución principal en la derrota de BIC. Presentar BIC como caso patológico de la definición aquí evaluada, en un apartado de robustez/limitaciones y con explicación del borde \(\lambda=0\).

### 2.2 Suavidad máxima fija \(S=1\) a menudo supera forecast-CV

Para `d=3,h=12`, la razón mediana `fixed_1/pooled_uniform_all` es **0.9912**, con **82.4% de las 136 celdas** favoreciendo a \(S=1\). En ese mismo contraste **54.4%** de las celdas muestran una ventaja de \(S=1\) favorable y Holm-significativa. Para `d=3,h=1` la razón mediana es **0.9930**, con **61.8%** de celdas favorables a \(S=1\). Por tanto, aunque forecast-CV supera muchos criterios clásicos de reconstrucción, **no supera uniformemente el control más simple de máxima suavidad**.

Como \(S=1\) proyecta sobre el núcleo polinómico de diferencias de orden \(d\), conviene explicar por qué extrapolación en ciertos DGP favorece esta restricción. Sin esta comparación sería engañoso afirmar superioridad predictiva universal.

## 3. Paper 2: seguimiento favorable bajo ciertas condiciones, sin identificación del mecanismo

En las 144 celdas disponibles de `d=3,h=1`, la mediana `tracked_recent_exp_8/pooled_recent_exp_8` es **0.9353**; **92.4%** de las celdas presentan un valor inferior a uno, y **49.3%** una mejora Holm-significativa. En `d=3,h=3` el cociente es **0.9654**, con 95.1% de celdas favorables a tracking y 54.2% Holm-significativas. A `d=3,h=12` el efecto se reduce a mediana **0.9893**.

### 3.1 Fallos por dependencia temporal

Al estratificar `d=3,h=1` por ruido, se observa:

| Ruido | Celdas | Mediana ratio tracking/pooled | Fracción de celdas favorable a tracking |
|---|---:|---:|---:|
| iid | 104 | **0.9362** | 99.0% |
| contaminado | 24 | **0.8679** | 100% |
| AR(1) | 16 | **1.0065** | 37.5% |

En `d=2,h=1`, AR(1) muestra mediana **1.0369**, con **0%** de las 16 celdas favoreciendo tracking. No es correcto afirmar mejoría general bajo dependencia serial. Tampoco basta mirar medianas: el máximo extremo auditado de `d=3,h=12` `tracked_recent_exp_8/pooled_recent_exp_8` alcanza **2.6016** en `D__double_jump__N300__contaminated__sd0.8__seasonal0`. Esa celda extrema tiene \(p_\mathrm{Holm}=1\), por lo que no debe publicitarse como una derrota significativa; sí muestra vulnerabilidad descriptiva a ciertas condiciones de ruptura.

El efecto varía por DGP/ruido/horizonte. Evitar comparaciones casuales de promedios globales sin estratificación.

### 3.2 Persistencia de ramas versus suavizado de S

En `weighted_surface_study.py`, la regla de tracking **identifica ramas persistentes** de mínimos locales *y también promedia los últimos \(K\) valores de \(S\) de la rama elegida*. Ninguna de las 100,848 réplicas incluye un contrafactual de `moving_average(global_minimum_S)`. Los contrastes tracking/pooled **no aíslan** si la ganancia viene de la identificación de ramas o solo de regularizar temporalmente \(S\). Este es el **principal hueco de identificación de la contribución original**, y no debe ocultarse. Bajo la instrucción del usuario de NO generar más simulaciones, queda marcado como limitación no resuelta.

## 4. Paper 3: mejor optimización no implica mejor pronóstico externo

Los **50,424** casos numéricos guardados cubren `h=3` solamente, en 120 grupos de estudio/forma/orden/ponderación. **69.75%** de los casos tienen `adaptive F` por debajo del mínimo de la cuadrícula densa: ésta es una referencia **discreta**, no el mínimo matemático global; tener regret negativo no es una contradicción.

Sin embargo, la búsqueda adaptativa tiene **MSFE observado exterior menor que el grid original solamente en 35.51% de los casos**, por lo que mayor precisión al optimizar el objetivo histórico \(F\) **no garantiza** mayor precisión predictiva exterior. Son preguntas empíricas distintas y no deben confundirse.

Una comparación adicional de `numerical_paired_summary.csv` muestra que las **medias por grupo** de `adaptive - grid` en MSFE exterior son negativas en 76 de 120 grupos (63.3%). Esto **no contradice** 35.5% de victorias caso a caso: media del contraste y frecuencia de ganar responden preguntas distintas, sobre todo con distribuciones asimétricas y heterogéneas. Ninguna de estas cifras por sí sola certifica que la búsqueda adaptativa sea superior a nivel predictivo.

Medianamente, entre las medias por grupo, Brent requirió \(\approx0.00112\) segundos y búsqueda adaptativa \(\approx0.01084\) segundos, frente a \(0.04867\) segundos de referencia densa. No confundir estas medianas con un benchmark aislado de latencia controlada por hardware/entorno.

## 5. Estado y recomendación editorial, sin experimentos adicionales

1. **P1:** corregir narrativa: aportación potencial es alineación temporal del criterio al pronóstico, no una superioridad universal a criterios clásicos o a \(S=1\). BIC en esta implementación es degenerado por límite interpolante.
2. **P2:** es la evidencia más prometedora para el efecto de tracking frente a pooled con pesos iguales. Pero el control de promedio de mínimos globales falta; destacar la pérdida bajo AR(1) a \(h=1\), la sensibilidad al horizonte y los saltos.
3. **P3:** presentar evidencia numérica como procedimiento de búsqueda y precisión de \(F\); no como mejora universal de MSFE ni certificación de mínimo global. Puede integrarse como apéndice metodológico hasta contar con resultados teóricos más específicos.
4. **Todos:** las pruebas Holm son **post hoc exploratorias**. La interrupción antes de las 144,000 réplicas y múltiples variantes evaluadas en un mismo panel impiden reclamos confirmatorios. Los datos existentes bastan para estas conclusiones descriptivas; **no se recomiendan más réplicas del mismo diseño**.

**Esta nota es una interpretación de los archivos de auditoría publicados**, no un experimento nuevo, no una reevaluación de forecasts y no un resultado de la investigación nueva sobre \(\mu\ne0\).
