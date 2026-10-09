# Working Paper — Numerical Methods

**Working title:** *Numerical Recovery of Multimodal Forecast-Smoothness Minima: Adaptive Search and Sturm Isolation*.

**Status:** active independent numerical-analysis working paper.
The objective is the reliable, efficient **recovery and ranking of
stationary points and minima on a single forecast-loss surface**, not
selection of temporal branches.

## Agent continuity and canonical app

The current independent app is
\`streamlit run apps/numerical_methods.py\`, with **one fixed
horizon-h weighted F(S)**, analytic derivatives and exact boundary
checks. Do not replace it with the old historical tracked-minima
dashboard: that visualizes earlier Val1/Val2 experiments.
Read [AI_HANDOFF.md](AI_HANDOFF.md) and
[THEORETICAL_CONTRIBUTIONS.md](../THEORETICAL_CONTRIBUTIONS.md)
for exact proof/novelty boundaries.

The [computational implementation note](../COMPUTATIONAL_IMPLEMENTATION.md)
records user-provided RTX 4500 Ada **float32 loss-kernel** performance
only as optional supplementary implementation evidence. A faster
matrix contraction is not automatically a new numerical solver theorem.
The priority remains stationary-point recovery, endpoint handling,
objective conditioning, analytic vs certified root isolation and
explicit assumptions.

## The numerical problem

Consider a PLS forecast-validation objective \(F(S)\) over normalized
smoothness \(S\in[0,1]\). The function may have multiple local minima
and minima near the exact limiting endpoints. Recover all *relevant*
interior and boundary candidates, and compare their objective values
while controlling numerical cost.

Methods under study:
1. Analytic derivatives in penalty and smoothness coordinates.
2. Adaptive sampling and derivative-sign root brackets.
3. Brent refinement and stationary-point classification.
4. Explicit boundary \(S=0,1\) comparisons.
5. Rational stationary equations and Sturm isolation for *small* instances.

## Available evidence and limits

The historical adaptive-search protocol recovered 240/240 adversarial
relevant optima, 2105/2105 synthetic dense-reference minima
and 473/473 financial geometry dense-reference minima.
Those are results **relative to the tested reference protocols**,
not a proof of global completeness for arbitrary objectives.
Exact rational Sturm root counting is proven only for the finite
rationalized instance on which the certificate is constructed.

The independent working manuscript is [main.tex](main.tex).
Notes and checkpoint evidence are local to this directory.
No branch tracking, chronological matching policy, or
branch-based forecasting decision is necessary for this numerical problem.

## Reproduce

~~~bash
python -m pip install -e ".[symbolic,dev]"
python experiments/numerical_smoothness_selection/run_sturm_minicheck.py
python -m pytest tests/test_sturm_forecast_smoothness.py
~~~

Manual LaTeX build from this folder:

~~~bash
cd "working_papers/Working Paper - Numerical Methods"
mkdir -p build
latexmk -pdf -interaction=nonstopmode -outdir=build main.tex
~~~

Frozen numerical outputs remain in shared repository \`results/\`.
