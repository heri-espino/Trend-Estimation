# Horizon-Matched Cross-Validation for Forecast-Optimal Penalized Trend Smoothness

**Status: ACTIVE.**

**Intended journal:** *Communications in Statistics—Simulation and Computation*.

**Provisional working title:** *Horizon-Matched Cross-Validation for Forecast-Optimal Penalized Trend Smoothness*.

## Research status — important 2026-10-08 update

**Research is ongoing; the present LaTeX article is a WORKING DRAFT, not the final publication text.** The current source of truth is [notes/INDEX.md](notes/INDEX.md), followed by [notes/research_objective.md](notes/research_objective.md), [notes/mathematical_foundations.md](notes/mathematical_foundations.md), [notes/research_log_2026-10.md](notes/research_log_2026-10.md), and [notes/next_experiments.md](notes/next_experiments.md).

The main problem is choosing the normalized index S over [0,1] by *historical completed future-block forecast MSE* to produce an extrapolatable trend; no current unobserved future enters the selection. Eigenvalue decomposition, analytic derivatives, and multi-minimum optimization are central technical topics. Branch tracking remains optional.

CP01–CP08 have already run and their results are preserved. **We plan to compare numerical solvers and may rerun/redesign simulations**; historical CP03 results should not automatically be treated as the definitive experiments for the final article. Changing the numerical solver does not change the exact minimizer of an unchanged mathematical objective.

**Editorial timing:** after mathematical/numerical verification and new experiment decisions, rewrite the final independent article from the completed notes. Earlier build and submission-ready checklists are provisional.

## Manuscript for Communications in Statistics—Simulation and Computation

The standalone manuscript is under `manuscript/` and uses a
standard single-column LaTeX submission draft with author-year
references. The revised main text emphasizes the primary
horizon-matched S-domain forecast-CV method and frozen CP03
Monte Carlo results. CP04–CP08 exploratory branch-based
experiments are retained in the appendices, not presented
as necessary components of the primary method.

**Current status:** manuscript sources revised and structurally
audited. A new PDF compilation and visual review remain
necessary. This is not a final submission approval.
See `SUBMISSION_READINESS_CSSC_2026-10.md`.

## Primary scientific question

How should the normalized smoothness of a finite-difference
penalized-least-squares trend be selected when that trend will be
extrapolated over a specified forecast horizon `h`?

The principal statistical construction minimizes **chronological,
horizon-matched forecast MSE** for the normalized smoothness
index. This is a complete method: it does **not** require tracking
local minima through time.

### The smoother and smoothness coordinate

\[
\widehat\tau_{\lambda,T}=H_\lambda x_T,\qquad
H_\lambda=(I+\lambda D_d^\top D_d)^{-1},
\]

\[
S(\lambda)=1-\frac{1}{L-d}\sum_{\delta_j>0}
\frac{1}{1+\lambda\delta_j}\in[0,1].
\]

This is a monotone rescaling of a Guerrero-type smoothness
index, not a new smoother.

### Proposed forecast-CV selection

For historical origins `t_m`, use the fitted trend and the
declared finite-difference continuation operator `G_{d,h}`
to forecast each subsequently observed validation block:

\[
F^{\mathrm{pool}}_{d,L,h}(S)
=\frac1M\sum_{m=1}^{M}\frac1h
\|y_{t_m+1:t_m+h}-G_{d,h}H_{\lambda(S)}x_{t_m}\|_2^2,
\]

\[
\widehat S^{\mathrm{FCV}}_{T,d,L,h}
\in\arg\min_{S\in[0,1]}
F^{\mathrm{pool}}_{d,L,h}(S).
\]

At the current outer forecast origin `T`, all historical
validation outcomes used for tuning are already observed.
After selection, discard all historical fitted trends, refit
on the latest `L` observations, and extrapolate into the
untouched future block.

Earlier primary comparison: horizon-matched forecast-CV against
one-step forecast-CV, ordinary CV, GCV, AICc, and
simulation-only signal-recovery oracles. CP03 was the frozen
paper-scale evaluation **for the older design**, not necessarily the next final suite.

## Numerical implementation

Forecast-CV searches the normalized smoothness domain S in [0,1].
The objective can be multimodal, so the numerical implementation
uses adaptive derivative brackets, Brent refinement, and exact
endpoint comparisons. Root-search details do not change the
statistical definition of horizon-specific forecast-CV.

## Optional time-adaptive extension

If the analyst assumes that recent favorable smoothing
regimes inform future performance, individual local minima
may be tracked across historical origins into branch
histories `V_j=[S, Validation-1 loss, Validation-2 loss]`.
Then use a historical branch selector `psi` and a
decision map `phi(V_j)` to choose current smoothness.
Possible `phi` mappings include newest, recent mean,
median, recency weighting, validation-loss weighting,
and extrapolation of the smoothness trajectory.

Different maps encode different assumptions. They are
not part of the core forecast-CV definition, and the
completed CP04–CP08 experiments do **not** establish
a universally best map. See
`notes/dynamic_tracked_smoothness.md` for this
**optional** layer.

## Paper boundary

- This paper: horizon-matched forecast-MSE selection of PLS
  smoothness, information-safe refitting, controlled comparison
  with conventional selectors, and optional adaptation examples.
- Numerical implementation: bracket and refine competing stationary
  roots and compare both limiting smoothness endpoints.
- This study does not claim invention of PLS, predictive cross-validation
  in general, or the Guerrero smoothness index.

## Completed empirical evidence

- CP03: frozen 3,000-scenario, 72,000-block simulation of horizon-matched
  pooled forecast-CV and classical smoothness benchmarks.
- CP04: 16 reserved outer tests from four heterogeneous time series;
  frozen recency branch rule / pooled CV gRMSE = 0.692.
- CP05: 64 previously unused financial series, 256 outer tests;
  frozen recency / pooled CV gRMSE = 1.642. Broad-panel superiority
  was not established.
- CP06: post-hoc continuation-order diagnostics identify high-order
  extrapolation as a major source of unstable forecast paths.
- CP07: 1,200 controlled roughness scenarios, 9,600 outer decisions;
  recency / pooled CV observed-log-RMSE = 1.037 overall.
- CP08: fresh 1,200-scenario demonstration of several maps
  \(\phi(V_j)\) from identical branch histories, including three
  reproducible figures and boundary-clipping diagnostics.

CP08 closes the rule-family demonstration stage; no universally best
functional is claimed. The next research step is **numerical verification and a new experimental decision**, not merely compiling the existing working draft. A PDF can still be built for inspection.


## Read first — current research direction

1. [notes/INDEX.md](notes/INDEX.md) — canonical map of research notes.
2. [notes/research_objective.md](notes/research_objective.md) — the prediction-based S selection question.
3. [notes/mathematical_foundations.md](notes/mathematical_foundations.md) — eigendecomposition, smoothness, derivatives, multimodal forecast MSE.
4. [notes/validation_semantics.md](notes/validation_semantics.md) — historical pseudo-futures and mandatory final refit.
5. [notes/research_log_2026-10.md](notes/research_log_2026-10.md) — actual CP01–CP08 archival outcomes.
6. [notes/next_experiments.md](notes/next_experiments.md) — old/new numerical comparison and prospective simulation design.
7. [AI_HANDOFF.md](AI_HANDOFF.md) — continuity for another research assistant.
8. `manuscript/main.tex` — *interim* CSSC-oriented LaTeX draft, not the final re-written article.

## Build: separate Windows and macOS stages

The working manuscript uses standard `article` LaTeX, one column, and BibTeX `plainnat` with author-year citations.
The Python preparation and the LaTeX build are **not** run on the same
machine. The two stages exchange generated assets through GitHub.

### 1. Windows PowerShell: Python, tests and figures only

From the repository root:

~~~powershell
git pull
powershell -NoProfile -ExecutionPolicy Bypass -File .\paper_smoothness-cv\prepare-paper.ps1
~~~

This script installs the editable package, runs the chronology/manuscript
tests, regenerates the tutorial figure (PDF/PNG/JSON), and executes
`python paper_smoothness-cv/build.py --check` (source validation only).
It **never** invokes `pdflatex`, `latexmk` or `bibtex`.

Push the generated figures so the Mac can see them:

~~~powershell
git add paper_smoothness-cv/manuscript/figures/
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { git commit -m "Update forecasting figures for LaTeX" }
git push
~~~

### 2. macOS Terminal: LaTeX compilation only

After the Windows changes are pushed:

~~~bash
git pull
bash paper_smoothness-cv/compile-paper.sh
~~~

This script checks that the committed source and figures exist, then
compiles the document with `pdflatex` and BibTeX (`latexmk` optional).
Python is used solely to run the existing LaTeX build helper. It does
**not** rerun figures, simulations, or Python tests.

Once the compiled manuscript has been inspected:

~~~bash
git add paper_smoothness-cv/EspinoMontelongo-2026-Forecast_Optimal_Smoothness.pdf
if ! git diff --cached --quiet; then
  git commit -m "Compile updated forecasting manuscript on macOS"
fi
git push
~~~

### If LaTeX fails on macOS

The generic `latexmk` message or Python `CalledProcessError` reports only
the failure status, not the underlying TeX error. The build helper now
prints the first actual error from the retained log automatically.
You can also inspect the previous failure **without rebuilding**:

~~~bash
python3 paper_smoothness-cv/build.py --diagnose
~~~

The full log is `paper_smoothness-cv/build/stage/main.log`.
Share the first TeX error and surrounding context, rather than the
last `latexmk` or Python traceback lines. Do not use `latexmk -f` to
force a build with unresolved TeX errors.
The compiled PDF keeps its existing repository path. The older
`build-workflow-paper.ps1` remains as a compatibility alias for
**Windows preparation only**, and does not compile LaTeX.

## Five-panel workflow tutorial

The forecasting manuscript includes a full-width pedagogical figure,
`fig_workflow_tutorial.pdf`, at the end of its evaluation-design section.
The five horizontal panels show:

- a historical Train/Validation-1/Validation-2 pair, followed by a
  **separate current/final Validation-1 block** and an untouched outer test;
- fresh penalized trend fits on the latest window for pooled CV, the newest
  tracked minimum, and the recency-weighted mean;
- the three forecasts against the subsequently observed outer test;
- the **current Validation-1 forecast-loss curve** (never the test-loss
  curve), recovered minima, and all three smoothness decisions;
- historical tracked minimum branches and the final branch-to-smoothness
  maps \(\phi(V_j)\).

The figure uses a deterministic example: CP07 switch-to-rough simulation,
seed 100, observation-noise SD 0.01, outer decision 8. It is not selected
using test performance. The script writes PDF, PNG, and machine-readable
provenance directly to `manuscript/figures/`.

To regenerate this figure on Windows, run `prepare-paper.ps1` and push
the generated figure files. The macOS-only `compile-paper.sh` will
then include the saved PDF during LaTeX compilation.
`build.py --check` intentionally reports a missing figure if the generator
has not been run. `build.py` stages the manuscript source (including its
`figures/` folder) and the separately frozen CP08 figures.


## Aplicaciones interactivas (no son checkpoints congelados)

### Laboratorio principal: seguimiento de mínimos para todos los órdenes d

La interfaz apps/smoothness_lab.py fija la combinación (d, regla)
**antes** de validación 1. Cada regla compone la función de pérdida
de validación 1 con su transformación histórica S_aplicado =
phi_regla(V_historial, s). Se identifican mínimos de esa función
**transformada por el método** y se siguen las ramas por cercanía de S_aplicado.
Cada rama pertenece a su par (d, regla), nunca se comparte entre reglas.
La superficie ECM(S;d) sin transformación sigue disponible para comparar
órdenes y conservar el caso original. La matriz V por (d, regla, rama)
almacena el argumento del mínimo, S_aplicado, ECM_val1 y ECM_val2.
Los métodos independientes del argumento actual producen objetivos planos,
que se etiquetan y no se presentan como mínimos únicos.

La regla se define **antes de conocer validación 2** del origen actual.
Al iniciar la evaluación de validación 2, no se selecciona otro S ni otro
orden: se usa el S producido por esa regla en validación 1. La tendencia
puede estimarse de nuevo a medida que se desplaza el origen y entran datos
nuevos, pero con el mismo método, d y S de la decisión. Cuando una regla
utiliza errores de validación 2 históricos, estos deben pertenecer a bloques
que **habían terminado antes** del origen actual, especialmente si se
solapan las ventanas.

Se incluyen el método original de **continuación polinómica del último
mínimo** (last), medias, medianas, reglas ponderadas por recencia o por
error de validación 2 y extrapolación temporal de los mínimos locales.
El criterio global selecciona (d, rama, regla) por menor ECM histórico
medio en validación 2, sujeto a cobertura mínima. En una validación 1
final, separada de las anteriores, se continúa la rama y se fija S
para el test, que permanece no visto hasta su evaluación. Se reportan
las observaciones reales y el pronóstico reservado para calcular errores
verdaderamente fuera de muestra. Posteriormente se reajusta el mismo
modelo, con d y S fijos, para pronosticar desde la última observación real.

La interfaz permite seleccionar mediante botones el orden d y la regla r
para inspeccionar sus propias curvas ECM de validación 1 (con historial
específico por rama). Las matrices V cuentan con un control para superponer
las demás ramas del mismo (d,r) con menor opacidad. Un gráfico del test
reservado muestra la tendencia extrapolada desde el último ajuste anterior
al test frente a sus valores reales: no se utilizan esos valores para
seleccionar d, r, rama ni S. El ajuste final con todos los datos y su
pronóstico posterior se muestran por separado. También se mantiene H_lambda.

### Caso particular: dos bloques sin seguimiento

La misma barra lateral permite cambiar al procedimiento directo:
los mínimos de una única validación 1 se comparan en una única
validación 2. Se conserva para que la generalización de ramas
pueda contrastarse con un caso sencillo.

La versión dinámica previa también se conserva sin cambios en
apps/smoothness_lab_advanced.py. El protocolo principal actualizado
se implementa en experiments/smoothness_cv/branch_rule_lab.py; el caso
directo se implementa en experiments/smoothness_cv/two_stage_lab.py.

### Ejecución

~~~bash
python -m pip install -e ".[dashboard,finance]"
streamlit run apps/smoothness_lab.py
~~~

Pruebas de invariancia temporal, regla original y matrices V:

~~~bash
python -m pytest tests/test_branch_rule_lab.py tests/test_two_stage_smoothness_lab.py tests/test_live_smoothness_lab.py
~~~

Estas interfaces son exploratorias y no modifican los experimentos
congelados CP03–CP08 ni sus resultados. El motor no afirma superioridad
predictiva hasta que se obtengan comparaciones válidas fuera de muestra.
