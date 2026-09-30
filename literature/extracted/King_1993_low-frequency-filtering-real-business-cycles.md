---
id: "King_1993_low-frequency-filtering-real-business-cycles"
source_pdf: "../pdf/King_1993_low-frequency-filtering-real-business-cycles.pdf"
source_filename: "King_1993_low-frequency-filtering-real-business-cycles.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/King_1993_low-frequency-filtering-real-business-cycles.references.md"
---

<!-- p:1 -->

## Low frequency filtering and real business cycles

### Robert G. King and Sergio T. Rebelo*

Rochester Center for Economic Research, Rochester, NY 14627, USA

Received November 1989, final version received December 1991

This paper discusses in detail the Hodrick-Prescott (1980) filter from time and frequency domain perspectives, motivating it as a generalization of the exponential smoothing filter. We show that the HP filter – when applied to large samples – contains a centered fourth difference and hence renders stationary time series that are difference-stationary' and, indeed, integrated of higher order.

However, our application of the HP filter to U.S. time series and to the simulated outcomes of real business cycle models leads us to question its widespread use as a unique method of trend elimination. We provide examples of how HP filtering dramatically alters measures of persistence, variability, and comovement.

## 1. Introduction

A hallmark of modern equilibrium business cycle theory is the view that growth, business cycles, and seasonal variations are to be studied within a unified framework. Even though rational economic agents are presumed to respond differently to shocks of varying duration, dynamic economic theory generally imposes concrete and extensive restrictions across frequencies. For one example, the manner in which agents respond to varying seasonal opportunities provides information about how they will respond to temporary opportunities during the course of business cycles. For another, the manner

*The authors are also affiliated with the University of Rochester (R. G. King) and Northwestern University, Portuguese Catholic University, and Bank of Portugal (S. T. Rebelo). They acknowledge financial support from the National Science Foundation. This research has benefited from discussions with Marianne Baxter, Gary Hansen, Robert Hodrick, Charles Plosser, Edward Prescott, Mark Watson, and David Wilcox. However, the authors are residual claimants with respect to errors of any sort.

0165-1889/93/$05.00 © 1993—Elsevier Science Publishers B.V. All rights reserved in which labor supply responds to the permanent wage and wealth changes during economic growth restricts responses at business cycle frequencies.


<!-- p:2 -->


Yet, beginning with Kydland and Prescott (1982), many studies in the real business cycle research area apply the HP filter - due to Hodrick and Prescott (1980) – to both time series generated from an artificial economy and actual data before making conclusions about the properties of the model and its congruence with observations. This practice corresponds to an implicit definition of the business cycle frequencies' and a decision to downplay the implications of the model at other frequencies, generally on the grounds that these represent growth rather than business cycles.

Reading the literature on real business cycles, one can easily come to the Gon  y y  , t o  a mno consequences for how one thinks about economic models and their consistency with observed time series. This paper demonstrates that the opposite conclusion is true: the practice of low frequency filtering has major consequences for both the stylized'facts of business cycles and the perceived operation of dynamic economic models. In fact, the mechanical application of the HP filter as a detrending procedure removes important time series o ru  s  s  ta es cycle phenomena.

Our motivation for this investigation derived from two sources, which we provide to the reader as puzzles to be investigated in the paper.

### 1.1. Implications for simulated time series

Oue une Se he  one a   oe hirn nan attempt to replicate results in Hansen's (1985) analysis of alternative labor supply elasticities in a basic real business cycle model.1

Table 1 provides population moments with and without HP filtering for an economy similar to the divisible labor model discussed in Hansen (1985). This model is one in which the single source of uncertainty is a trend-stationary technology shock to total factor productivity; it is detailed in King, Plosser, and Rebelo (1988a) and reviewed in section 5 below. From this table, it is clear that HP filtering alters the moment implications of the model in a quantitatively important manner, but that this influence is not constant across series. First, HP filtering, which extracts a component from the original series, lowers volatility as measured by the standard deviation columns in table 1. Second, HP filtering alters the relative volatilities (the standard deviation of a variable divided by that of output) of different series. In Table 1

1We thank Gary Hansen for providing some simulation results for unfiltered versions of his model (1985) that confirmed our conjectures that filtering, not model solution methods or model parameter values, lay at the heart of major differences in moments.


<!-- p:3 -->


Effects of filtering on population moments.

|                                                                        | I I I I I I I I                                      |
|------------------------------------------------------------------------|------------------------------------------------------|
|                                                                        | ~ ~5 c5 ~ ~5 c5 ~ ~5 I I I I I I I                   |
|                                                                        | I I                                                  |
| oO l~ l "~ ~ l ~ O~ ~ t~                                               | I                                                    |
| c5 c5 ~ ~5 ~ ~ ~ c5                                                    | ~ ~5 ~ ~ c5 c5 ~ ~5 I                                |
| eS ~ ~5 ¢5 ~5 ~5 ¢5 ~5                                                 | c5 ~5 c5 ~5 c5 c5 ~ ¢5                               |
| ~ ~ ~ t'q o~ ~ t~ "~ " oo oo t ~ q'~ oo oO ~.~ r.~ ~ ~ e5 c5 ~ ¢5 eS ~ | q'~ l "~ "~" "~" ~4~ ~ t¢~ ¢¢) ~5 ~5 ¢5 c5 ~ ~ ¢5 ~5 |
| "~" ~ t'q t~ ~t~ ~" t"q t ~ I                                          | I                                                    |
| c5 ~ ~ c5 c5 ~ ~ c5 I                                                  | c5 c5 ~ c5 ~ ¢5 c5 c5 I I I I I                      |
|                                                                        | c5 ~5 c5 c5 c5 ~ c5 c5 I I I I I I                   |
|                                                                        | t~ 00 t¢5 Ig~ ~4~ tg~ ~ t~ ~5 ~5 c5 ¢5 ~5 ~5 ~ ~     |
|                                                                        | c5 c5 c5 c5 c5 c5 c5¢5                               |
| ,d ~ e4 c5c5 c5 c5 ~                                                   | ,~c5 eq ~ ~ c5 c5c5                                  |
| t'q l ~ O0 ~ 0~ t'~ t ~ r'~ ,£-rq o~ t-,i eq eq ~ c5                   |                                                      |


<!-- p:4 -->


particular, it increases the relative volatility of investment and hours while lowering that of consumption, the real wage, and the capital stock. Third, the correlations between individual series and output – a measure of cyclical sensitivity – are generally altered by HP filtering. Notably, the cyclical variation in capital and labor input is dramatically altered by filtering. In the unfiltered economy, capital's correlation with output is 0.68 and labor's correlation with output is 0.79. With filtering, capital's correlation with output drops to 0.07 and labor's correlation with output rises to 0.98.

### 1.2. HP filtering of some U.S. post-war time series

Our second indication of the potential importance of HP filtering came from Marianne Baxter's empirical work [Baxter (1991) and Baxter and Stockman (1989)] on stylized facts of economic fluctuations in the United States and other countries.2 To provide some empirical background to our u b d b   n bi   hn snn unos a measure of aggregate economic activity and a measure of labor input. These are the logarithm of U.S. real gross national product, which we denote by y,, and the logarithm of per capita average hours worked, which we denote by N.

Like other low frequency filters, the HP filter can be viewed as extracting growth and cyclical components from the data.3 To start, let us focus on the (   a   d    s 'a deviation from a linear trend (so that the residual y' = y, − γt). If the growth component is assumed to be a deterministic trend, then the business cycle component is y. Under the HP filtering procedure, by contrast, the time series is permitted to have a stochastic growth component. In addition to extracting a linear trend – if one exists in the series under study - HP filtering also removes some additional variation whose properties depend on the series in ways detailed in section 2 below. The HP cyclical component is then defined as the difference between the original time series and the HP growth component.

Implications for real GNP: The first panel of fig. 1 plots the HP growth component versus the linear trend component of real gross national product. A relatively common reaction to this figure is that these two ways of removing

2We thank Marianne Baxter for suggesting the revealing examples contained in this section and for technical assistance in producing these results.

3In part, our discussion in this section and below involves the issue of how best to define business cycles. One possibility – which is sometimes discussed in evaluation of mechanical procedures such as the HP filter – would be to select some mechanical method that broadly replicated the stylized facts reported by NBER researchers following Mitchell (1927, 1951) and Burns and Mitchell (1941). However, preliminary work by King and Plosser (1989) leads us to believe that the NBER methods should be subject to some scrutiny as well.


<!-- p:5 -->


%

Trends in Output Per Capita

-3.8

Trend

RLinear Trend

-4.2

-4.4

-4.6

45

50

55

60

65

70

75

80

85

90

date

HP Growth Component &amp; Linear Trend Residual

20

10

HP Trend

0

Residual

-10

Growth

Component

-20

45

50

55

80

65

70

75

80

85

06

date

HP Cyclical Component

20

10

0

-10

-20

45

50

55

60

65

70

75

80

85

90

date

Fig. 1


<!-- p:6 -->


rett  it it  st e       so consequences for business cycle components.

In order to study the practical implications of alternative detrending methods, we construct the HP stochastic growth component by subtracting a linear trend from the HP growth component (taking the vertical difference between the series in the first panel of fig. 1). We call this component HP®(y,). Summarizing our definitions, the alternative decompositions are

$$y _ { t } = \gamma t + y _ { t } ^ { r } = \gamma t + H P ^ { c } ( \, y _ { t } ) + H P ^ { g } ( \, y _ { t } ) \, ,$$

i.e., the HP cyclical and stochastic growth components sum to the residual from the deterministic trend.

The second panel of fig. 1 makes clear that the HP stochastic growth component constitutes a major portion of the departure of output from a linear trend, so that the implied cyclical components arising from these two methods of trend elimination are very different both in terms of magnitude and persistence. Notably, the autocorrelation correlation coefficient of y at the annual lag is 0.72. The third panel of fig. 1 plots the HP cyclical component [HP(y,)] of real GNP, which is a rapidly fluctuating series, as may be judged from its autocorrelation structure. The autocorrelation of HP(y,) at a year lag (four quarters), for example, is only 0.09, which is an order of magnitude smaller than the autocorrelation coefficient for y' at the same lag.

Implications for GNP and labor input: The first panel of fig. 2 plots yi versus the departures of our labor input measure from its mean (i.e., N, — Ñ). There is not a strong relationship: the contemporaneous correlation o y y    o c yo   on output and hours in the second panel of fig. 2, there is a striking coincidence: the contemporaneous correlation is 0.86.

### 1.3. Outline of our analysis

To this point, we have shown that low frequency filtering - using the Hodrick and Prescott (1980) filter – has important implications for moments of U.S. time series and a simulated real business cycle model. In developing an explanation of the origin of these results and their practical consequences for business cycle research we proceed as follows. In section 2 we first discuss what linear filtering is and then review some facts about linear filters. In section 3 we derive the HP growth and cyclical filters as a direct generalization of the well-known exponential smoothing filter of Brown (1962). In section 4 we investigate the conditions under which the HP filter is an bpr     r  r    r  al aa uss s s us s uo uts s us s uste by section 3. Section 6 is a brief summary and conclusion.


<!-- p:7 -->

Hours - mean and Output - linear trend

0.2

0.1

Output

0

Hours

-0.1

-0.2

1945

1950

1955

1960

1965

19970

1975

1980

1985

1890

date

HP cyclical components of Output and Hours

0.2

0.1

Output

0

Hours

-0.1

-0.2

1945

1950

1955

1960

1985

1970

1975

1980

1985

1990

date

Fig. 2

## 2. Some facts about linear filtering

In this section, we provide an overview of analytical tools for studying the implications of linear filters. This discussion can be skipped by readers who are comfortable with introductory treatments of frequency domain methods [e.g., Harvey (1981, ch. 3)]. Throughout our discussion in this section, we will focus our attention on a representative time series y,, which we treat as the logarithm of an original series so that its first difference is a growth rate.

In filtering y,, a researcher is motivated by one of several objectives: (i) extraction of a component such as a growth, cyclical, or seasonal component, (ii) transformation to induce stationarity, or (iii) mitigation of measurement error that is assumed to be particularly important at specific frequencies. We concentrate on the first two motivations, since a detailed treatment of measurement error would require grappling with details of a specific application.


<!-- p:8 -->


To focus our discussion, then, consider the idea that a particular economic model makes predictions about a business cycle' component of a time series and that the researcher views the series as containing both growth and business cycle components,

$$y _ { t } = y _ { t } ^ { 8 } + y _ { t } ^ { c } ,$$

where y% is the growth component and yc is the business cycle component. Representing yå as a moving average (possibly two-sided) of observed y, permits extraction of the growth component (y) and the cyclical component (y). That is, suppose that we assume that

$$y _ { t } ^ { \& } = \sum _ { j = - \infty } ^ { \infty } g _ { j } y _ { t - j } = G ( B ) \, y _ { t } ,$$

where B is the backshift operator with B"x, =x,-n for n ≥0. Then, since yc = yt − yå, it follows that yc is also a moving average of yt,

$$y _ { t } ^ { c } = \left [ 1 - G ( B ) \right ] y _ { t } \equiv C ( B ) \, y _ { t } .$$

In the language of filtering theory, G(B) and C(B) = [1 − G(B)] are linear filters.

In order to discuss why a specific linear filter may be described as a low frequency filter, we are led to consideration of the Fourier transform of a linear filter (also called the frequency response function of the filter). For example, the frequency response of the growth filter is

$$\tilde { G } ( \omega ) = \sum _ { j = - \infty } ^ { \infty } g _ { j } \exp ( - i j \omega ) \, ,$$

where i denotes the imaginary number √(-1) and where ω is frequency measured in radians, i.e., − π ≤ ω ≤ π.

Gain and phase decomposition: At a given frequency ω, the frequency response (ω) is simply a complex number, so that it may be written in polar form as Ġ(ω) = Γ(ω)exp(−iΨ(ω)), where Γ(ω) = |Ġ(ω)| and Ψ(ω) are real numbers for fixed ω. In these expressions and below, |x| denotes the modulus of x (the square root of the product of x and its conjugate). The gain of the linear filter, Γ(ω), yields a measure – at the specified frequency ω – of the increase in the amplitude of the filtered series over the original series. The phase, Ψ(ω), yields a measure of the time displacement attributable to the linear filter, again at the specified frequency ω. The frequency response unt ntd  (tn untn on  ta nto n on untion Ψ(ω) by replicating the preceding decomposition at each value of ω.


<!-- p:9 -->

a: Impact of Filtering--Increase in Gain

2

1

0

-1

-2

0

5

10

15

20

25

30

35

40

time

Fig. 3. ----original series, ——filtered series.

b:Impact of Filtering--Phase Shift

2

1

0

-1

-2

0

5

10

15

20

25

30

35

40

time

To take a concrete example, suppose that a time series is strictly periodic with a period of 2π/ω*. Then application of the linear filter G would simply alter the range of this periodic function by Γ(ω*) = |G(ω*)|, as illustrated in fig. 3a. Further, fig. 3b illustrates the hypothetical phase shift effect of a linear filter.

Symmetric filters: In our analysis, we will focus on filters that possess a symmetry property in that gj = g –j. For any such filter, it is possible to show that

$$\tilde { G } ( \omega ) = g _ { 0 } + 2 \sum _ { j = 1 } ^ { \infty } g _ { j } \cos ( j \omega ) ,$$

using the trigonometric identity 2 cos(x) = {exp(ix) + exp(−ix)}. Symmetric filters have the important property that they do not induce a phase shift, i.e., Ψ(ω) = 0 for all ω, since the Fourier transform (ω) is real for a symmetric gain


<!-- p:10 -->


1.5

1

0.5

0


ω*0.1

0.2

a: idealized low frequency filter

0.3

0.4

0.5

0.6

0.7

0.8

0.9

1

angular frequency (in fractions of pi)

b: implied cyclical filter

1.5

1

gain

0.5

0


ω*0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

1

angular frequency (in fractions of pi)

Fig. 4

filter. Thus, the gain function is equal to the frequency response, so that we use these terms interchangeably below.

Further, in the class of symmetric filters, it is easy to see that

$$\tilde { G } ( 0 ) = \sum _ { j = - \infty } ^ { \infty } g _ { j } = 1$$

is a necessary and sufficient condition for a filter to have the property that it has unit gain at zero frequency.4 Thus, by extension, the associated cyclical filter C(B) = [1 - G(B)] will place zero weight on zero frequency whenever G(0) = 1.

By restricting attention to symmetric filters, then, we can simply express their implications by plotting the gain for various values of ω. Fig. 4a depicts -n  ae a y es e e o os e un cies up to some maximum ω*. It has unit gain for frequencies 0 ≤ ω ≤ ω* and zero gain for ω* ≤ ω ≤ π. Fig. 4b shows the gain of its cyclical counterpart, C(B) = [1 – G(B)].5 This type of band pass' filter is a natural procedure for isolating the business cycle frequencies. In fact, Prescott (1986) describes the Ga l ar       b r r at eliminates all frequencies lower than eight years.

4This property obtains for symmetric filters since cos(0) = 1 and it follows directly that Ġ(0) = 1. Moreover, this property holds as well for nonsymmetric filters since exp(0) = 1 implies that (0) = 1 under the condition that the filter weights sum to unity.


<!-- p:11 -->


## 3. Analysis of some common linear filters

In many practical contexts, one frequently approaches the task of extracting unobserved components by solving a minimization problem. Two noted examples are the problem (ES) which leads to the exponential smoothing filters for growth and cyclical components and the problem (HP) which leads to the Hodrick-Prescott (1980) filters for growth and cyclical components. The HP filter has been widely used in the real business cycle literature, while the ES filter was employed by Lucas (1980) in his empirical investigation of the quantity theory of money. These two filters can be obtained as the solutions to the following problems:6

$$( E S ) \quad \min _ { \{ y _ { t } ^ { \ell } \} _ { t = 1 } ^ { T } } \sum _ { t = 1 } ^ { T } \left [ ( \ y _ { t } - y _ { t } ^ { 8 } ) ^ { 2 } + \lambda ( \ y _ { t } ^ { 8 } - y _ { t - 1 } ^ { 8 } ) ^ { 2 } \right ] ,$$

$$( H ) \min _ { \{ y _ { t } ^ { s } \} _ { i = 0 } ^ { T + 1 } } \sum _ { t = 1 } ^ { T } \left [ ( \ y _ { t } - y _ { t } ^ { s } ) ^ { 2 } + \lambda \left [ ( \ y _ { t + 1 } ^ { s } - y _ { t } ^ { s } ) - ( \ y _ { t } ^ { s } - y _ { t - 1 } ^ { s } ) \right ] ^ { 2 } \right ] .$$

In practice, the ES program would contain an additional parameter - a constant mean of the growth rate – to permit the minimal extraction of a deterministic linear trend for each chosen value of λ. The HP program automatically involves extraction of a linear trend component, since this specification involves no change in the growth rate. Thus, throughout our discussion, we proceed as though a linear trend had already been removed from data.

Each of these minimization problems contains a parameter λ that penalizes' changes in the growth component [in problem (ES)] or in the acceleration of the growth component [in problem (HP)]. Below, we will use the first-order conditions from these problems to characterize the associated linear filters. For the minimization problem (ES), the first-order condition takes the form

5As discussed in Koopmans (1974, pp. 176–185), it is not possible to apply that ideal filter to a finite length data set, since its construction requires an infinite number of weights. Truncation of these weights gives rise to leakage' from those frequencies for which the band pass filter is zero to those for which it is unity.

6Our formulation of the HP problem is slightly different from that originally presented in Hodrick and Prescott (1980), in terms of treatment of endpoints. However, this difference is unimportant given our focus on the infinite sample' version of the filter.


<!-- p:12 -->


$$0 = - 2 [ y _ { t } - y _ { t } ^ { g } ] + 2 \lambda [ y _ { t } ^ { g } - y _ { t - 1 } ^ { g } ] - 2 \lambda [ y _ { t + 1 } ^ { g } - y _ { t } ^ { g } ] .$$

For the minimization problem (HP), the first-order condition takes the form

$$0 = - 2 ( y _ { t } - y _ { t } ^ { g } ) + 2 \lambda [ ( y _ { t } ^ { g } - y _ { t - 1 } ^ { g } ) - ( y _ { t - 1 } ^ { g } - y _ { t - 2 } ^ { g } ) ] \\ - 4 \lambda [ ( y _ { t + 1 } ^ { g } - y _ { t } ^ { g } ) - ( y _ { t } ^ { g } - y _ { t - 1 } ^ { g } ) ] \\ + 2 \lambda [ ( y _ { t + 2 } ^ { g } - y _ { t + 1 } ^ { g } ) - ( y _ { t + 1 } ^ { g } - y _ { t } ^ { g } ) ] .$$

In each case, then, the first-order condition links yc = y, − y% to changes in the growth component in adjacent periods. Below, this shared characteristic will play an important role in analysis of the growth and cyclical filters associated with these minimization problems.

In studying the optimal linear filters that solve these first-order conditions, we will consider the limiting version that obtains as the historical record length (T) is driven to infinity. This results in relatively simple formulae describing the filters and provides the maximum opportunity for these to match the perfect low frequency filter described earlier. In this case, each of the first-order conditions can be written in the form F(B)y = y,. The F(B) polynomials associated with the two problems are:

$$F _ { E S } ( B ) & = - \lambda B ^ { - 1 } + ( 1 + 2 \lambda ) - \lambda B \\ & = \left [ \lambda ( 1 - B ) ( 1 - B ^ { - 1 } ) + 1 \right ] , \\ F _ { H P } ( B ) & = \left [ \lambda B ^ { - 2 } - 4 \lambda B ^ { - 1 } + ( 6 \lambda + 1 ) - 4 \lambda B + \lambda B ^ { 2 } \right ] \\ & = \left [ \lambda ( 1 - B ) ^ { 2 } ( 1 - B ^ { - 1 } ) ^ { 2 } + 1 \right ] .$$

In order to find the growth and cyclical filter, we need to invert F(B) since G(B) = [F(B)]−1 and C(B) = 1 − G(B) = [F(B) − 1]F(B)]−1. The details of this process are relatively easy for the ES filter but are more tedious for the HP filter.7

7See appendix A of the working paper version of this research, King and Rebelo (1989), for these calculations.


<!-- p:13 -->


### 3.1. Growth and cyclical components via exponential smoothing

The extraction of low frequency components via exponential smoothing has a long tradition in economics, having been employed - to cite only one example – in Friedman's (1957) research on the permanent income hypothesis. In contrast to that application, however, the problem (ES) leads to a two-sided exponential smoothing filter since we do not constrain yå to be a function solely of past history. Manipulating the relevant first-order condition for the ES filter, we find that

$$C ( B ) = [ F ( B ) - 1 ] [ F ( B ) ] ^ { - 1 } = \frac { \lambda [ 1 - B ] [ 1 - B ^ { - 1 } ] } { 1 + \lambda [ 1 - B ] [ 1 - B ^ { - 1 } ] } .$$

Thus, we find that the ES cyclical filter contains forward and backward differences. A key implication of this finding is that the ES filter would render stationary Nelson and Plosser's (1982) difference-stationary stochastic processes and also integrated processes of order two, whose growth rates are not stationary.

Our convenient expression for the cyclical filter's Fourier transform is

$$O u \text { convenient expression for the cyclanite $i$-fourer} u \\ \tilde { C } ( \omega ) = [ F ( \exp ( - i \omega ) ) - 1 ] / F ( \exp ( - i \omega ) ) \\ = \frac { \lambda [ 1 - \exp ( - i \omega ) ] [ 1 - \exp ( i \omega ) ] } { 1 + \lambda [ 1 - \exp ( - i \omega ) ] [ 1 - \exp ( i \omega ) ] } \\ = \frac { 2 \lambda [ 1 - \cos ( \omega ) ] } { 1 + 2 \lambda [ 1 - \cos ( \omega ) ] } , \\ \text {where the third equality makes use of the trigonometric identity}$$

where the third equality makes use of the trigonometric identity discussed earlier. Thus, the cyclical filter has zero weight at the zero frequency [since cos(0) = 1] and assigns a weight close to unity at high frequencies [since cos(π) = − 1, Č(π) = 4λ /(1 + 4λ), which is close to one for large λ]. Higher values of λ raise the gain closer to unity for each fixed frequency.

Analysis of the cyclical filter in the time domain is slightly messier. To undertake this analysis, we define θ to be the smallest root of F, i.e., F(θ) = F(θ−1) = 0. This parameter is related to λ by the equation θ = {(1 + 2λ) − [(1 + 2λ)2 − 4λ2]1/2}/(2λ), so that it is real and less than one for any λ &gt; 0. The growth filter can then be expressed as G(B) = F(B)−1 = (θ/λ)[1 − θB]−1[1 − θB−1]−1. From a straightforward expansion,

$$y _ { t } ^ { s } = \left [ \frac { ( \theta / \lambda ) } { 1 - \theta ^ { 2 } } \right ] \left [ \sum _ { s = 0 } ^ { \infty } \theta ^ { s } y _ { t - s } + \sum _ { s = 0 } ^ { \infty } \theta ^ { s } y _ { t + s }$$


<!-- p:14 -->


i.e., the growth component is a two-sided exponentially weighted moving average of the original series. Similarly, the cyclical filter can be expressed as

$$C ( B ) = \frac { \theta [ 1 - B ] [ 1 - B ^ { - 1 } ] } { \lambda [ 1 - \theta B ] [ 1 - \theta B ^ { - 1 } ] } \, ,$$

which also makes clear that the effects of second differencing [1 – B][1 – B−1] in the numerator are partly undone by the presence of [1 – θB][1 – θB-1] in the denominator. In fact, if θ were unity (which is true in the limit as λ → ∞), then numerator and denominator terms would cancel. In practical applications θ is closer to 0.9, so that while this filter will render stationary an integrated time series, it will generally preserve more low frequency content than the first difference filter.

Larger values of λ - which penalize changes in the growth component – lead to smoother growth components. Thus, they lead to values of θ closer to unity [in the limit as λ →∞, θ → 1 so that C(B) = 1, i.e., yi = y,].

### 3.2. Growth and cyclical filters via the Hodrick-Prescott method

It turns out that the HP filters are closely related to those derived above. Manipulating the relevant first-order condition, the HP cyclical filter C(B) may be written as

$$C ( B ) = \left [ F ( B ) - 1 \right ] \left [ F ( B ) ^ { - 1 } \right ] = \frac { \lambda [ 1 - B ] ^ { 2 } [ 1 - B ^ { - 1 } ] ^ { 2 } } { 1 + \lambda [ 1 - B ] ^ { 2 } [ 1 - B ^ { - 1 } ] ^ { 2 } } \, .$$

Hence, the HP cyclical filter is also capable of rendering stationary any ie s s ds o is is  e  en soies tts numerator.

As with the exponential smoothing filter explored earlier, it turns out that enor  ha G or or   nrl orr iiy simple form:

$$\tilde { C } ( \omega ) = \frac { 4 \lambda [ 1 - \cos ( \omega ) ] ^ { 2 } } { 1 + 4 \lambda [ 1 - \cos ( \omega ) ] ^ { 2 } } \, .$$

Thus, the cyclical component filter places zero weight on the zero frequency [Č(0) = 0] and close to unit weight on high frequencies [Č(π) = 16λ/(1 + 16λ)]. Increasing λ shifts the gain function upward, moving a given frequency's gain closer to unity.


<!-- p:15 -->


Developing time domain representations of the filter is once again more involved.8 The first-order condition F(B) may be factored into (λ/θ1θ2) × [(1 − θ1B)(1 − θ2B)(1 − θ1B−1)1 − θ2B−1)], where θ1 and θ2 are complex conjugates whose value depends on λ. (These parameters are the zeros of F that satisfy |θ| &lt; 1.) With this factorization, we can develop a two-sided moving average expression for the growth component

$$y _ { t } ^ { g } = \left [ \frac { \theta _ { 1 } \theta _ { 2 } } { \lambda } \right ] \left [ \sum _ { j = 0 } ^ { \infty } \left [ A _ { 1 } \theta _ { 1 } ^ { j } + A _ { 2 } \theta _ { 2 } ^ { j } \right ] y _ { t - j } + \sum _ { j = 0 } ^ { \infty } \left [ A _ { 1 } \theta _ { 1 } ^ { j } + A _ { 2 } \theta _ { 2 } ^ { j } \right ] y _ { t + j } \right ] ,$$

where the parameter A1 = [(1 − θ2/θ1)(1 − θ1)2(1 − θ1θ2)]−1 and A2 is the complex conjugate of A1.9 It may be shown that the coefficient [A1θ + A2θ¿] is a real number for each j and that A1 and A2 are complex conjugates. Hence, the growth component is a two-sided moving average involving a kind of double exponential smoothing'. Panel 3 of fig. 5 plots the filter weights of the cyclical filter for the λ = 1600 value that has most frequently been employed, following Hodrick and Prescott (1980). The rationale behind the choice of λ = 1600 is discussed in the next section.

Combining the results of this section, we conclude that the HP filter will render stationary series that are integrated (up to fourth order), but that it also removes substantial low frequency variation. On the other hand, the HP filter will preserve more low frequency content than the first difference which is commonly employed for the purpose of achieving stationarity. As in the case of the ES filter, this property derives from the fact that the (fourth) r  nn   o d    1- - - -  - 0) since the modulus of θ is about 0.9 with the smoothing parameter λ set equal to 1600. Another way to reach this conclusion is to examine Singleton's (1988, fig. 2) comparison of the squared gain of the HP and first difference filter.

### 3.3. Comparisons of ES and HP filters

There is a single parameter on which the gain of the ES and HP cyclical filters depends, the smoothing parameter. To compare the filters, we chose λ = 1600 for the HP cyclical filter and required that the gain of the HP and ES cyclical filters be equal at the frequency π/16, which corresponds to a period of 8 years (32 quarters).

8See appendix A of the working paper version of this research.

9The analogue expression for the case in which the length of the data set is finite can be obtained following the same type of procedure as in Nerlove et al. (1979, p. 416–421).


<!-- p:16 -->

The HP, ES and Bandpass Cyclical Filters

F(λ=1600)

KES

gain

0.5

Bandpass

0


0.05

0.1

0.15

0.2

0.25

0.3

0.35

0.4

0.45

0.5

frequency in radians (fractions of pi)

The HP cyclical Filter: Frequency Response

1

λ=400

/1600

gain

0.5

λ=3200

0


0.05

0.1

0.15

0.2

0.25

0.3

0.35

0.4

0.45

0.5

frequency in radians (fractions of pi)

Fig. 5

The HP cyclical filter: lag weights

filter weight

λ=1600

0.5

0

-0.5

-40

-30

-20

-10

0

10

20

30

40

time shift


<!-- p:17 -->


The results of this comparison are given in panel 1 of fig. 5 which depicts the gain functions of HP, ES, and band pass filters. The HP filter looks more like the ideal filter presented in fig. 4, since its gain function is more nearly zero for frequencies below π/16 and more near unity for frequencies above it.

## 4. Inverse optimal linear filtering 10

In this section we investigate the conditions under which the HP filter is an optimal linear filter in the sense of minimizing the mean square error as in Wiener (1949) and Whittle (1963).11

To answer this question we need to posit a time series model for the growth and cycle components. To maximize the chances of the HP filter being an optimal linear filter, we chose a time series representation for yc which is linear and in which innovations to the growth and cycle components are orthogonal, so that growth and business cycles are separate phenomena. In particular we will assume that yo and y% are generated by the following ARMA models:

$$A ^ { s } ( B ) y _ { t } ^ { g } = M ^ { s } ( B ) \varepsilon _ { t } ^ { g } , \quad A ^ { c } ( B ) y _ { t } ^ { c } = M ^ { c } ( B ) \varepsilon _ { t } ^ { c } ,$$

where ε% and ε are white noise processes whose variances are s2(εc) and s2(ε8). By assumption, the roots of the autoregressive polynomials lie outside the unit circle (stationarity) and the roots of the moving average polynomial lie outside the unit circle (invertibility). We assume that the innovations ε% and ε are serially uncorrelated and E[εε] = 0. Further, for convenience, we define the ratio of variances ψ = s2(ε°)/[s3(ε) + s(ε8)].

Whittle (1963, ch. V) shows that the optimal (two-sided) signal extraction filter for the cyclical component is12

$$C ^ { * } ( B ) = \frac { \Gamma _ { c c } ( B ) } { \Gamma _ { c c } ( B ) + \Gamma _ { g g } ( B ) } \, ,$$

where Γcc(B) is the autocovariance-generating function of the cyclical component and Γgg(B) is the autocovariance-generating function of the growth component. From the ARMA structure it follows directly that

10This problem was first posed to us by Mark Watson, who also provided useful hints abot how to solve it. However, Watson should not be held responsible for any potential errors in following these leads or for our interpretation of the results. Our discussion of this material benefited from the comments of David Wilcox.

12Whittle's analysis (1963) is limited to stationary ARMA processes. However, recent work extends these formulas to cases with unit roots [Watson (1986) provides a brief summary of Bell's (1984) work on these cases].

11The mean squared error is defined as MSE = (1/T)Στ=(c − yc)2, where yc is the true cyclical component and o its estimate.


<!-- p:18 -->


$$z ) = \frac { M ^ { c } ( z ) M ^ { c } ( z ^ { - 1 } ) } { A ^ { c } ( z ) A ^ { c } ( z ^ { - 1 } ) } s ^ { 2 } ( \varepsilon _ { t } ^ { c } ) \, ,$$

$$\Gamma _ { \text {cc} } ( z ) = \frac { M ^ { \text {c} } ( z ) M ^ { \text {e} } ( z ^ { \ \cdot } ) } { A ^ { \text {c} } ( z ) A ^ { \text {c} } ( z ^ { \ \cdot \, 1 } ) } s ^ { 2 } ( \varepsilon$$

$$\Gamma _ { \mathbb { G } } ( z ) = \frac { M ^ { \mathfrak { g } } ( z ) M ^ { \mathfrak { g } } ( z ^ { - 1 } ) } { A ^ { \mathfrak { g } } ( z ) A ^ { \mathfrak { g } } ( z ^ { - 1 } ) } s ^ { 2 } ( \varepsilon _ { t } ^ { \mathfrak { g } } ) \, .$$

Hence, it follows that the optimal filter may be expressed as

$$C ^ { * } ( B ) = \frac { \psi A ^ { \mathfrak { g } } ( B ) A ^ { \mathfrak { g } } ( B ^ { - 1 } ) } { \psi A ^ { \mathfrak { g } } ( B ) A ^ { \mathfrak { g } } ( B ^ { - 1 } ) + ( 1 - \psi ) Q ( B ) } ,$$

where

$$Q ( B ) = \left [ \, A ^ { c } ( B ) \, A ^ { c } ( B ^ { - 1 } ) \right ] \left [ \, M ^ { g } ( B ) \, M ^ { g } ( B ^ { - 1 } ) \right ] \Big / \left [ \, M ^ { c } ( B ) \, M ^ { c } ( B ^ { - 1 } ) \right ] .$$

### 4.1. Matching the HP cyclical filter

The HP cyclical filter may be written as

$$C ( B ) = \left [ F ( B ) - 1 \right ] \left [ F ( B ) ^ { - 1 } \right ] = \frac { \lambda [ 1 - B ] ^ { 2 } [ 1 - B ^ { - 1 } ] ^ { 2 } } { 1 + \lambda [ 1 - B ] ^ { 2 } [ 1 - B ^ { - 1 } ] ^ { 2 } } \, .$$

The problem is to find AR and MA polynomials [A8(B), A(B), M8(B), and M(B)] such that C(B) and C*(B) coincide.

One example of such an inverse optimal filtering rule is discussed by Hodrick and Prescott (1980, p. 5) and involves assuming that

$$A ^ { g } ( B ) = ( 1 - B ) ^ { 2 } , \quad A ^ { c } ( B ) = M ^ { g } ( B ) = M ^ { c } ( B ) = 1 .$$

That is, under this specification, the change in the growth rate is a white noise as is the cyclical component. Further, the parameter λ corresponds to ψ/(1 − ψ) which is equal to the ratio of variances λ = s2(εc)/s2(ε8) or λi/2 = s(ε)/s(εε). Hodrick and Prescott (1980) use a prior view that a five prl  n    l y se y yl en percent change in the rate of growth in a quarter. This led us to select λ1/2 = 5/ or λ = 1600 as a value for the smoothing parameter.'

Pursuing this line further, suppose that we require that A8(B) = (1 – B)2 so as to accommodate nonstationarity in the growth rate. Then, it follows that C(B) = C*(B) requires that


<!-- p:19 -->


$$\frac { 1 } { \lambda } = \left ( \frac { 1 - \psi } { \psi } \right ) Q ( B ) \, .$$

Thus, the optimality of the HP filter requires – apart from the constant terms – restrictions across the A°(B), M(B), and M8(B) polynomials. In particular, it requires that

$$M ^ { c } ( B ) = \left [ \frac { \lambda ( 1 - \psi ) } { \psi } \right ] ^ { 1 / 2 } A ^ { c } ( B ) M ^ { g } ( B ) \, .$$

If innovations to the growth and cyclical components are uncorrelated, we find that a necessary condition for the HP filtering procedure to be optimal is that the stochastic growth component have a random walk growth rate, i.e., that it be second-difference-stationary in an extension of the Nelson and Plosser (1982) terminology. However, this condition is not sufficient. For the HP filter to be optimal, we must further require either that the cycle consist of uncorrelated events or that there be an identical dynamic mechanism that propagates changes in the growth rate and innovations to the business cycle component.

In real business cycle models growth and business cycles do not arise as separate phenomena, so that these models provide no theoretical justification for decomposition into growth and cycles. The simplest way to introduce growth into a real business cycle model is to assume that the level of Harrod-neutral technical progress expands at a constant rate. This induces cnes ss oms  ns s s os n monon stationary stochastic processes about this common trend. In this case there is a clear-cut separation between growth and cycles; growth is responsible for the common deterministic trend while cycles are the fluctuations around that trend. If we make exogenous technical progress stochastic and assume that it follows an integrated process (a kind of 'stochastic growth'), then these will generally set in motion complex responses that may resemble economic fluctuations [see King, Plosser, and Rebelo (1988b, sect. II)]. Thus, it is difficult to separate growth and fluctuations in this context. The dividing lines virtually disappear in models of endogenous economic growth, in which transient displacements to the dynamic system have permanent consequences for the paths of economic quantities [King and Rebelo (1986)]. However, given that there are a variety of motivations for filtering – some which do not hinge on an interest in precise growth versus cycle decompositions – we next explore the consequences of low frequency filtering in standard real business cycle models.


<!-- p:20 -->


## 5. Filtering a real business cycle model

Our next objective is to investigate how application of a low frequency filter influences the time series generated by an artificial economy. The specific economy that we study is one that we have explored in detail elsewhere [King, Plosser, and Rebelo (1988a)], so that our presentation is deliberately brief. For reference purposes, the economy is close to those studied by Hansen (1985) and Prescott (1986) and discussed in McCallum (1989).

The deep structure of the model economy – preferences, technology, and resource constraints – is specified as follows:

Preferences: The representative agent values sequences of consumption (C,) and leisure (L,) according to

$$E _ { 0 } \left \{ \sum _ { t = 0 } ^ { \infty } \beta ^ { t } [ \log ( C _ { t } ) + \eta \log ( L _ { t } ) ] \right \} .$$

In this expression E0 is the expectation conditioned on information available at time zero.

Technology: The production and accumulation technologies are

$$Y _ { t } = A _ { t } \left [ K _ { t } ^ { 1 - \alpha } ( N _ { t } X _ { t } ) ^ { \alpha } \right ] \ \text {and} \ K _ { t + 1 } = ( 1 - \delta ) K _ { t } + I _ { t } ,$$

where Y, is output, N, is labor input, K, is capital, I, is investment, and δ is the rate of depreciation. The production function is constant returns-to-scale with 0 &lt; α &lt; 1. The exogenous variables are X, which is a labor-augmenting technological shift that satisfies Xt +1/X, = γx &gt; 1, and A, which is a stationa /-   = /  t  t   t εAt with A &gt; 0, ρ &gt; 0, and ε, is an iid random variable with E(ε,) = 0 and

Resource constraints: The resource constraints for goods and leisure are

$$C _ { t } + I _ { t } = Y _ { t } \quad \text {and} \quad N _ { t } + L _ { t } = 1 .$$

Values for technology and preference parameters are those of the baseline model in King, Plosser, and Rebelo (1988a): δ = 0.025, α = 0.58, γx = 1.004, .s       s    = (3  =  / = e N = 0.20.

### 5.1. Approximate dynamics

The equilibrium quantities for consumption, investment, output, capital, and real wages will fluctuate stochastically around a common deterministic trend induced by X,. On the other hand, hours are stationary random variables. Approximating this system, we can develop a state space system for the logarithms of variables so that each variable can be written in the form log(Y,) = log(Y) + log( X,) + ,, where , is interpretable as the devia'oze v  sesc y     vyie i t [, ê, i, k, ω, N,I′ then is


<!-- p:21 -->


$$z _ { t } = \Pi s _ { t } ,$$

with state evolution governed by

$$s _ { t + 1 } = M s _ { t } + \varepsilon _ { t + 1 } \quad \text {and} \quad M = \left [ \begin{matrix} \mu _ { 1 } & \pi _ { k A } \\ 0 & \rho \end{matrix} \right ] ,$$

where s, = [k, À,]' and ε, = [0 εA, t + 1]. Stationarity of deviations from trend (μ, &lt; 1) is assured by diminishing returns to capital (holding fixed labor input). Thus, s, is stationary so long as A, is stationary (ρ &lt; 1). Given the state space representation just described, it is straightforward to compute the population movements of z, and s, using the procedures outlined in King, Plosser, and Rebelo (1987).

### 5.2. Filtering the system

To discuss the effects of filtering on moment implications we return to table 1.14 Looking first at the unfiltered moments in panel A, a researcher would draw one set of conclusions about the relative volatility of different series: labor input is about half as volatile as output; consumption is about two-thirds as variable; and investment is about twice as variable. The real wage is less volatile than output (about two thirds) but more variable than labor input. Further, one would conclude that labor input is at best only slightly more procyclical than capital input, on the basis that each has a contemporaneous correlation with output of about three quarters. Finally, one would view the stochastic components of output as relatively persistent given that the correlation of output with its fourth lag is 0.74 and the correlation with its twelfth lag is 0.42.

13Our approximation strategy – which works off the first-order conditions to the representative agent's dynamic optimization problem – is detailed in King, Plosser, and Rebelo (1987). In the present context, it is essentially equivalent to the log-linear approximation strategy of Christiano (1988), which uses quadratic approximation to the objective function.

Ihe as   e et a es te -r e e e om those reported in our working paper version of this research. This difference reflects the fact that results in our working paper were obtained with a version of the filter in which the number of coefficients was truncated to be 103, that is, 51 leads and lags. In this version of the paper iltg s s is  yt  s   s ter..


<!-- p:22 -->


Turning now to panel B, one finds the population moments for the components of time series isolated by the HP cyclical filter, with the smoothng i i i  y i i   s  i dor business cycles emerges. Consumption is now only 30% as variable as output, labor input is 64% as variable, and investment is now nearly three times as variable. The volatility of the real wage is only 40% of that of output. Further, with an application of the HP filter, the real wage it is sharply less volatile than labor input (only about two-thirds as volatile).

One also has a very different picture of cyclical movements in inputs: labor in s  d ( d d   o  st unrelated to cyclical activity (its correlation is 0.18). Finally, autocorrelation in output is 0.22 at a lag of one year (four quarters) and negative at a lag of three years (twelve quarters).

Considering the state space system, it is easy to interpret these results. The evolution of all variables depends on their weights placed on the state variables, the capital stock, and the technology shock. The technology shock isy      b        an A, = Σs=0ρε A,t−s Given the law of motion for capital, k1+1 = μ1k, + πkAA with μ ≈ 0.95, the capital stock is a moving average of technology shocks, with weights that die out very slowly. Relative to the technology shock, then, the capital stock is very slow moving and application of the low frequency filter downplays its influence and raises that of the technology shock. Notice that this occurs despite the fact that both capital and technology are driven by εAt, since they are related to it by different (one-sided) linear flters.15

### 5.3. Random walk technology shocks

It is possible to solve this model under the alternative assumption that technology shocks are integrated processes [see Christiano (1988) or King, Plosser, and Rebelo (1988b, sect. 2)]. In view of the Nelson-Plosser (1982) results and given the intuitive idea that technology shocks are well modeled as a random walk (with positive drift), we present some final results based on that alternative specification in table 2. Since the levels of variables are not stationary, population moments are not finite. Thus, we present results for the first difference filter and for the HP cyclical filter. In the presence of this nonstationarity, the HP filter produces results that broadly resemble those of table 1, although the shift to a random walk technology shock does reduce the extent of labor volatility, as stressed by Hansen (1988).

15Our working paper contains plots of original and filtered spectral densities of capital and output which are revealing about the issue discussed in this paragraph.


<!-- p:23 -->


Effects of filtering on population moments: Unit root model.

|    |                    |        | I l l l   |
|----|--------------------|--------|-----------|
|    | ,--~ ¢'4           |        | I         |
|    | oo ~, ~;           |        |           |
|    |                    | 3 ~    |           |
|    | ,--.~ 0 0 0 0      |        |           |
|    | 0 0                | ~ t",l |           |
|    | 0 0 0 0 0          | R      |           |
|    | .o.q . . 0 0 0 0 0 |        |           |
|    | 0 0 0 ~ 0          |        |           |
|    | 0 0 0 0 0          | 0      |           |
|    | Ndd d d            | 8      |           |
|    | .~.o. ~ ~.         | <      |           |
| ~2 |                    |        | ~ L ~ o   |
| >  |                    | >      |           |

bStandard deviation HP-filtered x relative to standard deviation of filtered output. Standard deviation of x relative to standard deviation of growth rate of output.


<!-- p:24 -->


## 6. Summary and conclusions

This paper has reported on implications of low frequency filtering, focusing on the Hodrick and Prescott (1980) filter which is commonly used in investigations of the stochastic properties of real business cycle models. We summarize our results as follows:

First, application of the filter to U.S. real gross national product and a measure of labor input illustrates the impact of HP filtering on the character of cyclical components. Second, we derive convenient expressions for the HP filter and the closely related exponential smoothing (ES) filter in forms appropriate for both the time domain and frequency domain. These results are used (i) to discuss the influence of smoothing parameters and (ii) to demonstrate that the cyclical components which these filters generate are stationary, when the underlying time series are differenced stationary stochastic processes in the sense of Nelson and Plosser (1982). Third, we consider the conditions under which the HP filter is the optimal linear filter in the sense of Wiener (1949) and Whittle (1963). These conditions are unlikely to be even approximately true in practice. Fourth, application of the HP filter to a basic real business cycle model demonstrates that this filter substantially influences the perception of the operation of the model economy, as viewed by researchers studying its moment implications.

At the end of our investigation, however, we remain struck by the figures presented in section 1: macroeconomic research focusing on the component of the time series that is isolated by the HP cyclical filter – in terms of either devising stylized facts or evaluating dynamic economic models – is likely to capture only a subset of the time series variation that most economists associate with cyclical fluctuations. A major facet of our ongoing research is the construction of dynamic models that more completely integrate the explanation of these components.
