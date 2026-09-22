---
id: "04_CortesGuerreroReyes_ComStat-SimCom2017"
source_pdf: "../pdf/04_CortesGuerreroReyes_ComStat-SimCom2017.pdf"
source_filename: "04_CortesGuerreroReyes_ComStat-SimCom2017.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/04_CortesGuerreroReyes_ComStat-SimCom2017.references.md"
---

<!-- p:1 -->

### Communications in Statistics - Simulation and Computation

ISSN: 0361-0918 (Print) 1532-4141 (Online) Journal homepage: http://www.tandfonline.com/loi/lssp20

## Trend smoothness achieved by penalized least squares with the smoothing parameter chosen by optimality criteria

##### Daniela Cortés-Toto, Víctor M. Guerrero &amp; Hortensia J. Reyes

To cite this article: Daniela Cortés-Toto, Víctor M. Guerrero &amp; Hortensia J. Reyes (2017) Trend smoothness achieved by penalized least squares with the smoothing parameter chosen by optimality criteria, Communications in Statistics - Simulation and Computation, 46:2, 1492-1507, DOI: 10.1080/03610918.2015.1005236

To link to this article:

[http://dx.doi.org/10.1080/03610918.2015.1005236](http://dx.doi.org/10.1080/03610918.2015.1005236)

CrossMark Accepted author version posted online: 01 Apr 2015. Published online: 01 Apr 2015.

[Submit your article to this journal](http://www.tandfonline.com/action/authorSubmission?journalCode=lssp20&show=instructions)

Article views: 26

[View related articles](http://www.tandfonline.com/doi/mlt/10.1080/03610918.2015.1005236)

[View Crossmark data](http://crossmark.crossref.org/dialog/?doi=10.1080/03610918.2015.1005236&domain=pdf&date_stamp=2015-04-01)

Full Terms &amp; Conditions of access and use can be found at

<!-- p:2 -->

#### Trend smoothness achieved by penalized least squares with the smoothing parameter chosen by optimality criteria

Daniela Cortés-Toto a , Víctor M. Guerrero b , and Hortensia J. Reyes a

a Facultad de Ciencias Físico Matemáticas, Benemérita Universidad Autónoma de Puebla. Puebla, Puebla, México; b Departamento de Estadística, Instituto Tecnológico Autónomo de México (ITAM). México, D.F., México

## ABSTRACT

This work presents a study about the smoothness attained by the methods more frequently used to choose the smoothing parameter in the context of splines: Cross Validation, Generalized Cross Validation, and corrected Akaike and Bayesian Information Criteria, implemented with Penalized Least Squares. It is concluded that the amount of smoothness strongly depends on the length of the series and on the type of underlying trend, while the presence of seasonality even though statistically significant is less relevant. The intrinsic variability of the series is not statistically significant and its effect is taken into account only through the smoothing parameter.

## 1. Introduction

When analyzing time series, it is usually interesting to study its trend component, which can be interpreted as an underlying element that reflects the smooth long-term behavior of the series; see Kaiser and Maravall (2001) and White and Granger (2011) for some references on this topic. A model to represent the observed series that encompasses the trend component has the form of an additive decomposition expressed as follows:

$$y _ { t } = \tau _ { t } + \xi _ { t } + \eta _ { t } , \text { for } t = 1 , \dots , N ,$$

where yt represents the observed values of the series at time t , τ t is its trend, η t is a random noise, and ξ t represents the seasonality of the series, if present. In what follows, the noise is assumed to be nonautocorrelated, with E (η t ) = 0 and Var (η t ) = σ 2 η for all t . In this section we assume that there are no seasonal effects, but the simulation will take those effects into account as a form of model misspecification. Representation (1) does not necessarily imply that we consider it a model for the true data-generating process, but only as a means to capture the empirical regularities typically observed in practice.

Penalized Least Squares (PLS) is a method to estimate the trend of a time series. It seeks to minimize a function of sums of squares that considers fidelity to the data, plus a penalization for the lack of smoothness. This function includes a smoothing parameter that trades off

## ARTICLE HISTORY

Received  October  Accepted  January 

####### KEYWORDS

Hodrick-Prescott filter; Penalized least squares; Percentage of smoothness; Smoothing parameter; Time series decomposition; Trend estimation

MATHEMATICSSUBJECT

CLASSIFICATION

M


<!-- p:3 -->


goodness of fit against smoothness. Thus, the problem is defined as follows:

$$\text {mises or not against smoothness.  This, the problem is defined as follows:} \\ \min _ { \{ \tau _ { t } \} } \left [ \sum _ { t = 1 } ^ { N } ( y _ { t } - \tau _ { t } ) ^ { 2 } + \lambda \sum _ { t = d + 1 } ^ { N } ( \nabla ^ { d } \tau _ { t } - \mu ) ^ { 2 } \right ] , \text { with } \lambda > 0 , \quad ( 2 ) \\ \text {are } d \text { is nonnegative integer} \text { such } \text {by the onevalst $D^{q}$} \text { is the difference operator of order} \text { for } \text {order}$$

where d is a nonnegative integer chosen by the analyst, ∇ d τ t is the difference operator of order d applied to { τ t } , that is, ∇ 0 τ t = τ t , ∇ τ t = τ t - τ t - 1 , ∇ 2 τ t = ∇ ( ∇ τ t ) , and so forth, while μ is a reference level for {∇ d τ t } and λ is the smoothing parameter. If λ → 0, there is basically no smoothness and the trend gets closer to the observed series, i.e., the fit is maximized by the observed data. On the other hand, by allowing λ →∞ priority is given to smoothness over fit and the series tends to behave like a polynomial expressed as ∇ d τ t = μ .

For d = 1 and d = 2, the PLS solutions with μ = 0 are known as Exponential Smoothing filter and Hodrick-Prescott (HP) filter, respectively, e.g., King and Rebelo (1993) and Hodrick and Prescott (1997). The former filter is used to smooth time series whose level changes along time, as it happens with financial series. The latter is employed in economics to smooth a time series on the assumption that its trend is locally linear. The usual application of the HP filter is for the analysis of economic cycles, since the cyclical component can be estimated as the difference between the observed series and its estimated trend; for details see Kaiser and Maravall (2001).

In an earlier use of (2), Whittaker (1923) and Henderson (1924) posed the minimization problem when smoothing actuarial data with μ = 0 and d = 2 or d = 3. When data is not equidistant, the problem has also arisen in a more general context, known as smoothing spline functions; see Wahba (1990).

The problem behind the HP filter gets solved by finding the vector τ that minimizes the function

$$M ( \lambda ) = ( \mathbf y - \tau ) ^ { \prime } ( \mathbf y - \tau ) + \lambda ( K _ { 2 } \tau ) ^ { \prime } ( K _ { 2 } \tau ) ,$$

with y = ( y 1 , . . . , yN ) ′ and τ = (τ 1 , . . . , τ N ) ′ . Where λ is fixed and K 2 is the matrix representation of the second-order difference operator, defined as the following matrix of size ( N - 2 ) × N

The solution is given by

where

is known as the smoothing matrix.

Ageneralsolution for the minimization problem (2) with d ≥ 0and μ = 0is found in Kitagawa and Gersch (1996), where it is focused from a least squares computational perspective. Instead, King and Rebelo (1993) employed optimal linear filtering tools to obtain essentially the same results for d = 1 and d = 2. A slightly more general solution was given by Guerrero (2007), where μ ̸= 0 was considered in problem (2).

$$K _ { 2 } = \begin{pmatrix} 2 ) \times N & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

$$\widehat { \tau } = S _ { \lambda } y$$

$$S _ { \lambda } = ( I _ { N } + \lambda K _ { 2 } ^ { \prime } K _ { 2 } ) ^ { - 1 }$$


<!-- p:4 -->


and

The solution found by PLS for d = 2 keeps a close resemblance with the smoothing cubic spline estimator, since the function to be minimized within a cubic spline context is

$$\sum _ { i = 1 } ^ { N } \{ y _ { i } - \widehat { f } ( x _ { i } ) \} ^ { 2 } + \lambda \int _ { a } ^ { b } \{ \widehat { f } ^ { ( 2 ) } ( x ) \} ^ { 2 } d x, \text { with } \lambda > 0 , \\ \intertext { f i s an unknown regression function to be estimated from the pairs of observations }$$

where f is an unknown regression function to be estimated from the pairs of observations ( xi , yi ) , i = 1 , . . . , N , related as

$$y _ { i } = f ( x _ { i } ) + \epsilon _ { i } , \text { with } E ( \epsilon _ { i } ) = 0$$

$$f ( x ) = E ( y | x ) , \\$$

while the ε i are independent random errors with common variance σ 2 .

Weinert (2012) developed algorithms to calculate the smoothing cubic spline based on Cholesky's decomposition and considered the function (2) with d = 2 and μ = 0, as a discretization of (6). This fact turns out to be important, since the usual methods to choose the smoothing parameter have been developed in the context of splines. Such is the case of Cross Validation (CV) and Generalized Cross Validation (GCV), introduced by Craven and Wahba (1979). The said methods propose to choose the smoothing parameter by minimizing a criterion that approximates the Mean Square Error (MSE). Other criteria commonly used to select the smoothing parameter are: Akaike Information Criterion (AIC; see Akaike 1973), its biascorrected version (AICc) proposed by Hurvich et al. (1998), and the Bayesian Information Criterion (BIC; see Schwarz 1978). These methods will be briefly described in the following section.

Guerrero (2007) proposed to follow a controlled smoothness approach with the aid of an index that measures smoothness and serves to choose the smoothing parameter. The smoothness index can be expressed as a percentage and is interpreted as a desired percentage of smoothnessfortheestimated trend; this method offers flexibility to the user, since the smoothness index depends only on the number of observations and the smoothing parameter.

The objective of this article is to analyze the effects of some factors assumed to affect the smoothing parameter selection, in terms of the smoothness attained by the aforementioned methods within the context of PLS, that is, CV , GCV , AICc, and BIC. Four factors are considered, with two levels each: (1) type of trend (linear or nonlinear); (2) seasonality in the series (absent or present); (3) variability of the data (high or low); and (4) number of observations (small sample or large sample). Several time series are simulated based on the additive decomposition model, reproducing all possible combinations that the factors and their levels can take on. Afterwards, the CV , GCV , AICc, and BIC methods are used in the context of PLS to choose the smoothing parameter, and the corresponding smoothed series is then obtained. The experiment carried out is a 2 4 factorial design with one and two replicates for each method, and the response variable is the smoothness achieved, as measured by the smoothness index. Thus, this work is motivated by the idea of measuring smoothness, since the methods for choosing the smoothing parameter have already been studied and compared in other contexts, e.g., Aydin and Tuzemen (2012) and Lee (2003).

This article is organized as follows. Section 2 presents the methods used for choosing the smoothing parameter, while Section 3 is devoted to the specification of the simulated time series, the implementation of the methods in the PLS context, and to describe the factorial design. The results of the analysis and some graphical summaries are included in Section 4.


<!-- p:5 -->


Finally, Section 5 presents some conclusions; for instance: all interactions among the factors were insignificant, so that the main effects can be interpreted in a direct and easy way. The type of trend was found significant at the 1% level and its effect diminishes the smoothness whenmovingfromlinear to nonlinear. The sample size was also significant at the 1% level and smoothness increases when the sample size grows larger. Seasonality was significant at the 5% level and its effect increases the amount of smoothness. The variability effect was insignificant even at the 10% level.

## 2. AReview of methods to choose the parameter λ

The smoothing parameter λ plays a fundamental role in the solution of the PLS problem, because it serves to trade off goodness of fit to the observed data against trend smoothness, in such a way that the estimated trend depends to a great extent on the selection of that parameter. The range of possibilities for choosing the smoothing parameter is wide and here we briefly describe some of the most frequently used methods. We start with the controlled smoothness method and then present some methods that could be considered as classical, within the context of splines: CV , GCV , AIC, AICc, and BIC. Later on, the AIC method will be discarded because it did not produce reliable results in some situations.

### 2.1. Controlled smoothness approach

Guerrero (2007) presented a method to estimate trends within the PLS framework, allowing the user to impose beforehand a desired percentage of smoothness for the trend. A smoothness index related in a direct way with the parameter λ is first defined, then by fixing the percentage of smoothness we implicitly select the value of the smoothing parameter. The smoothness index is given by

$$\text {thickness index is given by} & & \left \{ \lambda ( 1 + \lambda ) ^ { - 1 } & \text { if } d = 0 \\ S _ { d } ( \lambda ; N ) = \begin{cases} \lambda ( 1 + \lambda ) ^ { - 1 } & \text { if } d = 0 \\ 1 - t r [ ( I _ { N } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } ] / N & \text { if } d \geq 1 \\ \end{cases} \\ \intertext { t r ( \cdot ) denotes the trace of a matrix. } \text {is index depends only on the values of } \lambda \text { and } N , \text { since } d \text { is supposed to be fixed before}$$

where tr ( · ) denotes the trace of a matrix.

This index depends only on the values of λ and N , since d is supposed to be fixed beforehand, for example d = 2 with the HP filter that will be considered in the simulation study. Notice that Sd (λ ; N ) → 0 when λ → 0 and Sd (λ ; N ) → 1 - d N when λ →∞ ; this result follows by expressing the trace involved in (9) as a function of the eigenvalues of K ′ d Kd , d of which are zero, as shown by Eilers and Marx (1996). Therefore, given a value of λ we can calculate the amount of smoothness to be achieved with that selection. The index expressed in percentage terms is interpreted as a percentage of smoothness; thus the value of λ can be decided by first fixing a desired percentage of smoothness and then obtaining λ as the value that satisfies such a condition.

To deduce the smoothness index, Guerrero (2007) employed the statistical solution presented next for the PLS problem. Consider the following model for { τ t }

$$\nabla ^ { d } \tau _ { t } & = \mu + \varepsilon _ { t } \text { for } t = d + 1 , \dots , N , \\ \\ \intertext { t h e r } \varphi & = \begin{matrix} \nabla ^ { d } \tau _ { t } = \mu + \varepsilon _ { t } \text { for } t = d + 1 , \dots , N , \\ \end{matrix}$$

with { ε t } a sequence of noncorrelated random errors, identically distributed with mean zero and Var (ε t ) = σ 2 ε .

The following arrays are defined: Z = ( Z 1 , . . . , ZN ) ′ , τ = (τ 1 , . . . , τ N ) ′ , and η = (η 1 , . . . , η N ) ′ ; these are N × 1 vectors. ε = (ε d + 1 , . . . , ε N ) ′ and 1 N - d = ( 1 , . . . , 1 ) ′ are


<!-- p:6 -->


( N - d ) × 1 vectors and Kd is the matrix representation of the difference operator ∇ d , given by

$$K _ { d } = \left ( \begin{array} { c c c c } 0 & & k _ { d } & & 0 _ { N - d - 1 } \\ & & & k _ { d } & 0 _ { N - d - 2 } \\ & & 0 _ { N - d - 1 } & & k _ { d } \end{array} \right ) .$$

$$k _ { d } = \left ( ( - 1 ) ^ { d } \left ( \begin{matrix} d \\ d \end{matrix} \right ) , ( - 1 ) ^ { d - 1 } \left ( \begin{matrix} d \\ d - 1 \end{matrix} \right ) , \dots , ( - 1 ) \left ( \begin{matrix} d \\ 1 \end{matrix} \right ) , \left ( \begin{matrix} d \\ 0 \end{matrix} \right ) \right )$$

This is a matrix of size ( N - d ) × N , with k d the 1 × ( d + 1 ) vector given by

whose elements are binomial coefficients, i.e., ( d i ) = d ! / [ ( d - i ) ! i !] for i = 0 , ..., d and 0 m is a zero vector of size m × 1.

The vector of observed data Z can be expressed as follows:

$$Z & = \tau + \eta , \\$$

where the trend component is represented by

$$K _ { d } \tau = \mu 1 _ { N - d } + \varepsilon , \\$$

with μ a scalar that denotes the level of the differenced trend, while η and ε are random vectors with E ( η ) = 0 N , Var ( η ) = σ 2 η V , E ( ε ) = 0 N - d , Var ( ε ) = σ 2 ε IN - d , and E ( ηε ′ ) = 0, where V is a known symmetric positive definite matrix.

The linear estimator, with minimum MSE of the trend, is given by

with MSE matrix

$$\widehat { \tau } = ( V ^ { - 1 } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } ( V ^ { - 1 } Z + \lambda \mu K _ { d } ^ { \prime } \mathbf 1 _ { N - d } ) , \\ \text {matrix} \\ \Sigma \equiv \sigma ^ { 2 } ( V ^ { - 1 } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 }$$

$$\Sigma = \sigma _ { \eta } ^ { 2 } ( V ^ { - 1 } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } , \\ \intertext { \Sigma } \Sigma = \sigma _ { \eta } ^ { 2 } ( V ^ { - 1 } + \lambda K _ { d } ^ { \prime } K _ { d } ) ^ { - 1 } , \\$$

where λ = σ 2 η /σ 2 ε , as shown by Guerrero (2007). Moreover, the precision matrix of ̂ τ can be written as

$$\Sigma ^ { - 1 } = \sigma _ { \eta } ^ { - 2 } V + \sigma _ { \varepsilon } ^ { - 2 } K _ { d } ^ { \prime } K _ { d } , \\ \\ \sigma _ { \varepsilon } + \sigma _ { \eta } = \sigma _ { \eta } ^ { - 1 } V + \sigma _ { \varepsilon } ^ { - 2 } K _ { d } ^ { \prime } K _ { d } ,$$

where we see that total precision is the sum of two precision matrices, σ - 2 η V associated with model (11) for the observations and σ - 2 ε K ′ d Kd associated with model (12) for the smoothness component of the series. From (15) it is possible to measure the proportion of precision attributable to the smoothness component, with respect to total precision. This can be done with the aid of an index originally derived by Theil (1963) to quantify the proportion of a matrix P in ( P + Q ) - 1 , where P and Q are positive definite matrices of size N × N . The resulting measure is

$$\Lambda ( P ; P + Q ) = t r [ P ( P + Q ) ^ { - 1 } ] / N . \\$$

Theil demonstrated that this measure of relative precision takes on values in the interval [0,1], is invariant under linear nonsingular transformations of the variable involved, it behaves linearly, and Lambda1( P ; P + Q ) + Lambda1( Q ; P + Q ) = 1.

The smoothness index (9) has been used to select the smoothing parameter when estimating trends for economic time series in Guerrero (2008) and for financial time series in Guerrero and Galicia-Vázquez (2010).


<!-- p:7 -->


### 2.2. Choosing the smoothing parameter in the context of splines

There is a vast bibliography on the topic of splines, e.g., Wahba (1990) and Green and Silverman (1994), among others. The methods for choosing the smoothing parameter, presented next, were introduced and are mainly implemented in the context of smoothing splines.

####### ... Cross validation and generalized cross validation

Craven and Wahba (1979) introduced CV and GCV for smoothing cubic splines, where λ is selected in such a way that the Residual Sum of Squares (RSS) is minimized. Thus, the CV and GCV seek to minimize the following score functions of λ ,

$$C V ( \lambda ) = \sum _ { i = 1 } ^ { N } \left ( \frac { y _ { i } - \widehat { f } ( x _ { i } ) } { 1 - S _ { \lambda , i i } } \right ) ^ { 2 } \\ \sum _ { i = 1 } ^ { N } \left ( \sum _ { \nu _ { i } = \widehat { f } ( x _ { i } ) } \widehat { x } _ { i } \right ) ^ { 2 }$$

$$\frac { \sum _ { i = 1 } ^ { N } \left ( 1 - S _ { \lambda , i i } \right ) } { G C V ( \lambda ) = \sum _ { i = 1 } ^ { N } \left ( \frac { y _ { i } - \widehat { f } ( x _ { i } ) } { 1 - N ^ { - 1 } t r ( S _ { \lambda } ) } \right ) ^ { 2 } , } \\ \intertext { i t h a n t r y i n g t h e d i m a l o f t h e a m o o t h i n g m a t r i v i n g o w n o n d i n g t o ( F ) }$$

where S λ, ii is the i th entry in the diagonal of the smoothing matrix corresponding to (5), for the case of splines, i.e.,

$$S _ { \lambda } = ( I _ { N } + \lambda K _ { 2 } ^ { \prime } P ^ { \prime } K _ { 2 } ) ^ { - 1 } ,$$

where P is a Toeplitz tridiagonal symmetric matrix, with values 2/3 and 1/6 in the diagonal and subdiagonal, respectively.

####### ... Akaike, corrected akaike, and bayesian information criteria

AIC and BIC are similar in form and both try to achieve a balance between the logged RSS and the degrees of freedom, which are penalized differently by each method. They search for the smoothing parameter that minimizes the following functions:

$$A I C ( \lambda ) & = \log \{ R S S ( \lambda ) \} + 2 d f ( \lambda ) / N , \\ B I C ( \lambda ) & = \log \{ R S S ( \lambda ) \} - \log ( N ) + d f ( \lambda ) \log ( N ) / N$$

$$B I C ( \lambda ) = l o g \{ R S S ( \lambda ) \} - l o g ( N ) + d f ( \lambda ) l o g ( N ) / N ,$$

where log denotes natural logarithm and

$$R S S ( \lambda ) = \sum _ { i = 1 } ^ { N } \{ y _ { i } - \widehat { f } ( x _ { i } ; \lambda ) \} ^ { 2 } \\ \text {g the nonparametric estimation at the point}$$

with ̂ f ( xi ; λ) representing the nonparametric estimation at the point xi that arises when using λ , whereas d f (λ) denotes the degrees of freedom of the smoothing, i.e., the trace of the smoothing matrix (5).

Abias corrected form of the AIC criterion leads to AICc, which corrects the penalization of the AIC to adjust it for bias. Hurvich et al. (1998) demonstrated the superiority of AICc over AICinsmall samples and justified the use of AICc for nonlinear regression and autoregressive models; see also Cavanaugh (1997). The score function to be minimized now is

$$A I C c ( \lambda ) = \log \{ R S S ( \lambda ) \} + \frac { 2 d f ( \lambda ) + 1 } { N - d f ( \lambda ) - 2 } .$$


<!-- p:8 -->

## 3. Asimulation study with emphasis on smoothness

This section describes the model specifications considered by the simulations. The computational implementation was carried out in R.

### 3.1. Time series simulation

The time series were simulated with an additive decomposition model of type (1). The linear trend was generated as

$$\tau _ { t } = \frac { 4 t } { N } , \ t = 1 , \dots , N ,$$

while the nonlinear trend function was

$$\tau _ { t } = 0 . 6 \beta _ { 3 0 , 1 7 } ( t ) + 0 . 4 \beta _ { 3 , 1 1 } ( t ) , \ 0 \leq t \leq 1 , \\ \Gamma ( p + q ) _ { t } = 1 + \dots + 1$$

The nonlinear function (24) was used originally by Wahba (1985) in her simulation study with splines, and it was used also by Krivobokova (2013) for the study and comparison of the asymptotic properties of two particular smoothing parameter estimators for penalized splines. The linear trend function was chosen in such a way that it produces a range of values similar to that of the nonlinear function. The range of 'time' values was obtained by partitioning the interval [0,1] into N parts. Seasonality in the series was included with the following function:

where β p , q ( t ) = Gamma1( p + q ) Gamma1( p )Gamma1( q ) t p - 1 ( 1 - t ) q - 1 , 0 ≤ t ≤ 1.

$$\xi _ { t } = D _ { 1 , t } - 0 . 5 D _ { 2 , t } - 2 . 5 D _ { 3 , t } + 2 D _ { 4 , t } , \\ \\ \ t a l _ { 0 } + \ t a l _ { 1 } = D _ { 1 , t } - 0 . 5 D _ { 2 , t } - 2 . 5 D _ { 3 , t } + 2 D _ { 4 , t } ,$$

where Di , t = 1 if t = i , 4 + i , 8 + i , . . . and Di , t = 0 otherwise, for i = 1 , . . . , 4, trying to resemble a quarterly time series.

We should recall that the smoothing method presupposes that there is no seasonality in the series, so that the presence of seasonality can be interpreted as a misspecification in the underlying model of the smoothing technique. We consider this fact as a realistic possibility when working with observed series, since the absence of seasonality should be considered an assumption, not a given fact. So, by considering the seasonality in the simulated series we have the opportunity to verify the robustness of the method against this misspecification error.

Two levels were considered for the variability of the data, the low level with σ = 0 . 5 and the high level with σ = 2. In the same way, for the length of the series we considered two levels; low level with sample size N = 50 and the high level with N = 200.

### 3.2. Implementation of CV, GCV, AICc, and BIC methods with PLS

The CV and GCV methods are already implemented in various softwares within the context of splines and it is easy to use them for estimating trends. For instance, the algorithms implemented by Weinert (2012) to solve the PLS problem in its discrete and continuous versions are programmed in MATLAB (R2012a, 64 bit) and allow for selection of the smoothing parameter with GCV. One can also find various packages in R that include functions to smooth curves through splines, e.g., 'pspline, ' 'stats, ' and 'assist, ' among others. These packages include such functions as 'sm.spline' , 'smoothing.spline' , and 'ssr' , respectively, allowing for the fitting of curves by means of smoothing cubic splines and choosing the smoothing parameter by means of GCV or CV. The use of these already implemented algorithms is not convenient for our study because, on the one hand, in the splines context the estimated trend minimizes expression (6), not the appropiate one for PLS, which is given by (2) with d = 2 and μ = 0. On


<!-- p:9 -->

(a)AIC score function Lambda

(b)AICe score function

Figure . Score functions of AIC and AICc.

the other hand, the algorithms carry out the estimation and produce the degrees of freedom, but tend to round this number, so that it cannot be transformed into an appropriate amount of attained smoothness. Thus, we decided to implement the methods in the context of PLS explicitly.

To implement CV, GCV, AICc, and BIC in the context of PLS, expression (5) was used to calculate the trace of the smoothing matrix in the respective score functions. The AIC criteria was also implemented in the context of PLS; nevertheless, it produced several unreliable results that prevented us from using it to smooth some of the simulated series. This problem could be due to the fact that the command used to minimize the score function requires an initial approximation, and the score function of the AIC sometimes reaches its maximum for a very small value of λ , as seen in Fig. 1, while this defective behavior is corrected by the AICc.

### 3.3. Statistical analysis of the 2 4 factorial design

The experiment was carried out with a 2 4 factorial design model, that is,

$$T _ { i j k l m } = \theta _ { i j k l } + \gamma _ { i j k l m } , \text { with } \gamma _ { i j k l m } \sim i i d \ N ( 0 , \sigma _ { \gamma } ^ { 2 } )$$

with m replicates and where iid stands for independent and identically distributed.

The response variable is the smoothness index transformed to avoid its boundedness, since it lies between 0 and 1. The transformation employed was the logit that transforms the interval (0,1) into the whole real line. Thus, the response variable Tijklm is given by

$$T ( \lambda ; N ) = \log \left [ \frac { S _ { 2 } ( \lambda , N ) } { 1 - S _ { 2 } ( \lambda , N ) } \right ] = \log \left [ \left ( \frac { N - d f ( \lambda ) } { d f ( \lambda ) } \right ) \right ] , \\ \intertext { r e d f ( \lambda ) is the number of degrees of freedom used to estimate the trend for each simulated }$$

where df (λ) is the number of degrees of freedom used to estimate the trend for each simulated series. We also have

$$\theta _ { i j k l } & = \beta _ { 0 } + \beta _ { 1 } X 1 _ { i } + \dots + \beta _ { 4 } X 4 _ { l } + \beta _ { 5 } X 5 _ { i j } + \dots + \beta _ { 1 0 } X 1 0 _ { k l } \\ & \quad + \beta _ { 1 1 } X 1 1 _ { i j k } + \dots + \beta _ { 1 4 } X 1 4 _ { i k l } + \beta _ { 1 5 } X 1 5 _ { i j k l } , \\ \dots & \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \quad \dots \qu$$

with the variable specification shown in Table 1 and where the β ' s are parameters to be estimated by Ordinary Least Squares.


<!-- p:10 -->

Table . Factors and levels used in the 2 4 factorial design.

| Factors                      | Low level -    | High level    |
|------------------------------|-----------------|----------------|
| X 1 : Trend                  | Linear          | Nonlinear      |
| X 2 : Seasonality            | Absent          | Present        |
| X 3 : Variability            | σ = 0 . 5       | σ = 2          |
| X 4 : Number of observations | N =           | N =         |

We specify the following interactions, first order: X 5 i j = X 1 iX 2 j , . . . , X 10 kl = X 3 kX 4 l ; second order: X 11 i jk = X 1 iX 2 jX 3 k , . . . , X 14 jkl = X 2 jX 3 kX 4 l ; and third order: X 15 i jkl = X 1 iX 2 jX 3 kX 4 l . To interpret the estimated effects we require to transform back the estimated values from the logit scale to the original scale of the smoothness index. The inverse transformation of (26) becomes

Figure . Half normal plot for the effects.

<!-- p:11 -->


Table . Estimation results of 2 4 factorial analysis for CV and GCV.

| Type of effect Average   | CV - Estimate .   | CV - t statistic . ∗∗   | GCV - Estimate .   | GCV - t statistic . ∗∗   |
|--------------------------|------------------------|-----------------------------|-------------------------|------------------------------|
| X 1                      | - .               | - . ∗∗                  | - .                | - . ∗∗                   |
| X 2                      | .                 | . ∗                      | .                  | . ∗                       |
| X 3                      | .                 | .                        | .                  | .                         |
| X 4                      | .                 | . ∗∗                     | .                  | . ∗∗                      |
| X 5                      | - .               | - .                      | - .                | - .                       |
| X 6                      | .                 | .                        | .                  | .                         |
| X 7                      | .                 | .                        | .                  | .                         |
| X 8                      | - .               | - .                      | - .                | - .                       |
| X 9                      | .                 | .                        | .                  | .                         |
| X 10                     | - .               | - .                      | - .                | - .                       |
| X 11                     | -.                | - .                      | - .                | - .                       |
| X 12                     | - .               | - .                      | - .                | - .                       |
| X 13                     | - .               | - .                      | - .                | - .                       |
| X 14                     | - .               | - .                      | - .                | - .                       |
| X 15                     | - .               | - .                      | - .                | - .                       |

$$\widehat { S } _ { 2 } ( \lambda ; N ) = e ^ { \widehat { T } ( \lambda ; N ) } / ( 1 + e ^ { \widehat { T } ( \lambda ; N ) } ) . \\$$

## 4. Experimental results

Apreliminary analysis was carried out without replication and deciding statistical significance visually by comparing the estimated effects with a half normal plot, as shown in Fig. 2. In that figure we appreciate that the effects of X 1 (trend) and X 4 (number of observations) are evidently different from zero, and perhaps the effect associated to X 2 (seasonality) too, while no interaction is seen to have a notorious effect.

Since the 2 4 factorial design is supported by a linear model with 16 parameters, we performed the analysis again with two replicates, so that 32 observations were available for parameter estimation. Besides, now we are able to estimate the variance σ 2 γ and therefore calculate standard errors of the estimates to assign statistical significance. The results were basically the same as those obtained without replication and we decided that two replicates were enough to justify our conclusions. The results for each of the four methods entertained are summarized in Tables 2-5. We used the lm' function of the 'stats' package implemented in R to perform the numerical computations.

Tables 2-5 use the notation of Table 1, with reference to model (27). We should notice that the t statistic is the ratio of the estimated effect divided by its standard error and its significance is denoted by: ∗∗ 1%, ∗ 5%, and · 10%.

Table . Results of the reduced 2 4 factorial analysis for CV and GCV.

| Type of effect Average   | CV - Estimate .   | CV - t statistic . ∗∗   | GCV - Estimate .   | GCV - t statistic . ∗∗   |
|--------------------------|------------------------|-----------------------------|-------------------------|------------------------------|
| X 1                      | - .               | - . ∗∗                  | - .                | - . ∗∗                   |
| X 2                      | .                 | . ∗                      | .                  | . ∗                       |
| X 4                      | .                 | . ∗∗                    | .                  | . ∗∗                     |


<!-- p:12 -->

Table . Estimation results of the 2 4 factorial for AICc and BIC.

| Type of effect Average   | AICc - Estimate .   | AICc - t statistic . ∗∗   | BIC - Estimate .   | BIC - t statistic . ∗∗   |
|--------------------------|--------------------------|-------------------------------|-------------------------|------------------------------|
| X 1                      | - .                 | - . ∗∗                    | - .                | - . ∗∗                   |
| X 2                      | .                   | . ∗∗                       | .                  | . ∗                       |
| X 3                      | .                   | .                          | .                  | .                         |
| X 4                      | .                   | . ∗∗                       | .                  | · . ∗∗                   |
| X 5                      | .                   | .                          | .                  | . ∗                       |
| X 6                      | .                   | . ·                        | .                  | . ∗                       |
| X 7                      | - .                 | - .                        | - .                | - .                       |
| X 8                      | .                   | .                          | - .                | - .                       |
| X 9                      | .                   | .                          | - .                | - .                       |
| X 10                     | - .                 | - .                        | - .                | - .                       |
| X 11                     | - .                 | - .                        | - .                | - .                       |
| X 12                     | - .                 | - .                        | - .                | - .                       |
| X 13                     | - .                 | - .                        | - .                | - .                       |
| X 14                     | - .                 | - .                        | - .                | - .                       |
| X 15                     | - .                 | - .                        | - .                | - .                       |

In Table 2 we can see that with the CV and GCV methods, none of the interactions turned out to be significant at the 10% level; therefore, it is adequate to interpret the main effects individually. To that end, we considered the estimated effects of the reduced model shown in Table 3, that only considers the significant effects, and brought these values back to the smoothness scale. The average values for CV and GCV (2.9975 and 2.9965, respectively) are transformed into average percentages of smoothness of 95.25% for CV and 95.24% for GCV . The 1% significant main effects are type of trend and number of observations and the 5% significant main effect is seasonality. For the type of trend, smoothness decreases with both methods when the model changes from linear to nonlinear; the change from 50 to 200 observations results in an increment of smoothness and the presence of seasonality in the series causes an increase of smoothness. These effects can be interpreted in terms of percentage of smoothness when they are related to models (25)-(27).

To measure the change in the percentage of smoothness when going from a low level to a high one in the trend factor, in seasonality and the number of observations, we calculated the difference between the percentage of smoothness for the high and low levels of each factor. For example, to measure the increase in smoothness by changing from N = 50 to N = 200 observations with the CV method, we first calculated the effects in the logit scale, that is, 2 . 9975 - 0 . 6176 = 2 . 3799 and 2 . 9975 + 0 . 6176 = 3 . 6151, then by transforming theses values to the smoothness scale we obtained the following percentages of smoothness: 91.53% and 97.38%. The difference between these percentages provides the increase in smoothness attributable to increasing the number of observations from 50 to 200. In the CV and GCV

Table . Results of the reduced 2 4 factorial analysis for AICc and BIC.

| Type of effect Average   | AICc - Estimate .   | AICc - t statistic . ∗∗   | BIC - Estimate .   | BIC - t statistic . ∗∗   |
|--------------------------|--------------------------|-------------------------------|-------------------------|------------------------------|
| X 1                      | - .                 | - . ∗∗                    | - .                | - . ∗∗                   |
| X 2                      | .                   | . ∗∗                       | .                  | . ∗                       |
| X 4                      | .                   | . ∗∗                       | .                  | . ∗∗                     |
| X 5                      | -                        | -                             | .                  | . ∗                       |
| X 6                      | -                        | -                             | .                  | . ·                       |


<!-- p:13 -->


Figure . Time series with linear trend. Method to choose λ : CV.

cases, this increase was of 5.8 percentage points. In a similar way, the increased smoothness produced by the seasonality factor was of 1.4 percentage points. The reduction of smoothness by changing from a linear model to a nonlinear one is of 6.7 percentage points in both methods. In Table 4, we see that the interaction between type of trend and variability for the AICc is significant at the 10% level but we did not consider such an interaction relevant. With BIC the effect of two interactions appear to be significant at the 5% level (trend with seasonality and trend with variability); nonetheless, the variability effect is significant just at the 10% level individually, while seasonality would be significant at the 5% level. Thus, we did not consider trend with variability as an interaction truly significant. Therefore, for both methods, the effects that we interpreted individually are the number of observations and type of trend, both significant at the 1% level.

<!-- p:14 -->

Figure . Time series with nonlinear trend. Method to choose λ : CV.

<!-- p:15 -->


From the reduced model results shown in Table 5, we calculated as before the average values of the percentages of smoothness produced by the AICc and BIC methods: 95.73% and 96.37%, respectively (corresponding to the average estimates 3.1111 and 3.2777). Then by increasing the observations from 50 to 200, smoothness increases 4.4 and 4.6 percentage points for AICc and BIC, respectively, while the presence of seasonality increases 1.6 and the type of trend decreases 5.4 percentage points from linear to nonlinear for AICc.

### 4.1. Someillustrative time series smoothed with λ chosen by CV

The graphs presented here allow us to visualize the effect of the number of observations and the type of trend, both factors with significant effects at the 1% level. The latter factor is irrelevant in practice, since there is nothing we can do to control for this factor during the smoothing process. Nevertheless, we should be aware that higher percentages of smoothness can be attained when the time series under study shows a linear rather than a nonlinear behavior. Just for illustrative purposes, we only present graphs for the CV method that produces the lowest smoothness of the four methods entertained.

Plots (a),(b) and (c),(d) in Figs. 3 and 4 illustrate the increase in smoothness corresponding to an increase in the number of observations from 50 to 200, in series with the same kind of trend, same conditions of seasonality, and same standard deviation. The estimated trend is greatly improved in all cases. Let us notice that when the trend, seasonality, and number of observations are fixed at a given level (low or high), and the standard deviation is changed, the smoothness does not present a clear pattern. This fact corroborates the numerical results shown in Tables 2 and 4, so that variability does not affect smoothness significantly.

Thus, we obtained the following main results: smoothness gets larger when the number of observations increases; it gets smaller when moving from a linear to a nonlinear type of trend for the series; to a lesser degree, the presence of seasonality increases the amount of smoothness; and the variability of the observed time series does not affect the estimated trend smoothness.

It turns out that CV produces on average around 95% smoothness for series with linear trends and N = 50, which increases to 98% when N = 200. While for nonlinear trends and N = 50, the smoothness attained is about 86%, which increases approximately to 95% when N = 200. In similar fashion, BIC produces on average almost 96% smoothness when the trend is linear and N = 50, increasing to 99% when N = 200. Moreover, for nonlinear trends, the smoothness reduces to about 89% when N = 50 and to 96% when N = 200. This is a useful finding for analysts that want to use the controlled smoothness approach, since we can set in advance a desired percentage of smoothness around these values in order to produce comparable trends for different datasets, depending on the type of trend and sample size of the time series.

## 5. Conclusions

Out of the methods used here to choose the smoothing parameter, we can say that on average CV and BIC provide the lowest and highest smoothness for the trend, respectively. CV and GCVproduced in most cases approximately the same smoothness, while AICc and BIC vary a little more in the amount of smoothness of the estimated trends. The four methods are relatively easy to implement and they are already implemented in packages such as R or MATLAB, although in some cases the results provided are not exact. Rounding the number of degrees of freedom to the nearest digit tends to distort the corresponding amount of smoothness.


<!-- p:16 -->


From the results obtained with the factorial experimental design we conclude that the significant factors at the 1% level are only type of trend and number of observations. The trend effect decreases the amount of smoothness when changing from a linear to a nonlinear type of trend, while an increase in smoothness is observed when the number of observations changes from 50 to 200. Seasonality was significant at the 5% level and its presence causes an increase in smoothness. Finally, no significant effect attributable to variability was found and therefore, we conclude that it does not play a role in the amount of smoothness provided by each technique. This may be explained by the fact that the variability effect is implicitly taken into account by the smoothing parameter, since this parameter can be interpreted as a noise to signal variance-ratio.

Finally, the main conclusion is that the number of observations is the main factor affecting the amount of smoothness for each of the four methods used to select the smoothing parameter. This is useful because we can anticipate the effect of this factor before smoothing a time series. Moreover, this result lends empirical support to the use of the smoothness index associated with the controlled smoothness approach, since such an index depends basically on the sample size. A future investigation should analyze how much smoothness is obtained when the number of observations is increased, not just by considering two levels of sample size.

## Funding

Daniela Cortés-Toto thanks CONACYT for financial support to this work (Scholarship application: 231040), and Julián Francisco Ariza for his support in the computational part. Víctor M. Guerrero thanks Asociación Mexicana de Cultura A.C. for the support granted to work in this project.
