# Trend Estimation

Research software for finite-difference penalized trend estimation,
chronological forecast validation and numerical smoothness optimization.

## Three independent working papers

1. **[Smoothness Cross Validation](working_papers/Working%20Paper%20-%20Smoothness%20Cross%20Validation/)** — pooled historical future-block forecast-MSE selection of normalized PLS smoothness, with CP01–CP03 evidence.
2. **[Numerical Methods](working_papers/Working%20Paper%20-%20Numerical%20Methods/)** — analytic derivatives, recovery of multiple minima, endpoint handling, adaptive search, and small-instance Sturm root isolation.
3. **[Dynamic Branch Selection](working_papers/Working%20Paper%20-%20Dynamic%20Branch%20Selection/)** — individual forecast-loss minima through time, branch matrices and dynamic smoothing decisions, with completed CP04–CP08 evidence.

Each study has its **own manuscript, scientific question, notes,
bibliography, experiments and conclusions**. The three manuscripts
are independent; no publication or result is conditional on the others.

The structure is documented in [working_papers/README.md](working_papers/README.md).

## Ideas and inactive research

[ideas/README.md](ideas/README.md) holds inactive paper concepts,
legacy manuscripts, historical files and archived mixed drafts.
These are not current working papers.

## Interactive applications

From the repository root:

~~~bash
python -m pip install -e ".[dashboard,finance]"
streamlit run apps/pooled_forecast_cv.py
~~~

The [pooled forecast-CV app](apps/pooled_forecast_cv.py) displays
each historical F(S), pooled F, CV windows and stride, loss matrix,
smoothing matrix and trend forecasts. The existing
[branch laboratory](apps/smoothness_lab.py) remains separate.

Both `apps/smoothness_lab.py` and `apps/smoothness_lab_advanced.py`
also offer two reproducible article-inspired simulation designs:
the linear trend `tau_t = 4*t/N` and the beta-density mixture
`tau_t = 0.6*BetaPDF(t/N;30,17) + 0.4*BetaPDF(t/N;3,11)`.
The article's sample sizes `N=50,200`, Gaussian noise levels
`sigma=0.5,2.0`, and optional quarterly additive seasonality
`[1,-0.5,-2.5,2]` are user-selectable. In generated data,
`latent` remains the true trend and `observed` adds noise and
optional seasonality. Both apps call the same implementation,
`experiments/smoothness_cv/article_simulations.py`.

## Shared research infrastructure

- `src/trend_estimation/`: reusable statistical software.
- `experiments/`: experiment scripts.
- `results/`: versioned frozen outputs.
- `data/`: input data.
- `literature/`: bibliographic corpus.
- `tests/`, `docs/`: CI and API documentation.

Keeping reusable code and frozen datasets in shared folders
does **not** merge the three independent article questions.
Historical experiment namespaces are preserved for reproducibility.

## Installation

~~~bash
conda env create -f environment.yml
conda activate trend-estimation
python -m pip install -e ".[dev,docs,dashboard]"
python -m pytest
~~~

CI runs tests/docs automatically; heavyweight PDF builds remain manual.
