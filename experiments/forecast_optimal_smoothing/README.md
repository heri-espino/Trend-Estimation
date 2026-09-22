# Forecast-optimal smoothing experiments

This directory contains reproducible experiment entry points for the active
paper. Reusable estimators, derivatives, selectors, datasets, and validation
logic must remain in the installed `trend_estimation` library.

## First controlled simulation grid

`run_simulation_grid.py` studies a local-linear latent trend with AR(1)
observation noise while varying three stochastic ingredients independently:

- latent-trend roughness through slope innovation standard deviation;
- observation-noise scale;
- observation-noise serial dependence through AR(1) phi.

It also varies forecast horizon.

At every outer origin the script:

1. uses only history available at that origin;
2. selects order, window length, and forecast-optimal lambda with nested
   chronological validation;
3. forecasts the untouched future block;
4. compares against a no-change benchmark;
5. uses the known simulated latent trend to compute an oracle
   recovery-optimal lambda on the same selected order/window;
6. stores both normalized smoothness values.

This directly creates the diagnostic

[
S^star_{mathrm{forecast}}
-
S^star_{mathrm{recovery}},
]

which is only observable in simulation.

## Smoke test

After pulling the latest code, use this first. It runs only two configurations and is intended to verify that the full nested pipeline works end to end:

~~~bash
conda activate trend-estimation
pip install -e .
python experiments/forecast_optimal_smoothing/run_simulation_grid.py --preset smoke
~~~

## Quick experiment

The quick preset runs 32 configurations:

~~~bash
python experiments/forecast_optimal_smoothing/run_simulation_grid.py --preset quick
~~~

## Paper-scale grid

~~~bash
python experiments/forecast_optimal_smoothing/run_simulation_grid.py --preset paper
~~~

The paper preset is intentionally computationally expensive. It is not run by
push-triggered GitHub Actions. Outputs are written under `outputs/` and are
ignored by Git; final figures/tables should be generated from explicit scripts
after the experiment design is frozen.

## Interpretation warning

The oracle recovery optimum uses the true latent trend and therefore is not a
real-data tuning method. It exists to answer a scientific question in
simulation: whether the amount of smoothing that best reconstructs the latent
trend is the same as the amount that best forecasts future observations.


## Versioned result capture

By default every run now writes a self-contained, Git-trackable directory:

```text
results/forecast_optimal_smoothing/<timestamp>_<preset>_<git-sha>/
├── simulation_grid.csv
├── summary.csv
└── run_metadata.json
```

The metadata records the exact Git commit, preset, grid, horizons, windows,
orders, numerical search bounds, row count, and elapsed time. This makes a run
auditable and lets collaborators analyze results directly from GitHub.

The older `experiments/forecast_optimal_smoothing/outputs/` path remains
ignored and should be treated as scratch space.


## Persistence/horizon mechanism study

After the first factorial run, the next experiment isolates the mechanism behind
the strong persistence effect. It compares four smoothness objectives
conditional on the same selected order and window:

- observed-series forecast optimum;
- oracle latent-trend forecast optimum;
- oracle AR-residual-aware forecast optimum using the known simulation phi;
- oracle latent-trend recovery optimum.

Smoke test:

~~~bash
python experiments/forecast_optimal_smoothing/run_persistence_mechanism.py --preset smoke
~~~

Exploration run:

~~~bash
python experiments/forecast_optimal_smoothing/run_persistence_mechanism.py --preset explore
~~~

The exploration uses 30 seeds, nine AR(1) coefficients (including negative
values), and five forecast horizons. Results are versioned automatically under
`results/forecast_optimal_smoothing/`.
