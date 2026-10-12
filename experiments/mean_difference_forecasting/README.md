# New paper — nonzero difference-mean forecasting experiments

**Separate from the already-running \`formal8h\` CUDA simulation.**
The earlier source, methods, manifests and SQLite remain untouched.

## First mathematical/causal preflight (CPU, deliberately small)

~~~powershell
conda activate trend-estimation
git pull --ff-only origin main
python -m pytest tests/test_mean_difference_forecast_cv.py tests/test_mean_difference_pilot.py -q
python -m experiments.mean_difference_forecasting.run_pilot --dry-run
~~~

If these pass, start a small independent pilot:

~~~powershell
python -m experiments.mean_difference_forecasting.run_pilot --seeds 5 --max-cells 6 --orders 1,2,3 --horizons 1,3,6 --grid-points 41
~~~

This creates \`results/mean_difference_forecasting/pilot_v1.csv\` and
a matching \`.manifest.json\`. Repeating the SAME command
adds only missing row keys (but computes a candidate replication
again if the session was interrupted mid-task). A changed
design needs a NEW \`--output\` path.

## Fair comparison

Within each independently generated scenario/seed and outer
forecast origin T:
- Use only \`observed[:T]\` for nested/rolling historical selection.
- Fix \`d,L,h\`, the S grid, completed origins and loss weights.
- Compare \`zero\` (μ=0), \`guerrero\` (mean D x per training
  window), and \`profile\` (one analytically optimized μ(S)
  shared over weighted completed folds).
- Add \`naive\`, \`drift\`, \`seasonal_naive\`, \`linear_ols\`.
  These don't have S, λ or EDF, so those columns are BLANK.
- Score observed future y, true latent future τ, conditional
  τ+seasonal and past latent trend recovery separately.
- Save diagnostic μ_true_history from SIMULATED tau only
  after selection, not as a predictor.
- Aggregate error differences by **independent seed within
  DGP cell**, not by overlapping outer lead.
- Identify if profile μ(S) ceases to be identifiable;
  do not claim the old S normalization gives the EDF of
  the CV-optimized two-parameter selector.

Study B with N=360 and Gaussian σ=.25/.5/1 has the SAME latent
shape for all 3 noise levels; produce true/observed/fitted/
forecast plots only AFTER results exist. The pilot is
methodology validation, not publication evidence.

## Future CUDA implementation

The new affine mean loading \`b(S)\` is **independent of
simulation replicate and rolling origin** at fixed L,d,h,S.
This admits batched spectral loss evaluation on CUDA,
followed by analytical reductions for A,C,B and μ*(S)
before selecting S. However, this **has not yet been
implemented or benchmarked** for the NEW model.
Reuse the 32-CPU/one-GPU design after a CPU reference
test; never modify old \`mu=0\` campaign artifacts.
