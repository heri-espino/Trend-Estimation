# De las notas matemáticas al artículo final — protocolo editorial de los tres papers

**2026-10-09 · Guía de escritura de investigación, no manuscrito sometible.**
Este documento establece el proceso de maduración de notas Markdown
hacia los futuros \`main.tex\`; no da por probados los resultados ni por
ejecutados los experimentos nuevos.

## Por qué primero Markdown

La contribución debe poder expresarse con precisión y ser criticada
**antes** de elegir la clase LaTeX o imitar el formato de una revista.
Las notas no son el paper largo: constituyen una memoria de trabajo
de la que **seleccionaremos** teoremas, mecanismos, experimentos y
figuras que realmente sostengan una pregunta publicable.
El futuro artículo no es un volcado automático de todo el repositorio.

Cada paper tiene un centro distinto:

| Trabajo | Objeto de estudio | Contribución por investigar | No debe convertirse en |
| --- | --- | --- | --- |
| 1. Pooled Forecast-CV | Global \(\arg\min\) de \(F_M^{(m,d,L,h)}(S)\) | Selección de suavidad alineada con horizonte h, estabilidad y criterio ponderado | Tracking de mínimos individuales |
| 2. Dynamic Branch | Historia temporal de mínimos locales de **esas mismas** F | Persistencia/continuación, asociación y utilidad predictiva de una rama | El antiguo algoritmo Val1/Val2 |
| 3. Numerical Methods | Una F(S) fija y sus puntos estacionarios/extremos | Estructura algebraica y detección/aislamiento fiable de mínimos | Selección de ramas entre orígenes |

## Arquitectura de notas (cada working paper)

- \`notes/RESEARCH_NOTEBOOK.md\` — hilo narrativo comprensible:
  delimitación, pregunta y motivación, pasos, formalización, predicciones
  interpretativas, papel de simulaciones y esquema del artículo.
- \`notes/PROOF_LEDGER.md\` — afirmación por afirmación: hipótesis,
  demostración completa o referencia, ejemplo límite/contraejemplo,
  nivel de certeza y tareas de teoría pendientes.
- \`notes/SIMULATION_ATLAS.md\` — hipótesis examinadas por cada
  diseño generador, qué se simula, qué conoce el investigador, cómo
  se pronostica, curvas/figuras de comparación a múltiples niveles de
  ruido, controles y estructura de tablas; **no inventar resultados**.
- \`notes/README.md\` o \`INDEX.md\` — puerta de entrada que vincula
  estas tres notas con registros históricos, código y PDFs.
- \`AI_HANDOFF.md\` en cada working paper — estado ejecutivo para agentes.

El alcance de las notas no sustituye los anteriores
\`mathematical_foundations.md\`, \`results.md\`,
\`sturm_minicheck.md\`, etc. Conservan su trazabilidad y detalles.

## Estatus obligatorio de cada afirmación

**[CLÁSICO]** Resultado matemático publicado/estándar; atribuir.
**[DERIVADO]** Identidad demostrada aquí a partir de hipótesis explícitas,
no necesariamente original.
**[HIPÓTESIS]** Afirmación estadística que necesita prueba/simulación.
**[PENDIENTE]** No hay aún demostración suficiente o cálculo terminado.
**[HISTÓRICO]** Evidencia generada para un diseño anterior; no reutilizar
para el método nuevo sin repetir la evaluación.
**[IMPLEMENTADO, SIN RESULTADOS]** Código y diseño disponibles, ejecución
extensa no observada/verificada.
**[MEDIDO, POR VERIFICAR]** Mediciones provistas por el usuario sin
evidencia independiente o sin auditoría completa.

Nunca escribir «demostramos que ...» para una simulación o una
conjetura. Nunca escribir «el experimento confirma ...» antes
de producir un resultado con procedencia comprobable.

## Orden de escritura del futuro artículo

1. **Pregunta central y prioridad bibliográfica:** que un lector pueda
   reconocer qué problema se resuelve y qué ya habían hecho Guerrero,
   Cortés-Toto y la literatura forecast-CV / optimización.
2. **Modelo y supuestos:** qué observamos \(y\), qué es latente \(\tau\),
   qué significa \(S\), cuál es h, por qué se mantiene \(V=I,\mu=0\),
   qué mecanismo de extrapolación se usa.
3. **Definición reproducible del método:** selección dentro de historia
   completada, refit, pronóstico h pasos, outer test.
4. **Resultados matemáticos:** hipótesis → proposición → demostración
   → interpretación; citar lo clásico; evitar resultados triviales como
   la contribución principal.
5. **Diseño de simulación verificable:** ecuaciones generadoras,
   grilla factorial, semillas, T/L/d/h, pérdidas, métodos de selección,
   referencias/controles, S-oráculos solo diagnósticos, protocolo de
   errores pareados y decisiones de graficación predefinidas.
6. **Resultados**, solo tras ejecutar: tablas de MSFE/RMSE, bandas
   de incertidumbre por series independientes, efectos y casos en
   los que se pierde. Figuras interpretativas de señales y tendencias.
7. **Discusión / limitaciones:** lo que la evidencia permite o no
   concluir; dependencia temporal, cambios de régimen, sesgo por
   estudiar muchos escenarios, sensibilidad numérica y extensión futura.
8. **Apéndices:** demostraciones largas, descripciones exhaustivas de
   DGP, detalles computacionales y auditoría reproducible.

Ajustar número y ubicación de teoremas/figuras a la **guía real del
journal cuando se elija**, sin adoptar de antemano una estructura
especulativa sobre requisitos editoriales. Cada paper tendrá
métodos/resultados suficientes para sostenerse solo; referencias
cruzadas entre papers pueden aparecer como literatura en desarrollo,
pero no deben reemplazar definiciones esenciales.

## Principio de figuras (indispensable para esta investigación)

Siempre que interpretemos un método en datos **simulados** y
conozcamos \(\tau\), mostrar, con ejes y máscaras temporales idénticos:

- **Tendencia verdadera \(\tau\)** y **observaciones \(y\)**, a varios
  niveles de ruido para la **misma forma subyacente**.
- **Tendencias estimadas \(\widehat\tau\)** por criterios competidores,
  diferenciando la recuperación dentro de entrenamiento de la
  extrapolación \(\widehat y_{T+1:T+h|T}\).
- Una separación visual entre tramo **disponible** y bloque de
  **test exterior oculto durante selección**.
- Curvas \(F(S)\), mínimos globales (Paper 1), **ramas** (Paper 2),
  raíces/curvaturas y extremos (Paper 3) cuando corresponda.
- Análisis por celdas factoriales y por tipo de ruido, no solo
  ejemplos visuales elegidos a posteriori.

Si \(\xi\neq0\), diferenciar explícitamente línea \(\tau\),
señal condicional \(\tau+\xi\), observaciones \(y=\tau+\xi+\epsilon\),
y predicción que en el modelo actual **no** extrapola una
estacionalidad separada. Si el ruido depende del tiempo, indicar
que \(V=I\) sigue siendo la **función objetivo del estimador**,
no un supuesto verdadero del DGP.

## Capa experimental común y límites

[SIMULATION_EVALUATION_PROTOCOL.md](SIMULATION_EVALUATION_PROTOCOL.md)
describe 16 celdas inspiradas en Cortés-Toto + 384 formas/ruidos +
128 regímenes = 528 celdas del preset extensivo.
[CAMPAIGN_README.md](../experiments/smoothness_cv/CAMPAIGN_README.md)
describe los scripts, la base SQLite, la reanudación y los reportes.
52,800 combinaciones escenario–semilla a 100 semillas **no son**
52,800 observaciones globalmente independientes para inferencia:
medir incertidumbre a nivel semilla DENTRO de cada DGP.

**Distinguir:**
- Reproducción metodológica de Cortés-Toto: CV/GCV/AICc/BIC sobre
  N=50/200 **completos**, índice Guerrero original, \(d=2\);
- Nuestra nueva comparación de pronósticos: historia de longitud L,
  horizonte h, pérdidas completadas, outer test;
- Oráculos: «recuperación óptima» o «tendencia futura óptima» usan
  \(\tau\) simulada y son **inadmisibles para selección desplegable**;
- Un «mejor S retrospectivo frente al y del test» es un hindsight
  oracle optimista, NO un resultado válido de predicción.
- Las simulaciones basadas en grilla S son aproximaciones: no llamar
  óptimo matemático global certificado a un mínimo grid.

## Ruta de promoción: notas → resultados → LaTeX

Antes de tocar el manuscrito final de un paper deben cumplirse:
1. Pregunta principal, contribución y delimitación clara y verificadas
   contra literatura cercana.
2. Hipótesis matemáticas, demostraciones y contraejemplos
   completados o etiquetados como cuestiones abiertas.
3. Pruebas del estimador, cronología y no fuga en el código.
4. DGP, métricas, figuras y comparadores predeclarados.
5. Piloto y diseño confirmatorio con semillas/outer test no usados
   para elegir métodos, con manifest y resultados auditables.
6. Tablas/gráficas que expliquen tanto ganancias como fallos.
7. Evidencia de originalidad suficiente para una revista concreta.

Los tres papers pueden avanzar en distintos momentos; no bloquear
la teoría de uno por un benchmark de hardware de otro. El benchmark
CUDA float32 es **ingeniería complementaria**, no teorema central.
