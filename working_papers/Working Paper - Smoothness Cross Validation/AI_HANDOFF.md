# Paper 1 agent handoff — pooled/weighted horizon-h forecast CV

**Canonical version: 2026-10-09.** Read
[the theoretical charter](../THEORETICAL_CONTRIBUTIONS.md) and
[shared weighted-F protocol](../WEIGHTED_SURFACE_PROTOCOL.md) first.
The old draft \`manuscript/main.tex\` and CP01–CP03 are historical
evidence/draft; new recency-weighted results are **not yet proven**.

## Mathematical definition

Fix **declared** difference order \(d\in\{1,\dots,L-1\}\),
training window \(L\), operational horizon \(h\), historical origin
stride, weight method \(m\) and its parameters. At current origin T,
every historical validation loss must have **completed**:
\(t_q+h\le T\). Let
\[
Q=D_d^\top D_d=U\,\mathrm{diag}(\delta_j)U^\top,\quad
H_\lambda=(I+\lambda Q)^{-1},\quad
S=(L-\operatorname{tr}H_\lambda)/(L-d)\in[0,1].
\]
The spectral trace relationship and Guerrero-type smoothness are
**known**. The parameter \(S\) is a scalar, not \(H\). \(S=1\) is
the exact nullspace projection; use continuation operator
\(G_{d,h}\) (not naive last-point replication). Raw completed
forecast MSE:
\[
\ell_{t_q}^{(d,L,h)}(S)=
\frac1h\|y_{t_q+1:t_q+h}
-G_{d,h}H(S)y_{t_q-L+1:t_q}\|^2.
\]
Then choose
\[
\boxed{\widehat S_T
\in\arg\min_{S\in[0,1]}
\frac{\sum_{q\in I_m(M)}w^{(m)}_{M,q}\ell_{t_q}(S)}
{\sum_{q\in I_m(M)}w^{(m)}_{M,q}}.}
\]
**Aggregate entire functions, then minimize. Do not average the
\(S^*\) of separate folds. Do not perform branch matching.**
\(m\) may be all-origin uniform (the CP03 special case),
last-K uniform, last-K linear, or last-K exponential.

After selection, fit the newest L observed points, forecast exactly
h future observations, and score on a genuinely untouched outer
test. Choosing m/d/L by inspecting that same test contaminates it.
Overlapping rolling losses are correlated.

## Theory agenda

- Prove assumptions and exact endpoint behavior; continuity ensures
  existence of a minimizer but not uniqueness or convexity.
- Characterize dependence of \(F\), its derivatives and optimum
  on declared horizon h, true polynomial degree, effective degrees
  of freedom and temporal loss weighting.
- Compare reconstruction-optimal and forecast-directed smoothness,
  and identify when they differ. Work toward counterexamples and
  qualified propositions rather than merely displaying curves.
- Compare the *integrated horizon-directed decision* against closest
  literature; PLS, eigendecomposition, Guerrero index, rolling CV and
  time-weighted averaging are **not claimed novel individually**.
- Preserve stable/nonstationary failures and compare original
  full-N Cortés-Toto CV/GCV/AICc/BIC experiment separately.

## Implementation and app

- **App:** \`streamlit run apps/pooled_forecast_cv.py\`.
  Includes uniform historical pooled F plus a current weighted-F
  extension with rule and K/decay controls, forecast, loss heatmap,
  spectral H, S/EDF and exports. Does not plot/select branches.
- **Code:** \`experiments/smoothness_cv/pooled_lab.py\`,
  \`experiments/smoothness_cv/weighted_surface_study.py\`
  (shared pilot), \`src/trend_estimation/forecasting/objectives.py\`.
- **Experiment protocol:**
  [SIMULATION_EVALUATION_PROTOCOL.md](../SIMULATION_EVALUATION_PROTOCOL.md).
  528 predeclared factorial DGP cells; results not yet confirmed.
- **GPU:** secondary reproducibility/computation note; the user
  measured a float32 **loss kernel** speedup, not proof of complete
  forecast-selector acceleration. Do not center the paper on CUDA.
  See [computational note](../COMPUTATIONAL_IMPLEMENTATION.md).
- **Paper draft:** \`manuscript/main.tex\` remains out-of-sync until
  independently evaluated new methods and theory are finalized.
