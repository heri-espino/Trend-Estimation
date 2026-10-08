# Working Paper — Dynamic Branch Selection

**Status:** independent research working paper; exploratory results preserved,
no unconditional forecast-performance advantage established.

**Working title:** *Dynamic Branch Selection for Forecast-Optimal Trend Smoothness*.

## Research question

Do the histories of individual minima of chronological future-block forecast
loss functions help predict a useful current smoothing parameter?
For fixed difference order \(d\), window \(L\), horizon \(h\) and
historical origin \(t\), study the local minima of \(F_t(S)\) for
\(S\in[0,1]\), then follow them across completed validation origins.

For each branch \(j\), record

\[
V_j=[S_{j,t},\,\ell^{(1)}_{j,t},\,\ell^{(2)}_{j,t}]_t.
\]

A historical branch selector \(\psi(V_1,\ldots,V_J)\) chooses a branch,
and a decision map \(\phi(V_j)\) turns it into the smoothing
index for the **latest refitted forecast**. Examples include last,
recency-weighted and validation-loss-weighted means, and forecasts
of the smoothness trajectory itself.

## What is present

- Self-contained working manuscript: [manuscript/main.tex](manuscript/main.tex);
  formulation, branch rules, completed evaluation, limitations, bibliography
  and committed figures are local to this directory.
- Research notes: [notes/README.md](notes/README.md);
  original branch definitions and tracked-minimum continuation notes.
- Frozen chronological experiments: CP04, CP05, CP06, CP07 and CP08 in
  [checkpoints/](checkpoints/). A *separately labeled, unrun*
  numerical correspondence benchmark is also preserved.
- Historical figure and example code are kept under this working paper;
  reusable implementations and raw experiment artifacts stay in
  repository-wide \`src/\`, \`experiments/\`, and \`results/\`.

## Results / honesty

CP04 small confirmation favored recency weighting, but CP05
64-series evaluation and CP07/CP08 simulation designs did not
demonstrate universal improvement over simple pooled forecast-CV.
The numerical correspondence benchmark is **not** a completed
experiment; a persistent branch is not mathematically unique
when minima cross, appear or disappear.

This study stands on its own. The key contribution sought is
a defensible, information-safe dynamic smoothing decision based
on temporal minima, **not a claim that a larger validation matrix
automatically improves forecasts**.

## Build

From the repository root, with a standard \`latexmk\`/BibTeX
installation:

~~~bash
python "working_papers/Working Paper - Dynamic Branch Selection/build.py" --check
python "working_papers/Working Paper - Dynamic Branch Selection/build.py"
~~~

The PDF is generated to \`build/main.pdf\`. Builds are **manual only**.
The current source remains a working draft; it is not submission-ready.
