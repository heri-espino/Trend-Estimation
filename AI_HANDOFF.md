# AI Handoff

This repository is `Trend-Estimation`.

## Repository role

Treat the repository as a **shared research library**, not as a single-paper repository. Reusable estimators, mathematical operators, validation schemes, optimizers, simulations, metrics, and plotting belong under `src/trend_estimation/` or other reusable library modules. Individual papers should consume that library rather than copy estimator logic.

The maintainer has explicitly allowed the current repository layout to be changed freely when useful. Do not preserve an obsolete directory structure merely because it existed before. Git history and `legacy/` provide provenance.

## Active paper only

Current work is focused on:

`paper_forecast-optimal-smoothing/`

Working title:

**Forecast-Optimal Trend Smoothing under Changing Time-Series Regimes**

The current scientific question is whether forecast-optimal smoothness changes systematically with:

- forecast horizon \(h\);
- estimation-window length \(L\);
- local volatility;
- serial dependence/persistence;
- signal-to-noise structure;
- structural breaks/regimes;
- series class and observation frequency.

Planned data progression:

\[
\text{macro}
\rightarrow
\text{indices/ETFs}
\rightarrow
\text{equities}
\rightarrow
\text{crypto}.
\]

The decision-aware/portfolio project is paused. Do not add portfolio objectives, trading rules, or `lambda_decision` experiments unless the maintainer explicitly reactivates that work.

## Canonical analytic model for current derivations

Use the pure quadratic finite-difference smoother:

\[
\widehat t_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}y.
\]

Let \(Q=D_d^\top D_d\) and \(S_\lambda=(I+\lambda Q)^{-1}\). Then

\[
S_\lambda'=-S_\lambda Q S_\lambda,
\]

\[
\widehat t_\lambda'=-S_\lambda Q\widehat t_\lambda,
\qquad
\widehat t_\lambda''=2S_\lambda Q S_\lambda Q\widehat t_\lambda.
\]

Implementation:

- `src/trend_estimation/core/pure.py`
- `src/trend_estimation/core/derivatives.py`
- `src/trend_estimation/models/pure_penalized.py`

## Forecast-loss derivative

For an origin \(T\), horizon \(h\), and a linear forecast operator \(H\),

\[
r_T(\lambda)
=
y_{T+1:T+h}
-
H S_\lambda y_{\mathrm{past}}.
\]

Then

\[
r_T'
=
H S_\lambda Q S_\lambda y_{\mathrm{past}},
\]

\[
f_T'(\lambda)
=
\frac{2}{h}
r_T^\top H S_\lambda Q S_\lambda y_{\mathrm{past}},
\]

and

\[
f_T''(\lambda)
=
\frac{2}{h}
\left[
\|H S_\lambda Q S_\lambda y_{\mathrm{past}}\|_2^2
-
2r_T^\top H S_\lambda Q S_\lambda Q S_\lambda y_{\mathrm{past}}
\right].
\]

The full derivation is canonical in `notes/derivative.md`. If code and the note disagree, resolve the discrepancy explicitly; do not silently change the mathematics.

## Numerical search

Prefer \(\theta=\log\lambda\). If \(g(\theta)=f(e^\theta)\),

\[
g'(\theta)=\lambda f'(\lambda),
\qquad
g''(\theta)=\lambda f'(\lambda)+\lambda^2f''(\lambda).
\]

The intended robust search is:

1. scan a coarse grid in \(\theta\);
2. bracket sign changes in \(g'\);
3. solve each bracket with Brent's root method;
4. classify stationary points;
5. evaluate every local minimum plus the search boundaries;
6. retain the global minimum on the stated bounded domain.

Newton is a benchmark/refinement, not the only search method.

## Validation invariant

For financial/economic forecasting, at origin \(T\), no observation after \(T\) may affect the fitted trend or hyperparameter selection used to predict that future block.

Use `rolling_origin_splits` and eventually nested rolling-origin evaluation for tuning \((d,L,\lambda)\).

Random internal masking belongs to smoothing/reconstruction experiments, not to the main forecasting claim.

## Guerrero model definition

The Guerrero (2007) source has now been checked directly. Its feasible estimator uses

\[
\widehat m_y=(N-d)^{-1}\mathbf1^\top D_dy
\]

computed from the observed differenced series and plugs that value into the penalized estimator. The canonical `GuerreroTrend` now implements this as `drift_mode="data"`.

The previous repository algorithm that re-estimated drift from the fitted trend is preserved explicitly as `IteratedDriftTrend` / `drift_mode="iterated"`. Do not call that historical variant Guerrero (2007) equation (18).

See `notes/model_definitions.md`.

## Notes are canonical internal documentation

Before changing the active research direction, read:

- `notes/key_results.md`
- `notes/derivative.md`
- `notes/numerical_selection.md`
- `notes/model_definitions.md`
- `notes/roadmap.md`

Every new nontrivial result should be added to `notes/key_results.md` and receive a detailed note when derivation or interpretation matters.

## Papers

- `paper_forecast-optimal-smoothing/`: active paper.
- `paper_penalized-trend-tutorial/`: tutorial companion, secondary.
- `paper/`: legacy S&P 500 manuscript assets, not canonical.

Paper scripts should import the installed `trend_estimation` package. Do not put reusable estimator mathematics inside paper folders.

## Testing priorities

Before trusting a numerical result:

1. run the full test suite;
2. compare analytic derivatives against centered finite differences;
3. verify forecast-origin chronology;
4. compare root-based search against a dense diagnostic grid on synthetic cases;
5. report the exact bounded log-\(\lambda\) search domain;
6. distinguish level forecasting from return/direction forecasting;
7. compare price forecasts against a random-walk/no-change benchmark.

## Canonical roadmap

`notes/roadmap.md` is the authoritative record of what has been done, what is next, and why.


## Window-length/smoothness invariant

Normalized smoothness depends on fitted sample size \(N\). A common raw \(\lambda\) across expanding origins therefore does not imply a common smoothness level.

For the active object \(S^\star_{T,h,L}\), prefer fixed-width inner windows when optimizing one common \(\lambda\) for a candidate \(L\). The helper `select_fixed_window_pure_smoothness` implements this design.

See `notes/window_and_smoothness.md`.
