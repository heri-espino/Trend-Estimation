# Working Paper — Trend Simulation and Mean-Difference Forecasting

**Nuevo proyecto activo — 2026-10-11.** Antes de redactar el paper, se construye
un registro riguroso en **Markdown/Obsidian** con demostraciones, casos límite,
protocolos de simulación y resultados. El documento \`manuscript/main.tex\`
es un **esqueleto, NO un artículo listo para enviar**.

## Pregunta central

En la suavización de series temporales por mínimos cuadrados penalizados,
¿qué cambia al permitir que las diferencias de orden \(d\) de la tendencia
tengan media \(\mu\neq0\), y escoger \(S\) y \(\mu\) específicamente para
pronosticar a horizonte \(h\) mediante bloques de validación ya realizados?

El trabajo se enfoca en **tendencias verdaderas conocidas por simulación**:
recuperación pasada, pronóstico de la tendencia futura, pronóstico de
observaciones futuras y estabilidad de la media/del índice de suavidad.
No se presume ventaja universal.

## Modelos: tres reglas comparables

1. **Puro:** \(\mu=0\), \(S\) seleccionado por forecast-CV.
2. **Guerrero (2007):** media de diferencias observadas
   \(\widehat\mu_t^G=\mathbf1^\top D_dx_t/(L-d)\) calculada
   **separadamente en cada ventana de entrenamiento**.
3. **Perfilado de forecast-CV:** un \(\widehat\mu_T(S)\) común
   para los orígenes de validación históricos completados.
   Para cada \(S\), minimiza la pérdida ponderada
   h-step analíticamente; después se minimiza solo en \(S\).

Para un \(S\) fijo, \(\widehat z_t(S,\mu)=a_t(S)+\mu b(S)\).
El perfilado de \(\mu\) no constituye por sí solo una técnica
matemática nueva. La pregunta de novedad está en la formulación
estadística exacta para la extrapolación PLS y sus propiedades y
evidencia; requiere auditoría completa de precedentes.

## Índices de notas (leer antes de trabajar)

- [notes/INDEX.md](notes/INDEX.md): secuencia prioritaria del paper.
- [notes/RESEARCH_NOTEBOOK.md](notes/RESEARCH_NOTEBOOK.md): delimitación,
  justificación, algoritmo y preguntas teóricas.
- [notes/PROOF_LEDGER.md](notes/PROOF_LEDGER.md): resultados con hipótesis,
  demostración, límites y estatus de originalidad.
- [notes/SIMULATION_ATLAS.md](notes/SIMULATION_ATLAS.md): DGP,
  tendencias verdaderas, ruido, CV, pronóstico, figuras y métricas.
- [notes/LITERATURE_POSITIONING.md](notes/LITERATURE_POSITIONING.md):
  antecedentes y búsquedas prioritarias.
- [notes/RESEARCH_LOG.md](notes/RESEARCH_LOG.md):
  decisiones y resultados históricos/aún pendientes.
- [AI_HANDOFF.md](AI_HANDOFF.md): instrucciones para futuros agentes.
- Notas del vault: [[06-Media-de-diferencias-Guerrero]] y
  [[07-Perfilamiento-de-mu-en-CV]] (archivos en \`notes/conceptos/\`).

## Código fuente compartido

- **Ya existente:** \`src/trend_estimation/core/solvers.py\`
  implementa el plug-in Guerrero; \`forecasting/operators.py\`
  implementa continuación afín.
- **Nueva implementación:** \`src/trend_estimation/forecasting/mean_difference_cv.py\`
  calcula las tres alternativas, el extremo exacto y la media
  perfilada usando únicamente historia completada.
- **Pruebas:** \`tests/test_mean_difference_forecast_cv.py\`.
- **Piloto autónomo:** \`experiments/mean_difference_forecasting/run_pilot.py\`.
  No altera \`run_simulation_campaign.py\` ni \`outcomes.sqlite\`
  de la campaña anterior, cuya versión usaba \(\mu=0\).

## Estructura

\`\`\`text
Working Paper - Trend Simulation and Mean-Difference Forecasting/
├── README.md
├── AI_HANDOFF.md
├── build.py
├── notes/
│   ├── INDEX.md
│   ├── RESEARCH_NOTEBOOK.md
│   ├── PROOF_LEDGER.md
│   ├── SIMULATION_ATLAS.md
│   ├── LITERATURE_POSITIONING.md
│   └── RESEARCH_LOG.md
├── manuscript/
│   ├── main.tex
│   ├── references.bib
│   └── sections/01_...05_*.tex
├── checkpoints/
├── figures/
└── tables/
\`\`\`

La selección de formato de revista, título definitivo y resultados
NO se decide todavía. Los otros tres working papers **no se borran**:
sus matemáticas, código y resultados son antecedentes auditables.
Podemos reconsiderar la estructura editorial después de obtener
una contribución demostrable de este nuevo estudio.
