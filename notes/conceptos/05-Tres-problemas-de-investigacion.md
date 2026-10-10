---
tags: [investigacion, forecasting, optimizacion]
estado: mapa-conceptual
---
# 05 · Tres preguntas científicas diferentes

Partiendo de la misma familia de suavizadores y de las pérdidas futuras completadas, el repositorio distingue **tres problemas de investigación independientes**.

## Paper 1: Smoothness Cross Validation

**Pregunta:** ¿Qué suavidad minimiza globalmente una superficie $F_T(S)$ que agrega pérdidas históricas a horizonte $h$?

$$
S_T^\star\in\operatorname*{arg\,min}_{S\in[0,1]}F_T(S).
$$

Estudia la elección de suavidad según el rendimiento predictivo; no presupone que esa elección sea mejor que todos los benchmarks.

## Paper 2: Numerical Methods

**Pregunta:** ¿Cómo encontrar y verificar candidatos estacionarios y extremos de **una** $F_T$ fija?

Usa derivadas analíticas, búsqueda y métodos numéricos. Los argumentos basados en reducción racional y Sturm sólo entregan certificación bajo las condiciones **exactas y restringidas** que permiten formar el polinomio correspondiente. No equivalen a una prueba universal para matrices y datos flotantes.

## Paper 3: Dynamic Branch Selection

**Pregunta:** cuando llegan nuevas observaciones y cambia la superficie de $F_{T_1}$ a $F_{T_2}$, ¿puede el seguimiento de mínimos locales entre superficies aportar información adicional?

Para una familia diferenciable $F_T(S)$, un mínimo estricto no degenerado satisface

$$
\partial_SF_T(S)=0,\qquad
\partial_{SS}F_T(S)>0.
$$

El teorema de la función implícita puede justificar persistencia **local**, no continuidad global ni superioridad predictiva de la regla operativa de seguimiento.

## Cómo conectar los resultados

[[conceptos/03-Pronostico-y-CV-temporal|Superficies de pronóstico]] → [[conceptos/04-Derivadas-y-optimizacion|derivadas]] → búsqueda de candidatos → posible emparejamiento temporal → **evaluación externa no usada en selección**.

Las tres bitácoras científicas de autoridad están en [working_papers/](https://github.com/heri-espino/Trend-Estimation/tree/main/working_papers). Los [[Mapa de experimentos|experimentos históricos]] son antecedentes, no evidencia intercambiable.

**Límite central:** encontrar exactamente un mínimo de una función no demuestra que produzca el mejor pronóstico fuera de muestra.
