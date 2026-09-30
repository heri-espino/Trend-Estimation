---
id: "Franke_2026_data-driven-hp-smoothing-parameter"
source_pdf: "../pdf/Franke_2026_data-driven-hp-smoothing-parameter.pdf"
source_filename: "Franke_2026_data-driven-hp-smoothing-parameter.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/Franke_2026_data-driven-hp-smoothing-parameter.references.md"
---

<!-- p:1 -->

## A Data-Driven Method to Determine the Smoothing Parameter in the Hodrick-Prescott Filter

Reiner Franke 1 · Jiri Kukacka 2,3 · Stephen Sacht 1,4

Received: 4 February 2025 / Accepted: 31 May 2026 © The Author(s) 2026

### Abstract

The paper reconsiders the Hodrick-Prescott filter and the issue of a suitable choice of its  smoothing parameter λ for  quarterly  data.  Stochastic  processes  generate artificial  data  with  a  known  growth  trend  and  cyclical  component,  and  a  battery  of Monte Carlo  experiments  tests  what  values  of λ yield  the  best  approximation  of the true trend. Specifically, the main summary statistics of the first differences are required to closely match those of the real gross value added in the US, while the average length of their cyclical fluctuations is largely compatible with the spectro - grams of other business cycle data. Regarding the trend component, we distinguish between a deterministic and a stochastic trend. We find that appropriate values of λ are seven to twelve times higher than the conventional λ = 1600 . To make it more intuitive, the paper further proposes a slight modification of the filter that yields a segmented linear trend. Finally, we provide suitable values for its tuning parameter that determines the endogenous break points.

Keywords Business cycles · Trend concept · l 1 trend filter · Growth regimes

Jiri Kukacka

[jiri.kukacka@fsv.cuni.cz](mailto:jiri.kukacka@fsv.cuni.cz)

Reiner Franke franke@uni-bremen.de Stephen Sacht sacht@hwwi.org

1 Institute of Economics, Kiel University, Christian-Albrechts-Platz 4, Kiel 24118, Germany

2 Institute of Economic Studies, Faculty of Social Sciences, Charles University, Opletalova 26, Prague 1 110 00, Czechia

3 Institute of Information Theory and Automation, Czech Academy of Sciences, Pod Vodarenskou vezi 4, Prague 8 182 00, Czechia

4 Research Area Macroeconomic Analyses, Hamburg Institute of International Economics, Mönkedamm 9, Hamburg 20457, Germany

<!-- p:2 -->


### 1  Introduction

Macroeconomic  business  cycle  research  concerned  with  data  exhibiting  long-run growth often needs to decompose these time series into a component capturing a trend, which may possibly show some flexibility or some breaks, and a cyclical com - ponent, which is stationary. For many economists, detrending is a routine task and they prefer not to engage with the finer details. Instead, they are content to rely on a broadly accepted, low-effort procedure. A method that meets these requirements while remaining reasonably transparent is the Hodrick-Prescott (HP) filter. It is there - fore widely applied in academic research and practical business cycle analysis.

The filter is not without problems, though. Before we turn to the paper's central con - cern, a few words should be said about the most common (and usually unanswered) criticism of HP. It contends that the filter may produce spurious dynamic regularities in the cyclical component that are unrelated to the underlying data generation process. 1 There are two reasons why we do not consider this objection to be a concern. First, the criticism is based on elaborate mathematical arguments of mainly asymptotic character, but it is unclear how significant they could be for the finite and rather small empirical samples of hardly more than 250 quarters. Second and more importantly, entertaining the idea of the business cycle as a combination of recurrent phenomena (Lucas, 1977, p. 10), a theoretical possibility that a filter might introduce regularities where actually there are none would be pointless for us. We rather do expect to find waves of expansions and contractions in the data, and it is the purpose of a filter to let them emerge without being spoiled by influences that are not at the heart of the economic wave mechanisms. 2

Thus, in principle, we consider HP detrending as a convenient and useful method (at  least  as  a  first  step  in  an  investigation,  it  may  then  be  supplemented  by  other and perhaps more elaborate devices). However, this does not mean that we are not aware of another problem with the HP filter, which is the choice of the coefficient λ that governs the smoothing of the trend. 3 In this respect we will be solely concerned with quarterly data as the by far most relevant frequency. 4 Here researchers almost exclusively stick to λ = 1600 , the value that was originally proposed by Hodrick and Prescott (1980, 1997) themselves.

A rare exception is Gordon (2003). Studying the long-run evolution of labour productivity he expresses a profound scepticism, when he characterizes λ = 1600 as implying 'implausibly large accelerations and decelerations of the trend within each business cycle' (p. 218, emphasis added). In other words, Gordon argues that the conventional choice λ = 1600 is definitely too low because it sweeps too much of the cycle into the trend. 5

1 With its elaboration on previous work by Harvey (1985); Clark (1987); Cogley (1990), a basic reference in this respect is Harvey and Jaeger (1993).

2 End-of-sample distortions (or inefficiencies, to be more precise) are another criticism put forward against the HP filter (though it concerns any two-sided filter). These effects could be mitigated by applying the filter to a forecast-augmented series (see, e.g., Garratt et al., 2008). In order to avoid opening up a new topic, our investigations will content themselves with discarding a few periods of the time series at the beginning and end of thesample.

3 Danthine and Girardin (1989, p. 37) speak of the 'arbitrariness in the choice of λ [as] the Achilles' heel of this method'.

4 A  treatment  of  alternative  frequencies  would  overload the paper, given that our main interest is in a method of determining the smoothing parameter, not in a final list of its values across different situations. Besides, if the method is found sufficiently satisfactory, it might be applied to any frequency, although setting it up would require some effort.

<!-- p:3 -->


In fact, most studies working with λ = 1600 do not even present and discuss possible variations in the slope of their trend lines. The paper takes this issue as a point of departure to question the validity of λ = 1600 more systematically. Investigations in alternative values of λ commonly use elaborated econometric arguments. Also because they are based on asymptotic theory, their results are, however, hard to asses for nonspecialists. We therefore employ an alternative approach, which requires less technical expertise and tries to follow the KISS principle: 'Keep it sophisticatedly simple'. In essence, we run a large number of Monte Carlo simulations, for which we posit stochastic processes that generate artificial data with a known trend. We can then apply HP with alternative values of λ to these series and see which values will on average yield the best approximation of the true trend line, and also how satisfied we would be with it.

Of course, much hinges on the specific generation of the artificial time series and its  resemblance  to  empirical  data.  Working  with  too  general  a  class  of  stochastic processes could result in such a wide range of optimal values for λ across different realizations that they become uninformative. Regarding the cyclical component of our artificial series, we therefore bear upon their first differences and require that a number of elementary summary statistics tend to match those of an empirical reference series which is central to any business cycle research (this will be the quarterly real gross value added of the nonfinancial business sector in the US). In addition, evidence from other sources (like the spectrograms of stationary data) give us information about the average length of the period in the cyclical component. As concerns the artificial trend, because researchers may have different views on this issue and a priori we cannot be sure whether or not it would make a difference, we will impose our cyclical fluctuations on both a deterministic and a stochastic trend.

The aim of these experiments is that in the end they provide us with a basis for recommending a possibly more appropriate smoothing parameter than λ = 1600 . In the end we will come up with proposals for a value that may be used in practical work with time series that typically grow like GDP or similar macroeconomic variables, if researchers have some faith in the assumptions underlying our Monte Carlo investigations. 6

It goes without saying that any proposal can only approximate the true trend of a given empirical series, which after all is a theoretical construct only. But the simulations of our stochastic processes allow us some insights into the small sample properties of the trend estimations, and they give some impression of how good these approximations may turn out to be. In detail,  our  experiments  will  provide  some observations from which we can conclude that our estimations are fairly robust. That is, even though the smoothing parameters that we propose are different from a value that would be optimal for a given series, we can expect that the deterioration in fitting the trend would not be very serious. 7

5 Gordon illustrates this property of too much flexibility in the trend by quoting Hodrick and Prescott's (1997, p. 9) conclusion that the entire economic boom of the 1960s resulted from an acceleration of trend, rather than a deviation of actual output above trend. He argues that this evaluation neglects external information, 'such as the fact that the unemployment rate was unusually low and the capacity utilization rate was unusually high' (Gordon, 2003, p. 218). This example illustrates that the choice of λ is not innocuous and can materially influence important economic judgments.

6 The  paper  could  still  be  of  benefit  to  other  researchers,  if  they  conduct  similar  (though  perhaps  less costly) Monte Carlo experiments with artificial series that are constructed from their own, alternative assumptions.

<!-- p:4 -->


Furthermore, the paper takes a wider perspective than the usual HP filter. Based on a very similar principle, it also proposes an alternative to it, or rather a complementary concept. To introduce the main idea, recall that the trend line of the HP filter derives from minimizing a function that contains the squared differences between trend and data. In addition, weighted by the parameter λ it penalizes the sum of the squared changes in the slope of the trend. This is an intuitive and straightforward specification of a trade-off in the trend between smoothness and still keeping track of the data. While working with the squared changes is mathematically advantageous, one can also consider the absolute values of these changes. This specification is hardly known in economics but prevalent in  other  scientific  fields  (references  will  be  given  later  on).  It  will  be  convenient  to use the acronym 'HP2' for the original Hodrick-Prescott filter (because of the squared changes), and 'HP1' for its alternative (because of the absolute changes). 8

The interesting point in this distinction is that HP1 implies a qualitative change in the nature of the trend. While an HP2 filter yields a smoothly varying curve, the outcome of HP1 is a segmented linear line with endogenous break points. When HP1 is applied to the log of an output variable growing over time, the slopes of the different linear segments of the trend can therefore be interpreted as different growth regimes  over  endogenously  determined  subperiods.  Such  a  clear-cut  statement  as the by-product of the method may be a rather appealing feature of HP1. Of course, the number and dates of the break points will depend on the specific value of the coefficient attached to the absolute changes in the trend (which will be differently scaled from the λ in HP2). The problem is that for economic time series there are as yet practically no hints about a suitable range of its numerical value. Thus, a second purpose of the paper is to subject HP1 to the same Monte Carlo experiments as HP2 and so build up some experience regarding the other smoothing parameter.

Because of their common methodology it will not be expected that one HP version is systematically superior to the other. However, with the acquired knowledge about the smoothing coefficients a researcher may opt for the filter that tends to produce a trend line whose shape is more to their taste or preference.

The remainder of the paper is organized as follows. The next section introduces the two versions of Hodrick-Prescott detrending. Section 3 puts forward the stochastic  processes  with  which  we  generate  our  artificial  data.  Because  our  approach  is somewhat different from standard time series analysis, it also contains a justification of our choice. A battery of simulation experiments with our data is conducted in Section 4. They serve to derive numerical values for the smoothing parameters that yield a good approximation of the true trend. Some remarks will also give an impression of their robustness. Section 5 concludes, while complementary experiments on an alternative set of artificial data are described in an Appendix.

7 One might want to compare our approach to the one presented by Ravn and Uhlig (2002) who, in a different and more abstract analytical framework, ask how the HP smoothing parameter should be adjusted for different observation frequencies. It may, however, be noted that their investigation starts out from λ = 1600 , whereas our concern is just the appropriateness of this value and not general rescaling rules for other frequencies.

8 It is worth noting that Wolf et al. (2023) use similar denomination, namely HP-1s and HP-2s, to refer to one-sided and two-sided HP filters, respectively.

<!-- p:5 -->


### 2  Two versions of Hodrick-Prescott detrending

Let us first recapitulate the construction of HP2, the classical Hodrick-Prescott fil - ter.  Its  idea  is  actually  older  than  its  first  applications  in  economics  in  the  1980s. Its  origin  dates  back to Leser (1961), who in turn drew on early contributions by Whittaker (1922) and Henderson (1924). 9 The filter's decomposition of a given data series y t into its trend y ⋆ t and a cyclical component c t ( y t = y ⋆ t + c t ) is formulated as a minimization problem that aims to obtain the former as a smooth series which, on the other hand, does not differ too much from the observed data. It is well-known that even if y t is systematically growing in the long term, the detrended component is ensured to be stationary as long as the fourth differences of y t are stationary (King &amp; Rebelo, 1993).

The trade-off between smoothness and proximity to the data is represented by the renowned coefficient λ ,  which  governs  how severely a raggedness in the trend is penalized. For a better distinction from the discussion below it may here be denoted as λ 2 .  As indicated in the Introduction, we will question its standard value of 1600 for quarterly data, asking what multiple μ 2 of it may possibly be more appropriate. This issue will be made explicit in the notation as HP2 = HP2( μ 2 ). The optimization problem minimizes the variance of c t = y t - y ⋆ t over t = 1 , . . . , t max quarters, subject to a penalty for the variation in the second differences of the trend y ⋆ t :

$$H P 2 & = H P 2 ( \mu _ { 2 } ) \colon \\ & \quad \min _ { \{ y ^ { * } \} _ { t = 1 } ^ { t _ { m a x } } } \sum _ { t = 3 } ^ { t _ { m a x } } \left \{ \left ( y _ { t } - y _ { t } ^ { * } \right ) ^ { 2 } + \lambda _ { 2 } \left [ ( y _ { t } ^ { * } - y _ { t - 1 } ^ { * } ) \right ) _ { t - 1 } ( y _ { t - 1 } ^ { * } - y _ { t - 2 } ^ { * } ) \right ] ^ { 2 } \right \} , \\ & \lambda _ { 2 } = \mu _ { 2 } \cdot 1 6 0 0 .$$

$$\lambda _ { 2 } = \mu _ { 2 } \cdot 1$$

Clearly, μ 2 &lt; 1 makes the trend more flexible and μ 2 &gt; 1 introduces a higher degree of smoothness. Going to the limit, λ 2 →∞ , the trend would approximate a straight line. It is important to note that the choice λ 2 = 1600 contained a subjective factor, as it is based on prior beliefs about the magnitude of changes in the cyclical component relative to the trend component. Specifically, formulating the detrending as an opti - mal filter in a structural time series framework yields the relationship λ 2 = σ 2 c / σ 2 d , where σ 2 c is the variance of the cyclical component c t and σ 2 d the variance of the second differences in the square bracket of Eq. 1 . With the idea that a five per cent cyclical component is moderately large as is a one-eighth of one per cent change in the growth rate of a quarter, √ λ 2 = 5 / (1 / 8) = 40 is obtained, i.e. λ 2 = 1600 (Harvey &amp; Jaeger, 1993; Hodrick &amp; Prescott, 1980; King &amp; Rebelo, 1993).

9 We found this historical information in a blog on the web, https://davegiles.blogspot.com/2011/ 12 /con fidenc e-ban ds- for-hod rick-pre scott.html .

<!-- p:6 -->


It should not be neglected that, more particularly, this reasoning rests on the simplifying assumption that both the second differences in the trend as well as the cycli - cal component itself are normally distributed (so that the latter is not cyclical at all).

Hodrick and Prescott (1997) themselves explicitly mentioned that their probability model was false and so were sensitive to the fact that other values of λ 2 could possibly be more appropriate. It is, on the other hand, remarkable that λ 2 = 1600 finds  more  elaborate  support  by  a  different  approach,  which  is  based  on  Fourier analysis  with  its  series  of  trigonometric  functions.  It  invokes  the  concept  of  the gain  function  for  HP2  and  formulates  it  as  a  function  of λ 2 and  the  periodicity T of  a  cycle.  Setting  the  gain  equal  to  one-half  and  solving  the  equation  for λ 2 yields the expression λ 2 = [ 2 sin( π/T ) ] - 4 . Accordingly, employing HP2 with that λ 2 approximates the ideal low-pass filter that passes components with periods less than T quarters (Gomez, 2001). λ 2 = 1600 is then obtained by choosing T = 39 . 7 quarters (rounded). The familiar HP filter would thus be almost perfectly suited to deal with business cycle data. 10

While we already mentioned Gordon's ( 2003) severe doubts that this value would be definitely too low, Hamilton ( 2018, pp. 835f) takes a decidedly opposite view. To get a feel for an appropriate value, he maintains the assumption that the cyclical component and the second differences in the trend are normally distributed. This allows him to determine the aforementioned variances σ 2 c and σ 2 d as the solution of a maximum likelihood problem. Doing this for a number of macroeconomic time series he obtains values of λ 2 below ten, and most of them even below unity! Hamilton's simplification is certainly helpful to solve his estimation problem, but apparently it neglects any possible persistence in the cyclical component that could be interpreted as a business cycle. His implicit hope is that the error in this procedure will not be too serious (Franke et al., 2025). It is a main purpose of this paper to put his and the other conclusions about λ 2 under closer scrutiny.

Another issue of trend estimations is the recognition of possible structural breaks. Suppose one has prior beliefs or information from other sources that over a relatively short period of time there are large changes with permanent effects, giving rise to what might be called a new regime. Such a break or kink in a trend line would be typically smoothed over by HP2, moderating it when it occurs and spreading its effect forward and backward over several quarters or years (Giorno et al., 1995, p. 172). Regarding output data, in particular, it may be fruitful to distinguish different growth regimes, which in a stylized manner are characterized by different but piecewise con - stant slopes in log output. This conception can be conveniently captured by a slight modification of the classical Hodrick-Prescott approach. A good presentation for our purpose is Kim et al. (2009).

10 In  this  respect  it  is  also  worth  noting  that  already  (Prescott,  1986)  himself  described  the  generally employed HP filter as an approximation to a band pass filter that eliminates all frequencies lower than eight years. Such an approximation would be better the longer the time series. So one could ask the question if samples of 240 quarters, say, are long enough.

<!-- p:7 -->


The approach is mostly called l 1 trend filtering. The motivation for this label is that the sum of the squared second differences in the objective function ( 1), mathematically also referred to as their squared l 2 norm, is replaced with the sum of their absolute values, which is the l 1 norm of this vector. In our context we prefer the notation HP1 for this filter. Analogously to λ 2 for HP2, its penalty coefficient may be designated λ 1 . For a reason to become clear in a moment, we decompose it into the product μ 1 · λ 1 ,max , where the symbol λ 1 ,max will also be explained shortly. In this way the optimization problem becomes:

$$H P 1 & = H 1 ( \mu _ { 1 } ) \colon \\ & \quad \min _ { \{ y ^ { * } \} _ { t = 1 } ^ { t _ { m a x } } } \sum _ { t = 3 } ^ { t _ { m a x } } \left \{ \, ( y _ { t } - y _ { t } ^ { * } ) ^ { 2 } \, + \, \lambda _ { 1 } \, | \, ( y _ { t } ^ { * } - y _ { t - 1 } ^ { * } ) \, - \, ( y _ { t - 1 } ^ { * } - y _ { t - 2 } ^ { * } ) \, | \right \} , \ \ ( 2 ) \\ & \lambda _ { 1 } = \mu _ { 1 } \cdot \lambda _ { 1 , m a x } .$$

$$\lambda _ { 1 } = \mu _ { 1 } \cdot \lambda _ { 1 , m a x } .$$

The  solution  is  uniquely  determined  and  has  the  attractive  feature  that  geometrically the trend is a piecewise linear function of time with endogenous break points. Accordingly, one can identify different 'regimes' of the economy. Their timing may not be taken literally, but the method could be useful to arrive without great technical effort at a clear and pronounced statement, and to relate this information to other and perhaps more informal sources on the issue of structural change. The solution y ⋆ t is also relatively robust, in the sense that adding a new observation y t max +1 to the data does not change the slope of its last segment if that value is inside a certain interval (Kim et al., 2009, p. 343). 11

In  contrast  to  the  HP2  minimization problem, there is no analytical expression available for solving HP1. Hence this problem has to be treated numerically in an iterative procedure. 12 Another difference from HP2 is that there is no conventional value of λ 1 that applied research has largely agreed on. In fact, it has to be noted that because of the combination of an l 2 and l 1 norm in Eq. 2, applying HP1 with the same λ 1 to two different series may produce rather unequal matches of their true trend. This general property is the reason why we introduce the coefficient μ 1 in Eq. 2 , as the normalization with a 'maximal' λ 1 promises to make the results for different time series better comparable.

11 A referee made us aware of a more general point of view. He or she states that 'HP1 is indeed a special case of Steidl et al. (2006) and Kim et al. (2009). In general, the penalty function is expressed as the total variation of the trend function's k -th derivative. This specification has a notable advantage: the fitted trend is piece-wise k -th polynomial. Here, HP1 corresponds to k = 1 . A further reference is Tibshirani (2022), who further connects (Kim et al., 2009 )'s setup to discrete splines.' Interestingly, the referee also suggests to set k = 2 to make the fitted trend piece-wise quadratic. While pursuing this proposal would overextend the present paper, we are really gratefully for thus widening our horizon.

12 Over a linear segment, the differences ( y ⋆ t - y ⋆ t - 1 ) and ( y ⋆ t - 1 - y ⋆ t - 2 ) are  therefore only approximately equal. The procedure is described by Kim et al. (2009) in Section 6; for more mathematical background of convex optimization problems of this type, see Arias (2016). A software code for Matlab and C can be downloaded from https://web.stanford.edu/~boyd/l1\_tf/ (the first character 'l' in 'l1\_tf' is an 'ell', the second '1' is the number one).

<!-- p:8 -->


Regarding a discussion of the effects of λ 1 , let us begin with the elementary observation that the penalty coefficient has an impact on the number of break points in the estimated trend. While for λ 1 = 0 it would trivially coincide with the data points, the kinks in y ⋆ t will typically decrease in number as λ 1 is increased (although this relationship need not necessarily be everywhere monotonic; Kim et al., 2009, p. 344). All of the kinks disappear and the trend is given by one straight line when λ 1 gets large enough. As opposed to HP2, there is here a finite value λ 1 = λ 1 ,max for this to happen, which can also be explicitly computed (Kim et al., 2009, p. 343). A straight line also comes about for all λ 1 &gt; λ 1 ,max .

One has, however, to be aware that it is in the first instance this benchmark value that may be different for different series y t , even if they originate from the same stochastic process. 13

As a more detailed information we can add what we learnt from some explorations at the beginning of our investigations, namely that, given a regularly oscillating cyclical  component c t ,  the  value  of λ 1 ,max is  mainly  dependent  on  how  much  the true trend changes, and far less so on the amplitude or period of c t .  For example, a purely linear trend over 60 years yields λ 1 ,max ≈ 16 regardless of its slope. By contrast, a segmented linear trend with subsequent growth rates of 5, 3.5 and 2 per cent (or only two segments with 5 and 3.5 per cent growth) gives rise to λ 1 ,max ≈ 393 (or λ 1 ,max ≈ 260 ).  For  comparison, when doubling the amplitude of the cyclical component in the scenario with the three growth regimes from 0.05 to 0.10, λ 1 ,max only changes from 393 to λ 1 ,max ≈ 380 , while reducing the period of c t from 9.50 to 8.00 years yields λ 1 ,max ≈ 389 . Since at the same time suitable values of μ 1 were found to remain within a relatively limited interval, already these few cases underline the importance of decomposing the coefficient λ 1 in Eq. 2 into the two factors μ 1 and λ 1 ,max .

Back to the Hodrick-Prescott approach to detrending in general, its characteristic feature is the so-called regularization principle, which refers to the second term in the curly brackets in Eqs. 1 and 2. An l 1 regularization is given when an l 1 norm term is added to an objective that is to be minimized. Solutions to this type of problems typically have the form of, somewhat informally speaking, piecewise linear functions. This knowledge is by no means new and it has been made use of in various research fields such as geophysics and, more generally, signal processing (Kim et al., 2009, p. 344, give a large number of references in this respect).

Regarding  economics,  we  only  know  of  one  application  by  Yamada  and  Jin (2013). They employ this method to detrend the real GDP of the Japanese economy. For us it is interesting to note that, regarding the number of break points, they invoke prior research according to which there are three growth regimes in the postwar era until 2011; first rapid growth, then a slow-down, and ultra-slow growth in the third stage. With this view, the authors tune λ 1 such as to obtain two break points where, however,  the  dates  of  their  occurrence  are  not  imposed  but  endogenously  determined. Another idea, for which Yamada (2018) provides some analytical insights, is to select λ 1 = μ 1 · λ max such that the sum of the squared residuals of HP1( μ 1 ) and of HP2(1.00) may be equivalent.

13 It would thus have been more precise to write λ 1 ,max = λ 1 ,max ( { y t } t max t =1 ) in Eq. 2. We avoid this notation because it is visually cumbersome.

<!-- p:9 -->


### 3  Generation of the artificial data

There is a simple and easily reproducible experiment that is suited to cast elementary doubts on the conventional HP filter. Generate artificial quarterly data by positing a linear 60-year trend and an idealized cyclical motion around it. A prototype of the latter is an ordinary sine wave with a period of 8 or 10 years, say. In fact, numerical simulations of small-scale business cycle models frequently yield trajectories of their (normalized) state variables that show a rather similar behaviour. The trend estimated by HP2(1.00) and the true trend can then be best compared by plotting their slopes against time, which should just be a horizontal line. However, HP2(1.00) fails to filter out the oscillations; typically, the sine waves are still clearly visible in these plots.

We adopt the same approach in the present section but work with more 'realistic' data. 14 In this way we can test the ability of HP1 and HP2 to recover the true trend set up by us. Accordingly, we first have to specify a statistic, designated d , that measures the distance between the true trend y ⋆ of the data y and an estimated trend y ⋆, HP j ( μ j ) (in obvious notation). In view of an end-of-sample bias mentioned in the Introduction, we provide for the possibility of discarding the first and last q quarters of the sample. To begin with, let { y t } , { z t } be two time series observed at quarters t = 1 , 2 , . . . , t max and denote their root mean squared deviation as

$$t = 1 , 2 , \dots , t \quad \text {and} \ \text {decide then} \ \text {root mean squared deviation as} \\ \text {RMSD} \ ( y , z ; q ) \coloneqq & \sqrt { \frac { 1 } { t ^ { \max } - 2 q } \sum _ { t = 1 + q } ^ { t ^ { \max } - q } ( y _ { t } - z _ { t } ) ^ { 2 } } \ \ . \\ \text {Concretely, we work with } q = 4 \ \text {quarters. To make the distance between } y ^ { * } \text { and}$$

Concretely,  we  work  with q = 4 quarters.  To  make  the  distance  between y ⋆ and y ⋆, HP j ( μ j ) independent  of  the  size  of  the  variations  in  the  cyclical  component c t = y t - y ⋆ t , we scale their RMSD by the latter's standard deviation, which equals RMSD ( y, y ⋆ ; 4) . For an estimation y ⋆, HP j ( μ j ) we therefore define our distance measure d as

$$d \div R M S D \, \left ( y ^ { * , \, H P \, j ( \mu _ { j } ) } , y ^ { * } ; 4 \right ) \, / \, \ R M S D \, ( y , y ^ { * } ; 4 ) .$$

Hence d measures the deviations of the estimated from the true trend in per cent of the  cyclical  component's variability, so that values of d considerably below unity will certainly be desirable. This normalization will help us put our later quantitative results into perspective. Depending on the context and the feature that we want to stress, we may conveniently write d = d HP j or d = d ( μ j ) . Note that the distance between y ⋆ and an estimated trend y est is the same as the distance between the corresponding cyclical components c = y - y ⋆ and c est = y - y est .

14 Our methodology is thus essentially the same as in Hodrick (2020, Section 10). However, while for the generation of artificial data he uses several (estimated) stochastic standard processes, ours will be geared towards more specific features of the data and, in particular, a typical period of its fluctuations. In addition, we will not be limited to a stochastic trend concept, and we will also check our results with one of the more elaborate processes considered by Hodrick.

<!-- p:10 -->


Let us thus turn to the generation of the artificial data with which we want to test the trend estimations. We will distinguish several versions of dynamic processes to simulate these data, but all of them are composed of a trend and a cyclical component and all of them include random elements. To obtain conclusive results we will therefore have to run a great number of simulations. As another aspect to make our ambition of 'more realistic' data more concrete, we will calibrate the simulated series to an empirical business cycle variable. Here, instead of GDP, we refer to the quarterly real gross value added (GVA) of the US nonfinancial corporate business, measured in logs of course. 15 The basic idea is to determine the parameters in the stochastic processes such that the resulting data share some general key features with GVA. Essentially, this will be moment conditions. The finer details will, however, be given as we are going along.

We make two kinds of distinction in the specification of the data generation pro - cesses; one regarding the trend that we postulate and one regarding the cyclical component. For each of them two cases are considered, so that on the whole we will study four scenarios. For the remainder of the paper, please note that the underlying time unit will be a year instead of a quarter. The time horizon will in all cases be 60 years.

#### 3.1  Three growth regimes

Let us begin with the specification of the output trend, where we take account of an important divide in economic theory: the notion of a deterministic versus a stochastic trend. The former is commonly represented by an increasing line with a fixed slope, the  latter  by  a  random  walk  with  a  constant  drift.  For  the  post-war  US  economy (and not only for that), however, the supposition of a constant growth trend cannot be maintained; undoubtedly growth rates were systematically falling over time. A stylized narrative distinguishes between three growth regimes. Concretely we may draw on a recent discussion by Hall (2020), which incidentally did not primarily take place in an economic context. It charts changes in post-war growth in the following regimes. The first one is an era of modernization stretching from 1950 to 1975, the second an era of liberalism running from 1980 to 2000, and subsequently an era of knowledge-based growth. Connected to the keyword of the productivity slow-down, the growth rates are declining from one regime to the other.

Correspondingly, we postulate three regimes of 20 years each, exhibiting growth rates of 5, 3.5 and 2 per cent, respectively. In order not to put HP2 at an undue disadvantage, the discontinuous jumps from one period to the next are smoothed by a moving average around the break dates. To this end, let MA ( x t , 4) be the two-sided moving average of a series with an extension of 4 quarters on each side of a value x t . Applying it to the step function of the three growth rates, a continuous relationship of (actual or expected) trend growth rates g e t in periods t = 0 , 0 . 25 , 0 . 50 , . . . , 60 . 00 is obtained (though with kinks when the regimes change):

15 The series was downloaded from https: //fr ed.stlouis fed .org/s eries/B4 55RX1Q027SBEA, and the period 1960:1 - 2018:1 extracted. If we just speak of 'GVA' in the following, it may be understood that its real values are meant. GVA is chosen rather than GDP because it is closer to the output variable in most of the small-scale macro models, which is usually the output of only the firm sector. The general cyclical features of GVA and GDP are nevertheless fairly similar.

<!-- p:11 -->


$$\tilde { g } _ { t } ^ { e } = \begin{cases} & 0 . 0 5 0 & \text {if } t < 2 0 , \\ & 0 . 0 3 5 & \text {if } 2 0 \leq t < 4 0 , \\ & 0 . 0 2 0 & \text {if } t \geq 4 0 . \end{cases}$$

$$g _ { t } ^ { e } = M A \, \left ( \tilde { g } _ { t } ^ { e } , 4 \right ) .$$

Surely, g e t =  ̃ g e t most of the time. We use the acronyms DT and ST to refer to the deterministic  and  the  stochastic  trend  concept,  respectively.  With  an  initialization y ⋆ 0 = 0 and a variance σ 2 ε for the random walk, the two trend series are given by:

$$y _ { t } ^ { * } = y _ { t - 0 . 2 5 } ^ { * } \, + \, 0 . 2 5 \, g _ { t } ^ { e } .$$

$$y _ { t } ^ { * } = y _ { t - 0 . 2 5 } ^ { * } \, + \, 0 . 2 5 \, g _ { t } ^ { e } \, + \, \varepsilon _ { t } \, , \quad \varepsilon _ { t } \sim N ( 0 , \sigma _ { e } ^ { 2 } ) .$$

It goes without saying that the innovations ε t in (ST) are independently and identically distributed.

#### 3.2  Justifying our non-standard approach to the cyclical component

In a general description of our approach to test HP with artificial data from a sto - chastic  process,  it  is  similar  to  two  recent  papers  by  Hodrick  (2020,  Section  10) and Schüler (2021, Section 4). They conduct such comparisons between alternative detrending procedures on the basis of several processes which are rather standard in time series analysis and, roughly saying, differ in their complexity. However, while the processes are estimated on US output data, the authors do not discuss whether the resulting cyclical component is also capable of bringing out what we consider a principal characteristic of the business cycle. This is its periodicity as it is inferred from a pronounced peak in the spectrograms of cycle-related data with no long-run growth. Experimenting with estimations of similar processes ourselves, we suspect that a reasonable order of magnitude between, say, 8 and 10 years for their cyclical component may not be automatically guaranteed.

To corroborate our scepticism without going into too much detail, we took an example of a cyclical component in Hodrick's ( 2020) study. This is an AR(2) process as it was estimated by Hodrick as part of Clark's ( 1987) Unobserved Components Model. 16 To begin with, these series do not quite look to the naked eye like what one would be willing to recognize as a typical business cycle pattern. As an illustration consider Fig. 1. As a reference, its top-left panel shows a quarterly US output gap series for the non-farm business. It is given by the percentage deviations of the actual output from an estimation of the potential output by the Congressional Budget Office (CBO). One glance suffices to capture the kind of regularity in these fluctuations. By contrast, the bottom-left panel presents a sample run of the cyclical component of Clark's model. Obviously, its pattern is rather distinct from the empirical series. We may add that this stochastic example is not particularly special; other samples can easily exhibit even more irregularity.

16 The model is described in the Appendix.

<!-- p:12 -->


Fig. 1 The CBO output gap, a sample of Clark's cyclical component, and two samples of (C1), (C2). Note: The shaded areas in the top-left panel indicate the NBER peaks and troughs

Regarding the more objective criterion of a peak in the spectrograms of Clark's AR(2) process, we computed 5000 samples over a time horizon of 240 quarters. It turned out that the frequencies at which their major peaks occurred show an extremely wide dispersion. Their distribution was even bimodal, one mode associated with a period of more than 100 years (apparently reflecting a weak spurious trend in such a relatively small sample), and the other and higher mode characterizing a period of less than 4 years. Hence at least this process does not reliably produce fluctuations at a typical business cycle frequency. Nevertheless, to put our results for HP2 into perspective, we will run our experiments on it, too.

As another check, we specified the cyclical component c t as an  ARMA( p , q ) process, combined it with a trend y ⋆ t from DT or ST above, and as described in the next subsection estimated the sum y t = y ⋆ t + c t on moments of the first differences of a US output series. A choice p = 2 and q = 3 proved to be good enough in this respect. Again, we looked at the resulting spectrograms of the simulations of c t , and again they failed to establish a reliable tendency towards a peak at a typical business cycle frequency.

These explorations induced us not to rely on hopes that a process yields a desired periodicity as a side result. Instead, we stepped away from the standard time series processes and imposed such a periodicity on the cyclical component in a more direct, though unconventional, way. In this sense we believe the following experiments are more appropriate to study business cycle data. Indeed, their results may be viewed as complementary to the investigations by Hodrick (2020) and Schüler (2021).

<!-- p:13 -->


#### 3.3  The cyclical component

The desired periodicity in the spectrogram of the cyclical component is most conveniently ensured by specifying c t as a sine wave. While on its own this simple device will not be sufficient to meet the moment conditions that will be introduced below, incorporating suitable random disturbances will do the trick.

Two  sources  of  noise  are  considered  in  this  respect;  one  randomly  varies  the period of a sine wave from one full cycle run to the next, the other adds a moving average process to these waves. Let us begin with the description of the first concept of an oscillatory motion, designated s t . It has a constant amplitude α and an average period T .  The random periods of one single cycle are drawn from an interval [ T - ∆ T, T +∆ T ] with equal probabilities. If U denotes the uniform distribution and φ is a parameter that may shift the waves in times, we have s t = s t ( T, ∆ T, φ, α ) . The idea is simple but the precise formal specification is more cumbersome:

$$\cdot \text {The idea is simple but the precise formal specification is more cumbersome.} \\ s _ { t } ( T , \Delta T , \phi , \alpha ) & = \alpha \sin [ \omega _ { t } \left ( t - \tau _ { t } \right ) + \phi ] , \quad \text {where} \colon \\ \omega _ { t } & = 2 \pi / T ( k ) \quad \text {for } t _ { k - 1 } \leq t < t _ { k } , \\ T ( j ) & \sim U ( T - \Delta T , T + \Delta T ) \quad j = 1 , 2 , \dots , \\ t _ { k } & = \sum _ { j = 1 } ^ { k } T ( j ) \quad t _ { 0 } = 0 , \\ \tau _ { t } & = t _ { k - 1 } \quad \text {for } t _ { k - 1 } \leq t < t _ { k } . \\$$

To understand this patchwork, consider the motion in continuous time and put φ = 0 for a short moment. A cycle with period T ( k ) begins with a zero value at t = t k - 1 , when the argument of the sine function in the first row is ω t ( t - t k - 1 ) = 0 . Note that t k - t k - 1 = T ( k ) . Thus, as t approaches t k from the left, the argument tends towards ω t ( t k - t k - 1 ) = [2 π/T ( k )] T ( k ) = 2 π and the function converges to sin(2 π ) = 0 , from whereon the next cycle starts. With a nonzero shift factor φ , we have sin( φ ) at these connection points. Of course, the function s t is only evaluated in the quarterly intervals at t = 0 , 0 . 25 , 0 . 50 , . . . , 60 .

Function (7 ) leads us to the question of what period to choose for a 'typical' busi - ness cycle. According to much of the discussion around Hodrick-Prescott detrending, it is not longer than 8 years. Recent evidence provided by Beaudry et al. (2020) and by Barrales-Ruiz and von Arnim (2021), however, contradicts this view. Independently of possible problems with particular detrending devices, they compute spectograms of cycle-related empirical variables with no long-run growth (such as working hours per capita or job finding rates, for example). Here they find a pronounced peak between 38 and 40 quarters. This is also the order of magnitude that will be normative for our investigation.

Motions s t form the basis for our cyclical component. Even when adding some noise to s t , however, it may be expected that one such motion would be too regular and thus make the task for HP unduly easy. For this reason two cases will be distinguished, one being based on one oscillation s t and the other on a superimposition of two of them. The cases will be referred to as C1 and C2, respectively. For C1 we assume that the periods vary with ∆ T = ± 1 around T = 9 . 50 years. In the second scenario we add a second but less important motion s t . Its periods lie between 6 and 8 years and its amplitude is half as wide. This choice is motivated by a second minor peak in several of the aforementioned spectrograms.

<!-- p:14 -->


Regarding the additional random noise imposed on these constituent oscillations, it turns out that a moving average process with three lags, MA(3), is sufficient for our purpose. 17 Thus, with respect to an amplitude α , the MA coefficients θ 1 , θ 2 , θ 3 , and the variance σ 2 η of its innovations η t , our two cyclical scenarios are given by:

$$c _ { t } & = s _ { t } ( 9 . 5 0 , \Delta T , \phi , \alpha ) \\ & + \, \eta _ { t } \, + \, \sum _ { j = 1 } ^ { 3 } \theta _ { j } \, \eta _ { t - 0 . 2 5 \, j } \, , \quad \eta _ { t } \sim N \left ( 0 , \sigma _ { \eta } ^ { 2 } \right ) \, , \quad \Delta T = 1 . 0 0 , \, \phi = 0 . \\$$

$$c _ { t } & = s _ { t } ( 9 . 5 0 , 0 . 0 0 , 0 , \alpha ) \ + \ s _ { t } ( 7 . 0 0 , 1 . 0 0 , 0 . 7 0 \cdot 7 . 0 0 , \alpha / 2 ) \\ & \quad + \ \eta _ { t } \ + \ \sum _ { j = 1 } ^ { 3 } \theta _ { j } \, \eta _ { t - 0 . 2 5 \, j } \ , \quad \eta _ { t } \sim N \left ( 0 , \sigma _ { \eta } ^ { 2 } \right ) \ , \quad \Delta T = 1 . 0 0 . \quad ( C 2 ) \\ \intertext { t h e f t } \ The s h i f t \, \phi = 0 . 7 0 \colon 7 0 \, \text {in the second sine wave in } ( C 2 ) \text { introduces more irregular- }$$

The shift φ = 0 . 70 · 7 . 00 in the second sine wave in (C2) introduces more irregularity in the composite motion than, for example, φ = 0 . 50 · 7 . 00 . Note that the parameters θ 1 , θ 2 , θ 3 , σ 2 η will generally be different across C1 and C2. Before turning to their  determination, we should give a visual impression of the somewhat abstract description of C1 and C2. This is done in Fig. 1, which is based on the numerical calibration presented in a moment. The MA parts of the two scenarios use the same sequence of random numbers drawn from the unit normal (which are then multiplied by the specific standard deviation σ η for  (C1)  and  (C2),  respectively). The  series (C1) is seen to exhibit no great differences in the amplitudes of the single cycles. Especially the behaviour around the upper and lower turning points can be rather diverse, though. This equally holds true for the series (C2). In addition, however, there is now a noticeable variability in the amplitudes, too. On the whole, this series seems to constitute a good example of what detrending procedures qualitatively tend to produce in empirical work.

#### 3.4  Calibration of the numerical coefficients

Combining the trend scenarios (DT) and (ST) with the cyclical scenarios (C1) and (C2) yields our artificial data y t = y ⋆ t + c t . On the whole this gives us four scenarios with which we can test the Hodrick-Prescott filters and the choice of their smoothing parameters. That is, we will apply the filters to the data alternatively generated by (DT-C1), (DT-C2), (ST-C1), (ST-C2).

Even though the thus estimated cyclical components c est t will not coincide with the true c t , their spectrograms will not substantially differ. So the spectrogram crite rion for the artificial data can be safely considered satisfied. The other features that, as announced above, we want the data to share with the empirical GVA are more concise and refer to their first differences. In detail, we consider the five moments of their standard deviation and the first four autocorrelations. For each scenario we settle down on a parameter set β := ( α, θ 1 , θ 2 , θ 3 , σ η , σ ε ) such that, 'on average', the simulated moments come as 'close' as possible to their empirical counterparts. With respect to a random seed b = 1 , . . . , B , 'closeness' is described by a loss function L = L ( β, b ) that computes the mean of a quadratic distance between the moments across 10 simulation runs. 18 For each such b , parameters ˆ β b are computed that minimize this loss over all admissible β .

17 It is unnecessary to include an autoregressive part because its role is already taken on by the sine waves.

<!-- p:15 -->


It actually turns out that, in each case, all of the empirical moments are (almost) perfectly matched, L ( ˆ β b , b ) ≈ 0 for all b . For the two stochastic trend scenarios this holds for fixing σ ε at values less or equal to 0.0050, while raising σ ε above it would increasingly deteriorate the match. We choose σ ε = 0 . 0050 for our calibration, which in this sense acknowledges a maximal role to the randomness in the trend.

Now, it has to be taken into account that a single ˆ β b is only tailored to a particular random seed b , and that employing the same parameters for a different seed will spoil the optimal match L ( ˆ β b , b ) ≈ 0 .  In  other  words, a given parameter vector ˆ β b may prove more or less lucky in this extended context. To 'average' across the cases of good and bad luck, we opt for the random seed b o that, across all of the realizations of the stochastic processes that we considered, yields the lowest mean loss. Correspondingly, with respect to a given scenario (DT-C1), (DT-C2), etc., we generate the artificial data with the following parameter vector:

$$\beta ^ { o } = \hat { \beta } ^ { o } , \quad \text {where} \quad b ^ { o } \colon = \arg \min _ { b } \ \left \{ \frac { 1 } { B } \ \sum _ { c = 1 } ^ { B } \ L \left ( \hat { \beta } ^ { b } , c \right ) \right \} . \\ \\ \\ \\ \text {The outcome of the optimization} \ \quad \arg \sum _ { b } \ 1 - \log 1 _ { B } \log 1 _ { C } \ L \log 1 _ { B } \ L \log 1 _ { C } .$$

The outcome of the optimization procedure (8) is reported in Table 1. It does not seem very fruitful to compare the coefficients across the four scenarios, except per - haps for the observation that a lower amplitude α tends to be compensated by higher values of θ 1 , indicating a stronger role for the stochastic MA process (given that their variance σ 2 η does not greatly vary).

The minimum losses (1 /B ) ∑ c L ( β o , c ) in Eq. 8 are not very different across the scenarios. Hence all four scenarios would be suitable dynamic processes to generate the artificial data with which, in the next section, we can test HP1 and HP2 in a context of GVA cyclical growth. The statistics with which we want to evaluate these Monte Carlo experiments will be reported for all of the scenarios. For reasons of space, on the other hand, our graphical illustrations will concentrate on ST-C2 and DT-C2. In this way account may be taken of both believers in a deterministic and believers in a stochastic trend.

18 In a rigorous econometric framework such an averaging would increase the precision of the parameter estimates vis-à-vis the ideal case when the expected moments could be determined analytically; for details see, e.g., Duffie and Singleton ( 1993, p. 945).

<!-- p:16 -->


ε

| Table 1 Numerical coefficients β o from optimization (8) for the four scenarios (rounded) - α   |    θ 1 |    θ 2 |    θ 3 |   100 · σ η | 100 · σ   |
|-------------------------------------------------------------------------------------------------|--------|--------|--------|-------------|-----------|
| DT-C1: 0.0450                                                                                   | 1.4055 | 0.7221 | 0.6534 |      0.7256 | -         |
| DT-C2: 0.0433                                                                                   | 1.3885 | 0.7083 | 0.6475 |      0.7175 | -         |
| ST-C1: 0.0514                                                                                   | 1.1682 | 0.7497 | 0.5940 |      0.7383 | 0.500     |
| ST-C2: 0.0421                                                                                   | 1.2354 | 0.7515 | 0.6310 |      0.7117 | 0.500     |

### 4  Choosing the smoothing parameters

With  the  design  of  the  four  scenarios  for  our  artificial  data  and  their  numerical specification in Table 1, we have now laid the groundwork for the comprehensive Monte Carlo experiments in this section. In essence, for each scenario we generate b = 1 , . . . , B = 1000 samples of data and, applying HP1 and HP2 to each of them, determine the values μ opt j ( b ) , that minimize the distance d ( μ j , b ) between the estimated and the true trend ( j = 1 , 2 ). We can then study the distributions of these optimal values more closely.

Beforehand,  we  should  have  a  look  at  the  shape  of  the  single  functions μ j ↦→ d ( μ j , b ) . In particular, the minimization results would appear more reliable if we could mostly be sure that we will not have to face multiple local minima in these functions. Furthermore, by checking how sensitively the distances may react to minor changes in μ j , we would get a first impression of the robustness of the results below.

To this end, Fig. 2 picks out two sample runs over 60 years from scenario DT-C2 and ST-C2, respectively, and plots these functions over a relevant range. 19 The overall idea that the plots convey is that the functions are relatively well-behaved. In fact, from our explorations of many other examples we can say that these examples are qualitatively fairly representative. We nevertheless do not conceal a possible exception with the occurrence of two local minima (the bold (blue) line in the upper-left panel), but even though, the distances to which these values of μ 1 give rise are not very different. We can thus have some confidence that multiple minima are not a great problem in the minimization problems.

Another important observation is that small and even somewhat wider deviations from the optimal μ 's have rather limited effects. This holds for the performance of HP1 as well as HP2. It may in this context be emphasized that even a performance of d ( μ 1 ) = 0 . 30 versus d ( μ 1 ) = 0 . 26 , which visually does not seem negligible in the lower-left panel, would still be acceptable and need not necessarily suggest a rejection of the inferior μ 1 : when plotting the two corresponding cyclical components of these estimations in one diagram, this outcome will be assessed as practically the same. As a first and general result we can therefore state: 20

Remark 1 Regarding the choice of their smoothing parameters, the performance of the two HP detrending devices features a substantial robustness.

19 The samples have been chosen such that their distances d ( · ) are in a similar range.

20 It will also be supported by some observations that we can make in connection with the battery of Monte Carlo experiments below.

<!-- p:17 -->


Fig. 2 Distance d ( μ 1 ) , d ( μ 2 ) from HP1, HP2 for two sample runs from scenario DT-C2 and ST-C2, respectively. Note: Underlying the bold (blue) and thinner (red) lines on the left and on the right is the same cyclical component. The distance is minimized at the vertical dotted lines

As another result it comes as no great surprise that for both procedures HP1 and HP2 it is much harder to approximate the flexible stochastic trend than the segmented deterministic trend, as it is evidenced by the former's considerably higher distance statistics. Also, given the greater flexibility in the stochastic trend it makes sense that the optimal values of μ 1 and μ 2 tend be lower in this case than for the deterministic trend (see the vertical dotted lines). Nevertheless, more than this only casual information will have to be acquired on this issue.

Regarding a comparison of the performance of HP1 versus HP2, that one might be superior to the other, merely on the basis of the evidence in Fig. 2 one will not dare to formulate a general hypothesis.

For a more systematic investigation of the questions we have touched on it is thus time to turn to the experiments described at the beginning of this section. An overall picture is obtained by looking at the frequency distributions of the optimal parameters μ opt j ( b ) and the corresponding distances d ( μ opt j ( b )) ; j = 1 , 2 , b = 1 , . . . B = 1000 . Figure 3 does this for the two more important scenarios that combine the cyclical component C2 with a stochastic or deterministic trend. 21

Collecting the results, let us begin with HP2 and the question whether μ 2 ≈ 1 (i.e. λ ≈ 1600 for the ordinary HP filter) could be a suitable smoothing parameter. The answer is unequivocally in the negative, already visually. Numerically, across all scenarios and simulation runs, no μ 2 ≤ 3 was found that would minimize the distance. We may set this check off from the main text:

21 Regarding the lower-left panel, we have no convincing explanation for the kink in the distribution of

μ opt 2 ( b ) for DT-C2 at about μ 2 = 11 . 5 . It is perhaps more than accidental, because a similar phenomenon was found for DT-C1 and also in previous experiments with somewhat different artificial data.

<!-- p:18 -->


Fig. 3 Frequency distribution of the optimal smoothing parameters and their performance. Note: The vertical dotted lines in the left column (right column) indicate the median values  ̄ μ med 1 ,  ̄ μ med 2 of the distributions of the optimal parameters μ opt 1 ( b ) , μ opt 2 ( b ) (the medians of the corresponding distances d ( μ opt 1 ( b )) , d ( μ opt 2 ( b )) ); b = 1 , . . . 1000 . The dashed curves in the right column are the distributions d ( ̄ μ med 1 , b ) and d ( ̄ μ med 2 , b ) ,  respectively (the (blue) dashed line representing d ( ̄ μ med 2 , b ) for scenario DT-C2 in the lower-right panel is almost entirely covered by the bolder line representing d ( μ opt 2 ( b )) )

Remark 2 For HP2 and all of the artificial data series that we considered, the optimal parameters μ opt 2 are larger than and distinctly bounded away from unity.

What leaps to the eye in the diagram when generally comparing the distributions is a confirmation of the conjecture from Fig. 2, that suitable smoothing parameters tend to be lower for the stochastic trend than for the deterministic trend. Comparing, across  these  cases,  the  median  values  of  the  distributions  of μ opt 1 ( b ) and μ opt 2 ( b ) , respectively, Table 2 tells us that this does not only hold for scenario ST-C2 versus DT-C2 but also (though in weaker form) for ST-C1 versus DT-C1. Given the large number of the underlying simulation runs, these differences are highly significant. The following important message should therefore be kept in mind:

Remark 3 Before researchers planning to employ HP1 or HP2 for a particular value of μ 1 or μ 2 , they should make up their mind whether they tend to believe in a deterministic or rather a stochastic trend. That is, HP detrending is not a purely technical issue but requires a prior economic judgement, which may better be made explicit.

<!-- p:19 -->


Table 2 Smoothing parameters and their performance: statistics of the MC frequency distributions

|               |   μ opt 1 |   d ( μ opt 1 ) |   d ( ̄ μ med 1 ) |   d ( ̄ μ med 2 ) |   d ( μ opt 2 ) |   μ opt 2 |
|---------------|-----------|-----------------|------------------|------------------|-----------------|-----------|
| DT-C1: median |     0.881 |           19.56 |            20.09 |            21.52 |           21.40 |     12.24 |
| std           |     0.327 |            4.13 |             4.19 |             3.40 |            3.41 |      2.78 |
| DT-C2: median |     0.938 |           18.64 |            19.13 |            19.93 |           19.85 |     11.71 |
| std           |     0.221 |            3.48 |             3.46 |             2.88 |            2.91 |      2.31 |
| ST-C1: median |     0.707 |           29.59 |            30.36 |            30.14 |           29.76 |      8.95 |
| std           |     0.275 |            3.60 |             3.60 |             3.64 |            3.61 |      5.70 |
| ST-C2: median |     0.641 |           30.39 |            31.20 |            30.39 |           30.08 |      7.51 |
| std           |     0.222 |            3.63 |             3.64 |             3.56 |            3.53 |      4.91 |

Note: μ opt 1 and  all  distances d ( · ) are  multiplied  by  100,  'std'  reports  the  standard  deviation  of  the distributions. Boldface figures may be taken as benchmark values for believers in a deterministic or stochastic trend, respectively

In  greater  detail  we  can  observe  (and  confirm  by  the  corresponding  statistics) that the distributions of μ opt 1 ( b ) and μ opt 2 ( b ) are significantly skewed to the right. 22 Because mean values are sensitive to outliers, this is also the reason why for any scenario we only report the medians. The skewness could be explained by a certain tendency for the functions μ j ↦→ d ( μ j ) to be flatter for higher than for lower values of μ j ( j = 1 , 2 ).

The two panels in the right column of Fig. 3, the solid lines in which plot the distributions of the distances resulting from μ opt j ( b ) , make it unequivocally clear that, despite their optimality in each and every simulation run, the deterministic trend can be much better approximated than the stochastic trends. As it is already indicated by the small overlapping areas of DT-C2 and ST-C2, the medians of d ( μ opt j ( b )) are indeed significantly lower for the former scenario ( j = 1 , 2 ).

While Fig. 3 shows clear tendencies in the comparisons between the deterministic and  stochastic  trend  scenarios,  the  distributions  of μ opt j ( b ) and  the  corresponding distances d ( μ opt j ( b )) ( j = 1 , 2 )  exhibit a certain, nonnegligible dispersion. Table 2 expresses it quantitatively in terms of the standard deviations. Hence given the fact that in practical applications, where one is dealing with a specific time series, we do not know the best value of μ j , it is all the more urgent to ask for the implications if instead, by necessity, inferior values are chosen. Certainly, with respect to a given scenario, the most reasonable option if one has to decide on a specific parameter value would be to resort to the median values  ̄ μ med j := median { m opt j ( b ) } . 23 The dashed lines in the panels on the right-hand side of Fig. 3 plot the distributions of the thus resulting distances d ( ̄ μ med j , b ) and so give us an overall impression of how inferior this choice would be.

22 The standard error for skewness is solely a function of the sample size N , regardless of the values of the statistic themselves. Its variance is computed as: V = 6 N ( N - 1) / [( N - 2) ( N +1)( N +3)] .

23 We add a bar in order to emphasize that it is a fixed value.

Accordingly, the standard error s is approximately s ≈ √ 6 / 1000 = 0 . 077 , whereas the (by far) lowest skewness that we computed is 0.34 (for HP1 in scenario DT-C2).

<!-- p:20 -->


Comparing these distributions to those from the optimal values μ j , the deterioration appears to be rather limited. As a quantitative characterization by a single number, Table 2 also juxtaposes the median values of d ( ̄ μ med j , b ) and d ( μ opt j ( b )) . What is additionally seen in this way is that generally these differences are smaller for HP2 than for HP1. 24 For  the  application  of  HP2  in  scenario  DT-C2  in  the  lower-right panel of Fig. 3 ,  the deterioration by fixing the smoothing parameter at μ 2 =  ̄ μ med 2 is even negligible versus the optimal choice μ opt 2 ( b ) for each of the simulated time series. This is confirmed by a Wilcoxon-Mann-Whitney test, which yields a p -value far  above  the  5  per  cent  level  when  comparing  the  distributions  of d ( ̄ μ med 2 ) and d ( ̄ μ opt 2 ) . 25 It is also similarly high for HP2 and DT-C1.

On the other hand, for all other combinations of applying HP1, HP2 to DT, ST and C1, C2, the two distributions d ( ̄ μ med j , b ) and d ( μ opt j ( b )) , j = 1 , 2 ,  are  statistically told apart, though at possibly very different orders of magnitude (which, however, is a detailed issue that would lead us too far astray). Practically, however, this may not be rated too highly. So, for a general judgement, let us summarize (where the last sentence is based on observations like that mentioned in the presentation of Remark 1):

Remark 4 When in applied work with a given empirical time series, the best one can do is to resort to a fixed parameter like μ j =  ̄ μ med j , it can (but need not) be that the deterioration of d ( ̄ μ med j ) versus d ( μ opt j ) from an (unknown) optimal choice is statistical significant (this depends on which of the scenarios may approximately underly the series). That possibility should not, however, be overstated, since the resulting differences  in  the  corresponding  cyclical  components  are  typically  negligible  for most practical purposes. In other words, the conclusions drawn from a poorer (though informed) choice of μ j are unlikely to be seriously misleading.

Next, we may return to the question whether, on average, one of the two versions HP1 and HP2 may turn out to be superior to the other. If to this end we compare the medians of the distributions d ( ̄ μ med 1 , b ) and d ( ̄ μ med 2 , b ) ,  the  differences appear negligible.  Perhaps  somewhat  surprisingly,  bootstrapping  the  distribution  of  these medians, some of them can be statistically told apart (for DT-C1 and DT-C2, the median of d ( ̄ μ med 1 , b ) is significantly lower than that of d ( ̄ μ med 2 , b ) , whereas for STC2 it is the other way around). However, given the dispersion of the two distributions d ( ̄ μ med j , b ) , this seems a somewhat academic conclusion. So we may point out:

24 Tentatively, this regularity might be explained by the flatter shape of the functions μ 2 ↦→ d ( μ 2 ) that we meant to observe in Fig. 2.

25 It is p = 44 . 14 per cent, to be exact. The Wilcoxon-Mann-Whitney test, low p -values of which indicate that two distributions are significantly different, makes no parametric assumptions about them (more often the more general Kruskal-Wallis test is mentioned in this context). If the random events are identically distributed and the distributions have a similar shape and standard deviations, the p -value can be more specifically interpreted as testing for a difference between the medians of the distributions.

<!-- p:21 -->


Remark 5 None of the two detrending procedures HP1 and HP2 is systematically superior to the other. Hence a researcher may choose one of them on the ground of other considerations.

We can thus conclude with the main message of Table 2, which is a recommendation of suitable values for the smoothing parameters μ 1 or μ 2 . For the sake of brevity and because the cyclical component C1 may perhaps be considered to be too stylized, it only takes the more general component C2 into account.

Remark 6 If there are no other reasons, believers in a deterministic trend covering several growth regimes may settle for μ 1 ≈ 0 . 01 · 0 . 94 if  they  prefer  HP1,  or  for μ 2 ≈ 11 . 7 (i.e. λ = λ 2 = 11 . 7 · 1600 = 18720 )  if  they  prefer  HP2.  On  the  other hand, believers in a stochastic trend may choose μ 1 = 0 . 01 · 0 . 64 in the first case and μ 2 ≈ 7 . 5 (i.e. λ = λ 2 = 7 . 5 · 1600 = 12000 ) in the second.

When somewhat in doubt over these figures, a higher rather than a lower value may be chosen. This is motivated by the skewed distribution of the optimal μ 1 , μ 2 in Fig. 3 . Regarding HP2, additional confidence in high values of μ 2 might be gained from the experiments that we conducted on an estimation of Clark's ( 1987) Unobserved Components Model, which we already mentioned in Section 3 when justifying our non-standard approach to the generation of artificial data. For this process the optimal values of μ 2 were even considerably higher than the ones in Remark 6. The details are given in an Appendix.

The reason for our own interest in detrending is the resulting cyclical component and their main summary statistics, the standard deviation and the first four autocorre - lations-which the output gap of a small theoretical model should try to approximate. Intuitively, a good estimation of the trend should imply a good estimation of these empirical moments. Studying this issue in the extended version of this paper, a general downward bias was found. In all cases, however, it was less than 8 per cent. So it may be neglected, or the coefficients may be correspondingly corrected.

### 5  Conclusion

The paper reconsidered the widely employed Hodrick-Prescott filter and, with respect to quarterly data, put the common choice λ = 1600 for its smoothing parameter into question. Our interest originated with occasional remarks in the literature that this choice may tend to sweep too much of the cycle into the trend. We inquired into this issue by generating a battery of artificial data with a known trend and cyclical com - ponent, and checking how well different values of the smoothing parameters would be able to recover the true trend line.

Instead of considering rather general stochastic processes to produce the data, we constructed them with a view to the growth and business cycle characteristics of the real gross value added (GVA) in the US nonfinancial corporate business over the last 60 years. This means the trend exhibits positive but declining growth rates over this period, the fluctuations show a dominant cycle period of, on average, almost ten years in their spectrogram, and the main moments of the first differences of the growth series are required to come close to those of the empirical GVA. In addition, it proved relevant to distinguish between a deterministic (segmented linear) growth trend and a stochastic trend.

<!-- p:22 -->


As an alternative, or rather a complement, to the Hodrick-Prescott (HP) filter as it is known in economics, we furthermore offered a procedure known in geophysics and other scientific fields which, however, can also be viewed as a slight modification of HP. The specification details motivated us to denote it as HP1 and the original filter as HP2. The attractive feature of HP1 is the fact that it yields a segmented linear trend line with endogenous break points. This can be an easy way without presuppositions to identify different growth regimes. The number and dates of these points depend, nevertheless, on the tuning parameter of this procedure. Regarding the ability of the two filters to approximate the true trend, they turned out to be largely equivalent.

The upshot of the Monte Carlo experiments was a recommendation of suitable values of the smoothing parameters. Here it is, in particular, noteworthy that the one for HP2 is definitely several times higher than the familiar λ = 1600 .  It  was  also pointed out that deterioration in the trend estimates by suboptimal parameters are fairly limited, that is, the estimates are rather robust.

Regarding the generality of our results, it may not be disregarded that the smoothing parameters proposed by us are suitable for real GVA and time series (like GDP, consumption or investment) that behave similarly. We have, however, to be prepared that things might be different for variables that are not systematically growing over a longer time horizon, like unemployment rates, wage shares, or profit rates. In prin - ciple, one could address these cases in the same way as in our Monte Carlo study. In practice, however, most researchers will prefer to avoid that effort and instead apply a ready-made procedure. While we do not offer a panacea for this demand, we can at least sketch an approach that would substantially reduce the workload.

Concretely, with business cycle variables, one may begin with gaining an impression of different phases, or regimes, in their trend. Employing HP1 and trying a few values of its smoothing parameter should be good enough for this purpose. These explorations (or additional outside information) can also give an idea of a typical cycle period. In a second step, based on such a segmented linear trend and a researcher's view of the economy, a stylized deterministic or stochastic trend concept may be postulated, and subsequently a stochastic process for the cyclical component. The latter's specification may be the same or similar to our formulation for C1 or C2. Once such a data generation process is established, already three or four attempts (based on three or four different random seeds) to estimate the main moments of the first differences of the simulated series will be sufficient to decide on the numerical coefficients involved. In a third step, a few hundred time series can be sampled from the data generation process and for each one the optimal smoothing parameter be determined. This will be less effort than it might seem because Matlab, for example, is surprisingly fast in this respect. Finally one may choose the median of the collection of parameters thus obtained. Given the robustness of the approximations of the true trend that we observed on several occasions, there are good reasons to expect that such a result will be satisfactorily close to what a full-fledged simulation study would be able to offer us.


<!-- p:23 -->


### Appendix: Clark's Unobserved Components Model

In some personal discussions the high values of the optimal μ 2 in Table 2 were called into question. Suspected as responsible for this outcome were the segmented linear trend or perhaps also the only mildly randomly disturbed sine waves in our cyclical component. To check these doubts we ran our experiments on additional artificial data that were generated by a more standard and commonly accepted time series process. To this end we made convenient use of Clark's ( 1987) unobserved components model as it was already estimated by Hodrick (2020, Section 4). The model postulates that GDP is the sum of a stochastic trend y ⋆ t and a stochastic cycle c t , where the change in the trend is modelled with a slowly time-varying conditional mean d t - 1 and a homoskedastic innovation. With the overall three innovations following the standard normal and being mutually uncorrelated, the two components were estimated as follows (the time unit being a quarter here):

```
\Delta y _ { t } ^ { * } & = d _ { t - 1 } \, + \, 0 . 5 4 5 \, \varepsilon _ { y , t } , \\ d _ { t } & = d _ { t - 1 } \, + \, 0 . 0 2 1 \, \varepsilon _ { d , t } , \\ c _ { t } & = 1 . 5 1 0 \, c _ { t - 1 } \, - \, 0 . 5 6 5 \, c _ { t - 2 } \, + \, 0 . 6 0 3 \, \varepsilon _ { c , t } .
```

Again we simulated 1000 samples of this process over the same time horizon as in our other experiments.

The different cyclical pattern of c t compared to our sine waves was already illustrated in Fig. 1 . It is also obvious that Clark's trend is much more variable than, in particular, our deterministic trend line. The expectation, however, that these features would lead to considerably lower values of μ 2 proves wrong. A juxtaposition of the statistics of HP2 for DT-C2 from above and for Clark's model in Table 3 shows quite the contrary.

It  may especially be noted that the dispersion of the optimal μ 2 across the different realizations of Clark's process is extremely wide. This is due to the fact that typically the difference in the distance d ( · ) between, say, μ 2 = 10 and μ 2 = 15 is larger than the distance between μ 2 = 100 and μ 2 = 150 . Considering the optimal distances numerically it is seen that the higher irregularity in Clark's model makes it also much harder for HP2 to recover the true trend. Incidentally, in equal measure this is true for HP1).


<!-- p:24 -->


Table 3 Optimal smoothing parameters μ 2 for Clark's ( 1987) unobserved component model

|              |   μ opt 2 |   100 × d ( μ opt 2 ) |
|--------------|-----------|-----------------------|
| DT-C2:       |           |                       |
| median       |     11.71 |                 19.85 |
| std.dev.     |      2.31 |                  2.91 |
| Clark's UCM: |           |                       |
| median       |     34.56 |                 63.25 |
| std.dev.     |    217.37 |                 10.26 |

We can thus summarize that, if anything, Table 3 is only further evidence that for quarterly business cycle data Hodrick-Prescott's smoothing parameter λ 2 = 1600 is too low.

Author Contributions All authors contributed to the study conception and design. Material preparation, data collection and analysis were performed by Reiner Franke, Jiri Kukacka and Stephen Sacht. The first draft of the manuscript was written by Reiner Franke and all authors commented on previous versions of the manuscript. All authors read and approved the final manuscript.

Funding Open access publishing supported by the institutions participating in the CzechELib Transformative Agreement. This work was supported by the Czech Science Foundation under the project 'Linking financial and economic agent-based models: An econometric approach' [grant number 20-14817S]; Charles  University  UNCE  program  [grant  number  UNCE/HUM/035];  Cooperatio  Program  at  Charles University, research area Economics.

##### Declarations

Competing interests The authors have no relevant financial or non-financial interests to disclose.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as  you  give  appropriate  credit  to  the  original  author(s)  and  the  source,  provide  a  link  to  the  Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n s e s / b y / 4 . 0 / .
