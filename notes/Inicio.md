# Cuaderno de investigación · Trend Estimation

> [!abstract] Ruta de lectura
> Este vault es la **interfaz de estudio y navegación**. Los manuscritos y cuadernos particulares de cada working paper conservan la autoridad sobre sus afirmaciones científicas. La demostración extensa y compilable sigue en `notes_on_smoothnes/main.tex`.

## De Guerrero al suavizamiento óptimo

1. [[conceptos/01-Guerrero-y-PLS|01 · Modelo de Guerrero y PLS]] — ¿cómo surge la penalización de un modelo estadístico?
2. [[conceptos/02-Geometria-espectro-y-EDF|02 · Diferencias, espectro y grados de libertad]] — ¿por qué hay exactamente $d$ autovalores cero?
3. [[conceptos/03-Pronostico-y-CV-temporal|03 · Pronóstico y validación cronológica]] — ¿cómo escoger suavidad para predecir un bloque futuro?
4. [[conceptos/04-Derivadas-y-optimizacion|04 · Derivadas del suavizador y de la pérdida]] — ¿cómo se encuentran puntos estacionarios?
5. [[conceptos/05-Tres-problemas-de-investigacion|05 · Tres problemas distintos]] — ¿qué corresponde a cada working paper?

Estas fichas **resumen y conectan** resultados; no sustituyen la demostración completa. Para el recorrido detallado, consultar [[notes_on_smoothnes/README|Guía de la clase LaTeX]] y [main.tex en GitHub](https://github.com/heri-espino/Trend-Estimation/blob/main/notes/notes_on_smoothnes/main.tex).

## Nuevo eje de investigación · 2026-10-11

> [!important] Cuarto working paper: simulación de tendencias y media de diferencias
> Guerrero (2007) **ya** estudia medias no nulas de diferencias y una estimación plug-in. Lo nuevo que investigaremos es elegir esa media por **errores de pronóstico históricos completados**, concentrándola analíticamente antes de seleccionar la suavidad S.

6. [[conceptos/06-Media-de-diferencias-Guerrero|06 · De Guerrero a la media no nula]] — normal equations, corrección de bordes, particular binomial, EDF.
7. [[conceptos/07-Perfilamiento-de-mu-en-CV|07 · Perfilado analítico y sus demostraciones]] — F(S,μ), la media óptima en cada S, Hessiana concentrada y modelos que NO se deben confundir.
8. [[conceptos/08-Nuevo-paper-tendencia-y-media|08 · Nuevo paper y estado de investigación]] — notas del nuevo estudio y simulaciones futuras.

**Paper nuevo y prioritario:** [Trend Simulation and Mean-Difference Forecasting](https://github.com/heri-espino/Trend-Estimation/tree/main/working_papers/Working%20Paper%20-%20Trend%20Simulation%20and%20Mean-Difference%20Forecasting).
Sus notas de demostración y simulación viven fuera del vault, bajo \`working_papers/.../notes/\`, para conservar **una sola fuente de verdad**.

Los tres antiguos papers quedan como antecedentes en paralelo; los datos de la campaña CUDA existente corresponden al caso μ=0 y **no** son resultados del nuevo modelo.

## Resultados y conceptos del repositorio

- [[key_results|Identidades y resultados de referencia]]
- [[model_definitions|Modelos: puro, Guerrero con drift y variantes]]
- [[derivative|Derivada detallada del MSE de pronóstico]]
- [[numerical_selection|Selección numérica de suavidad]]
- [[window_and_smoothness|Longitud de ventana y suavidad comparable]]
- [[nested_validation|Evaluación nested sin fuga temporal]]
- [[ml_style_interpretation|Interpretación estilo ML]]

## Cuaderno y experimentos

- [[current_state|Estado histórico del proyecto]]
- [[roadmap|Roadmap histórico]]
- [[research_objective|Objetivo del estudio adaptativo previo]]
- [[Mapa de experimentos|Índice de experimentos y checkpoints]]
- [[Guia del vault|Cómo editar y sincronizar este vault]]

> [!important] Separación de fuentes
> Las notas superiores incluyen material histórico. Los tres proyectos actualmente independientes están bajo [working_papers/](https://github.com/heri-espino/Trend-Estimation/tree/main/working_papers), **fuera del vault**: el nuevo Trend Simulation and Mean-Difference Forecasting, más los tres anteriores como antecedentes. Sus propios cuadernos, demostraciones y resultados tienen prioridad para cada paper.

## Fórmula de referencia

Para $1\le d<L$, $Q_d=D_d^\top D_d$ y $\lambda\ge0$:

$$
\boxed{
\widehat\tau_{\lambda}=H_{\lambda}y,\quad
H_{\lambda}=(I_L+\lambda Q_d)^{-1},\quad
S_d(\lambda;L)=\frac{L-\operatorname{tr}H_{\lambda}}{L-d}.
}
$$

El papel de $S$ es medir la suavidad normalizada; **no** es otra matriz de suavizamiento. El criterio que se optimiza en el primer working paper es el error **futuro** de pronóstico, no el error dentro de la muestra.
