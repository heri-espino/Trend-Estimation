---
id: "6+-+Alejandro+Islas+e+Juan+A.+Zumaya+GALVÁN+(3)"
source_pdf: "../pdf/6+-+Alejandro+Islas+e+Juan+A.+Zumaya+GALVÁN+(3).pdf"
source_filename: "6+-+Alejandro+Islas+e+Juan+A.+Zumaya+GALVÁN+(3).pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/6+-+Alejandro+Islas+e+Juan+A.+Zumaya+GALVÁN+(3).references.md"
---

<!-- p:1 -->

ECONOMIA

dsn-vaf

## Exchange rate predictability: Multi-State Markov-Switching model and trend with controlled smoothness

### Alejandro Islas CAMARGO1

aislas@itam.mx D ORCID: https://orcid.org/0000-0003-0910-313X

## Juan A. Zumaya GALVÁN2

juan.abraham.zumaya@citi.com| iD ORCID: https://orcid.org/0009-0007-1032-661X

####### Abstract

This study presents an exchange rate (Mexican Pesos / U.S. Dollar) forecasting model. The statistical methodology used is based on the Multi-State Markov-Switching model with three different specifications. The model is applied to the trend of the time series data instead of the -ors ti s   rss  rn o  s ecs  t econ nique employed to estimate the trend allows us to control the amount of smoothness in the resulting trend. By doing this, the Markov-Switching approach captures the trend persistence oc c-s es aos-s  ss e aes as s a oo performance. Our results show that correctly identifying the trend in the exchange rate (Mexican Peoss g g g  ns g  r   s oipg g  pleg raans  c   s  d w  we  es we emphasize that when working with asset prices time series, a usual assumption is that the series behaves as a random walk, that is, as an I(1) process, and not as an I(2) process. Since we are interested in decomposing a financial time series into trend plus noise, we use the exponential smoothing (ES) filter rather than the Hodrick-Prescott (HP) filter, as other authors hads  p  y e rs (r e  s dh  d  on error in the sense that a sub-optimal procedure is used.

####### Keywords

Exchange rate, Forecasting, Exponential smoothing, Markov-Switching

1 Autonomous Technological Institute of Mexico (ITAM), Department of Statistics, Mexico City, Mexico.

2Autonomous Technological Institute of Mexico (ITAM), Mexico City, Mexico.

cc

1

<!-- p:2 -->


## Previsibilidade da taxa de câmbio: modelo de Markov-Switching multi-estado e tendência com suavidade controlada

##### Resumo

Este estudo apresenta um modelo de previsão da taxa de câmbio (pesos mexicanos/dólar americano). A metodologia estatística utilizada baseia-se no modelo Multi-State Markov-Switching com três especificações diferentes. O modelo é aplicado à tendência dos dados da série temporal em vez das observações originais para mitigar o efeito de outliers e blips transitórios. A técnica de filtragem empregada para estimar a tendência nos permite controlar a quantidade de suavidade na tendência resultante. Ao fazer isto, a abordagem Markov-Switching capta a per  o r  d s o   sa s   ssad pro ot  orns os osn o  ao  o onne De nn  (on aoa   d   x  D l fundamental na obtenção de capacidade superior de previsão em relação ao passeio aleatório simples. Além da nova abordagem para estimar uma tendência com suavidade controlada, enfatizamos que quando se trabalha com séries temporais financeiras, uma suposição usual c  ossro o oo 'es o ' ss o oo ro s so  o não como um processo I(2). Como estamos interessados em decompor uma série temporal financeira em tendência mais ruído, utilizamos o filtro de suavização exponencial (ES) em vez do filtro Hodrick-Prescott (HP), como fizeram outros autores. Aplicar o filtro HP a um processo I(1), como feito incorretamente, produz um erro de especificação no sentido de que um procedimento abaixo do ideal é usado.

####### Palavras-chave

Taxa de câmbio, Previsão, Suavização exponencial, Markov-Switching

####### JEL Classification

C32, C53, F31, F47

## 1. Introduction

Over the last two decades, exchange rates have become increasingly unpredictable while businesses have become more globalized. This means that many business decisions now consider forecasts of future exchange rates. Central banks in countries like Mexico, which heavily rely on importing and exporting commodities, need to forecast exchange rates as accurately as possible. Private businesses and forecasters will also want to predict exchange rates. Policymakers who rely on successful forecasts of macroeconomic indicators, mainly exchange rates, to make effective decisions need to pay attention to this topic (Wieland and Wolters, 2013 provides a detailed review of how forecasts are used in policymaking).

cc

1

BY


<!-- p:3 -->


Modeling exchange rates is a significant challenge to economists, market practitioners, academics, and decision-makers. In this paper, we empirically analyze one of the puzzles in international economics stemming from the findings of Meese and Rogoff (1983), and Messe, Rogoff and Frenkel (1983), that macroeconomic fundamentals are weak predictors of exchange rate movements, especially at the short horizon. Subsequent research works suggest that a random walk model appears to be the most successful model in forecasting out-of-sample nominal exchange rates. As Meese and Rogoff (1983) pointed out, parameter instability is the possible explanation for the poor performance of exchange rate forecasts.

As Sarno and Valente (2009) shows, it is possible that one variable is the critical predictor over a certain period but that it loses its predictive ability due to policy regime shifts, the agent's heterogeneity, or instabilities in exchange rate models. Based on this idea, after observing that the exchange rates tend to follow highly persistent trends and suggesting that the key to pea ( n      s    ss an extension of Engle and Hamilton's (1990) model. Such an extension allows, in addition to the appreciation and depreciation regimes, a trendless regime and a time series filtering technique to smooth out outliers and tranSit-b b t h   o b t s nsg framework captures the trend persistence in exchange rates more accurately.

In fact, Dacco and Satchel (1999) showed that the misclassification of regime tends to make the Markov-switching model less effective in beating the random walk even if an excellent in-sample performance has been presented. Furthermore, Mash (2000) argued that Markov-Switching model generally offers sound in-sample fit but fails to deliver superior out-of-sample forecast due to parameter instability over time. Therefore, since exchange rates are often extremely noisy, the oversensitivity of the conventional Markov-Switching model tends to induce instability in parameter estimation and misclassification of regime shifts and, in turn, undermine its forecast ability. Our proposed model that combines the Markov-Switching model with the controlled smoothing filter corrects this drawback and enhances both in-sample and out-of-sample forecasting performance.

Figure 1 shows the nominal monthly exchange rate (Mexican Pesos / U.S. Dollar) series. The sample period covers from January 1995 to August 2019. As it can be observed, assuming only two regimes, appreciation and depreciation, is inconsistent with the fact that the monthly exchange rate exhibits range-bound behavior for a sustained period, as shown on the shaded periods. Therefore, as in Yuan (2011), we suggest a third trendless regime is necessary to describe better the exchange rate behavior (Mexican Pesos / U.S. Dollar).

1


<!-- p:4 -->


Figurel - Nominal monthly exchange rate (Mexican Pesos / U.S. Dollar). The sample period covers from January 1995 to August 2019.

22.5

20.0

17.5

15.0

Mym

12.5

10.0

7.5

5.0

1995

1997

1999

2001

2003

2005

2007

2009

2011

2013

2015

2017

2019

Yuan (2011) argued that the standard two-state Markov-Switching model cannot provide strong evidence of outperforming the random walk. To tackle this issue, we suggest using a Multi-State Markov-Switching model to model the trend, including trendless periods and appreciation and depreciation in exchange rates. The goal is to enhance the model's forecasting ability. This approach aligns with Yuan's (2011) suggestion of using a time series filtering technique to eliminate outliers and transitor     os b g b b    bothg Markov-Switching framework accurately captures the trend persistence in exchange rates. Our proposed model goes one step forward, as it applies a filter that produces a trend with controlled smoothness and considers an implicit adjustment to the observations at both extremes of the time series, as in Guerrero (2007).

Furthermore, when working with asset prices time series, a usual assumption is that the series behaves as a random walk, that is, as an I(1) process. For instance, Baillie and Bollerslev (1989) found that the exchange rates of several currencies against the U.S. Dollar behave as random walks. To be consistent with this idea, since we are interested in decomposing a financial time series into trend plus noise, we use the exponential smoothing (ES) filter (Guerrero and Galicia-Vazquez, 2010) rather than the HodrickPrescott (HP) filter as Yuan (2011) did. King and Robelo (1993) expose the distinction between these filters. For our purposes, it suffices to say that the ES filter employs an I(1) representation for the trend, while the HP filter uses an I(2) representation. Besides, as Tödter (2002) pointed out, the HP filter is optimal if the data follow an I(2) process. Applying the HP filter to an I(1) process yields a specification error because a sub-optimal procedure is used (Refer to Tödter 2002 for a clear explanation of the meaning of "filter" and "optimal results" used in this context. Additionally, you can find an explanation of the specification error made when using the HP Filter in an I(1) process).

1

BY


<!-- p:5 -->


Using monthly and quarterly exchange rates (Mexican Pesos / U.S. Dollar) over the period from January 1995 to August 2019 and 1995: I-2019:II, respectively, our results reveal that the proposed forecasting model with the exponential filter can adequately capture the movements of exchange rates. Therefore, it achieves considerable forecast ability improvement relative to the random walk and the model with the HP-filter proposed by Yuan (2011), in terms of mean square forecast error. Specifically, the out-of-sample forecast precision gain, averaging over a horizon of up to 12 months and four quarters are 8.74% and 11.68%, respectively.

The remainder of this paper is organized as follows. The coming section presents the literature review. The second section presents the statistical methodology to be used, i.e., the Markov-Switching model and the controlled smoothness filtering technique that takes into account an adjustment at both ends of the time series, and that the exchange rates follow a process with just one unit root. The empirical application to exchange rate is presented in the fourth section, where detailed summaries of the estimation results are shown, together with a forecast evaluation of the models employed. The last section concludes with some final remarks.

## 2. Literature review

To bluster up the exchange rate forecast ability, various time-series models have been employed, where the coefficients of a given individual model change over time according to a rule. The Kalman filter approach (Wolff, 1987); Schinasi and Swamy (1989), the random walk coefficient model

cc

1


<!-- p:6 -->


(Stock and Watson, 1998), and the Markov switching model (Engel and Hamilton, 1990; Engel, 1994) are all examples of this approach. Some of these papers show out-of-sample forecast improvements over the random walk. This result, however, turns out to be fragile with an extended data set.

Other studies attempt to forecast exchange rates with a range of different variables. See Cheung, Menzie and Pacual (2005, 2019) and Rossi (2013) for a survey of the literature on predicting exchange rates. These authors carefully reviewed the performance of the most popular exchange rate models highlighting that economic models occasionally possess forecasting power, especially at medium-term horizons, they also stressed that the results are extremely sensitive to small changes in the forecast evaluation settings. Among these papers, we find the monetary model considered by Meese and Rogoff (1983) and its subsequent papers derive the exchange rate either from money supplies and real outputs or its adjusted form, money minus output. Considering that exchange rates can be approximated by a unit root process, Rossi (2006) and Rossi and Sekhposyan (2011) employ the growth rate of these variables. Taylor rules fundamentals, such as the inflation rate and output gap, are used by Molodtsova and Papell (2009) and produce better out-of-sample forecasts at short-horizons. Chen -ods os dd   s od s poe (od ods pdie tor, but Chen, Rogoff and Rossi (2010) reveal that in-sample predictability of commodity price fails to translate into out-of-sample success.

On the other hand, Engel, Mark and West. (2008), estimated the pace of Purchase Power Parity (PPP) adjustment with panel data techniques to minimize the role of estimation error. In a similar vein, Ca' Zorzi, Muck and Rubaszek (2016); Ca' Zorzi, Kolasa and Rubaszek (2017) proposed a calibrated half-life (HL) PPP model that bypasses the estimation error problem altogether. Recently, Ca'Zorzi and Rubaszek (2020) suggest that there are two regularities in foreign exchange markets only in advanced countries with flexible regimes. First, that real exchange rates are mean-reverting, and second, that the adjustment takes place via nominal exchange. With these regularities, the study concluded that the secret to beat the Random Walk (RW) is to impose a reasonable pace at which PPP is restored and assume that relative inflation is zero.

1


<!-- p:7 -->


## 3. The Method

### 3.1. Markov-Switching model

Markov-Switching is a nonlinear time series model that captures complex dynamic patterns by allowing the model to switch between multiple structures that characterize different regimes. The switching mechanism is controlled by an unobservable state variable that follows a first-order Markov Chain structure, meaning a given structure may prevail for a random period of time before being replaced by another structure.

In its broadest form, a Markov-Switching model for a time series {yt} can be written as follows:

$$y _ { t } = \mu ( s _ { t } ) + \sigma ( s _ { t } ) \varepsilon _ { t } \text { with } \varepsilon _ { t } \text { i} d \sim N ( 0 , 1 )$$

where {εt} is a sequence of random errors, iid stands for independent and identically distributed,{st} is an unobservable discrete-time Markov Chain with a finite number of states, k, while {yt} given {st}, follows an autoregressive process whose parameters, μ and σ, depend on the state of the Markov Chain. This model was introduced in the econometric literature by Hamilton (1989) and it is appropriate to capture changes in time series behavior due to extraordinary events such as wars, financial panics, natural disasters, and drastic changes in government policies. The original Hamilton model has been subject to several refinements to accommodate regime shifts in intercepts, autoregressive parameters, and variance (see, for example, Hamilton 1994, Krolzig 1997, Fruhwirth-Schnatter 2006, Koop G. 200).

Given the variety of Markov-Switching models that one can choose from, the dilemma is to determine which one is appropriate for the data at hand. It is not necessary that all the parameters in the model be regime-dependent. As in Engel and Hamilton (1990) and Yuan (2011), in our empirical application, we allow the autoregressive parameters, the mean or the intercepts to be regime-dependent, and the error term to be either heteroscedastic or homoscedastic. Regarding the selection of the value of k, when modelling the dynamics of the observed process, there is virtually no standard distributional theory applicable for evaluating the MarkovSwitching model against alternatives such as linear time series models (Raymond and Rich 1997, Hamilton 1989, Carrasco, Hu and Poberger 2014). Nevertheless, some procedures have been suggested to test the number of regimes, for instance, Hansen (1992) proposed to obtain the optimum of the likelihood surface through a grid search over the parameter space, but to some extent, the computational burden limits its applicability. On the other hand, Cheung and Erlandsson (2005) suggested a simulated likelihood ratio test based on a Monte Carlo method, but as they admitted, their results were fairly sample-specific.

cc

1


<!-- p:8 -->


### 3.2. Underlying trend with controlled smoothness

Instead of using the usual Markov-Switching model for the original time series, we opted to implement Yuan's (2011) recommendation of employing the Markov-Switching model for the trend of the relevant variable. This means that we suppose the observed time series can be represented as a signal-plus-noise model, not because we believe that this is the true data generating process, but just to take into account the empirical regularities in the data.

Additionally, when working with asset prices time series, a usual assumption is that the series behaves as a random walk, that is, as an I(1) process. For instance, Baillie and Bollerslev (1989) found that the exchange rates of several currencies against the U.S. Dollar behave as random walks. Similarly, Narayan and Smyth (2005) showed that the stock prices of the OECD countries should be considered I(1) processes. Moreover, Tsay (2002) uses a random walk with drift as a conventional model for prices. To be consistent with this idea, since we are interested in decomposing a financial time series into trend plus noise, we used the exponential smoothing (ES) filter rather than the HP filter as Yuan (2011) did.

Let us assume that an observed time series can be represented by the following unobserved component model:

$$y _ { t } = g _ { t } + \nu _ { t }$$

where {gt} is the trend (or signal) and {νt} is the noise of {yt}, for t =1,..., N. We will assume that the series {yt} is I(1) in such a way that its trend will also be I(1) and the noise process will be stationary. Then, we can use Penalized Least Squares (PLS) to estimate the trend by posing the following minimization problem as in Guerrero and Galicia-Vazquez (2010):

$$\min _ { g _ { t } } \{ \sum _ { t = 1 } ^ { N } ( y _ { t } - g _ { t } ) ^ { 2 } + \lambda \sum _ { t = 2 } ^ { N } ( \nabla g _ { t } - \mu ) ^ { 2 } \}$$

cc

1

BY


<!-- p:9 -->


Where ∇ denotes the difference operator given by ∇gt = gt - 9t-1 and λ &gt; 0 is a constant that penalizes the lack of smoothness in the trend. That is, as λ → 0, the trend resembles more closely the original data, i.e. gt → yt for all t, so that no smoothness is achieved, while the opposite occurs whenλ → ∞, in which case the trend follows essentially the polynomial model gt - gt-1 = μ which represents the trend growth expressed as a first difference. Hence, λ plays an important role in deciding the smoothness of the trend, while μ is a reference level for the trend growth. It should be noticed that the trend follows the first-degree polynomial given by:

$$g _ { t } = \beta _ { 0 } + \mu t \text { when } \mu \neq 0$$

which becomes a constant when μ = 0, so that using this reference level as 0, as is usual in practice (e.g. Yuan, 2011 in the case of the HP) has important consequences on the trend behavior, particularly at the endpoints of the series, as it will be seen below.

By solving the minimization problem (3) with μ ≠ 0, we obtain the ES filter which provides trend estimates of the series {yt}, where t =1, ..., N. Once the problem (3) is solved, assuming that both the reference level μ and the smoothing parameter λ are known, we have to provide appropriate values of those parameters, keeping in mind that a small value of the latter yields a trend that resembles the original data, while a large value produces a trend that behaves as a straight line. Below we will focus on this matter.

According to Yuan (2011), we should employ the Markov-Switching representation for the trend rather than the original series, so that expression (1) is no longer valid for yt, but for gt. Thus, let us consider the following unobserved-component model that underlies the minimization of (3).

$$y _ { t } = g _ { t } + \nu _ { t } \text { with } \nu _ { t } \sim N ( 0 , \sigma _ { \nu } ^ { 2 } ) \text { for } t = 1 , \dots , N$$

$$g _ { t } = \mu + g _ { t - 1 } + \varepsilon _ { t } \text { with } \varepsilon _ { t } \sim N ( 0 , \sigma _ { \varepsilon } ^ { 2 } ) \text { for } t = 2 , \dots , N ,$$

where we use ζ~N(0,σ2) to say that the random variable ζ has mean 0 and variance σ2. The sequence {vt} contains serially uncorrelated random errors and {εt} is another sequence of serially uncorrelated random errors that is also uncorrelated with the previous sequence.

1


<!-- p:10 -->


Solution of the minimization problem can be easily expressed in matrix notation by letting y, g and ν be vectors of size N containing the observations, trends and noises, respectively. Then we write equations (5) and (8) in matrix notation as

$$y = g + \nu$$

and

$$K g = \mu 1 _ { N - 1 } + \varepsilon$$

where ν and ε are random vectors such that E(v) = 0N, Var(v) = σγIN, E(ε) = 0N−1, Var(ε) = σ2 IN−1 and E(vε') = 0, with IM the M-dimensional identity matrix, and 1n-1 = (1, ..., 1). In (8) we use the following (N-1)×N matrix that represents the first difference operation appearing in (6)

$$K = \begin{pmatrix} - 1 & 1 & 0 & 0 & \dots & 0 & 0 \\ 0 & - 1 & 1 & 0 & \dots & 0 & 0 \\ \dots & & & & & & \\ 0 & 0 & 0 & 0 & \dots & 1 & 0 \\ 0 & 0 & 0 & 0 & \dots & 0 & - 1 & 1 \end{pmatrix}$$

An application of Generalized Least Squares (GLS) to the system of equations (7) – (8) yields the Best Linear Unbiased Estimator (BLUE) of the vector of trends, given by (see Guerrero, 2007 for details):

$$\widehat { g } = ( I _ { N } + \lambda K ^ { \prime } K ) ^ { - 1 } ( y + \lambda \mu K ^ { \prime } 1 _ { N - 1 } )$$

With λ = σ/σ2. GLS also produces the Variance-Covariance matrix Σ = σ2(IN + λK'K)−1. To appreciate the effect of the constant μ, we should notice that the array K ́1N-1 appearing in (10) is an N-dimensional et at t t  t t t ft t ct f cs K ́1N-1 = (1,0, ..., 0,1). Therefore, the observed values of the original series {yt} enter the formula of the estimator  modified in both of its extremes by the value of μ, weighted by λ. That is, (10) indicates to apply the smoother matrix (I + λK'K)−1 to:

$$y + \lambda \mu K ^ { \prime } 1 _ { N - 1 } = ( y _ { 1 } + \lambda \mu , y _ { 2 } , \dots , y _ { N - , 1 } , y _ { N } + \lambda \mu )$$

and by doing that we are adjusting the first and last values of the series, in the spirit of Yuan (2011). However, our "adjustment" comes out from the model specification for the trend (8), while Yuan solved the end-of-sample problem (for the HP filter) by using different smoothing parameter values. Yuan's solution forces the trend to get closer to the original data at the end points, but the choice of λ values has no theoretical justification. Likewise, let us recall that μ should be estimated as the mean of the series in first differences.

1

BY


<!-- p:11 -->


Moreover, μ also affects the results when extrapolating the trend, as is shown by expression (4) since μ ≠ 0 implies a trend that follows a linear polynomial and the extrapolated trend values critically depend on the last estimated value. That is, if we call μ ≠ 0 the h-period ahead forecast of 9N+h, with origin at N, we get for h ≥ 1.

$$\hat { g } _ { N } ( h ) = h \mu + g _ { N }$$

To apply (12) we follow Guerrero's (2007) proposal of choosing the smoothing parameter λ by fixing the value of the index first:

$$S ( \lambda , N ) = 1 - t r \left [ ( I _ { N } + \lambda K ^ { \prime } K ) ^ { - 1 } \right ] / N$$

that measures the smoothness achieved by the trend. Among other properties, this index takes on values between 0 and 1, and measures the proportion of precision induced by smoothing the data.

An appropriated percentage of smoothness can be obtained from the following guidelines deduced by Guerrero et al. (2017) through simulation study1. Then we suggest:

- (i) if the original series behaves as a straight line, the percentage of smoothness should start at 92.5% for N &gt; 48, and increasing for large value of N;

Given that the simulation study in Guerrero, Islas-Camargo, and Ramirez-Ramirez (2017) was carried out assuming ∇2git = 0, that is assuming μ = 0, the trend will be given by git = α + βt, i = 1,2. On the other hand, in the exponential filter proposed in this paper we assume μ ≠ 0, in such a case, the trend will be given by gt = α + μt. Therefore, for ρ = 0 we can apply the guidelines suggested by Gerrero, Islas-Camargo, and Ramirez-Ramirez (2017). Besides, as pointed out in Guerrero, IslasCamargo, and Ramirez-Ramirez (2017) page 6712, when there is no correlation between any pair of series (ρ = 0), the multivariated smoothness index reduces to the univariated index. As in Guerrero, Cortes and Reyes (2018), the smoothness index, equation (13) in our text, solely depends on the values λ and N since K remains fixed. It is important to note that K is a matrix of rank N-1. Therefore, the matrix K'K has one eigenvalue equal to zero, while the remaining N-1 nonzero eigenvalues can be arranged in descending order as e1 ≥ e2 ≥ . ≥ en-1. Consequently, the expression in (13) for the trace can be expressed as such:

$$t r ( I _ { N } + \lambda K ^ { \prime } _ { 2 } K _ { 2 } ) ^ { - 1 } = ( 1 + \lambda e _ { 1 } ) ^ { - 1 } + \dots \ ( 1 + \lambda e _ { n - 1 } ) ^ { - 1 } + 1$$

and it can be observed that S(λ, N) → 0 as λ → 0 and S(λ, N) → 1 − 1/N as λ → ∞. Therefore, more smoothness can be achieved with a larger sample size (N). This is why, as seen in section 4, we exceeded Guerrero, Islas-Camargo, and Ramirez-Ramirez (2017) suggested upper smoothing limit.

cc

1


<!-- p:12 -->


- (ii) when the series shows a non-straight-line pattern, the percentage of smoothness should start at 80% for N &gt; 48 and increasing for large values N of after fixing the percentage of smoothness following the guidelines mentioned above, the value of the smoothness constant, λ, is determined using daily bases data and solving Guerrero and Galicia-Vazquez's (2010) equation 32.2

It is important to emphasize that filters are designed to achieve specific goals. In the present case, we focus on estimating the underlying trend of the time series to apply Yuan's (2011) proposal. Still, we use the exponential smoothing (ES) filter rather than the HP filter, as Yuan (2011) did. Thus, instead of fixing the value of λ, we fix the percentage of smoothness to be achieved by the trend to establish valid comparisons for different sample sizes and frequencies of observations.

## 4. Results and discussions

We focus on monthly and quarterly exchange rate frequencies, as they are the ones of interest of economists; we did not consider very high frequency data analyses that are instead mostly of interest to risk management. Therefore, the data set used in our empirical analysis consists of monthly and quarterly nominal exchange rate (Mexican Pesos /U.S. Dollar) series. It is of particular interest to study if whether as a result of obtaining comparable trends, with the proposed filtering method, in exchange rates with different frequencies, the forecast performance through the MarkovSwitching model is robust. The sample period runs from January 1995 to September 2019 for the monthly series, while for the quarterly series it runs from 1995:I through 2019:II. We should stress that these series are formed

As is well known, a time series with a lower frequency of observation is related to that with a higher frequency using some aggregation mechanism. In cases where time series are not nondaily, Guerrero and Galicia-Vazquez (2010) proposed a solution to find the smoothing constant λ that produces equivalent results on time series with different periodicities, from a frequency domain perspective. Their methodology considers the aggregation type that connects a lower-frequency series {Y} with a higher-frequency time series {Yt}. Guerrero and Galicia-Vazquez (2010) proposed equation (32) that permits the finding of a smoothing constant λ for a disaggregated series that is equivalent to the λk value for the aggregated data, as follows:

$$\lambda = \begin{cases} ( k ^ { 2 } - 1 ) / 6 + k ^ { 2 } \lambda _ { k } ^ { * } & \text {for} \ f l o w s \\ k \lambda _ { k } ^ { * } & \text {for} \ s t o c s \end{cases}$$

Therefore, if you know the smoothing constant λ for the disaggregated time series, you can use equation (32) to solve for the corresponding value of λk. k is the number of observations Yt between two successive observations YT

cc

1

BY


<!-- p:13 -->


for the rate of the last day of the month and the last day of the quarter for the monthly and quarterly series, respectively. The exchange rates are from the Mexican Central Bank statistics (http://www.banxico.org.mx).

To contrast the forecasting results for the exchange rate obtained with the proposed smoothing technique, we used three models in the analysis. The first model was the standard Markov-Switching-Mean-Heteroscedastic model with three-regimes, known as MSMH(3). The second model was the three-regime Markov-Switching-Mean-Heteroscedastic-filtered model with the HP-filter (HP-MSMH(3)). When analyzing quarterly data using the HP filter, it is generally accepted to use the value λ =1600. This value was initially proposed by Hodrick &amp; Prescott based on their assumption that ∇2gt and vt were independent random variables with a normal disti         ke appropriate values for σν = 5 and σε = 1/8 for the US macroeconomic series they were studying were 5 and 1/8, respectively, resulting in a value of λ = σ2/σ2 = 1600. They also tested the results with other values of λ, -n              tti! mated trend change significantly. Therefore, the value of λ = 1600 became the consensus for the smoothing constant when using the HP filter for quarterly data.

However, consensus disappears when other frequencies of observations are used. For example, for monthly data, Dolado et al. (1993) use λ = 4800, while the econometric software E-views uses the default value 1 1 λm= 2λQ = 1600 = 14400. That is, the HP filter parameter λQ for α2 (1/3)2 quarterly data should be adjusted with the second power of the frequency change. In our analysis we will use λm = 14400 for monthly data.

The third model was the three-regime Markov-Switching-MeanHeteroscedastic-filtered model with the exponential filter (ESMSMH(3)). Following Guerrero, Islas-Camargo, and Ramirez-Ramirez's guideline (2017), a smoothness percentage of S(λ,N)%=95% was set to select the corresponding smoothing parameter from equation (32) in Guerrero and Galicia-Vazquez (2010). For a sample size of N= 5920, the smoothing parameter for daily data is λa = 100.81. Therefore, given that our series of stocks was constructed from daily data, the sample now comprises N= 296 monthly observations and N= 90 quarterly observations, considering a twenty-day month and sixty-five-day quarter.

cc

1


<!-- p:14 -->


The smoothing constant for the monthly series is λ2o = 5.05, while for the quarterly series, it is λ65 = 1.55, for S% = 95%, as obtained from Guerrero and Galicia-Vazquez's (2010) equation (32) by λa = 20λ20 and λa = 65λ*65, respectively. Figure 2 depicts the monthly and quarterly exchange rate series and their trend estimates. We observed that the trends estimated with the exponential filter and the same smoothness percentage showed similar dynamic behavior, regardless of the data frequency. Therefore, comparable trends were obtained for monthly and quarterly data. For further details, refer to Guerrero and Galicia-Vazquez (2010).

Figure 2 - Exchange rate (Mexican Peso/U.S. Dollar). Observed series and trend estimates with S% =95%. Left, monthly, λ = 5.04, N=296. Right, quarterly, λ = 1.55, N=98

22.5

22

20.0

20

18

17.5

16

15.0

14

12.5

12

10.0

10

7.5

8

5.0

6

1995

1998 2001

2004 2007 2010 2013 2016 2019

1995

1998

2001

2004 2007 2010 2013 2016 2019

Observed series

Trend ES

Trend HP

Observed series

Trend ES

Trend HP

Table 1 reports maximum likelihood estimates based on the entire sample of data. At the bottom of panels A and B of Table 1, we present some hypothesis tests for model selection. Because the conclusions drawn from the test results are unchanged for the ES-MSMH, HP-MSMH, and MSMH models in monthly and quarterly exchange rates, we need only explain the test results based on the ES-MSMH model in the monthly data. In Table 1, the notation ES-MSMH(2)|ES-MSMH(3) represents the null hypothesis of model ES-MSMH(2) against the alternative hypothesis of model ES-MSMH(3). The log-likelihood values for models ES-MSMH(2) and ES-MSMH(3) are, respectively, 334.2934 and 304.0390, and the LR statistic is 2 * [334.2934 − 304.0390] = 60.5098 &gt; χ2(2), which indicates that model ES-MSMH(3) is preferable to model ES-MSMH(2). Based on the LR test for model selection, the three-state Markov-Switching model is preferred to the two-state Markov-Switching model in all cases.

cc

1

BY


<!-- p:15 -->


According to Krolzig (1997), it is not possible to compare two models with different numbers of regimes using a general test. The reason for this is that the asymptotic theory cannot be applied in such cases due to unidentified nuisance parameters and violations of non-singularity conditions. Nevertheless, many researchers continue to use the LR test to obtain helpful supporting evidence. This paper considers the LR tests in this context.

Table 1, panel A shows the maximum likelihood estimates associated with the three-regime Markov-switching models applying to the monthly exchange rate by imposing a regime of mean zero. The three regimes considered are low-depreciation or appreciation exchange rate, trendless and depreciation or high-depreciation exchange rate, classified as regimes 1, 2, and 3, respectively. The estimates indicate that regime 1 is associated with a 22.96% monthly appreciation predicted by the unfiltered MSMH(3) model, while the HP-MSMH(3) model predicts a low-depreciation of about 3.3% and the ES-MSMH(3) model predicts an 8.5% appreciation in regime 1, respectively. The three models estimate a depreciation exchange rate trend of about 67.2%, 9.2%, and 16.2%, respectively. The asymmetry in mean depreciation and appreciation estimated for models MSMH(3) and ES-MSMH(3) in the monthly exchange rate roughly reflects the shape of its plot. The models with filter moderately scale down the magnitude of means, both depreciation and appreciation trend in the monthly exchange rate. One partial explanation could be that smoothing techniques have filtered out trivial shifts but left the relatively true shifts in account for mean change.

On the other hand, Table 1, panel B shows the estimated models for the quarterly exchange rate. Results indicate that regime 1 is associated with a 23.08% quarterly appreciation predicted by the unfiltered MSMH(3) model, while the HP-MSMH(3) model predicts a low-depreciation of about 14.5%, and the ES-MSMH(3) model predicts a 4.3% low-depreciation in regime 1, respectively. The MSMH(3) estimates an 18.9% quarterly medium-depreciation for regime 2, while models HP-MSMH(3) estimates a 7.5% medium-depreciation, and a zero-mean was imposed in model ES-MSMH(3). The three models estimate a high-depreciation of about 26.08%, 26.86%, and 52.49%, respectively.

Table 1, panel A also shows that according to the estimates of the HPMSMH(3) model, the monthly exchange rate seems to be characterized by long swings with sustained low depreciation, trendless and high depreciation regimes. This high persistence of regimes is represented by the high regime-staying probabilities, p11, p22, and p33; that is, the probability of staying in a regime once the process enters it. The expected duration of regime j is defined as 1/(1 - pjj). Thus, while the trendless regime is e    s   s   s  d MSMH(3) predicts that the low-depreciation regime is expected to persist about 1 year and 9 months on average; and the high-depreciation regime is expected to persist about 3 years and 3 months on average. These long persistence periods in each regime may be an inappropriate depiction of the monthly exchange rate for the following reasons: First and most important, the model does not identify a depreciation regime, which contradicts our visual inspection of Figure 1. Second, as we can see from Figure 1, the trendless and high-appreciation regimes were shorter.

cc

1


<!-- p:16 -->


Table 1 - Estimation results for each model (standard errors in parenthesis). Sample period from January 1995 to September 2019 for the monthly exchange rate and from 1995:II – 2019:II for quarterly exchange rate

| Parameter                      | Model: Monthly Exchange rate - MSMH(3)   | Model: Monthly Exchange rate - HP-MSMH(3)   | Model: Monthly Exchange rate - ES-MSMH(3)   |
|--------------------------------|------------------------------------------|---------------------------------------------|---------------------------------------------|
| μ 1                            | -0.22967 (0.0796)                        | 0.03389 (0.0008)                            | -0.08507 (0.0084)                           |
| μ 2                            | 0.00000 (-)                              | 0.00000 (-)                                 | 0.00000 (-)                                 |
| μ 3                            | 0.67244 (0.1078)                         | 0.09243 (0.0035)                            | 0.16216 (0.0126)                            |
| σ 1                            | 0.22498 (0.0752)                         | 0.00014 (0.00002)                           | 0.00380 (0.0004)                            |
| σ 2                            | 0.04165 (0.0051)                         | 0.00004 (0.000005)                          | 0.00106 (0.0002)                            |
| σ 3                            | 0.24859 (0.0800)                         | 0.001362 (0.00024)                          | 0.01200 (0.0002)                            |
| p 11                           | 0.523 (0.1115)                           | 0.955 (0.0242)                              | 0.866 (0.0008)                              |
| p 22                           | 0.946 (0.0172)                           | 0.990 (0.0137)                              | 0.887 (0.0337)                              |
| p 23                           | 0.304 (0.0365)                           | 0.975 (0.0231)                              | 0.878 (0.0032)                              |
| Model selection test           | Model selection test                     | Model selection test                        | Model selection test                        |
| MSMH(2)&#124;MSMH(3) 5.872***  | MSMH(2)&#124;MSMH(3) 5.872***            | HP-MSMH(2)&#124;HP-MSMH(3) 86.793*          | ES-MSMH(2)&#124;S-MSMH(3) 60.509*           |
| Model: Quarterly Exchange rate | Model: Quarterly Exchange rate           | Model: Quarterly Exchange rate              | Model: Quarterly Exchange rate              |
| μ 1                            | -0.23082 (0.0334)                        | 0.14540 (0.0029)                            | 0.04304 (0.0159)                            |
| μ 2                            | 0.18915 (0.0653)                         | 0.07547 (0.0017)                            | 0.00000 (-)                                 |
| μ 3                            | 0.26088 (0.1407)                         | 0.26867 (0.0071)                            | 0.52495 (0.0529)                            |
| σ 1                            | 0.01427 (0.0071)                         | 0.00035 (0.00006)                           | 0.04454 (0.0153)                            |
| σ 2                            | 0.07604 (0.0319)                         | 0.00021 (0.00003)                           | 0.00897 (0.0153)                            |
| σ 3                            | 0.83489 (0.1765)                         | 0.00133 (0.0006)                            | 0.04713 (0.0132)                            |
| p 11                           | 0.235 (0.0765)                           | 0.943 (0.0394)                              | 0.810 (0.0132)                              |
| p 22                           | 0.476 (0.0654)                           | 0.992 (0.0191)                              | 0.879 (0.0549)                              |
| p 23                           | 0.919 (0.0324)                           | 0.981 (0.0243)                              | 0.737 (0.0364)                              |
| Model selection test           | Model selection test                     | Model selection test                        | Model selection test                        |
| MSMH(2)&#124;MSMH(3) 6.981**   | MSMH(2)&#124;MSMH(3) 6.981**             | HP-MSMH(2)&#124;HP-MSMH(3) 72.888*          | S-MSMH(2)&#124;S-MSMH(3) 15.275*            |

MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic model; HP-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with HP-filter; ES-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with proposed Smoothing filter. ** *** Significant at the 1%, 5% and 10% level, respectively.

cc

1

BY


<!-- p:17 -->


This misidentification is corrected by the ES-MSMH(3) model. First, the model identifies an appreciation regime. Second, estimates indicate that ES s p ts s d  d rid -sist about 7 months on average; while the trendless regime is expected to persist about 9 months on average, and the depreciation regime is expected to persist about 8 months on average. This least persistence in regimes may be a better depiction of the monthly exchange rate's trendless like the one during 2006:06-2008:05, followed by depreciation and an appreciation during the periods of 2008:06-2009:02 and 2009:03-2010:04, respectively, which matches our visual inspection of Figure 1.

However, no long swings are predicted by the unfiltered MSMH(3) model. According to the regime staying probabilities, the appreciation regime is expected to persist for about 2 months; while the depreciation regime is expected to persist for about 1 month; and the trendless regime is expected to persist for about 1 year and 6 months on average. The ES-MS-MH(3) model for regime identification aligns more closely with the Central Bank of Mexico's analysis of exchange rate trends. Filtering the data improves the estimation procedure's accuracy in computing genuine regime shifts.

Regarding the quarterly exchange rate, model HP-MSMH(3) identifies three regimes, namely, a low-depreciation regime, a medium-depreciation regime, and a high-depreciation regime. This model predicts that the low-depreciation regime is expected to persist about 4 years on average; while the medium-depreciation regime is expected to persist about 25 years on average, and the high-depreciation regime is expected to persist about 12 years on average. As in the monthly exchange rate, these long persistence periods in each regime may be an inappropriate depiction of the quarterly exchange rate, since as can be seen in Figure 2, the medium and high depreciation regimes were shorter.

As in the monthly exchange rate, this misidentification is corrected by the ES-MSMH(3) model. First, the model identifies a trendless regime, which is evident from the visual inspection of Figure 2. Then, estimates indicate th ts t   t d   dted to persist about 1 year on average; while the trendless regime is expected to persist about 2 years on average, and the high-depreciation regime is expecet e s s  et  ram  et s  mes may be a better depiction of the quarterly exchange rate's low-depreciation like the one during 2002:IV-2004:I followed by a trendless and a high-depre  -:  :- r ich matches our visual inspection of Figure 2.

cc

1


<!-- p:18 -->


On the other hand, no long swings are predicted by the unfiltered MSMH(3) model. According to the regime staying probabilities, the appreciation regime is expected to persist for about 1 quarter; while the depreciation regime is expected to persist for about 2 quarters; and the medium-depreciation regime is expected to persist for about 2 and a half years on average.

The Markov-Switching model has an innovative feature - it can accurately date the state of the process using smoothed probabilities. Panels (b), (c), and (d) of Figures 3 and 4 show plots of the smoothed probabilities that the process is in each of the three regimes at each date in the sample, estimated by the ES-MSMH(3), MSMH(3) and HP-MSMH(3) models, respectively. Panel (a) shows the monthly and quarterly exchange rates and trend estimates. For comparison, the corresponding dates of each one of the three regimes, as identified by models HP-MSMH(3) and ES-MSMH(3), are presented in Tables 2 and 3 for the monthly and quarterly exchange rates, respectively. The dates at which we conclude that the process had switched between regimes are based on the following cutoff point for the smoothed probabilities p(st = i|In) ≥ 0.5.

Figure 3- (a) Monthly exchange rate and trend estimates; (b), (c), and (d) smoothed probabilities that the process is in each of the three regimes at each date in the sample, estimated by the ES-MSMH(3), MSMH(3), and HP-MSMH(3) models, respectively.

(a)

(b)

22

1.0

20

18

0.6

16

14

04

12

0.2

10

0.0

8

-0.2

1995

1997

1999

2001

2003

2005

2007

2009

2011 2013 2015 2017 2019

1995

1997

1999

2001

2003

2005 2007 2009 2011 2013 2015 2017 2019

Pmbability of the appreciation regime

Pmbability of the depreciation regine

Observed series

Trao s

Trend HP

Protatbilty olf the stagnation regime

(c)

(d)

1.00


0.75


0.50

0.60

0.25


0.00


1995

1997

1999

20012003

2005

2007

2009

2011 2013 2015 2017 2019

1995

1997

1999

2001

2003 2005

2007 2009

2011 2013 2015 2017 2019

Prubability of the appreciation regime

Probability of the depreciation regime

Prutebiíty of the low-depreciation regime

Prubability of the high-depreciation regime

Probability of the stagnation regime

Probebiity of the stagnation regime

<!-- p:19 -->


Figure 4 - (a) Quarterly exchange rate and trend estimates; (b), (c) and (d) smoothed probabilities that the process is in each of the three regimes at each date in the sample, estimated by the ES-MSMH(3), MSMH(3) and HP-MSMH(3) models, respectively.

(a)

(b)

22

1.0

20

0.8

18

0.6

16

14-

0.4

12

02

10

00

8

0.2

6

1995

1997

1999

2001

2003

2005

2007

2009

2011

2013

2015

2017

2019

1995

1997

Probabity of the low-deprecialion regime

1999

2001

2003

2005

2007

2009

Probability of the high-depreciation regime

2011

2013

2015

2017

2019

Observed series

Trend ES

Trend HP

(c)

(d)

1.0

1.00

0.8-

0.75

0.6

0.4

0.50

0.2

0.25

0.0

-0.2-

0.00

1995

1997

1999

2001

2003

2005

2007

2009

2011 2013

2015

207

2019

1995

1997

1999

2001

2003

2005

2007

2009

2011 2013

2015

2017

209

Probability of the arecialion regime

Probability of the high-depreciation regime

Probabiltyof the low-depreciation regime

Probability of the high-deprciation regime

Probability of the low-depreciation regime

Probabityof the mediumn-deprecation regime

Table 2 - Dates of the regimes, as identified by models HP-MSMH(3) and ESMSMH(3). Monthly exchange rates.

| Regimes - Model   | Regimes - Low depreciation   | Regimes - Trendless   | Regimes - High depreciation   |
|-------------------|------------------------------|-----------------------|-------------------------------|
| HP-MSMH(3)        | 1998:05-1999:08              | 1999:09-2001:04       | 1995:02-1998:04               |
|                   | 2001:05-2004:07              | 2004:08-2006:11       | 2008:02-2009:02               |
|                   | 2006:12-2008:01              | 2010:02-2012:07       | 2013:08-2017:07               |
|                   | 2009:03-2010:01              |                       |                               |
|                   | 2012:08-2013:07              |                       |                               |
|                   | 2017:08-2019:08              |                       |                               |
| Regimes           | Regimes                      | Regimes               | Regimes                       |
|                   | Appreciation                 | Trendless             | Depreciation                  |
| ES-MSMH(3)        | 1998:12-1999:04              | 1995:04-1995:06       | 1995:02-1995:03               |
|                   | 2004:11-2005:07              | 1996:02-1997:08       | 1995:07-1996:01               |
|                   | 2009:03-2010:04              | 1999:05-2002:03       | 1997:09-1998:11               |
|                   | 2010:08-2011:04              | 2003:03-2003:06       | 2002:04-2003:02               |
|                   | 2012:01-2012:01              | 2003:12-2004:10       | 2003:07-2003:11               |
|                   | 2012:06-2013:03              | 2005:08-2006:02       | 2006:04-2006:05               |
|                   | 2017:01-2017:07              | 2006:06-2008:05       | 2008:06-2009:02               |
|                   | 2018:12-2019:02              | 2010:05-2010:07       | 2011:06-2011:12               |
|                   |                              | 2011:05-2011:05       | 2012:04-2012:05               |
|                   |                              | 2012:02-2012:03       | 2013:05-2013:08               |
|                   |                              | 2013:04-2013:04       | 2014:06-2016:12               |
|                   |                              | 2013:09-2014:05       | 2018:04-2018:11               |
|                   |                              | 2017:08-2017:08       | 2019:08-2019:08               |
|                   |                              | 2018:01-2018:03       |                               |
|                   |                              | 2019:03-2019:07       |                               |

Note: The dates at which we conclude that the process had switched between regimes are based on the cutoff point p(st = i|IN) ≥ 0.5.

<!-- p:20 -->


Table 3 - Dates of the regimes, as identified by models HP-MSMH(3) and ES-MSMH(3). Quarterly exchange rates.

| Regimes - Model   | Regimes - Low depreciation   | Regimes - Medium depreciation   | Regimes - High depreciation   |
|-------------------|------------------------------|---------------------------------|-------------------------------|
| HP-MSMH(3)        | 1995:II-1999:I               | 1999:II-2012:I                  | 2013:III-2019:II              |
|                   | 2012:II-2013:II              |                                 |                               |
| Regimes           | Regimes                      | Regimes                         | Regimes                       |
|                   | Low depreciation             | Trendless                       | High depreciation             |
| ES-MSMH(3)        | 1995:II-1996:II              | 1996:III-1997:III               | 1997:IV-1998:III              |
|                   | 1998:IV-1998:IV              | 1999:I-2002:I                   | 2002:II-2002:III              |
|                   | 2002:IV-2004:I               | 2004:II-2008:II                 | 2008:III-2009:I               |
|                   | 2009:II-2010:II              | 2010:III-2011:II                | 2011:III-2011:III             |
|                   | 2011:IV-2012:II              | 2012:III-2014:II                | 2014:III-2016:IV              |
|                   | 2017:I-2018:IV               | 2019:I-2019:II                  |                               |

Note: The dates at which we conclude that the process had switched between regimes are based on the cutoff point p(st = i|IN) ≥ 0.5.

The monthly exchange rate trendless identified by the ES-MSMH(3) model during 2006:06-2008:05 followed by a depreciation and an appreciation durs  :-:0  20:-:00  0es special attention since this entire period includes the global financial crisis.

As per the Mexican Central Bank's Annual Report of 2006, the exchange rate remained stable throughout the year, except for a brief depreciation - os      o   y o onn vironment, where the financial market witnessed a speculative phase because of the robust economic growth and high oil prices. The international financial market's uncertainty, in turn, led to increased volatility, which raised the domestic interest rates and caused a depreciation in Mexico's exchange rate. Besides, the uncertainty surrounding the presidential election also contributed to the exchange rate's depreciation. During electoral campaigns, economic agents received information from competing parties, which caused great uncertainty about who would win the election. Such periods are usually associated with policy modifications that may affect the government's involvement with the exchange rate, and the uncertainty in expectations related to political events during election periods contributed to a risk premium in the exchange rate market. However, the international financial uncertainty dwindled after the election, and the favorable conditions for the exchange rate prevailed until mid-2008.

In 2008, the global economy and financial markets faced a crisis due to t s nse s s se .   ns ms aea financial crisis that affected various countries, including Mexico. The foreign exchange market in Mexico experienced liquidity problems because firms demanded more foreign currency derivatives. Mexico's Central Bank intervened by holding foreign currency auctions known as extraordinary auctions to address this issue. Figure 1 shows that the exchange rate depreciation began in June 2009, and it reached its maximum in March 2009, when the US Dollar-Mexican peso parity hit 15.6.

1

BY


<!-- p:21 -->


According to Benavides (2011), the Mexican currency depreciated nearly 5n   o      s al Bank to take action in the foreign exchange market by providing liquidity. Due to the high volatility in October 2008, Mexico's Central Bank conducted direct, non-coordinated interventions that amounted to USD 400 million. These interventions are publicly announced and are intended to influence exchange rates, and by December 15, USD 178 million had been sold in these auctions. Mexico's Central Bank also established a temporary currency agreement with the U.S. Federal Reserve on October 29, 2008, for up to USD 30 billion. This agreement was effective until oi  cs    cal institutions in Mexico. Benavides (2011) argues that during this period of high instability, the Central Bank's interventions were the only significant macroeconomic shocks.

The Mexican Central Bank's 2009 Annual Report states that in the first two months of that year, a regime where the exchange rates depreciated and became more volatile because of the adverse international environment prevailed. 2009 was uncertain in the maneuver of public finances caused by the reduction in oil revenues and the expectations of non-oil revenues.

Mexican authorities took coordinated actions to instill confidence and provide liquidity to the financial markets to reduce uncertainty. The Mexican Central Bank identified the following measures as the most significant: (i) The Foreign Exchange Commission, on three occasions, published assessments on the balance of payments for the year to build confidence. These assessments revealed that Mexico had no issues financing its current account deficit, which resulted in increased net exports and decreased the deficit. (ii) In 2009, the Mexican Central Bank provided liquidity to the foreign exchange markets by selling USD 16,246 million. (iii) On April 17, 2009, Mexico was granted a Flexible Credit Line up to USD 31,528 million in Special Drawing Rights by the International Monetary Fund, which helped boost confidence in the Mexican economy.

cc

1


<!-- p:22 -->


Because of these measures, the risk perception of the Mexican economy began to improve by March 2009. This improvement in risk perception generated better conditions in financial markets and economic growth. In response to the measures taken by financial authorities and the overall improvement in the global financial environment, the depreciation period and high volatility that started in June 2008 were reverted in March 2009. Consequently, the exchange rate of some emerging economies, including the Mexican, entered a period of appreciation that lasted until 2010 and later remained stable.

A close examination of these results reveals that the ES-MSMH(3) model can adequately capture the movements of the exchange rate and, therefore, improve its forecasting performance, as shown below.

### 4.1. A forecasting exercise

The accuracy of Markov-Switching models' predictions highly relies on the regime in which the forecast is made, so it only requires a small misclassification of which regime the process will be in to lose the advantage of knowing the correct model specification. One important question to consider is: Given that the filtered model works well in capturing the trend persistence of exchange rate, can it outperform, in terms of Mean Squared Error (MSE), some linear alternatives, specifically the simple random walk? (Yuan, 2011)

It is quite standard to assume that the optimal predictor is given by the conditional mean for a given information set Lt. Nevertheless, in contrast to linear models, the MSE optimal predictor does not have the property of being a linear predictor if the true data generating process is nonlinear. In general, the derivation of the optimal predictor may be quite complicated in empirical work. However, an attractive feature of Markov-Switching models as a class of nonlinear models is the simplicity of forecasting if the optimal predictor is the conditional expectation.

Following Hamilton (1994), let ξt|t be the k×1 vector of conditional probabilities, P{st = j|Lt; θ}, for j= 1,2,...,k, which are estimates of the value of st based on data obtained through date t. Given the maximum likelihood estimator, ê, the h-period ahead forecast of yt+h is given by:

$$\hat { y } _ { t + h | t } = E [ y _ { t + h } | \mathcal { L } _ { t } ; \hat { \theta } ] = \xi ^ { \prime } _ { t + h | t } * \hat { \mu } = \xi ^ { \prime } _ { t | t } * P ^ { h } * \hat { \mu }$$

cc

BY


<!-- p:23 -->


where β = (β1, 2, ..., Îk)′ is the vector of estimates of the mean-dependent trends. We generated h-period ahead forecasts of the level of exchange rates as:

$$\hat { e } _ { t + h | t } = e _ { t } + \sum _ { j = 1 } ^ { h } \hat { y } _ { t + j | t }$$

and calculated the average squared value of the forecast error as:

$$\sum _ { t = 1 } ^ { N - h } \left ( \hat { e } _ { t + h | t } - e _ { t + k } \right ) ^ { 2 } / ( N - h )$$

po  o on n  .  cn c ond h=1,2,3,..,12 for the monthly exchange rate.

As is well known, the standard for measuring forecast ability in the context of exchange rate is whether the proposed model can do well in forecasting in relation to a random walk. Tables 4 and 5 present the MSEs of the in-sample and out-of-sample forecasts and compares them with those of a random walk specification, whose forecasts are given by êt+h|t = et + hy, with y = Σt=1 yt/N, for the monthly and quarterly exchange rates, respectively.

To evaluate the out-of-sample forecasting performance of the models, we re-estimated the parameters with data up to the end of 2015. We chose this date so as not to consider the period prior to the 2016 U.S. presidential election where the Mexican peso had been under pressure given Trump's campaign promises to renegotiate the North American Free Trade Agreement (NAFTA). The Mexican peso had an inverse correlation to the -oe    h n Tr  n n   nnc tion the further the peso depreciated. There were a lot of unknowns about how the Trump presidency would unfold and how his trade and tariff agenda would impact NAFTA. Without a doubt, the uncertainty during this period of political potential change contributed to the existence of a risk premium in the exchange rate market. Hence, almost the entire period of Trump's administration where the Mexican exchange rate has been depreciated was not used for parameter estimation. Furthermore, with our out-of-sample forecast our model must meet the challenge of picking out this depreciation period. The parameter estimates for the truncated sample are similar to those of the full sample; using only data through 2015, there is also evidence in favor of the long swings movements.

1


<!-- p:24 -->


Table 4 presents the in-sample and out-of-sample mean squared error of forecast. As it can be observed in Table 4, panel A, for the monthly exchange rate, the average loss in in-sample forecast accuracy is about -1.18% for the unfiltered model MSMH(3), while for the two filtered models HP-MSMH(3) and ES-MSMH(3) the improvement is about 10.8% and 11.63%, respectively, averaging over the 12 months-ahead horizons. We further notice that the two filtered Markov-Switching models well outperform the unfiltered model during the forecast horizon considered. The average improvement in out-of-sample forecast precision is about 1.21% for the unfiltered model MSMH(3), -6.4% loss accuracy for the filtered model HP-MSMH(3), and 8.74% improvement for the filtered model ESMSMH(3), averaging over the forecast horizon up to 12 months. We further notice that the MSMH(3) and ES-MSMH(3) models well outperform the random walk and the filtered model HP-MSMH(3). It is worth noting that ES-MSMH(3) model achieves forecast accuracy improvement from a trivial 0.93% at the one month horizon to a significant 21.50% at the six month horizon.

On the other hand, Table 5 shows that for the quarterly exchange rate, the average loss in the in-sample forecast precision is about -1.50% for the unfiltered model MSMH(3), while for the two filtered models HPMSMH(3) and ES-MSMH(3) the improvement is about 4.41% and 9.63%, respectively, averaging over the four quarters-ahead horizons. We further notice that the two filtered Markov-Switching models well outperform the unfiltered model during the forecast horizon considered. The average improvement in out-of-sample forecast precision is about 11.68% for the filtered model ES-MSMH(3), while for the unfiltered model MSMH(3) and the filtered model HP-MSMH(3) the loss is about -1.16% and -8.37%, respectively, averaging over the forecast horizon up to four quarters. We further notice that the ES-MSMH(3) model well outperforms the random walk slightly more prominently in particular for the four-period-ahead forecast, with a significant 15.66% of accuracy improvement.

Interestingly, introducing a trendless regime to the ES-MSMH(3) model, one can see that this forecast model is robust in beating the random walk across the monthly and quarterly (Mexican Pesos / U. S. Dollar) exchange rate.

cc


<!-- p:25 -->


Table 4 - In-sample and out-of-sample MSE of the forecasts at horizons from one to twelve months.

Ee es ord  o  soe-m -eg i- = (m-e. HP-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with HP-filter; MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic model;

Out-of-sample Mean Squared Forecast Error where k is the forecast horizon.

| In-sample Mean Squared Error Forecast horizon   | 12               | 1.43199   | 1.46115   | -2.03%   | 1.16561   | -1.74% 18.60%                   | 1.29322 9.69%                                              |
|-------------------------------------------------|------------------|-----------|-----------|----------|-----------|---------------------------------|------------------------------------------------------------|
|                                                 | 1.09414          | 11        | 1.33403   | 1.36268  | -2.14%    | 17.98%                          | 1.20535                                                    |
|                                                 | 9.64%            |           | 10        | 1.25198  | 1.27983   | -2.22%                          | 1.0401 16.19%                                              |
|                                                 | 1.00820 1.12818  | 9.88%     |           | 9        | 1.18939   | 1.21208                         | -1.90%                                                     |
|                                                 | 15.23%           | 1.06908   | 10.11%    |          | 8         | 1.08884                         | 1.10779                                                    |
| 0.93983                                         | 13.68%           | 0.96576   | 11.30%    |          | 7         | 0.99409                         | 1.00920                                                    |
| 0.87842                                         | 0.77122 11.63%   | 0.87063   | 12.41%    | Forecast | 6         | 0.85595 -1.52%                  | 0.86750                                                    |
| -1.34%                                          | 0.66575 9.89%    | 0.73707   | 13.88%    |          | 5         | 0.72340                         | 0.73064                                                    |
| -1.00%                                          | 0.57566 7.96%    | 0.62126   | 14.11%    |          | 4         | 0.61130                         | 0.61437                                                    |
| -0.50%                                          | 5.82%            | 0.52757   | 13.69%    |          | 3         | 0.47290                         | 0.47399                                                    |
| -0.23% 0.45357                                  | 0.31414 4.08%    | 0.40855   | 13.60%    |          | 2         | 0.32236                         | 0.32217                                                    |
| 0.05%                                           | 2.54%            | 0.28216   | 12.46%    |          | 1         | 0.16812                         | 0.16749                                                    |
| 0.37% 0.16600                                   | HP-MSMH(3) 1.26% | 0.15340   | 8.75%     |          | Model     | Random walk Percent improvement | MSMH(3) Percent improvement ES-MSMH(3) Percent improvement |

| 12         | 1.59302     | 1.57162   | 1.34%               | 1.95189                        | -22.5%     | 1.50421 5.57%       |
|------------|-------------|-----------|---------------------|--------------------------------|------------|---------------------|
| 11         | 1.78010     | 1.77876   | 0.07%               | 2.02585 -13.80%                | 1.60735    | 9.70%               |
| 10         | 1.81443     | 1.80879   | 0.31%               | 2.03328 -12.0%                 | 1.61357    | 11.07%              |
| 9          | 2.09929     | 2.09531   | 0.18%               | 2.28061 -8.63%                 | 1.87107    | 10.87%              |
| 8          | 2.02347     | 2.02100   | 0.12%               | 2.16578 -7.03%                 | 1.79510    | 11.28%              |
| horizon 7  | 1.84847     | 1.84908   | -0.03%              | 1.94699 -5.32%                 | 1.62922    | 11.86%              |
| Forecast 6 | 1.49569     | 1.30932   | 12.46%              | 1.40786 5.87%                  | 1.1740     | 21.50%              |
| 5          | 1.29732     | 1.29871   | -0.10%              | 1.34057 -3.33%                 | 1.15392    | 11.05%              |
| 4          | 1.20637     | 1.20629   | 0.00%               | 1.23652 -2.49%                 | 1.12806    | 6.49%               |
| 3          | 1.06824     | 1.06794   | 0.02%               | 1.09015 -2.05%                 | 1.03664    | 2.95%               |
| 2          | 0.78711     | 0.78668   | 0.05%               | 0.79550 -1.06%                 | 0.77414    | 1.64%               |
| 1          | 0.49089     | 0.49015   | 0.14%               | 0.49112 -0.04%                 | 0.48636    | 0.92%               |
| Model      | Random walk | MSMH(3)   | Percent improvement | HP-MSMH(3) Percent improvement | ES-MSMH(3) | Percent improvement |

No0:  + : =1  s e s se s e   :0 - 0:s s s   se - 08

Out-of-sample forecast errors. Estimation sample 1995:02 - 2015:12 and MSEs are associated with forecasts for dates t=2016:01 +k to 2019:08 where k

is the forecast horizon.


<!-- p:26 -->


Table 5 - In-sample and out-of-sample MSE of the forecasts at horizons from one to four quarters.

| Model               | In-sample Mean Squared Forecast Error - Forecast horizon - 1   | In-sample Mean Squared Forecast Error - Forecast horizon - 2   | In-sample Mean Squared Forecast Error - Forecast horizon - 3   | In-sample Mean Squared Forecast Error - Forecast horizon - 4   |
|---------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Random walk         | 0.461369                                                       | 0.836660                                                       | 1.139401                                                       | 1.371647                                                       |
| MSMH(3)             | 0.456362                                                       | 0.838754                                                       | 1.166974                                                       | 1.43230                                                        |
| Percent improvement | 1.08%                                                          | -0.25%                                                         | -2.41%                                                         | -4.42%                                                         |
| HP-MSMH(3)          | 0.455124                                                       | 0.834895                                                       | 1.06652                                                        | 1.238349                                                       |
| Percent improvement | 1.35%                                                          | 0.21%                                                          | 6.39%                                                          | 9.71%                                                          |
| ES-MSMH(3)          | 0.417206                                                       | 0.751467                                                       | 1.034488                                                       | 1.25331                                                        |
| Percent improvement | 9.57%                                                          | 10.18%                                                         | 9.205%                                                         | 8.62%                                                          |

| Model               | Forecast horizon - 1   | Forecast horizon - 2   | Forecast horizon - 3   | Forecast horizon - 4   |
|---------------------|------------------------|------------------------|------------------------|------------------------|
| Random walk         | 1.114498               | 1.550066               | 2.320946               | 1.743215               |
| MSMH(3)             | 1.117218               | 1.559538               | 2.341984               | 1.794076               |
| Percent Improvement | -0.24%                 | -0.61%                 | 0.90%                  | -2.91%                 |
| HP-MSMH(3)          | 1.132383               | 1.59765                | 2.450035               | 2.148463               |
| Percent Improvement | -1.60%                 | -3.06%                 | -5.56%                 | -23.24%                |
| ES-MSMH(3)          | 1.068872               | 1.339254               | 2.011991               | 1.470084               |
| Percent Improvement | 4.09%                  | 13.60%                 | 13.31%                 | 15.66%                 |

Out-of-sample Mean Squared Forecast Error

Notes: In-sample forecast errors. Estimation sample 1995:II - 2019:II and MSEs are those associated with forecasts for dates t=1995:II+k to 2019:II where k is the forecast horizon.

Oss s     i - i os os sc s --ith forecasts for dates t=2016:I+k to 2019:II where k is the forecast horizon.

MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic model;

HP-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with HP-filter;

ES-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with proposed Smoothing filter.

### 4.2. Forecast evaluation

To complement the previous analysis of forecast bias and precision we now focus on forecast accuracy. Tables 6 and 7 present Diebold-Mariano (DM) test statistics (see Diebold and Mariano, 2002) for the null hypothesis of no difference in the accuracy of two competing forecasts, that is, the unfiltered and the two filtered models versus the random walk. Each calculated statistic should be compared with a standard normal distribution in order to declare statistical significance. However, since the standard DM test is known to over-reject the null hypothesis in the context of finite samples, we applied here the modified DM test proposed by Harvey, Leybourne and Newbold (1997).

BY


<!-- p:27 -->


Table 6 - Diebold-Mariano test for relative forecasting ability. Monthly exchange rate.

| 12         |                 | 0.9865    | 0.3912   | 0.3478   |                    | 1.2252    | -1.8400   | 0.9671                    | 0.9442    | 0.7729   | 0.2198   |
|------------|-----------------|-----------|----------|----------|--------------------|-----------|-----------|---------------------------|-----------|----------|----------|
| 11         |                 | 0.9992    | 0.0265   | 0.4894   |                    | 1.1380    | -1.2945   | 0.9022                    | 0.9029    | 1.4992   | 0.0669   |
| 10         |                 | 0.9968    | 0.1329   | 0.4471   |                    | 1.1206    | -1.2591   | 0.8960                    | 0.8893    | 1.8861   | 0.0296   |
| 9          |                 | 0.9981    | 0.1040   | 0.4585   |                    | 1.0863    | -1.0788   | 0.8596                    | 0.8912    | 2.2033   | 0.0137   |
| 8          |                 | 0.9987    | 0.0815   | 0.4675   |                    | 1.0703    | -0.9709   | 0.8342                    | 0.8871    | 2.5115   | 0.0060   |
| horizon 7  |                 | 1.0003    | -0.0268  | 0.5107   |                    | 1.0532    | -0.8039   | 0.7892                    | 0.8813    | 2.9854   | 0.0014   |
| Forecast 6 |                 | 0.8754    | 0.8756   | 0.1906   |                    | 0.9412    | 0.3916    | 0.3476                    | 0.7849    | 1.5019   | 0.0665   |
| 5          |                 | 1.0010    | -0.1493  | 0.5593   |                    | 1.0333    | -0.5900   | 0.7224                    | 0.8894    | 3.1186   | 0.0009   |
| 4          |                 | 0.9999    | 0.0162   | 0.4935   |                    | 1.0249    | -0.5330   | 0.7029                    | 0.9350    | 2.3218   | 0.0101   |
| 3          |                 | 0.9997    | 0.1242   | 0.4505   |                    | 1.0205    | -0.5486   | 0.7083                    | 0.9704    | 1.1182   | 0.1317   |
| 2          |                 | 0.9994    | 0.3870   | 0.3493   |                    | 1.0106    | -0.3663   | 0.6429                    | 0.9835    | 0.6217   | 0.2670   |
| 1          |                 | 0.9985    | 0.6803   | 0.2481   |                    | 1.0004    | -0.0263   | 0.5105                    | 0.9907    | 0.5388   | 0.2950   |
| Models     | MSMH(3) vs . RW | MSE Ratio | DM-stat  | p-value  | HP-MSMH(3) vs . RW | MSE Ratio | DM-stat   | p-value ES-MSMH(3) vs. RW | MSE Ratio | DM-stat  | p-value  |

ES-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with Exponential hing filter. HP-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with HP-filter; oe:-: d   0:-:6 d     0. RW = random walk; MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic model;

Cc


<!-- p:28 -->


Table 7 - Diebold-Mariano test for relative forecasting ability. Quarterly exchange rate.

| Models             |   Forecast horizon - 1 |   Forecast horizon - 2 |   Forecast horizon - 3 |   Forecast horizon - 4 |
|--------------------|------------------------|------------------------|------------------------|------------------------|
| MSMH(3) vs . RW    |                        |                        |                        |                        |
| MSE Ratio          |                 1.0024 |                 1.0061 |                 1.0090 |                 1.0291 |
| DM-stat            |                -0.1259 |                -0.2378 |                -0.3711 |                -1.1034 |
| p-value            |                 0.5500 |                 0.5939 |                 0.6447 |                 0.8650 |
| HP-MSMH(3) vs . RW |                        |                        |                        |                        |
| MSE Ratio          |                 1.0160 |                 1.0307 |                 1.0556 |                 1.2324 |
| DM-stat            |                -0.2199 |                -0.2449 |                -0.3558 |                -0.9485 |
| p-value            |                 0.5870 |                 0.5967 |                 0.0639 |                 0.8285 |
| S-MSMH(3) vs. RW   |                        |                        |                        |                        |
| MSE Ratio          |                 0.9590 |                 0.8640 |                 0.8668 |                 0.8432 |
| DM-stat            |                 1.2426 |                 1.5314 |                 1.2773 |                 0.8350 |
| p-value            |                 0.0690 |                 0.0683 |                 0.0687 |                 0.2018 |

RW = random walk; MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic model;

HP-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with HP-filter;

ES-MSMH(3) = 3-regime Markov-Switching Mean-Heteroskedastic filtered model with Smoothing filter.

Forecasts are based on estimated period 1995:I-2015:IV and forecast periods 2016:I-2019:II

The DM test results reported in Tables 6 and 7 support our findings in the lower panels of Tables 4 and 5. In this context, the null hypothesis of no difference in the accuracy of our proposed model, ES-MSMH(3), and the Random Walk Model is rejected for 8 out of the 12 analyzed forecast horizons for monthly data and for 3 out of the 4 horizons for quarterly data at a 10% significance level. There is no other null hypothesis rejection for the competing models, except the HP-MSMH (3) model for the 3-quarters forecast horizon.

## 5. Conclusions

This paper proposes the ES filter for estimating a trend with controlled smoothness in order for a Markov-Switching model to be applied more appropriately to detect different regimes in the time series of exchange rates. After identifying the different regimes and the probabilities of staying in each of the regimes estimated, the model was utilized to predict the exchange rate. The ES filter also enables us to set a target percentage for the smoothness of the trend, making it possible to compare different applications with varying time series or sample periods of the same series, as highlighted by Guerrero and Galicia-Vazquez (2010). Our results have found that by using a Multi-State Markov-Switching model in conjunction with the controlled smoothing filter technique, we can improve both in-sample and out-of-sample forecasting performance. Preliminary results obtained by applying the conventional model without a filtering technique warned us that the existence of highly irregular components in the data tends to distort the estimation procedure of the Markov-Switching model and undermines its forecasting power. Our suggested specification eliminates the modeling nuisance and enhances the forecasting superiority of the Markov-Switching model. We conducted an empirical application using three Multi-State Markov-Switching model specifications and found that the one based on our proposal was superior for parameter estimation and generated statistically better forecasts. This strong empirical evidence supports our proposed procedure. The results obtained in this particular application were clear in defining three different regimes associated with the behavior of the exchange rate: appreciation, trendless, and depreciation which can be easily and visually appreciated in the data under study. Our results show that correctly identifying the trend in the exchange rate plays a crucial role in achieving superior forecasting ability concerning the simple random walk. As a final conclusion, we want to emphasize that applying the HP filter to an I(1) time series does not produce optimal results. Our proposed procedure is data-driven, making it more objective than the HP filter. The smoothing parameter is determined by selecting a desired level of smoothness for the trend, which can be easily determined by following data-based guidelines.

cc

BY


<!-- p:29 -->
