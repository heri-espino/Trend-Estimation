# Working Paper — Smoothness Cross-Validation

**Working title:** *Horizon-Matched Cross-Validation for Forecast-Optimal Penalized Trend Smoothness*.

**Status:** active independent statistical-methodology working paper. **Intended journal:** *Communications in Statistics—Simulation and Computation*. The manuscript is an interim working draft, **not submission-ready**.

## Current protocol: weighted historical F, then its global minimum

**Prospective method (2026-10-08):** the original equal-weight
pooled rolling-origin forecast-CV remains the primary baseline.
We additionally examine **predeclared recency-weighted aggregates**
of the same completed \(h\)-step forecast-loss functions:
uniform recent window, linear recency, and exponential recency.

For method \(m\), the latest fully completed weighted surface is

\[
F_M^{(m,d,L,h)}(S)
=\frac{\sum_{q\in I_m(M)} w_{M,q}^{(m)}
\ell_{t_q}^{(d,L,h)}(S)}
{\sum_{q\in I_m(M)}w_{M,q}^{(m)}},\quad
\widehat S_T^{(m)}\in\arg\min_{S\in[0,1]}F_M^{(m,d,L,h)}(S).
\]

**Paper 1 averages forecast-loss functions and then chooses their
global minimum.** It does not track local minima across historical
surfaces; it does not average their individual minimizing S values.
The historical future blocks have already completed at selection
time. After selection, refit on the newest window at \(T\) and
forecast at the declared horizon \(h\).

The dynamic Paper 2 uses the **same predeclared weighted surfaces**,
but tracks their local minima instead of globally minimizing the
latest one. That shared estimator/validation infrastructure does
not make these two scientific questions the same.

- [Shared prospective formulation](../WEIGHTED_SURFACE_PROTOCOL.md).
- [Manual runnable comparison of both procedures](../../experiments/smoothness_cv/run_weighted_surface_study.py).

The existing CP01–CP03 results refer to the *historical* uniform
mean protocol; no recency-weighted experiment has been declared
completed. The current LaTeX manuscript is a dated working draft.

## Research question

For fixed difference order \(d\), fitting length \(L\), and operational horizon \(h\), select normalized PLS smoothness \(S\in[0,1]\) by minimizing historical *future-block* forecast MSE:

\[
\widehat S_T\in\operatorname*{arg\,min}_{S\in[0,1]}
\frac1{Mh}\sum_{m=1}^M
\|z_{t_m}-G_{d,h}H(S)x_{t_m}\|^2,
\qquad t_m+h\le T.
\]

The selected \(S\) is used to **refit** the latest \(L\)-observation window and forecast the genuinely unknown future. The pooled loss is the average of individual forecast-loss curves, not the average of their minimizing \(S\) values. There is **no tracking of minima across origins** in this procedure.

## Structure

- [Standalone working manuscript](manuscript/main.tex), including the spectral derivations, kernel/nullity, positive definiteness, exact \(S=1\) projection, existence, and forecast-MSE objective.
- [Research notes](notes/INDEX.md), the current source of truth during method development.
- [Original pooled checkpoints CP01–CP03](checkpoints/), retained as historical results.
- [Pooled Streamlit laboratory](../../apps/pooled_forecast_cv.py) and [app guide](notes/POOLED_APP.md).
- [Literature audit](LITERATURE_AUDIT_2026-10.md).

The frozen CP03 study completed 3,000 scenarios and 72,000 outer-origin/horizon decisions. Its geometric forecast-RMSFE ratios relative to one-step CV at horizons 3, 6, 12 were 0.947, 0.861, and 0.762; new numerical designs and experiments must not be described as completed.

## Reproducible preflight and build

From the **repository root**:

~~~bash
python -m pip install -e ".[dashboard,finance]"
streamlit run apps/pooled_forecast_cv.py
python "working_papers/Working Paper - Smoothness Cross Validation/build.py" --check
python "working_papers/Working Paper - Smoothness Cross Validation/build.py"
~~~

LaTeX/PDF builds are manual. Full-range smoothness \(S=1\) uses the exact null-space projection, not a numerical \(1-\varepsilon\) surrogate.
