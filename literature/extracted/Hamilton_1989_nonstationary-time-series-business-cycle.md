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
