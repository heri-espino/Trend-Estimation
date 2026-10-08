> **2026-10-08 clarification:** “Using future data” means using the *later outcomes of older historical forecast origins*, which are already observed by the current origin. We cannot see (y_{T+1:T+h}) while choosing today's smoothness. This remains the central information boundary of the evolving method. Full derivations: [mathematical_foundations.md](mathematical_foundations.md).

---

# Validation semantics — what forecast-CV selects and what is refit

**Canonical rule for every agent working on the smoothness-CV paper.**

This note defines the training/validation/test semantics. Do not reinterpret forecast-CV as selecting one of the intermediate fitted trends.

## Core distinction

Forecast-CV selects the **smoothness hyperparameter** \(S\), not a historical trend fit.

At an outer forecast origin \(T\), only

\[
y_{1:T}
\]

is available. For each candidate \(S\), inner chronological forecast splits are constructed strictly inside that history. If the retained fitting window has length \(L\), an inner split ending at origin \(t<T\) fits

\[
y_{t-L+1:t}
\]

and scores the resulting forecast against the following historical validation block

\[
y_{t+1:t+h}.
\]

The inner losses are averaged:

\[
F_{T,h}(S)
=
\frac{1}{M}
\sum_{m=1}^{M}
\operatorname{Loss}_{m,h}(S).
\]

Then

\[
\widehat S_{T,h}
\in
\arg\min_{S\in[0,1]} F_{T,h}(S).
\]

The intermediate trends fitted inside the \(M\) validation folds are used only to evaluate candidate values of \(S\). They are discarded after the selection step. We do **not** select the trend from the final validation fold, and we do **not** average fold-specific trends.

## Mandatory refit before the outer test

After \(\widehat S_{T,h}\) has been selected, the estimator is refit using the most recent information available at the outer origin:

\[
x_T
=
y_{T-L+1:T},
\]

\[
\widehat\tau_T
=
H_{\lambda(\widehat S_{T,h})}x_T.
\]

The actual outer forecast is then

\[
\widehat y_{T+1:T+h\mid T}
=
G_{d,h}\widehat\tau_T.
\]

Only after this forecast has been formed is the untouched outer block

\[
y_{T+1:T+h}
\]

revealed for test scoring.

Therefore the operational sequence is

\[
\boxed{
\text{historical rolling validation}
\rightarrow
\text{select }S
\rightarrow
\text{refit on the final }L\text{-window available at }T
\rightarrow
\text{forecast untouched future}
}
\]

This refit is essential. Keeping the fit from an earlier validation fold would discard information that is already available at forecast time and would not represent the intended forecasting procedure.

## What is averaged

Forecast-CV averages **validation forecast losses**, not trends:

\[
\frac{1}{M}\sum_m \operatorname{Loss}_{m,h}(S).
\]

The average loss estimates how a candidate smoothness value has behaved across historical pseudo-out-of-sample forecast origins. It is a criterion for choosing \(S\), not an ensemble forecast.

## Rolling outer evaluation

At the next outer origin \(T'>T\), observations that were previously in an outer test block are now historical information. They may therefore be used in the next tuning/refit cycle.

Thus every outer origin repeats:

\[
\text{history through }T
\rightarrow
\widehat S_{T,h}
\rightarrow
\text{refit through }T
\rightarrow
\text{forecast}
\rightarrow
\text{score},
\]

then moves forward in time and repeats with the enlarged history.

This is the intended rolling pseudo-out-of-sample experiment.

## Information boundary

- observations after \(T\) must not affect the inner CV criterion;
- observations after \(T\) must not affect \(\widehat S_{T,h}\);
- observations after \(T\) must not affect the final refit;
- the outer future block is used only for scoring;
- in simulation, latent future information is visible only to explicitly named oracle diagnostics, never to a feasible selector.

## Classical LOOCV/GCV versus our chronological forecast-CV

**Terminology and originality boundary.** Our procedure is an instance of *time-series cross-validation*, specifically **fixed-window rolling-origin / sliding-window forecast validation** when every inner fitting window has the same length `L`. An expanding-window design is different. Rolling-origin CV, walk-forward evaluation, and horizon-specific predictive tuning already exist; **we are not proposing a novel class of cross-validation**. The research question is the use and numerical/statistical analysis of historical, **horizon-matched future-block forecast MSE** to select normalized finite-difference PLS trend smoothness.

The **Cortés-Toto, Guerrero and Reyes (2017)** comparison of CV, GCV, AICc and BIC concerns *fitted-curve reconstruction / in-sample complexity*, not our declared native `h`-step finite-difference trend continuation. Distinguish:

- **Leave-one-out CV (LOOCV):** for each `i` in turn, omit observation `y_i`, fit with the other `N-1` observations, and assess the omitted-point error. This is **not one random holdout**. In a symmetric smoother, the remaining data can include observations *chronologically after* `i`, so it does not imitate a genuine forecast origin. For the linear zero-drift smoother, `CV(lambda) = sum_i [ (y_i - (H_lambda y)_i) / (1 - H_{lambda,ii}) ]^2` (or its mean), subject to defined denominators.
- **Generalized CV (GCV):** replaces the individual diagonal leverages `H_{lambda,ii}` with their average `tr(H_lambda)/N`: `GCV(lambda) = RSS(lambda) / [1 - edf(lambda)/N]^2`, up to a positive normalization factor independent of `lambda`. This is a reconstruction-oriented shortcut, **not** a forward-chaining method.
- **Our forecast-CV:** at each historical inner origin `t` with `t+h <= T`, fit `x_t = y_{t-L+1:t}` only, predict `z_t = y_{t+1:t+h}` using `G_{d,h} H(S) x_t`, and average `h`-step forecast MSE across eligible inner origins. We do **not** simply remove the last `h` observations *once* from the complete series; there are multiple historical origins. After selecting `S`, **refit** on the current `L` observations and issue an untouched outer forecast.

With the pure smoother and fixed `(L,d,h)`, the proposed objective is

\[
F_{T,d,L,h}^{\mathrm{pool}}(S)
=\frac{1}{Mh}\sum_{m=1}^M
\left\|y_{t_m+1:t_m+h}
-G_{d,h}H(S)y_{t_m-L+1:t_m}\right\|_2^2,
\qquad t_m+h\leq T.
\]

**Potential advantages relative to classical LOOCV/GCV:**

1. Enforces causal information availability at each forecasting origin.
2. Tunes the loss that corresponds to the declared **forecast horizon and continuation rule**, rather than only historical point reconstruction.
3. Can compare short versus long horizons and evaluate time variation of the loss surfaces.
4. Evaluates the **complete smoother + continuation procedure**, not just an in-sample fit.

**Costs, limitations, and cautions:**

1. More computation than closed-form LOOCV/GCV unless shared spectral transforms and loss evaluations are reused.
2. Fewer effective validation occasions, particularly with long training windows or long horizons; unstable minima are possible.
3. Overlapping future validation blocks can produce **dependent errors**; do not treat fold losses as independent replicates or overstate inferential precision.
4. The selected `S` is specific to `(d,L,h,G)` and the validation loss; changing the continuation, horizon, or target can change the optimum.
5. Predicting **future noisy observations** and recovering the **latent trend** are different targets. In simulations, an oracle latent-target score must be labelled separately and must not leak into the feasible selector.
6. Repeatedly exploring methods on the same outer test blocks can create *researcher-side test overfitting* even if the inner CV code is leakage-free; reserve independent evaluation for final claims.

**Appropriate paper wording:** “We investigate horizon-matched rolling-origin forecast-MSE selection of normalized penalized-trend smoothness.” Do **not** claim to invent time-series CV, to prove universal predictive superiority, or to guarantee unique/global minimizer recovery from a practical numerical search.

## Code mapping

These code mappings describe the older implementation's intended information flow; verify exact function signatures after changing the solver. The chronology and mandatory final refit remain invariant.

- `forecast_cv_curve(history, ...)` uses only `history = y[:origin]` and returns the validation-loss curve over candidate \(S\).
- `grid_argmin(...)` converts that curve into the selected smoothness \(\widehat S_{T,h}\).
- `y_window = history[-window:]` constructs the most recent \(L\)-observation window available at the outer origin.
- `fit_and_forecast(y_window, smoothness=selected_s, ...)` performs the fresh post-selection refit and then extrapolates.
- `observed_future = y[origin:origin+horizon]` is passed only to outer scoring.

Any future refactor must preserve these semantics.
