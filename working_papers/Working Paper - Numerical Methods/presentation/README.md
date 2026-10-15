# Numerical Methods — Figure Studio / Presentation

This folder provides a reproducible, independent visual explanation of the numerical-methods paper, suitable for a research talk and eventual supplementary figures. It does **not** change the paper's frozen benchmark protocols or automatically insert all graphics into the manuscript.

## Generate all figures

From the repository root, with the existing Python environment active:

~~~powershell
python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --list
python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --group concepts
python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --group all
~~~

The default generates **28 figures**, in both vector PDF and preview PNG, under presentation/figures/. It also writes a local figure_build_manifest.json. PDF plots remain vector; PNG previews are raster exports.

Other useful selections:

~~~powershell
python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --group algorithm
python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --group benchmarks
python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --group applied
python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --only 08_adaptive_search_steps 23_spy_rank_reversal
python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --group all --format pdf
~~~

Dependencies: the repository's usual Python environment, with numpy, pandas, matplotlib, scipy and trend_estimation importable. No GPU, yfinance/network download, new Monte Carlo, LaTeX or SymPy is needed for the figure suite. Activate your existing trend-estimation environment first, and run --group concepts as a short check.

## Compile the full Beamer presentation

The **LaTeX slide deck** is [slides.tex](slides.tex): a widescreen (16:9)
research talk with **all 28 figure PDFs**, a clear scientific question and
interpretation for each figure, four narrative acts, the precise PLS objective,
and conclusion/limitations/reproducibility slides.

**One command for both figures and presentation** (PowerShell from repository root,
after activating the usual environment):

~~~powershell
& "working_papers/Working Paper - Numerical Methods/presentation/build_all.ps1"
~~~

Or do the two steps separately:

~~~powershell
python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --group all --format pdf
cd "working_papers/Working Paper - Numerical Methods/presentation"
.\build_slides.bat
~~~

The resulting deck is **Numerical_Methods_Presentation.pdf**, in this presentation folder.
A working MiKTeX or TeX Live installation with latexmk is required.
The Beamer source can also be compiled *before* generating figures: missing PDFs
show explicitly labeled placeholders instead of causing a fatal LaTeX error.

**Important:** The Beamer source is complete, but you still need to generate
the 28 PDFs locally and run the final build. The figure rendering itself has
not been executed as part of committing this source.

## Scientific provenance

- Figures **01–06** are openly labeled pedagogical diagrams or generated toy observations. The fixed local random seeds serve illustration only, not empirical performance claims.
- Figures **07–13** explain the already documented six-observation Sturm example and inspect the existing adaptive code, analytic adversarial definitions and the frozen sensitivity CSV. Figure 08 reconstructs initial, endpoint and final sampling sets rather than a timestamped execution log.
- Figures **14–21** read committed CSVs from the **frozen 2026-09-30 adversarial, synthetic, sensitivity and financial studies**; they do not rerun the numerical experiment.
- Figures **22–28** read the frozen **2026-10-01 applied case-study outputs**. The fitted and forecast **levels** are visualized for interpretation, while reported CV and test MSE values were calculated using **log levels**.

The exact historical input directories are fixed in _style.py, and missing files result in a clear error rather than automatic replacement. Nothing writes into results/.

Dense-grid minima are **empirical references**, not mathematically certified roots. The Sturm root count refers to the **small rational input example only**. Financial figures are geometry and selection-sensitivity diagnostics, not evidence of trading value. Test-set ranks are retrospective diagnostics, never part of candidate selection.

## Presentation storyline

See [STORYBOARD.md](STORYBOARD.md) for a question-per-slide figure inventory, scientific provenance and suggested paper versus talk placement.

A recommended research talk has four acts:

1. **The object:** chronological forecast CV, smoothness, penalty, endpoints.
2. **The numerical challenge:** multimodality, gradients, adaptive search, endpoint failures, Sturm.
3. **Evidence:** adversarial truth, benchmark agreement, efficiency and sensitivity.
4. **Interpretation:** GDP contrast, SPY rank reversal, AAPL and BTC candidates, temporal splits.

## Files and tracking

~~~text
presentation/
  README.md
  STORYBOARD.md
  build_figures.py
  build_all.ps1
  build_slides.bat
  slides.tex
  _style.py
  figures_concepts.py
  figures_algorithm.py
  figures_benchmarks.py
  figures_applied.py
  figures/
    .gitignore
    .gitkeep
~~~

Vector PDFs are intentionally **not ignored**, so you can commit the selected plots once reviewed. Preview PNGs and the local generation manifest are ignored to avoid doubling repository size.

When the plots have been rendered and reviewed, from the repository root:

~~~powershell
git add "working_papers/Working Paper - Numerical Methods/presentation/figures/*.pdf"
git commit -m "figures(paper3): add reviewed presentation figures"
git push
~~~

This addition provides source code and instructions only. The current numerical-methods manuscript and frozen experiment files remain untouched.
