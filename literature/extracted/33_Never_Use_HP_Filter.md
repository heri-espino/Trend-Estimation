---
id: "33_Never_Use_HP_Filter"
source_pdf: "../pdf/33_Never_Use_HP_Filter.pdf"
source_filename: "33_Never_Use_HP_Filter.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "good"
extraction_score: 88.0
visual_assets: "disabled"
references_file: "../references/33_Never_Use_HP_Filter.references.md"
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
