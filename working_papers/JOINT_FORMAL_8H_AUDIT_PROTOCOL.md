# Auditoría estadística de la campaña congelada — 12 de octubre de 2026

**Estado: implementación de auditoría disponible; su ejecución y sus conclusiones numéricas están pendientes de verificarse en la computadora que conserva la copia SQLite.** Esta etapa **no ejecuta ninguna simulación**, no ajusta modelos y no altera el manifiesto histórico.

## 1. ¿Qué se audita?

La evidencia previa procede de una sola campaña histórica bajo el modelo de diferencias medias **\(\mu=0\)**. Se recuperaron 100,848 réplicas independientes de escenario/semilla (144/144 escenarios, 696–704 réplicas/escenario), frente a 144,000 planeadas, con 65,877,504 filas de resultados de selectores y 50,424 registros de optimización numérica. Revisión inicial: [informe retrospectivo](JOINT_FORMAL_8H_RETROSPECTIVE_2026-10-12.md). **La cuarta línea de investigación de \(\mu\ne0\) NO fue evaluada en esta campaña.**

Documentos/CSV de entrada ya generados:
- \`results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/ANALYSIS_MANIFEST.json\`.
- \`.../coverage_by_scenario.csv\`.
- \`.../paper1_forecast_cv_vs_classical.csv\`.
- \`.../paper2_tracking_vs_matched_pooled.csv\`.
- \`.../paper1_2_method_scenario.csv\` (diagnósticos de suavidad/EDF guardados solo localmente).
- \`.../outcomes.sqlite\`, con los diagnósticos numéricos históricos, solo en modo lectura.

## 2. Objetivo de inferencia: unidades independientes

Sean \(j\) una celda de diseño, \(r\) una semilla independiente, \(o\) un origen de pronóstico externo y \(k=(d,h,m)\) el método/orden/horizonte. Para dos decisiones *comparables* \(A,B\) evaluadas en los **mismos** orígenes,
\[
\Delta_{j,r,k}=
\frac1{|\mathcal O_{j,r,k}|}
\sum_{o\in\mathcal O_{j,r,k}}
\left(
\mathrm{MSFE}_{j,r,o,k}(A)-
\mathrm{MSFE}_{j,r,o,k}(B)
\right).
\]
El estadístico por celda es \(\bar\Delta_{j,k}=R_j^{-1}\sum_{r=1}^{R_j}\Delta_{j,r,k}\). La desviación estándar \(s_{j,k}\) se calcula entre las \(R_j\) réplicas, no entre orígenes de pronóstico superpuestos. El error estándar es
\[
\widehat{\mathrm{SE}}(\bar\Delta_{j,k})=\frac{s_{j,k}}{\sqrt{R_j}}.
\]

Además de la CI nominal normal del reporte original, la auditoría obtiene una \(p\) descriptiva de Student con \(R_j-1\) grados de libertad, bilateral. El ajuste **Holm** se realiza sobre la familia completa de comparaciones predeclaradas **dentro de cada paper**, no sobre un solo subconjunto conveniente seleccionado después. Holm no requiere independencia entre pruebas para controlar el error familiar bajo las hipótesis nulas, pero esta corrección no resuelve el carácter exploratorio del panel externo compartido ni constituye confirmación independiente.

Por separado, el RMSE relativo **en cada celda** es
\[
r_{j,k}=\sqrt{\frac{\overline{\mathrm{MSFE}}_{j,k}(A)}
                        {\overline{\mathrm{MSFE}}_{j,k}(B)}}.
\]
La mediana de \(r_{j,k}\) entre celdas **no equivale** a un RMSE de todas las observaciones juntas, ni su porcentaje de signos favorables es una prueba automática de generalización.

## 3. Protocolos por paper

### P1 — Comparación de forecast-CV con criterios clásicos

Emparejamiento histórico exacto: \`classical_cv/gcv/aicc/bic\` y \`fixed_*\` contra \`pooled_uniform_all\`, al mismo escenario, semilla, origen, \(d\) y \(h\).

Las diferencias mayores se concentran en casos con orden \(d=3\), horizonte \(h=12\). En particular BIC/pooled presentó razón mediana 83.9803 en 136 escenarios. **No etiquetar esto como bug ni como ventaja universal** antes de contrastar el \(S\) promedio, EDF promedio, frecuencias de valores extremos y dependencia por familia de DGP.

Verificación del código original en commit \`21bd563146e04eb545cae56b46393d93a9d98212\`: BIC se minimizó con la función discreta
\[
C_\mathrm{BIC}(S)=\log(\mathrm{RSS}(S)/L)+
\mathrm{edf}(S)\frac{\log L}{L}.
\]
Eso es una penalización basada en ajuste histórico; no se minimiza el error a \(h\) pasos. Con diferencias de orden \(d\), el pronóstico polinómico puede amplificar drásticamente un ajuste local de curvatura. La auditoría estratificará los extremos por forma de tendencia, ruido, \(L\), \(d\), \(h\), \(S\) y EDF. La revisión de las fórmulas y del código en commit original será distinta de los contrastes estadísticos.

### P2 — Seguimiento de ramas

Se exige \`tracked_<ponderación>\` contra \`pooled_<la misma ponderación>\`. La hipótesis relevante es que persistencia de mínimos locales aporta una decisión más robusta que el mínimo global de la **misma** superficie \(F^{(m)}_T(S)\). La implementación actual \`select_tracked_branch\` selecciona una rama y promedia **los últimos \(K\) valores \(S\)** dentro de ella. Por tanto, sin control explícito de **media temporal de óptimos globales**, no puede atribuirse la mejora únicamente a la continuidad de ramas.

La auditoría puede analizar diferencias en \(S\), EDF, número de mínimos y soporte por escenario con los resúmenes existentes. Ninguna de esas asociaciones sustituye a la ablación causal ausente. No se realizarán nuevas simulaciones: este punto quedará marcado como limitación del artículo.

### P3 — Métodos numéricos

Los 50,424 registros corresponden a diagnósticos archivados para **\(h=3\)**. Se reconstruirán diferencias **por cada caso registrado** entre grid, Brent y búsqueda adaptativa, tanto en pérdida \(F\) como en MSFE externa, y diferencias de coste de evaluación y tiempo.

El óptimo de la cuadrícula densa es una **referencia finita, no una cota inferior certificada** de \(\min_{S\in[0,1]}F(S)\). Por tanto, regret negativo de la búsqueda adaptativa respecto a esa referencia es matemáticamente posible. No declarar superioridad numérica global ni extrapolar los resultados a otros horizontes.

## 4. Auditorías de integridad y reporte

Antes de producir inferencias, se verifica:
1. Conteo de réplicas en \`coverage_by_scenario.csv\` frente al manifiesto, sin duplicados, y congruencia grupo A/B/C/D.
2. Si está disponible la copia SQLite congelada, identidad de commit original, total de réplicas y filas guardadas. La conexión es estrictamente **read only**.
3. Los emparejamientos correctos para P1/P2 y duplicados; \(\mathrm{RMSE}_{rel}=\sqrt{\mathrm{MSFE}_A/\mathrm{MSFE}_B}\) con denominadores positivos.
4. Número de unidades independientes para cada SE; contrastes bilaterales y Holm, por separado para P1 y P2.
5. Tablas completas de heterogeneidad \`study\`, \`shape\`, \`noise\`, \`sigma\`, \`seasonal\`. Cinco mejores y cinco peores celdas por par/orden/horizonte, preservando ambos extremos, no solo las victorias.
6. Concordancia de los casos numéricos archivados con los 50,424 registros de procedencia.
7. Salidas Markdown y CSV compactas publicables, conservando los 31 GiB de datos originales fuera de Git común.

## 5. Ejecutar sin simulaciones

~~~powershell
python -m pytest tests/test_analyze_frozen_compact.py tests/test_recover_campaign.py -q
python -m experiments.smoothness_cv.audit_frozen_evidence --report-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact --frozen-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN
python -m experiments.smoothness_cv.publish_frozen_audit --audit-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact/audit --push
~~~

El informe índice será \`.../frozen_compact/audit/AUDIT_OVERVIEW.md\`, con \`PAPER1_AUDIT.md\`, \`PAPER2_AUDIT.md\`, \`PAPER3_AUDIT.md\`, tablas de pruebas/heterogeneidad/extremos, diagnóstico \(S\)/EDF y diferencias numéricas pareadas.

La auditoría **no decide a priori** qué paper publicar ni qué regla declarar ganadora. Primero cuantifica la evidencia, los casos desfavorables y lo que todavía no puede establecerse con los datos archivados.
