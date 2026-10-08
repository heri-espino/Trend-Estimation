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

## Interactive laboratories (distinct statistical treatments)

Install once, then launch either research treatment from the repository root:

~~~bash
python -m pip install -e ".[dashboard,finance]"
streamlit run apps/pooled_forecast_cv.py
streamlit run apps/dynamic_branch_cv.py
~~~

**Laboratory 1: CV of the average historical F(S)**
(`apps/pooled_forecast_cv.py`). Each completed rolling-origin fold has
its own forecast-MSE curve F_t(S); the criterion is their **arithmetic
average**. The chosen S minimizes this pooled loss, **not** the average
of each fold's minimizer. There is **no branch tracking**.

**Laboratory 2: dynamic CV of local-minimum branches**
(`apps/dynamic_branch_cv.py`). For each order d and history-aggregation
rule r it identifies and tracks the relevant local minima in time,
builds branch-specific V matrices, and selects (d, branch, rule)
based on past Validation-2 losses. It is a **different estimator**,
not another visualization of pooled F(S). The older entry point
`apps/smoothness_lab.py` remains compatible. A separate legacy
dynamic interface lives at `apps/smoothness_lab_advanced.py`.

Both current laboratories (and the legacy interface) also expose the
same article-inspired linear trend `4t/N` and beta-density mixture
`0.6*BetaPDF(t/N;30,17) + 0.4*BetaPDF(t/N;3,11)`. Sliders allow
`50 <= N <= 200` and `0.5 <= sigma <= 2`; the article's exact
experimental levels are `N=50,200` and `sigma=0.5,2`.
Optionally add the quarterly cycle `[1,-0.5,-2.5,2]` with seeded
iid Gaussian noise. The theoretical latent trend is kept separate.

**Whole-series trend (optional):** both laboratories have a toggle
to fit a PLS trend to **all available observations**, holding their
already-selected d and S fixed. This uses the outer test if present
and is **descriptive in-sample smoothing**, not a forecast/backtest.
The original chronology, reserved-test predictions, and selection
results remain untouched. Full-series trends can be exported as CSV.

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
