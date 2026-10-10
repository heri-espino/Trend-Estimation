# Tres working papers, preguntas no intercambiables

[[Inicio|Inicio]] · [[mapas/Mapa de resultados|Ruta matemática]]

## Paper 1 — Smoothness Cross Validation

Para $m,d,L,h$ fijos se agregan **funciones completas** de pérdida futura en una superficie ponderada [[DEF-007|$F_M(S)$]] y se elige su mínimo global [[RES-011]]. No se promedian minimizadores de folds.

[Fuente de verdad del paper 1](https://github.com/heri-espino/Trend-Estimation/tree/main/working_papers/Working%20Paper%20-%20Smoothness%20Cross%20Validation).

## Paper 2 — Numerical Methods

En una **superficie fija**, estudia candidatos estacionarios, derivadas [[RES-009]], comparación de extremos y algoritmos numéricos. El conteo por Sturm exige un caso polinómico **exacto y restringido**, no es certificado automático de todas las instancias en punto flotante.

[Fuente de verdad del paper numérico](https://github.com/heri-espino/Trend-Estimation/tree/main/working_papers/Working%20Paper%20-%20Numerical%20Methods).

## Paper 3 — Dynamic Branch Selection

Con la **misma** $F_r$, estudia familias cronológicas de mínimos locales: detección → emparejamiento adyacente → regla de rama. El resultado [[RES-012]] sólo respalda la persistencia **local** de mínimos simples bajo cambios suaves, no la superioridad estadística de seguir una rama.

[Fuente de verdad del paper dinámico](https://github.com/heri-espino/Trend-Estimation/tree/main/working_papers/Working%20Paper%20-%20Dynamic%20Branch%20Selection).

**Advertencia histórica:** checkpoints CP01–CP08 que estudiaron Val1/Val2 corresponden a un método anterior, no a la selección dinámica vigente. Véanse [el contrato de teoría](https://github.com/heri-espino/Trend-Estimation/blob/main/working_papers/THEORETICAL_CONTRIBUTIONS.md) y [el protocolo de superficies](https://github.com/heri-espino/Trend-Estimation/blob/main/working_papers/WEIGHTED_SURFACE_PROTOCOL.md).
