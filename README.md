# Trend Estimation

`trend_estimation` is a Python research library for penalized trend estimation,
forecasting, chronological validation, and numerical smoothness selection.

The repository is **library-first**: reusable methods live in
`src/trend_estimation/`; papers and experiments import the installed package.

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

Verify the editable install:

~~~bash
python -c "import trend_estimation as td; print(td.__version__)"
pytest
~~~

## Quick start

~~~python
import trend_estimation as td

data = td.make_local_linear_ar1_series(
    n_obs=200,
    observation_noise_std=0.4,
    ar1_phi=0.3,
    random_state=7,
)

model = td.PurePenalizedTrend(order=2, lambda_=10.0).fit(data.y)
print(model.forecast(steps=5))
~~~

For forecast-optimal selection:

~~~python
selection = td.select_fixed_window_pure_smoothness(
    data.y,
    orders=(1, 2, 3),
    windows=(24, 48, 72),
    horizon=3,
)
print(selection.best_)
~~~

## Documentation

The Sphinx site is the canonical user-facing documentation:

~~~bash
sphinx-build -W -b html docs docs/_build/html
~~~

Open `docs/_build/html/index.html` after the build.

Internal derivations and checkpoints remain in `notes/`. They are intentionally
separate from API documentation.

## Repository layout

~~~text
src/trend_estimation/                  installable Python package
docs/                                  Sphinx documentation
tests/                                 tests
examples/                              small public-API examples
experiments/forecast_optimal_smoothing adaptive-paper experiments
experiments/smoothness_recurrence/     smoothness/recurrence experiments
results/                               lightweight versioned experiment results
notes/                                 adaptive-paper derivations/checkpoints
literature/                            bibliography/RAG metadata
paper_forecast-optimal-smoothing/      adaptive forecasting paper
paper_smoothness-recurrence/           smoothness/financial recurrence paper
paper_penalized-trend-tutorial/        tutorial paper
~~~

Historical draft reports, old manuscript assets, copied legacy scripts, and
unimplemented placeholder namespaces are intentionally absent from `main`.
Git history is the archive.

## Research papers

The repository contains two distinct research tracks. Do not merge their
scientific objectives.

### Smoothness and financial recurrence

`paper_smoothness-recurrence/` is the compact SMCCA-oriented paper:

\[
S_h^\star
=
\arg\min_{S\in[0,1]} CV_h(S).
\]

It selects normalized smoothness directly on its compact domain, searches for
multiple local minima without an exhaustive dense grid, forecasts a frozen
trend path, and studies first-return/crossing times relative to that path.

Read `paper_smoothness-recurrence/notes/research_objective.md` and
`paper_smoothness-recurrence/notes/roadmap.md` first for this track.

### Adaptive forecast-optimal trend estimation

`paper_forecast-optimal-smoothing/` studies the broader adaptive object

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

Its canonical internal notes remain under `notes/`. Results from this track
are not automatically results of the recurrence paper.

## GitHub Actions

Automatic CI is lightweight: install, tests, and documentation validation.
Paper compilation remains manual-only through
`.github/workflows/build-papers.yml`.
