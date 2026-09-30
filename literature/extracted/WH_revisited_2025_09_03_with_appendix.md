---
id: "WH_revisited_2025_09_03_with_appendix"
source_pdf: "../pdf/WH_revisited_2025_09_03_with_appendix.pdf"
source_filename: "WH_revisited_2025_09_03_with_appendix.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/WH_revisited_2025_09_03_with_appendix.references.md"
---

<!-- p:1 -->

## Whittaker-Henderson Smoothing Revisited: A Modern Statistical Framework for Practical Use

Guillaume Biessy, PhD, LinkPact†and Sorbonne Université

September 3, 2025

Introduced over a century ago, Whittaker-Henderson smoothing remains widely used by actuaries in constructing one-dimensional and two-dimensional experience tables for mortality, disability and other life insurance risks. In this paper, we reinterpret this smoothing technique within a modern statistical framework and address six practically relevant questions about its use.

First, we adopt a Bayesian perspective on this method to construct credible intervals. Second, in the context of survival analysis, we clarify how to choose the observation and weight vectors by linking the smoothing technique to a maximum likelihood estimator. Third, we improve accuracy by relaxing the method's reliance on an implicit normal approximation. Fourth, we select the smoothing parameters by maximizing a marginal likelihood function. Fifth, we improve computational efficiency when dealing with numerous observation points and consequently parameters. Finally, we develop an extrapolation procedure that ensures consistency between estimated and predicted values through constraints.

#### Table of contents

|   1 | Introduction                                               | 3                                 |
|-----|------------------------------------------------------------|-----------------------------------|
|     | 1.1 A brief reminder of WH smoothing mathematical          | formulation . . . . . . . . . . 3 |
|     | 1.2 Structure of the paper . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . 5 |
|   2 | How to measure uncertainty in smoothing results?           | 9                                 |
|     | 2.1 Maximum a posteriori estimate . . . . . . . . . . .    | . . . . . . . . . . . . . . . . 9 |

guillaume.biessy78@gmail.com

‡Sorbonne Université, CNRS, Laboratoire de Probabilités, Statistique et Modélisation, LPSM, 75005 Paris, France

†LinkPact, 75015 Paris, France

3


5

9


<!-- p:2 -->


| 2.2                                                                  | Posterior distribution of θ &#124; y . . . . . . . . . . . . . . . . . . .   | . . . . . . . . . 9   |
|----------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------|
| 2.3                                                                  | Consequence for the WH smoothing . . . . . . . . . . . . . . .               | . . . . . . . . . 10  |
| 3 Which observation and weight vectors to use?                       | 3 Which observation and weight vectors to use?                               | 10                    |
| 3.1                                                                  | Survival analysis framework . . . . . . . . . . . . . . . . . . . .          | . . . . . . . . . 10  |
| 3.2                                                                  | Likelihood equations . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . . . . 11  |
| 3.3                                                                  | Consequence for the WH smoothing . . . . . . . . . . . . . . .               | . . . . . . . . . 12  |
| 4 How to improve the accuracy of smoothing with limited data volume? | 4 How to improve the accuracy of smoothing with limited data volume?         | 12                    |
| 4.1                                                                  | Generalized Whittaker-Henderson smoothing . . . . . . . . . .                | . . . . . . . . . 12  |
| 4.2                                                                  | Impact of the normal approximation in the original smoothing                 | . . . . . . . . . 13  |
| 5 How to select the smoothing parameters?                            | 5 How to select the smoothing parameters?                                    | 15                    |
| 5.1                                                                  | Impact of smoothing parameter choice . . . . . . . . . . . . . .             | . . . . . . . . . 15  |
| 5.2                                                                  | Statistical criteria for parameter selection . . . . . . . . . . . .         | . . . . . . . . . 16  |
| 5.3                                                                  | Selection in the original smoothing . . . . . . . . . . . . . . . .          | . . . . . . . . . 18  |
| 5.4                                                                  | Selection in the generalized smoothing . . . . . . . . . . . . . .           | . . . . . . . . . 19  |
| 5.5                                                                  | Algorithms for the maximization of the marginal likelihood . .               | . . . . . . . . . 20  |
| 5.6                                                                  | Performance comparison . . . . . . . . . . . . . . . . . . . . . .           | . . . . . . . . . 21  |
| 6                                                                    | How to improve smoothing computational efficiency?                           | 23                    |
| 6.1                                                                  | Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . . . . 23  |
| 6.2                                                                  | Practical computation for penalized smoothers . . . . . . . . .              | . . . . . . . . . 25  |
| 6.3                                                                  | Banded optimization for WH smoothing . . . . . . . . . . . . .               | . . . . . . . . . 27  |
| 6.4                                                                  | Natural parameterization and rank reduction of WH smoothing                  | . . . . . . . . . 29  |
| 7 How                                                                | to extrapolate the smoothing?                                                | 34                    |
| 7.1                                                                  | Defining the extrapolation of the smoothing . . . . . . . . . . .            | . . . . . . . . . 34  |
| 7.2                                                                  | Unconstrained solution for the 1D case . . . . . . . . . . . . . .           | . . . . . . . . . 36  |
| 7.3                                                                  | Constrained solution for the 2D case . . . . . . . . . . . . . . .           | . . . . . . . . . 37  |
| 8 Discussion                                                         | 8 Discussion                                                                 | 40                    |
| References                                                           | References                                                                   | 43                    |
| Appendices                                                           | Appendices                                                                   | 46                    |
| A Exposure computation in the survival analysis framework            | . . .                                                                        | . . . . . . . . . 46  |
| B                                                                    | Simulated datasets . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . . . . 48  |
| C                                                                    | Derivation of marginal likelihood and LAML . . . . . . . . . .               | . . . . . . . . . 52  |
| D                                                                    | Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . . . . 54  |
| E                                                                    | Illustrations for the natural parameterization of WH smoothing               | . . . . . . . . . 56  |
| F                                                                    | Derivation of constrained extrapolation in the 2D case . . . . .             | . . . . . . . . . 60  |
| G                                                                    | Choosing the order of the difference matrices . . . . . . . . . .            | . . . . . . . . . 62  |

62


<!-- p:3 -->


#### Notations

In this paper, vectors are denoted in boldface and matrix names in uppercase letters. If y is a vector and A is a matrix, Var(y) denotes the variance-covariance matrix associated with y, diag(A) represents the diagonal of matrix A, and Diag(y) is the diagonal matrix such that diag(Diag(y)) = y. The sum of the diagonal elements of A is denoted as tr(A) and its transpose as AT. In the case where A is invertible, A−1 denotes its inverse and |A| denotes the product of the eigenvalues of A. For a non-invertible matrix A, A− refers to the Moore-Penrose dsss n  o e -  o nrd  sp o+ e  o s-sng the eigendecomposition as A = UΣVT, where U and V are orthogonal matrices and Σ is a diagonal matrix containing the eigenvalues of A, and by denoting Σ− as the matrix obtained by replacing the non-zero eigenvalues in Σ with their inverses leaving the zero eigenvalues unchanged, the pseudo-inverse is given by A− = VΣ-UT. The Kronecker product of two matrices A and B is denoted as A ⊗ B, and their Hadamard (element-wise) product, is denoted as A  B. [x] denotes the greatest integer less than or equal to x ∈ R. Finally, the symbol ∝ denotes proportionality between the expressions on both sides.

## 1 Introduction

Whittaker-Henderson (WH) smoothing is a graduation method designed to mitigate the effects of sampling fluctuations in a vector of evenly spaced discrete observations. Although this method was originally proposed by Bohlmann (1899), it is named after Whittaker (1923), who applied it to graduate mortality tables, and Henderson (1924), who popularized it among actuaries in the United States. The method was later extended to two dimensions by Knorr (1984). WH smoothing may be used to build experience tables for a broad spectrum of life insurance risks, such as mortality, disability, long-term care, lapse, mortgage default and unemployment. We begin with a brief overview of the method before outlining the structure and main contributions of the paper.

### 1.1 A brief reminder of WH smoothing mathematical formulation

#### The one-dimensional case

Let y be a vector of observations and w a vector of positive weights, both of size n. The estimator associated with Whittaker-Henderson smoothing is given by:

$$\hat { y } = \arg \min _ { \theta } \{ F ( y , w , \theta ) + R _ { \lambda , q } ( \theta ) \} \\$$

where:


<!-- p:4 -->


- n · F(y, w, θ) = Σ wi(yi − θi)2 represents a fidelity criterion with respect to the observations, i=1
- n−q · Rλ,q(θ) = λ ∑ (∆aθ)2 represents a smoothness criterion. i=1

In the latter expression, λ ≥ 0 is a smoothing parameter and ∆a denotes the forward difference operator of order q, such that for any i ∈ {1, . . . , n − q}:

$$( \Delta ^ { q } \theta ) _ { i } = \sum _ { k = 0 } ^ { q } \left ( \begin{matrix} q \\ k \end{matrix} \right ) ( - 1 ) ^ { q - k } \theta _ { i + k } .$$

Define W = Diag(w), the diagonal matrix of weights, and Dn,q as the order q difference matrix of dimensions (n − q) × n, such that (Dn,qθ)i = (∆aθ)i for all i ∈ [1, n − q]. The first- and second-order difference matrices are given by:

$$D _ { n , 1 } = \begin{bmatrix} - 1 & 1 & 0 & \dots & 0 \\ 0 & - 1 & 1 & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & \ddots \\ 0 & \dots & 0 & - 1 & 1 \end{bmatrix} \quad \text {and} \ D _ { n , 2 } = \begin{bmatrix} 1 & - 2 & 1 & 0 & \dots & 0 \\ 0 & 1 & - 2 & 1 & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & \ddots & \ddots \\ 0 & \dots & 0 & 1 & - 2 & 1 \end{bmatrix} .$$

while higher-order difference matrices follow the recursive formula Dn,q = Dn-1,q-1Dn,1. The fidelity and smoothness criteria can be rewritten with matrix notations as:

$$F ( y , w , \theta ) = ( y - \theta ) ^ { T } W ( y - \theta ) \quad \text {and} \quad R _ { \lambda , q } ( \theta ) = \lambda \theta ^ { T } D _ { n , q } ^ { T } D _ { n , q } \theta$$

and the WH smoothing estimator thus becomes:

$$\hat { y } = \arg \min _ { \theta } \left \{ ( y - \theta ) ^ { T } W ( y - \theta ) + \theta ^ { T } P _ { \lambda } \theta \right \}$$

where Pλ = λDx,9 qDn,q. n,q

#### The two-dimensional case

In the two-dimensional case, consider a matrix Y of observations and a matrix Ω of non-negative weights, both of dimensions nx × nz. The WH smoothing estimator solves:

$$\widehat { Y } = \arg \min _ { \Theta } \{ F ( Y , \Omega , \Theta ) + R _ { \lambda , q } ( \Theta ) \}$$

where:

- F (Y, Ω, Θ) = Σi=1 Σj=1 Ωi,j(Yi,j − Θi,j)2 represents a fidelity criterion with respect to the observations,


<!-- p:5 -->


- rion with λ = (λx, λz).

This latter criterion adds row-wise and column-wise regularization criteria to Θ, with respective orders qx and qz, weighted by non-negative smoothing parameters λx and λz. In matrix notation, let y = vec(Y), w = vec(Ω), and θ = vec(Θ) as the vectors obtained by stacking the columns of the matrices Y, Ω, and Θ, respectively. Additionally, denote W = Diag(w) and n = nx × nz. The fidelity and smoothness criteria become:

$$F ( y , w , \theta ) = ( y - \theta ) ^ { T } W ( y - \theta )$$

and the associated estimator also takes the form of Equation 2 except in this case

$$P _ { \lambda } = \lambda _ { x } I _ { n _ { z } } \otimes D _ { n _ { x } , q _ { x } } ^ { T } D _ { n _ { x } , q _ { x } } + \lambda _ { z } D _ { n _ { z } , q _ { z } } ^ { T } D _ { n _ { z } , q _ { z } } \otimes I _ { n _ { x } } .$$

Extension to higher dimensions is straightforward and not discussed here.

#### An explicit solution

If W + Pλ is invertible, Equation 2 admits the closed-form solution:

$$\hat { y } = ( W + P _ { \lambda } ) ^ { - 1 } W y .$$

Indeed, as a minimum,  satisfies:

$$0 = \frac { \partial } { \partial \theta } \Big | _ { \hat { y } } \left \{ ( y - \theta ) ^ { T } W ( y - \theta ) + \theta ^ { T } P _ { \lambda } \theta \right \} = - 2 W ( y - \hat { y } ) + 2 P _ { \lambda } \hat { y } .$$

It follows that (W + Pλ) = Wy, proving Equation 3. If λ ≠ 0, W + Pλ is invertible as long as w has q non-zero elements in the one-dimensional case, and Ω has at least qx × qz non-zero elements spread across qx different rows and qz different columns in the two-dimensional case. These conditions are always met in real datasets.

### 1.2 Structure of the paper

Introduced a century ago, Whittaker-Henderson (WH) smoothing remains widely used by actuaries, particularly in France and North America (Canadian Institute of Actuaries 2017; Society of Actuaries 2018). Other non-parametric smoothing methods have since emerged, notably spline-based techniques (Reinsch 1967), which gained even greater popularity with P-splines (Eilers and Marx 1996). A broader overview of alternative smoothers is available in Wood (2017, chap. 5).


<!-- p:6 -->


For evenly spaced discrete observations, WH smoothing may be considered a particular case of P-splines with degree-zero splines and identity model matrix. Its appeal lies in its simplicity: no selection of knots, parameters equal to fitted values, and shape controlled solely via penalization. However, it involves more parameters than low-rank smoothers, making it more computationally intensive.

Originally proposed as an empirical alternative to polynomial regression and weighted averages, WH smoothing offered key benefits noted by Whittaker (1923): first q moment preservation, adjustable smoothing parameters, and robustness at boundaries. While smoothing theory has evolved—particularly via generalized additive models (Hastie and Tibshirani 1990), use of WH smoothing by actuaries remains largely unchanged. This paper reinterprets WH within modern statistical theory to bridge that gap and address six practical questions, each discussed in a dedicated section.

#### How to measure uncertainty in smoothing results?

We propose a method to quantify the uncertainty in WH smoothing based on data volume, a topic that has received little attention in the literature. In a Frequentist framework, the WH estimator is biased, which complicates the construction of valid confidence intervals for finite samples. However, under certain conditions, WH smoothing can be viewed as a Bayesian model, enabling the derivation of credible intervals. This Bayesian interpretation was originally suggested by Whittaker (1923) as a justification for the method and formally revisited decades later by Taylor (1992). In this section, we build on that equivalence to derive credible intervals for WH smoothing.

#### Which observation and weight vectors to use?

For the Bayesian interpretation of WH smoothing discussed in Section 2 to hold, it must be applied to a vector y of independent, normally distributed observations with known variances. The weight vector w should then contain the inverse variances (up to a constant), as noted by Taylor (1992) and Verrall (1993). We show that, under piecewise constant transition intensities in duration models, the maximum likelihood estimator of crude rates produces vectors (y, w) that asymptotically meet these conditions. This, combined with the results from the previous section, offers a statistical foundation for the use of WH smoothing in constructing experience tables for life insurance risks.

#### How to improve the accuracy of smoothing with limited data volume?

The standard approach applies WH smoothing to crude rate estimates, assuming they are asymptotically normal. However, this assumption often breaks down in practice when data are limited, making the method unreliable in such cases. Following Verrall (1993), we propose a generalization of WH smoothing that replaces the two-step procedure with the direct maximization of a penalized log-likelihood. Instead of smoothing pre-estimated rates, this method works directly with aggregated event and exposure counts. The estimation is performed iteratively using the PIRLS algorithm. We evaluate both methods on simulated datasets reflecting typical life insurance portfolios. Results show that, in smaller samples, the normal approximation in the traditional method introduces notable bias. This supports the use of the generalized approach—based on penalized log-likelihood—as a more robust alternative when data are limited.


<!-- p:7 -->


#### How to select the smoothing parameters?

We now turn to the crucial choice of the smoothing parameter λ, which has long been left to actuarial judgment. Giesecke and Center (1981) suggested choosing λ so that the variance of the smoothed results matches the average variance of a Chi-square statistic, but uses n - q as degrees of freedom, thus ignoring the reduction in effective model dimension due to penalization. Brooks et al. (1988) minimized the global cross-validation criterion introduced by Wahba (1980), though this can result in severe under-smoothing as noted by Wood (2011). We instead propose to select λ by maximizing a marginal likelihood function, a method first introduced by Patterson and Thompson (1971) and later applied to smoothing parameter selection by Anderssen and Bloomfield (1974). This approach is consistent with the Bayesian framework discussed earlier and performs well in small samples, as shown by Reiss and Todd Ogden (2009). This marginal likelihood function has a closed-form expression and can be maximized numerically. For the proposed generalization of WH smoothing, the marginal likelihood is no longer available in closed form. Instead, we rely on the Laplace Approximation of the Marginal Likelihood (LAML), which can be maximized numerically. As both solving likelihood equations and selecting the optimal smoothing parameter are iterative processes, we explore different ways of nesting these iterations. We compare three nesting strategies combined with three numerical optimization algorithms for maximizing the marginal likelihood or LAML. Simulation results show that all strategies have near-optimal accuracy, with the fastest performance achieved using the outer iteration strategy combined with the Newton algorithm

#### How to improve smoothing computational efficiency?

When the number of observations—and thus parameters—is large, the computational cost of WH smoothing becomes a major challenge. This is particularly relevant in actuarial contexts, such as smoothing two-dimensional tables for disability or long-term care modelling. Beyond actuarial applications, WH smoothing is also widely used in economics for long time series, where it is known as the Hodrick-Prescott filter (Hodrick and Prescott 1997). Although fast algorithms have been developed to exploit the structure of the penalization matrix (e.g., Weinert


<!-- p:8 -->


2007; Cornea-Madeira 2017) they are typically limited to the one-dimensional case and cannot be directly extended to two dimensions.

After briefly outlining the main computational steps of (generalized) WH smoothing-including smoothing parameter selection via marginal likelihood or LAML-and their leading-order costs, we introduce two complementary strategies to reduce the computational burden:

1. Banded matrix exploitation: WH smoothing involves model and penalization matrices with banded structure. Taking advantage of this structure greatly accelerates key computations.
2. Reduced-rank basis via natural parametrization: Building on the work of Demmler and Reinsch (1975), we apply an eigendecomposition to the one-dimensional penalization matrices and drop components associated with the largest eigenvalues, which reduces the problem size. In two dimensions, we further improve efficiency using the Generalized Linear Array Model (GLAM) framework (Currie, Durban, and Eilers 2006) which leverages the rectangular shape of the data.

In the two-dimensional case, we compare these strategies with a cubic P-spline alternative using simulated datasets. Results show that the banded implementation reduces computation time by up to a factor of 25. The reduced-rank approach brings further gains—up to a factor of 250—at the cost of a slight reduction in accuracy. Its performance is comparable to P-spline smoothing with a cubic basis of similar size.

#### How to extrapolate smoothing results?

We conclude by addressing how to extrapolate smoothing results. Semi-parametric models like WH and P-splines can extrapolate beyond the observed data—similar to parametric models—but this feature is often overlooked in actuarial practice. The existing literature is limited and mostly focused on mortality forecasting.

Currie, Durban, and Eilers (2004) uses P-splines to fit and forecast mortality rates by treating on e on rn os s so - e o  aros 2007; Currie 2013). While this works well in one dimension, Carballo, Durban, and Lee (2021) showed that it distorts the fit in two dimensions. To fix this, they proposed adding constraints to preserve the values that would result from fitting the observed data alone.

However, their approach to confidence intervals overlooks potential innovation error beyond the observed data, effectively treating the extrapolated process as perfectly smooth. In contrast, we propose an approach that derives credible intervals for extrapolated values, accounting for the underlying variability beyond the observed data range.


<!-- p:9 -->


## 2 How to measure uncertainty in smoothing results?

≠ −( + ) = t t   te  t  x () when λ ≠ 0. This implies that penalization introduces a smoothing bias, which prevents the construction of confidence intervals for finite samples centred on E(y). Therefore, in this section, we turn to a Bayesian framework where smoothing can be interpreted more naturally.

### 2.1 Maximum a posteriori estimate

Supe    &lt;  s  (  ) ∼ θ ne (-  ∼ θ    dna allows us to express the posterior likelihood f(θ | y) associated with these choices in the following form:

$$f ( \theta \, | \, y ) \, \infty \, f ( y \, | \, \theta ) f ( \theta ) \, \infty \exp \left ( - \frac { 1 } { 2 \sigma ^ { 2 } } \left [ ( y - \theta ) ^ { T } W ( y - \theta ) + \theta ^ { T } P _ { \lambda } \theta \right ] \right ) .$$

Hence the mode of the posterior distribution, ê = argmax[.f (θ | y)], also known as the maximum a posteriori (MAP) estimate, coincides with the solution  from Equation 2, whose explicit form is given by Equation 3.

### 2.2 Posterior distribution of θ | y

A second-order Taylor expansion of the log-posterior likelihood around  = ê gives us:

$$A \text { second-order any expansion of the log-posution in the} \theta \text { around } y = 0 \text { gives us} . \\ \ln f ( \theta | y ) = \ln f ( \hat { \theta } | y ) + \frac { \partial \ln f ( \theta | y ) } { \partial \theta } \Big | _ { \theta = \hat { \theta } } ^ { T } ( \theta - \hat { \theta } ) + \frac { 1 } { 2 } ( \theta - \hat { \theta } ) ^ { T } \, \frac { \partial ^ { 2 } \ln f ( \theta | y ) } { \partial \theta \partial \theta ^ { T } } \Big | _ { \theta = \hat { \theta } } ( \theta - \hat { \theta } ) \\$$

$$\text {where} \quad \frac { \partial \ln f ( \theta \, | \, y ) } { \partial \theta } \Big | _ { \theta = \hat { \theta } } = 0 \quad \text {and} \quad \frac { \partial ^ { 2 } \ln f ( \theta \, | \, y ) } { \partial \theta \partial \theta ^ { T } } \Big | _ { \theta = \hat { \theta } } = - \frac { 1 } { \sigma ^ { 2 } } ( W + P _ { \lambda } ) .$$

As this last derivative no longer depends on θ, higher-order derivatives are all zero. The Taylor expansion allows for an exact computation of ln f(θ | y). Substituting the result back into Equation 4 yields:

$$f ( \theta | y ) \, \infty \exp \left [ \ln f ( \hat { \theta } | y ) - \frac { 1 } { 2 \sigma ^ { 2 } } ( \theta - \hat { \theta } ) ^ { T } ( W + P _ { \lambda } ) ( \theta - \hat { \theta } ) \right ] \\ \infty \exp \left [ - \frac { 1 } { 2 \sigma ^ { 2 } } ( \theta - \hat { \theta } ) ^ { T } ( W + P _ { \lambda } ) ( \theta - \hat { \theta } ) \right ]$$

which can immediately be recognized as the density of the N(, σ2(W + Pλ)−1) distribution.


<!-- p:10 -->


### 2.3 Consequence for the WH smoothing

The prior θ ∼ N(0, σ2P−) provides a Bayesian interpretation of the smoothness penalty, expressing an (improper) prior belief about the structure of y.

This Bayesian framework and the resulting credible intervals rely on the assumption that y | θ ∼ N(θ, σ2W−), meaning that the components of y are independent with known variances (up to a constant σ2). The weight vector w must then be proportional to the inverse variances, not chosen empirically. If σ2 is known, 100(1 − α)% credible intervals take the form:

$$\mathbb { E } ( y ) \, | \, y \in \left [ \hat { y } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \sigma ^ { 2 } \text {diag} \left \{ ( W + P _ { \lambda } ) ^ { - 1 } \right \} } \right ]$$

where  = (W + Pλ)−1Wy and Φ is the cumulative distribution function for the standard normal distribution. According to Marra and Wood (2012), such intervals have good Frequentist coverage.

If σ2 is unknown, it can be estimated as:

$$\hat { \sigma } ^ { 2 } = \frac { ( y - \hat { y } ) ^ { T } W ( y - \hat { y } ) } { n - \text {tr} ( H ) } \quad \text {where} \quad H = ( W + P _ { \lambda } ) ^ { - 1 } W .$$

In that case, σ2 is replaced by ρ2 and the normal distribution in Equation 5 by the Student t - distribution with n − tr(H) degrees of freedom.

## 3 Which observation and weight vectors to use?

Section 2 highlighted that Whittaker-Henderson smoothing may be interpreted in a robust statistical framework when applied to a vector y of independent, normally distributed observations with known variances, and a weight vector w proportional to the inverses of those variances. In this section, we propose, within the framework of duration models used for constructing experience tables for life insurance risks, vectors y and w that satisfy these conditions.

### 3.1 Survival analysis framework

We consider a longitudinal follow-up of m individuals, subject to left truncation and noninformative right censoring, and aim to estimate a distribution governed by a continuous explanatory variable x (e.g., age). Let μ denote the hazard function, also known as the force of mortality in the study of the death risk. Under standard survival analysis assumptions, the log-likelihood takes the following continuous-time form:

$$\ell ( \theta ) = \sum _ { i = 1 } ^ { m } \left [ \delta _ { i } \ln \mu ( x _ { i } + t _ { i } , \theta ) - \sum _ { u = 0 } ^ { t _ { i } } \mu ( x _ { i } + u , \theta ) d u \right ] .$$


<!-- p:11 -->


Here xi is the age at the start of observation, ti is the follow-up duration for individual i and δi is an event indicator: 1 if the event is observed and 0 if censored.

Although model estimation can be based on direct maximization of Equation 6, this approach ea  - ea     o  oo sps parametric cases. We instead adopt a discrete approximation by assuming the hazard rate is piecewise constant over one-year intervals:

$$\mu ( x + \epsilon ) = \mu ( x ) \quad \text {for all} \quad x \in \mathbb { N } , \epsilon \in [ 0 , 1 [ .$$

Under this assumption, the log-likelihood simplifies to a sum over discrete ages:

$$\ell ( \theta ) = \sum _ { x = x _ { \min } } ^ { x _ { \max } } \ln \mu ( x , \theta ) d ( x ) - \mu ( x , \theta ) e _ { c } ( x ) .$$

Here d(x) is the number of observed events at age x and ec(x) is the central exposure to risk, i.e., the total duration individuals are observed at age x.

This discretization, first introduced by Hoem (1971), is widely used in actuarial science. Its advantages are underlined for example in Gschlössl, Schoenmaekers, and Denuit (2011). It extends naturally to the two-dimensional case by assuming μ(x + €, z + ξ) = μ(x, z) and summing over (x, z) pairs.

Details on the derivation of Equations 6 and 7, along with the computation of central exposures and event counts, are provided in Section A of the appendices.

### 3.2 Likelihood equations

Assuming one parameter per observation and using the exponential link μ(θ) = exp(θ), we recover the crude rates estimator, which models each age (or age pair) independently. The exponential link ensures positive hazard rates. The log-likelihood, in both one- and two-dimensional cases, takes the vectorized form:

$$\ell ( \theta ) = \theta ^ { T } d - \exp ( \theta ) ^ { T } e _ { c }$$

where d and ec are the vectors of observed deaths and central exposures.

The derivatives of this likelihood are:

$$\frac { \partial \ell } { \partial \theta } = \mathbf d - \exp ( \theta ) \odot e _ { c } \quad \text {and} \quad \frac { \partial ^ { 2 } \ell } { \partial \theta \partial \theta ^ { T } } = - D i a g ( \exp ( \theta ) \odot e _ { c } ) .$$

These equations correspond to those of a Poisson GLM (Nelder and Wedderburn 1972) with mean μ(θ)  ec, although derived under different assumptions.


<!-- p:12 -->


The model admits the closed-form solution ê = ln(d/ec). Under standard regularity conditions, the maximum likelihood estimator satisfies  ∼ N(θ, W−1), with W = Diag(d).

Notably, this asymptotic approximation depends on the number of individuals m and not the dimension n of the aggregated vectors.

### 3.3 Consequence for the WH smoothing

We conclude that, under the duration model framework and using crude rates, the log-estimate ln(d/ec) is asymptotically normal:

$$\ln ( \mathbf d / \mathbf e _ { c } ) \sim \mathcal { N } ( \ln \mu , W ^ { - 1 } ) \quad \text {with} \quad W = D i a g ( \mathbf d ) .$$

This justifies applying Whittaker-Henderson smoothing to the observation vector y = ln(d/ec) with weight vector w = d. Using results from Section 2, and σ2 = 1, the credible intervals for ln μ are:

$$\ln \mu \, | \, d , e _ { c } \in \left [ \hat { \theta } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \text {diag} \left \{ ( \text {Diag} ( d ) + P _ { \lambda } ) ^ { - 1 } \right \} } \right ]$$

with ê = (W + Pλ)−1W(lnd − ln ec). Credible intervals for μ itself are then obtained by exponentiating the bounds.

## 4 How to improve the accuracy of smoothing with limited data volume?

### 4.1 Generalized Whittaker-Henderson smoothing

The approach described in Section 3.2 assumes that the crude rates estimator is asymptotically normal, justifying the application of WH smoothing to its logarithm. However, with limited data, this approximation may introduce significant bias. We therefore propose an alternative based directly on the exact likelihood in Equation 8. Applying the Bayesian framework from Section 2 and assuming θ ∼ N(0, P−), Bayes' theorem gives:

$$f ( \theta \, | \, d , e _ { c } ) \, \infty \, f ( d , e _ { c } \, | \, \theta ) f ( \theta ) \, \infty \, \exp \left [ \ell ( \theta ) - \frac { 1 } { 2 } \theta ^ { T } P _ { \lambda } \theta \right ] .$$

We define the penalized log-likelihood as lp(θ) = l(θ) − θT Pλθ/2. The maximum a posteriori estimate is the maximizer of lp.

Using a second-order Taylor expansion of the posterior log-likelihood around ê leads to the Laplace approximation:


<!-- p:13 -->


$$f ( \theta \, | \, d , e _ { c } ) \approx \mathcal { N } ( \hat { \theta } , ( W _ { \hat { \theta } } + P _ { \lambda } ) ^ { - 1 } )$$

where W = Diag(exp()  ec). Unlike the normal case studied in Section 2, the higher-order derivatives of the posterior log-likelihood are not zero, and Equation 10 only provides an approximation of the posterior log-likelihood, which yields asymptotic credible intervals:

$$\ln \mu \left | \, d , e _ { c } \in \left [ \hat { \theta } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \text {diag} \left \{ \left ( W _ { \hat { \theta } } + P _ { \lambda } \right ) ^ { - 1 } \right \} } \right ] .$$

Unlike the closed-form estimator in Equation 9, no analytical solution for ê exists here. We solve numerically using Newton's algorithm, which iteratively updates:

$$\theta _ { k + 1 } = \theta _ { k } + ( W _ { k } + P _ { \lambda } ) ^ { - 1 } ( d - \exp ( \theta _ { k } ) \odot e _ { c } - P _ { \lambda } \theta _ { k } ) ]$$

with Wk = Diag(exp(θk) O ec). The update can be rewritten as:

$$\theta _ { k + 1 } = ( W _ { k } + P _ { \lambda } ) ^ { - 1 } W _ { k } z _ { k } \quad \text {where} \quad z _ { k } = \theta _ { k } + W _ { k } ^ { - 1 } [ \text {d} - \exp ( \theta _ { k } ) \odot \text {e} _ { \text {c} } ] .$$

Initializing with the crude rates estimator θ0 = ln(d/ec) implies W0 = Diag(d) and z0 = ln(d/ec), so the first iteration recovers the classical WH smoothing result.

Subsequent iterations refine the observation and weight vectors. This process can thus be interpreted as an iterative generalization of WH smoothing, akin to how generalized linear models extend linear models.

We refer to this method as generalized Whittaker-Henderson smoothing. The iterative estimation algorithm described above corresponds to the Penalized Iteratively Reweighted Least Squares (PIRLS) algorithm, widely used for fitting generalized additive models.

This framework naturally extends to other exponential family distributions, such as the binomial case suggested in Verrall (1993), by adapting the likelihood, link function, weight matrix, and working vector. However, we advocate for the Poisson-like likelihood of Equation 8, which offers several advantages: it generalizes to competing risks, supports multiplicative covariate effects via the log link, and allows the use of an external reference table as a multiplicative offset.

### 4.2 Impact of the normal approximation in the original smoothing

As discussed in Section 3, classical Whittaker-Henderson smoothing can be viewed as an approximation to a penalized likelihood maximization, relying on a crude rate estimator assumed to be asymptotically normal. To assess the practical consequences of this approximation, we conduct an empirical comparison based on six simulated datasets reflecting the typical structure and volume of real insurance portfolios:


<!-- p:14 -->


Table 1: Key figures associated with the 6 simulated datasets

| Portolio type   | Dimensions   |   Head count |   Exposure count |   Death count |
|-----------------|--------------|--------------|------------------|---------------|
| annuity         | 45           |       20,000 |          136,524 |         1,722 |
| annuity         | 45           |      100,000 |          679,728 |         8,452 |
| annuity         | 45           |      500,000 |        3,405,892 |        42,499 |
| LTC             | 30 x 15      |       20,000 |            8,115 |         1,888 |
| LTC             | 30 x 15      |      100,000 |           40,004 |         9,281 |
| LTC             | 30 x 15      |      500,000 |          202,666 |        47,358 |

- The first three datasets simulate annuity portfolios with 20,000, 100,000, and 500,000 policyholders. The sole covariate is age, ranging from 50 to 95.
- The next three mimic long-term care (LTC) portfolios of the same sizes. Modelling of LTC typically relies on the illness-death model (Fix and Neyman 1951; Clifford 1977). To get a two-dimensional illustration we focus on the transition between the disabled and dead states (the two other transitions would provide additional one-dimensional examples). Two covariates are used: age (70–100) and duration in LTC (0–15 years).

Each dataset consists of individual-level longitudinal data, from which we derive event counts d and exposures ec, aggregated by age x (for annuities) of by (x, z) pairs (for LTC). All datasets within each group share the same underlying structure and differ only in size. Key dataset statistics are provided in Table 1 and additional details about how those datasets were generated are provided in Section B of the appendices.

We apply two methods:

1. Original WH smoothing using y = ln(d/ec) and weights w = d as in Section 3.
2. Generalized WH smoothing, using the likelihood formulation of Section 4.

Both methods use the same smoothing parameter(s) λ, to ensure that prior assumptions on θ = ln μ are held constant. We fix the penalty order at q = 2, corresponding to second-order differences.

As both estimators target θ, we compare them using the following relative error metric:

$$\Delta ( \theta ) = \frac { \ell _ { P } ( \hat { \theta } _ { M L } ) - \ell _ { P } ( \theta ) } { \ell _ { P } ( \hat { \theta } _ { M L } ) - \ell _ { P } ( \hat { \theta } _ { \infty } ) } .$$

Here ê maximizes the penalized likelihood, while ê∞ corresponds to the solution with λ → ∞, which we later show to be the degree-(q - 1) polynomial that maximizes the likelihood. By construction:

$$\Delta ( \hat { \theta } _ { \text {ML} } ) = 0 , \ \Delta ( \hat { \theta } _ { \infty } ) = 1 , \ \text { and } \ \Delta ( \theta ) \geq 0 .$$


<!-- p:15 -->


Table 2: Impact of the approximation from the original WH smoothing on the 6 simulated datasets

| Portolio type   |   Head count | Relative Error   | SMR    |
|-----------------|--------------|------------------|--------|
| annuity         |       20,000 | 1,91%            | 99,19% |
| annuity         |      100,000 | 0,02%            | 99,89% |
| annuity         |      500,000 | 0,00%            | 99,99% |
| LTC             |       20,000 | 93,27%           | 86,86% |
| LTC             |      100,000 | 5,12%            | 97,59% |
| LTC             |      500,000 | 0,24%            | 99,56% |

A model with ∆(θ) &gt; 1 performs worse than a simple polynomial fit under the prior.

Table 2 presents the values of ∆(ênorm) across the six datasets. As expected, discrepancies decrease with portfolio size. For annuities, the approximation performs reasonably well even at smaller scales. In contrast, for LTC, it yields substantial errors, except for the largest portfolio.

One explanation, supported by the Standardized Mortality Ratio (SMR) also provided in Table 2, is the positive correlation between observed event counts and their use as weights. This causes high crude rates to be overweighted, and low rates to be underweighted—introducing systematic overestimation of mortality rates. This bias is more severe in the LTC case where the observed deaths by data point is lower. In contrast, generalized WH smoothing preserves total event counts by construction, always yielding an SMR of exactly 100%. These results support adopting generalized WH smoothing in most practical settings. It retains the advantages of the original method while offering improved accuracy—even in small samples—and remains straightforward to implement.

## 5 How to select the smoothing parameters?

### 5.1 Impact of smoothing parameter choice

In the one-dimensional case, WH smoothing involves a single smoothing parameter λ; in two dimensions a pair λ = (λx, λz). These parameters govern the trade-off between fidelity to the data and smoothness of the estimate, as defined in Equation 1.

Figure 1 illustrates this effect in a one-dimensional annuity dataset (100,000 policyholders, see Section 4.2), with three values of λ. The effective degrees of freedom (edf), computed as the trace of the hat matrix H = (W + Pλ)−1W, are shown for each curve. This quantity serves as a non-parametric analog of the number of free parameters in classical models and can take fractional values.


<!-- p:16 -->


As shown, a low value λ = 101 yields an overfitted result that mirrors sampling noise, while a high value λ = 107 oversmooths and obscures the underlying trend. A mid-range value λ = 104 appears visually balanced. However, selecting a smoothing parameter by eye is unreliable: small-sample variability at the extremes of the age range can easily be mistaken for meaningful patterns.

α α 10'

α0 1044

α □ 107

Force of mortality (logarithmic scale)

edf:35.21

edf : 6.71

edf: 2.10

10−-1

10-3

50

60

70

80

90

50

60

70

80

90

50

60

70

80

90

Age

Figure 1: WH smoothing on a synthetic annuity portfolio with 3 smoothing levels. Dots: crude rates; curves: smoothed estimates; shaded areas: credibility intervals. edf: effective degrees of freedom.

The two-dimensional case further illustrates this difficulty. Figure 2 presents the smoothed transition rates from disability to death in an LTC portfolio (100,000 policyholders), using 9 combinations of (λx, λz). Choosing an appropriate parameter pair visually becomes nearly impossible, reinforcing the need for a data-driven statistical selection criterion.

### 5.2 Statistical criteria for parameter selection

Smoothing parameter selection typically relies on two classes of statistical criteria:

1. Prediction-based criteria, which aim to minimize prediction error, such as the Akaike Information Criterion (AIC) (Akaike 1973) and Generalized Cross-Validation (GCV) (Wahba 1980);
2. Likelihood-based criteria, which maximize the marginal likelihood—an approach introduced by Patterson and Thompson (1971) (under the name REML in the Gaussian case) and adapted to smoothing by Anderssen and Bloomfield (1974).

While prediction-based criteria have desirable asymptotic properties (Wahba 1985; Kauermann 2005), their convergence toward optimal smoothing parameters can be slow. In contrast, marginal likelihood criteria tend to perform more robustly in finite samples (Reiss and Todd Ogden 2009; Wood 2011).


<!-- p:17 -->


Figure 2: WH smoothing applied to disability-to-death transitions in an LTC portfolio, using 9 combinations of smoothing parameters. Contour lines and colours show the smoothed mortality surface by age and LTC duration.

α2 ± 10-1

α2 ± 102

αz ± 105

95

90-

85

Force of

80

mortality

75

0,585

edf : 29.6

edf: 9.4

edf : 4.5

70

0,461

95

0,373

90

0,286

0,229

85

0,185

80

0,150

75

0,118

edf: 99.8

edf : 36.7

edf : 16.0

70

0,090

95

0,066

90

0,043

85

80

75

edf : 364.7

edf : 112.9

edf : 54.9

70

10


Duration in LTC

To illustrate this, we apply AIC, GCV, and marginal likelihood to 100 replicates of the annuity portfolio with 100,000 policyholders (see Section 4.2). For each replicate, we select the optimal smoothing parameter and compute the corresponding effective degrees of freedom.

As shown on the left side of Figure 3, marginal likelihood produces stable and coherent degrees of freedom across replicates, whereas AIC and especially GCV often yield overly complex models. On the right, we plot the GCV and marginal likelihood profiles for a single replicate: marginal likelihood exhibits a well-defined maximum, while GCV presents two local minima. One aligns with the marginal likelihood optimum, but the global minimum corresponds to a model with ~35 degrees of freedom—an implausibly complex mortality curve.


<!-- p:18 -->


These observations support the use of marginal likelihood over prediction-based criteria, especially in actuarial applications where robustness is key. Moreover, this choice aligns naturally with the Bayesian framework introduced in Sections 2 to 4.

We now detail its implementation—first for the original WH smoothing, then for the generalized setting—introducing three optimization strategies and three numerical algorithms and comparing their respective performances.

1010

Figure 3: Comparison of criteria for selecting the smoothing parameter in one-dimensional WH smoothing. Left: distribution of effective degrees of freedom under AIC, GCV, and marginal likelihood across 100 replicates. Right: GCV and marginal likelihood values for one replicate as functions of the smoothing parameter.

●

GCV

marginal likelihood

of freedom

edf : 6.08

40

3.0

Criterion value

-100

30

2.5

Effective degrees

20

2.0

-150

1.5

10

-200

edf: 35.31

GCV

AIC

marginal likelihood

100

102

104

106

108

1010

100

102

104

106

108

Criterion

Smoothing parameter (logarithmic scale)

### 5.3 Selection in the original smoothing

-       o   o θ | λ ∼ N(0, σ2P−). In the empirical Bayes approach, the smoothing parameter λ is estimated by maximizing the marginal likelihood:

$$\mathcal { L } _ { \text {norm} } ^ { m } ( \lambda ) = f ( y \, | \, \lambda ) = \int f ( y , \theta \, | \, \lambda ) d \theta = \int f ( y \, | \, \theta ) f ( \theta \, | \, \lambda ) d \theta .$$

This is simply the maximum likelihood method applied to the smoothing parameter, treated as deterministic but unknown. A closed-form expression for this integral can be derived using standard Gaussian identities (see Section C of the appendices), yielding the marginal log-likelihood:

$$\ell _ { n o r m } ^ { m } ( \lambda ) = - \frac { 1 } { 2 } \left [ ( y )$$

where θλ = (W + Pλ)−1Wy, and C = − ln |W|+ + (n* − q) ln(2πσ2) is a constant independent of λ. This function is maximized numerically to obtain λnorm.


<!-- p:19 -->


### 5.4 Selection in the generalized smoothing

The empirical Bayes approach introduced in the normal framework can be extended to the generalized smoothing framework developed in Section 4. While no closed-form expression exists for the marginal likelihood in this context, it can be approximated using a second-order Taylor expansion of the log-posterior density around its maximum θλ—similarly to what was done in the normal case. This yields the so-called Laplace Approximation of the Marginal Likelihood (LAML), defined as:

$$\ell _ { L A M L } ^ { m } ( \lambda ) = \ell ( \hat { \theta } _ { \lambda } ) - \frac { 1 } { 2 } \left [ \hat { \theta } _ { \lambda } ^ { T }$$

where Wλ = Diag(exp(êλ)  ec) and l(λ) is the log-likelihood evaluated at the penalized MLE. The detailed derivation of the Laplace approximation in this setting is provided in Section C of the appendices. This approximation plays a central role in the automatic selection of the smoothing parameter λ in the generalized Whittaker-Henderson smoothing framework. As in the normal case, the marginal likelihood lAmL (λ) must be maximized numerically. However, a key distinction is that the penalized likelihood maximizer θλ now depends on λ and must be recomputed at each iteration via the PIRLS algorithm. This leads to a two-level optimization procedure:

- an inner loop estimating λ for fixed λ using PIRLS;
- and an outer loop optimizing lLAmL(λ) with respect to λ.

This outer iteration approach is the most principled method for smoothing parameter selection in this setting.

Alternative strategies have been proposed to reduce computational burden. The first one, known as performance-oriented iteration, was introduced by Gu (1992) and relies on the observation that, at each PIRLS step, the working response vector zk can be treated as approximately normal: zk | θ ∼ N(θ, W−1). Assuming Wk independent of λ, the marginal likelihood can be maximized within each PIRLS step using the normal approximation methodology of Section 5.3, with y replaced by zk and W by Wk. This effectively reverses the nesting structure, potentially saving computational time when updating λ is less costly than recomputing a PIRLS step. A formal justification of the method is provided by Wood (2017, 149) which emphasizes that it does not actually require zk to have a normal distribution to be well-founded.

A third and even simpler strategy is the alternate iteration approach, used for instance by Wood et al. (2017). It consists in alternating updates of θ (via PIRLS) and λ (via approximate marginal likelihood), without fully optimizing either at each step. This relies on the empirical observation that a coarse update of λ may suffice, as the marginal likelihood surface changes between iterations.

Despite their efficiency, both performance-oriented and alternate iteration approaches lack formal convergence guarantees. Unlike outer iteration, they operate on different smoothing parameters at each step, rendering penalized likelihood values non-comparable across iterations. Moreover, they do not track the value of lLAmL(λ) during the optimization, making it harder to assess convergence or apply step-length controls.


<!-- p:20 -->


Detailed algorithmic formulations of all three strategies in the generalized WH smoothing framework are provided in Section D of the appendices.

### 5.5 Algorithms for the maximization of the marginal likelihood

Several algorithms can be used to maximize the marginal likelihood or its Laplace approximation (LAML). It is generally preferable to apply these algorithms to the logarithm of the smoothing parameters, for three main reasons:

1. It ensures positivity of the smoothing parameters;
2. It simplifies the expressions of derivatives, when required;
3. It allows more uniform coverage of the range of interest (e.g., from λ = 101 to 107, as in Figure 1, differences of comparable magnitude occur on a logarithmic scale).

#### Derivative-free heuristics

A first, operationally simple option is to use general-purpose derivative-free optimization methods:

- Brent's method (Brent 1973) in the one-dimensional case;
- The Nelder-Mead simplex algorithm (Nelder and Mead 1965) in higher dimensions.

These are readily available in base R via the optimize and optim functions. They only require evaluating the marginal likelihood or LAML at each step, which is computationally inexpensive. However, they typically require more iterations to converge and cannot be combined with the alternate iteration approach, as they do not guarantee systematic improvement of the criterion at each step.

#### Generalized Fellner-Schall method

A more specialized algorithm is the generalized Fellner-Schall method, based on ideas from Fellner (1986) and Schall (1991), and adapted for smoothing parameter selection in multidimensional generalized linear models by Rodriguez-Alvarez et al. (2015). It may be summarised by the update formula:

$$\lambda _ { j } ^ { n e x t } = \frac { \text {tr} ( P _ { \lambda } ^ { - } P _ { j } ) - \text {tr} [ ( X ^ { T } W X + P _ { \lambda } ) ^ { - 1 } P _ { j } ] } { \hat { \beta } _ { \lambda } ^ { T } P _ { j } \hat { \beta } _ { \lambda } } \chi _ { j } ^ { \text {current} } \quad \text {for} \quad j \in \{ x , z \} .$$


<!-- p:21 -->


where for WH smoothing Pj = Dn+,qDn+,q in the one-dimensional case and Px (resp. Pz) 1xDnx,qx (resp. Dnz, zDnz,qz ⊗ Inx) in the nz,qz two-dimensional case.This update can be interpreted more intuitively as:

$$\hat { \beta } _ { \lambda } ^ { T } ( \lambda _ { j } ^ { \text {next} } P _ { j } ) \hat { \beta } _ { \lambda } = \text {tr} [ P _ { \lambda } ^ { - } \lambda _ { j } ^ { \text {current} } P _ { j } - ( X ^ { T } W X + P _ { \lambda } ) ^ { - 1 } \lambda _ { j } ^ { \text {current} } P _ { j } ]$$

w e  o  e e    e-t  oret λcurrent Pj, and the left-hand side to a squared error, normalized by the updated penalty precision. This makes λnext resemble a REML-based estimator for the inverse variance. More details may be found in Rodríguez-Álvarez et al. (2019). This method:

- May be combined with any of the three iteration nesting schemes (outer, performance, alternate);
- Does not require explicit derivative computations;
- Converges toward an approximate maximum of LAML in the generalized case, since it ignores the dependence of W on λ;
- Tends to take longer steps than EM-like algorithms (Dempster, Laird, and Rubin 1977), but shorter than Newton updates (see Wood and Fasiolo 2017, which also provides a thorough justification for the method).

#### Newton algorithm

A third option is the Newton method, which involves computing both the first and second derivatives of the marginal likelihood (or LAML) with respect to ln λ. Full derivations are provided in Wood (2011), which covers a more general case. The method applies in both the normal and generalized cases, but in the latter, derivative expressions are more complex due to the dependence of W on λ. The Newton algorithm is fast and precise and applicable to all three nesting strategies. The downside is the operational complexity associated with this method, especially in the generalized case.

### 5.6 Performance comparison

Sections 5.4 and 5.5 introduced eight combinations of nesting strategies and optimization algorithms applicable to the generalized WH smoothing. We now assess the potential convergence issues and approximation errors associated with each of them.

This analysis is based on 100 replicates of the simulated annuity and LTC portfolios with 100,000 policyholders, as described in Section 4.2. For each replicate and each method combination, we compute the LAML at the selected smoothing parameters, and compare this value to the (approximate) optimal value obtained across all combinations, denoted λopt.


<!-- p:22 -->


To quantify the discrepancy, we define the relative error:

$$\Delta ( \lambda ) = \frac { \ell _ { L A M L } ^ { m } ( \hat { \lambda } _ { o p t } ) - \ell _ { L A M L } ^ { m } ( \lambda ) } { \ell _ { L A M L } ^ { m } ( \hat { \lambda } _ { o p t } ) - \ell _ { L A M L } ^ { m } ( \infty ) }$$

where lLAML (∞) corresponds to the LAML value when using an infinite smoothing penalty, i.e., the overly smooth baseline. By construction, ∆(λ) ≥ 0 for all tested methods, with ∆(λopt) = 0 and ∆(∞) = 1. In the two-dimensional setting, we also compare average computation time for each method across replicates.

Results are summarised in Figure 4. The top panel displays the relative error ∆(λ) (capped below 10−10 for readability). In the outer iteration framework:

- The Newton method consistently achieves relative errors below 10−10;
- Brent and Nelder-Mead heuristics yield slightly higher errors but remain below 10−7;
- The generalized Fellner-Schall method produces higher errors, but still below 10-5 and negligible in practice.

In the performance and alternate iteration frameworks, all methods yield similar errors, consistently below 10-5, with no convergence issues observed in any replicate. These findings suggest that method selection can be guided by practical considerations such as speed and implementation ease.

The bottom panel of Figure 4 compares computation times (relative to the Nelder-Mead + outer iteration baseline):

- In the outer iteration framework, the Newton method is the fastest, followed by the Fellner-Schall approach;
- All outer iteration variants are faster than their performance or alternate counterparts.

This is unsurprising, as PIRLS steps are particularly lightweight in WH smoothing (where the model matrix is the identity). However, alternate strategies may remain useful for more general cases like those described in Section 6.4.

For reference, the average time required for a single iteration using Nelder-Mead in the 2D outer iteration case is approximately 1.68 seconds (versus 5 milliseconds in the 1D case).


<!-- p:23 -->


Figure 4: Comparison of the 8 nesting strategy and algorithm combinations in the 1D and 2D simulated cases. Top: relative error on the LAML (log scale). Bottom: improvement in average computation time compared to the Nelder-Mead + outer iteration reference.

1D, Outer iteration

1D, Performance iteration

1D, Alternated iteration

10-6

Relative error on marginal likelihood

Brent

Fellner-Schall

Newton

Brent

Fellner-Schall

Newton

Fellner-Schall

Newton

2D, Outer iteration

2D, Performance iteration

2D, Alternated iteration

000

10-9

10-10

Nelder-Mead Fellner-Schall

Newton

Nelder-Mead Fellner-Schall

Newton

Fellner-Schall

Newton

Outer iteration

Performance iteration

Alternated iteration

3,0

factor

2,5

2,33

Speed-up

2,0

1,98

1,64

1,32

1,33

1,15

1,0

1,00

0,63

0,5

Nelder-Mead Fellner-Schall

Newton

Nelder-Mead Fellner-Schall

Newton

Fellner-Schall

Newton

Selection method

## 6 How to improve smoothing computational efficiency?

### 6.1 Motivation

Whittaker-Henderson (WH) smoothing is a full-rank method, meaning that it includes as many parameters as there are observation points. This feature ensures a high degree of flexibility, allowing the estimator to closely track the input signal when sufficient data is available. Formally, WH smoothing is asymptotically unbiased since:


<!-- p:24 -->


$$\mathbb { E } ( \hat { y } ) = ( W + P _ { \lambda } ) ^ { - 1 } W \mathbb { E } ( y ) \stackrel { m \to \infty } { \to } \mathbb { E } ( y ) ,$$

where m denotes the number of observed individuals, which influences the matrix W.

However, this flexibility comes at a computational cost. Some key operations, such as (implicit) matrix inversions, scale cubically with the number of parameters. As a result, WH smoothing may become impractical with large number of combinations or when applied repeatedly (e.g. in simulations or bootstraps).

In one-dimensional settings, such as age-only models with annual discretization, the number of points rarely exceeds 100, and computation time is negligible. In contrast, two-dimensional use cases—common in insurance—can lead to substantially larger datasets:

- Disability tables in France must cover entry ages from 18 to 61 and exit ages up to 62, resulting in (62 − 18) × (62 − 18 + 1)/2 = 990 combinations.
- Transition tables from short-term incapacity to disability involve entry ages from 18 to 67 and monthly durations from 0 to 36 months, yielding (67 – 18) × 36 = 1, 764 combinations.
- Long-term care (LTC) models require coverage over ages 50 to 100 and durations from 0 to 20 years, totalling (100 − 50) × (20 − 0) = 1, 000 combinations (in practice, this number may be lower due to data sparsity).

In such settings, computing WH smoothing—especially when paired with smoothing parameter selection—can take several minutes per application, limiting usability in iterative contexts.

To address this limitation, we now analyse the computational complexity of the main steps in WH smoothing and smoothing parameter selection then introduce two complementary strategies to reduce computation time:

- A structural optimization that exploits the specific form of WH penalization matrices;
- A reduced-rank approximation that lowers the number of parameters while minimizing bias compared to the full-rank estimator.

Finally, we benchmark these strategies in terms of runtime and accuracy using 100 replicates of the mid-size annuity and LTC portfolios from Section 4.2. The structural optimization is compared to the original WH method, while the reduced-rank approximation is evaluated against the original method, the structural optimization, and a reference P-spline smoothing approach.


<!-- p:25 -->


### 6.2 Practical computation for penalized smoothers

Whittaker-Henderson (WH) smoothing belongs to a broader family of penalized smoothing methods that produce estimates of the form:

$$\hat { y } _ { \lambda } = X \hat { \beta } _ { \lambda } \quad \text {where } \beta _ { \lambda } \text { solves } ( X ^ { T } W X + P _ { \lambda } ) \hat { \beta } _ { \lambda } = X ^ { T } W y .$$

Here, X and Pλ denote the model and penalization matrices of size n × p and p × p respectively, and W is a diagonal matrix of positive weights of size n × n.

#### Computational steps

The computation of λ for a given λ typically involves the following steps:

1. Absorb the weights in the model matrix and observation vector, forming W1/2X and W1/2y, which requires O(n2) and O(n) operations respectively (multiplying each row of X and each element of y by the corresponding element of w).
2. Form the matrix Pλ. The cost of this operation is typically O(p2) in the general case.
3. Form the matrix XTWX and the vector XTWy, which requires up to O(np2) and O(np) operations respectively.
4. Add together XTWX and Pλ which requires O(p2) operations in the general case.
5. Compute the Cholesky decomposition XTWX + Pλ = RT R at a cost of O(p3).
6. Obtain βλ by forward-backward substitution, first solving RTu = XTWy then Rβλ = u with an associated cost of O(p2) for each system.
7. Compute λ = Xβλ at a cost of O(np).

As an alternative to Cholesky, QR decomposition may be used for greater numerical stability (see Golub and Van Loan 2013). It applies to the weighted design matrix stacked with a matrix B such that BT B = Pλ.

#### Simplifications for WH smoothing

In WH smoothing, X = In, which simplifies computations:

- Step 7 is unnecessary, as well as the first part of step 3.
- XTWy = Wy (step 3) is computed in O(n) by multiplying w and y.
- XTWX + Pλ = W + Pλ (step 4) is also computed in O(n) by adding the vector w to the leading diagonal of Pλ.


<!-- p:26 -->


#### Generalized WH smoothing with outer iteration

When using the outer iteration approach (see Section 5), each candidate λ requires a full PIRLS cycle to estimate λ, with new working vector żk and weight matrix Wk. Steps 1–6 above are repeated until convergence of the PIRLS algorithm, which may be assessed by monitoring the changes in penalized deviance. The deviance may be computed at a O(n) cost. For penalization based on differences matrices, computation of βλ T Pλβλ should be based on the expression of Rλ,q provided in Section 1.1 for an associated cost of O(qp). In addition, PIRLS iterations for each new λ can be initialized using the previous estimate of λ for faster convergence.

#### LAML computation

Once the deviance is known, computing the marginal likelihood/LAML also requires:

- ln |XTWX + Pλ|, which may be computed at a cost of O(p) from the leading diagonal of the Cholesky/QR factor R computed at step 5 in the derivation of λ.
- ln |Pλ|+, which may be obtained from the eigenvalues of the penalization matrix: Section 6.4 shows that in the two-dimensional case, it can be computed via eigendecomposition of D x,qxDpx,qx and D,qzD z,qz, performed only once, at a O(px + p3) cost. Computation of ln |Pλ|+ then only requires scaling the eigenvalues for a cost of O(p).

#### Algorithm-specific computations

Brent and Nelder-Mead require only marginal likelihood/LAML evaluations.

The generalized Fellner-Schall algorithm relies on the update formula of Equation 12:

$$\lambda _ { j } ^ { n e x t } = \frac { \text {tr} ( P _ { \lambda } ^ { - } P _ { j } ) - \text {tr} [ ( X ^ { T } W X + P + P _ { j } ) ] } { \hat { \beta } _ { \lambda } ^ { T } P _ { j } \hat { \beta } _ { \lambda } }$$

Evaluation of tr(P− Pj) does not require any matrix product. In the one-dimensional case it is simply (p − q)/λ while in the two-dimensional case it may be obtained directly at a O(p) cost using the eigenvalues of the aforementioned penalization matrices Pj. Evaluation of tr[(XTWX + Pλ)−1 Pj] may use the identity tr(AB) = Σi,j AijBji and therefore be computed at an O(p2) cost if the matrix (XTWX + Pλ)−1 and Pj are available. Computation of V = (XTWX + Pλ)−1 is done by first solving for the inverse K = R−1 of the Cholesky/QR factor and then forming V as KKT. Both operations have a O(p3) cost.

Newton method also requires computation of V, as well as several matrix products involving the penalization matrix Pj. For example, the second derivatives of marginal likelihood require tr[V PjV Pk] terms and the second derivatives of marginal likelihood require tr[V(X(∂W/∂ρj)X + Pj)V(X(∂W/∂ρk)X + Pk)] terms where ρj = ln(λj), j = k = x in the one-dimensional case and {j, k} ∈ {x, z} in the two-dimensional case. The identity tr(AB) = Σi,j AijBji can also be used in this case but matrix products VPj or V[X(∂W/∂ρj)X + Pj] still need to be explicitly computed, for a respective cost of O(p3) and O(np2) each.


<!-- p:27 -->


These additional computations make Newton updates more expensive than generalized FellnerSchall updates, but they generally yield faster convergence and higher precision (see Section 5.6).

### 6.3 Banded optimization for WH smoothing

We now consider how to exploit the banded structure of the penalization matrix in WhittakerHenderson (WH) smoothing. This structure enables significant computational gains, especially when dealing with large number of observations. Throughout this section, we assume X = In and p = n, which holds for both the original and generalized WH smoothing.

#### One-Dimensional Case

symmetric and banded with bandwidth q. As a consequence:

1. Compact storage: Pλ can be stored in a compact form with dimensions n × (q + 1), and updated for new λ at a cost of O(qn). The matrix W + Pλ shares this structure.
2. Efficient Cholesky decomposition: the Cholesky factor R of W + Pλ can be computed in O(q2n) instead of O(n3), and R is also banded with the same bandwidth.
3. Efficient back-substitution: computing λ = βλ using R is now O(qn) instead of O(n2).
4. Efficient inversion of R: the inverse K = R−1 costs O(qn2), an improvement over the O(n3) cost for dense matrices.

However, K is a dense triangular matrix, meaning the computation of V = KKT remains o    -   om odo u diagonal of V, which can be obtained from K in O(n2), since:

$$\lambda _ { j } [ \text {tr} ( P _ { \lambda } ^ { - } P _ { j } ) - \text {tr} ( V P _ { j } ) ] = ( n - q ) - ( n - \text {tr} [ V W ] ) = \text {diag} ( V ) ^ { T } \mathbf w - q .$$

Furthermore, the Newton algorithm benefits as well: the trace terms involving VPλ or V(∂W/∂ln λ + Pλ) are based on banded matrices, making those products computable in O(qn2) instead of O(n3).


<!-- p:28 -->


#### Two-dimensional Case

In two dimensions, the penalization matrix is Pλ = λxPx + λzPz where :

- Px = Inz ⊗ Dnx,qxDnx,qx
- Pz = DT nz,qz1 zDnz,qz ⊗ Inx·

This structure has the following key properties:

- Both matrices are made of nz × nz square blocks of dimensions nx × nx each.
- Px is block-diagonal with nz identical nx × nx banded blocks (bandwidth qx).
- Pz is block-banded with bandwidth qz. Each block is a scaled identity matrix.
- As a whole, Pz and Pλ may be viewed as banded matrices with bandwidth q = qz × nx.

This implies that all statements made in the one-dimensional case carry over to the twodimensional case with this value of q. It also suggests that, if (qx + 1)/nx &lt; (qz + 1)/nz, dimensions x and z should be permuted before applying WH smoothing for maximal efficiency.

As in the one-dimensional case, the generalized Fellner-Schall update formula does not require the full computation of V. Indeed, to compute tr[VPx] and tr[VPz], we only need access to elements of V for which either Px or Pz is non-zero. From what precedes, Px has bandwidth qx while Pz only contains qz non-zero diagonals on each side of the leading diagonal. As V is symmetric, we only need to compute qx + qz + 1 diagonals of V for an associated cost of O([qx + qz]n2) instead of O(n3).

With the Newton method, while computing V = KKT still incurs a O(n3) cost, matrix multiplications like VPj or V(∂W/∂ρj + Pj) can be performed block-wise. It may easily be checked for example that the products VPx and V(∂W/∂ρx + Px) have a cost of O(qxn2) while the products V Pz and V(∂W/∂ρz + Pz) have a cost of O(qzn2).

#### Summary of complexity gains

Thanks to the banded structure, most computations involved in WH smoothing can be accelerated by a factor of n/(q + 1) in the 1D case and max(nx/(qz + 1), nz/(qx + 1)) in the 2D case. There are 3 notable exceptions:

- Cholesky decomposition is improved from O(n3) to O(q2n)—a quadratic speed-up.
- Computation of V = KKT remains O(n3).
- Some matrix products required by Newton method get a full n/(qz + 1) or n/(qz + 1) speed-up in the 2D case.


<!-- p:29 -->


Table 3: Compared theoretical leading-order costs associated with the key steps in smoothing computations for several frameworks. All cells should be read as O(...).

| Computation       | Dense   | Banded   | Rank-reduced   |
|-------------------|---------|----------|----------------|
| X T WX            | ∅       | ∅        | np 2           |
| X T Wz            | n       | n        | np             |
| P λ               | n 2     | qn       | p              |
| X T WX + P λ      | n       | n        | p              |
| R                 | n 3     | q 2 n    | p 3            |
| ˆ β λ             | n 2     | qn       | p 2            |
| ˆ y λ = X ˆ β λ   | ∅       | ∅        | np             |
| ML/LAML           | qn      | qn       | n              |
| K = R - 1         | n 3     | qn 2     | p 3            |
| V = KK T          | n 3     | n 3      | p 3            |
| Brent/Nelder-Mead | n 3     | q 2 n    | p 3            |
| Fellner-Schall    | n 3     | qn 2     | p 3            |
| Newton            | n 3     | n 3      | p 3            |

Table 3 summarises theoretical complexities across different frameworks, including a typical generalized additive model framework for which the penalization matrix is diagonal. This last framework is used by the rank-reduced WH smoothing approach introduced next, as well as the P-spline alternative used for comparison.

#### Empirical gains

Figure 5 compares actual computation times of WH smoothing (two-dimensional, outer iteration), showing that adapting the implementation to exploit banded structures results in large speed gains:

- The Nelder-Mead method benefits the most, with a 25 × speedup compared to dense computation.
- Newton and Fellner-Schall methods see 6.6 × and 10 × improvements, respectively, making them fall behind the Nelder-Mead method.

As a final advantage, Brent and Nelder-Mead heuristic methods rely solely on banded matrices that can be stored as compact matrices of dimensions (q + 1) × n, adding further efficiency.

### 6.4 Natural parameterization and rank reduction of WH smoothing

Demmler and Reinsch (1975) proposed a natural parameterization for penalized smoothers using the eigendecomposition of the penalization matrix. This provides both an intuitive interpretation of the smoothing mechanism and a foundation for dimension reduction via rank-restricted estimation.


<!-- p:30 -->


Figure 5: Computation time comparison for 2D generalized WH smoothing with outer iteration. The speed-up factor is computed relative to the original dense method using the Nelder-Mead algorithm.

Dense computations

Banded computations

35

3,0

30

factor

2,5

25

24,93

2,33

Speed-up f

2,0

20

16,65

1,64

15

15,38

1,5

8

10

1,0

1,00

●00

Nelder-Mead

Fellner-Schall

Newton

Nelder-Mead

Fellner-Schall

Newton

Selection method

#### One-dimensional Case

In one dimension, let Dn. gDn,q = UΣUT be the eigendecomposition of the penalty matrix, n,q where U is orthogonal and Σ diagonal with non-negative eigenvalues. A change of variable θ = Uβ transforms the WH optimization into:

$$\hat { y } = U \hat { \beta } \quad \text {where} \quad \hat { \beta } = \arg \min _ { \beta } \left \{ ( y - U \beta ) ^ { T } W ( y - U \beta ) + \lambda \beta ^ { T } \Sigma \beta \right \}$$

yielding the solution:

$$\hat { y } = U ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W y \quad \text {where} \quad S _ { \lambda } = \lambda \Sigma .$$

This formulation shows that WH smoothing decomposes the signal into eigenvector components and attenuates each according to the associated eigenvalue—the higher the eigenvalue, the stronger the shrinkage.

We refer to Section E of the appendices for graphical illustrations of:

- the basis eigenvectors of D T Dn,q; n,q
- the evolution of their effective degrees of freedom under smoothing.

These figures show that only the first few components retain substantial degrees of freedom under moderate smoothing, motivating dimensionality reduction.


<!-- p:31 -->


#### Two-dimensional case

In two dimensions, the penalization matrix takes the form:

$$P _ { \lambda } = \lambda _ { x } I _ { n _ { z } } \otimes D _ { n _ { x } , q _ { x } } ^ { T } D _ { n _ { x } , q _ { x } } + \lambda _ { z } D _ { n _ { z } , q _ { z } } ^ { T } D _ { n _ { z } , q _ { z } } \otimes I _ { n _ { x } } ,$$

with eigendecompositions DTx and DT Dnz,qz = UzΣzUT. nx,qx nz,qz

Define U = Uz ⊗ Ux, and θ = Uβ. Then the WH estimate becomes:

$$\hat { y } = U ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W y \quad \text {where} \quad S _ { \lambda } = \lambda _ { x } I _ { n _ { z } } \otimes \Sigma _ { x } + \lambda _ { z } \Sigma _ { z } \otimes I _ { n _ { x } } .$$

As in the one-dimensional case, this representation reveals how smoothing operates via coordinate-wise shrinkage in the eigenbasis. Section E of the appendices displays the corresponding per-parameter effective degrees of freedom.

#### Rank reduction strategy

Inns s oe    s       ony especially those associated with high eigenvalues. This suggests reducing the dimension by keeping only the p &lt; n components with the lowest eigenvalues.

In the one-dimensional case, the reduced-rank approximation is:

$$\hat { y } _ { p } = U _ { p } ( U _ { p } ^ { T } W U _ { p } + \lambda \Sigma _ { p } ) ^ { - 1 } U _ { p } ^ { T } W y$$

where Up and Σp consist of the first p eigenvectors and their corresponding eigenvalues respectively.

In the two-dimensional case, we retain px and pz eigenvectors in each dimension and use:

$$\hat { y } _ { p _ { x } , p _ { z } } = U _ { p _ { x } , p _ { z } } ( U _ { p _ { x } , p _ { z } } ^ { T } W U _ { p _ { x } , p _ { z } } + \lambda _ { x } I _ { p _ { z } } \otimes \Sigma _ { x , p _ { x } } + \lambda _ { z } \Sigma _ { z , p _ { z } } \otimes I _ { p _ { x } } ) ^ { - 1 } U _ { p _ { x } , p _ { z } } ^ { T } W y$$

with Upx,pz = Uz,pz ⊗ Ux,px. In that case, given a target number of parameters pmax, we propose selecting (px, pz) such that pxpz ≤ pmax and px/nx ≈ pz/nz using the rule:

$$\kappa = \sqrt { p _ { \max } / n _ { x } n _ { z } } , \ \ p _ { x } = \lfloor \min ( \kappa , 1 ) n _ { x } \rfloor , \ \ p _ { z } = \lfloor \min ( \kappa , 1 ) n _ { z } \rfloor .$$

Adaptations for generalized WH smoothing follow by replacing (y, W) with (zk, Wk) in the above expressions.


<!-- p:32 -->


#### Efficient computation via GLAM

Currie, Durban, and Eilers (2006) propose a general framework, Generalized Linear Array Models (GLAM), that exploits Kronecker structure for efficient computations. In our context, the model matrix Upx,pz inherits a Kronecker product form, allowing operations that rely on this matrix to be executed dimension-wise without explicit construction of the full matrix. This significantly reduces memory use and computation time in the two-dimensional rank-reduced WH framework.

#### Impact of using the rank-reduced basis

We now evaluate the impact of the rank-reduced WH basis introduced in Section 6.4 in terms of both smoothing accuracy and computational speed. For context, results are compared against those obtained using P-spline smoothing with the same number of basis functions.

To ensure a fair comparison, both approaches were implemented in the same computational framework, including the use of GLAM in the two-dimensional case—only the structure of the basis (and hence the model matrix) differs. The penalty structure, as well as the unpenalized fixed effects (polynomials of degree q − 1), are identical.

In addition to the full basis of size 450 (30 × 15), three reduced basis of respective size 288 (24 × 12), 128 (16 × 8) and 32 (8 × 4) were considered.

As in Section 5.6, accuracy is assessed using the relative LAML error defined in Equation 13. Note, however, that since both reduced-rank and P-spline smoothers rely on different bases and penalization matrices, their LAML expressions are different from the one used for full-rank WH smoothing. Hence, a reduced model can exhibit a higher LAML than the full-rank version at its selected smoothing parameter.

Figure 6 summarises the average speed-up achieved by both the reduced-rank and P-spline smoothers compared to the full-rank WH smoothing. As the number of retained parameters decreases, computation time drops substantially. Compared to the full-rank WH smoothing (unoptimized):

- the 128-parameter basis achieves an 88 × speed-up;
- the 32-parameter basis achieves up to 256 × faster computation.

The alternate iteration and performance iteration strategies outperform the outer iteration in the reduced setting, primarily because model matrix construction becomes the new computational bottleneck—even with the use of the GLAM framework. In this context, the Newton algorithm combined with alternate iteration proves to be the most efficient, with the generalized FellnerSchall update being nearly as competitive for smaller bases.

The gains in computational speed come with a moderate tradeoff in estimation accuracy. As shown in Figure 7, the relative LAML errors remain small:


<!-- p:33 -->


Figure 6: Computation speed improvement from WH smoothing with a reduced-rank basis (solid lines) or P-spline basis (dashed lines), relative to unoptimized full-rank WH smoothing, as a function of basis size.

Nelder-Mead

Fellner-Schall

Newton

153,18

137,78

100

38,60

37,15

100,65

40,64

96,92

13,55

23,89

27,62

34,94

10

11,46

5,34

5,93

2,51

5,74

4,35

1,84

0,80

2,48

1,29

time improvement factor

1,64

1

0,72

1,28

244,43

224,21

100

75,66

52,81

210,99

67,44

189,30

64,92

61,04

18,78

38,40

17,95

9,25

10

5,37

8,70

Computation t

0,73

2,49

1,27

4,54

2.57

2,42

2,47

0,73

1,22

215,00

256,31

100

204,41

88,31

191,71

44,98

75,70

33,42

13,15

10

5,51

13,08

iteration

3,55

4,44

1,26

3,42

1,21

450

288

128

32

450

288

128

32

450

288

128

32

Number of retained parameters

- For the 128-parameter basis, the average error is just 0.82%.
- For the 32-parameter basis, it rises to 2.26%.

Across all sizes, the reduced-rank WH smoother slightly outperforms the P-spline smoother in terms of LAML error, confirming its effectiveness as a principled dimension reduction strategy.


<!-- p:34 -->


Figure 7: Relative LAML error of WH smoothing with a reduced-rank basis (solid lines) or a P-spline basis (dashed lines), with respect to unoptimized full-rank WH smoothing, as a function of basis size.

marginal likelihood

4,51%

%

%ε

error on

2%

2,26%

1,21%

Relative

1%

0,33%

0,91%

0,82%

%0

●

0,00%

0,05%

450

288

128

32

Number of retained parameters

Smoothing basis

WH (rank-reduced)

P-splines

## 7 How to extrapolate the smoothing?

Semi-parametric methods such as P-splines and Whittaker-Henderson (WH) smoothing naturally allow for extrapolation—that is, predicting values outside the range of the original data. Extrapolation is handled by solving an extended smoothing problem where extrapolated positions are associated with zero-weight observations.

However, in the two-dimensional case, extrapolation must be performed carefully: constraints are needed to ensure that the extrapolated solution remains consistent with the original smoothing result over the observed data. Following the approach introduced by Carballo, Durban, and Lee (2021) for P-splines, we now extend WH smoothing to support extrapolation while also enabling the construction of credibility intervals that capture uncertainty both inside and outside the original observation domain.

### 7.1 Defining the extrapolation of the smoothing

Let  be the WH smoothing result obtained from an observation vector y defined over positions x (in 1D) or (x, z) (in 2D). We wish to extend predictions to a larger domain x+ (or (x+, z+)), with x ⊂ x+ and similarly for z.

To preserve WH smoothing's requirement for evenly spaced points, we assume that x+ and z+ are sequences of consecutive integers. Let n+ be the length of x+ in the on-dimensional case. In the two-dimensional case, let nx+ and nz+ be the lengths of x+ and z+ and note n+ = nx+ × nz+.


<!-- p:35 -->


We define matrices Cx and Cz such that each extracts the indices of the original data from the larger domain. Specifically: Cj = (O | Ini | O), where j ∈ {x, z} and Inj is an identity matrix aligned with the observed positions. Define the matrix C as:

$$C = \begin{cases} C _ { x } & \text {in the one-dimensional case,} \\ C _ { z } \otimes C _ { x } & \text {in the two-dimensional case.} \end{cases}$$

Then C has the following useful properties:

- For any full-domain vector y+, Cy+ returns the observed values only.
- CTy embeds the observed values into a larger zero-padded vector.
- CCT = In and CTC is a 2 × 2 block matrix with an identity matrix block and zeros everywhere else.

The extrapolated WH smoothing is defined as the solution to the following extended problem:

$$\hat { y } _ { + } = \arg \min _ { \theta _ { + } } \left \{ ( y _ { + } - \theta _ { + } ) ^ { T } W _ { + } ( y _ { + } - \theta _ { + } ) + \theta _ { + } ^ { T } P _ { + } \theta _ { + } \right \}$$

where:

- y+ = CTy is the extended data vector (zeros for unobserved points),
- W+ = CTWC is the extended weight matrix (zeros for unobserved points),
- P+ is the penalization matrix over the extended grid, defined as:

$$P _ { + } = \begin{cases} \lambda D _ { n _ { + } , q } ^ { T } D _ { n _ { + } , q } & \text {in the one-dimensional case,} \\ \lambda _ { x } I _ { z + } \otimes D _ { n _ { x + } , q _ { x } } ^ { T } D _ { n _ { x + } , q _ { x } } + \lambda _ { z } D _ { n _ { z + } , q _ { z } } ^ { T } D _ { n _ { z + } , q _ { z } } \otimes I _ { x + } & \text {in the two-dimensional case.} \end{cases}$$

Importantly, the smoothing parameters λ, λx, and λz must remain fixed during extrapolation— they are inherited from the original fit and no new information is introduced.

The fidelity term in Equation 14 simplifies to:

$$( y _ { + } - \theta _ { + } ) ^ { T } V _ { + } ( y _ { + } - \theta _ { + } ) = ( C ^ { T } y - \theta _ { + } ) ^ { T } C ^ { T } W C ( C ^ { T } y - \theta _ { + } ) = ( y - \theta ) ^ { T } W ( y - \theta )$$

where θ = Cθ+. This is the fidelity term from the original fit.

The smoothness criterion, on the other hand, now applies to the entire extended domain, constraining the extrapolated parts of + to remain smooth and consistent with the trend learned from the data.


<!-- p:36 -->


The same extrapolation approach applies directly to generalized WH smoothing, simply by replacing y by zk and W by Wk, obtained at convergence of the PIRLS algorithm and setting σ2 = 1 in the derived credible intervals.

### 7.2 Unconstrained solution for the 1D case

The solution to the extrapolation problem in Equation 14 can be obtained directly, as in Section 1.1, by taking derivatives with respect to θ+ and setting them to zero. This yields the closed-form solution:

$$\hat { y } _ { + } = ( W _ { + } + P _ { + } ) ^ { - 1 } W _ { + } y _ { + } \quad \text {where} \quad y _ { + } = C ^ { T } y \quad \text {and} \quad W _ { + } = C ^ { T } W C .$$

(1−+ ∼ +θ e (1−++θ ∼ +θ  +   s  s obtain, as in Section 2, the following credible interval:

$$\mathbb { E } ( y _ { + } ) \, | \, y _ { + } \in \left [ ( W _ { + } + P _ { + } ) ^ { - 1 } W _ { + } y _ { + } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \sigma ^ { 2 } \text {diag} \left \{ ( W _ { + } + P _ { + } ) ^ { - 1 } \right \} } \right ] .$$

To get a better understanding about how the variance-covariance matrix V+ = (W+ + P+)−1 for the unconstrained extrapolation problem of Equation 14 is related to the variance-covariance matrix V = (W + Pλ)−1 of the original smoothing problem, introduce matrices  ̄j (for j ∈ x, z) which selects the rows in the extrapolated domain that are not part of the original data and define:

$$\overline { C } = \begin{cases} \overline { C } _ { x } & \text { in the one-dimensional case,} \\ \overline { C } _ { z } \otimes \overline { C } _ { x } & \text { in the two-dimensional case,} \end{cases} \quad \text {and} \quad Q = \left [ \frac { C } { \overline { C } } \right ] .$$

With this definition, Q is a permutation matrix moving observed positions to the top.

In the unidimensional case, the extended difference matrix Dn+,q takes the block-wise form:

$$& \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

The extended weight and penalization matrices may be rewritten:

$$W _ { + } = Q ^ { T } \begin{bmatrix} W & 0 \\ 0 & 0 \end{bmatrix} Q \quad \text {and} \quad P _ { + } = D _ { n _ { + } , q } ^ { T } D _ { n _ { + } , q } = \lambda Q ^ { T } \begin{bmatrix} P _ { \lambda } + P _ { + } ^ { 1 1 } & P _ { + } ^ { 1 2 } \\ P _ { + } ^ { 2 1 } & P _ { + } ^ { 2 2 } \end{bmatrix} Q$$

where Pij i = λDT Dj, for i, j ∈ {1, 2}.

This block structure allows us to apply standard results for partitioned matrix inverses to derive:


<!-- p:37 -->


$$V _ { + } & = Q ^ { T } \begin{bmatrix} V _ { + } ^ { 1 1 } & V _ { + } ^ { 1 2 } \\ V _ { + } ^ { 2 1 } & V _ { + } ^ { 2 2 } \end{bmatrix} Q = Q ^ { T } \left [ - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V _ { + } ^ { 1 1 } & ( P _ { + } ^ { 2 1 } ) ^ { - 1 } P _ { + } ^ { 1 1 } P _ { + } ^ { 2 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \\ & ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V _ { + } ^ { 1 1 } & ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V _ { + } ^ { 1 1 } P _ { + } ^ { 2 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } + ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \right ] Q \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ & \\ &$$

From the above, we retrieve:

$$C \hat { y } _ { + } = C V _ { + } W _ { + } y _ { + } = C Q ^ { T } V _ { + } Q C ^ { T } W y = V _ { + } ^ { 1 1 } W y .$$

This coincides with the original fit  only if V11 = V. In general, this equality does not hold, since the extrapolation solution minimizes the total smoothness of the extended vector, not just of the observed part.

In V22, V+2, we identify:

- a propagation term: (P22)-1 P21V11 P12(P2)−1, capturing the uncertainty transferred from the known part to the extrapolated part;
- an innovation error term: (P22)-1 associated with the prior on the extrapolated coefficients Cy+.

In the one-dimensional case, D2 is block-diagonal with invertible triangular blocks, so:

$$P _ { + } ^ { 1 1 } - P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } = D _ { 1 } ^ { T } D _ { 1 } - D _ { 1 } ^ { T } D _ { 2 } ( D _ { 2 } ^ { T } D _ { 2 } ) ^ { - 1 } D 2 ^ { T } D _ { 1 } = 0$$

which means that V11 = (W + Pλ)−1 = V. This confirms the result from Carballo et al. (2021), namely that with a difference-based penalty, a perfectly smooth extrapolation that leaves the original fit unchanged can always be constructed in the one-dimensional case.

This behaviour is illustrated in Figure 8, which shows the extrapolated fit (with q = 2) obtained from generalized WH smoothing applied to the annuity portfolio used previously. The extrapolation follows a straight line—the polynomial of degree q − 1 = 1—and joins smoothly with the original curve.

### 7.3 Constrained solution for the 2D case

In the two-dimensional case, while the extended penalization matrix P+ still takes the same = 0, therefore V11 ≠ V and C+ ≠ . Solving the unconstrained extrapolation problem thus leads to a modification of the estimated coefficients for the observed data positions, as demonstrated by Carballo, Durban, and Lee (2021).

This difference arises because, unlike the one-dimensional case, the smoothness criterion in two dimensions penalizes both rows and columns simultaneously, making it impossible to extrapolate without increasing the penalization. Since no new data is introduced in the extrapolated region, the smoothness criterion weighs more heavily in the optimization, prompting adjustments to the originally fitted values in order to produce a globally smoother estimate.


<!-- p:38 -->


Figure 8: Extrapolation of one-dimensional WH smoothing. The smoother is extrapolated on both sides of the initial observation range following a polynomial of degree q - 1 (in this case a straight line as q = 2).

Force of mortality (logarithmic scale)

100

10-3

40

50

60

0

80

90

100

110

Age

To address this, we follow the approach proposed by Carballo, Durban, and Lee (2021) and formulate a constrained optimization problem that enforces preservation of the original fitted values in the smoothing region. This is done by introducing a Lagrange multiplier ω and solving the following constrained problem:

$$( \hat { y } _ { + } ^ { * } , \hat { \omega } ) = \arg \min _ { \theta _ { + } ^ { * } , \omega } \left \{ ( y _ { + } - \theta _ { + } ^ { * } ) ^ { T } W _ { + } ( y _ { + } - \theta _ { + } ^ { * } ) + \theta _ { + } ^ { * T } P _ { + } \theta _ { + } ^ { * } + 2 \omega ^ { T } ( C \theta _ { + } ^ { * } - \hat { y } ) \right \} .$$

This optimization admits a closed-form solution for the constrained extrapolated estimator + as a linear transformation of y. The derivation details are provided in Section F of the appendices. The final form is:

$$Q ^ { T } \left [ \begin{matrix} I \\ - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } \end{matrix} \right ] \hat { y }$$

and the associated variance-covariance matrix is:

$$V _ { + } ^ { * } = Q ^ { T } \left [ \begin{matrix} V & - V P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \\ - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V & ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } + ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \right ] Q .$$


<!-- p:39 -->


This formulation differs from the variance matrix of the unconstrained solution. Indeed, it enforces the constraint that the initial coefficients remain unchanged, as reflected by the presence of V (the original variance matrix) instead of V11. The corresponding credible intervals are:

$$\mathbb { E } ( y _ { + } ) \left | \, y _ { + } \in \left [ \hat { y } _ { + } ^ { * } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \sigma ^ { 2 } \text {diag} ( V _ { + } ^ { * } ) } \right ] .$$

The following figures illustrate the impact of the constrained extrapolation procedure discussed above, using the LTC portfolio of 100,000 policyholders as a case study.

- Figure 9, left (mortality rates): this panel shows the estimated mortality rates obtained after applying the constrained extrapolation procedure to the two-dimensional WH smoothing model. The dotted lines indicate the boundaries of the original smoothing region. Visually, the transition from the smoothing region to the extrapolated area is seamless—the extrapolated surface naturally extends the smoothed mortality rates while respecting the original fitted values within the data range.
- Figure 9, right (standard deviation): this panel displays the posterior standard deviation (or credible interval width) associated with the extrapolated estimates. It reflects both the uncertainty from the original smoothing and the innovation error introduced in the extrapolated region. As expected, the standard deviation increases as we move away from the observed region, illustrating growing uncertainty about farther values.
- Figure 10 (ratio of mortality rates): this heatmap shows the pointwise ratio between the unconstrained and constrained extrapolation of the mortality rates. A value above 1 indicates that the unconstrained version overshoots the constrained one at that location,

Figure 9: Constrained extrapolation of 2D WH smoothing. The contour lines of mortality rates and the associated standard deviation are depicted. The dotted lines delimit the boundaries of the initial smoothing region.

Force of

Standard

mortality

deviation

100


1,447

1,310

0,968

0,890

0,652

0,621

90

06

0,441

0,476

Age

0,298

Age

0,377

0,204

0,292

80

0,144

80

0,213

0,101

0,145

0,074

0,102

70

0,053

70

0,081

0,034

1900

60

10

15

20

60

5

10

15

20

Duration in LTC


<!-- p:40 -->


while values below 1 indicate underestimation. We observe that discrepancies exist not only in the extrapolated region but also within the original data region—confirming that the unconstrained approach distorts the original estimates in order to achieve overall smoothness.

Figure 10: Ratio of mortality rates resulting from the extrapolation of 2D WH smoothing. The numerator corresponds to the unconstrained extrapolation and the denominator to the constrained extrapolation presented in Figure 9.

Force of

mortality

ratio

100

1,20

1,10

90

1,05

Age

1,01

80

0,99

0,95

0,90

70

0,80

0,50

60

10

15

20

Duration in LTC

- Figure 11 (ratio of standard deviations): this final figure includes two panels comparing uncertainty estimates.
- Left panel: ratio of standard deviation from the unconstrained extrapolation over that from the constrained extrapolation (including innovation error). The unconstrained vro o    o o o  t ron but also within the original data region, again reflecting the adjustments made to the original estimates in order to achieve overall smoothness.
- Right panel: ratio of standard deviation from the constrained extrapolation without innovation error over the fully constrained version with innovation error. This illustrates the contribution of the innovation error to the total uncertainty—it is substantial and should not be neglected.

## 8 Discussion

#### Choosing the order of the penalization

Throughout this work, we have assumed second-order difference matrices for penalization. This choice is both standard and meaningful: from a Bayesian perspective, it corresponds to a prior belief that the log-transformed quantity of interest evolves linearly, which implies exponential behaviour on the original scale—consistent with actuarial models such as Gompertz.


<!-- p:41 -->


Figure 11: Ratio of standard deviation of log-mortality rates from the three extrapolation methods. Left: unconstrained vs constrained with innovation error. Right: constrained without vs with innovation error. In both, the denominator is the fully constrained method of Figure 9.

Unconstrained

Without innovation error

Standard

deviation

ratio

100

0,99

0,98

90

0,95

Age

0,90

80

0,80

0,75

70

0,70

0,65

60

10

15

200

5

10

15

20

Duration in LTC

The difference order directly shapes both the estimated trend and its extrapolation: higher-order penalties allow for more flexibility, but may induce unstable or erratic behaviour outside the data range. While Whittaker originally used third-order differences and higher orders can marginally improve model fit according to information criteria such as AIC, second-order penalties typically offer a robust compromise between smoothness, interpretability, and extrapolation stability. A detailed evaluation is provided in Section G of the appendices.

#### Summary of contributions

This paper revisits the classical Whittaker-Henderson (WH) smoothing approach through the lens of modern statistical modelling. Each section brought forward a key practical insight:

- Section 2 established that WH smoothing is more than an empirical method. It has a firm Bayesian foundation. Under Gaussian assumptions, credibility intervals may be derived and used as practical substitutes to confidence intervals.
- Section 3 clarified how to construct observation and weight vectors in survival analysis models: using log-crude rates as observations and event counts as weights yields a sound statistical formulation.


<!-- p:42 -->


- Section 4 introduced generalized WH smoothing, in which the penalization is applied directly to the likelihood rather than a normal approximation. This refined method yields more accurate results, especially in situations where the available data volume is limited but the number of combinations is high, such as in the two-dimensional case.
- Section 5 advocated for smoothing parameter selection via marginal likelihood (or its Laplace approximation, LAML), offering a principled and robust alternative to heuristic criteria like AIC or GCV.
- Section 6 presented two computational improvements: one exploits the banded structure of WH matrices to reduce runtime by up to a factor of 25; the other relies on reduced-rank smoothing basis, leading to even faster estimation (up to 250 × speed-up) with limited loss in accuracy, slightly outperforming P-splines.
- Section 7 addressed extrapolation: while WH smoothing naturally extends beyond the data range, constraints are needed in two dimensions to preserve the original fit. We proposed a method to extrapolate while accounting for both structural uncertainty and innovation error, and provided credible intervals accordingly.

All these techniques are available in the WH package for the statistical software R (R Core Team 2025), including automated smoothing parameter selection and constrained extrapolation with uncertainty quantification.

#### Limitations and outlook

Despite its strong practical appeal, WH smoothing has limitations that suggest several avenues for future work:

- Regular spacing requirement: WH smoothing assumes evenly spaced observations, which aligns well with standard life insurance grids (age and/or duration). However, this is less suitable when events are concentrated in a short period, such as in disability or long-term care claims. One solution is to combine finer discretization in early durations with methods like P-splines that accommodate irregular grids. Alternatively, and adaptive WH smoothing procedure (based on the ideas in Ruppert and Carroll 2000; Krivobokova, Crainiceanu, and Kauermann 2008) could offer a way to retain regular spacing while varying the smoothness locally.
- Limited covariate handling: The basic WH framework does not accommodate additional explanatory variables (e.g., gender or policy features). However, WH smoothing can be extended using ideas from smoothing spline ANOVA and hierarchical models (Lee and Durban 2011; Gu 2013), allowing for structured random effects and flexible interactions. This opens the door to richer, more personalized experience modelling while preserving interpretability.


<!-- p:43 -->


In sum, revisiting WH smoothing through a modern lens reinforces its theoretical foundations and offers practitioners fast, transparent, and adaptable tools for experience modelling. It remains a compelling alternative to more recent—yet often more opaque—techniques when working with evenly spaced discrete data.

## Appendices

### A Exposure computation in the survival analysis framework

This appendix outlines the methodology used to compute central exposure to risk in survival analysis, for both univariate and bivariate settings.

The derivation relies on standard assumptions of left truncation and non-informative right censoring, and models the hazard rate as piecewise constant over one-year intervals. This discretization allows reformulating the continuous-time log-likelihood in terms of aggregated death counts and exposure durations.

In the one-dimensional case, exposure corresponds to the total time under observation within each integer age interval. The same principle extends naturally to the two-dimensional case, such as mortality modelling by age and duration in LTC, where exposure is computed over the age-duration grid using the same piecewise constant assumption.

These quantities—death counts and central exposures—form the inputs to the generalized Whittaker-Henderson smoothing approach used throughout the paper.

#### One-dimensional case

Consider the observation of m individuals in a longitudinal study subject to left truncation and non-informative right censoring. Suppose we aim to estimate a distribution that depends on only one continuous explanatory variable, denoted by x. One may for example think of a mortality distribution with the explanatory variable of interest x representing age. Such a distribution is fully characterized by either of the following quantities:

- the cumulative distribution function F(x) or its complement, the survival function S(x) = 1 − F(x),
- the instantaneous hazard function μ(x) = d ln S(x). xp
- the associated probability density function f(x) = d S(x), xp

Those 3 quantities are related by the following relationships:

$$S ( x ) = \exp \left ( \int _ { u = 0 } ^ { x } \mu ( u ) d u \right ) \quad \text {and} \quad f ( x ) = \mu ( x ) S ( x ) .$$


<!-- p:47 -->


Suppose that the considered distribution depends on a vector of parameters θ estimated using maximum likelihood. The likelihood associated with the observation of the individuals takes the form:

$$\mathcal { L } ( \theta ) = \prod _ { i = 1 } ^ { m } \left [ \frac { f ( x _ { i } + t _ { i } , \theta ) } { S ( x _ { i } , \theta ) } \right ] ^ { \delta _ { i } } \left [ \frac { S ( x _ { i } + t _ { i } , \theta ) } { S ( x _ { i } , \theta ) } \right ] ^ { 1 - \delta _ { i } }$$

where xi represents the age at the start of observation, ti represents the duration of observation for individual i and δi is the indicator of event observation, which takes the value 1 if the event of interest is observed and 0 if the observation is instead censored. We will not go into the details of how these three quantities are derived, however they should take into account individual-specific information such as the subscription date, lapse date if applicable, as well as the global characteristics of the product such as the presence of a waiting period or medical selection phenomenon, and the choice of a restricted observation period due to delays in the reporting of event of interests. These factors typically result in a narrower effective observation window than the actual time individuals spend in the portfolio.

Using Equation 15, the log-likelihood associated with Equation 16 can be rewritten using only the instantaneous hazard function (also known as force of mortality in the case of the death risk):

$$\ell ( \theta ) = \sum _ { i = 1 } ^ { m } \left [ \delta _ { i } \ln \mu ( x _ { i } + t _ { i } , \theta ) - \sum _ { u = 0 } ^ { t _ { i } } \mu ( x _ { i } + u , \theta ) d u \right ]$$

We discretize the problem by assuming that the mortality rate is piecewise constant over one-year intervals between two integer ages or more formally μ(x + €) = μ(x) for all x ∈ N and ε ∈ [0, 1[. Further note that, if 1 denotes the indicator function, then for any xmin ≤ a &lt; xmax, may therefore be rewritten as:

$$\text {there be rewritten as.} \\ \ell ( \theta ) = \sum _ { i = 1 } ^ { m } \left [ \sum _ { x = x _ { \min } } ^ { x _ { \max } } \delta _ { i } 1 ( x \leq x _ { i } + t _ { i } < x + 1 ) \ln \mu ( x _ { i } + t _ { i } , \theta ) \\ - \int _ { u = 0 } ^ { t _ { i } } \sum _ { x = x _ { \min } } ^ { x _ { \max } } 1 ( x \leq x _ { i } + u < x + 1 ) \mu ( x _ { i } + u , \theta ) d u \right ] .$$

The assumption of piecewise constant mortality rates implies that:

$$1 ( x \leq x _ { i } + t _ { i } < x + 1 ) \ln \mu ( x _ { i } + t _ { i } , \theta ) = 1 ( x \leq x _ { i } + t _ { i } < x + 1 ) \ln \mu ( x , \theta ) \quad \text {and} \\ 1 ( x \leq x _ { i } + u < x + 1 ) \mu ( x _ { i } + u , \theta ) = 1 ( x \leq x _ { i } + u < x + 1 ) \mu ( x , \theta ) .$$

It is then possible to interchange the two summations to obtain the following expressions:


<!-- p:48 -->


$$\ell ( \theta ) = \sum _ { x = x _ { \min } } ^ { x _ { \max } } \left [ \ln \mu ( x , \theta ) d ( x ) - \mu ( x , \theta ) e _ { c } ( x ) \right ] \quad \text {where} \\$$

$$d ( x ) = \sum _ { i = 1 } ^ { m } \delta _ { i } 1 ( x \leq x _ { i } + t _ { i } < x + 1 ) \quad \text {and} \\$$

$$e _ { c } ( x ) = \sum _ { i = 1 } ^ { m } \int _ { u = 0 } ^ { t _ { i } } 1 ( x \leq x _ { i } + u < x + 1 ) d u = \sum _ { i = 1 } ^ { m } \left [ \min ( t _ { i } , x - x _ { i } + 1 ) - \max ( 0 , x - x _ { i } ) \right ] ^ { + }$$

by denoting a+ = max(a, 0), where d(x) and ec(x) correspond to the number of observed deaths between ages x and x + 1 and the sum of observation durations of individuals between these ages, respectively. The latter quantity is also known as central exposure to risk.

#### Two-dimensional case

The extension of the proposed approach to the two-dimensional framework requires only minor adjustments to the previous reasoning. Let zmin = min(z) and zmax = max(z). The piecewise constant assumption for the mortality rate needs to be extended to the second dimension. Formally, assume that μ(x + ∈, z + ξ) = μ(x, z) for all pairs x, z ∈ N and ∈, ξ ∈ [0, 1[. The sums involving the variable x are then replaced by double sums considering all combinations of x and z. The log-likelihood becomes:

$$x _ { \max } = z _ { \max }$$

$$d \ z . \ The \log { - \text {likelihood becomes:} } \\ \ell ( \theta ) = \sum _ { x \min z = z _ { \min } } ^ { x _ { \max } } \sum _ { m } \left [ \ln \mu ( x , z , \theta ) d ( x , z ) - \mu ( x , z , \theta ) e _ { \text {c} } ( x , z ) \right ] \text {  where} \\ d ( x , z ) = \sum _ { i = 1 } ^ { m } \delta _ { 1 } ( x \leq x _ { i } + t _ { i } < x + 1 ) 1 ( z \leq z _ { i } + t _ { i } < z + 1 ) \quad \text {and} \\ \ t _ { i } = \sum _ { m } ^ { m } \int _ { 1 } ^ { 1 } 1 ( x \leq x _ { i } + u < x + 1 ) 1 ( z \leq z _ { i } + u < z + 1 ) d u \\ = \sum _ { i = 1 } ^ { m } \left [ \min ( t _ { i } , x + 1 - x _ { i } , z + 1 - z _ { i } ) - \max ( 0 , x - x _ { i } , z - z _ { i } ) \right ] ^ { + } . \\$$

### B Simulated datasets

This appendix details the simulation process used to generate the datasets on which the comparative analysis of accuracy and computational efficiency is based.


<!-- p:49 -->


#### General approach

The simulated datasets were constructed following a five-step methodology:

1. Define hypothetical underlying laws to serve as the ground truth.
2. Generate an initial population of insured individuals.
3. Simulate life outcomes for each individual.
4. Extract samples of a predetermined size from the simulated population.
5. Compute aggregated event counts and central exposures for each sample.

#### Defining the underlying laws

The synthetic laws used in the simulations are not meant to be accurate representations of real-world phenomena. However, they incorporate features commonly observed in mortality and long-term care (LTC) experience studies to ensure plausible dynamics for testing purposes.

#### General population mortality

Mortality rates are derived from the Human Mortality Database for France in 2019. The dataset includes death counts and central exposure to risk by age (0 to 109) and gender. A smoothing algorithm is applied to reduce sampling noise, particularly at younger ages. The resulting rates define the general population mortality.

#### Insured population mortality

To reflect the well-documented observation that insured individuals generally exhibit lower os  a o t o  dtstoeor  o oe, ot adjustment factor to the general population mortality. This factor transitions from 40% at age 30 to 100% at age 90, with a midpoint of 70% at age 60. The adjusted rates define the insured population mortality, which is used for all annuity simulations.


<!-- p:50 -->


#### Long-Term Care (LTC) transition and mortality laws

For LTC simulations, assumptions are needed for:

- Autonomous mortality (i.e., mortality of individuals not in LTC),
- Incidence of entry into LTC,
- Mortality within LTC.

We draw upon assumptions from a technical note published by the reinsurer SCOR in 1995, adapted to use the previously defined insured population mortality qref(x, g) for age x and gender g:

- qa(x, g) = 0.8 × qref(x, g) (autonomous mortality),
- i(x) = 5.535 × 10−3 exp[(x − 52)/8] (LTC incidence),
- (  I) ·0 + ( x)) × 7 = ( x)() ·

We refine the disabled mortality law to include a shock at LTC onset, reflecting heightened mortality during the first years in LTC, caused by cancer-related admissions (see for example Biessy 2015 for details about this phenomenon and impacts on curves for mortality in LTC). The refined mortality is:

$$q _ { i } ( x , t , g ) = 2 \times q _ { \text {ref} } ( x , g ) + 0 . 0 3 5 + K ( g ) f ( x - t ) h ( t ) .$$

where:

- t is the time since onset of LTC,
- K(g) encodes a gender-specific intensity (0.5 for females, 0.75 for males),
- f and h are logistic-shaped modifiers to reflect attenuation with age and time since entry, respectively.

This formulation captures the elevated initial mortality due to severe conditions like terminal cancers, which tapers off within two years or by age 90. For further discussion, see Biessy (2016).


<!-- p:51 -->


#### Simulating a population of insured lives

We simulate 1,000,000 insured individuals over a subscription period from 1990 to 2009. Eligibility spans:

- ages 20 to 65 for annuity policies;
- ages 50 to 75 for LTC policies.

Subscription age, year, and gender are drawn with replacement from weighted distributions based on French population demographics. Birth dates and subscription dates are assigned uniformly at random within valid ranges.

#### Simulating life trajectories

For each individual, we simulate life outcomes from their subscription date up to December 31, 2024. The process involves:

1. Dividing the time axis into intervals delimited by birthdays.
2. For each interval, computing event probabilities based on applicable mortality or incidence rates.
3. Drawing events using uniform random variables:
- In the LTC case, distinguishing between autonomous death and LTC incidence.
- Recording the event date accordingly.
4. If no terminating event occurs, proceeding to the next interval.

For individuals who enter LTC, a second simulation phase begins, spanning from LTC entry to the end of observation. This time, the timeline is segmented by both age and duration-in-LTC anniversaries. Within each subperiod, we compute and simulate death-in-LTC events.

#### Sampling subsets from the simulated population

#### Sample from the simulated population to get a subset of desired size

To match study requirements, we extract 100 independent samples of 100,000 individuals from the simulated population without replacement. While not fully independent, overlap is limited (~10% on average), which is deemed acceptable for the study's objectives.


<!-- p:52 -->


#### Aggregating events and exposures

Each sample is aggregated to produce death counts and central exposures :

- by age in the annuity case;
- by age and duration in the LTC case.

Aggregation is performed using the methodology described in Appendix A.

### C Derivation of marginal likelihood and LAML

This appendix presents the derivations of the marginal likelihood and its Laplace approximation (LAML) used for the automatic selection of smoothing parameters.

In the Gaussian case, where the model assumes normal conditional and prior distributions, the marginal likelihood can be computed in closed form by integrating out the latent parameters. This yields an explicit expression involving the penalty and weight matrices, and forms the basis of the outer iteration strategy.

For more general models in the exponential family, no closed-form solution is available. Instead, we apply a Laplace approximation to the marginal likelihood, based on a second-order expansion of the penalized log-likelihood around its maximum. The resulting LAML criterion is used in the performance and alternated iteration approaches for efficient and principled smoothing parameter selection.

#### Marginal likelihood

Assume that y | θ ∼ N(θ, σ2W−) and θ | λ ∼ N(0, σ2P−). In the empirical Bayes approach, the smoothing parameter λ is estimated by maximizing the marginal likelihood:

$$\mathcal { L } _ { n o r m } ^ { m } ( \lambda ) = f ( y \, | \, \lambda ) = \int f ( y , \theta \, | \, \lambda ) d \theta = \int f ( y \, | \, \theta ) f ( \theta \, | \, \lambda ) d \theta .$$

The conditional and prior densities involved in this integral are:

$$f ( y \, | \, \theta ) & = \sqrt { \frac { | W | _ { + } } { ( 2 \pi \sigma ^ { 2 } ) ^ { n _ { * } } } } \exp \left ( - \frac { 1 } { 2 \sigma ^ { 2 } } ( y - \theta ) ^ { T } W ( y - \theta ) \right ) \\ f ( \theta \, | \, \lambda ) & = \sqrt { \frac { | P _ { \lambda } | _ { + } } { ( 2 \pi \sigma ^ { 2 } ) ^ { p - q } } } \exp \left ( - \frac { 1 } { 2 \sigma ^ { 2 } } \theta ^ { T } P _ { \lambda } \theta \right )$$

where n* is the number of non-zero weights and q is the order of the penalization (corresponding to the rank deficiency of Pλ).


<!-- p:53 -->


We then apply a second-order Taylor expansion of the joint log-density ln f(y, θ | λ) around its mode êλ to approximate the integral:

$$\ln f ( y , \theta \, | \, \lambda ) = \ln f ( y , \hat { \theta } _ { \lambda } \, | \, \lambda ) + \frac { 1 } { 2 } ( \theta - \hat { \theta } _ { \lambda } ) ^ { T } ( W + P _ { \lambda } ) ( \theta - \hat { \theta } _ { \lambda } ) \\$$

This gives the following expression for the marginal likelihood:

$$\mathcal { L } _ { n o r m } ^ { m } ( \lambda ) = f ( y , \hat { \theta } _ { \lambda } \, | \, \lambda ) \int \exp \left [ - \frac { 1 } { 2 \sigma ^ { 2 } } ( \theta - \hat { \theta } _ { \lambda } ) ^ { T } ( W + P _ { \lambda } ) ( \theta - \hat { \theta } _ { \lambda } ) \right ] \mathrm d \theta$$

which evaluates to:

$$\mathcal { L } _ { n o r m } ^ { m } ( \lambda ) = \sqrt { \frac { | W | _ { + } | P _ { \lambda } | _ { + } } { ( 2 \pi \sigma ^ { 2 } ) ^ { n _ { s } - q } | W + P _ { \lambda } | } } \exp \left ( - \frac { 1 } { 2 \sigma ^ { 2 } } \left [ ( y - \hat { \theta } _ { \lambda } ) ^ { T } W ( y - \hat { \theta } _ { \lambda } ) + \hat { \theta } _ { \lambda } ^ { T } P _ { \lambda } \hat { \theta } _ { \lambda } \right ] \right )$$

where θλ = (W + Pλ)−1Wy.

Taking the logarithm yields the marginal log-likelihood:

$$\ell _ { n o r m } ^ { m } ( \lambda ) = - \frac { 1 } { 2 } \left [ ( y - \hat { \theta } _ { \lambda } ) ^ { T } W ( y - \hat { \theta } _ { \lambda } ) / \sigma ^ { 2 } + \hat { \theta } _ { \lambda } ^ { T } P _ { \lambda } \hat { \theta } _ { \lambda } / \sigma ^ { 2 } + \ln | W + P _ { \lambda } | - \ln | P _ { \lambda } | _ { + } + C \right ] .$$

where êλ = (W + Pλ)−1Wy, and C = − ln |W|+ + (n* − q) ln(2πσ2) is a constant independent of λ.

#### Laplace approximation of the marginal likelihood

Assume that the log-likelihood l(θ) is combined with a Gaussian prior on the parameter vector: θ ∼ N(0, P−1). The marginal likelihood of the data (d, ec) given λ is:

$$\mathcal { L } _ { \text {ML} } ^ { m } ( \lambda ) = f ( \text {d} , e _ { c } \, | \, \lambda ) = \int f ( \text {d} , e _ { c } , \theta \, | \, \lambda ) f ( \theta \, | \, \lambda ) d \theta .$$

Since no closed-form expression exists for this integral in the general exponetial family case, we apply a second-order Taylor expansion of the log-posterior around its mode êλ = arg max lp(θ), where lp(θ) = l(θ) − 1θT Pλθ is the penalized log-likelihood.

The resulting Laplace approximation of the marginal likelihood is:

$$\mathcal { L } _ { M L } ^ { m } ( \lambda ) \approx \exp \left ( \ell _ { P } ( \hat { \theta } _ { \lambda } ) \right ) \sqrt { \frac { ( 2 \pi ) ^ { p } } { | W _ { \lambda } + P _ { \lambda } | } } ,$$

where Wλ = Diag(exp(λ)  ec) is the observed Fisher information. Taking the logarithm leads to the LAML criterion:

$$\ell _ { M L } ^ { m } ( \lambda ) \approx \ell ( \hat { \theta } _ { \lambda } ) - \frac { 1 } { 2 } \left [ \hat { \theta } _ { \lambda } ^ { T } P _ { \lambda } \hat { \theta } _ { \lambda } + \ln | W _ { \lambda } + P _ { \lambda } | - \ln | P _ { \lambda } | _ { + } - q \ln ( 2 \pi ) \right ] \stackrel { \text {def} } { = } \ell _ { L A M L } ^ { m } ( \lambda ) .$$


<!-- p:54 -->


### D Algorithms

This appendix presents the computational procedures used to implement the generalized Whittaker-Henderson (WH) smoothing framework and the various automatic selection methods for the associated smoothing parameters.

#### Generalized WH smoothing

Algorithm 1 implements the core iterative procedure for generalized WH smoothing, as introduced in Section 4. It details the iterative computation of the estimated log-rates θ given fixed smoothing parameters and a chosen differencing order. The algorithm iteratively solves a penalized weighted least-squares problem until convergence is achieved, based on a predefined deviance threshold.

```
dependent weights based on the difference matrices of order q.
      deviance threshold.

      ----------------
      Algorithm 1: Iterative solution of generalized Whittaker-Henderson smoothing
      ----------------
      inputs        : d and e_c
      outputs       : \theta
      parameters  : \theta, q, \epsilon = 10^-8
      begin
      |    Construct the penalty matrix P, based on the difference matrices of order q.
      |    k      0
      |    \theta      \ln d/ \epsilon), where d* = max(d, \epsilon)
      |    devv      \infty,    cond     true
      |    while cond do
      |      w_k      Diag(exp(\theta_k) \circ e_c)
      |      z_k      \theta _ + d/ w_k - 1
      |      Form W_k + P_ \lambda by adding w_k to the diagonal of P_a.
      |      Find the Cholesky factor R of W_k + P_a.
      |      Find \substack{th that R^u = w_k, 0 \zeta, by forward substitution.
      |      Find \theta_k+1 such that R^u = w_k+1 = u by backward substitution.
      |      devk+1     devp( \theta_k+1),   cond     devv+1 \leq (1 - \epsilon)devv_k
      |      k       k + 1
      |    \hat{ \theta }     \theta_k
      |
      ----------------

      Smoothing parameter selection, approximations.

```

Algorithm 1: Iterative solution of generalized Whittaker-Henderson smoothing

#### Smoothing parameter selection approaches

In Section 5, we introduced three alternative strategies to automatically calibrate the smoothing parameter λ, based on marginal likelihood maximization. The following three algorithms formalize their respective procedures.


<!-- p:55 -->


Together, these algorithms offer a modular and flexible framework for implementing WH smoothing and its data-driven calibration in practical applications.

#### Outer iteration

Algorithm 2 corresponds to the outer iteration approach. In this strategy, a series of candidate values for λ are tested sequentially. For each candidate, the generalized WH smoother of 1 is applied until convergence, and the corresponding marginal likelihood is evaluated. The process continues until no further improvement is observed. This approach separates the parameter selection and smoothing steps into nested loops.

```
-Algorithm 2: Smoothing parameter selection for generalized Whitaker-Henderson
                       smoothing - outer iteration approach.
                       -----------------
                       inputs        : d and e,
                       outputs       : \a
                       parameters : q, \epsilon = 10^{-8}, \epsilon1 = 10^{-8
                       begin
                       |    k       0
                       |    laml0     \cx,    cond.laml      true
                       while cond.laml do
                         |    If k = 0, choose an arbitrary initial value \a1 for the smoothing parameter(s);
                             otherwise, choose the next value \lambda+1 using the desired heuristic.
                             k      k + 1
                             Use Algorithm 1 to determine the vector \theta_{\lambda} associated with the choice of \lambda,
                             using a convergence threshold of \epsilon.
                             Calculate the marginal likelihood \ell(LAML(\lambda) associated with the choice of \lambda,
                             using the intermediate quantities calculated during the estimation of \theta_{\lambda}.
                             \laml   \ell^{LAML(\lambda)},   cond.laml      \laml, \geq (1 + \epsilon.laml) \laml_{k-1}
                         \laml    \lambda_{k}

```

Algorithm 2: Smoothing parameter selection for generalized Whittaker-Henderson smoothing - outer iteration approach.

#### Performance iteration

Algorithm 3 implements the performance iteration strategy. Here, the smoothing parameter is optimized at each step based on updated pseudo-response and weight vectors. The smoother and the parameter estimation are intertwined, with λ being re-optimized after each update of the linear predictor. This often leads to faster convergence toward the maximum marginal likelihood compared to the outer iteration approach.

Let us note that in the algorithm, lLAML(λk+1 | θk+1) denotes an approximate LAML, in which θk+1—the maximizer of the approximate normal marginal likelihood constructed from wk and zk—replaces the true penalized likelihood maximizer λk+1, which is not available in the performance iteration approach.


<!-- p:56 -->


```
- The performance iteration approach.
      - Algorithm 3: Parameter selection for generalized Whittaker-Henderson smoothing -
        performance iteration approach
      -     inputs        : d and e
         outputs        : \a
         parameters  : q, eml = 10^8, claml = 10^8
         begin
          |     k      0
          |     \a      (n/d /e)
          | laml0      xc,    cond.laml     true
          | while con.daml.ml do
          |     w_k      Diag(exp(0.k) @ e.c)
          |     z_k      \p_k + d/w_k - 1
          |     Find the parameter \lambda+k + maximizing the marginal likelihood \ellm  associated
          |     with the observation vector z, and the weight vector w, using the desired
          |     heuristic, using a convergence threshold of eml.
          |     Form W_k + P_{k+1}  by adding w_k to the diagonal of P_{k+1}
          |     Find the Cholesky factor R of W_k + P_{k+1}'.
          |     Find u such that R^T u = w_{k} \circ z_{k} by forward substitution.
          |     Find 9,k+1 such that R^T 0=w_{k+1} = u by backward substitution.
          |     laml_k+1     \ell_LAML(\lambda+1 | \theta_{k+1}),   cond.laml      laml_{k+1} \geq (1 + \ellm)laml_{k}
          |     k      k + 1
          |     \lambda      \lambda_{k};

!
!  Altered iteration.

```

Algorithm 3: Parameter selection for generalized Whittaker-Henderson smoothing - performance iteration approach

#### Alternated iteration

Finally, Algorithm 4 presents the alternated iteration approach. This hybrid method alternates between updating the smoothing parameter λ on one hand, and and an updated pseudo-response and weight vector on the other hand until convergence of an approximate marginal likelihood.

As in the performance iteration approach, lLAML(λk+1 | θk+1) denotes an approximate LAML, based on the maximizer of an approximate normal marginal likelihood rather than the true penalized likelihood maximizer.

### E Illustrations for the natural parameterization of WH smoothing

This appendix provides an interpretation of Whittaker-Henderson (WH) smoothing in the framework of natural parameterization, based on the eigendecomposition of the penalty matrix.


<!-- p:57 -->


Algorithm 4: Parameter selection for generalized Whittaker-Henderson smoothing - alternated iteration approach

```
-Algorithm 4: Parameter selection for generalized Whitaker-Henderson smoothing -
                       -alternated iteration approach
                       -inputs        : d and e.c
                       -outputs        : \a
                       -parameters: q, elaml = 10-8
                       -begin
                       |   k      0
                       |   \a     (n/d/e.)
                       | laml0      c0,    condj.aml      true
                       | while cond.iaml do
                       |     w_k       Diag(exp(0.k) ) \e c.e)
                       |   z_k       6.0 + d/w_k - 1
                       |   If k = 0, choose an arbitrary value \a for the smoothing parameter(s); otherwise,
                       |     choose the next value \a%+1 to improve the marginal likelihood \a%m using the
                       |     desired heuristic.
                       |   Form W_k + P_{k+1}  by adding w_k to the diagonal of P_{k+1} .
                       |   Find the Cholesky factor R of W_{k + P_{k+1}} .
                       |   Find u such that R^t u = w_{k} \circledast forward substitution.
                       |   Find \theta_{k+1} such that R^e \circledast u by backward substitution.
                       |   laml_{k+1}     \ell^LAML(\lambda+1 | \theta_{k+1}),   condj.aml      laml_{k+1} \geq (1 + \ell \cdot \lambda) \ell.
                       |   k      k + 1
                       | \lambda       \lambda_k
                       |

                       This approach reveals how smoothing acts as a spectral filter thatprogressively alternates
```

This approach reveals how smoothing acts as a spectral filter that progressively attenuates components of the signal associated with rougher variations.

In the one-dimensional case, the smoothing problem is re-expressed in a rotated basis formed by the eigenvectors of the penalty operator, leading to a clear decomposition of the signal into smoother and rougher components. The effect of smoothing is visualized via effective degrees of freedom associated with each component.

The two-dimensional extension leverages Kronecker product identities to generalize the spectral interpretation to tensor-product smoothing penalties. Illustrations are provided to highlight how smoothing parameters affect the influence of each spectral component in both dimensions.

#### One-dimensional case

Building on the natural parameterization introduced by Demmler and Reinsch (1975), the WH estimator can be reformulated as the solution to the following optimization problem:

$$\hat { y } = U \hat { \beta } , \quad \hat { \beta } = \arg \min _ { \beta } \left \{ ( y - U \beta ) ^ { T } W ( y - U \beta ) + \lambda \beta ^ { T } \Sigma \beta \right \} .$$


<!-- p:58 -->


β can be interpreted as a vector of coordinates in the basis of eigenvectors of Pλ, yielding a spectral decomposition of the signal into components with varying degrees of smoothness, as determined by the associated eigenvalues. Figure 12 represents 8 of the eigenvectors associated with q = 2 for a basis of size n = 45. The first q eigenvalues are zero as Dn,q is of rank n − q.

Figure 12: A subset of the eigenvectors for the penalization matrix Dπ,g Dn,q with n = 45 and n,q q = 2.

eigenvector 1

eigenvector 2

eigenvector 3

eigenvector 4

0.3

eigenvalue0


eigenvalue1.22 × 104

eigenvalue 9.26 × 104

0.2

0.1

0.0

-0.1

-0.2

Coefficient

-0.3

eigenvector 5

eigenvector 22

eigenvector 44

eigenvector 45

0.3

eigenvalue3.55x 103

eigenvalue1.58 × 10^{1

eigenvalue1.6 × 101

0.2

0.1

0.0

-0.1

-0.2

-0.3

10

20

30

40

0

10

20

30

40

10

20

30

40

0

10

20

30

40

Observation

By using the fact that U−1 = UT and by linking this expression back to the original smoothing formulation, we obtain the explicit solution:

$$\hat { y } = U ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W y \quad \text {where} \quad S _ { \lambda } = \lambda \Sigma .$$

In order to interpret Equation 18, consider the special case where all weights are equal to 1 and therefore:

$$\hat { y } = U ( U ^ { T } U + \lambda \Sigma ) ^ { - 1 } U ^ { T } y = U ( I _ { n } + \lambda \Sigma ) ^ { - 1 } U ^ { T } y .$$

The transformation from y to  can then be seen as a 3-step process, reading the equation from right to left:

1. Decomposition of the signal y in the basis of eigenvectors through the left multiplication by UT.


<!-- p:59 -->


2. Attenuation of the signal components based on the eigenvalues associated with these components. If we denote s = diag(Σ), then (In + λΣ)−1 = Diag[1/(1 + λs)]. After the left multiplication by (In + λΣ)−1, each component is hence divided by a factor 1 + λs ≥ 1. This coefficient increases linearly with λ, but the rate of increase varies with the magnitude of the corresponding eigenvalue.
3. Recomposition of the attenuated signal in the canonical basis through the left multiplication by U.

When weights are not uniform, the structure becomes more complex since UTWU is no longer a diagonal matrix. However, it is still possible to interpret the effect of smoothing from the diagonal of the matrix F = (UTWU + Sλ)−1UTWU. Indeed:

$$U ^ { T } \hat { y } = U ^ { T } U \hat { \theta } = \hat { \theta } = ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W y = ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W U U ^ { T } y = F U ^ { T } y .$$

Since the vectors UTy and β = UTy represent the coordinates of y and  respectively in the basis of eigenvectors of Dn,qDn,q, F thus acts as a transformation matrix on the spectral coordinates, analogous to the role played by the hat matrix H = U(UTWU + Sλ)−1UTW for the observations. The diagonal values of F may be interpreted as the effective degrees of freedom associated with each eigenvector after smoothing. It can be verified that:

$$t r ( F ) = t r [ ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W U ] = t r [ U ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W ] = t r ( H )$$

which means that the sum of the effective degrees of freedom remains the same whether it is counted per observation or per parameter.

Figure 13 represents the effective degrees of freedom per parameter in the previous illustration of smoothing. The first q eigenvectors are never penalized, so their effective degrees of freedom are always equal to 1, regardless of the smoothing parameter used. The other eigenvectors have strictly decreasing effective degrees of freedom with λ. These degrees of freedom are weights and for small values of λ, this is not always the case.

#### Two-dimensional case

Similar to the one-dimensional case, we can perform the eigendecomposition of the matrices Dnz,qzDnz,qz = UzΣzUT. z Define U = Uz ⊗ Ux and perform the reparametrization β = UTθ ⇔ θ = Uβ. By leveraging the properties of the Kronecker product, we can rewrite the smoothness criterion in a simplified form:

$$\theta ^ { T } P _ { \lambda } \theta = ( U \beta ) ^ { T } P _ { \lambda } ( U \beta ) = \beta ^ { T } ( \lambda _ { x } I _ { n _ { z } } \otimes \Sigma _ { x } + \lambda _ { z } \Sigma _ { z } \otimes I _ { n _ { x } } ) \beta .$$

This leads to an alternative formulation of the optimization problem:


<!-- p:60 -->


Figure 13: Effective degrees of freedom per eigenvector after applying 1D WH smoothing, for different combinations of smoothing parameter.

α □ 10'

α □ 104

α □ 107

1,0

edf : 35.21

edf: 6.71

co

edf: 2.10

Effective degrees of freedom

0,8

0,6

0,4

0,2

0,0

0

10

20

30

40

0

10

20

30

40

0

10

20

30

40

Eigenvector

$$\hat { y } = U \hat { \beta } , \quad \hat { \beta } = \arg \min _ { \beta } \left \{ ( y - U \beta ) ^ { T } W ( y - U \beta ) + \lambda \beta ^ { T } ( \lambda _ { x } I _ { n _ { z } } \otimes \Sigma _ { x } + \lambda _ { z } \Sigma _ { z } \otimes I _ { n _ { x } } ) \beta \right \} .$$

The solution to the smoothing problem, as in the one-dimensional case, is given by:

$$\hat { y } = U ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W y \quad \text {where} \quad S _ { \lambda } = \lambda _ { x } I _ { n _ { z } } \otimes \Sigma _ { x } + \lambda _ { z } \Sigma _ { z } \otimes I _ { n _ { x } } .$$

Figure 14 represents the residual degrees of freedom associated with each parameter after applying the smoothing, in the two-dimensional case, for different combinations of the smoothing parameters. Similar to the one-dimensional case, these degrees of freedom decrease as the smoothing parameters increase and are particularly small for higher eigenvalues. The eigenvectors are sorted in ascending order of eigenvalues for each one-dimensional penalty matrix DT xDnx,qx and Dπz, zDnz,qz· nx,qx nz,qz

### F Derivation of constrained extrapolation in the 2D case

This appendix provides a closed-form expression for the constrained extrapolated estimator, which extends the smoothed surface beyond the observed domain while preserving the values estimated during the initial fit. It also derives the associated variance-covariance matrix, accounting for both propagated uncertainty and additional variability in the extrapolated region.

To obtain an estimator y* that minimizes the extended optimization problem under the consne e  oe o  =  e s e  one e osed by Carballo, Durban, and Lee (2021) and introduce a Lagrange multiplier ω. The associated constrained extended optimization problem is now written as:


<!-- p:61 -->


Figure 14: Residual degrees of freedom per eigenvector after applying 2D WH smoothing, for different combinations of smoothing parameters.

α2 □ 10-1

± 102

\_2 ± 10$

30

25

20

Effective

15-

degrees

of freedom

10

per eigenvector

5

(0.8,1]

edf: 29.6

edf : 9.4

edf: 4.5

30

(0.6,0.8]

Eigenvector (age)

25

(0.4,0.6]

20

(0.2,0.4]

15

(0.1,0.2]

10

(0.05,0.1]

5

edf: 99.8

edf : 36.7

edf : 16.0

(0.02,0.05]

30

(0.01,0.02]

25

(0.001,0.01]

20

15

[0,0.001]

10

5-

edf : 364.7

edf:112.9

edf: 54.9

9

12

15

3

12

15

3

12

15

Eigenvector (time spent in LTC state)

$$( \hat { y } _ { + } ^ { * } , \hat { \omega } ) = \arg \min _ { \theta _ { + } ^ { * } , \omega } \left \{ ( y _ { + } - \theta _ { + } ^ { * } ) ^ { T } W _ { + } ( y _ { + } - \theta _ { + } ^ { * } ) + \theta _ { + } ^ { * T } P _ { + } \theta _ { + } ^ { * } + 2 \omega ^ { T } ( C \theta _ { + } ^ { * } - \hat { y } ) \right \} .$$

Taking the partial derivatives of Equation 19 with respect to θ*+ and ω gives:

$$& \text {taking the partial derivatives of Equation 19 with respect to $\theta^{\dagger}$ and $\omega$ gives:} \\ & \frac { \partial } { \partial \theta ^ { * } _ { + } } \left \{ ( y _ { + } - \theta _ { + } ^ { * } ) ^ { T } W _ { + } ( y _ { + } - \theta _ { + } ^ { * } ) + \theta _ { + } ^ { * } P _ { + } \theta _ { + } ^ { * } + 2 \omega ^ { T } ( C \theta _ { + } ^ { * } - \hat { y } ) \right \} = - 2 W _ { + } ( y _ { + } - \theta _ { + } ^ { * } ) + 2 P _ { + } \theta _ { + } ^ { * } + 2 \omega ^ { T } C \\ & \frac { \partial } { \partial \omega } \left \{ ( y _ { + } - \theta _ { + } ^ { * } ) ^ { T } W _ { + } ( y _ { + } - \theta _ { + } ^ { * } ) + \theta _ { + } ^ { * } P _ { + } \theta _ { + } ^ { * } + 2 \omega ^ { T } ( C \theta _ { + } ^ { * } - \hat { y } ) \right \} = 2 ( C \theta _ { + } ^ { * } - \hat { y } ) \\ & \text {Setting these derivatives to zero yields the linear system:}$$

Setting these derivatives to zero yields the linear system:

$$\begin{bmatrix} W _ { + } + P _ { + } & C ^ { T } \\ C & 0 \end{bmatrix} \begin{bmatrix} \hat { y } _ { + } ^ { * } \\ \hat { \omega } \end{bmatrix} = \begin{bmatrix} W _ { + } y _ { + } \\ \hat { y } \end{bmatrix}$$


<!-- p:62 -->


The solution for *+ can be derived using formulas for the inversion of a symmetric matrix partitioned with 2 × 2 blocks, setting V+ = (W+ + P+)−1:

$$\hat { y } _ { + } ^ { * } = V _ { + } \left \{ I - C ^ { T } [ C V _ { + } C ^ { T } ] ^ { - 1 } C V _ { + } \right \} W _ { + } y _ { + } + V _ { + } C ^ { T } [ C V _ { + } C ^ { T } ] ^ { - 1 } \hat { y } .$$

Since W+ = CTWC, the first term is actually zero, and this expression simplifies to:

$$\hat { y } _ { + } ^ { * } = V _ { + } C ^ { T } [ C V _ { + } C ^ { T } ] ^ { - 1 } \hat { y } = V _ { + } C ^ { T } ( V _ { + } ^ { 1 1 } ) ^ { - 1 } \hat { y } = Q ^ { T } \left [ _ { - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } } ^ { I } \right ] \hat { y }$$

which is a linear transformation of .

I Defining A*+ = QT −(P22)−1P21 , a variance-covariance of y* | θ+ based on this expression

is given by:

$$A _ { + } ^ { * } V A _ { + } ^ { * T } = Q ^ { T } \begin{bmatrix} V & - V P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \\ - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V & ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \end{bmatrix} Q .$$

Equation 20 is very similar to the equivalent formulation in the one-dimensional case with however two main differences. First, every occurrence of V11 is replaced by V. This is consistent with the constraint that the coefficients over the initial domain are held fixed at their estimated values. Second, as the solution to the constrained extended optimization problem of Equation 19 was expressed as a linear transformation of , Equation 20 is missing the innovation error term (P22)-1 associated with the prior on the extrapolated coefficients. Not including this term would be tantamount to considering that θ+ has some degree of variability in the region of the initial data but is perfectly smooth beyond this range. Adding this innovation error, we obtain the following variance-covariance matrix for the constrained optimization problem:

$$V _ { + } ^ { * } = Q ^ { T } \left [ _ { - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V } \left ( P _ { + } ^ { 2 2 } \right ) ^ { - 1 } P _ { + } ^ { 2 1 } V P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } + ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \right ] Q .$$

which still verifies

$$V _ { + } ^ { * } W _ { + } y _ { + } = V _ { + } ^ { * } C W y = Q ^ { T } \left [ \begin{matrix} I \\ - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } \end{matrix} \right ] V W y = \hat { y } _ { + } ^ { * } .$$

### G Choosing the order of the difference matrices

This appendix investigates how the choice of the difference order q in WH smoothing affects model performance. It provides empirical guidance for selecting q based on AIC values computed across simulation replicates, and confirms that second-order differences offer a good balance between fit quality and extrapolation stability.


<!-- p:63 -->


In Whittaker-Henderson (WH) smoothing, the order of the difference matrix used in the penalization term, typically denoted q (or (qx, qz) in the two-dimensional case), governs the smoothness prior imposed on the underlying signal. While Whittaker originally proposed using third-order differences, second-order differences have since become the standard choice. This aligns with the common statistical definition of smoothness as the integrated squared second derivative, a justification also used for cubic spline smoothing (Reinsch 1967) and P-splines (Eilers and Marx 1996).

From a Bayesian perspective, penalizing second-order differences is equivalent to assuming that the log-transformed target function follows a locally affine (i.e., linear) trajectory. For mortality data, this implies a prior belief in exponential growth of the mortality rate—a widely accepted assumption consistent with the Gompertz model. For other biometric risks, such as disability or long-term care, this prior is also appropriate for the age dimension if included.

Penalizations of order q &gt; 3 are harder to justify in actuarial practice. They may produce undesirable artefacts in the extrapolated regions, where the extrapolation from the fit tends to follow a polynomial of degree q − 1.

It is possible to treat the choice of q as a model selection problem. REML is not suitable in this context, as it assumes an equal fixed effect structure, however standard criteria such as AIC and GCV can be used instead. Relying on AIC and the 100 replicate datasets described in Section 6, we found that:

- For the annuity datasets, Figure 15 shows that second-order differences (q = 2) provides the best results.
- For the duration dimension in LTC datasets, Figure 16 shows that, regarding the age dimension, second-order differences (q = 2) is still the best option while for the duration dimension, AIC improves significantly when moving from first- to second-order penalization, and then slightly improves further for higher orders. This suggests that higher-order prior may be relevant for the duration dimension in this particular dataset.

Still, the gains from increasing the order beyond 2 are limited and may not outweigh the risks of erratic extrapolation. Therefore, second-order differences remain a pragmatic and robust default.


<!-- p:64 -->


Figure 15: AIC values for different penalization orders in WH smoothing, based on 100 replicates of the annuity portfolio (100,000 individuals).

80

70

AIC

60

50

2

Difference order

Figure 16: AIC values for combinations of difference matrix orders along age and duration in WH smoothing, based on 100 replicates of the LTC portfolio (100,000 individuals).

qz = 1

qz = 2

900

800

00L

600

500

AIC

qz = 3

qz = 4

900

800

700

600

500

2

3

2

3

4

Difference order qx
