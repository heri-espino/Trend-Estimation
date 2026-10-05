# NEXT — Numerical-methods paper after the 2026-10-05 split

## Priority 1 — Refactor the manuscript identity

- [ ] Rewrite the abstract/introduction so the criterion \(F(S)\) is input from the companion smoothness-CV paper, not the numerical paper's primary novelty.
- [ ] Keep only enough Guerrero/Hart/forecast-CV background to make the numerical problem self-contained.
- [ ] Move criterion-level novelty language to \`../../paper_smoothness-cv/\`.
- [ ] Preserve the frozen numerical benchmark results, endpoint treatment, derivatives, multimodality evidence, and applied geometry examples.
- [ ] Audit every use of "forecast-optimal smoothness" so the paper clearly distinguishes definition of the target from numerical solution of the target.

## Priority 2 — Decide the numerical-paper strength

Current production method:
\[
\text{adaptive discovery}
\rightarrow
\text{root brackets}
\rightarrow
\text{Brent refinement}.
\]

The stronger possible method is:
\[
\text{rational structure}
\rightarrow
\text{certified real-root isolation}
\rightarrow
\text{Brent refinement}.
\]

- [ ] Decide whether the paper will stop at the frozen adaptive-Brent method or pursue certified root isolation.
- [ ] If pursuing certification, generalize the Sturm mini-check beyond the toy case.
- [ ] Construct the stationary polynomial numerator \(R(\lambda)\) robustly for practical \(L,d,h\).
- [ ] Benchmark root counts/brackets against the existing frozen suites.
- [ ] State precise assumptions and degenerate cases.
- [ ] Do not claim "grid-free" or "certified" until this generalized implementation exists and passes tests.

## Priority 3 — Finish the frozen-method paper if certification is deferred

- [ ] Finish numerical-conditioning discussion near \(S=0\) and \(S=1\).
- [ ] Write the limitations section on missed tangential/even-multiplicity roots.
- [ ] Generate final figures/tables from frozen results.
- [ ] Compile the SMCCA manuscript through the manual workflow.
- [ ] Run notation/claim consistency pass.
- [ ] Run referee-style novelty/readability review.

## Frozen boundaries

- Do not retune the N009 primary search from confirmatory benchmark results.
- Dense search is a reference approximation, not mathematical ground truth.
- Financial panels are geometry stress tests, not evidence of predictability or trading value.
- Epsilon spacing is post-processing, not root discovery.
- Brent refines bracketed roots; it does not discover the global set by itself.
