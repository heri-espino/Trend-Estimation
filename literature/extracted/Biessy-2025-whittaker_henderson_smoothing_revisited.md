---
id: "Biessy-2025-whittaker_henderson_smoothing_revisited"
source_pdf: "../pdf/Biessy-2025-whittaker_henderson_smoothing_revisited.pdf"
source_filename: "Biessy-2025-whittaker_henderson_smoothing_revisited.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/Biessy-2025-whittaker_henderson_smoothing_revisited.references.md"
---

<!-- p:1 -->

####### RESEARCHARTICLE

## Whittaker-Henderson smoothing revisited: A modern statistical framework for practical use

Guillaume Biessy, PhD1.21D

1LinkPact, Paris, 75015, France

2Sorbonne Université, CNRS, Laboratoire de Probabilités, Statistique et Modélisation, LPSM, Paris, 75005, France Email: guillaume.biessy78@gmail.com

Received: 17 October 2024; Revised: 23 July 2025; Accepted: 24 July 2025; First published online: 3 September 2025

Kk a   s l m  m  m s :es approach; marginal likelihood; LAML; extrapolation

###### Abstract

Introduced over a century ago, Whittaker-Henderson smoothing remains widely used by actuaries in constructing one-dimensional and two-dimensional experience tables for mortality, disability, and other life insurance risks. In this paper, we reinterpret this smoothing technique within a modern statistical framework and address six practically relevant questions about its use. First, we adopt a Bayesian perspective on this method to construct credible intervals. Second, in the context of survival analysis, we clarify how to choose the observation and weight vectors by linking the smoothing technique to a maximum likelihood estimator. Third, we improve accuracy by relaxing the method's reliance on an implicit normal approximation. Fourth, we select the smoothing parameters by maximizing a marginal likelihood function. Fifth, we improve computational efficiency when dealing with numerous observation points and consequently parameters. Finally, we develop an extrapolation procedure that ensures consistency between estimated and predicted values through constraints.

## Notations

In this paper, vectors are denoted in boldface and matrix names in uppercase letters. If y is a vector and A is a matrix, Var(y) denotes the variance-covariance matrix associated with y, diag(A) represents the diagonal of matrix A, and Diag(y) is the diagonal matrix such that diag(Diag(y)) = y. The sum of the diagonal elements of A is denoted as tr(A) and its transpose as AT. In the case where A is invertible, A−1 denotes its inverse and |A| denotes the product of the eigenvalues of A. For a non-invertible matrix A, A− refers to the Moore-Penrose pseudo-inverse of A, and |A|+ denotes the product of the non-zero eigenvalues of A. By writing the eigendecomposition as A = UΣVT, where U and V are orthogonal matrices and Σ is a diagonal matrix containing the eigenvalues of A, and by denoting Σ- as the matrix obtained by replacing the non-zero eigenvalues in Σ with their inverses leaving the zero eigenvalues unchanged, the pseudo-inverse is given by A− = VΣ- UT. The Kronecker product of two matrices A and B is denoted as A ⊗ B, and their Hadamard (element-wise) product is denoted as A  B. [x] denotes the greatest integer less than or equal to x ∈ R. Finally, the symbol α denotes proportionality between the expressions on both sides.

## 1. Introduction

Whittaker-Henderson (WH) smoothing is a graduation method designed to mitigate the effects of sampling fluctuations in a vector of evenly spaced discrete observations. Although this method was originally proposed by Bohlmann (1899), it is named after Whittaker (1923), who applied it to graduate mortality tables, and Henderson (1924), who popularized it among actuaries in the United States. The method

© The Author(s), 2025. Published by Cambridge University Press on behalf of The International Actuarial Association. This is an Open Access article, distributed under the terms of the Creative Commons Attribution licence (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted re-use, distribution and reproduction, provided the original article is properly cited.

IAA

AAI

International Actuarial Association

Association Actuarielle Internationale


<!-- p:2 -->


## 2 Guillaume Biessy

was later extended to two dimensions by Knorr (1984). WH smoothing may be used to build experience tables for a broad spectrum of life insurance risks, such as mortality, disability, long-term care, lapse, mortgage default, and unemployment. We begin with a brief overview of the method before outlining the structure and main contributions of the paper.

### 1.1. A brief reminder of WH smoothing mathematical formulation

The one-dimensional case

Let y be a vector of observations and w a vector of positive weights, both of size n. The estimator associated with WH smoothing is given by

$$\hat { y } = \arg \min _ { \theta } \{ F ( y , w , \theta ) + R _ { \lambda , q } ( \theta ) \}$$

where:

- n · F(y, w, θ) = ∑w(yi — θ)2 represents a fidelity criterion with respect to the observations, i=1
- n−q · Rλ,q(θ) = λ∑(∆aθ)2 represents a smoothness criterion. i=1

In the latter expression, λ ≥ 0 is a smoothing parameter and ∆a denotes the forward difference operator of order q, such that for any i ∈ {1, . . . , n − q}:

$$( \Delta ^ { q } \theta ) _ { i } = \sum _ { k = 0 } ^ { q } \left ( \begin{matrix} q \\ k \end{matrix} \right ) ( - 1 ) ^ { q - k } \theta _ { i + k } . \\$$

Define W = Diag(w), the diagonal matrix of weights, and Dn,q as the order q difference matrix of dimensions (n − q) × n, such that (Dn,qθ) = (∆aθ)i for all i ∈ [1, n − q]. The first- and second-order difference matrices are given by

$$\text {distance matrices giving by} \\ D _ { n , 1 } = \begin{bmatrix} - 1 & 1 & 0 & \dots & 0 \\ 0 & - 1 & 1 & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & 0 \\ 0 & \dots & 0 & - 1 & 1 \end{bmatrix} \quad \text {and} \ D _ { n , 2 } = \begin{bmatrix} 1 & - 2 & 1 & 0 & \dots & 0 \\ 0 & 1 & - 2 & 1 & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & \ddots & 0 \\ 0 & \dots & 0 & 1 & - 2 & 1 \end{bmatrix} .$$

while higher-order difference matrices follow the recursive formula Dn,q = D-1,q-1Dn,1. The fidelity and smoothness criteria can be rewritten with matrix notations as

$$F ( y , w , \theta ) = ( y - \theta ) ^ { T } W ( y - \theta ) \quad \text {and} \quad R _ { \lambda , q } ( \theta ) = \lambda \theta ^ { T } D _ { n , q } ^ { T } D _ { n , q } \theta \\$$

and the WH smoothing estimator thus becomes

$$\hat { y } = \arg \min _ { \theta } \left \{ ( y - \theta ) ^ { r } W ( y - \theta ) + \theta ^ { T } P _ { \lambda } \theta \right \}$$

where Pλ = λDna Dn,q n,q

#### The two-dimensional case

In the two-dimensional case, consider a matrix Y of observations and a matrix Ω of non-negative weights, both of dimensions nx × nz. The WH smoothing estimator solves:

$$\widehat { Y } = \arg \min _ { \Theta } \{ F ( Y , \Omega , \Theta ) + R _ { \lambda , q } ( \Theta ) \}$$

where:

- F(Y, Ω, Θ) = Σi=1 Σj=1 Ωij(Yij − Θi,j)2 represents a fidelity criterion with respect to the observations,


<!-- p:3 -->


- Rx,q(O) = λx ∑j=1 ∑i=1 (∆%Θ.j) + λz ∑i=1 ∑j=1 (∆%Oi ) isa moothness crtrion wihit λ = (λx, λz).

This latter criterion adds row-wise and column-wise regularization criteria to Θ, with respective orders qx and qz, weighted by non-negative smoothing parameters λx and λz. In matrix notation, let y = vec(Y), w = vec(Ω), and θ = vec(Θ) as the vectors obtained by stacking the columns of the matrices Y, Ω, and Θ, respectively. Additionally, denote W = Diag(w) and n = nx × nz. The fidelity and smoothness criteria become

$$F ( y , w , \theta ) = ( y - \theta ) ^ { T } W ( y - \theta ) \\ R _ { \lambda , q } ( \theta ) = \theta ^ { T } ( \lambda _ { x } I _ { n _ { z } , q _ { x } } D _ { n _ { z } , q _ { x } } + \lambda _ { z } D _ { n _ { z } , q _ { z } } ^ { T } D _ { n _ { z } , q _ { z } } \otimes I _ { n _ { x } } ) \theta \\ \text {cited estimator also takes the form of Equation } 1 , 2 \text { except in this case}$$

and the associated estimator also takes the form of Equation 1.2 except in this case

$$P _ { \lambda } = \lambda _ { x } I _ { n _ { z } } \otimes D _ { n _ { x } , q _ { x } } ^ { T } D _ { p _ { x } }$$

Extension to higher dimensions is straightforward and not discussed here.

#### An explicit solution

If W + Pλ is invertible, Equation (1.2) admits the closed-form solution:

$$\hat { y } = ( W + P _ { \lambda } ) ^ { - 1 } W y .$$

Indeed, as a minimum,  satisfies:

$$0 = \frac { \partial } { \partial \theta } \Big | _ { \hat { y } } \left \{ ( y - \theta ) ^ { T } W ( y - \theta ) + \theta ^ { T } P _ { \lambda } \theta \right \} = - 2 W ( y - \hat { y } ) + 2 P _ { \lambda } \hat { y } .$$

It follows that (W + Pλ) = Wy, proving Equation (1.3). If λ ≠ 0, W + Pλ is invertible as long as w has q non-zero elements in the one-dimensional case and Ω has at least qx × qz non-zero elements spread across qx different rows and qz different columns in the two-dimensional case. These conditions are always met in real datasets.

### 1.2. Structure of the paper

Introduced a century ago, WH smoothing remains widely used by actuaries, particularly in France and North America (Canadian Institute of Actuaries, 2017; Society of Actuaries, 2018). Other nonparametric smoothing methods have since emerged, notably spline-based techniques (Reinsch, 1967), which gained even greater popularity with P-splines (Eilers and Marx, 1996). A broader overview of alternative smoothers is available in Wood (2017, chap. 5).

For evenly spaced discrete observations, WH smoothing may be considered a particular case of Psplines with degree-zero splines and identity model matrix. Its appeal lies in its simplicity: no selection of knots, parameters equal to fitted values, and shape controlled solely via penalization. However, it involves more parameters than low-rank smoothers, making it more computationally intensive.

Originally proposed as an empirical alternative to polynomial regression and weighted averages, WH smoothing offered key benefits noted by Whittaker (1923): first q moment preservation, adjustable smoothing parameters, and robustness at boundaries. While smoothing theory has evolved – particularly via generalized additive models (Hastie and Tibshirani, 1990), use of WH smoothing by actuaries remains largely unchanged. This paper reinterprets WH within modern statistical theory to bridge that gap and address six practical questions, each discussed in a dedicated section.

#### How to measure uncertainty in smoothing results?

We propose a method to quantify the uncertainty in WH smoothing based on data volume, a topic that has received little attention in the literature. In a frequentist framework, the WH estimator is biased, which


<!-- p:4 -->


###### 4 Guillaume Biessy

complicates the construction of valid confidence intervals for finite samples. However, under certain conditions, WH smoothing can be viewed as a Bayesian model, enabling the derivation of credible intstt  a (l   s il a u usa   ton for the method and formally revisited decades later by Taylor (1992). In this section, we build on that equivalence to derive credible intervals for WH smoothing.

#### Which observation and weight vectors to use?

For the Bayesian interpretation of WH smoothing discussed in Section 2 to hold, it must be applied to a vector y of independent, normally distributed observations with known variances. The weight vector w should then contain the inverse variances (up to a constant), as noted by Taylor (1992) and Verrall (1993). We show that, under piecewise constant transition intensities in duration models, the maximum likelihood estimator of crude rates produces vectors (y, w) that asymptotically meet these conditions. This, combined with the results from the previous section, offers a statistical foundation for the use of WH smoothing in constructing experience tables for life insurance risks.

#### How to improve the accuracy of smoothing with limited data volume?

The standard approach applies WH smoothing to crude rate estimates, assuming they are asymptotically normal. However, this assumption often breaks down in practice when data are limited, making the method unreliable in such cases. Following Verrall (1993), we propose a generalization of WH smoothing that replaces the two-step procedure with the direct maximization of a penalized log-likelihood. Instead of smoothing pre-estimated rates, this method works directly with aggregated event and exposure counts. The estimation is performed iteratively using the PIRLS algorithm. We evaluate both methods on simulated datasets reflecting typical life insurance portfolios. Results show that, in smaller samples, the normal approximation in the traditional method introduces notable bias. This supports the use of the generalized approach – based on penalized log-likelihood – as a more robust alternative when data are limited.

#### How to select the smoothing parameters?

We now turn to the crucial choice of the smoothing parameter λ, which has long been left to actuarial judgement. Giesecke and Center (1981) suggested choosing λ so that the variance of the smoothed results matches the average variance of a Chi-square statistic, but uses n — q as degrees of freedom, thus ignoring the reduction in effective model dimension due to penalization. Brooks et al. (1988) minimized the global cross-validation criterion introduced by Wahba (1980), though this can result in severe undersmoothing as noted by Wood (2011).

We instead propose to select λ by maximizing a marginal likelihood function, a method first introduced by Patterson and Thompson (1971) and later applied to smoothing parameter selection by Anderssen and Bloomfield (1974). This approach is consistent with the Bayesian framework discussed earlier and performs well in small samples, as shown by Reiss and Todd Ogden (2009). This marginal likelihood function has a closed-form expression and can be maximized numerically. For the proposed generalization of WH smoothing, the marginal likelihood is no longer available in closed form. Instead, we rely on the Laplace approximation of the marginal likelihood (LAML), which can be maximized numerically. As both solving likelihood equations and selecting the optimal smoothing parameter are iterative processes, we explore different ways of nesting these iterations. We compare three nesting strategies combined with three numerical optimization algorithms for maximizing the marginal likelihood or LAML. Simulation results show that all strategies have near-optimal accuracy, with the fastest performance achieved using the outer iteration strategy combined with the Newton algorithm


<!-- p:5 -->


###### How to improve smoothing computational efficiency?

When the number of observations – and thus parameters – is large, the computational cost of WH smoothing becomes a major challenge. This is particularly relevant in actuarial contexts, such as smoothing two-dimensional tables for disability or long-term care modelling. Beyond actuarial applications, WH smoothing is also widely used in economics for long time series, where it is known as the HodrickPrescott filter (Hodrick and Prescott, 1997). Although fast algorithms have been developed to exploit the structure of the penalization matrix (e.g., Weinert, 2007; Cornea-Madeira, 2017) they are typically limited to the one-dimensional case and cannot be directly extended to two dimensions.

After briefly outlining the main computational steps of (generalized) WH smoothing-including smoothing parameter selection via marginal likelihood or LAML-and their leading-order costs, we introduce two complementary strategies to reduce the computational burden:

1. Banded matrix exploitation: WH smoothing involves model and penalization matrices with banded structure. Taking advantage of this structure greatly accelerates key computations.
2. Reduced-rank basis via natural parametrization: Building on the work of Demmler and Reinsch (1975), we apply an eigendecomposition to the one-dimensional penalization matrices and drop o ss ss   s   ss    sowo dimensions, we further improve efficiency using the generalized linear array model (GLAM) framework (Currie et al., 2006) which leverages the rectangular shape of the data.

In the two-dimensional case, we compare these strategies with a cubic P-spline alternative using simulated datasets. Results show that the banded implementation reduces computation time by up to a factor of 25. The reduced-rank approach brings further gains – up to a factor of 250 – at the cost of a slight reduction in accuracy. Its performance is comparable to P-spline smoothing with a cubic basis of similar size.

#### How to extrapolate smoothing results?

We conclude by addressing how to extrapolate smoothing results. Semi-parametric models like WH and P-splines can extrapolate beyond the observed data – similar to parametric models – but this feature is often overlooked in actuarial practice. The existing literature is limited and mostly focused on mortality forecasting.

Currie et al. (2004) uses P-splines to fit and forecast mortality rates by treating the extrapolated positions as zero-weight observations (see also Delwarde et al., 2007; Currie, 2013). While this works well in one dimension, Carballo et al. (2021) showed that it distorts the fit in two dimensions. To fix this, they proposed adding constraints to preserve the values that would result from fitting the observed data alone.

However, their approach to confidence intervals overlooks potential innovation error beyond the observed data, effectively treating the extrapolated process as perfectly smooth. In contrast, we propose an approach that derives credible intervals for extrapolated values, accounting for the underlying variability beyond the observed data range.

## 2. How to measure uncertainty in smoothing results?

The explicit solution given by Equation (1.3) indicates that E() = (W + Pλ)−1WE(y) ≠ E(y) when λ ≠ 0. This implies that penalization introduces a smoothing bias, which prevents the construction of confidence intervals for finite samples centred on E(y). Therefore, in this section, we turn to a Bayesian framework where smoothing can be interpreted more naturally.

### 2.1. Maximum a posteriori estimate

Suppose that y | θ ∼ N(θ, σ2W−) and θ ∼ N(0, σ2P−) for some σ &gt; 0. The Bayes formula allows us to express the posterior likelihood f(θ | y) associated with these choices in the following form:


<!-- p:6 -->


$$f ( \theta \, | \, y ) \otimes f ( y \, | \, \theta ) f ( \theta ) \otimes \exp \left ( \frac { 1 } { 2 \sigma ^ { 2 } } \left [ ( y - \theta ) ^ { T } W ( y - \theta ) + \theta ^ { T } P _ { \lambda } \theta \right ] \right ) .$$

Hence the mode of the posterior distribution, ê = argmax[f(θ | y)], also known as the maximum a posteriori (MAP) estimate, coincides with the solution  from Equation (1.2), whose explicit form is given by Equation (1.3).

### 2.2. Posterior distribution of θ | y

A second-order Taylor expansion of the log-posterior likelihood around  = ê gives us:

$$\ln f ( \theta \, | \, y ) = \ln f ( \hat { \theta } \, | \, y ) + \frac { \partial \, \ln f ( \theta \, | \, y ) } { \partial \theta } \Big | _ { \theta = \hat { \theta } } ^ { T } ( \theta - \hat { \theta } ) + \frac { 1 } { 2 } ( \theta - \hat { \theta } ) ^ { r } \, \frac { \partial ^ { 2 } \ln f ( \theta \, | \, y ) } { \partial \theta \partial \theta ^ { T } } \Big | _ { \theta _ { \theta } = \hat { \theta } } ( \theta - \hat { \theta } ) \quad ( 2 . 1 )$$

$$\ln f ( \theta | y ) = \ln f ( \theta | y ) + \frac { \partial \theta } { \partial \theta } \Big | _ { \theta = \hat { \theta } } \Big | _ { \theta = 0 } ( \theta - \theta ) + \frac { \partial ( \theta - \theta ) ^ { \prime } } { 2 } \Big | _ { \theta = \hat { \theta } } ( \theta - \theta ) \Big | _ { \theta = \hat { \theta } } \\ \text {where} \quad \frac { \partial \ln f ( \theta | y ) } { \partial \theta } \Big | _ { \theta = \hat { \theta } } = 0 \quad \text {and} \quad \frac { \partial ^ { 2 } \ln f ( \theta | y ) } { \partial \theta \partial \theta ^ { \prime } } \Big | _ { \theta = \hat { \theta } } = - \frac { 1 } { \sigma ^ { 2 } } ( W + P _ { \lambda } ) . \\ \text {As this last derivative no longer depends on $\theta$, higher-order derivatives are all zero. The Taylor expansion}$$

As this last derivative no longer depends on θ, higher-order derivatives are all zero. The Taylor expansion allows for an exact computation of ln f(θ | y). Substituting the result back into Equation (2.1) yields:

$$f ( \theta | y ) \in & \exp \left [ \ln f ( \hat { \theta } | y ) - \frac { 1 } { 2 \sigma ^ { 2 } } ( \theta - \hat { \theta } ) ^ { T } ( W + P _ { \lambda } ) ( \theta - \hat { \theta } ) \right ] \\ & \quad \times \exp \left [ - \frac { 1 } { 2 \sigma ^ { 2 } } ( \theta - \hat { \theta } ) ^ { T } ( W + P _ { \lambda } ) ( \theta - \hat { \theta } ) \right ]$$

which can immediately be recognized as the density of the N(, σ2(W + Pλ)−1) distribution.

### 2.3. Consequence for the WH smoothing

The prior θ ~ N(0, σ2P−) provides a Bayesian interpretation of the smoothness penalty, expressing an (improper) prior belief about the structure of y.

This Bayesian framework and the resulting credible intervals rely on the assumption that y |θ~ N(θ, σ2W−), meaning that the components of y are independent with known variances (up to a constant σ2). The weight vector w must then be proportional to the inverse variances, not chosen empirically. If σ2 is known, 100(1 — α)% credible intervals take the form:

$$\mathbb { E } ( y ) \, | \, y \in \left [ \hat { y } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \sigma ^ { 2 } \text {diag} \left \{ ( W + P _ { \lambda } ) ^ { - 1 } \right \} } \right ]$$

where  = (W + Pλ)−1Wy and Φ is the cumulative distribution function for the standard normal distribution. According to Marra and Wood (2012), such intervals have good Frequentist coverage.

If σ2 is unknown, it can be estimated as

$$\hat { \sigma } ^ { 2 } = \frac { ( y - \hat { y } ) ^ { T } W ( y - \hat { y } ) } { n - \text {tr} ( H ) } \quad \text {where} \quad H = ( W + P _ { \lambda } ) ^ { - 1 } W .$$

In that case, σ2 is replaced by ô2 and the normal distribution in Equation (2.2) by the Student t - distribution with n — tr(H) degrees of freedom.

## 3. Which observation and weight vectors to use?

Section 2 highlighted that WH smoothing may be interpreted in a robust statistical framework when applied to a vector y of independent, normally distributed observations with known variances, and a weight vector w proportional to the inverses of those variances. In this section, we propose, within the framework of duration models used for constructing experience tables for life insurance risks, vectors y and w that satisfy these conditions.


<!-- p:7 -->


### 3.1. Survival analysis framework

We consider a longitudinal follow-up of m individuals, subject to left truncation and non-informative right censoring, and aim to estimate a distribution governed by a continuous explanatory variable x (e.g. age). Let μ denote the hazard function, also known as the force of mortality in the study of the death risk. Under standard survival analysis assumptions, the log-likelihood takes the following continuous-time form:

$$\ell ( \theta ) = \sum _ { i = 1 } ^ { m } \left [ \delta _ { i } \ln \mu ( x _ { i } + t _ { i } , \theta ) - \sum _ { u = 0 } ^ { t _ { i } } \mu ( x _ { i } + u , \theta ) d u \right ] . \\$$

Here x is the age at the start of observation, t is the follow-up duration for individual i and δ is an event indicator: 1 if the event is observed and 0 if censored.

Although model estimation can be based on direct maximization of Equation (3.1), this approach scales poorly with large m and generally requires numerical integration – except in simple parametric cases. We instead adopt a discrete approximation by assuming the hazard rate is piecewise constant over one-year intervals:

$$\mu ( x + \epsilon ) = \mu ( x ) \quad \text {for all} \quad x \in \mathbb { N } , \epsilon \in [ 0 , 1 ] .$$

Under this assumption, the log-likelihood simplifies to a sum over discrete ages:

$$\ell ( \theta ) = \sum _ { x = x _ { \min } } ^ { \max } \ln \mu ( x , \theta ) d ( x ) - \mu ( x , \theta ) e _ { c } ( x ) . \\$$

Here d(x) is the number of observed events at age x and e(x) is the central exposure to risk, that is, the total duration individuals are observed at age x.

This discretization, first introduced by Hoem (1971), is widely used in actuarial science. Its advantages are underlined for example in Gschlössl et al. (2011). It extends naturally to the two-dimensional case by assuming μ(x + ∈, z + ξ) = μ(x, z) and summing over (x, z) pairs.

Details on the derivation of Equations (3.1) and (3.2), along with the computation of central exposures and event counts, are provided in Section A of the Supplementary Materials.

### 3.2. Likelihood equations

Assuming one parameter per observation and using the exponential link μ(θ) = exp(θ), we recover the crude rates estimator, which models each age (or age pair) independently. The exponential link ensures positive hazard rates. The log-likelihood, in both one- and two-dimensional cases, takes the vectorized form:

$$\ell ( \theta ) = \theta ^ { T } d - \exp ( \theta ) ^ { T } e _ { c }$$

where d and ec are the vectors of observed deaths and central exposures.

The derivatives of this likelihood are

$$\frac { \partial \ell } { \partial \theta } = \mathbf d - \exp ( \theta ) \odot \mathbf e _ { c } \quad \text {and} \quad \frac { \partial ^ { 2 } \ell } { \partial \theta \partial \theta ^ { \prime } } = - \text {Diag} ( \exp ( \theta ) \odot \mathbf e _ { c } ) .$$

These equations correspond to those of a Poisson GLM (Nelder and Wedderburn, 1972) with mean μ(θ)  e, although derived under different assumptions.

The model admits the closed-form solution ê = ln (d/ec). Under standard regularity conditions, the maximum likelihood estimator satisfies ê ~ N(θ, W−1), with W3 = Diag(d).


<!-- p:8 -->


Notably, this asymptotic approximation depends on the number of individuals m and not the dimension n of the aggregated vectors.

### 3.3. Consequence for the WH smoothing

We conclude that, under the duration model framework and using crude rates, the log-estimate ln (d/ec) is asymptotically normal:

$$\ln \left ( \mathbf d / \mathbf e _ { c } \right ) \sim \mathcal { N } ( \ln \mu , W ^ { - 1 } ) \quad \text {with} \quad W = D i a g ( \mathbf d ) .$$

This justifies applying WH smoothing to the observation vector y = ln (d/ec) with weight vector w = d. Using results from Section 2, and σ2 = 1, the credible intervals for ln μ are

$$\ln \mu \, | \, d , e _ { \epsilon } \in \left [ \hat { \theta } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \text {diag} \left \{ ( \text {Diag} ( \text {d} ) + P _ { \lambda } ) ^ { - 1 } \right \} } \right ]$$

with ê = (W + Pλ)−1W(ln d − ln ec). Credible intervals for μ itself are then obtained by exponentiating the bounds.

## 4. How to improve the accuracy of smoothing with limited data volume?

### 4.1. Generalized Whittaker-Henderson smoothing

The approach described in Section 3.2 assumes that the crude rates estimator is asymptotically normal, justifying the application of WH smoothing to its logarithm. However, with limited data, this approximation may introduce significant bias. We therefore propose an alternative based directly on the exact likelihood in Equation (3.3). Applying the Bayesian framework from Section 2 and assuming θ ~ N(0, P−), Bayes' theorem gives

$$f ( \theta \, | \, d , e _ { c } ) \, \infty f ( d , e _ { c } \, | \, \theta ) f ( \theta ) \, \infty \exp \left [ \ell ( \theta ) - \frac { 1 } { 2 } \theta ^ { T } P _ { \lambda } \theta \right ]$$

We define the penalized log-likelihood as lp(θ) = l(θ) − θ Pλθ/2. The maximum a posteriori estimate is the maximizer of lp.

Using a second-order Taylor expansion of the posterior log-likelihood around ê leads to the Laplace approximation:

$$f ( \theta \, | \, \mathbf d , \mathbf e _ { \mathbf c } ) \approx \mathcal { N } ( \hat { \theta } , ( W _ { \hat { \theta } } + P _ { \lambda } ) ^ { - 1 } )$$

where W = Diag(exp()  ec). Unlike the normal case studied in Section 2, the higher-order derivatives of the posterior log-likelihood are not zero, and Equation (4.1) only provides an approximation of the posterior log-likelihood, which yields asymptotic credible intervals:

$$\ln \mu \left | \, d , e _ { c } \in \left [ \hat { \theta } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \text {diag} \left \{ ( W _ { \hat { \theta } } + P _ { \lambda } ) ^ { - 1 } \right \} } \right ] .$$

Unlike the closed-form estimator in Equation (3.4), no analytical solution for ê exists here. We solve numerically using Newton's algorithm, which iteratively updates:

$$\theta _ { k + 1 } = \theta _ { k } + ( W _ { k } + P _ { \lambda } ) ^ { - 1 } ( \text {d} - \exp ( \theta _ { k } ) \odot \mathfrak { e } _ { \mathfrak { c } } - P _ { \lambda } \theta _ { k } ) ]$$

with Wk = Diag(exp(θk)  ec). The update can be rewritten as

$$\theta _ { k + 1 } = ( W _ { k } + P _ { \lambda } ) ^ { - 1 } W _ { k } z _ { k } \quad \text {where} \quad z _ { k } = \theta _ { k } + W _ { k } ^ { - 1 } [ \mathbf d - \exp ( \theta _ { k } ) \odot \mathbf e _ { \mathbf c } ] .$$

Initializing with the crude rates estimator θ0 = ln (d/ec) implies W0 = Diag(d) and z0 = ln (d/ec), so the first iteration recovers the classical WH smoothing result.


<!-- p:9 -->


Table 1. Key figures associated with the 6 simulated datasets.

| Portolio type   | Dimensions   |   Head count |   Exposure count |   Death count |
|-----------------|--------------|--------------|------------------|---------------|
| Annuity         | 45           |       20,000 |          136,524 |         1,722 |
| Annuity         | 45           |      100,000 |          679,728 |         8,452 |
| Annuity         | 45           |      500,000 |        3,405,892 |        42,499 |
| LTC             | 30 × 15      |       20,000 |            8,115 |         1,888 |
| LTC             | 30 × 15      |      100,000 |           40,004 |         9,281 |
| LTC             | 30 15        |      500,000 |          202,666 |        47,358 |

Subsequent iterations refine the observation and weight vectors. This process can thus be interpreted as an iterative generalization of WH smoothing, akin to how generalized linear models extend linear models.

We refer to this method as generalized WH smoothing. The iterative estimation algorithm described above corresponds to the penalized iteratively reweighted least squares (PIRLS) algorithm, widely used for fitting generalized additive models.

This framework naturally extends to other exponential family distributions, such as the binomial case suggested in Verrall (1993), by adapting the likelihood, link function, weight matrix, and working vector. However, we advocate for the Poisson-like likelihood of Equation (3.3), which offers several advantages: it generalizes to competing risks, supports multiplicative covariate effects via the log link and allows the use of an external reference table as a multiplicative offset.

### 4.2. Impact of the normal approximation in the original smoothing

As discussed in Section 3, classical WH smoothing can be viewed as an approximation to a penalized likelihood maximization, relying on a crude rate estimator assumed to be asymptotically normal. To assess the practical consequences of this approximation, we conduct an empirical comparison based on six simulated datasets reflecting the typical structure and volume of real insurance portfolios:

- The first three datasets simulate annuity portfolios with 20,000, 100,000, and 500,000 policyholders. The sole covariate is age, ranging from 50 to 95.
- The next three mimic long-term care (LTC) portfolios of the same sizes. Modelling of LTC typically relies on the illness-death model (Fix and Neyman, 1951; Clifford, 1977). To get a two-dimensional illustration we focus on the transition between the disabled and dead states (the two other transitions would provide additional one-dimensional examples). Two covariates are used: age (70–100) and duration in LTC (0–15 years).

Each dataset consists of individual-level longitudinal data, from which we derive event counts d and exposures ec, aggregated by age x (for annuities) of by (x, z) pairs (for LTC). All datasets within each group share the same underlying structure and differ only in size. Key dataset statistics are provided in Table 1 and additional details about how those datasets were generated are provided in Section B of the Supplementary Materials.

We apply two methods:

1. Original WH smoothing using y = ln (d/ec) and weights w = d as in Section 3.
2. Generalized WH smoothing, using the likelihood formulation of Section4.

Both methods use the same smoothing parameter(s) λ, to ensure that prior assumptions on θ = ln μ are held constant. We fix the penalty order at q = 2, corresponding to second-order differences. As both estimators target θ, we compare them using the following relative error metric:

$$\Delta ( \theta ) = \frac { \ell _ { P } ( \hat { \theta } _ { M L } ) - \ell _ { P } ( \theta ) } { \ell _ { P } ( \hat { \theta } _ { M L } ) - \ell _ { P } ( \hat { \theta } _ { \infty } ) } .$$


<!-- p:10 -->


Table 2. Impact of the approximation from the original WH smoothing on the 6 simulated datasets.

| Portolio type   |   Head count | Relative error   | SMR    |
|-----------------|--------------|------------------|--------|
| Annuity         |       20,000 | 1,91%            | 99,19% |
| Annuity         |      100,000 | 0,02%            | 99,89% |
| Annuity         |      500,000 | 0,00%            | 99,99% |
| LTC             |       20,000 | 93,27%           | 86,86% |
| LTC             |      100,000 | 5,12%            | 97,59% |
| LTC             |      500,000 | 0,24%            | 99,56% |

Here maximizes the penalized likelihood, while ê corresponds to the solution with λ → ∞, which we later show to be the degree-(q – 1) polynomial that maximizes the likelihood. By construction:

$$\Delta ( \hat { \theta } _ { _ { M L } } ) = 0 , \ \Delta ( \hat { \theta } _ { _ { \infty } } ) = 1 , \ \text { and } \ \Delta ( \theta ) \geq 0 .$$

A model with ∆(θ) &gt; 1 performs worse than a simple polynomial fit under the prior.

Table 2 presents the values of ∆(ênorm) across the six datasets. As expected, discrepancies decrease with portfolio size. For annuities, the approximation performs reasonably well even at smaller scales. In contrast, for LTC, it yields substantial errors, except for the largest portfolio.

One explanation, supported by the standardized mortality ratio (SMR) also provided in Table 2, is the positive correlation between observed event counts and their use as weights. This causes high crude rates to be overweighted, and low rates to be underweighted – introducing systematic overestimation of mortality rates. This bias is more severe in the LTC case where the observed deaths by data point is lower. In contrast, generalized WH smoothing preserves total event counts by construction, always yielding an SMR of exactly 100%. These results support adopting generalized WH smoothing in most practical settings. It retains the advantages of the original method while offering improved accuracy – even in small samples – and remains straightforward to implement.

## 5. How to select the smoothing parameters?

### 5.1. Impact of smoothing parameter choice

In the one-dimensional case, WH smoothing involves a single smoothing parameter λ; in two dimensions a pair λ = (λx, λz). These parameters govern the trade-off between fidelity to the data and smoothness of the estimate, as defined in Equation (1.1).

Figure 1 illustrates this effect in a one-dimensional annuity dataset (100,000 policyholders, see Section 4.2), with three values of λ. The effective degrees of freedom (edf), computed as the trace of the hat matrix H = (W + Pλ)−1W, are shown for each curve. This quantity serves as a non-parametric analog of the number of free parameters in classical models and can take fractional values.

As shown, a low value λ = 101 yields an overfitted result that mirrors sampling noise, while a high value λ = 107 oversmooths and obscures the underlying trend. A mid-range value λ = 104 appears visually balanced. However, selecting a smoothing parameter by eye is unreliable: small-sample variability at the extremes of the age range can easily be mistaken for meaningful patterns.

The two-dimensional case further illustrates this difficulty. Figure 2 presents the smoothed transition rates from disability to death in an LTC portfolio (100,000 policyholders), using 9 combinations of (λx, λz). Choosing an appropriate parameter pair visually becomes nearly impossible, reinforcing the need for a data-driven statistical selection criterion.

### 5.2. Statistical criteria for parameter selection

Smoothing parameter selection typically relies on two classes of statistical criteria:


<!-- p:11 -->

λ = 10o

λ = 104

λ = 107

Force of mortality (logarithmic scale)

edf : 35.21

edf : 6.71

edf : 2.10

10-

8%

10

50

60

70

80

90

50

60

0

80

90

50

60

0L

80

90

Age

Figure 1. WH smoothing on a synthetic annuity portfolio with 3 smoothing levels. Dots: crude rates; curves: smoothed estimates; shaded areas: credibility intervals. edf: effective degrees of freedom.

λ2 = 10−1

λ2 = 102

λ2 = 105

95

90

85

Force of

80

mortality

75

0,585

70

edf: 29.6

edf : 9.4

edf : 4.5

0,461

95

0,373

90

0,286

Age

85

0,229

0,185

80

0,150

75

edf : 99.8

edf : 36.7

edf : 16.0

0,118

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

edf: 54.9

70

0

10


5

10

Duration in LTC

Figure 2. WH smoothing applied to disability-to-death transitions in an LTC portfolio, using 9 combinations of smoothing parameters. Contour lines and colours show the smoothed mortality surface by age and LTC duration.

1. Prediction-based criteria, which aim to minimize prediction error, such as the Akaike Information Criterion (AIC) (Akaike, 1973), and generalized cross-validation (GCV) (Wahba, 1980);
2. Likelihood-based criteria, which maximize the marginal likelihood – an approach introduced by Patterson and Thompson (1971) (under the name REML in the Gaussian case) and adapted to smoothingby Anderssen and Bloomfield (1974).

While prediction-based criteria have desirable asymptotic properties (Wahba, 1985; Kauermann, 2005), their convergence towards optimal smoothing parameters can be slow. In contrast, marginal


<!-- p:12 -->


1010

Figure 3. Comparison of criteria for selecting the smoothing parameter in one-dimensional WH smoothing. Left: distribution of effective degrees of freedom under AIC, GCV, and marginal likelihood across 100 replicates. Right: GCV and marginal likelihood values for one replicate as functions of the smoothing parameter.

GCV

marginal likelihood

Effective degrees of freedom

40

3.0

edf : 6.08

Criterion value

-100

30

2.5

20

2.0

-150

1.5

10

-200

edf : 35.31

GCV

Aic

marginal likelihood

100

202

104

106

108

1010

00

102

104

1906

108

Criterion

Smoothing parameter (logarithmic scale)

likelihood criteria tend to perform more robustly in finite samples (Reiss and Todd Ogden, 2009; Wood, 2011).

To illustrate this, we apply AIC, GCV, and marginal likelihood to 100 replicates of the annuity portfolio with 100,000 policyholders (see Section 4.2). For each replicate, we select the optimal smoothing parameter and compute the corresponding effective degrees of freedom.

As shown in the left side of Figure 3, marginal likelihood produces stable and coherent degrees of freedom across replicates, whereas AIC and especially GCV often yield overly complex models. On the right, we plot the GCV and marginal likelihood profiles for a single replicate: marginal likelihood exhibits a well-defined maximum, while GCV presents two local minima. One aligns with the marginal likelihood optimum, but the global minimum corresponds to a model with 35 degrees of freedom – an implausibly complex mortality curve.

These observations support the use of marginal likelihood over prediction-based criteria, especially in actuarial applications where robustness is key. Moreover, this choice aligns naturally with the Bayesian framework introduced in Sections 2–4.

We now detail its implementation – first for the original WH smoothing, then for the generalized setting – introducing three optimization strategies and three numerical algorithms and comparing their respective performances.

### 5.3 Selection in the original smoothing

We consider again the normal framework from Section 2, where y |θ ∼N(θ, σ2W−) and θ |λ~ N(0, σ2P−). In the empirical Bayes approach, the smoothing parameter λ is estimated by maximizing the marginal likelihood:

$$\mathcal { L } _ { \text {norm} } ^ { m } ( \lambda ) = f ( \mathbf y \, | \, \lambda ) = \int f ( \mathbf y , \theta \, | \, \lambda ) d \theta = \int f ( \mathbf y \, | \, \theta ) f ( \theta \, | \, \lambda ) d \theta .$$

This is simply the maximum likelihood method applied to the smoothing parameter, treated as deterministic but unknown. A closed-form expression for this integral can be derived using standard Gaussian identities (see Section C of the Online Supplementary Materials), yielding the marginal log-likelihood:

$$\ell _ { \text {norm} } ^ { m } ( \lambda ) = - \frac { 1 } { 2 } \left [ ( \text {y} - \hat { \theta } _ { \lambda } ) ^ { T } W ( \text {y} - \hat { \theta } _ { \lambda } ) / \sigma ^ { 2 } + \hat { \theta } _ { \lambda } ^ { T } P _ { \lambda } \hat { \theta } _ { \lambda } / \sigma ^ { 2 } + \ln | W + P _ { \lambda } | - \ln | P _ { \lambda } | _ { + } + C \right ] .$$

where θλ = (W + Pλ )−1 Wy, and C = − ln |W|+ + (n* − q) ln (2π σ2) is a constant independent of λ. This function is maximized numerically to obtain λnorm


<!-- p:13 -->


### 5.4. Selection in the generalized smoothing

The empirical Bayes approach introduced in the normal framework can be extended to the generalized smoothing framework developed in Section 4. While no closed-form expression exists for the marginal likelihood in this context, it can be approximated using a second-order Taylor expansion of the logposterior density around its maximum θλ – similarly to what was done in the normal case. This yields the so-called Laplace approximation of the marginal likelihood (LAML), defined as

$$\ell _ { L A M L } ^ { m } ( \lambda ) = \ell ( \hat { \theta } _ { \lambda } ) - \frac { 1 } { 2 } \left [ \hat { \theta } _ { \lambda } ^ { T } P _ { \lambda } \hat { \theta } _ { \lambda } + \ln | W _ { \lambda } + P _ { \lambda } | - \ln | P _ { \lambda } | _ { + } - q \ln ( 2 \pi ) \right ]$$

where Wλ = Diag(exp (λ)  ec) and l(λ) is the log-likelihood evaluated at the penalized MLE. The detailed derivation of the Laplace approximation in this setting is provided in Section C of the u o aus t     e a da so   uon smoothing parameter λ in the generalized WH smoothing framework. As in the normal case, the marginal likelihood lAmL(λ) must be maximized numerically. However, a key distinction is that the penalized likelihood maximizer  now depends on λ and must be recomputed at each iteration via the PIRLS algorithm. This leads to a two-level optimization procedure:

- an inner loop estimating θλ for fixed λ using PIRLS;
- and an outer loop optimizing lLAmL(λ) with respect to λ.

This outer iteration approach is the most principled method for smoothing parameter selection in this setting.

Alternative strategies have been proposed to reduce computational burden. The first one, known as performance-oriented iteration, was introduced by Gu (1992) and relies on the observation that, at each PIRLS step, the working response vector Zk can be treated as approximately normal: Zk | θ ~ N(θ, W−1). Assuming Wk independent of λ, the marginal likelihood can be maximized within each PIRLS step using the normal approximation methodology of Section 5.3, with y replaced by Zk and W by Wk. This effectively reverses the nesting structure, potentially saving computational time when updating λ is less costly than recomputing a PIRLS step. A formal justification of the method is provided by Wood (2017, 149), which emphasizes that it does not actually require zk to have a normal distribution to be well founded.

A third and even simpler strategy is the alternate iteration approach, used for instance by Wood et al. (2017). It consists in alternating updates of θ (via PIRLS) and λ (via approximate marginal likelihood), without fully optimizing either at each step. This relies on the empirical observation that a coarse update of λ may suffice, as the marginal likelihood surface changes between iterations.

Despite their efficiency, both performance-oriented and alternate iteration approaches lack formal convergence guarantees. Unlike outer iteration, they operate on different smoothing parameters at each step, rendering penalized likelihood values non-comparable across iterations. Moreover, they do not track the value of lLAmL(λ) during the optimization, making it harder to assess convergence or apply step-length controls.

Detailed algorithmic formulations of all three strategies in the generalized WH smoothing framework are provided in Section D of the Supplementary Materials.

### 5.5. Algorithms for the maximization of the marginal likelihood

Several algorithms can be used to maximize the marginal likelihood or its Laplace approximation (LAML). It is generally preferable to apply these algorithms to the logarithm of the smoothing parameters, for three main reasons:

1. It ensures positivity of the smoothing parameters;
2. It simplifies the expressions of derivatives, when required;


<!-- p:14 -->


###### 14 Guillaume Biessy

3. It allows more uniform coverage of the range of interest (e.g. from λ = 101 to 107, as in Figure 1, differences of comparable magnitude occur on a logarithmic scale).

#### Derivative-free heuristics

A first, operationally simple option is to use general-purpose derivative-free optimization methods:

- Brent's method (Brent, 1973) in the one-dimensional case;
- The Nelder-Mead simplex algorithm (Nelder and Mead, 1965) in higher dimensions.

These are readily available in base R via the optimize and optim functions. They only require evaluating the marginal likelihood or LAML at each step, which is computationally inexpensive. However, they typically require more iterations to converge and cannot be combined with the alternate iteration approach, as they do not guarantee systematic improvement of the criterion at each step.

#### Generalized Fellner-Schall method

A more specialized algorithm is the generalized Fellner-Schall method, based on ideas from Fellner (1986) and Schall (1991), and adapted for smoothing parameter selection in multidimensional generalized linear models by Rodríguez-Álvarez et al. (2015). It may be summarized by the update formula:

$$\lambda _ { j } ^ { \text {next} } = \frac { \text {tr} ( P _ { \lambda } ^ { - } P _ { j } ) - \text {tr} [ ( X ^ { T } W X + P _ { , } ) ^ { - 1 } P _ { j } ] } { \hat { \beta } _ { \lambda _ { j } } ^ { T } P _ { j } \hat { \beta } _ { \lambda } } \lambda _ { j } ^ { \text {current} } \quad \text {for} \quad j \in \{ x , z \} .$$

in the one-dimensional case and Px (resp. Pz) is the marginal Dnz,qz © Ix) in the two-dimensional case.This update can be interpreted more intuitively as

$$\hat { \beta } _ { \lambda } ^ { T } ( \lambda _ { j } ^ { \text {next} } P _ { j } ) \hat { \beta } _ { \lambda } = \text {tr} [ P _ { \lambda } ^ { - } \lambda _ { j } ^ { \text {current} } P _ { j } - ( X ^ { T } W X + P _ { \lambda } ) ^ { - 1 } \lambda _ { j } ^ { \text {current} } P _ { j } ]$$

where the right-hand side corresponds to an effective degrees of freedom associated with λcurrent Pj, and the left-hand side to a squared error, normalized by the updated penalty precision. This makes λnext resemble a REML-based estimator for the inverse variance. More details may be found in RodríguezÁlvarez et al. (2019). This method:

- May be combined with any of the three iteration nesting schemes (outer, performance, and alternate);
- Does not require explicit derivative computations;
- Converges towards an approximate maximum of LAML in the generalized case, since it ignores the dependence of W on λ;
- Tends to take longer steps than EM-like algorithms (Dempster et al., 1977), but shorter than Newton updates (see Wood and Fasiolo 2017, which also provides a thorough justification for the method).

#### Newton algorithm

A third option is the Newton method, which involves computing both the first and second derivatives of the marginal likelihood (or LAML) with respect to ln λ. Full derivations are provided in Wood (2011), which covers a more general case. The method applies in both the normal and generalized cases, but in the latter, derivative expressions are more complex due to the dependence of W on λ. The Newton al   s   s    e ade  sid e   oal complexity associated with this method, especially in the generalized case.


<!-- p:15 -->


### 5.6. Performance comparison

Sections 5.4 and 5.5 introduced eight combinations of nesting strategies and optimization algorithms applicable to the generalized WH smoothing. We now assess the potential convergence issues and approximation errors associated with each of them.

This analysis is based on 100 replicates of the simulated annuity and LTC portfolios with 100,000 policyholders, as described in Section 4.2. For each replicate and each method combination, we compute the LAML at the selected smoothing parameters and compare this value to the (approximate) optimal value obtained across all combinations, denoted λopt.

To quantify the discrepancy, we define the relative error:

$$\Delta ( \lambda ) = \frac { \ell _ { L A M L } ^ { m } ( \hat { \lambda } _ { o p t } ) - \ell _ { L A M L } ^ { m } ( \lambda ) } { \ell _ { L A M L } ^ { m } ( \hat { \lambda } _ { o p t } ) - \ell _ { L A M L } ^ { m } ( \infty ) } \\ \text {s bounds to the } L \ A M L \ v e l u e \text { when using an infinite smoothening penalty that is the }$$

where lLAmL(∞) corresponds to the LAML value when using an infinite smoothing penalty, that is, the overly smooth baseline. By construction, ∆(λ) ≥ 0 for all tested methods, with ∆(λopt) = 0 and ∆(∞) = sn  e oe s voo ae vo ose  s as  s s replicates.

Results are summarised in Figure 4. The top panel displays the relative error ∆(λ) (capped below 10-10 for readability). In the outer iteration framework:

- The Newton method consistently achieves relative errors below 10-10;
- Brent and Nelder-Mead heuristics yield slightly higher errors but remain below 10-7;
- The generalized Fellner-Schall method produces higher errors, but still below 10-5 and negligible in practice.

In the performance and alternate iteration frameworks, all methods yield similar errors, consistently below 10-5, with no convergence issues observed in any replicate. These findings suggest that method selection can be guided by practical considerations such as speed and implementation ease.

The bottom panel of Figure 4 compares computation times (relative to the Nelder-Mead + outer iteration baseline):

- In the outer iteration framework, the Newton method is the fastest, followed by the FellnerSchall approach;
- All outer iteration variants are faster than their performance or alternate counterparts.

This is unsurprising, as PIRLS steps are particularly lightweight in WH smoothing (where the model matrix is the identity). However, alternate strategies may remain useful for more general cases like those described in Section 6.4.

For reference, the average time required for a single iteration using Nelder-Mead in the 2D outer iteration case is approximately 1.68 s (versus 5 ms in the 1D case).

## 6. How to improve smoothing computational efficiency?

### 6.1. Motivation

WH smoothing is a full-rank method, meaning that it includes as many parameters as there are observation points. This feature ensures a high degree of flexibility, allowing the estimator to closely track the input signal when sufficient data are available. Formally, WH smoothing is asymptotically unbiased since:

$$\mathbb { E } ( \hat { y } ) = ( W + P _ { \lambda } ) ^ { - 1 } W \mathbb { E } ( y ) \stackrel { m \to \infty } { \to } \mathbb { E } ( y ) ,$$

where m denotes the number of observed individuals, which influences the matrix W.

However, this flexibility comes at a computational cost. Some key operations, such as (implicit) matrix inversions, scale cubically with the number of parameters. As a result, WH smoothing may become impractical with large number of combinations or when applied repeatedly (e.g. in simulations or bootstraps).


<!-- p:16 -->


Figure 4. Comparison of the 8 nesting strategy and algorithm combinations in the 1D and 2D simulated cases. Top: relative error on the LAML (log scale). Bottom: improvement in average computation time compared to the Nelder-Mead + outer iteration reference.

1D, Outer iteration

1D, Performance iteration

1D, Alternated iteration

9-01

Relative error on marginal likelihood

10-7

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

10-6

10−7

10-8

10-9

01-01

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

8

Speed-up factor

2,5

2,33

2,0

1,98

1.4

1,5

1,32

1,33

1.15

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

In one-dimensional settings, such as age-only models with annual discretization, the number of points rarely exceeds 100, and computation time is negligible. In contrast, two-dimensional use cases – common in insurance – can lead to substantially larger datasets:

- Disability tables in France must cover entry ages from 18 to 61 and exit ages up to 62, resulting in (62 − 18) × (62 − 18 + 1)/2 = 990 combinations.
- Transition tables from short-term incapacity to disability involve entry ages from 18 to 67 and monthly durations from 0 to 36 months, yielding (67 — 18) × 36 = 1, 764 combinations.
- Long-term care (LTC) models require coverage over ages 50–100 and durations from 0 to 20 years, totalling (100 — 50) × (20 – 0) = 1000 combinations (in practice, this number may be lower due to data sparsity).

In such settings, computing WH smoothing – especially when paired with smoothing parameter selection – can take several minutes per application, limiting usability in iterative contexts.

To address this limitation, we now analyse the computational complexity of the main steps in WH smoothing and smoothing parameter selection then introduce two complementary strategies to reduce computation time:

- A structural optimization that exploits the specific form of WH penalization matrices;


<!-- p:17 -->


- A reduced-rank approximation that lowers the number of parameters while minimizing bias compared to the full-rank estimator.

Finally, we benchmark these strategies in terms of runtime and accuracy using 100 replicates of the mid-size annuity and LTC portfolios from Section 4.2. The structural optimization is compared to the original WH method, while the reduced-rank approximation is evaluated against the original method, the structural optimization, and a reference P-spline smoothing approach.

### 6.2. Practical computation for penalized smoothers

WH smoothing belongs to a broader family of penalized smoothing methods that produce estimates of the form:

$$\hat { y } _ { \lambda } = X \hat { \beta } _ { \lambda } \quad \text {where $\beta_{\lambda}$ solves} \, ( X ^ { T } W X + P _ { \lambda } ) \hat { \beta } _ { \lambda } = X ^ { T } W y .$$

Here, X and Pλ denote the model and penalization matrices of size n × p and p × p, respectively, and W is a diagonal matrix of positive weights of size n × n.

#### Computational steps

The computation of  for a given λ typically involves the following steps:

1. Absorb the weights in the model matrix and observation vector, forming W1/2X and W1/2y, which requires O(n2) and O(n) operations, respectively (multiplying each row of X and each element of y by the corresponding element of w).
2. Form the matrix Pλ. The cost of this operation is typically O(p2) in the general case.
3. Form the matrix XT WX and the vector XT Wy, which requires up to O(np2) and O(np) operations respectively.
4. Add together XTM WX and Pλ which requires O(p2) operations in the general case.
5. Compute the Cholesky decomposition XT WX + Pλ = RT R at a cost of O(p3).
6. Obtain βλ by forward-backward substitution, first solving Ru = X Wy then Rβλ = u with an associated cost of O(p2) for each system.
7. Compute λ = Xβλ at a cost of O(np).

As an alternative to Cholesky, QR decomposition may be used for greater numerical stability (see Golub and Van Loan, 2013). It applies to the weighted design matrix stacked with a matrix B such that BT B = Pλ.

#### Simplifications for WH smoothing

In WH smoothing, X = In, which simplifies computations:

- Step 7 is unnecessary, as well as the first part of step 3.
- XT Wy = Wy (step 3) is computed in O(n) by multiplying w and y.
- XT WX + Pλ = W + Pλ (step 4) is also computed in O(n) by adding the vector w to the leading diagonal of Pλ.

#### Generalized WH smoothing with outer iteration

When using the outer iteration approach (see Section 5), each candidate λ requires a full PIRLS cycle to estimate , with new working vector k and weight matrix Wk. Steps 1–6 above are repeated until convergence of the PIRLS algorithm, which may be assessed by monitoring the changes in penalized deviance. The deviance may be computed at a O(n) cost. For penalization based on differences matrices, computation of βλ Pλβ should be based on the expression of Rλ,q provided in Section 1.1 for an associated cost of O(qp). In addition, PIRLS iterations for each new λ can be initialized using the previous estimate of  for faster convergence.


<!-- p:18 -->


#### LAML computation

Once the deviance is known, computing the marginal likelihood/LAML also requires:

- ln |X†WX + Pλ|, which may be computed at a cost of O(p) from the leading diagonal of the Cholesky/QR factor R computed at step 5 in the derivation of λ.
- ln |Pλ|+, which may be obtained from the eigenvalues of the penalization matrix: Section 6.4 shows that in the two-dimensional case, it can be computed via eigendecomposition of DT px,qx then only requires scaling the eigenvalues for a cost of O(p).

#### Algorithm-specific computations

Brent and Nelder-Mead require only marginal likelihood/LAML evaluations.

The generalized Fellner-Schall algorithm relies on the update formula of Equation (5.1):

$$\lambda _ { j } ^ { \text {next} } = \frac { \text {tr} ( P _ { \lambda } ^ { - } P _ { j } ) - \text {tr} [ ( X ^ { T } W X + P _ { \lambda } ) ^ { - 1 } P _ { j } ] } { \hat { \beta } _ { \lambda } ^ { T } P _ { j } \hat { \beta } _ { \lambda } } \lambda _ { j } ^ { \text {current} } \quad \text {for} \quad j \in \{ x , z \} . \\ \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot$$

Evaluation of tr(P− Pj) does not require any matrix product. In the one-dimensional case it is simply (p — q)/λ while in the two-dimensional case it may be obtained directly at a O(p) cost using the eigenvalues of the aforementioned penalization matrices Pj. Evaluation of tr[(XWX + Pλ)−1 P] may use the identity tr(AB) = Σ,j AijBji and therefore be computed at an O(p2) cost if the matrix (XT WX + Pλ)−1 and Pj are available. Computation of V = (XT WX + Pλ)−1 is done by first solving for the inverse K = R−1 of the Cholesky/QR factor and then forming V as KKT. Both operations have a O(p3) cost.

Newton method also requires computation of V, as well as several matrix products involving the penalization matrix Pj. For example, the second derivatives of marginal likelihood require tr[VP,VPk] terms, and the second derivatives of marginal likelihood require tr[V(X(∂W/∂ρj)X + Pj)V(X(∂ W/∂ρk)X + Pk)] terms where ρj = ln (λj), j = k = x in the one-dimensional case and {j, k} ∈ {x, z} in the two-dimensional case. The identity tr(AB) = Σi,j ABji can also be used in this case but matrix products VPj or V[X(∂W/∂ρj)X + P] still need to be explicitly computed, for a respective cost of O(p3) and O(np2) each.

These additional computations make Newton updates more expensive than generalized FellnerSchall updates, but they generally yield faster convergence and higher precision (see Section 5.6).

### 6.3. Banded optimization for WH smoothing

We now consider how to exploit the banded structure of the penalization matrix in WH smoothing. This structure enables significant computational gains, especially when dealing with large number of bso ot o os o m   =  pne  =  nt s ons t n  ssal and generalized WH smoothing.

#### One-dimensional case

banded with bandwidth q. As a consequence:

1. Compact storage: Pλ can be stored in a compact form with dimensions n × (q + 1) and updated for new λ at a cost of O(qn). The matrix W + Pλ shares this structure.
2. Efficient Cholesky decomposition: the Cholesky factor R of W + Pλ can be computed in O(q2n) instead of O(n3), and R is also banded with the same bandwidth.


<!-- p:19 -->


3. Efficient back-substitution: computing λ = βλ using R is now O(qn) instead of O(n2).
4. Efficient inversion of R: the inverse K = R−1 costs O(qn2), an improvement over the O(n3) cost for dense matrices.

However, K is a dense triangular matrix, meaning the computation of V = KK remains a O(n3) operation. Fortunately, the generalized Fellner-Schall algorithm only requires the diagonal of V, which can be obtained from K in O(n2), since:

$$\lambda _ { j } [ \text {tr} ( P _ { \lambda } ^ { - } P _ { j } ) - \text {tr} ( V P _ { j } ) ] = ( n - q ) - ( n - \text {tr} [ V W ] ) = \text {diag} ( V ) ^ { T } \mathbf w - q .$$

Furthermore, the Newton algorithm benefits as well: the trace terms involving VPλ or V(∂ W/∂ ln λ + Pλ) are based on banded matrices, making those products computable in O(qn2) instead of O(n3).

#### Two-dimensional case

In two dimensions, the penalization matrix is Pλ = λxPx + λzPz where:

- P x = In ⊗ DT, Dnx,9x nx,qx
- Pz = DT Dn2,4z ©Inx. nz,qz

This structure has the following key properties:

- Both matrices are made of nz × nz square blocks of dimensions nx × nx each.
- Px is block diagonal with nz identical nx × nx banded blocks (bandwidth qx).
- Pz is block banded with bandwidth qz. Each block is a scaled identity matrix.
- As a whole, Pz and Pλ may be viewed as banded matrices with bandwidth q = qz × nx.

This implies that all statements made in the one-dimensional case carry over to the two-dimensional case with this value of q. It also suggests that, if (qx + 1)/nx &lt; (qz + 1)/nz, dimensions x and z should be permuted before applying WH smoothing for maximal efficiency.

As in the one-dimensional case, the generalized Fellner-Schall update formula does not require the full computation of V. Indeed, to compute tr[VPx] and tr[VPz], we only need access to elements of V for which either Px or Pz is non-zero. From what precedes, Px has bandwidth qx while Pz only contains qz non-zero diagonals on each side of the leading diagonal. As V is symmetric, we only need to compute qx + qz + 1 diagonals of V for an associated cost of O([qx + qz]n2) instead of O(n3).

With the Newton method, while computing V = KKTM still incurs a O(n3) cost, matrix multiplications like VPj or V(∂ W/∂ρj + Pj) can be performed block-wise. It may easily be checked, for example, that the products VPx and V(∂ W/∂ρx + Px) have a cost of O(qxn2), while the products VPz and V(∂W/∂ρz + Pz) have a cost of O(qzn2).

#### Summary of complexity gains

Thanks to the banded structure, most computations involved in WH smoothing can be accelerated by a factor of n/(q + 1) in the 1D case and max (nx/(qz + 1), nz/(qx + 1)) in the 2D case. There are 3 notable exceptions:

- Cholesky decomposition is improved from O(n3) to O(q2n) – a quadratic speed-up.
- Computation of V = KK remains O(n3).
- Some matrix products required by Newton method get a full n/(qz + 1) or n/(qz + 1) speed-up in the 2D case.

Table 3 summarizes theoretical complexities across different frameworks, including a typical generalized additive model framework for which the penalization matrix is diagonal. This last framework is used by the rank-reduced WH smoothing approach introduced next, as well as the P-spline alternative used for comparison.


<!-- p:20 -->


Table 3. Compared theoretical leading-order costs associated with the key steps in smoothing computations for several frameworks. All cells should be read as O(. . .).

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

Figure 5. Computation time comparison for 2D generalized WH smoothing with outer iteration. The speed-up factor is computed relative to the original dense method using the Nelder–Mead algorithm.

Dense computations

Banded computations

35

3,0

30

Speed-up factor

2,5

2,33

25

24,93

2,0

20

1,64

15

16,65

15,38

1,5

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

#### Empirical gains

Figure 5 compares actual computation times of WH smoothing (two-dimensional, outer iteration), showing that adapting the implementation to exploit banded structures results in large speed gains:

- The Nelder-Mead method benefits the most, with a 25 × speedup compared to dense computation.
- Newton and Fellner-Schall methods see 6.6 × and 10 × improvements, respectively, making them fall behind the Nelder-Mead method.

As a final advantage, Brent and Nelder-Mead heuristic methods rely solely on banded matrices that can be stored as compact matrices of dimensions (q + 1) × n, adding further efficiency.

### 6.4. Natural parameterization and rank reduction of WH smoothing

Demmler and Reinsch (1975) proposed a natural parameterization for penalized smoothers using the eigendecomposition of the penalization matrix. This provides both an intuitive interpretation of the smoothing mechanism and a foundation for dimension reduction via rank-restricted estimation.


<!-- p:21 -->


###### One-dimensional case

In one dimension, let Dn,Dn,q = UΣUT be the eigendecomposition of the penalty matrix, where U is orthogonal and Σ diagonal with non-negative eigenvalues. A change of variable θ = Uβ transforms the WH optimization into:

$$\hat { y } = U \hat { \beta } \quad \text {where} \quad \hat { \beta } = \arg \min _ { \beta } \left \{ ( y - U \beta ) ^ { T } W ( y - U \beta ) + \lambda \beta ^ { T } \Sigma \beta \right \}$$

yielding the solution:

$$\hat { y } = U ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W y \quad \text {where} \quad S _ { \lambda } = \lambda \Sigma .$$

This formulation shows that WH smoothing decomposes the signal into eigenvector components and attenuates each according to the associated eigenvalue – the higher the eigenvalue, the stronger the shrinkage.

We refer to Section E of the Online Supplementary Materials for graphical illustrations of:

- the basis eigenvectors of Dn,qDn,q; n,q
- the evolution of their effective degrees of freedom under smoothing.

These figures show that only the first few components retain substantial degrees of freedom under moderate smoothing, motivating dimensionality reduction.

#### Two-dimensional case

In two dimensions, the penalization matrix takes the form:

$$P _ { \lambda } = \lambda _ { x } I _ { n _ { z } } \otimes D _ { n _ { x } , q _ { x } } ^ { T } D _ { n _ { x } , q _ { x } } + \lambda _ { z } D _ { n _ { z } , q _ { z } } ^ { T } D _ { n _ { z } , q _ { z } } \otimes I _ { n _ { x } } ,$$

Define U = Uz ⊗ Ux, and θ = Uβ. Then the WH estimate becomes:

$$\hat { y } = U ( U ^ { T } W U + S _ { \lambda } ) ^ { - 1 } U ^ { T } W y \quad \text {where} \quad S _ { \lambda } = \lambda _ { x } I _ { n _ { e } } \otimes \Sigma _ { x } + \lambda _ { z } \Sigma _ { z } \otimes I _ { n _ { z } } .$$

As in the one-dimensional case, this representation reveals how smoothing operates via coordinatewise shrinkage in the eigenbasis. Section E of the Online Supplementary Materials displays the corresponding per-parameter effective degrees of freedom.

#### Rank reduction strategy

Inspection of the effective degrees of freedom reveals that many components are heavily shrunk, especially those associated with high eigenvalues. This suggests reducing the dimension by keeping only the p &lt; n components with the lowest eigenvalues.

In the one-dimensional case, the reduced-rank approximation is

$$\hat { y } _ { p } = U _ { p } ( U _ { p } ^ { T } W U _ { p } + \lambda \Sigma _ { p } ) ^ { - 1 } U _ { p } ^ { T } W y$$

where Up and Σ consist of the first p eigenvectors and their corresponding eigenvalues, respectively.

In the two-dimensional case, we retain px and pz eigenvectors in each dimension and use:

$$\hat { y } _ { p _ { x } , p _ { z } } = U _ { p _ { x } , p _ { z } } ( U _ { p _ { x } , p _ { z } } ^ { T } W U _ { p _ { x } , p _ { z } } + \lambda I _ { x } \otimes \Sigma _ { x , p _ { x } } + \lambda _ { z } \Sigma _ { z , p _ { z } } \otimes I _ { p _ { x } } ) ^ { - 1 } U _ { p _ { x } , p _ { z } } ^ { T } W y \\ U _ { p _ { x } , p _ { z } } = U _ { p _ { x } , p _ { z } } ( U _ { p _ { x } , p _ { z } } ^ { T } W U _ { p _ { x } , p _ { z } } + \dot { \lambda } _ { z } I _ { p _ { z } } \otimes I _ { p _ { x } } ) ^ { - 1 } U _ { p _ { x } , p _ { z } } ^ { T } W y \\$$

with Upx,pz = Uz,pz ⊗ Ux,px. In that case, given a target number of parameters pmax, we propose selecting (px, pz) such that pxPz ≤ pmax and px/nx ≈ pz/nz using the rule:

$$\kappa = \sqrt { p _ { \max } / n _ { x } n _ { z } } , \ \ p _ { x } = \lfloor \min ( \kappa , 1 ) n _ { x } \rfloor , \ \ p _ { z } = \lfloor \min ( \kappa , 1 ) n _ { z } \rfloor .$$

Adaptations for generalized WH smoothing follow by replacing (y, W) with (zk, Wk) in the above expressions.


<!-- p:22 -->


###### Efficient computation via GLAM

Currie et al. (2006) propose a general framework, GLAM, that exploits Kronecker structure for efficient computations. In our context, the model matrix Upx,pz inherits a Kronecker product form, allowing operations that rely on this matrix to be executed dimension-wise without explicit construction of the full matrix. This significantly reduces memory use and computation time in the two-dimensional rank-reduced WH framework.

#### Impact of using the rank-reduced basis

We now evaluate the impact of the rank-reduced WH basis introduced in Section 6.4 in terms of both smoothing accuracy and computational speed. For context, results are compared against those obtained using P-spline smoothing with the same number of basis functions.

To ensure a fair comparison, both approaches were implemented in the same computational framework, including the use of GLAM in the two-dimensional case – only the structure of the basis (and hence the model matrix) differs. The penalty structure and the unpenalized fixed effects (polynomials of degree q – 1) are identical.

In addition to the full basis of size 450 (30 × 15), three reduced basis of respective size 288 (24 × 12), 128 (16 × 8) and 32 (8 × 4) were considered.

As in Section 5.6, accuracy is assessed using the relative LAML error defined in Equation (5.2). Note, however, that since both reduced-rank and P-spline smoothers rely on different bases and penalization matrices, their LAML expressions are different from the one used for full-rank WH smoothing. Hence, a reduced model can exhibit a higher LAML than the full-rank version at its selected smoothing parameter.

Figure 6 summarises the average speed-up achieved by both the reduced-rank and P-spline smoothers compared to the full-rank WH smoothing. As the number of retained parameters decreases, computation time drops substantially. Compared to the full-rank WH smoothing (unoptimized):

- the 128-parameter basis achieves an 88 × speed-up;
- the 32-parameter basis achieves up to 256 × faster computation.

The alternate iteration and performance iteration strategies outperform the outer iteration in the -e et ot o se o ct e s oid es etles neck – even with the use of the GLAM framework. In this context, the Newton algorithm combined with alternate iteration proves to be the most efficient, with the generalized Fellner-Schall update being nearly as competitive for smaller bases.

The gains in computational speed come with a moderate tradeoff in estimation accuracy. As shown in Figure 7, the relative LAML errors remain small:

- For the 128-parameter basis, the average error is just 0.82%.
- For the 32-parameter basis, it rises to 2.26%.

Across all sizes, the reduced-rank WH smoother slightly outperforms the P-spline smoother in terms of LAML error, confirming its effectiveness as a principled dimension reduction strategy.

## 7 How to extrapolate the smoothing?

- ot os s s ts s s s- s s  -n that is, predicting values outside the range of the original data. Extrapolation is handled by solving an extended smoothing problem where extrapolated positions are associated with zero-weight observations.

However, in the two-dimensional case, extrapolation must be performed carefully: constraints are needed to ensure that the extrapolated solution remains consistent with the original smoothing result over the observed data. Following the approach introduced by Carballo et al. (2021) for P-splines, we now extend WH smoothing to support extrapolation while also enabling the construction of credibility intervals that capture uncertainty both inside and outside the original observation domain.


<!-- p:23 -->


Figure 6. Computation speed improvement from WH smoothing with a reduced-rank basis (solid lines) or P-spline basis (dotted lines), relative to unoptimized full-rank WH smoothing, as a function of basis size.

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

11,.46

5,34

5,93

2,51

5,74

4,35

1,84

0.80

2.48

1.29

Computation time improvement factor

0,72

1,28

1,64

244,43

224,21

100

75,66

52,81

210,99

67,44

189,30

Performance iteration

64,92

61,04

18,78

38,40

10

17,95

5,37

9.25

8,70

0.73

0,73

2,42

2.49

1.27

4,54

2,47

2,57

1,22

215,00

256,31

100

204,41

88,31

191,71

44,98

75.70

Alternated iteration

33.42

13,15

10

5.51

13,08

3,55

4,.44

1.26

3,42

1,21

450

288

128

32 450

288

128

32 450

288

128

32

Number of retained parameters

Figure 7. Relative LAML error of WH smoothing with a reduced-rank basis (solid lines) or a P-spline basis (dotted lines), with respect to unoptimized full-rank WH smoothing, as a function of basis size.

4,51%

Relative error on marginal likelihood

%

3%

2,26%

2%

1,21%

0,91%

1%

0,33%

0,82%

0,05%

0%

0,00%

450

288

128

32

Number of retained parameters

Smoothing basis

WH (rank-reduced)

P-splines


<!-- p:24 -->


### 7.1. Defining the extrapolation of the smoothing

Let ê be the WH smoothing result obtained from an observation vector y defined over positions x (in 1D) or (x, z) (in 2D). We wish to extend predictions to a larger domain x+ (or (x+, z + )), with x ⊂ x+ and similarly for z.

To preserve WH smoothing's requirement for evenly spaced points, we assume that x+ and z+ are sequences of consecutive integers. Let n+ be the length of x+ in the on-dimensional case. In the twodimensional case, let nx+ and nz+ be the lengths of x+ and z+ and note n+ = nx+ × nz+.

We define matrices Cx and Cz such that each extracts the indices of the original data from the larger o   i    i   { x}    ( l    =  :s observed positions. Define the matrix C as

$$C = \begin{cases} C _ { x } & \text {in the one-dimensional case,} \\ C _ { z } \otimes C _ { x } & \text {in the two-dimensional case.} \end{cases}$$

Then C has the following useful properties:

- For any full-domain vector y+, Cy+ returns the observed values only.
- Cay embeds the observed values into a larger zero-padded vector.
- CCTM = In and C C is a 2 × 2 block matrix with an identity matrix block and zeros everywhere else.

The extrapolated WH smoothing is defined as the solution to the following extended problem:

$$\hat { y } _ { + } = \arg \min _ { \theta _ { + } } \left \{ ( y _ { + } - \theta _ { + } ) ^ { T } W _ { + } ( y _ { + } - \theta _ { + } ) + \theta _ { + } ^ { T } P _ { + } \theta _ { + } \right \}$$

where:

- y+ = CTy is the extended data vector (zeros for unobserved points),
- W+ = CT WC is the extended weight matrix (zeros for unobserved points),
- P+ is the penalization matrix over the extended grid, defined as

$$P _ { + } = \begin{cases} \lambda D _ { n _ { + } , q } ^ { T } D _ { n _ { + } + q } & \text {in the one-dimensional case,} \\ \lambda _ { x _ { z + } } I _ { z + } \otimes D _ { n _ { x + } + q _ { x } } ^ { T } D _ { n _ { x + } + q _ { x } } + \lambda _ { z } D _ { n _ { z + } + q _ { z } } ^ { T } D _ { n _ { x + } + q _ { z } } \otimes I _ { x + } & \text {in the two-dimensional case.} \end{cases}$$

Importantly, the smoothing parameters λ, λx, and λz must remain fixed during extrapolation – they are inherited from the original fit and no new information is introduced.

The fidelity term in Equation (7.1) simplifies to:

$$( y _ { + } - \theta _ { + } ) ^ { T } W _ { + } ( y _ { + } - \theta _ { + } ) = ( C ^ { T } y - \theta _ { + } ) ^ { T } C ^ { T } W C ( C ^ { T } y - \theta _ { + } ) = ( y - \theta ) ^ { T } W ( y - \theta )$$

where θ = Cθ+. This is the fidelity term from the original fit.

The smoothness criterion, on the other hand, now applies to the entire extended domain, constraining the extrapolated parts of + to remain smooth and consistent with the trend learned from the data.

The same extrapolation approach applies directly to generalized WH smoothing, simply by replacing y by zk and W by Wk, obtained at convergence of the PIRLS algorithm and setting σ2 = 1 in the derived credible intervals.

### 7.2. Unconstrained solution for the 1D case

The solution to the extrapolation problem in Equation 7.1 can be obtained directly, as in Section 1.1, by taking derivatives with respect to θ+ and setting them to zero. This yields the closed-form solution:

$$\hat { y } _ { + } = ( W _ { + } + P _ { + } ) ^ { - 1 } W _ { + } y _ { + } \quad \text {where} \quad y _ { + } = C ^ { T } y \quad \text {and} \quad W _ { + } = C ^ { T } W C .$$


<!-- p:25 -->


Assuming a Bayesian model where y+ |θ+ ∼N(θ+, σ2W +−1) and θ+ ∼ N(0, σ2P +−1 ), we obtain, as in Section 2, the following credible interval:

$$\mathbb { E } ( y _ { + } ) \, | \, y _ { + } \in \left [ ( W _ { + } + P _ { + } ) ^ { - 1 } W _ { + } y _ { + } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \sigma ^ { 2 } \text {diag} \left \{ ( W _ { + } + P _ { + } ) ^ { - 1 } \right \} } \right ] .$$

To get a better understanding about how the variance-covariance matrix V+ = (W+ + P+)−1 for the unconstrained extrapolation problem of Equation (7.1) is related to the variance-covariance matrix V = (W + Pλ)−1 of the original smoothing problem, introduce matrices Cj (for j ∈ x, z), which selects the rows in the extrapolated domain that are not part of the original data and define:

$$\overline { C } = \begin{cases} \overline { C } _ { x } & \text { in the one-dimensional case,} \\ \overline { C } _ { z } \otimes \overline { C } _ { x } & \text { in the two-dimensional case,} \end{cases} \quad \text {and} \quad Q = \begin{cases} C \\ \overline { C } \end{cases} \, .$$

With this definition, Q is a permutation matrix moving observed positions to the top.

In the unidimensional case, the extended difference matrix D+,q takes the block-wise form:

$$D _ { n + q } = \begin{bmatrix} D _ { 2 - } & D _ { 1 - } & 0 \\ 0 & D _ { n , q } & 0 \\ 0 & D _ { 1 + } & D _ { 2 + } \end{bmatrix} = Q ^ { r } \left [ \begin{matrix} D _ { n , q } & 0 \\ D _ { 1 } & D _ { 2 } \end{matrix} \right ] Q \quad \text {where } D _ { 1 } = \left [ \begin{matrix} D _ { 1 - } \\ D _ { 1 + } \end{matrix} \right ] \text { and } D _ { 2 } = \left [ \begin{matrix} D _ { 2 - } & 0 \\ 0 & D _ { 2 + } \end{matrix} \right ] .$$

The extended weight and penalization matrices may be rewritten:

$$W _ { + } = Q ^ { T } \left [ \begin{matrix} W & 0 \\ 0 & 0 \end{matrix} \right ] Q \quad \text {and} \quad P _ { + } = D _ { n _ { + , q } , q } ^ { T } D _ { n _ { + , q } } = \lambda Q ^ { T } \left [ \begin{matrix} P _ { \lambda } + P _ { + } ^ { 1 1 } & P _ { + } ^ { 1 2 } \\ P _ { + } ^ { 2 1 } & P _ { + } ^ { 2 2 } \end{matrix} \right ] Q$$

where P+ = λDτ Dj, for i, j ∈ {1, 2}.

This block structure allows us to apply standard results for partitioned matrix inverses to derive:

$$V _ { + } = Q ^ { T } \begin{bmatrix} V _ { + } ^ { 1 1 } & V _ { + } ^ { 1 2 } \\ V _ { + } ^ { 2 1 } & V _ { + } ^ { 2 2 } \end{bmatrix} Q = Q ^ { T } \begin{bmatrix} V _ { + } ^ { 1 1 } & & & - V _ { + } ^ { 1 1 } P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \\ & & & \\ - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V _ { + } ^ { 1 1 } & & ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V _ { + } ^ { 1 1 } P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } + ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \end{bmatrix} Q$$

with V11 1 = [W + Pλ + P1 − P12(P22)−1 P21]−1.

From the above, we retrieve:

$$C \hat { y } _ { + } = C V _ { + } W _ { + } y _ { + } = C Q ^ { T } V _ { + } Q C ^ { T } W y = V _ { + } ^ { 1 1 } W y .$$

This coincides with the original fit  only if V1 = V. In general, this equality does not hold, since the extrapolation solution minimizes the total smoothness of the extended vector, not just of the observed part.

In V22, we identify:

- known part to the extrapolated part;
- an innovation error term: (P2)-1 associated with the prior on the extrapolated coefficients C +.

In the one-dimensional case, D2 is block-diagonal with invertible triangular blocks, so:

$$P _ { + } ^ { 1 1 } - P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } = D _ { 1 } ^ { T } D _ { 1 } - D _ { 1 } ^ { T } D _ { 2 } ( D _ { 2 } ^ { T } D _ { 2 } ) ^ { - 1 } D 2 ^ { T } D _ { 1 } = 0$$

which means that V1 = (W + Pλ)−1 = V. This confirms the result from Carballo et al. (2021), namely that with a difference-based penalty, a perfectly smooth extrapolation that leaves the original fit unchanged can always be constructed in the one-dimensional case.

This behaviour is illustrated in Figure 8, which shows the extrapolated fit (with q = 2) obtained from generalized WH smoothing applied to the annuity portfolio used previously. The extrapolation follows n i   s w ve −-  =  -    ood t - l ns e Age


<!-- p:26 -->

(logarithmic scale)

100

10-1

Force of mortality

10-2

O

10-3

40

50

60

70

80

90

100

110

Figure 8. Extrapolation of one-dimensional WH smoothing. The smoother is extrapolated on both sides of the initial observation range following a polynomial of degree q – 1 (in this case a straight line as q = 2).

### 7.3. Constrained solution for the 2D case

In the two-dimensional case, while the extended penalization matrix P+ still takes the same structure as previously described, the expressions of its block components P11, P12, P21, P21, and P22 are more com-+, +, + C+ ≠ . Solving the unconstrained extrapolation problem thus leads to a modification of the estimated coefficients for the observed data positions, as demonstrated by Carballo et al. (2021).

This difference arises because, unlike the one-dimensional case, the smoothness criterion in two dimensions penalizes both rows and columns simultaneously, making it impossible to extrapolate without increasing the penalization. Since no new data are introduced in the extrapolated region, the smoothness criterion weighs more heavily in the optimization, prompting adjustments to the originally fitted values in order to produce a globally smoother estimate.

To address this, we follow the approach proposed by Carballo et al. (2021) and formulate a constrained optimization problem that enforces preservation of the original fitted values in the smoothing region. This is done by introducing a Lagrange multiplier ω and solving the following constrained problem:

$$( \hat { y } _ { + } ^ { * } , \hat { \omega } ) = \arg \min _ { \theta _ { + } ^ { * } , \omega } \left \{ ( y _ { + } - \theta _ { + } ^ { * } ) ^ { T } W _ { + } ( y _ { + } - \theta _ { + } ^ { * } ) + \theta _ { + } ^ { * T } P _ { + } \theta _ { + } ^ { * } + 2 \omega ^ { T } ( C \theta _ { + } ^ { * } - \hat { y } ) \right \} .$$

This optimization admits a closed-form solution for the constrained extrapolated estimator * as a linear transformation of . The derivation details are provided in Section F of the Online Supplementary Materials. The final form is

$$\hat { y } _ { + } ^ { * } = Q ^ { T } \left [ \begin{matrix} I \\ - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } \end{matrix} \right ] \hat { y }$$

and the associated variance-covariance matrix is

$$V _ { + } ^ { * } = Q ^ { T } \left [ \begin{matrix} V & - V P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \\ - ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V & ( P _ { + } ^ { 2 2 } ) ^ { - 1 } P _ { + } ^ { 2 1 } V P _ { + } ^ { 1 2 } ( P _ { + } ^ { 2 2 } ) ^ { - 1 } + ( P _ { + } ^ { 2 2 } ) ^ { - 1 } \end{matrix} \right ] Q .$$

This formulation differs from the variance matrix of the unconstrained solution. Indeed, it enforces the constraint that the initial coefficients remain unchanged, as reflected by the presence of V (the original variance matrix) instead of V1. The corresponding credible intervals are


<!-- p:27 -->


Figure 9. Constrained extrapolation of 2D WH smoothing. The contour lines of mortality rates and the associated standard deviation are depicted. The dotted lines delimit the boundaries of the initial smoothing region.

Force of

Standard

mortality

deviation

100


1,447

1,310

0,968

0,890

90

0,652

90

0,621

0,441

0,476

Age

07*8

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

180'0

0,034

1900

60

0

5

10

15

20

60

10

15

20

Duration in LTC


$$\mathbb { E } ( y _ { + } ) \left | y _ { + } \in \left [ \hat { y } _ { + } ^ { * } \pm \Phi ^ { - 1 } \left ( 1 - \alpha / 2 \right ) \sqrt { \sigma ^ { 2 } \text {diag} ( V _ { + } ^ { * } ) } \right ] .$$

The following figures illustrate the impact of the constrained extrapolation procedure discussed above, using the LTC portfolio of 100,000 policyholders as a case study.

- Figure 9, left (mortality rates): this panel shows the estimated mortality rates obtained after applying the constrained extrapolation procedure to the two-dimensional WH smoothing model. The dotted lines indicate the boundaries of the original smoothing region. Visually, the transition from the smoothing region to the extrapolated area is seamless – the extrapolated surface naturally extends the smoothed mortality rates while respecting the original fitted values within the data range.
- Figure 9, right (standard deviation): this panel displays the posterior standard deviation (or credible interval width) associated with the extrapolated estimates. It reflects both the uncertainty from the original smoothing and the innovation error introduced in the extrapolated region. As expected, the standard deviation increases as we move away from the observed region, illustrating growing uncertainty about farther values.
- Figure 10 (ratio of mortality rates): this heatmap shows the pointwise ratio between the unconstrained and constrained extrapolation of the mortality rates. A value above 1 indicates that the unconstrained version overshoots the constrained one at that location, while values below 1 indicate underestimation. We observe that discrepancies exist not only in the extrapolated region but also within the original data region – confirming that the unconstrained approach distorts the original estimates in order to achieve overall smoothness.
- Figure 11 (ratio of standard deviations): this final figure includes two panels comparing uncertainty estimates.
- Left panel: ratio of standard deviation from the unconstrained extrapolation over that from the constrained extrapolation (including innovation error). The unconstrained version underestimate the actual uncertainty not only in the extrapolated region but also within the original data region, again reflecting the adjustments made to the original estimates in order to achieve overall smoothness.
- Right panel: ratio of standard deviation from the constrained extrapolation without innovation error over the fully constrained version with innovation error. This illustrates the contribution of the innovation error to the total uncertainty – it is substantial and should not be neglected.


<!-- p:28 -->


Figure 10. Ratio of mortality rates resulting from the extrapolation of 2D WH smoothing. The numerator corresponds to the unconstrained extrapolation and the denominator to the constrained extrapolation presented in Figure 9.

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

0

10

15

20

Duration in LTC

Figure 11. Ratio of standard deviation of log-mortality rates from the three extrapolation methods. Left: unconstrained versus constrained with innovation error. Right: constrained without versus with innovation error. In both, the denominator is the fully constrained method of Figure 9.

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

0

5

10

15

200

10

15

20

Duration in LTC

## 8. Discussion

#### Choosing the order of the penalization

Throughout this work, we have assumed second-order difference matrices for penalization. This choice is both standard and meaningful: from a Bayesian perspective, it corresponds to a prior belief that the log-transformed quantity of interest evolves linearly, which implies exponential behaviour on the original scale – consistent with actuarial models such as Gompertz.

The difference order directly shapes both the estimated trend and its extrapolation: higher-order penalties allow for more flexibility, but may induce unstable or erratic behaviour outside the data range. While Whittaker originally used third-order differences and higher orders can marginally improve model fit according to information criteria such as AIC, second-order penalties typically offer a robust compromise between smoothness, interpretability, and extrapolation stability. A detailed evaluation is provided in Section G of the Online Supplementary Materials.


<!-- p:29 -->


###### Summary of contributions

This paper revisits the classical WH smoothing approach through the lens of modern statistical modelling. Each section brought forward a key practical insight:

- Section 2 established that WH smoothing is more than an empirical method. It has a firm Bayesian foundation. Under Gaussian assumptions, credibility intervals may be derived and used as practical substitutes to confidence intervals.
- Section 3 clarified how to construct observation and weight vectors in survival analysis models: using log-crude rates as observations and event counts as weights yields a sound statistical formulation.
- Section 4 introduced generalized WH smoothing, in which the penalization is applied directly to the likelihood rather than a normal approximation. This refined method yields more accurate results, especially in situations where the available data volume is limited, but the number of combinations is high, such as in the two-dimensional case.
- Section 5 advocated for smoothing parameter selection via marginal likelihood (or its Laplace approximation, LAML), offering a principled and robust alternative to heuristic criteria like AIC or GCV.
- Section 6 presented two computational improvements: one exploits the banded structure of WH matrices to reduce runtime by up to a factor of 25; the other relies on reduced-rank smoothing ae  s  s (-s ×   u o e   a ssac slightly outperforming P-splines.
- Section 7 addressed extrapolation: while WH smoothing naturally extends beyond the data range, constraints are needed in two dimensions to preserve the original fit. We proposed a method to extrapolate while accounting for both structural uncertainty and innovation error and provided credible intervals accordingly.

All these techniques are available in the WH package for the statistical software R (R Core Team, 2025), including automated smoothing parameter selection and constrained extrapolation with uncertainty quantification.

#### Limitations and outlook

Despite its strong practical appeal, WH smoothing has limitations that suggest several avenues for future work:

- Regular spacing requirement: WH smoothing assumes evenly spaced observations, which aligns well with standard life insurance grids (age and/or duration). However, this is less suitable when events are concentrated in a short period, such as in disability or long-term care claims. One solution is to combine finer discretization in early durations with methods like P-splines that accommodate irregular grids. Alternatively, and adaptive WH smoothing procedure (based on the ideas in Ruppert and Carroll, 2000; Krivobokova et al., 2008) could offer a way to retain regular spacing while varying the smoothness locally.
- Limited covariate handling: The basic WH framework does not accommodate additional explanatory variables (e.g., gender or policy features). However, WH smoothing can be extended using ideas from smoothing spline ANOVA and hierarchical models (Lee and Durban, 2011; Gu, 2013), allowing for structured random effects and flexible interactions. This opens the door to richer, more personalized experience modelling while preserving interpretability.

In sum, revisiting WH smoothing through a modern lens reinforces its theoretical foundations and offers practitioners fast, transparent, and adaptable tools for experience modelling. It remains a compelling alternative to more recent – yet often more opaque – techniques when working with evenly spaced discrete data.


<!-- p:30 -->


Supplementary material. The supplementary material for this article can be found at https://doi.org/10.1017/asb.2025.10061.

Acknowledgments. The author thanks the two anonymous referees for their valuable comments, which helped improve the quality and clarity of the paper.

Data availability statement. The synthetic data used to conduct the performance comparisons in this study are available from the author upon request.

Competing interests. The author declares no competing interests.
