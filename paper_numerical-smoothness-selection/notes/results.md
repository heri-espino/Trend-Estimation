# Numerical Results Log

## 2026-09-30 — First synthetic smoke and diagnostic quick run

### Smoke

The first synthetic smoke benchmark covered 8 surfaces with

\[
d\in\{1,2\},\qquad L\in\{63,126\},\qquad h\in\{1,5\}.
\]

All dense-reference interior minima were matched by the adaptive search. The
adaptive optimum was within roughly one dense-grid cell of the dense optimum in
every case.

### First quick run: diagnostic only

The first quick run contained 216 surfaces:

- 3 seeds;
- 2 synthetic scenarios (baseline, persistent);
- \(d\in\{1,2,3,4\}\);
- \(L\in\{63,126,252\}\);
- \(h\in\{1,5,20\}\);
- a 2001-point dense reference on \(S\in[0,1]\).

Observed diagnostic totals:

- dense interior minima: 229;
- matched by adaptive search: 222;
- missed: 7 minima in 6 of 216 surfaces;
- mean adaptive evaluations: 71.23 versus 2001 dense evaluations;
- median adaptive evaluations: 68.5;
- mean evaluation fraction: 3.56%;
- total adaptive-search time: 2.36 s;
- total dense-reference time: 55.70 s.

The failures were highly structured: all 7 missed minima occurred for \(d=4\),
and the problematic optima were concentrated near the upper endpoint
\(S\approx1\).

### First numerical diagnosis: structural nullspace

For an order-\(d\) finite-difference penalty,

\[
Q=D_d^\top D_d
\]

has exact nullity \(d\). Generic eigensolvers can return those structural zeros
as tiny positive or negative floating-point values whose exact values depend on
the LAPACK/backend implementation. Near \(S=1\), the corresponding finite
\(\lambda\) can be extremely large, so nominally zero eigenvalues can contaminate
the \(S\leftrightarrow\lambda\) inversion and derivative calculations.

The implementation was changed to canonicalize the first \(d\) eigenvalues to
exact zero and clip the positive spectrum to nonnegative values. Exact
\(S=1\) remains represented by \(\lambda=+\infty\).

This first quick run is retained only as a diagnostic record and must not be
used as a final performance table.

## 2026-09-30 — Post-nullspace quick rerun and adversarial suite

After nullspace canonicalization, the 216-surface quick benchmark improved but
still exposed a second failure mode.

Compared with the 2001-point dense reference:

- 211/216 surfaces matched every dense interior minimum;
- 5 interior minima were missed;
- mean adaptive evaluations were 64.01 versus 2001 dense evaluations
  (3.20% of the dense evaluation count);
- median absolute error in selected smoothness was approximately
  \(8.54\times10^{-5}\);
- the largest selected-\(S\) discrepancy was 0.01869.

Three missed minima had negligible effect on the selected objective. Two were
materially relevant and both occurred in the upper tail with persistent noise
and \(h=20\):

\[
(\text{seed},d,L,h)=(2,3,126,20)
\]

had dense \(S^\star\approx0.996\), adaptive
\(S^\star\approx0.97731\), and objective regret approximately 0.11654; and

\[
(\text{seed},d,L,h)=(2,4,126,20)
\]

had dense \(S^\star\approx0.997\), adaptive
\(S^\star\approx0.98576\), and objective regret approximately 0.04366.

These failures were not the earlier nullspace/LAPACK problem. Several
derivative roots were compressed into the final coarse cell of the normalized
domain near \(S=1\).

### Adversarial analytic benchmark

The adversarial quick benchmark evaluated 9 known analytic objective shapes over

\[
N\in\{63,252\},\qquad d\in\{1,2,3,4\}.
\]

Before endpoint refinement, the adaptive-\(S\) search recovered every known
local minimum, flat minimum, and boundary optimum. The 8 deliberately
constructed stationary inflections were not recovered. Mean evaluations per
case were 52.38.

The uniform log-\(\lambda\) stationary search required 273.21 mean evaluations
and missed 7 members of the deliberately close two-minimum case, in addition
to the stationary-inflection targets. The dense reference used 5001
evaluations per case.

Stationary inflections are not optimization candidates. The paper therefore
claims recovery of relevant minima under the tested designs, not certified
recovery of every stationary root of an arbitrary smooth function.

### Endpoint-aware correction

The search was augmented with a small deterministic dyadic skeleton inside the
two boundary cells before applying adaptive subdivision. This is motivated by
the compactification

\[
S\to1 \quad\Longleftrightarrow\quad \lambda\to\infty,
\]

under which several objective features can be compressed near an endpoint.
Six endpoint-refinement levels were adopted for the next preregistered quick
rerun. The two materially missed synthetic surfaces were added as regression
tests.

## 2026-09-30 — Endpoint-aware quick benchmark: defaults frozen

The final pre-paper quick rerun used the endpoint-aware search with

\[
\text{initial grid}=9,\qquad
\text{endpoint levels}=6,\qquad
\text{max depth}=8,\qquad
\Delta S_{\min}=10^{-3}.
\]

The synthetic benchmark again contained 216 surfaces and used a 2001-point
dense reference.

### Synthetic result

- dense interior minima: 227;
- matched by adaptive search: **227**;
- missed interior minima: **0**;
- surfaces with any missed minimum: **0/216**;
- positive objective regret: **0 on all 216 surfaces**;
- maximum \(|S^\star_{\text{adaptive}}-S^\star_{\text{dense}}|\):
  0.0002545;
- mean absolute \(S^\star\) error: 0.0000996;
- median absolute \(S^\star\) error: 0.0000801;
- mean adaptive evaluations: 82.84;
- median adaptive evaluations: 82;
- dense evaluations: 2001 per surface;
- mean adaptive evaluation fraction: **4.14%**.

The small negative reported regrets arise because the adaptive root refinement
can locate a minimum between dense-grid points; they are not failures relative
to the continuous objective.

The selected optimum came from an interior stationary point in 171 surfaces,
from exact \(S=0\) in 43 surfaces, and from exact \(S=1\) in 2 surfaces. This
supports retaining both exact endpoints as explicit candidates.

### Endpoint-aware adversarial result

With the same frozen endpoint-aware settings, the adversarial quick suite again
recovered every known local minimum, flat minimum, and boundary optimum. The
only unrecovered truth points were the 8 deliberately constructed stationary
inflections, which are outside the optimization target.

Mean adaptive evaluations increased from 52.38 to 75.26 after adding endpoint
refinement. This remains far below the 5001 evaluations used by the dense
reference and below the 273.21 mean evaluations of the log-\(\lambda\) search.

### Decision

The search defaults are now frozen **before** the paper-scale benchmark. The
paper-scale results will evaluate this fixed algorithm; they will not be used
to retune its search parameters.

Search-design sensitivity remains useful as a robustness analysis, but any
later sensitivity run must leave the frozen primary specification unchanged.

## 2026-09-30 — Frozen paper-scale benchmark

The confirmatory paper-scale benchmark was run **after** the primary numerical
search specification had been frozen under Decision N009.

### Synthetic benchmark

The final synthetic benchmark contained

\[
10\times 3\times 4\times 4\times 4
=
1920
\]

forecast-validation surfaces:

- 10 random seeds;
- 3 synthetic regimes: baseline, persistent, and rough;
- \(d\in\{1,2,3,4\}\);
- \(L\in\{63,126,252,504\}\);
- \(h\in\{1,5,20,60\}\);
- a 5001-point dense \(S\)-grid reference for every surface.

Across those 1920 surfaces:

- dense-reference interior minima: **2105**;
- adaptive matches: **2105/2105**;
- missed minima: **0**;
- surfaces with any missed minimum: **0/1920**;
- cases with positive objective regret beyond numerical roundoff: **0**;
- maximum positive reported regret:
  \(3.56\times10^{-14}\);
- maximum selected-\(S\) discrepancy: **0.0001018**;
- mean selected-\(S\) discrepancy: **0.0000406**;
- median selected-\(S\) discrepancy: **0.0000388**;
- 95th percentile selected-\(S\) discrepancy: **0.0000938**.

The dense grid spacing was

\[
\Delta S_{\rm dense}=\frac{1}{5000}=0.0002,
\]

so the maximum selected-\(S\) discrepancy was approximately one half of one
dense-grid cell. Negative regrets occur because root refinement can locate a
continuous minimum between dense-grid points.

The adaptive search required:

- mean evaluations: **78.35**;
- median evaluations: **75**;
- 95th percentile evaluations: **139.05**;
- maximum evaluations: **220**.

Relative to 5001 dense evaluations, the mean evaluation fraction was

\[
\frac{78.35}{5001}\approx 0.0157,
\]

or **1.57%** of the dense evaluation count.

Measured total runtime over all 1920 surfaces was:

- adaptive search: **27.29 s**;
- dense reference: **1497.85 s**.

Thus the observed total runtime ratio was approximately

\[
\frac{1497.85}{27.29}\approx 54.9.
\]

This wall-clock ratio is implementation- and hardware-dependent and should be
reported separately from the more portable evaluation-count comparison.

Exact endpoints remained empirically relevant: the selected optimum was

- interior in 1574 surfaces;
- exact \(S=0\) in 312 surfaces;
- exact \(S=1\) in 34 surfaces.

The result was stable across all tested orders, windows, horizons, and
simulation regimes: every subgroup had zero missed minima and zero meaningful
positive regret.

### Adversarial paper-scale benchmark

The adversarial paper benchmark evaluated the 9 known analytic objective
families over

\[
N\in\{63,126,252,504\},
\qquad
d\in\{1,2,3,4\},
\]

for 144 configurations per search method.

For the frozen adaptive-\(S\) search:

- relevant known minima/boundary optima detected: **240/240**;
- mean evaluations: **75.24**;
- median evaluations: **57**;
- 95th percentile evaluations: **206**;
- maximum global-optimum \(S\) error: **0.0000906**;
- maximum positive objective regret:
  \(2.17\times10^{-15}\).

The uniform log-\(\lambda\) stationary search detected **226/240** relevant
known minima and required 273.44 mean evaluations. Its failures were
concentrated in the deliberately close two-minimum construction. The
20001-point dense grid detected 240/240 relevant minima.

Neither the adaptive search nor the dense local-minimum detector identifies the
deliberately constructed stationary inflection, which is not a local minimum
and is outside the primary optimization claim.

The analytic adversarial benchmark is extremely cheap per objective evaluation.
Consequently, wall-clock timing there is dominated by method overhead and is
not used to claim that adaptive-\(S\) is faster than log-\(\lambda\). The
evaluation-count comparison and the synthetic forecast-objective benchmark are
the primary computational evidence.

### Confirmatory conclusion

The frozen primary algorithm passed the paper-scale benchmark without a
single missed dense-reference minimum across 1920 synthetic forecast surfaces
and without a single relevant missed minimum in the analytic adversarial
suite.

No further tuning of the primary search is permitted from these results.
Remaining experiments are sensitivity analyses, controlled breadth, and real
data stress tests.

## 2026-09-30 — Search-design sensitivity

The OFAT sensitivity analysis evaluated 216 common synthetic surfaces for the
frozen primary specification and 15 one-factor alternatives.

### Robust factors

Changing the following factors preserved all 228 dense-reference minima and
produced zero positive-regret cases over the sensitivity panel:

- initial grid size \(5,7,9,13\);
- maximum adaptive depth \(4,6,8,10\);
- minimum interval width \(5\times10^{-4},10^{-3},2\times10^{-3},5\times10^{-3}\);
- endpoint refinement levels \(2,4,6,8\);
- near-zero derivative ratio \(0.2\) or \(0.5\).

Several cheaper settings also passed this finite sensitivity panel, but the
primary N009 specification remains frozen and is not retuned after the
confirmatory benchmark.

### Factors with observed failure modes

Removing endpoint refinement entirely reproduced the previously diagnosed upper
tail failure mode:

- 5 missed minima in 5/216 surfaces;
- 3 positive-regret cases;
- maximum positive regret 0.11657;
- maximum selected-\(S\) error 0.01849.

Thus endpoint-aware refinement is not merely a performance optimization; it is
empirically necessary for the tested compactified search geometry.

Reducing the near-zero derivative ratio from 0.2 to 0.1 missed one secondary
local minimum in 1/216 surfaces, although it did not change the selected global
optimum. Increasing the ratio to 0.5 recovered all minima but increased mean
evaluation count from 82.84 to 92.71.

The frozen value 0.2 is therefore retained as a conservative compromise; this
is a robustness interpretation, not post-hoc retuning.

### Epsilon spacing

The paper-scale candidate sweep already evaluated

\[
\varepsilon\in\{0,0.02,0.05,0.10,0.15\}.
\]

Among the 1588 surfaces with at least one detected interior minimum, the
unspaced search produced 2108 interior candidates (mean 1.327 per surface,
maximum 4).

At \(\varepsilon=0.10\):

- 330 surfaces had at least one nearby candidate suppressed;
- 359 candidates were removed;
- 1749 representative candidates remained;
- mean representatives per affected candidate-bearing surface fell to 1.101;
- the maximum number of representatives was 3.

Because candidates are sorted by objective value before suppression, the
best detected local minimum is never removed by the spacing rule. Epsilon is
therefore treated as **post-processing for summarizing multiple minima**, not as
part of the numerical optimization algorithm.

### Sensitivity conclusion

The primary search is robust over the tested one-factor perturbations, while
the sensitivity experiment independently confirms why endpoint refinement and
a nontrivial near-zero derivative heuristic are present. No primary parameter
is changed after the frozen paper-scale benchmark.

