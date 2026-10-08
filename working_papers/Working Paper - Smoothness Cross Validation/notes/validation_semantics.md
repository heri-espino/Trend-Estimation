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

## Code mapping

These code mappings describe the older implementation's intended information flow; verify exact function signatures after changing the solver. The chronology and mandatory final refit remain invariant.

- `forecast_cv_curve(history, ...)` uses only `history = y[:origin]` and returns the validation-loss curve over candidate \(S\).
- `grid_argmin(...)` converts that curve into the selected smoothness \(\widehat S_{T,h}\).
- `y_window = history[-window:]` constructs the most recent \(L\)-observation window available at the outer origin.
- `fit_and_forecast(y_window, smoothness=selected_s, ...)` performs the fresh post-selection refit and then extrapolates.
- `observed_future = y[origin:origin+horizon]` is passed only to outer scoring.

Any future refactor must preserve these semantics.

## Dynamic branch extension

The same information rule applies when `S` is selected from a tracked branch.
At historical origin `t`, a local minimum produces a Validation-1 loss.
After that minimum is identified, the model is refit through Validation 1
and forecasts the immediately following Validation-2 block. This produces
the row

\[
(S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t})
\]

stored in branch matrix `V_j`.

At the outer forecast origin `T`, `psi` may use only historical branch rows
and `phi(V_j)` may use only smoothness/loss information already observed.
Once `S_hat_T` is produced, a fresh final refit on `y[T-L+1:T]` is mandatory.

A recent-mean or weighted `phi` rule averages **smoothness values**. It does
not average historical trend estimates.
