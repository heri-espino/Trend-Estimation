# Exploration 04 — Within-Series Persistence Regime Transition

## Scientific role

This is the first experiment that directly targets the adaptive forecasting
object of the active paper:

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

Explorations 01–03 established target differences, a persistence/horizon
mechanism, and numerical-domain robustness. Exploration 04 asks what happens
when the stochastic regime changes **inside one observed series**.

## First transition factor: persistence

Hold fixed:

\[
\sigma_{\rm slope}=0.01,
\qquad
\sigma_\varepsilon=0.5,
\]

with no level or slope jump.

Use a known regime point

\[
T_0=180
\]

inside a length-300 series.

The experiment compares four paired paths:

| label | pre phi | post phi | role |
|---|---:|---:|---|
| stable_low | 0.0 | 0.0 | low-persistence control |
| low_to_high | 0.0 | 0.8 | upward persistence transition |
| high_to_low | 0.8 | 0.0 | downward persistence transition |
| stable_high | 0.8 | 0.8 | high-persistence control |

For a fixed seed, low_to_high is identical to stable_low before the regime
point, and high_to_low is identical to stable_high before the regime point.
The controls therefore give matched reference paths rather than unrelated
Monte Carlo baselines.

## Forecast design

Explore horizons

\[
h\in\{1,3,6,12\}.
\]

Use 30 seeds, candidate orders {1,2,3}, candidate windows {24,48,72},
outer initial train 120, outer step 3, and inner step 3.

After Exploration 03, the numerical search uses:

\[
\log\lambda\in[-18,24],
\qquad
n_{\rm grid}=321.
\]

At every outer origin, selection remains strictly causal.

## Why T0=180 and n=300

The first outer origin is 120, leaving 60 observations of pre-change outer
evaluation before the regime point and 120 observations after it.

The post-change segment is also longer than the largest candidate window
(72). Therefore the experiment observes the full transition from:

1. windows containing only the old regime;
2. mixed old/new windows;
3. windows containing only the new regime.

For every selected configuration, the output records the fraction of the
selected window that comes from the post-change regime.

## Main path

The primary plot/table object is

\[
T\mapsto
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h}).
\]

The row-level output additionally records:

- selected lambda;
- numerical-search source;
- number of stationary points;
- post-change observations available at the forecast origin;
- old/new composition of the selected window;
- untouched outer block MSE;
- no-change benchmark MSE;
- block relative RMSFE.

## Paired adaptation measure

For low_to_high, stable_low is the start reference and stable_high is the
target reference. For high_to_low, the roles reverse.

At each relative origin k=T-T0, define aggregate smoothness progress:

\[
P_S(k)
=
\frac{
\bar S_{\rm transition}(k)-\bar S_{\rm start}(k)
}{
\bar S_{\rm target}(k)-\bar S_{\rm start}(k)
}.
\]

Thus P_S near 0 means the transition still resembles the old regime, while
P_S near 1 means it resembles the matched target-regime control.

The experiment reports 50% and 80% adaptation delays. A threshold is counted
only when it is reached for three consecutive outer origins, reducing the
effect of one noisy crossing.

The delay unit is the number of post-change observations available to the
selector.

## Full configuration diagnostics

Smoothness progress gives the first scalar adaptation-delay measure, but the
paper's object is not smoothness alone. Therefore paired outputs also track:

- absolute smoothness gap to the target control;
- order match with the target control;
- window match with the target control;
- joint (order, window) match;
- mean selected-window post-regime fraction.

This lets us inspect whether S adapts before or after the discrete coordinates
d and L.

## Outputs

The run writes:

- transition_grid.csv — outer-origin rows;
- path_summary.csv — mean path across seeds by transition/horizon/relative time;
- selection_shares.csv — joint order/window selection frequencies;
- paired_controls.csv — matched transition versus start/target controls;
- adaptation_path.csv — progress and configuration-gap path;
- adaptation_summary.csv — 50%/80% smoothness adaptation delays;
- run_metadata.json.

## Command

From the repository root:

~~~powershell
python experiments\forecast_optimal_smoothing\run_regime_transition.py --preset explore
~~~

A one-seed syntax/runtime check is available with:

~~~powershell
python experiments\forecast_optimal_smoothing\run_regime_transition.py --preset smoke
~~~

## Questions

1. Does low-to-high persistence push the selected method from the low-phi
   control toward the high-phi control after T0?
2. Does the reverse transition adapt symmetrically?
3. How does adaptation delay depend on horizon?
4. Does L shorten immediately after the change, as expected from a
   contamination-versus-variance tradeoff?
5. Does d change systematically or mostly remain a secondary coordinate?
6. Does S adapt before the selected window becomes fully post-regime?
7. How does forecast skill evolve during the mixed-window period?

## Decision after this experiment

If the joint configuration tracks the new regime in a structured way, the
next experiment should test **adaptation value**: adaptive selection versus
strong fixed configurations under the same untouched outer forecasts.

After persistence transitions are understood, repeat the regime-transition
design separately for observation-noise scale and latent-trend roughness.

Do not combine all regime dimensions into one large DGP before the isolated
transition mechanisms are understood.