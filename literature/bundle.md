

<!-- BEGIN SOURCE 18/40: Guerrero_2007_time-series-smoothing-penalized-least-squares.md -->

# Source: `Guerrero_2007_time-series-smoothing-penalized-least-squares.md`

---
id: "Guerrero_2007_time-series-smoothing-penalized-least-squares"
source_pdf: "../pdf/Guerrero_2007_time-series-smoothing-penalized-least-squares.pdf"
source_filename: "Guerrero_2007_time-series-smoothing-penalized-least-squares.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/Guerrero_2007_time-series-smoothing-penalized-least-squares.references.md"
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

<!-- END SOURCE 18/40: Guerrero_2007_time-series-smoothing-penalized-least-squares.md -->

---

<!-- BEGIN SOURCE 19/40: Guerrero_2008_estimating-trends-percentage-smoothness.md -->

# Source: `Guerrero_2008_estimating-trends-percentage-smoothness.md`

---
id: "Guerrero_2008_estimating-trends-percentage-smoothness"
source_pdf: "../pdf/Guerrero_2008_estimating-trends-percentage-smoothness.pdf"
source_filename: "Guerrero_2008_estimating-trends-percentage-smoothness.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/Guerrero_2008_estimating-trends-percentage-smoothness.references.md"
---

<!-- p:1 -->

## ESTIMATING TRENDS WITH PERCENTAGE OF SMOOTHNESS CHOSEN BY THE USER

por

#### Víctor M. Guerrero1

###### DE-C05.5

1 Department of Statistics, Instituto Tecnológico Autónomo de México (ITAM) and Research Coordination,

National Institute of Statistics Geography and Informatics (INEGI)


<!-- p:2 -->


## Estimating Trends With Percentage of Smoothness Chosen by the User

#### Victor M. Guerrero

Department of Statistics, Instituto Tecnológico Autónomo de México -ITAM (guerrero@itam.mx) and Research Coordination, National Institute of Statistics, Geography and Informatics (INEGI)

This work presents a method for estimating trends of economic time series that allows the user to fix at the outset the desired percentage of smoothness for the trend. The calculations are based on the Hodrick and Prescott filter usually employed in business cycle analysis. The situation considered here is not related to that kind of analysis, but with describing the dynamic behavior of the series by way of a smooth curve. To apply the filter, the user requires to specify a smoothing constant that determines the dynamic behavior of the trend. A new method that formalizes the concept of trend smoothness is proposed here to choose that constant. Smoothness of the trend is measured in percentage terms with the aid of an index related to the underlying statistical model of the filter. Some empirical illustrations are provided using data on the Mexican economy with different frequencies of observation.

KEY WORDS: Hodrick and Prescott filter; Kalman filter; Relative precision; Smooth curve; Time series models.

1. INTRODUCTION

The concept of trend arises naturally when carrying out statistical or econometric analysis of economic time series. A reason for this is that the trend of a time series plays a descriptive role equivalent to that of a centrality measure of a data set, but the center of a time series behaves dynamically. Another reason is that very often the analyst wants to distinguish between short-term and long-term movements. In fact, the common notion of trend is that of an underlying component of the observed series that reflects its long-term behavior and evolves smoothly (see Maravall, 1993). Therefore, when dealing with trends it is natural to use the following unobserved component representation


<!-- p:3 -->


$$y _ { t } = \tau _ { t } + \eta _ { t } \quad \text {for} \ \ t = 1 , \dots , N ,$$

with yt the observed value of the series under study at time t, τ its trend component and ηt its complement, called the noise component. This representation does not necessarily indicate how the actual data were generated, but is a way to present the stylized facts referred to by the analysts and frequently observed by just plotting the data. The trend behavior can be represented through deterministic or stochastic models although, as Nelson and Kang (1981) showed, deterministic models tend to produce spurious results. Therefore, stochastic models are preferable.

The need of estimating a trend may arise just for informative purposes. In that case, a simple graphical display of the data is useful to show the relevant patterns of the series, such as its trend. This idea is not new (see e.g. Deville and Malinvaud, 1983) and it has led, for instance, to present economic time series data adjusted for seasonality in a routinely manner. On the other hand, there is the need of eliminating the trend without affecting other components of the series, such as seasonality, cycles, etc. This need occurs when the analyst plans to carry out subsequent analyses on the detrended series. Some of those analyses typically include turning point forecasting and business cycle explanation. This paper is concerned with estimating trends for several series in a routinely manner and just for informative purposes, so that an easy-to-use method must be applied.

This article is organized as follows. Section 2 presents the most common approaches employed up to date to represent trends of economic time series. Hodrick and Prescott's (HP) filter is emphasized because it is considered a reasonable approach for estimating trends. Since the HP filter depends heavily on a smoothing parameter, Section 3 describes several procedures devised for choosing that parameter. Section 4 presents a new method for selecting the smoothing constant with quarterly series, in such a way that a desired percentage of trend smoothness can be fixed at the outset. Section 5 extends the applicability of this method to non-quarterly series. Both in Sections 4 and 5, some illustrative applications on actual data are presented. Section 6 concludes with some remarks.

3


<!-- p:4 -->


### 2. TREND REPRESENTATION AND ESTIMATION

Maravall (1993) presented several approaches that lead to stochastic models generally used to represent trends of economic time series. They are based on: a) ARIMA (Auto-Regressive Integrated Moving Average) models; b) Structural Models, as those proposed by Harvey (1989); c) the X-11 Seasonal Adjustment procedure (Cleveland and Tiao, 1976); and d) the HP filter (see Hodrick and Prescott, 1997, originally appeared as a non-published manuscript in 1980). Those approaches yield similar model specifications in which the difference operator is applied twice to the trend component. The general difference operator and B is the backshift operator such that BXt = Xt-1 for every variable X and subindex t. The parameters θ1 and θ2 are constant and {at} is a white noise Gaussian process, i.e. it is a sequence of independent and identically distributed random errors with Normal distribution.

A filter is defined here by any operation on the observed series {yt} that yields another series, which in the present case will be the estimated trend {τt } . Since τt is a random variable it would be preferable to call t its predictor rather than its estimator, nevertheless the usual terminology that refers to estimation instead of prediction, will be employed here. The approach to be used for estimating trends will be that of the HP filter, mainly because it does not require the application of a formal statistical model building process before estimating the trend, as it happens with the ARIMA and the Structural model-based approaches. Besides, the HP filter is easier to apply than a seasonal adjustment procedure and produces results that are equivalent to those obtained with any of the following three methods: (1) smoothing by Penalized Least Squares, (2) Kalman filtering with smoothing and (3) signal extraction via the Wiener – Kolmogorov filter. This fact has been shown by Gómez (1999), and by Young and Pedregal (1999). Knowing this result is useful to take advantage of the respective merits of each individual method. The monograph by Kaiser and Maravall (2001) exposes in detail the HP filtering methodology within the context of business cycle analysis.


<!-- p:5 -->


The penalized approach that gives rise to the HP filter postulates that the trend must minimize the function

$$M ( \lambda ) = \sum _ { t } ^ { N } ( y _ { t } - \tau _ { t } ) ^ { 2 } + \lambda \sum _ { t } ^ { N } ( \nabla ^ { 2 } \tau _ { t } ) ^ { 2 }$$

where λ &gt; 0 is a constant that penalizes the lack of smoothness in the trend. By writing F Σt 1(yt − τt)2 and S Σt 3(∇2τt)2 it can be seen that as λ → 0, the fit (F) of the trend to the data is emphasized over its smoothness (S), so that τt → yt . The opposite occurs when λ → ∞ , in which case the trend follows essentially the straight line model ∇2τ 0. Hence λ plays a very important role in deciding the smoothness of the trend.

This method was proposed by Whittaker and Henderson in 1924 for graduating actuarial data, although an earlier application was made in 1867 by the Italian astronomer Schiaparelli (see Hodrick and Prescott, 1997).

The minimization problem underlying the HP filter can be written in matrix notation as

$$\min _ { \tau } M ( \lambda ) \quad ( y - \tau ) ^ { \prime } ( y - \tau ) + \lambda ( K _ { 2 } \tau ) ^ { \prime } ( K _ { 2 } \tau ) \, ,$$

with y (y1, ., ,N)' and τ (τ1, ., ,N )', where K2 is the (N-2)×N matrix given by

$$K _ { 2 } = \begin{pmatrix} 1 & - 2 & 1 & 0 & 0 & \dots & 0 & 0 & 0 & 0 \\ 0 & 1 & - 2 & 1 & 0 & & 0 & 0 & 0 & 0 \\ & & & & & & & & & & \\ 0 & 0 & 0 & 0 & 0 & \dots & 0 & 1 & - 2 & 1 \end{pmatrix} .$$

The solution can be obtained by taking the derivative of M(λ) with respect to τ, equating to zero the derivative evaluated at τ î and solving the resulting equation. Thus we get

$$\hat { t } = \left ( I _ { N } + \lambda K _ { 2 } ^ { ^ { \prime } } K _ { 2 } \right ) ^ { - 1 } y \, .$$

Since the second derivative of M(λ) evaluated at τ ê is a symmetric positive definite matrix, it follows that (5) produces a minimum and therefore solves the problem. It should be noticed that in order to get ê, an N×N matrix has to be inverted. This calculation may cause instability and lack of precision of the numerical solution when N is large. Thus, the penalized approach has the advantage of showing explicitly the roles played by λ, F and S, but it does not provide an efficient calculation tool for the trend.


<!-- p:6 -->


The Kalman filter requires formulating a state space model as follows. The state and measurement equations are given by

$$\mathbf x _ { t } = A _ { t } \mathbf x _ { t - 1 } + \mathbf w _ { t } , \, \mathbf y _ { t } = \mathbf c _ { t } ^ { ^ { \prime } } \mathbf x _ { t } + \eta _ { t } ,$$

with

$$x _ { t } = \begin{pmatrix} \tau _ { t } \\ \sigma _ { \tau _ { t - 1 } } \end{pmatrix} , \ A _ { t } = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix} , \ \dot { c } _ { t } = ( 1 \ \ 0 ) \ \text { and } \ w _ { t } = \begin{pmatrix} \varepsilon _ { t } \\ 0 \end{pmatrix} ,$$

where ε and ηt are two independent zero-mean random errors, serially uncorrelated and identically distributed with Var(ε) σ 2ω and Var(nt) σ 2 η Thus the state equation implies using the model

$$\tau _ { t } = 2 \tau _ { t - 1 } - \tau _ { t - 2 } + \varepsilon _ { t } \, .$$

To equate the results of the Kalman filter with smoothing, with those obtained directly from (5) we should assume that σ 2 1 and σ 2 λ. The numerical calculations required ε η by the illustrative applications shown below were carried out with the RATS package Version 5 (see Doan, 2000).

The third equivalent method is known as the Wiener – Kolmogorov filter (see Whittle, 1983 for the stationary series case and Bell, 1984 for its extension to nonstationary series). This method also assumes that (1) holds and that the trend is linear. Then the estimated trend is given by the symmetric filter (see Young and Pedregal, 1999)

$$^ { 2 } \, ) / [ \sigma _ { \varepsilon } ^ { 2 } / \sigma _ { \eta } ^ { 2 } + ( 1 - B ) ^ { 2 } ( 1 - B ^ { - 1 } ) ^ { 2 } ] \} y _ { t } \, ,$$

where B-1 is such that B−1Xt Xt+1 for every variable X. The Wiener - Kolmogorov filter produces the estimator with minimum Mean Square Error (MSE) of {τ } if a complete realization (from t -∞ to t ∞) of the series {yt } is available. In any other case the result should be considered only from a theoretical perspective, because its use in practice would require truncation at the extremes.

Equivalence of the previous three methods enables us to interpret the HP filter as a method that yields a feasible trend estimator produced by the Wiener – Kolmogorov filter, so that it has minimum MSE. Besides, the spectral analysis theory underlying that filter is also applicable to the HP filter and such measures as function gain and phase can also be calculated with ease for the HP filter, as did Gómez (1999). There are some other alternative techniques for estimating or eliminating time series trends. For instance, e pt  e () t  ter for performing analysis of the economic situation and detecting turning points. Another technique is that of Beveridge and Nelson (1981) which allows an analyst to decompose a nonstationary time series into permanent and transitory components. This method is based on an ARIMA representation of the observed series and does not necessarily produce a smooth permanent component that may be considered an estimate of the trend.


<!-- p:7 -->


The method based on the eventual forecast function of an ARIMA model can also be considered useful to estimate a trend (see Box, Pierce and Newbold, 1987). This method only makes use of data previous to time t for estimating the trend at t and therefore behaves like a filter without smoothing and it does not produce an estimate of the trend at the beginning of the series. Baxter and King (1999) designed band-pass filters that can be calculated as moving averages and that are appropriate for extracting some kind of trends defined by the frequencies that the filter allows to pass, so this technique is useful for carrying out business cycle analysis. Boone and Hall (1999) proposed an extension of the HP filter based on a state space model whose state equation generalizes the linear model. This proposal is useful to get a better statistical representation of the series and its trend, but becomes impractical for massive and repetitive application. Finally, the technique proposed by Kitagawa and Gersch (1996) produces a trend estimator that is supported by a Bayesian statistical argument and is intimately related to the HP filter, in the sense that both employ essentially the same equations. There are also several detractors of the HP filter when it is used for business cycle analysis. Harvey and Jaeger (1993), as well as Cogley and Nason (1995) and Park (1996) are among them, because they found that the HP filter sometimes induce spurious cycles as those cited by Slutzky (1937). In contrast Pedersen (2001) argued that the main reason for getting spurious results is the very definition of a Slutzky effect employed and he showed that the HP filter, with an appropriate definition of the cycle, produces adequate results for business cycle analysis.

The main focus of this paper lies on estimating trends for descriptive purposes via smooth curves produced by the HP filter. As a motivating example, Figure 1 presents some plots that allow comparison of the estimated trend for the quarterly seasonally adjusted series of Mexico's Gross Domestic Product (GDP). The data employed appear in the Appendix. This figure allows us to appreciate the results of the HP filter as compared with those produced by the seasonal adjustment program X-12-ARIMA. Plot (a) shows the estimated trend that comes out of the X-12-ARIMA package with the automatic options. Plot (b) presents the trend produced by the HP filter with the traditional value λ=1600, and plots (c) and (d) show the trend obtained with λ=1 and λ=199. Smoothness of the trend is very similar in cases (a) and (c), but it is substantially different in the other cases. Thus, in order to estimate the trend appropriately we have to choose the constant λ in an objective way.


<!-- p:8 -->


Figure 1. Trend Estimation of Mexico's GDP Quarterly Series, at 1993 Prices, Seasonally Adjusted with the X-12-ARIMA package. Trend obtained with: (a) automatic options of X-12ARIMA, (b) HP filter with λ = 1600, (c) HP filter with λ = 1 and (d) HP filter with λ = 199.

(a)

(b)

1700000


1600000


1500000


1400000


1300000


1200000


1100000

110000

1000000

- Deseas. GDP

100000

- Deseas. GDP

-X-12-ARIMA

−λ. 1600

900000


1980-01

1982-01

1984-01

1986-01

1988-01

1990-01

1992-01

1994-01

1996-01

1998-01

2000-01

2002-01

2004-01

1980-01

1982-01

1984-01

1986-01

1988-01

1990-01

1992-01

1994-01

1996-01

1998-01

2000-01

2002-01

2004-01

(c)

(d)

1700000


1600000


1500000


1400000


1300000


1200000


110000

1100000

1000000

- Deseas. GDP

1000000

- Deseas. GDP

-λ 199

900000


1980-01

1982-01

1984-01

1986-01

1988-01

1990-01

1992-01

1994-01

1996-01

1998-01

2000-01

2002-01

2004-01

1980-01

1982-01

1984-01

1986-01

1988-01

1990-01

1992-01

1994-01

1996-01

1998-01

2000-01

2002-01

2004-01


<!-- p:9 -->


In closing this section, we should bear in mind that the trend component of an economic time series requires the use of ∇2 , not of ∇d for d ≥ 1 in general, as one could think in order to make the trend specification more flexible. In particular using d=1 in a minimization problem of the function (2), gives rise to the Exponential Smoothing filter cited by King and Rebelo (1993). The HP filter is one of those filters that employ ∇2 ; its original derivation as a Penalized Least Squares problem makes explicit the trade off between smoothness and fit when estimating the trend; it can be interpreted as an optimal statistical estimation method, in MSE sense; it may be calculated efficiently by means of Kalman filtering with smoothing; it has adequate properties in terms of spectral analysis; and to be able to apply it in practice we only require to fix the value of the smoothing parameter λ.

### 3. CHOOSING THE SMOOTHING CONSTANT

In order to select the value of λ, Hodrick and Prescott (1997) tentatively assumed that ∇2τ and ηt were independent random variables identically distributed as N(0,σ2) and N(0,σ2), respectively. A usual application of the HP filter for business cycle analysis presumes that the observed series is expressed in logarithms, in which case Vyt can be interpreted as a growth rate. Therefore the change in the growth rate of the trend and the noise are supposed to be Gaussian white noise processes. In their original work, Hodrick and Prescott decided a priori that the values σn 5 and σε 1/8 were appropriate for the quarterly macroeconomic US series they were studying (for the period 1950 – 1979). Therefore, they decided to use λ σ2 1600. They also carried out a sensitivity ε analysis of their results with λ=400, λ=6400 and λ=∞. They concluded that only with λ=∞ the results changed in an important way, while the other two values produced basically the same measures of empirical regularity. Thus, λ=1600 became the traditional value for the smoothing constant when using the HP filter.

The HP filter keeps a strong resemblance with the cubic splines employed, for instance, in nonparametric regression. There, the trend depends on some independent variables, x1,.., xp , and it is given by τ(x1..,.x) (IN + λX)-1 y where X is a matrixx that depends on the x's. Thus, it is natural to think that the methods employed within the context of splines for choosing the smoothing constant, may also work for the HP filter. Lee (2003) compared the performance of several methods for selecting λ through Monte Carlo simulation and, for the purposes of the present work, it is important to notice the following aspects of such methods: their computational complexity; their lack of interpretation for the numerical value of λ; that they do not take into account the order of the data explicitly; and that, when there is a temporal ordering in the data, it does not correspond to a discrete and equally spaced ordering of the successive observations. For these reasons, such methods are not considered adequate to estimate trends of economic time series routinely and massively.


<!-- p:10 -->


A formal statistical approach must consider postulating a model, estimating its parameters (one of which is λ) and verifying that the underlying assumptions are not seriously violated. That is what Harvey and Jaeger (1993) proposed to do with a Structural time series model and using Maximum Likelihood estimation. Again, this procedure does not lend itself to massive applications. A more realistic approach is that of Kitagawa and Gersch (1996, chapter 4) who proposed to use model (1) with (8) and estimate λ by Maximum Likelihood. They admitted explicitly that the assumption ∇2τ ε is incorrect because the true trend function is unknown, but they also reminded us that this is the same argument employed by Shiller in 1973, when he proposed what is known as the smoothness prior approach.

The approach adopted by Young (1994), Pedersen (2001) and Kaiser and Maravall (2001) to select an appropriate value of the smoothing constant is based on the interpretation of the results produced by different choices of λ. They considered the effects of λ in the frequency domain and suggested criteria for choosing it appropriately, in the sense of allowing the HP filter to eliminate cycles whose periodicity is less than some value considered adequate for carrying out business cycle analysis. In particular, Kaiser and Maravall (2001, chapter 7) proposed to choose λ by fixing the length of the period over which the analyst wishes to measure cyclical activity. Thus for quarterly series they provided a table (Table 5.11) where the period in years is related to an approximate value of λ.


<!-- p:11 -->


and

### 4. CHOOSING λ TO ACHIEVE SOME DESIRED SMOOTHNESS

The method proposed here arises from an explicit statistical model which is employed in a tentative manner to arrive at expression (5), as in Hodrick and Prescott (1997) or Kitagawa and Gersch (1996). Thus, even though the assumptions may be empirically invalid, they are required for deriving the theoretical results. Thus let us suppose tentatively that (1) and (8) hold valid, with {nt } and {εt } mutually uncorrelated zero-mean white noises, with variances σ 2 and σ 2 Then it follows that η

$$y = \tau + \eta \text { with } E ( \eta ) = 0 \text { and } V a r ( \eta ) = \sigma _ { \eta } ^ { 2 } I _ { N }$$

$$K _ { 2 } \tau \ \varepsilon \ \text { with } E ( \varepsilon ) \ \ 0 \ \text { and } \text { Var} ( \varepsilon ) \ \ \sigma _ { \varepsilon } ^ { 2 } I _ { N - 2 } \, ,$$

where K2 is given by (5). Since E(εη') 0 we get

$$\begin{pmatrix} y \\ 0 \end{pmatrix} \, \begin{pmatrix} I _ { N } \\ K _ { 2 } \end{pmatrix} \tau + \begin{pmatrix} \eta \\ - \varepsilon \end{pmatrix} \, \text { with } E \begin{pmatrix} \eta \\ - \varepsilon \end{pmatrix} \, \begin{pmatrix} 0 & \text { and } \, \text { Var} \begin{pmatrix} \eta \\ - \varepsilon \end{pmatrix} & \begin{pmatrix} \sigma _ { \eta } ^ { 2 } I _ { N } & 0 \\ 0 & \sigma _ { \varepsilon } ^ { 2 } I _ { N - 2 } \end{pmatrix} .$$

Therefore, Generalized Least Squares produces the minimum MSE linear estimator

$$\hat { \tau } = \left ( \sigma _ { \eta } ^ { - 2 } I _ { N } + \sigma _ { \varepsilon } ^ { - 2 } K _ { 2 } ^ { \, \cdot } K _ { 2 } \right ) ^ { - 1 } \sigma _ { \eta } ^ { - 2 } y$$

whose MSE matrix is given by

$$\Gamma \quad \text {Var} ( \hat { t } _ { t } ) \quad ( \sigma _ { \eta } ^ { - 2 } I _ { N } + \sigma _ { \varepsilon } ^ { - 2 } K _ { 2 } ^ { \prime } K _ { 2 } ) ^ { - 1 } .$$

By looking at the precision matrix Γ−1 , we see that it is the sum of two precision matrices, σ−2 This fact was exploited by Guerrero, Juarez and Poncela (2001) within the context of actuarial graduation, to propose an index (originally employed by Theil in 1963), to measure the proportion of P in (P + Q)−1, where P and Q are N×N positive definite matrices. Such an index is given by

$$\Lambda ( P ; P + Q ) \quad \text {tr} [ P ( P + Q ) ^ { - 1 } ] / N \, ,$$

where tr(.) denotes trace of a matrix. This is a measure of relative precision that has the following properties: (i) it takes values between zero and one; (ii) it is invariant under linear nonsingular transformations of the variable involved; (ii) it behaves linearly; and (iv) it is symmetric, in the sense that Λ(P; P + Q) + Λ(Q; P + Q) 1 .


<!-- p:12 -->


Thus, it is sensible to use (15) to quantify the proportion of precision attributable to the trend smoothness induced by model (11). Such an index of smoothness becomes

$$S ( \lambda ; N ) & \quad \Lambda ( \sigma _ { \varepsilon } ^ { - 2 } K _ { 2 } ^ { ^ { \prime } } K _ { 2 } ; \Gamma ) \\ & \quad 1 - \text {tr} [ ( I _ { N } + \lambda K _ { 2 } ^ { ^ { \prime } } K _ { 2 } ) ^ { - 1 } ] / N$$

with λ σ 2 This index depends only on the values λ and N, because K2 is fixed. It is clear that S(λ; N)→0 as λ → 0 and S(λ; N)→1 as λ → ∞ . Furthermore, if we express this index as a percentage, we can write S(λ; N)% or simply S% to interpret it as the percentage of smoothness achieved by the HP filter. Figure 2 allows us to appreciate the behavior of S(λ; N)%, for three different values of N and λ.

100%


(a)

(b)

95%

%S%

%06


N = 50

-λ

400

85%


N = 100

λ 1600

N = 200

6400

80%


0

1000

2000

3000

4000

5000

6000

0

50

100

150

200

N

λ

igg 10.1 (  1 0= () : %%(. )  0  0.

It is interesting to see in Figure 2 (a) that S(λ; N)% grows very rapidly as λ gets larger until around λ=1000, then it grows very slowly, independently of the sample size. Similarly, Figure 2 (b) allows us to appreciate the effect of the sample size for fixed λ values (those employed by Hodrick and Prescott, 1997). In the three cases shown by each graph, the percentage of smoothness is greater than 90% even with a sample size as small as N=50, or a smoothing constant as small as λ=400. Discriminating among different λ values could be done in terms of the S% achieved for a fixed sample size. For instance, the traditional value employed with the HP filter for business cycle analysis produces the following results: S(1600;50)%=92.4%, S(1600;100)%=93.4% and S(1600;200)=93.9%, in such a way that the percentage of smoothness achieved with λ=1600 fluctuates around 93.2% for the sample sizes most commonly used with quarterly time series. Such a percentage of smoothness might be considered relatively high for descriptive purposes.


<!-- p:13 -->


This work proposes to estimate the trend of a quarterly economic time series with a given sample size N, by fixing the desired percentage of smoothness and then looking for the λ value that satisfies this criterion. Such a value for the smoothing constant must be employed with all the quarterly time series of the same size, in order to establish valid comparisons. The basis of this suggestion is similar to that underlying the interval estimation of a fixed parameter θ by means of an expression like θ ± k × se() , with se() the standard error of ê. In such a case, what we usually do is fixing the desired confidence level, instead of fixing the value of the constant k. By doing that we achieve a better interpretation of the interval and greater comparability with other intervals. Something similar happens if, rather than fixing the value of the smoothing constant arbitrarily, we fix the desired characteristic of the HP filter in terms of the percentage of smoothness.

In case we were interested in performing business cycle analysis we should bear in mind Kaiser and Maravall's (2001) results, which provide a sound basis for selecting the smoothing parameter in that context. On the other hand, when we intend to apply the HP filter for descriptive purposes of the series, the recommendation is to fix the desired percentage of smoothness S% and derive from it the corresponding λ value. Since solving expression (16) for λ, given fixed values of N and S% is not straightforward, it is convenient to refer to Table 1. There we can see the λ values that correspond to some selected percentages of smoothness for different sample sizes.


<!-- p:14 -->


Table 1. Values of λ as a Function of Sample Size N and Percentage of Smoothness S% (Quarterly Series)

|   N |   Percentage of smoothness S% - 60% |   Percentage of smoothness S% - 65% |   Percentage of smoothness S% - 70% | Percentage of smoothness S% - 75%   | Percentage of smoothness S% - 80%   | Percentage of smoothness S% - 85%   | Percentage of smoothness S% - 90%   | Percentage of smoothness S% - 92.5%   | Percentage of smoothness S% - 95%   |
|-----|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|---------------------------------------|-------------------------------------|
|   4 |                                2.98 |                                5.60 |                                13.7 | ---                                 | ---                                 | ---                                 | ---                                 | ---                                   | ---                                 |
|   8 |                                1.61 |                                2.88 |                                 5.9 | 14.3                                | 42                                  | 197                                 | ---                                 | ---                                   | ---                                 |
|  12 |                                1.30 |                                2.25 |                                 4.3 | 9.6                                 | 27                                  | 116                                 | 977                                 | ---                                   | ---                                 |
|  16 |                                1.18 |                                2.00 |                                 3.7 | 8.0                                 | 21                                  | 83                                  | 641                                 | 3059                                  | ---                                 |
|  20 |                                1.12 |                                1.87 |                                 3.4 | 7.2                                 | 19                                  | 68                                  | 511                                 | 2126                                  | ---                                 |
|  24 |                                1.08 |                                1.79 |                                 3.3 | 6.7                                 | 17                                  | 60                                  | 410                                 | 1803                                  | 15396                               |
|  28 |                                1.05 |                                1.73 |                                 3.1 | 6.4                                 | 16                                  | 55                                  | 352                                 | 1506                                  | 11481                               |
|  32 |                                1.03 |                                1.69 |                                 3.0 | 6.2                                 | 15                                  | 51                                  | 317                                 | 1281                                  | 10128                               |
|  36 |                                1.01 |                                1.66 |                                 3.0 | 6.0                                 | 15                                  | 49                                  | 292                                 | 1136                                  | 9080                                |
|  40 |                                1.00 |                                1.64 |                                 2.9 | 5.9                                 | 14                                  | 47                                  | 275                                 | 1039                                  | 8047                                |
|  44 |                                0.99 |                                1.62 |                                 2.9 | 5.8                                 | 14                                  | 45                                  | 261                                 | 968                                   | 7138                                |
|  48 |                                0.98 |                                1.60 |                                 2.9 | 5.7                                 | 14                                  | 44                                  | 250                                 | 913                                   | 6439                                |
|  52 |                                0.97 |                                1.59 |                                 2.8 | 5.6                                 | 13                                  | 43                                  | 242                                 | 869                                   | 5915                                |
|  56 |                                0.97 |                                1.58 |                                 2.8 | 5.6                                 | 13                                  | 42                                  | 234                                 | 834                                   | 5522                                |
|  60 |                                0.96 |                                1.57 |                                 2.8 | 5.6                                 | 13                                  | 42                                  | 229                                 | 805                                   | 5217                                |
|  64 |                                0.96 |                                1.56 |                                 2.8 | 5.5                                 | 13                                  | 41                                  | 224                                 | 781                                   | 4966                                |
|  68 |                                0.96 |                                1.56 |                                 2.7 | 5.5                                 | 13                                  | 41                                  | 219                                 | 760                                   | 4758                                |
|  72 |                                0.95 |                                1.55 |                                 2.7 | 5.4                                 | 13                                  | 40                                  | 215                                 | 742                                   | 4580                                |
|  76 |                                0.95 |                                1.54 |                                 2.7 | 5.4                                 | 13                                  | 40                                  | 212                                 | 726                                   | 4427                                |
|  80 |                                0.95 |                                1.54 |                                 2.7 | 5.4                                 | 13                                  | 39                                  | 209                                 | 712                                   | 4296                                |
|  84 |                                0.94 |                                1.53 |                                 2.7 | 5.3                                 | 13                                  | 39                                  | 207                                 | 700                                   | 4184                                |
|  88 |                                0.94 |                                1.53 |                                 2.7 | 5.3                                 | 12                                  | 39                                  | 204                                 | 690                                   | 4082                                |
|  92 |                                0.94 |                                1.53 |                                 2.7 | 5.3                                 | 12                                  | 39                                  | 202                                 | 680                                   | 3991                                |
|  96 |                                0.94 |                                1.52 |                                 2.7 | 5.3                                 | 12                                  | 38                                  | 200                                 | 671                                   | 3914                                |
| 100 |                                0.94 |                                1.52 |                                 2.7 | 5.3                                 | 12                                  | 38                                  | 199                                 | 663                                   | 3842                                |

NOTE: Values calculated numerically by solving expression (16) for λ, given S% and N. --- Denotes an unreliable value.

In order to simplify the selection of λ in practical applications, a parsimonious function of N that would provide a good fit to the values in Table 1 was searched for by fitting several regression models for each S% value. There were some particularly best fitting models (in the sense of yielding higher R2 coefficients) for some individual S% values, nevertheless a generic form was preferred for all the percentages of smoothness considered. The estimation results of the best generic fitting model appear in Table 2, where we can see the model form as well as the corresponding R2 coefficients, which are all very close to unity.


<!-- p:15 -->


Table 2. Estimation Results of Fitting a Generic Model for Relating λ with N and S% (Quarterly Series)

| Model form: log( λ ) = b 0 + b 1 /N - S%   |   Model form: log( λ ) = b 0 + b 1 /N - b 0 |   Model form: log( λ ) = b 0 + b 1 /N - b 1 |   Model form: log( λ ) = b 0 + b 1 /N - R 2 |
|--------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|
| 60%                                        |                                   -0.118673 |                                    4.785972 |                                      0.9993 |
| 65%                                        |                                    0.359485 |                                    5.461539 |                                      0.9997 |
| 70%                                        |                                    0.905558 |                                    6.809808 |                                      0.9994 |
| 75%                                        |                                    1.565911 |                                    8.499703 |                                      0.9974 |
| 80%                                        |                                    2.397834 |                                   10.680865 |                                      0.9993 |
| 85%                                        |                                    3.482772 |                                   14.952133 |                                      0.9986 |
| 90%                                        |                                    5.065726 |                                   22.265061 |                                      0.9985 |
| 92.5%                                      |                                    6.199961 |                                   29.844806 |                                      0.9976 |
| 95%                                        |                                    7.818861 |                                   44.597357 |                                      0.9951 |

In order to carry out business cycle analysis, the HP filter must be applied to deseasonalized series, to avoid the confusion of cyclical movements with seasonal fluctuations. When the HP filter is used as a descriptive device to estimate the trend, the series under consideration might or might not be previously deseasonalized, because the resulting trend will not be affected by seasonal fluctuations, when the desired percentage of smoothness is at least 80%. This is guaranteed by Kaiser and Maravall's (2001) results which indicate that a smoothing constant λ≥9 is big enough to cancel out all those fluctuations whose frequency is less than two years, which obviously include the seasonal ones. Then, by looking at Table 1 we can see that λ≥9 produces percentages of smoothness close to 80%.

As an illustrative application of the previous results let us consider the quarterly GDP series shown in Figure 1. The sample period runs from 1980:01 to 2004:01, so that N=97. If the desired percentage of smoothness is S%=90%, the corresponding smoothing constant is obtained from Table 2 and becomes λ=199. In that case we get plot (d) of Figure 1. When the smoothing constant is λ=1, we get plot (c) of that figure and the percentage of smoothness achieved is 60.7%, while λ=1600 produces 93.9% smoothness. It should be mentioned that in these cases, the HP filter was applied to the seasonally adjusted GDP expressed in logarithms. Afterwards, the resulting trend was exponentiated t    e osd s    ss e    e s the other hand, in Figure 3 we can see the trends produced by the HP filter applied directly to the GDP series (without using logarithms nor seasonal adjustment). Two different percentages of smoothness were used for the trend, namely S%=90% and S%=80%.


<!-- p:16 -->


Figure 3. Trend Estimation of Mexico's Quarterly GDP, Unadjusted for Seasonality. With percentage of smoothness: (a) S%=90% and (b) S%=80%.

(a)

(b)

1700000


1600000


1500000


1400000


1300000


1200000


1100000


1000000

GDP

1000000

GDP

-λ199

− λ 12

900000


1980-01

1982-01

1984-01

1986-01

1988-01

1990-01

1992-01

1994-01

1996-01

1998-01

2000-01

2002-01

2004-01

1980-01

1982-01

1984-01

1986-01

1988-01

1990-01

1992-01

1994-01

1996-01

1998-01

2000-01

2002-01

2004-01

By comparing the trend shown in Figure 3 (a) with that of Figure 1 (d), both of which achieve 90% smoothness, we corroborate empirically the fact that seasonally adjusting a series does not affect trend estimation, as long as the percentage of smoothness is 80% or higher. Now, by looking at Figure 3 we can appreciate that the trend in (a) reacts more slowly to unexpected fluctuations in the series than in (b). Therefore the trend in (a) may be considered more conservative than that in (b). This kind of facts should be taken into account when deciding an appropriate percentage of smoothness for the trend. Furthermore, the degree of smoothness is especially relevant when there is a need for extrapolating the trend. In that situation, the most recent values of the observed series may be unduly affected by local fluctuations and mislead about the future path of the trend. This can be appreciated in the extremes of the trends shown by plots (a) and (b) in Figure 3. In fact, were we interested in extrapolating the trend of the series, we would use model (8) to do it. That is, we would employ the expression τN+h 2τN+h-1 − τN+h-2 for h=1, 2, .. which makes use of only the last two estimated trend values (τN–1 and τN) and then it follows its own linear dynamics.


<!-- p:17 -->


### 5. SELECTION OF λ FOR NON-QUARTERLY SERIES

When the time series under study is non-quarterly, the λ values shown in Tables 1 and 2 are not applicable. To see why this is so, let us suppose that the observation period covers years 1999 through 2003. That means there are 20 quarterly data, 60 monthly data, or only 5 yearly data, depending on the frequency of observation of the series. Therefore, although the long-term behavior of the series must be essentially the same in the quarterly, monthly or yearly data, Table 2 would lead us to select different λ values for the same S% for each of those series. The problem would arise if we do not take into account that series with lower frequencies of observation are related to those with higher frequency by means of some type of aggregation mechanism. This fact was realized by Maravall and del Rio (2001), who proposed four different solutions to find λ values capable of producing equivalent results on series with different periodicities. They preferred to choose λ in such a way as to preserve the period of the cycle for which the HP filter gain is 0.5. This choice is consistent with the proposal of Kaiser and Maravall (2001), when the objective of using the HP filter is to carry out business cycle analysis.

In the present case we should choose the smoothing constant for non-quarterly series in such a way that it yields an equivalent percentage smoothness as the λ value that corresponds to the quarterly series. Therefore, we require to decide the λ value on the basis of the very nature of the non-quarterly series. To that end we must consider the type of operation that lies behind the aggregation employed to obtain the lower frequency series {yτ}, say a quarterly series, from the higher frequency series {yt} , say a monthly series. The aggregation is assumed to be of the form

$$y _ { T } ^ { ^ { * } } \ \sum _ { j \ 1 } ^ { k } c _ { j } y _ { k ( T - 1 ) + j }$$

where k is the number of observations yt between two successive observations yτ . For instance, there are k=3 monthly observations in a quarter. The c,'s are constants that define the type of aggregation, so that c1 ... ck 1 are used to aggregate a flow series, c1 ... ck 1/k are used when working with an index or an annualized flow series (in which case we will also say that it is a flow series). When c1 = 1, c2 ... ck 0 or c1 ... ck-1 0, ck 1 we are dealing with a stock series, in which case the aggregated series is said to be generated by systematic sampling.


<!-- p:18 -->


The underlying statistical model for the HP filter to be applied to the aggregated data is of the same form as (10) - (11), that is

$$y ^ { ^ { * } } = \tau ^ { ^ { * } } + \eta ^ { ^ { * } } \text { with } E ( \eta ^ { ^ { * } } ) = 0 \text { and } V a r ( \eta ^ { ^ { * } } ) = \sigma _ { \eta } ^ { ^ { * } 2 } I _ { n }$$

$$K _ { 2 } \tau ^ { * } = \varepsilon ^ { * } \quad \text {with} \ E ( \varepsilon ^ { * } ) = 0 \text { and } V a r ( \varepsilon ^ { * } ) = \sigma _ { \varepsilon } ^ { * 2 } I _ { n - 2 }$$

with E(ε*η*') 0, where the star denotes an aggregated variable. As before, the trend estimator becomes

$$\tilde { t } ^ { ^ { * } } = ( \sigma _ { \eta } ^ { ^ { * } - 2 } I _ { n } + \sigma _ { \varepsilon } ^ { ^ { * } - 2 } K _ { 2 } ^ { ^ { * } } K _ { 2 } ) ^ { - 1 } \sigma _ { \eta } ^ { ^ { * } - 2 } y ^ { ^ { * } } ,$$

where n=[N/k] and [x] denotes the integer part of a real number x. Even though expressions (18) – (20) for the aggregated series are similar to their counterparts for the disaggregated series, the HP filter does not preserve itself under aggregation. That is, if we aggregate the components {tt} and {nt} we do not get {τT} and {T} which are obtained directly from the aggregated series (see Maravall and del Rio, 2001). However, it is possible to find a λ* value for the aggregated series that yields results equivalent to those produced by λ for the disaggregated series, in the sense of percent smoothness.

To obtain equivalent λ values, we must equate the underlying models of the HP filter for the aggregated and disaggregated series. That is, since the aggregated model is

$$\nabla ^ { 2 } y _ { T } ^ { * } \quad \varepsilon _ { T } ^ { * } + \nabla ^ { 2 } \eta _ { T } ^ { * } ,$$

i.e. an IMA(2,2) model, it follows that its variance and autocovariances are given by Γ0 σ *2 + 6σ *2 -4σ *2 and Γ2 σ *2 . On the other hand, by aggregating the ε disaggregated model and using the fact that ∇k ∇Sk , where Sk 1+ B + ...+ Bk-1 and ∇k 1– Bk, we get the following model (see Maravall and del Rio, 2001 for details)

$$\nabla ^ { 2 } y _ { T } ^ { * } \ \ S _ { k } ^ { 3 } \varepsilon _ { t } + S _ { k } \nabla _ { k } ^ { 2 } \eta _ { t } \text { for flows } \text { and } \nabla ^ { 2 } y _ { T } ^ { * } \ \ S _ { k } ^ { 2 } \varepsilon _ { t } + \nabla _ { k } ^ { 2 } \eta _ { t } \text { for stocks.}$$

The Autocovariance Generating Function (AGF) of the disaggregated series, γ(B) Σj −∞ γ jBj , is given by

γ(B) σ +Sk 2 ∆+ σ for stocks (23) ε


<!-- p:19 -->


with Sk 1 + B−1 + ...+ B−k+1 and ∇k 1− B−k . For instance, for k=3 and a flow series we obtain γo 141σ 2 +18σ 2 γ1 126σ 2 +8σ γ2 90σ 2 -2σ 2 γ3 50σ 2 -12σ 2 ε η, ε η, ε η, ε η, 21σ ε 2 -7σ n, γ5 2 6σ 2 ε -2σ 2 η Y6 σ ε 2 +3σ 2 , γ7 2σ η, 2 γ8 σ η 2 and γj r j≥ 9. While for a stock series γo 19σ +6σ , γ1 16σ 52, γ2 10σ 5ε, γ3 4σ 2 -4σ 2 ε η, σ ε , 2 γ5 50, γ6 σ η 2 and γj 0 for j ≥ 7. The values of σ ε, 2 σ η, 2 σ *2 ε and σ *2 that make equivalent the results of the two HP filters are obtained by equating the autocovariances γ0, γ1k and γ2k to Γ0, Γ1 and Γ2. This amounts to asking that the following system of equations holds true

$$\begin{pmatrix} 1 & 6 \\ 0 & - 4 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} \sigma _ { \varepsilon } ^ { * 2 } \\ \sigma _ { \eta } ^ { * 2 } \end{pmatrix} \begin{pmatrix} a _ { 1 1 , k } & a _ { 1 2 , k } \\ a _ { 2 1 , k } & a _ { 2 2 , k } \\ a _ { 3 1 , k } & a _ { 3 2 , k } \end{pmatrix} \begin{pmatrix} \sigma _ { \varepsilon } ^ { 2 } \\ \sigma _ { \eta } ^ { 2 } \end{pmatrix}$$

where a11,k, a21,k and a31,k are the coefficients of B0, Bk and B2k in the polynomial for a flow series, or in the polynomial S2S for a stock series. In a similar fashion, a12,k, a22,k and a32,k are the coefficients of B0, Bk and B2k in the polynomial Sk ∇kSk ∇2 if the series is of flows, or in the polynomial ∇k∇k if the series is of stocks.

Now, by algebraic manipulation it can be shown that

$$\nabla _ { k } ^ { 2 } \nabla _ { k } ^ { 2 } \quad 6 - 4 ( B ^ { k } + B ^ { - k } ) + ( B ^ { 2 k } + B ^ { - 2 k } )$$

and

$$S _ { k } \nabla _ { k } ^ { 2 } \overline { S } _ { k } \nabla _ { k } ^ { 2 } \quad [ k + ( k - 1 ) ( B + B ^ { - 1 } ) + \dots + 2 ( B ^ { k - 2 } + B ^ { - k + 2 } ) + ( B ^ { k - 1 } + B ^ { - k + 1 } ) ] \nabla _ { k } ^ { 2 } \nabla _ { k } ^ { 2 } \\ 6 k - 4 k ( B ^ { k } + B ^ { - k } ) + k ( B ^ { 2 k } + B ^ { - 2 k } ) + P _ { k } ( B , B ^ { - 1 } ) \, ,$$

where Pk (B,B−1) is a symmetric polynomial in B and B1 that does not contain powers of type Bik for i=0, 1, 2. Therefore, we obtain a12,k 6k, a22,k −4k and a32,k k for flows, and a12,k 6, a22,k -4 and a32,k 1 for stocks. The elements a11,k, a21,k and a31,k are coefficients of B0, Bk and B2k in the polynomials associated to 2 in the σ AGF. These elements are shown in Table 3 for some values of k considered of practical relevance.


<!-- p:20 -->


Table 3. Coefficients of the Polynomials Associated to the Variance σ in γ(B)

|   k |   Flows - 11,k a |   Flows - 21,k a |   Flows - 31,k a |   Stocks - 11,k a |   Stocks - 21,k a |   Stocks - 31,k a |
|-----|------------------|------------------|------------------|-------------------|-------------------|-------------------|
|   2 |               20 |                6 |                0 |                 6 |                 1 |                 0 |
|   3 |              141 |               50 |                1 |                19 |                 4 |                 0 |
|   4 |              580 |              216 |                6 |                44 |                10 |                 0 |
|   5 |             1751 |              666 |               21 |                85 |                20 |                 0 |
|   6 |             4332 |             1666 |               56 |               146 |                35 |                 0 |
|   7 |             9331 |             3612 |              126 |               231 |                56 |                 0 |
|  12 |           137292 |            53768 |             2002 |              1156 |               286 |                 0 |
|  13 |           204763 |            80262 |             3003 |              1469 |               364 |                 0 |

The linear system (24) has only two unknowns (either σ 2 and σ 2 if σ *2 and σ *2 are η, ε η given, or vice-versa). Therefore it does not have an exact solution. Nonetheless, as in Maravall and del Rio (2001) we can get an approximate solution by minimizing the sum of squares SCk Σ 0(Γ j − γ jk)2 . That is, if we fix the values σk *2 1 and σ *2 * we ε η can find the values ô 2 and ô 2 that minimize SCk. To this end we may use standard ε η calculus (see the Appendix) to obtain the solution

$$\hat { \sigma } _ { \varepsilon } ^ { 2 } \quad ( 5 3 a _ { 1 1 , k } - 6 x _ { 0 } ) / ( 5 3 x _ { 1 } - x _ { 0 } ^ { 2 } ) \\ \hat { \sigma } _ { \eta } ^ { 2 } \quad \begin{cases} [ ( 6 x _ { 1 } - x _ { 0 } a _ { 1 1 , k } ) / ( 5 3 x _ { 1 } - x _ { 0 } ^ { 2 } ) + \lambda _ { k } ^ { * } ] / k & \text { for flows} \\ \ ( 6 x _ { 1 } - x _ { 0 } a _ { 1 1 , k } ) / ( 5 3 x _ { 1 } - x _ { 0 } ^ { 2 } ) + \lambda _ { k } ^ { * } & \text { for stocks,} \end{cases}$$

with x0 6a11,k − 4a21,k + a31,k and x1 a ̄1,k + a21,k + a31,k · Table 4 presents the values 2 λ ô 2 /0 2 that come out of (27) for some selected values of k. For instance, k=3 serves to ε relate quarterly data to monthly data; with k=5, 6 or 7 we can relate weekly data to daily data (with 5, 6 or 7 days per week); and k=13 is useful to relate quarterly data to weekly data.


<!-- p:21 -->


Table 4. Values of λ Equivalent to λ, for Selected Values of k

|   k | Flows                         | Stocks                     |
|-----|-------------------------------|----------------------------|
|   3 | 3.9975 + 71.2556 * 3 λ        | 0.9547 + 24.7661 * 3 λ     |
|   5 | 31.9644 + 544.4521 * 5 λ      | 4.7792 + 113.8831 * 5 λ    |
|   6 | 66.6390 + 1127.0891 * 6 λ     | 8.3654 + 196.5614 * 6 λ    |
|   7 | 123.8457 + 2085.9705 * 7 λ    | 13.3865 + 311.9137 * 7 λ   |
|  13 | 1482.0110 + 24764.5972 * 13 λ | 87.0343 + 1995.1365 * 13 λ |

When we need to find the smoothing constant for a lower frequency series, equivalent to the value λk corresponding to a higher frequency series, we can use again the idea of minimizing the sum of squares SCk Σ 0(Γj − γ jk)2 . All we need to do now is fixing the values σ ε 2 1 and σ 2 η λk to look for σ%2 *2 and σ *2 η that minimize SCk. In such a case, the solution becomes

$$\hat { \sigma } _ { \eta } ^ { ^ { * } 2 } & \quad ( a _ { 3 1 , k } - 4 a _ { 2 1 , k } ) / 1 7 + \lambda _ { k } \left ( a _ { 3 2 , k } - 4 a _ { 2 2 , k } \right ) / 1 7 \\ & \quad \hat { \sigma } _ { \varepsilon } ^ { ^ { * } 2 } \quad a _ { 1 1 , k } + a _ { 1 2 , k } \lambda _ { k } - 6 \hat { \sigma } _ { \eta } ^ { ^ { * } 2 } \, .$$

For instance, with k=4 we get: λ*=-0.057170+0.004531λ4 for a flow series and λ*=0.040486+0.017206λ4 for a stock series. With these values we can relate the smoothness of a quarterly series with that of a yearly series. It should be noticed that these formulas differ from those given by Table 4 when we solve for the smoothing constant for the aggregated series (λ4=-0.057919+0.004461λ for flows and λ*=- * 0.040879+0.017114λ for stocks) since the solution of system (24) is not exact. Therefore the results in Table 4 should only be used to get equivalent λ values for higher frequency data from those of lower frequency data and (28) should be used otherwise.

The proposed method is now applied to Mexico's monthly GDP series as an illustrative application. To get the λ value equivalent to the constant λ3 employed with the quarterly series, with a sample period covering 1980:01 to 2004:03, we start by noticing that the N=291 months of data are equivalent n=97 quarters and that we are dealing with a flow series. Hence, the formula to use is λ=3.9975+71.2556 λ3, in such a way that to attain S%=90% we require λ3 =199.38 (see Table 2) and to attain S%=80% the value has to be λ3 =12.28. These constants yield the equivalent values for the monthly series λ=14212 and λ=879, respectively. The trends produced by the HP filter are shown in Figure 4. It is interesting to compare the plots in this figure with those in Figure 3. By doing that we can conclude that the trends with the same percentage of smoothness have essentially the same dynamic behavior, no matter what the periodicity of observation of the data is.


<!-- p:22 -->


Figure 4. Mexico's Monthly GDP Series and its Trend. With percentage of smoothness: (a) S%=90% and (b) S%=80%.

(a)

(b)

1750000


1650000


1550000


1450000


1350000


1250000


1150000


1050000


950000

W

GDP

950000

GDP

λ 879

850000


1980:01

1982:01

1984:01

1986:01

1988:01

1990:01

1992:01

1994:01

1996:01

1998:01

2000:01

2002:01

2004:01

1980:01

1982:01

1984:01

1986:01

1988:01

1990:01

1992:01

1994:01

1996:01

1998:01

2000:01

2002:01

2004:01

The following illustrative example makes use of the yearly GDP series. In this case we have n=24 whole years (1980 - 2003), then the number of quarters becomes N=96 and the smoothing constants corresponding to S%= 90% and S%=80% are λ4=199.86 and λ4=12.29. By employing the relation λ*=-0.057170+0.004531λ4 we get the values λ*=0.8484 and λ*=-0.0015≈0.00001 (since λ has to be positive) for the respective desired percentages of smoothness. Those values produced the trends shown in Figure 5. There, we can appreciate again that the trends with the same percentage of smoothness behave essentially the same, independently of the frequency of observation of the series.


<!-- p:23 -->


Figure 5. Mexico's Yearly GDP Series and its Trend. With percentage of smoothness: (a) S%=90% and (b) S%=80%.

(a)

(b)

1700000


1000

1600000

1500000


1400000


1300000


1200000


1100000


1000000

GDP

10000

-GDP

λ0.8484

− λ 0.0000

000006

900000

1980:01

1982:01

1984:01

1986:01

1988:01

1990:01

1992:01

1994:01

1996:01

1998:01

2000:01

2002:01

1980:01

1982:01

1984:01

1986:01

1988:01

1990:01

1992:01

1994:01

1996:01

1998:01

2000:01

2002:01

A final illustrative example considers the daily Exchange Rate (Pesos/US Dollar) series. The sample period runs from July 1, 1999 through September 6, 2004. Therefore we have N=1306 working days, corresponding to n=20 whole quarters of a stock series. To achieve percentages of smoothness S%=90% and S%=80% in the quarterly series we should use λ13 =482.50 and λ13 =18.76 respectively, as indicated by Table 2. Then, to calculate the equivalent weekly constant we use expression λ=87.0343+1995.1365 λ3 to obtain λ=962739 and λ=37521, respectively. Since the data correspond to a 5 day week, these values now play the roles of λ to get the equivalent constants for the daily series, by means of λ=4.7792+113.8831 λ. Hence, the required values for the daily series become λ=109639660 and λ=4273061. The resulting estimated trends produced by the HP filter for the daily Exchange Rate series are shown in Figure 6.

### 6. FINAL REMARKS

The need of estimating trends for economic time series may arise for several reasons, one of which is the description of the series by way of a smooth curve that represents its mean value dynamically. In that case, the method suggested here is the HP filter, because of its statistical basis and practical interpretation. The numerical computations involved can be done easily by Kalman filtering and the only remaining problem to apply the HP filter in practice was specifying the smoothing constant. This paper presents a solution to this problem that allows us to determine such a constant as a function of the desired percentage of smoothness of the trend.


<!-- p:24 -->


Figure 6. Daily Exchange Rate (Peso/US Dollar) and its Estimated Trend. With percentage of smoothness: (a) S%=90% and (b) S%=80%.

(a)

(b)

11.5


10.5


9.5


- Exchange rate


λ 109639660

λ4273061

8.5


1999:128

1999:236

2000:90

2000:198

2001:52

2001:160

2002:14

2002:122

2002:230

2003:84

2003:192

2004:46

2004:154

1999:128

1999:236

2000:90

2000:198

2001:52

2001:160

2002:14

2002:122

2002:230

2003:84

2003:192

2004:46

2004:154

The concept of trend smoothness is formalized here by associating it to the relative precision attributable to the smoothness component of the statistical model underlying the HP filter. Therefore, we can measure trend smoothness by way of an index that involves the smoothing constant of the HP filter. That enables us to choose the smoothing constant by fixing a desired percentage of smoothness for the trend at the outset. By being able to fix the percentage of smoothness of the trend for every series under study, we can make valid comparisons between trends for different series with the same percentage of smoothness. Similarly we can compare trends with different percentages of smoothness for the same series.

The procedure for choosing the smoothing constant arises naturally for quarterly series since the HP filter was proposed originally for that kind of series. Nevertheless, the procedure is generalized here to other type of data frequencies. To do that we require knowing whether the series consists of flows or stocks. Then, some formulas are provided to relate the smoothing constants for series with different frequencies of observation, so that they produce trends with the same percentage of smoothness. The values required for applying the procedure with quarterly or non-quarterly series are provided in some tables in order to facilitate its use. Several illustrative examples are presented for both quarterly and non-quarterly series. It is clear that this is an easy-to-use procedure, whose results are very reasonable and justify its empirical application. If this procedure is considered for massive and routine application on several time series, e.g. at an official statistical agency, it is recommended that a pilot study be carried out in order to decide the appropriate percentage of smoothness (say 90% or 80%) either for all the series under consideration or for groups of series.


<!-- p:25 -->


### ACKNOWLEDGMENTS

The author wishes to acknowledge the valuable participation of Eduardo Becerra, who commented on several aspects of this work and carried out the computations leading to Figure 2 and Table 1. The author thanks INEGI for its hospitality during a sabbatical year granted by ITAM. He also thanks Asociación Mexicana de Cultura, A. C., for its support through a Professorship on Time Series Analysis and Forecasting in Econometrics. Able research assistance was also provided by J. A. Juárez.

### APPENDIX A: APPROXIMATE SOLUTION FOR EQUIVALENT VARIANCES

The sum of squares involved is

$$\text {The sum of squares involved is } \\ S C _ { k } \quad \sigma _ { s } ^ { * 4 } + 1 2 \sigma _ { s } ^ { * 2 } \sigma _ { \eta } ^ { * 2 } + 5 3 \sigma _ { \eta } ^ { * 4 } - 2 [ ( \sigma _ { s } ^ { * 2 } + 6 \sigma _ { \eta } ^ { * 2 } ) ( a _ { 1 1 , k } \sigma _ { k } ^ { * 2 } + a _ { 1 2 , k } \sigma _ { \eta } ^ { * 2 } ) \\ - 4 \sigma _ { \eta } ^ { * 2 } ( a _ { 2 1 , k } \sigma _ { \varepsilon } ^ { * 2 } + a _ { 2 2 , k } \sigma _ { \eta } ^ { * 2 } ) + \sigma _ { \eta } ^ { * 2 } ( a _ { 3 1 , k } \sigma _ { \varepsilon } ^ { * 2 } + a _ { 3 2 , k } \sigma _ { \eta } ^ { * 2 } ) ] \\ + ( a _ { 1 1 , k } \sigma _ { \varepsilon } ^ { * 2 } + a _ { 1 2 , k } \sigma _ { \eta } ^ { * 2 } ) ^ { 2 } + ( a _ { 2 1 , k } \sigma _ { \varepsilon } ^ { * 2 } + a _ { 2 2 , k } \sigma _ { \eta } ^ { * 2 } ) ^ { 2 } + ( a _ { 3 1 , k } \sigma _ { \varepsilon } ^ { * 2 } + a _ { 3 2 , k } \sigma _ { \eta } ^ { * 2 } ) ^ { 2 } , \\$$

thus, if we fix the values *2 ε 1 and σ *2 * we get the following derivatives

乙

$$\text {and} \\ \frac { \partial \text {SC} _ { k } } { \partial \sigma _ { n } ^ { 2 } } & \quad - 2 [ ( 1 + 6 \lambda _ { k } ^ { ^ { * } } ) a _ { 1 2 , k } - 4 \lambda _ { k } ^ { ^ { * } } a _ { 2 2 , k } + \lambda _ { k } ^ { ^ { * } } a _ { 3 2 , k } ] \\ & + 2 [ ( a _ { 1 2 , k } ^ { 2 } + a _ { 2 2 , k } ^ { 2 } + a _ { 3 2 , k } ^ { 2 } ) \sigma _ { \eta } ^ { 2 } + ( a _ { 1 1 , k } a _ { 1 2 , k } + a _ { 2 1 , k } a _ { 2 3 , k } ) \sigma _ { \eta } ^ { 2 } + ]$$

$$\frac { \partial S C _ { k } } { \partial \sigma _ { \varepsilon } ^ { 2 } } & \quad - 2 [ ( 1 + 6 \lambda _ { k } ^ { ^ { * } } ) a _ { 1 1 , k } - 4 \lambda _ { k } ^ { ^ { * } } a _ { 2 1 , k } + \lambda _ { k } ^ { ^ { * } } a _ { 3 1 , k } ] \\ & + 2 [ ( a _ { 1 1 , k } ^ { 2 } + a _ { 2 1 , k } ^ { 2 } + a _ { 3 1 , k } ^ { 2 } ) \sigma _ { \varepsilon } ^ { 2 } + ( a _ { 1 1 , k } a _ { 1 2 , k } + a _ { 2 1 , k } a _ { 2 2 , k } + a _ { 3 1 , k } a _ { 3 2 , k } ) \sigma _ { \eta } ^ { 2 } ] \\$$

and Then, by evaluating these on the optimal values ô 2ω and 0 2 equating to zero and solving η, the resulting equations, we get expressions (27).


<!-- p:26 -->


### APPENDIX B. QUARTERLY GDP DATA (ORIGINAL AND SEASONALLY ADJUSTED)

|      | Quarter   |     GDP |   X-12- ARIMA |      | Quarter   |     GDP |   X-12- ARIMA |   Quarter | Quarter   |     GDP |   X-12- ARIMA |
|------|-----------|---------|---------------|------|-----------|---------|---------------|-----------|-----------|---------|---------------|
| 1980 | I         |  938135 |        925194 | 1989 | I         | 1068783 |       1071763 |      1998 | I         | 1431862 |       1434478 |
| 1980 | II        |  935461 |        935822 | 1989 | II        | 1111605 |       1087027 |      1998 | II        | 1455594 |       1447484 |
| 1980 | III       |  925245 |        953337 | 1989 | III       | 1050907 |       1095429 |      1998 | III       | 1412882 |       1455247 |
| 1980 | IV        |  995587 |        979721 | 1989 | IV        | 1111908 |       1101880 |      1998 | IV        | 1496902 |       1459603 |
| 1981 | I         | 1015503 |       1005851 | 1990 | I         | 1115170 |       1115518 |      1999 | I         | 1460942 |       1468982 |
| 1981 | II        | 1031141 |       1024350 | 1990 | II        | 1156562 |       1134458 |      1999 | II        | 1504375 |       1490807 |
| 1981 | III       | 1004063 |       1039941 | 1990 | III       | 1102849 |       1151058 |      1999 | III       | 1473442 |       1514324 |
| 1981 | IV        | 1067221 |       1044995 | 1990 | IV        | 1193417 |       1162646 |      1999 | IV        | 1575240 |       1542587 |
| 1982 | I         | 1046417 |       1039734 | 1991 | I         | 1157545 |       1171418 |      2000 | I         | 1569060 |       1574738 |
| 1982 | II        | 1036685 |       1032007 | 1991 | II        | 1221764 |       1180083 |      2000 | II        | 1614588 |       1600933 |
| 1982 | III       |  996733 |       1023675 | 1991 | III       | 1140122 |       1192505 |      2000 | III       | 1576881 |       1612036 |
| 1982 | IV        | 1016646 |       1006702 | 1991 | IV        | 1241096 |       1204600 |      2000 | IV        | 1648861 |       1614851 |
| 1983 | I         | 1004290 |        990674 | 1992 | I         | 1211845 |       1217541 |      2001 | I         | 1599979 |       1609591 |
| 1983 | II        |  986440 |        982735 | 1992 | II        | 1249936 |       1230998 |      2001 | II        | 1617803 |       1602359 |
| 1983 | III       |  955682 |        983353 | 1992 | III       | 1191296 |       1239700 |      2001 | III       | 1556932 |       1595571 |
| 1983 | IV        | 1007248 |       1000269 | 1992 | IV        | 1276025 |       1243618 |      2001 | IV        | 1626989 |       1592954 |
| 1984 | I         | 1037162 |       1015389 | 1993 | I         | 1248725 |       1245689 |      2002 | I         | 1561778 |       1597256 |
| 1984 | II        | 1015362 |       1023847 | 1993 | II        | 1260352 |       1251571 |      2002 | II        | 1648074 |       1609981 |
| 1984 | III       | 1000452 |       1024586 | 1993 | III       | 1211580 |       1258038 |      2002 | III       | 1581356 |       1620765 |
| 1984 | IV        | 1035536 |       1032083 | 1993 | IV        | 1304127 |       1265441 |      2002 | IV        | 1657089 |       1620816 |
| 1985 | I         | 1054820 |       1038124 | 1994 | I         | 1277838 |       1284699 |      2003 | I         | 1601329 |       1620316 |
| 1985 | II        | 1052454 |       1044371 | 1994 | II        | 1331435 |       1312020 |      2003 | II        | 1649944 |       1624718 |
| 1985 | III       | 1012227 |       1046652 | 1994 | III       | 1267386 |       1327279 |      2003 | III       | 1591019 |       1635122 |
| 1985 | IV        | 1058455 |       1039653 | 1994 | IV        | 1372142 |       1314911 |      2003 | IV        | 1690011 |       1653443 |
| 1986 | I         | 1023030 |       1027117 | 1995 | I         | 1272242 |       1273114 |      2004 | I         | 1661053 |       1677559 |
| 1986 | II        | 1047878 |       1016757 | 1995 | II        | 1209053 |       1225767 |      2004 |           |         |               |
| 1986 | III       |  964237 |       1005708 | 1995 | III       | 1165580 |       1213029 |      2004 |           |         |               |
| 1986 | IV        | 1014174 |        998515 | 1995 | IV        | 1275557 |       1237444 |      2004 |           |         |               |
| 1987 | I         | 1012635 |       1011103 | 1996 | I         | 1273078 |       1266122 |           |           |         |               |
| 1987 | II        | 1050061 |       1025848 | 1996 | II        | 1287401 |       1282625 |           |           |         |               |
| 1987 | III       |  992042 |       1036854 | 1996 | III       | 1248665 |       1298697 |           |           |         |               |
| 1987 | IV        | 1064328 |       1041439 | 1996 | IV        | 1366292 |       1318910 |           |           |         |               |
| 1988 | I         | 1038644 |       1040885 | 1997 | I         | 1331527 |       1342915 |           |           |         |               |
| 1988 | II        | 1061388 |       1036158 | 1997 | II        | 1395247 |       1369714 |           |           |         |               |
| 1988 | III       |  993274 |       1040351 | 1997 | III       | 1342048 |       1394358 |           |           |         |               |
| 1988 | IV        | 1078618 |       1053788 | 1997 | IV        | 1457278 |       1414893 |           |           |         |               |

NOTE: Millions of pesos at 1993 value. Source: INEGI, Sistema de Cuentas Nacionales, http://www.inegi.gob.mx X-12-ARIMA indicates deseasonalized data with that procedure.


<!-- p:27 -->

<!-- END SOURCE 19/40: Guerrero_2008_estimating-trends-percentage-smoothness.md -->

---

<!-- BEGIN SOURCE 20/40: Hamilton_1989_nonstationary-time-series-business-cycle.md -->

# Source: `Hamilton_1989_nonstationary-time-series-business-cycle.md`

---
id: "Hamilton_1989_nonstationary-time-series-business-cycle"
source_pdf: "../pdf/Hamilton_1989_nonstationary-time-series-business-cycle.pdf"
source_filename: "Hamilton_1989_nonstationary-time-series-business-cycle.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 98.0
visual_assets: "disabled"
---

<!-- p:1 -->

####### A NEW APPROACH TO THE ECONOMIC ANALYSIS OF NONSTATIONARY TIME SERIES AND THE BUSINESS CYCLE

##### BY JAMES D. HAMILTON1

This paper proposes a very tractable approach to modeling changes in regime. The parameters of an autoregression are viewed as the outcome of a discrete-state Markov process. For example, the mean growth rate of a nonstationary series may be subject to occasional, discrete shifts.

The econometrician is presumed not to observe these shifts directly, but instead must draw probabilistic inference about whether and when they may have occurred based on the observed behavior of the series. The paper presents an algorithm for drawing such probabilistic inference in the form of a nonlinear iterative filter. The filter also permits estimation of population parameters by the method of maximum likelihood and provides the foundation for forecasting future values of the series.

An empirical application of this technique to postwar U.S. real GNP suggests that the periodic shift from a positive growth rate to a negative growth rate is a recurrent feature of the U.S. business cycle, and indeed could be used as an objective criterion for defining and measuring economic recessions. The estimated parameter values suggest that a typical eco o  t e  nd      sn n.

KEYwoRDs: Switching regression, segmentation, nonstationary, business cycle, nonlinear filtering, regime changes.

## 1. INTRODUCTION AND SUMMARY

A NUMBER OF RECENT STUDIES have sought to characterize the nature of the long term trend in GNP and its relation to the business cycle. Researchers such as Beveridge and Nelson (1981), Nelson and Plosser (1982), and Campbell and Mankiw (1987a, b) explored this question using ARIMA models or ARMA processes around a deterministic trend. Others, such as Harvey (1985), Watson (1986), and Clark (1987) based their analyses on linear unobserved components models. A third approach employs the co-integrated specification of Engle and Granger (1987), whose relevance for business cycle research is examined in a fascinating paper by King, Plosser, Stock, and Watson (1987).

These approaches are based on the assumption that first differences of the log of GNP follow a linear stationary process; that is, in all of the above studies, optimal forecasts of variables are assumed to be a linear function of their lagged values. In this paper I suggest a modest alternative to these currently popular approaches to nonstationarity, exploring the consequences of specifying that first differences of the observed series follow a nonlinear stationary process rather than a linear stationary process. A variety of parameterizations for characterizing nonlinear dynamics have recently been proposed, and there has now accumulated abundant evidence that departures from linearity are an important feature of many key macro series. Studies establishing such nonlinearities include the bispectral analysis of Hinich and Patterson (1985), documentation of business cycle asymmetries by Neftci (1984) and Sichel (1987), the ARCH-M model of Engle, Lilien, and Robins (1987), Stock's (1987) time transformation, chaos models (Brock and Sayers, 1988), Gallant and Tauchen's (1987) "seminonparametric" approach to modeling dynamics, and Quah's (1987) "clinging" process.

1I am indebted to John Cochrane, Angus Deaton, Robert Engle, Marjorie Flavin, Kevin Hassett, and anonymous referees for comments on earlier drafts of this paper. This material is based upon work supported by the National Science Foundation under Grant No. SES-8720731. The Government has certain rights to this material.


<!-- p:2 -->


The nonlinearities with which my paper is concerned arise if the process is subject to discrete shifts in regime—episodes across which the dynamic behavior of the series is markedly different. My basic approach is to use Goldfeld and Quandt's (1973) Markov switching regression to characterize changes in the parameters of an autoregressive process. For example, the economy may either be in a fast growth or slow growth phase, with the switch between the two governed by the outcome of a Markov process. Building upon ideas developed by Cosslett and Lee (1985), a nonlinear filter and smoother are presented for uncovering optimal statistical estimates of the state of the economy based on observations of output. As in the Kalman filter, one is using the time path of an observed series to draw inference about an unobserved state variable. But whereas the Kalman filter is a linear algorithm for generating estimates of a continuous unobserved state vector, the filter and smoother in this paper provide nonlinear inference about a discrete-valued unobserved state vector.

A very similar stochastic specification has also been explored by Aoki (1967, p.  ts  o (   (  1)  ( o these researchers was quite different from the one suggested here. Aoki discussed control of such systems but did not develop the estimation algorithm presented in this paper. Tong treated the shifts in regime as directly observable, whereas the core of my paper addresses optimal probabilistic inference about such shifts based on the observed behavior of GNP. Sclove calculated what the likelihood function would have been if the regimes were observable, and then assumed that the actual historical regimes were those that would make this joint likelihood of GNP along with unobserved regimes as big as possible. My approach, by contrast, is to solve for the actual marginal likelihood function for GNP, maximize this likelihood function with respect to population parameters, and then use these parameters and the data to draw the optimal statistical inference about the unobserved regimes.

My algorithm might also be viewed as formalizing the statistical identification of "turning points" of a time series. Modern treatments by Wecker (1979), Neftci (1982), and Diebold and Rudebusch (1987) provide references to some of the earlier work and interest on this question. Wecker discussed optimal forecasts of an "indicator function" (e.g., z, = 1 if both yt−1 &lt; y, and y, &gt; yt+ 1). Wecker's indicator is imposed more or less arbitrarily on an otherwise linear process; in my ss   s t s   ,   t ons inherent in the data-generating process. Neftci (1982) analyzed the case where (1) only the most recent turning point influences the density function for current observations, and (2) there is known to be a possibility of at most one turning point observed during a given interval (t1, t2). These assumptions could also be imposed as a special case of the general framework studied here, generating Neftci's algorithm for dating turning points as a special case of the basic filter used in this study.


<!-- p:3 -->


The filter also has a clear analog in the analysis of Liptser and Shiryayev (1977), who developed a nonlinear continuous-time filter for a similar problem.2 The discrete-time filter developed here has three distinct advantages over their treatment. First, if one used Liptser and Shiryayev's formula (which is only strictly valid for continuous time) to approximate discrete changes over short intervals of time, in principle one could end up generating a probability outside the unit interval. By contrast, all probabilities generated by the filter and smoother proposed in this paper are exact, and so lie in [0, 1] by construction. Second, a natural byproduct of the discrete-time filter used here is evaluation of the sample likelihood, permitting ready estimation and hypothesis testing about the system's parameters. Third, the specification adopted in this paper fits in neatly as a complement to conventional time series tools and techniques; for example, present value calculations turn out to be quite straightforward.

My approach could also be viewed as a natural extension of Neftci's (1984) analysis of U.S. unemployment data. In Neftci's specification, the economy is said to be in state 1 whenever unemployment is rising and in state 2 whenever unemployment is falling, with transitions between these two states modeled as the outcome of a second-order Markov process. In my paper, by contrast, the unobserved state is only one of many influences governing the dynamic process followed by output, so that even when the economy is in the "fast growth" state, output in principle might be observed to decrease.

The paper applies the technique to postwar U.S. data on real GNP. One possible outcome of maximum likelihood estimation of parameters might have been the identification of long-term trends in the U.S. economy, separating per it s      s o    oot what was found. Instead, the best empirical fit to the data is obtained when the growth states of the Markov process are associated in a very direct way with the business cycle. A positive growth rate is associated with normal times, and a negative growth rate associated with recessions. Indeed, the best statistical estimates of which quarters were historically characterized by negative growth states for the U.S. economy are remarkably similar to NBER dating of business cycles, and could be used as an alternative objective algorithm for dating business cycles. The results complement the findings by Nelson and Plosser (1982) and Campbell and Mankiw (1987a, b), who concluded that business cycles are associated with a large permanent effect on the long run level of output. The estimates also provide empirical support for the proposition that the dynamics of recessos sit   s io    u   scal sense, and reinforce Neftci's (1984) and Sichel's (1987) evidence on the asymmetry of U.S. business cycles.

2See Liptser and Shiryayev (1977, Theorem (9.1), p. 333).


<!-- p:4 -->


The plan of the paper is as follows. Section 2 specifies the basic model of trend explored in the paper, and compares it with an ARIMA model with normally distributed innovations. Section 3 characterizes the optimal forecast of the future level of a series generated by such a trend. Section 4 presents one example of how this nonlinear trend might interact with a linear process to generate data, and discusses maximum likelihood estimation and inference about the unobserved state for this case. Section 5 applies the technique to postwar U.S. data on real GNP. Section 6 explores the implications for defining and measuring business cycles, and provides a comparison of alternative approaches. Section 7 presents diagnostics comparing the model with the standard ARIMA specification, while Section 8 addresses the long-term consequences of an economic recession. Brief conclusions are offered in Section 9.

## 2. A MARKOV MODEL OF TREND

Let n, denote the trend component of a particular time series y. I will say that n, obeys a Markov trend in levels if

$$( 2 . 1 ) \quad n _ { t } = \alpha _ { 1 } \cdot s _ { t } + \alpha _ { 0 } + n _ { t - 1 }$$

where s, = 0 or 1 denotes the unobserved state of the system.3 I assume that the transition between states is governed by a first-order Markov process:

$$\text {transition between states is governed by a first-order
} & \quad \text {Prob} \left [ S _ { t } = 1 | S _ { t - 1 } = 1 \right ] = p , \\ & \quad \text {Prob} \left [ S _ { t } = 0 | S _ { t - 1 } = 1 \right ] = 1 - p , \\ & \quad \text {Prob} \left [ S _ { t } = 0 | S _ { t - 1 } = 0 \right ] = q , \\ & \quad \text {Prob} \left [ S _ { t } = 1 | S _ { t - 1 } = 0 \right ] = 1 - q . \\ \text {Generalization to a higher-order process and to } &$$

Generalization to a higher-order process and to more than two states is discussed below.

I will describe ñ, ≡ exp(n,) as exhibiting a Markov trend in logs.

The stochastic process for S, (equation 2.2) is strictly stationary, and admits the following AR(1) representation:

$$( 2 . 3 ) \quad s _ { t } = ( 1 - q ) + \lambda s _ { t - 1 } + v _ { t } ,$$

$$( 2 . 4 ) \quad \lambda \equiv - 1 + p + q ,$$

where conditional on S,-1 = 1,

$$V _ { t } & = ( 1 - p ) \quad \text {with probability } p , \\ V _ { t } & = - p \quad \text {with probability } 1 - p ,$$

conditional on S,-1 = 0,

$$V _ { t } & = - ( 1 - q ) \quad \text {with probability } q , \\ V _ { t } & = q \quad \text {with probability } 1 - q .$$

3I adopt the usual notational convention that for discrete-valued variables, capital letters denote the random variable and small letters a particular realization. Both interpretations of course apply to euu  u       '(   woon


<!-- p:5 -->


On the basis of representation (2.3), then, one can view (2.1) as a special case of a standard ARIMA model, albeit with a somewhat unusual probability distribution of the innovation sequence {V, }. It is therefore useful to describe in some detail the differences between (2.3) and an AR(1) process driven by normally distributed innovations.

Before doing so, however, note some of the essential properties of (2.3). From (2.3) and the fact that E0V, = 0 for all t &gt; 0, we see

$$E _ { 0 } S _ { t } = \frac { ( 1 - q ) ( 1 - \lambda ^ { t } ) } { ( 1 - \lambda ) } + \lambda ^ { t } E _ { 0 } S _ { 0 }$$

where E0 denotes the expectation conditional on information available at date zero (which need not include observation of s0). Observing that E0S, can be interpreted as the probability that S, = 1 given information available at time zero (denoted P0[S, = 1]), (2.5) can be rewritten

$$P _ { 0 } [ S _ { t } = 1 ] = \pi + \lambda ^ { t } ( \pi _ { 0 } - \pi )$$

where

$$\pi & \equiv ( 1 - q ) / ( 1 - p + 1 - q ) , \\ \pi _ { 0 } & \equiv P _ { 0 } [ S _ { 0 } = 1 ] .$$

Asymptotically, then, the conditional probability converges to the limiting unconditional probability given by

$$P \left [ S _ { t } = 1 \right ] = \pi .$$

As in the case of an ARIMA process with normally distributed innovations, the error term V, in equation (2.3) is uncorrelated with lagged values of S,,

$$E \left [ V _ { t } | S _ { t - j } = 1 \right ] = E \left [ V _ { t } | S _ { t - j } = 0 \right ] = 0 \quad \text {for} \quad j = 1 , 2 , \dots \, .$$

In contrast to the normal case, however, V, is not statistically independent of lagged values of S, e.g.,

$$E \left [ V _ { t } ^ { 2 } | S _ { t - 1 } = 1 \right ] = p \left ( 1 - p \right ) ,$$

$$E \left [ V _ { t } ^ { 2 } | S _ { t - 1 } = 0 \right ] = q ( 1 - q ) .$$

The latter property makes an important difference when noise is added to the system. For example, in the model that I will fit to data, I assume that the state s, is not observed directly, but instead is one of many factors influencing an observed series. To appreciate the difference that arises in this case between (2.1) and an ARIMA model with normal innovations, consider the simplest possible example:

$$( 2 . 8 ) \quad y _ { t } = s _ { t } + \varepsilon _ { t } .$$

H  ~   (   is s   s  e ' ) is an i.i.d. series independent of V,-, for all j. Applying (1 − λL) where L is the lag operator (L jx, = xt−j) to (2.8),


<!-- p:6 -->


$$y _ { t } - \lambda \, y _ { t - 1 } = ( 1 - q ) + v _ { t } + \varepsilon _ { t } - \lambda \varepsilon _ { \varepsilon _ { t - 1 } } .$$

The error term on the right-hand side of (2.9) admits an MA(1) representation,

$$v _ { t } + \varepsilon _ { t } - \lambda \varepsilon _ { t - 1 } = u _ { t } - \theta u _ { t - 1 } ,$$

or

$$( 2 . 1 0 ) \quad u _ { t } = v _ { t } + \theta v _ { t - 1 } + \theta ^ { 2 } v _ { t - 2 } + \theta ^ { 3 } v _ { t - 3 } + \cdots + \varepsilon _ { t } + ( \theta - \lambda ) \varepsilon _ { t - 1 } \\ + ( \theta - \lambda ) \theta \varepsilon _ { t - 2 } + ( \theta - \lambda ) \theta ^ { 2 } \varepsilon _ { t - 3 } + \cdots \\$$

where θ is the value less than one in absolute value that, along with σ2, satisfies

$$( 2 . 1 1 ) \quad ( 1 + \theta ^ { 2 } ) \sigma _ { u } ^ { 2 } = ( 1 + \lambda ^ { 2 } ) \sigma _ { e } ^ { 2 } + \sigma _ { v } ^ { 2 } \\$$

$$\sigma _ { u } ^ { 2 } = - \lambda \sigma _ { e } ^ { 2 } ,$$

where

$$\sigma _ { v } ^ { 2 } & = E \left ( V _ { t } ^ { 2 } \right ) \\ & = p \left ( 1 - p \right ) \pi + q ( 1 - q ) ( 1 - \pi ) .$$

As in the case of V,, the innovation U, is uncorrelated with U,\_, for j &gt; 0, but is not independent. An earlier version of this paper illustrated the relevance of this point by way of example, showing that while E[U(U,-1− θU,-2)] = 0, it nonetheless is the case that

$$E \left [ U _ { t } ( U _ { t - 1 } - \theta U _ { t - 2 } ) ^ { 2 } \right ] = \theta \left ( \frac { ( 1 - p ) ( 1 - q ) ( \ p - q ) } { ( 1 - \lambda ) } \right ) \left ( \frac { \theta \lambda ^ { 2 } - 2 \lambda - 1 } { 1 - \theta \lambda } \right ) ,$$

in general not zero. What this means in practical terms is that while one could use the ARMA(1, 1) representation

$$y _ { t } - \lambda \, y _ { t - 1 } = ( 1 - q ) + u _ { t } - \theta u _ { t - 1 }$$

as a basis for forecasting y,+j as a linear function of y, yt–1, ..., these forecasts are not optimal; nonlinear forecasts that exploit the serial dependence of the white noise series U, are superior.4 From (2.6), these optimal forecasts are given by

$$E _ { t } y _ { t + j } = \pi + \lambda ^ { j } \cdot \left \{ \, P [ S _ { t } = 1 | y _ { t } , \, y _ { t - 1 } , \dots ] - \pi \, \right \}$$

where P[S, = 1|y, yt-1,...] is the nonlinear function of y, yt-1,... to be presented in Section 4.

Thus, the essential differences between the specification (2.1) and a standard ARIMA model with normal innovations are twofold. First, (2.1) specifies that the growth rate n,- n,-1 need not change every period, but rather only does so in response to occasional, discrete events. Second, when added to a linear normal process, (2.1) generates a nonlinear process for the observed series for which, while an ARIMA representation exists, it does not generate optimal forecasts of the future value of the series.

4See Granger (1983) on this general issue.


<!-- p:7 -->


## 3. FORECASTING AND PRESENT VALUE CALCULATIONS

### 3.1. Markov Trend in Levels

Let i, denote the cumulative number of "ones" since time zero,

$$Let i , \detone the cumulative number of ``ones'' since time z \\ i _ { t } \equiv s _ { 1 } + s _ { 2 } + \cdots + s _ { r } , \\ \text {so from (2.1),} \\ ( 3 . 1 ) \quad n _ { t } = n _ { 0 } + \alpha _ { 1 } + \alpha _ { t } . \\ \text {Recall from (2.6) that} \\ ( 3 . 2 ) \quad E \left \{ S _ { t } | \text {Prob} \left [ S _ { 0 } = 1 \right ] = \pi _ { 0 } \right \} = \pi + \lambda ^ { t } ( \pi _ { 0 } - \pi ) \\ \text {and so from (3.1),} \\ ( 3 . 3 ) \quad E _ { 0 } \{ N _ { 1 } | E _ { 0 } [ N _ { 0 } ] = n _ { 0 } , \text {Prob} \left [ S _ { 0 } = 1 \right ] = \pi _ { 0 } \right \} \\ = n _ { 0 } + \alpha _ { 1 } \left [ \pi t + \sum _ { \tau = 1 } ^ { t } \lambda ^ { t } ( \pi _ { 0 } - \pi ) \right ] + \alpha _ { 0 } t \\ = n _ { 0 } + [ \alpha _ { 1 } \pi + \alpha _ { 0 } ] t + \left [ \alpha _ { 1 } \lambda ( 1 - \lambda ^ { t } ) / ( 1 - \lambda ) \right ] [ \pi _ { 0 } - \pi ]$$

$$= n _ { 0 } + [ \alpha _ { 1 } \pi + \alpha _ { 0 } ] t + [ \alpha _ { 1 } \lambda ( 1 - \lambda ^ { t } ) / ( 1 - \lambda ) ] [ \pi _ { 0 } - \pi ] .$$

The limiting growth rate as t → ∞ is seen from (3.3) to be independent of information about the state of the system at date 0:

$$\lim _ { t \to \infty } E \left [ ( N _ { t + 1 } - N _ { t } ) | n _ { 0 } , \pi _ { 0 } \right ] = \alpha _ { 1 } \pi + \alpha _ { 0 } .$$

Intuitively, we know from equation (2.6) that for large t the economy will be in state 1 with probability π, in which case the growth rate would be α1 + αo, whereas the economy will be in state 0 with probability 1 - π, in which case the growth rate would be α0; hence the expected growth rate is α1π + α0. Furthermore, if one had no useful information about the state of the system at date 0, π0 = π and (3.3) implies that this limiting growth rate would be the basis for constructing forecasts of N, for all finite t. On the other hand, if one did have useful information that, say, π0 &gt; π, then for α1λ &gt; 0, E[N,|P0(S0 = 1) = π0] wo l 1    =  =   l s  yhe difference growing with t as the term (1 - λ') goes to unity. In particular, if we co d dn d ( =   = t  dd d mdat S0 = 0 (π0 = 0), we see

$$( 3 . 4 ) \quad \lim _ { t \to \infty } \left \{ \, E [ N _ { t } | S _ { 0 } = 1 ] - E [ N _ { t } | S _ { 0 } = 0 ] \right \} = \alpha _ { 1 } \lambda / ( 1 - \lambda ) .$$

So, while information about the state of the economy at date 0 has no effect on the long run growth rate (N,+1 − N,), it does exert a permanent effect on the level N.5

An analogous result of course characterizes a standard ARIMA( p,1, q) process. See Beveridge

and Nelson (1981, p. 155).


<!-- p:8 -->


The discounted present value can also be evaluated from (3.3):

$$The d i s c u n t ed p e r s e n v a l u a d e v a l u a d e f o r ( 3 . 3 ) & \\ ( 3 . 5 ) & \quad E \left \{ \sum _ { \iota = 0 } ^ { \infty } \beta ^ { \prime } N _ { \iota } | n _ { 0 } , \pi _ { 0 } \right \} = \frac { n _ { 0 } } { ( 1 - \beta ) } \\ & + \alpha _ { 1 } \left [ \frac { \beta ( 1 - q ) } { ( 1 - \beta ) ^ { 2 } ( 1 - \beta \lambda ) } + \frac { \beta \lambda \pi _ { 0 } } { ( 1 - \beta ) ( 1 - \beta \lambda ) } \right ] \\ & + \frac { \alpha _ { 0 } \beta } { ( 1 - \beta ) ^ { 2 } } .$$

### 3.2. Markov Trend in Logs

Here I characterize forecasts of future values of a series that follows a Markov trend in logs by exploiting a simple vector recursion in expected values.

Let P[A, B] denote the probability that events A and B will occur together, conditional on information available at r. Note that the following recursion,

$$( 3 . 6 ) \quad P _ { 0 } [ \, I _ { t } = i , \, S _ { t } = 1 \, ] = & \, p \cdot P _ { 0 } [ \, I _ { t - 1 } = i - 1 , \, S _ { t - 1 } = 1 \, ] \\ & + ( 1 - q ) \cdot P _ { 0 } [ \, I _ { t - 1 } = i - 1 , \, S _ { t - 1 } = 0 \, ] ,$$

holds for t = 1, 2, ... and i = 1, 2, .. . , t. For i = 0 we of course have

$$( 3 . 7 ) \quad P _ { 0 } [ I _ { t } = 0 , \, S _ { t } = 1 ] = 0$$

holding for t = 1, 2,... . Similarly, the recursion

$$P _ { 0 } [ I _ { t } = i , \, S _ { t } = 0 ] = & ( 1 - p ) \cdot P _ { 0 } [ I _ { t - 1 } = i , \, S _ { t - 1 } = 1 ] \\ & + q \cdot P _ { 0 } [ \, I _ { t - 1 } = i , \, S _ { t - 1 } = 0 ] ,$$

holds for t = 1, 2, ... and i = 0, 1, ... , t − 1, with

$$( 3 . 9 ) \quad P _ { 0 } [ I _ { t } = t , \, S _ { t } = 0 ] = 0$$

for t = 1, 2, . . . .

Let 1 ≡ exp (α1) and 0 ≡ exp(α0). Multiplying equation (3.6) by , summing for i = 1, 2, ... , t, and using (3.7) yields

$$\ m i g \text { for } i = 1 , 2 , \dots , t , \text { and using } ( 3 . 7 ) \text { yields} \\ ( 3 . 1 0 ) \quad & \sum _ { i = 0 } ^ { t } \hat { \alpha } _ { 1 } ^ { i } \hat { \alpha } _ { 0 } ^ { \prime } \cdot P _ { 0 } [ I _ { t } = i , \, S _ { t } = 1 ] \\ & = [ \hat { \alpha } _ { - 1 } \hat { \alpha } _ { 0 } p ] \cdot \sum _ { j = 0 } ^ { t - 1 } \hat { \alpha } _ { j } ^ { j } \hat { \alpha } _ { 0 } ^ { - 1 } \cdot P _ { 0 } [ I _ { t - 1 } = j , \, S _ { t - 1 } = 1 ] \\ & + [ \hat { \alpha } _ { 1 } \hat { \alpha } _ { 0 } ( 1 - q ) ] \cdot \sum _ { j = 0 } ^ { t - 1 } \hat { \alpha } _ { 1 } ^ { j } \hat { \alpha } _ { 0 } ^ { - 1 } \cdot P _ { 0 } [ I _ { t - 1 } = j , \, S _ { t - 1 } = 0 ] . \\ \text {Similarly, multiplying } ( 3 . 8 ) \text { by } \hat { \alpha } _ { 0 } ^ { i } \hat { \alpha } _ { 0 } ^ { \prime } , \text { summing } \text { for } i = 0 , 1 , \dots , t - 1 , \text { and using}$$

Similarly, multiplying (3.8) by , summing for i = 0, 1,..., t − 1, and using


<!-- p:9 -->


(3.9) gives

$$( 3 . 9 ) \text { gives } & & ( 3 . 9 ) \text { gives } & & ( 3 . 1 ) & \sum _ { i = 0 } ^ { t } \hat { \alpha } _ { 1 } ^ { i } \hat { \alpha } _ { 0 } ^ { t } \cdot P _ { 0 } [ I _ { t } = i , \, S _ { t } = 0 ] \\ & & = [ ( 1 - p ) \hat { \alpha } _ { 0 } ] \cdot \sum _ { j = 0 } ^ { t - 1 } \hat { \alpha } _ { 1 } ^ { j } \hat { \alpha } _ { 0 } ^ { t - 1 } \cdot P _ { 0 } [ I _ { t - 1 } = j , \, S _ { t - 1 } = 1 ] \\ & & + [ q \hat { \alpha } _ { 0 } ] \cdot \sum _ { j = 0 } ^ { t - 1 } \hat { \alpha } _ { 1 } ^ { j } \hat { \alpha } _ { 0 } ^ { t - 1 } \cdot P _ { 0 } [ I _ { t - 1 } = j , \, S _ { t - 1 } = 0 ] . \\ \text {Define}$$

Define

$$( 3 . 1 2 ) \quad M _ { 0 } ( t , s ) = \sum _ { i = 0 } ^ { t } \hat { \alpha } _ { 1 } ^ { i } \hat { \alpha } _ { 0 } ^ { t } \cdot P _ { 0 } [ \, I _ { t } = i , \, S _ { t } = s \, ] \\$$

for s = 0,1 and write (3.10) and (3.11) as

$$\begin{bmatrix} M _ { 0 } ( t , 1 ) \\ M _ { 0 } ( t , 0 ) \end{bmatrix} & = \begin{bmatrix} \hat { \alpha } _ { 0 } \hat { \alpha } _ { 1 } p & \hat { \alpha } _ { 0 } \hat { \alpha } _ { 1 } ( 1 - q ) \\ \hat { \alpha } _ { 0 } ( 1 - p ) & \hat { \alpha } _ { 0 } q \end{bmatrix} \begin{bmatrix} M _ { 0 } ( t - 1 , 1 ) \\ M _ { 0 } ( t - 1 , 0 ) \end{bmatrix} ,$$

or, defining

$$B \equiv \begin{bmatrix} \hat { \alpha } _ { 1 } p & \hat { \alpha } _ { 1 } ( 1 - q ) \\ ( 1 - p ) & q \end{bmatrix} ,$$

we have

$$\begin{array} { r l } & { w i t h a n t } \\ & { ( 3 . 1 3 ) } & { \begin{bmatrix} M _ { 0 } ( t , 1 ) \\ M _ { 0 } ( t , 0 ) \end{bmatrix} = \hat { \alpha } _ { 0 } B \begin{bmatrix} M _ { 0 } ( t - 1 , 1 ) \\ M _ { 0 } ( t - 1 , 0 ) \end{bmatrix} . } \\ & { \quad } \\ & { \quad } \\ & { ( 3 . 1 3 ) } & { \begin{bmatrix} M _ { 0 } ( t , 0 ) \end{bmatrix} = \hat { \alpha } _ { 0 } B \begin{bmatrix} M _ { 0 } ( t - 1 , 0 ) \\ M _ { 0 } ( t - 1 , 0 ) \end{bmatrix} . } \end{array}$$

Note from (3.12) that M0(0, s) = P0[S0 = s]. Thus (3.13) has the solution

$$\left [ \begin{matrix} M _ { 0 } ( t , 1 ) \\ M _ { 0 } ( t , 0 ) \end{matrix} \right ] = \hat { \alpha } _ { 0 } ^ { t } B ^ { t } \left [ \begin{matrix} \pi _ { 0 } \\ 1 - \pi _ { 0 } \end{matrix} \right ] .$$

Solving for the roots of |μI − B| = 0, we see

$$\mu _ { 1 } + \mu _ { 2 } = q + p \hat { \alpha } _ { 1 } , \\ \mu _ { 1 } \mu _ { 2 } = \hat { \alpha } _ { 1 } ( - 1 + p + q ) .$$

Following Chiang (1980, pp. 148–152), write

$$( 3 . 1 4 ) \quad B ^ { t } = T \begin{bmatrix} \mu _ { 1 } ^ { t } & 0 \\ 0 & \mu _ { 2 } ^ { t } \end{bmatrix} T ^ { - 1 } \\$$

where

$$t$$

$$T & = \left [ \begin{array} { c c c } ( \mu _ { 1 } - q ) & ( \mu _ { 2 } - q ) \\ ( 1 - p ) & ( 1 - p ) \end{array} \right ] , \\ T ^ { - 1 } & = \frac { 1 } { ( \mu _ { 1 } - \mu _ { 2 } ) ( 1 - p ) } \left [ \begin{array} { c c c } ( 1 - p ) & ( q - \mu _ { 2 } ) \\ - ( 1 - p ) & ( \mu _ { 1 } - q ) \end{array} \right ] .$$


<!-- p:10 -->


The expected value of the level of a series that follows a Markov trend in logs is then seen to be

$$1 \text { then see } & 0 \text { 0C} \\ & ( 3 . 1 5 ) \quad E _ { 0 } \hat { N } _ { t } = \hat { n } _ { 0 } \left [ M _ { 0 } ( t , 1 ) + M _ { 0 } ( t , 0 ) \right ] \\ & = \hat { n } _ { 0 } \cdot \left [ 1 \ \ 1 \right ] \hat { \alpha } _ { 0 } ^ { t } B ^ { \prime } \left [ \pi _ { 0 } \quad 1 - \pi _ { 0 } \right ] ^ { \prime } \\ & = \frac { \hat { n } _ { 0 } \hat { \alpha } _ { 0 } ^ { t } \left \{ ( k _ { 0 } - \mu _ { 2 } ) \mu _ { 2 } ^ { t } - ( k _ { 0 } - \mu _ { 1 } ) \mu _ { 1 } ^ { t } \right \} } { ( \mu _ { 1 } - \mu _ { 2 } ) } \\$$

where

$$k _ { 0 } & \equiv [ \mu _ { 1 } \mu _ { 2 } / \hat { \alpha } _ { 1 } ] [ \pi _ { 0 } + \hat { \alpha } _ { 1 } ( 1 - \pi _ { 0 } ) ] \\ & = [ - 1 + p + q ] [ \pi _ { 0 } + \hat { \alpha } _ { 1 } ( 1 - \pi _ { 0 } ) ] \, .$$

Normalizing μ1 &gt; μ2, we see that, as in the case of a Markov trend in levels, the long-run growth rate is independent of information about the initial state:

$$\lim _ { t \to \infty } \frac { E _ { 0 } \hat { N } _ { t + 1 } } { E _ { 0 } N _ { t } } = \hat { \alpha } _ { 0 } \mu _ { 1 }$$

but a change in the current state exerts a permanent effect on the future level of the series,

$$\lim _ { t \to \infty } \frac { E _ { 0 } \{ \, \hat { N } _ { t } | \pi _ { 0 } = 1 \} } { E _ { 0 } \{ \, \hat { N } _ { t } | \pi _ { 0 } = 0 \} } = \frac { \mu _ { 1 } - ( - 1 + p + q ) } { \mu _ { 1 } - \hat { \alpha } _ { 1 } ( - 1 + p + q ) } \, .$$

From (3.15), the present value is

$$E _ { 0 } \sum _ { t = 0 } ^ { \infty } \beta ^ { t } \hat { N } _ { t } = \frac { \hat { n } _ { 0 } ( 1 - k _ { 0 } \beta \hat { \alpha } _ { 0 } ) } { 1 - \beta \hat { \alpha } _ { 0 } ( \ p \hat { \alpha } _ { 1 } + q ) + \beta ^ { 2 } \hat { \alpha } _ { 0 } ^ { 2 } ( - 1 + p + q ) \hat { \alpha } _ { 1 } } \, .$$

4. ESTIMATION, FILTERING, AND SMOOTHING

### 4.1. Stochastic Specification

Several options are available for combining the trend term n, with another stochastic process. Here I discuss the approach that results in the computationally simplest maximum likelihood estimation.

Suppose we have observations on a time series { }. Specify

$$\tilde { y } _ { t } = n _ { t } + \tilde { z } _ { t }$$

where n, is as given in (2.1) and (2.2) and ž, follows a zero mean ARIMA(r, 1, 0) process:

$$\tilde { z } _ { t } - \tilde { z } _ { t - 1 } = \phi _ { 1 } ( \tilde { z } _ { t - 1 } - \tilde { z } _ { t - 2 } ) + \phi _ { 2 } ( \tilde { z } _ { t - 2 } - \tilde { z } _ { t - 3 } ) + \cdots \\ + \phi _ { r } ( \tilde { z } _ { t - r } - \tilde { z } _ { t - r - 1 } ) + \varepsilon _ { t } .$$


<!-- p:11 -->


I take {ε, } to be an i.i.d. N(0, σ2) sequence that is independent of { n,+j} for all j. Differencing (4.1) and rewriting (4.2) we obtain

$$y _ { t } = \alpha _ { 1 } s _ { t } + \alpha _ { 0 } + z _ { t } , \\ z _ { t } = \phi _ { 1 } z _ { t - 1 } + \phi _ { 2 } z _ { t - 2 } + \cdots + \phi _ { r } z _ { t - r } + \varepsilon _ { t } ,$$

where y, ≡ yt − yt − 1 and z, ≡ ž, − z t− 1.

The econometrician is presumed to observe y, but not z, or s,. I first discuss a filter whereby the econometrician can draw probabilistic inference about the o vo o     ow s o ' s onn the sample likelihood is a natural byproduct of the filter. The analysis is closely related to the discussion by Cosslett and Lee (1985), who derived a recursion to evaluate the likelihood function for the case where (4.3) is a standard stationary regression equation with no lagged dependent variables.

### 4.2. Filtering

The basic filter accepts as input the joint conditional probability

$$P [ S _ { t - 1 } = s _ { t - 1 } , \, S _ { t - 2 } = s _ { t - 2 } , \dots , S _ { t - r } = s _ { t - r } | y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } ]$$

and has as output

$$P \left [ S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r + 1 } = s _ { t - r + 1 } | y _ { t } , \, y _ { t - 1 } , \dots , \, y _ { - r + 1 } \right ]$$

along with, as a byproduct, the conditional likelihood of y,:

$$f ( y _ { t } | y _ { t - 1 } , y _ { t - 2 } , \dots , y _ { - r + 1 } ) .$$

Note well the notation: [s, st-1 ..., st-r+1] refers to the r most recent values of s whereas [y, yt-1,..., y −r+1] denotes the complete history of y observed through date t. By "P[S, = sp, St−1 = st−1, . . ., St−r+1 = st−r+1|yr, yt−1,. . . , y −r+1]" I refer to a vector consisting of 2' elements. For example, suppose r = 4. The element indexed by (1, 0, 1, 1) denotes the probability that S,-1 = 1, S,-2 = 0, S,– 3 = 1, and S,–4 = 1. These 16 probabilities sum to unity by construction, and represent an inference about the unobserved state (s,-1, st-2, st-3, s--4) based on observations of y through date t – 1. The algorithm is as follows.

STEP 1: Calculate

$$P \left [ S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r } = s _ { t - r } | y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } \right ] \\ = P \left [ S _ { t } = s _ { t } | S _ { t - 1 } = s _ { t - 1 } \right ] \times P \left [ S _ { t - 1 } = s _ { t - 1 } , \, S _ { t - 2 } = s _ { t - 2 } , \dots ,$$

$$S _ { t - r } = s _ { t - r } | y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } \right ]$$

where P[S, = s,|St−1 = st−1] is given by (2.2). (Note P[S, = s,|St−1 = st−1] = P[S, = s,|St−1 = st−1, St−2 = st−2, ., St−r = st−r, yt−1, yt−2, . . . , y −r+1] by the independence and first-order Markov assumptions.)


<!-- p:12 -->


STEP 2: Calculate the joint conditional density-distribution of y, anc (S1, St− 1, . . . , St− r):

$$( S _ { t } , S _ { t - 1 } , \dots , S _ { t - r } ) ^ { t } & \quad \\ f ( y _ { t } , S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r } = s _ { t - r } | y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } ) \\ & = f ( y _ { t } | S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r } = s _ { t - r } , \, y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } ) \\ & \quad \times P [ S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r } = s _ { t - r } , | y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } ]$$

where we know

$$w h e r w & \quad f ( y _ { t } | S _ { t } = s _ { t } , S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r } = s _ { t - r } , y _ { t - 1 } , y _ { t - 2 } , \dots , y _ { - r + 1 } ) \\ & = \frac { 1 } { \sqrt { 2 \pi \sigma } } \exp \left [ - \, \frac { 1 } { 2 \sigma ^ { 2 } } \left ( ( y _ { t } - \alpha _ { t } s _ { t } - \alpha _ { 0 } ) - \phi _ { 1 } ( y _ { t - 1 } - \alpha _ { 1 } s _ { t - 1 } - \alpha _ { 0 } ) \right ) \\ & \quad - \cdots - \phi _ { r } ( y _ { t - r } - \alpha _ { 1 } s _ { t - r } - \alpha _ { 0 } ) ) ^ { 2 } \right ] .$$

STEP 3: We then have

$$\text {Step} \, 3 \colon \text {We then have} & & f ( y _ { t } | y _ { t - 1 } , y _ { t - 2 } , \dots , y _ { - r + 1 } ) \\ & = \sum _ { s , t = 0 } ^ { 1 } \sum _ { s _ { t - 1 } = 0 } ^ { 1 } \cdots \sum _ { s _ { t - r } , - r = 0 } ^ { 1 } f ( y _ { t } , S _ { t } = s _ { t } , S _ { t - 1 } = s _ { t - 1 } , \dots , \\ & \quad S _ { t - r } , = s _ { t - r } , | y _ { t - 1 } , y _ { t - 2 } , \dots , y _ { - r + 1 } )$$

STEP 4: Thus

$$P [ S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r } = s _ { t - r } | y _ { t } , \, y _ { t - 1 } , \dots , \, y _ { - r + 1 } ] \\ = \frac { f ( y _ { t } , S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , \, S _ { t - r } = s _ { t - r } | y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } ) } { f ( \, y _ { t } | y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } ) } .$$

STEP 5: The desired output is then obtained from

$$S _ { \text {EP} } \, J \colon \, & \text {The decimal output of } \, | y _ { 0 } , y _ { 1 } , \dots , S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r + 1 } = s _ { t - r + 1 } | y _ { t } , y _ { t - 1 } , \dots , y _ { - r + 1 } \ ] \\ & P [ S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r + 1 } = s _ { t - r + 1 } | y _ { t } , y _ { t - 1 } , \dots , y _ { - r + 1 } ] \\ & = \sum _ { s _ { t - r } = 0 } ^ { 1 } \, P [ S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r } = s _ { t - r } | y _ { t } , y _ { t - 1 } , \dots , y _ { - r + 1 } ] \cdot$$

One could start up the algorithm with

$$P [ S _ { 0 } = s _ { 0 } , \, S _ { - 1 } = s _ { - 1 } , \dots , S _ { - r + 1 } = s _ { - r + 1 } | y _ { 0 } , \, y _ { - 1 } , \dots , \, y _ { - r + 1 } ]$$

though evaluating this expression proves to be somewhat involved computationally. I have instead in this paper adopted the simpler expedient of starting the filter with the unconditional probability P[S0 = so, S\_1 = s-1,..., S\_r+1 = s\_r +1], evaluated as follows. Set P[S \_r+1 = 1] equal to the limiting probability π of the Markov process from equation (2.7), and of course set P[S\_r+1 = 0] =


<!-- p:13 -->


$$1 - \pi . \text { Then for } \tau = - r + 2 , - r + 3 , \dots , 0 \text { calculate } \\ P [ S , = s _ { \tau } , S _ { \tau - 1 } = s _ { \tau - 1 } , \dots , S _ { - r + 1 } = s _ { - r + 1 } ] \\ = P [ S , = s _ { \tau } , | S _ { - 1 } = s _ { - 1 } ] \\ \times P [ S _ { \tau - 1 } = s _ { \tau - 1 } , S _ { - 2 } = s _ { \tau - 2 } , \dots , S _ { - r + 1 } = s _ { - r + 1 } ] .$$

The final product of this subiteration,

$$P [ S _ { 0 } = s _ { 0 } , \, S _ { - 1 } = s _ { - 1 } , \dots , S _ { - r + 1 } = s _ { - r + 1 } ] ,$$

is then used as input for the basic filter for t = 1. The iteration on the basic filter is then repeated for t = 1,2,..., T.

For some applications, one might want to allow the possibility of a permanent change in regime (e.g., q = 1). For such applications, we should not set P[S\_r+1 = 1] from equation (2.7), but should instead treat it as a separate parameter (say π–r+1) to be estimated along with the others.

It is easy to verify that the output of the filter is always a well-defined probability distribution with the terms nonnegative and summing to unity.

Neftci's (1982) algorithm for dating business cycle turning points can be obtained as a special case of the basic filter by setting q = 1 and r = 0.

One byproduct of the filter is evaluation of the conditional likelihood in Step 3. The sample conditional log likelihood is

which can be maximized numerically with respect to the unknown parameters (α1, α0, P, q, σ, φ1, φ2, . .. , φ), and optionally π−r+1 as described above. Obviously the model is unidentified in the sense that the decision of which state to call state 0 and which to call state 1 is arbitrary. I normalize by letting state 1 be the fast growth state and state 0 be the slow growth state, achieved by setting α1 + α0 &gt; α0 or α1 &gt; 0.

The logic of the filter is equally valid under much more general specifications. With n rather than 2 states, the input to the filter is a vector consisting of n' elements, and the summations in Steps 3 and 5 are over (0, n – 1) rather than (0,1). The autoregressive parameters (φ) can also be made a function of the regime by replacing φ; in Step 2 with φ(S,) or φ(S,-j). In my (1988) paper I applied the algorithm with the standard deviation σ(S) also a function of the regime, and extended the estimation theory to a multivariate context where the econometrician wishes to impose the cross-equation restrictions implied by rational expectations. Higher-order dynamics for the regime shift are also conceptually straight-forward—e.g., replace P[S, = s,|S,-1 = s,-1] in Step 2 with P[S, = s,|S,−1 = st−1, St−2 = st−2]. That is, instead of multiplying each of the 16 numbers in the input to the filter by p, q, 1 - p, or 1 − q (depending on the value of s, and s,-1) one multiplies by one of P11, P12,... depending on the value of st, st−1, and st−2.


<!-- p:14 -->


Such extensions are in principle straight-forward. Any problems are chiefly numerical. Identification of the parameters characterizing the dynamics of S, ( p, q, and α1) separately from those of the Gaussian component (φ1, φ2,..., φ) depends on nonlinearities in the data. There is a practical limit on how complicat       f s     ian component to become and still have hope of obtaining useful results.

The relation between my approach and that of Sclove (1983) should now be stated more precisely. Let y ≡ (y1, . . ., yτ)', s ≡ (s1, . . . , sτ)', and θ = (α1, α0, P, q, σ, φ1, φ2, . ., φ, )'. My filter evaluates f( y|θ, y − r+1, . . . , y0) and maximizes with respect to θ. The MLE θ is then used in a final pass through the filter to draw probabilistic inference about s. Sclove, by contrast, would calculate f( y, s|θ, y-r+1,..., yo) and maximize with respect to both θ and s. Thus the output of my algorithm is a sequence of conditional probabilities, and the output of Sclove's maximization is an imputed historical sequence for s. Sclove's empirical application also opted for the other end of the trade-off between a rich part     a   s   in Markov component. He assumed no autocorrelation for the Gaussian component, whereas I allow four lags; Sclove tested for up to nine different regimes, whereas I permit only two.

### 4.3. Smoothing

Another byproduct of the basic filter is inference about the state s, based on currently available information,

Alternatively, one can obtain a more reliable inference about the lagged value of the state using currently available information. For example, using the output from Step 4 of the basic filter, one can calculate an r-lag smoother:

$$from Step 4 of the basic filter, one can calculate an F-lag smoother: \\ P [ S _ { t - } , = s _ { t - } , | y _ { t - 1 } , \dots , y _ { - t + 1 } ] \\ = \sum _ { s , - 0 } \sum _ { s _ { t - 1 } = 0 } ^ { 1 } \cdots \sum _ { s _ { t - 1 } = 0 } ^ { 1 } P [ S _ { t } , = s _ { t } , S _ { t - 1 } = s _ { t - 1 } , \dots , \\ S _ { t - } , = s _ { t - } , | y _ { t } , y _ { t - 1 } , \dots , y _ { - t + 1 } ] . \\ A _ { \ } \text {full-sample smoother} \, c a n b e t a n d \, f r o n g a n d s u g e s t h e m o d y$$

A full-sample smoother can be obtained from adapting a suggestion made by Cosslett and Lee (1985) in a slightly different context. Suppose that instead of using

$$P \left [ S _ { t - 1 } = s _ { t - 1 } , \, S _ { t - 2 } = s _ { t - 2 } , \dots , S _ { t - r } = s _ { t - r } | y _ { t - 1 } , \, y _ { t - 2 } , \dots , y _ { - r + 1 } \right ]$$


<!-- p:15 -->


as input into the basic filter, we used in its place

$$P [ S _ { t - 1 } = s _ { t - 1 } , \, S _ { t - 2 } = s _ { t - 2 } , \dots , S _ { t - r } = s _ { t - r } | S _ { \tau } = \hat { s } _ { \tau } , \\ S _ { \tau - 1 } = \hat { s } _ { \tau - 1 } , \dots , S _ { \tau - r + 1 } = \hat { s } _ { \tau - r + 1 } , \, y _ { t - 1 } , y _ { t - 2 } , \dots , y _ { - r + 1 } ] \\$$

for some τ ≤ t − 1 and for some choice of (s, −1, ..., −r+1) to be specified shortly. Running through the steps of the basic filter, it is easy to verify that the output of the filter would in this case be

$$P [ S _ { t } = s _ { t } , \, S _ { t - 1 } = s _ { t - 1 } , \dots , S _ { t - r + 1 } = s _ { t - r + 1 } | S _ { \tau } = \hat { s } _ { \tau } , \\ S _ { \tau - 1 } = \hat { s } _ { \tau - 1 } , \dots , S _ { \tau - r + 1 } = \hat { s } _ { \tau - r + 1 } , \ y _ { t } , \, y _ { t - 1 } , \dots , \, y _ { - r + 1 } ] \\$$

with byproduct

$$f ( y _ { t } | S _ { \tau } = \hat { s } _ { \tau } , \, S _ { \tau - 1 } = \hat { s } _ { \tau - 1 } , \dots , \, S _ { \tau - r + 1 } = \hat { s } _ { \tau - r + 1 } , \, y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } ) .$$

Bearing this in mind, the full-sample smoother can be obtained as follows.

STEP 1: Run through the basic filter for t = 1,..., T and store the resulting s +-- +- = +--= -  = d sns f(y,|y−1, yτ−2, . . ., y −r+1) for τ = 1,2,..., T.

STEP 2: For each τ and for each possible value of the vector (s, s−1, . . . , s−r+1), repeat the following: (a) Set

$$P [ S _ { \tau } = s _ { \tau } , \, S _ { \tau - 1 } = s _ { \tau - 1 } , \dots , S _ { \tau - r + 1 } = s _ { \tau - r + 1 } | S _ { \tau } = \hat { s } _ { \tau } , \\ S _ { \tau - 1 } = \hat { s } _ { \tau - 1 } , \dots , S _ { \tau - r + 1 } = \hat { s } _ { \tau - r + 1 } , \ y _ { t - 1 } , \, y _ { t - 2 } , \dots , \, y _ { - r + 1 } ] \\$$

equal to unity if s, = sr, sτ−1 = sr−1, . . , sr−r+1 = ê−r+1 and zero otherwise. (b) Repeat the basic filter using (4.4) to start the iteration and iterate over t = τ + 1, τ + 2,..., T, storing the output from Step 3 of the basic filter as

- (c) The smoothed probabilities are given by
- f(y,|S, = Sr, Sτ−1 = Sτ−1, ..., Sr−r+1 = Sτ−r+1, yt−1, yt−2, . .., y −r+1).

$$f ( y _ { r } | S _ { r } - 3 _ { r } , \, S _ { r - 1 } - S _ { r - 1 } , \dots , S _ { r - r + 1 } ) \, y _ { t - 1 } , y _ { t - 2 } , \dots , y _ { - r + 1 } ) , y _ { t - 1 } , y _ { t - 2 } , \dots , y _ { - r + 1 } ) . \\ ( c ) \, \text {The smooth probabilities are given by} \\ P [ S , = \hat { s } , \, S _ { - 1 } = \hat { s } _ { r - 1 } , \dots , S _ { r - r + 1 } = \hat { s } _ { r - r + 1 } | y _ { T } , \, y _ { T - 1 } , \dots , y _ { - r + 1 } ] \\ = P [ S , = \hat { s } , \, S _ { - 1 } = \hat { s } _ { r - 1 } , \dots , S _ { r - r + 1 } = \hat { s } _ { r - r + 1 } | y _ { r } , \, y _ { r - 1 } , \dots , y _ { - r + 1 } ] \\ \times \frac { f ( y _ { r + 1 } | S _ { r } = \hat { s } _ { r } , \, S _ { - 1 } = \hat { s } _ { r - 1 } , \dots , S _ { r - r + 1 } = \hat { s } _ { r - r + 1 } | y _ { r } , \, y _ { r - 1 } , \dots , y _ { - r + 1 } ) } { f ( y _ { r + 1 } | y _ { r } , \, y _ { r - 1 } , \dots , y _ { - r + 1 } ) } \\ \times \frac { f ( y _ { r + 2 } | S _ { r } = \hat { s } _ { r } , \, S _ { - 1 } = \hat { s } _ { r - 1 } , \dots , S _ { r - r + 1 } = \hat { s } _ { r - r + 1 } , y _ { r + 1 } , \, y _ { r + 2 } , \dots , y _ { - r + 1 } ) } { f ( y _ { r + 2 } | y _ { r + 1 } , \, y _ { r } , \dots , y _ { - r + 1 } ) } \\ \times \dots \times \frac { f ( y _ { T } | S _ { r } = \hat { s } _ { r - 1 } , \, S _ { - 1 } = \hat { s } _ { r - 1 } , \dots , S _ { r - r + 1 } = \hat { s } _ { r - r + 1 } , y _ { T - 1 } , \, y _ { T - 2 } , \dots , y _ { - r + 1 } ) } { f ( y _ { T } | y _ { T - 1 } , \, y _ { T - 2 } , \dots , y _ { - r + 1 } ) } .$$

## 5. MAXIMUM LIKELIHOOD ESTIMATES FOR U.S. GNP DATA

The above technique was applied to U.S. postwar data on real GNP. The variable used for y, was 100 times the change in the log of real GNP for t = 1951 : II to 1984: IV.6 Numerical maximization of the conditional log likelihood function led to the maximum likelihood estimates reported in Table I. Also reported are asymptotic standard errors.7


<!-- p:16 -->


TABLEI MAXIMUM LIKELIHOOD ESTIMATES OF PARAMETERS AND ASYMPTOTIC STANDARD ERRORS BASED ON DATA FOR U.S. REAL GNP, t = 1952 : II TO 1984 : IV

| Parameter   |   Estimate |   Standard error |
|-------------|------------|------------------|
| α1          |      1.522 |           0.2636 |
| α0          |    -0.3577 |           0.2651 |
| p           |     0.9049 |          0.03740 |
| q           |     0.7550 |          0.09656 |
| σ           |     0.7690 |          0.06676 |
| φ1          |      0.014 |            0.120 |
| σ2          |     -0.058 |            0.137 |
| $3          |     -0.247 |            0.107 |
| φ4          |     -0.213 |            0.110 |

One possible outcome that might have been expected a priori would associate the states s, = 0 and 1 with slow and fast growth rates for the U.S. economy, corresponding to decade-long changes in trends. In fact, however, the sample likelihood is maximized by a negative growth rate of -0.4% per quarter during state 0 and a positive growth of (α0 + α1) = + 1.2% during state 1. These values clearly correspond to the dynamics of business cycles as opposed to long-term variations in secular growth rates. Indeed, the first- and second-order serial correlation in logarithmic changes of real GNP seem to be better captured by shifts between states rather than by the leading autoregressive coefficients, as indicated by the fact that φ1 and 2 come out remarkably close to zero. Negative co t i i t t i t is t    t the Bureau of Economic Analysis for deseasonalizing introduces spurious periodicity when applied to data generated by a nonlinear process such as this one. These coefficients further suggest that investigating a higher-order Markov process for the trend might also be a fruitful topic for future research.

Figure 1 reports the estimated probability that the economy is in the negative growth state (P[S, = 0]) based on currently available information (panel A) and information available one year later (panel B). A full sample smoother (not shown) was also calculated. The probabilities from the full-sample smoother differed very little from those of the four-lag smoother in panel B. The average absolute difference between these two smoothed series was .016, with the maximum difference occurring in the second quarter of 1956; (the four-lag smoother FIGURE 1.—Inferred probability that S, = 0. Panel (A) reports the inferred probability that the economy was in the falling GNP state at date t using information available at the time (P[S, = 0|y, yt-1,... ). Panel (B) reports the inferred probability that the economy was in the falling GNP state at date t using information available 4 quarters later (P[S, = 0|yt + 4, yt + 3... ]).

6The level of GNP is measured at an annual rate in 1982 dollars. Data are from Business Conditions Digest, February, 1986, p. 102, Series 50. The order of lags r was set arbitrarily to 4; the basjc filter was thus started for t = 1952 : II.

7Maximization was achieved by a Davidon-Fletcher-Powell routine. Convergence to the global maximum reported in Table I proved relatively robust with respect to a broad range of start-up values. Second derivatives of the log likelihood were calculated numerically, from which asymptotic standard errors were constructed. I would like to thank Kent Wall for use of his DFP algorithm and Steve Stern for use of his second-derivative program.


<!-- p:17 -->

puts the probability of contraction at .40 for this quarter, whereas the full-sample inference was .15). This suggests that reasonably precise estimates are available from the four-lag smoother associated with the basic filter itself, and it may be unnecessary to employ the full-sample smoother for many applications. Another reasonable alternative to the full-sample smoother is to augment the basic filter with a few additional lags on s.

## 6. ESTABLISHING THE DATES OF HISTORICAL BUSINESS CYCLES

The specific inferences about the historical incidence of growth states generated by the filter and smoother correspond extremely closely to conventional dating of business cycles, and indeed could be employed as an independent objective algorithm for generating such dating. A sensible metric might be based on whether the econometrician would conclude that the economy is more likely than not to be in a recession (P[S, = 0|yτ, yτ-1,..., y−r+1] &gt; 0.5). Dates for postwar business cycles based on this measure are compared with NBER values in Table II.8 In contrast to NBER dates, my series indicates that the recessions of 1957–58 and 1979-80 immediately followed the oil price increases of 1957:I associated with the Suez Crisis and 1979: II associated with the Iranian revolution, respectively.9 For the other recessions, the two dating techniques are always within three months of each other.


<!-- p:18 -->


TABLE II ALTERNATIVE DATING OF U.S. BUSINESS CYCLE PEAKS AND TROUGHS AS DETERMINED BY (1) NBER, AND (2) PROBABILITY OF BEING IN RECESSION GREATER THAN 0.5 AS DETERMINED FROM FULL-SAMPLE SMOOTHER

| NBER - Peak   | NBER - Trough   | Smoother - Peak   | Smoother - Trough   |
|---------------|-----------------|-------------------|---------------------|
| 1953:III      | 1954:II         | 1953:III          | 1954:II             |
| 1957:III      | 1958:II         | 1957:1            | 1958:I              |
| 1960:II       | 1961:I          | 1960:II           | 1960:IV             |
| 1969:IV       | 1970:IV         | 1969:III          | 1970:IV             |
| 1973:IV       | 1975:1          | 1974:I            | 1975:I              |
| 1980:I        | 1980:III        | 1979:II           | 1980:III            |
| 1981 :III     | 1982:IV         | 1981:II           | 1982:IV             |

Note that the particular decision rule P[S, = 0] &gt; 0.5 seems to be largely iro    s s    f    i Figure 1 lie between 0.3 and 0.7. The algorithm is usually arriving at a fairly strong conclusion about whether the economy is in a recession. The implicit histogram would also seem to suggest that the filter is not simply fitting parameters to an arbitrary nonlinear process, but rather reflects an underlying pattern in the data of dichotomous shifts between the expansion and contraction phase.

Another interesting implication of the Markov framework is that one can calculate from the maximum likelihood parameter estimates the expected duration of a typical recession and compare this predicted magnitude with the historical average. Conditional on being in state 0, the expected duration of a recession is

or 4.1 quarters. The historical average duration of a recession was 4.7 quarters during the postwar period according to the NBER figures. The expected duration of an expansion is likewise (1 – p)-1 or 10.5 quarters, compared with an average of 14.3 quarters in NBER dating.

-uene es  ue ues ues use  ues e ut s use urnt ment of Commerce.

My (1985) paper provided a detailed discussion of these events.


<!-- p:19 -->


FiGURE 2.—Comparison of actual GNP data with predictions of Markov model of trend.

## 7. COMPARING LINEAR AND NONLINER MODELS OF GNP GROWTH

The Markov model offers a nonlinear alternative to linear representations such as the Box-Jenkins ARIMA specification (used by Beveridge and Nelson (1981), and Campbell and Mankiw (1987a,b)) or the unobserved components (UC) models of Harvey and Todd (1983), Watson (1986), and Clark (1987). One might well ask why, if the Markov model were the true data-generating process, do parsimoniously parameterized linear models seem to have fit the data so well?

Panel A of Figure 2 reports the sample autocorrelogram of actual postwar changes in the log of quarterly real GNP. Indeed this looks much like that predicted for low-order ARIMA processes.10 An AR(4) model fit to the growth rate of real GNP exhibits only the most modest autocorrelation of residuals (Figure 2, panel A).


<!-- p:20 -->


What would these same diagnostics be expected to reveal if the data were in fact generated by the Markov model? The Markov model posits that y, = α1s, + α0 + z, with z, a zero-mean Gaussian AR(r) process and E(S,) = π. From the independence of S, and z, we know

$$E [ \, y _ { t } - E y _ { t } ] [ \, y _ { t - j } - E y _ { t - j } \, ] = E [ \, z _ { t } z _ { t - j } \, ] + \alpha _ { 1 } ^ { 2 } E \left [ \, S _ { t } - \pi \, \right ] \left [ \, S _ { t - j } - \pi \, \right ] .$$

The first term is the jth autocovariance from a standard AR(r) process, and can be calculated using well-known formulas. Using (2.5) and the fact that Var(S0) = π(1 – π), we can evaluate the second term from

$$E [ S _ { t } - \pi ] [ S _ { t - j } - \pi ] = \lambda ^ { j } \pi ( 1 - \pi )$$

where as before λ ≡ (−1 + p + q) and π ≡ (1 − q)/(1 − λ). Thus the theoretical autocorrelogram of data generated by a Markov model is known. Panel B of Figure 2 plots this function for the MLE parameter values of Table I. It would clearly be extremely difficult to distinguish the Markov model from a simple linear alternative on the basis of the observed autocorrelations in a sample the size of postwar quarterly data.

Figure 2 also reports some Monte Carlo results. For each of 1000 samples of size T = 130 generated by the Markov model, an AR(4) specification was fit by os  d s  as   vsss a  s very close to that for actual postwar data (panel A). The average sample autocorrelogram of the residuals again would provide negligible evidence against the AR(4) specification, even though we know that the true model used to simulate the data in panel B was the nonlinear Markov process and not an AR(4). I conclude that the Markov model satisfies the "encompassing" criterion of Hendry and Richard (1982)—the apparent success (on the basis of Box-Jenkins diagnostics) of simple ARIMA representations is precisely what one would predict if the Markov model were the true data-generating process.

There are, however, several predictions of the Markov model that are inconsistent with an ARIMA or linear UC specification. The Markov model asserts that forecasts of the log of GNP that are restricted to linear functions of lagged values will be suboptimal; additional useful information is alleged to be contained in the nonlinear function P[St-1 = 1|yt-1, yt-2,...] which summarizes the inference drawn the previous period about the unobserved state variable S,–1. The intuition for the sign and magnitude of the predicted effect is as follows. If the Markov model were true and we knew that the economy was in the expansion phase of the cycle last period (S,-1 = 1), we would forecast

$$E \left [ ( \alpha _ { 0 } + \alpha _ { 1 } s _ { i } ) | S _ { t - 1 } = 1 \right ] = \alpha _ { 0 } + \alpha _ { 1 } p$$

10For example, Watson (1986) settled on an ARIMA(1,1,0) specification for the log of GNP,

Campbell and Mankiw (1987b) preferred a (2,1,2), and Clark (1987) selected (0,1,2).


<!-- p:21 -->


whereas when the economy was in recession last period,

$$E \left [ ( \alpha _ { 0 } + \alpha _ { 1 } S _ { t } ) | S _ { t - 1 } = 0 \right ] = \alpha _ { 0 } + \alpha _ { 1 } ( 1 - q ) .$$

The difference in the forecast growth rate of the economy knowing that the economy was in expansion rather than recession last period would thus be on the order of α1( p − 1 + q), or about 1% faster GNP growth forecast when the economy was in expansion last period.11 The Markov model therefore predicts that the lagged output of the basic filter,

$$X _ { t - 1 } \equiv P [ S _ { t - 1 } = 1 | y _ { t - 1 } , y _ { t - 2 } , \dots , y _ { - r + 1 } ]$$

should enter statistically significantly with a positive coefficient when added to the AR(4) representation for GNP growth. The ARIMA or UC specifications predict that it should have coefficient zero. When one performs this regression on actual postwar GNP data, one finds (standard errors in parentheses)

$$\text {actual postwar GNP data, one finds (standard errors in parentheses)} \\ y _ { t } = - \, \begin{array} { c c c } y _ { t } = - \, \begin{array} { c c c } 1 9 9 & - \, . 0 7 2 & y _ { t - 1 } - \, . 0 6 3 9 & y _ { t - 2 } - \, . 1 8 1 5 & y _ { t - 3 } \\ ( 2 9 4 ) & ( . 1 6 0 9 ) & ( . 1 0 0 8 ) ^ { 2 } & ( . 0 9 2 7 ) ^ { 3 } & \end{array} \\ - \, \begin{array} { c c c } 1 6 3 9 & y _ { t - 4 } + 1 . 6 7 0 & X _ { t - 1 } + u _ { t } . \\ ( 0 9 1 7 ) & ( . 5 9 0 ) & \end{array} \\$$

The t statistic associated with the null hypothesis that GNP growth rates were truly generated by an AR(4) model is 2.83, though X,-1 being a generated regressor, it is unclear what distribution theory is appropriate for interpreting this statistic.12 The change in forecast is on the order of 1% of GNP.

Another prediction of the Markov model that is inconsistent with an ARIMA or UC specification concerns the heteroskedasticity of the residuals. The intuition is as follows. If the data were truly generated by the Markov model and we knew that the economy was in expansion last period (S,-1 = 1) along with knowing past values for ε,-j, then the expected squared error in forecasting log GNP this period would be given by

$$E \left [ \varepsilon _ { t } ^ { 2 } \right ] + E \left \{ \left [ ( \alpha _ { 1 } S _ { t } + \alpha _ { 0 } ) - ( \alpha _ { 1 } p + \alpha _ { 0 } ) \right ] ^ { 2 } | S _ { t - 1 } = 1 \right \} = \sigma _ { e } ^ { 2 } + \alpha _ { 1 } ^ { 2 } p \left ( 1 - p \right ) .$$

11This discussion (which rederives eq. (2.5) from first principles) is intended purely as an aid to the intuition. The formula in the text does not literally give the expected value of the coefficient in the regression that follows. One can of course arrive at the precise effect expected by adding s,–1 to the AR(4) regression of the Monte Carlo simulations described earlier. Its expected coefficient turns out to be 1.08.

12One might think it more natural to test the AR(4) specification against the Markov alternative as a conventional nested hypothesis. When α1 = 0, the growth rates in states 0 and 1 are the same. Thus, an AR(4) model for first-differences of the data obtains as a special case of the Markov specification, and one might think of using a likelihood ratio, Wald, or Lagrange multiplier test. Unfortunately, the usual regularity conditions for establishing asymptotic properties of these tests fail to apply here. Under the nuli hypothesis that α1 = 0, the parameters p and q are unidentified. When p, q, and α1 are all treated as separate parameters, the information matrix is singular under the null hypothesis and the MLE's β and ą cannot be regarded as consistent estimates of any population values. Furthermore, the derivative of the log likelihood with respect to α1 is also zero at the constrained MLE. Davies (1977), Watson and Engle (1985), and Lee and Chesher (1986) have discussions of how one might try to construct asymptotic test statistics that are robust to these issues.


<!-- p:22 -->


By contrast, if we knew that the economy was in recession last period,

$$E \left [ \varepsilon _ { t } ^ { 2 } \right ] + E \left \{ \left [ ( \alpha _ { 1 } S _ { t } + \alpha _ { 0 } ) - ( \alpha _ { 1 } ( 1 - q ) + \alpha _ { 0 } ) \right ] ^ { 2 } | S _ { t - 1 } = 0 \right \} \\ = \sigma _ { t } ^ { 2 } + \alpha _ { 1 } ^ { 2 } q ( 1 - q ) .$$

Sine  t ( e t  t t       ave a smaller variance when the economy was in expansion last period than when the economy was in recession last period, the expected difference being on the order of13

$$\alpha _ { 1 } ^ { 2 } [ \ p ( 1 - p ) - q ( 1 - q ) ] = - . 2 2 9 .$$

Thus, the Markov model predicts that in a regression of the square of the AR(4) oes  s  n s       sstler statistically significantly and with a negative sign. The ARIMA or UC models predict homoskedastic errors and a coefficient of zero. In actual postwar GNP data one finds (standard errors in parentheses)

$$\hat { u } _ { t } ^ { 2 } = 1 . 5 7 0 \, - \, . 8 1 3 \, X _ { _ { t } - 1 } + e _ { _ { t } } , \quad R ^ { 2 } = . 0 3 6 5 4 ,$$

where û, is the estimated residual from the AR(4) regression in panel B of Figure 2. The Breusch-Pagan (1979) test of the null hypothesis of homoskedastic errors is 1/{2[(σ2)2]} times the explained sum of squares from this regression, which comes out to 5.17. Engle (1982, p. 1000) proposes calculating TR2 = 4.75. Again abstracting from the generated regressor problem, both statistics should be χ2(1) (whose 5% critical value is 3.84) under the null hypothesis that the data were generated by an AR(4) model with Gaussian homoskedastic errors. The data thus reveal evidence of the kind of conditional heteroskedasticity predicted by the Markov model and inconsistent with the ARIMA or UC specifications. Again the heteroskedasticity is economically large; (the squared residuals from an AR(4) are twice as large on average when the preceding period's inference about s,-1 pointed confidently to a recession).

## 8. ON THE CONSEQUENCES OF BUSINESS CYCLES

####### FOR THE LONG RUN LEVEL OF OUTPUT

Much effort has recently been devoted to measuring the effect of an unanticipat       aad d     ra asn arbitrarily long time horizon. This question holds interest for two reasons. The first concerns the nature of the business cycle and its persistence; the second pertains to the response of consumers and firms to changing business conditions. I discuss the implications of my Markov parameterization for each of these issues in turn.

13Again, this discussion is meant primarily to highlight the intuition and not to derive the precise mag     - ' +       t   t   one Carlo simulations on data truly generated by the Markov model, the expected coefficient on s,-1 in the Breusch-Pagan regression that follows turns out to be – .345.


<!-- p:23 -->


TABLE III PREVIOUS ESTIMATES OF THE EFFECT OF AN UNANTICIPATED 1% INCREASE IN REAL GNP

ON THE FUTURE LEVEL OF GNP AT AN ARBITRARILY LONG TIME HORIZON

| BASIC WOLD REPRESENTATION: (1 − L) = μ + ↓(L)u{                                                                     | BASIC WOLD REPRESENTATION: (1 − L) = μ + ↓(L)u{                                                                     | BASIC WOLD REPRESENTATION: (1 − L) = μ + ↓(L)u{                                                                     | ↓(1)                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ARIMA( p,1, q) MODELS: 4ψ(L) = [1 + θ1L + · . · + θqL9]/[1 − φ1L − · .· −φp LP]                                     | ARIMA( p,1, q) MODELS: 4ψ(L) = [1 + θ1L + · . · + θqL9]/[1 − φ1L − · .· −φp LP]                                     | ARIMA( p,1, q) MODELS: 4ψ(L) = [1 + θ1L + · . · + θqL9]/[1 − φ1L − · .· −φp LP]                                     | ARIMA( p,1, q) MODELS: 4ψ(L) = [1 + θ1L + · . · + θqL9]/[1 − φ1L − · .· −φp LP]                                     |
| Watson (1986)                                                                                                       | ARIMA(1,1,0)                                                                                                        | ARIMA(1,1,0)                                                                                                        | 1.68%                                                                                                               |
| Clark (1987)                                                                                                        | ARIMA(0,1,2)                                                                                                        | ARIMA(0,1,2)                                                                                                        | 1.62%                                                                                                               |
| Campbell and Mankiw (1987b)                                                                                         | ARIMA(2,1,2)                                                                                                        | ARIMA(2,1,2)                                                                                                        | 1.49%                                                                                                               |
| LINEAR UNOBSERVED COMPONENTS MODELS: ↓(L)ut = eτ + (1 − L)κ(L)ec                                                    | LINEAR UNOBSERVED COMPONENTS MODELS: ↓(L)ut = eτ + (1 − L)κ(L)ec                                                    |                                                                                                                     |                                                                                                                     |
| Watson (1986)                                                                                                       | Watson (1986)                                                                                                       | Watson (1986)                                                                                                       | 0.57%                                                                                                               |
| Clark (1987)                                                                                                        | Clark (1987)                                                                                                        | Clark (1987)                                                                                                        | 0.64%                                                                                                               |
| BIVA RIATE MODEL: (univariate representation implied by bivariate process for GNP growth and level of unemployment) | BIVA RIATE MODEL: (univariate representation implied by bivariate process for GNP growth and level of unemployment) | BIVA RIATE MODEL: (univariate representation implied by bivariate process for GNP growth and level of unemployment) | BIVA RIATE MODEL: (univariate representation implied by bivariate process for GNP growth and level of unemployment) |
| Evans (1987)                                                                                                        | Evans (1987)                                                                                                        | ARIMA(6,1,3)                                                                                                        | 0.55%                                                                                                               |
| COCHRANE'S NONPARAMETRIC ESTIMATE:                                                                                  | COCHRANE'S NONPARAMETRIC ESTIMATE:                                                                                  | COCHRANE'S NONPARAMETRIC ESTIMATE:                                                                                  | COCHRANE'S NONPARAMETRIC ESTIMATE:                                                                                  |
| Campbell and Mankiw (1987a)                                                                                         | Campbell and Mankiw (1987a)                                                                                         | Campbell and Mankiw (1987a)                                                                                         | 0.80% to 1.27%                                                                                                      |

### 8.1. On the Nature and Persistence of the Business Cycle

Nelson and Plosser (1982) and Campbell and Mankiw (1987a, b) were interested in the extent to which recessions represent temporary deviations from potential output with the shortfall largely made up during the subsequent recovery. Earlier approaches to this question were ultimately based on the standard linear representation for a nonstationary series y,:

$$( 1 - L ) \, \tilde { y } _ { t } = \mu + \sum _ { j = 0 } ^ { \infty } \psi _ { j } u _ { t - j } = \mu + \psi ( L ) \, u _ { t } . \\$$

The permanent effect on the level of the series of a current innovation u, is given by

$$\lim _ { j \to \infty } \frac { \partial E _ { t } \tilde { y } _ { t + j } } { \partial u _ { t } } & = \sum _ { j = 0 } ^ { \infty } \psi _ { j } = \psi ( 1 ) . \\$$

Previous researchers sought a finite-sample approximation to ψ(L) based on Box-Jenkins methods, linear unobserved components models, bivariate models, and nonparametric tests. A sampling of estimates based on these techniques is provided in Table III.14

By contrast, the Markov model is fundamentally nonlinear and provides an alternative perspective on the basic question about business cycles posed by these researchers. We can write this model in the form

$$( 1 - L ) \, \tilde { y } _ { t } = ( \alpha _ { 0 } + \alpha _ { 1 } s _ { t } ) + \left [ \phi ( L ) \right ] ^ { - 1 } \varepsilon _ { t } .$$

Notice that the two fundamental sources of randomness, S, and ε,, are allowed to have very different implications for the future path followed by y. The earlier discussion argued that we could associate S, with the business cycle directly, and ε, with other factors contributing to changes in output. The permanent effect of the non-business-cycle component ε, is given by

14See also Cochrane (1987, 1988), Campbell and Deaton (1987), and Gagnon (1988). For comparison, the AR(4) model fit to GNP growth in panel 1 of Figure 2 implies ψ(1) = 1.31.


<!-- p:24 -->


$$\lim _ { j \to \infty } \frac { \partial E _ { t } \tilde { y } _ { t + j } } { \partial \epsilon _ { t } } = \frac { 1 } { \phi ( 1 ) } = \frac { 1 } { 1 - . 0 1 4 + . 0 5 8 + . 2 4 7 + . 2 1 3 } = 0 . 6 6 .$$

On the other hand, if at date t the economy is in a recession (S, = 0) rather than the growth state (S, = 1), the consequences for the long-run future level of (100 times the log of) real GNP is given by equation (3.4):15

$$times \, \text {the log of} \, \text {real} \, \text {GNP is given by equation (3.4):} ^ { 1 5 } \\ ( 5 . 1 ) \quad \lim _ { j \to \infty } \left \{ E _ { t } [ \tilde { y } _ { t + j } | S _ { t } = 1 ] - E _ { t } [ \tilde { y } _ { t + j } | S _ { t } = 0 ] \right \} \\ = \frac { \alpha _ { 1 } ( - 1 + p + q ) } { ( 2 - p - q ) } \\ = \frac { 1 . 5 2 2 ( - 1 + . 9 0 4 9 + . 7 5 5 0 ) } { ( 2 - . 9 0 4 9 - . 7 5 5 0 ) } = 2 . 9 5 3 \\ \text {or about a 3% drop in GNP} .$$

or about a 3% drop in GNP.

a s ns  ns   a  an  b using equation (3.16), which, in contrast to (5.1), forecasts the level rather than the log of GNP. Notice that for the MLE's in Table I, the term 1 in equation (3.16) is estimated to be exp(1.522/100) = 1.01534. The eigenvalues are μ1 = 1.01138 and μ2 = 0.66264. Thus from (3.16),

$$\lim _ { j \to \infty } \left \{ E _ { t } \left [ \exp \left ( \tilde { y } _ { t + j } / 1 0 0 \right ) | S _ { t } = 1 , \, z _ { t } \right ] \div E _ { t } \left [ \exp \left ( \tilde { y } _ { t + j } / 1 0 0 \right ) | S _ { t } = 0 , \, z _ { t } \right ] \right \} \\ = \frac { 1 . 0 1 1 3 8 - ( - 1 + . 9 0 4 9 + . 7 5 5 0 ) } { 1 . 0 1 1 3 8 - ( 1 . 0 1 5 3 4 ) ( - 1 + . 9 0 4 9 + . 7 5 5 0 ) } = 1 . 0 2 9 7 \\$$

virtually the identical 3% change predicted in eq. (5.1).

### 8.2. Implications for the Permanent Income Hypothesis

A conceptually separate reason for interest in the magnitudes in Table III arises from a desire to understand the spending habits of consumers. Here Deaton (1986) and Campbell and Deaton (1987) raise the issue as to whether an unanticipated 1% increase in income rationally signals a greater than 1% increase in permanent income. The magnitudes in Table III are then used to evaluate theories of consumption behavior as distinct from theories of the business cycle per se. Watson (1986) showed that different finite-parameter approximations to a given process can yield strikingly different answers to this question. In this spirit I examine ψ(1) for the linear Wold representation for my Markov process,

15This calculation holds the current level of GNP constant, and calculates only the "signalling" consequences of the recession for future GNP. If instead one wanted a dynamic multiplier (the future and present consequences of a shift from S, = 1 to S, = 0 with the history of e's and all past s,-j constant), one should add α1 (or 1.522%) to the values reported in the text.


<!-- p:25 -->


$$1 \, \text { examine } \, \psi ( 1 ) \, \text { for } \, \text {unc inline } \, \text { word rep} \, \text {sec} \, \intertext { ( 8 . 1 ) } ( 8 . 1 ) \quad y _ { t } = \alpha _ { 0 } + \alpha _ { 1 } S _ { t } + \left [ \phi ( L ) \right ] ^ { - 1 } \varepsilon _ { t } \\ = \mu + \psi ( L ) e _ { t } .$$

Note from (2.3), (2.13), and (8.1) that y, has the spectrum

$$Note \, \text {from } ( 2 . 3 ) , ( 2 . 1 3 ) , \, \text {and } ( 8 . 1 ) \text { that } y _ { t } \text { has the spectrum } \\ & \sigma _ { e } ^ { 2 } \\ ( 8 . 2 ) \quad f ( \omega ) = \frac { } { ( 1 - \phi _ { 1 } e ^ { i \omega } - \cdots - \phi _ { r } e ^ { i \omega r } ) ( 1 - \phi _ { 1 } e ^ { - i \omega } - \cdots - \phi _ { r } e ^ { - i \omega r } ) } \\ & + \frac { \alpha _ { 1 } ^ { 2 } [ \ p ( 1 - \ p ) \pi + q ( 1 - q ) ( 1 - \pi ) ] } { ( 1 - \lambda e ^ { i \omega } ) ( 1 - \lambda e ^ { - i \omega } ) } \\ & = \sigma _ { e } ^ { 2 } \psi ( e ^ { i \omega } ) \psi ( e ^ { - i \omega } ) \\ \text {where our task is to calculate } \psi ( 1 ) . \text { From } ( 8 . 2 ) \text { we see }$$

where our task is to calculate ψ(1). From (8.2) we see

$$\text {where our task is to calculate $\psi(1).$ From $(8,2)$ we see } \\ f ( 0 ) = \frac { \sigma _ { \text {e} } ^ { 2 } } { ( 1 - \phi _ { 1 } - \cdots - \phi _ { } ) ^ { 2 } } + \frac { \alpha _ { 1 } ^ { 2 } [ \, p ( 1 - p ) \pi + q ( 1 - q ) ( 1 - \pi ) ] } { ( 1 - \lambda ) ^ { 2 } } \\ = \sigma _ { \text {e} } ^ { 2 } \cdot [ \psi ( 1 ) ] ^ { 2 } .$$

Using the maximum likelihood estimates in Table I, we calculate

- 2 · [ψ(1)]2 = .261 + 2.277 = 2.538. (8.3)

We further know (e.g., Anderson (1971, p. 422))

$$\sigma _ { e } ^ { 2 } = \exp \left [ \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \log f ( \omega ) \, d \omega \right ]$$

which one calculates to be .9703 by numerical integration of (8.2). Thus

$$\psi ( 1 ) = \left [ \frac { \sigma _ { e } ^ { 2 } \cdot \left [ \psi ( 1 ) \right ] ^ { 2 } } { \sigma _ { e } ^ { 2 } } \right ] ^ { 1 / 2 } = 1 . 6 2 .$$

This estimate is completely dominated by the contribution of the business cycle variable (see the second term in the sum on the right-hand side of (8.3)).

It is also straightforward to calculate the effect a recession would have on permanent income if consumers knew with certainty that a recession had started, that is, calculate the effect of a recession on the cumulative discounted value of future output flows. From equation (3.17), the ratio of the discounted value of the trend term when π0 = 1 to the value when π0 = 0 is given by16

$$\frac { 1 - ( - 1 + p + q ) \beta \cdot \exp \left ( \alpha _ { 0 } / 1 0 0 \right ) } { 1 - ( - 1 + p + q ) \beta \cdot \exp \left [ \left ( \alpha _ { 0 } + \alpha _ { 1 } \right ) / 1 0 0 \right ] } .$$

16Recall that in the case of a Markov trend in logs, the stochastic specification is multiplicative, not additive (, = ñ, ,) and so use of this formula is only strictly valid for E, 2t + , constant. It does seem to offer a useful benchmark, however, for summarizing a key feature of these empirical estimates. See

also the preceding footnote.


<!-- p:26 -->


Using β = 0.99 for the quarterly real discount factor, this expression comes out to 1.029 for the empirical estimates in Table I; that is, the certain knowledge that the economy has gone into a recession is associated with a 3% drop in permanent income.

## 9. CONCLUSIONS

This paper explored the possibility that growth rates of real GNP are subject to autocorrelated discrete shifts. Empirical estimation suggested that the business cycle is better characterized by a recurrent pattern of such shifts between a recessionary state and a growth state rather than by positive coefficients at low lags in an autoregressive model. Indeed, statistical estimates of the economy's growth state cohere remarkably well with NBER dating of postwar recessions, and might be used as an alternative objective method for assigning business cycle dates. A move from expansion into recession is associated with a 3% decrease in the present value of future real GNP and similarly portends a 3% drop in the long-run forecast level of GNP.

Department of Economics, Rouss Hall, University of Virginia, Charlottesville, VA 22901, U.S.A.

Manuscript received November, 1986; final revision received June, 1988.

####### REFERENCES

ANDERsON, T. W. (1971): The Statistical Analysis of Time Series. New York: John Wiley and Sons, Inc.

BEVERIDGE, STEPHEN, AND CHARLES R. NELSON (1981): "A New Approach to Decomposition of Economic Time Series into Permanent and Transitory Components with Particular Attention to Measurement of the 'Business Cycle'," Journal of Monetary Economics, 7, 151–174.

AoKI, MAsANAO (1967): Optimization of Stochastic Systems: Topics in Discrete-Time Systems. New York: Academic Press.

BOX, G. E. P., AND GwILYM M. JENKINS (1976): Time Series Analysis: Forecasting and Control, Revised Edition. San Francisco: Holden-Day.

BROCK, W. A., AND CHERA L. SAYERs (1988): "Is the Business Cycle Characterized by Deterministic Chaos?"Journal of Monetary Economics, 22, 71–80.

BREUsCH, T. S., AND A. R. PAGAN (1979): "A Simple Test for Heteroscedasticity and Random Coefficient Variation,"Econometrica, 47, 1287–1294.

CAMPBELL, JoHN Y., AND ANGUs DEATON (1987): "Is Consumption Too Smooth?" NBER Working Paper No. 2134.

in Macroeconomic Fluctuations,"American Economic Review Papers and Proceedings, 77, 111–117. (1987b): "Are Output Fluctuations Transitory?" Quarterly Journal of Economics, 102, 857-880.

CAMPBELL, JoHN Y., AND N. GREGORY MANKIW (1987a): "Permanent and Transitory Components

CHIANG, CHIN LoNG (1980): An Introduction to Stochastic Processes and Their Applications. New York: Krieger.

Economics, 102, 797-814.

CLARK, PETER K. (1987): "The Cylical Component of U.S. Economic Activity," Quarterly Journal of

Coi      ss  a, :   sity of Chicago.

(1988): "How Big is the Random Walk in GNP?" Journal of Political Economy, 96, 893–920.


<!-- p:27 -->


- CosSsLETT, STEPHEN R., AND LUNG-FEI LEE (1985): "Serial Correlation in Discrete Variable Models," Journal of Econometrics, 27, 79–97.
- DAvIEs, R. B. (1977): "Hypothesis Testing When a Nuisance Parameter is Present Only Under the Alternative,"Biometrika, 64, 247–254.
- DEATON, ANGUs S. (1987): "Life-Cycle Models of Consumption: Is the Evidence Consistent with the Theory?" in Advances in Econometrics, Fifth World Congress, Vol. II., ed. by T. F. Bewley. New York: Cambridge University Press, pp. 121–148.
- DIEBOLD, FRANCIs X., AND GLENN D. RUDEBUSCH (1987): "Scoring the Leading Indicators," Federal Reserve Board, Special Studies Paper No. 206.
- ENGLE, RoBERT F. (1982): "Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation,"Econometrica, 50, 987–1007.
- ENGLE, RoBERT F., AND C. W. J. GRANGER (1987): "Co-Integration and Error Correction: Representation, Estimation, and Testing,"Econometrica, 55, 251–276.
- ENGLE, RoBERT F., DAVID LILIEN, AND RUSSELL P. RoBINs (1987): "Estimating Time Varying Risk Premia in the Term Structure: The ARCH-M Model,"Econometrica, 55, 391–407.
- EvANs, GEORGE W. (1987): "Output and Unemployment Dynamics in the United States: 1950–1985," Working Paper, Stanford University.
- GAGNoN, JosEPH E. (1988): "Short-Run Models and Long-Run Forecasts: A Note of the Permanence of Output Fluctuations," Quarterly Journal of Economics, 103, 415–424.
- G   , :    di  ddi: tionally Constrained Heterogeneous Processes: Asset Pricing Applications,"Mimeographed, North Carolina State University.
- GOLDFELD, STEPHEN M., AND RICHARD E. QUANDT (1973): "A Markov Model for Switching Regressions," Journal of Econometrics, 1, 3–16.
- GRANGER, C. W. J. (1983): "Forecasting White Noise," Applied Time Series Analysis of Economic Data, in Proceedings of the Conference on Applied Time Series Analysis of Economic Data, Oct. 13–15, 1981, Arlington, VA, ed. by Arnold Zellner. Washington, D.C.: U.S. Department of Commerce, Bureau of the Census, pp. 308–314.
- HamILToN, JAMEs D. (1985): "Historical Causes of Postwar Oil Shocks and Recessions," Energy Journal, 6, 97–116.
- (1988): "Rational-Expectations Econometric Analysis of Changes in Regime: An Investigation of the Term Structure of Interest Rates," Journal of Economic Dynamics and Control, 12, 385-423.
- HARvEY, A. C. (1985): "Trends and Cycles in Macroeconomic Time Series," Journal of Business and Economic Statistics, 3, 216–227.
- HARvEY, A. C., AND P. H. J. ToDD (1983): "Forecasting Economic Time Series with Structural and Box-Jenkins Models: A Case Study," Journal of Business and Economic Statistics, 1, 299-307.
- HENDRY, DAVID F., AND JEAN-FRANCOIs RICHARD (1982): "On the Formulation of Empirical Models in Dynamic Econometrics," Journal of Econometrics, 20, 3–33.

HINICH, MELVIN J., AND DoUGLAs M. PATTERsON (1985): "Evidence of Nonlinearity in Daily Stock

Returns," Journal of Business and Economic Statistics, 3, 69–77.

- KING, ROBERT, CHARLES PLOSSER, JAMES STOCK, AND MARK WATSON (1987): "Stochastic Trends and Economic Fluctuations," NBER Working Paper No. 2229.
- LEE, LUNG-FEI, AND ANDREW CHESHER (1986): "Specification Testing when the Score Statistics Are Identically Zero," Journal of Econometrics, 31, 121–149.
- LIPTSER, R. M., AND A. N. SHIRYAYEV (1977): Statistics of Random Processes, Volume I: General Theory. New York: Springer-Verlag.
- e   m e  l e :m  m mnn Dynamics and Control, 4, 225–241.
- o fo   s e   s   ,, :(cal Economy, 92, 307–328.
- NELSON, ČHARLES R., AND CHARLES I. PLOsSER (1982): "Trends and Random Walks in Macroeconomic Time Series: Some Evidence and Implications," Journal of Monetary Economics, 10, 139-162.
- QUAH, DANNY (1986): "What Do We Learn from Unit Roots in Macro Economic Time Series?" Working Paper, MIT.
- SCLOVE, STANLEY L. (1983): "Time-Series Segmentation: A Model and a Method," Information Sciences, 29, 7–25.
- SicHEL, DANIEL E. (1987): "Business Cycle Asymmetry: A Deeper Look," Mimeographed, Princeton University.


<!-- p:28 -->


SToCK, JAMEs H. (1987): "Measuring Business Cycle Time," Journal of Political Economy, 95, 1240-1261.

THots   Ss Ss  S-  St t  et ger Verlag.

Wa     , : i      ih a Stationary AR(1) Alternative,"Review of Economics and Statistics, 67, 341–346.

WATsoN, MARK W. (1986): "Univariate Detrending Methods with Stochastic Trends," Journal of Monetary Economics, 18, 49–75.

WECKER, WILLIAM E. (1979): "Predicting the Turning Points of a Time Series," Journal of Business, 52, 35-50.

<!-- END SOURCE 20/40: Hamilton_1989_nonstationary-time-series-business-cycle.md -->

---

<!-- BEGIN SOURCE 21/40: Hamilton_2018_never-use-hp-filter.md -->

# Source: `Hamilton_2018_never-use-hp-filter.md`

---
id: "Hamilton_2018_never-use-hp-filter"
source_pdf: "../pdf/Hamilton_2018_never-use-hp-filter.pdf"
source_filename: "Hamilton_2018_never-use-hp-filter.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "good"
extraction_score: 88.0
visual_assets: "disabled"
references_file: "../references/Hamilton_2018_never-use-hp-filter.references.md"
---

<!-- p:1 -->

###### NBER WORKING PAPER SERIES

###### WHY YOU SHOULD NEVER USE THE HODRICK-PRESCOTT FILTER

James D. Hamilton

Working Paper 23429 http://www.nber.org/papers/w23429

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 May 2017

I thank Daniel Leff for outstanding research assistance on this project and Frank Diebold, Robert King, James Morley, and anonymous referees for helpful comments on an earlier draft of this paper. The views expressed herein are those of the author and do not necessarily reflect the views of the National Bureau of Economic Research.

NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications.

© 2017 by  James  D.  Hamilton.  All  rights  reserved.  Short  sections  of  text,  not  to  exceed  two paragraphs, may  be  quoted  without  explicit  permission  provided  that  full  credit,  including  © notice, is given to the source.


<!-- p:2 -->


Why You Should Never Use the Hodrick-Prescott Filter James D. Hamilton NBER Working Paper No. 23429 May 2017 JEL No. C22,E32,E47

##### ABSTRACT

Here's why. (1) The HP filter produces series with spurious dynamic relations that have no basis in the underlying data-generating process. (2) Filtered values at the end of the sample are very different from  those  in  the  middle,  and  are  also  characterized  by  spurious  dynamics.  (3)  A statistical  formalization of  the  problem  typically  produces  values  for  the  smoothing  parameter vastly at odds with common practice, e.g., a value for λ far  below 1600 for quarterly data. (4) There's a better alternative. A regression of the variable at date t+h on the four most recent values as of date t offers a robust approach to detrending that achieves all the objectives sought by users of the HP filter with none of its drawbacks.

James D. Hamilton Department of Economics, 0508 University of California, San Diego 9500 Gilman Drive La Jolla, CA 92093-0508 and NBER jhamilton@ucsd.edu

A data appendix is available at http://www.nber.org/data-appendix/w23429


<!-- p:3 -->


## 1 Introduction.

Often economic researchers have a theory that is specified in terms of a stationary environment, and wish to relate the theory to observed nonstationary data without modeling the nonstationarity. Hodrick and Prescott (1981, 1997) proposed a very popular method for doing this, commonly interpreted as decomposing an observed variable into trend and cycle. Although drawbacks to their approach have been known for some time, the method continues today to be very widely adopted in academic research, policy studies, and analysis by private-sector economists. For this reason it seems useful to collect and expand on those earlier concerns here and note that there is a better way to solve this problem.

## 2 Characterizations of the Hodrick-Prescott filter.

Given T observations on a variable y t , Hodrick and Prescott (1981, 1997) proposed interpreting the trend component g t as a very smooth series that does not differ too much from the observed y t . 1 It is calculated as

$$\min _ { \{ g _ { t } \} _ { t = - 1 } ^ { T } } \left \{ \sum _ { t = 1 } ^ { T } ( y _ { t } - g _ { t } ) ^ { 2 } + \lambda \sum _ { t = 1 } ^ { T } [ ( g _ { t } - g _ { t - 1 } ) - ( g _ { t - 1 } - g _ { t - 2 } ) ] ^ { 2 } \right \} .$$

When the smoothness penalty λ → 0 , g t would just be the series y t itself, whereas when λ →∞ the procedure amounts to a regression on a linear time trend (that is, produces a series whose second difference is exactly 0). The common practice is to use a value of λ = 1600 for quarterly time series.

1 Phillips and Jin (2015) reviewed the rich prior history of generalizations of this approach.


<!-- p:4 -->


A closed-form expression for the resulting series can be written in vector notation by defining  ̃ T = T +2, y ( T × 1) = ( y T , y T - 1 , ..., y 1 ) ′ , g (  ̃ T × 1) = ( g T , g T - 1 , ..., g - 1 ) ′ and

$$\left ( y _ { T } , y _ { T - 1 } , \dots , y _ { 1 } \right ) ^ { ( \tilde { T } \times 1 ) } _ { ( T \times \tilde { T } ) } & = \left ( g _ { T } , g _ { T - 1 } , \dots , g _ { - 1 } \right ) ^ { T } \text { and } \\ & \quad H _ { \substack { ( T \times \tilde { T } ) \\ ( T \times T ) } } = \left [ \begin{array} { c c c } g _ { T } & g _ { T - 1 } & \dots & g _ { - 1 } \end{array} \right ] \\ & \quad \left [ 1 \ - 2 \ 1 \ 0 \ \cdots \ 0 \ \ 0 \ 0 \ 0 \ \right ] \\ & \quad 0 \ 1 \ - 2 \ 1 \ \cdots \ 0 \ \ 0 \ 0 \ 0 \\ Q _ { ( T \times \tilde { T } ) } & \vdots \ \vdots \ \vdots \ \vdots \ \vdots \ \vdots \ \vdots \ \vdots \ \vdots \\ & 0 \ 0 \ 0 \ 0 \ \cdots \ - 2 \ 1 \ 0 \\ 0 \ 0 \ 0 \ 0 \ \cdots \ 1 \ \ - 2 \ 1 \ \end{array} \right ] .$$

The solution to (1) is then given by 2

$$g ^ { * } = ( H ^ { \prime } H + \lambda Q ^ { \prime } Q ) ^ { - 1 } H ^ { \prime } y = A ^ { * } y .$$

The inferred trend g ∗ t for any date t is thus a linear function of the full set of observations on y for all dates.

As noted by Hodrick and Prescott (1981) and King and Rebelo (1993), the identical inference can alternatively be motivated from particular assumptions about the time-series behavior of the trend and cycle components. Suppose our goal was to choose a value for a ( T × 1) vector a t such that the estimate  ̃ g t = a ′ t y has minimum expected squared difference from the true trend:

$$\min _ { a _ { t } } E ( g _ { t } - a _ { t } ^ { \prime } y ) ^ { 2 } .$$

2 The appendix provides a derivation of equations (2) and (4). Cornea-Madeira (forthcoming) provided further details on A ∗ and a convenient algorithm for calculating it.


<!-- p:5 -->


The solution to this problem is the population analog to a sample regression coefficient, and is a function of the variance of y and its covariance with g :

$$\tilde { g } = E ( g y ^ { \prime } ) \left [ E ( y y ^ { \prime } ) \right ] ^ { - 1 } y = \tilde { A } y .$$

As an example of a particular set of assumptions we might make about these covariances, let c t denote the cyclical component and v t the second difference of the trend component:

$$y _ { t } = g _ { t } + c _ { t }$$

$$g _ { t } = 2 g _ { t - 1 } - g _ { t - 2 } + v _ { t } .$$

Suppose that we believed that v t and c t are uncorrelated white noise processes that are also uncorrelated with ( g 0 , g - 1 ), and let C 0 denote the (2 × 2) variance of ( g 0 , g - 1 ). These assumptions imply a particular value for  ̃ A in (4). As we let the variance of ( g 0 , g - 1 ) become arbitrarily large (represented as C - 1 0 → 0) , then in every sample the inference (4) would be numerically identical to expression (2).

Proposition 1. For λ = σ 2 c /σ 2 v and any fixed T, under conditions (5)-(6) with c t and v t white noise uncorrelated with each other and uncorrelated with ( g 0 , g - 1 ), the matrix  ̃ A in (4) converges to the matrix A ∗ in (2) as C - 1 0 → 0.

The proposition establishes that if researcher 1 sought to identify a trend by solving the minimization problem (1) while researcher 2 found the optimal linear estimate of a trend process that was assumed to be characterized by the particular assumption that v t and c t were both white noise, the two researchers would arrive at the numerically identical series for trend and cycle provided the ratio of σ 2 c to σ 2 v assumed by researcher 2 was identical to the value of λ used by researcher 1.


<!-- p:6 -->


The Kalman smoother is an iterative algorithm for calculating the population linear projection (4) for models where the variance and covariance can be characterized by some recursive structure. 3 In this case, (5) is the observation equation and (6) is the state equation. Thus as noted by Hodrick and Prescott, applying the Kalman smoother to the above state-space model starting from a very large initial variance for ( g 0 , g - 1 ) ′ offers a convenient algorithm for calculating the HP filter, and is in fact a way that the HP filter is often calculated in practice. Nevertheless, this observation should also be a bit troubling for users of the HP filter, in that they never defend the claim that the particular structure assumed in Proposition 1 is an accurate representation of the true data-generating process. Indeed, if a researcher did know for certain that these equations were the true data-generating process, and further knew for certain the value of the population parameter λ = σ 2 c /σ 2 v , he would probably be unhappy with using (2) to separate cycle from trend! The reason is that if this state-space structure was the true DGP, the resulting estimate of the cyclical component c t = y t -  ̃ g t would be white noise- it would be random and exhibit no discernible patterns. By contrast, users of the HP filter hope to see suggestive patterns in plots of the series that is supposed to be interpreted as the cyclical component of y t .

Premultiplying (2) by H ′ H + λQ ′ Q gives a system of equations whose t th element is

$$[ 1 + \lambda ( 1 - L ^ { - 1 } ) ^ { 2 } ( 1 - L ) ^ { 2 } ] g _ { t } ^ { * } = y _ { t } \quad \text {for } t = 1 , 2 , \dots , T - 2$$

for L the lag operator ( L k x t = x t - k , L - k x t = x t + k ) . In other words, F ( L ) g ∗ t = y t for

$$F ( L ) = 1 + \lambda ( 1 - L ^ { - 1 } ) ^ { 2 } ( 1 - L ) ^ { 2 } .$$

3 See for example Hamilton, 1994, equation [13.6.3].


<!-- p:7 -->


The following proposition establishes some properties of this filter. 4

Proposition 2. For any λ : 0 &lt; λ &lt; ∞ , the inverse of the operator (8) can be written

$$[ F ( L ) ] ^ { - 1 } = C \left [ \frac { 1 - ( \phi _ { 1 } ^ { 2 } / 4 ) L } { 1 - \phi _ { 1 } L - \phi _ { 2 } L ^ { 2 } } + \frac { 1 - ( \phi _ { 1 } ^ { 2 } / 4 ) L ^ { - 1 } } { 1 - \phi _ { 1 } L ^ { - 1 } - \phi _ { 2 } L ^ { - 2 } } - 1 \right ]$$

where

$$\frac { 1 } { 1 - \phi _ { 1 } z - \phi _ { 2 } z ^ { 2 } } & = \sum _ { j = 0 } ^ { \infty } R ^ { j } [ \cos ( m j ) + \cot ( m ) \sin ( m j ) ] z ^ { j } \\ \frac { 1 } { 1 - \phi _ { 1 } z ^ { - 1 } - \phi _ { 2 } z ^ { - 2 } } & = \sum _ { j = 0 } ^ { \infty } R ^ { j } [ \cos ( m j ) + \cot ( m ) \sin ( m j ) ] z ^ { - j }$$

$$\phi _ { 1 } ( 1 - \phi _ { 2 } ) = - 4 \phi _ { 2 }$$

$$( 1 - \phi _ { 1 } - \phi _ { 2 } ) ^ { 2 } = - \phi _ { 2 } / \lambda$$

$$C = \frac { - \phi _ { 2 } } { \lambda ( 1 - \phi _ { 1 } ^ { 2 } - \phi _ { 2 } ^ { 2 } + \phi _ { 1 } ^ { 3 } / 2 ) } \\ R = \sqrt { - \phi _ { 2 } }$$

$$\cos ( m ) = \phi _ { 1 } / ( 2 R ) .$$

Roots of (1 - φ 1 z - φ 2 z 2 ) = 0 are complex and outside the unit circle, φ 1 is a real number between 0 and 2 , φ 2 a real number between - 1 and 0, and R a real number between 0 and 1 .

Figure 1 plots the values of φ 1 and φ 2 generated by different values of λ. For λ = 1600 , φ 1 = 1 . 777 and φ 2 = - 0 . 7994 . These imply R = 0 . 8941 , so that the absolute value of the weights decay with a half-life of about 6 quarters while R 60 = 0 . 0012 . 5

4 Related results have been developed by Singleton (1988), King and Rebelo (1989, 1993), Cogley and Nason (1995), and McElroy (2008). Unlike these papers, here I provide simple direct expressions for the values of φ 1 and φ 2 , and my analytical expressions of the HP filter entirely in terms of real parameters in (9) and (10) appear to be new.

5 The other parameters for this case are C = 0 . 056075 , m = 0 . 111687 and cot( m ) = 8 . 9164 .


<!-- p:8 -->


Expression (7) means that for t more than 15 years from the start or end of a sample of quarterly data, the cyclical component c t = y t - g ∗ t is well approximated by

$$c _ { t } = \lambda ( 1 - L ^ { - 1 } ) ^ { 2 } ( 1 - L ) ^ { 2 } g _ { t } ^ { * } = \frac { \lambda ( 1 - L ^ { - 1 } ) ^ { 2 } ( 1 - L ) ^ { 2 } } { F ( L ) } y _ { t } = \frac { \lambda ( 1 - L ) ^ { 4 } } { F ( L ) } y _ { t + 2 } .$$

As noted by King and Rebelo, obtaining the cyclical component for these observations thus amounts to taking fourth differences of the original y t +2 and applying the operator [ F ( L )] - 1 to the result, so that the HP cycle might be expected to produce a stationary series as long as fourth-differences of the original series are stationary. However, De Jong and Sakarya (2016) noted there could still be significant nonstationarity coming from observations near the start or end of the sample, and Phillips and Jin (2015) concluded that for commonly encountered sample sizes, the HP filter may not successfully remove the trend even if the true series is only I (1) .

## 3 Drawbacks to the HP filter.

### 3.1 Appropriateness for typical economic time series.

The presumption by users of the HP filter is that it offers a reasonable approach to detrending for a range of commonly encountered economic time series. The leading example of a time-series process for which we would want to be particularly convinced of the procedure's appropriateness would be a random walk. Simple economic theory suggests that variables such as stock prices (Fama, 1965), futures prices (Samuelson, 1965), long-term interest rates (Sargent, 1976; Pesando, 1979), oil prices (Hamilton, 2009), consumption spending (Hall, 1978), inflation, tax rates, and money supply growth rates (Mankiw, 1987) should all follow martingales or near martingales. To be sure, hundreds of studies have claimed to find evidence of statistically detectable departures from pure martingale behavior in all these series. Even so, there is indisputable evidence that a random walk is often extremely hard to beat in out-of-sample forecasting comparisons, as has been found for example by Meese and Rogoff (1983) and Cheung, Chinn, and Pascual (2005) for exchange rates, Flood and Rose (2010) for stock prices, Atkeson and Ohanian (2001) for inflation, or Balcilar, et al. (2015) for GDP, among many others. Certainly if we are not comfortable with the consequences of applying the HP filter to a random walk, then we should not be using it as an all-purpose approach to economic time series.


<!-- p:9 -->


For y t = y t - 1 + ε t , where ε t is white noise and (1 - L ) y t = ε t , Cogley and Nason (1995) 6 noted that expression (15) means that when the HP filter is applied to a random walk, the cyclical component for observations near the middle of the sample will approximately be characterized by

$$c _ { t } = \frac { \lambda ( 1 - L ) ^ { 3 } } { F ( L ) } \varepsilon _ { t + 2 } .$$

For λ = 1600 this is

$$c _ { t } = 8 9 . 7 2 \left \{ - q _ { 0 , t + 2 } + \sum _ { j = 0 } ^ { \infty } ( 0 . 8 9 4 1 ) ^ { j } [ \cos ( 0 . 1 1 1 7 j ) + 8 . 9 1 6 \sin ( 0 . 1 1 1 7 j ) ] ( q _ { 1 , t + 2 - j } + q _ { 2 , t + 2 + j } ) \right \}$$

with q 0 t = ε t - 3 ε t - 1 +3 ε t - 2 - ε t - 3 , q 1 t = ε t - 3 . 79 ε t - 1 +5 . 37 ε t - 2 - 3 . 37 ε t - 3 +0 . 79 ε t - 4 ) , 7 and q 2 t = - 0 . 79 ε t +1 +3 . 37 ε t - 5 . 37 ε t - 1 +3 . 79 ε t - 2 - ε t - 3 . The underlying innovations ε t are completely random and exhibit no patterns, whereas the series c t is both highly predictable (as a result of the dependence on lags of ε t - j ) and will in turn predict the future (as a result of dependence on future values of ε t + j ) . Since the coefficients that make up [ F ( L )] - 1 are determined solely by the value of λ, these patterns in the cyclical component are entirely a feature of having applied the HP filter to the data rather than reflecting any true dynamics of the data-generating process itself.

6 Harvey and Jaeger (1993) also have a related discussion.

7 The term q 1 t is the expansion of (1 - L ) 3 [1 - ( φ 2 1 / 4) L ] ε t .


<!-- p:10 -->


For example, consider the behavior of stock prices and real consumption spending. 8 The top panels of Figure 2 show the autocorrelation functions for first-differences of these series, confirming that there is little ability to predict either from its own past values, as we might have expected from the literature cited at the start of this section. The lower panels show cross correlations. Consumption has no predictive power for stocks, though stock prices may have a modest ability to anticipate changes in aggregate consumption.

Figure 3 shows the analogous results if we tried to remove the trend by HP filtering rather than first-differencing. The HP cyclical components of stock prices and consumption are both extremely predictable from their own lagged values as well as each other. The rich dynamics in these series are purely an artifact of the filter itself and tell us nothing about the underlying datagenerating process. Filtering takes us from the very clean understanding of the true properties of these series that we can easily see in Figure 2 to the artificial set of relations that appear in Figure 3. The values plotted in Figure 3 summarize the filter, not the data.

### 3.2 Properties of the one-sided HP filter.

The HP trend and cycle have an artificial ability to 'predict' the future because they are by construction a function of future realizations. One way we might try to get around this would be to restrict the minimization problem in (3), forcing a t to load only on values ( y t , y t - 1 , ..., y 1 ) ′

8 Stock prices were measured as 100 times the natural log of the end-of-quarter value for the S&amp;P 500 and consumption from 100 times the natural log of real personal consumption expenditures from the U.S. NIPA accounts. All data for this figure are quarterly for the period 1950:1 to 2016:1.


<!-- p:11 -->


that have been observed as of date t, rather than also using future values as was done in the HP filter end-of-sample HP-filtered series for a sample ending at

(4). The value of this one-sided projection for date t could be calculated by taking the t, repeated for each t. 9 The top panel of Figure 4 shows the result of applying the usual two-sided HP filter to stock prices. The trend is identified to have been essentially flat throughout the 2000s, with the prerecession booms and post-recession busts in stock prices viewed entirely as cyclical phenomena. The bottom panel shows the results of applying a one-sided HP filter to the same data. This would instead identify the trend component as rising during economic expansions and falling during recessions. The reason is that a real-time observer would not know in early 2009, for example, that stock prices were about to appreciate remarkably, and accordingly would have judged much of the drop observed up to that date to be permanent. It is only with hindsight that we are tempted to interpret the 2008 stock-market crash as a temporary phenomenon. Making use of unknowable future values in this way is in fact a fundamental reason that HPfiltered series exhibit the visual properties that they do, precisely because they impose patterns that are not a feature of the data-generating process and could not be recognized in real time. Some researchers might be attracted by the simple picture of the 'long-run' component of stock prices summarized by the top panel of Figure 4. But that picture is just something that their imagination has imposed on the data. And the end-of-sample value obtained from the procedure is actually quite different from what the researcher is seeing in the middle of the sample.

Moreover, although a one-sided filter would eliminate the problem of generating a series that is artificially able to predict the future, changes in both the one-sided trend and its implied cycle are readily forecastable from their own lagged values, and likewise by values of any other variables. Again this is not a feature of the stock prices themselves, but instead is an artifact of choosing to characterize the cycle and trend in this particular way.

9 An easier way to calculate the one-sided projection is with a single pass of the Kalman filter through the entire sample for the state-space model assumed in Proposition 1 with C 0 large and σ 2 c /σ 2 v = 1600 . The Kalman filter gives the one-sided projection while the Kalman smoother gives the usual two-sided HP filter.


<!-- p:12 -->


### 3.3 Data-coherent values for λ.

A separate question is what value we should use for the smoothing parameter λ . Hodrick and Prescott motivated their choice of λ = 1600 based on the prior belief that a large change in the cyclical component within a quarter would be around 5%, whereas a large change in the trend component would be around (1/8)%, suggesting a choice of λ = σ 2 c /σ 2 v = (5 / (1 / 8)) 2 = 1600 . Ravn and Uhlig (2002) showed how to choose the smoothing parameter for data at other frequencies if indeed it would be correct to use 1600 on quarterly data. These rules of thumb are almost universally followed.

It's worth noting that if the state-space representation in Proposition 1 were indeed an accurate characterization of the trend that we were trying to infer, we would not need to make up a value for λ but could in fact estimate it from the data. If for example we assumed a Normal distribution for the innovations ( v t , c t ) ′ we could use the Kalman filter to evaluate the likelihood function for the observed sample ( y 1 , ...., y T ) ′ and find the values for σ 2 v and σ 2 c that maximize the likelihood function. 10 This could alternatively be given a quasi-maximum likelihood interpretation as a GLS minimization of the squared forecast errors weighted by reciprocals of their model-implied variance.

10 See for example Hamilton (1994, equations [13.4.1]-[13.4.2]). Note that although the inferred value for the trend g t depends only on the ratio σ 2 c /σ 2 v , the parameters σ 2 c and σ 2 v are separately identifiable because σ 2 c can be inferred from the average observed size of ( y t - g t ) 2 .


<!-- p:13 -->


Table 1 reports MLEs of σ 2 v , σ 2 c , and λ for a number of commonly studied macroeconomic series. For every one of these we would estimate a value for σ 2 c whose magnitude is similar to, and in fact often smaller than, σ 2 v , and certainly not 1600 times as large. 11 If we used a value of λ = 1 instead of λ = 1600 , the resulting series for g t would differ little from the original data y t itself; λ = 1 implies a value for R in expression (10) of 0 . 48 , which decays with a half-life of less than one quarter .

Thus not only is the HP filter very inappropriate if the true process is a random walk. As commonly applied with λ = 1600, the HP filter is not even optimal for the only example (namely (5)-(6)) for which anyone has claimed that it might provide the ideal inference!

## 4 A better alternative.

Here I suggest an alternative concept of what we might mean by the cyclical component of a possibly nonstationary series: how different is the value at date t + h from the value that we would have expected to see based on its behavior through date t ? 12 This concept of the cyclical component has several attractive features. First, as noted by den Haan (2000), the forecast error is stationary for a wide class of nonstationary processes. Second, the primary reason that we would be wrong in predicting the value of most macro and financial variables at a horizon of h = 8 quarters ahead is cyclical factors such as whether a recession occurs over the next two years and the timing of recovery from any downturn. 13

11 Nelson and Plosser (1982, pages 157-158) have also made this observation.

12 This idea is related to Beveridge and Nelson's (1981) definition of the trend component of y t as g t = lim h →∞ lim p →∞ E ( y t + h | y t , y t - 1 , .., y t - p +1 ) which limit exists and can be calculated provided that (1 - L ) y t is a mean-zero stationary process. Beveridge and Nelson then (somewhat curiously) interpreted the cyclical component as c t = g t - y t . By contrast, here we keep h and p fi xed and take advantage of the fact that g t = E ( y t + h | y t , y t - 1 , .., y t - p +1 ) exists for a broad range of nonstationary processes. We interpret the cyclical component at date t + h as c t + h = y t + h - g t .


<!-- p:14 -->


While it might seem that calculating this concept of the cyclical component requires us already to know the nature of the nonstationarity and to have the correct model for forecasting the series, neither of these is the case. We can instead always rely on very simple forecasts within a restricted class, namely, the population linear projection of y t + h on a constant and the 4 most recent values of y as of date t. This object exists and can be consistently estimated for a wide range of nonstationary processes, as I now show.

### 4.1 Forecasting when the true process is unknown.

Suppose that the d th difference of y t is stationary for some d . For example, d = 2 would mean that the growth rate is nonstationary but the change in the growth rate is stationary. Note the d th difference is also stationary for any series with a deterministic time trend characterized by a d th-order polynomial in time. For any such process we can write the value of y t + h as a linear function of initial conditions at time t plus a stationary process. For example, when d = 1 , letting u t = ∆ y t we can write

$$y _ { t + h } = y _ { t } + w _ { t } ^ { ( h ) }$$

where the stationary component is given by w ( h ) t = u t +1 + · · · + u t + h . For d = 2 and ∆ 2 y t = u t ,

$$y _ { t + h } = y _ { t } + h \Delta y _ { t } + w _ { t } ^ { ( h ) }$$

where now w ( h ) t = u t + h +2 u t + h - 1 + · · · + hu t +1 . This result holds for general d , as demonstrated in the following proposition.

13 This same consideration suggests using h = 24 for monthly data and h = 2 for annual data.


<!-- p:15 -->


Proposition 3. If (1 - L ) d y t is stationary for some d ≥ 1 , then for all finite h ≥ 1 ,

$$y _ { t + h } = \kappa _ { h } ^ { ( 1 ) } y _ { t } + \kappa _ { h } ^ { ( 2 ) } \Delta y _ { t } + \dots + \kappa _ { h } ^ { ( d ) } \Delta ^ { d - 1 } y _ { t } + w _ { t } ^ { ( h ) }$$

with ∆ s = (1 - L ) s , κ (1) l = 1 for l = 1 , 2 , .. and κ ( s ) j = ∑ j l =1 κ ( s - 1) l for s = 2 , 3 , ..., d and w ( h ) t is a stationary process.

It further turns out that if ∆ d y t ∼ I (0) and we regress y t + h on a constant and the d most recent values of y as of date t, the coefficients will be forced to be close to the values implied by the coefficients κ ( j ) h in Proposition 3. For example, if ∆ 2 y t is I (0) then in a regression of y t + h on ( y t , y t - 1 , 1) ′ , the fitted values will tend to y t + h ( y t - y t - 1 ) + μ h for μ h = E ( w ( h ) t ) as the sample size gets large; that is, the coefficient on y t will go to 1 + h and the coefficient on y t - 1 will go to - h. The implication is that the residuals from a regression of y t + h on ( y t , y t - 1 , 1) ′ will be stationary whenever y itself is I (2) . The reason is that any other values for these coefficients would imply a nonstationary series for the residuals, whose sum of squares become arbitrarily large relative to those implied by the coefficients 1 + h and - h as the sample size grows large.

If ∆ d y t is stationary and we regress y t + h on a constant and the p most recent values of y as of date t for any p &gt; d, the regression will use d of the coefficients to make sure the residuals are stationary and the remaining p + 1 - d coefficients will be determined by the parameters that characterize the population linear projection of the stationary variable w ( h ) t on the stationary regressors (∆ d y t , ∆ d y t - 1 , ..., ∆ d y t - p + d +1 , 1) ′ . The following proposition provides a formal statement of these claims. In the proof of this proposition I have followed Stock (1994, p. 2756) in defining a series u t to be I (0) if it has fixed mean μ and satisfies a Functional Central Limit Theorem. 14 This requires that the sample mean of u t has a Normal distribution as the sample size T gets large, as does a sample mean that used only Tr observations for 0 &lt; r ≤ 1 . Formally,


<!-- p:16 -->


$$T ^ { - 1 / 2 } \sum _ { s = 1 } ^ { [ T r ] } ( u _ { t } - \mu ) \Rightarrow \omega W ( r ) ,$$

where [ Tr ] denotes the largest integer less than or equal to Tr, W ( r ) denotes Standard Brownian Motion, and ' ⇒ ' denotes weak convergence in probability measure. I will show that if either the d th difference ( u t = ∆ d y t ) satisfies (18) or if the deviation from a d th-order deterministic polynomial in time ( u t = y t - δ 0 - δ 1 t - δ 2 t 2 -··· - δ d t d ) satisfies (18), then we can remove the nonstationary component with the same simple regression. 15

̸

Proposition 4. Suppose that either u t = ∆ d y t satisfies (18) or that u t = y t - ∑ d j =0 δ j t j with δ d = 0 satisfies (18) for some unknown d . Let x t = ( y t , y t - 1 , ..., y t - p +1 , 1) ′ for some p ≥ d and consider OLS estimation of y t + h = x ′ t β + v t + h for t = 1 , ..., T with estimated coefficient

$$\hat { \beta } = \left ( \sum _ { j = 1 } ^ { T } x _ { t } x _ { t } ^ { \prime } \right ) ^ { - 1 } \left ( \sum _ { j = 1 } ^ { T } x _ { t } y _ { t + h } \right ) .$$

If p = d, the OLS residuals y t + h - x ′ t ˆ β converge to the variable w ( h ) t - E ( w ( h ) t ) in Proposition 3. If p &gt; d, the OLS residuals converge to the residuals from a population linear projection of w ( h ) t on (∆ d y t , ∆ d y t - 1 , ..., ∆ d y t - p + d +1 , 1) ′ .

̸

14 Stock (1994, p. 2749) demonstrated that an example of sufficient conditions that imply (18) is that u t = μ + ∑ ∞ j =0 ψ j η t where η t is a martingale difference sequence with variance σ 2 and finite fourth moment, ψ (1) = 0 , and ∑ ∞ j =0 j | ψ j | &lt; ∞ , in which case ω 2 in (18) is given by σ 2 [ ψ (1)] 2 . Alternatively, Phillips (1987, Lemma 2.2) derived (18) from primitive moment and mixing conditions on u t .

̸

15 The reason to state these as two separate possibilities is that if the nonstationarity is purely deterministic, then the d th differences will not satisfy the Functional Central Limit Theorem. For example, if y t = γ 0 + γ 1 t + ε t with ε t white noise, then ∆ y t = γ 1 + ψ ( L ) ε t for ψ ( L ) = 1 - L and ψ (1) = 0. Of course when u t = ∆ d y t satisfies (18) with μ = 0 , the series y t has both d th-order stochastic as well as d th-order deterministic polynomial trends, so that case, along with pure stochastic trends ( μ = 0) and pure deterministic trends are all allowed by Proposition 4.


<!-- p:17 -->


Proposition 4 establishes that if we estimate an OLS regression of y t + h on a constant and the p = 4 most recent values of y as of date t ,

$$y _ { t + h } = \beta _ { 0 } + \beta _ { 1 } y _ { t } + \beta _ { 2 } y _ { t - 1 } + \beta _ { 3 } y _ { t - 2 } + \beta _ { 4 } y _ { t - 3 } + v _ { t + h } ,$$

$$\hat { v } _ { t + h } = y _ { t + h } - \hat { \beta } _ { 0 } - \hat { \beta } _ { 1 } y _ { t } - \hat { \beta } _ { 2 } y _ { t - 1 } - \hat { \beta } _ { 3 } y _ { t - 2 } - \hat { \beta } _ { 4 } y _ { t - 3 }$$

offer a reasonable way to construct the transient component for a broad class of underlying processes. The series is stationary provided that fourth differences of y t are stationary, a goal that HP intends but does not necessarily achieve. But whereas the approximation to the HP filter in equation (15) imposes all 4 unit roots, the sample regression would only use 4 differences if it is warranted by observed features of the data. The proposed procedure has a number of other advantages over HP. First, any finding that ˆ v t + h predicts some other variable x t + h + j represents a true ability of y to predict x rather than an artifact of the way we chose to detrend y, by virtue of the fact that ˆ v t + h is a one-sided filter 16 . Second, unlike the HP cyclical series c t + h , the value of ˆ v t + h will by construction be difficult to predict from variables dated t and earlier . 17 If we find such predictability, it tells us something about the true data-generating process, for example, that x Granger-causes y. Third, the value of ˆ v t + h is a model-free and essentially assumptionfree summary of the data. Regardless of how the data may have been generated, as long as (1 - L ) d y t is covariance stationary for some d ≤ 4 , there exists a population linear projection of

16 While the OLS coefficients (19) make use of future observations, this influence vanishes asymptotically, in contrast to HP's first-order dependence on future observations. Expression (22) below offers another alternative that allows zero inference of future observations for any sample size T.

17 Note however that c t + h by construction can be predicted by variables known at date t + h - 1 . The value of c t + h will be correlated with its own lagged values c t + h - 1 , c t + h - 2 , ..., c t +1 but likely uncorrelated with c t , c t - 1 , ...

the residuals y t + h on ( y t , y t - 1 , y t - 2 , y t - 3 , 1) ′ . That projection is a characteristic of the data-generating process that can be used to define what we mean by the cyclical component of the process and can be consistently estimated from the data. Given a dynamic stochastic general equilibrium or any other theoretical model that would imply an I ( d ) process, we could calculate this population characteristic of the model and estimate it consistently from the data.


<!-- p:18 -->


### 4.2 Properties in some common settings.

Random walk. Given the literature cited in Section 3.1 it is instructive to examine the consequences if this procedure were applied to a random walk: y t = y t - 1 + ε t . In this case, d = 1 and w ( h ) t = ε t + h + ε t + h - 1 + · · · + ε t +1 . For large samples, the OLS estimates of (20) converge to β 1 = 1 and all other β j = 0 , and the resulting filtered series would simply be the difference

$$\tilde { v } _ { t + h } = y _ { t + h } - y _ { t } ,$$

that is, how much the series changes over an h = 8-quarter horizon, or equivalently the sum of the observed changes over h periods. Note that for h = 8 the filter 1 - L h wipes out any cycles with frequency of exactly one year, and thus is taking out both the long-run trend as well as any strictly seasonal components. 18 This also fits with the common understanding of what we would mean by the cyclical component. Because the simple filter (22) does not require estimation of any parameters, it can also be used as a quick robustness check for concerns about the small-sample applicability of the asymptotic claims in Proposition 4, as will be illustrated in the applications below.

18 As in Hamilton (1994, pp. 171-172), the filter 1 - L 8 has power transfer function (1 - e - 8 iω )(1 - e 8 iω ) = 2 - 2 cos(8 ω ) which is zero at ω = 0 , π/ 4 , π/ 2 , 3 π/ 4 , π and thus eliminates not only cycles at the zero frequency but also cycles that repeat themselves every 8,4,8/3, or 2 quarters. See also Hamilton (1994, Figures 6.5 and 6.6).


<!-- p:19 -->


Deterministic time trend. Another instructive example is a pure deterministic time trend of order d = 1: y t = δ 0 + δ 1 t + ε t for ε t white noise. In this case ∆ y t = δ 1 + ε t - ε t - 1 is stationary and w ( h ) t = ∆ y t +1 + · · · + ∆ y t + h = δ 1 h + ε t + h - ε t is also stationary for any h . I show in the appendix that for this case the limiting coefficients on y t , .., y t - p +1 described by Proposition 4 are each given by 1 /p and the implied trend for y t + h is

$$\delta _ { 0 } + \delta _ { 1 } ( t + h ) + p ^ { - 1 } ( \varepsilon _ { t } + \varepsilon _ { t - 1 } + \cdots + \varepsilon _ { t - p + 1 } ) .$$

Even for p = 1 this is not a bad estimate and for p = 4 should not differ much from the true trend δ 0 + δ 1 ( t + h ) . Again regardless of the choice of p, the difference between y t + h and (23) will be stationary.

Interpreting DSGE's. A third instructive example is when y t is an element of a theoretical dynamic stochastic general equilibrium model that is stationary around some steady-state value μ. If the effects of shocks in the theoretical model die out after h periods, then the linear projection (20) in the theoretical model is characterized by β 0 = μ and β 1 = β 2 = β 3 = β 4 = 0 . In other words, the component v t + h is exactly the deviation from the steady state. If shocks have not completely died out after h periods, then part of what is being labeled trend by this method would include the components of shocks that persist longer than h periods. But for any value of h, the linear projection is a well-defined population characteristic of the theoretical stationary model, and there is an exactly analogous object one can calculate in the possibly nonstationary observed data. The method thus offers a way to make an apples-to-apples comparison of theory with data of the sort that users of the HP filter often desire, but which the HP filter itself will always fail to deliver.


<!-- p:20 -->


### 4.3 Specification of p and h.

One might be tempted to use a richer model than (20) to forecast y t + h , such as using a vector of variables, more than 4 lags, or even a nonlinear relation. However, such refinements are completely unnecessary for the goal of extracting a stationary component, and have the significant drawback that the more parameters we try to estimate by regression, the more the small-sample results are likely to differ from the asymptotic predictions. The simple univariate regression (20) is estimating a population object that is well defined regardless of whether the variable is part of a large vector system with nonlinear dynamics. For this reason, just as the HP filter is always implemented as a univariate procedure, my recommendation is to follow that same strategy for the approach here.

A related issue is the choice of h. For any fixed h, there exists a sample size T for which the results of Proposition 4 hold. However, a bigger sample size T will be needed the bigger is h . The information in a finite data set about very long-horizon forecasts is quite limited. If we are interested in business cycles, a 2-year horizon should be the standard benchmark. It is also desirable with seasonal data to have both p and h be integer multiples of the number of observations in a year. Hence for quarterly data my recommendation is p = 4 and h = 8 .

In other settings the fundamental interest could be in shocks whose effects last substantially longer than two years but are nevertheless still transient. A leading example would be the recent interest in debt cycles prompted by datasets such as developed by Jord` a, Schularick, and Taylor (2016). For such an application I would use h = 5 years, with the regression-free implementation ( y t +5 - y t ) having particular appeal given the length of datasets available.


<!-- p:21 -->


### 4.4 Empirical illustrations.

Figure 5 shows the results when this approach is applied to data on U.S. total employment. The raw seasonally adjusted data ( y t ) are plotted in the upper left panel. The residuals from regression (20) estimated for these data are plotted in black in the lower-left panel, while the 8-lag difference (22) is in red. The latter two series behave very similarly in this case, as indeed I have found for most other applications. The primary difference is that the regression residual has sample mean zero by construction (by virtue of the inclusion of a constant term in the regression) whereas the average value of (22) will be the average growth rate over a two-year period.

One interesting observation is that the cyclical component of employment starts to decline significantly before the NBER business cycle peak for essentially every recession. Note that this inference from Figure 5 is summarizing a true feature of the data and is not an artifact of any forward-looking aspect of the filter.

The right panels of Figure 5 show what happens when the same procedure is applied to seasonally unadjusted data. The raw data themselves exhibit a very striking seasonal pattern, as seen in the top right panel. Notwithstanding, the cyclical factor inferred from seasonally unadjusted data (bottom right panel) is almost indistinguishable from that derived from seasonally adjusted data, confirming that this approach is robust to methods of seasonal adjustment.

Figure 6 applies the method to the major components of the U.S. national income and product accounts. Investment spending is more cyclically volatile than GDP, while consumption spending is less so. Imports fall significantly during recessions, reflecting lower spending by U.S. residents on imported goods, and exports substantially less so, reflecting the fact that international downturns are often decoupled from those in the U.S. Detrended government spending is dominated by war-related expenditures- the Korean War in the early 1950s, the Vietnam War in the 1970s, and the Reagan military build-up in the 1980s.


<!-- p:22 -->


Table 2 reports the standard deviation of the cyclical component of each of these and a number of other series, along with their correlation with the cyclical component of GDP. We find very little cyclical correlation between output and prices. 19 Both the nominal fed funds rate and the ex ante real fed funds rate (the latter based on the measure in Hamilton, et al., 2016) are modestly procyclical, whereas the 10-year nominal interest rate is not.

## 5 Conclusion.

The HP filter is intended to produce a stationary component from an I (4) series, but in practice it can fail to do so, and invariably imposes a great cost. It introduces spurious dynamic relations that are purely an artifact of the filter and have no basis in the true data-generating process, and there exists no plausible data-generating process for which common popular practice would provide an optimal decomposition into trend and cycle. There is an alternative approach that can isolate a stationary component from any I (4) series, preserves the underlying dynamic relations and consistently estimates well-defined population characteristics for a broad class of possible data-generating processes.

19 Identifying the sign of this correlation was one of the primary interests of den Haan's (2000) application of a related methodology. In contrast to the results in Table 2, he found a positive correlation between the cyclical components of these series. I attribute the difference to differences in sample period.


<!-- p:23 -->

<!-- END SOURCE 21/40: Hamilton_2018_never-use-hp-filter.md -->

---

<!-- BEGIN SOURCE 22/40: Hart_1994_time-series-cross-validation.md -->

# Source: `Hart_1994_time-series-cross-validation.md`

---
id: "Hart_1994_time-series-cross-validation"
source_pdf: "../pdf/Hart_1994_time-series-cross-validation.pdf"
source_filename: "Hart_1994_time-series-cross-validation.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/Hart_1994_time-series-cross-validation.references.md"
---

<!-- p:1 -->

## Automated Kernel Smoothing of Dependent Data by using Time Series Cross-Validation

By JEFFREY D. HART†

Texas A&amp;M University, College Station, USA

[Received October 1992. Revised April 1993]

### SUMMARY

The problem of selecting the bandwidth of a kernel regression estimator when the observed data are serially correlated is considered. The bandwidth is selected by using a version of cross-validation that seeks a good one-step-ahead predictor of the data. This method, referred to as time series cross-validation (TSCV), simultaneously estimates an optimal bandwidth and, given a time series model for the errors, the autocorrelation function of the data. In addition, different time series models having the same number of parameters can be compared by using TSCV. Boundary kernels play a key role in the proposed methodology since one-step-ahead prediction entails extrapolating past the available data. Boundary kernels are used at the bandwidth selection stage, but 'proper' kernels are used to estimate the regression function. It is shown that smooth (i.e. at least continuous) boundary kernels have some robustness to misspecification of the error model. This means that a simple correlation model, such as the first-order autoregressive process, will often suffice for selecting a bandwidth. A simulation study and real data examples indicate the usefulness of TSCV for smoothing time series data.

KeywOrds: COVARIANCE STATIONARY TIME SERIES; KERNEL ESTIMATORS; NONPARAMETRIC CURVE ESTIMATION; PREDICTION

## 1. INTRODUCTION

We consider the problem of automatically smoothing dependent data. By automatic methods, we mean methods that are well-defined functions of the data, and not greatly influenced by a subjective choice of model. Here, we shall consider such methods in the setting of time series trend estimation. The trend is to be estimated by a kernel smoother, and we consider the problem of choosing the kernel estimate's smoothing parameter, or bandwidth.

The problems inherent in nonparametric function estimation using correlated data have come under considerable scrutiny. In probability density estimation, moderate serial correlation among identically distributed observations tends to be a relatively minor nuisance (see, for example, Rosenblatt (1970) and Hart (1984)). Hart and Vieu (1990) considered the effect of serial correlation on the crossvalidation method of choosing a kernel density estimator's bandwidth. They showed that cross-validation is reasonably effective unless the data are very highly correlated. Similar results have been obtained by Härdle and Vieu (1992) for estimating an autoregression function of a stationary time series.

The setting of the current paper is essentially fixed design, nonparametric regression with correlated errors. Here, correlation has a more profound effect on an estimator's efficiency than it does in probability density or autoregression function estimation. (See Hall and Hart (1990).) Correlation also greatly complicates the problem of choosing an estimator's smoothing parameter in the fixed design case. Some recent work on smoothing parameter choice includes that of Diggle and Hutchinson (1989), Chiu (1989), Altman (1990), Hurvich and Zeger (1990), Chu and Marron (1991), Hart (1991), Herrmann et al. (1992) and Kohn et al. (1992).

†Address for correspondence: Department of Statistics, Texas A&amp;M University, College Station, TX 77843-3143, USA.

©1994Royal Statistical Society


<!-- p:2 -->


Suppose that we observe data Y1, . . ., Y obeying the model

$$Y _ { j } = \mu _ { j } + \epsilon _ { j } , \quad j = 1 , \, \dots , \, n ,$$

where the μj are unknown constants (comprising the trend) and €1, €2, . . . form a zero-mean covariance stationary time series with covariance function γ. The latter condition implies that cov(€j, €j+k) = γ(k) for all j and k. Here we assume that the data are observed at regularly spaced time points, although the methodology to be proposed extends readily to irregularly spaced data.

We shall estimate the trend at time j by a kernel smoother of the Gasser-Müller form (Gasser and Müller, 1979), i.e. we estimate μj by

Our focus will be on the time series setting, but our results also apply to more general regression settings with correlated errors. A time series trend is usually defined to be slowly changing over time, and so, for practical purposes, we may regard μj as being equal to, say, m {(j−0.5)/n}, where m is a smooth regression function defined on [0, 1].

$$\hat { \mu } _ { j h } = \frac { 1 } { h } \sum _ { i = 1 } ^ { n } \, Y _ { i } \sum _ { ( i - 1 ) / n } ^ { i / n } K \{ \frac { ( j - 0 . 5 ) / n - u } { h } \} \, d u , \quad h \leqslant \frac { j - 0 . 5 } { n } \leqslant 1 - h . \quad ( 1 . 2 ) \quad \frac { \hat { \sigma } } { \hat { \sigma } }$$

The quantity h &gt; 0 is called the bandwidth and determines how smooth the trend estimate is. The kernel is K, which we assume to be a continuous density function that has support (-1, 1), is unimodal and symmetric about 0. Boundary kernels are used to modify βjh when (j−0.5)/n∈ [0, h) or (j−0.5)/n∈ (1−h, 1] (see Gasser and Müller (1979), Müller (1991) and Hart and Wehrly (1992)).

The problem to be considered is data-based selection of βjh's bandwidth. When the errors in model (1.1) are independent, a popular means of choosing h is crossvalidation, which is based on the notion of picking a kernel smoother that provides a good predictor of the data. The observation Y, is predicted by the value βh of a smoother constructed from all the data except Yj. The mean-squared prediction error

$$p ( h ) = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( Y _ { j } - \hat { \mu } _ { j h } ^ { j } \right ) ^ { 2 } \\$$

is computed, and h is chosen to minimize p(h). When the data are independent, a good trend estimate and a good mean-squared error predictor of the data are the same. This is due to the fact that

$$E ( Y _ { j } | Y _ { 1 } , \dots , Y _ { j - 1 } , Y _ { j + 1 } , \dots , Y _ { n } ) = \mu _ { j } ,$$

whenever the Y; are statistically independent.

It is well documented (see Chiu (1989), Diggle and Hutchinson (1989), Altman (1990), Hurvich and Zeger (1990) and Hart (1991)) that this form of cross-validation often yields a very poor undersmoothed estimate of trend when the ej are positively serially correlated. On this score cross-validation appears to fail miserably. However, cross-validation was designed to choose a good predictor of the data, and judged in this way it works quite well. It just so happens that the estimation and prediction problems are no longer consonant when the data are correlated.


<!-- p:3 -->


The aim of this paper is to propose and analyse a method of smoothing parameter selection that has the original flavour of cross-validation, i.e. a method which builds a model from part of the data and then uses that model to predict a datum from another part. In this sense the method proposed is similar in spirit to the leave-oneout approach of Kohn et al. (1992) for choosing the smoothing parameter of a spline estimator. The method to be discussed, which we refer to as time series crossvalidation (TSCV), seeks to find a good one-step-ahead predictor based on past data. This is in contrast with the leave-one-out approach usually used in nonparametric regression (see model (1.3) and Kohn et al. (1992)). Finding a good one-stepahead predictor is often of practical interest with time series data, and hence TSCV seems quite natural. An important aspect of TSCV is that it allows a comparison of different time series models for the errors. In this sense it is more objective than some previous proposals, such as Chiu (1989), Altman (1990), Chu and Marron (1991) and Hart (1991).

Although we focus on bandwidth selection, TSCV can also be applied when forecasting is the primary aim of the data analysis. A study of the methodology in the forecasting context will be taken up elsewhere.

The rest of the paper will proceed as follows. In Section 2 the method is described and some of its aspects discussed. Section 3 contains some theoretical results that provide at least a partial justification for the method. Robustness of TSCV to misspecification of the time series model for the errors is also addressed in Section 3. It is shown that trend estimates obtained by using a simple, but incorrect, correlation model are often reasonable. This robustness is achieved by using an appropriate kernel at the bandwidth selection stage. Finally, in Section 4 the usefulness of TSCV is illustrated with both real and simulated data.

## 2. TIME SERIES CROSS-VALIDATION

Before describing TSCV, it is worthwhile to discuss a fundamental issue. In most st   is  a     i is s dil from which the data were generated. One has a right to feel satisfied if he or she identifies a model that is more consistent with the observed data than any other. In the time series setting it seems intuitively clear that there will often be a large' equivalence class of models, each of which has virtually the same probability of producing data like we observed. In many cases a completely stochastic model would provide just as good an explanation for the data as would model (1.1). (Chaos models are yet another alternative to models containing some stochastic element.) It is important to keep this in mind, since it points out how unrealistic it is to expect an automated method to choose the correct' model. Perhaps the best that we can do is to decide whether one model is more consistent with the observed data than another.

We now consider a smoothing method based on judging a model's prediction capability. The method can be used whenever model (1.1) is assumed and the error process is held to be in a given parametric family of models. For simplicity we shall define the method by modelling the errors as a pth-order autoregressive (or AR(p)) process. In other words, suppose that model (1.1) holds and that {ej} is a covariance stationary, mean 0 process such that


<!-- p:4 -->


$$\epsilon _ { j } \, = \, \phi _ { 1 } \epsilon _ { j - 1 } \, + \, \dots \, + \, \phi _ { p } \epsilon _ { j - p } \, + \, Z _ { j } , \quad j = p + 1 , \, \dots , \, n ,$$

where φ1, ..., φp are unknown parameters, Zp+1, ..., Zn are independent random variables that are independent of ε1, : : ., €p, var (Zj) = σž &lt; ∞, j = p + 1, . . ., n, and the ej have common variance σ2 for j = 1, . . ., n.

An interesting prediction problem in time series is that of predicting the future observation Y, based on the data through time j-1. In model (1.1) with AR(p) errors, if the trend and φ1, . . ., φp were known, a best mean-squared error predictor of Yj given the previous data is

$$\hat { Y } _ { j } = \mu _ { j } + \phi _ { 1 } ( Y _ { j - 1 } - \mu _ { j - 1 } ) \ + \ \dots \ + \ \phi _ { p } ( Y _ { j - p } - \mu _ { j - p } ) .$$

If the trend is unknown, it can be estimated by using a kernel smoother based on the data through time j-1. Define a predictor

$$\hat { Y } _ { j } ( a _ { 1 } , \dots , a _ { p } , \, h ) = \tilde { \mu } _ { j h } ^ { j } + a _ { 1 } ( Y _ { j - 1 } - \tilde { \mu } _ { j - 1 , h } ^ { j } ) + \dots + a _ { p } ( Y _ { j - p } - \tilde { \mu } _ { j - p , h } ^ { j } ) ,$$

where μkh, k = j − p, . . ., j, are values of a kernel smoother that uses only the data Y1,". . ., Yj-1 and has smoothing parameter h. We propose to choose a1, . . ., ap and h to minimize

$$P ( a _ { 1 } , \dots , a _ { p } , \, h ) = \frac { 1 } { n - p } \sum _ { j = p + 1 } ^ { n } \left \{ Y _ { j } - \hat { Y } _ { j } ( a _ { 1 } , \dots , a _ { p } , \, h ) \right \} ^ { 2 } . \quad \\$$

Since j -p, . . ., j are at the right-hand edge of the data used to construct μkh, we to stan us o t ationg estimator μkh is, for 0 &lt; h &lt; 1 and (k−0.5)/n≥ (j −1)/n − h,

$$\tilde { \mu } _ { k h } ^ { j } = \frac { 1 } { h } \sum _ { i = 1 } ^ { j - 1 } Y _ { i } \sum _ { ( i - 1 ) / n } ^ { i / n } K _ { q } \left \{ \frac { ( k - 0 . 5 ) / n - u } { } \right \}$$

where (j−1)/n − qh = (k−0.5)/n, Kq is a kernel with support (−q, 1) and the properties

$$\int _ { - q } ^ { 1 } K _ { q } ( u ) \, d u & = 1 , \\ \int _ { - q } ^ { 1 } u \, K _ { q } ( u ) \, d u & = 0$$

Notice that the predictor Ý(a, . . ., ap, h) is the sum of two terms, one being a trend estimate and the other a predictor of the random variable ej. The latter term explicitly accounts for the possibility of correlation among the e. Use of equation (2.1) often leads to a reasonable estimate of trend even if the time series model is misspecified. This robustness issue will be discussed further in Section 3.

for each q.


<!-- p:5 -->


For any given h, the minimizer 1h, . . ., ph of P(a1, . . ., ap, h) with respect to the a can be obtained explicitly. This leads to a criterion function P(h) = P(1, ·., ph, h) whose minimum with respect to h may be approximated numerically.

We now indicate how to obtain a bandwidth for estimator (1.2) by using the method just described. It will be argued in Section 3 that, if the time series model used in the TSCV criterion is the correct model and μj = m{(j−0.5)/n} for all j and n, then the bandwidth minimizing P(a, . . ., ap, h) is asymptotic to that minimizing the mean average squared error (MASE)

$$M A S ( h ) = n ^ { - 1 } \sum _ { j = p + 1 } ^ { n } E ( \tilde { \mu } _ { j h } ^ { j } - \mu _ { j } ) ^ { 2 } . \quad \ \ ( 2 . 3 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

Let L =K0, where K0 is as in property (2.2), and define

$$J _ { g } = \int g ^ { 2 } ( u ) \, d u \text { and } \sigma _ { g } ^ { 2 } = \int u ^ { 2 } g ( u ) \, d u .$$

Then the minimizer of equation (2.3) is asymptotic to

$$\left \{ J _ { L } S _ { \epsilon } ( 0 ) \Big / \sigma _ { L } ^ { 4 } \int _ { 0 } ^ { 1 } m ^ { \prime \prime } ( x ) ^ { 2 } d x \right \} ^ { 1 / 5 } n ^ { - 1 / 5 } , \\ \stackrel { \dots } { \underset { \partial } { \underset { 3 } { \sim } } }$$

where S, is the spectrum of the error process, i.e.

$$S _ { \epsilon } ( \omega ) = \gamma ( 0 ) \, + 2 \sum _ { k = 1 } ^ { \infty } \, \gamma ( k ) \cos ( \pi k \omega ) , \quad 0 \leqslant \omega \leqslant 1 .$$

The trend estimate that we wish to use is βjh, defined in equation (1.2). The asymptotic minimizer of n− 1Σj=1E(βjh − μj)2 has the same form as expression (2.4) with K substituted for L (see Hart (1991)). The ratio of the two limiting bandwidths is

$$R ( K , L ) = ( J _ { K } \sigma _ { L } ^ { 4 } / J _ { L } \sigma _ { K } ^ { 4 } ) ^ { 1 / 5 } ,$$

which is free of unknown parameters. Hence, we propose the following data-based bandwidth h for use in βjh:

$$\hat { h } = \tilde { h } R ( K , L ) , \quad \stackrel { \circledcirc } { \underset { \stackrel { \circledcirc } { \vee } } { o } }$$

where h is the minimizer of the TSCV curve. With this approach we may use any boundary kernel L at the cross-validation stage and any other second-order kernel at the estimation stage, i.e. L need not be a boundary-modified version of K.

We close this section with a couple of remarks.

Remark 1. In principle any time series model, linear or non-linear, could be used in place of the autoregressive model. All that we need to know is the form of the optimal one-step-ahead predictor for the model in question.

Remark 2. It would be sensible to use TSCV to compare the predictive ability oo dmi ms     te dm ts  e i or parameters. Otherwise we must be concerned with having an overparameterized model. For example, it would not be reasonable to compare autoregressive models of greatly different orders, since the sample prediction error must decrease with increasing order. However, it may be feasible to use a modified form of TSCV with an appropriate penalty for the number of parameters used in the error model. This idea is beyond the scope of the current paper and will be investigated elsewhere.


<!-- p:6 -->


## 3. THEORETICAL RESULTS

Here we do some theoretical analysis of the TSCV curve. Most of the results are asymptotic, on the assumption that n → ∞ in the model

$$Y _ { i } = m \left ( \frac { i - 0 . 5 } { n } \right ) + \epsilon _ { i n } , \quad i = 1 , \dots , n , \quad \ \ ( 3 . 1 a ) \ \ \ \frac { \cup } { \cup }$$

where m has two continuous derivatives on [0, 1] and, for all n,

$$\text {cov} \left ( \epsilon _ { i n } , \, \epsilon _ { j n } \right ) = \gamma ( \, | i - j | \, ) , \quad 0 \, \leqslant | i - j | \, \leqslant n - 1 , \quad \\$$

for some covariance function γ. This model cannot be expected to hold literally in cases where we observe ever more data from the same time series. None-the-less, the asymptotic results obtained provide considerable insight about the operating characteristics of the TSCV curve.

To simplify notation we shall assume that the error model fitted to the data is of AR(1) form. At this point we are not assuming that the true covariance function γ corresponds to that of an AR(1) process. In fact, some of our results address what happens when γ is not of AR(1) form. It should become clear that our basic conclusions can be generalized to settings where any given parametric model is fitted to the data.

As proposed in Section 2, we choose a and h to minimize

$$P ( a , \, h ) = \frac { 1 } { n - 1 } \sum _ { j = 2 } ^ { n } \, ( e _ { 2 }$$

$$e _ { 1 j h } = Y _ { j - 1 } - \tilde { \mu } _ { ( j - 1 ) , h } ^ { j } , & \Big ) _ { j = 2 } , \dots , n . \\ e _ { 2 j h } = Y _ { j } - \tilde { \mu } _ { j h } ^ { j } , & \Big ) _ { j = 2 } , \dots , n .$$

where

For any given h, the minimizer of P(a, h) is

$$h = \sum _ { j = 2 } ^ { n } e _ { 1 j h } e _ { 2 j h } \Big / \sum _ { j = 2 } ^ { n } e _ { 1 j h } ^ { 2 } ,$$

and hence the TSCV bandwidth minimizes

$$a n d \text { hence the } & \text {Src} \, \text { bandwidth} \, \underset { \infty } { \min } \, \underset { \infty } { \max } \\ & P ( h ) = \frac { 1 } { n - 1 } \sum _ { j = 2 } ^ { n } \, \left ( e _ { 2 j h } - \hat { \phi } _ { 1 h } e _ { j h } \right ) ^ { 2 } . \\ \text {Define } S _ { i n } & = \left ( n - 1 \right ) ^ { - 1 } \Sigma _ { j = 2 } ^ { n } e _ { i jh , \, i } ^ { 2 } , \, i = 1 , \, 2 , \, \text { and } \, C _ { h } \, = \, ( n - 1 ) ^ { - 1 } \Sigma _ { j = 2 } ^ { n } e _ { i jh } e _ { 2 j h } . \text { Then } \\ & P ( h ) = S _ { 2 h } - C _ { h } ^ { 2 } / S _ { 1 h } .$$

It is easy to show that

$$P ( h ) = T _ { n } ( h ) \, + \, U _ { n } + R _ { n } ( h ) ,$$


<!-- p:7 -->


where

$$T _ { n } ( h ) = S _ { 2 h } - \hat { \sigma } ^ { 2 } + \hat { \rho } _ { 1 } ^ { 2 } ( S _ { 1 h } - \tilde { \sigma } ^ { 2 } ) \, - 2 \hat { \rho } _ { 1 } \{ C _ { h } - \hat { \gamma } ( 1 ) \} ,$$

∂2 = (n−1)−1∑j=23, σ2 = (n−1)−1∑q=1e3, γ(1) = (n−1)−1Σj=26j∈j-b ρ1 = γ(1)/σ2, Un is a random variable free of h and R(h) is a random variable depending on n and h. Expression (3.3) is useful in describing the behaviour of P(h) when it is minimized over a set of h of the form [ln, 1], where ln → 0 and nln → ∞ as n→ ∞. (The quantity ln will satisfy these conditions throughout this section.) Theoretically, this is the only relevant set since under model (3.1) the asymptotically optimal bandwidth h is such that hn ~ Cn-1/5. Practically, however, bandwidths of the form c/n, where c &gt; 0 is a constant, cannot be neglected when investigating the TSCV bandwidth. The behaviour of P(c/n) will be described by direct use of equation (3.2).

Much can be learned about the operating characteristics of TSCV by simply considering E{T(h)} as a function of h. A more detailed theoretical analysis of P(h) will be done elsewhere. However, some of our conjectures based on analysing E{T(h)} will be borne out in the simulation study in Section 4.

Let {hn} be a sequence of bandwidths such that h →0 and nh→∞. An argument available from the author shows that under general conditions R(h) is asymptotically negligible in comparison with T(h). Since U is free of h, this suggests that the minimizer of P(h) over h∈ [ln, 1] behaves like the minimizer of T(h) over the same set.

Arguing as in Hart (1991), it is straightforward to show that, as n → ∞, h → 0 and nh → ∞,

$$E \{ T _ { n } ( h ) \} = ( 1 - \rho _ { 1 } ) ^ { 2 } \left [ M A S E \left ( h \right ) + \frac { L \left ( 0 \right ) } { n h } \left \{$$

$$\{ T _ { n } ( h ) \} & = ( 1 - \rho _ { 1 } ) ^ { 2 } \left [ M A S E ( h ) + \frac { L ( 0 ) } { n h } \left \{ \gamma ( 0 ) \, \frac { 1 + \rho _ { 1 } } { 1 - \rho _ { 1 } } - S _ { \epsilon } ( 0 ) \, \right \} \right ] \\ & + o \{ M A S E ( h ) + 1 / n h \} ,$$

where ρ1 = γ(1)/γ(0), MASE(h) is defined in equation (2.3) and L is the boundary kernel with q = 0 (see properties (2.2)) used in the TSCV criterion. This result points out some interesting aspects of TSCV. First, if the errors follow an AR(1) model, then minimizing E{Tn(h)} is equivalent, asymptotically, to minimizing MASE(h), since S€(0) = γ(0)(1 +ρ1)/(1−ρ1) for an AR(1) process. Using a similar argument, we may establish much more generally that, when the fitted model matches the true error model, then minimizing E{T(h)} is tantamount to minimizing MASE(h). This observation is the basis of the proposal in Section 2 for modifying the TSCV bandwidth to obtain a bandwidth for use in βjh.

Expression (3.4) also yields insight about the robustness of TSCV to misspecifying the error model. The most obvious way to make TSCV robust is to use a kernel L such that L(0) =0. Doing so leads to a TSCV curve whose expected value is approximately proportional to MASE(h) +constant even when the correlation model is misspecified. Interestingly, each of the smooth, optimum boundary kernels derived by Müller (1991) has the property L(0) =0. If we use, for example, L(u) = 6u(1 - u)(6– 10u) I(0,1) (u), then we have a kernel that is at once 'optimum' in a class of continuous kernels and robust to misspecification of the error model. If, perhaps for aesthetic reasons, we wish to use a boundary kernel with L(0) &gt; 0, then equation (3.4) leads to some further insights. For example, by using the minimum variance boundary kernel L(u) = (4− 6u) I(0,1) (u) (see Gasser and Müller (1979)), the asymptotic minimizer of E{T(h)} over [ln, 1] is guaranteed to be of the form Cn-'/5, where C &gt; 0. This result is in sharp contrast with the lack of robustness exhibited by ordinary cross-validation (see Hart (1991)). Presumably, MASE-based methods such as that of Hermann et al. (1992) also have the property that h ~ Cn-1/5when the error model is misspecified.


<!-- p:8 -->


The above analysis no longer holds if h is of the form c/n for c a positive constant. Under model (3.1) this is not of great concern for large n since the relevant bandwidths satisfy nh → ∞. However, in practice we have only one sample size, and the behaviour of P(h) near h =0 is important.

$$Z _ { 1 } ( c ) & = \epsilon _ { j - 1 } - \sum _ { 1 \leqslant i \leqslant c + 3 / 2 } \epsilon _ { j - i } w _ { i - 1 } ( c ) , \\ Z _ { 2 } ( c ) & = \epsilon _ { j } - \sum _ { 1 \leqslant i \leqslant c + 1 / 2 } \epsilon _ { j - i } w _ { i } ( c ) ,$$

$$1 \leqslant i \overline { \lesssim c } + 1 / 2$$

$$w _ { i } ( c ) & = \sum _ { ( i - 0 . 5 ) / c } ^ { ( i + 0 . 5 ) / c } L ( u ) \, d u . \\$$

Define

where

Then it is straightforward to show using equation (3.2) that P(c/n) converges in probability, as n → ∞, to

$$M ( c ) = E \{ Z _ { 2 } ^ { 2 } ( c ) \} ( 1 - \rho _ { c } ^ { 2 } ) \, ,$$

where ρc = corr {Z1(c), Z2(c)}. Now, when the true error model is AR(1),

$$\lim _ { n \to \infty } \{ E \{ P ( c / n ) \} ] \, > \, \lim _ { n \to \infty } \left [ E \{ P ( h ) \} \right ] = \gamma ( 0 ) \left ( 1 - \rho _ { 1 } ^ { 2 } \right )$$

for any sequence of hs such that h → 0 and nh → ∞. This follows from the fact that ρ1€j-1 has the smallest mean-squared error among all predictors of ej based on €1, . . ., €j-1. If the AR(1) model is incorrect though, lim→∞[E{P(c/n)}] can be smaller than γ(0)(1 −ρ). Hence, if we minimize P(h) over h∈ (0, 1), then the minimum of the TSCV curve (with L(0) =0) will occur near the MASE optimal h only when γ(0)(1 −ρ) &lt; infc&gt;o{M(c)}. The important issue becomes whether or not ρ1€j-1 is a better mean-squared error predictor of ej than is the 'kernel' predictor

$$\sum _ { 1 \leq i \leq c + 1 / 2 } \epsilon _ { j - i } w _ { i } ( c ) + \tilde { \rho } _ { c } \left \{ \epsilon _ { j - 1 } - \sum _ { \iota \leq i \leq c + 3 / 2 } \epsilon _ { j - i } w _ { i - 1 } ( c ) \right \} ,$$

where ρc = ρc{E Z2(c)/E Z}(c)}/2. Herein lies TSCV's susceptibility to the identifiability problem discussed at the beginning of Section 2. TSCV will avoid this problem to the extent that the data analyst can choose a time series model for the errors with more predictive ability than the 'haphazard'kernel predictor (3.5).

## 4. SIMULATION STUDY AND DATA ANALYSIS

A small scale simulation study was conducted to gain some insight into the finite sample behaviour of TSCV. Data were generated from a model of the form (3.1), where


<!-- p:9 -->


$$m ( x ) = 1 0 + 1 0 0 \left ( \frac { x } { 2 } \right ) ^ { 3 } \left ( 1 - \frac { x } { 2 } \right ) ^ { 3 } , \quad 0 \leq x \leq 1 . \\ \intertext { a $ w e r $ o b t a i n d $ f o r $ u n d $ e x $ l e c $ p a r $ s $ } \intertext { a $ w e r $ o b t a i n d $ f o r $ u n d $ e x $ l e c $ p a r $ s $ } \intertext { a $ w e r $ o b t a i n d $ f o r $ u n d $ e x $ l e c $ p a r $ s $ }$$

For each set of observations Y1, . . ., Y1oo, bandwidth (2.5) was computed for two choices of the boundary kernel used in μkn. One boundary kernel was a smooth, optimum boundary kernel of Müller (i991), and the other was obtained by multiplying the Epanechnikov kernel by a linear function. The kernel K used in βjh was the Epanechnikov kernel throughout the study. For q=0, the two boundary kernels are respectively

Data were obtained from four models for the error process: AR(1) with φ, = 0, 0.3, 0.7 and AR(2) with φ1= 1, φ2= −0.6. For each of the four error models ε ~ N(0, 0.252), i= 1, . . ., n. The same sample size, n = 100, was used in every case, and 1000 replications were performed for each error model.

$$L _ { 1 } ( u ) = 6 u ( 1 - u ) \left ( 6 - 1 0 u \right ) I _ { [ 0 , 1 ] } ( u )$$

$$L _ { 2 } ( u ) = \frac { 1 2 } { 1 9 } \left ( 8 - 1 5 u \right ) \left ( 1 - u ^ { 2 } \right ) I _ { [ 0 , 1 ] } \left ( u \right ) ,$$

with R(K, L1) = 0.6424 and R(K, L2) = 0.5371. Note that L1(0) =0 and L2(0) = 8 × 12/19. When the errors were AR(1), the error model used to compute P(h) was AR(1), leading to two TSCV bandwidths, one for each type of boundary kernel. For the AR(2) errors, both the AR(1) and the AR(2) models were used for

TABLE 1 Simulation results when the errors follow an AR(1) process†

|                        | <PI       | h ev                           | hTsev,l                             | hTsev,2                                          | h o               |
|------------------------|-----------|--------------------------------|-------------------------------------|--------------------------------------------------|-------------------|
| mean(h)                | 0         | 0.2308                         | 0.2007 0.2299 ( -0.0290)2           | 0.2290 0.0093 0.0527 0.0973 2 0.085 0.135 0.1302 | 0.2197            |
|                        | 0.3 0.7 0 | 0.0667 0.0169 2                | 0.3072                              | 0.3116                                           | 0.2589            |
| {mean(h) - mean(h o)}2 | 0.3 0.7   | 0.0111 ( -0.1922)2 ( -0.3308)2 | ( -0.0190)2                         | 0.4450 2 2                                       | 0.3477            |
| var(h)                 | 0 0.3     | 0.101 2 0.077 2 0.007 2        | ( -0.0405)2 0.044 2 0.054 2 0.098 2 | 2 2                                              | 0.061 2 0.088 2 2 |
| corr(h, h o )          | 0.7 0 0.3 | -0.29 -0.09                    | -0.23 -0.14                         | -0.25 -0.11                                      | 0.116             |
| mean {ASE(h)} x 1000   | 0.7 0     | 0.03 4.061                     | -0.03 3.640                         | -0.08 3.581                                      | 2.826             |
|                        | 0.3       | 20.275                         | 6.112                               | 6.250                                            | 4.823             |
|                        | 0.7       | 48.183                         | 14.332                              | 13.278                                           | 10.518            |

and


<!-- p:10 -->


TABLE 2 Simulation results when the errors follow an AR(2) process †

|                                                                                | li cv                        | IiAR1.1                             | IiAR1. 2                         | IiAR2.1                                | IiAR2.2                               | lio                  |
|--------------------------------------------------------------------------------|------------------------------|-------------------------------------|----------------------------------|----------------------------------------|---------------------------------------|----------------------|
| mean(li) {mean(li)- mean(li o ) }2 var(li) corr(li, lio) mean {ASE(Ii)} x 1000 | 0.0107 ( -0.2233)2 O. 48.114 | 0.2635 0.0295 2 0.043 2 -0.05 3.626 | 0.4945 0.2605 2 O.I~ -0.10 7.567 | 0.2076 ( -0.0264)2 0.047 2 -0.19 4.310 | 0.2235 (- 0.0105)2 0.1002 -0.17 5.220 | 0.2340 0.068 2 3.154 |

†The results are based on 1000 replications, n =100 and regression function (4.1). The AR parameters were φ1 = 1.0 and φ2 = − 0.6. The bandwidths hCv and h0 are as defined in Table 1. The bandwidth hARi,j, i = 1, 2, j = 1, 2    t     t       ( o Table 1.

each type of boundary kernel. Use of the AR(1) model in the latter case allows us to investigate the robustness of TSCV to misspecification of the error model.

The error criterion used to assess a given estimate βjh was average squared error (ASE), defined by

$$\overline { n } _ { \lambda }$$

For each set of data, ASE(h) was computed at each TSCV bandwidth, at the ordinary cross-validation bandwidth and at the minimizer of ASE(h) for the given set of data. All TSCV curves were computed at b1, . . ., b6s, a grid of evenly spaced points on the interval [0.02, 0.98], whereas the ASE and ordinary crossvalidation curves were computed at 0.5371b1, . . ., 0.5371b65.

The results are summarized in Tables 1 and 2. When the correct error model was used, TSCV performed quite well. The clearest pattern emerging from the study

16

14

TSCV

12

10

8

0.0

0.1

0.2

0.3

0.4

h

Fig. 1. TSCV curves for the mile race data; - , AR(1) error model; -----, AR(2) error model


<!-- p:11 -->


Fig. 2. TSCV curves for the Beveridge data: —, AR(1) error model; -----, AR(2) error model

0.050

0.045

0.040

TSCV

0.035

0.030

0.0

0.1

0.2

0.3

0.4

h

Fig. 3. Mile race data and kernel smoother curves (each curve is an Epanechnikov kernel estimate with boundary correction): TSCV bandwidth corresponding to an AR(1) error model; ....., ordinary cross-validation estimate

280

270

seconds

260

250

240

230

1860

1880

1900

1920

1940

1960

1980

years

was that the bandwidth obtained by using boundary kernel L, was considerably leos ndsg  tg  t ng n  a d tsitg the study was the performance of the TSCV bandwidth based on L, when the error model was misspecified (Table 2). This lends credence to the argument in Section 3 for robustness of boundary kernels with L(0) =0. The fact that hAR1,2 tended to be too large is also consistent with equation (3.4), since L2(0) &gt; 0 and s  s  (    = (/() −- (- )/( + 1) contrast with the oversmoothing of hAR1,2, we see in Tables 1 and 2 the characteristic undersmoothing of ordinary cross-validation when the data are positively autocorrelated.


<!-- p:12 -->


Fig. 4. Beveridge data and kernel smoother curves (each curve is an Epanechnikov kernel estimate with boundary correction): TSCV bandwidth corresponding to AR(1) error model; -----, TSCV bandwidth corresponding to AR(2) error model

HART

9

5

log of price index

4

3

1500

1600

1700

1800

years

It is of interest to consider the case where the errors are uncorrelated, i.e. φ =0 in the AR(1) model. Here, the median of the ratios ASE(hTscv,2)/ASE(hcv) was 0.977 and ASE(htscv,2) &lt; ASE(hcv) in 548 of the 1000 replications. The latter result and the sign test show that median {ASE(hτscv,2)/ASE(hcv)} is significantly smaller than 1 (P-value 0.0024).

It is worth noting the tendency for the data-driven bandwidths to be negatively correlated with the bandwidth minimizing the ASE. This is a well-documented aspect of cross-validation, as seen in Scott and Terrell (1987), Härdle et al. (1988) and Hall and Johnstone (1992).

More interesting is to consider the relative risk regret studied by Hall and Johnstone (1992). Define R(h) to be the mean of ASE(h) over the 1000 replications. Then the relative risk regret is estimated by {R(hTscv,2) − R(h0)}/ {R(hcv) − R(h0)} = (3.581 -2.826)/(4.061 -2.826) = 0.61, i.e. hrscv,2 accounted for about 39% of the possible savings when comparing the risk of ordinary cross-validation with the best possible risk. Apparently, there is a pay-off to modelling correlation in the data, even when the correlation is spurious!

In their simulation study the method proposed by Hall and Johnstone (1992) achieved about 70% of the possible risk savings. Although our method achieved less, it has the virtue of being completely automated. There also remains the possibility that another time series model is, in some sense, more robust to spurious autocorrelation than is the AR(1) model. This possibility warrants further study.

TSCV is now applied to two sets of time series data. One set consists of yearly low times in the mile race over the period 1860-1982, and the other is the yearly Beveridge index of wheat prices in Europe from 1500 to 1869. (The latter set may be found in Anderson (1971).) Three cross-validation curves were computed for each data set; the ordinary cross-validation curve and two TSCV curves, corresponding to AR(1) and AR(2) error models. The TSCV curves are shown in Figs 1 and 2.


<!-- p:13 -->


For the mile race data the two TSCV curves are in close agreement and lead to the less wiggly estimate in Fig. 3. However, for the price index data, the AR(2) model has substantially smaller average prediction error than does the AR(1) model. The two models also lead to somewhat different trend estimates (Fig. 4).

The use of ordinary cross-validation in each data set leads to a very wiggly trend estimate. In the mile race case, for example, the smoother trend estimate seems much more satisfying. The short run smoothness in the data is most probably a function of the particular athletes who were involved, and hence better modelled as a random effect. However, the downward trend in times would not be expected to change much from one population of top athletes to another and is thus more reasonably labelled'deterministic',

### ACKNOWLEDGEMENTS

The author is grateful to a referee for pointing out that certain boundary kernels proposed by Müller (1991) are continuous, a property that increases the robustness of TSCV to misspecifying the error model. The author also appreciates the keen eye of Seongbaek Yi, who pointed out an error in the revision.

<!-- END SOURCE 22/40: Hart_1994_time-series-cross-validation.md -->

---

<!-- BEGIN SOURCE 23/40: Hodrick_1997_postwar-us-business-cycles.md -->

# Source: `Hodrick_1997_postwar-us-business-cycles.md`

---
id: "Hodrick_1997_postwar-us-business-cycles"
source_pdf: "../pdf/Hodrick_1997_postwar-us-business-cycles.pdf"
source_filename: "Hodrick_1997_postwar-us-business-cycles.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/Hodrick_1997_postwar-us-business-cycles.references.md"
---

<!-- p:1 -->

Postwar U.S. Business Cycles: An Empirical Investigation

Author(s): Robert J. Hodrick and Edward C. Prescott

Source: Journal of Money, Credit and Banking, Vol. 29, No. 1 (Feb., 1997), pp. 1-16

Published by: Blackwell Publishing

Stable URL:

[http://www.jstor.org/stable/2953682](http://www.jstor.org/stable/2953682?origin=JSTOR-pdf)

Accessed: 10/07/2009 11:45

Your use of the JSTOR archive indicates your acceptance of JSTOR's Terms and Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp. JSTOR's Terms and Conditions of Use provides, in part, that unless you have obtained prior permission, you may not download an entire issue of a journal or multiple copies of articles, and you may use content in the JSTOR archive only for your personal, non-commercial use.

Please contact the publisher regarding any further use of this work. Publisher contact information may be obtained at http://www.jstor.org/action/showPublisher?publisherCode=black.

Each copy of any part of a JSTOR transmission must contain the same copyright notice that appears on the screen or printed page of such transmission.

JSTOR is a not-for-profit organization founded in 1995 to build trusted digital archives for scholarship. We work with the scholarly community to preserve their work and the materials they rely upon, and to build a common research platform that promotes the discovery and use of these resources. For more information about JSTOR, please contact support@jstor.org.

Blackwell Publishing is collaborating with JSTOR to digitize, preserve and extend access to Journal of Money, Credit and Banking.

<!-- p:2 -->


## ROBERT J. HODRICK EDWARD C. PRESCOTT

Postwar U.S. Business Cycles: An Empirical Investigation

We propose a procedure for representing a time series as the sum of a smoothly varying trend component and a cyclical component. We document the nature of the comovements of the cyclical components of a variety of macroeconomic time series. We find that these comovements are very different than the corresponding comovements of the slowly varying trend components.

THE PURPOSE OF THIS ARTICLE is to document some features of aggregate economic fluctuations sometimes referred to as business cycles. The investigation uses quarterly data from the postwar U.S. economy. The fluctuations studied are those that are too rapid to be accounted for by slowly changing demographic and technological factors and changes in the stocks of capital that produce secular growth in output per capita.

As Lucas (1981) has emphasized, aggregate economic variables in capitalist economies experience repeated fluctuations about their long-term growth paths. Prior to Keynes' General Theory, the study of these rapid fluctuations, combined with the attempt to reconcile the observations with an equilibrium theory, was regarded as the main outstanding challenge of economic research. Although the Keynesian Rev-

Support of the National Science Foundation is acknowledged. We also acknowledge helpful comments by the participants at the 1979 Summer Warwick Workshop on Expectation and the money workshops at the Üniversities of Chicago and Virginia and at Carnegie-Mellon University. In particular, we thank Robert Avery, V.V. Chari, Lars Peter Hansen, Charles R. Nelson, Thomas J. Šargent, Kenneth J. Singleton, and John H. Wood for comments. We also thank the Wharton Economic Forecasting Associates for providing the data.

This paper is substantially the same as our 1981 working paper. The only major change to the paper is the addition of an Appendix of Tables that mirror our originals and contain data ending in 1993. Sinče we did not update the citations, we apologize to the many authors who have used the Hodrick-Prescott filter and studied its properties in the intervening eighteen years since its original development.

RoBERT J. HoDRICk is Nomura Professor of International Finance at the Graduate School of Business, Columbia University. EDWARD C. PREsCoTT is Regents' Professor at the University of Minnesota and Advisor to the Federal Reserve Bank of Minneapolis. Both are research associates of the National Bureau of Economic Research.

Journal of Money, Credit, and Banking, Vol. 29, No. 1 (February 1997) Copyright 1997 by The Ohio State University Press olution redirected effort away from this question to the one of determining the level of output at a point in time in disequilibrium, the failure of the Keynesian Theory in the 1970s has caused many economists to want to return to the study of business cycles as equilibrium phenomena. In their search for an equilibrium model of the business cycle, modern economists have been guided by the insights of Mitchell (1913) and others who have used techniques of analysis that were developed prior to the development of modern computers. The thesis of this paper is that the search for an equilibrium model of the business cycle is only beginning and that studying the comovements of aggregate economic variables using an efficient, easily replicable technique that incorporates our prior knowledge about the economy will provide insights into the features of the economy that an equilibrium theory should incorporate.


<!-- p:3 -->


This study should be viewed as documenting some systematic deviations from the restrictions upon observations implied by neoclassical growth theory.1 Our statistical approach does not utilize standard time series analysis. Our prior knowledge concerning the processes generating the data is not of the variety that permits us to specify a probability model as required for application of that analysis. We proceed in a more -anu  u  a ant u or  smu  u snuco nomic theory. The maintained hypothesis, based upon growth theory considerations, sh is so sons ss oe sae  s oi et t ser time. The sense in which it varies smoothly is made explicit in section 1.

We find that the nature of the comovements of the cyclical components of macroeconomic time series are very different from the comovements of the slowly varying components of the corresponding variables. Growth is characterized by roughly proportional growth in (per capita) output, investment, consumption, capital stock and productivity (output per hour), and little change in the hours of employment per capita or household. In contrast, the cyclical variations in output arise principally as the result of changes in cyclical hours of employment and not as the result of changes in cyclical productivity or capital stocks. In the case of the cyclical capital stocks in both durable and nondurable manufacturing industries, the correlation with cyclical output is even negative. Another difference is in the variability of components of aggregate demand. Cyclical consumption varies only one-half and investment three times as much as does cyclical output.

Section 2 presents our findings regarding the comovements of these series with the cyclical component of real GNP, as well as an examination of the cyclical components of prices, interest rates, and nominal and real money balances. Section 3 examines the serial correlation properties of a number of the series.

Several researchers, using alternative methods, have added and are adding to our knowledge of aggregate economic fluctuations.2 Our view is that no one approach dominates all the others and that it is best to examine the data from a number of different perspectives. We do think our approach documents some interesting regularities.

1. Lucas (1980) interprets the work of Mitchell (1913) in a similar light.

2. Examples include Litterman and Sargent (1979), Nelson and Plosser (1980), Neftci (1978), Sargent and Sims (1977), Sims (1980, a, b), and Singleton (1980).


<!-- p:4 -->


### 1. DECOMPOSITION PROCEDURE

The observed time series are viewed as the sum of cyclical and growth components. Actually, there is also a seasonal component, but as the data are seasonally adjusted, this component has already been removed by those preparing the data series. If growth accounting provided estimates of the growth component with errors that were small relative to the cyclical component, computing the cyclical component would be just a matter of calculating the difference between the observed value and the growth component. Growth theory accounting (cf. Denison 1974), in spite of its considerable success, is far from adequate for providing such numbers. If our prior knowledge were sufficiently strong so that we could model the growth component as a deterministic component, possibly conditional on exogenous data, plus a stochastic process and the cyclical component as some other stochastic process, estimating the cyclical component would be an exercise in modern time series analysis. Our prior knowledge is not of this variety, so these powerful methods are not applicable. Our prior knowledge is that the growth component varies "smoothly" over time.

Our conceptual framework is that a given time series y, is the sum of a growth component gt and a cyclical component c,:

$$y _ { t } = g _ { t } + c _ { t } \quad \text {for } t = 1 , \dots , T \, .$$

Our measure of the smoothness of the {g} path is the sum of the squares of its second difference. The c, are deviations from g, and our conceptual framework is that over long time periods, their average is near zero. These considerations lead to the following programming problem for determining the growth components:

$$\min _ { \{ g _ { t } \} _ { r = - 1 } ^ { T } } \left \{ \sum _ { t = 1 } ^ { T } c _ { t } ^ { 2 } + \lambda \sum _ { t = 1 } ^ { T } \left [ ( g _ { t } - g _ { t - 1 } ) - ( g _ { t - 1 } - g _ { t - 2 } ) \right ] ^ { } { 2 } \right \}$$

where c, = yt — gr. The parameter λ is a positive number which penalizes variability in the growth component series. The larger the value of λ, the smoother is the solution series. For a sufficiently large λ, at the optimum all the gt+1 – g must be arbitrarily near some constant β and therefore the gt arbitrarily near go + βt. This implies that the limit of solutions to program (2) as λ approaches infinity is the least squares fit of a linear time trend model.

Our method has a long history of use, particularly in the actuarial sciences. There it is called the Whittaker-Henderson Type A method (Whittaker 1923) of graduating or smoothing mortality experiences in constructing mortality tables. The method is still in use.3 As pointed out in Stigler's (1978) historical review paper, closely related methods were developed by the Italian astronomer Schiaparelli in 1867 and in the ballistic literature in the early forties by, among others, von Neuman.

3. We thank Paul Milgrom for bringing to our attention that the procedure we employed has been long used in actuarial science.


<!-- p:5 -->


Value of the Smoothness Parameter

The data analyzed, with the exception of the interest rates, are in natural logarithms so the change in the growth component, gt — gt–1, corresponds to a growth rate.

The growth rate of labor's productivity has varied considerably over this period (see McCarthy 1978). In the 1947–53 period, the annual growth rate was 4.20 pere 1   -    1  1   r cent, and in the subsequent period it was even smaller. Part of these changes can be ec o co  r r r-g n   rog on labor force. But, as shown by McCarthy, a sizable and variable unexplained component remains, even after correcting for cyclical factors. The assumptions that the growth rate has been constant over our thirty-year sample period, 1950–79, is not tenable. To proceed as if it were would result in errors in modeling the growth component and these errors are likely to be nontrivial relative to the cyclical component. For this reason, an infinite value for the smoothness parameter was not selected.

The following probability model is useful for bringing to bear prior knowledge in the selection of the smoothing parameter λ. If the cyclical components and the second differences of the growth components were identically and independently distributed, normal variables with means zero and variances σ and σ2 (which they are not), the conditional expectation of the g, given the observations, would be the solution to program (2) when √λ = σ1/σ2.

As this probability model has a state space representation, efficient Kalman filtering techniques can be used to compute these g.4 By exploiting the recursive structure, one need not invert a (T + 2) by (T + 2) matrix (T is the number of observations in the sample) as would be necessary if one solved the linear first-order conditions of program (2) to determine the gr. The largest matrix that is inverted using the Kalman filtering computational approach is 2 by 2. If T is large, this is amc  a o  c s t l  s acal rounding problems when implemented on computers. Kalman filtering can be performed with computer packages that are widely available.

Our prior view is that a 5 percent cyclical component is moderately large, as is a one-eighth of 1 percent change in the growth rate in a quarter. This led us to select √λ = 5/(1/8) = 40 or λ = 1,600 as a value for the smoothing parameter. One issue is, how sensitive are the results to the value of λ that is selected? To explore this issue, various other values of λ were tried. Table 1 contains the (sample) standard deviations and autocorrelations of cyclical real GNP for the selected values of the smoothing parameter as well as statistics to test for the presence of a unit root in the cyclical components.5 These numbers change little if λ is reduced by a factor of four to 400 or increased by a factor of four to 6,400. As λ increases, the standard deviation increases and there is greater persistence, with the results being very different for λ = ∞. It is noteworthy that only the results for the linear detrending violate the assumption that no unit root is giving rise to nonstationarity in the cyclical component.

4. This minimization has two elements, go and go — g-, which are treated as unknown parameters with diffuse priors. The Kalman smoothing technique (see Pagan 1980) was used to compute efficiently the conditional expectations of the g, given the observed y,. The posterior means of go and go — g–1 are theg  oa    g      a   s t  ons of these parameters and the observations.

S  t e e t - e  st un  o d t t   n the cyclical component is regressed on a constant, the level of the cyclical component, and six lags of the


<!-- p:6 -->


TABLE 1 STANDARD DEVIATION AND SERIAL CORRELATIONS OF CYCLICAL GNP FOR DIFFERENT VALUES OF THE SMOOTHING PARAMETER; SAMPLE PERIOD: 1950.1–1979.2

|                     | A = 400          | A = 1600         | A = 6400         | A = infinity     |
|---------------------|------------------|------------------|------------------|------------------|
| Standard Deviations | 1.56%            | 1.80%            | 2.03%            | 3.12%            |
| Autocorrelations    | Autocorrelations | Autocorrelations | Autocorrelations | Autocorrelations |
| Order 1             | .80              | .84              | .87              | .94              |
| Order 2             | .48              | .57              | .65              | .84              |
| Order 3             | .15              | .27              | .41              | .73              |
| Order 4             | - .14            | - .01            | .17              | .61              |
| Order 5             | -.32             | -.20             | .00              | .52              |
| Order 6             | - .39            | - .30            | - .11            | .44              |
| Order 7             | - .42            | - .38            | - .20            | .38              |
| Order 8             | - .44            | -.44             | -.27             | .31              |
| Order 9             | -.41             | -.44             | -.31             | .25              |
| Order 10            | - .36            | -.41             | -.32             | .20              |
| Unit-Root Test      | - 5.02           | - 4.47           | - 3.57           | - 1.15           |

With our procedure for identifying the growth component (λ = 1,600), the annual rate of change of the growth component varied between 2.3 and 4.9 percent over the sample period, with the minima occurring in 1957 and in 1974. The maximum growth rate occurred in 1964, with another peak of 4.4 percent in 1950. The average growth rate over the period was 3.4 percent. The differences between our cyclical components and those obtained with perfect smoothing (λ = ∞) are depicted in Figure 1, along with the cyclical component. The smoothness of the variation in this difference, relative to the variation in the cyclical component, indicates that the smoothing parameter chosen is reasonable. We caution against interpreting the cyclical characteristic of the difference as a cycle of long duration. Such patterns can appear as artifacts of the data analysis procedure.

The same transformation was used for all series: that is, for each series j

$$g _ { j t } = \sum _ { i = 1 } ^ { T } w _ { i t } ^ { T } y _ { j i } ,$$

where T is the length of the sample period. If the sample size were infinite, it would not be necessary to index these coefficients by t and

$$g _ { j t } = \sum _ { i = - \infty } ^ { \infty } w _ { i } ^ { \infty } y _ { j , t + i }$$


<!-- p:7 -->


6

:

where

Wi

∞

= 0.8941 [0.056168 cos(0.11168 i) + 0.055833 sin(0.11168 i)]

IV,,

] (5)

fo     t r  r    &gt;  o -  = r     of are near wi-i, so our method is approximately a two-way moving average with weights subject to a damped harmonic. The advantage of using the exact solution is that observations near the beginning and the end of the sample period are not lost. the  sample,

The above makes it clear that the data are being filtered. As any filter alters the serial correlation properties of the data, the reported serial correlations should be interpreted with caution. The results do indicate that there is considerable persistence in the rapidly varying component of output. When using the statistics reported here to examine the validity of a model of the cyclical fluctuations of an artificial economy, the serial correlation of the rapidly varying component of the model's aggregate output series should be compared to these numbers. That is, the s   s s     s ss s s s

6. See Miller (1946) for a derivation. There are certain implicit restrictions on the y, sequence when the sample is infinite. Ótherwise, the gj may not exist. We require that the {y,} sequenċe bēlongs to the space for which

FIG. 1.


<!-- p:8 -->


7

economy. Only then, would the model's statistics and those reported here be comparable.

As the comovement results were not particularly sensitive to the value of the smoothing parameter λ selected, in the subsequent analysis only the statistics for λ = 1,600 are reported. With a larger λ, the amplitudes of fluctuations are larger, but the relative magnitudes of fluctuations of the series change little. We do think it is important that all series be filtered using the same parameter λ.

### 2. VARIABILITY AND COVARIABILITY OF THE SERIES

The components being studied are the cyclical components and subsequently all references to a series relate to its cyclical component. The sample standard deviations of a series is our measure of a series's variability, and the correlation of a series with real GNP is our measure of a series's covariability. These measures are computed for the first half and the second half of the sample, as well as for the entire sample. This is a check for the stability of the measures over time.

A variable might be strongly associated with real output, but lead or lag real output. Therefore, as a second measure of the strength of association with real output, the R-squared for the regression

for each series j was computed.

The ratio of the explained sum of the squares for this regression to the explained sum of squares for the regression when the coefficients are not constrained to be equal in the first and the second halves of the sample is our measure of stability. It is a number between zero and one, with one indicating that the best-fit equation is precisely the same in the first and second halves of the sample.

We chose this measure rather than applying some F-test for two reasons. First, we do not think the assumption of uncorrelated residuals is maintainable. Second, even if it were, it is very difficult to deduce the magnitude of the instability from the reported test statistic.

##### Aggregate Demand Components

The first set of variables studied are the real aggregate demand components. The results are summarized in Tables 2 and 3. The series that vary the least are consumption of services, consumption of nondurables and state and local government purchases of goods and services. Each of these has standard deviation less than the 1.8 percent value for real output. The investment components, including consumer durable expenditures, are about three times as variable as output. Covariabilities of consumption and investment with output are much stronger than the covariability of government expenditures with output.


<!-- p:9 -->


TABLE 2

AGGREGATE DEMAND COMPONENTS: STANDARD DEVIATIONS AND CORRELATIONS WITH GNP SAMPLE PERIOD: 1950.1-1979.2

|                     |   Standard Deviations in Percents - Whole |   Standard Deviations in Percents - First Half |   Standard Deviations in Percents - Second Half |   Correlations with Real Output - Whole |   Correlations with Real Output - First Half |   Correlations with Real Output - Second Half |   Average - GNP |
|---------------------|-------------------------------------------|------------------------------------------------|-------------------------------------------------|-----------------------------------------|----------------------------------------------|-----------------------------------------------|-----------------|
| Real GNP            |                                       1.8 |                                            1.7 |                                             1.9 |                                         |                                              |                                               |                 |
| Total Consumption   |                                       1.3 |                                            1.2 |                                             1.4 |                                    .739 |                                         .503 |                                          .917 |            61.7 |
| Services            |                                        .7 |                                             .7 |                                              .6 |                                    .615 |                                         .441 |                                          .781 |            26.8 |
| Nondurables         |                                       1.2 |                                            1.0 |                                             1.3 |                                    .714 |                                         .575 |                                          .808 |            26.5 |
| Durables            |                                       5.6 |                                            6.1 |                                             5.0 |                                    .574 |                                         .298 |                                          .884 |             8.4 |
| Total Invest. Fixed |                                       5.1 |                                            4.2 |                                             5.9 |                                    .714 |                                         .454 |                                          .884 |            14.2 |
| Residential         |                                      10.7 |                                            8.5 |                                            12.4 |                                    .436 |                                         .123 |                                          .637 |             4.4 |
| Nonresidential      |                                       4.9 |                                            4.4 |                                             5.3 |                                    .684 |                                         .554 |                                          .777 |             9.7 |
| Equipment           |                                       5.8 |                                            5.6 |                                             5.9 |                                    .707 |                                         .642 |                                          .760 |             6.0 |
| Structures          |                                       4.5 |                                            3.8 |                                             5.1 |                                    .512 |                                         .225 |                                          .698 |             3.7 |
| Total Government    |                                       4.8 |                                            6.5 |                                             2.2 |                                    .258 |                                         .353 |                                          .152 |            22.6 |
| Federal             |                                       8.7 |                                           11.6 |                                             4.2 |                                    .266 |                                         .377 |                                          .125 |            10.8 |
| State and Local     |                                       1.3 |                                            1.6 |                                             1.0 |                                   -.170 |                                        -.408 |                                          .131 |            11.8 |

##### Factors of Production

The second set of variables considered are the factors of production and productivity which is output per hour. These results are summarized in Tables 4 and 5. There is a strong and stable positive relationship between hours and output. In addition, the variability in hours is comparable to the variability in output. The contemporaneous association between productivity and output is weak and unstable with the standard deviation of productivity being much smaller than the standard deviation of output. It is interesting to note that when lead and lag GNPs are included, the

#### TABLE 3

AGGREGATE DEMAND COMPONENTS: STRENGTH OF ASSOCIATION WITH GNP AND MEASURE OF STABILITY

SAMPLE PERIOD: 1950.1-1979.2

|                     |   R2 for Regression - Correlation with Real Output Squared |   R2 for Regression - 2 cJ, = aJ + E fij,GNP,+ |   R2 for Regression - Stability Measure |
|---------------------|------------------------------------------------------------|------------------------------------------------|-----------------------------------------|
| Total Consumption   |                                                       .546 |                                           .620 |                                    .922 |
| Services            |                                                       .378 |                                           .424 |                                    .877 |
| Nondurables         |                                                       .510 |                                           .589 |                                    .968 |
| Durables            |                                                       .329 |                                           .415 |                                    .829 |
| Total Invest. Fixed |                                                       .509 |                                           .552 |                                    .785 |
| Residential         |                                                       .190 |                                           .441 |                                    .809 |
| Nonresidential      |                                                       .468 |                                           .602 |                                    .831 |
| Equipment           |                                                       .500 |                                           .631 |                                    .908 |
| Structures          |                                                       .262 |                                           .367 |                                    .834 |
| Total Government    |                                                       .067 |                                           .119 |                                    .509 |
| Federal             |                                                       .071 |                                           .129 |                                    .482 |
| State and Local     |                                                       .029 |                                           .095 |                                    .298 |


<!-- p:10 -->


TABLE 4 FACTORS OF PRODUCTION: STANDARD DEVIATIONS AND CORRELATIONS WITH GNP

SAMPLE PERIOD: 1950.1-1979.2

|                           |   Standard Deviations in Percents - Whole |   Standard Deviations in Percents - First Half | Standard Deviations in Percents - Second Half   |   Correlations with Real Output - Whole |   Correlations with Real Output - First Half |   Correlations with Real Output - Second Half |
|---------------------------|-------------------------------------------|------------------------------------------------|-------------------------------------------------|-----------------------------------------|----------------------------------------------|-----------------------------------------------|
| Real GNP                  |                                       1.8 |                                            1.7 | 1.9                                             |                                         |                                              |                                               |
| Capital Stocks            |                                           |                                                |                                                 |                                         |                                              |                                               |
| Inventory                 |                                       1.7 |                                            2.0 | 1.4                                             |                                    .507 |                                         .686 |                                          .309 |
| Capital Stock Durables    |                                       1.2 |                                            1.4 | 1.0                                             |                                   -.210 |                                        -.178 |                                         -.274 |
| Capital Stock Nondurables |                                        .7 |                                             .7 | .7                                              |                                   -.236 |                                        -.185 |                                         -.297 |
| Hours                     |                                       2.0 |                                            2.1 | 1.8                                             |                                    .853 |                                         .896 |                                          .824 |
| Work Week                 |                                        .5 |                                             .6 | .5                                              |                                    .820 |                                         .854 |                                          .800 |
| Employees                 |                                       1.4 |                                            1.6 | 1.2                                             |                                    .773 |                                         .831 |                                          .732 |
| Productivity              |                                       1.0 |                                            1.0 | 1.l                                             |                                    .100 |                                        -.231 |                                          .361 |

association between GNP and productivity increases dramatically with the R-squared increasing from .010 to .453.

Capital stocks, both in durable goods and nondurable goods industries, are less variable than real output and negatively associated with output. Inventory stocks, on the other hand, have a variability comparable to output, and their correlations with output are positive. Further, the strength of association of inventories with GNP increases when lag and lead GNPs are included in the regression. This is indicated by the increase in the R-squared from .257 to .622.

##### Monetary Variables

Results for the final set of variables are presented in Tables 6 and 7. Correlations between nominal money, velocity, and real money with GNP are all positive. The differences in the correlations in the first and second halves of the sample, with the exception of nominal M1, suggest considerable instability over time in these relationships. A similar conclusion holds for the short-term interest rate. The correlations of GNP with the price variables are positive in the first half of the sample and

TABLE 5 FACTORS OF PRODUCTION: STRENGTH OF ASSOCIATION WITH GNP AND MEASURE OF STABILITY SAMPLE PERIOD: 1950.1-1979.2

|                           |   R2 for Regression - Correlation with Real Output Squared |   R2 for Regression - 2 cjt = aj + 2 fij,GNP,+I t=-2 |   R2 for Regression - Stability Measure |
|---------------------------|------------------------------------------------------------|------------------------------------------------------|-----------------------------------------|
| Capital Stocks            |                                                            |                                                      |                                         |
| Inventory                 |                                                       .257 |                                                 .622 |                                    .828 |
| Capital Stock Durables    |                                                       .044 |                                                 .235 |                                    .782 |
| Capital Stock Nondurables |                                                       .056 |                                                 .129 |                                    .740 |
| Hours                     |                                                       .728 |                                                 .838 |                                    .954 |
| Work Week                 |                                                       .672 |                                                 .700 |                                    .513 |
| Employees                 |                                                       .600 |                                                 .801 |                                    .935 |
| Average Product of Labor  |                                                       .010 |                                                 .453 |                                    .773 |

9


<!-- p:11 -->


TABLE 6 MONETARY AND PRICE VARIABLES: STANDARD DEVIATIONS AND CORRELATIONS WITH GNP SAMPLE PERIOD: 1950.1-1979.2

|                | su ndard Deviations in Percents - Whole   |   su ndard Deviations in Percents - First Half | su ndard Deviations in Percents - Second Half   | Correlations with Real Output - Whole   |   Correlations with Real Output - First Half |   Correlations with Real Output - Second Half |
|----------------|-------------------------------------------|------------------------------------------------|-------------------------------------------------|-----------------------------------------|----------------------------------------------|-----------------------------------------------|
| Real GNP       | 1.8                                       |                                            1.7 | 1.9                                             |                                         |                                              |                                               |
| M1             |                                           |                                                |                                                 |                                         |                                              |                                               |
| Nominal Value  | .9                                        |                                             .8 | 1,0                                             | .661                                    |                                         .675 |                                          .649 |
| Velocity       | 1.6                                       |                                            2.0 | 1.0                                             | .614                                    |                                         .801 |                                          .415 |
| Real Value     | 1.5                                       |                                            1.2 | 1.7                                             | .565                                    |                                         .079 |                                          .865 |
| M2             |                                           |                                                |                                                 |                                         |                                              |                                               |
| Nominal        | 1. 1                                      |                                             .9 | 1.3                                             | .480                                    |                                         .175 |                                          .665 |
| Velocity       | 1.9                                       |                                            2.4 | 1.2                                             | .529                                    |                                         .818 |                                          .131 |
| Real Value     | 1.8                                       |                                            1.4 | 2.1                                             | .432                                    |                                          221 |                                          .828 |
| Interest Rates |                                           |                                                |                                                 |                                         |                                              |                                               |
| Short          | .24                                       |                                             27 | 19                                              | 510                                     |                                         .738 |                                          .255 |
| Long           | .06                                       |                                                |                                                 |                                         |                                         .640 |                                           175 |
| Price Indexes  |                                           |                                                |                                                 |                                         |                                              |                                               |
| GNP Deflator   | 1.0                                       |                                            1.0 | 1.1                                             | - .239                                  |                                         .490 |                                           814 |
| CPI            | 1.3                                       |                                            1.3 | 1.3                                             | -.316                                   |                                         .223 |                                           799 |

negative in the second half with the correlation for the entire period being small and negative.

### 3. SERIAL CORRELATION PROPERTIES OF DATA SERIES

A sixth-order autoregressive process was fit to a number of the series which displayed reasonable stable comovements with real output. Figure 2 presents plots of the unit impulse response functions for GNP and nine other series for the estimated

TABLE 7 MONEY AND PRICE VARIABLES: STRENGTH OF ASSOCIATION WITH GNP AND MEASURE OF STABILITY SAMPLE PERIOD: 1950.1-1979.2

|                       | 22 for Regession - CoITelation with Real Output Squared   |   22 for Regession - 2 CJf = atJ + E ISJIGNPr+I t= -2 |   22 for Regession - Stability Measure |
|-----------------------|-----------------------------------------------------------|-------------------------------------------------------|----------------------------------------|
| M1                    |                                                           |                                                       |                                        |
| Nominal Value         | .437                                                      |                                                  .445 |                                   .378 |
| . ve OClty            | .378                                                      |                                                  .408 |                                   .281 |
| Real Value            | .319                                                      |                                                  .495 |                                   .678 |
| M2 .                  |                                                           |                                                       |                                        |
| . . . . > omlna va ue | .230                                                      |                                                  .371 |                                   .749 |
| Velocity              | .280                                                      |                                                  .376 |                                   .650 |
| Real Value            | .187                                                      |                                                  .428 |                                   .684 |
| Interest Rates        |                                                           |                                                       |                                        |
| Short                 | .260                                                      |                                                  .506 |                                   .748 |
| Long                  | .037                                                      |                                                  .381 |                                   .724 |
| Price Index           |                                                           |                                                       |                                        |
| GNP Deflator          | *057                                                      |                                                  .261 |                                   .567 |
| CPI                   | .010                                                      |                                                  .330 |                                   .481 |


<!-- p:12 -->


uz

;

-

<!-- p:13 -->


autoregressive function.7 The function for GNP increases initially to a peak of 1.15 in period one and has a minimum of —.39 in period eight. The patterns for consumption and investment are similar except that the peak for consumption is in the initial period. The function for consumption and each of its three components (not pictured) are similar to the one for the aggregate.

The pattern for total hours and the number of employees, except for the greater amplitude, is very similar to the pattern for GNP. The average work-week pattern, however, begins to decline immediately and the period of damped oscillation is shorter. The monetary variables have very different response patterns, indicating serial correlation properties very different than those of real output.

There is a dramatic difference in the response pattern for the capital stock in durable goods industries. The maximum amplitude of the response is much greater, being about 3.6, and occurs slightly over a year subsequent to the unit impulse. The pattern for the capital stock in the nondurable goods industries (not pictured) is similar though the maximum amplitude is smaller, being 2.8. For both capital stocks the peaks in the unit response function are in period five.

## APPENDIX

All the data from the original paper were obtained from the Wharton Economic Forecasting Association Quarterly Data Bank. The short-term interest rate was the taxable three-month U.S. Treasury bill rate, and the long-term interest rate, the yield on U.S. Government long-term bonds.

Tables A.1-A.7 contain data from 1947.1 to 1993.4. All data for Tables A.1– A.3 come from the National Income and Product Accounts: Historical NIPA Quarterly Data, Survey of Current Business, U.S. Department of Commerce. The capital stock data in Tables A.5 and A.6 come from the Survey of Current Business as annual series. We used quarterly investment series from the NIPA with the annual capital stocks to construct quarterly series. All labor data in Tables A.5 and A.6 come from Citibase. Data for the price series in Tables A.6 and A.7 also come from Citibase. The interest rate series are from the Federal Reserve Bulletin and are constructed from the monthly series in Tables 1.33 and 1.35. Real M1 and Real M2 were obtained from the Business Cycle Indicators Historical Diskette, published by the U.S. Department of Commerce. Nominal series were calculated by multiplying by the GNP deflator.

7. Letting a, be the innovations and

-e ses  e e  e s e ne oes e  ue n une tion in period i. One must take care in interpreting the response pattern. Two moving average processes can be observationally equivalent (same autocovariances function) yet have very different response patterns. We chose the invertible representation because it is unique. It is just one way to represent the serial correlation properties of a covariance stationary stochastic process. Öthers are the spectrum, the autoregressive representation, and the autocovariance function.


<!-- p:14 -->


TABLE A1 STANDARD DEVIATION AND SERIAL CORRELATIONS OF CYCLICAL GNP FOR DIFFERENT VALUES OF THE SMOOTHING PARAMETER. SAMPLE PERIOD: 1947.1-1993.4

|                     | A = 400   | A = 1600   | A = 6400   | A = - infinity   |
|---------------------|-----------|------------|------------|------------------|
| Standard Deviations | 1.47%     | 1.80%      | 2.14%      | 4 4.94%          |
| Autocorrelations    |           |            |            |                  |
| Order 1             | .81       | .86        | .9o        |                  |
| Order 2             | .53       | .64        | .73        | .96              |
| Order 3             | .22       | .39        | .53        | .91              |
| Order 4             | -.03      | .16        | .34        | .86              |
| Order S             | -.21      | -.05       | .18        | .80              |
| Order 6             | -.32      | -.27       | .02        | .74              |
| Order 7             | -.39      | -.30       | 09         | .69              |
| Order 8             | -.43      | -.37       | .19        | .63              |
| Order 9             | -.40      | -.40       | 26         | .58              |
| Order 10            | -.35      | -.40       | 28         | .52              |
| Unit-Root Test      | -6.52     | -5.91      | 98         | .47 -2.34        |

TABLE A2 AGGREGATE DEMAND COMPONENTS: STANDARD DEVIATIONS AND CORRELATIONS WITH GNP SAMPLE PERIOD: 1947.1-1993.4

|                     |   Standard - Whole |   Standard - Deviations First Half |   Standard - Percents Second Half | Correlations with Real Output - Whole   | Correlations with Real Output - First Half   | Correlations with Real Output - Second Half   |   Average GNP |
|---------------------|--------------------|------------------------------------|-----------------------------------|-----------------------------------------|----------------------------------------------|-----------------------------------------------|---------------|
| RealGNP             |                1.8 |                                1.8 |                               1.8 |                                         |                                              |                                               |               |
| Total Consumption   |                1.2 |                                0.9 |                               1.4 | .719                                    | .511                                         | .875                                          |          61.7 |
| Services            |                0.7 |                                0.7 |                               0.8 | .685                                    | .544                                         | .810                                          |          31.2 |
| Nondurable          |                1.2 |                                1.0 |                               1.3 | .707                                    | .558                                         | .827                                          |          24.5 |
| Durables            |                5.5 |                                5.4 |                               5.6 | .457                                    | .112                                         | .787                                          |           6.9 |
| Total Invest. Fixed |                5.5 |                                4.5 |                               6.4 | .732                                    | .470                                         | .927                                          |          15.2 |
| Residential         |               10.9 |                                9.1 |                              12.6 | .462                                    | .755                                         | .745                                          |           5.1 |
| Nonresidential      |                5.1 |                                4.6 |                               5.6 | .746                                    | .659                                         | .820                                          |          10.1 |
| Equipment           |                6.1 |                                5.8 |                               6.4 | .798                                    | .715                                         | .871                                          |           6.1 |
| Structures          |                4.8 |                                3.8 |                               5.6 | .469                                    | .397                                         | .528                                          |           4.0 |
| Total Government    |                3.9 |                                5.4 |                               1.2 | .350                                    | .515                                         | -.012                                         |          21.6 |
| Federal             |                6.9 |                                9.5 |                               1.9 | .348                                    | .540                                         | - .164                                        |          10.7 |
| State and Local     |                1.5 |                                1.9 |                               1.1 | - .216                                  | - .453                                       | .015                                          |          10.8 |

#### TABLE A3

AGGREGATE DEMAND COMPONENTS: STRENGTH OF ASSOCIATION WITH GNP AND MEASURE

OF STABILITY

SAMPLE PERIOD: 1947.1-1993.4

|                     |   R2 for Regression - Correlation with Real Output Squared |   R2 for Regression - 2 Cj, = 0tj + 22 jiGNP,+ |   R2 for Regression - Stability Measure |
|---------------------|------------------------------------------------------------|------------------------------------------------|-----------------------------------------|
| Total Consumption   |                                                       .517 |                                           .571 |                                    .808 |
| Services            |                                                       .469 |                                           .512 |                                    .873 |
| Nondurables         |                                                       .500 |                                           .520 |                                    .872 |
| Durables            |                                                       .209 |                                           .324 |                                    .669 |
| Total Invest. Fixed |                                                       .536 |                                           .580 |                                    .796 |
| Residential         |                                                       .213 |                                           .482 |                                    .731 |
| Nonresidential      |                                                       .557 |                                           .662 |                                    .929 |
| Equipment           |                                                       .637 |                                           .702 |                                    .955 |
| Structures          |                                                       .220 |                                           .396 |                                    .792 |
| Total Government    |                                                       .123 |                                           .229 |                                    .500 |
| Federal             |                                                       .121 |                                           .224 |                                    .436 |
| State and Local     |                                                       .047 |                                           .080 |                                    .200 |


<!-- p:15 -->


TABLE A4

FACTORS OF PRODUCTION: STANDARD DEVIATIONS AND CORRELATIONS WITH GNP

SAMPLE PERIOD: 1947.1-1993.4

|                           |   Standard Deviations in Percents - Whole |   Standard Deviations in Percents - First Half |   Standard Deviations in Percents - Second Half | Correlations with Real Output - Whole   | Correlations with Real Output - First Half   |   Correlations with Real Output - Second Half |
|---------------------------|-------------------------------------------|------------------------------------------------|-------------------------------------------------|-----------------------------------------|----------------------------------------------|-----------------------------------------------|
| Real GNP                  |                                       1.8 |                                            1.8 |                                             1.8 |                                         |                                              |                                               |
| Capital Stocks            |                                           |                                                |                                                 |                                         |                                              |                                               |
| Inventory                 |                                       2.1 |                                            2.4 |                                             1.8 | .510                                    | .547                                         |                                          .475 |
| Capital Stock Durables    |                                       1.2 |                                            1.1 |                                             1.2 | .510                                    | .387                                         |                                          .619 |
| Capital Stock Nondurables |                                       1.0 |                                            1.0 |                                             0.9 | - .055                                  | - .125                                       |                                          .021 |
| Hours                     |                                       1.8 |                                            1.9 |                                             1.7 | .883                                    | .860                                         |                                          .911 |
| Work Week                 |                                       1.1 |                                            1.1 |                                             1.0 | .778                                    | .778                                         |                                          .783 |
| Employees                 |                                       1.5 |                                            1.6 |                                             1.5 | .828                                    | .808                                         |                                          .850 |
| Productivity              |                                       0.9 |                                            1.0 |                                             0.8 | .239                                    | .151                                         |                                          .360 |

TABLE A5

FACTORS OF PRODUCTION: STRENGTH OF ASSOCIATION WITH GNP AND MEASURE OF STABILITY SAMPLE PERIOD: 1947.1-1993.4

|                           |   R2 for Regression - Squared CoITelation with Real Output |   R2 for Regression - ' J t=-2 ' c,, - sx, + S ,,GNP,+I |   R2 for Regression - Stability |
|---------------------------|------------------------------------------------------------|---------------------------------------------------------|---------------------------------|
| Capital Stocks            |                                                            |                                                         |                                 |
| Inventory                 |                                                       .260 |                                                    .373 |                            .801 |
| Capital Stock Durables    |                                                       .260 |                                                    .728 |                            .967 |
| Capital Stock Nondurables |                                                       .003 |                                                    .356 |                            .874 |
| Hours                     |                                                       .779 |                                                    .869 |                            .992 |
| Work Week                 |                                                       .605 |                                                    .764 |                            .994 |
| Employees                 |                                                       .685 |                                                    .858 |                            .989 |
| Average Product of Labor  |                                                       .057 |                                                    .465 |                            .933 |

TABLE A6

MONETARY AND PRICE VARIABLES: STANDARD DEVIATIONS AND CORRELATIONS WITH GNP SAMPLE PERIOD: 1947.1-1993.4

|                |   Standard Deviations in Percents - Whole |   Standard Deviations in Percents - First Hif |   Standard Deviations in Percents - Second Hif | colTelations with Real OuWut - wole   |   colTelations with Real OuWut - First Hif | colTelations with Real OuWut - Second Hif   |
|----------------|-------------------------------------------|-----------------------------------------------|------------------------------------------------|---------------------------------------|--------------------------------------------|---------------------------------------------|
| Real GNP       |                                       1.8 |                                           1.8 |                                            1.8 | -                                     |                                            | -                                           |
| M1             |                                           |                                               |                                                |                                       |                                            |                                             |
| Nominal Value  |                                       2.1 |                                           1.3 |                                            2.7 | .368                                  |                                       .542 | .318                                        |
| Velocity       |                                       2.7 |                                           2.1 |                                            3.1 | .328                                  |                                       .680 | .104                                        |
| Real Value     |                                       2.7 |                                           1.6 |                                            3.4 | .347                                  |                                       .219 | .436                                        |
| M2             |                                           |                                               |                                                |                                       |                                            |                                             |
| Nominal        |                                       1.8 |                                           1.4 |                                            2.2 | .337                                  |                                       .324 | .357                                        |
| Velocity       |                                       2.5 |                                           2.5 |                                            2.6 | .404                                  |                                       .672 | .151                                        |
| Real Value     |                                       2.4 |                                           1.8 |                                            2.9 | .319                                  |                                       .058 | .49l                                        |
| Interest Rates |                                           |                                               |                                                |                                       |                                            |                                             |
| Short          |                                       1.1 |                                           0.6 |                                            1.5 | .324                                  |                                       .335 | .358                                        |
| Long           |                                       0.6 |                                           0.2 |                                            0.8 | .032                                  |                                       .228 | -.020                                       |
| Price Indexes  |                                           |                                               |                                                |                                       |                                            |                                             |
| GNP Deflator   |                                       1.0 |                                           1.0 |                                            1.0 | -.156                                 |                                       .327 | -.635                                       |
| CPI            |                                       1.6 |                                           1.4 |                                            1.7 | -.222                                 |                                       .247 | -.585                                       |

###### TABLE A7

MONEY AND PRICE VARIABLES: STRENGTH OF ASSOCIATION WITH GNP AND MEASURE

OF STABILITY

SAMPLE PERIOD: 1947.1-1993.4


<!-- p:16 -->


|                |   R2 for Regression - CoIIelation with Real Output Squared |   R2 for Regression - 2 cJ, = (xJ + E J,GNP,+l i=-2 |   R2 for Regression - Stability Measure |
|----------------|------------------------------------------------------------|-----------------------------------------------------|-----------------------------------------|
| M1             |                                                            |                                                     |                                         |
| Nominal Value  |                                                       .135 |                                                .229 |                                    .783 |
| Velocity       |                                                       .108 |                                                .280 |                                    .747 |
| Real Value     |                                                       .120 |                                                .270 |                                    .738 |
| M2             |                                                            |                                                     |                                         |
| Nominal Value  |                                                       .114 |                                                .291 |                                    .782 |
| Velocity       |                                                       .163 |                                                .377 |                                    .755 |
| Real Value     |                                                       .102 |                                                .321 |                                    .707 |
| Interest Rates |                                                            |                                                     |                                         |
| Short          |                                                       .105 |                                                .336 |                                    .701 |
| Long           |                                                       .001 |                                                .191 |                                    .701 |
| Price Index    |                                                            |                                                     |                                         |
| GNP Deflator   |                                                       .024 |                                                .199 |                                    .430 |
| CPI            |                                                       .049 |                                                .248 |                                    .485 |

<!-- END SOURCE 23/40: Hodrick_1997_postwar-us-business-cycles.md -->

---

<!-- BEGIN SOURCE 24/40: Islas-Camargo_2019_forecasting-remittances-mexico-rjef.md -->

# Source: `Islas-Camargo_2019_forecasting-remittances-mexico-rjef.md`

---
id: "Islas-Camargo_2019_forecasting-remittances-mexico-rjef"
source_pdf: "../pdf/Islas-Camargo_2019_forecasting-remittances-mexico-rjef.pdf"
source_filename: "Islas-Camargo_2019_forecasting-remittances-mexico-rjef.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/Islas-Camargo_2019_forecasting-remittances-mexico-rjef.references.md"
---

<!-- p:1 -->

## FORECASTING REMITTANCES TO MEXICO WITH A MULTI-STATE MARKOVSWITCHING MODEL APPLIED TO THE TREND WITH CONTROLLED 3.

## SMOOTHNESS

#### A. ISLAS 1 Víctor M. GUERRERO 2 Eliud SILVA 3

### Abstract

Remittances  inflows  have  been  associated  with  a  reduction  in  the  level  and  severity  of poverty.  They contribute to higher human capital accumulation, to improved access to formal financial sector services, to enhanced small business investment and to more entrepreneurship. Remittances play also an important role in contributing to the livelihoods of less prosperous people. Considering these facts, this paper proposes a statistical model to  forecast  remittances  flows  to  Mexico  in  order  to  provide  information  for  the  design  of policies that can help attract remittances inflows and use them productively. Here, we apply a  statistical  methodology  based  on  the  Multi-State  Markov-Switching  model  with  three different specifications. The model is applied to the trend of the time series data instead of the original observations with the aim of mitigating the effect of outliers and transitory blips. The filtering technique employed to estimate the trend allows us to control the amount of smoothness in the resulting trend. This method is also useful to take into account an implicit adjustment of the data at both extremes of the time series, thus providing better results than conventional  filtering  techniques  such  as  the  Hodrick-Prescott  filter.  Thus,  the  MarkovSwitching  approach  captures  more  precisely  the  trend  persistence  of  remittances  and enhances both in-sample and out-of-sample forecast performance.

Keywords : remittances,  migration,  forecast,  Markov-switching,  penalized  least  squares, controlled smoothing

JEL Classification : C32 , C53 , F24, F47, J21, O15

1  Corresponding author. Department of Statistics, ITAM Río Hondo No. 1, Col. Progreso Tizapán, 01080 México, D.F. E-mail: aislas@itam.mx.

2  Department of Statistics, ITAM Río Hondo 1, Col. Progreso Tizapán, México 01080 México D.F. E-mail: guerrero@itam.mx.

3  Universidad Anáhuac Mexico  Av. Universidad Anáhuac, Col. Lomas Anáhuac, Edo. de México 52786.


<!-- p:2 -->


## 1. Introduction

Remittances  are  an  important  source  of  external  financing,  particularly  in  developing countries. They have been growing in both absolute volume and relative to other sources of external financing, becoming nowadays a major stable source of income for many countries, surpassing even income from exports, foreign direct investment and official development aid. In fact, they are also larger than or equal to foreign exchange reserves in many small countries  and  reach  more  than  a  quarter  of  Gross  Domestic  Product  (GDP)  in  several countries, see Ratha et al . (2010). They contribute to stabilizing the current account position and reduce output volatility of recipient countries, as pointed out by Ratha (2005, 2007), World Bank (2005), Bugamelli and Paterno (2009), Chami et al. (2009) and Gupta et al. (2009).  They  have  also  been  associated  with  reduction  in  poverty,  increased  household resources  devoted  to  investment,  improved  health  and  education  outcomes,  and  higher levels  of  entrepreneurship  (Adams  and  Page,  2005;  Hildebrandt  and  McKenzie,  2005; Fajnzylber and Lopez, 2007; Valero-Gil, 2009; Amuedo-Dorantes et al ., 2011). On the other hand, some studies have pointed out how remittances have affected the receiving economy by cultivating a culture of dependency that reduces labor supply and promotes conspicuous consumption.  At  a  macroeconomic  level,  remittances  have  been  found  to  hurt  prices  of domestically produced goods and exchange rates and the export sector through the socalled Dutch disease (Khurshid et al. , 2016, and 2018). Regarding the determinants of remittances flows, macroeconomic studies have emphasized the level of economic activity in the host and the home countries, the wage rate, inflation, interest  rate  differential,  or  the  efficiency  of  the  banking  system  (El-Sakka  and  McNabb, 1999; Russell, 1986). Real earnings of workers and the total number of migrants in the host country  were  consistently  found  to  have  a  significant  and  positive  effect  on  the  flow  of remittances (Chami et  al., 2005; Elbadawi and Rocha, 1992; Straubhaar, 1986; Swamy, 1981). In addition, factors such as remittances costs and migrants' vintage also play a role in influencing remittances flows. In a survey of Tongan migrants in New Zealand, Gibson et al. (2006) found that remittances would rise by 0.22% if costs fell by 1%. In a sample of five Mediterranean countries, Faini (1994) found evidence that the real exchange rate is also a significant  determinant  of  remittances.  Demographic  factors  like  the  share  of  female employment or high age-dependency ratio in the host country reduce remittances, while illiteracy rates affect them positively (Buch and Kuckulenz, 2004). Wahba (1991) suggests that political  stability  and  consistency in government policies and financial intermediation significantly affect the flow of remittances. Mexico's Central Bank (BANXICO)  estimates indicate that since the mid-nineties remittances flows to Mexico have grown continuously and steadily until 2007, reaching U.S. $6.5 billion in 2000. In the initial years of the current millennium, remittances grew strongly, reaching $15.1 billion by 2003, and peaking at $26 billion in 2007. However, from that year and until 2013, the flows of remittances to Mexico fell and stabilized at around $21 to $23 billion  per  year.    Remittances flows have trended upwards again since 2014, reaching a record amount of money in 2016, taking advantage of the strong U.S. labor market and a weakening Mexican peso amid worries about actions that the administration of the U.S. President Trump may take against immigrant or remittances. Figure 1 shows the quarterly remittances flows to Mexico over the period 1995:I - 2016:IV, where we appreciate three phases of the growth rate: medium during 1995:I - 1999:IV and

2014:I - 206:IV, high during 2000:I - 2007:IV and low or negative during 2008:I -   2013:IV.


<!-- p:3 -->


Figure 1 Quarterly Remittances Received by Mexico, 1995:I - 2016:IV

##### (Millions of U.S. Dollars)

Source: BANXICO: http://www.banxico.org.mx.

Tracking the dynamics of remittances flows to Mexico is a very important issue, since they represent  a  major  source  of  capital  resources  nationally,  regionally  and  locally.  In  this context, policymakers should consider the short and medium term trends of that variable to better  react  to  falls  in  remittances  flows,  which  could  adversely  impact  the  economy  of thousands  of  Mexican  households  that  heavily  depend  on  that  kind  of  income.  While remittances  are  influenced  by  the  aforementioned  factors,  using  them  in  a  forecasting exercise is constrained by the lack of reliable forecasts of their future evolution. Moreover, remittances  flows  could  be  affected  by  unpredictable  drastic  changes  in  both  U.S.  and Mexican government policies that add uncertainty to the forecast.

To the best of our knowledge, the literature registers just one attempt to forecast remittances by  means  of  a  structural  model,  namely  the  work  of  Mohapatrand  and  Ratha  (2010). Nevertheless, these authors recognize that much remains to be done on the quality of the data to improve their forecast methodology. When we only have access to a time series of remittances,  we  face  basically  two  different  situations:  (i)  working  with  the  original  data, where such components as seasonality and cycle may appear, and apply a time series model, say a Seasonal Auto-Regressive Integrated Moving Average (SARIMA) model to produce short-term forecasts, and (ii) filtering the data to estimate the underlying trend and then forecast the trend to obtain medium-term forecasts. Of course, both sets of forecasts are valuable and interesting for their corresponding forecasting horizons, but they can be achieved with different analytical tools and here we concentrate on the second one.

Thus,  we  propose  to  use  a  Multi-State  Markov-Switching  model  to  the  trend  in  order  to account for episodes of high, medium and slow growth in remittances. By doing that we expect to improve the model's forecasting ability. This idea is in line with that of Yuan's (2011),  who  suggested  using  time  series  filtering  techniques  to  smooth  out  outliers  and transitory  blips  from  the  original  data,  so  as  to  guarantee  that  the  Markov-Switching framework captures more precisely the trend persistence in remittances. We move one step forward since we apply a filter that produces a trend with controlled smoothness and that also takes into account an implicit adjustment to the observations at both extremes of the time series, as in Guerrero (2007).


<!-- p:4 -->


Using  quarterly  remittances  flows  to  Mexico  over  the  period  1995:I-2016:IV,  our  results reveal  that  the  proposed  forecasting  model  can  adequately  capture  the  movements  of remittances inflows. Therefore, it achieves considerable forecast ability improvement relative to the random walk, in terms of mean square forecast error. Specifically, the out of sample forecast precision gain, averaging over horizon of up to four quarters, is 37%.

The remainder of this paper is organized as follows. Next section presents the statistical methodology to be used, i.e . the Markov-Switching model and the controlled smoothness filtering technique that takes into account an adjustment at both ends of the time series. The empirical  application  to  remittances  is  presented  in  the  third  section,  where  detailed summaries of the estimation results are shown, together with a forecast evaluation of the models employed. The last section concludes with some final remarks.

## 2. Statistical Methodology

### 2.1 The Markov-Switching Model

Markov-Switching  has  become  one  of  the  most  popular  nonlinear  time  series  modeling approach. Roughly speaking, it involves multiple structures that characterize the time series behavior during different regimes. By allowing the model to switch between these structures, this representation is able to capture relatively complex dynamic patterns. A feature of this kind of model is that the switching mechanism is controlled by an unobservable state variable that  follows  a  first-order  Markov  chain  structure.  The  Markovian  property  regulates  the process in such a way that the current value of the state variable depends on its immediate past value. As such, a given structure may prevail for a random period of time, and it is replaced by another structure when switching takes place.

In its broadest form, a Markov-Switching model for a time series { yt } can be written as follows

$$y _ { t } = \mu ( s _ { t } ) + \sigma ( s _ { t } ) \varepsilon _ { t } \text { with } \varepsilon _ { t } \text { i} d \sim N ( 0 , 1 ) ,$$

where:  { ε t }  is  a  sequence  of  random  errors, iid stands  for  independent  and  identically distributed and ሼs ௧ ሽ is an unobservable discrete-time Markov chain with a finite number of states, k . Given ሼs ௧ ሽ , the process ሼy ௧ ሽ follows an autoregressive structure whose parameters, μ and σ , depend on the state of the Markov chain for t =1,..., N . This model was introduced by Hamilton (1989) as an appropriate specification to capture changes in the time series behavior due to extraordinary events such as wars, financial panics, natural disasters and drastic changes in government policies. Hamilton's model has been subjected to a number of  refinements  in  order  to  accommodate  regime  shifts  in  intercepts,  in  autoregressive parameters and/or in variance.

Given the variety of Markov-Switching models that one can choose from, the dilemma is to determine  which  one  is  adequate  for  the  data  at  hand.  It  is  not  necessary  that  all  the parameters  in  the  model  be  regime-dependent.  A  plausible  specification  for  empirical applications  allows  the  autoregressive  parameters  and  the  mean  or  the  intercepts  to  be regime-dependent, while the error term can be either hetero or homoskedastic. Regarding the selection of the k value , when modeling the dynamics of the observed process, there is virtually  no  standard  distributional  theory  that  can  be  applied  to  evaluate  the  MarkovSwitching model against alternatives such as a linear time series model. Nevertheless, some procedures have been suggested to test for the number of regimes. For instance, Hansen (1992) proposed to obtain the optimum of the likelihood surface through a grid search over the parameter space, but to some extent, the computational burden limits the applicability of this procedure. On the other hand, Cheung and Erlandsson (2005) suggested a simulated likelihood ratio test based on a Monte Carlo method, but as they admitted, their results are fairly sample-specific. In this work we follow our economic intuition and the visual inspection of the data to suggest a three-state model as an appropriate specification, so that k = 3. This way we capture the non linearity in the data generating process in which remittances flows to Mexico alternate between sustained periods of medium, high and low or negative growth rate.


<!-- p:5 -->


To  complete  the  description  of  the  Markov-Switching  model  we  point  out  that  the unobservable realization of the regime s ௧ ∈ ሼ1,2,3ሽ is governed by a discrete-time, discretestate Markov stochastic process, which is defined by transition probabilities as follows

$$p _ { i j } = \Pr ( s _ { t + 1 } = j | s _ { t } = i ) , \ \ \sum _ { j = 1 } ^ { 3 } p _ { i j } = 1 \ \ \text {for all } \ i , j \ \in \{ 1 , 2 , 3 \}$$

where: p௜௝ denotes  the  probability  that  state i will  be  followed  by  state j, and  these  are collected into a transition probability matrix P given by

$$P & = \begin{bmatrix} p _ { 1 1 } & p _ { 1 2 } & p _ { 1 3 } \\ p _ { 2 1 } & p _ { 2 2 } & p _ { 2 3 } \\ p _ { 3 1 } & p _ { 3 2 } & p _ { 3 3 } \end{bmatrix} .$$

The model is useful to make probabilistic inferences about the unobserved state s ௧ based on estimates of the transition probabilities, p௜௝ . Two types of inference can be made: (i) about the smoothed probability, Prሺs ௧ ൌ j|Iே ሻ , which is the probability of being in state j based on the  entire  observed  information  set,  and  (ii)  about  the  filtered  probability,  denoted  as Prሺs ௧ ൌ j|I ௧ ሻ, which is the best guess about s ௧ inferred from information in the sample data up to time t &lt; N .

In this work, we model the dynamics of remittances through a Markov-Switching model with three regimes, to allow for episodes of medium, high and low growth. Because episodes of high growth are normally more volatile than periods of recession, which in turn are more volatile than periods of low growth, we consider a heteroskedastic error term in the model. We also consider a regime-dependent mean model instead of a regime-dependent intercept one, since the former implies that a permanent regime shift leads to an immediate jump in the mean growth rate of the process to its new level. For the latter, a once and for all regime shift in the intercept gives rise to a dynamic response of the growth rate of the observed variable that is identical to an equivalent shock in the white noise series (see Krolzing, 1997).

### 2.2 Underlying Trend with Controlled Smoothness

Rather than using the standard Markov-Switching model for the original time series,  we follow Yuan's (2011) suggestion of applying the Markov-Switching model to the trend of the variable of interest. Thus, we assume that the observed time series can be expressed as a signal-plus-noise model, not because we believe that the data were generated this way, but just to take into account the empirical regularities in the data, that is,

$$y _ { t } = \tau _ { t } + \eta _ { t }$$

where: ሼτ ௧ ሽ is the trend (or signal) and ሼη ௧ ሽ is the noise of ሼy ௧ ሽ , for t =1,..., N .


<!-- p:6 -->


Then,  we  can  use  Penalized  Least  Squares  (PLS)  to  estimate  the  trend  by  posing  the following minimization problem, as in Guerrero (2007)

$$\min _ { \{ \tau _ { i } \} } \{ \sum _ { t \, 1 } ^ { N } ( y _ { t } - \tau _ { t } ) ^ { 2 } + \lambda \sum _ { t \, 3 } ^ { N } ( \tau _ { t } - 2 \tau _ { t - 1 } + \tau _ { t - 2 } - \mu ) ^ { 2 } \}$$

where 0   is a constant that penalizes the lack of smoothness in the trend. That is, as 0,   the trend resembles more closely the original data, so that t t y τ  for all t , and no smoothness is achieved. The opposite occurs when   , in which case the trend follows  essentially  the  polynomial  model    2 1 2 ttt τ τ - τ which  represents  the  trend growth expressed as a second difference. Hence,  plays an important role in deciding the smoothness of the trend, while μ is  a  reference level for the trend growth. It should be noticed that the trend follows the second degree polynomial given by

$$\tau _ { t } \, \quad \beta _ { 0 } + \beta _ { 1 } t + ( \mu \, / \, 2 ) t ^ { 2 } \, \text { when } \, \mu \neq 0 \, ,$$

which becomes a straight line when 0  μ . Thus, using the reference level as 0, as is usual in practice ( e.g ., Yuan, 2011) has important consequences on the trend behavior, particularly at the end points of the time series, as it will be seen below.

By solving the minimization problem (5) with 0  μ ,  we obtain the Hodrick-Prescott (HP) filter  which provides trend estimates of the series ሼy ௧ ሽ ,  where t  =1, ..., N .  Problem (5) is solved assuming that both the reference level μ and the smoothing parameter λ are known,

but in practice we have to provide appropriate values of those parameters, keeping in mind that a small value of the latter yields a trend that resembles the original data and a large value produce a trend that behaves as a straight line. Below, we focus on this matter.

Following Yuan's (2011) idea we employ the Markov-Switching representation for the trend rather than the original series, so that expression (1) is no longer valid for y ௧ , but for τ ௧ . Thus, let us consider the following unobserved-component model that underlies the minimization problem (5)

$$y _ { t } = \tau _ { t } + \eta _ { t } \text { with } \eta _ { t } \sim ( 0 , \sigma _ { \eta } ^ { 2 } ) \text { \ for } t = 1 , \dots , N$$

$$\tau _ { t } \quad \mu + 2 \tau _ { \varepsilon _ { - 1 } } - \tau _ { t \varepsilon _ { 2 } } + \varepsilon _ { t } \text { \ with } \varepsilon _ { t } \sim ( 0 , \sigma _ { \varepsilon } ^ { 2 } ) \text { \ for } t = 3 , \dots , N ,$$

where we use  ~ ) (0 2 ν , σ to say that the random variable  has mean 0 and variance 2 ν σ .

The  sequence  { t η }  contains  serially  uncorrelated  random  errors  and  { t ε }  is  another sequence of serially uncorrelated random errors that is also uncorrelated with the previous sequence.

Solution of the minimization problem can be expressed in matrix notation by letting y , τ and η be vectors of size N containing the observations, trends and noises, respectively. Then we write equations (7) and (8) in matrix notation as

and

$$\begin{matrix} y & \tau + \eta , \end{matrix}$$


<!-- p:7 -->


$$K \tau \quad \mu 1 _ { _ { N - 2 } } + \varepsilon \, ,$$

where: η and ε are random  vectors such that N E 0 η  ) ( , N I Var 2 ) (   η ,

2 ) (   N E 0 ε , 2 2 ) (   N I Var   ε and 0 ' ) (  ηε E ,  with I M the M -dimensional  identity matrix. In (10) we use the following ( N2)× N matrix representation of the second difference operation appearing in (8)

$$K \begin{pmatrix} 1 & - 2 & 1 & 0 & \dots & 0 & 0 \\ 0 & 1 & - 2 & 1 & \dots & 0 & 0 \\ & & & & \ddots & & & \\ 0 & 0 & 0 & & \dots & - 2 & 1 \end{pmatrix} .$$

An application of Generalized Least Squares (GLS) to the system of equations (9) - (10) yields  the  Best  Linear  Unbiased  Estimator  (BLUE)  of  the  trend  vector,  given  by  (see Guerrero, 2007 for details)

$$\hat { t } \ \ ( I _ { _ { N } } + \lambda K ^ { \prime } K ) ^ { - 1 } ( y + \lambda \mu K ^ { \prime } 1 _ { _ { N - 2 } } ) \, ,$$

with 2 2 /      . GLS produces the Variance-Covariance matrix 1 2 ) ' (     K K I N    and  once  an  appropriate  value  of  is  given,  unbiased estimators of the error variances are obtained from 2 2 ˆ ˆ   λσ σ  and

$$\hat { \sigma } _ { \eta } ^ { 2 } & \, \left [ \sum _ { t \, ^ { 1 } } ^ { N } ( y _ { t } - \hat { \tau } _ { t } ) ^ { 2 } + \lambda \sum _ { t \, ^ { d + 1 } } ^ { N } ( \hat { \tau } _ { t } - 2 \hat { \tau } _ { t - 1 } + \hat { \tau } _ { t - 2 } - \hat { \rho } ) ^ { 2 } \right ] / ( N - 3 ) \, \text {with} \, \hat { \rho } \text { the sample mean} \\ \text {of the obtained coords in some different ones} \, T & \, \text {the results about estimoting variance are not}$$

of the observed series in second differences. The results about estimating variances are not used in the sequel, but are mentioned just for completeness of this procedure.

To appreciate the effect of the constant μ , we should notice that the array 2 '  N K 1 appearing in (12) is an N -dimensional vector of zeros, except for the first two and last two elements, that is,   ' 1,  1, 0, ..., 0,  1, 1 ' 2   N K 1 . Therefore, the observed values of the original series } { t y enter the formula of the estimator τ  modified in both of its extremes by the value of μ , weighted by  . That is, (12) indicates applying the smoother matrix 1 ) ' (   K K I N  to

$$y + \lambda \mu K ^ { \prime } 1 _ { _ { N - 2 } } \quad ( y _ { 1 } + \lambda \mu , \, y _ { 2 } + \lambda \mu , \, y _ { 3 } , \dots , y _ { _ { N - 2 } } , \, y _ { N - 1 } + \lambda \mu , \, y _ { \, N } + \lambda \mu ) ^ { \prime }$$

and by doing that we are adjusting the first two and last two values of the series, in the spirit of Yuan (2011). However, our 'adjustment' comes out from the model specification for the trend  (10),  while  Yuan  solved  the  end-of-sample  problem  by  using  different  smoothing parameter values, that is, λ for t = 3 to N -2, 2 λ /3 for t = 2 and t = N -1, and λ /3 for t = 1 and t = N. That solution forces the trend to get closer to the original data at the end points, but the choice of λ values has no theoretical justification.


<!-- p:8 -->


Moreover,  we  should  notice  that  the  presence  of μ also  affects  the  results  when extrapolating the trend, as shown by expression (6) since 0   implies a trend that follows a quadratic polynomial and the extrapolated trend values depend critically on the last two estimated values. That is, if we call ) ( ˆ h N  the h -period ahead forecast of h N   , with origin at N , we get for 1  h

$$\hat { \tau } _ { N } ( h ) = [ h ( h + 1 ) / 2 ] _ { \mu } + ( h + 1 ) \tau _ { N } - h \, \tau _ { N - 1 } \, .$$

In order to apply (12), we follow Guerrero's (2007, 2008) proposal of choosing the smoothing parameter λ by first fixing the value of the index

$$\text {by first fixing the value of the index} \\ S ( \lambda , N ) \quad 1 - t r \left [ ( I _ { N } + \lambda K ^ { \prime } \, K ) ^ { - 1 } \right ] / \, N$$

that measures the smoothness achieved by the trend. Among other properties, this index takes on values between 0 and 1 ,  and  measures the proportion of precision induced by smoothing the data. Thus, we fix the amount of desired smoothness for the trend and solve equation (15) numerically for the corresponding λ value.

An appropriate percentage of smoothness can be obtained from the following guidelines deduced by Guerrero et al . (2017) through a simulation study. In all cases, it is convenient to choose a large value for the index of smoothness, without exceeding the upper bound 12/N. This bound is obtained by noticing that the K matrix involved has rank N2, so that the matrix K'K has two eigenvalues equal to zero and the remaining N2 nonzero eigenvalues are 2 1 ,...,  N e e . Thus, the trace appearing in (15) can be written as     2 ) (1 ... ) (1 ' 1 2 1 1 1            N N e e K K I tr    and, therefore,   N N S 2 / 1 ,    as    . Then, from the results of the aforementioned simulation

study we suggest:

- (i) if  the  original  series  behaves  as  a  straight  line,  choose  a  large  value  of 100   N S ,  % , starting from 90% for N &gt; 48 , and increase it for larger values of N ;
- (ii) when the series shows a non-straight line pattern, the percentage of smoothness should start at 85%, and increase its value for larger values of N &gt; 48 .

It  is  important  to  emphasize  that  filters  are  designed  to  achieve  specific  goals, e.  g. , Fitzgerald and Christiano's (2003) band pass filter is useful when the focus of the study lies on business cycles. In the present case, we focus on the estimation of the underlying trend of the time series in order to apply Yuan's (2011) proposal, who used the usual HP filter (with the usual value for the smoothing parameter λ = 1600) to that end. We employed a databased approach that includes the HP filter as a special case. Thus, instead of fixing the value of λ we fix the percentage of smoothness to be achieved by the trend, in order to be able to establish valid comparisons for different sample sizes and different frequency of observations. Some robustness exercises of the approach followed here have been provided elsewhere (see Guerrero, 2008).


<!-- p:9 -->


## 3. Empirical Results

The data for the empirical application is a quarterly series of workers' remittances in dollars received by Mexico and recorded by BANXICO from 1995:I through 2016:IV. We applied a first difference to the data expressed in logarithms and multiplied those values by 100 to work with percent growth rates. The resulting series runs from 1995:II to 2016:IV. We carried out the computations with the WinRATS package, version 9.0 (www.estima.com).

To contrast the forecasting results for remittances obtained with the proposed smoothing technique,  we  used  three  models  in  our  analysis.  The  first  one  is  the  standard  MarkovSwitching  model,  namely  the  Markov-Switching-Mean-Heteroskedastic  model  with  3 regimes, called MSMH(3). The second one is the three-regime Markov-Switching-MeanHeteroskedastic-filtered  model  with  the  HP-filter  (HP-MSMH),  the  filtering  technique employed in this model is the standard Hodrick-Prescott filter with the value λ ൌ 1600 (that produces the smoothness index   N S ,  % = 93.18%, which lacks a practical interpretation).

The third one is the three-regime Markov-Switching-Mean-Heteroskedastic-filtered model with Smoothing (S-MSMH), with the filtering technique proposed in this paper and   N S ,  % = 85% , so that λ ൌ 45.1 .  Figure 2 shows the logarithm of remittances flows to Mexico and its  trend  estimates.  Let us recall that the two filtered models are proposed because the standard Markov-Switching model is likely to overreact to irregular transitory blips in the data and such overreaction induces instability in parameter estimation and misclassification of regime shifts, which in turn undermines the model's forecasting ability.

Figure 2 Logarithm of Remittances Flows to Mexico and Trend Estimates

Note: Trends obtained with the HP filter ( λ ൌ 1600 ) and with 85% smoothness ( λ ൌ 45.15ሻ .

Table 1 reports the maximum likelihood estimates based on the full sample of data. In the panel  at  the  bottom  of  Table  1  we  present  some  hypothesis  tests  for  model  selection. Because the conclusions drawn from the test results are unchanged for the S-MSM, HPMSM and MSMH models, we need only explain the test results based on the S-MSM. The notation  S-MSM(2)|S-MSM(3) in Table 1 denote the null hypothesis of model S-MSM(2) model against the alternative hypothesis of model S-MSM(3). The log likelihood values for models S-MSM(2) and S-MSM(3) are -163.8733 and -138.8753, respectively, and the LR statistic is 2 ∗ ሾെ138.8753 െ ሺെ163.8733 ሻሿ ൌ 49.996 ൐ χ ଶ ሺ2ሻ , which indicates that model SMSM(3) is preferable to model S-MSM(2). The LR test for model selection indicates that the three-state Markov-Switching model is preferable to the two-state Markov-Switching model in each case of the compared models.


<!-- p:10 -->


As Krolzing (1997) argues, there is no general test to compare two models with different number of regimes. The issue is that the asymptotic theory cannot be used here because there  are  unidentified  nuisance  parameters  as  well  as  violation  of  the  non-singularity conditions.  However,  most  researchers  still  use  the  LR  to  obtain  useful  supporting evidences. Throughout this paper, the LR tests are considered in this way.

The three regimes considered are low or negative growth, medium growth and high growth, classified  as  regimes  1,  2  and  3,  respectively.  The  estimates  indicate  that  regime  1  is associated with a 3.83% quarterly downward trend predicted by the unfiltered MSMH model, while the HP-MSMH and S-MSMH models predict no growth of remittances in regime 1. The MSMH estimates a 2.47% quarterly downward trend for regime 2, while models HP-MSMH and S-MSMH estimate an upward trend for remittances of about 3.1% and 2.7%, for the same regime. The three models estimate an upward remittances trend of about 18.9%, 4.5% and 5.5% for regime 3, respectively.

Table 1 Estimation Results for Each Model (Standard Errors in Parenthesis). Period 1995:II - 2016:IV

| Parameter                         | Model - MSMH(3)             | Model - HP-MSMH(3)                 | Model - S-MSMH(3)                          |
|-----------------------------------|-----------------------------|------------------------------------|--------------------------------------------|
| μ ଵ μ ଶ μ ଷ σ ଵ σ ଶ σ ଷ p ଵଵ p ଶଶ | -3.835 (1.310)              | 0.385 (0.121)                      | -0.069 (0.216) 2.750 (0.108) 5.513 (0.201) |
|                                   | -2.477 (1.225)              | 3.145 (0.008)                      |                                            |
|                                   | 18.914 (1.130)              | 4.502 (0.147)                      |                                            |
|                                   | 43.406 (12.360)             | 0.674 (0.222)                      | 1.918 (0.604)                              |
|                                   | 29.655 (8.045)              | 0.0009 (0.000)                     | 0.460 (0.131)                              |
|                                   | 24.923 (8.714)              | 0.917 (0.231)                      | 1.483 (0.414)                              |
|                                   | 0.412 (0.109)               | 0.986 (0.231)                      | 0.963 (0.279)                              |
|                                   | 0.299 (0.000)               | 0.967 (0.025)                      | 0.977 (0.026)                              |
| p ଷଷ                              | 0.066 (0.000)               | 0.965 (0.012)                      | 0.952 (0.012)                              |
| Model selection test              | Model selection test        | Model selection test               | Model selection test                       |
| MSMH(2)&#124;MSMH(3) 19.63*       | MSMH(2)&#124;MSMH(3) 19.63* | HP-MSMH(2)&#124;HP-MSMH(3) 72.178* | S-MSMH(2)&#124;S-MSMH(3) 49.996*           |

Note: MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic model; HP-MSMH(3) = 3regime Markov-Switching Mean-Heteroskedastic filtered model with HP-filter; S-MSMH(3) = 3regime Markov-Switching Mean-Heteroskedastic filtered model with proposed Smoothing filter.

*Significant at the 5% level.

Table 1 also shows that according to the estimates of the HP-MSMH and S-MSMH models, remittances seem to be well-characterized by long swings with sustained low, medium and high growth regimes. This high persistence of regimes is represented by the large regimestaying probabilities, pଵଵ , pଶଶ and pଷଷ ; that is, the probability of staying in a regime once the process enters it. The expected duration of regime j is defined as 1/ ሺ1 െ p ௝௝ ሻ . Thus, the SMSMH and HP-MSMH models predict that the low-growth regime is expected to persist


<!-- p:11 -->


about 9 and 12 years on average, respectively; while the medium-growth regime is expected to  persist  about  7  and  6  years  on  average,  respectively;  and  the  high-growth  regime  is expected to persist about 5 and 6 years on average, respectively. These long persistence periods in each regime may be an appropriate depiction of the remittances' lengthy mediumgrowth rate during 1995:I-1999:IV and 2014:I-206:IV, high-growth rate during 2000:I-2007:IV and low or negative growth rate from 2008:I-2013:IV, which matches our visual inspection of Figure 1.

On the other hand, no long swings are predicted by the unfiltered MSMH model. According to the regime staying probabilities, the low growth regime is expected to persist about two quarters; while the medium and high growth regimes are expected to persist about 1 quarter. This misidentification is corrected by the models with smoothing. On this regard, a merit of the use of filtering the data is that it enables the estimation procedure to compute more precisely the signals of genuine regime shifts.

One  of  the  most  innovative  aspects  of  the  Markov-Switching  model  lies  in  its  ability  to objectively date the state of the process using the so-called smoothed probabilities. Panels (b), (c) and (d) of Figure 3 show plots of the smoothed probabilities that the process is in each of the three regimes at each date in the sample, estimated by the MSMH, HP-MSMH and S-MSMH models, respectively; while panel (a) plots the logarithm of remittances flows to Mexico. For comparison, the corresponding dates of each one of the three regimes, as identified by HP-MSMH and S-MSMH models, are presented in Table 2. The dates at which we conclude that the process had switched between regimes are based on the following cutoff point for the smoothed probabilities, pሺs ௧ ൌ i|Iே ሻ ≷ 0.5 .

Figure 3 (a) Log-remittances; (b), (c) and (d) Smoothed Probabilities that the Process is in Each of the Three Regimes at Each Date in the Sample, Estimated by the MSMH, HP-MSMH and S-MSMH Models, Respectively

The high-growth rate period identified by the S-MSMH model is particularly interesting, since it matches the period where the average transaction cost of money transfers fell more than 50%, also the inclusion of debit and credit cards as an option to transfer remittances to Mexico, and the single most important determinant of the increase of remittances after year 2000, namely, a better mechanism implemented by BANXICO to measure remittances.


<!-- p:12 -->


Although  the  HP-MSMH  and  S-MSMH  models  identified  almost  the  same  date  for  the beginning of the lower or negative growth rates period, they differ when identifying the end of this period; while the former identifies 2016:IV, the latter identifies 2013:IV. The lower or negative growth rates period identified by the S-MSMH model deserves special attention. This matches the period when the U.S. Government implemented a restrictive immigration policy that increased the number of Border Patrol agents in the South West border and the number of aircraft and ground surveillance systems to contain the flows of migrants. It also matches the beginning of the 2008 economic crisis that severely affected the U.S. economy and, hence, some economic sectors which traditionally employ Mexican immigrants.

The smoothed probabilities estimated by the S-MSMH model at the end of the period of analysis also deserve special attention. Panels (c) and (d) in Figure 3 show the smoothed probabilities estimated by the HP-SMSH and S-MSMH models, respectively. As we can see, panel (d) shows that at the end of the period of analysis, S-MSMH model identifies another medium-growth rate regime. This behavior is not observed in the smoothed probabilities estimated with the HP-MSMH model and could be explained by the recovery of remittances flows to Mexico since the first quarter of 2014. The improvements noticed at the end of 2013 and the beginning of 2014 in the U.S. employment indicators, specifically in those states where Mexican immigrants typically reside, such as California and Texas, seem to explain the recent recovery of remittances to Mexico. Additionally, following the November 2016 Presidential election, there were increased fears among Mexicans in the U.S, both with and without legal immigration status that President Trump would fulfill his campaign promise to impose restrictions or taxes on remittances to Mexico. It is therefore possible that people fearing they might be affected by such measures increased their remittances in November and December 2016 to avoid future regulation or taxation. The depreciation of the Mexican peso  with  respect  to  the  U.S.  Dollar  is  another  factor  contributing  to  the  increase  in remittances in these two months.

A close examination of these results reveals that the S-MSMH(3) model can adequately capture  the  movements  of  remittances  flows  to  Mexico  and,  therefore,  improve  its forecasting performance, as we show below.

Table 2 Dates of the Regimes, as Identified by the HP-MSMH and S-MSMH Models

| Regimes - Model   | Regimes - Medium-growth rate   | Regimes - High-growth rate   | Regimes - Low-growth rate   |
|-------------------|--------------------------------|------------------------------|-----------------------------|
| HP-MSMH           | 1995:II-1997:IV                | 1998:I-2006:II               | 2006:III-2016:IV            |
| S-MSMH            | 1995:II-2001:I 2015:I-2016:IV  | 2000:II-2006:I               | 2006:II-2014:IV             |

Note: The dates at which we conclude that the process had switched between regimes are based on the cutoff point, pሺs௧ ൌ i|I ே ሻ ≷ 0.5 .

### 3.1 A Forecasting Exercise

Remittances  have  had  a  significant  positive  effect  on  the  nation's  economy  and  on household well-being for those families that receive them. Studies have shown that workers' remittances  reduce  poverty  (Esquivel  and  Huerta-Pineda  2007),  increase  investment  in children's schooling (Borraz 2005; Hanson and Woodruff 2003), finance small business and increase access to financial services (Demirguc-Kunt et al ., 2011).  From a macroeconomic perspective, remittances can boost aggregate demand and thereby GDP as well as spur economic growth. However, remittances may also have adverse macroeconomic impacts by increasing prices of domestically produced goods and exchange rate as well as by creating moral hazard problems.


<!-- p:13 -->


Moral hazard problems are related to the potential reduction in labor supply, the development of conspicuous consumption patterns and the inability to develop a culture of saving that can enable future  investment and growth.  Another impact  of remittances flows  is  their  effect uplifting the prices in the recipient economy. There are some evidences that remittances flows to Mexico have significant positive effect on both inflation and relative price variability (Balderas and Nath, 2008).  Thus, policymakers are concerned about the effects of money transfers at a time when local economic growth is also slowing and needs forward-looking analyses of the sustainability of remittances, trying to foresee whether remittances flows would continue at their current or higher levels, in the short and medium term. Therefore, the need of generating forecasts is clear in this context.

The  forecasting  exercise  described  below  could  be  used  by  policymakers  to  choose appropriate policies according to the different states of remittances growth. For example, if a negative or low grow rate is foreseen in the near future, policies like 'Directo a Mexico,' a mechanism implemented by the Mexican government to reduce average transaction costs of money transfers and the introduction of technology, including debit and credit cards, could be reinforced to avoid the slowdown of flows. Facilitating access to banking services lets migrants  take  advantage  of  the  more  secure  and  less  expensive  transmission  methods offered  by  banks  while  helping  them  build  a  relationship  with  the  bank.  Building  that relationship is key to gaining financial literacy and access to credit for asset accumulation and investment, and hence avoid the conspicuous consumption.

On the other hand, if a medium or high growth rate is predicted for the near future, the financial intermediaries can take advantage of this information to be creative, channel these flows  towards  the  productive  sectors  through  the  banking  system,  thus  dampening  the effects of inflation. Remittances initiative programs like 'Your House in Mexico' designed by the Mexican government to help the migrant to get a property, by paying it through money transfers, could also be reinforced to give a better use of remittances inflows.

The forecasting performance of Markov-Switching models heavily depends on the regime in which the forecast is made, so it requires only a small misclassification of which regime the process  will  be  in  to  lose  the  advantage  of  knowing  the  correct  model  specification.  A question of particular interest here is the following: Given that the filtered model works well in capturing the trend persistence of remittances flows to Mexico, can it outperform, in terms of  Mean  Squared  Error  (MSE),  some  linear  alternatives,  specifically  the  simple  random walk?

It is quite standard to assume that the optimal predictor is given by the conditional mean for a  given  information  set Y௧ .  Nevertheless,  in  contrast  to  linear  models,  the  MSE  optimal predictor does not have the property of being a linear predictor if the true data generating process  is  nonlinear.  In  general,  the  derivation  of  the  optimal  predictor  may  be  quite complicated in empirical work. However, an attractive feature of Markov-Switching models as a class of nonlinear models is the simplicity of forecasting if the optimal predictor is the conditional expectation.

Following Hamilton (1994), let ξ መ ௧|௧ be the k ൈ 1 vector of conditional probabilities, Pሼs ௧ ൌ j|Y ௧ ; θሽ , for j=1,2,...,k , which are estimates of the value of s ௧ based on data obtained through date t . Given the maximum likelihood estimator, θ ෠ , the h -period ahead forecast of y௧ା௛ is given by

$$\hat { y } _ { t + h | t } = E [ y _ { t + h } | y _ { t } ; \hat { \theta } ] = \xi ^ { \prime } _ { t + h | t } * \hat { \mu } = \xi ^ { \prime } _ { t | t } * P ^ { h } * \hat { \mu } ,$$


<!-- p:14 -->


where: μ̂ ൌ ሺμ̂ ଵ , μ̂ ଶ , ... , μ̂ ௞ ሻ′ is  the  vector  of  estimates  of  the  mean-dependent  trends.  We generated h -period ahead forecasts of the level of log-remittances flows to Mexico as

$$\hat { e } _ { t + h | t } = e _ { t } + \sum _ { j = 1 } ^ { h } \hat { y } _ { t + j | t } ,$$

and calculated the average squared value of the forecast error as

$$\sum _ { t = 1 } ^ { N - h } \left ( \hat { e } _ { t + h | t } - e _ { t + k } \right ) ^ { 2 } / ( N - h ) ,$$

for forecast horizons h=1, ..., 4 .

Table 3 presents the MSEs of the in-sample and out-of-sample forecasts and compares them with those of a random walk specification, whose forecasts are given by ê ௧ା௛|௧ ൌ e௧ ൅ hy ത , with y ത ൌ ∑ y௧ ே ௧ୀଵ /N . As we can see, the average improvement in the in-sample forecast precision is about 16.7% for the unfiltered MSMH model, while for the two filtered HP-MSMH and S-MSMH models it is about 16.8% and 18.9%, respectively, averaging over the fourquarter-ahead horizon. We further notice that the two filtered Markov-Switching models well outperform the unfiltered model during the forecast horizon considered.

Table 3 In-sample and Out-of-sample MSE of the Forecasts at Horizons from One to Four Quarters

| In-sample Mean Squared Forecast Error - Model   | In-sample Mean Squared Forecast Error - Forecast horizon - 1   | In-sample Mean Squared Forecast Error - Forecast horizon - 2   | In-sample Mean Squared Forecast Error - Forecast horizon - 3   | In-sample Mean Squared Forecast Error - Forecast horizon - 4   |
|-------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Random walk                                     | 121.81713                                                      | 214.55569                                                      | 209.52447                                                      | 174.75727                                                      |
| MSMH(3)                                         | 92.72398                                                       | 144.24375                                                      | 168.04381                                                      | 191.07547                                                      |
| Percent improvement                             | 23.8%                                                          | 32.7%                                                          | 19.7%                                                          | -9.3%                                                          |
| HP-MSMH(3)                                      | 117.63691                                                      | 199.67678                                                      | 174.21680                                                      | 108.39477                                                      |
| Percent improvement                             | 3.4%                                                           | 6.9%                                                           | 16.8%                                                          | 37.9%                                                          |
| S-MSMH(3)                                       | 116.74488                                                      | 194.66759                                                      | 166.24532                                                      | 101.86081                                                      |
| Percent improvement                             | 4.1%                                                           | 9.2%                                                           | 20.6%                                                          | 41.7%                                                          |
| Out-of-sample Mean Squared Forecast Error       | Out-of-sample Mean Squared Forecast Error                      | Out-of-sample Mean Squared Forecast Error                      | Out-of-sample Mean Squared Forecast Error                      | Out-of-sample Mean Squared Forecast Error                      |
|                                                 | Forecast horizon                                               | Forecast horizon                                               | Forecast horizon                                               | Forecast horizon                                               |
| Model                                           | 1                                                              | 2                                                              | 3                                                              | 4                                                              |
| Random walk                                     | 103.86399                                                      | 190.50762                                                      | 256.25722                                                      | 328.23586                                                      |
| MSMH(3)                                         | 98.72661                                                       | 175.40750                                                      | 227.60289                                                      | 256.26342                                                      |
| Percent Improvement                             | 4.9%                                                           | 7.9%                                                           | 11.1%                                                          | 21.9%                                                          |
| HP-MSMH(3)                                      | 91.28532                                                       | 142.97628                                                      | 145.63749                                                      | 126.45526                                                      |
| Percent Improvement                             | 12.1%                                                          | 24.9%                                                          | 43.1%                                                          | 61.4%                                                          |
| S-MSMH(3)                                       | 90.65535                                                       | 140.98101                                                      | 140.47951                                                      | 116.37265                                                      |
| Percent Improvement                             | 12.7%                                                          | 25.9%                                                          | 45.1%                                                          | 64.5%                                                          |

Notes :  In-sample  forecast  errors.  Estimation  sample  1995:II  -  2016:IV  and  MSEs  are  those

associated with forecasts for dates t=1995:II+k  to 2015:II where k is the forecast horizon. Out-of-sample forecast errors. Estimation sample 1995:I - 2007:IV and MSEs are associated with

forecasts for dates t=2008:I+k to 2016:IV where k is the forecast horizon.

MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic model;

HP-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with HP-filter; S-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with proposed Smoothing filter.


<!-- p:15 -->


To evaluate the out-of-sample forecasting performance of the models, we re-estimated the parameters with data up to the end of 2007. We chose this date so as not to take into account the period prior to the beginning of the 2008 economic crisis, which severely affected the U.S.  economy.  Hence,  almost  the  entire  period  of  the  low  or  negative  growth  rate  of remittances was not used for parameter estimation. The lower panel of Table 3 compares the out-of-sample MSEs of the forecasts of the three models with that of the random walk. We can observe that the three models generally outperform the random walk, particularly at long forecasting horizons. The average improvement in out-of-sample forecast precision is about 11.4% for the unfiltered MSMH model, 35.3% for the filtered HP-MSMH model, and 37% for the filtered S-MSMH model, averaging over the forecast horizon up to four quarters. We further notice that the HP-MSMH and S-MSMH models well outperform the random walk and the unfiltered model, slightly more prominently the latter and in particular for the fourperiod-ahead forecast.

### 3.2 Forecast Evaluation

To  complement  the  previous  analysis  of  forecast  bias  and  precision  we  now  focus  on forecast accuracy. Table 4 presents Diebold-Mariano (DM) test statistics (see Diebold and Mariano, 1995) for the null hypothesis of no difference in the accuracy of two competing forecasts, that is, the unfiltered and the two filtered models versus the random walk. Each calculated  statistics  should  be  compared  with  a  standard  normal  distribution  in  order  to declare statistical significance. However, since the standard DM test is known to over-reject the null hypothesis in the context of finite samples, we applied here the modified DM test proposed by Harvey et al . (1997).

The DM test results reported in Table 4 reinforce our findings in Table 3 lower panel, that the unfiltered and the two filtered models are generally significantly better than the random walk, in the context of out-of-sample forecasting.

Table 4

##### The Diebold-Mariano Test for Relative Forecasting Ability

| Models             |   Forecast horizon - 1 |   Forecast horizon - 2 |   Forecast horizon - 3 |   Forecast horizon - 4 |
|--------------------|------------------------|------------------------|------------------------|------------------------|
| MSMH(3) vs . RW    |                        |                        |                        |                        |
| MSE Ratio          |                 0.9583 |                 0.9220 |                 0.8884 |                 0.7843 |
| DM-stat            |                 0.4407 |                 2.0814 |                 5.3450 |                 4.0376 |
| p-value            |                 0.3297 |                 0.0187 |                 0.0000 |                 0.0000 |
| HP-MSMH(3) vs . RW |                        |                        |                        |                        |
| MSE Ratio          |                 0.8856 |                 0.7496 |                 0.5604 |                 0.3881 |
| DM-stat            |                 1.5593 |                 2.2134 |                 3.6545 |                 3.1643 |
| p-value            |                 0.0594 |                 0.0134 |                 0.0001 |                 0.0007 |
| S-MSMH(3) vs. RW   |                        |                        |                        |                        |
| MSE Ratio          |                 0.8799 |                 0.7386 |                 0.5384 |                 0.3563 |
| DM-stat            |                 1.4826 |                 2.1242 |                 3.5121 |                 3.0408 |
| p-value            |                 0.0690 |                 0.0168 |                 0.0002 |                 0.0011 |

Note : RW = random walk; MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic model; HP-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with HP-filter; TS-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with Smoothing filter.

Forecasts are based on estimated period 1995:I-2007:IV and forecast periods 2008:I-2016:IV .


<!-- p:16 -->

## 4. Conclusions

This paper proposes a new approach for estimating a trend with controlled smoothness in order  for  a  Markov-Switching  model  to  be  applied  more  appropriately  to  detect  different regimes in the time series of remittances flows to Mexico. Once those regimes are detected and the probabilities of staying in each of the regimes estimated, the model was used to predict remittances flows. The new approach allowed us to fix a desired percentage for the smoothness of the trend, so that valid comparisons can be obtained for different applications (with different time series or for different sample periods for the same series) as stressed by Guerrero (2008). Besides, the proposal also includes a new data-based and very simple way of taking care of the adjustment of the trend at the endpoints of the time series. We  show  that  combining  a  Multi-State  Markov-Switching  model  with  the  controlled smoothing  filter  technique  enhances  both  in  sample  and  out-of-sample  forecasting performance. Preliminary results obtained by applying the conventional model and filtering technique warned us that the existence of highly irregular components in the data tends to distort  the  estimation  procedure  of  the  Markov-Switching  model  and  undermines  its forecasting  power.  Our  proposed  specification  eliminates  this  modeling  nuisance  and reinforces  the  forecasting  superiority  of  the  Markov-Switching  model.  The  empirical application  was  carried  out  with  three  different  Multi-State  Markov-Switching  model specifications  and  the  one  based  on  our  proposal  was  seen  to  be  best  for  parameter estimation as well as for generating statistically better forecasts, so that strong empirical support was obtained for our proposed procedure. The results obtained in this particular application were clear in defining three different regimes associated with the speed of growth of  remittances  flows:  low-growth,  medium-growth  and  high-growth  that  can  be  easily appreciated visually in the data under study. Thus, the interpretation was very reasonable and  the  results  are  therefore  practically  free  of  misjudgments.    Our  results  shows  that correctly identifying the trend in the inflow remittances plays a key role in achieving superior forecasting ability with respect to the simple random walk. Although our model provides good forecasts in terms of the MSE, a forecast based on a structural model could provide more information for designing policies that can help attract remittances inflows and for using them productively. However, such a model is difficult to implement until the quality of data on the determinants of remittances improves. We believe that, even though research has expanded the understanding of remittances flows and their impacts, there is more to do about their prediction and understanding of how predictability of the flows may affect their impact. As a final conclusion, we stress that the HP-filtered model produces suboptimal results, even though the smoothed probabilities for staying in a particular regime, as well as the regime dates and the remittance forecasts, are similar to those produced with our proposal. Besides, our proposed procedure is basically data-based, hence more objective than that based on the HP filter, since the smoothing parameter involved comes out as a result of fixing a desired percentage of smoothness for the trend, which in turn can be decided from very easy-to-

follow and data-based guidelines.

### Acknowledgements

The  authors  gratefully  acknowledge  the  comments  and  suggestion  of  two  anonymous referees and the editor of this journal. Islas and Guerrero thank the financial support provided by Asociación Mexicana de Cultura, A. C. to carry out this work. A. Islas also acknowledges support  from  the  National  Council  for  Science  and  Technology  of  Mexico  (CONACYT), sabbatical scholarship. This work was done whilst A. Islas was visiting the Department of Economics, Nepal Study Center, and the RWJF Center for Health Policy at the University of New Mexico, USA. Eliud Silva dedicates this article to his mother.


<!-- p:17 -->

<!-- END SOURCE 24/40: Islas-Camargo_2019_forecasting-remittances-mexico-rjef.md -->

---
