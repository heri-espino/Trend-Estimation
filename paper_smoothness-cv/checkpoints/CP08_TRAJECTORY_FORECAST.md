# Checkpoint 08 — Forecast the tracked smoothness trajectory

**Status: FROZEN DEVELOPMENT DESIGN BEFORE RUN.**

CP07 showed that backward-looking recency averaging stabilizes the newest
tracked minimum but does not beat pooled forecast-CV. CP08 tests the forward-
looking extension that motivated the branch-matrix formulation: predict the
next smoothness value from the selected branch trajectory.

CP08 is a **development** experiment. It uses fresh simulation seeds
`100..199`. Seeds `200..399` are reserved for a later one-shot confirmation
after one trajectory rule is frozen.

## Fixed forecasting environment

- `d = 2`;
- `L = 120`;
- horizon `h = 20`;
- 8 non-overlapping outer tests;
- 30 historical paired Val1/Val2 origins;
- `track_epsilon = 0.10`;
- `candidate_spacing = 0.02`;
- at most 5 initial local-minimum branches;
- branch selection by persistence plus historical Val2 log-RMSE;
- same six roughness mechanisms and two observation-noise levels as CP07.

Thus the only new object is the branch-to-smoothness functional `phi`.

## Candidate forward-looking rules

Let the selected branch values, including the current final-Val1 minimum, be

\[
S_1,\ldots,S_T.
\]

CP08 compares:

1. `linear_k3`: OLS line through the last 3 branch values, extrapolated one
   branch step;
2. `linear_k5`: same using the last 5;
3. `linear_k10`: same using the last 10;
4. `ew_linear_hl3`: exponentially weighted linear trend using all available
   branch values with half-life 3;
5. `ew_linear_hl5`: same with half-life 5;
6. `delta_hl3`: current S plus an exponentially weighted mean of historical
   branch increments, half-life 3;
7. `delta_hl5`: same with half-life 5.

All extrapolated values are clipped to `[0,1]`. The raw un-clipped value and
whether clipping occurred are saved for diagnostics.

Baselines are:

- `recency_hl3` from CP04--CP07;
- `last`;
- `pooled_cv_same_config`.

## Development decision rule

The candidate trajectory rule with the smallest geometric observed-log-RMSE
ratio relative to pooled CV over the **changing-roughness mechanisms** is the
development winner.

Ties or nearly equal rules are resolved conservatively by, in order:

1. lower clipping rate;
2. better stationary-mechanism ratio;
3. simpler rule / shorter specification.

No trajectory rule is declared confirmed from CP08.

## Confirmation boundary

After CP08 is observed, exactly one trajectory rule may be frozen. The
confirmation experiment must use seeds `200..399` and may compare only that
frozen trajectory rule with `recency_hl3`, `last`, and pooled CV.

Do not use seeds `200..399` during CP08 development.
