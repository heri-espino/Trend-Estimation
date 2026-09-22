---
id: "26_Tests_of_Conditional_Predictive_Ability"
source_pdf: "../pdf/26_Tests_of_Conditional_Predictive_Ability.pdf"
source_filename: "26_Tests_of_Conditional_Predictive_Ability.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/26_Tests_of_Conditional_Predictive_Ability.references.md"
---

<!-- p:1 -->

## Tests of conditional predictive ability

Raffaella Giacomini and Halbert White*

University of California, San Diego

This version: April 2003

###### Abstract

We argue that the current framework for predictive ability testing (e.g.,West, 1996) is not necessarily useful for real-time forecast selection, i.e., for assessing which of two competing forecasting methods will perform better in the future. We propose an alternative framework for out-of-sample comparison of predictive ability which delivers more practically relevant conclusions. Our approach is based on inference about conditional expectations of forecasts and forecast errors rather than the unconditional expectations that are the focus of the existing literature. We capture important determinants of forecast performance that are neglected in the existing literature by evaluating what we call the forecasting method (the model and the parameter estimation procedure), rather than just the forecasting model. Compared to previous approaches, our tests are valid under more general data assumptions (heterogeneity rather than stationarity) and estimation methods, and they can handle comparison of both nested and non-nested models, which is not currently possible. To illustrate the usefulness of the proposed tests, we compare the forecast performance of three leading parameter-reduction methods for macroeconomic forecasting using a large number of predictors: a sequential model selection approach, the "diffusion indexes" approach of Stock and Watson (2002), and the use of Bayesian shrinkage estimators.

*Discussions with Clive Granger, Graham Elliott and Andrew Patton were essential to the paper. We also wish to

h t   d s   d r  ut d d z se

LSE, University of Exeter, University of Warwick, University of Manchester, Cass Business School, North Carolina

State University, Boston College, Texas A&amp;M, University of Chicago GSB, the International Finance Division of the

Federal Reserve Board and the 2002 EC2 conference in Bologna, Italy for helpful comments. The computations in

the paper were carried out in the UCSD Experimental and Computational Laboratory, for which we thank Vince

Crawford. Corresponding author: Raffaella Giacomini, Department of Economics, University of California, San

Diego, 9500 Gilman Dr., La Jolla, CA 92093-0508, U.S.A. Web page: http://www.econ.ucsd.edu/~rgiacomi. E-mail:

rgiacomini@ucsd.edu.


<!-- p:2 -->


##### 1Introduction

Forecasting is central to economic decision-making. Government institutions and regulatory authorities often base policy decisions on forecasts of major economic variables, and firms rely on forecasting for inventory management and production planning decisions. A problem that economic forecasters often face is how to select the best forecasting method from a set of two (or more) alternatives. The econometric answer to this problem is to develop tests for comparing the predictive ability of two alternative forecast methods, given the forecaster's loss function. The literature on forecast comparison has witnessed a renaissance in recent years, and a number of authors have proposed econometric techniques for forecast comparison under general loss functions, known as out-of-sample predictive ability testing. This literature was initiated by Diebold and Mariano (1995) and further formalized by West (1996), West and McCracken (1998), McCracken (2000), Clark and McCracken (2001), Corradi, Swanson and Olivetti (2001), Chao, Corradi and Swanson (2001), among others, and it represents a generalization of several existing evaluation techniques which typically restricted attention to a particular loss function (e.g., Granger and Newbold 1977, McCulloch and Rossi 1990, Leitch and Tanner 1991, West, Edison and Cho 1993, Harvey, Leybourne and Newbold 1997).

In this paper, we argue that the current framework for out-of-sample predictive ability testing (which in the remainder of the paper we consider to be represented by West, 1996) is not necessarily appropriate for real-time forecast selection, i.e., for assessing which of two competing forecasting methods will give better forecasts in the future. We propose an alternative approach to outof-sample predictive ability testing that delivers inferences that are more relevant to economic forecasters. Our tests can be applied to multi-step point, interval, probability or density forecasting, and they can be viewed as a generalization of the tests of West (1996) since they are applicable in all cases in which his tests are applicable and in many more besides.

From a methodological point of view, the main idea of the paper is to view the problem of forecast evaluation as a problem in inference about conditional expectations of forecasts and forecast errors rather than the unconditional expectations that are the focus of the approach of West (1996).

An important distinction between our approach and the existing literature is that we consider the object of the evaluation to be what we call the "forecasting method", which includes not only the forecast model but also a number of choices that must be made by the forecaster at the time of the prediction, such as which estimation procedure to choose and which data to use for estimation. The current approach to forecast evaluation focuses instead solely on the forecast model. The reason for evaluating the forecasting method and not just the model is that all elements of the method can affect future forecast performance: a good model can produce bad forecasts if its parameters are not precisely estimated or if they change over time. The fact that we consider the forecasting method rather than the model implies that our tests can lead to a different conclusion than West's (1996) tests. Suppose for example that one of the two models is correctly specified but has a large number of parameters, while the competitor is a simpler, misspecified model. West's (1996) test will tend to choose the large model, while our tests may choose the forecasting method that uses the small model, especially if we are in the presence of high estimation uncertainty.


<!-- p:3 -->


Our approach is applicable in many situations where the tests of West (1996) are not valid. One such case is when the data are heterogeneous, in the form of time-varying underlying processes for the series of interest. As emphasized by Clements and Hendry (1998, 1999), this is a more realistic assumption for economic forecasting contexts than the assumption of stationarity that is typically made in the literature. The assumption of heterogeneity also affects the approach to estimation. In this context, instead of considering a recursive forecasting scheme, where the estimation window expands over time, it makes sense to consider a rolling window forecast procedure where the forecasts are based on a moving window of the data which discards old observations. The size of the estimation window can itself be time-varying, as in the procedure suggested by Pesaran and Timmermann (2002). A fundamental difference with the existing literature is that here we consider the estimation window to be a component of the forecasting method under evaluation. In the existing literature, instead, the sample split between estimation and evaluation samples is arr e t    o   e   e e

Another situation where the tests of West (1996) are not applicable is in comparing forecasts based on nested models. This is an important comparison because many models considered for forecasting are naturally derived as generalizations of existing models and it is often of interest to test if a larger, more sophisticated model can outperform a simple, nested benchmark model. Our framework permits a unified treatment of nested and non-nested models.

Finally, the current framework for predictive ability testing is not valid when the forecasts are obtained by using estimation methods such as Bayesian estimation, semi-parametric, or nonparametric estimation. Our framework, instead, can accommodate such estimation procedures and can thus be used to compare the impact on forecast performance of using different estimation techniques, a question that cannot be answered within the current framework.

A final, practical advantage of our tests is that they are easily computed using standard regression packages, whereas the existing tests can be quite difficult to compute or have limiting distributions that are context-specific (e.g., Clark and McCracken, 2001).

To illustrate the usefulness of the conditional predictive ability tests, we consider the problem of macroeconomic forecasting using a large number of predictors and compare forecasts of eight macroeconomic variables obtained by employing leading methods for parameter reduction: a sequential procedure which is a simplified version of the general-to-specific model selection approach implemented by Hoover and Perez (1999), the "diffusion indexes" approach of Stock and Watson


<!-- p:4 -->


(2002) and the use of Bayesian shrinkage estimators (Litterman, 1986). We use the data set of Stock and Watson (2002), including monthly U.S. data on 146 macroeconomic variables and evaluate 1-, 6- and 12-month ahead forecasts of four measures of real activity and four price indexes obtained using the different forecasting methods. The general conclusion is that for the price indexes the forecast performance of the three methods is indistinguishable from that of a univariate autoregression. For the real variables, instead, Bayesian shrinkage appears to be the preferred method. Finally, the sequential model selection approach performs poorly for most variables and forecast horizons, and it is often outperformed by the naive autoregressive and random walk benchmarks.

### 2 Unconditional and conditional approaches to predictive ability testing

To illustrate the differences between conditional and unconditional out-of-sample predictive ability testing, suppose we are interested in comparing the accuracy of two competing forecasting models ft(β1) and gt(β2) for the conditional mean of the variable of interest Yt+1, given a squared error loss function. The dependence of the forecasts on parameters β1 and β2 indicates that in this example s ots  os (is   r  g ors os t tul hypothesis of equal accuracy of the two forecasts formulated as

$$H _ { 0 } \colon E [ ( Y _ { t + 1 } - f _ { t } ( \beta _ { 1 } ^ { * } ) ) ^ { 2 } - ( Y _ { t + 1 } - g _ { t } ( \beta _ { 2 } ^ { * } ) ) ^ { 2 } ] = 0 ,$$

where β1 and β2 are population values of the parameters (i.e., probability limits of the parameter estimates). The null hypothesis (1) can be interpreted as saying that the two forecast models are equally accurate on average. If the null hypothesis is rejected, one would choose the model yielding the lower loss. Notice that a test of the null hypothesis (1) will tend to choose a forecast based on a correctly specified model (i.e., the test will choose the correctly specified model asymptotically with probability 1 − α, where α is the level of the test).1 A focus on the null hypothesis (1) is thus justifiable if one is interested in establishing which of two models better approximates the datagenerating process. However, even a model that well approximates the data-generating process may forecast poorly, for example in the case that its parameters are imprecisely estimated. If the question is which model will give better forecasts in the future, therefore, it is not clear that (1) is in fact the appropriate null hypothesis.

The central idea of this paper is to test a null hypothesis different than (1), where the expectation is conditional on the information set Ft available at time t and the losses depend on the parameter estimates at time t, β1t and β2t, rather than on their probability limits:

1To see why, suppose forecast 1 is based on a correctly specified model, which implies that ft(β1) is the true conditional mean of Yt+1. Also assume for simplicity that the two forecasts are based on the same information set. Sn o   t  o   o   o  mt l o cted loss: E[(Yt+1 − ft(β1))2] &lt; E[(Yt+1 − ft)2] for any other forecast ft, and thus in particular for gt(β2).


<!-- p:5 -->


$$H _ { 0 } \colon E [ ( Y _ { t + 1 } - f _ { t } ( \hat { \beta } _ { 1 t } ) ) ^ { 2 } - ( Y _ { t + 1 } - g _ { t } ( \hat { \beta } _ { 2 t } ) ) ^ { 2 } | \mathcal { F } _ { t } ] = 0 \ \text {almost surely, } t = 1 , 2 , \dots \quad ( 2 )$$

We call a test of the hypothesis (2) a test of equal conditional predictive ability. The motivation for conducting inference about a conditional, rather than an unconditional, expectation is that it more closely represents the real-time problem of a forecaster. In particular, we can view this hypothesis as saying that the forecaster cannot predict which of the two forecasts will be more accurate, given what is known today.

Further motivation for expressing the null hypothesis in terms of time-t parameter estimates rather than probability limits is that they are more relevant for the forecaster: since the population parameters are not known and must be estimated, it is the actual future loss that is of interest to the forecaster, rather than that based on some population value that is only attained in the limit. As a result, whereas the unconditional tests restrict attention to the forecast model, the conditional approach allows evaluation of the forecasting method, which includes the model, the estimation procedure and the possible choice of estimation window. Viewed this way, it appears obvious that considering the forecasting method as a whole is appropriate, as each of its components can have a potential impact on future forecast performance.

In the following subsections, we outline in detail the directions along which the conditional testing framework represents a more realistic environment for forecast evaluation and discuss how it directly accounts for different determinants of forecast performance that are neglected by the unconditional framework.

## 2.1 Heterogeneity of economic data

One of the conclusions of Clements and Hendry (1998, 1999) is that the main explanation for systematic forecast failure in economics is a non-constant underlying process generating the series to be forecast. It is thus of fundamental importance to develop evaluation techniques that take into account the possibly heterogeneous nature of economic variables. In this paper, we therefore work with the assumption that the data generating process is heterogeneous rather than stationary.2 In our view, this is a realistic and practical assumption for economic forecasting contexts and more plausible than the perhaps idealistic assumption of stationarity typically made in the unconditional predictive ability literature. Specific sources for heterogeneity in the series that economists forecast are several. First, even if the underlying economic processes were stationary, heterogeneity in the observed time series can arise from changes in the measurement process. This source of heterogeneity is one that macroeconomic variables are particularly sensitive to; among other things: the definition of the measured variables may change from time to time; which entities are measured in constructing the variables measured changes; budgets for the economic, demographic, and statistical agencies measuring the processes of interest change, leading to the possibility of greater or lesser care in producing the official numbers on strict time schedules; and directors and other key personnel of these agencies regularly join and leave, leading to intentional or unintentional variations in the processes and procedures that produce the official time series. Heterogeneity in even one of these sources would produce heterogeneity in the observed series. These sources of heterogeneity are plausibly less a concern for non-aggregated time series, such as the prices of welldefined commodities, as in financial economics. Nevertheless, the underlying economic processes themselves are comprised of a variety of forces that operate as further sources of heterogeneity, affecting either the nature of the commodity itself, or the way the commodity is traded. With regard to the latter, the laws and regulations governing trade change, and the technologies used by buyers and sellers of the commodities change. (The onward march of both computing and software technology is an obvious example.) With regard to the former, the laws and regulations governing for example the behavior of firms represented by equity assets change, as do market conditions and technologies used by such firms. Taken together, these factors make it plausible in our view that the relations between variables of interest this month and next relevant for forecasting are somewhat different now than they were last year, let alone five, ten, or twenty years ago, and are not plausibly identical, as stationarity would require.

2The type of non-stationarity we consider here is that induced by a distribution that changes over time. We also assume short memory, thus ruling out non-stationarity due to the presence of unit roots.


<!-- p:6 -->


If heterogeneity is accepted as an accurate description of economic time series, appropriate methods for model-based forecasting and forecast evaluation need to be applied. In general, it seems appropriate in a time-varying environment to consider estimators with finite memory, rather than basing forecasts on an expanding window of data. An example is the practice of specifying and estimating forecast models over a rolling window of the data, as a way to accommodate a data generating process that varies slowly over time (e.g., Fama and McBeth, 1973, Gonedes, 1973). The size of the estimation window may itself be time-varying, as was recently suggested by Pesaran and Timmermann (2002), who propose a recursive procedure which detects breaks in real time and then uses an appropriate subset of the data for estimation. Further, the estimators can usefully incorporate time weights which may assign decreasing importance to observations from the more distant past. The use of these methods in the production of forecasts has important implications for the evaluation procedure. The approach to out-of-sample testing in the unconditional predictive ability framework is to arbitrarily split the data into an estimation and an evaluation sample, and to obtain the asymptotic distribution of the test statistic under the assumption that both the insample and the out-of-sample sizes diverge to infinity. The choice of sample split is thus a finite sample artifice. In contrast, in our conditional framework the size of the estimation window and the possible time weighting are treated as choice variables of the forecast method, and as such they can be evaluated along with the forecast model and the estimation procedure as parts of the forecasting method under analysis.


<!-- p:7 -->


## 2.2 Estimation uncertainty

As emphasized by Clements and Hendry (1998, 1999) and Ericsson (2002), parameter estimation uncertainty is an important determinant of forecast performance. Our conditional tests directly account for the effects of estimation uncertainty on forecast performance by expressing the null hypothesis in terms of parameter estimates and by considering finite window estimation, which leads to asymptotically non-vanishing estimation uncertainty. In contrast, the unconditional framework does not take into account differing model complexities, unless explicitly incorporated into the accuracy measure (e.g., AIC or BIC); further, the presence of probability limits in the unconditional null hypothesis (1) means that different estimators that converge to the same limit will lead to the same conclusion. As a result, the unconditional tests are not able to detect superior forecasting performance which is due to reduced estimation uncertainty. For example, consider the case of comparing the accuracy of nested models in the unconditional framework. If the smaller model is correctly specified, the forecast errors from the two models calculated at the probability limits of the parameters are identical, and the null hypothesis (1) is automatically satisfied (this would hold for any loss function). In other words, one would conclude that the two models yield equally accurate forecasts, regardless of the number of excess parameters contained in the larger model. A test of this sort may thus lead to misleading conclusions if the goal is real-time forecast selection.

##### 2.3Out-of-sample versus in-sample testing

The literature on forecast evaluation has long argued that out-of-sample, rather than in-sample, testing is the "true" test of a forecast model. As Granger (1999, p. 65) observes, the potentially large number of parameters compared with the relative scarcity of macroeconomic data "leads to worries that a model presented for consideration is the result of considerable specification searching ..., data mining, or data snooping (in which data are used several times). Such a model might well appear to fit the data, in sample, rather well but will often not perform satisfactorily out-of-sample". This is related to the problem of overfitting: a good fit may result from explaining not only the stable relationships that are useful for forecasting but also possible accidental relationships that are specific to the sample. Out-of-sample evaluation of forecast performance, on the contrary, simulates a real-time forecast scenario where the quality of a forecasting method is directly measured against the actual data. The unreliability of in-sample testing is particularly evident if the data in the sample are generated by a time-varying process, whereas out-of-sample testing can incorporate this heterogeneity through recursive specification and estimation of the model. Our conditional testing framework is fully congruent with this motivation for out-of-sample testing: it is valid under heterogeneity of the data-generating process, and it is based on the forecasts and forecast errors actually observed, rather than viewing them as estimates of some population quantities. In the unconditional predictive ability framework, on the other hand, it is less clear why one should use out-of-sample rather than in-sample testing if the goal is to test hypotheses about population parameters under the assumption of stationarity. This point is well made by Inoue and Kilian (2002), who argue that if the goal of the testing procedure is to assess population predictability (corresponding to testing a null hypothesis of equal unconditional predictive ability of two nested models, e.g., as in (1)), the use of out-of-sample testing involves an unnecessary loss of information, whereas the in-sample test of the same hypothesis utilizes all the information available and thus leads to power gains in finite samples.


<!-- p:8 -->


## 2.4 Practical advantages of the conditional tests

In addition to the methodological considerations just articulated, there are also significant practical advantages to the approach advocated here. The main benefit of our approach is that it allows a unified treatment of nested and non-nested models, while the existing testing framework of West (1996) is only valid under non-nestedness. Unconditional tests of predictive ability for nested models have been proposed by Clark and McCracken (2001), among others, but they lack the general applicability of West (1996)'s results, as the test statistics have complicated limiting distributions that are context-specific. As discussed in section 3.2, the different treatment of nested and nonnested models in the unconditional framework is due to the fact that the asymptotic distribution of the test statistic relies on convergence of the parameter estimates to their probability limits, and this limiting behavior differs in the two cases. The fact that we don't rely on such convergence in the conditional approach instead makes it possible to consider nested and non-nested models in the same framework. A second advantage of the conditional tests is that they do not impose restrictions on the estimation procedure utilized to produce the forecasts, while the approach of West (1996) rules out, e.g., Bayesian, semi-parametric, and non-parametric estimation. Finally, our tests are simple to compute due to the imposition of a particular time dependence structure under the null hypothesis (e.g., martingale difference sequences for the one-step-ahead forecasts), which leads to a computationally simple expression for the asymptotic variance estimator.

### 3Theory

##### 3.1Description of the environment

Consider a stochastic process W ≡ {Wt : Ω — Rs+1, s ∈ N, t = 1, . . . , T} defined on a complete probability space (Ω, F, P). We partition the observed vector Wt as Wt ≡ (Yt, Xt)', where Yt : Ω → R is the variable of interest and Xt : Ω → Rs is a vector of predictor variables, and we define Ft = σ(W1, ..., Wt, Xt+1)' (as in, e.g., White, 1994, pg. 96). We adopt the standard convention of denoting random variables by upper case letters and realizations by lower case letters.


<!-- p:9 -->


We focus for simplicity on univariate forecasts. Consider a situation where two alternative models are used to forecast the variable of interest τ steps ahead, Yt+r. The forecasts are formulated at time t and are based on the information set Ft. Denote the two forecasts by fm,t ≡ f (wt, wt−1, ..., wt−m+1; βm,t) and Îm,t ≡ g(wt, wt−1, ..., wt−m+1; βm,t), where f and g are measurable functions. The subscripts indicate that the forecast formulated at time t is a measurable function of a sample of at most size m, consisting of the m most recent observations. Recall that we do not restrict attention to point forecasting. Our framework accommodates evaluation of point, interval, probability, and density forecasts. If the forecasts are based on parametric models, the parameter estimates from the two models are collected in the k × 1 vector βm,t. Otherwise, βm,t represents whatever semi-parametric or non-parametric estimators are used in constructing forecasts. The estimator βm,t can be further selected to minimize a weighted loss function over the estimation period, where smaller weights are typically assigned to observations from the more distant past. For example, for a linear model Yt = Xtβ + ut and a quadratic loss function, we can consider the a sequence of weights assigned to the observations in the estimation sample that can be selected by the user (for example one may assign exponentially decreasing weights to the observations further away from t).

We emphasize that the estimators may be parametric, semi-parametric or non-parametric. The only requirement here is that m (the maximum estimation window size) must be finite. All of the elements listed above - the model, the estimation procedure, the size of the estimation window and the estimation weight function - are treated as dimensions of choice by the user and are part of what we call the "forecasting method" under evaluation.

The evaluation is performed in a simulated out-of-sample fashion. Let T be the size of the sample available. Since the data indexed 1, ..., m are used for estimation of the first set of parameters, the first τ-step ahead forecasts are formulated at time m and compared to the realization ym+τ. The second set of forecasts is produced by moving the estimation window forward one step and estimating the parameters on data indexed 2, ..., m + 1. These forecasts are compared to the realization ym+1+r. The procedure is thus iterated and the last forecasts are generated at time T − τ, by estimating the parameters on data indexed T − τ − m + 1, .., T − τ, and they are compared to yT. This rolling window procedure yields a sequence of n ≡ T − τ − m + 1 forecasts and relative forecast errors.

The sequence of out-of-sample forecasts thus produced is evaluated by selecting a loss function Lt+τ(Yt+τ, fm,t), which depends on the forecasts and on the realizations of the variable. This loss function is either an economically meaningful criterion such as utility or profits (e.g., Leitch and Tanner 1991, West, Edison, and Cho 1993) or a statistical measure of accuracy. The following are some examples of statistical loss functions that have been considered in the forecast evaluation literature. Examples of appropriate loss functions for the evaluation of quantile, probability, and density forecasts are also discussed in Diebold and Lopez (1996), Lopez (2001), Giacomini and Komunjer (2002) and Giacomini (2002). For simplicity, let ft ≡ fm,t and consider τ = 1.


<!-- p:10 -->


1. Squared error loss function: Lt+1(Yt+1, ft) = (Yt+1 − ft)2.
2. Absolute error loss function: Lt+1(Yt+1, ft) = |Yt+1 − ft|.
3. Asymmetric linear cost function of order α (also known as the lin-lin or "tick function"):
4. Lt+1(Yt+1, ft) = (α − 1(Yt+1 − ft &lt; 0))(Yt+1 − ft), for α ∈ (0, 1).
4. Linex loss function: Lt+1(Yt+1, ft) = exp(a(Yt+1 − ft)) − a(Yt+1 − ft) − 1, a ∈ R.
5. Direction-of-change loss function: Lt+1(Yt+1, ft) = 1{sign(Yt+1 − Yt) ≠ sign(ft − Yt)}.
6. Predictive log-likelihood: Lt+1(Yt+1, ft) = log ft(Yt+1), where ft is in this case the density forecast of Yt+1

## 3.2 One-step conditional predictive ability test

For a given loss function, we write the null hypothesis of equal conditional predictive ability of forecasts f and g as

$$H _ { 0 } \ & \colon \ E [ L _ { t + \tau } ( Y _ { t + \tau } , \hat { f } _ { m , t } ) - L _ { t + \tau } ( Y _ { t + \tau } , \hat { g } _ { m , t } ) | \mathcal { F } _ { t } ] \\ & \equiv \ E [ \Delta L _ { m , t + \tau } | \mathcal { F } _ { t } ] = 0 \ \text {almost surely} \ t = 1 , 2 , \dots \, .$$

Due to certain computational issues, we consider separately the cases of one-step and multi-step forecast horizons.

### 3.2.1 Null hypothesis

When τ = 1, the null hypothesis claims that the out-of-sample sequence {∆Lm,t+1, Ft} is a martingale difference sequence (mds). In this case, the conditional moment restriction (3) is equivalent to stating that E[ht∆Lm,t+1] = 0, for all Ft— measurable functions ht. Let us restrict attention to a given subset of such functions, which we collectively denote by the q × 1 Ft- measurable vector ht and follow Stinchcombe and White (1998) by referring to this as the "test function". For a given choice of test function ht, we construct a test exploiting the consequence of the mds property that H0,h : E[ht∆Lm,t+1] = 0. The standard unconditional approach to predictive ability testing corresponds to testing the hypothesis H0,h with ht = 1 and with the parameter estimate βm,t replaced with its probability limit β*.


<!-- p:11 -->


For fixed m, standard asymptotic normality arguments suggest using a Wald-type test statistic of the form

$$T _ { n , m } ^ { h } = n ( n ^ { - 1 } \sum _ { t = m } ^ { T - 1 } h _ { t } \Delta L _ { m , t + 1 } ) ^ { \prime } \hat { \Omega } _ { n } ^ { - 1 } ( n ^ { - 1 } \sum _ { t = m } ^ { T - 1 } h _ { t } \Delta L _ { m , t + 1 } ) = n \bar { Z } _ { m , n } ^ { \prime } \hat { \Omega } _ { n } ^ { - 1 } \bar { Z } _ { m , n }$$

Z 1−1 1−u ≡   1+q ≡ I+'z I+7z 1−1 1−u ≡ 'z an− Zm,t+1Zm,t+1′ is a q × q matrix consistently estimating the variance of Zm,t+1.

A level α test can be conducted by rejecting the null hypothesis of equal conditional predictive ability whenever Th,n 2 distribution. The asymptotic justification for the test is provided in the following theorem, which characterizes the behavior of the test statistic (4) under the null hypothesis.

Theorem 1 (Conditional predictive accuracy test) For forecast horizon τ = 1, maximum estimation window size m &lt; ∞ and q × 1 test function sequence {ht} suppose:

(i) {Wt}, {ht} are mixing sequences with φ of size −r/(2r − 1), r ≥ 1 or α of size −r/(r − 1), r &gt; 1;

(ii) E|Zm,t+1,i|2(r+δ) &lt; ∆ &lt; ∞ for some δ &gt; 0, i = 1, ., and for all t; E[Zm,t+1Z'm,t+1] is uniformly positive definite. Then, under H0 in (3), Th, d a χq 2 as n → ∞. n,m

Comments: 1. Assumption (i) is mild, allowing the data to be characterized by considerable heterogeneity as well as dependence. This is in contrast with the existing literature, which typically assumes stationarity of the loss differences.

2. The asymptotic distribution is obtained for the number of out-of-sample observations going to infinity, whereas the estimation sample size m remains finite. This leads to asymptotically non-vanishing estimation uncertainty. In contrast, in the unconditional framework of West (1996), both the in-sample and the out-of-sample sizes grow, causing estimation uncertainty to vanish asymptotically. A result of letting both m and n grow is that the choice of how to split the available sample into in-sample and out-of-sample portions is arbitrary, while in our framework the choice of estimation window (up to some maximum m) is part of the forecasting method under evaluation. Also notice that the requirement of finite estimation window rules out the use of a recursive forecasting scheme, which utilizes an expanding estimation window.

3. Assumption (iii), imposing positive definiteness of the asymptotic variance of the test statistic, is related to a similar requirement made in the existing literature about predictive ability testing (e.g., West, 1996, McCracken, 2000), but it differs in a fundamental way. In that literature, the size of the estimation window is assumed to grow at the same rate or faster than the out-of-sample size, which means that the asymptotic variance of the test statistic is computed at the probability limits of the parameters. Because of the focus on this limiting behavior, the asymptotic variance matrix may be singular when the forecasts are based on nested models. In contrast, in the conditional framework the size of the estimation window remains finite as the prediction sample size n grows to infinity, which prevents the parameter estimates from reaching their probability limits. This makes our tests applicable to both nested and non-nested models.


<!-- p:12 -->


4. The test statistic for conditional predictive ability test is straightforward to compute. A further simplifying feature is the fact that the null hypothesis imposes a particular time dependence structure (in this case that of a martingale difference sequence), which implies that the asymptotic variance can be consistently estimated by the sample variance.

The following results provide computationally convenient ways to obtain the test statistic for the conditional predictive ability test using standard regression packages.

computed as nR2, where R2 is the uncentered squared multiple correlation coefficient for the artificial regression of the constant unity on the 1 × q vector (ht∆Lm,t+1)' for t = m, ..., T − 1.

Corollary 3 Let assumptions (i), (iii) and (iv) of Theorem 1 hold and further assume

(ii)′ E|∆Lm,t+1|2(r+δ1) &lt; ∆1 &lt; ∞ and E|hti|2(r+δ2) &lt; ∆2 &lt; ∞ for some δ1, δ2 &gt; 0, i = 1,..., q and for all t;

(v) E[(∆Lm,t+1)2|Ft] = σ2 for all t and some σ2 &gt; 0.

Then the conditional predictive ability test can be alternatively based on the test statistic nR2, where R2 is the uncentered squared multiple correlation coefficient for the artificial regression of ∆Lm,t+1 on the 1 × q vector ht, for t = m, ..., T − 1. A level α test can be conducted by rejecting is the (1 − α)−quantile of a χ2 distribution.

If the conditional homoskedasticity assumption (v) can be reasonably expected to hold in a given application, the true distribution of the regression-based test statistic in Corollary 3 may be better approximated by its asymptotic distribution than the statistic of Corollary 2, and it might thus deliver better inference.

### 3.2.2 Alternative hypothesis

We now analyze the behavior of the test statistic Th,n under a form of global alternative to the null hypothesis H0. Because we do not impose the requirement of identical distribution, we must exercise care in specifying the global alternative in this context. In fact, we will be able to obtain tests consistent against


<!-- p:13 -->


$$H _ { A , h } \colon E [ \bar { Z } ^ { \prime } _ { m , n } ] E [ \bar { Z } _ { m , n } ] \geq \delta > 0 \text { for all } n \text { sufficiently large} .$$

under the global alternative HA,h.

Theorem 4 Given Assumptions (i), (ii) and (iii) of Theorem 1, under HA,h in (5) for any constant c ∈ R, P[Tn,m &gt; c] → 1 as n → ∞.

Notice that H0 and HA,h are not necessarily exhaustive. For a given test function sequence {ht}, it may in fact happen that E[Ž′,n]E[Žm,n'] = 0 for some sequence {n′}, without {∆Lm,t+1} being an mds. The resulting test may thus have no power against alternatives for which ∆Lm,t+1 is uncorrelated with the chosen test function (and thus E[Żm,n]E[Żm,n'] = 0) but it is correlated with some element of the information set Ft that is not contained in ht. In other words, the properties of the test will depend on the chosen test function. The flexibility in the choice of test function is both a shortcoming and an advantage of our testing framework. On the one hand, for any given selection of ht the test may have no power against possibly important alternatives. On the other hand, one is left free to choose which test function is more relevant in any situation and thus focus power in that specific direction. Further, using methods developed recently in the statistics literature, one wo e dtk oe  e e   os i t o e  et of the null hypothesis using the notion of False Discovery Rate for multiple comparison testing procedures (Benjamini and Hochberg, 1995).

In practice, the test function is chosen by the researcher to embed elements of the information set Ft that are believed to have potential explanatory power for the future difference in predictive ability. Examples are, e.g., indicators of past relative performance or other variables that may help distinguish between the forecast performance of the two methods, such as business cycle indicators that may capture possible asymmetries in relative performance during booms and recessions. When choosing the number of elements for the test function ht, it is important to keep in mind that the properties of the test will be altered if one either includes too few or too many elements. If ht leaves out elements of the information set Ft that are correlated with ∆Lm,t+1, the test may have little or no power against the alternative for which ∆Lm,t+1 is not mds. As a consequence, the test would incorrectly "accept" a false null hypothesis. On the other hand, the inclusion of a number of elements that are either uncorrelated or weakly correlated with ∆Lm,t+1 will in some sense dilute the significance of the truly important elements and thus erode the power of the test. A possible way to confront this difficulty is to apply the approaches advocated by Bierens (1990) or Stinchcombe and White (1998), which deliver consistent tests.


<!-- p:14 -->


## 3.3 Multi-step conditional predictive ability test

For a forecast horizon τ &gt; 1, the null hypothesis (3) of equal conditional predictive ability of forecasts f and g implies in particular that for all Ft-measurable test functions ht the sequence {ht∆Lm,t+τ} is "finitely correlated", so that cov(ht∆Lm,t+r, ht−j∆Lt+τ−j(βm,t-j)) = 0 for all j ≥ τ. Similarly to the previous section, we are able to exploit this simplifying feature in the derivation of the test statistic. Using reasoning that mirrors the development of the test for the one-step horizon, we construct a test of

$$H _ { 0 , \tau } \colon E [ \Delta L _ { m , t + \tau } | \mathcal { F } _ { t } ] = 0$$

against the global alternative

$$H _ { A , h , \tau } \colon E [ \bar { Z } _ { m , n } ^ { \prime } ] E [ \bar { Z } _ { m , n } ] \geq \delta > 0 \text { for all } n \text { sufficiently large} ,$$

ht∆Lm,t+τ. For a fixed maximum estimation window length m, the test is based on the statistic

$$\ t i c \\ T _ { n , m , \tau } ^ { h } & = n ( n ^ { - 1 } \sum _ { t = m } ^ { T - \tau } h _ { t } \Delta L _ { m , t + \tau } ) ^ { \prime } \tilde { \Omega } _ { n } ^ { - 1 } ( n ^ { - 1 } \sum _ { t = m } ^ { T - \tau } h _ { t } \Delta L _ { m , t + \tau } ) = n \bar { Z } _ { m , n } ^ { \prime } \tilde { \Omega } _ { n } ^ { - 1 } \bar { Z } _ { m , n } \\ \tilde { \Gamma } & = \Gamma _ { n } ^ { T }$$

with wn,j a weight function such that wn,j → 1 as n → ∞ for each j = 1, ..., τ − 1 (see, e.g., Newey and West, 1987 and Andrews, 1991).

A level α test rejects the null hypothesis of equal conditional predictive ability whenever Th,r n,m,τ &gt; χ2,1-α, where χ2,1-α is the (1 − α)-quantile of a χ2 distribution. The following result is the equivalent of Theorems 1 and 4 for the multi-step forecast horizon case.

Theorem 5 (Multi-step conditional predictive accuracy test) For given forecast horizon τ &gt; 1, maximum estimation window size m &lt; ∞ and a q × 1 test function sequence {ht} suppose:

(i) {Wt}, {ht} are mixing sequences with φ of size −r/(2r − 2), r ≥ 2 or α of size −r/(r − 2), r &gt; 2;

(ii) E|Zm,t+1,i|r+δ &lt; ∆ &lt; ∞ for some δ &gt; 0, i = 1,.., q and forall t;t is uniformly positive deinite.

Then, (a) under H0,τ in (6), Th,r d as n → ∞ and (b) under HA,h,τ in (7), for any n,m,τ constant c ∈ R, P[Th,m,r &gt; c] → 1 as n → ∞.

## 3.4 A decision rule for forecast selection

If the null hypothesis of equal conditional predictive ability of forecast methods f and g is rejected, this raises the possibility that one might be able to select at time T a best forecasting method for time T + τ. Rejection of the null hypothesis is caused by the fact that the test functions {ht} have predictive power for the loss differences {∆Lm,t+τ} over the out-of-sample period. This suggests that the test function at time T, hT, can be used to predict which forecast method will yield lower loss at time T + τ, resulting, for example, in the following decision rule:


<!-- p:15 -->


- Let n denote the coefficient obtained by regressing ∆Lm,t+τ = Lt+τ(Yt+r, fm,t)−Lt+τ(Yt+τ, Îm,t) on ht over the out-of-sample period t = m, ..., T − τ. Then choose g if htn &gt; c and choose f if hpn &lt; c, where c is a user-specified threshold.

In general, the plot of the predicted loss differences over the out-of-sample period {htân}t-τ T−τ contains useful information for assessing the relative performance of f and g. For example, one taking the value 1 if A is true and 0 otherwise. In,c represents the proportion of times that the above decision rule would have chosen forecast method g over the out-of-sample period. In the empirical application in section 5, we utilize the indicator In,c with c = 0 to summarize the relative performance of the forecast methods under analysis.

### 4 Monte Carlo evidence

In this section, we investigate the size and power properties of our conditional predictive ability test in finite samples of the sizes typically available in macroeconomic forecasting applications. For simplicity, we restrict attention to a squared error loss function and to the one-step forecast horizon.

## 4.1 Size properties

In order to construct a series of data and forecasts that satisfy the null hypothesis, we exploit the following result.

Proposition 6 E[(Yt+1 − fm,t)2 − (Yt+1 − Îm,t)2|Ft] = 0 if and only if either fm,t = Îm,t a.s. or E[Yt+1|Ft] = (fm,t + Îm,t)/2.

We can thus generate data under the null hypothesis

$$H _ { 0 } \colon E [ ( Y _ { t + 1 } - \hat { f } _ { m , t } ) ^ { 2 } - ( Y _ { t + 1 } - \hat { g } _ { m , t } ) ^ { 2 } | \mathcal { F } _ { t } ] = E [ \Delta L _ { m , t + 1 } | \mathcal { F } _ { t } ] = 0$$

by first constructing forecasts {fm,t, Îm,t} and then letting Yt+1 = (fm,t + Îm,t)/2 + εt+1, where εt+1 ~ i.i.d. N(0, σ2). One of the important features of our testing framework is its ability to handle heterogeneous data. To create data that exhibits interesting behavior we consider an actual macroeconomic time series {Wt}, which corresponds to one of the measures of inflation that we ont   (       e e e t  one monthly U.S. Consumer Price Index measured over the period 1959:1-1998:12, for a total sample size T = 468. We construct the forecasts fm,t and Îm,t by a rolling window procedure; the first forecast is simply the unconditional mean of the estimation sample, while the second is the forecast implied by an AR(1) model for Wt:


<!-- p:16 -->


$$\hat { f } _ { m , t } \ & = \ ( W _ { t } + \dots + W _ { t - m + 1 } ) / m \\ \hat { g } _ { m , t } \ & = \ \hat { \alpha } _ { m , t } + \hat { \beta } _ { m , t } W _ { t } .$$

We consider a range of values for the size of the estimation sample m and for the variance of the disturbances σ2 : m = (36, 60, 120, 240, 360) and σ2 = (.1, 1, 3). For each pair (m, σ2) we generate 10, 000 Monte Carlo replications of the time series {Yt+1, fm,t, Îm,t} and compute the proportion of rejections of the null hypothesis (9) at the 10% nominal level. The test function is ht = (1, ∆Lm,t)'. The results are collected in Table 1.

#### [TABLE 1 HERE]

From the analysis of Table 1, the test appears to be reasonably well-sized, with a mild tendency to under-reject. The size properties of the test are seemingly unaffected by varying the length of the estimation window and the error variances.

## 4.2 Power properties

We investigate the power of the CPA test against serially correlated alternatives. In particular, we consider the following alternative hypothesis

$$H _ { a , \rho } \colon E [ \Delta L _ { m , t + 1 } | \mathcal { F } _ { t } ] = \rho \Delta L _ { m , t } ,$$

which occurs when E[Yt+1|Ft] = (fm,t + Îm,t)/2 − ρ∆Lm,t/(2(fm,t − Îm,t)). We consider a number of different values for the AR coefficient ρ, ranging from ρ = 0.05 to ρ = 0.5, at increments of 0.05. For a given ρ, we generate data under the alternative hypothesis (11) by first constructing the forecasts {fm,t, Îm,t} as in (10) and then letting Yt+1 = (fm,t + Îm,t)/2 − ρ∆Lm,t/(2(fm,t − Îm,t)) + εt+1, where εt+1~i.i.d. N(0, 1) and the initial value ∆Lm,m is drawn from a standard normal distribution. For each parameterization, we generate 10, 000 Monte Carlo replications of the time series {Yt+1, fm,t, Îm,t} and compute the proportion of rejections of the null hypothesis (9) at the 10% nominal level.3 Figure 1 plots the power curves for m = (60, 120, 240).

e ep   n   } ss t e   s 1oe sne  o n e the initial observation, which leaves us with a total sample size T = 368.


<!-- p:17 -->


#### [FIGURE 1 HERE]

e o  t   o t o p os    s  o able to detect the presence of moderately low serial correlation (i.e., an AR coefficient between 0.15 and 0.2). As expected, the power of the test increases as the size of the out-of-sample evaluation data set increases.

### 5 Application: comparing parameter-reduction methods in macroeconomic forecasting

A problem that often arises in macroeconomic forecasting is the selection of a manageable subset of predictors from a large number of potentially useful variables. In this situation, one key determinant of the resulting forecast performance is the trade-off between the information content of each series and the estimation uncertainty introduced. The goal of our application is to analyze and compare the forecast performance of several parameter-reduction schemes that have been considered in the literature to overcome this so-called "curse of dimensionality". We will consider three leading methods; a sequential model-selection approach based on a simplified general-to-specific modelling strategy (see the overview of Mizon, 1995), the "diffusion indexes" approach of Stock and Watson (2002) and the use of Bayesian shrinkage estimation (Litterman, 1986, Sims and Zha, 1998). We also compare each method to benchmark forecasts. The existing framework for comparison of predictive ability is not appropriate for addressing these issues, since it does not easily accommodate, for example, Bayesian estimation or the presence of estimated regressors. Further, some of the comparisons are between nested models, in which case the existing techniques are not readily applicable. In contrast, our conditional predictive ability approach is naturally well suited for comparison of nested models and for detecting differences in predictive ability arising from use of different modelling and estimation techniques.

We consider the "balanced panel" subset of the data set of Stock and Watson (2002) (henceforth SW), including 146 monthly economic time series measured over the period 1959:1-1998:12. We use the different parameter reduction methods to construct 1-, 6- and 12- month-ahead forecasts for eight U.S. macroeconomic variables: four measures of aggregate real activity and four price indexes. The first group includes the components of the Index of Coincident Economic Indicators maintained by the Conference Board: total industrial production; real personal income less transfers; real manufacturing and trade sales and number of employees on nonagricultural payrolls. The price indexes are: consumer price index; consumer price index less food; personal consumption expenditure implicit price deflator and producer price index.4 We refer the reader to SW for a complete description of the data.

4These variables coincide with the variables forecasted by SW, with the exception of the consumer price index


<!-- p:18 -->


## 5.1 Parameter-reduction methods

Following SW, our approach to multistep-ahead forecasting is to consider forecast models that project the τ-step ahead variable Yt+τ onto predictor variables measured at time t. Both the dependent variable and the predictors are transformations of the original data that render these variables I(0). In particular, the real variables are modeled as being I(1) in logarithms and the price indexes as I(2) in logarithms. If RAWt is the original datum at time t, this implies that Yt+τ is generated as

$$R e a l { \text { variables } } \ \colon \ Y _ { t + \tau } ^ { \tau } = ( 1 2 0 0 / \tau ) \log ( R A W _ { t + \tau } / R A W _ { t } )$$

For ease of notation, we denote the one-step ahead variable Yt1+1 as Yt+1.We consider the following forecasting methods.

### 5.1.1 Sequential model selection

This method considers the entire set of 145 predictors, together with lags of the dependent variable and performs a sequential selection search on each estimation sample that retains only variables that are statistically significant. The subset of significant variables is then used for forecasting. The initial model specification is

$$Y _ { t + \tau } ^ { \tau } = \alpha + \beta ^ { \prime } X _ { t } + \gamma ( L ) Y _ { t } + \varepsilon _ { t + \tau } .$$

where Xt indicates the vector containing the 145 predictors and γ(L) is an autoregressive polynomial of order 6. We overcome the problem of multicollinearity in the original Xt matrix by removing a    s   v v s vot v a  sd g of all the highly correlated variables. After this procedure, the new matrix Xt contains a total of 130 regressors. Our sequential modeling approach begins by estimating the full model and then applies a series of sequential tests until a more parsimonious restriction is found that conveys most of the information contained in the initial model.5 We apply a simplified version of the search algorithm described by Hoover and Perez (1999, p.175), which consists of reducing the number of regressors in the model by performing a sequence of stability tests, residual autocorrelation tests and t— and F— tests of significance of the regressor's coefficients. The simplification adopted here considers only one reduction path rather than multiple paths and performs only a subset of the sequential tests in Hoover and Perez (1999). As suggested by these authors, we use a significance level α = 0.01 for all the tests, which should encourage parsimony of the final model. A complete description of the particular algorithm that we utilize is contained in Appendix B.

less food which replaces the consumer price index less food and energy series considered by SW (not included in the data set available to the authors).

5See Hoover and Perez, (1999) and the ensuing discussion for relevant references, a thorough description of the methodology, and an account of the heated debate about the merits and shortcomings of the so-called LSE approach to econometric modeling.


<!-- p:19 -->


### 5.1.2 Diffusion indexes

This is a new method proposed by SW. The forecasts are constructed using a two-step procedure. First, the method of principal components is used to estimate the factors Ft from the predictors Xt. Second, the forecasting model is constructed as

$$Y _ { t + \tau } ^ { \tau } = \alpha + \beta ^ { \prime } \hat { F } _ { t } + \gamma ( L ) Y _ { t } + \varepsilon _ { t + \tau } ,$$

where both the number of factors k retained in t and the order p of γ(L) are selected by BIC, with 1 ≤ k ≤ 12 and 0 ≤ p ≤ 6.

### 5.1.3 Bayesian shrinkage estimation

We consider the full model (13) and apply Bayesian estimation of its coefficients using the Litterman (1986) prior. The Litterman prior, when applied to variables expressed in differences, shrinks all coefficients in (13) towards zero, except that for the intercept term a diffuse prior is used. Formally, the variance-covariance matrix V for the prior distribution of θ ≡ (α, β′, γ′)′ is diagonal, with α ∼ N(0, 108), βi ∼ N(0, (w · λ · ôy/ôxi)2), i = 1, ..., k and γj ∼ N (0, (λ/j))2), j = 1, .., p. There are two hyperparameters that must be selected a priori: λ and w. The parameter λ is the prior standard deviation of the first autoregressive coefficient (that is, the coefficient of Yt). The prior standard deviation of the subsequent lags of Yt is further divided by the lag length to reflect an increasing confidence in the prior mean for longer lags. The parameter w is a number between zero and one that reflects the belief that the predictors collected in Xt are less useful for forecasting than lagged values of the dependent variable. Further, the prior standard deviation of βi is multiplied by the ratio of the sample standard deviations of the dependent variable and of the ith regressor ôy/ôxi, to eliminate the effects of differences in scale. The Bayesian estimate of θ is then given by

$$\theta ^ { B } = ( X ^ { \prime } X + \hat { \sigma } ^ { 2 } V ^ { - 1 } ) ^ { - 1 } ( X ^ { \prime } Y ^ { \tau } ) ,$$

where X is the m×151 matrix (m is the size of the estimation sample) with rows (Xt, Yt, Yt–1, ..., Yt–5), Yτ is the m × 1 vector with rows Yt+τ and ô is the estimated standard error of the residuals in a univariate autoregression for Yt+τ. As suggested by Litterman (1986), we set w = 0.2 and λ = 0.2.6

6The results were generally robust to a number of different choices for w and λ.


<!-- p:20 -->


## 5.1.4Benchmarks

In addition to the three methods above, we consider two benchmarks. The first is a forecasting method based on an autoregressive (AR) model

$$Y _ { t + \tau } ^ { \tau } = \alpha + \gamma ( L ) Y _ { t } + \varepsilon _ { t + \tau } ,$$

os o         s  ( od s       od benchmark is based on a random walk hypothesis for the levels of the variable; this amounts to specifying the following forecast equation for the variable in differences:

$$Y _ { t + \tau } ^ { \tau } = \alpha + \varepsilon _ { t + \tau } .$$

## 5.2 Real-time forecasting experiment

The five methods described above are used to simulate real-time forecasting. The available sample has size T = 468, and we choose a maximum estimation window m = 150 + τ, which is the minimal length that allows us to estimate and test the full model in the sequential model selection approach. For comparability, we apply the same transformations to the original series as those documented in Appendix B of SW. The first estimation sample we consider ranges from 1960:1 through 1972:6 + τ (the first 12 data were used as initial observations). The data in this sample are first screened for outliers, which we replace with the unconditional mean of the corresponding variable. We then standardize the regressors, estimate the diffusion indexes and select the autoregressive lag lengths and number of diffusion indexes by BIC. Finally, we run the regressions (13), (14), (16), (17) and apply the Bayesian shrinkage method for t =1960:1,...,1972:6. We use the values of the regressors at time t =1972:6 + τ to generate a set of forecasts for Y1972:6+2r. We then move the estimation window forward one period and repeat all of the above steps (outlier detection, standardization, specification, estimation and so forth) on data from 1960:2 through 1972:7 + τ. This generates the set of forecasts for Y1972:7+2r. The final forecasts are produced at t =1998:12 – τ for the variable Y1998:12.

## 5.3 Results of the conditional predictive ability tests

We apply the conditional predictive ability test of Theorem 1 to evaluate the accuracy of the different forecast methods. We take the series of 1-, 6- and 12-month-ahead forecast errors e calculated above for each of the five models and conduct a number of pairwise tests using absolute error and squared error loss functions: L1(e) = |e| and L2(e) = e2. For τ = 1, 6 and 12, the null hypotheses of equal conditional predictive ability for the two loss functions are given by

$$H _ { 0 } ^ { 1 } & \ \colon \ E [ | Y _ { t + \tau } - \hat { f } _ { m , t } | - | Y _ { t + \tau } - \hat { g } _ { m , t } | \ | \mathcal { F } _ { t } ] \equiv E [ \Delta L _ { 1 t + \tau } | \mathcal { F } _ { t } ] = 0 \text { and } \\ H _ { 0 } ^ { 2 } & \ \colon \ E [ ( Y _ { t + \tau } - \hat { f } _ { m , t } ) ^ { 2 } - ( Y _ { t + \tau } - \hat { g } _ { m , t } ) ^ { 2 } | \mathcal { F } _ { t } ] \equiv E [ \Delta L _ { 2 t + \tau } | \mathcal { F } _ { t } ] = 0 .$$


<!-- p:21 -->


The hypothesis test H makes use of test function: ht = (1, ∆Lit)', i = 1, 2. As discussed in section 3.4, in case of rejection of the null hypothesis of equal conditional predictive ability, we consider which method would have been selected at each point in time by the decision rule described in that section. To illustrate, Figure 2 plots the sequence of predicted absolute error loss differences ood s  o o od od sd  od  o- del selection versus AR and Bayesian shrinkage versus AR.

#### [FIGURE 2 HERE]

The predicted loss for the sequential method is greater than the predicted loss for the AR for the vast majority of the sample dates, while the predicted loss for the Bayesian shrinkage is always smaller than that of the AR. Further, notice that the predicted loss differences for the pair sequential-AR are several orders of magnitude higher and more volatile than those for the pair Bayesian shrinkage-AR. Provided the test rejects the null hypothesis of equal conditional predictive ability, these considerations lead to the conclusion that Bayesian shrinkage would have been invariably a better method than the AR for forecasting one-month ahead industrial production over the years 1972-1998.

The results of the test for all pairwise comparisons, loss functions, and forecast horizons are contained in Tables 2-5. Tables 2 and 3 present the results for the real variables forecasts, whereas Tables 4 and 5 consider the price indexes forecasts. The entries in each table are the p-values of the tests of equal conditional predictive ability of the two methods. The number within parentheses below each entry is the indicator In,c discussed in section 3.4 (for c = 0) which represents the proportion of times the method in the column would have been preferred to the method in the row over the out-of-sample period using the decision rule described in that section. To facilitate interpretation of the tables, we use a plus sign to indicate rejection of the null hypothesis of equal conditional predictive ability of the two methods at the 10% level and to signal that the method in the column would have been chosen more often than the method in the row (as suggested by an entry In,c &gt; .5). Similarly, a minus sign denotes rejection of the null hypothesis at the 10% level and it indicates that the method in the column would have been chosen more often than the method in the row (i.e., In,c &lt; .5).

#### [TABLES 2 - 5 HERE]

A sharp result that emerges from Tables 2-5 is that the sequential model selection method is characterized by the worst performance across all forecast horizons, especially for the real variables. In the majority of cases, it is outperformed by every other method, including the naive random walk forecast. The likely explanation for this is the tendency of the method to select over-parameterized models (cases with 40 or more predictors in the final model were not uncommon), in spite of the use of a small confidence level for the sequential tests. Further, performing a new sequential search on each of the rolling estimation windows means that we typically select a different model at each iteration, in spite of the fact that consecutive windows only differ by two observations. This suggests that improvements on the performance of the sequential method may be obtained by updating the model less frequently than every month.


<!-- p:22 -->


A second general observation is that the information contained in the predictors seems to be less useful for forecasting price indexes than real variables. For the price indexes, there are only a few cases where the AR benchmark is outperformed (by the diffusion index method). In the majority of cases, the parameter-reduction methods, while outperforming the naive random walk forecasts, are indistinguishable from the AR benchmark. Further, the Bayesian shrinkage method is outperformed by the diffusion indexes and by the AR method mainly at the 6- and 12-month forecast horizons.

The Bayesian shrinkage and the diffusion indexes methods appear to fare better for forecasting real variables. Bayesian shrinkage, in particular, outperforms the AR in 11 of the 12 comparisons, while the diffusion indexes method outperforms the AR in 7 of the 12 comparisons. It is interesting to note that for the majority of variables and forecast horizons the AR forecasts are not distinguishable from the random walk forecasts. This suggests that the predictors do contain useful information for forecasting real variables beyond what can be captured by the variable's own lags. Bayesian shrinkage emerges in this case as the best method for reducing the estimation uncertainty of the system, while still conveying its information content.

### 6Conclusion

We propose a general framework for out-of-sample predictive ability testing which, as we argue, represents a more realistic setting for economic forecasting than the existing framework, exemplified by West (1996). We start from the premise that the forecaster not only cares about whether two competing forecasts do equally well on average, but also whether she can predict which forecast will do better tomorrow. We implement this different focus by conducting inference about conditional, rather than unconditional moments of forecasts and forecast errors. Recognizing that even a good model may produce bad forecasts due to estimation uncertainty or model instability, we make the object of evaluation the entire forecasting method (including the model, the estimation procedure and the size of the estimation window), whereas the existing literature concentrates solely on the model. In so doing, we are also able to handle more general data assumptions (heterogeneity rather than stationarity) and estimation methods, as well as providing a unified framework for comparing forecasts based on nested or non-nested models, which was not previously available.


<!-- p:23 -->


One useful application of the conditional predictive ability tests is in evaluating different methods for model selection and parameter estimation. We considered in particular the case of macroeconomic forecasting with a large number of predictors and compared the forecast performance of different parameter-reduction methods: a sequential model selection approach, the "diffusion indexes" approach of Stock and Watson (2002) and the use of Bayesian shrinkage estimation. Using the data set of Stock and Watson (2002), including monthly U.S. data on a large number of macroeconomic variables, we generated 1-, 6- and 12-month ahead forecasts of four measures of real activity and four price indexes using the different forecast methods. The conditional predictive ability tests led to the conclusion that the sequential model selection was the worst performing method, probably due to its tendency to select large models. A second general result was that the information contained in the predictors appeared to be less useful for forecasting price indexes than real variables. For the price indexes, the performance of the various methods was mostly indistinguishable from the one of a simple autoregression. For the real variables, instead, we found that the predictors did contain useful information beyond what is contained in the variable's own lags. For these variables Bayesian shrinkage seemed to be the best method for reducing the estimation uncertainty of the system. We emphasize that the results of the empirical application are specific to the situation where the number of parameters is very large relative to the sample size and thus one should be careful in generalizing our conclusions to other situations. The fact that shrinkage estimation methods work best in such an environment should come as no surprise. Likewise, it could be argued that the sequential model selection approach was originally conceived for the case where there are enough observations per parameter to make the results of the sequential tests credible. Viewed in this light, our experiments may be unduly hard on the sequential methodology.

Much work remains to be done. A refinement that we are currently exploring is to consider a richer set of decision rules for selecting the best forecasting method or for optimally combining the information embedded in each method once the null hypothesis of equal conditional predictive ability is rejected. A further natural generalization of the tests proposed in the paper is to consider multiple comparisons, for example by adapting the approach of White (2000) to our conditional framework. Finally, it may be possible to obtain asymptotic refinements of the tests presented here by using bootstrap resampling techniques, for example by establishing whether the results of Andrews (2002) can be extended to the case of heterogeneous data.


<!-- p:24 -->


### 7 Appendix A. Proofs

Proof of Theorem 1. Under the null hypothesis H0 in (3), {Zm,t+1, Ft} is an mds, and we can apply an mds central limit theorem (CLT) to show that

$$\hat { \Omega } _ { n } ^ { - 1 / 2 } \sqrt { n } \bar { Z } _ { m , n } \stackrel { d } { \rightarrow } N ( 0 , I )$$

as n → ∞, from which it follows that Th,n d as n → ∞. The mds CLT we use requires n,m conditions such that the sample variance Ôn is a consistent estimator of Ωn = var(√nŽm,n), i.e., such that Ωn − Ωn  0. Write Zm,t+1Zm,t+1 = f(ht, Wt+1, .., Wt−m), where f(·) is a measurable function. Since {Wt} and {ht} are mixing from (i), and f is a function of only a finite number of leads and lags of Wt and ht, it follows from Lemma 2.1 of White and Domowitz (1984) that {Zm,t+1Z′m,t+1} is also mixing of the same size as Wt. To apply a law of large numbers (LLN) to Zm,t+1Z'm,t+1, we further need to ensure that each of its elements has absolute r + δ mo++z+z  (   ze-     nk q t [E|Zm,t+1,i|t+δ]1/2[E|Z2m,t+1,j|r+]1/2 &lt; ∆1/2∆1/2 &lt; ∞, i, j =1, ..,q and for all . that Ωn−Ωn 0 then follows from McLeish (1975)'s LLN as in Corollary 3.48 of White (2001). Ωn is finite by (ii) and it is uniformly positive definite by (iii).

N(0, 1), which implies that Ω−1/2√nŽm,n d N(0, I). Consider

$$\lambda ^ { \prime } \Omega _ { n } ^ { - 1 / 2 } \sqrt { n } \bar { Z } _ { m , n } = n ^ { - 1 / 2 } \sum _ { t = m } ^ { T - 1 } \lambda ^ { \prime } \Omega _ { n } ^ { - 1 / 2 } Z _ { m , t + 1 }$$

and write λ'Ω−1/2 Zm,t+1 = Σi=1 λZm,t+1,i. The variable λZm,t+1,i is measurable with respect to Ft, and the linearity of conditional expectations implies that

$$E [ \lambda ^ { \prime } \Omega _ { n } ^ { - 1 / 2 } Z _ { m , t + 1 } | \mathcal { F } _ { t } ] = \sum _ { i = 1 } ^ { q } \tilde { \lambda } _ { i } E [ Z _ { m , t + 1 , i } | \mathcal { F } _ { t } ] = 0 ,$$

i = var(λ′Ω−1/2√nZm,n) = XΩ−1/2var(√n ̄m,n)Ω−1/2λ = 1 for all sufficiently large. We have that

$$n ^ { - 1 } \sum _ { t = m } ^ { T - 1 } \lambda ^ { \prime } \Omega _ { n } ^ { - 1 / 2 } Z _ { m , t + 1 } Z _ { m , t + 1 } ^ { \prime } \Omega _ { n } ^ { - 1 / 2 } \lambda - 1 = \lambda ^ { \prime } \Omega _ { n } ^ { - 1 / 2 } \hat { \Omega } _ { n } \Omega _ { n } ^ { - 1 / 2 } \lambda - \lambda ^ { \prime } \Omega _ { n } ^ { - 1 / 2 } \Omega _ { n } \Omega _ { n } ^ { - 1 / 2 } \lambda = g ( \hat { \Omega } _ { n } ) - g ( \Omega _ { n } ) \stackrel { p } { \rightarrow } 0 ,$$

since Ωn — Ωn  0 and by Proposition 2.30 of White (2001). Further, by Minkowski's inequality,

$$E | \lambda ^ { \prime } \Omega _ { n } ^ { - 1 / 2 } Z _ { m , t + 1 } | ^ { 2 + \delta } = E | \sum _ { i = 1 } ^ { q } \tilde { \lambda } _ { i } Z _ { m , t + 1 , i } | ^ { 2 + \delta } \leq [ \sum _ { i = 1 } ^ { q } \tilde { \lambda } _ { i } ( E | Z _ { m , t + 1 , i } | ^ { 2 + \delta } ) ^ { 1 / ( 2 + \delta ) } ] ^ { 2 + \delta } < \infty ,$$

the last inequality following from (ii). Hence, the sequence {λ'Ω−1/2 Zm,t+1, Ft} satisfies the condi- N(0, 1). By the Cramér-Wold device (e.g., Proposition 5.1 of White, 2001), Ω−1/2 √nZm,n N(0, I), from which (19) follows by consistency of Ôn for Ωn. ■


<!-- p:25 -->


Proof of Corollary 2. The (constant unadjusted) R2 for the regression of the constant unity on the variables Zm,t+1 ≡ (ht ∆Lm,t+1)′ can be written as R2 = t′Zm[ZmZm]−1Zmt/t′t, where t is an n × 1 vector of ones and Zm is the n × q matrix with rows Zm,t+1· Since Ôn = ZmZm/n, it thus ■

Proof of Corollary 3. The (constant unadjusted) R2 for the regression of ∆Lm,t+1 on ht can be written as R2 = ∆L'h[h'h]−1h′∆L/∆L'∆L, where ∆L is the n × 1 vector with elements ∆Lm,t+1 and h is the n × q matrix with rows ht. We thus have nR2 = nŽm,n(ônVn)−1Žm,n, where ôn = ∆L'∆L/n and Vn = h′h/n. We will show that ônVn − Ωn  0, which implies that the two statistics T,n and nR2 are asymptotically equivalent and thus the conditional predictive ability test can be alternatively based on the statistic nR2. By the law of iterated expectations

$$\Omega _ { n } = n ^ { - 1 } \sum _ { t = m } ^ { T - 1 } E [ h _ { t } ( \Delta L _ { m , t + 1 } ) ^ { 2 } h _ { t } ^ { \prime } ] & = n ^ { - 1 } \sum _ { t = m } ^ { T - 1 } E [ h _ { t } E [ ( \Delta L _ { m , t + 1 } ) ^ { 2 } | \mathcal { F } _ { t } ] ] h _ { t } ^ { \prime } ] = \sigma ^ { 2 } E [ h ^ { \prime } h / n ] , \\$$

where the last equality follows from assumption (v). Given assumptions (i) and (ii)', the sequences {htht} and {(∆Lm,t+1)2} satisfy a LLN and it thus follows that Vn − E[h′h/n]  0 and ôn − σ2 = ôn− E[ôn]  0, where the last equality is implied by (v). Hence, ônVn−Ωn = ônVn−σ2 E[h′h/n] 0, and the proof is complete. ■

Proof of Theorem 4. Given Assumption (i), it follows from Lemma 2.1 of White and Domowitz (1984) that {Zm,t+1} is mixing of the same size as Wt, since it is a function of only a finite number of leads and lags of Wt and ht. Further, each element of Zm,t+1 is bounded uniformly in t by (ii). McLeish (1975)'s LLN (as in Corollary 3.48 of White, 2001) then implies that Žm,n− E[Żm,n] D 0. By definition, under HA,h there exists ε &gt; 0 such that E[Ž′,n]E[Žm,n] &gt; 2ε for all n sufficiently large. We then have that

$$P [ \bar { Z } _ { m , n } ^ { \prime } \bar { Z } _ { m , n } > \varepsilon ] & \geq P [ \bar { Z } _ { m , n } ^ { \prime } \bar { Z } _ { m , n } - E [ \bar { Z } _ { m , n } ^ { \prime } ] E [ \bar { Z } _ { m , n } ] > - \varepsilon ] \geq P [ | \bar { Z } _ { m , n } ^ { \prime } \bar { Z } _ { m , n } - E [ \bar { Z } _ { m , n } ^ { \prime } ] E [ \bar { Z } _ { m , n } ] | < \varepsilon ] \to 1 . \\ \\ \\ P [ \bar { Z } _ { m , n } ^ { \prime } \bar { Z } _ { m , n } > \varepsilon ] & \geq P [ \bar { Z } _ { m , n } ^ { \prime } \bar { Z } _ { m , n } - E [ \bar { Z } _ { m , n } ^ { \prime } ] E [ \bar { Z } _ { m , n } ] > - \varepsilon ] \geq P [ | \bar { Z } _ { m , n } ^ { \prime } \bar { Z } _ { m , n } - E [ \bar { Z } _ { m , n } ^ { \prime } ] E [ \bar { Z } _ { m , n } ] | < \varepsilon ] \to 1 . \\$$

By arguments identical to those used in the proof of Theorem 1, {Zm,t+1Zm,t+1} is mixing of the (            (    s s LLN then implies that Ôn − Ωn  0, with Ωn uniformly positive definite by (iii). The conditions of Theorem 8.13 of White (1994) are then satisfied, and the theorem implies that for any constant c ∈ R, P[Th,m &gt; c] → 1 as n → ∞. ■

Proof of Theorem 5. (a) Under the null hypothesis H0 in (3), we show that

$$\tilde { \Omega } _ { n } ^ { - 1 / 2 } \sqrt { n } \bar { Z } _ { m , n } \stackrel { d } { \rightarrow } N ( 0 , I )$$

as n → ∞, from which (a) follows. First, we apply the Cramér-Wold device and show that for all λ ∈ R9, λ′λ = 1, λ'Ω−1/2√nŽm,n d N(0, 1), where Ωn = var(√nŽm,n), using the fact that E[Zm,t+τ|Ft] = 0. The asymptotic variance Ωn is finite by (ii) and it is uniformly positive definite by (i), Write 'Ω−1/2 √nZm,n = n−1/2 ∑t=-τ λ'Ω−1/2 Zm,t+r and consider the scalar sequence {λ'Ω−1/2 Zm,t+τ}. We verify that the sequence satisfies the conditions of the Wooldridge and White (1988) CLT for mixing processes. For each t, 'Ω−1/2 Zm,t+r = f(ht, Wt+τ, .., Wt−m), where f(·) is a measurable function. Since { Wt} and {ht} are mixing from (i), and f is a function of only a finite number of leads and lags of Wt and ht, it follows from Lemma 2.1 of White and Domowitz (1984) that {λ'Ω−1/2 Zm,t+τ} is also mixing of the same size as Wt. Further, σ2 = var(λ′Ω−1/2√nŽm,n) = X'Ω−1/2var(√nžm,n)Ω−1/2λ = 1 &gt; 0 for all n suffciently large. Finally, by Minkowski's inequality,


<!-- p:26 -->


$$E | \lambda ^ { \prime } \Omega _ { n } ^ { - 1 / 2 } Z _ { m , t + \tau } | ^ { 2 + \delta } = E | \sum _ { i = 1 } ^ { q } \tilde { \lambda } _ { i } Z _ { m , t + \tau i } | ^ { 2 + \delta } \leq [ \sum _ { i = 1 } ^ { q } \tilde { \lambda } _ { i } ( E | Z _ { m , t + \tau i } | ^ { 2 + \delta } ) ^ { 1 / ( 2 + \delta ) } ] ^ { 2 + \delta } < \infty ,$$

the last inequality following from (ii). Hence, the sequence {λ'Ω−1/2Zm,t+τ} satisfies the conditions of Corollary 3.1 of Wooldridge and White (1988), which implies that λ'Ω−1/2√nžm,n d N(0, 1). By the Cramér-Wold device (e.g., Proposition 5.1 of White, 2001), we then conclude that Ω−1/2√nŽm,n d N(0, I). It remains to show that Ωn − Ωn  0, from which (21) follows. We have that

$$\text {that} & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

For j = 0, ..., τ − 1, {Zm,t+τZm,t+τ−j} is mixing of the same size as Wt and each of its elements is bounded uniformly in t by (ii). Applying McLeish (1975)'s LLN (e.g., Corollary 3.48 of White, 2001) E(Zm,t+τZm,t+τ−j)]  0 for each j = 0, ..,τ − 1 (with wn,0 ≡ 1), which in turn implies that ñn − Ωn  0 and the proof is complete.

(b) Given Assumption (i), it follows from Lemma 2.1 of White and Domowitz (1984) that nd y    n e s  s e se s s    s ad} and lags of Wt and ht. Further, each element of Zm,t+τ is bounded uniformly in t by (ii). McLeish (1975)'s LLN (as in Corollary 3.48 of White, 2001) then implies that Žm,n − E[Żm,n]  0. By definition, under HA,h,τ there exists ε &gt; 0 such that E[Žm,n]E[Żm,n] &gt; 2ε for all n sufficiently large. We then have that

$$P [ \bar { Z } _ { m , n } ^ { \prime } \bar { Z } _ { m , n } > \varepsilon ] \geq P [ \bar { Z } _ { m , n } ^ { \prime } \bar { Z } _ { m , n } - E [ \bar { Z } _ { m , n } ^ { \prime } ] E [ \bar { Z } _ { m , n } ] > - \varepsilon ] \geq P [ | \bar { Z } _ { m , n } ^ { \prime } \bar { Z } _ { m , n } - E [ \bar { Z } _ { m , n } ^ { \prime } ] E [ \bar { Z } _ { m , n } ] | < \varepsilon ] \to 1 .$$


<!-- p:27 -->


By arguments identical to those used in part (a) - which for this particular result did not necessitate the time dependence structure imposed under the null hypothesis - it follows that ñn — Ωn  0, with Ωn uniformly positive definite by (iii). Theorem 8.13 of White (1994) then implies that for

Proof of Proposition 6. We have E[(Yt+1 − fm,t)2 − (Yt+1 − Îm,t)2|Ft] = E[−2Yt+1(fm,t − Îm,t) + fm,t − gm,t|Ft] = −2(fm,t − Îm,t)E[Yt+1|Ft] + fm,t − g2,t = (fm,t − Îm,t)(−2E[Yt+1|Ft] + fm,t + Îm,t) which is zero (a.s.) if and only if either one of the two factors is zero (a.s.).

### 8 Appendix B. Sequential model selection algorithm

The following is our modification of the search algorithm described by Hoover and Perez (1999, pp.175-176). All the tests are conducted for a significance level α = 0.01 and use heteroskedasticity and autocorrelation consistent standard errors and covariance matrices (e.g., Newey and West, 1987, Andrews, 1991).

1. Estimate the full model on the available sample and run the following tests:

a. Autocorrelation of residuals up to sixth order (LM test; see Breusch and Pagan, 1980).

b. Stability test (Chow predictive test leaving out the last 10 observations in the sample; see Fisher, 1970).

If the full model fails any one of the tests (i.e., autocorrelation and/or structural breaks are detected), do not use this test in the following steps.

2. Eliminate the variable of the general specification that has the lowest t-statistic and reestimate the model, which becomes the current model.
3. On each current model, perform the two tests in step 1 together with c. F-test of the hypothesis that the coefficients of the variables in the full model that are not

included in the current model are jointly insignificant. If the hypothesis cannot be rejected, the current model can be considered a valid restriction of the full model (in this case we say that the model passes the test).

4. If the current model passes all three tests, eliminate the variable with the next lowest t-statistic and perform the tests on the new current model. If this model fails any one of the tests, restore the last variable eliminated and remove the variable with the next lowest t—statistic. Continue in this fashion until the current model passes all the tests and either all the variables are significant or the elimination of any residual insignificant variable would lead to failing one of the tests.


<!-- p:28 -->


5. Estimate the final model from step 4.

5.1. If all remaining variables are significant terminate the algorithm.

5.2. If there are remaining insignificant variables, remove all of them and perform the three tests on the restricted model.

a. If the restricted model passes all the tests and all the variables are significant, terminate the algorithm.

b. If the restricted model fails any of the tests, restore the block of eliminated insignificant variables and terminate the algorithm.

c. If the restricted model passes all the tests but there are some remaining insignificant variables, go back to step 5.2.


<!-- p:29 -->
