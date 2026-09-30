# Numerical Results Log

## 2026-09-30 — First synthetic smoke and quick runs

**Status:** diagnostic. The smoke run is useful; the first quick run must be repeated after the nullspace canonicalization fix described below.

### Smoke

The synthetic smoke benchmark covered 8 surfaces with

\[
d\in\{1,2\},\qquad L\in\{63,126\},\qquad h\in\{1,5\}.
\]

All dense-reference interior minima were matched by the adaptive search. The adaptive optimum was within roughly one dense-grid cell of the dense optimum in every case.

### First quick run

The first quick run contained 216 surfaces:

- 3 seeds;
- 2 synthetic scenarios (baseline, persistent);
- \(d\in\{1,2,3,4\}\);
- \(L\in\{63,126,252\}\);
- \(h\in\{1,5,20\}\);
- 2001-point dense reference on \(S\in[0,1]\).

Observed diagnostic totals:

- dense interior minima: 229;
- matched by adaptive search: 222;
- missed: 7 minima in 6 of 216 surfaces;
- mean adaptive evaluations: 71.23 versus 2001 dense evaluations;
- median adaptive evaluations: 68.5;
- mean evaluation fraction: 3.56%;
- total adaptive-search time: 2.36 s;
- total dense-reference time: 55.70 s.

The failures were highly structured:

- \(d=1\): 0 missed minima;
- \(d=2\): 0 missed minima;
- \(d=3\): 0 missed minima;
- \(d=4\): all 7 missed minima.

The problematic optima were concentrated near the upper endpoint \(S\approx1\). Four surfaces showed a practically relevant global-optimum disagreement. The worst diagnostic case was

\[
\text{seed}=1,\quad \phi=0.8,\quad d=4,\quad L=252,\quad h=20,
\]

where the dense reference had its best grid point near \(S=0.995\), while the adaptive run on the Windows machine selected \(S=1\).

### Numerical diagnosis

For an order-\(d\) finite-difference penalty,

\[
Q=D_d^\top D_d
\]

is positive semidefinite with **exact nullity \(d\)**. Generic eigensolvers return these structural zero eigenvalues as tiny positive or negative floating-point values whose exact values depend on the LAPACK/backend implementation.

This matters when \(S\) is close to one because the corresponding finite \(\lambda\) may be extremely large. Multiplication by a nominally zero eigenvalue can then amplify machine/backend differences and alter the \(S\leftrightarrow\lambda\) inversion and derivative calculations.

The repository now canonicalizes the first \(d\) eigenvalues to exact zero and clips the positive spectrum to nonnegative values before smoothness or pure spectral calculations. Exact \(S=1\) remains represented by \(\lambda=+\infty\).

Two quick-run cases that were missed on the Windows run were added as regression tests. They are recovered on CI after canonicalization.

### Interpretation

The first quick run should **not** be used as a final performance table because it was generated before this numerical correction. It served its intended purpose: identify a failure mode before paper-scale experiments.

The next experiment is a complete repeat of --preset quick on the Windows machine after pulling the canonicalization change. We will compare the new result against this diagnostic run and only then decide whether explicit upper-boundary tail refinement is necessary.


## 2026-09-30 — Adversarial benchmark and post-nullspace quick rerun

The post-nullspace quick rerun again covered 216 forecast-validation surfaces.
Compared with the 2001-point dense reference:

- 211/216 surfaces matched every dense interior minimum;
- 5 interior minima were missed, one in each of 5 surfaces;
- mean adaptive evaluations were 64.01 versus 2001 dense evaluations
  (3.20% of the dense evaluation count);
- median absolute error in the selected smoothness was approximately
  (8.54\times10^{-5});
- the largest selected-(S) discrepancy was 0.01869.

Three of the five missed local minima had negligible effect on the selected
objective. Two were materially relevant and both occurred in the upper tail
with persistent noise and horizon (h=20):

[
(	ext{seed},d,L,h)=(2,3,126,20)
]

had dense (S^starapprox0.996), adaptive
(S^starapprox0.97731), and objective regret approximately 0.11654; and

[
(2,4,126,20)
]

had dense (S^starapprox0.997), adaptive
(S^starapprox0.98576), and objective regret approximately 0.04366.

These failures are not the earlier nullspace/LAPACK problem. They reveal a
search-design issue: several derivative roots can be compressed into the last
coarse interval of the normalized domain near (S=1).

### Adversarial analytic benchmark

The adversarial quick benchmark evaluated 9 known analytic objective shapes
over

[
Nin{63,252},qquad din{1,2,3,4}.
]

For the proposed adaptive-(S) search:

- every known local minimum, flat minimum, and boundary optimum was recovered;
- the 8 deliberately constructed stationary inflections were not recovered;
- mean evaluations per case were 52.38.

The uniform log-(lambda) stationary search required 273.21 mean
evaluations and missed 7 members of the deliberately close two-minimum case,
in addition to the stationary-inflection targets. The dense reference used
5001 evaluations per case.

The stationary-inflection result is not currently treated as an optimization
failure: such points are neither local minima nor candidate smoothness values.
The manuscript should therefore claim recovery of relevant minima, not
certified recovery of every stationary root of an arbitrary smooth function.

### Endpoint-aware correction

A regression test was added for the two materially missed synthetic surfaces.
It fails under the previous search.

The search now augments its uniform initial partition with a deterministic
dyadic skeleton inside the two boundary cells. The motivation is structural:
the normalized (S) parametrization compactifies the unbounded
(lambda)-domain, so multiple objective features can be compressed close to
(S=1). Six endpoint-refinement levels are now the default and are recorded
in benchmark metadata.

The new regression test passes on CI. The complete adversarial and synthetic
quick benchmarks must now be rerun once more. Those reruns, rather than the
results above, will determine whether the numerical defaults can be frozen.
