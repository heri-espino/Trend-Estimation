---
marp: true
theme: gaia
size: 16:9
paginate: true
math: katex
footer: "Trend reconstruction · Study M.2 · October 2026"
style: |
  section {
    background: #fcfdff;
    color: #12213a;
    font-family: "Aptos", "Segoe UI", Arial, sans-serif;
    font-size: 26px;
    padding: 48px 64px;
  }
  h1 { color: #142c4a; font-weight: 750; font-size: 1.6em; }
  h2 { color: #17666b; font-size: 1.16em; }
  strong { color: #135f67; }
  p, li { line-height: 1.28; }
  table { font-size: 0.68em; border-collapse: collapse; }
  th { background: #e6f1f4; color: #142c4a; }
  td, th { padding: 8px 12px; }
  blockquote { border-left: 6px solid #278b90; background: #eef7f8; padding: 6px 20px; font-size: 0.95em; }
  section.lead { background: #142c4a; color: #eaf8fa; }
  section.lead h1, section.lead h2 { color: #fff; }
  section.lead strong { color: #66d3d1; }
  section.tight { font-size: 21px; }
  section.figure { padding-top: 33px; font-size: 23px; }
  section.figure h1 { margin-bottom: 14px; }
  section.small { font-size: 23px; }
  section.small table { font-size: 0.68em; }
  section.divider { background: #eaf5f4; color: #132c46; }
  section.divider h1 { font-size: 2.2em; }
---

<!-- _class: lead -->

# How should we choose trend smoothness?

## A lecture on penalized least squares, pooled LOOCV and nine stochastic processes

**Study M.1 + M.2 | 1,000 independent seeds | 198,000 method evaluations**

Heriberto Espino Montelongo · Research lecture, 19 October 2026

---

# Learning goals

By the end of this lecture, we should be able to:

1. Derive the penalized least-squares trend estimator.
2. Explain CV, GCV, AICc, and Gaussian covariance ML.
3. Understand **estimating a nonzero mean of differences**.
4. Reproduce the nine-process experiment and its paired comparisons.
5. Identify why **pooling sometimes helps and sometimes harms**.

> Our target is **retrospective latent-trend reconstruction**, not future forecasting.

---

# The central statistical question

Suppose we observe a noisy sequence

$$
y_t=\tau_t+\eta_t,\qquad t=1,\ldots,N.
$$

We want a smooth estimate of the **realized latent** trend $\tau$.

The difficulty is not merely computing an estimate. It is choosing **how strongly to smooth**.

- Too little smoothing: we follow measurement noise.
- Too much smoothing: we erase real movement and structural change.

---

# What can we observe?

- We observe $y_t$, but **not** the underlying realized $\tau_t$.
- In a simulation, we deliberately generate and save both.
- In financial or economic applications, the true latent trend is generally **not available for evaluation**.

**Simulation advantage:** we can compare the chosen estimate directly with the realized simulated $\tau$, after selecting all parameters using only $y$.

![width:820px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/gaussian_reference_R1.png)

---

<!-- _class: divider -->

# Part I

## Penalized trend estimation: from assumptions to matrices

---

# Start with a roughness penalty

For an analyst-chosen difference order $d$, minimize

$$
J_\lambda(\tau)=\underbrace{\|y-\tau\|_2^2}_{\text{fit observations}}
+\lambda\underbrace{\|D_d\tau\|_2^2}_{\text{penalize changes}}.
$$

Here $D_d$ is the order-$d$ finite-difference matrix.

**Question:** what happens if the analyst changes $\lambda$?

- $\lambda=0$: interpolation of the observed series.
- $\lambda\to\infty$: restrict to the null space of $D_d$.

---

# Example: second differences

For $d=2$,

$$
(D_2\tau)_t=\tau_{t+2}-2\tau_{t+1}+\tau_t.
$$

Its matrix starts as

$$
D_2=
\begin{bmatrix}
1&-2&1&0&\cdots\\
0&1&-2&1&\cdots\\
\vdots&&\ddots&&\vdots
\end{bmatrix}.
$$

A zero second difference describes a **straight line**.

**Teaching interpretation:** penalizing $D_2\tau$ discourages rapid changes of slope.

---

# Why is the penalty matrix singular?

Define $Q=D_d^\top D_d$.

$$
x^\top Qx=\|D_dx\|^2\ge 0,
$$

so $Q$ is positive semidefinite.

Because all discrete polynomials of degree at most $d-1$ lie in $\ker(D_d)$,

$$
\operatorname{rank}(Q)=N-d,\qquad
\dim\ker(Q)=d.
$$

For $d=2$, the **two zero eigenvalues** correspond to an intercept and linear trend.

---

# Derive the solution

Differentiating the objective,

$$
\nabla_\tau J_\lambda
=-2(y-\tau)+2\lambda Q\tau=0.
$$

Therefore

$$
(I+\lambda Q)\widehat\tau_\lambda=y,
\qquad
\boxed{\widehat\tau_\lambda=H_\lambda y,}
$$

with

$$
H_\lambda=(I+\lambda Q)^{-1}.
$$

Unlike $Q$, the matrix $I+\lambda Q$ is invertible for $\lambda\ge 0$.

---

# Eigenvalues explain smoothing

Let $Q=U\operatorname{diag}(q_1,\ldots,q_N)U^\top$, where $q_j\ge0$.

Then

$$
H_\lambda
=U\operatorname{diag}\left(\frac{1}{1+\lambda q_j}\right)U^\top.
$$

- If $q_j=0$, that component is not shrunk.
- If $q_j$ is large, larger $\lambda$ suppresses it more.
- This connects a **roughness penalty** to **spectral filtering**.

The smoothing operator is linear for fixed $\lambda$ and fixed mean structure.

---

# Trace and effective degrees of freedom

The fixed-mean smoother has

$$
\mathrm{df}(\lambda)=\operatorname{tr}(H_\lambda).
$$

From the eigenvalues,

$$
\operatorname{tr}(H_\lambda)
=d+\sum_{j=1}^{N-d}\frac{1}{1+\lambda q_j}.
$$

Thus

$$
\operatorname{tr}(H_0)=N,
\qquad
\operatorname{tr}(H_\infty)=d.
$$

**Interpretation:** increasing $\lambda$ reduces effective flexibility.

---

# A normalized smoothness coordinate

Following the paper's normalized convention,

$$
\boxed{S(\lambda)=
\frac{N-\operatorname{tr}(H_\lambda)}{N-d}}.
$$

This maps the smoothing range to $[0,1]$:

- $S=0$: no smoothing.
- $S=1$: projection onto the order-$d$ null space.

**Important:** with an estimated common difference mean, this nominal $S$ is **not** the full pooled effective degrees of freedom.

---

# Teaching question: what is selected?

Three independent decisions:

1. **Statistical score:** CV, GCV, AICc, likelihood or fixed $S$.
2. **Mean assumption:** impose $\mu=0$ or estimate one common $\mu$.
3. **Numerical optimizer:** scan, bounded refinement, multibracket, etc.

> Different scores and different optimizers must not be confused.

Study M.2 keeps the existing numerical selection implementation fixed. It does **not** establish which optimizer is best.

---

<!-- _class: divider -->

# Part II

## A nonzero mean of trend differences

---

# The stochastic-trend model

In the baseline data-generating model,

$$
D_d\tau_r=\mu\mathbf1+\varepsilon_r,
\qquad
y_r=\tau_r+\eta_r,
\quad r=1,\ldots,R.
$$

- $\mu$: a **common** expected $d$-th difference.
- $\varepsilon_r$: latent difference innovations.
- $\eta_r$: measurement or observation error.

For $d=2$, nonzero $\mu$ introduces a **quadratic mean component**.

This idea of nonzero difference means predates our work; the pooled joint fit is the branch's extension.

---

# Construct a particular polynomial

For indices $t=0,\ldots,N-1$, choose

$$
p_t=\binom{t}{d}
\quad\Longrightarrow\quad D_dp=\mathbf1.
$$

Then $\tau_r=\widetilde\tau_r+\mu p$ gives

$$
D_d\widetilde\tau_r=\varepsilon_r.
$$

**Question:** should we fix $\mu=0$, plug in observed differences, or estimate $\mu$ jointly?

We compare all three strategies using observed data only.

---

# Joint penalized fitting: the objective

Given a common unknown $\mu$, minimize

$$
\sum_{r=1}^{R}
\left(
\|y_r-\tau_r\|^2+
\lambda\|D_d\tau_r-\mu\mathbf1\|^2
\right).
$$

For fixed $(\lambda,\mu)$,

$$
\widehat\tau_r
=H_\lambda y_r+\mu(I-H_\lambda)p.
$$

Then **profile $\mu$ using the same observed pool**.

---

# Profile the common difference mean

Define

$$
T_\lambda=QH_\lambda,\qquad
b_\lambda=T_\lambda p,\qquad
k_\lambda=p^\top T_\lambda p,
\quad
\bar y=\frac1R\sum_{r=1}^R y_r.
$$

The fitted mean is

$$
\boxed{
\widehat\mu_\lambda=
\frac{b_\lambda^\top\bar y}{k_\lambda}
}.
$$

This is a function of $\lambda$, so choosing the smoothing parameter also changes the fitted mean.

---

# Joint fitting changes the degrees of freedom

For the pooled fitted-mean model,

$$
\boxed{
\mathrm{EDF}_{\rm joint}(\lambda)
=R\operatorname{tr}(H_\lambda)
+\lambda\frac{\|b_\lambda\|^2}{k_\lambda}.
}
$$

Compare:

- Fixed $\mu$: effective dimension tends to $Rd$.
- One fitted common $\mu$: it tends to **$Rd+1$**.

It would be incorrect to use only $R\operatorname{tr}(H_\lambda)$ for pooled joint-mean GCV/AICc.

---

<!-- _class: divider -->

# Part III

## How do we choose the smoothness parameter?

---

# CV: delete one observation honestly

For fixed $\mu=0$ and a linear smoother, ordinary LOOCV uses

$$
\mathrm{CV}(\lambda)
=\frac1{RN}\sum_{r=1}^R\sum_{i=1}^N
\left(
\frac{y_{ri}-\widehat\tau_{ri}}
{1-(H_\lambda)_{ii}}
\right)^2.
$$

The familiar denominator corrects the in-sample residual for leverage.

**Key issue:** if $\mu$ is estimated, it must also be reestimated **without the deleted observation**.

---

# Exact fold-clean CV with estimated mean

For positive finite $\lambda$, the existing derivation gives

$$
e_{ri}^{(-ri)}
=
\frac{
(T_\lambda y_r)_i-b_{\lambda,i}\widehat\mu_\lambda
}{
(T_\lambda)_{ii}-b_{\lambda,i}^2/(Rk_\lambda)
}.
$$

Therefore

$$
\boxed{
\mathrm{CV}_{\rm joint}(\lambda)
=\frac1{RN}\sum_{r,i}\left(e_{ri}^{(-ri)}\right)^2.
}
$$

The same exact deletion-honest objective works across the pooled series, with one common fitted $\mu$.

---

# GCV: replace individual leverage by average leverage

Let $\mathrm{RSS}=\sum_{r,i}(y_{ri}-\widehat\tau_{ri})^2$ and $M=RN$.

The implementation uses

$$
\boxed{
\mathrm{GCV}(\lambda)
=\frac{\mathrm{RSS}/M}
{\left(1-\mathrm{EDF}_{\rm total}/M\right)^2}
}.
$$

- More economical surrogate for ordinary LOOCV.
- Depends on a valid model-wide EDF.
- Can behave differently when observations are autocorrelated.

The score is not a known-latent-trend MSE.

---

# AICc: in-sample fit with a complexity correction

In this codebase, for $M=RN$ and $\mathrm{df}=\mathrm{EDF}_{\rm total}$,

$$
\boxed{
\mathrm{AICc}(\lambda)=
\log(\mathrm{RSS}/M)
+\frac{2\,\mathrm{df}+1}{M-\mathrm{df}-2}.
}
$$

It is undefined when $M-\mathrm{df}\le2$.

The precise convention follows our implementation of the Cortés-Toto et al. (2017) criterion, extended to pooled observations and fitted common mean.

---

# What about BIC?

The broader branch compares CV, GCV, AICc and BIC.

However, the particular implemented BIC score has

$$
\log(\mathrm{RSS}/M)+
\mathrm{df}\frac{\log M}{M}.
$$

As $\lambda\downarrow0$, the smoother interpolates and $\mathrm{RSS}\to0$.

**Consequence:** the raw log-RSS term can drive this score to the interpolation boundary. Its numerical lower-bound behavior should not be interpreted as an unconstrained optimum.

**Study M.2 therefore uses the 11 feasible policies shown next, not BIC.**

---

# Gaussian covariance maximum likelihood

From the difference model,

$$
z_r=D_dy_r,\qquad
\operatorname{Cov}(z_r)
=\sigma_\varepsilon^2I+
\sigma_\eta^2D_dD_d^\top.
$$

Estimate variance components from **observed differences**, and set

$$
\widehat\lambda=
\frac{\widehat\sigma_\eta^2}
{\widehat\sigma_\varepsilon^2}.
$$

The branch also has a Gaussian GLS estimate of $\mu$ and a pooled observed-difference plug-in alternative.

These are quasi-likelihood approaches when the assumed covariance is wrong.

---

# The eleven feasible policies

| Mean structure | Criterion or policy |
|---|---|
| Imposed $\mu=0$ | CV, GCV, AICc, Gaussian difference ML |
| Joint fitted $\mu$ | CV, GCV, AICc |
| Joint fitted $\mu$ | Gaussian GLS mean + variance ML |
| Pooled observed-difference plug-in $\mu$ | Plug-in mean + our Gaussian variance ML |
| Joint fitted $\mu$ | Preset $S=0.5$, preset $S=0.8$ |

**Total: 11.**

No method is permitted to use the simulated true $\tau$ when selecting $\mu$ or $\lambda$.

---

# Historical attribution

**Existing work:** Guerrero's stochastic-trend framework allows a nonzero mean of differences. Cortés-Toto, Guerrero and Reyes (2017) study alternative optimality criteria for penalized trend smoothness.

**This project's implementation:** pooled common-$\lambda$ comparisons across $R$ series, fitted common-$\mu$ formulas, exact fold-clean pooled PRESS, and the nine-process simulation experiment.

Our experiments do **not** demonstrate that every one of these components is novel in the global literature.

---

<!-- _class: divider -->

# Part IV

## Designing the experiments: change the process, then replicate

---

# First: deliberately generate the latent truth

The default baseline of Study M.2 is

$$
N=80,\quad d=2,\quad
\mu=0.04,\quad
\sigma_\varepsilon=0.12,\quad
\sigma_\eta=0.80.
$$

We generate **three** latent integrated trends and observation-noise sequences using a common Gaussian random source.

For the reference:

$$
\varepsilon_{rt}\sim N(0,0.12^2),
\quad\eta_{rt}\sim N(0,0.80^2).
$$

The other eight examples change the signal, the noise, or the pooling assumptions.

---

# Nine processes, three mechanisms of departure

| Signal shape changes | Observation errors change | Pooling structure changes |
|---|---|---|
| Smooth sinusoidal cycle | Isolated outliers | Unequal series noise SD |
| Change in slope | AR(1) correlation | Common observation shock |
| True level jump | Variance regime switch | Gaussian reference baseline |

Each case holds as much of the **underlying random draw** fixed as possible while modifying the named mechanism.

This makes process-to-process comparisons paired, not independent.

---

# Gallery 01: correctly specified Gaussian reference

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/gaussian_reference_R3.png)

A single simulated realization reveals the difference between fitted trend lines. **It cannot estimate expected reconstruction risk.**

---

# Gallery 02: smooth cycle

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/smooth_cycle_R3.png)

The sinusoidal addition changes the mean structure of second differences. Oversmoothing can erase genuine oscillations.

---

# Gallery 03: change in slope

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/slope_break_R3.png)

The generating signal acquires a kink: a deterministic change in slope halfway through the observed interval.

---

# Gallery 04: true level jump

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/level_jump_R3.png)

This is a **jump in the simulated latent trend itself**. The correct reconstruction should respond to it, not remove it as noise.

---

# Gallery 05: observation-only outliers

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/observation_outliers_R3.png)

Here the realized latent trend has **no added jump**: only selected observed measurements are contaminated.

---

# Gallery 06: autocorrelated measurement noise

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/ar1_observation_R3.png)

Observation noise is generated as stationary AR(1), with $\phi=0.85$. Adjacent errors carry related information.

---

# Gallery 07: change in observation variance

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/variance_regime_R3.png)

The observation-error scale is multiplied by 0.45 in the first half and 1.35 in the second half.

---

# Gallery 08: unequal noise across pooled series

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/heterogeneous_pool_R3.png)

The three observation-noise standard deviations are **0.25, 0.80 and 1.50**. Should one common smoothing parameter fit all three?

---

# Gallery 09: shared observation shocks

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/shared_observation_shock_R3.png)

The observation errors share a common factor; the resulting cross-series noise correlation is **0.70**.

---

# Why we did not stop after nine pictures

The illustrated seed may show one method winning **by chance**.

The initial gallery used one seed and produced

$$
9\text{ mechanisms}\times2\text{ pool sizes}\times11\text{ methods}
=\boxed{198\text{ evaluations}}.
$$

We then fixed the processes and policies and asked a more reliable question:

> Which procedures have lower **mean reconstruction error** over independent repetitions?

---

# The 1,000-seed design

Study M.2 uses 1,000 **new** seed indices. Within each:

- Draw one underlying innovation pool.
- Apply all nine paired process modifications.
- Evaluate both $R=1$ and $R=3$ on nested series.
- Fit all 11 policies without access to true $\tau$.
- Save realized latent reconstruction losses.

$$
1000\times9\times2\times11
=\boxed{198{,}000\text{ method evaluations}}.
$$

There are **1,000 independent seed units**, not 198,000 independent data draws.

---

# What do we measure?

For seed $j$, process $c$, pool size $R$, and policy $m$,

$$
L_{j,c,R,m}=
\frac1{RN}\sum_{r=1}^{R}\sum_{t=1}^{N}
(\widehat\tau_{j,c,R,m,r,t}-\tau_{j,c,r,t})^2.
$$

The estimated conditional reconstruction risk is

$$
\boxed{\widehat{\mathcal R}_{c,R,m}
=\frac1{1000}\sum_{j=1}^{1000}L_{j,c,R,m}.}
$$

Also report MAE, median MSE, 90th-percentile MSE, fitted $\mu$ and selected $S$.

---

# Why paired comparisons?

Within seed $j$, every method sees the same simulated observations.

For methods $A,B$, form

$$
\delta_j=L_{j,c,R,A}-L_{j,c,R,B}
$$

and then estimate

$$
\widehat\Delta_{A-B}=\frac1{1000}\sum_{j=1}^{1000}\delta_j.
$$

Negative values favor $A$.

A confidence interval for **paired differences** is usually more informative than comparing two unrelated marginal intervals.

---

# What does Holm correction do?

There are

$$
9\times2\times\binom{11}{2}=\boxed{990}
$$

method pairs.

We compute nominal paired $t$-test p-values, then apply **one global Holm adjustment** over the 990 comparisons.

- Pointwise 95% confidence intervals remain pointwise.
- The adjusted p-values address multiplicity for this reported family.
- A statistically detectable difference may be **practically tiny**.

The aggregate audit found 787/990 adjusted p-values below 0.05; many reflect obviously poor fixed-$S$ alternatives, **not 787 independent discoveries**.

---

<!-- _class: divider -->

# Part V

## Study M.2: reading the actual results

---

<!-- _class: figure -->

# All nine mechanisms — R = 1

![width:1130px](../figures/study_m2_relative_excess_mse_R1.svg)

Percentage excess mean-MSE above the best mean-MSE policy **within the same process**. **Color does not encode statistical significance.**

---

<!-- _class: figure -->

# All nine mechanisms — R = 3

![width:1130px](../figures/study_m2_relative_excess_mse_R3.svg)

The apparent winner changes across processes. The figure compares **relative regret**, not raw MSE on a common scale.

---

<!-- _class: tight -->

# Lowest mean MSE in each process, R=1

| Process | First-place policy | Mean MSE |
|---|---|---:|
| Gaussian reference | Pooled plug-in + ML | **0.09953** |
| Smooth sinusoid | Preset $S=.8$ | **0.12217** |
| Slope break | Pooled plug-in + ML | **0.10779** |
| True latent jump | Preset $S=.5$ | **0.31674** |
| Observation outliers | Joint AICc | **0.17469** |
| AR(1) observations | Preset $S=.8$ | **0.49066** |
| Changing variance | Pooled plug-in + ML | **0.10249** |
| Unequal pool noise | Pooled plug-in + ML | **0.01697** |
| Shared observation shock | Pooled plug-in + ML | **0.10214** |

**These are sample risk minima; significance must be tested separately.**

---

<!-- _class: tight -->

# Lowest mean MSE in each process, R=3

| Process | First-place policy | Mean MSE |
|---|---|---:|
| Gaussian reference | Pooled plug-in + ML | **0.09674** |
| Smooth sinusoid | Preset $S=.8$ | **0.12327** |
| Slope break | Pooled plug-in + ML | **0.10642** |
| True latent jump | Preset $S=.5$ | **0.31671** |
| Observation outliers | Pooled plug-in + ML | **0.16961** |
| AR(1) observations | Preset $S=.8$ | **0.49615** |
| Changing variance | Gaussian GLS/ML | **0.09785** |
| Unequal pool noise | Gaussian GLS/ML | **0.13598** |
| Shared observation shock | Gaussian GLS/ML | **0.09827** |

**R3 GLS/ML and plug-in ML often differ by only $10^{-5}$–$10^{-4}$ MSE.**

---

# A first-place rank can be an almost exact tie

In the Gaussian baseline at $R=3$:

| Policy | Mean latent MSE |
|---|---:|
| Pooled plug-in mean + ML | **0.0967383** |
| Gaussian GLS/ML fitted mean | **0.0967548** |
| Joint CV | 0.098430 |
| Joint AICc | 0.09889 |

Plug-in minus GLS:

$$
\widehat\Delta=-0.00001653
$$

95% paired CI: **[−0.00013802, +0.00010495]**. Global Holm-adjusted $p=1$.

**Conclusion:** practically and statistically indistinguishable in this design.

---

# Which R3 top-vs-second differences survive Holm?

Only two of the nine sample first places are clearly separated from the nearest competitor after global Holm adjustment:

- **True latent level jump:** preset $S=.5$ beats zero-mean GCV.
- **AR(1) observation errors:** preset $S=.8$ beats joint AICc.

For the other seven, the top-two gap is not familywise significant.

> "Rank 1" is an empirical ordering, not a theorem or a universal recommendation.

---

# A genuine jump rewards less smoothing

Under the +7 **true level jump**, $R=3$:

| Policy | Mean MSE | Median nominal $S$ |
|---|---:|---:|
| **Preset $S=.5$** | **0.31671** | .500 |
| GCV, $\mu=0$ | 0.33395 | .727 |
| Joint CV | 0.33641 | .734 |
| Gaussian GLS/ML | 0.41371 | .827 |

Preset $S=.5$ minus zero-mean GCV:

$$
-0.01724,\qquad95\%\ \mathrm{CI}=[-0.01920,-0.01527].
$$

The distinction survives global Holm adjustment.

---

<!-- _class: figure -->

# The genuine jump, illustrated

![width:1070px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/level_jump_R3.png)

For a **true structural jump**, aggressive global smoothing introduces substantial bias near the discontinuity.

---

# An observation spike is a different problem

In the outlier case, the true trend is not changed.

Under $R=1$:

| Policy | Mean MSE | 90th percentile MSE |
|---|---:|---:|
| **Joint AICc** | **0.17469** | 0.25455 |
| Joint CV | 0.18348 | 0.27232 |
| Gaussian GLS/ML | 0.28195 | **0.69367** |

The single-series Gaussian ML estimator suffers some very poor realizations.

**Do not confuse smoothing under contaminated observations with explicit robust regression.** None of these is a robust M-estimator.

---

<!-- _class: figure -->

# Observation outliers, illustrated

![width:1070px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/observation_outliers_R1.png)

Compare with the preceding true-jump slide. The same kind of sharp visual disturbance can demand the **opposite** inferential decision.

---

# Strongly autocorrelated noise changes the game

For AR(1) measurement errors with $\phi=.85$, $R=3$:

| Policy | Median $S$ | Mean MSE |
|---|---:|---:|
| Joint GCV | .422 | 0.58183 |
| Joint CV | .445 | 0.57850 |
| Gaussian GLS/ML | .658 | 0.54295 |
| Joint AICc | .707 | 0.52978 |
| **Preset $S=.8$** | **.800** | **0.49615** |

Joint point-LOOCV follows correlated observation fluctuations too closely **in this DGP**.

---

# The AR(1) advantage is large

Under $R=3$, relative to preset $S=.8$:

- Joint CV has **0.08235 higher** mean MSE.
- Joint AICc has **0.03363 higher** mean MSE.
- Gaussian GLS/ML has **0.04680 higher** mean MSE.

All three paired differences remain significant after Holm correction.

Preset $S=.8$ is the lowest realized-MSE policy in **100% of the 1,000 R3 seeds** among the eleven policies tested.

This does **not** establish that $S=.8$ is generally optimal at other correlation levels.

---

<!-- _class: figure -->

# AR(1) example: reconstructed curves

![width:1050px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/ar1_observation_R3.png)

A method can fit observed $y$ well but reconstruct the **latent** $\tau$ poorly when measurement errors are serially dependent.

---

# How do smooth cycles differ?

For the sinusoidal trend at $R=3$:

- Preset $S=.8$: mean MSE **0.123268**.
- Zero-mean GCV: mean MSE **0.123526**.

Their paired CI includes zero; global Holm $p=1$.

However, preset $S=.8$ versus **joint** CV has difference **−0.00248**, CI [−0.00281,−0.00216], significant after Holm.

**Lesson:** estimating a mean of differences is a modeling choice; it can interact with periodic misspecification.

---

# What did we learn about estimating μ?

Joint mean estimation adds a degree of freedom, and the fitted mean changes with $\lambda$.

- In the Gaussian reference, mean fitted $\mu$ is close to the baseline **0.04**.
- In the smooth-cycle case, joint CV fitted mean averages approximately **0.0345**.
- The pooled observed-difference plug-in averages approximately **0.0291** in that cycle case.

The constant-$D_2$-mean assumption is not literally true after adding the sinusoid.

**We should not claim that joint fitting is always superior to $\mu=0$.**

---

<!-- _class: divider -->

# Part VI

## Pooling: when does three-series fitting help?

---

# Define the SAME-series pooling comparison

Let $\widehat\tau^{(1)}_{R=1}$ be estimated from the first series alone and $\widehat\tau^{(1)}_{R=3}$ from all three series.

We compare

$$
\boxed{
\widehat\Delta_{\rm pool}
=\frac1{1000}\sum_{j=1}^{1000}
\left[
\frac{\|\widehat\tau^{(1)}_{R=3,j}-\tau^{(1)}_j\|^2}{N}
-\frac{\|\widehat\tau^{(1)}_{R=1,j}-\tau^{(1)}_j\|^2}{N}
\right].
}
$$

- **Negative:** pooling helps the first series.
- **Positive:** pooling harms the first series.

Do not compare R3 *average across three series* against R1 when their noise levels differ.

---

<!-- _class: tight -->

# Pooling effects on the identical first series

| Process / policy | R1 first MSE | R3 first MSE | Difference (R3−R1) |
|---|---:|---:|---:|
| Gaussian / GLS ML | 0.11854 | 0.09538 | **−0.02316** |
| Gaussian / joint CV | 0.10946 | 0.09696 | **−0.01250** |
| Outliers / GLS ML | 0.28195 | 0.16703 | **−0.11492** |
| Shared shock / GLS ML | 0.11791 | 0.09843 | **−0.01948** |
| Unequal SD / GLS ML | **0.01701** | **0.04037** | **+0.02336** |
| Unequal SD / joint CV | 0.01851 | 0.03942 | **+0.02090** |
| AR(1) / joint AICc | 0.52236 | 0.52441 | **+0.00206** |

These are paired mean errors; the full 99-row file also contains pointwise intervals and win fractions.

---

# The strongest warning: heterogeneous pooling

One common smoothing parameter is fitted to three series with measurement-noise SDs

$$
(\sigma_{\eta,1},\sigma_{\eta,2},\sigma_{\eta,3})
=(0.25,\ 0.80,\ 1.50).
$$

The **cleanest** series is the first.

Using GLS/ML:

$$
\mathrm{MSE}_{R=1}=0.01701,\qquad
\mathrm{MSE}_{R=3}=0.04037.
$$

Its paired deterioration is **+0.02336**, pointwise 95% CI **[+0.02237,+0.02435]**.

---

# Why does the first-series MSE grow?

For the heterogeneous case:

- GLS/ML median nominal $S$ changes from **0.758** at R1 to **0.888** at R3.
- Joint CV's median $S$ changes from **0.751** to **0.888**.

The two noisier series drive the **common** parameter toward heavier smoothing.

A parameter good for the pooled sample is not necessarily good for the lowest-noise member.

> Pooling may reduce estimation variability while increasing mismatch bias.

---

<!-- _class: figure -->

# Heterogeneous pooling, illustrated

![width:1040px](../../../results/pooled_loocv_smoothness/process_examples/gallery_001/heterogeneous_pool_R3.png)

The qualitative question is not "does pooling help on average?" but "**which series benefits, and which gets damaged?**"

---

# Shared noise is not the same as unequal noise

For observation-noise correlation **0.70** across series, GLS/ML:

$$
\mathrm{MSE}_{R=1}^{(1)}=0.11791,
\qquad
\mathrm{MSE}_{R=3}^{(1)}=0.09843.
$$

The paired improvement is **−0.01948**, pointwise CI **[−0.02411,−0.01484]**.

This example still gains from pooling despite a violated independence assumption.

**It does not prove pooling is safe for every cross-series dependence structure.**

---

<!-- _class: divider -->

# Part VII

## Interpretation, uncertainty and next research questions

---

# One seed versus 1,000 seeds

The best method by **realized MSE in the single-seed gallery** matched the lowest **mean MSE over 1,000 independent seeds** in only

$$
\boxed{7\text{ of }18\text{ process–pool combinations}}.
$$

This is **descriptive agreement**, not a significance test or 18 independent trials.

The more interesting output is the *risk difference across independent seeds*, with uncertainty.

---

# What is robustly supported?

Within these nine specified data-generating mechanisms:

1. **AR(1) measurement noise** leads ordinary point-CV/GCV to select weaker smoothing than the fixed-$S$ policy that attains lower latent MSE.
2. A **real structural level jump** favors less smoothing than regular Gaussian likelihood in this setup.
3. **Gaussian GLS/ML versus pooled plug-in ML** is frequently a near tie when R=3.
4. **Pooling with a common parameter can harm a cleaner series** if the pooled noise levels differ strongly.

None is a claim of universal statistical dominance.

---

# What this experiment does NOT establish

- How to forecast future prices or returns at horizon $h$.
- Which method recovers the **true real-world** latent financial trend.
- A method that detects structural breaks or robustly rejects outliers.
- A universally optimal $\lambda$ or $S$.
- Guaranteed global numerical minimization by the score-grid optimizer.
- Full independent reaggregation of 198k raw rows: those compressed shards remain user-local.

The evidence is conditional on $N=80$, $d=2$, specified amplitudes and noise mechanisms.

---

# What is the next meaningful experiment?

A **one-factor sensitivity analysis**, not more identical-case seeds:

1. Sweep measurement-error AR(1) correlation $\phi$, add blocked CV or correctly specified covariance baselines.
2. Vary **latent jump size** separately from **outlier size**.
3. Vary **across-series noise ratios** and compare common $\lambda$ against weighted or series-specific smoothing.

These target mechanisms suggested by the completed study; they are **not yet executed results**.

---

# Reproducibility: what is actually on GitHub?

- One-seed gallery: **18 trajectory figures**, 198 method evaluations.
- Study M.2: **1,000 independent seeds**, 198,000 method evaluations.
- Committed aggregates: **198 risk rows, 990 method pairs, 99 pooling effects**.
- Manifest: **COMPLETE**, 40/40 seed chunks, with source SHA and software versions.
- Independent compact-table consistency audit: **passed**.

The raw compressed per-seed shards are *excluded from Git*. **Back them up locally** if full row-level reaggregation is required.

---

# Discussion questions for the audience

1. Would blocked CV reduce the apparent AR(1) undersmoothing?
2. Should the smoothing penalty itself adapt to a genuine jump?
3. When should a series receive its own $\lambda$, rather than a pooled one?
4. Can we estimate measurement-error covariance sufficiently accurately to guide pooling?
5. How could we evaluate these choices when **no true latent trend is observed**?

---

<!-- _class: lead -->

# Main takeaway

**There is no universal smoothness selector.**

The choice depends on the latent trend's structure, the observation error's dependence, and the validity of pooling assumptions.

**Statistical objective, mean model, numerical optimizer and evaluation target are different things.**

---

<!-- _class: tight -->

# Source notes and reproducibility

- **Study M.2 results:** notes/STUDY_M2_1000_SEED_PROCESS_RESULTS_2026-10-19.md
- **M.2 design:** notes/STUDY_M2_PROCESS_DIVERSITY_INDEPENDENT_SEEDS_2026-10-19.md
- **Nine-process generator:** experiments/pooled_loocv_smoothness/run_process_examples.py
- **Seeded runner:** experiments/pooled_loocv_smoothness/run_process_monte_carlo.py
- **Mathematical methods:** experiments/pooled_loocv_smoothness/cortes_optimality_criteria.py
- **Committed data:** results/pooled_loocv_smoothness/process_examples/seed_study_1000_v1/
- **Literature anchors:** Guerrero (2007); Cortés-Toto, Guerrero and Reyes (2017).

The full paths and stable source code SHA are documented in the accompanying presentation README and research notes.

