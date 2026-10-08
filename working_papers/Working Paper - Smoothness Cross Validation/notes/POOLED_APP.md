# Pooled Forecast-CV Streamlit Lab

**New, separate app:** [../../../apps/pooled_forecast_cv.py](../../../apps/pooled_forecast_cv.py)

Existing \`apps/smoothness_lab.py\`, \`apps/smoothness_lab_advanced.py\`
and the historical branch-tracking dashboard are **not modified**.

## Launch

From the repository root on Windows PowerShell:

~~~powershell
git pull --ff-only
python -m pip install -e ".[dashboard,finance]"
streamlit run apps/pooled_forecast_cv.py
~~~

On macOS/Linux, run the same Python/Streamlit commands in a shell with an
active environment. You may also run it without Yahoo Finance data using
the synthetic or CSV sources.

This is an exploratory app, not a frozen paper experiment.

## What this app computes

At an outer origin \`T\` with only the first \`T\` observations available,
a rolling fold ending at \`t\` uses the most recent \`L\` observations to
estimate a pure order-\`d\` penalized least-squares trend:

\[
\widehat \tau_t(S)=H(S)y_{t-L+1:t},\quad
H(S)=(I+\lambda(S)D_d^\top D_d)^{-1}.
\]

The future forecast for the next \`h\` observations is the fitted
polynomial continuation \(G_{d,h}\widehat\tau_t(S)\).

For each **historically completed** validation block \(t_m+h\le T\):

\[
F_{t_m}(S)=h^{-1}
\|y_{t_m+1:t_m+h}-G_{d,h}H(S)y_{t_m-L+1:t_m}\|^2.
\]

The main pooled objective is the **equal-weight average of all per-fold
curves**, not an average of their minimizing values:

\[
F_{\rm pool}(S)=M^{-1}\sum_{m=1}^{M}F_{t_m}(S),\qquad
\widehat S_{\rm pooled}\in\arg\min_{S\in[0,1]} F_{\rm pool}(S).
\]

Then refit on the latest \(L\)-observation window ending at \(T\), forecast
the next \(h\) points, and (if enabled) score on an **untouched outer
holdout**. There is no branch tracking or \(\phi(V_j)\) decision policy.

## Adjustable controls

| Group | Adjustable inputs |
| --- | --- |
| Data | Synthetic function formula, series length, noise distribution, noise standard deviation, AR(1) correlation, seed |
| External data | Yahoo Finance ticker, frequency, historical period, field; numeric CSV column and optional date |
| Data representation | Original levels, logs, index base 100, simple/log returns |
| Trend model | Difference order \(d\in\{1,2,3,4\}\), training window \(L\), horizon \(h\) |
| Rolling CV | Fold stride \(\Delta\), number of most recent completed folds \(M\), optional full \(h\)-block outer holdout |
| Optimization | \(S\)-grid density, optional local valley refinement; exact \(S=0\) and \(S=1\) checks |
| Comparisons | Last-fold minimum, optional \(h=1\) pooled CV on the same origins, freely chosen manual \(S\) for visual sensitivity |

Fold spacing \(\Delta\) counts **observations**. If daily financial observations
have gaps for weekends/holidays, \(\Delta=5\) means five *data rows*,
not necessarily five calendar days. If \(\Delta<h\), validation target
blocks overlap and their errors are dependent. The original statistical
criterion uses equal weighting across the selected folds; changing
\(\Delta\) or \(M\) changes the validation protocol.

**Chronology:** The fold endpoints are anchored at the most recent completed
\(h\)-step validation block, and older origins are spaced backward by
\(\Delta\). When an outer holdout is requested, the latest \(h\) observations
are removed from all fitting/CV computations until outer scoring.

## Views

1. **Final trend & forecast:** observed series, separate fitted PLS trends,
   polynomial forecasts, last-origin and optional one-step selectors, manual
   \(S\), and actual holdout test values/MSE when available.
2. **All F curves & pooled F:** every historical \(F_{t_m}(S)\), pooled
   curve, selected minima, and the fold × fixed \(S\) loss heatmap.
   Per-fold displayed minima are grid estimates, **not tracked branches**.
3. **Folds & historical predictions:** exact training/validation positions,
   selected fold forecasts against their *now-observed* outcomes, and split table.
4. **Smoothness mathematics:** penalty eigenshrinkage, normalized smoothness
   and effective degrees of freedom, optional full smoothing matrix heatmap,
   and resolvent derivatives.
5. **Data & downloads:** input series and source-specific information;
   export complete loss matrix, all loss curves, fold minima summary,
   fitted forecasts and outer truth (when available), and JSON configuration.

## Accuracy and limitations

The app reuses the library's cached spectral PLS solver and
\`prepare_rolling_pure_forecast_objective\`, thereby avoiding repeated dense
matrix inversions. It searches a finite \(S\) grid and optionally refines
sampled valleys with bounded scalar minimization, always comparing exact
endpoints. This is a fast visualization/numerical *approximation*, **not a
certified all-roots or globally complete minimizer**. Narrow minima may be
missed at low grid resolution; increase the grid and compare results.

The one-step comparator uses the same origins as the \(h\)-step validation
curve, but tunes \(S\) with one-step loss, then uses that \(S\) for the actual
\(h\)-step future forecast.

All loss values measure forecast error of **observed values** in the
transformed units squared, not latent-trend oracle error. The synthetic
latent curve is visualization-only and is never used to choose \(S\).
A single outer holdout is an illustrative test, not a conclusive measure
of forecasting superiority.

## Tests

~~~bash
python -m pytest tests/test_pooled_forecast_cv_lab.py -q
~~~

The tests check pooling, fold spacing, spectral consistency with the
existing forecast objective, untouched-holdout invariance, native
polynomial continuation, exports, and input validation.


## UI smoke validation

CI also compiles the Streamlit source and attempts an offline
Streamlit AppTest render using the default synthetic example:

~~~bash
python -m pytest tests/test_pooled_forecast_cv_app.py -q
~~~

This test does **not** require Yahoo Finance access.
