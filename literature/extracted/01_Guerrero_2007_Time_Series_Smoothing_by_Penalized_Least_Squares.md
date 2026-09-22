---
id: "01_Guerrero_2007_Time_Series_Smoothing_by_Penalized_Least_Squares"
source_pdf: "../pdf/01_Guerrero_2007_Time_Series_Smoothing_by_Penalized_Least_Squares.pdf"
source_filename: "01_Guerrero_2007_Time_Series_Smoothing_by_Penalized_Least_Squares.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/01_Guerrero_2007_Time_Series_Smoothing_by_Penalized_Least_Squares.references.md"
---

<!-- p:1 -->

Provided for non-commercial research and educational use only. Not for reproduction or distribution or commercial use.

Volume 77, issue 12

1 July 2007

ISSN 0167-7152

ELSIVIER

STATISTICS&amp;

PROBABILITY

LETTERS

Silver Jubilee Issue Dedicated to Richard A. Johnson on his 70th birthday

Guest Editors Hira L. Koul Michael Akritas Anton Schick

This article was originally published in a journal published by Elsevier, and the attached copy is provided by Elsevier for the author's benefit and for the benefit of the author's institution, for non-commercial research and educational use including without limitation use in instruction at your institution, sending it to specific colleagues that you know, and providing a copy to your institution's administrator.

All other uses, reproduction and distribution, including without limitation commercial reprints, selling or licensing copies or access, or posting on open internet sites, your personal or institution's website or repository, are prohibited. For exceptions, permission may be sought for such use through Elsevier's permissions site at:

http://www.elsevier.com/locate/permissionusematerial


<!-- p:2 -->

ELSEVIER

##### Abstract

its od  en a s o iot    d ss d os soies s icam solution involves an implicit adjustment to the observations at both extremes of the time series. The resulting estimated trend becomes more statistically grounded and an estimate of its sampling variability is provided. An index of smoothness is derived and proposed as a tool for choosing the smoothing constant.

©2007 Elsevier B.V. All rights reserved.

Keywords: Mean square error; Smoothness index; Unobserved components

## 1. Introduction

A basic objective of a time series analysis is to estimate unobserved components that are assumed to underlie the time series under study. In fact, the following unobserved components model of an observable time series provides a useful and simple representation of the data {Zt}:

$$Z _ { t } = \tau _ { t } + \eta _ { t } \quad \text {for } t = 1 , \dots , N ,$$

where τ, denotes the trend or signal of the data and η, is the noise at time t. Researchers in different fields have employed this representation. In an early use of (1), Whittaker (1923) and Henderson (1924) suggested to graduate (smooth) actuarial data by solving the following penalized least squares problem for μ = 0 and λ&gt;0:

$$\min _ { \{ \tau _ { i } \} } \sum _ { i = 1 } ^ { N } ( Z _ { t } - \tau _ { t } ) ^ { 2 } + \lambda \sum _ { i = d + 1 } ^ { N } ( \nabla ^ { d } \tau _ { i } - \mu ) ^ { 2 } .$$

Here, μ denotes the mean, if it exists, or just a reference level for {∇a τ}, where ∇a τ, denotes the dth order difference of {τt}, with d a nonnegative integer. That is, ∇0τ, = τt, ∇τt = τt − τt−1, ∇2τt = ∇(∇τt) and so on, in {u} o sos    s ( o  s

The constant λ is called the smoothing parameter since it penalizes the lack of smoothness in the trend. That is, {τ} → {Zt} as λ → 0, in which case the smoothness diminishes, while as λ → ∞, {τt} gets closer to the (smooth) polynomial implied by ∇aτ, = μ. Thus, in the latter case, when d = 0 the trend will be constant and when d≥1 the trend will be given by τt = β0 + β1t + · . · + βd−1td−1 + (μ/d!)td, where the constants βi, for

E-mail address: guerrero@itam.mx.

Available online at www.sciencedirect.com

### ScienceDirect

Statistics &amp; Probability Letters 77 (2007) 1225–1234

STATISTICS &amp;

PROBABILITY

LETTERS

www.elsevier.com/locate/stapro

## Time series smoothing by penalized least squares

Victor M. Guerrero

Departamento de Estadistica, Instituto Tecnológico Autónomo de México (ITAM), México 01000, D.F., Mexico

Available online 16 March 2007


<!-- p:3 -->


i = 0, . . . , d – 1, depend on the first d values of {τt}. Therefore, assuming μ = 0 has implications on the degree of the polynomial.

The value of d in (2) is usually chosen by the analyst on a priori grounds as d ≤2, and seldom is d≥3 used in practice. When μ = 0 and d = 1 or 2, the corresponding solutions to the minimization problem are well known in the financial and econometric literature. They are called exponential smoothing and Hodrick-Prescott filtering, respectively (see King and Rebelo, 1993). When the observed data are not equally spaced the problem has been considered in the general setting of smoothing splines (see Wahba, 1990). However, the observations of a time series are equally spaced and the problem has also received considerable attention in this context, as is evidenced in Kitagawa and Gersch (1996) and Kaiser and Maravall (2001).

In what follows, a statistical solution to the smoothing problem is proposed. Then, the focus is placed on the problem of selecting a λ value in such a way that it produces a percentage of smoothness for the trend specified beforehand. This result is specialized to the cases d = 0, 1 and 2, which are considered of outmost practical interest. Some numerical examples are shown to provide empirical evidence of the usefulness of the method proposed here.

## 2. A statistical solution

The minimization problem (2) is slightly more general than the usual problem considered in the literature because μ is not assumed to be zero beforehand. A solution to the problem for μ = 0 can be found in Kitagawa and Gersch (1996, p. 34) who approached it from a least squares computational perspective, while King and Rebelo (1993) employed optimal linear filtering tools to obtain essentially the same solution. In this paper, the problem is posed as the estimation of a random vector in order to develop a statistical solution and to derive an index of smoothness. Thus, let us consider the following tentative statistical model for {τ}, similar to that used by Hodrick and Prescott (1997) or Kitagawa and Gersch (1996), that is:

$$\nabla ^ { d } \tau _ { t } = \mu + \varepsilon _ { t } \quad \text {for } t = d + 1 , \dots , N ,$$

with {ε} a sequence of serially uncorrelated and identically distributed random errors with mean zero and Var(εt) = σ2

Now, let us define the following arrays: Z = (Z1, . . . , ZN)', τ = (τ1, . . . , τN)' and η = (η1, . . . , ηN)' are N × 1 vectors; ε = (εd+1, . . . , εN)' and 1N−d = (1, . . . , 1)' are (N − d) × 1 vectors and Kd is the matrix representation of the difference operator ∇a, so that

$$\left ( 0 \text { and else } \text {Operator} \, , & \, , \, \text {so that} \right ) \\ K _ { d } & \equiv \begin{pmatrix} 0 & \text {k} _ { d } & \text {0} \overset { \overset { \dots } { N } - d - 1 } { N } \\ & & \ddots & \ddots & \ddots \end{pmatrix} \\ & \quad 0 _ { N - d - 1 } \\ \cdot & \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \$$

is an (N − d) × N matrix, with kd the 1 × (d + 1) vector given by

and 0m the m × 1 zero vector. Thus, the vector of data Z can be expressed as

$$\text {is an } ( N - d ) \times N \text { matrix, with } \mathbf k _ { d } \text { the } 1 \times ( d + 1 ) \text { vector given by} \\ \mathbf k _ { d } = \left ( ( - 1 ) ^ { d } \binom { d } { d } , ( - 1 ) ^ { d - 1 } \binom { d } { d - 1 } , \dots , ( - 1 ) ^ { d } \binom { d } { 1 } , \binom { d } { 0 } \right ) \\ \text {and } 0 _ { \mathbf k } \text { the } m \times 1 \text { zero} \text { vector, thus, the vector of data } Z \text { can be expressed as}$$

$$Z = \tau + \eta , \sqrt { \gamma }$$

where the trend component is given, for μ known, by

$$K _ { d } \tau = \mu \mathbf 1 _ { N - d } + \varepsilon ,$$

E(ηε′) = 0, with V a known positive definite matrix.

The following result combines two sources of information in order to obtain an optimal linear predictor, in mean square error (MSE) sense, of a random vector.


<!-- p:4 -->


Lemma. Let us suppose that an unobservable random vector X is related to the observable vectors W and Y by means of

$$\mathbf X - E ( \mathbf X | \mathbf W ) = \gamma \quad \text {and} \quad \mathbf Y = C \mathbf X + \delta ,$$

where γ is a random vector corresponding to a stationary process, with E(γ|W) = 0 and E(γγ'|W) = P. C is a known full rank matrix and δ is another random vector coming from a stationary process with E(δ|W) = 0, E(δδ′|W) = R and E(γδ′|W) = 0. Then, the minimum MSE linear estimator (predictor) of X based on W and Y becomes

$$\hat { X } = E ( X | W ) + A [ Y - C E ( X | W ) ] .$$

Its corresponding MSE matrix Σ = Var( − X|W) is given by

$$\Sigma = P ( I - C ^ { \prime } A ^ { \prime } ) ,$$

where

$$A = P C ^ { \prime } ( C P C ^ { \prime } + R ) ^ { - 1 } .$$

Proof. The Law of Iterated Projections (see Sargent, 1979, p. 208) leads us to

E(X|W, Y) = E(X|W) + E[X − E(X|W)|Y − E(Y|W)].

Then, from (8) we get Y − E(Y|W) = (CX + δ) − CE(X|W) = Cγ + δ and E[X − E(X|W)|Y − E(Y|W)] = E(y|Cγ + δ). Since we are looking for a linear estimator, the last expectation must be of the form E(γ|Cγ + δ) = A(Cγ + δ), with A a constant matrix. Moreover, to minimize the length of γ − A(Cγ + δ), the following orthogonality condition must hold E{(Cγ + δ)[γ' − (γ'C' + δ)A′]|W} = 0 and this yields (11). Therefore, given W and Y we get (9), while (10) follows from

$$\hat { X } - X = [ E ( X | W ) + A ( C \gamma + \delta ) ] - [ E ( X | W ) + \delta ] = \begin{pmatrix} A C \end{pmatrix} - I ) \gamma + A \delta .$$

Hence, given W and Y,

$$Var ( \hat { X } - X | W , Y ) & = ( A C - I ) P ( C ^ { \prime } A ^ { \prime } - I ) + \widehat { A } R A ^ { \prime } \\ & = P - A C P - P C ^ { \prime } A ^ { \prime } + \underbrace { ( A C P C ^ { \prime } A ^ { \prime } + A R A ^ { \prime } } \\ & = P ( I - C ^ { \prime } A ^ { \prime } ) ,$$

where the last equality holds because ACP = PC' A' = A(CPC' + R)A'. □

Since E(τ|Z) = Z, an application of the lemma with X = τ, W = Z, γ = −η, Y = μ1N−d, C = Kd, δ = ε, P = σ2 V and R = σ2I N-d produces the following result.

Proposition 1. The minimum MSÉ linear estimator (predictor) of the trend τ is

$$\hat { \tau } = ( V ^ { - 1 } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } ( V ^ { - 1 } \widehat { Z } + \lambda \mu K _ { d } ^ { \prime } \mathbf 1 _ { N - d } ) ,$$

with MSE matrix

$$\Sigma = \sigma _ { \eta } ^ { 2 } ( V ^ { - 1 } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } .$$

Proof. From (9) and (10) we get τ = Z + A(μ1N−d − KdZ), whose MSE matrix is Σ = σ2(IN − AKd)V, where A = σ2 VK'(σ2KdVK'd + σ2IN−d)−1. These results can be expressed in a more familiar form within the time series smoothing framework,

$$\ s i n s \sinh & \frac { \ } { \ } \ln ( \sum \lim i t s _ { K } ^ { 2 } ( \sqrt { \sigma _ { \eta } } V - \sigma _ { \eta } ^ { 2 } V K _ { d } ^ { \prime } ( \sigma _ { \eta } ^ { 2 } K _ { d } V K _ { d } ^ { \prime } + \sigma _ { \eta } ^ { 2 } I _ { N - d } ) ^ { - 1 } K _ { d } V \sigma _ { \eta } ^ { 2 } \\ & \sum = \sigma _ { \eta } ^ { 2 } V - \sigma _ { \eta } ^ { 2 } V K _ { d } ^ { \prime } ( \sigma _ { \eta } ^ { 2 } K _ { d } V K _ { d } ^ { \prime } + \sigma _ { \eta } ^ { 2 } I _ { N - d } ) ^ { - 1 } K _ { d } V \sigma _ { \eta } ^ { 2 } \\ & = ( \sigma _ { \eta } ^ { - 2 } V ^ { - 1 } + \sigma _ { \varepsilon } ^ { - 2 } K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 }$$

$$\hat { \tau } & = ( \sigma _ { \eta } ^ { - 2 } \Sigma V ^ { - 1 } Z + \sigma _ { \varepsilon } ^ { - 2 } \mu \Sigma K _ { d } ^ { \prime } 1 _ { N - d } ) ^ { - 1 } \\ & = ( \sigma _ { \eta } ^ { - 2 } V ^ { - 1 } + \sigma _ { \varepsilon } ^ { - 2 } K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } ( \sigma _ { \eta } ^ { - 2 } V ^ { - 1 } Z + \sigma _ { \eta } ^ { - 2 }$$

and Furthermore, since the smoothing parameter is defined as λ = σ2/σ2, the last two expressions become (13) and (12). □


<!-- p:5 -->


Remarks. (i) The lemma allows us to estimate a random vector coming from a nonstationary time series process. In fact, the first equation of (8) is valid both for stationary and nonstationary processes, as it was shown by Bell (1984). The second equation of (8) is valid only if the processes corresponding to Y and CX are ets      s   o o    as  sccal point of view in order to apply Proposition 1 appropriately, because Y = μ1N-d being a constant vector implies that CX = Kaτ must correspond to a stationary process {∇a τt}. Hence, d must be chosen accordingly.

(ii) In a less formal way, the estimator ê can also be obtained from

$$\begin{pmatrix} Z \\ \mu _ { N - d } \end{pmatrix} = \begin{pmatrix} H _ { N } \\ K _ { d } \end{pmatrix} \tau + \begin{pmatrix} \eta \\ - \varepsilon \end{pmatrix} ,$$

with

$$E \left ( \begin{matrix} \eta \\ - \varepsilon \end{matrix} \right ) = 0 _ { 2 N - d } \quad \text {and} \quad \text {Var} \left ( \begin{matrix} \eta \\ - \varepsilon \end{matrix} \right ) = \left ( \begin{matrix} \sigma _ { \eta } ^ { 2 } V & 0 \\ 0 & \sigma _ { \varepsilon } ^ { 2 } I _ { N - d } \end{matrix} \right ) ,$$

in which case generalized least squares (GLS) produces (12) and (13). Thus, the intuitive interpretation of GLS carries over to the results provided by Proposition 1.

(iii) Expression (12) is clearly a generalization of existing work. If we let μ = 0, then appropriate specification of the matrix V allows the proposed model to take into account heteroskedasticity and autocorrelation of the observed series. For instance, Reeves et al. (2000) consider a diagonal matrix V with nonconstant variances σ2, for t = 1, . . . , N. Then, the resulting estimated trend corresponds to a time-varying smoothing parameter λ. The matrix V could also be used to account for the presence of cycles in the observed series by considering an appropriate autocorrelation structure (e.g. a moving average model of finite order or an auto-regressive model of order p≥2). However, in practice it is customary to make V = IN and that is the case considered below. Even in such a case, by letting d be a nonnegative integer we have as special cases of (12) the well-known exponential smoothing (d = 1) and Hodrick–Prescott (d = 2) filters, studied by King and Rebelo (1993).

(iv) When d≥1, the vector K'1N–d is zero except for its first d and last d elements. This follows because ∑i=0(−1)i(d) = 0, so that

$$K _ { d } ^ { \prime } 1 _ { N - d } = \left ( \sum _ { i = d } ^ { d } ( - 1 ) ^ { i } \binom { d } { i } , \dots , \sum _ { i = 1 } ^ { d } ( - 1 ) ^ { i } \binom { d } { i } , 0 , \dots , 0 , \sum _ { i = 0 } ^ { d - 1 } ( - 1 ) ^ { i } \binom { d } { i } , \dots , \sum _ { i = 0 } ^ { 0 } ( - 1 ) ^ { i } \binom { d } { i } \right ) ^ { ^ { \prime } } .$$

Therefore, the observed values of {Zt} enter the formula of the estimator ê modified in both of its extremes by the mean value μ weighted by λ. On the other hand, if d = 0 the estimator becomes λ = αZ + (1 — α)μ1N, with α = (1 + λ)−1.

(v) The effect of the mean should be kept in mind when extrapolating the trend, since μ≠0 implies the trend o oe  -  l  o  e  =  e  op  ool  oe extrapolated values will depend critically on the last d estimated trend values. That is, if we call îN(h) the h-period ahead forecast of τN+h, with origin at N, then for h≥ 1we get τN(h) = μ if d = 0, τN(h) = hμ + τN if d = 1 and τN(h) = [h(h + 1)/2]μ + (h + 1)τN − hτN−1 if d = 2.

A feasible trend estimator must take into account the fact that μ is commonly unknown and therefore it has to be estimated from the very data. Thus, an unbiased estimator of μ is given by the sample mean of {∇a Zt}, that is,

$$\hat { \mu } = ( N - d ) ^ { - 1 } \mathring { I } _ { N - d } K _ { d } Z .$$

So, expression (12) becomes

$$\hat { \tau } = ( I _ { N } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } [ I _ { N } + \lambda ( N - d ) ^ { - 1 } K _ { d } ^ { \prime } \mathbf 1 _ { N - d } \mathbf 1 _ { N - d } ^ { \prime } K _ { d } ] Z .$$


<!-- p:6 -->


Further, in order to measure variability around the estimated series {î} we need to estimate Σ in (13), which This estimator is provided by the following result.

is given by

$$\tilde { \sigma } _ { \eta } ^ { 2 } = [ Z ^ { \prime } Z - \hat { \tau } ^ { \prime } ( I _ { N } + \lambda K _ { d } ^ { \prime } K _ { d } ) \hat { \tau } ] / ( N - d ) + \lambda \mu ^ { 2 } .$$

Proof. The result follows by writing

$$V a r \left ( \begin{matrix} \eta \\ - \varepsilon \end{matrix} \right ) = \sigma _ { \eta } ^ { 2 } \left ( \begin{matrix} I _ { N } & 0 \\ 0 & \lambda ^ { - 1 } I _ { N - d } \end{matrix} \right ) = \sigma$$

and defining the residual vector as

$$e ^ { * } = \left ( \begin{matrix} \hat { \eta } \\ - \hat { \varepsilon } \end{matrix} \right ) = \left ( \begin{matrix} Z \\ \mu _ { N - d } \end{matrix} \right ) - \left ( \begin{matrix} I _ { N } \\ K _ { d } \end{matrix} \right ) \hat { \tau }$$

with η = Z − τ and δ = Kdτ − μ1N−d. Then, we get

$$e ^ { * } = ( I _ { 2 N - d } - M ) \left ( \begin{matrix} \eta \\ - \varepsilon \end{matrix} \right ) ,$$

where the matrix M is given by

$$M = \left ( \begin{array} { c } I _ { N } \\ K _ { d } \end{array} \right ) ( I _ { N } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } ( I _ { N } \lambda K _ { d } ^ { \prime } ) .$$

onal

This is an idempotent matrix with trace tr(M) = N. Therefore, the sum of squared residuals is given by

$$e ^ { * ^ { \prime } } \Omega ^ { - 1 } e ^ { * } = \hat { \eta } ^ { \prime } \hat { \eta } + \lambda \hat { \varepsilon } ^ { \prime } \hat { \varepsilon } = Z ^ { \prime } Z - \hat { \tau } ^ { \prime } ( I _ { N } + \lambda K _ { d } ^ { \prime } K _ { d } ) \hat { \tau } + ( \hat { N } - d ) \lambda \mu ^ { 2 } .$$

Hence, an unbiased estimator of σ2 becomes (19).

Remark. By wrongly assuming μ = 0, not only the endpoints of the estimator î will be affected, but also the variance σ2 will be underestimated by an amount that grows as λμ2.

It should be stressed that the estimator 2 was obtained on the assumption that μ was a known parameter, while in fact it has to be estimated. Thus, when using β in place of μ, it makes sense to correct (19) for this fact. = (N − d)2/(N − d − 1), that is,

$$\hat { \sigma } _ { \eta } ^ { 2 } = \left [ \sum _ { \iota = 1 } ^ { N } ( Z _ { \iota } - \hat { \tau } _ { \iota } ) ^ { 2 } + \lambda \sum _ { \iota = d + 1 } ^ { N } ( \hat { \nabla } ^ { d } \hat { \tau } _ { \iota } \hat { = } \hat { \mu } ) ^ { 2 } \right ] / ( N - d - 1 ) .$$

## 3. A measure of smoothness

The precision matrix of ê is defined as

$$\sum ^ { - 1 } = \sigma _ { \eta } ^ { - 2 } I _ { N } + \sigma _ { \bar { x } } ^ { 2 } K _ { \bar { d } } ^ { \prime } \hat { K } _ { d } .$$

This matrix is composed by two precision matrices, σ−2IN associated with model (6) for the observations and (0)   oo   o  s    s t oo ( o  o  1 we can measure the precision contributed by the smooth component to the total precision. Such a measure was originally derived by Theil (1963) to quantify the proportion of a matrix P in (P + Q)−1, where P and Q are N × N positive definite matrices. Theil's measure is

$$\Lambda ( P ; P + Q ) = \text {tr} [ P ( P + Q ) ^ { - 1 } ] / N .$$

This measure of relative precision has the following properties: (i) it lies in the interval [0, 1]; (ii) it is invariant under linear non-singular transformations of the variable involved; (iii) it behaves linearly and (iv) ∆(P; P + Q) + ∆(Q; P + Q) = 1.


<!-- p:7 -->


Table 1 Values of λ for selected values of d and Sd(λ, N), with N = 100

|   Difference - d |   S d ð l ; N Þ - 0.5 |   S d ð l ; N Þ - 0.6 |   S d ð l ; N Þ - 0.7 |   S d ð l ; N Þ - 0.8 |   S d ð l ; N Þ - 0.9 |
|------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|                0 |                 1.000 |                 1.500 |                 2.333 |                 4.000 |                 9.000 |
|                1 |                 0.765 |                 1.346 |                 2.614 |                 6.312 |                27.420 |
|                2 |                 0.427 |                 0.970 |                 2.812 |                13.506 |               244.872 |

The proposal is to use (22) to measure the proportion of precision induced by the smoothness component. The corresponding smoothness index is given by

$$S _ { d } ( \lambda , N ) = \Lambda ( \sigma _ { \varepsilon } ^ { - 2 } K _ { d } ^ { \prime } K _ { d } ; \Sigma ^ { - 1 } ) = \begin{cases} \lambda ( 1 + \lambda ) ^ { - 1 } & \text {if } d = 0 , \\ 1 - \text {tr} [ ( I _ { N } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } ] / N & \text {if } d \geqslant 1 . \end{cases}$$

It is clear that Sd(λ, N) → 0 as λ → 0 and Sd(λ, N) → 1 as λ → ∞. Then, we should specify the smoothness Sd(λ, N) and find the corresponding λ value for fixed values of N and d. If d = 0 we get λ = S0(λ, N)/[1 − S0(λ, N)] and if d≥1 we can use a nonlinear routine to solve (23) for λ, given N and d. For instance, when N = 100, the λ values corresponding to different smoothness indices are shown in Table 1.

## 4. Some illustrative examples

In this section, two examples are provided to shed some light into the proposed procedure and the results that can be obtained through its application in practice.

Example 1. Monthly mean temperature (°C) in December for a region of the State of Veracruz, Mexico. The region of reference is geographically located at —98 to —93 longitude and 17–22 latitude. A study of this kind of data is generally done to assess the potential impacts of climate change on human activities and natural systems. It is a common belief that the climate is changing and, therefore, it is reasonable to estimate trends of weather series (see, for instance, Jewson and Penzer, 2006). The data employed in this illustration cover the years 1901–1995 as shown in Table 2 and their study is important to assess the effect of climate change on coffee production.

A graph of the temperature series shows an underlying slow changing mean pattern (see Fig. 1) that indicates that the series may be stationary. An application of the augmented Dickey-Fuller (ADF) unit root test confirms the idea that d = 0. The estimated ADF regression employed was (standard errors in parenthesis)

$$\nabla Z _ { t } = 1 3 . 4 2 - 0 . 6 2 Z _ { t - 1 } \rightarrow 0 . 0 9 \nabla Z _ { t - 1 } - 0 . 0 2 \nabla Z _ { t - 2 } \\ ( 3 . 1 4 ) \ \widehat { ( 0 . 1 4 ) } \ \widehat { ( 0 . 1 3 ) } \quad ( 0 . 1 3 )$$

so that the statistic τμ = -4.26 leads to rejecting the null hypothesis of a unit root by comparing it with the asymptotic 1% critical point given by —3.43.

The results of applying the smoothing procedure are shown in Figs. 1 and 2. We see that the smoother the trend, the smaller the uncertainty around it. Thus, as the degree of smoothness increases, less data points are included within the two-standard error limits.

Example 2. Smoothing and trend forecasting of Mexico's real gross domestic product (GDP). Quarterly data on seasonally adjusted GDP from 1980:1 to 2006:2 were obtained from the website of the National Institute of Statistics, Geography and Informatics (INEGI, www.inegi.gob.mx). Table 3 shows the data for all quarters (Q1, . . . , Q4) from 1980:1 up to 2005:4 employed for smoothing, the remaining two data points will be used to check the validity of the forecasts.


<!-- p:8 -->


Table 2 Mean temperature of December in a region of the State of Veracruz, Mexico

| Years     |   Temperature in  C |   Temperature in  C |   Temperature in  C |   Temperature in  C |   Temperature in  C |   Temperature in  C |   Temperature in  C |   Temperature in  C |   Temperature in  C |   Temperature in  C |
|-----------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|
| 1901-1910 |                21.68 |                21.12 |                19.96 |                20.00 |                19.66 |                20.52 |                20.98 |                21.54 |                21.72 |                20.16 |
| 1911-1920 |                21.76 |                21.60 |                21.38 |                22.32 |                22.40 |                22.68 |                20.76 |                21.38 |                21.70 |                22.48 |
| 1921-1930 |                21.94 |                21.80 |                22.04 |                21.78 |                20.72 |                22.54 |                22.24 |                21.44 |                21.18 |                20.96 |
| 1931-1940 |                22.66 |                22.26 |                21.92 |                22.16 |                21.54 |                21.44 |                21.62 |                20.64 |                22.14 |                22.24 |
| 1941-1950 |                23.10 |                22.48 |                21.04 |                20.50 |                21.84 |                21.84 |                20.94 |                22.52 |                21.82 |                20.44 |
| 1951-1960 |                22.86 |                22.54 |                22.90 |                22.10 |                22.80 |                23.04 |                22.26 |                22.54 |                22.26 |                20.86 |
| 1961-1970 |                22.36 |                21.72 |                20.24 |                21.92 |                21.22 |                20.62 |                22.30 |                21.48 |                21.74 |                22.48 |
| 1971-1980 |                23.48 |                21.92 |                20.52 |                22.02 |                20.92 |                20.36 |                22.14 |                22.40 |                21.40 |                20.48 |
| 1981-1990 |                22.14 |                22.02 |                21.92 |                22.66 |                21.86 |                21.58 |                22.32 |                21.82 |                19.60 |                21.58 |
| 1991-1995 |                22.08 |                23.20 |                22.08 |                22.70 |                22.26 |                      |                      |                      |                      |                      |

Source: IPCC Data Distribution Center, http://ipcc-ddc.cru.uea.ac.uk/java/time\_series.html.

Fig. 1. Observed temperature, trend with 60% smoothness and two-standard error limits.

23.5

23.0

22.5

22.0

21.5

21.0

20.5

20.0

19.5

191191111111119899

DATA

TREND

LIMINF

LIMSUP

Fig. 2. Observed temperature, trend with 90% smoothness and two-standard error limits.

23.5

23.0

22.5

22.0

21.5

21.0

20.5

20.0

19.5

191191991911119111989

DATA

TREND

LIMINF

LIMSUP


<!-- p:9 -->


Table 3 Mexico's seasonally adjusted real GDP (millions of pesos at constant prices of 1993)

|   Year |        Q1 |        Q2 |        Q3 |        Q4 |   Year |        Q1 | Q2             |        Q3 |        Q4 |
|--------|-----------|-----------|-----------|-----------|--------|-----------|----------------|-----------|-----------|
|   1980 |   927,175 |   933,282 |   953,408 |   981,005 |   1993 | 1,248,397 | 1,243,247      | 1,263,081 | 1,269,349 |
|   1981 | 1,002,873 | 1,028,945 | 1,034,287 | 1,052,803 |   1994 | 1,285,127 | 1,307,914      | 1,320,085 | 1,334,517 |
|   1982 | 1,032,472 | 1,034,157 | 1,026,666 | 1,004,127 |   1995 | 1,271,536 | 1,197,052      | 1,212,502 | 1,240,097 |
|   1983 |   996,799 |   976,591 |   984,778 |   996,096 |   1996 | 1,272,751 | 1,276,343      | 1,296,591 | 1,328,347 |
|   1984 | 1,023,495 | 1,008,657 | 1,032,948 | 1,023,840 |   1997 | 1,348,818 | 1,367,810      | 1,389,749 | 1,417,996 |
|   1985 | 1,042,443 | 1,041,846 | 1,048,176 | 1,045,330 |   1998 | 1,434,459 | 1,445,439      | 1,458,317 | 1,458,454 |
|   1986 | 1,025,365 | 1,021,222 | 1,001,958 |   999,218 |   1999 | 1,472,412 | 1,491,061      | 1,518,099 | 1,538,944 |
|   1987 | 1,005,031 | 1,032,919 | 1,033,814 | 1,046,291 |   2000 | 1,579,909 | 1,604,483      | 1,621,328 | 1,613,068 |
|   1988 | 1,039,207 | 1,035,951 | 1,037,192 | 1,057,847 |   2001 | 1,613,188 | 1,605,815      | 1,598,076 | 1,591,576 |
|   1989 | 1,077,778 | 1,077,952 | 1,098,202 | 1,088,509 |   2002 | 1,597,918 | 1,615,749      | 1,624,288 | 1,622,711 |
|   1990 | 1,111,879 | 1,136,521 | 1,151,835 | 1,166,461 |   2003 | 1,616,953 | 1,634,614      | 1,640,865 | 1,655,974 |
|   1991 | 1,169,716 | 1,187,390 | 1,189,810 | 1,211,274 |   2004 | 1,676,417 | copy 1,696,390 | 1,713,939 | 1,735,402 |
|   1992 | 1,210,803 | 1,231,241 | 1,242,485 | 1,243,492 |   2005 | 1,738,030 | 1,732,358      | 1,771,762 | 1,781,799 |

Fig. 3. Mexico's GDP (in logs), trend with 60% smoothness and two-standard error limits.

14.4

14.3

14.2

14.1

14.0

13.9

13.8

ersonal

13.7

19 119111111804

— DATA — TREND

LIMINF— LIMSUP

In order to perform business cycle a analysis, GDP data are usually logged before applying the Hodrick-Prescott filter, which amounts to choosing d = 2 on a priori grounds. The logarithmic transformation was also applied here, but a unit root test was used to select the value of d empirically. The ADF regression model for Zt = log(GDPt) became in this case

$$\nabla ^ { 2 } Z _ { t } = 0 . 0 0 5 - 0 . 7 9 8 \nabla Z _ { t - 1 } + 0 . 0 6 6 \nabla ^ { 2 } Z _ { t - 1 } + 0 . 2 3 6 \nabla ^ { 2 } Z _ { t - 2 } \\ ( 0 . 0 0 2 ) \ \widehat { ( 0 . 1 3 2 ) } \ \widehat { ( 0 . 1 2 2 ) } \quad ( 0 . 0 9 9 ) .$$

Since the ADF test statistic took on the value τμ = —6.05 we were led to reject the unit root hypothesis at the 1% significant level (the corresponding critical value is —3.43). Therefore, the value d = 1 was used in the smoothing procedure. The smoothing constant corresponding to N = 104 for a trend with 60% percentage of smoothness became λ = 1.31 and the estimated value ôn = 0.0119 was used to calculate two-standard error limits around the estimated trend shown in Fig. 3.

We can get forecasts of the trend by using the estimated mean of the series {∇log(GDPt)} and the last estimated trend value, that is, ρ = 0.0063 and τ2005:4 = 14.3818. Thus, trend forecasts for quarters 2006:1 and 2J  1   4 = 2: +  = 2:  15 = 4: +  = (10:0  :t we apply the smoothing procedure to the whole sample (from 1980:1 to 2006:2) we get the following estimated trend figures with two-standard error intervals, for quarters 2005:4, 2006:1 and 2006:2, 14.3937 (14.3786, 14.4089), 14.4034 (14.3878, 14.4190) and 14.4086 (14.3906, 14.4266). In all three cases, these intervals cover the


<!-- p:10 -->


14.4

Fig. 4. Mexico's GDP (in logs), trend with d = 2, 60% smoothness and two-standard error limits.

14.3

14.2

14.1

14.0

13.9

13.8

13.7

1980 1982 1984 1986 1988 19901992 1994 1996 1998 2000 2002 2004

DATA — TREND

-LIMINF LIMSUP

previously estimated trend values. The trend estimates and forecasts in the original scale can be obtained by exponentiating the forecasts of the series in logs. In case we want to interpret the resulting forecasts as expected values, an adjustment should be applied to correct for bias introduced by this retransformation, as indicated in Guerrero (1993). Otherwise, if no adjustment is applied the forecasts are still valid, but they should be interpreted as estimated median values.

If we use d = 2, the smoothing constant for 60% of smoothness becomes λ = 0.96, and we get ôn = 0.0077. The corresponding graph is shown in Fig. 4. Trend forecasts can be obtained by using the estimated mean of the series {∇2 1og(GDPt)}, ρ = −9 × 10−6, as well as the two most recent estimated trend values, τ2005:3 = 14.3832 and τ2005:4 = 14.3931. Trend forecasts for 2006:1 and 2006:2 are τ2005:4(1) = ρ + 2τ2005:4 − τ2005:3 = 14.4030 and τ2005:4(2) = 3ρ + 3τ2005:4 − 2τ2005:3 = 14.4129.

In this illustration it is clear that the choice of d is crucial for trend estimation and forecasting. When d = 1, the results are conservative both in terms of variability and estimated trend values (particularly at the extremes of the series). On the contrary, if d = 2, the estimated trend is more volatile and the forecasts of future trend values become more adaptive. Thus, the degree of smoothness is not comparable for different values of d. Therefore we should select d in an objective (preferably data-based) way. Even if the values of d and λ have been established by the standard application of the smoothing method (e.g. the Hodrick–Prescott filter for quarterly series uses d = 2 and λ = 1600), we should be aware that the smoothness achieved varies according to the sample size. For instance, the smoothness achieved by applying the filter to the GDP data with N = 104, d = 2 and λ = 1600 is about 93%, whereas λ = 1600 produces only 88% of smoothness when N = 20 and d = 2.

## 5. Concluding remarks

The basic proposal of this work is to select the percentage of smoothness at the outset, instead of the smoothing constant. It is argued that the results obtained with the same degree of smoothness will be more comparable for different series or for the same series with different lengths. If we approach the time series smoothing problem from the standpoint suggested here, including the mean of the series in differences, we can get results that are not only justified from a computational perspective, but they are also well grounded in statistical theory. The basic theoretical results here derived provide an elementary justification of the proposed procedure, but more inferential tools are still required, perhaps based on classical normal distribution theory (e.g. to test whether μ = 0 is a valid assumption).

##### Acknowledgements

The author is grateful to Asociación Mexicana de Cultura, A.C. for providing financial support to carry out this work through a Professorship on Time Series Analysis and Forecasting in Econometrics. He also thanks José L. Farah and an anonymous referee for providing useful comments on a previous version of this paper.


<!-- p:11 -->
