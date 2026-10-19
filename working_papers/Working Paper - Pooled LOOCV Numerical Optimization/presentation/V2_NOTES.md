# Lecture V2 — detailed authoring, source and audit notes

**2026-10-19. COMMITTED MASTER DECK.** V1 is preserved unchanged. V2 is a distinct, editable Marp presentation at [002_process_diversity_lecture_v2.md](002_process_diversity_lecture_v2.md).

## What is actually completed

- **187 slides** at the time of this checkpoint (source frontmatter and slide markers should be checked again after edits). V2 contains all source-grounded V1 content plus:
  - A dozen formal linear-algebra and spectral-smoothing proof slides, including forward-difference operators, the null space and rank of Q, positive definiteness of the Hessian, eigenvalue attenuation, limits, derivative and monotonicity of S, and fixed-lambda bias/variance.
  - Derivations of the particular polynomial, the profiled pooled difference mean, the hat-matrix rank-one coupling, full EDF, and deletion-honest pooled PRESS.
  - Detailed Gaussian contrast covariance and profile GLS mean, AICc and BIC boundaries, and careful separation of statistical scores from numerical optimizers.
  - Paired-simulation inference, common random numbers, global Holm adjustment, win frequency versus mean-MSE rank, and the *same first series* pooling estimand.
  - Seven worked audience exercises with answers.
  - **18 complete risk-table slides**: all 9 processes × R=1/R=3 × 11 feasible selectors = 198 archived result rows, including mean MSE/MAE, p90, nominal S, fitted mean and win share.
  - **Nine complete pooling-table slides**: all 9 processes × 11 feasible selectors = 99 source-archived first-series paired differences, pointwise CIs and win fractions.
  - Eleven NEW, source-derived SVG figures and associated stand-alone editable SVG files in assets/.
- **Completed studies reused, not rerun**: the 18 original one-seed gallery PNGs, 198 result aggregates, 990 paired method contrasts, 99 pooling contrasts and two R1/R3 risk excess heatmaps remain at their original source paths.
- **New vector images**: v2_win_frequency_R1.svg, v2_win_frequency_R3.svg, v2_selected_s_R1.svg, v2_selected_s_R3.svg, v2_fitted_mu_R3.svg, v2_ranking_ladder_R3.svg, v2_mean_vs_p90_R1.svg, v2_mean_vs_p90_R3.svg, v2_pooling_forest_cv_joint.svg, v2_pooling_forest_aicc_joint.svg and v2_pooling_forest_plugin_mu_ml.svg. The generator [generate_v2_figures.mjs](generate_v2_figures.mjs) recomputes them from committed compact CSVs without Monte Carlo simulations. Some styling may vary upon regeneration; numerical values come from source CSV.
- **Optional additional teaching plots**: [export_v2_criterion_examples.py](export_v2_criterion_examples.py) is implemented but NOT executed in this authoring session. It is a small, single-seed exporter for actual CV/GCV/AICc-versus-S curves, ex-post *synthetic* tau MSE-versus-S, actual fitted trend curves at S=.20/.50/.80/.93, and R-specific total EDF-versus-S. These are **not yet linked** in V2 because their PNG files are absent until a user runs the exporter; no invented empirical curves are silently substituted.

## Why the statistical claims remain narrow

The uploaded run manifest records 1000 *independent base seeds* (not 198000 independent method rows), 9 common-shock mechanism changes, nested R=1/3, 11 feasible policies, d=2, N=80, 40/40 chunks and source SHA fda4e69d64d47675e5bd126bf7332aa22a3d68fc. The compact result CSVs and original one-seed gallery plots were committed in 47392dbc4d11ca63d2e856fc9d974e4a24a11021.

At R3 **only the winner-vs-runner-up gap in the true latent level-jump and strongly AR1-correlated observation-noise cases** survives the global Holm adjustment. Several Gaussian GLS versus plug-in mean comparisons are mean-risk near ties despite numerical ranks. A common lambda selected from series with unequal observation noise SDs can *harm* the clean first series. These are retrospective realized latent-trend reconstruction experiments and do **not** establish future horizon-h forecast skill, real-market latent reconstruction accuracy, universal smoothing or optimizer novelty.

The original 1000-seed raw gzip rows are ignored by Git and must remain backed up on the user's machine. V2 plots are from compact summaries: there is no false claim that raw seed results were reaggregated within lecture production.

## Exact regeneration and checks (PowerShell, repository root)

    conda activate trend-estimation
    git switch paper/pooled-loocv-numerical-optimization
    git pull --ff-only

    $pres = "working_papers/Working Paper - Pooled LOOCV Numerical Optimization/presentation"
    python "$pres/check_deck.py" --version v1
    python "$pres/check_deck.py" --version v2

    node "$pres/generate_conceptual_figures.mjs"
    node "$pres/generate_results_figures.mjs"
    node "$pres/generate_v2_figures.mjs"

    # Optional, creates NEW figures not yet embedded in the deck:
    python "$pres/export_v2_criterion_examples.py"

    New-Item -ItemType Directory -Force -Path "$pres/build" | Out-Null
    npx --yes @marp-team/marp-cli@latest --allow-local-files "$pres/002_process_diversity_lecture_v2.md" -o "$pres/build/002_process_diversity_lecture_v2.html"
    npx --yes @marp-team/marp-cli@latest --allow-local-files "$pres/002_process_diversity_lecture_v2.md" --pdf -o "$pres/build/002_process_diversity_lecture_v2.pdf"
    npx --yes @marp-team/marp-cli@latest --allow-local-files "$pres/002_process_diversity_lecture_v2.md" --pptx -o "$pres/build/002_process_diversity_lecture_v2.pptx"

Node.js can be installed into Conda via conda-forge without administrator permissions. Marp browser-based rendering may require Chrome/Chromium available on the local machine. Build exports are ignored by Git; only source, diagrams, tests and documentation are tracked.

## What remains to verify locally

1. **Render and inspect** all slides in HTML/PDF: no clipped tables or equation overflow, particularly the compact source-data appendix slides. Static asset/syntax checks cannot certify visual layout.
2. Run the optional criterion-curve exporter if the lecture should show genuine objective-curve shapes. The scripts should be run from repository root after the environment is activated. Do not insert links to images until they have actually been created and reviewed.
3. Optionally include *selected* criterion-curve PNGs after auditing numeric minimizers, and then regenerate the deck and notes with the new links.
4. Preserve source-driven interpretation: no method is selected by looking at simulated true tau, and each criterion-score curve is scaled independently for plotting because raw scores are incomparable across criteria.

## Source references

- [Source results and independent compact audit](../notes/STUDY_M2_1000_SEED_PROCESS_RESULTS_2026-10-19.md)
- [Frozen experiment protocol](../notes/STUDY_M2_PROCESS_DIVERSITY_INDEPENDENT_SEEDS_2026-10-19.md)
- [Selector implementation](../../../experiments/pooled_loocv_smoothness/cortes_optimality_criteria.py)
- [Nine-process generator](../../../experiments/pooled_loocv_smoothness/run_process_examples.py)
- [One-thousand-seed runner](../../../experiments/pooled_loocv_smoothness/run_process_monte_carlo.py)
- [Study M.2 manifest](../../../results/pooled_loocv_smoothness/process_examples/seed_study_1000_v1/manifest.json)

**Next agent:** Update this note and the working paper's handoff after any manual rendering/export analysis; do not merely claim that the optional curve figures or compiled HTML/PDF/PPTX have already been produced on GitHub. No PR/merge/main changes; stay in the research branch.
