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
