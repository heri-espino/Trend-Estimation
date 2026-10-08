# NEXT — Applied interpretation of multiple forecast-CV minima

## Priority 1 — Run the frozen applied protocol

- [x] Freeze the four data families: GDPC1, SPY, AAPL, BTC-USD.
- [x] Freeze development/test separation before test evaluation.
- [x] Freeze \(\varepsilon=0.10\).
- [x] Freeze deterministic development-only configuration selection.
- [x] Implement run_applied_case_studies.py.
- [x] Run the paper preset and commit its result directory.

## Priority 2 — Inspect validation/test ranking

For every frozen candidate:

- [x] record rolling validation error \(CV_k\);
- [x] record untouched test MSE \(E_k^{\mathrm{test}}\);
- [x] inspect validation rank and test rank;
- [x] inspect \(\Delta CV_k\) and \(\Delta E_k^{\mathrm{test}}\);
- [x] count validation--test rank reversals;
- [x] verify no example/configuration was selected using test performance.

The test-best candidate is diagnostic only.

## Priority 3 — Interpret the minima

- [ ] Explain the spectral attenuation
      \(\alpha_j(\lambda)=1/(1+\lambda\delta_j)\).
- [ ] Explain how smoothness changes endpoint slope/curvature and continuation.
- [ ] Identify examples with similar CV error but visibly different trends.
- [ ] Show whether their validation ordering persists on test.
- [ ] Describe the candidate set as selection sensitivity, not uncertainty.

## Priority 4 — Manuscript revision

- [x] Add subsection: Why multiple forecast-optimal smoothness levels can arise.
- [x] Add subsection: Applied examples and validation--test ranking.
- [x] Integrate the four-row applied figure.
- [ ] Reduce current financial stress-test prose if page pressure grows.
- [ ] Revisit abstract and introduction after applied results are frozen.
- [ ] Consider one compact standard scalar-optimizer comparator.
- [ ] Compile the SMCCA PDF and run a referee-style review.

## Submission boundary

The paper remains a numerical/applied-mathematics paper. The applied examples
interpret the consequences and stability of smoothness selection; they do not
establish economic regimes, universal forecasting superiority, or trading
value.
