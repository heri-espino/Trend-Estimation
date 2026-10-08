# Penalized Trend Tutorial

This manuscript is the step-by-step mathematical companion to the Trend Estimation library.

It is secondary to the active research paper and should not drive the research agenda. Its role is pedagogical: explain finite-difference penalties, smoothness, temporal validation, analytic derivatives, and numerical selection carefully while remaining mathematically consistent with the library.

Reusable logic belongs in `src/trend_estimation/`; derivation checkpoints belong in `notes/`.

Build from the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -outdir=paper_penalized-trend-tutorial/build paper_penalized-trend-tutorial/main.tex
```
