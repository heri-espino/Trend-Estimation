---
id: "34_Boosting_HP_Filter"
source_pdf: "../pdf/34_Boosting_HP_Filter.pdf"
source_filename: "34_Boosting_HP_Filter.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/34_Boosting_HP_Filter.references.md"
---

<!-- p:1 -->

BOOSTING: WHY YOU CAN USE THE HP FILTER

By

Peter C. B. Phillips and Zhentao Shi

December 2019

COWLES FOUNDATION DISCUSSION PAPER NO. 2212

LUX ET VERTAT

COWLES FOUNDATION FOR RESEARCH IN ECONOMICS YALE UNIVERSITY Box 208281 New Haven, Connecticut 06520-8281

http://cowles.yale.edu/


<!-- p:2 -->


## Boosting: Why you Can Use the HP Filter

Peter C.B. Phillips Yale University, University of Auckland

University of Southampton and Singapore Management University

Zhentao Shi

The Chinese University of Hong Kong

December 4, 2019

###### Abstract

The Hodrick-Prescott (HP) filter is one of the most widely used econometric methods in applied macroeconomic research. The technique is nonparametric and seeks to decompose a time series into a trend and a cyclical component unaided by economic theory or prior trend specification. Like all nonparametric methods, the HP filter depends critically on a tuning parameter that controls the degree of smoothing. Yet in contrast to modern nonparametric methods and applied work with these procedures, empirical practice with the HP filter almost universally relies on standard settings for the tuning parameter that have been suggested largely by experimentation with macroeconomic data and heuristic reasoning about the form of economic cycles and trends. As recent research (Phillips and Jin, 2015) has shown, standard settings may not be adequate in removing trends, particularly stochastic trends, in economic data. This paper proposes an easy-to-implement practical procedure of iterating the HP smoother that is intended to make the filter a smarter smoothing device for trend estimation and trend elimination. We call this iterated HP technique the boosted HP filter in view of its connection to L2-boosting in machine learning. The paper develops limit theory to show that the boosted HP (bHP) filter asymptotically recovers trend mechanisms that involve unit root processes, deterministic polynomial drifts, and polynomial drifts with structural breaks, thereby covering the most common trends that appear in macroeconomic data and current modeling methodology. In doing so, the boosted filter provides a new mechanism for consistently estimating multiple structural breaks even without knowledge of the number of such breaks. A stopping criterion is used to automate the iterative HP algorithm, making it a data-determined method that is ready for modern data-rich environments in economic research. The methodology is illustrated using three real data examples that highlight the differences between simple HP filtering, the data-determined boosted filter, and an alternative autoregressive approach. These examples show that the bHP filter is helpful in analyzing a large collection of heterogeneous macroeconomic time series that manifest various degrees of persistence, trend behavior, and volatility.

Key words: Boosting, Cycles, Empirical macroeconomics, Hodrick-Prescott filter, Machine learning, Nonstationary time series, Trends, Unit root processes JEL codes: C22, C55, E20

This paper is an updated and revised version of an earlier working paper entitled 'Boosting the Hodrick Prescott Filter' (Phillips and Shi, 2019). Phillips acknowledges research support from the Kelly Foundation at the University of Auckland, the NSF under Ġrant No. SES 18-50860, and an LKC Fellowship at Singapore Management University. Shi acknowledges support from the Hong Kong Research Grants Council Early Career Scheme No. 24614817. We thank Yang Chen for excellent research assistance and Zheng Song for helpful comments. Peter C. B. Phillips: peter.phillips@yale.edu. Zhentao Shi: zhentao.shi@cuhk. edu.hk.


<!-- p:3 -->


The principle adopted here in the construction of a trend for a time series consists in minimizing a linear combination of two sums of squares, of which one refers to the second differences of the trend values, the other to the deviations of the observations from the trend values ... this procedure seems a particularly natural one when dealing with economic time series. The resulting family of trends may be described as quasi-linear trends. Leser (1961)

Our statistical approach does not utilize standard time series analysis. The maintained hypothesis based on growth theory considerations is that the growth component of aggregate economic times series varies smoothly over time. Hodrick and Prescott (1997)

##### 1Introduction

Two prominent features of macroeconomic data are trending long-run growth in aggregate economic activity and a cyclical component that represents fluctuations in this activity over shorter periods known as business cycles. Modern macroeconomic theory of the business cycle, evident in the vast literature on RBC and DSGE modeling, seeks to explain the cyclical movement and co-movement of macroeconomic variables about long-run trends. Both aspects of economic activity are important in economic analysis and policy making. Trends are an intrinsic element in determining long term economic prospects and the overall health of an economy. Cyclical behavior is especially important to policy makers, who are interested in understanding past contractions with a view to foreseeing the onset of future recessions and minimizing their impact on employment and business activity.

To analyze business cycles in observed data it is necessary to isolate the cyclical component from the trend. Rigorous study requires clarity concerning the trend mechanism and various definitions have been used in past work to distinguish slow moving and cyclical mechanisms in the data.1 Decomposition into trend and cycle is commonly achieved by regression or filtering. The latter is primarily motivated by the prior view that a trend is distinguished as a smoothly varying component in relation to the observed data, a concept reflected in the header quotation from Hodrick and Prescott (1997) (hereafter HP), leading to the so-called HP filter, to the use of spectral methods (Hannan, 1963; Christiano and Fitzgerald, 2003), and to the use of orthonormal polynomial regression (Phillips, 1998, 2005, 2014). The HP filter belongs to the statistical approach that was introduced by Whittaker (1922) and Whittaker and Robinson (1924), who provided a probabilistic framework of penalized maximum likelihood estimation to deliver a quantitative measure of trend (or graduation in their terminology). The explicit form of the smoothness measure penalty involving squared second differences in HP (1997) was used in earlier work by Leser (1961), who emphasized its relevance to trend determination with economic data on the grounds of its quasi-linear trend-producing properties, as indicated in the primary header quotation.

The HP method is now widely used in applied macroeconomic work by economists in central banks, international economic agencies, industry, and government. Its use in academic work is less extensive, partly because it has been subject over many years to considerable criticism and analyses that have revealed a myriad of its limitations for empirical studies in economics, an early example being Cogley and Nason (1995). For recent discussion of the merits and demerits of the filter, see Phillips and Jin (2015) (PJ, henceforth) and Hamilton (2018) and the many references cited therein.

1Readers are referred to Phillips (1998, 2003, 2005, 2010a), Phillips and Shimotsu (2004), White and Granger (2011), and Müller and Watson (2018) for general discussion and limitations of trend formulations commonly used in empirical work.


<!-- p:4 -->


Given time series data (xt : t = 1, . . . , n), the HP method decomposes the series into two additive components — a trend component (ft), and a residual or cyclical component (ct), estimated as

$$\left ( \widehat { f } _ { t } ^ { H P } \right ) = \arg \min _ { ( f _ { t } ) } \left \{ \sum _ { t = 1 } ^ { n } \left ( x _ { t } - f _ { t } \right ) ^ { 2 } + \lambda \sum _ { t = 2 } ^ { n } \left ( \Delta ^ { 2 } f _ { t } \right ) ^ { 2 } \right \} , \text { and } \quad \left ( \widehat { c } _ { t } ^ { H P } \right ) = \left ( x _ { t } - \widehat { f } _ { t } ^ { H P } \right ) \quad ( 1 )$$

where ∆ft = ft − ft−1, ∆2 ft = ∆ft − ∆ft−1 = ft−2ft−1 + ft−2, and λ ≥ 0 is a tuning parameter that controls the extent of the penalty. As is apparent from this criterion, the method is nonparametric and the choice of λ inevitably plays a major role in determining the shapes of the fitted trend and cycle functions. If λ is selected too large, the fitted trend becomes nearly linear, as implied by Leser's (1961) characterization, and a linear trend is indeed the solution as λ → ∞. In consequence, if the trend is nonlinear and λ is too large, the HP fitted trend produces a residual trend that contaminates the cyclical component. If λ is selected too small, the fitted trend becomes highly flexible, so that it closely tracks the data and thereby embodies elements of short-term fluctuations. In the absence of an underlying model that defines and enables direct quantification of trend and cycle, some degree of cycle distortion with the HP filter is inevitable. Of course, precisely the same criticism applies to other smoothing techniques, as well as regression methods of trend extraction when the trend model is misspecified, as is nearly always the case in practical work.

In the application of modern nonparametric methods, serious efforts are normally made to choose tuning parameters based on some well-defined optimization criterion with data-determined versions of these criteria that can be implemented in empirical work. This approach is greatly facilitated by the use of an underlying model representing the generating mechanism. By contrast, empirical practice with the HP filter almost universally relies on standard settings for the tuning parameter that have been suggested largely by experimentation with macroeconomic data and heuristic reasoning about the form of economic cycles and trends. For quarterly data the standard choice is λ = 1600, as recommended by HP (1997) based on their experimentation with US data. This value has served as a gold standard in converting the tuning parameter to other sampling frequencies such as annual or monthly data (Ravn and Uhlig, 2002). Importantly, these HP filter smoothing parameter settings are normally employed irrespective of the sample size of the data in contrast to standard nonparametric methods.

HP filtering retains an agnostic position with regard to the exact functional form of the trend and cycle. This approach has the advantage of generality, but the central weakness is that its prt o o n ood r o e  ww   ord to the relevant choice of the tuning parameter. Recent research by PJ (2015) has shown that the performance of the filter as a potentially consistent estimator of trends of certain types can be assessed directly in relation to the choice of the tuning parameter, just as in standard nonparametric analysis as the sample size n → ∞. That work revealed the constraints that are needed on λ in order to achieve consistent trend estimation for polynomial trends and stochastic process trends. The paper also analyzed the effect of the filter on trends with structural breaks. In doing so, PJ showed how the standard HP filter settings may not be adequate in removing trends — particularly stochastic trends — in economic data, a conclusion that reverses earlier thinking (King and Rebelo, 1993) to the effect that the HP filter removes up to four unit roots in the original data. PJ further showed that the common choice of the tuning parameter λ = 1600 for quarterly data is typically tc      s ssod os o o o o tnie ti   e te ot  is os d e  s ss s linger in the fitted cycles of much applied research, a conclusion supported by the recent examples exhibited in Hamilton (2018) and the earlier work by Cogley and Nason (1995).


<!-- p:5 -->


The present paper proposes an easy-to-implement modification that is designed to make the HP filter more effective in trend fitting and trend elimination, and is formulated with data-determined smoothing choices to aid practical application. The idea is simple. Since the cyclical component may often retain trend elements, we feed the data into the filter again to clean the leftover elements. The notion of refitting the residual in statistical applications goes back to Tukey (1977) under the name twicing, where procedures were employed twice to assist in data-cleaning exercises. The notion of twicing can be continued into "n-ing", as discussed in Buja, Hastie, and Tibshirani (1989). This approach motivates the present proposal of repeated application of the HP filter. Since the solution of the HP filter can be explicitly expressed as a linear operation, which will be made clear in Section 2, repeated HP fitting is closely related to the L2-boosting (Bühlmann and Yu, 2003) procedure which is now commonly used in machine learning.

The existing statistical theory on boosting is developed mostly for environments with independent identically distributed (iid) data. We are unaware of any earlier work concerned with the use of L2-boosting on stochastically trending data or nonstationary time series. A primary contribution of the present paper is to apply and analyze the idea of repeated fitting algorithms in machine learning to trend detection and nonstationary time series environments. In particular, we establish asymptotic theory to justify the use of the boosted version of the HP filter, extending earlier work by PJ on the asymptotics of the HP filter. We find that if the number of iterations slowly diverges with the sample size, the boosted HP filter (bHP filter, hereafter) can recover the underlying trend irrespective of whether the time series contains a stochastic process trend, a deterministic polynomial drift, or a polynomial drift with a structural break. An interesting implication of the asymptotic theory in the latter case is that the bHP filter effectively delivers a consistent estimator of the break point. This result extends to the case of multiple structural breaks, so the boosted filter provides a new device for consistently estimating multiple break points, delivered automatically without additional methods of detection.

Use of machine learning methods in econometrics has grown quickly in recent years with a particular focus on applied microeconomics where large cross sectional and wide panel datasets are available. The low-frequency nature of most macroeconomic time series, on the other hand, means that the volume of today's macroeconomic databases is much smaller by comparison and is, of course, completely dwarfed by those generated from Internet communication.2 Nonetheless, the phenomena that macroeconomists study are no less complex than those that confront scientists ns a  d s   m     a empirical analysis using country-level macro indicators, macroeconomists handle data collected from r  oo s ess on  os os n s es ernn r such cases, where there are many possible determining factors and diverse time series trajectories, automated econometric procedures (e.g., Phillips (2005)) can be of tremendous appeal in practical work, as has been argued recently by many authors since the development of high dimensional regression methods such as Lasso (Tibshirani, 1996).

-m  at s s (   s -  s      s o. MD is the Monthly Databases for Macroeconomic Research (https://research.stlouisfed.org/econ/mccracken/ fred-databases/). See McCracken and Ng (2016) for details.


<!-- p:6 -->


This line of thinking partly motivates the present econometric implementation of machine learning methods in which we propose two data-driven stopping rules to terminate iterations of the bHP filter. One rule ceases the iteration according to the outcome of a unit root test, and is appropriate when stationary time series is considered a prerequisite for further investigation, such as business cycle analysis. The second rule relies on a new version of the Bayesian information criterion (BIC) that is developed for the present bHP filter framework to take into account sample fit and effective degrees of freedom after each iteration. The latter approach accords with the now common practice of using BIC-type information criteria as stopping rules in econometric work.

We conduct three real data applications of the HP and bHP filters to study the impact of our iterative fitting algorithm. The first application revisits Okun's law, which posits an empirical association of comovement between real GDP and unemployment, in an international cross country setting. Ball, Leigh, and Loungani (2017) extend the scope of Okun (1962)'s original focus on the United States to 20 OECD countries, applying the standard HP filter to each time series to obtain deviations from long run levels. Accordingly, when the standard filter fails to remove the time trend, the resulting Okun law regression can suffer spurious regression effects. The bHP filter helps to mitigate the effects of potential contamination from long run influences.

A second example conducts a cross country comparison of business cycles. In an extensive application of HP methods to remove trend, Aguiar and Gopinath (2007) suggest that cyclical components are more persistent and volatile in emerging economies than in developed countries. In revisiting this application using the bHP filter, we find that the time series collected from the emerging economies are much shorter than those from the developed ones, and so the use of the standard λ = 1600 tuning parameter uniformly across all countries tends to over-penalize the shorter series. Repeated fitting helps to regularize the unbalanced panel and robustify the finding by Aguiar and Gopinath (2007) of the empirical distinction in cyclical behavior between emerging and developed economies.

The third application examines US industrial production over the last century from 1919 to 2018. Like many other macroeconomic time series this series displays strong trend characteristics with some major fluctuations over subperiods that include two world wars and the great depression during the early part of the period, and the financial crisis and great recession over the latter period. As such, the series presents challenges in trend determination that include the complex issue of whether such subperiods are better interpreted as part of the trend or part of the evolving cyclical processes of modern industrialized economies. In this application, we provide a detailed comparison of the HP and bHP filters with the alternative autoregressive modeling approach recently advocated by Hamilton (2018).

We close this introduction with a brief discussion of related literature on filtering and boosting. First, there are now many competing methods of data filtering to remove trend such as the band pass filter methods of Baxter and King (1999), Christiano and Fitzgerald (2003), and Corbae and Ouliaris (2006). Most of these share many common characteristics with the HP filter. Nonetheless, the HP filter remains the most popular3 in practical work and serves as a benchmark for other agnostic methods of trend extraction. In addition, there has been renewed recent interest in the theoretical properties of the HP filter, useful algebraic representations, and computational algorithms. Phillips

3As of April, 2019, the article by Hodrick and Prescott (1997) had 8,540 listed citations and the article by Baxter and King (1999) 3,559 citations in Google Scholar.


<!-- p:7 -->


(2010b) and PJ (2015) provide exact matrix and operator representations and new asymptotics. Cornea-Madeira (2017) gives an explicit algebraic formula for the HP filter in finite samples. De Jong and Sakarya (2016) and Sakarya and de Jong (2017) provide further finite sample results, including another representation of the HP filter as a symmetric weighted average plus some adjustments. Hamilton (2018) provides a cautionary note concerning the limitations of the HP filter approach, reinforcing earlier warnings and suggesting the alternative of scalar autoregression.

Second, machine learning methods have been employed to generate new statistical procedures specifically tailored for economic applications in recent work by Belloni, Chen, Chernozhukov, and Hansen (2012), Belloni, Chernozhukov, and Hansen (2014), Chernozhukov, Hansen, and Spindler (2015), Fan, Liao, and Yao (2015), Hirano and Wright (2017) and Caner and Kock (2018), to name a few. Boosting is one of the most successful machine learning methods. Originally proposed for classification problems (Freund and Schapire, 1995), boosting has given rise to many useful variants (e.g. Hastie, Tibshirani, and Friedman (2009)). Bühlmann and Yu (2003) extended the idea of refitting to linear regression with the L2 norm for the residuals, opening up a wide range of potential applications. In high dimensional regression, component-wise boosting is also related to forward stage selection and the greedy algorithm (Bühlmann, 2006). The idea of refitting (specifically twicing) was introduced by Tukey (1977) and appeared in econometrics in Newey, Hsieh, and Robins (2004). In high-dimensional regression, Bai and Ng (2009) employed boosting in macroeconomic forecasting. Shi (2016) used boosting to select relevant moments in structural models defined by many moment conditions. Ng (2014) and Luo and Spindler (2017) applied boosting to recession forecasting and other economic examples.

The rest of the paper is organized as follows. Section 2 introduces the iterative algorithm for boosting the HP filter and develops asymptotic theory that characterizes the behavior of the boosted filter, giving conditions for consistent estimation of stochastic process and deterministic polynomial trends with possible structural breaks. Stopping rules are provided to automate the procedure for practical work. Simulations are conducted in Section 3 to reveal the effect of boosting along with the stopping rules. Section 4 reports three empirical applications of the bHP methodology. Section 5 concludes with a summary of arguments in support of the bHP filter as a trend determination o enl   nt re n e o  ed e e t ree  n the HP filter by Hamilton (2018).

### 2 The Boosted HP Filter

## 2.1 The Boosting Algorithm

The optimization problem (1) leading to the HP filter and related criteria for general filters of this type have closed-form algebraic solutions in convenient matrix form.4 In the HP case, if D' is the rectangular (n − 2) × n matrix with second differencing vector d = (1 −2 1) along the leading tri-diagonals and In is the n × n identity matrix, the explicit form of the trend solution is

$$\widehat { f } ^ { H P } = S x ,$$

4See Phillips (2010b), Phillips and Jin (2015), De Jong and Sakarya (2016), and Cornea-Madeira (2017) for recent work on exact matrix forms and other exact representations of the HP and related filters.


<!-- p:8 -->


where S = (In + λDD')−1 is a deterministic operator and x = (x, ., xn)' is the sample data. The smoothed component fHP is interpreted as the estimated trend and

$$\widehat { c } ^ { \text {HP} } = x - \widehat { f } ^ { \text {HP} } = ( I _ { n } - S ) \, x$$

as the estimated cyclical or stationary component.

The behavior and asymptotic properties of the estimated trend fHP crucially depend on the choice of the tuning parameter and the underlying generating mechanism of xt. For macroeconomic data the mechanism may reasonably be expected to involve a stochastic trend, possibly accompanied by some deterministic drift component that may be well modeled by a low order polynomial or a similar deterministic function subject to breaks. In the prototypical case of a unit root process, xt satisfies under quite general conditions the functional law (Phillips and Solo, 1992)

$$\frac { x _ { [ n r ] } } { \sqrt { n } } \sim & \ B ( r )$$

where [·] is the floor function, B is Brownian motion with variance ω2 given by the long run variance of ∆xt, and ~ signifies weak convergence, here on the Skorohod space D[0, 1].

The problem of consistent HP filter estimation of the trend then amounts to whether as n → ∞ fHP we have [nr] B(r), in which case the filter asymptotically captures the underlying stochastic √n process trend in xt. PJ show that this reproduction of the asymptotic form of the trend holds only under special restrictions on the smoothing parameter λ that ensure it does not diverge too quickly. is inconsistent. In [nr] fHP such cases, J[nr] 1  fHP (r) where fHP (r) is a smooth stochastic process different from B(r), which √n implies that the cyclical component HP = x — fHP inevitably inherits elements of the stochastic trend even in the limit. Similar issues arise in the case of time series with stochastic trends coupled with deterministic drift or deterministic drift with breaks (see PJ for details). In all these cases, the HP filter fails to recover the underlying trend in xt asymptotically. The limit theory therefore confirms much informal commentary in the literature concerning the shortcomings of the HP filter as a suitable trend determination mechanism for economic data.

We propose an easy remedy to establish consistent estimation of stochastic process and deterministic trends in the data. If the cyclical component cHP still exhibits trending behavior after HP filtering, we continue to apply the HP filter to cHP to remove the leftover trend residual. After a second fitting, the cyclical component can be written as

$$\widehat { c } ^ { ( 2 ) } = ( I _ { n } - S ) \, \widehat { c } ^ { \text {HP} } = ( I _ { n } - S ) ^ { 2 } \, x ,$$

where the superscript "(2)" indicates that the HP filter is fitted twice. The corresponding trend component becomes

$$\widehat { f } ^ { ( 2 ) } = x - \widehat { c } ^ { ( 2 ) } = \left ( I _ { n } - ( I _ { n } - S ) ^ { 2 } \right ) x .$$

If c(2) continues to exhibit trend behavior, the filtering process may be continued for a third or further time. After m repeated applications of the filter, the cyclical and trend component are


<!-- p:9 -->


$$\begin{array} { r l } { \widehat { c } ^ { ( m ) } } & { = } & { ( I _ { n } - S ) \, \widehat { c } ^ { ( m - 1 ) } = ( I _ { n } - S ) ^ { m } \, x } \\ { \widehat { f } ^ { ( m ) } } & { = } & { x - \widehat { c } ^ { ( m ) } = B _ { m } x , } \end{array}$$

where Bm = In − (In − S)m . We call this iterated process the boosted HP filter, in view of its similarity to L2-boosting in terms of numerical implementation.

Boosting is so-called because it has the capacity to enhance the flexibility of what is called in the machine learning literature a weak base learner as the starting point. In machine learning language, this process is known as a mechanism for achieving the 'strength of weak learnability' (Schapire, 1990). The intuition behind the asymptotic validity of the bHP filter is the observation that the HP filter, with a conventional choice of the tuning parameter λ, serves as a weak base learner.5 In consequence, the crude HP filter is too weak by itself to fully capture the underlying trend, particularly when the trend involves a stochastic process. Initiating from the conventional HP filter, we iterate the procedure to strengthen this filter as a weak base learner. As discussed in the following section, under certain conditions on the number of iterations m the boosted version is able to restore the trend as n → ∞, even if the base learner itself is too weak for consistency.

## 2.2 Asymptotic Theory

The criterion underlying the HP filter is agnostic about the data generation process. The key element in controlling the capacity of the filter to capture underlying trend behavior of various forms lies in the choice of the smoothing parameter λ and controls that are implemented on its asymptotic behavior in relation to sample size. The latter is particularly important and is presently almost universally neglected in empirical work. As we now discuss, suitable controls may be implemented on the boosted HP filter to ensure that underlying trend behavior is captured consistently.

It will be convenient to start with the case where the time series xt has a stochastic trend and satifies the functional law (4). In this case, Theorem 3 of PJ (2015) shows that if λ = μn4 for some fixed constant μ &gt; 0 independent of the sample size n, then

$$\frac { \widehat { f } _ { \lfloor n r \rfloor } ^ { \text {HP} } } { \sqrt { n } } \sim & \, f ^ { \text {HP} } \left ( r \right ) = \sum _ { k = 1 } ^ { \infty } \frac { \lambda _ { k } ^ { 2 } } { \mu + \lambda _ { k } ^ { 2 } } \sqrt { \lambda _ { k } } \varphi _ { k } \left ( r \right ) \xi _ { k } ,$$

where ξk ∼ iid N (0, ω2), φk (r) = √2 sin (r/√λk) and λk = [(k − 1) π]−2. This asymptotic form of the HP filtered data is deduced by analyzing the asymptotic impact of the HP operator on the Karhunen-Loève (KL) representation6 of the Brownian motion limit function given in (4), viz,

$$B ( r ) = \sum _ { k = 1 } ^ { \infty } \sqrt { \lambda _ { k } } \varphi _ { k } \left ( r \right ) \xi _ { k }$$

5In quarterly economic time series for example, accumulating evidence has shown that the setting λ = 1600 is often too large given the length of the time series typically encountered in empirical macroeconomics (Schlicht, 2005; Phillips and Jin, 2015; Hamilton, 2018).

6Readers may refer to Phillips (1998) for further details of KL representations and their relevance in the asymptotic analysis of nonstationary time series.


<!-- p:10 -->


The representations (5) and (6) are orthonormal series in the trigonometric polynomials φk (r) as well as the random coefficients ξk and the series converge almost surely and uniformly for r ∈ [0, 1]. But whereas Brownian motion is everywhere non-differentiable, the asymptotic form of the HP filter given in (5) is differentiable to the fourth order and converges almost surely and uniformly for r ∈ [0, 1]. As discussed in PJ, for typical time series of quarterly macroeconomic data, the limit form in (5) produces a smoothed version of the time series that closely matches output from a HP filter with λ = 1600 when the constant μ is set so that μ = 1600/n4 to ensure comparability of the tuning parameter with the standard setting that is used in practical work with quarterly data. Thus, (5) may be regarded as an asymptotic approximation to the trend output from HP filtering typical quarterly macroeconomic time series. The upshot is that when the HP filter is conducted under standard settings for λ, it fails to deliver a consistent estimate of an underlying stochastic trend in the data.

The limit formula on the right-hand side of (5) is particularly convenient as a starting point in understanding the effects of repeated HP fitting. The following theorem confirms that, in contrast to (5), the bHP filter ftm) f(m) captures the stochastic trend in the data when the number of iterations m in the boosted filter is allowed to diverge and the primary tuning parameter setting is λ = μn4.

Theorem 1. Suppose that xt satisfies the functional limit law (4) and the HP filter is iterated m times according to the boosted HP algorithm with λ = μn4 and μ fixed. If m → ∞ as n → ∞ then

$$\frac { \widehat { f } _ { \lfloor n r \rfloor } ^ { ( m ) } } { \sqrt { n } } \sim B ( r ) .$$

##### Remarks

- (i) This result shows that repeated application of the HP filter to the cyclical component residual from each pass of the filter is successful in asymptotically eliminating remnants of the stochastic trend from the estimated cyclical component of the time series. The bHP filter algorithm thereby assures consistent estimation of a stochastic process trend like Brownian motion. Importantly and distinct from the asymptotic result in PJ, consistent estimation of the stochastic process trend applies for the boosted filter even with the primary filter setting retained as λ = μn4.
- (ii) The heuristic explanation of (7) is as follows. Both series representations (5) and (6) converge almost surely and uniformly in r and therefore admit further linear operations associated with the boosted filter. Successive operations of the filter then proceed to remove the remaining stochastic trend components from the cycle, leading to consistent estimation of the stochastic trend. The proof of the theorem makes use of the operator Gλ = 1 which λL−2(1−L)4+1' is the asymptotic form (apart from end corrections) of the HP operator on the time series. As shown in PJ, the operator Gλ may be interpreted as a pseudo-integral operator, which facilitates the analysis of its asymptotic properties. The corresponding operator that delivers the cyclical component is 1 − Gλ and m successive operations in the boosted HP filter then lead to the operator (1 − Gλ)m. The asymptotic result is obtained by using the approximation (1 − Gλ) φk ( ≈ μ ) , which holds with a well-controlled approximation error.


<!-- p:11 -->


Repeated fitting leads to

$$( 1 - G _ { \lambda } ) ^ { m } \, \varphi _ { k } \left ( \frac { t } { n } \right ) \approx \left ( \frac { \mu } { \mu + \lambda _ { k } ^ { 2 } } \right ) ^ { m } \varphi _ { k } \left ( \frac { t } { n } \right ) \to 0 , \quad \text {as } m \to \infty .$$

Then, [1 − (1 − Gλ)] φk [nr] ≈ φk (r), as m, n → ∞. Pursuing this line of argument, n the proof of Theorem 1 establishes (7) rigorously by verifying that the approximation errors accumulated throughout the series summation are asymptotically negligible.

- (iii) When it is viewed as a special case of linear penalized spline smoothing, the HP filter places knots on the n − 2 observed time points xt, t = 2, . . . , n − 1 omitting the first and last observations (Paige and Trindade, 2010, Eq.(2.2)). The nonstationary nature of the knots in trending time series cases requires new technical tools in analyzing the asymptotic behavior of the boosting procedure. In this respect, the present results go beyond the scope of existing work, such as Bühlmann and Yu (2003)'s Section 3.2 which is concerned with boosting nonparametric mean models based on penalized spline smoothing with fixed or iid knots.

We next proceed to consider the effect of boosting the HP filter when the time series involves a deterministic trend. PJ have shown that the HP filter itself asymptotically preserves a polynomial trend up to the 3rd order. In consequence, the boosted HP filter also asymptotically maintains the presence of a polynomial trend up to the 3rd order. The following result further shows that the boosted HP filter consistently estimates any higher order polynomial trends that may accompany a stochastic process trend in the data, as well as the limiting stochastic trend itself, thereby capturing the full limiting trend process.

Theorem 2. Let xt = αn + βn,1t + . . · + βn,JtJ + xt where xt follows the functional limit law (4) and the coefficients in the polynomial αn/ √n → α, nj−1/2βn,j → βj for j = 1, . , J. Suppose the HP filter is iterated m times with λ = μn4 and μ fxed. If m, n → ∞, then

$$\frac { x _ { \lfloor n r \rfloor } } { \sqrt { n } } , \frac { \widehat { f } _ { \lfloor n r \rfloor } ^ { ( m ) } } { \sqrt { n } } & \sim \alpha + \beta _ { 1 } r + \dots + \beta _ { J } r ^ { J } + B \left ( r \right ) .$$

The polynomial component of xt in Theorem 2 is specified with sample size dependent coefficients, assuring that the standardized time series x[nr↓ satisfies the functional law (8), giving a limit √n stochastic process trend with polynomial drift of degree J. The result extends Theorem 4 of PJ by showing that boosting the HP filter with primary tuning parameter setting λ = μn4 asymptotically preserves a polynomial trend of any finite order as m → ∞. The implication is that when using the conventional λ = 1600 setting of the smoothing parameter for quarterly macroeconomic time series, the boosting algorithm ensures that the filter delivers a consistent estimator of the limiting form of the trend in a time series that has a stochastic process trend with a finite order polynomial drift.

A closely related result might be expected in the case of boosting the HP filter applied to a time series that has a stochastic process limiting trend function accompanied by a deterministic drift that is piecewise continuous with a finite number of break points. Theorem 5 of PJ showed by using the Fourier series representation of the drift function that the asymptotic effect of the HP filter is to smooth a piecewise continuous limit drift function into a smooth curve in which the breaks in the deterministic trend are represented by smooth transitions over adjacent neighborhoods. In view of Theorem 2, we might expect that boosting the HP filter would enable the filter under some conditions to capture the continuous parts of a polynomial trend as m, n → ∞. The following result provides asymptotic theory and conditions for the case of a time series with a stochastic trend and time polynomial drift with a single break point.


<!-- p:12 -->


To fix ideas, suppose gn (t) is a trend break polynomial with a single break point at τ0 = [nr0] with r0 ∈ (0, 1) that takes the form

$$g _ { n } \left ( t \right ) = \left \{ \begin{array} { l l } { \alpha _ { n } ^ { 0 } + \beta _ { n , 1 } ^ { 0 } t + \dots + \beta _ { n , J } ^ { 0 } t ^ { J } } & { t < \tau _ { 0 } = \lfloor n r _ { 0 } \rfloor } \\ { \alpha _ { n } ^ { 1 } + \beta _ { n , 1 } ^ { 1 } t + \dots + \beta _ { n , J } ^ { 1 } t ^ { J } } & { t \geq \tau _ { 0 } = \lfloor n r _ { 0 } \rfloor } \end{array} ,$$

with → α and {nj− 2 βn,j → βj : : j = 1, .., J } for δ = 0, 1. The limiting form of this polynomial break function is

$$n ^ { - 1 / 2 } g _ { n } \left ( \lfloor n r \rfloor \right ) \rightarrow g \left ( r \right ) = \left \{ \begin{array} { l l } { \alpha ^ { 0 } + \beta _ { 1 } ^ { 0 } r + \dots + \beta _ { J } ^ { 0 } r ^ { J } } & { r < r _ { 0 } } \\ { \alpha ^ { 1 } + \beta _ { 1 } ^ { 1 } r + \dots + \beta _ { J } ^ { 1 } r ^ { J } } & { r \geq r _ { 0 } } \end{array} ,$$

giving a piecewise continuous polynomial function with a single break at r = r0 ∈ (0, 1). If the generating mechanism of the observed data xt is xt = gn (t) + x0, where x0 is a stochastic trend that satisfies the functional limit law (4), then the normalized process n−1/2xt=[nr」has the following limit

$$n ^ { - 1 / 2 } x _ { t = \lfloor n r \rfloor } \sim g \left ( r \right ) + B \left ( r \right ) = \colon B _ { g } ( r )$$

as n → ∞. PJ (2015) explored the asymptotic form of the HP filter applied to such a time series xt, showing that when λ = μn4 the limiting form of the normalized HP filtered time series is a smooth function BHP(r) := gHP (r) + BHP (r) where gHP (r) is a continuous function approximation to g (r) that smooths over the break point of g (r) at r0 and BHP(r) is a smooth functional approximation to the Brownian motion B (r) of the same form as (5).

The following result shows that the boosted HP filter can consistently estimate the limit function Bg(r) for r ≠ ro., thereby capturing the polynomial drift function at all points except the break point, as well as the stochastic trend process.

Theorem 3. Let xt = gn (t) + x0 where xt satisfies n−1/2xt=|nr] ∼ g (r) + B (r) . Suppose the HP filter is iterated m times with λ = μn4 and μ ixed. If 1 十 m → 0 as n → ∞, then m n

$$\frac { \widehat { f } _ { \lfloor n r \rfloor } ^ { ( m ) } } { \sqrt { n } } \sim g ^ { \flat \text {HP} } \left ( r \right ) + B \left ( r \right ) \colon = \left \{ \begin{array} { l l } { g \left ( r \right ) + B \left ( r \right ) , } & { r \neq r _ { 0 } } \\ { \frac { 1 } { 2 } \left \{ g \left ( r _ { 0 } ^ { - } \right ) + g \left ( r _ { 0 } ^ { + } \right ) \right \} + B \left ( r _ { 0 } \right ) , } & { r = r _ { 0 } } \end{array} .$$

for each r ∈ [0, 1] and r0 ∈ (0, 1).

Compared with Theorem 2, this result imposes the additional condition that m/n → 0 as m, n → ∞. The extra condition is useful in the proof in deriving the limit behavior of the boosted filter around the break point r = r0. When r ≈ r0, the HP filter and boosted filter both smooth the time series trajectory of xt using observations on either side of the break point. Like the Fourier series approximation of a piecewise continuous function (and the Gibbs phenomenon), the HP filter and boosted filter do not converge to the true value, Bg(ro), of the limit function at the break point r = r0. PJ show that when λ = μn4 the HP filter converges to a smoothed version of the limit process Bg(r) for all r ∈ (0, 1). The above result shows that for the same tuning parameter setting of λ the boosted filter provides a substantial enhancement by consistently estimating Bg(r) for all r ≠ r0 in the limit as m, n → ∞ when m/n → 0. An implication of this result is that the bHP filter provides a consistent estimate of the break point ro in an arbitrary polynomial trend. By consistently estimating Bg(r) = g(r) + B(r) for all r ≠ r0 the boosted filter effectively reveals the break point r0 by virtue of the fact that the deterministic limit function g(r) has a finite right limit to the value g(r+) = g(ro) on the right and has a finite left limit to a value g(ro−) ≠ g(ro). The the limit of the bHP filter is the simple average of the left and right limits, viz., ↓ {9 (r−) + g (r+) }, thereby mimicking the behavior of the Fourier series representation of the function g(r) at the break point r0.


<!-- p:13 -->


Theorem 3 is proved for a polynomial of arbitrary finite order with a single break point. The proof of this theorem reveals that under the same conditions the result may be extended to any piecewise continuous polynomial function with a finite number of break points. In effect, the extended result shows that the boosted HP filter can consistently estimate a stochastic trend together with a breaking polynomial drift that has multiple structural breaks. Consistency applies for all points in the domain with the exception of the break points themselves. But in the same manner as Theorem 3 the fact that consistency holds almost everywhere with exceptions at the break points ensures that the boosted HP filter delivers consistent estimates of the break points themselves. These results hold in the presence of discrete break points. The present asymptotic development does not provide for local break point departures with breaks that decay with the sample size. The analysis of the asymptotic properties of the bHP filter in such cases is left as a topic of future research.

## 2.3 Numerical Illustrations with the Boosted HP Filter

It is not uncommon for modern machine learning methods — such as boosting, random forest and artificial neural network — to have multiple tuning parameters. The bHP filter has been formulated with two tuning parameters, one primary (λ) and one secondary (m). The near-universal choice for the primary smoothing parameter is λ = 1600 for quarterly data and Theorems 1 and 2 show that with this choice, assuming that λ = μn4 = 1600, the boosted filter can successfully consistently estimate and extract both stochastic and deterministic trends. This setting therefore means that there is good reason to continue using the standard value λ = 1600 with quarterly data and to focus attention on a suitable choice for the secondary parameter m. This approach matches Bühlmann and Yu (2003)'s recommendation of using a relatively large primary parameter for smoothing and designating the boosting parameter as the sole tuning parameter. This regularization method of terminating the algorithm after several iterations is called early stopping in statistical learning theory.

As the results of the last section show, the asymptotic effect of increasing m is similar to reducing the value of λ in the simple HP filter, as both approaches can lead to consistent estimation of stochastic trends. In particular, PJ's results imply that consistent trend estimation is restored if smaller values of λ are used so that λ/n4 shrinks to 0 fast enough as n → ∞. But implementing such a scheme would require a grid system (λ(1), λ(2) , . . . , λ(m)) to be specified and the performance of the HP filter over these choices to be monitored and evaluated by some other criterion. Such a regularization scheme itself is an iterative procedure that is conceptually no more appealing than early stopping and is difficult to implement absent suitable criteria for the selection process and supporting asymptotic theory.


<!-- p:14 -->


Macroeconomic time series are now available internationally in great abundance and computation is therefore a relevant consideration in all such big data applications when machine learning methods are employed (Aruoba, Diebold, Kose, and Terrones, 2010; Aruoba and Diebold, 2010). A key computational advantage in the use of a bHP filter and early stopping procedure is its lower computational complexity and higher numerical stability in comparison to choosing λ values on a grid system for the simple HP filter (Raskutti, Wainwright, and Yu, 2014; Blanchard, Hoffmann, and Reiß, 2017). Early stopping computes only once the inverse matrix operator S = S(λ) = (In + λDD')−1 for a given λ. Using the same matrix S(λ) stored in computer memory, successive iterations in the boosted HP filter involve simple matrix-scalar multiplication (In − S(λ))e(m−1), which amounts to 2n2 — n linear operations. In contrast, searching for a suitable λ on a grid system involves inverting an n × n matrix to obtain S (λ) or carrying out QR decomposition7 for every value of λ on the grid, compared to which the computational cost of matrix-scalar multiplication is negligible.

We discuss various stopping rules for determining the number m of boosting iterations in Section 2.4 below. Before doing so, we conduct a numerical exercise to observe the effects of repeated fitting in three prototypical cases involving a stochastic trend, and a stochastic trend with a drift and a mean break. Let ut2 and gn(t) be a deterministic sequence. Define

$$\begin{array} { c c c } z _ { t } & = & z _ { t - 1 } + u _ { t } ^ { ( z ) } , \\ e _ { t } & = & 0 . 5 e _ { t - 1 } + u _ { t } ^ { ( e ) } + u _ { t - 1 } ^ { ( e ) } , \\ \tilde { x } _ { t } & = & g _ { n } ( t ) + z _ { t } , \\ x _ { t } & = & \tilde { x } _ { t } + e _ { t } , \end{array}$$

where (zt) is a random walk, (et) is an ARMA(1,1) stationary process, (xt) is a trend consisting of a non-random drift component gn(t) and the stochastic trend component zt, and (xt) is the observed time series, which allows for stationary deviations or measurement error in observations of xt.

Given the same realized stochastic trend (measured with error) x0 = zt + et of length n = 100, we generate the observations xt = gn(t) +xf shown in the panels of Figure 1 by varying the deterministic component as follows to accommodate two prototypical trends8: a 4th order polynomial trend gn(t) = 10−3 . (n − t)2 + 3 · 10−7 . t4 in the upper panel, and a mean shift gn(t) = 20 · 1{t ≥ 0.5n + 1} in the lower panel. The observations xt are represented by the black scattered dots, the trend xt by the solid grey line, and the deterministic trend gn(t) by the dashed grey line. The HP filter with λ = 1600 is used to extract the trend and is shown as the red curve (m = 1) in the figure. The other curves are the fitted trends obtained by iterating the HP filter m times (the m values are given in the figure legend) according to the boosted filter.

7Instead of directly computing the matrix inverse it is common to use a QR decomposition of the (2n − 2) × n o     os   ns s   eon  o   ,   tim number of linear operations is

8The third prototypical trend is a simple stochastic trend with no deterministic component and results for this case are given in Table 1 below.


<!-- p:15 -->


Figure 1: In each panel, observations xt are shown in black dots, the underlying trend process xt by the solid grey lines, the deterministic trend gn(t) by the dashed grey lines, and the fitted trend lines obtained by the HP filter (red line) and bHP filters (colored shades of orange progressing to shades of blue). A sequential decomposition of the upper panel of the figure into the component graphics is shown in Figure B1, highlighting the trend capture performance of the HP and bHP filters in comparison to that of an AR(4) autoregression.

30

品

0

000

Stoc.+Deter. Trends

20

0

10

品

品0

0

30

oo

0

Stoc. Trend+Mean Shift

品

20

10

0

品0

0

25

50

75

100

Time

Iterations m=  1  2  4816 32  64  128


<!-- p:16 -->


The upper panel reveals that the repeated fitting tracks the random wandering behavior of the random walk uniformly better than the HP filter. The bHP filter gives a superior fit to the true trend (represented by the solid grey line in Figure 1) with a smaller L2 distance to the grey line than the HP filter (m = 1) for all values of 2 ≤ m ≤ 128. The curves are insensitive to the number of iterations once m becomes large. This phenomenon is known as boosting's resistance to overfitting'.9 It is corroborated analytically in the proof of Theorem 1 where it is shown that as m becomes large for given n the boosted filter stabilizes and approximates a finite number of terms in the orthonormal series representation of the limiting trend process. This finite term orthonormal representation is a smooth approximation to the true limit process, explaining the smooth form of the boosted HP filter. Further analysis of this example by decomposition of the component graphics is given in Figure B1, which includes a comparison of the trend capture performance of the bHP filter with that of an AR(4) autoregression

In the lower panel, it is evident from the plots that boosting the filter goes a long way towards enhancing performance in the region of the structural break by eliminating a substantial amount of the transition smoothing in the HP filter around the break point. For large m ≈ n, the boosted filter trajectory is strongly suggestive of a structural break around observation t = 50 with a mid-point estimate of the value at the break point, corroborating the implications of Theorem 3.

## 2.4 Stopping Criterion

The residual component after trend extraction by smoothing methods such as the HP filter has long been a building block for applied macroeconomists in studying business cycles and the interactions between macroeconomic aggregates and indicators. By definition, the cyclical component is a time series that exhibits no long run trending behavior, so that its spectrum has no unit root or deterministic trend asymptote at the zero frequency. In practice this criterion can be implemented by the elimination of all low frequency elements, an approach that band-pass filter methods use directly in filtering the data (Baxter and King, 1999; Christiano and Fitzgerald, 2003; Corbae and Ouliaris, 2006).

A natural and somewhat analogous approach in the present context is to refilter the data until there is no evidence of a non-stationary zero frequency asymptote. This can be conveniently achieved c(m). Standard procedures for unit by monitoring the outcome of unit root tests on the residual series root testing such as the augmented Dickey-Fuller (ADF) or Phillips-Perron (Phillips and Perron, 1988) tests can be used and the boosting iterations can be continued until the test statistic is smaller than a specified p-value, such as 0.05 or 0.01. Such test-based stopping criteria are easy to implement and are well-tailored to existing applied macroeconomic practice, echoing Kozbur (2017)'s test-based stopping criterion for forward selection, and Diebold and Kilian (2000)'s testbased forecasting approach. Relatedly, Hodrick and Prescott (1997) used unit root tests to assist in determining an appropriate setting for the primary smoothing parameter λ. In our simulations and empirical examples, we will use the ADF test conducted with significance level 0.05 to illustrate implementation of this approach. The boosted HP filter that results from this ADF test-based selection will be denoted bHP-ADF.

9Further evidence of resistance to overfitting is given later by Figure 3 in the simulation study.


<!-- p:17 -->


Information criteria offer an alternative approach to a stopping criterion. These criteria are routinely employed in statistics to achieve bias-variance trade-offs and to prevent overfitting in modeling and forecasting. We therefore consider the following Bayesian-type information criterion (BIC) for the selection of the stopping time for m

$$I C \left ( m \right ) = \frac { \widehat { c } ^ { \left ( m \right ) } \widehat { c } ^ { \left ( m \right ) } } { \widehat { c } ^ { \left H P \right } \widehat { c } ^ { \left H P } } + \log \left ( n \right ) \frac { \text {tr} \left ( B _ { m } \right ) } { \text {tr} \left ( I _ { n } - S \right ) } .$$

Similar to BIC, this criterion penalizes fit by adding log(n) times a term that quantifies the relative weight of the m additional iterations that are involved in the boosted filter. The first term of (12) measures the residual sum of squares fit of the boosted HP filter, c(m)/ê(m), relative to the HP filter itself, cHP/cHP. The penalty term involves the usual log(n) scale factor multiplied by a ratio that measures the effective degrees of freedom of the boosted filter after m iterations to the effective degrees of freedom of the HP filter. To interpret this ratio, it is useful to think of the linear operator (In − S) that produces the residual cyclical component cHP = (In − S) x of the HP filter as analogous to a linear regression projector or hat matrix, so that tr (In - S) is analogous to the Peg-   (o -  −-  =  eo o  ee res     eo operator corresponding to the boosted filter and the quantity tr(Bm) may therefore be interpreted in a similar way as the effective degrees of freedom after successive fitting by the boosted HP. This interpretation corresponds to usage in the machine learning literature (Tutz and Binder, 2006). It is convenient from now on to refer to the criterion IC (m) simply as BIC and to the boosted HP filter that results from this selection rule as bHP-BIC. .

It is shown in the Appendix that tr(Bm) can be asymptotically approximated by the following simple analytic expression as n → ∞

$$\text {tr} ( B _ { m } ) = \text {tr} ( I _ { n } - ( I _ { n } - S ( \lambda ) ) ^ { m } ) = n - \sum _ { k = 1 } ^ { n - 2 } \frac { ( \lambda \delta _ { k } ^ { 2 } ) ^ { m } } { ( 1 + \lambda \delta _ { k } ^ { 2 } ) ^ { m } } \left \{ 1 + o \left ( 1 \right ) \right \} , \quad \delta _ { k } ^ { 2 } = 4 \left ( 1 - \cos \frac { k \pi } { n - 1 } \right ) ^ { 2 } .$$

Figure 2 graphs tr(Bm) against this approximation as a function of m, showing how the penalty term coefficient tr(Bm) increases monotonically and nonlinearly with m for any given value of the sample size n. Differentiating (13) with respect to m gives

$$\frac { \partial t r \left ( B _ { m } \right ) } { \partial m } = \log \left ( 1 + \frac { 1 } { \lambda \delta _ { k } ^ { 2 } } \right ) \sum _ { k = 1 } ^ { n - 2 } \left ( \frac { 1 } { 1 + 1 / \left ( \lambda \delta _ { k } ^ { 2 } \right ) } \right ) ^ { m } \{ 1 + o \left ( 1 \right ) \} > 0 ,$$

so that tr(Bm) is increasing in m with decreasing derivative as m increases, as is evident in Figure 2. Moreover, as is clear from formula (13) and the graph, the penalty coefficient tr(Bm) → 2 as =      )     =    n  ∞ ← impact of the penalty on the choice of m is attenuated as n → ∞.

With the implementation of one of these stopping rules, the boosted HP fitting algorithm is automated and data-determined, making it ready for practical use like other non-parametric procedures with data-determined bandwidth selectors. The following sections assess the performance of these stopping rules in simulated experiments and provide two real data applications.

As a numerical illustration for the data displayed in Figure 1, the deviation of the estimated trend ft from the underlying trend xt is measured in terms of the mean squared error (MSE) calculated


<!-- p:18 -->

tr(B\_m) 22

20

18

16

14

12

10

8

6

4

2

0

100

200

300

400

500

600

700

800

m

(λδ2)m Figure 2: Plots of tr(Bm) = n −) {1 + o (1)} for n = 50, 75, 100 (green, blue, sienna). ∑k=1 (1+λδ2)m

as Mn = 1 n−4 4(ft − xt)2. The end points are trimmed in Mn to accommodate start-up in the n-8 ∑t=5 AR(4) process and end points in the HP filter. Calculating the MSE using Mn without trimming did not materially affect the results. In this particular experiment, both ADF and BIC significantly reduce the MSE of the HP filter while AR(4) evidently does not fit the underlying trend well. For further analysis and more detailed graphical displays see Figure B1 in Appendix B.1.

Table 1: MSE of the Estimated Trend in Figure 1

|          |                             | ❍a80   | ❆❉❋   | ❇■❈   | ❆❘✭✹✮   |
|----------|-----------------------------|--------|-------|-------|---------|
| ❙a116♦❝✳ | ❚a114❡♥❞                    | ✷✳✷✼✹  | ✶✳✺✻✶ | ✶✳✸✸✻ | ✸✳✾✶✺   |
| ❙a116♦❝✳ | ✰ ❉❡a116❡a114✳ ❚a114❡♥❞a115 | ✷✳✸✹✹  | ✶✳✺✽✺ | ✶✳✸✸✻ | ✹✳✵✹✻   |
| ❙a116♦❝✳ | ❚a114❡♥❞ ✰ ▼❡❛♥ ❙❤✐❢a116    | ✽✳✻✵✵  | ✻✳✹✾✺ | ✹✳✷✶✷ | ✽✳✻✽✼   |

Note: Use of the fitted AR(4) autoregression follows Hamilton (2018)'s recommended approach, namely ft = β0 + Σk=1 βkxt-k, with coefficients (βk)k=0 obtained from an AR(4) regression with fitted intercept.

### 3 Simulations

We conduct simulation exercises with six data generating processes to observe the finite sample performance of the boosted HP filter in practice when the trend process involves both stochastic and deterministic elements. Similar to the models used in Section 2.3, in DGPs 1 and 2 below we add a stationary component to the deterministic trends. With the addition of this component to the data iterating an excessive number of times in the boosting process in finite samples can potentially lead to overfitting. The experimental design therefore reveals the bias-variance tradeoff that occurs in such cases and the effectiveness of the two stopping criteria in preventing saturation fitting in practical applications of the boosted filter.

DGPs 3-6 focus on fitting a trend under alternative plausible generating mechanisms that include a pure random walk, a structural break, a sinusoidal trend, and various combinations of these trends. The experiments also provide performance comparisons of the boosted filter approach to trend extraction with the autoregressive model estimation approach advocated in Hamilton (2018).


<!-- p:19 -->


## 3.1 The Bias-Variance Tradeoff in Boosting

According to Theorem 2, the boosted HP filter can asymptotically remove any finite-order polynomial drift, whereas the HP filter can only handle a polynomial drift up to the 3rd order. Higher order time polynomials are known to be useful in modeling the nonlinear growth of both macroeconomic and microeconomic time series and as sieve approximations to more general nonlinear trend functions (Baek, Cho, and Phillips (2015); Cho and Phillips (2018)). We are therefore interested in the capability of the boosting mechanism to enable the HP filter to capture these general deterministic trend elements in addition to stochastic trends.

The following two experimental designs involve finite degree polynomial drift functions, gn(t), to accompany the stochastic trend generating mechanism as in (11). The specification illustrates the potential gains that can be obtained in trend determination by boosting the HP filter even in the presence of simple deterministic drifts.

(a) DGP 1: stochastic trend with 3rd-order polynomial drift

5

4

400

3

2

200

1

0

10

20

30

40

1

2

3

4

5

6

8

9

bias\_sqvariance

·MSE

□ADF□BIC

(b) DGP 2: stochastic trend with 4th-order polynomial drift

250

9

200

150

6

100

3

50

0

10

20

30

40

1

2

3

4

5

6

7

8

9

bias\_sqvariance

· MSE

□ADF□BIC

Figure 3: Bias-variance tradeoffs in trend estimation (left panel) and distributions of stopping times calculated by the ADF (green) and BIC (blue) criteria (right panel) for the HP (m = 1) and boosted HP filters (m &gt; 1). The number of iterations (m) is shown on the horizontal axis in each figure.

DGP 1 Set the sample size n = 100 (25 years in quarterly data), and the deterministic trend sn  + ( = x std Go std poet es  eet : dt  = (7 as defined in (11). Step 2: Given the realized trend xt in Step 1, simulate the stationary random component et, also defined in (11), to produce the measured observation xt = xt + et. Step 3: Repeat Step 2 50 times (calling this the inner loop) in order to compute the bias and variance of the filters given the trend xt. Step 4: Repeat Steps 1-3 for 1000 replications (we call this the outer loop) to average the bias and variance over the various realizations of the trend process.


<!-- p:20 -->


- DGP 2 This experimental design is identical to DGP 1 except for the fact that the deterministic trend component is generated by a 4th order polynomial gn(t) = 5· 10−6 . t4 rather than a 3rd order polynomial.

Given a realized xt, in the inner loop of 50 replications we compute for fixed t and m the empirical versions of the bias B(m) = E[f(m)] − xt and the variance var[ftm)]. Then over the realized trend trajectory x = (xt)t=1 we calculate the squared-bias Q(m) = 1n [B(m)]2 and the ∑t=1 n n replications of Q(m) and V(m). The squared bias and the variance are displayed in the left subgraph of Figure 3 for each m = 1, . . . , 40. The black dotted line above the bars sums the underlying two bars and gives the mean squared error (MSE).

In both DGPs, similar patterns of bias-variance tradeoff are evident. Initiating the iteration process from the HP filter (m = 1), we observe a sizable drop in the squared bias and MSE in the first few iterations of boosting. The squared bias continues to decrease as the iterations proceed, whereas variance slowly increases. After it reaches a minimum, the MSE remains insensitive as a rather flat curve as m continues to grow, which reflects the boosting saturation that occurs in finite samples.

To evaluate the effect of the data-driven stopping criteria, we save the number of iterations in each instance and take the sample average in the inner loop. The outer loops provide 1000 such average stopping times and histograms of these average stopping times are shown in the right subgraph of Figure 3. In DGP 1 the 3rd-order polynomial trend can be asymptotically removed by fitting the HP filter only once. Setting the test size to be 0.05, we find that only 25.9% of the average ADF stopping times are smaller than two, indicating that some remnants of the stochastic trend appear in the residual cyclical component with nontrivial probability. The BIC criterion requires at least two iterations in all replications and often three or four fittings. The effect of these fittings is evident in the large reductions in the squared bias as observed in the left panel.

The stopping time data is more intriguing in DGP 2 where we replace DGP 1's cubic trend by a 4th-order time polynomial. According to the limit theory, without the use of boosting the HP filter cannot asymptotically remove such a higher order polynomial trend. This asymptotic theory is clearly supported in the finite sample computations. The bottom-right subgraph of Figure 3 shows that the average ADF stopping criterion is at least two and the BIC criterion requires at least three fittings and often as many as four or five.

## 3.2 Goodness of Trend Determination

In the previous subsection, DGPs 1 and 2 were designed as mechanisms to produce a polynomial trend plus a stochastic trend. Whatever the precise nature of the trend, conditional on its realized form computations of the bias and variance of the boosted HP filter reveal the tradeoff that occurs in these measures of fit as the number m of iterations in the boosted filter rises. As the results with DGPs 1 and 2 show, bias typically falls quickly as m begins to rise, demonstrating immediate gains from boosting. But with increasing m bias reductions diminish and variance rises to a point where mean squared error stabilizes. Thus, in finite samples there are limits to what can be accomplished by boosting just as in any nonparametric procedure.


<!-- p:21 -->


Figure 4: Plots of various sinusoidal trend functions yt: trigonometric 2 cos(0.05πt) (black); trending trigonometric 2t0.25 cos(0.05πt) (green); evaporating trigonometric 2t−0.25 cos(0.05πt) (sienna); and evolving duration trigonometric 2t0.25cos(0.05πt0.90) (blue).

y\_t

6

4

2

0

20

40

-2

-4

-6

Many empirical studies model time series data in terms of integrated or near-integrated processes augmented with various complementary mechanisms such as polynomial drifts, similar drifts with breaks, sinusoidal trends, or trends induced by time varying coefficients, all of which are intended to improve harmony with the observed data but with no certainty concerning the true specification of its generating mechanism. This section considers the performance of the bHP filter in such cases and compares the performance of the bHP filter with Hamilton (2018)'s alternative recommendation of the use of autoregressive (AR) modeling with a small number of lags, typically an AR(4) which is expected to be well suited to quarterly data applications.

The following four models are used to illustrate the performance characteristics of these approaches. The pure random walk case is used as a baseline in DGP 3 and DGPs 4-6 couple this integrated process with various other complementary trend specifications that progressively enhance the complexity of the generating mechanism. The notation follows the framework of (11).

- DGP 3 The observed time series is xt3 (3) = zt, a random walk with independent Gaussian increments.
## DGP 4 Real economic activity may involve long duration cycles that are time-dependent and evolve in a non-replicative manner, for example with varying magnitudes or cycle lengths. We use a deterministic sinusoidal trend of the form gn(t) = 5t1/5 cos(0.05πt0.9) to embody this type of complexity. Figure 4 graphs the form of various expanding and decaying sinusoidal trends of this type. The observed time series is expressed in the form xt4 (4) = gn(t) + xt3). (3)
- DGP 5 This model serves as a simple prototype of GDP takeoff that can be used to represent a successful emerging economy growth trajectory. The model has a structural break in the


<!-- p:22 -->


middle of the sample and takes the form

$$x _ { t } ^ { ( 5 ) } = u _ { t } ^ { ( z ) } \cdot 1 \{ t < 0 . 5 n \} + ( t - 0 . 5 n + \sum _ { s = 0 . 5 n } ^ { t } u _ { s } ^ { ( z ) } ) \cdot 1 \{ t \geq 0 . 5 n \} .$$

The first half of the sample is a stationary sequence and the second half is an integrated process with a linear upward drift.

- DGP 6 This model is formed from the composition of the deterministic sinusoidal trend gn(t) = 5t1/5 cos(0.05πt0.9) of DGP 4 with the structural break model in DGP 5 leading to the time series xt (6) = gn(t) + xt (5)

The goal in the simulation exercise is to determine the trend from data generated by these different mechanisms using the HP filter, the bHP filter, and the AR(4) regression technique of Hamilton (2018). In each replication the observed time series is filtered or regressed to obtain the corresponding fitted trend estimate ft. Deviation from the underlying trend xt is measured in terms of the MSE calculated as before using Mn = 1 n-8 Mn to accommodate start-up in the AR(4) process and end points in the HP filter. Calculating the MSE using Mn without trimming did not materially affect the results reported below. The trend processes xt are produced from the generating processes prescribed above so that x(3 (3) = xt , (3) 1x (4) = gn(t) + x(3), (5) (6) = gn(t) + x(5) for each corresponding DGP.

Table 2: MSE of Trend Estimation and Number of Iterations

|       |                                                |                                                |                                                |                                                |
|-------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| ❉●a80 | ❍a80                                           | ❆❉❋                                            | ❇■❈                                            | ❆❘✭✹✮                                          |
|       | ▼❙❊                                            | ▼❙❊                                            | ▼❙❊                                            | ▼❙❊                                            |
| ✸     | ✶✳✺✾✽✷                                         | ✶✳✺✵✸✸                                         | ✵✳✽✺✹✵                                         | ✵✳✾✷✾✺                                         |
| ✹     | ✷✳✻✷✵✹                                         | ✶✳✹✻✾✼                                         | ✵✳✾✾✹✸                                         | ✶✳✶✺✸✻                                         |
| ✺     | ✶✳✵✼✶✾                                         | ✵✳✾✵✵✶                                         | ✵✳✺✼✽✼                                         | ✶✳✵✵✾✶                                         |
| ✻     | ✶✳✽✼✾✺                                         | ✵✳✽✾✶✸                                         | ✵✳✻✸✷✾                                         | ✶✳✷✽✽✶                                         |
|       | ❆✈❡a114❛❣❡ ♥✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115 | ❆✈❡a114❛❣❡ ♥✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115 | ❆✈❡a114❛❣❡ ♥✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115 | ❆✈❡a114❛❣❡ ♥✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115 |
| ✸     |                                                | ✶✳✷✸✹✷                                         | ✾✳✹✽✺✽                                         |                                                |
| ✹     |                                                | ✷✳✶✵✶✷                                         | ✺✳✼✸✽✹                                         |                                                |
| ✺     |                                                | ✶✳✺✹✺✻                                         | ✺✳✸✸✹✽                                         |                                                |
| ✻     |                                                | ✷✳✸✷✽✹                                         | ✹✳✾✶✷✵                                         |                                                |

Table 2 reports the empirical average of Mn and the observed number of iterations in the bHP filter over 5000 replications. In DGP 3, where the time series is generated from a random walk, the fitted AR(4) is particularly well suited since the regression model includes the true generating mechanism. Unlike the AR(4) regression which is based only on past information in forecasting the trend, the two-sided nature of the HP filter uses all sample information, including future observations to determine the current period trend value. There are notable differences in the results between the ADF selected and BIC selected stopping times for the iteration. These differences reveal the importance of iterating the filter. The BIC selector leads to a substantially lower MSE in trend determination from the boosted filter. The ADF selector tends to stop the iteration too early to achieve optimal improvement with an average number of iterations of 1.23, which is close to the HP filter itself (with m = 1) and substantially lower than the average number of 9.49 iterations for the BIC selector. With the BIC selector the bHP filter provides a substantial reduction in MSE over the HP filter. The bHP-BIC filter also produces a smaller MSE to the underlying trend than the AR(4) regression, an interesting result given that the AR(4) regression model encompasses the simple random walk model DGP 3 and the bHP has none of these explicit features.


<!-- p:23 -->


The HP filter methods are all nonparametric in nature and, as the asymptotic theory suggests, when the tuning parameters are chosen appropriately these methods can adapt to complex trend processes and generating mechanisms. The simulation evidence supports this theory. In particular, once a slowly moving smooth deterministic trend is added to the random walk in DGP 4, the differences in performance are magnified and the MSE of the AR(4) regression deteriorates more than the bHP-BIC filter. Interestingly, the presence of a deterministic trend triggers more iterations in the bHP-ADF filter and it reduces the MSE to 1.47 from the value 1.50 in DGP 3.

Since the first half of the DGP 5 sample is a white noise for which the constant level trend function is easy to predict in a nonparametric method, the filter methods each obtain a smaller MSE than their counterparts in DGP 3. However, as a global parametric method, the AR(4) regression is inevitably misspecified when this structural break from an I(0) to an I(1) process is present in the observed series. In this case, the MSEs of the bHP-ADF and bHP-BIC filters are both q       st    (y   t ta  sy including an evolving sinusoidal trend. For this DGP, the boosted filter again provides much better trend determination. In fact, bHP-BIC has MSE less than half that of the AR(4). Comparison of the results for DGP 4 and DGP 6 shows that the boosted HP filter provides a very effective tool that adapts well to increasing complexity in the underlying trend mechanism. The HP filter, on the other hand, has MSE that is almost three times the size of that of the bHP-BIC filter.

### 4 Empirical Examples

fe e  e     s    sp  e  e pes revisits empirical support for Okun's law across 20 OECD countries. The second explores business cycle behavior in a panel of 78 heterogeneous time series covering emerging and developed markets with various degree of persistence and volatility. The third studies the behavior of the filters in trend determination using US industrial production data over the past century. In this last application we use the HP and bHP filters as well as the AR(4) parametric approach.

## 4.1 Okun's Law

Okun's law (Okun, 1962) posits an empirical association between output and the unemployment rate that has received wide attention among practicing economists and policy makers as well as academic economists and authors of undergraduate economics texts. For the United States, Okun's law is stated as relating a 1% increase in GDP (relative to potential GDP) to a 0.5% reduction in the unemployment rate (relative to the natural rate of unemployment). Following the original formulation by Okun, Ball, Leigh, and Loungani (2017) specify the empirical model in terms of the following empirical regression equation


<!-- p:24 -->


Figure 5: Fitted OLS coefficients and R2 statistics for equation (14) with data obtained by simple HP and boosted HP filtering using ADF and BIC tuning parameter selection. Annual data over 1980 to 2016.

coefficient

Australia

Austria

Belgium

Canada

Denmark

0.00

-0.25

-0.50

-0.75

-1.00

Finland

France

Germany

Ireland

Italy

0.00

-0.25

-0.50

-0.75

-1.00

Japan

Netherlands

New Zealand

Norway

Portugal

0.00

-0.25

-0.50

-0.75

-1.00

Spain

Sweden

Switzerland

United Kingdom

United States

0.00

-0.25

-0.50

-0.75

-1.00

HP

ADF

BIC

HP

ADF

BIC

HP

ADF

BIC

HP

ADF

BIC

HP

ADF

BIC

R-squared

Australia

Austria

Belgium

Canada

Denmark

0.75

0.50

0.25

0.00

Finland

France

Germany

Ireland

Italy

0.75

0.50

0.25

0.00

Japan

Netherlands

New Zealand

Norway

Portugal

0.75

0.50

0.25

0.00

Spain

Sweden

Switzerland

United Kingdom

United States

0.75

0.50

0.25

0.00

HP

ADF

BIC

HP

ADF

BIC

HP

ADF

BIC

HP

ADF

BIC

HP

ADF

BIC


<!-- p:25 -->


$$U _ { t } { - } U _ { t } ^ { * } = \beta \left ( Y _ { t } - Y _ { t } ^ { * } \right ) + \varepsilon _ { t } ,$$

where Ut is the unemployment rate, Yt is the logarithm of GDP, and Ut and Yt* are the natural rate of unemployment and the potential GDP. The sign and the magnitude of β signify the direction and strength of the relationship. In view of its potential policy implications, Okun's law has been extensively tested over time and cross countries. Most recently, Ball, Leigh, and Loungani (2017) testify to its robustness in 20 advanced economies. These authors, as many others, estimate the long-run levels of Ut and Yt* by means of the HP filter under the primary parameter setting λ = 100 for annual data. Equation (14) is therefore a simple regression between two cyclical components produced by the HP filter.

The primary motivation of using trend extraction techniques prior to the regression (14) is to focus on cyclical variates. A secondary motivation is to eliminate the possibility of spurious regression in the variables, which would distort inference (Granger and Newbold, 1974; Phillips, 1986) unless there is strong justification for residual stationarity and a cointegrating relationship between the variables. Use of the ADF test in the implementation of the boosted filter assists in addressing both these issues and rationalizing the regression.

Figure 6: Cyclical components of GDP and the unemployment rate in Ireland. The negative unemployment rate is shown in the second panel. Annual data over 1980 to 2016.

GDP

0.10

0.05

0.00

-0.05

-0.10

1980

1990

2000

2010

(negative) unemployment rate

0.02

0.00

-0.02

-0.04

1980

1990

2000

2010

HP=bHP-ADF=bHP-BIC

We collect annual GDP data from the OECD (0ECD.stat) and annual unemployment rates from the World Bank. We follow Ball, Leigh, and Loungani (2017) in studying the same 20 economies over the period 1980 to 2016. The dataset is mostly balanced, except for a few countries with 1 or 2 missing values at the beginning of the time period. We maintain the primary parameter setting of λ = 100 for the simple HP filter, and we apply the boosted HP filter based on the same tuning parameter λ. For each country, Figure 5 reports the OLS coefficient estimate of β in the upper panel, and the regression R2 in the lower panel. The regressions are conducted with cyclical components extracted by the simple HP filter (shown by red bars), the boosted HP filter with iterations stopped by (i) ADF test outcomes at the 5% level (shown by green bars), and (ii) use of the information criterion (12) (shown by blue bars).


<!-- p:26 -->


For most countries, the fitted coefficients and R2 are similar across the filtering methods. For example, in United States the coefficient is approximately -0.5, and R2 is around 0.8. These figures accord with established results for the USA and the recent findings of Ball, Leigh, and Loungani (2017). In particular, the results from using the boosted filter tend to confirm the conclusion of the latter authors that 'Okun's law is a strong relationship in most countries'.

One country where there is a surprisingly large contrast among the methods is Ireland, where the equation R2 is 0.71 after simple HP filtering but only 0.10 after bHP-ADF filtering and 0.43 after bHP-BIC filtering. To explore these differences, we display the relevant data for Ireland in Figure 6. The upper panel graphs the estimated cyclical components of GDP obtained by HP, bHP-ADF and bHP-BIC. The red line produced by the HP filter shows a long upward trend from the mid 1990s to 2007, followed by a sustained slump until 2013. These trends are evident in the data from inspection and it is apparent that the HP filter fails to remove them in estimating the cycle. In fitting the boosted filter using the ADF procedure to select the boosting tuning parameter 19 iterations of the filter were needed, the largest number of iterations among all the 40 series in this experiment. The associated cyclical component is represented by the green line. This GDP cyclical component fluctuates around the mean in a smaller range, shows no evidence of a residual trend, and it appears much more stable than the cycle determined by the HP filter. The shape of the cycle obtained by using BIC selection is very similar after m = 5 iterations.

The lower panel displays the three fitted curves of the (negative) unemployment rate for Ireland. The negative rate is used in the figure to better visualize the association with the GDP fitted cycles shown in the upper panel. For the unemployment rate series, the boosted filter is stopped by ADF after 2 iterations and by BIC after 5 iterations. In both cases, the use of repeated filtering clearly mitigates residual trend behavior in the unemployment rate in comparison with the HP filter. The mitigation is more evident in the case of bHP-BIC filtering where the fitted cycle in Ghp e y -  e epr o  srr r n eng the aftermath of the 2007-2008 financial crisis. These adjustments in the fitted cycle from bHP htse   e s    ese t  s   rede son coefficients after bHP filtering indeed have similar values, as shown in the upper panel of Figure 5.

In sum, this application continues to support the robustness of Okun's law across developed countries, thereby reinforcing the conclusion of Ball, Leigh, and Loungani (2017). But the results also expose the insufficiency of the standard HP filter to remove stochastic trend components in the case of Ireland. Repeated fitting in this case helps to isolate the cyclical component in each time series.


<!-- p:27 -->


Table 3: Number of iterations and some moments (median in each group)

|                         | ❍a80 - ❡♠❡a114❣✐♥❣ - ◆✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115   | ❍a80 - ❞❡✈❡❧♦♣❡❞ - ◆✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115   | ❜❍a80✲❆❉❋ - ❡♠❡a114❣✐♥❣ - ◆✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115   | ❜❍a80✲❆❉❋ - ❞❡✈❡❧♦♣❡❞ - ◆✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115   | ❜❍a80✲❇■❈ - ❡♠❡a114❣✐♥❣ - ◆✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115   | ❜❍a80✲❇■❈ - ❞❡✈❡❧♦♣❡❞ - ◆✉♠❜❡a114 ♦❢ ✐a116❡a114❛a116✐♦♥a115   |
|-------------------------|------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------|
| ●❉a80 ✭❨✮               | ✶                                                          | ✶                                                        | ✷                                                               | ✸                                                             | ✶✵                                                              | ✼                                                             |
| ❈♦♥a115✉♠♣a116✐♦♥ ✭❈✮   | ✶                                                          | ✶                                                        | ✷                                                               | ✷                                                             | ✶✵                                                              | ✼                                                             |
| ■♥✈❡a115a116♠❡♥a116 ✭■✮ | ✶                                                          | ✶                                                        | ✹                                                               | ✷                                                             | ✶✷                                                              | ✻                                                             |
|                         | ❱❛a114✐❛♥❝❡ ❛♥❞ ❝♦a114a114❡❧❛a116✐♦♥ ❝♦❡✣❝✐❡♥a116          | ❱❛a114✐❛♥❝❡ ❛♥❞ ❝♦a114a114❡❧❛a116✐♦♥ ❝♦❡✣❝✐❡♥a116        | ❱❛a114✐❛♥❝❡ ❛♥❞ ❝♦a114a114❡❧❛a116✐♦♥ ❝♦❡✣❝✐❡♥a116               | ❱❛a114✐❛♥❝❡ ❛♥❞ ❝♦a114a114❡❧❛a116✐♦♥ ❝♦❡✣❝✐❡♥a116             | ❱❛a114✐❛♥❝❡ ❛♥❞ ❝♦a114a114❡❧❛a116✐♦♥ ❝♦❡✣❝✐❡♥a116               | ❱❛a114✐❛♥❝❡ ❛♥❞ ❝♦a114a114❡❧❛a116✐♦♥ ❝♦❡✣❝✐❡♥a116             |
| σ ( Y t )               | ✵✳✵✷✺✶                                                     | ✵✳✵✶✸✹                                                   | ✵✳✵✷✷✽                                                          | ✵✳✵✵✾✹                                                        | ✵✳✵✶✼✸                                                          | ✵✳✵✵✼✻                                                        |
| σ ( C t )               | ✵✳✵✸✸✾                                                     | ✵✳✵✶✷✼                                                   | ✵✳✵✸✷✺                                                          | ✵✳✵✵✾✸                                                        | ✵✳✵✷✸✸                                                          | ✵✳✵✵✼✵                                                        |
| σ ( I t )               | ✵✳✵✾✻✵                                                     | ✵✳✵✹✶✸                                                   | ✵✳✵✼✽✻                                                          | ✵✳✵✸✸✷                                                        | ✵✳✵✻✵✼                                                          | ✵✳✵✷✻✽                                                        |
| ρ ( C t ,Y t )          | ✵✳✼✺✾✷                                                     | ✵✳✼✷✸✹                                                   | ✵✳✻✷✽✹                                                          | ✵✳✹✼✼✷                                                        | ✵✳✻✻✶✵                                                          | ✵✳✹✸✼✵                                                        |
| ρ ( I t ,Y t )          | ✵✳✽✸✷✼                                                     | ✵✳✼✵✷✹                                                   | ✵✳✼✺✷✼                                                          | ✵✳✺✹✸✺                                                        | ✵✳✼✶✼✼                                                          | ✵✳✺✶✸✺                                                        |
| ρ ( Y t ,Y t - 1 )      | ✵✳✼✻✵✽                                                     | ✵✳✼✺✷✽                                                   | ✵✳✻✷✵✶                                                          | ✵✳✺✻✷✹                                                        | ✵✳✺✹✹✹                                                          | ✵✳✹✹✼✺                                                        |

## 4.2 International Business Cycles: Emergent and Developed Economies

The HP filter was originally motivated in Hodrick and Prescott (1997) through its usefulness in the empirical study of business cycles in the USA. In an influential paper with a similar thematic concerning international evidence of business cycles, Aguiar and Gopinath (2007) find that emerging markets (represented by 13 economies) in general are more persistent in the cyclical components of the three series they consider (GDP, consumption and investment) than those of the developed markets (represented by another group of 13 countries). In summarizing their study they declared that "[for emerging markets] the cycle is the trend."

We revisit this conclusion using the methods of the present paper to analyze the same data that the authors provide online.10 Within each country, the three time series have the same length but across countries the length of the time series varies considerably. For example, the median length is 52 quarters for the emerging economies, with Argentina the shortest (1993Q1–2002Q4, 40 quarters), whereas the median is 94 quarters for the developed countries, with Australia, Finland, Netherlands and Norway the longest (1979Q3—2003Q2, 95 quarters). The authors established their empirical results after HP-filtering all 78 time series with the standard setting λ = 1600. As discussed earlier in the paper, the analysis in Phillips and Jin (2015) shows that the implied penalty from using this standard setting is heavier for shorter time series, making stochastic trend identification difficult in international comparisons with series of differing lengths. As our asymptotic theory shows, the boosted HP filter provides a mechanism for adapting the standard setting to account for shorter and longer sample sizes. We employ the iterated procedure to the logarithm of GDP, consumption and investment to study whether the cyclical patterns noted by Aguiar and Gopinath (2007) in the two groups of countries remain distinguishable.11

For each of the 78 time series, we apply the HP filter and automated bHP filters, all with the same λ = 1600 setting, to extract trend and save the cyclical component. In general, the emerging economies need more iterations than the developed countries to isolate trend, manifesting the differences in persistence. Table 3 displays within each group of 13 countries the medians of the number of iterations, standard deviations, and correlation coefficients. The standard deviations typically become smaller as boosting progresses, while the relative magnitude between the emerging and developed markets remains stable. Similar relative sizes are observed in the correlation coefficients. The repeated filtering changes absolute values, but the relative magnitudes of the volatility and persistence are largely maintained in the two groups of countries.

10Downloadable at https://scholar.harvard.edu/gopinath/pages/data-and-codes.

11 Aguiar and Gopinath (2007) report the moments after processing the cyclical components in a macroeconomic se r r r se o    or     o    s possible.


<!-- p:28 -->


Figure 7: Cyclical components of GDP, Consumption, and Investment obtained by the HP, bHPADF and bHP-BIC filters, the latter with data-determined stopping. Developed nations are displayed in green and emerging nations are shown in black.

HP

bHP-ADF

bHP-BIC

0.1

0.0

Consumption

-0.1

0.25

Investment

0.00

-0.25

-0.50

0.10

0.05

GDP

0.00

-0.05

-0.10

1980

1985

1990

1995

2000

1980

1985

1990

1995

2000

1980

1985

1990

1995

2000


<!-- p:29 -->


Figure 7 shows the cyclical components of each time series, with the developed nations in green and the emerging nations in black. Despite the small number of iterations involved, the bHP-ADF filter provides noticeably greater smoothing of the time series. With a only few more iterations taken by the bHP-BIC filter, the cyclical components appear more stable around the mean. The contrast in the volatility of the two groups of countries is strongly manifest in the graph. Overall, this application of the boosted filter therefore confirms that Aguiar and Gopinath (2007)'s findings are robust when machine learning methods are used to assist in compensating for the differing lengths of the time series across countries.

## 4.3 US Industrial Production Index

In this final application of our methods, we analyze a single macroeconomic time series of industrial production that has visually evident trend and (somewhat irregular) cyclical components over a long historical period. The US industrial production index used here is an indicator of aggregate economic activity that measures real production output of manufacturing, mining, and utility industries based on hundreds of individual time series. The series is seasonally adjusted, covers the last century from 1919:Q1-2018:Q2, and comprises 398 observations. It is one of the longest US quarterly macroeconomic series available from the Federal Reserve data base.12

In Figure 8, the black dots plot the logarithm of the raw time series. The shaded regions are the recessions dated by NBER, where both the Great Depression and the recent Great Recession are clearly visible. The index is very volatile before the Second World War. Following the Second World War, fluctuations around the upward path of the index moderate but occur regularly until the end of the 20th century. Figure 9 zooms in on the more recent and more dramatic period of 21st century experience over 2000:Q1–2018:Q2.

It is common for macroeconomists, for example Romer (1999), to study the many changing features of long time series of this type by analyzing subperiods and comparing their defining characteristics across such periods. The HP filter approach, as well as other forms of trend extraction, se e  ses te  oe e te t oe oe e etn  sesr in Figure 8(a) is created with smoothing parameter setting λ = 1600, and this filter accordingly smooths out the peaks and valleys of the index.13 The bHP-BIC filter, shown in Figure B3(b), involves 7 iterations. Compared to the HP filter, it is more responsive to the downturn of industrial production during the episode of the financial crisis.

Figure 9 zooms in the period after 2000. The HP filter completely ignores the dot-com bubble collapse in 2001-2002 whereas the bHP-BIC filter declines in 2001, indicating an impact of this collapse on trend and with the residual deviations (the bHP cycle) corresponding closely to the NBER dated 2001 recession shown by the shaded area of the graph. The bHP filter subsequently reflects the serious impact of the Great Recession on the upward trend path of production, matches the first part of the NBER dated 2008-2009 recession, and extends the recession period to 2010. As a measure of potential industrial production, the estimated impact on trend from the boosted HP filter is more consistent with the fundamental deterioration that many macroeconomists, such as Krugman (2012), perceived to have occurred in the aftermath of the financial crisis.

12Downloadable at https://fred.stlouisfed.org/series/IPB50001SQ.

13bHP-ADF is stopped after one iteration and thereby producing the same result as the HP filter. It is discussed in Section B.3.


<!-- p:30 -->


Figure 8: US Quarterly Industrial Production and fitted trends over 1919-2019. The shaded periods show the recessions dated by the NBER. 29

3

2

1919

1924

1929

1934

1939

1944

1949

1954

1959

1964

1969

1974

1979

1984

1989

1994

1999

2004

2009

2014

2019

(a) HP

3

2

1919

1924

1929

1934

1939

1944

1949

1954

1959

1964

1969

1974

1979

1984

1989

1994

1999

2004

2009

2014

2019

(b) bHP-BIC

4

3

2

1919

1924

1929

1934

1939

1944

1949

1954

1959

1964

1969

1974

1979

1984

1989

1994

1999

2004

2009

2014

2019

(c) AR(4)


<!-- p:31 -->


Figure 9: US Quarterly Industrial Production and fitted trend lines in the 21st century, zoomed versions of Figure 8.

4.65

4.60

4.55

4.50

2000

2001

2002

2003

2004

2005

2006

2007

2008

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019

(a) HP

4.65

4.60

4.55

4.50

2000

2001

2002

2003

2004

2005

2006

2007

2008

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019

(b) bHP-BIC

4.65

4.60

4.55

4.50

2000

2001

2002

2003

2004

2005

2006

2007

2008

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019

(c) AR(4)


<!-- p:32 -->


Table 4: Residual variance (×1000) from HP and bHP filtering and AR(4) autoregression

| a114❡a115✐❞✉❛❧ ✈❛a114✐❛♥❝❡   | ❍a80   | ❇■❈   | ❆❘✭✹✮   |
|------------------------------|--------|-------|---------|
| x t - ̂ f t                  | ✹✳✾✹✺  | ✷✳✹✸✽ | ✶✳✷✾✽   |
| x t +1 - ̂ f t               | ✺✳✵✼✽  | ✷✳✼✶✸ | ✵✳✷✽✻   |

Figures 8(c) and 9(c) report additional findings from the alternative AR(4) approach. During both crashes in the first decade of the 21st century, the AR(4) fitted trend overshoots the extremes of the realized observations both before the burst of the financial bubble and at the end of the collapse that produced the downturn in the real economy that is reflected in the production index. This phenomenon is a typical feature of highly autoregressive (near unit root) fitting. In the present case the fitted AR(4) has long run autoregressive coefficient 0.9978 which is virtually unity.14 Autoregressive fitting of time series tends to capture the fine grain as well as the global features of a time series trajectory, thereby removing most of the variation in the time series and reducing the residual closer to a series with martingale difference characteristics (see also Figure B3(c) in Appendix B). This approach seems too rigid in its goal of removing variation to separate slow moving trend components from irregular cyclical and stationary elements in time series. In particular, as this example demonstrates, the AR approach seems unable to effectively differentiate between trends and cycles in the economic environment, especially during episodes of extraordinary change that impact both trend and cyclical elements in economic activity. In the present case, the slow economic recovery following the crisis may be viewed as a distinguishing feature of the great recession cycle and the overall downturn that was induced may be considered as an inevitable impact on the trend (c.f., Krugman, 2012).

Our assessment of these findings of trend and cycle extraction with a century-long time series is that the bHP-BIC filter works well during periods of normal growth and mild cyclical activity and is also capable of capturing more complex heterogeneous features of the downturns in trend and slow variable recovery from the major recessions that arose in earlier and later years of this long historical period.

This application reveals some major differences between the filter and autoregressive approaches to cycle estimation. Table 4 shows the sample variance of the fitted cyclical components. In the first row of the table, it is clear that the autoregression has very small residual variance, amounting oo b l  l -   l  t    l l de ot that of the HP filter residual. This substantial gain in fitting the time series so well compared with the filtering methods arises from the capacity of the autoregression to capture a stochastic trend component in the time series parametrically (effectively by means of a near-unit root autoregression – here with a long run autoregressive coefficient 0.9978 that is so close to unity) – and to employ a parametric damped cycle of amplitude 0.4531 with period around 1.15 years that is induced by a pae o  e    nt  oe  se xt e ted cycle has high frequency and is much closer to representing a damped seasonal oscillation in the production series than a business cycle, even though the time series that is used here is seasonally adjusted.

14The estimated coefficients of the AR(4) model intercept and the first to fourth lags are 0.011, 1.421, -0.514, 0.216 ss  o  u o o ossi uus osss o s o es oss oe coefficients, is 0.9978. The characteristic polynomial has roots [0.6123, 0.9959, -0.0936 ± 0.4433i] and the complex ross s         (      ed industrial production series was also analyzed and produced very similar results to those given here, so they are not reported.


<!-- p:33 -->


A more dramatic illustration of the forecast-oriented and fit-driven nature of the autoregression is apparent with a simple one-period phase shift. In particular, if we move the observed time series one period forward, then in the second row of the table the sample variance of xt+1 - ft is only about 20% that of the unshifted fit in the first row. Thus, the AR(4) is far better at predicting past values than future values of the trending trajectory, just as may be expected from a unit root autoregression fit of a far more complex time series trajectory. Such a one-period-ahead forecasting mechanism is highly effective in reducing residual variation. But this success in the AR mechanism ms  s s s (- rrns s oros  ns oo s  rme series that involve features over many time periods. Of course, by construction, the parametric AR(4) filter is fundamentally different from the HP filter and has different traditional modeling goals, such as forecasting using past information and studying the impact of past shocks on the system variable.15

By comparison, phase shifting in the case of the HP and bHP-BIC filters leads naturally to deterioration in residual variation. As seen in the table, the sample variance grows in the second row of the table for both HP filters. This is explained by the fact that these filters are designed as nonparametric penalized and smoothly varying best fits to each individual observation in the time series trajectory, taking into account what is happening in neighboring observations. Such a mechanism seems more closely aligned with the general objective of historical trend determination when the concept of trend is based on the hypothesis articulated by Hodrick and Prescott (1997) in the header quotation that "the growth component of aggregate economic time series varies smoothly over time".

15In his pioneering study of business cycles in the United States between 1919-1932, Tinbergen (1939, p.140) employed a fourth-order difference equation to describe the "systematic cyclical forces" in the US economy, analyzing the amplitude and period of the cycle, which turned out to be 4.8 years. Tinbergen claimed that the influence of further lags was "found to be small", a conclusion that matches the recommendation of Hamilton (2018) in using the AR(4) approach. In our present example, there is some evidence that extending the number of lags is beneficial in capturing in-sample fluctuation. Use of an AR(6), for example, reduces the residual variance of 1.298 (shown in the first row of Table 4) of the AR(4) to 1.087. Further, autoregressive lag determination by the standard BIC criterion clearly prefers AR(6) (BIC = −6.75) to AR(4) (BIC = −6.58) for the industrial production time series. The roots of the characteristic equation of the estimated AR(6) are {0.0256, 0.9971, −0.3934 ± 0.6608i, 0.6360 ± 0.4128i}, in which the two sets of complex roots indicate damped cycles of periods 1.51 years and 2.73 years.


<!-- p:34 -->


##### 5 Conclusion

This paper explores the use of a machine learning modification of the HP filter that is designed for trend extraction in studying business cycles in macroeconomic data. The algorithm is based on the idea of repeated HP filtering and is linked to L2-boosting methods that are now commonly used in machine learning approaches to linear regression. The boosted HP filter allows empirical investigators to continue to use a primary tuning parameter setting such as the standard λ = 1600 setting for quarterly data applications but alleviates the concern of using a single choice of this parameter in filtering time series of various lengths and persistence. To enhance the asymptotic performance of the HP filter, the boosted filter introduces a secondary tuning parameter that controls the degree of boosting while holding the primary parameter λ fixed at customary levels such as 1600 for quarterly data. In practical applications, data-determined methods that rely on nonstationarity tests or information criteria may be used to select this secondary parameter in a convenient way. Asymptotic theory shows that the boosted HP filter has the capacity to consistently estimate, and thereby remove, a stochastic trend with time polynomial drift as well as a stochastic trend with deterministic polynomial drift and multiple structural breaks. These results seem relevant for many empirical applications in which standard HP tuning parameter settings are currently used.

The limit theory reveals some of the capabilities of HP filter methods as trend fitting and extraction processes for practical work that have heretofore been little understood. The methodology allows empirical researchers to rely on existing software for standard implementation of the HP filter in the boosting environment. Like ordinary least squares and vector autoregressions, empirically convenient methods such as the HP filter are unlikely ever to be put out of business, in spite of concerns that have been repeatedly raised over many years about their usefulness and their effects on subsequent analysis.

It is hoped that the present contribution will help empirical researchers to better understand the capabilities and limitations of the HP filter and to guide the implementation of a simple machinelearning vehicle for its improvement in applications, thereby mitigating some of the limitations of the HP filter itself. Our position is therefore more optimistic than that of Hamilton (2018). As we have shown, a key advantage of the boosted filter is that it provides a new device for consistently estimating in a nonparametric manner a wide class of trending mechanisms including processes that involve structural breaks, while remaining agnostic about the precise form of the trend non st t  rr   so ar r r    ome optimism, support continuing empirical use, and clearly distinguish the methods from competitor approaches that are typically reliant on correct model specification.

To close the paper, we provide a summary response based on our present findings to the recent critique of the HP filter by Hamilton (2018), which takes up a long tradition of critiquing the HP filter as a tool of applied macroeconomics. Hamilton specifically argues for disuse of the HP filter on the following grounds: (i) it induces spurious cycles; (ii) it is inappropriate for a random walk; (iii) it is two-sided, giving future-informed predictions; (iv) a long autoregression, such as an AR(4) should be used instead. We consider each of these points in turn.

Point (i) repeats the central thesis of Cogley and Nason (1995). The possible presence of spurious cycles in the residual is explained by the asymptotic theory of Theorem 3 of Phillips and Jin (2015) and the smoothness of the limiting form of the filter for popular choices of the smoothing parameter. But point (i) no longer holds if the HP filter consistently estimates the trend function. In particular, t ( e  s s   ss (   s   on smoothing parameter do lead to consistent estimates of stochastic and deterministic trend functions. Moreover, the present paper demonstrates that consistent estimation of a wide class of such trends is possible even with popular choices of the smoothing parameter by 'boosting' the HP filter using machine learning techniques. Point (ii) is invalid when the HP filter consistently estimates the limiting stochastic process corresponding to a random walk or a more general stochastic trend. Again, as shown in Phillips and Jin (2015), suitable choices of the smoothing parameter in relation to the sample size achieve consistent estimation of many limiting stochastic process trend functions; and, further, methods such as boosting can accelerate this convergence to the true function, as shown here. Point (iii) is correct. Like a fixed design nonparametric regression, the HP filter smooths observations on either side of the current observation. So it is true that the HP filter in its standard form is not intended as a predictive device. As Whittaker explained in his original formulation, the goal of the penalized likelihood formulation is to find the 'most probable' function, which in this case is the trend function. The HP filter is a trend detection device that seeks to determine the most probable trend' using clear probabilistic principles. Notwithstanding this primary goal of the filter, one sided filtering can be used recursively for prediction and the methods on       s   n   (   s on terms of a series of smooth functions can be modified to produce predictive techniques. Point (iv) offers an alternative. We have analyzed the performance of an autoregressive approach to trend and cycle determination in our numerical and empirical work, where the findings show a clear preference for the bHP filter over autoregression.


<!-- p:35 -->


We end this paper with a more general response to the proposal of using autoregressions for trend and cycle determination. Autoregressions are widely used in applied economic research and represent a valid modeling approach. But as trend elimination and cycle determination mechanisms autoregressions have limitations. These seem worthy to report in detail. Much of the motivation for using long autoregressions stems from their capacity to capture a wide class of data generating mechanisms, motivated by inversion of the Wold representation in the stationary case and by unit root or near unit root fitting in nonstationary cases via the long run autoregressive coefficient. These valid properties coupled with convenience of implementation have sustained their extensive use in applied work over many decades. Nonetheless, autoregressions are unable to consistently estimate trends of a general form beyond simple polynomials via the inclusion of intercepts and polynomial time trends in their formulation. Further, by virtue of their potential in approximating the Wold representation of the stationary component in a time series, long autoregressions tend to produce residuals whose properties approximate martingale difference innovations, a feature that has led to their extensive use in the identification and analysis of policy shocks. Accordingly, the residuals from fitted autoregressions provide poor approximants of cyclical behavior for which temporal dependence, rather than absence of correlation, is a critical element. Finally, while autoregressions may naturally generate cycles from complex conjugate dynamic roots, such induced cycles are necessarily characterized by regularity, a fact that stands in contrast to the properties of macroeconomic data where both the period and intensity of business cycles and recessions are so noted for their irregularity that these features are embodied in the many popular descriptive terminologies that are given to them, among which we may mention the terms great depression, great moderation, great recession, short sharp recession, and long recovery. There are no doubt many others. In counterpoint to a long autoregression, what the HP filter does and what the boosted filter of this paper does even better is to find the most probable trend, one of sufficient generality that the residuals may take many different forms, thereby accommodating time series that can capture a potentially wide class of cyclical downturns and expansions. For all these reasons it is our view that the HP n         e n  s n e    d applied econometric work.


<!-- p:36 -->


To implement the automated boosted HP filters in practical work, we have developed a documented R function BoostedHP along with a test example to assist empirical researchers. These programs may be downloaded from the following website

https://github.com/zhentaoshi/Boosted\_HP\_filter.


<!-- p:37 -->

### A Proofs

Proof of Theorem 1. We apply the approach used in the proof of Theorem 3 of PJ (2015) with some new modifications. The idea is to use the KL series representations (5) and (6) and the fact that these series converge almost surely and uniformly in r so that successive pseudo-integral operations may be applied to them to obtain the asymptotic form of the boosted filter. The derivations here primarily relate to the asymptotic impact of boosting.

Write Xn (r) = n−1/2x|nr]. By Lemma 3.1 of Phillips (2007) it is known that an expanded probability space can be constructed with a corresponding limiting Brownian motion for which the following uniform convergence holds almost surely

$$\sup _ { 0 \leq t \leq n } \left | X _ { n } \left ( \frac { t } { n } \right ) - B \left ( \frac { t } { n } \right ) \right | = o _ { a . s . } \left ( 1 \right ) .$$

In what follows calculations are made in this expanded space where almost sure convergence applies and in the original space the results translate as usual into weak convergence.

Since the KL series representation (6) of B (r) converges almost surely and uniformly in r we · (I)  = |()  − (dt) | Id e  ∞ ← n

$$\sup _ { 0 \leq t \leq n } \left | X _ { n } \left ( \frac { t } { n } \right ) - B ^ { K _ { n } } \left ( \frac { t } { n } \right ) \right | = o _ { a . s . } \left ( 1 \right ) ,$$

q oe  on s o s ()  t    ←   ∞ ← BKn () for all t ≤ n as n → ∞. We therefore consider the effect of the HP trend operator n Gλ = λL−2(1−L)4+1 1 directly upon BKn √λk4k ξk as n → ∞.

Noting that √λk = [(k − 1) π]−1 and φk (−) = √2 sin t/n , we have, analogous to PJ (2015), k

$$\left ( \sqrt { n } \right ) \sqrt { v _ { k } } & \left [ ( \sqrt { n } ) ^ { 2 } \right ] ^ { n } \frac { \det \varphi _ { k } \left ( \frac { 2 n } { n } \right ) } { \det \left ( \sqrt { \lambda _ { k } } \right ) } , \frac { \det \left ( \frac { t - 1 } { n } \right ) } { \det \left ( \sqrt { \lambda _ { k } } \right ) } \right ) \\ n \left ( 1 - L \right ) \varphi _ { k } \left ( \frac { t } { n } \right ) & \ = \ \sqrt { 2 } n \left [ \sin \left ( \frac { \frac { t } { n } } { \sqrt { \lambda _ { k } } } \right ) - \sin \left ( \frac { \frac { t - 1 } { n } } { \sqrt { \lambda _ { k } } } \right ) \right ] \\ & = \ \sqrt { 2 } \cdot 2 n \cdot \sin \left ( \frac { 1 } { 2 n \sqrt { \lambda _ { k } } } \right ) \cos \left ( \frac { 2 \frac { t - 1 } { n } } { 2 \sqrt { \lambda _ { k } } } \right ) \\ & = \ \frac { \sqrt { 2 } } { \sqrt { \lambda _ { k } } } \cdot \frac { \sin \left ( \frac { 1 } { 2 n \sqrt { \lambda _ { k } } } \right ) } { \frac { 1 } { 2 n \sqrt { \lambda _ { k } } } } \cos \left ( \frac { \frac { 2 t - 1 } { n } } { 2 \sqrt { \lambda _ { k } } } \right ) = O \left ( \frac { 1 } { \sqrt { \lambda _ { k } } } \right ) \\ \intertext { w h e r e t u s l e t h o u l f i n r l y i n t < n a n d u i n f o r a l l k > 1 s i n c \frac { \sin x } { 2 } a n d c o s \left ( x \right ) a r e b o t h }$$

where the result holds uniformly in t ≤ n and uniformly for all k ≥ 1 since sin x and cos (x) are both x uniformly bounded. It follows from (A2) that

$$n \left ( 1 - L \right ) \varphi _ { k } \left ( \frac { t } { n } \right ) = \frac { \sqrt { 2 } } { \sqrt { \lambda _ { k } } } \cos \left ( \frac { \frac { t } { n } } { \sqrt { \lambda _ { k } } } \right ) \left \{ 1 + o \left ( 1 \right ) \right \} , \text { as } n \to \infty ,$$

uniformly in t ≤ n and uniformly in k ≤ Kn with n√λKn → ∞, which holds when Kn/n → 0. By repeated argument as in (A2) we find that


<!-- p:43 -->


$$L ^ { - 2 } \left [ n \left ( 1 - L \right ) \right ] ^ { 4 } \varphi _ { k } \left ( \frac { t } { n } \right ) = \frac { \sqrt { 2 } } { \lambda _ { k } ^ { 2 } } \sin \left ( \frac { \frac { t } { n } } { \sqrt { \lambda _ { k } } } \right ) \left \{ 1 + o \left ( 1 \right ) \right \} = \frac { \varphi _ { k } \left ( \frac { t } { n } \right ) } { \lambda _ { k } ^ { 2 } } \left \{ 1 + o \left ( 1 \right ) \right \} , \quad \left ( A 4 \right )$$

again uniformly in t ≤ n and uniformly for all k ≤ Kn whenever Kn/n → 0. Similarly, as in (A2), we have L−2 [n (1 − L)]4 φk (−) = O (1/λ2) for all k ≥ 1 and t ≤ n.

er av  &lt;  s t  =  b t s avn

$$( 1 - G _ { \lambda } ) ^ { m } = \left ( \frac { \mu L ^ { - 2 } \left [ ( n \left ( 1 - L \right ) \right ] ^ { 4 } } { \mu L ^ { - 2 } \left [ ( n \left ( 1 - L \right ) \right ] ^ { 4 } + 1 } \right ) ^ { m } .$$

Using (A4) and the operational calculus in PJ (2015) we find that

$$( 1 - G _ { \lambda } ) ^ { m } \varphi _ { k } \left ( \frac { t } { n } \right ) & = \left ( \frac { \mu L ^ { - 2 } \left [ ( n ( 1 - L ) ) ^ { 4 } } { \mu L ^ { - 2 } \left [ ( n ( 1 - L ) ) ^ { 4 } + 1 \right ) } \right ) ^ { m } \varphi _ { k } \left ( \frac { t } { n } \right ) \\ & = \left ( \frac { \frac { \mu } { \lambda _ { k } } } { 1 + \frac { \frac { \mu } { \lambda _ { k } } } { \lambda _ { k } ^ { \frac { \mu } { \lambda } } } } \right ) ^ { m } \varphi _ { k } \left ( \frac { t } { n } \right ) \{ 1 + o ( 1 ) \} = \left ( \frac { \mu } { \mu + \lambda _ { k } ^ { 2 } } \right ) ^ { m } \varphi _ { k } \left ( \frac { t } { n } \right ) \{ 1 + o ( 1 ) \} , \ \ ( A 5 ) \\$$

whenever Kn/n → 0, as in (A4). Then, for λ = μn4 with μ &gt; 0 and using (A5), we have for the boosted HP filter

$$\text {boosted in} \ m a t h s c r { I } & = \ [ 1 - ( 1 - G _ { \lambda } ) ^ { m } ] \, B ^ { K _ { n } } \left ( r \right ) = \sum _ { k = 1 } ^ { K _ { n } } \sqrt { \lambda _ { k } } \left [ 1 - ( 1 - G _ { \lambda } ) ^ { m } \right ] \varphi _ { k } \left ( \frac { t } { n } \right ) \xi _ { k } \\ & = \ \sum _ { k = 1 } ^ { K _ { n } } \sqrt { \lambda _ { k } } \left [ 1 - \left ( \frac { \mu } { \mu + \lambda _ { k } ^ { 2 } } \right ) ^ { m } \right ] \varphi _ { k } \left ( \frac { t } { n } \right ) \xi _ { k } + o _ { a . s . } ( 1 ) \\$$

as n → ∞ with Kn → 0 as in (A5). Next, observe that as m → ∞ n

$$\sum _ { k = 1 } ^ { K _ { n } } \sqrt { \lambda _ { k } } \left [ 1 - \left ( \frac { \mu } { \mu + \lambda _ { k } ^ { 2 } } \right ) ^ { m } \right ] \varphi _ { k } \left ( \frac { t } { n } \right ) \xi _ { k } \rightarrow _ { a . s . } \sum _ { k = 1 } ^ { K _ { n } } \sqrt { \lambda _ { k } } \varphi _ { k } \left ( \frac { t } { n } \right ) \xi _ { k } ,$$

because, for all k ≤ Kn, (μ+λk μ m V μ+λKn μ m μ+λkn λkn m → 0 as m → ∞ and Kn/m → 0.

$$\begin{array} { r l } { \frac { \hat { f } _ { \frac { t } { n } , K _ { n } } ^ { ( m ) } } { \xi _ { \frac { t } { n } , K _ { n } } } } & { = \sum _ { k = 1 } ^ { K _ { n } } \sqrt { \lambda _ { k } } \left [ 1 - \left ( \frac { \mu } { \mu + \lambda _ { k } ^ { 2 } } \right ) ^ { m } \right ] \varphi _ { k } \left ( \frac { t } { n } \right ) \xi _ { k } + o _ { a . s . } ( 1 ) } \\ & { = \sum _ { k = 1 } ^ { K _ { n } } \sqrt { \lambda _ { k } } \varphi _ { k } \left ( \frac { t } { n } \right ) \xi _ { k } + o _ { a . s . } ( 1 ) , } \end{array}$$

→a.s. BKn (r) as m, n → ∞. t=[nr] -,Kn n

We deduce that Moreover, since BKn (r) →a.s. B(r) as Kn → ∞, we deduce that


<!-- p:44 -->


$$\widehat { f } _ { \frac { t = | n r | } { n } , K _ { n } } ^ { ( m ) } \to _ { a . s . } B \left ( r \right ) ,$$

as m, Kn, n → ∞ with Kn/n → 0, which together ensure that (A4) and (A5) hold. Then, since Xn ) is almost surely uniformly well approximated by BKn (ν) for all t ≤ n as n → ∞, it f(m) follows that }t=[nr] →a.s. B(r), as m, n → ∞. In the original probability space, this means that √n f(m) Jt=[nr] B(r), and the stated result follows. □ √n

Proof of Theorem 2. The stochastic trend component xt of xt is handled in the same way as the proof of Theorem 1. It remains to show that repeated applications of the HP filter in the boosting algorithm preserve the deterministic polynomial component of the J-th degree in xt . Let yt = β1 t +   · + βJ denote the polynomial trend so that xt = yt + xθ. The boosting algorithm n n applies the operator

$$1 - G _ { \lambda } = \frac { \lambda L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } } { \lambda L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + 1 }$$

repeatedly m times. Taking the j-th term of yt, we note that after m iterations

$$( 1 - G _ { \lambda } ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } = \frac { \lambda ^ { m } L ^ { - 2 m } \left ( 1 - L \right ) ^ { 4 m } \left ( \frac { t } { n } \right ) ^ { j } } { \left ( \lambda L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + 1 \right ) ^ { m } } = 0$$

for all j ≤ 4m − 1, since in that event the numerator component of the operator yields

$$\lambda ^ { m } L ^ { - 2 m } \left ( 1 - L \right ) ^ { 4 m } \left ( \frac { t } { n } \right ) ^ { j } = 0 .$$

The polynomial degree J of yt is finite and so whenever the number of iterations m in the boosted HP algorithm is sufficiently large in the sense that 4m − 1 ≥ J, we have (1 − (1 − Gλ)m) yt = yt. The denominator component of the operator in (A9) may be handled as in PJ (2015) using Fourier methods. An alternative approach to handling the effect of the denominator in this case is to use an integral version of the operator. In particular,

$$& \text {an integral version of the operator. In particular,} \\ & \quad ( 1 - G _ { \lambda } ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } = \left ( \frac { \lambda L ^ { - 2 } ( 1 - L ) ^ { 4 } } { \lambda L ^ { - 2 } ( 1 - L ) ^ { 4 } + 1 } \right ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } = \left ( \frac { L ^ { - 2 } ( 1 - L ) ^ { 4 } } { L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } } \right ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } \\ & = \ \frac { 1 } { \Gamma ( m ) } \int _ { 0 } ^ { \infty } s ^ { m - 1 } e ^ { - s } e ^ { S [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } ] } d s \cdot L ^ { - 2 m } ( 1 - L ) ^ { 4 m } \left ( \frac { t } { n } \right ) ^ { j } \\ & = \ \frac { 1 } { \Gamma ( m ) } \sum _ { k = 0 } ^ { \infty } \left \{ \frac { ( - 1 ) ^ { k } } { k ! } \int _ { 0 } ^ { \infty } s ^ { m + k - 1 } e ^ { - s } d s \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } \right \} \cdot L ^ { - 2 m } \left ( 1 - L \right ) ^ { 4 m } \left ( \frac { t } { n } \right ) ^ { j } = 0 , \\ \intertext { u s i n } & \text {just as in (A10)} \, \text {above for all} \, \ m \, \text { such that } 4 m > \lambda > \dots + 1 > \, j + 1 , \, \text {Thus, (A9)} \, \text { holds and boosting} \\ & \quad \text {and} \, \text {the} \, \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \quad \text { } \$$

just as in (A10) above for all m such that 4m ≥ J + 1 ≥ j + 1. Thus, (A9) holds and boosting removes the polynomial component of the time series. In effect, boosting the HP algorithm raises its capacity to capture accurately a polynomial trend of any finite order as m → ∞. □


<!-- p:45 -->


Proof of Asymptotic Approximation (13). We need to show that as n → ∞

$$t r \left ( B _ { m } \right ) & = t r \left ( I _ { n } - \left ( I _ { n } - S \left ( \lambda \right ) \right ) ^ { m } \right ) = n - \text {tr} \left [ \sum _ { k = 1 } ^ { n - 2 } \left ( \frac { 4 \mu n ^ { 4 } \left ( 1 - \cos \left ( \frac { k \pi } { n - 1 } \right ) ^ { 2 } \right ) } { 1 + 4 \mu n ^ { 4 } \left ( 1 - \cos \left ( \frac { k \pi } { n - 1 } \right ) ^ { 2 } \right ) } \right ) \right ] \left \{ 1 + o ( 1 ) \right \} . \\ \intertext { \text {Define } d ^ { \prime } _ { 2 } = ( 1 , - 2 , 1 ) \text { and the } ( n - 2 ) \times 1 \text { unit vectors} \quad e _ { 1 } \quad = ( 1 , 0 , \dots , 0 ) ^ { \prime } \text { and } \quad e _ { n } \quad = ( 0 , 0 , \dots , 1 ) ^ { \prime } .$$

Define d2 = (1, −2, 1) and the (n−2) × 1 unit vectors e1 , = (1, 0, ..., 0)' and e , = (0, 0, ..., 1)′. (n−2)×1 (n−2)×1 We then write the (n − 2) × n second differencing matrix D' as

$$D ^ { \prime } = \left [ \begin{array} { c c c c c } d _ { 2 } ^ { \prime } & 0 & 0 & \cdots & 0 \\ & d _ { 2 } ^ { \prime } & 0 & \cdots & 0 \\ & & d _ { 2 } ^ { \prime } & \cdots & 0 \\ & & & \ddots & 0 \\ & & & & d _ { 2 } ^ { \prime } \end{array} \right ] = [ e _ { 1 } , M , e _ { n } ] , \\$$

where M is the (n − 2) × (n − 2) tridiagonal symmetric Toeplitz matrix

$$M = \left [ \begin{array} { c c c c c c c } - 2 & 1 & 0 & & & \\ & 1 & - 2 & 1 & \ddots & \\ & & \ddots & \ddots & \ddots & \\ & & & 1 & - 2 & 1 & 0 \\ & & & & 1 & - 2 & 1 \\ \end{array} \right ] .$$

Use the inverse matrix formula

$$\begin{array} { r c l } S ( \lambda ) & = & I _ { n } - \lambda D \left ( I _ { n - 2 } + \lambda D ^ { \prime } D \right ) ^ { - 1 } D ^ { \prime } \\ & = & I _ { n } - \lambda \left [ e _ { 1 } , M , e _ { n } \right ] ^ { \prime } \left ( I _ { n - 2 } + \lambda \left ( e _ { 1 } e _ { 1 } ^ { \prime } + M ^ { 2 } + e _ { n } e _ { n } ^ { \prime } \right ) \right ) ^ { - 1 } \left [ e _ { 1 } , M , e _ { n } \right ] \\ & \sim & I _ { n } - \lambda \left [ e _ { 1 } , M , e _ { n } \right ] ^ { \prime } \left ( I _ { n - 2 } + \lambda M ^ { 2 } \right ) ^ { - 1 } \left [ e _ { 1 } , M , e _ { n } \right ] , \end{array}$$

where the last line follows by

$$I _ { n - 2 } + \lambda D ^ { \prime } D = I _ { n - 2 } + \lambda \left ( e _ { 1 } e _ { 1 } ^ { \prime } + M ^ { 2 } + e _ { n } e _ { n } ^ { \prime } \right ) \sim I _ { n - 2 } + \lambda M ^ { 2 } ,$$

ignoring the end matrix corrections to the first and last diagonal elements as n → ∞. The (n − 2) × (n − 2) central matrix elements of S(λ) are given by the symmetric matrix

$$S _ { n - 2 } \left ( \lambda \right ) = I _ { n - 2 } - \lambda M \left ( I _ { n - 2 } + \lambda M ^ { 2 } \right ) ^ { - 1 } M .$$

The eigenvalues of the symmetric tridiagonal Toeplitz matrix M are well known (Noschese, Pasquini, and Reichel, 2013) to be given by δk = −2 (1 − cos kπ , k = 1, ..., n − 2, and so the eigenvalues n−1


<!-- p:46 -->


We deduce that

$$\begin{array} { r l } { \ t r \left ( B _ { m } \right ) } & { = } & { n - \ t r \left ( \left ( I _ { n } - S \left ( \lambda \right ) \right ) ^ { m } \right ) \sim n - \ t r \left ( \left ( I _ { n - 2 } - S _ { n - 2 } \left ( \lambda \right ) \right ) ^ { m } \right ) } \\ & { = } & { n - \sum _ { k = 1 } ^ { n - 2 } \left ( 1 - \frac { 1 } { 1 + \lambda \delta _ { k } ^ { 2 } } \right ) ^ { m } = n - \sum _ { k = 1 } ^ { n - 2 } \left ( \frac { \lambda \delta _ { k } ^ { 2 } } { 1 + \lambda \delta _ { k } ^ { 2 } } \right ) ^ { m } } \\ & { = } & { n - \sum _ { k = 1 } ^ { n - 2 } \left [ \frac { 4 \mu n ^ { 4 } \left ( 1 - \cos \left ( \frac { k \pi } { n - 1 } \right ) ^ { 2 } \right ) } { 1 + 4 \mu n ^ { 4 } \left ( 1 - \cos \left ( \frac { k \pi } { n - 1 } \right ) ^ { 2 } \right ) } \right ] ^ { m } , } \\ & { \cdot \, l f . \left ( 1 1 \right ) \, l . } & { 4 } \\ & { = } & { n - \sum _ { k = 1 } ^ { n - 2 } \left [ \frac { 4 \mu n ^ { 4 } \left ( 1 - \cos \left ( \frac { k \pi } { n - 1 } \right ) ^ { 2 } \right ) } { 1 + 4 \mu n ^ { 4 } \left ( 1 - \cos \left ( \frac { k \pi } { n - 1 } \right ) ^ { 2 } \right ) } \right ] ^ { m } , } \end{array}$$

as required for (A11) when λ = μn4.

Proof of Theorem 3. We follow the line of argument used in the proof of Theorem 2. The polynomial component gn (t) is handled in a similar way to the proof of Theorem 2 but with complications arising from the break separating the two segments t &lt; τ0 and t &gt; τ0. We analyze these two segments in turn first. Then, following those arguments, we consider limit behavior of the boosted filter at the break point r0 itself.

#### (i) Lower Segment

Over the lower segment we have t = [nr] &lt; τ0 = [nr0] for r &lt; r0, so that for large enough n we have

$$t + 2 m = \lfloor n r \rfloor + 2 m < \tau _ { 0 } = \lfloor n r _ { 0 } \rfloor , \quad \\$$

which implies that 1 {t + 2m &lt; τ0} = 1 since m = o (n) . Repeated applications of the HP filter in the boosting algorithm lead to

$$( 1 - G _ { \lambda } ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } 1 \{ t < \tau _ { 0 } \} = \left ( \frac { L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } } { L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + 1 / \lambda } \right ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } 1 \{ t < \tau _ { 0 } \} .$$

Applying the numerator operator gives

$$L ^ { - 2 m } \left ( 1 - L \right ) ^ { 4 m } \left ( \frac { t } { n } \right ) ^ { j } 1 \{ t < \tau _ { 0 } \} & = ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m < \tau _ { 0 } \} \\ = \quad ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } & = 0 ,$$

because 1 {t + 2m − k &lt; τ0 } = 1 for all k ≥ 0 in view of (A13) and because (1 − L)4m tj = 0 for all j ≤ J, which is finite, and m → ∞ which ensures that 4m ≥ J + 1. Next, combining the numerator and denominator operators in (A14) we have

It follows that the eigenvalues of Sn-2 (λ) are given by

$$\left \{ 1 - \frac { \lambda \delta _ { k } ^ { 2 } } { 1 + \lambda \delta _ { k } ^ { 2 } } \right \} _ { k = 1 } ^ { n - 2 } = \left \{ \frac { 1 } { 1 + \lambda \delta _ { k } ^ { 2 } } \right \} _ { k = 1 } ^ { n - 2 } .$$


<!-- p:47 -->


$$& ( 1 - G _ { \lambda } ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } = \left ( \frac { L ^ { - 2 } ( 1 - L ) ^ { 4 } } { L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } } \right ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } 1 \{ t < \tau _ { 0 } \} \\ & = \ \frac { 1 } { \Gamma \left ( m \right ) } \int _ { 0 } ^ { \infty } s ^ { m - 1 } e ^ { - s } e ^ { S [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } ] } d s \left ( 1 - L \right ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m < \tau _ { 0 } \} \\ & = \ \frac { 1 } { \Gamma \left ( m \right ) } \sum _ { k = 0 } ^ { \infty } \frac { ( - 1 ) ^ { k } } { k ! } \int _ { 0 } ^ { \infty } S ^ { m + k - 1 } e ^ { - s } d s \left [ \frac { L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } ] ^ { k } } { 1 - L } \right ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m < \tau _ { 0 } \} \\ & = \ \sum _ { k = 0 } ^ { \infty } \frac { \Gamma \left ( m + k \right ) ( - 1 ) ^ { k } } { \Gamma \left ( m \right ) k ! } \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m < \tau _ { 0 } \} \\ & = \ \sum _ { k = 0 } ^ { \infty } \frac { ( m ) _ { k } \left ( - 1 \right ) ^ { k } } { k ! } \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m < \tau _ { 0 } \} \quad ( A 1 5 ) \\ & \text {Observe that if $4 m > J + 1$}$$

Observe that if 4m &gt; J + 1

$$& \quad \left [ L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } \left ( 1 - L \right ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \left \{ t + 2 m < \tau _ { 0 } \right \} \\ & = \quad \sum _ { i = 0 } ^ { k } \left ( \begin{matrix} k \\ i \end{matrix} \right ) \frac { 1 } { \lambda ^ { k - i } } L ^ { - 2 i } \left ( 1 - L \right ) ^ { 4 [ m + i ] } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \left \{ t + 2 m < \tau _ { 0 } \right \} \\ & = \quad \sum _ { i = 0 } ^ { k } \left ( \begin{matrix} k \\ i \end{matrix} \right ) \frac { 1 } { \lambda ^ { k - i } } \left ( 1 - L \right ) ^ { 4 [ m + i ] } \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] < \tau _ { 0 } \right \} \\ & = \quad 0 \\ \intertext { \text {for all } } \left ( \begin{matrix} k \\ i \end{matrix} \right ) \text { and for all } k < k _ { i } = | n ( r _ { 0 } - r ) / 4 | \text { because then for } \left | \text {large enough } n \text { and with } m = o ( n ) \end{matrix}$$

for all j ≤ J and for all k ≤ kn = [n(r0 − r)/4] because then for large enough n and with m = o (n) we have

$$t + 2 \left [ m + i \right ] \leq \lfloor n r \rfloor + 2 \left [ m + k \right ] \leq \lfloor n r \rfloor + 2 m + \lfloor n ( r _ { 0 } - r ) / 2 \rfloor + 1 < \lfloor n r _ { 0 } \rfloor = \tau _ { 0 } , \quad ( A 1 7 )$$

in which case 1 {t + 2 [m + i] &lt; τ0} = 1 for all i ≤ k ≤ kn, just as in (A13). In this event, it follows that

$$( 1 - L ) ^ { 4 [ m + i ] } \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \{ t + 2 \left [ m + i \right ] < \tau _ { 0 } \} = ( 1 - L ) ^ { 4 [ m + i ] } \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } = 0 , \ \ ( A 1 8 )$$

and then

$$\text { then } & & \left [ L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \left \{ t + 2 m < \tau _ { 0 } \right \} = 0 ,$$


<!-- p:48 -->


for all k ≤ kn. Hence, the first kn terms of the series in (A15) are zero for large enough n and so

$$& \sum _ { k = 0 } ^ { \infty } \frac { ( m ) _ { k } ( - 1 ) ^ { k } } { k ! } \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m < \tau _ { 0 } \} \\ = & \sum _ { k > k _ { n } = \lfloor n ( r _ { 0 } - r ) / 4 \rfloor } ^ { \infty } \frac { ( m ) _ { k } ( - 1 ) ^ { k } } { k ! } \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m < \tau _ { 0 } \}$$

Next, for k &gt; kn = [n ( )], using (A18) we have 4

$$N e x t , \, & \text {for } k > k _ { n } = \lfloor n \left ( \frac { \tau _ { 0 } - r } { 4 } \right ) \rfloor , \, \text {using } ( A 1 8 ) \, \text { we have} \\ & \quad \left [ L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } \left ( 1 - L \right ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \left \{ t + 2 m < \tau _ { 0 } \right \} \\ & = \quad ( 1 - L ) ^ { 4 m } \sum _ { i = 0 } ^ { k } \binom { k } { i } \frac { 1 } { \lambda ^ { k - i } } L ^ { - 2 i } \left ( 1 - L \right ) ^ { 4 i } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \left \{ t + 2 m < \tau _ { 0 } \right \} \\ & = \quad ( 1 - L ) ^ { 4 m } \sum _ { i = k _ { n } + 1 } ^ { k } \binom { k } { i } \frac { 1 } { \lambda ^ { k - i } } \left ( 1 - L \right ) ^ { 4 i } \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] < \tau _ { 0 } \right \} \\ & = \quad ( 1 - L ) ^ { 4 m } \sum _ { i = k _ { n } + 1 } ^ { k } \binom { k } { i } \frac { 1 } { \lambda ^ { k - i } } \left ( 1 - L \right ) ^ { 4 i } \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] < \tau _ { 0 } \right \} \\ & \text {for all } j \leq J . \text { When } i \geq i _ { n } \colon = \lfloor n \left ( \frac { r _ { 0 } - r } { 2 } \right ) \rfloor \text { we have}$$

for all j ≤ J. When i ≥ in := [n r0−r )」 we have 2

t + 2 [m + i] ≥ [nr] + 2 [m + [n(r0 − r)/2]] &gt; [nr] + [n (r0 − r)] + m &gt; [nr0] = τ0,

which implies 1 {t + 2 [m + i] &lt; τ0} = 0. However, even in this case, application of powers of the differencing operator (1 − L)4i leads to adjacent integer values for which {t + 2 [m + i] − (p − 1) &gt; τ0} and {t + 2 [m + i] − p &lt; τ0} for some positive integer p. Hence,

$$& t + 2 \left [ m + i \right ] - p < \tau _ { 0 } \right \} \text { for some positive integer } p . \text { Hence} , \\ & \quad ( 1 - L ) ^ { 4 i } \left [ \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] < \tau _ { 0 } \right \} \right ] \\ & = \sum _ { p = 0 } ^ { 4 i } \binom { 4 i } { p } \left ( - 1 \right ) ^ { p } L ^ { p } \left [ \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] < \tau _ { 0 } \right \} \right ] \\ & = \sum _ { p = 0 } ^ { 4 i } \binom { 4 i } { p } \left ( - 1 \right ) ^ { p } \left ( \frac { t + 2 \left [ m + i \right ] - p } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] - p < \tau _ { 0 } \right \} \\ & = \sum _ { p = P _ { t } ( \real ) } ^ { 4 i } \binom { 4 i } { p } \left ( - 1 \right ) ^ { k } \left ( \frac { t + 2 \left [ m + i \right ] - p } { n } \right ) ^ { j } , \\ \intertext { P } P _ { ( t ) } \text { is the smallest } p \text { for which } \{ 0 \leq t + 2 \left [ m + i \right ] - p < \tau _ { 0 } \} \text { , in which case } 1 \{ t + 2 \left [ m + i \right ] - p < \tau _ { 0 } \}$$

where P(t) is the smallest p for which {0 ≤ t + 2 [m + i] − p &lt; τ0 } , in which case 1 {t + 2 [m + i] − p &lt; τ0} =


<!-- p:49 -->


1 for p ≥ P(t). We then deduce that

$$1 & \text { for } p \geq P _ { ( t ) } . \text { We then deduce that } \\ & \sum _ { k = 0 } ^ { \infty } \frac { ( m ) _ { ( - 1 ) } ^ { ( k ) } } { k ! } \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m < \tau _ { 0 } \} \\ & = \sum _ { k > k _ { n } = [ n ( r _ { 0 } - r ) / 4 ] } \frac { ( m ) _ { k } ( - 1 ) ^ { k } } { k ! } \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m < \tau _ { 0 } \} \\ & = \sum _ { k > k _ { n } = [ n ( r _ { 0 } - r ) / 4 ] } \frac { ( m ) _ { k } ( - 1 ) ^ { k } } { k ! } \left ( 1 - L \right ) ^ { 4 m } \sum _ { i = k _ { n } + 1 } ^ { k } \binom { k } { i } \frac { 1 } { \lambda ^ { k - i } } ( 1 - L ) ^ { 4 i } \left ( \frac { t + 2 | m + i | } { n } \right ) ^ { j } 1 \{ t + 2 | m + i | < \tau _ { 0 } \} \\ & = \sum _ { k > k _ { n } = [ n ( r _ { 0 } - r ) / 4 ] } \frac { ( m ) _ { k } ( - 1 ) ^ { k } } { k ! } \sum _ { i = k _ { n } + 1 } ^ { k } \binom { k } { i } \frac { 1 } { \lambda ^ { k - i } } ( 1 - L ) ^ { 4 m } \left [ \sum _ { p = P ( t ) } ^ { 4 i } \left ( \frac { 4 i } { p } \right ) ( - 1 ) ^ { k } \left ( \frac { t + 2 | m + i | - p } { n } \right ) ^ { j } \right ] \\ & = 0 , \\ & \text { because } ( 1 - L ) ^ { 4 m } \left ( t + 2 \left [ m + i \right ] - p \right ) ^ { j } = 0 \text { for all } j \leq J \text { since } m \to \infty . \text { This proves that on the lower }$$

because (1 − L)4m (t + 2 [m + i] − p)j = 0 for all j ≤ J since m → ∞. This proves that on the lower segment t = [nr] &lt; τ0 = [nr0] with r &lt; r0 we have

$$( 1 - G _ { \lambda } ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } 1 \{ t < \tau _ { 0 } \} \to 0 , \ \text {as} \ m , n \to \infty .$$

#### (ii) Upper Segment

Treatment of the segment t &gt; τ0 is similarly complicated because application of powers of the dier ns { } () ertd es t o ( - ) oreos Stons on either side of the break point that occurs at t = τ0. Proceeding as in (A15) we have

$$& \quad \text {on either side of the break point that occurs at } t = \tau _ { 0 } . \ \text {Proceeding as in (A15) where} \\ & \quad ( 1 - G _ { \lambda } ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } = \left ( \frac { L ^ { - 2 } ( 1 - L ) ^ { 4 } } { L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } } \right ) ^ { m } \left ( \frac { t } { n } \right ) ^ { j } 1 \{ t > \tau _ { 0 } \} \\ & \quad = \ \frac { 1 } { \Gamma ( m ) } \int _ { 0 } ^ { \infty } s ^ { m - 1 } e ^ { - s } e ^ { [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } ] } d s \left ( 1 - L \right ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m > \tau _ { 0 } \} \\ & \quad = \ \frac { 1 } { \Gamma ( m ) } \sum _ { k = 0 } ^ { \infty } \frac { ( - 1 ) ^ { k } } { k ! } \int _ { 0 } ^ { \infty } s ^ { m + k - 1 } e ^ { - s } d s \left [ L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } \left ( 1 - L \right ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m > \tau _ { 0 } \} \\ & \quad = \ \sum _ { k = 0 } ^ { \infty } \frac { ( m ) _ { k } \left ( - 1 \right ) ^ { k } } { k ! } \left ( 1 - L \right ) ^ { 4 m } \left [ L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m > \tau _ { 0 } \} .$$


<!-- p:50 -->


Next observe that if 4m &gt; J + 1

$$\text {Next observe that if 4 m > J + 1 } \\ ( 1 - L ) ^ { 4 m } \left [ L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \left \{ t + 2 m > \tau _ { 0 } \right \} \\ = \ \sum _ { i = 0 } ^ { k } \left ( \frac { k } { i } \right ) \frac { 1 } { \lambda ^ { k - i } } L ^ { - 2 i } \left ( 1 - L \right ) ^ { 4 \left [ m + i \right ] } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \left \{ t + 2 m > \tau _ { 0 } \right \} \\ = \ \sum _ { i = 0 } ^ { k } \left ( \frac { k } { i } \right ) \frac { 1 } { \lambda ^ { k - i } } \left ( 1 - L \right ) ^ { 4 \left [ m + i \right ] } \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] > \tau _ { 0 } \right \} \\ = \ 0 , \\ \text {for all } j \leq J \text { and for all } k \leq k _ { n } ^ { \varepsilon } = | n \left ( \frac { r - r _ { 0 } - \varepsilon } { 4 } \right ) | \text { for some small } \varepsilon > 0 \text { such that } r > r _ { 0 } + \varepsilon . \text { The final }$$

for all j ≤ J and for all k ≤ kκ = [n (4 r−r0−ε )] for some small ε &gt; 0 such that r &gt; r0 + ε. The final 4 line (A21) follows because for large enough n and with m = o (n) we have

$$t + 2 \left [ m + i \right ] - 4 \left [ m + i \right ] & \geq \left \lfloor n r \right \rfloor + 2 m - 4 \left [ m + k _ { n } ^ { \varepsilon } \right ] = \left \lfloor n r \right \rfloor - 2 m - 4 \left \lfloor n \left ( \frac { r - r _ { 0 } - \varepsilon } { 4 } \right ) \right \rfloor > \left \lfloor n r _ { 0 } \right \rfloor = \tau _ { 0 } , \\ \intertext { s o t h a t 1 } \left \{ t + 2 \left [ m + i \right ] - 4 \left [ m + i \right ] & > \tau _ { 0 } \right \} - 1 \text { for all } i \leq k < k ^ { \varepsilon } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text {$$

so that 1 {t + 2 [m + i] − 4 [m + i] &gt; τ0} = 1 for all i ≤ k ≤ kκ. It then follows that

$$( 1 - L ) ^ { 4 [ m + i ] } \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \{ t + 2 \left [ m + i \right ] > \tau _ { 0 } \} = ( 1 - L ) ^ { 4 [ m + i ] } \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } = 0 , \ \ ( A 2 3 )$$

when 4m ≥ J + 1. We deduce that

$$\sum _ { k = 0 } ^ { \infty } \frac { ( m ) _ { k } ( - 1 ) ^ { k } } { k ! } \left ( 1 - L \right ) ^ { 4 m } \left [ L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \left \{ t + 2 m > \tau _ { 0 } \right \} \\ = \sum _ { k = k _ { n } ^ { s } } ^ { \infty } \frac { ( m ) _ { k } ( - 1 ) ^ { k } } { k ! } \left ( 1 - L \right ) ^ { 4 m } \left [ L ^ { - 2 } \left ( 1 - L \right ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \left \{ t + 2 m > \tau _ { 0 } \right \} .$$

Next, for k &gt; kn i = [n r0−r and in view of (A23), we have 4

$$\text {Next, for $k > k_{n}^{+}\equiv\lfloorn\left( \frac{4}{4} \right\rfloor}$ and in the view $\delta(A^{2S},\mathbb{W}$ have} \\ & \quad \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m > \tau _ { 0 } \} \\ & = \sum _ { i = 0 } ^ { k } \binom { k } { i } \frac { 1 } { \lambda ^ { k - i } } \left ( 1 - L \right ) ^ { 4 [ m + i ] } \binom { t + 2 [ m + i ] } { n } ^ { j } 1 \{ t + 2 [ m + i ] > \tau _ { 0 } \} \\ & = \sum _ { i = k _ { n } ^ { \varepsilon } + 1 } ^ { k } \binom { k } { i } \frac { 1 } { \lambda ^ { k - i } } \left ( 1 - L \right ) ^ { 4 [ m + i ] } \left ( \frac { t + 2 [ m + i ] } { n } \right ) ^ { j } 1 \{ t + 2 [ m + i ] > \tau _ { 0 } \} \, . \quad ( A 2 5 ) \\ \text {When } i > i _ { \varepsilon } ^ { \varepsilon } \colon = | n ( \frac { r _ { 0 } - r + \varepsilon } { i } ) |$$

When i ≥ in := [n (r0−r+ε )」 2

$$t + 2 \left [ m + i \right ] \geq \lfloor n r \rfloor + 2 \left [ m + \left \lfloor n \left ( \frac { r _ { 0 } - r + \varepsilon } { 2 } \right ) \right ) \right ] \right ] > \lfloor n r \rfloor + \lfloor n \left ( r _ { 0 } - r \right ) \rfloor + m > \lfloor n r _ { 0 } \rfloor = \tau _ { 0 } ,$$

which implies that 1 {t + 2 [m + i] &gt; τ0} = 1. For large k and i in (A25) application of the operator


<!-- p:51 -->


(1 – L)4[m+i] involves powers of the differencing operator (1 – L) that lead to adjacent integer values for which {t + 2 [m + i] − (p − 1) &gt; τ0} and {t + 2 [m + i] − p &lt; τ0} for some positive integer p. In this event,

$$& \text {event} , & & ( 1 - L ) ^ { 4 i } \left [ \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] > \tau _ { 0 } \right \} \right ] \\ & = \ \sum _ { p = 0 } ^ { 4 i } \binom { 4 i } { p } \left ( - 1 \right ) ^ { p } L ^ { p } \left [ \left ( \frac { t + 2 \left [ m + i \right ] } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] > \tau _ { 0 } \right \} \right ] \\ & = \ \sum _ { p = 0 } ^ { 4 i } \binom { 4 i } { p } \left ( - 1 \right ) ^ { p } \left ( \frac { t + 2 \left [ m + i \right ] - p } { n } \right ) ^ { j } 1 \left \{ t + 2 \left [ m + i \right ] - p > \tau _ { 0 } \right \} \\ & = \ \sum _ { p = 0 } ^ { P ( \iota ) } \binom { 4 i } { p } \left ( - 1 \right ) ^ { k } \left ( \frac { t + 2 \left [ m + i \right ] - p } { n } \right ) ^ { j } , \\ & P _ { ( t ) } \text { is the largest } p \text { for which } \{ t + 2 \left [ m + i \right ] - p > \tau _ { 0 } \} \text {, in which case } 1 \left \{ t + 2 \left [ m + i \right ] - p < \tau _ { 0 } \right \}$$

where P(t) is the largest p for which {t + 2 [m + i] − p &gt; τ0} , in which case 1 {t + 2 [m + i] − p &lt; τ0} = oo er t tet p   · (t  &lt; d   = {0 &gt; d − [2 +  + 7} I re (t   d o I n

$$1 & \text { for } p \leq P _ { ( t ) } \text { and } \{ t + 2 | m + i \} - p < \tau _ { 0 } \} = 0 \text { for } p > P _ { ( t ) } . \text { We then deduce that for large enough } \\ & n \\ & \sum _ { k = 0 } ^ { \infty } \frac { ( m ) _ { k } - 1 ^ { k } } { k ! } \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m > \tau _ { 0 } \} \\ & = \sum _ { k > k _ { n } ^ { \varepsilon } \in \left [ n ( r _ { 0 } - r ) / 4 \right ] } \frac { ( m ) _ { k } - 1 ^ { k } } { k ! } \left [ L ^ { - 2 } ( 1 - L ) ^ { 4 } + \frac { 1 } { \lambda } \right ] ^ { k } ( 1 - L ) ^ { 4 m } \left ( \frac { t + 2 m } { n } \right ) ^ { j } 1 \{ t + 2 m > \tau _ { 0 } \} \\ & = \sum _ { k > k _ { n } ^ { \varepsilon } \in \left [ n ( r _ { 0 } - r ) / 4 \right ] } \frac { ( m ) _ { k } - 1 ^ { k } } { k ! } \left ( 1 - L \right ) ^ { 4 m } \sum _ { i = k _ { n } ^ { \varepsilon } + 1 } ^ { k } \left ( \begin{matrix} t + 2 | m + i | \\ \lambda ^ { 2 } - i ( 1 - L ) ^ { 4 i } \\ \lambda ^ { 2 } - i ( 1 - L ) ^ { 4 i } \end{matrix} \right ) ^ { t + 2 | m + i | } 1 \{ t + 2 | m + i | > \tau _ { 0 } \} \\ & = \sum _ { k > k _ { n } ^ { \varepsilon } \in \left [ n ( r _ { 0 } - r ) / 4 \right ] } \frac { ( m ) _ { k } - 1 ^ { k } } { k ! } \sum _ { i = k _ { n } ^ { \varepsilon } + 1 } ^ { k } \left ( \begin{matrix} t \\ i \end{matrix} \right ) ^ { 1 } \frac { 1 } { \lambda ^ { k - i } } \left ( 1 - L \right ) ^ { 4 m } \left [ \sum _ { p = 0 } ^ { P _ { ( t ) } } \left ( 4 ^ { i } i \right ) ( - 1 ) ^ { k } \left ( \frac { t + 2 \left [ m + i \right ] - p } { n } \right ) ^ { j } \right ] \\ & = 0 , \\ \\ \text { because } ( 1 - L ) ^ { 4 m } \left ( t + 2 \left [ m + i \right ] - p \right ) ^ { j } \, = \, 0 \text { for all } j \, \leq \, J \text { since } m \to \infty . \text { This proves that on the }$$

because (1 − L)4m (t + 2 [m + i] − p)j = 0 for all j ≤ J since m → ∞. This proves that on the p   &lt;   [] =  &lt; [] =  ps ve

$$( 1 - G _ { \lambda } ) ^ { m } \left ( t / n \right ) ^ { j } 1 \left \{ t < \tau _ { 0 } \right \} \to 0 , \text { as } m , n \to \infty .$$

By combining the results for both segments t &lt; τ0 and t &gt; τ0, it follows that the boosted filter eventually reproduces accurately the polynomial component gn (t) for all t = [nr] with r ≠ r0. The stochastic trend component xθ is treated in the same manner as the proof of Theorem 1, showing that as m, n → ∞ and λ = μn4 for any fixed μ &gt; 0, the boosted filter accurately captures the stochastic trend. It then follows that

$$\frac { \widehat { f } _ { \lfloor n r \rfloor } ^ { ( m ) } } { \sqrt { n } } \sim g \left ( r \right ) + B \left ( r \right ) , \text { for all } r \neq r _ { 0 } ,$$


<!-- p:52 -->


when 1 十 m → 0 as n → ∞, giving the required result for all r ≠ r0. m n

#### (iii) Limit theory at the Break Point

From the above analysis, we know that as m, n → ∞ with m 0← n

$$n ^ { - 1 / 2 } \widehat { f } _ { \lfloor n r \rfloor } ^ { ( m ) } \sim B _ { g } \left ( r \right ) = g \left ( r \right ) + B \left ( r \right ) , \text { for all } r \neq r _ { 0 } .$$

$$[ 1 - ( 1 - G _ { \lambda } ) ^ { m } ] \, g _ { n } \left ( t \right ) 1 \left \{ t = \lfloor n r \rfloor < \lfloor n r _ { 0 } \rfloor \right \} \to g \left ( r \right ) \text { for all } r < r _ { 0 } ,$$

In particular,

and

$$[ 1 - ( 1 - G _ { \lambda } ) ^ { m } ] \, g _ { n } \left ( t \right ) 1 \left \{ t = \lfloor n r \rfloor > \lfloor n r _ { 0 } \rfloor \right \} \to g \left ( r \right ) \text { for all } r > r _ { 0 } .$$

The limit function g (r) of gn (t) as n → ∞ has the form

$$g \left ( r \right ) = \left \{ \begin{array} { l l } { \alpha ^ { 0 } + \beta _ { 1 } ^ { 0 } r + \dots + \beta _ { J } ^ { 0 } r ^ { J } } & { r < r _ { 0 } } \\ { \alpha ^ { 1 } + \beta _ { 1 } ^ { 1 } r + \dots + \beta _ { J } ^ { 1 } r ^ { J } } & { r \geq r _ { 0 } } \end{array}$$

so that the limit function Bg in (A26) satisfies limr r− Bg (r) = Bg (r−) = g (r−) + B (r0) because B (r) is continuous and g (r) is continuous for all r &lt; r0 and has finite left limit g (r−) . Similarly, limr r+ Bg (r) = Bg (r+) = g (r0) + B (r0) because g (r) is continuous for all r &gt; r0 and has finite right limit g (r+) = g (r0) . At the break point τ0 = [nr0] itself, we can write the indicator 1 {t = τ0} as the simple symmetric average of the limits of the left and right side indicators

$$1 \{ t = \lfloor n r \rfloor = \lfloor n r _ { 0 } \rfloor \} = \frac { 1 } { 2 } \left [ \lim _ { r _ { * } \nearrow r _ { 0 } } 1 \{ t = \lfloor n r \rfloor \leq \lfloor n r _ { * } \rfloor \} + \lim _ { r _ { * } \nearrow r _ { 0 } } 1 \{ t = \lfloor n r \rfloor \geq \lfloor n r ^ { * } \rfloor \} \right ] .$$

So by virtue of the continuity of the limit function g (r) on the right and left sides of r = r0, the existence of the right and left side limits of g (r) at r0, and the asymptotic symmetry1 of the action of the filter about the interior point τ0 = [nr0] when r0 ∈ (0, 1) we deduce that

$$n ^ { - 1 / 2 } \widehat { f } _ { \lfloor r r _ { 0 } \rfloor } ^ { ( m ) } \sim B _ { g } \left ( r _ { 0 } \right ) = \frac { 1 } { 2 } \left [ g \left ( r _ { 0 } ^ { - } \right ) + g \left ( r _ { 0 } ^ { + } \right ) \right ] + B \left ( r _ { 0 } \right ) ,$$

giving the stated result.

### B Graphic Demonstrations

This section displays additional graphs to illustrate the performance characteristics and empirical behavior of the trend determination methods discussed in the main text, specifically the HP filter, the bHP-BIC filter, and the fitted AR(4) autoregression. The bHP-ADF filter generally lies between the conventional HP and bHP-BIC versions of the filter and is omitted to avoid overcrowding the graphics.

1The asymptotic symmetry of the filter follows from the asymptotic symmetric Toeplitz representation of the filter given in (A12). Importantly, this asymptotic symmetry holds away from the end points and is valid therefore for an interior break point τ0 = [nr0] when r0 ∈ (0, 1) .


<!-- p:53 -->


### B.1 Decomposition of Figure 1

To assist visualization of trend capturing performance by filters and autoregression, Figure B1 expands on Figure 1 by displaying the trajectory (shown in grey) of a time series composed of (i) a stochastic trend, superposed with (ii) a deterministic fourth order time polynomial trend, and (iii) a stationary ARMA(1,1) disturbance – see equation (11). The trend function is shown in successive panels against the HP filter (shown in red in panel (a)), the bHP filter (shown in orange in panel (b)), and an AR(4) fitted trend (shown in violet in panel (c)). In the middle panel (b), the BIC selector determined the iteration number m = 10 that led to the bHP-BIC fitted trend (shown in orange), which evidently tracks the underlying trend curve (shown in grey) more faithfully than when many more iterations of the filter are employed, as shown by the dark blue curve for m = 128. The third (lower) panel (c) of Figure B1 shows the fitted trend (shown in violet) from an AR(4) autoregression for comparison, which wanders around the true trend curve (in grey), showing greater susceptibility to noise and failure to capture the trend character of the deterministic fourth order time polynomial. This failure is manifested clearly in the systematic deviations of the AR(4) trend from the underlying trend that are apparent in the figure and are quantified in the MSE reported in Table 1 in the text.

### B.2 Illustration of the DGPs in Section 3.2

Figure B2 shows typical trend paths for DGPs 4 and 6 along with the corresponding estimated t  s   i o    e e   eslot the underlying trend than that of the HP filter. The AR(4) does not fit well in the stationary episode of DGP 6, most likely due to its nonsmooth nature and tendency to track the observations rather than the trend. Moreover, when the time series has no stationary episode as in DGP 4, the AR(4) fits also encounter difficulty in adapting to turning points in the time series. The latter is a feature that echoes the empirical example in Section 4.3 where the filter's behavior during economic crises is studied. Once the more complex deterministic mechanism is removed, the bHP filter and the AR(4) both fit well, as is evident in the MSE for DGP 3 in Table 2.

### B.3 Additional Graphs For Section 4.3

Figures in this section detail the fitted cycles obtained in the filtering exercise for US industrial production index given in Section 4.3. Figure B3 displays the entire series along with the fitted cycles, and Figure B4 zooms in on the two decades of the 21st century.

Despite the large error magnitude and volatility in the early years, the HP filter cyclical component oscillates around zero and little evidence is observed of a tendency to drift away from the u  e  nt     s  e  n ss reom bHP-BIC cycle produces a similar test outcome as the standard HP filter, rejecting unit root nonstationarity. The resulting cyclical component of bHP-BIC has fewer large fluctuations than HP but shows cycles of irregular duration and intensity. In contrast, the AR(4)'s fitted trend closely tracks all observations in typical autoregressive fashion and there is little evidence of cycles in the residual.


<!-- p:54 -->


Figure B1: Underlying trend (grey) and fitted trend (magenta) in the upper panel of Figure 1.

30

20-

10

0

25

50

75

100

(a) HP

30

20

10

0

25

50

75

100

(b) bHP-BIC (orange, data-determined m = 10) and bHP with m = 128 (dark blue)

30-

20

10

0

25

50

75

100

(c) AR(4)


<!-- p:55 -->


Figure B2: A typical path of the underlying trend of DGP 4 and 6 (grey dotted curve) and estimated trend (HP: red, bHP-BIC: blue, AR(4): violet).

10

0

DGP4

-10

40

30

20

DGP6

10

0

-10

0

25

50

75

100

HPbHP-BICAR(4)


<!-- p:56 -->


Figure B3: Industrial Production, fitted cycles, and NBER dated recessions starting from 1919. The black dots in the upper panel are the raw IP series data in logarithms. The lower panels show the fitted cycles. The shaded areas are the NBER dated recessions.

4

3

1919

1924

1929

1934

1939

1944

1949

1954

1959

1964

1969

1974

1979

1984

1989

1994

1999

2004

2009

2014

2019

0.2

0.1

0.0

H

-0.1

-0.2

-0.3

0.2

0.1

0.0

BIC

-0.1

-0.2

-0.3

0.2

0.1

0.0

AR4

-0.1

-0.2

-0.3

1919

1924

1929

1934

1939

1944

1949

1954

1959

1964

1969

1974

1979

1984

1989

1994

1999

2004

2009

2014

2019


<!-- p:57 -->


Figure B4: Industrial Production, fitted cycles, and NBER (shaded) recessions in the 21st century, zoomed from Figure B3.

4.65

4.60

d

4.55

4.50

2000

2001

2002

2003

2004

2005

2006

2007

2008

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019

0.05

0.00

-0.05

-0.10

0.05

0.00

BIC

-0.05

-0.10

0.05

0.00

AR4

-0.05

-0.10

2000

2001

2002

2003

2004

2005

2006

2007

2008

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019
