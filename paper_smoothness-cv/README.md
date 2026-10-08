# Forecast-optimal smoothness by chronological cross-validation

**Status: ACTIVE.**

**Intended journal:** *Communications in Statistics—Simulation and Computation*.

**Working title:** *Forecast-Optimal Smoothness Selection by Chronological Cross-Validation*.

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

Primary comparison: horizon-matched forecast-CV against
one-step forecast-CV, ordinary CV, GCV, AICc, and
simulation-only signal-recovery oracles. CP03 is the frozen
paper-scale core evaluation.

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
- Neither paper claims invention of PLS, predictive cross-validation
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
functional is claimed. The next step is to compile and review the
manuscript, including the completed empirical section and illustrations.


## Read first

1. `AI_HANDOFF.md`
2. `notes/dynamic_tracked_smoothness.md`
3. `notes/validation_semantics.md`
4. `notes/research_objective.md`
5. `notes/roadmap.md`
6. `manuscript/main.tex`

## Build: separate Windows and macOS stages

The manuscript uses standard `article` LaTeX, one column, and BibTeX `plain`.
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


## Interactive companion (not a frozen checkpoint)

A separate Streamlit app at `../apps/smoothness_lab.py` lets you explore the
latest dynamic tracked-minima design, using reproducible synthetic functions,
Yahoo Finance market series or a local CSV. It shows time-origin by smoothness
Validation-1 MSE heatmaps, local minima, Validation-2 MSE paths, the branch
matrices `V_j`, and `H_lambda` smoothing-matrix heatmaps. Plot choices
include the underlying generating trend (when known), level/log/return
representations, residuals, first differences and polynomial forecast
continuations. You can compare dynamic `phi(V_j)`, pooled forecast-CV and
manual smoothing, and export the inputs and resulting numerical matrices.

Run from repository root:

~~~bash
python -m pip install -e ".[dashboard,finance]"
streamlit run apps/smoothness_lab.py
~~~

The newest test block is excluded from selection and is revealed only on
request. Unlike the paper's frozen settings, the app uses a configurable,
lighter numerical-search depth and a grid-pooled benchmark for responsiveness.
No CP03--CP08 evidence is recomputed or changed. See the repository README for
the full validation contract.


### Guía de la interfaz interactiva en español

La aplicación se ejecuta desde la raíz del repositorio mediante
`streamlit run apps/smoothness_lab.py`.

Los cinco apartados de la interfaz distinguen explícitamente:

- **Tendencia y pronóstico:** serie observada, tendencia estimada,
  extrapolación y un esquema cronológico de ajuste, dos validaciones y prueba.
- **Errores de validación 1:** superficie del error cuadrático medio
  (ECM) para cada origen histórico y nivel normalizado de suavidad.
  El color relativo es solo una transformación de presentación; al consultar
  la matriz se muestra el ECM original.
- **Ramas y validación 2:** trayectoria temporal de los mínimos locales,
  ECM de validación 2 y matriz histórica `V_j=[S, ℓ₁, ℓ₂]`.
- **Matriz de suavizamiento:** pesos `H_ij`, traza del suavizador,
  grados de libertad efectivos y suavidad normalizada.
- **Tablas y descargas:** valores sin redondeo gráfico, con títulos y
  encabezados formales en español.

Los parámetros numéricos, la notación `d, L, h, S, λ` y los nombres internos
del motor permanecen invariantes. Las pruebas específicas de visualización se
encuentran en `tests/test_smoothness_spanish_ui.py`.
