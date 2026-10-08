# Temporal matching of local forecast-loss minima

**Active independent Dynamic Branch Selection study.** For each
historical forecast origin \(t\) with completed future-block targets,
recover local minimizing candidates
\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\}\subseteq[0,1].
\]

## Current input to the correspondence problem

**Prospective 2026-10-08 change:** the active Paper 2 now tracks
local minima of the **rolling temporally weighted** surfaces
\(F_r^{(m,d,L,h)}(S)\), one separate collection of branches for each
predeclared weighting method and difference order. Every surface
uses only completed past/present \(h\)-step losses. The correspondence
problem and nonuniqueness caveats below still apply.

The **Val1/Val2** \(V_j\) schema near the end of this historical
note describes the **earlier CP04–CP08 design**, not the new
weighted-\(F\) method. Current branch state is
\(V_j=[(r,t_r,S^*_{j,r},F_r(S^*_{j,r}))]\) and only an untouched
outer test is required. Full specification:
[dynamic_tracked_smoothness.md](dynamic_tracked_smoothness.md).

## Correspondence model

A previous candidate \(S_{j,t-1}\) may be linked to a current
candidate \(S_{k,t}\) if
\[
|S_{j,t-1}-S_{k,t}|\le\varepsilon_{\rm track}.
\]
The historical implementation greedily matches nearest admissible
pairs one-to-one. Its radius is different from candidate-spacing
epsilon used to merge close minima **within one surface**.

Greedy matching is not always maximum-cardinality:
with old values 0.40, 0.48, new values 0.34, 0.43 and
radius 0.10, greedy accepts 0.40 -> 0.43 and cannot match
the remaining values, although links 0.40 -> 0.34 and
0.48 -> 0.43 satisfy both bounds.

Pairwise maximum-cardinality/minimum-distance assignment is
one alternative, but neither rule guarantees correct identity
through crossings, births, deaths or ambiguous minima.

## Evidence and proposed controlled evaluation

A historical four-series example recorded **1,392**
initialized branch-origin states, 924 matched and 468 missing.
These are *algorithm output counts*, not verified identity
accuracy rates. The original detailed tracking note is
archived under \`ideas/archive_temporal_matching_note_2026-10.md\`.

The independent planned labeled-trajectory experiment
[NUMERICAL_TRACKING_CP05_UNRUN](../checkpoints/NUMERICAL_TRACKING_CP05_UNRUN.md)
has **not been executed**. It proposes known labels,
different trajectory mechanisms and matching radii.

## Forecast decision

For matched minima, store historical smoothness and losses
\[
V_j=[(S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t})]_t.
\]
Choose \(\widehat j=\psi(V_1,\ldots,V_J)\) and
\(\widehat S_T=\phi(V_{\widehat j})\), then **refit**
a trend on today's latest observations. The outer future
cannot be used while constructing \(V,\psi,\phi\).
