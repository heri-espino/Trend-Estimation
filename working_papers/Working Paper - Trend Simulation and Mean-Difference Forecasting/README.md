# Working Paper — Trend Simulation and Mean-Difference Forecasting

**Nuevo proyecto activo — 2026-10-11.** Antes de redactar el paper, se construye
un registro riguroso en **Markdown/Obsidian** con demostraciones, casos límite,
protocolos de simulación y resultados. El documento \`manuscript/main.tex\`
es un **esqueleto, NO un artículo listo para enviar**.

## Publication positioning (decision of 2026-10-15)

The **nonzero-\(\mu\)** investigation is retained as an **independent possible fourth paper**, not merged into the existing \(\mu=0\) forecast-CV paper. The immediate publication priority is the existing **numerical-methods Paper 3** (user's SMCCA submission target: **9 November 2026**); then the existing forecast-optimal smoothness Paper 1. The **mean-difference paper is prospective Paper C**, and the dynamic branch-selection paper is deferred.

**Concise research idea, exact identities already derived, and the limits of all existing experimental evidence:**
[notes/PAPER_C_IDEA_AND_EXISTING_RESULTS.md](notes/PAPER_C_IDEA_AND_EXISTING_RESULTS.md).

No completed external comparison of estimated nonzero \(\mu\) is claimed, and the frozen zero-mean Monte Carlo campaign is not reinterpreted as nonzero-\(\mu\) evidence.

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

## App Streamlit independiente del nuevo paper

\`\`\`powershell
streamlit run apps/mean_difference_forecasting.py
\`\`\`

Permite generar señales sintéticas con ruido, cargar CSV/Yahoo,
comparar **μ=0, μ plug-in de Guerrero y μ perfilada**,
dibujar la tendencia estimada pasada y el pronóstico futuro,
superponer la tendencia latente verdadera en datos sintéticos,
inspeccionar las curvas de forecast-CV y μ(S),
y exportar las decisiones, funciones y configuración.
La app llama el selector matemático compartido; no implementa
una segunda lógica independiente. Es exploratoria y aún requiere
prueba real en tu entorno.


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
