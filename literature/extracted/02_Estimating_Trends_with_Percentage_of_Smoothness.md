---
id: "02_Estimating_Trends_with_Percentage_of_Smoothness"
source_pdf: "../pdf/02_Estimating_Trends_with_Percentage_of_Smoothness.pdf"
source_filename: "02_Estimating_Trends_with_Percentage_of_Smoothness.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/02_Estimating_Trends_with_Percentage_of_Smoothness.references.md"
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
