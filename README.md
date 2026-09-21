# Trend Estimation

`trend_estimation` is a research-oriented Python library for penalized trend estimation, chronological validation, forecasting, and numerical smoothness selection.

The repository is deliberately **library-first**. Reusable mathematics, estimators, validation protocols, optimizers, metrics, and simulation tools belong in `src/trend_estimation/`. Papers and experiments consume the installed library; they should not duplicate estimator mathematics.

## Active research question

The current paper studies **forecast-optimal smoothness**:

\[
S^\star = S^\star(h,L,\mathcal R,\text{series class}),
\]

where \(h\) is forecast horizon, \(L\) is the estimation-window length, and \(\mathcal R\) denotes local time-series conditions such as volatility, serial dependence, signal-to-noise ratio, and structural change.

The planned empirical progression is

\[
\text{macroeconomic series}
\rightarrow
\text{market indices / ETFs}
\rightarrow
\text{individual equities}
\rightarrow
\text{crypto}.
\]

The goal is not to assume that "more volatility means less predictability." The goal is to measure how forecast-optimal smoothing and forecast skill vary with horizon, window length, and local stochastic regime.

The downstream portfolio/decision-aware project is **paused**. It remains a possible future extension but is not part of the active paper.

## Core model currently used for analytic work

For observations \(y\in\mathbb R^n\), difference operator \(D_d\), and \(Q=D_d^\top D_d\),

\[
\widehat t_{\lambda,d}
=
\arg\min_t
\left\{
\|y-t\|_2^2+\lambda\|D_dt\|_2^2
\right\}
=
(I+\lambda Q)^{-1}y.
\]

Writing \(S_\lambda=(I+\lambda Q)^{-1}\),

\[
S_\lambda'=-S_\lambda Q S_\lambda,
\qquad
\widehat t_\lambda'=-S_\lambda Q\widehat t_\lambda,
\qquad
\widehat t_\lambda''=2S_\lambda Q S_\lambda Q\widehat t_\lambda.
\]

These identities are implemented and tested in the library.

## Forecast validation invariant

At forecast origin \(T\), fitting code may use only observations available at or before \(T\). Future observations can score the forecast but may not influence the fitted trend.

Repeated evaluation should use rolling or expanding forecast origins. Random internal masking is useful for a different question—trend reconstruction/interpolation—but it is not the main validation protocol for the active forecasting paper.

## Numerical selection of smoothness

The active numerical direction is:

\[
\text{coarse log-}\lambda\text{ scan}
\rightarrow
\text{bracket roots of }CV'(\lambda)
\rightarrow
\text{Brent root solving}
\rightarrow
\text{classify stationary points}
\rightarrow
\text{evaluate every local minimum}.
\]

Newton in log-\(\lambda\) remains useful as a refinement/benchmark, but not as the only global search when the validation objective is multimodal.

See `notes/key_results.md`, `notes/derivative.md`, and `notes/numerical_selection.md`.

## Papers

Paper directories use the convention `paper_<short-title>/`.

- `paper_forecast-optimal-smoothing/` — **active research paper**.
- `paper_penalized-trend-tutorial/` — mathematical/tutorial companion; currently secondary.
- `paper/` — legacy S&P 500 manuscript assets retained as historical material, not a canonical manuscript.

The active paper must call the installed `trend_estimation` package for experiments. If a method is useful beyond one manuscript, implement it in the library first.

## Internal research documentation

`notes/` is the scientific notebook for this repository.

- `notes/key_results.md`: compact list of results we currently rely on.
- `notes/derivative.md`: step-by-step forecast-loss derivative derivation.
- `notes/numerical_selection.md`: root-finding strategy for high-degree/non-unimodal objectives.
- `notes/model_definitions.md`: exact estimator definitions and unresolved model-identification issues.
- `notes/roadmap.md`: canonical record of what we are doing, why, what is done, and what comes next.

Every mathematical note should state where the result is used in `src/trend_estimation/` and whether it is implemented, tested, or only derived.

## Literature

`literature/` holds the bibliography manifest and research-reading workflow. Local PDFs belong in `literature/pdfs/`, which is ignored by Git so copyrighted or institutionally accessed files are not redistributed accidentally.

## Installation

```bash
conda env create -f environment.yml
conda activate trend_estimation
python -m pip install -e ".[dev,finance]"
pytest
```

## Repository layout

```text
src/trend_estimation/                  reusable research library
tests/                                 unit and mathematical-consistency tests
notes/                                 internal derivations, checkpoints, roadmap
literature/                            bibliography manifest and RAG workflow
paper_forecast-optimal-smoothing/      active paper
paper_penalized-trend-tutorial/        tutorial companion
experiments/                           reproducible experiments using the library
paper/                                 legacy S&P 500 manuscript assets
legacy/                                older historical snapshots
```

## Research-workspace policy

The current repository is a maintainer-controlled research workspace. The current `main` branch may be reorganized, renamed, or refactored when that improves the research program. Old directory structure is not treated as an API contract. Scientific provenance is preserved through Git history and the existing archive material rather than by freezing current source layout.

## Status

Implemented:

- finite-difference operators;
- pure penalized smoother;
- Guerrero (2007) plug-in estimator plus an explicitly named historical iterated-drift variant;
- spectral solution machinery;
- analytic first and second \(\lambda\)-derivatives for the pure smoother;
- train/validation selectors;
- rolling-origin split generation;
- log-\(\lambda\) optimization utilities;
- multiple-local-minimum diagnostics;
- forecasting/extrapolation helpers;
- benchmark models, metrics, plotting, synthetic datasets, and tests.

Immediate work for the active paper:

1. implement the differentiable forecast-loss objective;
2. implement bracketed stationary-point search in log-\(\lambda\);
3. verify both against finite differences and synthetic functions;
4. formalize rolling-origin/nested temporal selection;
5. run controlled simulations;
6. move from macroeconomic series to index/ETF, equity, and crypto data;
7. study how optimal smoothness and forecast skill vary by horizon, window, and regime;
8. add formal forecast-comparison inference and robustness checks.

The canonical detailed plan is `notes/roadmap.md`.
