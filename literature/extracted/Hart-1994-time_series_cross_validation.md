---
id: "Hart-1994-time_series_cross_validation"
source_pdf: "../pdf/Hart-1994-time_series_cross_validation.pdf"
source_filename: "Hart-1994-time_series_cross_validation.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/Hart-1994-time_series_cross_validation.references.md"
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
