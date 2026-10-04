# Sturm-Sequence Mini-Check for the Forecast-Loss Objective

Date: 2026-10-03

## Purpose

This is a deliberately small symbolic check of the structural claim documented
in \`notes/numerical_selection.md\`: for fixed \(d,L,h\), the pure
zero-drift forecast-MSE objective is a rational function of \(\lambda\), so its
stationary points are the nonnegative real roots of a finite-degree polynomial
numerator.

The check is not intended as the production optimizer. Its purpose is to verify
on one exact nontrivial example that:

1. the symbolic forecast loss is rational;
2. its derivative numerator is a polynomial;
3. a Sturm sequence counts the positive stationary roots exactly;
4. a numerical sign-change scan plus Brent recovers the same simple roots;
5. the symbolic objective and first two derivatives agree with the production
   implementation.

Script:

\`experiments/numerical_smoothness_selection/run_sturm_minicheck.py\`

## Exact test case

The frozen toy case uses

\[
L=6,\qquad d=2,\qquad h=2,
\]

with

\[
y_{\rm past}=(4,0,-2,-1,3,1)^\top,
\qquad
y_{\rm future}=(0,1)^\top.
\]

The exact zero-drift forecast operator is built with integer arithmetic, and

\[
H_\lambda=(I+\lambda D_2^\top D_2)^{-1}
\]

is formed symbolically with SymPy.

For this case the exact forecast MSE simplifies to

\[
f(\lambda)
=
\frac{
8450\lambda^8
-129930\lambda^7
+2682435\lambda^6
+865838\lambda^5
-24763\lambda^4
-20766\lambda^3
+901\lambda^2
+378\lambda
+17
}{
2(3\lambda^2+8\lambda+1)^2(35\lambda^2+16\lambda+1)^2
}.
\]

The denominator is strictly positive on \(\lambda\ge0\), so there are no poles
on the admissible domain.

The derivative numerator is the degree-10 polynomial

\[
\begin{aligned}
R(\lambda)
={}&
9592925\lambda^{10}
-300158795\lambda^9
-168113655\lambda^8
+300725008\lambda^7\\
&+213740018\lambda^6
+49150530\lambda^5
+2563890\lambda^4
-765384\lambda^3\\
&-141999\lambda^2
-9279\lambda
-219.
\end{aligned}
\]

Thus the stationary-point problem is exactly a polynomial root problem for this
configuration.

## Sturm result

For the exact Sturm sequence of \(R\),

\[
V(0^+)=5,
\qquad
V(+\infty)=2.
\]

By Sturm's theorem, the number of distinct positive roots is therefore

\[
\boxed{
V(0^+)-V(+\infty)=3.
}
\]

Their numerical locations are approximately

\[
\lambda_1=0.146706269970,
\qquad
\lambda_2=1.101542792611,
\qquad
\lambda_3=31.808860111816.
\]

The second derivative classifies them as

\[
\boxed{
\text{minimum},\quad
\text{maximum},\quad
\text{minimum}.
}
\]

A log-spaced derivative scan followed by Brent refinement recovers the same
three roots to numerical precision.

## Interpretation

This mini-check supports the structural point that the production problem is
not analogous to a pathological smooth function with infinitely accumulating
oscillations. In this exact example the stationary-point set is finite and can
be counted before numerical refinement.

It also clarifies the role of Brent:

\[
\text{Sturm / root isolation}
\rightarrow
\text{certified root intervals}
\rightarrow
\text{Brent refinement}.
\]

That would be a stronger architecture than relying on sampled sign changes
alone.

## What this does *not* establish

One toy example is not yet a theorem for every production configuration.
Before upgrading the paper to a certified-root claim, we still need to:

- formalize the rational representation for the pooled fixed-\((d,L,h)\)
  objective in the notation of the paper;
- handle repeated eigenvalues and algebraic cancellations cleanly;
- characterize degenerate cases such as \(R\equiv0\);
- decide whether exact polynomial construction is computationally practical for
  paper-scale \(L\);
- study numerical conditioning if coefficients are formed in floating point;
- implement a robust root-isolation route for realistic configurations.

The present conclusion is narrower: **the Sturm approach is viable in principle,
and an exact nontrivial mini-check behaves exactly as the rational-structure
argument predicts.**

## Run

If SymPy is not installed in the environment:

\`\`\`bash
python -m pip install -e ".[symbolic]"
\`\`\`

Then run:

\`\`\`bash
python experiments/numerical_smoothness_selection/run_sturm_minicheck.py
\`\`\`

The script exits with an assertion failure if the Sturm count, Brent roots,
root classification, or production objective/derivative comparisons disagree.
