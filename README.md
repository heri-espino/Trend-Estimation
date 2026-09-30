# Trend Estimation

trend_estimation is a Python research library for penalized trend estimation,
forecasting, chronological validation, and numerical smoothness selection.

The repository is **library-first**: reusable methods live in
src/trend_estimation/; papers and experiments import the installed package.

## Current research focus

There are **three research papers** in this repository, plus one tutorial
companion.

Only one research paper is active:

\[
\boxed{\text{paper\_numerical-smoothness-selection/}}
\]

We are finishing that paper first. Until it is complete, do not start new
experiments or expand the scope of the other two research papers.

### 1. ACTIVE — Numerical smoothness selection

Directory: paper_numerical-smoothness-selection/

Working title:

**Numerical Selection of Forecast-Optimal Smoothness in Penalized Trend Estimation**

Core problem:
\[
S^\star\in\arg\min_{S\in[0,1]}CV_h(S),
\]
where the forecast-validation objective may have multiple local minima.

Main contribution: derivative-aware numerical discovery/refinement of relevant
minima on the compact smoothness domain, validated against a dense reference.

Read first:

- paper_numerical-smoothness-selection/notes/research_objective.md
- paper_numerical-smoothness-selection/notes/scope.md
- paper_numerical-smoothness-selection/notes/roadmap.md
- paper_numerical-smoothness-selection/notes/decisions.md

### 2. PARKED — Adaptive forecast-optimal trend estimation

Directory: paper_forecast-optimal-smoothing/

Working title:

**Adaptive Forecast-Optimal Trend Estimation under Changing Time-Series Regimes**

Core object:
\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

This paper owns regime/state adaptation and joint time-varying selection of
difference order, memory length, and smoothness. It resumes only after the
numerical paper is finished.

### 3. PARKED — Financial trend forecasting and recurrence

Directory: paper_smoothness-recurrence/

Working title:

**Forecasting Financial Trends and Measuring Recurrence under Competing Trend Models**

This paper compares a compact set of established trend/forecasting principles
such as forecast-optimal PLS, GCV PLS, likelihood/state-space models,
AR/ARIMA, residual-AR models, and no-change. It then studies first-passage and
recurrence behavior relative to the frozen ex-ante trend paths.

It does **not** own the smoothness-search algorithm. It resumes after the
numerical paper is finished.

### Tutorial companion

paper_penalized-trend-tutorial/ is explanatory material, not one of the three
research-paper tracks.

## Install

From the repository root:

~~~bash
conda env create -f environment.yml
conda activate trend-estimation
pip install -e .
~~~

For development and documentation:

~~~bash
pip install -e ".[dev,docs]"
~~~

Optional finance dependencies:

~~~bash
pip install -e ".[finance]"
~~~

Verify:

~~~bash
python -c "import trend_estimation as td; print(td.__version__)"
pytest
~~~

## Repository layout

~~~text
src/trend_estimation/                       reusable Python package
docs/                                       Sphinx API documentation
tests/                                      tests
examples/                                   small public-API examples
literature/                                 source literature and extracted text

paper_numerical-smoothness-selection/       ACTIVE research paper
paper_forecast-optimal-smoothing/           PARKED adaptive paper
paper_smoothness-recurrence/                PARKED financial/recurrence paper
paper_penalized-trend-tutorial/             tutorial companion

experiments/numerical_smoothness_selection/ active-paper experiments
experiments/forecast_optimal_smoothing/      parked adaptive experiments
experiments/smoothness_recurrence/           parked/historical applied experiments

results/                                    lightweight versioned experiment results
notes/                                      detailed legacy/adaptive scientific notes
~~~

## Documentation

The Sphinx site is the canonical user-facing library documentation:

~~~bash
sphinx-build -W -b html docs docs/_build/html
~~~

Paper-specific scientific decisions belong inside the corresponding paper
folder. Reusable code never belongs inside a paper directory.

## GitHub Actions

Push/pull-request CI stays lightweight: editable install, tests, and Sphinx
validation.

Paper/PDF compilation is manual-only through
.github/workflows/build-papers.yml. Heavy paper outputs are never generated on
ordinary pushes.
