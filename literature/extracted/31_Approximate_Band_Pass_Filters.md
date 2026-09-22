---
id: "31_Approximate_Band_Pass_Filters"
source_pdf: "../pdf/31_Approximate_Band_Pass_Filters.pdf"
source_filename: "31_Approximate_Band_Pass_Filters.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/31_Approximate_Band_Pass_Filters.references.md"
---

<!-- p:1 -->

### NBER WORKING PAPER SERIES

### MEASURING BUSINESS CYCLES APPROXIMATE BAND-PASS FILTERS FOR ECONOMIC TIME SERIES

Marianne Baxter Robert t G. King

Working Paper No.5 5022

#### NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 February 1995

We thank Bennett McCallum, Sergio Rebelo, Mark Watson, Kei-Mu Yi, and seminar participants at the University of Florida, the Federal Reserve Bank of Richmond, and the University of Virginia for helpful comments and suggestions. Baxter gratefully acknowledges the support of the National Science Foundation. This paper is part of NBER's research program in Economic Fluctuations. Any opinions expressed are those of the authors and not those of the National Bureau of Economic Research.

© 1995 by Marianne Baxter and Robert G. King. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source.


<!-- p:2 -->


### MEASURING BUSINESS CYCLES APPROXIMATE BAND-PASS FILTERS FOR ECONOMIC TIME SERIES

### ABSTRACT

This paper develops a set of approximate band-pass filters designed for use in a wide range of economic applications. In particular, we design and implement a specific band-pass filter which isolates business-cycle fluctuations in macroeconomic time series. This filter was designed to isolate fluctuations in the data which persist for periods of two through eight years. This filter also "detrends" the data, in the sense that it will render stationary time series that are integrated of order two or less, or that contain deterministic time trends. We apply our filter to several of the key macroeconomic time series, and describe the picture of the U.S. postwar business cycle that emerges from our analysis. We also provide detailed comparisons with several alternative detrending methods.

Marianne Baxter Department of Economics Rouss Hall University of Virginia Charlottesville, VA 22903 and NBER

Robert G. King Department of Economics Rouss Hall University of Virginia Charlottesville, VA 22903 and NBER


<!-- p:3 -->


## 1 Introduction

The study of business cycles necessarily begins with the measurement of business cycles. The seminal contribution of Burns and Mitchell [1946] was influential because it provided a comprehensive catalogue of the empirical features of the business cycles of developed countries, notably, the United States. However, their work was also important because it developed methods for measuring business cycles that could be used by other researchers working with other countries or other sample periods.

Contemporary students of the business cycle still face the same basic issue as did Burns and Mitchell fifty years ago: how should one isolate the cyclical coiponent of an economic time series? In particular, how should one separate business-cycle elements from slowly evolving secular trends, and rapidly varying seasonal or irregular components? The decomposition used by Burns and Mitchell is no longer in common use, due both to its complexity and its central element of judgment.1 In its place, modern empirical macroeconomists employ a variety of detrending and smoothing techniques to carry out trend-cycle decompositions. These decompositions are frequently ad hoc in the sense that the researcher only requires that the detrending procedure produce a stationary business-cycle component, and does not otherwise specify the statistical characteristics of business cycles. Examples of techniques in common use are (i) application of two-sided moving averages; (ii) first-differencing; (iii) removal of linear or quadratic time trends; and (iv) application of the HodrickPrescott [1980] filter. Many recent studies using a battery of such methods to measure business cycles.

In our view, this proliferation of techniques for measuring business cycles has resulted from a lack of attention to an issue which Burns and Mitchell [1946] viewed as central: the definition of a business cycle. In this paper, we develop methods for measuring business cycles which require that the researcher begin by specifying characteristics of these cyclical components. Our procedures then isolate business cycle l, a    Ts lg s  ly we develop approximate band-pass filters that are constrained to produce stationary outcomes when applied to growing time series.2

1 However, it is possible to implement a judgment-free version of the Burns and Mitchell procedure, using the business cycle dating algorithını of Bry and Boschan [1981]. Two recent examples are King []  ge [] d 9

2In recent work, Englund, Persson, and Svensson [1992] and Hassler, Lundvik, Persson, and o d  s  s s  p    es se  t no extract business cycle compouents from time series. They employ a two-step procedure in which they first detrend the time series using the Hodrick-Prescott [1980] filter, and then extract business-cycle components by band-pass filtering in the frequency domain. Canova [1993] also uses high-pass and band-pass filters in the frequency domain in his extensive analysis of detrending and business-cycle facts. We discuss these methods in more detail later in the paper.


<!-- p:4 -->


For the empirical applications in this paper, we adopt the definition of the business cycle suggested by the procedures and findings of NBER researchers like Burns and Mitchell [1946]. We apply our method to a several quarterly post-war U.S. time series. Burns and Mitchell specified that business cycles were cyclical components of no less than six quarters (eighteen months) in duration and they found that U.S. business cycles typically last fewer than thirty two quarters (eight years). We adopt these limits as our defnition of the business cycle.

Specifying the business cycle as fluctuations with a specified range of periodicities results in a particular two-sided moving average (a linear filter). In the particular case of the NBER defnition of the business cycle, the desired filter is a band-pass filter, i.e., a filter which passes through components of the time series with fluctuations between six and thirty-two quarters, while removing components at higher and lower frequencies. However, the resulting moving average is of infinite order, so an approximation to this filter is necessary for it to be applicable to finite time series. Thus a central problem addressed by this paper is how to construct a good approximation to the optimal filter—i.e., the filter that accomplishes the business cycle decomposition specified by the researcher.3

In approaching this problem of filter design, we require that our method meet six objectives.4 First, as suggested above, the filter should extract a specified range of periodicities, and otherwise leave the properties of this extracted component unaffected. Second, we require that the ideal band-pass filter should not introduce phase shift, i.e., that it not alter the timing relationships between series at any frequency. These two objectives define an ideal moving average of the data with symmetric weights on leads and lags. Third, we require that our method be an optimal approximation to the ideal band-pass filter; we specify a specific loss function for discrepancies between the exact and approximate filter. Fourth, we require that the application of an approximate band-pass result in a stationary time series even when applied to trending data. Given recent empirical which suggests the presence of stochastic trends in economic time series, we design our filters so that they will make a filtered time series stationary if the underlying time series is integrated of order one or two. (Equivalently, we impose the requirement that the approximate filter's frequency response is zero at the zero frequency). This requirement also means that our band-pass filters will eliminate quadratic trends from a time series. Fifth, we require that the method yield business cycle components that are unrelated to the length of the sample period. Sixth, and finally, we require that our method be operational. In the general filter approximation problem, there is an important tradeoff involved: the ideal band-pass filter can be better approximated with the longer moving averages, but adding more leads and lags also means that observations must be dropped at the beginning and end of the sample thus leaving fewer for analysis. We therefore experiment extensively with the application of our filter to macroeconomic time series and provide some guidance about the tradeoffs involved. We recommend that researchers use moving averages based on six years of data for both quarterly and annual time series.

3Like many of the ad hoc filters listed above, our approximate filters are moving averages which can readily be applied to time series. However, our filters have the important advantage that the researcher can specify the objective of the data transformation explicitly, which in business-cycle research is presumably to isolate the component of a time series with particular periodicities.

4These requirements are very similar to those that Prescott [1986] discusses in justifying use of the Hodrick-Prescott [1980] filter.


<!-- p:5 -->


The organization of the paper is as follows. Section 2 describes the construction of approximate band-pass filters. In section 3, we define our business cycle filter and apply it to post-war U.S. data. Further, we investigate the implication of changing the number of leads and lags used to construct the approximate filter for certain summary statistics, using both post-war U.S. data and a specified stochastic data generating process (for which we can compute the influence of the length of the moving average on population moments). In section 4, we contrast our business cycle filter to the results of other commonly used procedures. In section 5, we provide a detailed comparison of two "HP" filters: the cyclical filter of Hodrick and Prescott [1980] and a high pass filter constructed using our methods. Particular attention is directed to two practical problems that researchers encounter using the Hodrick-Prescott method: unusual behavior of cyclical components near the end of the sample, and the choice of the smoothing parameter for data sampled at other than the quarterly frequency. Section 6 concludes the paper with a brief review of the goals and findings of the paper. Three appendices provide information on the stochastic and deterministic trend reduction implications of a class of moving average filters that contains our approximate filters and many others; details of the derivation of the optimal approximate band-pass filter; and printouts of the MATLAB programs used to implement the filters developed in this paper.

## 2 Band-pass filters for economic time series

This section describes the construction of moving averages that isolate the periodic co    ds e e  te s t e e o in the jargon of time series analysis, we are interested in constructing band-pass linear filters. We are particularly interested in designing a business cycle filter, defined as a linear filter which eliminates very slow moving ("trend") components and very high frequency ("irregular") componeuts while retaining intermediate ("business cycle") components.

It has long been understood that moving averages alter the relative importance of the periodic components in a time series (for a recent presentation, see Harvey [1981, chapter 3]). If the time series yt is stationary, then we can use frequency domain methods to study the implications of applying moving averages to yt. In this paper, we employ frequency domain analysis to consider the design of linear filters, but we ultimately will undertake our filtering entirely in the time domain (i.e., we will simply apply moving averages to macroeconomic data). Thus, readers who are simply interested in the practical results of our filtering methods may skip ahead to section 3.


<!-- p:6 -->


### 2.1 Applying moving averages to time series

Applying a moving average to a time series, yt, produces a new time series y:

$$y _ { t } ^ { * } = \sum a _ { k } y _ { t - k } \ .$$

For convenience, we will write the moving average as a polynomial in the lag operator L: a(L) = Σk=−K akLk, with L defined so that Lkxt = xt-k for positive and negative values of k. We will further specialize our attention to symmetric moving averages, '.  =  p  = p

One traditional use of moving averages has been to isolate or to eliminate trends in economic time series. If a symmetric moving average has weights that sum to properties. That is, if the weights sum to zero, we can always factor a(L) as:

$$a ( L ) = ( 1 - L ) ( 1 - L ^ { - 1 } ) \psi ( L ) & & ( 2 )$$

where ψ(L) is a symmetric moving average with K – 1 leads and lags. Symmetric moving averages with weights that sun to zero will thus render stationary series that contain quadratic deterministic trends; i.e., components of the form τt = γo+γ1t+γ2t2. Further, these moving averages can also make stationary the stochastic trends which arise when a time series is a realization of an integrated stochastic process (of the I(1) or I(2) type in the lexicon of Engle and Granger [1987]).

The Cramer representation of the stationary time series yt is:

$$y _ { \iota } = \int _ { - \pi } ^ { \pi } \xi ( \omega ) d \omega .$$

That is, the time series can be expressed as the integral of random periodic components, the ξ(ω), which are mutually orthogonal (Eξ(ω1)ξ(ω2) = 0 for ω1 ≠ ω2). In turn, the filtered time series can be expressed as

$$y _ { \iota } ^ { * } = \int _ { - \pi } ^ { \pi } \alpha ( \omega ) \xi ( \omega ) d \omega .$$

where α(ω) = Σ=-k ahe-iwh is the frequency response function of the linear filter. That is, α(ω) indicates the extent to which yi responds to yt at frequency ω, in the sense that α(ω) is the weight attached to the periodic component ξ(ω). Since the periodic components ξ(ω) are orthogonal, it follows that we can write the variance of the filtered series as:

$$v a r ( y _ { t } ^ { * } ) = \int _ { - \pi } ^ { \pi } | \alpha ( \omega ) | ^ { 2 } f _ { y } ( \omega ) d \omega .$$


<!-- p:7 -->


where |α(ω)|2 is the squared gain or transfer function of the linear filter at frequency ω and fy(ω) = var(ξ(ω)) is the spectral density of the series y at frequency ω. The squared gain thus indicates the extent to which a moving average raises or lowers the contribution to variance in the filtered series from the level in the original series.

In terms of our discussion below, it is important to note that the frequency response function α(ω) takes on a value of zero at frequency zero if and only if we require that the sum of the filter weights is zero (α(0) = Σh=-κ ahe−i0h = 0 if and only if ∑h=-κ ah = 0).

We turn next to the problem of designing filters to isolate specific frequencies in the data. Our method is to use frequency domain logic to design a moving average that emphasizes specified frequency bands. But we also require that our business cycle filter have the trend reduction properties discussed in this section, so that it can be meaningfully applied to economic time series which are nonstationary. We thus require that our business-cycle filter has a frequency response function with α(0) = 0.

### 2.2 The low-pass filter

A basic building block in filter design is the low-pass filter, by which we mean a filter which retains only slow-moving components of the data. An ideal low-pass filter, which passes only frequencies -ω ≤ ω ≤ ω, is illustrated in Panel A of Figure 1.5 The ideal low-pass filter we will study thus has a frequency response function given by β(ω) = 1 for |ω| ≤ ω, and β(ω) = 0 for |ω| &gt; ω. Notice that it is symmetric, β(ω) = β(−ω).

Let b(L) = Σ=-∞ b Lh denote the time-domain representation of this ideal lowpass filter. The filter weights bh may be found by the inverse Fourier transform of the frequency response function:

$$b _ { h } = \int _ { - \pi } ^ { \pi } \beta ( \omega ) e ^ { i \omega h } d \omega$$

Evaluating the integral above (see Appendix B for the details), the filter weights bh for the ideal filter are b0 = ω/π, and bh = sin(hω)/hπ for h = 1,2, ... Notice that an infinite-order moving average is necessary to construct the ideal filter. Hence, we are led to consider approximation of the ideal filter with a finite moving average a(L) = Σk=-k aLh; this approximating filter has a frequency response function aκ(ω) = ∑h=-k ahe−iwh.

5In this Figure, as in others below, we measure frequency ω as a fraction of π, so that the horizontal axis ranges from -1 to 1. For the figures, this means that periodicity of the frequency component is simply p = 2/ω, so that the most rapid oscillations shown in Figure 1 have period two. The "cutoff frequency" for the low pass filter corresponds to a period of p = 32 time units (presumed to be quarters of a year in view of empirical work below) and, hence, ω = 2/32 = 1/16 ≈ .07. However, for the analytical results below, we use the more conventional definition that the frequency ω has as its domain the interval −π ≤ ω ≤ π.


<!-- p:8 -->


### 2.3 Approximation of symmetric filters

If one is considering the general problem of choosing an approximate filter, ακ(ω), to approximate a specific filter β(ω), then a natural approximation strategy is to choose the approximating filter's weights ah to minimize:

$$Q = \int _ { - \pi } ^ { \pi } | \delta ( \omega ) | ^ { 2 } \, d \omega ,$$

-hi   i s s        ie. quency ω. This loss function thus attaches equal weight to the squared approximation errors at different frequencies.

There is a remarkable, general result for this class of optimization problems: the optimal approximating filter for given maximum lag length, K, is constructed by simply truncating the ideal filter's weights ah at lag K. This result reflects the fact that each of the truncated terms in a symmetric linear filter is orthogonal to the included terms. Thus the optimal approximate low-pass filter sets ah = bh for h = 0, 1, ..., K, and ah = 0 for h ≥ K + 1, where the weights bh are those given in section 2.2 above.6

### 2.4 Construction of high-pass and band-pass filters

High-pass and band-pass filters are easily constructed from low-pass filters. Before defining these additional filters, we establish some notation which we use throughout the rest of the paper. Since it is more natural for us to think in terms of periodicity of cycles than frequencies, we let LPk(p) denote the approximate low-pass filter which is truncated at lag K and which passes components of the data with periodicity greater than or equal to p. Since the ideal filter involves K = ∞, the ideal low-pass filter is denoted LP∞(p).

The ideal high-pass filter HP∞(p) passes components of the data with periodicity less than or equal to p, as illustrated in panel B of Figure 1. If the weights of the low-pass filter in Figure 1 panel A are bh for h = 0 and h = ±1, 2, ..., then the weights of the high-pass filter are 1 − b0 at h = 0 and −bh at h = ±1, 2, ... Correspondingly, the optimal approximate high-pass filter, H Pκ(p) is simply constructed by truncating the weights of H P∞(p) = 1 − LPk(p).7

The ideal band-pass filter passes only frequencies in the ranges ω ≤ ω| ≤ ω . It is therefore constructed from the two low-pass filters with cutoff frequencies ω and w: we denote the frequency response of these filters as β(ω) and β(ω). Then, to get the desired frequency response, we form the band-pass filter's frequency response as

6A classic reference on the approximation of linear filters using K'th order linear filters is Koopmans [1974].

7This is implied by the result discussed in section 2.3: that approximation of the ideal low-pass filter simply involves truncation of the ideal filter's weights at lag K.


<!-- p:9 -->


β(ω) - β(ω) since this will give unit frequency response on the frequency bands ω ≤ |ω| ≤ ω and zero elsewhere.

It is then easy to derive the filter weights for a band-pass filter. If we let bh and h be the filter weights for the low-pass filters with cutoffs ω and  then the band-pass filter has weights h- b. Panel C of Figure 1 plots an ideal band-pass filter which passes through cycles of length between 6 and 32 quarters, which corresponds to the Burns and Mitchell [1946] definition of business-cycle frequencies.

We use a similar notation for the approximate band-pass filters to that developed above for the high and low pass filters: BPk(p, q) denotes our approximation bandpass filter which passes cycles between p and q periods in length, for given truncation point K,where p denotes the shortest cycle length passed by the band-pass filter and q denote the longest cycle length (in Figure 1-C, p = 6 and q = 32). We construct BPk(p, q) by truncating the ideal band-pass filter.

### 2.5 Constraints on specific points

The minimization problem described above may be reformulated to recognize that cr i     oet t o o ad  ort so tto design a low-pass filter that places unit weight at the zero frequency (αk(ω) = 1 at ω = 0). If we construct a low-pass filter in this way, then the corresponding high-pass and band-pass filters will place zero weight at the zero frequency and, as we have seen above, this will mean that they give rise to stationary time series when applied to a range of nonstationary time series.

The constraint that αk(0) = 1 may be incorporated as a side condition to the minimization problem discussed above. Using the results of Appendix C, we find the following modification of the optimal approximate filter weights, ah, as functions of the weights of the ideal low-pass filter, bh,

$$a _ { h } = b _ { h } + \theta ,$$

where θ is a constant that depends on the specified maximum lag length, K. That is, since we require that the filter weights sum to one, (Σk=-k ah = 1), the normalizing constant is θ = (1 − Σh=-k bh)/(2K + 1). Thus the constraint that the low-pass filter place unit weight at the zero frequency results in a relatively simply adjustment of the filter weights.

Similar adjustments are necessary when constructing optimal truncated high-pass and band-pass filters subject to constraints on the frequency-zero value of the frequency response function. As discussed above, the unconstrained band-pass filter has weights which are the difference between two low-pass filters, i.e., the weights are bh- bh where bh is the filter weight at lag/lead h for the upper cut-off filter and bh is the weight for the lower-cutoff filter. The constrained band-pass filter involves the requirement that the sum of its weights must be zero. Hence, the weights in the constrained optimal band-pass filter are adjusted as follows:


<!-- p:10 -->


$$( \bar { b } _ { h } - \underline { b } _ { h } ) + ( \bar { \theta } - \underline { \theta } )$$

where ē is the adjustment coefficient associated with the upper-cutoff filter and θ is the adjustment coefficient associated with the lower cut-off filter (see Appendix C for additional discussion of this point). That is, the constrained optimal Kth order band-pass filter is simply the difference between two constrained optimal Kth order low-pass filters. Throughout the remainder of the paper, we consider only bandpass filters with this zero frequency constraint imposed. We use the notation defined above, BPk(p,q), to denote our approximation to the ideal band-pass filter which passes cycles between p and q periods.

### 2.6 The effects of truncation

This section explores the effect of changes in the maximum lag length, K, on the shape of the constrained low-pass and high-pass filters. If we choose an approximating moving average with maximum lag length K, implementing the filter means that we lose 2K observations (i.e., K leads and K lags). There is no "best" value of K; increasing K leads to a better approximation to the ideal filter, but results in more lost observations. Thus the researcher will have to balance these opposing factors, so that the best choice of K in a particular instance will depend on the length of the data period, and the necessity to obtain a good approximation to the ideal filter. The next section will explore this trade-off in the context of postwar U.S. macroeconomic time series. In this section, however, we are simply concerned with describing the effect of variations in K on the shape of the approximating filters.

Figure 2 illustrates the effect of truncation on the shape of the low-pass filter which has been constrained to have unit weight at the zero frequency. The ideal filter, illustrated by the dotted line in each panel, passes frequencies ω which corresponds to cycles in the quarterly data of length greater than or equal to 32 quarters. This Figure shows that there are important effects on the shape of the approximate lowpass filter of changes in K. When K = 4, so that the moving average covers only the preceding and subsequent four quarters, there is a major departure from the ideal filter. In particular, the approximate filter admits substantial components from the range of frequencies just above the cutoff frequency ω = π/16. This phenomenon ta ty t ta oo tt  tt t  l,   as passed through frequencies that the filter was designed to suppress, including them with those the filter was designed to retain. Correspondingly, the approximating filter has less than unit frequency response on the range |ω| ≤ π/16, which we define Aaos o  s  s     ty  os,, sey approximates the true filter. With K = 8, the problems of leakage and compression have been substantially reduced relative to the K = 4 case. Further reductions in leakage and compression are obtained with K = 16 and K = 32.


<!-- p:11 -->


Figure 3 displays the frequency response function for approximate band-pass filte , s  t  -   s an nd "compression" for small values of K. However, it is an empirical question whether improvement in approximating the ideal filter (by use of larger values of K) lead to important changes in moments computed from the filtered time series. In the next section we explore the effects of changes in K on the behavior of filtered macroeconomic time series.

### 2.7 Why filter in the time domain?

One common approach to band-pass filtering is the frequency domain method used by Hassler, et al. [1992], Canova [1993], and Li, et al. [1994]. This method works as follows. First, one takes a discrete Fourier transform of the economic data, computing the periodic components associated with a finite number of "harmonic" frequenciuee   t      t  ,  s st. Third, one computes the inverse Fourier transform to get the time domain filtered series, { ̄1, , ... ̄T}. We see two major drawbacks with this explicitly frequency domain procedure, relative to our time domain method. First, since there are likely to be stochastic trends (unit root components) in most economic time series, it is necessary to first detrend the series prior to taking the Fourier transform. That is: in order to accomplish band-pass filtering, one must first choose a detrending method. Working with annual data, Hassler et. al. [1992] use the Hodrick-Prescott filter with λ = 10 for this initial detrending step. Working with quarterly data, Li, et. al. [1994] argue for a much larger value, λ = 10, 000, in the initial detrending step so as to avoid distorting business cycle outcomes. Second, the results of the frequency domain method at all dates are dependent on the sample length T. Consider, for example, the "business cycle" component of a time series at a particular date t, denoted  ̄t, obtained from a study of economic data in a study of length T1. When the sample length is extended to T2, the discrete Fourier transform of {y1, y2, ...yT} must be recomputed and each of its elements will change. Consequently, so too will each of the elements of the inverse Fourier transform of the filtered series, i.e., the cyclical observations, {1, ,.. r}. Thus, the cyclic component of output at a particular date will change when the sample period changes. This time variation violates the fifth requirement that we discussed in section 1 above, which is also one that we share with Prescott [1986].

#### 31 Measuring business cycles

This section explores several empirical issues raised by the foregoing discussion of approximate band-pass filters. As discussed earlier, an ideal business cycle filter is defined to be the BP∞(6, 32) filter, and its optimal approximation is the BPk(6, 32) filter for 0 &lt; K &lt; ∞. First, we describe the effect of changes in the truncation point K on moments computed from a specified data generating process. Second, we explore the effect of variation in K on moments computed from several macroeconomic time series.


<!-- p:12 -->


### 3.1 Effect of variation in K on an AR(1) process

A useful way to explore the approximation error induced by application of the approximate band-pass filter is to compute moments for a known stochastic process using both the ideal and approximate filters. We examine the effect of variation in K on the autocovariances of the following first-order autoregression:

$$x _ { t } = 0 . 9 5 x _ { t - 1 } + \varepsilon _ { t }$$

with σe = 1. Table 1 gives the autocovariances of xt for the ideal business-cycle filter and for several approximations to this filter, i.e., several values of K.8 Looking first at the variance of xt, (the autocovariance at lag 0), we see that when K is small, so that the moving average covers only a few observations, the approximate filter produces a series whose variance is much smaller than the true or "exact" variance of 1.38. The approximation error for the filtered variance becomes quite small once K ≥ 12. This phenomenon can be understood by recalling that the K = 4 approximation to the dea o o   oso,  , o  y e Figure 3). For variables possessing Granger's [1966] typical spectral shape, such as this highly persistent AR(1) process, the effect of the compression is to filter out large components of frequencies for which there is substantial power in the original time series. As K rises and the accuracy of the approximate filter improves, this problem becomes smaller.

Interestingly, the variance computed from the approximate filter does not converge monotonically to the true variance as K rises. However, the departures from the true value are small for large values of K. A similar picture emerges for the other autocovariances: small values of K generally produce autocovariances smaller, in absolute value, than those produced by the ideal filter. Throughout, the approximation error is small for K ≥ 12.

### 3.2 Empirical effects of variation in K

This sub-section explores the effect of the length of the moving average on summary statistics for several post-war U.S. time series. To provide some information about how one's view of the macroeconomic "facts"" might depend on K, we have computed a set of summary statistics for several U.S. post-war quarterly macroeconomic time series using a range of values for K. Table 2 presents statistics on standard deviations, serial correlation coefficients, and contemporaneous correlations with GNP for K = od   1d ro e rd  t toiod   i io}d associated with the shortest filtered time series (i.e., the K = 20 filter), so differences in moments are not due to differences in the sample period. Summary statistics are also presented for three other filters—a centered moving average; the first-difference filter; and the Hodrick-Prescott [1980] filter, but we defer discussion of these results until Section 4.

tion moents, and were computed by applying the approximate bandpass filter's transfer function, {αk(ω)|2, to the spectral density of the first-order autoregression and then numerically integrating the result. -Iuqoq 9Th moil inoM oIisD .3fI3rnu1qxs  v,r!T er1T8  89DfI6i16vo3o3u 019w


<!-- p:13 -->


Table 2-A shows that one commonly-used measure of volatility—the standard deviation—is sensitive to the choice of K. Specifically, the measured volatility of v      s    s t t s  ss  ) som  s      sre      ows that there is little effect of increases in K on the standard deviations of the filtered time series for K ≥ 12. These results are consistent with the results obtained above for the AR(1): small values of K yielded low variances, while a good approximation was obtained for K ≥ 12.

Table 2-B presents serial correlation coefficients. As with the standard deviations, the serial correlations of the filtered time series depend on K. In particular, this measure of persistence is uniformly lower for the smallest value of K, compared with the largest. The reason, once again, can be traced to the effects of leakage and compression for small K on the filtered time series. Since the most persistent components of economic time series occur at the lower frequencies, the effect of compression in particular is to reduce the measured persistence of the filtered time series. As with standard deviations, the problem is most severe for K = 4, and there is little change for K ≥ 12.

Table 2-C presents results for the contemporaneous correlation of various aggregates with GNP, which is one commonly used measure of the comovement of a variable with the business cycle. This table shows that there is a tendency for a variable's correlation with GNP to increase as K increases, although this is not uniformly true. As before, there is a tendency for the estimated moments not to change much for K ≥ 12. Overall, our results suggest that summary statistics computed from the key macroeconomic time series are largely invariant to further improvements in the approximate business cycle filter beyond K = 12.

### 3.3 Inspecting the results for GNP

Figure 4 displays the results of applying five filters to the natural logarithm of gross national product. Throughout the four graphs, we use the band-pass business-cycle filter with K = 12 as our reference point: it the dashed line which is present in all of the graphs. The common sample period for these graphs is 1947-1993, but since we use K = 12 we lose three years of data at each end of the plots for the band-pass and high-pass filters.


<!-- p:14 -->


The First Difference Filter: Panel A of Figure 4 shows the quarterly growth rate of real GNP vs. the band-pass filter. The first-difference filter's heavy weight on on n n    n   snn ohce filtered time series. There is little correspondence between the time series produced by the first-difference and the band-pass filters.

The Hodrick-Prescott Filter: Panel B of Figure 4 plots Hodrick-Prescott filtered real GNP. There is a very close correspondence between the cycles isolated by this filter and those generated by the band-pass filter, although the Hodrick-Prescott filtered series is somewhat less smooth.

The High Pass Filter (H Pk(32)): Panel C displays a high-pass filter constructed using our procedures which isolates periodic components of 32 quarters (eight years). We have chosen the same K value for this filter as for the reference band-pass filter, so that the panel simply illustrates the effect of the smoothing of high frequency components introduced by our band-pass filter. For GNP, the panel makes clear that this smoothing out of irregular components has little effect on the overall volatility.

The Deviation from 5 year Moving Average Filter: Finally, Panel D displays deviations from a moving average. As with the Hodrick-Prescott filter and the high pass filter, the correspondence with the band-pass filter is quite close, with the moving average filter being somewhat more volatile.

### 3.4 Inspecting the results for inflation

In Figure 5, we present the results of applying the same five filters to the inflation rate. As before, the solid line in each panel is the BPk(6, 32) business-cycle filter.

The First Difference Filter: Panel A of Figure 5 shows the quarterly growth rate of inflation vs. the band-pass filter. As before, the first difference filter produces a highly volatile time series which bears little resemblance to the band-pass filter.

The Hodrick-Prescott Filter: Panel B of Figure 5 plots Hodrick-Prescott filtered real GNP. In contrast to the results for GNP, there is a notable difference between the Hodrick-Prescott filter and the band-pass filter. The reason is that inflation contains important high-frequency components which are passed by the HodrickPrescott filter, but which are removed by the band-pass filter. GNP, by contrast, does not have important variation at high frequencies.

The High Pass Filter (H Pk(32)): Panel C displays results for the H P12(32) filter. Like the Hodrick-Prescott filter, this filter passes the high-frequency components of inflation, leading to a more volatile filtered time series compared with that produced by the band-pass filter (0.48 for the high-pass filter, versus 0.32 for the band-pass filter over this sample period).

The Deviation from 5 year Moving Average Filter: Finally, Panel D displays deviations from an equally-weighted moving average. As with the Hodrick-Prescott filter and the high pass filter, the correspondence with the band-pass filter is weaker when we consider inflation compared with GNP. Once again, the reason is that highfrequency variation is much more important as a source of overall variation in inflation, compared with GNP.


<!-- p:15 -->


#### 4 Detailed Comparison with Other Filters

This section compares the properties of our proposed business cycle filter with other commonly used filters. We evaluate each filter in terms of its ability to achieve the following characteristics which we have argued are necessary for a "good" businesscycle filter: (i) ability to remove unit roots; (ii) absence of phase shift; (iii) ability to isolate business cycle frequencies without re-weighting components at the desired frequencies. Further, since model evaluation involves comparison of model moments with moments computed from the data, it is desirable that a business-cycle filter be easily (and consistently) applied both to the data and to economic models.

### 4.1 Removal of linear trends

Although the removal of linear (or log-linear) trends historically was a standard method for separating trends from cycles, a large and growing body of evidence suggests that many macroeconomic time series contain unit root (stochastic trend) components which would not be removed by this procedure. Primarily for this reason, this approach to detrending has fallen out of favor in empirical macroeconomic investigations. Although this procedure does not induce phase shift, nor does it re-weight frequencies, the failure to remove unit root components from the data means that linear detrending is undesirable for most macroeconomic time series.

### 4.2 The first-difference filter

The first-difference filter extracts the cyclic component yf from a time series yt as follows: yi = (1 - L)yt. It is evident that this filter removes unit root components from the data; for this reason, use of the first-difference filter has been popular in recent years. However, there are several problems with this filter with respect to the criteria listed above. First, because this filter is not symmetric, it alters timing relationships between variables (i.e., there is phase shift for this filter). Second, this filter involves a dramatic re-weighting of frequencies. Figure 6-A plots the frequency response function for this filter; the first-difference filter re-weights strongly toward the higher frequencies, while down-weighting lower frequencies. If the goal of a business cycle filter is to isolate fluctuations in the data which occur between specific periodicities, without special emphasis on any particular frequency, the first-difference filter is a poor choice.


<!-- p:16 -->


### 4.3 The Hodrick-Prescott filter

Use of the business cycle filter proposed by Hodrick and Prescott [1980] has grown dramatically in recent years, especially in investigations involving the quantitative equilibrium approach to constructing aggregative models The properties of this filter were previously studied by King and Rebelo [1993], and the following discussion borrows heavily from their analysis.

The infinite sample version of the Hodrick-Prescott filter defines the cyclic component of a time series yt as follows:

$$y _ { t } ^ { c } = \left ( \frac { \lambda ( 1 - L ) ^ { 2 } ( 1 - L ^ { - 1 } ) ^ { 2 } } { 1 + \lambda ( 1 - L ) ^ { 2 } ( 1 - L ^ { - 1 } ) ^ { 2 } } \right ) y _ { t }$$

where λ is a parameter which penalizes variation in the growth component (for quarterly data, Hodrick and Prescott recommend a value of λ = 1600). From this equation we see that the Hodrick-Prescott filter removes unit root components from the data (in fact, it will remove nonstationary components that are integrated of order four or less). Further, the filter is symmetric so there is no phase shift. Expanding equation (10) gives the following time domain representation of the growth component extracted by the Hodrick-Prescott filter (see Appendix A to King and Rebelo [1989] for the derivation):

$$y _ { t } ^ { \varrho } = \frac { \theta _ { 1 } \theta _ { 2 } } { \lambda } \left [ \sum _ { j = 0 } ^ { \infty } \left ( A _ { 1 } \theta _ { 1 } ^ { j } + A _ { 2 } \theta _ { 2 } ^ { j } \right ) y _ { t - j } + \sum _ { j = 0 } ^ { \infty } \left ( A _ { 1 } \theta _ { 1 } ^ { j } + A _ { 2 } \theta _ { 2 } ^ { j } \right ) y _ { t + j } \right ]$$

where A1 and A2 depend on θ1 and θ2; the coefficient A1θi + A2θ¿ is a real number for each j, and A1 and A2 are complex conjugates.9

As noted by King and Rebelo, the Fourier transform of the cyclical component of the Hodrick-Prescott filter has a particularly simple form:

$$\tilde { C } ( \omega ) = \frac { 4 \lambda ( 1 - \cos ( \omega ) ) ^ { 2 } } { 1 + 4 \lambda ( 1 - \cos ( \omega ) ) ^ { 2 } }$$

Thus the cyclical component of the Hodrick-Prescott filter places zero weight on the zero frequency (Č(0) = 0), and close to unit weight on high frequencies (Č(π) = 16λ/(1 + 16λ)). Figure 6-B plots the frequency response function of the HodrickPrescott filter for λ = 1600. Visually, this filter looks remarkably like an approximate high-pass filter with cutoff frequency ω = π/16.

In terms of the objectives that we specified for our filter design problem, the Hodrick-Prescott cyclical filter has several desirable features. First, it is a symmetric filter so that no phase shift is introduced. Second, it has trend reduction properties: it places zero weight at the zero frequency or, equivalently, contains multiple differencing operations. Third, with λ = 1600, it approximates the high pass filter HP∞(32) reasonably well since its gain rise sharply from near zero to near unit in the vicinity of the cutoff frequency ω = π/16. However, since the Hodrick Prescott filter of equation (10) is an infinite order moving average, some modification is necessary in order to apply it to data. We return to discussion of this topic in section 5 below.

9Equation (11) makes it clear that the Hodrick-Prescott filter is a two-sided moving average, as are several of the filters we consider. This equation also shows that the moving average is of infinite order, so that in empirical applications some approximation to this filter is required. We discuss the issue of approximation of the Hodrick-Prescott filter in section 5 below; the discussion here focuses on the exact Hodrick-Prescott filter.


<!-- p:17 -->


### 4.4 Moving averages

Another widely used method of detrending economic time series is to define the growth or trend component as a two-sided or centered moving average, with the cyclic component defined in the usual way as the deviation of a particular observation from the trend line. That is: the growth or trend component is formed as

$$y _ { t } ^ { g } = \frac { 1 } { 2 K + 1 } \sum _ { j = - K } ^ { K } y _ { t - j } .$$

Thus the cyclic component of yt is generated as yi = a(L)yt with ao = 1 − 1 2K+1 k+1 for j = 1, ,..., K. This filter places zero weight at the zero and aj = a−j = 2 2K+1 frequency since Σ ak = 0, and is symmetric. Figure 6-C plots the gain for the centered moving average filter for several values of K. The general shape of this filter is very similar to that of the approximate high-pass filter, plotted in Figure 6-D, although the "side-lobes" are more exaggerated for the moving average filter.

### 4.5 A high-pass flter

We have defined a high-pass business-cycle filter, HPk(32), as a filter which passes components of the data with periodicity less than or equal to 32 quarters. Figure 6-D plots the gain for this filter for several values of K. As with the moving average filter, this filter yields a good approximation to an ideal high-pass filter for sufficiently large values of K (i.e., K ≥ 12).

### 4.6 Comparisons across filters

Table 2 shows how application of these alternative filters affects moments computed from several postwar U.S. time series. We focus on three set of moments of particular interest to business-cycle analysis: volatility; persistence; and correlation with output.

Volatility. Table 2-A presents volatility statistics. As discussed earlier, the band-pass filter with K ≥ 12 yields a very good approximation to the ideal bandpass filter. For this reason, we regard the statistics computed with the K = 20 band pass filter as the best measure of business-cycle volatility, and then compare the other filters to this benchmark. Except for inflation, which we discuss separately below, a clear pattern emerges. The Hodrick-Prescott filter produces volatility statistics that exceed those of the ideal band-pass filter, although in many cases not by a large amount. The moving average filter produces volatility statistics that are larger still, although again the changes are not dramatic. The first difference filter, by contrast, produces volatility statistics that are smaller—in many cases, much smaller-than those produced by the band-pass filter. Having studied the gain functions of these filters, these results are easy to understand. The Hodrick-Prescott and moving average filters are rough approximations to a high-pass filter, which means that retain some high-frequency volatility which is removed by the band-pass filter. These macroeconomic time series do not have a great deal of power at high frequencies, so including these components leads to only small increases in the volatility of the filtered time series. The first difference filter produces smaller measures of volatility because it removes more of the low-frequency components of the time series than the band-pass filter, while re-weighting the frequencies to emphasize the higher frequencies. For all the variables studied except inflation, most of the power is at the lower frequencies.


<!-- p:18 -->


The pattern described above is reversed for inflation: here, the first-difference filter produces the highest measure of cyclic volatility. As discussed in section 3.4 above, inflation contains sizable high-frequency components—components which are emphasized by the first-difference filter. This also explains why the moving average and Hodrick-Prescott filters produce significantly higher volatility measures compared with the band-pass filter: the band-pass filter removes the high-frequency components, while these alternative filters do not.

Persistence. Table 2-B presents statistics on the first-order autocorrelation of filtered macroeconomic time series. As before, we take the band-pass filter (for K ≥ 12) as our benchmark. Compared with this benchmark, each of the other filters produces a lower measure of persistence. Excepting, once again, the inflation series, the differences are relatively small for the moving average and Hodrick-Prescott filters. However, the first-difference filter produces dramatically smaller measures of persistence compared with the other filters. Once again, this is due to the fact that the first-difference filter removes more of the highly-persistent, low-frequency comn o-ns --n n msn ns nss before, the inflation series behaves differently than the other time series, because of its important high-frequency components. With the emphasis on these components provided by the first-difference filter, the measured persistence of inflation is actually negative!

Correlation with GNP. Finally, Table 2-C provides statistics on the correlation b-at   a  e     es a e erage and Hodrick-Prescott filters produce statistics that are roughly similar to those computed using the band-pass filter. The first-difference filter produces correlations that are, in many cases, significantly smaller (in absolute value). Overall, researchers using the band-pass filter, the moving average filter, or the Hodrick-Prescott filter on quarterly postwar U.S. time series are likely to obtain a similar impression of the nature of business cycles. However, use of the first-difference filter will yield a markedly different view of the central business cycle "facts."


<!-- p:19 -->


In general, the first difference procedure produces filtered time series with lower volatility than those generated by the band-pass filters or the Hodrick-Prescott filter. This is a direct consequence of the fact that the first-difference filter downweights the lower frequencies relative to the alternative filters. For the same reason, the firstdifference filter produces time series which exhibit much lower persistence than those pro s   o   (  s so   lso much lower (Table 2-C).

#### 5 Comparing HP's

In this section, we undertake a detailed comparison of the Hodrick-Prescott filter with high pass filters constructed using our approach. For the purposes of many users of the Hodrick-Prescott filter, we shall conclude that our high-pass filter is better in two important dimensions: its ease of application to data sampled at frequencies other than quarterly, and its appropriate treatment of observations near the endpoints of the sample.

### 5.1 The quarterly HP filters can be very close

The first observation is that our H P12(32) filter and the conventional Hodrick-Prescott filter give essentially similar results for quarterly GNP, thus reinforcing the idea discussed in the previous section—that the Hodrick-Prescott filter is a reasonable approximation to the band-pass filter. This result is suggested by comparison of panels C and D of figure 6, discussed in section 3.2 above: the two series look very much like each other. In fact, the correlation of the Hodrick-Prescott cyclical component and the H P12(32) cyclical component is 0.994 over the common sample period.

### 5.2 The Hodrick-Prescott filter in finite samples

Many individuals currently use the Hodrick-Prescott filter with λ = 1600 to define cyclical components of quarterly economic time series. One main rationale for this, suggested by Prescott [1986], is that the filter is approximately a band-pass filter that passes cyclical components of periodicity greater than eight years (32 quarters). The results presented above suggested that there is indeed a close correspondence between alternative HP filters.


<!-- p:20 -->


To apply the Hodrick-Prescott cyclical filter to data, one strategy would be to truncate its weights at some fixed lag K, which would be analogous to our approximation of the ideal band-pass filter. However, in actual practice, an alternative procedure is typically used. This procedure has the apparently attractive feature that there is no loss of data from filtering. That is, for a time series yt for t = 1, ...T, the Hodrick-Prescott procedure produces estimates of the cyclical component, y, for t = 1,...T.

To understand this result, it is useful to return to the original derivation of the Hodrick-Prescott filter as the solution to a specific econometric problem, which is essentially to find the optimal estimates of trend and cycle corresponding to a particular known probability model. If we let yτ denote the trend component and continue to let y denote the cyclical component, this probability model is that trend and cycle are driven by independent white noises (ηt and €t respectively) and that their dynamics are ∆2yτ = ηt and yi = €t. If one knows the relative magnitude of σ2 and σ , then it is possible to extract estimates of yτ and y¿ at each date of a finite sample t = 1, ...T. Further, these estimates are simply weighted averages of the original data, so that the cyclical component at date t is:

$$y _ { t } ^ { c } = \sum _ { h = 1 } ^ { T } d _ { h t } y _ { h } . \\$$

While this derivation makes the date t cyclical component a moving average of the data, the linear filter is not time-invariant: the weights depend on the date t as well as the lead/lag index h. However, the algorithm that we use for computing the HodrickPrescott filter makes it easy to recover the coefficients dht so that we can study their properties. One feature that emerges is that for each date t, Σh=1 dht = 0 so that, in this fashion, the time-varying linear filter displays trend reduction properties at every date.10

To begin our more detailed look at the time-varying filter, Figure 7 plots the gain of the linear filter dt(L) = Σh=1 dhtL(h−t) for a range of dates t = {1,2,3}, {4,6,8},

10We implement the finite sample Hodrick-Prescott filter as follows. First, we stack the data Snen on dn  s e    on nn nr  vn n  to of "growth components", YG, to the data: Y = ΓYG. Third, we compute the vector of "cyclical components" as: YC = Y − YG = (I − Γ-1)Y. The matrix Γ is implied by the equations that link the growth components to the data. The general equation is:

$$y _ { t } = \lambda y _ { t + 2 } ^ { g } - 4 \lambda y _ { t + 1 } ^ { g } + ( 1 + 6 \lambda ) y _ { t } ^ { g } - 4 \lambda y _ { t - 1 } ^ { g } + \lambda y _ { t - 2 } ^ { g }$$

but this expression must be modified near the endpoints. For example, at the beginning of the sample, we use

$$y _ { 1 } = ( 1 + \lambda ) y _ { 1 } ^ { g } + ( - 2 \lambda ) y _ { 2 } ^ { g } + ( 1 + \lambda ) y _ { 3 } ^ { g }$$

$$y _ { 2 } = ( - 2 \lambda ) y _ { 1 } ^ { g } + ( 1 + 5 \lambda ) y _ { 2 } ^ { g } + ( - 4 \lambda ) y _ { 3 } ^ { g } + \lambda y _ { 4 } ^ { g }$$

and

and comparable modifications must be made near the end of the sample.


<!-- p:21 -->


{12,16,24}, {32,48,60}. These choices are motivated by the idea that we are studying a quarterly sample period of post-war size, so that there are about 180 observations, and we want to explore the effects of time variation near the endpoints and in the middle of the sample. (It is sufficient to look at the initial values because there is a symmetry property to the weights: d1T = dTı, etc.) These figures show that the dht coefficients at the beginning of the sample period are such that the dt(L) has very different properties than an exact high-pass filter: the gain functions differ sharply from each other for t = 1,2,3 and from the gain of the exact high-pass filter. (There is also phase shift near the endpoints, since dt(L) is not close to being a symmetric linear filter for t close to 1 or T). But as we move toward the middle of the sample period, the gain of the filter differs less sharply from one observation to the next and the overall filter looks closer to the ideal band-pass filter.

Another perspective on the extent of time variation in the filter weights is afforded by considering the effect of d(L) if it is applied to a specific data generating process. While it is feasible to undertake this for standard macroeconomic models, we opted for the simpler procedure of evaluating the effects of the filter on population variance of a first order autoregression, yt = ρ yt-1 + et with σ2 gives the variance by observation with the time-varying weight version of the HodrickPrescott filter (this variance should be viewed as calculated across many realizations of the time series generated by this first order autoregressive process). Although each observation has the same variance before filtering, time-variation in the filter applied to the process leads to different variances across observations. In fact, the change in the variance is not even monotonic, as suggested by the gain patterns in Figure 7.

This investigation thus suggests that the Hodrick-Prescott filter does not really generate as many useful estimates of the cyclical component as there are data points. Since the filter weights settle down after about observation 12, it would seem natural to drop 12 observations from the beginning and end of the sample period. But, then, there would be little reason to prefer the Hodrick-Prescott filter to our high-pass filter for quarterly data. Further, our HP filter embeds a mechanical rule for handling (i.e., dropping) endpoints.

### 5.3 HP Filters at other data frequencies

Is the Hodrick-Prescott filter an adequate approximation to a high-pass filter when used with data sampled at other frequencies? The answer to this question is important to researchers concerned with international and public finance questions—very often, the data used by these researchers are available only at the annual frequency. For our procedures, it is clear how to move between different data frequencies. For example, if we are considering results from the high-pass filter HPi2(32) with data at the quarterly frequency then the natural filter first filter to consider for annual data is H P3(8): we isolate the same frequencies (periodicities of eight years and higher) and we lose the same number of years of data at the ends of the sample.


<!-- p:22 -->


However, it is much less clear how to proceed with the Hodrick-Prescott method. The difficulty is that the Hodrick-Prescott filter requires the researcher to specify the "smoothing parameter," λ. For quarterly data, we found that λ = 1600 produces a reasonable approximation to a high-pass filter. For annual data, current empirical P [             s   aoe λ = 100 in their study of international business cycles). To investigate whether these values of λ yield a good approximation to a band-pass filter for annual data, figure 8 plots annual GNP filtered with our BP3(2,8) filter together with data filtered with the Hodrick-Prescott filter, for several values of λ.11 Examining the top two panels of figure 8 shows that the commonly-used values of λ = 400 and λ = 100 do not produce a filtered time series for GNP that closely resembles that produced by the band-pass filter. However, setting λ = 10, as in the third panel, produces a much better correspondence between the Hodrick-Prescott and band-pass filters. The bottom panel of this figure shows that little improvement is made when the length of the moving average is increased from K = 3 to K = 6. Figure 9 plots the gain for the Hodrick-Prescott filter for the three values of λ against the ideal filter. This figure shows why λ = 100 and λ = 400 produce such different pictures for fltered GNP compared with the optimal approximate band-pass filter: for these values of λ, the Hodrick-Prescott filter is a poor approximation to the ideal filter. In particular, these filters contain a great deal of "leakage" from low frequencies. That is: the λ = 100 and λ = 400 filters pass through nearly all of the components of the data with cycles between 9 and 16 years—components that most researchers would not identify as "business cycle" components. The approximation to the ideal band-pass filter is significantly better for λ = 10. However, even the λ = 10 filter contains significant "leakage" as well as significant "compression."12

The foregoing discussion concerned the properties of the exact Hodrick-Prescott filter. In practice, however, a finite-moving-average approximation to this exact filter must be used. Figure 10 plots the gain for the finite-sample version of the HodrickPrescott filter for λ = 10, by observation number, in a manner comparable with figure 7 presented earlier. As in the prior case, the finite-sample version of the filter produces serious departures from the ideal filter for the first three observations, but improves dramatically from observation 4 onward.

Overall, we find that our approximate band-pass filters are more straightforward tdpe , e  s o e e ne o p e se e ry when changing data frequencies. Second, we find that the commonly-used values of λ = 100 and λ = 400 for annual versions of the Hodrick-Prescott filter produce very poor approximations to a business-cycle filter. Third, we find that it is important to drop at least three data points from each end of the sample when using the HodrickPrescott filter on annual data, even if one chooses λ = 10.

11Since the shortest detectable cycle in a time series is one that lasts two periods, the annual business cycle filter passes components with cycle length between two and eight years. Note that, in this case, the band-pass filter is equivalent to a high-pass filter.

12Hassler et al. [1992] also argue that λ = 10 is the appropriate value for the smoothing parameter when applying the Hodrick-Prescott filter to annual data.


<!-- p:23 -->


#### 6 Summary and conclusions

This paper develops a set of approximate band-pass filters designed for use in a wide range of economic applications. The empirical focus of the paper is on isolating cyclic fluctuations in economic time series, defined as cycles in the data between specified frequency bands. We make detailed comparisons of our band-pass businesscycle filter with other commonly used filters, and evaluate these alternative filters in terms of their ability to isolate business-cycle fluctuations in the data. We found that linear detrending and first-differencing the data are not desirable business-cycle filters. On the other hand, deviations from an equally-weighted moving-average and Hodrick-Prescott filtering can, in some cases, produce reasonable approximations to an ideal business cycle filter. However, the optimal approximate band-pass filter that we develop in this paper is more flexible and easier to implement than these filters, while producing a better approximation to the ideal filter. While the main focus of our investigation is on construction of a business cycle filter, the results should be of more general interest since the defining periodicities may be readily specified by a researcher and applied to data at any observation frequency. Based on the results of this paper, we recommend three filters for use with quarterly and annual macroecononic data. These filters are illustrated in Figure 11 and the weights are given in Table 4.

For quarterly macroeconomic data, we recommend the "Burns and Mitchell" band-pass filter, which admits frequency components between 6 and 32 quarters, with K = 12. This filter renoves low-frequency trend variation and smooths highnr vr  g vc   e le va les Some macroeconomists, particularly those who have extensively used the HodrickPre   y  ,     n  y ncy components between 2 and 32 quarters with K = 12. Essentially, this filter removes the trend variation without removing the higher frequency irregular variation in the series. Relative to the Hodrick-Prescott method, this filter does involve dropping three years of data at the beginning and end of the sample; we have seen, however, tHhoo t e  t s l a  o   t tcot filter are rapidly changing near the ends of the sample, resulting in substantial distortions of these cyclical observations. Figures 11-A and 11-B provide plots of these weights, which are also given in the first two columns of Table 4.

Fu c-st q-s  -  hnccs an drs are equivalent. We accordingly recommend a single filter that admits periodic components between two and eight years, with K = 3. The filter weights are illustrated in Figure 11-C and given in table 4.

We have applied the filters constructed in this paper in some recent work, which provides an additional demonstration of their flexibility and usefulness. For example, Baxter [1994] uses the methods of this paper to study the relationship between real exchange rate differentials and real interest rates at low frequencies (trend components), medium frequencies (business cycle components) and high frequencies (irregular components). She concludes that prior studies have missed interesting relationships between these variables because a concern for producing stationary data led researchers to use the first difference filter. This procedure emphasized irregular (high-frequency) components where little relationship exists at the expense of the business cycle components where a striking, positive relationship emerges. In another application, King - t  se   i sd,  t s i ott tre lation of inflation and unemployment, appear strong at the business cycle frequencies even though they are hard to see in the original inflation and unemployment time series. This latter investigation uses monthly data and thus defines the business cycle periodicities as eighteen months to ninety-six months. It thus highlights one important strength of our approach: it is easy to alter the filter construction when the sampling frequency changes.


<!-- p:24 -->


In conclusion, the primary goal of this paper was to "build a better mousetrap' that is, to develop an approach to filtering of economic time series that is fast, flexible, and easy to implement. Our goal in this undertaking is to encourage empirical researchers to adopt a common approach to filtering, which will greatly aid in replication and comparison of results across researchers.


<!-- p:25 -->

#### A Trend-reduction properties of symmetric moving average filters

In this appendix, we consider how symmetric moving average filters reduce series with deterministic and stochastic trends to series that are stationary. In particular, we consider the filter:

$$a ( L ) = \sum _ { k = - K } ^ { K } a _ { k } L ^ { k } \\$$

where L is the lag operator. We impose two conditions, which are that the filter's coefficients sum to zero and that the filter is symmetric:

$$a ( 1 ) = \sum _ { k = - K } ^ { K } a _ { k } = 0$$

$$a _ { k } = a _ { - k } .$$

#### A.1 Deterministic trends

Consider a quadratic trend specification,

$$\tau _ { t } = \gamma _ { 0 } + \gamma _ { 1 } t + \gamma _ { 2 } t ^ { 2 } .$$

We are interested in the effects of applying the two sided moving average to this trend, ¿.e., creating a new variable

$$s _ { t } = a ( L ) \tau _ { t } = \sum _ { k = - K } ^ { K } a _ { k } \tau _ { t - k } = \gamma _ { 0 } \sum _ { k = - K } ^ { K } a _ { k } + \gamma _ { 1 } \sum _ { k = - K } ^ { K } a _ { k } ( t - k ) + \gamma _ { 2 } \sum _ { k = - K } ^ { K } a _ { k } ( t - k ) ^ { 2 } .$$

Writing out (t − k)2 as t2 − 2tk + k2 and consolidating terms we find that

$$s _ { t } = \{ \gamma _ { 0 } \sum _ { k = - K } ^ { K } a _ { k } - \gamma _ { 1 } \sum _ { k = - K } ^ { K } a _ { k } k + \gamma _ { 2 } \sum _ { k = - K } ^ { K } a _ { k } k ^ { 2 } \} + \{ \gamma _ { 1 } \sum _ { k = - K } ^ { K } a _ { k } - \gamma _ { 2 } \sum _ { k = - K } ^ { K } a _ { k } k \} t + \{ \gamma _ { 2 } \sum _ { k = - K } ^ { K } a _ { k } \} t ^ { 2 }$$

It follows that the general conditions for trend reduction—elimination of t for all values of γ1, γ2—are as follows:

$$\sum _ { k = - K } ^ { K } a _ { k } = 0$$


<!-- p:28 -->


$$\sum _ { k = - K } ^ { K } a _ { k } k = 0$$

The first of these conditions is imposed as eq. (15) above. Further, any symmetric

$$\sum _ { k = - K } ^ { K } a _ { k } k = \sum _ { k = 1 } ^ { K } ( a _ { k } - a _ { - k } ) k = 0$$

directly from the symmetry condition (ak = a\_k). Thus, eq. (18) is satisfied under our assumptions. Hence, the filters defined by eqs. (14)-(16) reduce series containing quadratic deterministic trends series to ones with no influence of time.13

An Example: The simplest example arises if K = 1. Then, there is a single free parameter of the specification a(L). In particular, symmetry implies that a1 = a-1 = -θ. The a(1) = 0 condition then implies that ao = 2θ. Applying this filter directly to eq. (14), we find that:

$$s _ { t } = 2 \ \theta \ \gamma _ { 2 } .$$

Thus, the influence of time is eliminated but there is not necessarily a zero-mean series as a result of the application of this filter.

Note that this filter may alternatively be written as:

$$a ( L ) = \theta [ ( - L ^ { - 1 } + 2 - L ) ] = \theta [ ( 1 - L ^ { - 1 } ) ( 1 - L ) ] ,$$

which indicates that the basic trend reduction filter contains two differencing operations, a forward and backward difference. It is this property which permits it to remove the influence of time from eq. (14). We will see next that this "double difference" property holds for all members of the class.

#### A.2 Stochastic trends

We now consider the "differencing operations" implicit in more general trend reduction schemes. We write:

$$a ( L ) = \sum _ { k = - K } ^ { K } a _ { k } L ^ { k } = \sum _ { k = - K } ^ { K } a _ { k } L ^ { k } - a _ { k } = \sum _ { k = 1 } ^ { K } a _ { k } ( L ^ { k } + L ^ { - k } - 2 )$$

The first equality follows from assumption (15), Σk=-κ ak = 0. The second follows from the symmetry assumption (16), ak = a-k.

Now, consider the individual terms in the preceding sum. We can write:

13If we also wish to require that there is a zero mean for the series st, then we must also require be removed after filtering the series of interest.


<!-- p:29 -->


$$( L ^ { k } + L ^ { - k } - 2 ) = - ( 1 - L ^ { k } ) ( 1 - L ^ { - k } ) .$$

We know that (1 − Lk) = (1 − L)[1 + L + L2 + ... Lk−1]. Further, with a little bit of algebra, we can show

$$[ 1 + L ^ { 1 } + L ^ { 2 } + \dots + L ^ { k - 1 } ] [ 1 + L ^ { - 1 } + L ^ { - 2 } + \dots + L ^ { - ( k - 1 ) } ] = \sum _ { h = - ( k - 1 ) } ^ { ( k - 1 ) } ( k - | h | ) L ^ { h } .$$

Hence, we can write:

$$a ( L ) = \sum _ { k = - K } ^ { K } a _ { k } L ^ { k } = \sum _ { k = - K } ^ { K } a _ { k } L ^ { k } - a _ { k } = - \sum _ { k = 1 } ^ { K } a _ { k } [ ( 1 - L ^ { k } ) ( 1 - L ^ { - k } ) ] = - ( 1 - L ) ( 1 - L ^ { - 1 } ) \psi _ { K } ( L )$$

where ψκ(L) = {Σk=1 ak Σk=−(k−1)(k − |h|)Lh]} and is a symmetric moving average -(k-1) with K - 1 leads and lags.

That is, our general moving average filter a(L) contains (at least) two differences, i.e., that it has the ability to render stationary I(2) stochastic processes.14 This accords with the finding on deterninistic trend specifications in the prior section.

## B Weights for the ideal low-pass filter

The inverse Fourier transform of the ideal low-pass filter implies that

$$b _ { h } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \beta ( \omega ) e ^ { i \omega h } d \omega = \frac { 1 } { 2 \pi } \int _ { - \underline { \omega } } ^ { \overline { \omega } } e ^ { i \omega h } d \omega ,$$

where the second line derives from the fact the β(ω) = 1 for |ω| ≤ ω and β(ω) = 1 for |ω| &gt; ω.

Hence, it follows that

$$b _ { 0 } = \frac { 1 } { 2 \pi } \int _ { - \underline { \omega } } ^ { \overline { \omega } } d \omega = \frac { \underline { \omega } } { \pi }$$

and that

$$b _ { h } = \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \beta ( \omega ) e ^ { i \omega h } = \frac { 1 } { 2 \pi } \left [ \frac { 1 } { i h } e ^ { i \omega h } \right ] _ { - \underline { \omega } } ^ { \underline { \omega } } = \frac { 1 } { \pi h } \sin ( \omega h )$$

where the last equality follows from 2i sin(x) = eix — e−ix.

14Since ψκ(L) is a finite-term moving average, it does not alter the stationarity properties of the series to which it is applied.


<!-- p:30 -->


#### C Optimal approximation of symmetric linear filters

In this section, we consider the optimal approximation of an ideal symmetric linear filter by a Kth order symmetric moving average. (This filter might be a low-pass filter, but it is useful to consider the more general case, for reasons that will become clear below). The problems is to minimize

$$Q = \, \int _ { - \pi } ^ { \pi } | \delta ( \omega ) | ^ { 2 } d \omega ,$$

with δ(ω) being the discrepancy between the exact and approximating filters at frequency ω, δ(ω) = β(ω) - α(ω). Some versions of the problem discussed in the text require that the approximating filter take on a specified value at the zero frequency, which we represent as α(0) = φ.

To solve this constrained maximization problem, we form the Lagrangian,

$$\mathcal { L } = Q + \lambda [ \phi - \alpha ( 0 ) ] .$$

The first order conditions are that:

$$\frac { \partial \mathcal { L } } { \partial a _ { 0 } } = \frac { \partial Q } { \partial a _ { 0 } } - \lambda = 0$$

$$\frac { \partial \mathcal { L } } { \partial a _ { h } } = \frac { \partial Q } { \partial a _ { h } } - 2 \lambda = 0 \text { for } h \, = 1 , \dots K$$

$$\frac { \partial \mathcal { L } } { \partial \lambda } & = \phi - \alpha ( 0 ) = 0 . \\$$

To evaluate ∂Q/∂ah, it is desirable to proceed as follows. First, we compute ∂|δ(ω)|/∂ah. Second, we compute the relevant integrals.

#### C.1 Computation of the partial derivative

The partial derivative of interest is found as follows. We begin by noting that:

$$\frac { \partial } { \partial a _ { h } } \left [ \delta ( \omega ) \delta ( - \omega ) \right ] & = \frac { \partial \delta ( \omega ) } { \partial a _ { h } } \delta ( - \omega ) + \delta ( \omega ) \frac { \partial \delta ( - \omega ) } { \partial a _ { h } } = 2 \ \delta ( \omega ) \frac { \partial \delta ( \omega ) } { \partial a _ { h } } , \\$$

where the second equality follows from the symmetry of the discrepancy measures, δ(ω) = β(ω) − α(ω) = β(−ω) − α(−ω) = δ(−ω).

Further, since the frequency response function of the approximating filter is α(ω) = Σh=-K ahe-iwh, it follows that:

$$\partial \delta ( \omega ) / \partial a _ { 0 } = - 1$$


<!-- p:31 -->


and that

$$\partial \delta ( \omega ) / \partial a _ { h } = - ( e ^ { i \omega h } + e ^ { - i \omega h } ) \text { for } h = 1 , 2 , \dots K$$

These results imply that ∂Q/∂ah = ∫^ ∂|δ(ω)|/∂adω takes the form

$$\partial Q / \partial a _ { h } = - \int _ { - \pi } ^ { \pi } 2 \ \delta ( \omega ) d \omega \text { for } h = 0$$

$$\partial Q / \partial a _ { h } = - \int _ { - \pi } ^ { \pi } 2 \ \delta ( \omega ) ( e ^ { i \omega h } + e ^ { - i \omega h } ) d \omega \ \text {for} \ h = 1 , 2 , \dots$$

Our next task is to evaluate these integrals, which it turns out is best done by deriving a set of intermediate results.

#### C.2 Intermediate results

If we have a symmetric linear filter g(L) = Σh=-∞ ghLh with frequency response function γ(ω) = ∑h=-∞ ghe-iwh, then it follows that there are simple expressions for integrals of the form f ̄π γ(ω)dω and f−π γ(ω)(eiwj +e-iwj )dω for integer j. To evaluate these integrals, we make repeated use of the facts that ∫π eiwne-iwm dω = 0 for n ≠ m and ∫=π π eiwne-iwm dω = 2π for n = m, where n and m are integers.

Using this pair of results in the first integral, we find that:

$$\int _ { - \pi } ^ { \pi } \gamma ( \omega ) d \omega = \int _ { - \pi } ^ { \pi } \sum _ { h = - \infty } ^ { \infty } g _ { h } e ^ { - i \omega h } d \omega = 2 \pi \ g _ { 0 } \ .$$

since all terms integrate to zero for h ≠ 0. Using them in the second integral, we find that:

$$\int _ { - \pi } ^ { \pi } \gamma ( \omega ) ( e ^ { i \omega j } + e ^ { - i \omega j } ) d \omega = \int _ { - \pi } ^ { \pi } \sum _ { h = - \infty } ^ { \infty } g _ { h } e ^ { - i \omega h } ( e ^ { i \omega j } + e ^ { - i \omega j } ) d \omega = 2 \pi ( g _ { j } + g _ { - j } ) = 4 \, \pi \ g _ { j } .$$

#### C.3 Evaluation of the first order conditions

The K + 1 first order conditions, ∂Q/∂αh − λ = 0, then can be expressed as:

$$- 4 \pi [ b _ { 0 } - a _ { 0 } ] + \lambda = 0$$

$$- 8 \, \pi [ b _ { h } - \alpha _ { h } ] + 2 \lambda = 0 \text { for } h = 1 , 2 , \dots K .$$

and as and as

Hence, if there is no constraint on α(0), i.e., λ = 0, then it follows that the optimal approximate filter is simply derived by truncation of the ideal filter's weights. Notice that this result is quite general in that it applies for the approximation of any symmetric ideal filter, i.e., it does not make use of any properties of β(ω) except for symmetry.


<!-- p:32 -->


If there is a constraint on α(0), then λ must be chosen so that the constraint is satisfied. For this purpose, it is useful to write the FOCs as:

$$a _ { 0 } = b _ { 0 } + \theta \text { and } a _ { h } = b _ { h } + \theta , \text { for } h = 1 , 2 , \dots K ,$$

where θ = λ/(8π). Then, requiring that α(0) = Σh=-κ ah = φ, we find that the required value adjustment is

$$\theta = \frac { \phi - \sum _ { h = - K } ^ { K } b _ { h } } { 2 K + 1 } \, .$$

Again, the result is a general one. It implies that construction of the optimal approximating filter contains two steps: first, truncation of the ideal filter's weights and, second, addition of correction term θ which depends on the extent to which the truncation disturbs the desired zero frequency behavior.

Further, the form of this correction process makes clear the origins of some of the observations made in the main text. For example, it is easy to see that the constrained Kth order approximate band-pass filter is the difference between two constrained Kth order approximate low-pass filters. Since the ideal band-pass filter weights are simply differences between the weights of two low-pass filters, bh - bh,, it follows that the weights for an optimal truncated band-pass filter are (bh - bh) - [∑h=−K (bh − bh)]/[2K + 1]. As this may be rearranged as {bh + [1 − ∑k=\_K bh]/[2K + t tt   {t +     -  + } - { constrained approximate band-pass filter are simply the difference in the weights of the two constrained Kth order low-pass filters.


<!-- p:33 -->


#### D MATLAB programs

Following are the programs used to implement the approximate band-pass filters dv a veid    e  v   dd   l second program called FILTK.M. A replication diskette is available from the authors which contains these and other programs used to produce this paper.

#### Program name: BPF.M

function yf=bpf(y,up,dn,K);

```
Which contains thec and other frequency (e.g., 6)

                Program name: BPF.M

                function yf=bpf(y,up,dn,K);

                % bpf.m
                % Program to compute band-pass filtered series
                % Inputs are
                %  y:   data (rows = observations, columns=series)
                %  up:  period corresponding to highest frequency (e.g., 6)
                %  dn:  period corresponding to lowest frequency (e.g., 32)
                %  K:   number of terms in approximate moving average
                %  [calls flthk.n (filter with symmetric weights) as subroutine]
                x=[up dn];
                disp(' ')
                disp('bpf(y,up,dn,K): band-pass filtering of series y with symmetric MA(2K+1)')
                disp(' ')
                disp('                for additional information see: ')
                disp(' ')
                disp('                M. Baxter and R.G. King        ')
                disp(' ')
                disp('                Measuring Business Cycles:    ')
                disp('                Approximate Band-Pass Filters')
                disp('                for Microeconomic Time Series')
                disp(' ')
                disp('Filter extracts components between periods of: ')
                disp('    up   dn')
                disp(x)
                % pause(2)

                if (up>dn)
                disp('Periods reversed: switching indices up & dn')
                disp(' ')
                dn=x(1); up=x(2);
                end

```


<!-- p:34 -->


```
if (up<2)
 up=2;
 disp('Higher periodicity > max: Setting up=2')
 disp(' ')
end

% convert to column vector
[r c]=size(y);
if (r<c)
 y=y';
 disp('There are more columns than rows: Transposing data matrix')
 disp(' ')
end

% Implied Frequencies
ombar=2*pi/up;
ombar=2*pi/dn;

% An approximate low pass filter, with a cutoff frequency of "ombar",
% has a frequency response function
%
%  alpha(om) = a0 + 2*a1 cos(om) + ... 2*aK cos(K om)
%
% and the ak's are given by:
%
% a0 = ombar/(pi)                ak = sin(k ombar)/(k pi)
%
% where ombar is the cutoff frequency.

% A band-pass filter is the difference between two
% low-pass filters,
%   bp(L) = bu(L) - bl(L)
% with bu(L) being the filter with the high cutoff point and bl(L) being
% that with the low cutoff point.  Thus, the weights are differences
% of weights for two low-pass filters.

% Construct filter weights for bandpass filter (a(0)...a(K)).

akvec=zeros(1,1;K+1);

akvec(1)=(ombar-ombar)/(pi);  % weight at k=0
```


<!-- p:35 -->


```
for k=1:K;
  akvec(k+1)=(sin(k*omubar)-sin(k*omblar))/(k*pi); % weights at k=1,2,...,K
end

% Impose constraint on frequency response at om = 0
% (If high pass filter, this amounts to requiring that weights sum to zero).
% (If low pass filter, this amounts to requiring that weights sum to one).

if (dn>1000)
  disp('dn > 1000: assuming low pass filter')
  phi=1;
else
  phi=0;
end

% sum of weights without constraint
theta=akvec(1)+2*sum(akvec(2:K+1));
% amount to add to each nonzero lag/lead to get sum = phi
theta=phi-(theta/(2*K+1));
% adjustment of weights
akvec=akvec+theta;

% filter the time series
yf=filtk(y,akvec);

if (r<c)
  yf=yf;
end
--


Program_name: FILTK.M

function  yf=filtk(y,a);

% Filter data with a filter with symmetric filter with weights
% data is organized (rows=obs, columns=series)
% a=[a0 a1 ... aK];

K=max(size(a))-1;  % max lag;

T=max(size(y));    % number of observations;

```


<!-- p:36 -->


% Set vector of weights

avec=zeros(1,2*K+1); avec(K+1)=a(1); for i=1:K; avec(K+1-i)=a(i+1); avec(K+1+i)=a(i+1); end yf=zeros(y); for t=K+1:1:T-K yf(t,:)=avec*y(t-K:t+K,:); end quarterly data, 1947:1- 1993:1


<!-- p:37 -->


TABLE1 Effect of K on moments of an AR(1) process

| K        | Vfl10C0AL!flJCG f - 0   | Vfl10C0AL!flJCG f - 1   | Vfl10C0AL!flJCG f - 3   | Vfl10C0AL!flJCG f - 1   | Vfl10C0AL!flJCG f - 8   |
|----------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| 3        | ff03                    | ff01                    | ff01                    | ff00                    | ff00                    |
| 3        | OT                      | 00                      | 0.OJ                    | -if 0X                  | 000                     |
| 4        | ff43                    | ff33                    | 010                     | 0.31                    | 000                     |
| Q        | 0.8X                    | 0W                      | Ot3                     | -0.3                    | -0U                     |
| 8        | 04                      | 08]                     | O4                      | -ff31                   | -ff3t                   |
| T3       | 134                     | 131                     | O'8Q                    | ff08                    | 032                     |
| J        | T'Sô                    | FJQ                     | O1                      | ff03                    | O3                      |
| 30       | F3f                     | 110                     | 0Q                      | 003                     | ff4                     |
| 5t       | I5                      | 1.1 1                   | 0Q                      | 003                     | Ot\                     |
| 33       | 133                     | 150                     | 0 0t                    | O.0'1                   | O3                      |
| 8        | J3t                     | 150                     |                         | ff0'f                   | OtQ                     |
| QO       | 133                     | TJÔ                     | 0f                      | 003                     | 0t8                     |
| àO       | JThI                    | 150                     | 084                     | ff03                    | 0f                      |
| GXC1     | I                       | J33                     | 0.8                     | 0.O                     | -04                     |
| 110 flGL | 105Q                    | W                       | 3Q                      | W3                      | Q0                      |


<!-- p:38 -->


TABLE 2 Effect of filtering on monents:

#### A. Standard deviations

| AL1PJG          | : 1LflUCiOU bow' oi p&uq-b   | : 1LflUCiOU bow' oi p&uq-b - 8   | : 1LflUCiOU bow' oi p&uq-b - T   | : 1LflUCiOU bow' oi p&uq-b - JQ   | : 1LflUCiOU bow' oi p&uq-b - O   | ATOAJU   | bLCOU I-IoqL!c-   | qic1.cuc J!'   |
|-----------------|------------------------------|----------------------------------|----------------------------------|-----------------------------------|----------------------------------|----------|-------------------|----------------|
| Q1'Ib           | O'8f                         | 131                              | 1Q3                              | 1R                                | JRÔ                              | 1Ô       | TT                | 100            |
| cou: qflL1pJG2  |                              |                                  |                                  |                                   | c180                             |          |                   |                |
| cou2: uouqnpj   |                              |                                  | iio                              | TO                                | TO                               |          |                   | ox             |
| cou: qnucpjc    | O•33                         | Ot                               | oQo                              | 0R8                               | ORQ                              |          | OQQ               | ORO            |
| IUAC2UJGU       |                              | tJO                              |                                  | •TT                               |                                  |          |                   |                |
| HOflL2 bL bcLou | O3                           |                                  | OO                               | OtO                               | OtO                              | OfQ      | Of5               |                |
| EWbI0AWGIII     | OX1                          |                                  |                                  | fI                                | 1ct5                             |          | 1O                |                |
| FXBOLf2         |                              |                                  |                                  |                                   |                                  |          | 2R8               |                |
| JuJboLt         |                              |                                  |                                  |                                   |                                  |          |                   |                |
| Wccbou          |                              |                                  |                                  |                                   |                                  | TRT      |                   |                |
| QoAJbnLcpc      | o.o                          |                                  |                                  | TQ                                |                                  |          | 31                | 131            |
| QI4J qcjot      |                              | O3                               | O                                | OO                                | OX                               | JJ8      | OO                | OO             |
| JIJU&fiOU*      | 0T8                          |                                  |                                  |                                   |                                  | O4       | O                 | ORO            |

Notes: Application of these filters involves loss of data points at both ends of the sample. For consistency, the moments reported are for the truncated sample 1952:1 - 1988:1 (the longest period available for the K=20 band-pass filter). Except for starred variables, natural logs were taken before filtering.


<!-- p:39 -->


#### TABLE 2, cont'd.

#### B. First-order autocorrelation

| iVP1G          | : R11UCJ1J ou bou jo pruq-b UJtGL   | : R11UCJ1J ou bou jo pruq-b UJtGL - g   | : R11UCJ1J ou bou jo pruq-b UJtGL - 13   | : R11UCJ1J ou bou jo pruq-b UJtGL - IQ   | : R11UCJ1J ou bou jo pruq-b UJtGL - 30   | &AGLC OAJU   | LLG2COU J-oqucjc-   | qJIICLCUCG bTL   |
|----------------|-------------------------------------|-----------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|--------------|---------------------|------------------|
|                | o                                   | o 0.\                                   | 03 0•I                                   | 0•aJ                                     | 0oJ                                      |              | ot                  | oT               |
| cou: qnLpJc2   |                                     |                                         | oi                                       | o 03                                     | o 0T                                     | o 080        | 0Q                  |                  |
| cou: uouqnpjc  | o oT                                | 0Q og                                   |                                          | 00                                       | 00                                       |              | 0 o.gs              | o.3              |
| coIJ: qnUfJG   |                                     |                                         | 0ô 01                                    | 0                                        | 0                                        | 0ô           |                     | 010              |
|                | 0.81                                | 00                                      |                                          |                                          |                                          | 0J           | 08ô                 | 0tct             |
| H0flLbGLbCL20U | 080                                 | 08                                      | 0R                                       | 088                                      | 088                                      | 0J           | 08                  | 05Q              |
| EWbJoAWGLU     | ox ogt                              | 0 oa                                    | 03 os                                    | os                                       | os                                       | ooj          | oo                  |                  |
| EboLf2         | o                                   | ox                                      |                                          | 0ô1                                      | 0J                                       | o 0t         | 0Q                  |                  |
| JwboL          | 08t                                 | 0                                       | 0Q ooi                                   | oo                                       | oo                                       |              | os                  | -ou              |
| 4G GXboL42     |                                     | 0R                                      | 0                                        | 0X 0W                                    | 0&t                                      | 03           | 00                  | 0J               |
| Qo,j brncp     | o 08                                | o3                                      | 0àQ                                      | o                                        | oot 0Q                                   | 0Q           | 0t                  | o os             |
| QJ qcJOL       |                                     |                                         |                                          | 08Q                                      |                                          | ot           | oo                  |                  |
| J[JTJWOU*      | 0Q                                  | 0R3                                     | 08                                       |                                          | 0                                        | 058          | 030                 |                  |

Notes: Application of these filters involves loss of data points at both ends of the sample. For consistency, the moments reported are for the truncated sample 1952:1 - 1988:1 (the longest period available for the K=20 band-pass filter). Except for starred variables, natural logs were taken before filtering.


<!-- p:40 -->


#### TABLE 2, cont'd.

#### C. Contemporaneous correlation with GNP

| AL!PIG          | : tLnUCJOU I bonn OL p&uq-bi22 UUGL - 4   | : tLnUCJOU I bonn OL p&uq-bi22 UUGL   | : tLnUCJOU I bonn OL p&uq-bi22 UUGL   | : tLnUCJOU I bonn OL p&uq-bi22 UUGL - IQ   | : tLnUCJOU I bonn OL p&uq-bi22 UUGL - 30   | gACL1G yo/nJ   | bLGCOIT OqLC(-   | qJLGuCG J!Lt   |
|-----------------|-------------------------------------------|---------------------------------------|---------------------------------------|--------------------------------------------|--------------------------------------------|----------------|------------------|----------------|
| 0Mb             | F00                                       | 100                                   | J'OO                                  | o 100                                      | o 100                                      | 100            | o' 100           | 100            |
| co: qnuipj      |                                           |                                       |                                       |                                            |                                            | o              |                  |                |
| cou: uoIJqnLpJc |                                           | oo                                    | ogj                                   | or                                         |                                            |                | o                | ot             |
| cou: qnrpc      | o oo                                      |                                       |                                       |                                            |                                            | oo             | oo               | ot0            |
| I1WUr           |                                           |                                       | 08                                    | 083                                        | 08                                         | 08T            |                  |                |
| H0I1L bcL bcLou | o O'8                                     |                                       | 085                                   |                                            | O3                                         | 080            | o 080            | 0Q8            |
| EwbIo?mcul      |                                           |                                       |                                       |                                            |                                            |                |                  | oi             |
| EXbOI4          | o 033                                     |                                       |                                       | O5                                         | 033                                        | 058            | O5               | o 05T          |
| jwboi.          |                                           | o                                     |                                       |                                            |                                            | oxo            |                  |                |
| WGXb0U2         | -03Q                                      | -OtJ                                  | -Oi                                   | -OX                                        | -Ot5                                       |                | -OQ              |                |
| OOAfbflLcpG2    | 0U                                        | 0J0                                   | O5                                    | Ot                                         | OJ                                         | O8             | 053              | Ot             |
| QqGJ1OL         | O.O                                       | -01T                                  | -Ot                                   | -035                                       | -O5                                        | -038           | -O               | -0T1           |
| I11U!0U*        | O3                                        |                                       | OT                                    | O'30                                       | 032                                        | O3             |                  | OOX            |

Notes: Application of these filters involves loss of data points at both ends of the sample. For consistency, the moments reported are for the truncated sample 1952:1 - 1988:1 (the longest period available for the K=20 band-pass filter). Except for starred variables, natural logs were taken before filtering.


<!-- p:41 -->


TABLE3 Effect of Hodrick-Prescott filter with time-varying weights

| Op6LMJt!OU   | 1ULWUCG   |
|--------------|-----------|
| I            | F.X4Q8    |
| S            | usso      |
| 3            | 10353     |
| 4            | OO        |
| Q            | T1831     |
| 8            | J4O3      |
| 15           | JQ038     |
| JQ           | FQ1Q      |
| 54           | I•QQ14    |
| 35           | IQôQ      |
| 48           | IQ8       |
| QO           | IQôO      |
| o            | TQOO      |


<!-- p:42 -->


TABLE4 Moving-average weights for business-cycle filters

| I1   | Bb(Q3)   | llh(3)   | rn&g)   |
|------|----------|----------|---------|
| 0    | 05\X     | 045      | 0\4J    |
| I    | 03304    | 002XI    | -05010  |
| S    | 00838    | -0.0     | -0T3T   |
| 3    | 0.03J    | 0023ô    | 0.0J0   |
| 4    | 0J184    | 00T3     |         |
|      | 01015    | 004ô     |         |
| Q    | 00435    | 00440    |         |
|      | OOOJQ    | 003W     |         |
| 8    | 000J     | 003t8    |         |
| o    | -o'os    | -oosox   |         |
| JO   | -0OOJ    | 00544    |         |
| IT   | 00453    | -0OJàO   |         |
| 15   | 00Ik     | 00I3     |         |


<!-- p:43 -->


#### FIGURE 1: Ideal filters

<!-- p:44 -->


FIGURE 2: Constrained approximate low-pass filters 一

<!-- p:45 -->


FIGURE 3: Constrained approximate band-pass filters (6-32 quarters)

<!-- p:46 -->


FIGURE 5: Effects of alternative filters on inflation

<!-- p:47 -->


FIGURE 6: Alternative filters vs. an ideal high-pass filter (cutoff=32 quarters)

1

<!-- p:48 -->


FIGURE 7: The Hodrick-Prescott filter in finite samples

<!-- p:49 -->


FIGURE 9: Alternative annual Hodrick-Prescott filters

<!-- p:50 -->


FIGURE 11: Lag weights for business-cycle filters
