# Exploration 02 — Persistence/Horizon Mechanism

## Relationship to the active paper

This is a **Level-II mechanism study**, not the central research objective.

The active paper studies forecast-optimal trend estimation as an adaptive
forecasting method,

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

This experiment isolates one mechanism inside that object: how serial
persistence and horizon affect the smoothness coordinate when residual
dynamics are or are not modeled. Persistence is not synonymous with local
regime, and the oracle AR-aware forecast is not the proposed real-data method.

Canonical objective: \`notes/research_objective.md\`.

## Why this experiment exists

The first paper-scale factorial run showed that the gap between forecast-optimal
and recovery-optimal smoothness is small when observation noise is
uncorrelated, but can become very large when the observation disturbance is
persistent.

The proposed mechanism is:

\[
y_t=\tau_t+\varepsilon_t,
\qquad
\varepsilon_t=\phi\varepsilon_{t-1}+u_t.
\]

When \(\phi\) is large, the residual component is not useless for forecasting
the next observed value. A trend-only forecast may therefore retain some
persistent residual structure by selecting less smoothing.

This experiment tests that explanation directly.

## Controlled factors

Hold fixed:

\[
\sigma_{\rm slope}=0.01,
\qquad
\sigma_{\varepsilon}=0.5.
\]

Explore:

\[
\phi\in
\{-0.8,-0.4,0,0.2,0.4,0.6,0.8,0.9,0.95\}
\]

and

\[
h\in\{1,2,3,6,12\}.
\]

The exploration preset uses 30 seeds.

Negative \(\phi\) is included as a contrast: if the phenomenon is genuinely
about serial dependence and forecast horizon, the sign structure should matter.

## Four lambda objectives

At each outer origin, the ordinary observed-series nested selector chooses
\(d\) and \(L\). Then, conditional on exactly that same \(d\), \(L\), and set of
inner origins, lambda is re-optimized under four objectives.

### Observed-series forecast

The feasible objective used in real-data forecasting.

### Oracle latent-trend forecast

The model still fits the observed series, but inner future predictions are
scored against the known latent trend.

### Oracle AR-residual-aware forecast

The true simulation \(\phi\) is used to forecast the final fitted residual:

\[
\widehat\varepsilon_{T+k|T}
=
\phi^k
\left(y_T-\widehat\tau_T\right).
\]

The full forecast is

\[
\widehat y_{T+k|T}
=
\widehat\tau_{T+k|T}
+
\widehat\varepsilon_{T+k|T}.
\]

Because \(\phi\) is treated as known, this diagnostic remains affine in the
fitted trend and retains analytic lambda derivatives.

This is an oracle mechanism test, not the proposed real-data model.

### Oracle recovery

On the same rolling training windows, lambda minimizes recovery MSE against the
known latent trend.

## Main hypothesis

If the low-smoothness effect at high positive persistence is partly caused by
the trend-only model absorbing predictable residual dynamics, then

\[
S^\star_{\rm observed}
<
S^\star_{\rm latent}
\]

and

\[
S^\star_{\rm observed}
<
S^\star_{\rm recovery}
\]

should be strongest at short horizons and large positive \(\phi\).

After explicitly forecasting the persistent residual, we expect

\[
S^\star_{\rm AR}
\]

to move toward the latent/recovery optima.

The gaps should also shrink with \(h\), broadly consistent with the decay of
the residual contribution as \(\phi^h\).

## Commands

Smoke test:

~~~bash
python experiments/forecast_optimal_smoothing/run_persistence_mechanism.py --preset smoke
~~~

Exploration:

~~~bash
python experiments/forecast_optimal_smoothing/run_persistence_mechanism.py --preset explore
~~~

Results are written automatically under `results/forecast_optimal_smoothing/`.

## What comes after this

Do not immediately increase the original factorial grid. First determine whether
the persistence effect is explained by this decomposition.

If the mechanism is supported, the next exploration should be a within-series
regime-transition experiment asking how quickly selected smoothness adapts when
\(\phi\), noise scale, or trend roughness changes.

A separate signal-to-noise/roughness interaction experiment should follow.

Only after those exploratory studies should the final large simulation design
be frozen.
