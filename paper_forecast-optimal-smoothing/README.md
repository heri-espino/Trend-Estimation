# Forecast-Optimal Trend Smoothing

This is the **active** research manuscript.

Working title:

**Adaptive Forecast-Optimal Trend Estimation under Changing Time-Series Regimes**

The manuscript must consume reusable functionality from the installed `trend_estimation` package. Do not place reusable estimators, derivative code, optimizers, or validation logic inside this directory.

## Canonical research objective

> **Forecast-optimal trend estimation as an adaptive forecasting method, where
> smoothness, memory length and difference order depend on horizon and local
> regime.**

Formally,

[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
]

The paper asks both whether the full forecast-optimal configuration changes
systematically with horizon/local state and whether adapting it improves
untouched out-of-sample forecasts relative to strong fixed methods.

The persistence/AR(1) experiment is one **mechanism study** explaining part of
the behavior of (S^\star). It is not the research objective and persistence
must not be used as a synonym for local regime.

## Internal sources

Before editing the paper, read:

- `../notes/research_objective.md` — first scientific source of truth;
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
