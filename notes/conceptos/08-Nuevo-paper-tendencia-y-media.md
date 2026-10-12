---
title: "08 · Nuevo working paper: simulacion y pronostico de tendencia"
tags: [research-roadmap, publication, forecast, obsidian]
status: newly-scaffolded
---
# 08 · Nuevo artículo: estimar y pronosticar tendencias con diferencias de media no nula

## Pregunta

¿Mejora el pronóstico y la recuperación de una tendencia PLS modelar explícitamente el nivel medio $\mu$ de las diferencias de orden d, y **seleccionar $\mu$ para el horizonte de pronóstico** en lugar de fijarlo en cero o estimarlo únicamente del historial de diferencias?

## Tres alternativas mínimas

1. **Puro:** $\mu=0$, con suavidad S seleccionada mediante el mismo histórico TSCV.
2. **Guerrero (2007):** $\widehat\mu_t=\mathbf1^\top D_dx_t/(L-d)$ recalculada por ventana de ajuste, mientras S se elige sobre pérdida h-step.
3. **Nueva política conjunta:** $\mu^*(S)$ de bloques históricos de forecast-CV ya completados, y luego minimizamos $\widetilde F_T(S)$ sobre S.

Para evitar falsa contribución: casos 1 y 2 son antecedentes estándar o especializaciones. El tercero es una propuesta que requiere búsqueda bibliográfica exhaustiva, pruebas y evidencia fuera de muestra.

## Distinción esencial de los resultados

- \`notes/conceptos/06-Media-de-diferencias-Guerrero.md\`: derivación y ecuaciones fuente.
- \`notes/conceptos/07-Perfilamiento-de-mu-en-CV.md\`: perfilado, Hessiana concentrada, EDF, diferencias frente a la optimización in-sample.
- [Working paper nuevo](../../working_papers/Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting/README.md).
- [Protocolo de simulación nuevo](../../working_papers/Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting/notes/SIMULATION_ATLAS.md).

## Reorganización editorial: conservar antes de borrar

Los tres manuscripts anteriores quedan **como líneas paralelas / antecedentes**; no se destruyen PDFs, código ni resultados congelados. El nuevo paper pasará a ser el centro del estudio de simulación de tendencias y medias de diferencias. Solo al confirmar novedad y resultados podremos decidir si absorber, separar o archivar los trabajos antiguos; hacer "trash" sin auditar perdería comparadores, pruebas y trazabilidad.

## Checkpoint

**Demostrado en notas:** forma afín de pronóstico, media cuadrática óptima de validación, perfilado y fórmula de curvatura bajo no degeneración.

**Implementado sin afirmar tests pasados en GPU:** selector de prueba en nueva API y runner exploratorio separado.

**Pendiente:** resultados simulados, comparación con baselines y oráculos, evaluación de robustez temporal, benchmark de derivadas y manuscrito publicable.

> [!important] Estudio separado
> La campaña CUDA \`joint_formal_8h_v1\` ya iniciada pertenece al método con $\mu=0$. NO cambiar su objetivo ni su manifest para incluir el nuevo problema: crear resultados independientes después de validaciones unitarias.
