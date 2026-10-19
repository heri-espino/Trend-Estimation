# Marp lecture — pooled trend smoothness and Study M.2

**Title:** *How should we choose trend smoothness?*  
**Status:** first COMPLETE editable teaching edition, 2026-10-19.  
**Branch:** paper/pooled-loocv-numerical-optimization.  
**Markdown:** [001_process_diversity_lecture.md](001_process_diversity_lecture.md).

This is a **full, source-grounded lecture** from the observation model, matrix penalty, normal equations, eigenvalues and degrees of freedom, through pooled exact deletion-honest CV, GCV, AICc, Gaussian covariance ML, nine data-generating processes, and the completed 1,000-seed Study M.2 results. It distinguishes **retrospective reconstruction** from future forecasting throughout.

The authored deck contains **89 slides, 28 inserted image references / 25 distinct image assets**, including **12 newly designed lecture SVGs**, saved one-seed process graphics and previously audited R1/R3 excess-risk heatmaps. It has explicit worked formulas, experimental tables, interpretation, pooling contrasts, discussion questions and methodological limitations. The two heatmaps and single-seed trajectories are reused without changing the historical result source files. Source-specific findings are in [the completed M.2 analysis](../notes/STUDY_M2_1000_SEED_PROCESS_RESULTS_2026-10-19.md).

## Rendering (PowerShell from repository root)

Marp CLI uses Node.js. If your current Conda environment does not have Node/npm/npx, install them **without administrator rights** with:

    conda install -c conda-forge nodejs

Then:

    git switch paper/pooled-loocv-numerical-optimization
    git pull --ff-only

    $folder = "working_papers/Working Paper - Pooled LOOCV Numerical Optimization/presentation"
    $deck = "$folder/001_process_diversity_lecture.md"

    python "$folder/check_deck.py"

    # Optional: regenerate ALL 12 new standalone lecture SVGs from source.
    node "$folder/generate_conceptual_figures.mjs"
    node "$folder/generate_results_figures.mjs"

    New-Item -ItemType Directory -Force -Path "$folder/build" | Out-Null

    npx --yes @marp-team/marp-cli@latest --allow-local-files "$deck" -o "$folder/build/001_process_diversity_lecture.html"
    npx --yes @marp-team/marp-cli@latest --allow-local-files "$deck" --pdf -o "$folder/build/001_process_diversity_lecture.pdf"
    npx --yes @marp-team/marp-cli@latest --allow-local-files "$deck" --pptx -o "$folder/build/001_process_diversity_lecture.pptx"

The outputs under presentation/build/ are deliberately ignored by Git. **All generated SVGs and the source deck remain tracked.** Marp may need a working Chromium/Chrome-compatible browser for browser-dependent PDF/PPTX conversion; HTML may work independently. Rendering was **not executed in the document-authoring environment** because Marp CLI/browser dependencies were unavailable; use the commands above and inspect slides for font/clipping on your local machine. The Markdown and image paths passed a structural verification using the exact branch tree.

For more on CLI flags, see the [official Marp CLI documentation](https://github.com/marp-team/marp-cli).

## Teaching outline

| Lecture segment | Main question | Supporting graphics |
|---|---|---|
| I. Setting and PLS | Why does the second-difference penalty produce a smooth trend? | Original Gaussian gallery; lecture observed-versus-latent and D2 SVG; spectral diagram |
| II. Nonzero mean | Why profile a common difference mean instead of fixing it at zero? | Derivation of particular polynomial, joint profile, extra EDF |
| III. Statistical criteria | What differs between exact CV, GCV, AICc and Gaussian variance-component ML? | Fully written formulas, 11-method table; numerical/statistical separation |
| IV. Experimental mechanism design | How do we tell a genuine trend jump from corrupted observation noise? | Nine saved R3 trajectory plots, fresh common-seed diagram |
| V. 1,000-seed findings | Is a lowest-MSE method consistently better? | R1/R3 risk heatmaps, runner-up gap, AR1 S-vs-risk, level-jump risk, outlier tails |
| VI. Pooling effects | When does pooling damage the cleanest series? | First-series GLS forest, R1/R3 heterogeneity bars, pooling-logic diagram |
| VII. Limitations and next steps | What does the experiment support and not support? | One-seed-vs-mean winner agreement figure, discussion questions |

The deck is intentionally detailed. For a shorter presentation, exclude optional gallery slides for mechanisms not central to the audience (without deleting their files), or split into two lectures: **theory and selection** / **process experiments and inference**.

## Visual data provenance

**Twelve lecture-specific SVGs, reproducible in the assets/ directory:**

- Conceptual diagrams (5): observed-vs-latent, $D_2$ matrix, spectral transfer, common seed design, identical-first-series pooling.
- Committed-data statistical diagrams (7): R3 runner-up mean-risk gap with Holm flags, AR1 selected $S$ versus MSE, jump risk comparison, outlier distribution summaries (median/mean/p90), first-series GLS pooling forest with paired CIs, low-noise first-series damage under pooling, and M.1 one-seed winner versus M.2 mean winner agreement.

Reproduction is deterministic with the Node-only generators in this folder. The empirical figures read *only* committed CSV summaries and do **not** claim access to the 40 ignored raw per-seed gzip shards. The conceptual figures are deliberately marked as teaching schematics, **not empirical measurements**. No plots claim a raw distribution, violin chart or bootstrap unavailable in the archive.

**Previously committed:** 18 M.1 single-seed trajectory PNGs and two risk-excess SVG heatmaps. The Marp deck references representative images as teaching examples; the remaining archive images are retained in results for follow-up.

**Mathematical boundaries:** normal equations and $(I+\lambda Q)^{-1}$, PSD rank/nullity, $S$ normalized from $\operatorname{tr} H$, joint mean profile and EDF, exact fold-clean CV, and the specific AICc and Gaussian contrast ML implementation are drawn from the current working-paper source. The nonzero difference-mean model is not invented by this project. The implemented BIC boundary problem is discussed but BIC is **not among the eleven M.2 methods**.

**Statistical boundaries:** 1,000 *independent base seeds*, 9 dependent mechanism transformations per seed, R1 nested within R3, 11 feasible methods; 198,000 *method records* rather than independent draws. Global Holm p adjusted over 990 pairwise mean-MSE comparisons, intervals remain pointwise. In **seven of the nine R3 processes** the nearest two mean-risk policies are **not significantly separated** after global Holm. The very strong R3 differences favoring fixed S=.5 for genuine level jump and S=.8 for AR1 are conditional on the chosen DGP amplitudes and phi.

## Source files and scope

- [M.2 results note](../notes/STUDY_M2_1000_SEED_PROCESS_RESULTS_2026-10-19.md)
- [M.2 preregistered protocol](../notes/STUDY_M2_PROCESS_DIVERSITY_INDEPENDENT_SEEDS_2026-10-19.md)
- [Compact-only audit](../../../experiments/pooled_loocv_smoothness/audit_process_monte_carlo_compact.py)
- [Study M.1 trajectory generator](../../../experiments/pooled_loocv_smoothness/run_process_examples.py)
- [Study M.2 independent-seed generator](../../../experiments/pooled_loocv_smoothness/run_process_monte_carlo.py)
- [Theory and criteria implementation](../../../experiments/pooled_loocv_smoothness/cortes_optimality_criteria.py)
- [Results/manifest](../../../results/pooled_loocv_smoothness/process_examples/seed_study_1000_v1/manifest.json)

**Never** merge this research lecture into the separate horizon-h forecasting working paper. Store any new findings in dated paper notes; regenerate diagrams when result CSVs change; keep the user's raw gzip replicate shards backed up and out of ordinary Git.
