---
id: "07_Forecasting_Remittances_to_Mexico"
source_pdf: "../pdf/07_Forecasting_Remittances_to_Mexico.pdf"
source_filename: "07_Forecasting_Remittances_to_Mexico.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/07_Forecasting_Remittances_to_Mexico.references.md"
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
