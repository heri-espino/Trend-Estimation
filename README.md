# Trend Estimation

trend_estimation is a library-first research repository for finite-difference penalized trend estimation, forecasting, chronological validation, and smoothness selection.

## Research map

As of 2026-10-06, there are exactly **two active papers**.

### Paper A — Dynamic forecast-optimal smoothness

Directory: `paper_smoothness-cv/`

Primary target: **Journal of Forecasting**.

The pooled chronological selector remains a baseline,

\[
\widehat S^{\mathrm{pool}}_{T,h}
\in\arg\min_S F^{\mathrm{pool}}_{T,h}(S),
\]

but the central research object is now the sequence of local minima of
origin-specific forecast-loss surfaces,

\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\}.
\]

Nearby minima are tracked through time as data-driven branches. Each branch
stores smoothness, Validation-1 loss, and subsequent Validation-2 loss,

\[
V_j=[S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t}]_t.
\]

The forecasting decision is

\[
\widehat j_T=\psi(V_1,\ldots,V_J),
\qquad
\widehat S_T=\phi(V_{\widehat j_T}).
\]

Paper A owns branch scoring, branch selection, final smoothness rules, refitting,
and forecast evaluation.

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

Los paneles muestran el esquema cronológico, las curvas ECM(S) para diferentes
órdenes d, el seguimiento gráfico de ramas, las matrices V específicas de cada
(d, rama, regla), la comparación de ECM históricos, el test real y el
suavizador matricial H_lambda. Se pueden descargar matrices V completas y
subconjuntos particulares.

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
