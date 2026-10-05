---
id: "Kitagawa-2003-smoothness_prior_large_scale_time_series"
source_pdf: "../pdf/Kitagawa-2003-smoothness_prior_large_scale_time_series.pdf"
source_filename: "Kitagawa-2003-smoothness_prior_large_scale_time_series.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/Kitagawa-2003-smoothness_prior_large_scale_time_series.references.md"
---

<!-- p:1 -->

Theoretical Computer Science 292 (2003) 431-446

##### Theoretical Computer Science

www.elsevier.com/locate/tcs

## Smoothness prior approach to explore mean structure in large-scale time series

Genshiro Kitagawa, Tomoyuki Higuchi ∗ , Fumiyo N. Kondo

The Institute of Statistical Mathematics, 4-6-7 Minami-Azabu, Minato-ku, Tokyo 106-8569 Japan

##### Abstract

This article is addressed to the problem of modeling and exploring mean value structure of large-scale time series data and time-space data. A smoothness prior modeling approach (Smoothness Prior Analysis of Time Series, Lecture Notes in Statistics, vol. 116, Springer, New York, 1996.) is taken. In this approach, the observed series are decomposed into several components each of which are expressed by smoothness priors models. In the analysis of POS and GPS data, various useful information were extracted by this decomposition, and result in discoveries in these areas. c © 2002 Elsevier Science B.V. All rights reserved.

Keywords: Smoothness priors; State space model; Time series; Space-time data; Data mining; Seasonal adjustment; POS; GPS

### 1. Introduction

In statistical information processing, introduction of the information criterion AIC [1,20] facilitated to compare various types of statistical models freely and changed the conventional paradigm of statistical research which consisted of estimation and statistical test. It revealed the importance of proper statistical modeling, and the use of parametric models become very popular since then [4,14]. AIC criterion suggests that if the available data set is short, we have to use simpler model to obtain reliable information from that data. However, by the progress of various measuring devices, it has become possible to use huge amount of data in various FFelds of sciences and societies. In this situation, a more important problem is to extract useful information from huge

∗ Corresponding author.

E-mail addresses: kitagawa@ism.ac.jp (G. Kitagawa), higuchi@ism.ac.jp (T. Higuchi), kondo@ism.ac.jp

(F.N. Kondo).

URL:

http://www.ism.ac.jp


<!-- p:2 -->


amount of data, which is diSOcult to achieve by a simple parametric model. Namely, in this situation, modeling with small number of parameters is sometimes inadequate and a more CRexible tool for extracting useful information from data is necessary.

In an analysis of input-output relationship of econometric time series, Shiller [21] introduced the notion of 'smoothness priors', and considered constrained least-squares problem. A similar concept has already appeared in Whittaker [23] addressing a problem of the estimation of a smooth trend. The trade-oVT parameters were determined subjectively until Akaike [2,3] proposed the method of choosing the trade-oVT parameters or hyperparameters in a Bayesian framework, by maximizing the likelihood of a Bayes model [18]. The calculation of the likelihood of a Bayes model for time series requires intensive computation, the burden of which Gersch and Kitagawa [6] eased by employing a state space representation of the model and recursive algorithm of Kalman FFltering [11].

In this paper, we will present applications of this smoothness priors approach for exploring large-scale time series data or space-time data. SpeciFFcally, we consider the point of sales (POS) scanner data and global positioning system (GPS) data, because automatic transaction of these data is one of the most attractive and potential targets in statistical science. By the analyses of these data, it will be shown that by removing trend and seasonal components by a proper smoothness prior modeling, useful information such as the trading day eVTect (for economic data), competitive relation (for POS data) and local CRuctuation associated with an atmospheric condition (for GPS) are discovered.

### 2. Smoothness prior modeling

#### 2.1. Flexible semi-parametric modeling

A smoothing approach attributed to [23], is as follows: Let

$$y _ { n } = f _ { n } + \varepsilon _ { m } , \ \ n = 1 , \dots , N$$

denote observations, where fn is an unknown smooth function of n , and SI n is an independently identically distributed (i.i.d.) normal random variable with zero mean and unknown variance ESC 2 . The problem is to estimate fn; n =1 ; : : : ; N from the observations, yn; n =1 ; : : : ; N , in a statistically sensible way. Here the number of parameters to be estimated is equal to the number of observations. Therefore, the ordinary least-squares method or the maximum likelihood method yield meaningless results. Whittaker [23] suggested that the solution fn; n =1 ; : : : ; N balances a tradeoVT between inFFdelity to the data and inFFdelity to a k th order diVTerence equation constraint. Namely, for FFxed values of NAK 2 and k , the solution satisFFes

$$\min _ { f } \left [ \sum _ { n = 1 } ^ { N } \left ( y _ { n } - f _ { n } \right ) ^ { 2 } + \lambda ^ { 2 } \sum _ { n = 1 } ^ { N } \left ( \Delta ^ { k } f _ { n } \right ) ^ { 2 } \right ] . \\ \\ \text {The first term in the} \, \phi \text { is} \, \text { } \phi \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \$$

The FFrst term in the brackets in (2) is the inFFdelity-to-the-data measure, the second is the inFFdelity-to-the-constraint measure, and NAK 2 is the smoothness tradeoVT parameter. Whittaker left the choice of NAK 2 to the investigator.


<!-- p:3 -->


#### 2.2. Automatic parameter determination via Bayesian interpretation

A smoothness priors solution [2] explicitly solves the problem posed by Whittaker [23]. A version of the solution is as follows: Multiply (2) by - 1 = (2 ESC 2 ) and exponentiate it. Then the solution that minimizes (2) achieves the maximization of

$$\exp \left \{ - \frac { 1 } { 2 \sigma ^ { 2 } } \sum _ { n = 1 } ^ { N } \left ( y _ { n } - f _ { n } \right ) ^ { 2 } \right \} \exp \left \{ - \frac { \lambda ^ { 2 } } { 2 \sigma ^ { 2 } } \sum _ { n = 1 } ^ { N } \left ( \Delta ^ { k } f _ { n } \right ) ^ { 2 } \right \} . \\ \\ \ U l d o n _ { \ } t h e a m p o m t i o n _ { \ } o f \ n o m p o l i t y _ { \ } ( 3 ) \ v i l d o n _ { \ } o \, R o v o i j o n _ { \ } i n t o m o t i o n$$

Under the assumption of normality, (3) yields a Bayesian interpretation

$$\pi ( f | y , \lambda ^ { 2 } , \sigma ^ { 2 } , k ) \otimes p ( y | \sigma ^ { 2 } , f ) \pi ( f | \lambda ^ { 2 } , \sigma ^ { 2 } , k ) , \\ \\ \\$$

where EM ( f | NAK 2 ; ESC 2 ; k ) is the prior distribution of f and p ( y | ESC 2 ; f ) the data distribution, conditional on ESC 2 and f , and EM ( f | y; NAK 2 ; ESC 2 ; k ) the posterior of f . Akaike [2] obtained the marginal likelihood for NAK 2 and k by integrating (3) with respect to f . This facilitates an automatic determination of the tradeoVT parameters in constrained least squares which has been treated subjectively for many years and eventually led to the frequent use of Bayesian method in statistical and information science communities. Several interesting applications of this method can be seen in [4].

#### 2.3. Time series interpretation and state space modeling

Consider a problem of FFtting polynomial of order k - 1 deFFned by

where SI n ∼ N (0 ; ESC 2 ). It is easy to see that this polynomial is the solution to the diVTerence equation

$$y _ { n } = t _ { n } + \varepsilon _ { n } , \ \ t _ { n } = a _ { 0 } + a _ { 1 } n + \cdots + a _ { k - 1 } n ^ { k - 1 } , \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\$$

$$\Delta ^ { k } t _ { n } = 0 ,$$

with appropriately deFFned initial conditions. This suggests that by modifying the above diVTerence equation so that it allows for a small deviation from the equation, namely by letting SOH k t n ≈ 0, it might be possible to obtain a more CRexible regression curve than the usual polynomials. A possible formal expression is the stochastic diVTerence equation model

$$\Delta ^ { k } t _ { n } = v _ { n } ,$$

where vn ∼ N (0 ; FS 2 ) is an i.i.d. Gaussian white noise sequence. For small noise variance FS 2 , it reasonably expresses our expectation that the noise is mostly very 'small' and with a small probability it may take a relatively 'large' value. Actually, the solution to the model is, at least locally, very close to a ( k - 1)th order polynomial. However, globally a signiFFcant diVTerence arises and (7) can express a very CRexible function. For k =1, it is locally constant and becomes a well-known random walk model, t n = t n - 1+ vn . For k =2, the model becomes t n =2 t n - 1 - t n - 2 + vn and the solution is a locally linear function.


<!-- p:4 -->


The models (5) together with (7) can be expressed in a special form of the state space model

$$x _ { n } & = F x _ { n - 1 } + G v _ { n } \pmod { ( \text {system model} ) } , \\ y _ { n } & = H x _ { n } + w _ { n } \pmod { ( \text {observation model} ) } ,$$

where vn ∼ N (0 ; FS 2 ), wn ∼ N (0 ; ESC 2 ) and xn =( t n ; : : : ; t n - k +1) ′ is a k -dimensional state vector, F , G and H are k × k , k × 1 and 1 × k matrices, respectively. For example, for k =2 ; they are given by

$$x _ { n } = \begin{bmatrix} t _ { n } \\ t _ { n - 1 } \end{bmatrix} , \ \ F = \begin{bmatrix} 2 & - 1 \\ 1 & 0 \end{bmatrix} , \ \ G = \begin{bmatrix} 1 \\ 0 \end{bmatrix} , \ \ H = [ 1 , 0 ] .$$

One of the merits of using this state space representation is that we can use computationally eSOcient Kalman FFlter for state estimation. Since the state vector contains unknown trend component, by estimating the state vector xn , the trend is automatically estimated. Also unknown parameters of the model, such as the variances ESC 2 and FS 2 can be estimated by the maximum likelihood method. In general, the likelihood of the time series model is given by

$$L ( \theta ) & = p ( y _ { 1 } , \dots , y _ { N } | \theta ) = \prod _ { n = 1 } ^ { N } \, p ( y _ { n } | Y _ { n - 1 } , \theta ) , \\ \\$$

where Yn - 1= { y 1 ; : : : ; y n - 1 } and each component p ( yn | Yn - 1 ; DC2 ) can be obtained as byproduct of the Kalman FFlter [11]. It is interesting to note that the tradeoVT parameter NAK 2 in the penalized least-squares method (2) can be interpreted as the ratio of the system noise variance to the observation noise variance, or the signal-to-noise ratio.

The individual terms in (10) are given by, in general p -dimensional observation case,

$$p ( y _ { n } | Y _ { n - 1 } , \theta ) = \frac { 1 } { ( \sqrt { 2 \pi } ) ^ { p } } \left | W _ { n | n - 1 } \right | ^ { - 1 / 2 } \exp \left \{ - \frac { 1 } { 2 } \, \varepsilon _ { n | n - 1 } ^ { \prime } W _ { n | n - 1 } ^ { - 1 } \varepsilon _ { n | n - 1 } \right \} ,$$

where SI n | n - 1= yn - yn | n - 1 is one-step-ahead prediction error of time series and yn | n - 1 and V n | n - 1 are the mean and the variance covariance matrix of the observation yn , respectively, and are deFFned by

$$y _ { n | n - 1 } = H x _ { n | n - 1 } ,$$

$$W _ { n | n - 1 } = H V _ { n | n - 1 } H ^ { \prime } + \sigma ^ { 2 } .$$

Here x n | n - 1 and V n | n - 1 are the mean and the variance covariance matrix of the state vector given the observations Yn - 1 and can be obtained by the Kalman FFlter [11].

If there are several candidate models, the goodness of the FFt of the models can be evaluated by the AIC criterion deFFned by

$$A I C = - 2 \, \log L ( \hat { \theta } ) + 2 \, \text { (number of parameters).}$$


<!-- p:5 -->


AIC is derived from an asymptotically unbiased estimate of the expected log-likelihood, or equivalently the Kullback-Leibler information of the model, and the model with the smallest AIC is considered to be the best one [1,20].

#### 2.4. Modeling of space-time data

Let Z i n , ( n =1 ; : : : ; N ; i =1 ; : : : ; I ) be scalar observation at a discrete time of n for a station (site) i . Along the line mentioned above, we consider the following model to decompose Z i n into trend, T i n , and irregular component, D i n , namely,

$$Z _ { n } ^ { i } = T _ { n } ^ { i } + D _ { n } ^ { i } , \quad D _ { n } ^ { i } \sim N ( 0 , \sigma ^ { 2 , i } ) . \\ \\$$

A direct approach to realize the Bayesian space-time (space-temporal) model is given by considering the following system model for each n :

$$T _ { n } ^ { i } & = 2 T _ { n - 1 } ^ { i } - T _ { n - 2 } ^ { i } + E _ { n } ^ { i } , \quad E _ { n } ^ { i } \sim N ( 0 , \tau ^ { 2 i } ) \ \forall i , \\ & \\ & \quad \dot { i } \quad \dot { i } \quad \dot { i } \quad \dot { i } \quad \dot { i } \quad \dots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \quad \ddots \$$

where SOH ij is some measure of a distance between station i and j , and RS is usually assumed as a linear function truncated at SOH th which is set to be the mean of distance between the neighboring points. Although this approach is desirable from the statistical viewpoint, its numerical realization on computer is impractical due to large memory required for a large number of I ≈ 1000 that we usually deal with. For a case with lower dimensional model like I 6 100, a simple approach to deal with T n =[ T 1 n ; T 2 n ; : : : ; T I n | T 1 n - 1 ; T 2 n - 1 ; : : : ; T I n - 1 ] ′ as a state vector can be implemented on a computer with large memory [12].

$$T _ { n } ^ { i } - T _ { n } ^ { j } & = V _ { n } ^ { i } , \ \ V _ { n } ^ { i } \sim N ( 0 , ( \phi ( \Delta ^ { i j } ) ) ^ { 2 } s ^ { 2 } ) \ \forall ( i , j ) , \\ \\ \intertext { t } T _ { n } ^ { i j } - T _ { n } ^ { j } & = V _ { n } ^ { i } , \quad V _ { n } ^ { i } \sim N ( 0 , ( \phi ( \Delta ^ { i j } ) ) ^ { 2 } s ^ { 2 } ) \quad \forall ( i , j ) ,$$

A simple way to mitigate this computational diSOculty in the direct Bayesian approach for a case with I ≈ 1000 is to assume that each time series Z i =[ Z i 1 ; Z i 2 ; : : : ; Z i N ] ′ is mutually independent vector. This assumption allows the smoothness priors approach mentioned earlier to be employed. Then, we use the system model given by (16) only. The maximum likelihood estimates for ESC 2 ; i and FS 2 ; i are denoted by ˆ ESC 2 ; i and ˆ FS 2 ; i , respectively. The Kalman FFlter and smoother with ˆ ESC 2 ; i and ˆ FS 2 ; i yield the estimates for the trend component, ˆ T i n . The estimated irregular components ˆ D i n = Z i n - ˆ T i n is called the residual hereafter. A vector of the residual components for the station i is denoted by D i and the median of ˆ T i n , for each n , by SYN Tn . Similarly, their percentile points corresponding to ± ESC and ± 2 ESC intervals of ˆ T i n versus n are denoted by T ± 1 n and T ± 2 n , respectively.

The next step for exploring the mean structure of the space-time data is to examine the spatial correlation of the residual components in terms of a correlation coeSOcient C ij between D i and D j . For a FFxed station i , a spatial distribution of C ij as a function of a distance measure SOH ij has to be examined visually. In fact, a large number of C ij hampers such kind of visual examination. Therefore, a plot of C ij versus SOH ij guides us to further improvements on the mean structure of the space-time data. Obviously, when there appear many points with high correlation in the small value of SOH , taking the spatial correlation into account would improve an initial estimate on the mean structure of the space-time data, ˆ T i n . Such kind of improvements can be realized by considering the following smoothness priors model for a spatial data:


<!-- p:6 -->


$$\hat { T } _ { n } ^ { i } & = \mu _ { n } ^ { i } + U _ { n } ^ { i } , \quad U _ { n } ^ { i } \sim N ( 0 , r ^ { 2 } ) \ \forall i , \\ \mu _ { n } ^ { i } - \mu _ { n } ^ { j } & = V _ { n } ^ { i } , \quad V _ { n } ^ { i } \sim N ( 0 , ( \phi ( \Delta ^ { i j } ) ) ^ { 2 } s ^ { 2 } ) \ \forall ( i , j ) , \\ \text {where } \mu _ { n } ^ { i } \text { is an improved trend component. The iterative procedure mentioned above}$$

where SYN i n is an improved trend component. The iterative procedure mentioned above is practical for improving the estimates of the mean structure of the space-time data set [9].

### 3. Applications

#### 3.1. An illustrative example: seasonal adjustment

The smoothness priors method has been applied to many real world problems [4,13]. Most of the economic time series contain trend and almost periodic components which make it diSOcult to capture the essential change of economic activities. Therefore in economic data analysis, removal of these eVTects is important. In our modeling it is realized by the decomposition

$$y _ { n } = t _ { n } + s _ { n } + w _ { n } ,$$

where t n , s n and wn are trend, seasonal and irregular components. A reasonable solution to this decomposition was given by the use of smoothness priors for both t n and s n [6]. The trend component t n and the seasonal component s n are assumed to follow

$$t _ { n } & = 2 t _ { n - 1 } - t _ { n - 2 } + v _ { n } , \\ s _ { n } & = - ( s _ { n - 1 } + \cdots + s _ { n - 1 1 } ) + u _ { n } , \\ \intertext { w h e r e } \ w h e r e \ \intertext { s u n } \ w h e r e \ \intertext { s o n } \intertext { w h e r e } \intertext { w h e r e } \intertext { s u n } \intertext { w h e r e } \intertext { s o n }$$

We FFt this model to BDHWWS (Wholesale Hardware Sales, US Bureau of the Census, January 1967-February 1989) data. The variance of the irregular component, the log-likelihood and AIC of the model are 0.001193, 454.6 and 3095.2, respectively. Figs. 1A-C show the log-transformed original data and the estimated trend, seasonal component and the irregular component, respectively. The estimated seasonal component is very stable over the whole period and the trend clearly captures the depression of the sales in 1975 and 1982. The irregular component is small compared with the seasonal variation. Although, by this seasonal adjustment, it is possible to extract or remove seasonal component, we can extract more information by a smoothness prior modeling. Many of the economic time series related to sales or production are aVTected by the number of days of the week. For example, the sales of a department store will be strongly aVTected by the number of Sundays and Saturdays in each month. Such kind of eVTect is called the trading day eVTect.

where vn , un and wn are Gaussian white noise with vn ∼ N (0 ; FS 2 t ), un ∼ N (0 ; FS 2 s ) and wn ∼ N (0 ; ESC 2 ).

To extract the trading day eVTect, we consider the decomposition

$$y _ { n } = t _ { n } + s _ { n } + t d _ { n } + w _ { n } ,$$


<!-- p:7 -->


Fig. 1. Seasonal adjustment of BDHWWS.

where t n , s n and wn are as above and the trading day eVTect component, t d n , is assumed to be expressed as

$$t d _ { n } & = \sum _ { j = 1 } ^ { 7 } \beta _ { j } d _ { j n } , \\ \\$$

where djn is the number of j th day of the week (e.g., j =1 for Sunday and j =2 for Monday, etc.) and FF j is the unknown trading day eVTect coeSOcient. To assure the identiFFability, it is necessary to put constraint that FF 1+ · · · + FF 7 =0. The variance of the irregular component, the log-likelihood and AIC of the model are 0.000602, 515.4 and 2985.7, respectively. The reduction of the variance and the AIC value clearly indicates the existence of the trading day eVTect. Fig. 2A shows the estimated trading day eVTect coeSOcients FF j ; j =1 ; : : : ; 7. It reveals that Sunday ( j =1) and Saturday ( j =7) have negative eVTect. This suggests that many wholesale stores are closed on Sunday and Saturday. The coeSOcients for the weekend are positive. However, those of Monday, Wednesday and Friday are close to zero.


<!-- p:8 -->


Fig. 2. Trading day eVTect coeSOcients: (A) 7-factor model, and (B) 2-factor model.

To check the reliability of these coeSOcients, we considered a constrained model that assumes

$$\beta _ { 1 } = \beta _ { 7 } , \quad \beta _ { 2 } = \beta _ { 3 } = \beta _ { 4 } = \beta _ { 5 } = \beta _ { 6 } .$$

The variance, log-likelihood and AIC of this model are 0.000636, 512.8, 2980.9, respectively. Since AIC of the model is smaller than the former model, it indicates that this constrained model is better than the former one. Namely, the diVTerence of the trading day coeSOcients within weekdays and also that of Sunday and Saturday are not signiFFcant. Fig. 2B shows the trading day coeSOcients obtained by this model.

Figs. 1D and E show the trading day eVTect and the irregular component obtained by this model. The trend and seasonal components are visually indistinguishable from the ones shown in Figs. 1A and B. The trading day eVTect is very small compared with the seasonal variation. However, the irregular component becomes considerably small. Actually, the variance of the residual becomes a half. Fig. 1F shows the plot of the seasonal component plus trading day eVTect. Comparing with Fig. 1A, it can be seen that the seasonal component plus trading day eVTect reproduces the detailed behavior of the series.

Since the numbers of day of the week are completely determined by the calendar, if we obtain good estimates of the trading day eVTect coeSOcients, then it will greatly contribute to the increase of prediction ability.

Similar decomposition methods are developed for the analysis of earth tide data and groundwater data. In these applications, the time series is decomposed as

$$y _ { n } = t _ { n } + p _ { n } + e _ { n } + r _ { n } + w _ { n } ,$$

where pn , en and r n are the barometric air pressure eVTect, the earth tide eVTect and the precipitation eVTect, respectively [4]. By the decomposition of 10 years groundwater data with this model, the eVTects of earthquakes are clearly detected, and various knowledge on the relation between occurrence of earthquakes and the groundwater level are obtained [14,15].


<!-- p:9 -->


#### 3.2. Analysis of POS data

Analysis of POS scanner data is an important research area of 'data mining' and discovery science, which may provide store managers with useful information to control price or stock levels of goods. The promotional eVTect measurements responding to price changes and semi-automatic sales forecasts of each brand may be useful in order to pursue price promotions eSOciently and reduce the risk of 'dead-stock' or 'out-of-stock'.

POS data set consists of a huge number of items and the analyses so far are mostly concentrated on the detection of mutual relation between items. In this subsection, we will show that, by the smoothness prior modeling of multivariate time series which takes into account of various components such as long term baseline sales trend, weekly pattern and competitive eVTects, it is possible to discover the eVTect of temporary pricecut and competitive relation between several items.

Assume that yn =[ y (1) n ; : : : ; y ( ' ) n ] ′ denotes ' dimensional time series of sales of a certain product category, and pn =[ p (1) n ; : : : ; p ( ' ) n ] ′ the covariate expressing the price of each brand. The generic model we consider here for the analysis of POS data is given by

$$y _ { n } = t _ { n } + d _ { n } + x _ { n } + w _ { n } ,$$

where t n , dn , xn and wn are the baseline sales trend, weekly pattern, sales promotion eVTect, and observation noise, respectively. Each component of the baseline sales trend, t ( j ) n , is assumed to follow the FFrst order trend model

$$t _ { n } ^ { ( j ) } = t _ { n - 1 } ^ { ( j ) } + u _ { n } ^ { ( j ) } .$$

The weekly pattern, d ( j ) n , can be considered as a special form of seasonal component with period length 7 and is assumed to follow

$$d _ { n } ^ { ( j ) } = - ( d _ { n - 1 } ^ { ( j ) } + \cdots + d _ { n - 6 } ^ { ( j ) } ) + v _ { n } ^ { ( j ) } . \\$$

The price promotion eVTect is assumed to be expressed by a linear function of nonlinear transformation of the price (price function)

$$x _ { n } = B _ { n } f ( p _ { n } ) .$$

In the analysis that follows, we assume that the price function is given by

$$f ( p _ { n } ) ^ { ( j ) } = \exp \{ - \gamma ( n - n _ { 0 } ) \} I _ { A } ( \Delta p _ { n } ^ { ( j ) } - c _ { n } ^ { ( j ) } ) , \\$$

where SOH p ( j ) n denotes the temporary price-cut from its regular (precisely the maximum) price, CR , a parameter, n 0 a starting point of price-cut, c ( j ) n a condition that a price-cut is eVTective to cause sales increases, and I A ( ) an indicator function. In actual modeling, this price promotion eVTect is further decomposed into xn = gn + z n , where gn is the category expansion eVTect and corresponds to the contribution to the increase of total


<!-- p:10 -->

-150

Fig. 3. Decomposition of the brand B1 (left) and B2 (right). Top plots: observed series, second plots: baseline trend plus weekly pattern, third plots: category expansion, fourth to sixth plots: brand substitution, positive due to own price-cuts and negative due to competitors' price-cuts.

sales. On the other hand, z n is the brand switch eVTect which is the increase of the sales of a brand obtained at the expense of the decrease of other brands and does not contribute to the increase of category total [19].

This model can be conveniently expressed in linear state space model and thus the numerically eSOcient Kalman FFlter can be used for state estimation, namely for the decomposition into components, and parameter estimation. Within various possible candidate models, the best model was found by the AIC criterion.

The presented model was applied to scanner data sets of daily milk category, for the period of 1994 = 2 = 28-1996 = 3 = 3 ( N =735). Five-variate series consisted of top four brands and the others total were analyzed. Only two brands B1 and B2 are shown on top of Fig. 3. The second plots show the estimated baseline trend components plus the estimated weekly pattern. Only about 20% of the variation of the original series is explained by this day of the week eVTect. However, for other stores where the prices of brands did not change so signiFFcantly, the weekly pattern contribute much more than this present case.


<!-- p:11 -->


Fig. 4. Competitive relationships between four brands.

Fig. 4 shows the detected competitive relationship among four major brands discovered via identiFFed model. The competitive coeSOcients are shown as well. The brand, B3, is a low fat type of B2 and is identiFFed to be independent of other brand's price promotion due to the type diVTerence. Price-cut of B4 (B2) increases sales of B4 (B2), but reduces those of B1 and B2 (B1). Price-cut of B1 increases sales of B1 and does not aVTect the sales of the competitive three brands.

The decomposition of price promotion eVTect into brand switch eVTect and category expansion eVTect is achieved by using the category total sales instead of the others total sales with a zero constraint on the brand switch eVTect of the category total for each price function. The third plots of Fig. 3 show the estimated category expansion eVTect. The price-cuts of B1 and B2 contribute to the expansion of category total. The fourth plots show the estimated brand switch components, being positive by own price-cuts, and the FFfth or sixth plots, being negative by the competitors' price-cuts.

The brand switch components of B1 and B2 are quite diVTerent. The plot for B1 indicates that the price-cut of B1 slightly contributes to the expansion of its own sales. However, B1 is vulnerable to the price-cut of B2 (see the FFfth plots) and B4 (see the sixth plots). On the other hand, the price-cut of B2 considerably contributes to the increase of the own sales (see the fourth plots) and B2 is slightly aVTected by the price-cut of B4 (see the FFfth plots) .

#### 3.3. Analysis of GPS data

The GPS is one of the most interesting and important data set which allows us to investigate a global change in environment precisely. Its high precision information on positions of permanent stations can be supplied by signal processing of microwave signal from GPS satellite. Several physical quantities of media existing between the GPS satellite and ground stations, such as electron, water vapor, and so on, aVTect phase information of microwave signals and result in propagation delays [5,7,10]. Therefore, a careful treatment of propagation delays is required to extract reliable information as to measurements of the positions.


<!-- p:12 -->


Dominant sources to bring about propagation delays are (1) ionosphere origin and (2) troposphere origin, such as atmospheric pressure and atmospheric water vapor [22]. The propagation delay generated by the atmospheric water vapor, called the wet delay, is most diSOcult to evaluate among these factors. A good estimation on the propagation delay can be given to the ionosphere origin and atmospheric pressure origin sources, by utilizing other physical quantities measured simultaneously. As a result, the wet delay turns out to appear as 'noise source' in the processing of the GPS data and has to be subtracted prior to diagnosing the GPS data in terms of information on positions.

In Japan, considerable eVTorts to establish a nationwide GPS array has been kept making by the Geographical Survey Institute of Japan (GSI) [8]. The Japanese GPS array is characterized by its high spatial resolution; the array is composed of nearly one thousand stations separated typically by 15-30 km from one another [22]. Then, a proper processing of the GPS data set taking the wet delay eVTect into account allows us to estimate a high-frequent spatial pattern of the atmospheric water vapor, in particular, precipitable water vapor (PWV) which plays an important role in forecasting a weather map. Actually, an approach to extract information concerning the PWV from the GPS data draws much attention in a FFeld of the meteorology and now is referred to as the GPS meteorology [5,7,22].

Many previous works to infer a quantitative relationship between the PWV and GPS data used the hourly GPS data sequences for some special events in limited local areas, because an association of space-time variation of the GPS data with other information obtained by radar echo and radiosonde measurements would be useful and direct [7,10,22]. Our objective in this study is aimed at FFnding empirical rules to give a quantitative description for the relationship between the CRuctuations observed in the GPS data and PWV. We begin with a statistical analysis of the daily GPS array data provided by the GSI. Let U i n be the n th day starting from January 1st, 1996 at the station (site) i :

$$U _ { n } ^ { i } = [ X _ { n } ^ { i } , Y _ { n } ^ { i } , Z _ { n } ^ { i } ] , \quad i = 1 , \dots , I , \ n = N _ { s } ^ { i } , \dots , N _ { e } ^ { i }$$

where X , Y , and Z correspond to the north-south, east-west, and up-down components, respectively. N i s and N i e represent the starting and last date of the GPS data available to us now. I is the number of stations.

Our preparatory analysis shows that the CRuctuations associated with the PWV are most clearly seen in the up-down component, Z i n , among the three components. Then, in this study, we focus on the up-down component Z i n . Unfortunately, the original GPS array data contains the outliers as well as the missing observations. These unsatisfactory cases can be easily treated by smoothness priors approach with the state space model, presented in Section 2.3, which provides us with the reasonable interpolated data (see [4] for details). Denoising procedure based on another modeling approach has been proposed to deal with an identiFFcation of outliers and discontinuities and has produced the similar estimates on T i n [16]. The interpolation allows us to determine ˆ T i n , T ± 1 n , and T ± 2 n systematically. In Fig. 5 we show SYN Tn , T ± 1 n , and T ± 2 n obtained by applying the smoothness priors approach to Z i n . A seasonal pattern, which is expected to be associated with the PWV, is clearly seen in this FFgure. A spatial distribution of SYN Tn can be illustrated by a GIF animation ( http://www.ism.ac.jp/ ∼ higuchi/GPS/SpaAll.gif ).


<!-- p:13 -->


Fig. 5. The median, ± 1 ESC , and ± 2 ESC percentile points of the estimated trend of the up-down component versus n , SYN Tn; T ± 1 n , and T ± 2 n .

In addition, a relatively signiFFcant amplitude of the seasonal variation is found to be larger than the typical amplitude of the residuals, which can be approximated by the mean of the standard deviation of D i . Therefore, it is apparent that an extraction of precise information on the position from the GPS array requires an elimination of an eVTect of the PWV from the GPS data. A power spectrum analysis is performed on the SYN Tn component and FFnd no eminent peak except for a yearly cycle in a frequency domain. A detail investigation is being made on this FFgure to discover with what factors is associated from the viewpoint of a climatology.

Fig. 6 shows a plot of SOH ij versus C ij , where the unit of SOH is degree; roughly speaking, the distance of the degree corresponds to 111km. In this FFgure, only 10 000 points that are randomly drawn from about 180 000 C ij are shown for the sake of reducing a FFle size for this FFgure. An appearance of many points with high correlation in a small value of SOH clearly suggests that a residual sometimes shows a similar CRuctuation with that in the neighboring stations.

Three lines superposed on this FFgure are

$$C ( \Delta ) = \exp \left ( - \frac { \Delta } { 7 } \right ) \, \left [ \exp . \, d a c y \, \text { type} \right ] \, ( \min \, \text {line} ) ,$$

C ( SOH ) = (0 : 82) SOH [ AR type ] (broken line) ;

$$C ( \Delta ) = 1 - 0 . 3 6 \cdot ( \Delta ) ^ { 0 . 2 9 } \, \left [ \text {long memory type} \right ] \, ( \text {thick line} ) .$$


<!-- p:14 -->


Fig. 6. Plots of SOH ij versus C ij .

The horizontal line indicates a value of 1 =e . Each curve represents a correlation function induced from a model denoted in bold face. The thin and thick lines are drawn so as to have them resemble an envelope of the upper bound and +2 ESC percentile as a function of SOH in the range of SOH 6 10. A good agreement of the thick line to +2 ESC envelope would imply that a long-memory-type spatial correlation ( H ∼ 0 : 15) [17] happens to be observed for an atmospheric spatial pattern. An examination of the weather map for these cases is interesting, but the detailed discussion will be left to other places.

### 4. Conclusion

The key to the success of a statistical procedure is the appropriateness of the model used in the analysis. The smoothness prior approach facilitates to develop various types of models based on prior information on the subject and the data. In this paper, we applied the smoothness priors method for the modeling of large-scale time series and space-time data with mean value structure and competitive relations between variables. In the analysis of POS data, the time series is decomposed into several components and various knowledge to make a strategy concerning price promotion and risk control of dead-stock are obtained. By the analysis of GPS data, a useful information for making a conjecture on the relationship between the propagation delay and PWV is successfully extracted based on the detailed investigation on the trend and residual components.

Softwares based on the smoothness prior approach are available at the following Web sites. The seasonal adjustment method discussed in Section 3.1 can be directly performed on Web-Decomp (http: == www.ism.ac.jp =  ̃ sato) without installing any software. Some other models based on the smoothness prior approach or state space modeling can be run on the Web site of Institute of Geoscience, National Institute of Advanced Industrial Science and Technology (http: == 150.29.8.26 = GSJ E = analysis = index.html).


<!-- p:15 -->


### Acknowledgements

The GPS array data were provided by the Geographical Survey Institute of Japan (GSI). One of the authors (T.H.) thanks to Dr. S. Miyazaki (GSI) for his help to understand the original data structure. One of the authors (F.N.K) wishes to thank Mr. Ono and Mr. Nishiyama, The Distribution Systems Research Institute, for providing us with valuable daily scanner data.
