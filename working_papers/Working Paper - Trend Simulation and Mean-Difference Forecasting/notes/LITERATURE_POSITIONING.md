# Precedentes y auditoría de novedad

## Fuente verificada directamente

**Guerrero, V. M. (2007).** *Time series smoothing by penalized
least squares.* Statistics & Probability Letters 77,
1225–1234. DOI: 10.1016/j.spl.2007.03.006.

- Ecuación (2): penalización en torno al nivel medio
  $\mu$ de diferencias de orden d.
- Ecuación (3): modelo estadístico para esas diferencias.
- Ecuaciones (12), (16): ajuste con corrección de extremos.
- Ecuaciones (17) y (18): estimador plug-in de μ a
  partir de las diferencias observadas.
- Observaciones v y ejemplos: pronóstico y dependencia
  de orden d y media.

**NO atribuir al artículo de Guerrero** una selección
analítica de μ por pérdidas rolling-origin h-step
como la nueva propuesta.

## Otro material del repositorio

- Cortés-Toto, Guerrero & Reyes, *Trend smoothness
  achieved by penalized least squares with the smoothing
  parameter chosen by optimality criteria*, sobre
  comparadores CV/GCV/AICc/BIC.
- Literatura existente de TSCV/rolling-origin y
  forecast evaluation (véanse las notas
  \`working_papers/JOINT_FORMAL_8H_PROTOCOL.md\`).
- Literatura de penalización de diferencias con
  intercepto/drift, Hodrick–Prescott, modelos
  locales lineales y estimación de tendencia.

## Tareas de prioridad bibliográfica NO completadas

1. Buscar trabajos donde la media de orden-d diferencias
   se estime **por error predictivo multistep**, no por
   promedios observados, perfilada algebraicamente.
2. Buscar equivalencias con smoothing splines penalizados
   alrededor de una tendencia determinista y con
   trend-cycle filtering de media estimada.
3. Evaluar si optimizar μ e S sobre los mismos folds
   equivale a una regresión o estimación de drift
   previamente descrita bajo otra notación.
4. Buscar teoría estadística para CV con parámetros
   perfilados y dependencias h-step.
5. Evaluar qué teorema real (más allá de
   una identidad clásica) podría distinguir
   el trabajo de una aplicación.

**Estado:** el registro diferencia antecedentes
verificados y preguntas abiertas. NO afirmar novedad
de publicación sin completar la búsqueda.
