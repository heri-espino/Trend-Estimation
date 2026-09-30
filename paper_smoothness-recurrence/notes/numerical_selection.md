# Numerical Selection on the Smoothness Domain

## 1. Smoothness compactifies the penalty domain

Let

\[
Q=D_d^\top D_d
\]

for a series of length (N). For (d\ge1), (Q) has (d) zero
eigenvalues and (N-d) positive eigenvalues
(delta_1,\ldots,delta_{N-d}).

The penalized smoother is

\[
A_\lambda=(I+\lambda Q)^{-1}.
\]

The normalized smoothness index can be written

\[
\boxed{
S(\lambda)
=
1-
\frac{1}{N-d}
\sum_{j=1}^{N-d}
\frac{1}{1+\lambda\delta_j}.
}
\]

Hence

\[
S(0)=0,
\qquad
\lim_{\lambda\to\infty}S(\lambda)=1.
\]

Moreover,

\[
\boxed{
S'(\lambda)
=
\frac{1}{N-d}
\sum_{j=1}^{N-d}
\frac{\delta_j}{(1+\lambda\delta_j)^2}
>0,
}
\]

and

\[
\boxed{
S''(\lambda)
=
-\frac{2}{N-d}
\sum_{j=1}^{N-d}
\frac{\delta_j^2}{(1+\lambda\delta_j)^3}
<0.
}
\]

Thus (S(\lambda)) is strictly increasing and concave, with

\[
\lambda\in(0,\infty)
\longleftrightarrow
S\in(0,1).
\]

## 2. Forecast objective under reparameterization

Let (f(\lambda)) denote chronological forecast CV loss and define

\[
F(S)=f(\lambda(S)).
\]

Then

\[
\boxed{
F'(S)=\frac{f'(\lambda)}{S'(\lambda)}.
}
\]

Since (S'(\lambda)>0),

\[
\boxed{
F'(S)=0
\iff
f'(\lambda)=0.
}
\]

At a stationary point,

\[
\boxed{
F''(S^\star)
=
\frac{f''(\lambda^\star)}
{[S'(\lambda^\star)]^2}.
}
\]

Therefore stationary points and their local min/max classification are
preserved by the reparameterization.

Implementation consequence: existing analytic derivatives in (lambda)
remain useful. A root search in (S) may use
(f'(\lambda(S))) because it has exactly the same interior zeros as
(F'(S)).

## 3. Proposed adaptive algorithm

1. Evaluate the exact boundary objectives for (S=0) and (S\to1).
2. Start from a small deterministic partition of ((0,1)).
3. At each sampled (S), map to (lambda(S)) and evaluate
   (f,f',f'').
4. Refine an interval when:
   - endpoint derivatives have opposite signs;
   - a sampled derivative is near zero;
   - derivative/curvature behavior suggests unresolved stationary structure;
   - the interval remains too wide for the current tolerance.
5. Recursively subdivide only marked intervals.
6. Apply Brent to derivative sign-change brackets.
7. Deduplicate roots.
8. Classify roots using (f''(\lambda^\star)).
9. Compare all local minima with both boundaries.
10. Return the global best candidate, full stationary-point set, and evaluation
    diagnostics.

## 4. Important limitation

Without additional regularity/bounding assumptions, a finite adaptive sampler
cannot certify that it found every stationary point of an arbitrary smooth
function. Do not claim such a theorem unless it is actually proved.

Instead validate empirically against a very dense GPU reference grid over many
synthetic and real CV objectives. Report missed roots, missed minima, selected
optimum disagreement, objective regret, evaluation count, and wall-clock time.

## 5. Boundary handling

Do not represent (S=1) scientifically as (0.999999).

- (S=0): exact (lambda=0).
- (S=1): (lambda\to\infty), i.e. projection onto the null space of
  (D_d).

Interior (lambda(S)) can use monotone root solving/bisection with cached
eigenvalues.
