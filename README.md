# Trend Estimation

trend_estimation is a library-first research repository for finite-difference penalized trend estimation, forecasting, chronological validation, and smoothness selection.

## New independent pooled F Streamlit app

- **[Pooled Forecast-CV Lab](apps/pooled_forecast_cv.py):** individual F_t(S) curves, pooled F(S), the fold-by-S validation MSE heatmap, rolling-CV controls, trend fits and forecasts, spectral views and downloadable results. It **does not** track minimum branches.
- **[Existing tracked-minima lab](apps/smoothness_lab.py):** the more general branch and validation-rule experiment. It is **unchanged**.

Launch the new app from the repository root:

~~~bash
python -m pip install -e ".[dashboard,finance]"
streamlit run apps/pooled_forecast_cv.py
~~~

See [the complete guide](paper_smoothness-cv/notes/POOLED_APP.md).

## Research map

**Current direction (2026-10-08):** The forecasting study focuses on choosing normalized PLS smoothness by minimizing pooled, horizon-matched historical forecast MSE. The current intended journal is *Communications in Statistics—Simulation and Computation*. The manuscript is an interim draft; the numerical method and final simulations remain under investigation. [Canonical research notes](paper_smoothness-cv/notes/INDEX.md).

### Paper A — Horizon-matched forecast-optimal smoothness

Directory: paper_smoothness-cv/

\[
\widehat S_{T,d,L,h}^{\mathrm{pool}}
\in\arg\min_{S\in[0,1]}\frac1M\sum_{m=1}^{M}F_{t_m}(S).
\]

The F curves score forecasts issued at earlier historical origins against their subsequent, **now-observed** future blocks. After tuning, the estimator refits at the current origin and predicts the genuinely unknown future. Tracking individual minima across folds is a separate, optional hypothesis and is not required for the pooled criterion. Frozen CP01–CP08 outputs remain preserved as historical evidence.

### Paper B — Numerical recovery and tracking of minima

Directory: `paper_numerical-methods/`

Paper B owns:

1. recovery of all relevant local minima of each multimodal forecast-loss surface;
2. exact endpoint handling;
3. adaptive derivative-aware search and Brent refinement;
4. temporal correspondence of minima across adjacent surfaces.

The current temporal baseline is one-to-one matching under

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon_{\mathrm{track}}.
\]

Do not confuse `track_epsilon` with within-surface `candidate_spacing`.

Frozen evidence for the per-surface solver remains 240/240 adversarial relevant
optima, 2105/2105 synthetic reference minima, and 473/473 financial geometry
stress minima.

## Laboratorio interactivo de mínimos, ramas y suavidad

La aplicación principal **en español** en apps/smoothness_lab.py implementa
el protocolo más general: **seguir mínimos locales para cada orden de
diferencias d, construir matrices V por rama y por regla de suavidad, y elegir
entre ellas según su error histórico en validación 2**.

El procedimiento para cada origen cronológico es:

1. **Fijar primero el orden d y la regla r**. La regla define la transformación
   S_aplicado = phi_r(V_historial, s). La pérdida de validación 1 se busca sobre
   la función **dependiente del método** ECM_1(phi_r(V_historial, s); d),
   no sobre la misma curva para todos los métodos. La superficie original
   ECM_1(S; d) también se representa, como referencia.
2. Recuperar los mínimos de esta función transformada por (d, regla, rama) y
   seguir sus trayectorias según la S **aplicada**. Las ramas pertenecen a un
   (d, regla): nunca se reutilizan para otra regla. Cada nueva rama comienza
   sin historial y el primer mínimo coincide con el de la función original.
   Las reglas incluyen el último mínimo (continuación polinómica original),
   medias, medianas, pesos por recencia, pesos por ECM histórico de validación
   2 y extrapolaciones. Si la regla no depende de s actual, su función
   transformada es plana: se registra como objetivo no identificable, no
   como un mínimo local nuevo.
3. Registrar en la matriz V específica de la combinación los valores del
   mínimo local, S_aplicado, ECM de validación 1 y ECM de validación 2.
   **En validación 2 no se vuelve a optimizar S**: al desplazarse el origen,
   la tendencia se estima mecánicamente con los datos hasta ese origen,
   pero conserva el método, d y S_aplicado que ya fijó la regla.
4. Comparar el **ECM medio histórico de validación 2** por (d, rama, regla);
   únicamente seleccionar ramas con soporte mínimo. Errores de validaciones
   2 aún no terminadas nunca alimentan las reglas retrospectivamente.
5. Con la regla ganadora y la última validación 1 disponible, obtener
   S* y pronosticar la **prueba reservada** sin reoptimizar ningún
   hiperparámetro. Mostrar lado a lado el pronóstico y los **valores reales**
   que ocurrieron, e informar su ECM.
6. Mantener el mismo método, d* y S* y volver a estimar con las últimas
   L observaciones disponibles para pronosticar más allá de la serie real.

Los paneles muestran el esquema cronológico y permiten elegir con controles
separados el orden d y la regla r para representar el ECM de validación 1
**transformado por el método** para cada rama. También se muestra el
seguimiento de ramas y la matriz V para cada (d, r, rama), con la opción de
superponer otras ramas con menor opacidad. Una figura retrospectiva aproxima
visualmente la continuación de tendencia pronosticada en el test con la
serie real reservada: se utiliza la tendencia estimada antes del test y se
muestran los valores reservados **solo después**, para fines informativos.
Un gráfico distinto muestra el modelo final reajustado y el pronóstico
operativo posterior a la última observación. Se mantienen las descargas y
la visualización del suavizador matricial H_lambda.

**Caso particular:** en la barra lateral se puede elegir selección directa en
dos bloques. Esta omite el seguimiento histórico y selecciona el par (d,S)
por la segunda validación. La selección directa sigue disponible en
experiments/smoothness_cv/two_stage_lab.py; la generalización con reglas se
implementa en experiments/smoothness_cv/branch_rule_lab.py. La versión
histórica anterior continúa disponible por separado en
apps/smoothness_lab_advanced.py, sin sustituir los checkpoints congelados.

Instalar y lanzar desde la raíz del repositorio:

~~~bash
python -m pip install -e ".[dashboard,finance]"
streamlit run apps/smoothness_lab.py
~~~

Ejecutar las pruebas relevantes:

~~~bash
python -m pytest tests/test_branch_rule_lab.py tests/test_two_stage_smoothness_lab.py tests/test_live_smoothness_lab.py tests/test_smoothness_spanish_ui.py
~~~

**Alcance:** se comparan reglas para convertir los mínimos históricos en
suavidad aplicada, no distintos modelos estadísticos de extrapolación.
La extrapolación de la tendencia sigue siendo la polinómica por diferencias
penalizadas. El ECM de validación 1 es descriptivo, ya que sus datos también
se utilizaron para encontrar el mínimo; el ECM histórico de validación 2
separa selección y evaluación dentro de cada origen. La elección global
de (d, rama, regla) usa esos resultados históricos y debe juzgarse sobre
la prueba realmente reservada. Los experimentos son exploratorios y no
modifican CP03–CP08.

### Other directories

Other paper directories are historical, parked, tutorial, or idea workspaces.
They are **not active research tracks**. Do not add new research work to them
unless the user explicitly reactivates one.

The legacy `paper_numerical-smoothness-selection/` directory is a historical
pre-split snapshot and must not receive new work.

## Canonical reading order for another AI agent

1. `AI_HANDOFF.md`
2. `RESEARCH_MAP.md`
3. `paper_smoothness-cv/AI_HANDOFF.md`
4. `paper_smoothness-cv/notes/dynamic_tracked_smoothness.md`
5. `paper_smoothness-cv/notes/validation_semantics.md`
6. `paper_numerical-methods/AI_HANDOFF.md`
7. `paper_numerical-methods/notes/temporal_minima_tracking.md`

## Stable implementation namespaces

Reusable methods remain under src/trend_estimation/.

For reproducibility, the existing experiment/result namespaces are intentionally not renamed yet:

- experiments/numerical_smoothness_selection/
- results/numerical_smoothness_selection/

The active Journal of Forecasting criterion paper now has its own checkpointed empirical pipeline under `experiments/smoothness_cv/`, with versioned outputs under `results/smoothness_cv/`.

Those names are historical implementation namespaces, not the current paper title.

## Install

~~~bash
conda env create -f environment.yml
conda activate trend-estimation
pip install -e .
pytest
~~~

## CI policy

Automatic CI stays lightweight. Paper/PDF compilation remains manual-only through workflow_dispatch.
