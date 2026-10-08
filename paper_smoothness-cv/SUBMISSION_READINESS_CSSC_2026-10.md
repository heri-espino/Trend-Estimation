> **2026-10-08: WORKING-DRAFT CHECKLIST ONLY.** This submission-preparation file documents the October CSSC-oriented *interim* manuscript, **not the final stage of the project**. Numerical methods are being reassessed and new simulations may replace old CP03 results in a future submission, while all old outputs remain archived. We intend to finish research notes, select numerical methods, run/freeze any new experiments, complete prior-art work, and **only then rewrite the final paper**. Compilation/style checks listed below are still relevant but are not the next scientific priority. See [notes/INDEX.md](notes/INDEX.md), [notes/research_log_2026-10.md](notes/research_log_2026-10.md), [notes/next_experiments.md](notes/next_experiments.md).

---

# Submission preparation: Communications in Statistics—Simulation and Computation

Updated: October 8, 2026

## Editorial fit

The target journal emphasizes computational statistical methodology
and rigorous, reproducible simulation comparisons. The revised
manuscript is a statistical simulation paper, not a financial
forecasting application or a stand-alone theoretical note.

**Working title:** *Horizon-Matched Cross-Validation for Forecast-Optimal
Penalized Trend Smoothness*.

## Main question

For a finite-difference penalized least-squares trend continued
over horizon h, choose S in [0,1] by minimizing the historical
mean squared errors of the actual h-step future-block forecasts.
Only completed validation blocks may inform the forecast
at outer origin T. The final trend is refitted before prediction.

The monotone S transform compactifies lambda in [0,infinity],
including both limiting smoothing regimes. This supports a
complete search and interpretable comparisons; the transform
does not create a new smoothing estimator, change the objective's
minimizing fitted trend, or make a multimodal loss unimodal.

## Closest literature and distinctions

| Prior work | What it establishes | Relation to this manuscript |
| --- | --- | --- |
| Guerrero (2007, 2008) | PLS trend smoother and user-controlled percentage smoothness | The S index is established; its forecast-error selection is the present focus |
| Cortés-Toto et al. (2017), *CSSC* | PLS criteria including CV, GCV, AICc and BIC; attained smoothness | Direct same-estimator comparison, but distinct from h-step trend continuation MSE |
| Vilar-Fernández and Cao (2007), *CSSC* | Nonparametric time-series forecasting and smoothing choices | Important journal-level predictive smoothing precedent |
| Bates et al. (1987), *CSSC* | Computational generalized CV routines | Computational regularization precedent |
| Hart (1994) | One-step predictive CV for kernel smoothing with correlated errors | Strong prior art for forecast-based tuning; do not claim invention of the concept |
| Islas, Guerrero, and Silva (2019) | Remittance forecasts using controlled-smoothness trend and Markov switching | Refutes novelty of controlled-trend forecasting in general |
| Islas Camargo and Zumaya Galván (2025) | Exchange-rate forecasts with controlled smoothness | Related forecasting application, with a different model and tuning design |
| Franke, Kukacka, and Sacht (2026) | Simulation-based HP parameter choice for recovering known latent trends | Different loss target: recovery versus future prediction |
| Biessy (2026) | Whittaker-Henderson smoothing, marginal likelihood and extrapolation constraints | Different criterion and forecasting construction |

The manuscript makes the specific combined methodological claim,
**not** a categorical novelty claim for PLS, the index, or
time-series cross-validation.

## Paper structure

1. Motivation and precise statistical object
2. Direct literature comparison focused on this journal and nearby PLS work
3. Penalized smoother, normalized S, and polynomial continuation
4. Operational chronological h-step forecast CV and refitting
5. Properties and limits of the bounded parametrization
6. Frozen factorial simulation and paired predictive evaluation
7. Main CP03 results: 3,000 scenarios, 72,000 outer-origin/horizon evaluations
8. Discussion and qualified conclusions
9. Appendices: branch history V_j and complete CP04–CP08 exploratory results

Three CP03 figures are central. The optional CP08 figures and workflow
tutorial are retained in the appendices. No checkpoint has been
rerun or retuned to generate this revision.

## Honest interpretation of results

The CP03 geometric RMSFE ratios for matched-horizon tuning
relative to one-step tuning are 1.000, 0.947, 0.861, and
0.762 at horizons 1, 3, 6, and 12. They summarize paired
results under the specified factorial design, not universal risk
dominance. Resampling must respect shared random seeds.
Higher-order continuation and data-generating mechanisms outside
the design remain limitations.

The exploratory branch results are mixed. A four-series held-out
confirmation favored one rule, whereas a much larger financial
panel and changing-roughness simulations did not reproduce its
aggregate advantage against pooled forecast-CV. The appendices
preserve these failures.

## Verification and remaining work before submission

- [x] Main text reframed around pooled forecast-CV on normalized S
- [x] Nearby controlled-smoothing forecasting studies addressed explicitly
- [x] Relevant *CSSC* predecessors emphasized
- [x] CP03 prioritized; exploratory extensions moved to appendices
- [x] Equation and bibliography static audits
- [ ] Build a fresh PDF from the new LaTeX and inspect tables, captions, page breaks, citations, and all figures
- [ ] Confirm latest journal-specific author instructions and any required final LaTeX template/style
- [ ] Verify citation metadata and read full-text sources where currently absent from extracted literature
- [ ] Strengthen comparative validation if aiming for a methodological claim substantially beyond known forecast-based smoothing: e.g. a direct predictive-smoothing comparator and sensitivity across continuation orders and data-generating processes
- [ ] Confirm all submission declarations, author metadata, and reproducibility access

## Commands

From the repository root:

```bash
git pull --ff-only
python paper_smoothness-cv/build.py --check
python paper_smoothness-cv/build.py
```

The submission manuscript and code must not suggest numerical,
computational, or predictive superiority beyond the experiments
actually reported.
