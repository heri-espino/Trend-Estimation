# Forecast-Optimal Trend Smoothing

This is the **active** research manuscript.

Working title:

**Forecast-Optimal Trend Smoothing under Changing Time-Series Regimes**

The manuscript must consume reusable functionality from the installed `trend_estimation` package. Do not place reusable estimators, derivative code, optimizers, or validation logic inside this directory.

## Current research question

How do forecast-optimal smoothness, window length, and difference order vary with forecast horizon and local stochastic regime, and does adaptive selection provide out-of-sample skill across macroeconomic, equity, and crypto series?

## Internal sources

Before editing the paper, read:

- `../notes/key_results.md`
- `../notes/derivative.md`
- `../notes/numerical_selection.md`
- `../notes/model_definitions.md`
- `../notes/roadmap.md`

Literature metadata lives in `../literature/`.

## Build

From the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -outdir=paper_forecast-optimal-smoothing/build paper_forecast-optimal-smoothing/main.tex
```

The paper is currently a research skeleton. Do not write strong novelty or performance claims until the literature audit and planned experiments in `notes/roadmap.md` are complete.
