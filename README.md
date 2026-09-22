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
experiments/forecast_optimal_smoothing active experiments
notes/                                 derivations and checkpoints
literature/                            bibliography/RAG metadata
paper_forecast-optimal-smoothing/      active paper
paper_penalized-trend-tutorial/        tutorial paper
~~~

Historical draft reports, old manuscript assets, copied legacy scripts, and
unimplemented placeholder namespaces are intentionally absent from `main`.
Git history is the archive.

## Active research

The current paper studies whether forecast-optimal smoothness varies with
forecast horizon, estimation-window length, and local time-series conditions:

\[
S^\star_{T,h,L}=G(h,L,\mathcal R_T,X_T).
\]

See `notes/roadmap.md` for the internal research roadmap.

## GitHub Actions

Automatic CI is lightweight: install, tests, and documentation validation.
Paper compilation remains manual-only through
`.github/workflows/build-papers.yml`.
