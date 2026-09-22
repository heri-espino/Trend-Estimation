---
id: "32_Band_Pass_Filter"
source_pdf: "../pdf/32_Band_Pass_Filter.pdf"
source_filename: "32_Band_Pass_Filter.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/32_Band_Pass_Filter.references.md"
---

<!-- p:1 -->

### NBER WORKING PAPER SERIES

### THE BAND PASS FILTER

Lawrence J. Christiano Terry J. Fitzgerald

Working Paper 7257 http://www.nber.org/papers/w7257

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138

Jy 9

We thank Jeff Schwarz for his outstanding research assistance. Christiano is grateful for a National Science Foundation Grant to the National Bureau of Economic Research. The views expressed herein are those of the authors and not necessarily those of the Federal Reserve Bank of Cleveland, the Federal Reserve System, or the National Bureau of Economic Research. -

© 1999 by Lawrence J. Christiano and Terry J. Fitzgerald. All rights reserved. Short sections of text, not xie iit et t d rsd  it   r 'se t e t notice, is given to the source.


<!-- p:2 -->


The Band Pass Filter Lawrence J. Christiano and Terry J. Fitzgerald NBER Working Paper No. 7257 ry 9 JEL No. E3, C1, C2, C22

### ABSTRACT

The 'ideal' band pass filter can be used to isolate the component of a time series that lies within a particular band of frequencies. However, applying this filter requires a dataset of infinite length. In practice, some sort of approximation is needed. Using projections, we derive approximations that are optimal when the time series representations underlying the raw data have a unit root, or are stationary about a trend. We identify one approximation which, though it is only optimal for one particular time series representation, nevertheless works well for standard macroeconomic time series.

To illustrate the use of this approximation, we use it to characterize the change in the nature of the Phillips curve and the money-inflation relation before and after the 1960s. We find that there is surprisingly little change in the Phillips curve and substantial change in money growth-inflation relation.

| Lawrence J. Christiano Department of Economics Northwestern University 2003 Sheridan Road Evanston, IL 60628-2600 and NBER lchrist@meiie.acns.nwu.edu   | Teriy Fitzgerald Research Department Federal Reserve Bank of Cleveland P0 Box 6387 Cleveland, OH 44101 tj.fitzgerald®clev.frb.org   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|


<!-- p:3 -->


## 1. Introduction

Economists have long been interested in the different frequency components of the data. For example, business cycle theory is primarily concerned with understanding fluctuations in the range of 1.5 to 8 years while growth theory focuses on the longer run components of the data. In addition, some economic hypotheses are naturally formulated in the frequency domain, such as Milton Friedman's h         t negatively sloped, and the proposition that money growth and inflation are highly correlated in the long run, and less correlated in the short run. As a final example, certain frequency components of the data are important as inputs into macroeconomic stabilization policy. For instance, a policy maker who observes a recent change in output is interested in knowing whether that change is part of a trend (i.e., part of the lower frequency component of the data) or is more transitory (i.e., part of the higher frequency component).

The theory of the spectral analysis of time series provides a rigorous foundation for the notion that there are different frequency components of the data. An advantage of this theory: relative to other perspectives on decomposing time series, is that it does not require a commitment to any particular statistical model of the data. Instead, it relies on the Spectral Representation Theorem, according to which any time series within a broad class can be decomposed into different frequency components. The theory also supplies a tool for extracting those components. That tool is the ideal band pass filter. It is a linear transformation of the data, which leaves intact the components of the data within a specified band of frequencies and eliminates all other components. The adjective, ideal, on this filter reflects an important practical limitation. Literally, application of the ideal band pass filter requires an infinite amount of data. Some sort of approximation is required.

In this paper, we characterize and study optimal linear approximations, assess alternative approaches developed in the literature and provide empirical illustrations. To explain what we mean by an optimal linear approximation, let yt denote the data generated by applying the ideal, though infeasible, band pass filter to the raw data, x. We approximate yt by Ît, a linear function, or filter, of the observed sample πe's. We select the fiter weights to make Ît as close as possible to the object of interest, , in the sense of minimizing the mean square error criterion:

$$E \left [ ( y _ { t } - \hat { y } ) ^ { 2 } | x \right ] , \, x \equiv \{ x _ { 1 } , \dots , x _ { T } \} ,$$

where the expectation operator is evaluated using the time series properties of x. Thus, Ît is the linear projection of y onto every element in the data set, x, and there is a different projection problem for each date t. We derive closed form formulas for the filter weights in these projections.


<!-- p:4 -->


We illustrate the use of ét in two empirical applications: one concerns the relationship between inflation and unemploymnent and the other, the relationship between money growth and inflation. We use the filtering technology developed here to characterize the change in the dynamics of these variables before and after 1960. A bootstrap procedure is applied for conducting the relevant statistical inference.

The optimal approximation to the band pass filter requires knowing the true time series representation of x. In practice, this is not known and must be estimated. It turns out, however, that for standard macroeconomic time series, a more straightforward approach that does not involve first estimating a time series model works well. That approach uses the approximation that is optimal under the (most likely, false) assumption that the data are generated by a pure random walk.1 The procedure is nearly optimal for the type of time series representations that fit US data on interest rates, unemployment, inflation, and output. The filter is easy to implement, and is described as follows. To isolate the component of x, with period of oscillation between pl and pu, where 2 ≤ pl &lt; Pu &lt; ∞, our recommended approximation of yt, Ît, is computed as follows:2

$$\hat { y } _ { t } & = B _ { 0 } x _ { t } + B _ { 1 } x _ { t + 1 } + \dots + B _ { T - 1 - t } x _ { T - 1 } + \bar { B } _ { T - t } x _ { T } \\ & + B _ { 1 } x _ { t - 1 } + \dots + B _ { t - 2 } x _ { 2 } + \tilde { B } _ { t - 1 } x _ { 1 } ,$$

for t = 3, 4, .., T − 2. In (1.2),

Also, B-1 solves

$$\begin{array} { r l } { \quad } & { B _ { j } = \frac { \sin ( j b ) - \sin ( j a ) } { \pi j } , \, j \geq 1 } \\ & { B _ { 0 } = \frac { b - a } { \pi } , \, a = \frac { 2 \pi } { p _ { u } } , \, b = \frac { 2 \pi } { p _ { u } } . } \end{array}$$

and BT-t, Bt-1 are simple linear functions of the Bj's.3 The formulas for Ît when t = 2 and T – 1 are straightforward adaptations on the above expressions. The formulas for ý1 and iT are also of interest.

'Our formulas assume there is no drift in the random walk. If there is a drift in the raw data, we assume it has been removed prior to analysis. For more details, see footnote 5 below.

3In particular, BT-t is the sum of the By's over j = T−t, T −t + 1, .. and Be−1 is the sum of the Bj's over j = t − 1. t, .. . Exploiting the fact that Bo + 2 ∑i, B; = 0,

2If the data are quarterly and pt = 6, pu = 32, then y. is the component of r, with periodicities between 1.5 and 8 years.

$$\tilde { B } _ { T - 1 } = - \frac { 1 } { 2 } B _ { 0 } - \sum _ { j = 1 } ^ { T - 1 } B _ { j } , \text { for } t = 3 , \dots , T - 2$$

0 = B0 + B1 + ... + BT-1-t + BT-t + B1 + ... + Bt-2 + B.


<!-- p:5 -->


For r example, For example,

$$\dot { y } _ { T } = \left ( \frac { 1 } { 2 } B _ { 0 } \right ) x _ { T } + B _ { 1 } x _ { T - 1 } + \dots + B _ { T - 2 } x _ { 2 } + \tilde { B } _ { T - 1 } x _ { 1 } , \quad u \quad$$

where BT-1 is constructed using the analog of the formulas underlying the Bj's in (1.2). The expression for îr is useful in circumstances when an estimate of yr is required in real time, in which case only a one-sided filter is feasible. As we discuss below, the need for real time estimates of yt arises in a macroeconomic stabilization context.

Note from (1.2) that our recommended filter varies with time, and is not symmetric in terms of future and past xt's. It is easy to adjust our recommended filter weights to impose stationarity and symmetry, if these features were deemed to be absolutely necessary. Simply construct (1.2) so that it is a function of a fixed number, p, of leads and lags of x and compute the weights on the highest lead and lag using simple functions of the Bj's.5 This is the solution to our projection problem when xt is a random walk, and t is restricted to be a linear function of {xt, t±1, ..., t±p} only. With this approach, it is not possible to estimate yt for the first and last p observations in the data set. In practice, this means restricting p to be relatively small, to say three years of data. This filter renders stationary time series which have up to two unit roots, or which have a polynomial trend up to the power of two.

It is important to emphasize a caveat regarding our recommended filter, (1.2)-(1.3). That filter does not closely approximate the optimal filter in all circumstances. To illustrate this, we display an example in which the first difference of the data displays substantial negative autocorrelation, and our recommended filter does not work well. For cases in which the appropriateness of our recommended filter is questionable, it makes sense to estimate the time series representation of the data to be filtered, and then compute, using the formulas we provide, the optimal filter based on the estimated time series representation.6 Our formulas work for a fairly large class of time series models. Still, the class can be extended even further by applying the kind of algebraic manipulations we do in the appendix.

The outline of the paper is as follows. In section two we describe precisely the component of the

Bj.

sThe weights on , t±,., ±(p-1) are B, .., Bp-1, respectively. The weight on t-p and +p, p, is obtained using

$$\bar { B } _ { p } = - \frac { 1 } { 2 } \left [ B _ { 0 } + 2 \sum _ { j = 1 } ^ { p - 1 } B _ { j } \right ] .$$

It is easy to verify that in this case there is no need to drift-adjust the raw data because the output of the formula is invariant to drift. The reason is that the optimal symmetric filter when the raw data are a random walk has two unit roots. The first makes x: stationary and the second eliminates any drift. In contrast, the output of the potentially asymmetric filter just discussed in the text is not invarient to drift. When p ≠ f. that filter has just one unit root.

Software for computing the filters in MATLAB is available from the authors on request. The default option in this software takes as input a raw time series, removes its drift, and then filters it using our recommended random walk flter. Alternatively, any other formula in this paper can also be implemented simply by overriding the default.


<!-- p:6 -->


data we seek to identify. We then discuss how we estimate it in a finite data set. Section 3 does a quantitative evaluation of alternative approaches to this estimation problem. Section 4 relates our analysis to the relevant literature. We stress in particular, the important papers by Baxter and King (1999) and Hodrick and Prescott (1997). Section 5 presents two empirical applications to illustrate the use of the filtering technology analyzed here. These examples complement the ones presented in Baxter (1994), Baxter and King (1999), Hornstein (1998), King and Watson (1994), King, Stock and Watson (1995), and Stock and Watson (1998). Section 6 concludes.

## 2. The Problem and Its Solution

Ou analysis accommodates two types of xt processes. In one, xt has a zero mean, and is covariance stationary. If the raw data have a non-zero mean, we assume it has been removed prior to analysis. If the raw data are covariance stationary about a trend, then we assume that trend has been removed. We also consider the unit root case, in which xt - xt-1 is a zero mean, covariance stationary process. If in the raw data this mean is non-zero, then we suppose that it has been removed prior to analysis.7 As we will see, the latter is actually only necessary when we consider asymmetric filters. Any' sampling uncertainty in the parameters needed obtain xt from the raw data is ignored in our analysis.

We begin this section by defining precisely the object that we seek: the component of x, that lies in a particular frequency range. We then explain why this is difficult to compute directly in a finite data set and that some sort of approximation is necessary. We describe a method for obtaining an optimal approximation. Several examples are presented which convey the intuition about the formulas we develop to implement this.

### 2.1. The Ideal Band Pass Filter

Consider the following orthogonal decomposition of the stochastic process, t:

$$x _ { t } = y _ { t } + \bar { x } _ { t } .$$

Removing this mean corresponds to 'drift adjusting' the x, process. We elaborate on this briefly here. Suppose the raw data are denoted w, and they have the representation, w. = μ + ut-1 + u, where u, is a zero mean, covariance stationary process. Then, wt can equivalently be expressed as w, = (t − j)μ + xt, where xt = xt-1 + ut for all t and j is a fixed integer, which we normalize to unity for concreteness. The variable, x, is the 'drift-adjusted' version of wt, and can be recovered from observations on w, as follows: x1 = w1, x2 = w2- μ, x3 = w3 - 2μ, ... . In practice, μ must. be estimated, with  = (wr - w1)/(T – 1). Though we set j = 1, it is readily confirmed that the output of our filter is invariant to the value of j chosen. In sum, in the unit root case, we assume z. is the result of removing a trend line from the raw data, where the slope of the line is the drift in the raw data and the level is arbitrary.


<!-- p:7 -->


The process, yt, has power only in frequencies belonging to the interval {(a, b) U (−b, −a)} ∈ (−π, π). The process, t, has power only in the complement of this interval in (−π, π). Here, 0 &lt; a ≤ b ≤ π. It is well known (see, for example, Sargent (1987, p. 259)), that,

$$y _ { t } = B ( D ) x _ { t } , & & \quad ^ { t } ( 2 . 2 )$$

where the ideal band pass filter, B(L), has the following structure:

$$B ( L ) = \sum _ { j = - \infty } ^ { \infty } B _ { j } L ^ { j } , \, L ^ { t } x _ { t } \equiv x _ { t - l } ,$$

where the Bj's are given by (1.3). With this specification of the Bj's, we have

$$u & = B ( e ^ { - i w } ) \ = u , \text { for } w \in ( a , b ) \cup ( - b , - a ) \quad u \\ & = \ 0 , \text { otherwise.}$$

Our assumption, a &gt; 0, implies, together with (2.3), that B(1) = 0. Note from (2.2) that to compute yt using B(L) requires an infinite number of observations on x.8 Moreover, it is not clear that simply truncating the Bj's will produce good results.

This can be seen in two ways. First, consider Figure 1a, which displays Bj for j = 0, ..., 200, when a = 2π/96 and b = 2π/18. These frequencies, in monthly data, correspond to the business cycle, e.g., t   t    e   e Even after j = 120, i.e., 10 years, the Bj's remain noticeably different from zero. Second, Figures 1b - 1d show that truncation has a substantial impact on B(e-iw). They display the Fourier transform of filter coefficients obtained by truncating the Bj's for j &gt; p and j &lt; −p for p = 12, 24, 36 (i.e., 1 to 3

sAs already noted, we want to consider not just cases in which r. is covariance stationary, but also cases in which it has a unit root. In the unit root case, the covariance function and hence, the spectral density of rt, are not well defined. This creates a problem of how to interpret the notion that (2.1) represents an orthogonal decomposition. We do so as follows. Let z.(λ) for |λ| &lt; 1 be a covariance stationary stochastic process in which the unit root of x, is replaced by λ. Denote the spectral density of this process, which is well defined, by fs.(ω). Then, (see Sargent (1987, p. 268)) the cross-spectrum between yt and i, 9y.s(ω; λ), is

$$g _ { n , 1 } ( \omega _ { n } , \lambda ) = B ( e ^ { - i \omega _ { n } } ) \left [ 1 - B ( e ^ { i \omega _ { n } } ) \right ] f _ { n , 1 } ( \omega _ { n } ) , \, | \lambda | < 1 .$$

By the definition of B (see (2.3)), this cross spectrum is zero for all ω, for each λ. Since the covariance between y and i at any lag is just the suitably weighted integral of this spectrum, it follows that èr and i, are uncorrelated at all leads and lags, for each λ. In the unit root case, our interpretation of (2.1) as an orthogonal decomposition reflects that we define

5.

for all ω ∈ (−π, π).

$$g _ { r } ( \omega ; 1 ) = \lim _ { \lambda \to 4 } g _ { r ^ { \lambda } } ( \omega _ { r } , \lambda ) = 0 ,$$


<!-- p:8 -->


years).9 These differ noticeably from B(e-iw).

### 2.2. Optimal Approximations

Suppose we have a finite set of observations, x = [x1, ..., xτ] and that we know the population second moment properties of {xt}. Our estimate of y = {y1 ..., yτ] is ý, the projection of y onto the available data:

$$\dot { y } = P \left [ y | x \right ] .$$

This corresponds to the following set of projection problems:

$$\hat { y } _ { t } = P [ y _ { t } | x ] , \, t = 1 , \dots , T .$$

For each t, the solution to the projection problem is a linear function of the available data:

$$\hat { y } = \sum _ { j = - f } ^ { p } \hat { B } _ { j } ^ { p , f } x _ { t - j } ,$$

where f = T - t and p = t - 1, and the Bps's solve

$$\min _ { \hat { B } _ { j } ^ { \prime } \cdot j = - f _ { \dots , \mathcal { P } } } E \left [ ( y _ { t } - \hat { y } _ { t } ) ^ { 2 } | x | \right ] .$$

Presumably, the solution to this problem would be different if instead of having the true second moment properties of {xt}, we had to rely on sample estimates. Studying the solution to (2.6) in this latter case is beyond the scope of this paper. In any case, we report results below which suggest that in practice, reasonable approximations to the solution can be obtained without knowing the details of the time series representation of rt.

To discuss the solution to (2.6), it is useful to first define the following filter:

$$\hat { B } ^ { p , f } ( L ) = \sum _ { j = - f } ^ { p } \hat { B } _ { j } ^ { p , f } L ^ { j } , \, L ^ { h } x _ { t } \equiv x _ { t - h } .$$

The strategy for estimating y1, y2, ..,yr described above in effect uses a different filter for each t. The filters differ according to the values of p and f: which vary with t.

Alternative strategies for estimating the yt's impose various restrictions. For example, one might impose stationarity, i.e., constancy of p and f, and/or symmetry, i.e., p = f, on the sequence of projection problems defined above. A feature of these alternatives is that they do not use all the available observations on t to estimate the yt's. There may be advantages to restricting one's attention to stationary and/or symmetric filters. For example, stationarity may have econometric advantages. Symmetry has the advantage of ensuring that there is no phase shift between it and yt.1o Thus, there at t    s s    bos  bt  t t hg sense of (2.6). One of our objectives is to quantify the severity of this trade-off in settings that are of practical interest.

The figure reports Bo + 2 ∑j= Bj cos(wj) for various values of p.


<!-- p:9 -->


For given t, we can obtain a closed form solution to the projection problem, (2.4), by formulating it in the frequency domain:

$$\min _ { \dot { B } _ { f } ^ { p , f } ( j = - f _ { r } , \dots , p ) } \int _ { - \infty } ^ { \infty } | B ( e ^ { - i \omega } ) - \dot { B } ^ { p , f } ( e ^ { - i \omega } ) | ^ { 2 } f _ { x } ( \omega ) d \omega , \quad n o t h s c r { U }$$

where fx(ω) is the spectral density of x.11 This formulation of the problem emphasizes that the solution to the projection problem, (2.4), depends on the time series properties of the data being filtered. This is true, despite the fact that the ideal band pass filter is not dependent on the time series properties of the data.

### 2.3. Time Series Representations

We consider the following class of time series representations for t:

$$x _ { t } = x _ { t - 1 } + \theta ( L ) \varepsilon _ { t } , \ E \varepsilon _ { t } ^ { 2 } = 1 , \quad \, \quad ,$$

$$\Omega _ { 0 } = \frac { \Omega _ { 0 } } { \Omega _ { 1 } } ( \omega ) = \frac { \theta ( e ^ { - i \omega } ) \theta ( e ^ { i \omega } ) } { ( 1 - e ^ { - i \omega } ) ( 1 - e ^ { i \omega } ) } .$$

so that so that

10This observation follows from standard results. The phase-shift between ýt and y: is determined by the phase of the z-transform of the cross-covariance function between Ît and yt, 9sv(z). This is given by:

$$g _ { n } ( z ) = \hat { B } ^ { p , l } ( z ) B ( z ^ { - 1 } ) f _ { s } ( z ) ,$$

where f≠(z) is the z-transform of the covariance function of the data being filtered. The phase in gey(e-) is related to the complex part of giy(e-). Given that B(e-) and fs(e-) are real, this is zero if, and only if, p.s(e-) is real. But, this is equivalent to the requirement, .(e-) = .(e), i.e., that . = .!.

1This formula corresponds to one derived under similar circumstances by Sims (1972). Sims (1972) posits a situation in which some variable, yt, is related to z. by a distributed lag, yt = B(L)x, + εt, while the econometrician imposes that the lag structure has the form, ./(L). He assumes that the restrictions imposed by the econometrician on .(L) exclude the true distributed lag, B(L). Sims showed that, in population, the econometrician's estimate of J(L), obtained by a least squares regression of yt on x,'s, solves (2.7).


<!-- p:10 -->


We place a simple structure on θ(L), by assuming it is a finite-ordered polynomial12:

$$\theta ( z ) = \theta _ { 0 } + \theta _ { 1 } z + \dots + \theta _ { q } z ^ { q } , \ q \geq 0 .$$

We suppose that p and f are large by comparison with q.13 Specifically,

$$p \geq 0 , \ f \geq 0 , \ p + f > 0 , \ p + f \geq 2 q .$$

Define Demne

$$g ( z ) = \theta ( z ) \theta ( z ^ { - 1 } ) = c _ { 0 } + c _ { 1 } ( z + z ^ { - 1 } ) + \dots + c _ { q } ( z ^ { q } + z ^ { - q } ) ,$$

with c−r = cr for all τ, and cr = 0 for τ &gt; q.

The case where x is difference stationary corrcsponds to θ(1) ≠ 0. The covariance stationary case corresponds to θ(1) = 0, when the time series representation of xt is x, = [θ(L)/(1 − L)] εt = ē(L)εt. where (L) is a finite-ordered polynomial in L.

Formulas for the solution to (2.7) when xt has the time series representation, (2.8), are derived in Appendix A. The solution when x, is a random walk (i.e., θ(L) ≡ 1) was presented in the introduction.14 Other special cases are discussed in the next subsection.

### 2.4. The Optimal Approximation and fz

The key to understanding the solution to (2.7) is to note that for finite p and f, it is not possible to construct p.f(e-iω) so that p.f(e−) = B(e-ω) for all ω. The two functions can be made close over some subintervals, but only at the cost of sacrificing accuracy over other subintervals. The existence of this trade-off implies that some weighting scheme is needed to determine which intervals to emphasize in constructing p,s(e-). The weighting scheme implicit in our optimization criterion is the spectral density of x. The reason for this is that the optimization problem seeks to make yt and Ît as close as possible, and this translates into making the product of B and fx similar to the product of ps and fr. Thus, the optimization criterion picks the Bp.f's so that P.f(e-i) resembles B(e-) closely for values of ω where fr() is large and places less emphasis on regions where fz is relatively small. We illustrate this principle using four examples. The four examples tilt the graph of fr(ω), ω ∈ (0, π) in various ways and the effects on the Bp.f's are displayed.

intensive, extension of what we do here. Our analysis suggests that the extension to the rational polynomial case may not be necessary to achieve good results in practice.

IThe random walk case is simple, and can be established with the following time-domain argument. The problem is that not all the observations on xt are available to evaluate yt in (2.2). The missing data are the x's after the end of the data set and before the beginning. We can use the assumed time series model for x, to forecast and backcast these missing observations based on the actual data. We obtain ý. by incorporating the actual data and the estimates for the missing observations into the formula for y. In the random walk case, the formulas for the missing observations are particularly simple: for j &lt; t − T, P[zt-j|x1....,xτ] = xT and for j &gt; t − 1, P[x-,[x1, .., τ] = x1. With these observations, it is easy to verify (1.2)-(1.4), where Bτ-t is the sum of the Bj's over all j ≥ T − t and B-1 is the sum of the B,'s over all j ≥ t – 1. This time domain strategy for solving our problem follows the one implement by Stock and Watson (1998) in a business cycle context and by Geweke (1978) and Wallis (1981) in a seasonal adjustment context.

13This is only imposed to simplify the projection formulas in the Appendix. The requirement could be dropped by a suitable extension of the formulas derived there.


<!-- p:11 -->


In what we call the 'IID case', θ(z) = 1−z, so that fr(ω) = 1 for all ω. In this case, the optimization criterion assigns equal weight to all frequencies. In the appendix, it is shown that the Pf's that solve (2.7) in this case are given by:

$$I I D \, \text {case} \colon \, \tilde { B } _ { j } ^ { p . f } = B _ { j } , \, \text {for} \, j = - f , - f + 1 , \dots , 0 , \dots , p .$$

For p = f = 12, pu = 24, pt = 4 (see (1.3)), p.s(e−) and B(e−ω) are displayed in Figure 2a.15

In our other three examples, x, has a single unit root. That (2.12) is not the solution to (2.7) in this case can be seen using a simple argument by contradiction. Thus, suppose (2.12) is the solution to (2.7) in the unit root case. Since B(1) = 0, it follows that yt is covariance stationary. But, since most likely p.f(1) ≠ 0, Ît will not be covariance stationary.16 This implies that Ît and, hence, yt - Ît: has infinite variance. This variance can be made finite by just altering the filter weights so that P.f(1) = 0. This is a contradiction to the assumption that the filter weights solve (2.7).

The preceding considerations suggest that a necessary condition for p.f(L) to solve (2.7) when xt has a unit root is that p.f(1) = 0. We impose this in the formulas derived in the appendix.

To illustrate these formulas, we analyze the following additional exampleș. The case where xt is a random walk is discussed in the introduction. In the 'Near IID case',

$$\Omega _ { 0 } = \theta ( z ) = 1 - ( 1 - \eta ) z , \ \eta > 0 , \ \eta \text { small} .$$

1sThat (2.12) is the solution to (2.7) in the IID case can be verified trivially using the time domain strategy in footnote 12. The frequency domain strategy is also straightforward in this case. The first order condition of (2.7) associated with the optimal choice of p. is

$$\int \lim i t s _ { - \infty } B ( e ^ { - \omega } ) e ^ { - \omega j } d \omega = \int \lim i t s _ { - \infty } \dot { B } ^ { j , j } ( e ^ { - \omega } ) e ^ { - \omega j } d \omega , \\$$

for j = -f, -f + 1, .., 0, ..., p. Equation (2.12) follows by evaluating these integrals using the well known fact

$$\int \lim i t s _ { - \infty } ^ { \infty } e ^ { - \log \omega } d \omega = \left \{ \begin{array} { l l } { 2 \pi , \, h = 0 } \\ { 0 , \, h \neq 0 } \end{array} .$$

ee  '  t t   f e d   e s e e sd     e e BP.S's are constructed as in (2.12).


<!-- p:12 -->


Note that if η = 0, then this reduces to the IID case just discussed. However, with η positive, no matter how small, fz(ω) diverges to infinity for ω → 0. Outside of a small region around ω = 0, the spectrum of x, in the Near IID case looks like the one in the IID case: constant at unity. In this case, the solution to (2.7), for p = f, is

$$\text {Near IID base} \colon \hat { B } _ { j } ^ { p , f } = B _ { j } + \frac { \Delta } { 1 + 2 p } , \, j = 0 , \pm 1 , \dots , \pm p ,$$

$$\Delta = - \left [ B _ { 0 } + 2 \sum _ { j = 1 } ^ { P } B _ { j } \right ] ,$$

where where

and the Bj's are defined in (1.3).17 In this case, it is optimal to truncate the ideal band pass filter and then adjust all the weights by a constant to ensure psf(1) = 0. This differs from the Random Walk case discussed in the introduction. In the latter, optimality dictates truncating the ideal band pass filter, and then only adjusting the highest order terms to ensure p.f(1) = 0.

Figure 2 allows us to assess the impact on the optimal filter approximations of the three specifications of fz already described and of the fourth one that will be described shortly. We begin by comparing B12,12(e-) in the Near IID and IID cases (see Figures 2a and 2b). We can think of the Near IID case as adapting B12,12(e-i) from the IID case by shifting it up towards zero in the neighborhood of ω = 0. This improvement is achieved at the cost of making 12,12(e-i) diverge from B(e-iω) for values of ω slightly above zero. In the IID case, when fz(ω) = 1 for all ω, this cost outweighs the improvement. In the Near IID case, when f(0) = ∞, the situation is reversed. For fes  oe  se t    (t    e i eos that shifting power towards one frequéncy range causes the optimal filter to become more accurate in the re e ne   e  e tge.

a (   s ar   C    (t   e spectrum of xt in the Random Walk case resembles the one in the Near IID case in that it diverges to infinity for ω → 0. However, it declines more slowly as ω increases above zero.18 As a result,

17Verifying this is only a little more complicated than the problem of verifying (2.12), discussed in footnote 12. Consider unsurprising feature of the p = f case, and is established rigorously in Appendix A.) The p + 1 unknown p.s's may be found by solving the condition, p.f(1) = 0, and the p first order conditions associated with (2.7): the case, p = so that the solution to (2.7) is symmetric with B"1 = for p (this symmetry property is an

$$\int _ { - \tau } ^ { \tau } B ( e ^ { - \omega } ) e ^ { - \omega j } f _ { s } ( \omega ) d \omega = \int _ { \tau } ^ { \tau } \dot { B } ^ { p . f } ( e ^ { - \omega } ) e ^ { - \omega j } f _ { s } ( \omega ) d \omega ,$$

for j = 0,..., p – 1. That these indeed are the first order conditions can be verified with some algebra, but in any case is established carefully in Appendix A. It is easily verified that the ÀP.'s in (2.14) satisfy these conditions.

18In the random walk case, fz(ω) = 1/ [2(1 − cos(ω))|.


<!-- p:13 -->


by comparison with the IID case, the Random Walk case assigns relatively heavy weight to the low frequencies and relatively low weight to the others. The effects on the optimal filter are evident in Figure 2b: the Random Walk case does better than the Near IID case in the region of ω = 0, but at the cost of performing relatively poorly at the higher frequencies.

A final case, the Persistent case, is studied in Figure 2c. There,

$$\theta ( z ) = 1 + z + \dots + z ^ { 1 3 } .$$

Taking the Random Walk case as a benchmark, this case goes to the opposite extreme relative to the Near IID case. The Persistent case tilts power in xt even more towards frequency zero and away from the higher frequencies. It almost corresponds to the case in which it is not the first difference, but the second difference of xt, that is a white noise. We compare B12,12(e-) for these two cases in Figure 2c. Note how 12,12(e-iw) for the Persistent case does better in a neighborhood of ω = 0 than the Random Walk case. This is achieved in exchange for a very pronounced deterioration in performance in the higher frequencies.

## 3. Quantitative Assessment of Various Filters

A key purpose of this section is to explore the quantitative importance of three factors in the solution to (2.7). We examine the role of asymmetry and time nonstationarity of the p.S's. We also assess the importance of knowing the details of the time series representation of x. Clearly, the importance of these three factors depends on the actual time series properties of x. To make the analysis interesting, we use difference stationary and trend stationary time series representations that fit standard US macroeconomic data.

Our findings are as follows. First, in minimizing (1.1), the biggest gains come from allowing the filter weights to vary over time. These gains refiect that allowing nonstationarity substantially increases the amount of information in r that can be used in estimating Ît. Second, allowing the filter weights to be asymmetric further increases the amount of information in x that can be used in constructing èt, though by a lesser amount. So, we find that nonstationarity and asymmetry are valuable in minimizing the distance metric. It turns out that the cost of these features is relatively minor. We display evidence that the degree of asymmetry and nonstationary in the optimally filtered data is quantitatively small.19 Finally, we find that there is relatively little gain in knowing the precise details of the time series representation generating the xt's. In particular, the gain from using the true time series representation of xt to compute Ît rather than proceeding as though xt is a random walk, is minimal in practice. These are the findings that lead us to the view that an adequate, though not optimal, procedure for isolating frequency bands in macroeconomic time series is to proceed as if the data were a random walk and use filters that are optimal in that case.

19This is similar to results obtained for the Hodrick-Prescott filter, which is also nonstationary and asymmetric. Christiano and den Haan (1996) show that, apart from data at the very beginning and end of the data set, the degree of


<!-- p:14 -->


The second purpose of this section is to evaluate other filtering approaches used in the literature. These include the band-pass filtering approach recommended by Baxter and King (1999) and the filter proposed by Hodrick and Prescott (1997) (HP). In addition, we consider the band-pass approximation based on regressing data on sine and cosine functions, as described in Christiano and Fitzgerald (1998, Appendix) and Hamilton (1994, pages 158-163). We call this last procedure the Trigonometric Regression procedure.

The first subsection describes the statistics that we use in our analysis. The next subsection studies the properties of the solution to (2.7). The third subsection compares these properties with those of alternative filters that are used in the literature. The second and third subsections are based on unit root representations of the data. The final subsection considers robustness of our results by considering trend stationary representations instead.

### 3.1. Some Useful Statistics

We evaluate the filtering procedures by studying the dynamic correlations, corrt(ét, yt-r), and the relative standard deviations, (vart(ýt)/var(yt))1/2, for various t.20 This section explains why we look at these statistics, and how we compute them.

These statistics have three features which make them useful for our purposes. First, wher the s are based on variable lag filters, they are non-trivial functions of time. We use the quantitative magnitude of this variation to assess the degree of non-stationarity in Ît. Of course, statistics based on yt alone, or statistics based on Ît when fixed lag filters are used, are invariant with respect to t, given the data generating mechanisms that we consider. Second, for filters that solve a projection problem.

nonstationarity in this filter is quantitatively small.

20Following convention, a statistic for a particular date is defined across the ensemble of realizations for the underlying stochastic process at that date.


<!-- p:15 -->


the projection criterion, E[(yt – t)2Ω], is a simple function of the correlation between yt and :21

$$E [ ( y _ { t } - \dot { y } _ { t } ) ^ { 2 } | \Omega _ { t } ] = \left [ 1 - c o r r _ { t } ( \dot { y } _ { t } , y _ { t } ) ^ { 2 } \right ] v a r ( y _ { t } ) .$$

Here, Ω is the relevant information set in the projection.22 This relation indicates that we are free to think of the projection criterion in terms of corrt(ýt, yt), an object that we find easier to interpret than E[(yt – ýt)2|Ω] itself. In evaluating our results, it is useful to be aware of two other results that are true when Ît solves a projection problem:

$$c o r r _ { t } ( \hat { y } _ { t } , y _ { t } ) = \left [ \frac { v a r _ { t } ( \hat { y } _ { t } ) } { v a r ( y _ { t } ) } \right ] ^ { 1 / 2 } , \ v a r _ { t } ( \hat { y } _ { t } ) \leq v a r ( y _ { t } ) .$$

Third, one of our concerns is to quantify the phase shifts that exist between yt and Ît when the latter is computed using non-symmetric filters. As explained below, the dynamic correlations between yt and Ît are useful for this.

We now briefly discuss how we compute these statistics. We evaluate the variance of yt using the following relation:23

$$v a r ( y _ { t } ) = \frac { 1 } { \pi } \int _ { a } ^ { b } f _ { x } ( \omega ) d \omega .$$

21This is a standard result. To see it, note that by the orthogonality property of projections, we can write yt = t + ε, where ε, is orthogonal to Ω, and, hence, i: itself. Then,

$$v a r _ { t } ( y _ { t } - \dot { y } _ { t } ) = v a r _ { t } ( y _ { t } ) - v a r _ { t } ( \dot { y } _ { t } ) = v a r _ { t } ( y ) \left [ 1 - \frac { v a r _ { t } ( \dot { y } _ { t } ) } { v a r ( y _ { t } ) } \right ] = v a r ( y _ { t } ) \left [ 1 - \rho _ { t } ( 0 ) ^ { 2 } \right ] .$$

The last equality follows from the following observation:

$$c o r r ( \dot { y } , y _ { l } ) = \frac { c o v _ { l } ( \dot { y } , y _ { l } ) } { [ v a r ( \dot { y } ) v a r _ { l } ( y _ { l } ) ] ^ { 1 / 2 } } = \frac { v a r _ { l } ( \dot { y } _ { l } ) } { [ v a r ( \dot { y } ) v a r _ { l } ( y _ { l } ) ] ^ { 1 / 2 } } = \left ( \frac { V a r _ { l } ( \dot { y } _ { l } ) } { V a r _ { l } ( y _ { l } ) } \right ) ^ { 1 / 2 } .$$

22That is, Ω, = {x1,., r} for all t in the case of Optimal, e-12,..., 0,.., e+12 in the case of Optimal Fixed, p = f = 12, etc. In practice, we approximate an integral like this by the Riemann sum:

$$\frac { 1 } { \pi } \int _ { \real } f _ { x } ( \omega ) \omega \approx \frac { b - a } { \pi } \frac { 1 } { N } \sum _ { j = 1 } ^ { N } f _ { x } ( \omega _ { j } ) = \frac { b - a } { \pi } \frac { 1 } { N } \sum _ { j = 1 } ^ { N } \frac { \theta ( e ^ { - j } ) \theta ( e ^ { j } ) } { 2 ( 1 - \cos ( \omega _ { j } ) ) } , \, \omega _ { j } = a + \frac { b - a } { N } j , \, j = 1 , \dots , N$$

To guarantee that var(yt) is accurately computed, and because it only needs to be computed a few times, we set N to a very high value, 10,000.


<!-- p:16 -->


We evaluate the variance of ýt using the following expression:24

$$v a r _ { t } ( \dot { y } _ { t } ) = \frac { 1 } { \pi } \int _ { 0 } ^ { \pi } | \dot { B } ^ { p , f } ( e ^ { - i \omega } ) | ^ { 2 } f _ { x } ( \omega ) d \omega .$$

Here, var is a non-trivial function of time when p and f vary with t.

The dynamic correlations between. yt: and ýt are computed using the following the expression:

$$c o r r _ { t } ( \dot { y } _ { t } , y _ { - \tau } ) = \frac { c o v _ { t } ( \hat { y } _ { t } , y _ { - \tau } ) } { \sqrt { v a r _ { t } ( \dot { y } _ { t } ) v a r ( y _ { t } ) } } = \frac { \frac { 1 } { \pi } \int _ { a } ^ { b } \real { \text {real} } \left [ r ^ { p . } ( e ^ { - \dot { w } } ) e ^ { i ( \theta ( w ; p . ) + \omega k ) } f _ { x } ( \omega ) \right ] d \omega } { \sqrt { v a r _ { t } ( \dot { y } _ { t } ) v a r ( y _ { t } ) } } .$$

For convenience, we have written p.f in polar form:

$$\hat { B } ^ { p , f } ( e ^ { - i \omega } ) = r ^ { p f } ( e ^ { - i \omega } ) e ^ { i \omega ( \omega _ { i } p , \omega ) } ,$$

where r.f (e-) is real and the function θ(ω; p, f) is the phase of ps (e-) (see Sargent (1987, chapter XI).25 We use the location of the peak of this correlation function to determine whether there is a phase shift between yt and ýt. To see the rationale for this, consider the following special cases. When p.f is symmetric, so that θ(ω; p, f) ≡ 0 and there is no phase shift betweer y and Ît, then it is easily verified that corrt(ýt, yt-r) is symmetric about τ = 0.26 When p.f is not symmetric, so that there is a nonzero phase shift between yt and Ît, then this symmetry property of the correlatiou fuction fails. Consider, for example, the extreme case in which p.f(L) = Lh and h ≠ 0, so that τP.f(e−) = 1 and θ(ω;p, F) = -hω. In this case, it is easy to see that corrt(ýt, yt-r) is symnetric about τ = h. In general,when symmetry fails the phase of pf(e-iw) does not satisfy this proportionality property,

2The integrand in the expression for var (ýt) exhibits substantial variation, particularly in the region about ω = a and ω = b. To ensure that these integrals are computed accurately, we divided the interval, ω ∈ (0, π) into five regions: (0, a − ∆1), (a − ∆1, a + ∆1), (a + ∆1, b − ∆2), (b − ∆2, b + ∆2), (b + ∆2, x), with ∆1, ∆2 &gt; 0. The integral in each region was evaluated using the Riemann approximation formula described in the previous footnote, with N = 100 in each interval.

2sTo verify our covariance formula, note first from the results in Sargent (1987, chapter XI), that

$$c o v ( \dot { y } _ { t } , y _ { t - k } ) = \frac { 1 } { 2 \pi } \int _ { - \tau } ^ { \tau } \hat { B } ^ { p , f } ( e ^ { - i \omega } ) B ( e ^ { i \omega } ) e ^ { i k } f _ { t } ( \omega ) d \omega .$$

Then, note that the integral from 0 to π is the complex conjugate of the integral from -π to 0. Finally, we have taken into account of the definition of B to limit the range of integration.

s     e n d se s  e    s   o hy symmetry of p./ also implies symmetry of the covariance function, note that when θ ≡ 0, the covariance can be written

$$\frac { 1 } { \pi } \int _ { 0 } ^ { 1 } B ( e ^ { - i \omega } ) r ^ { 2 } ( e ^ { - i \omega } ) e ^ { i \omega t } f _ { 2 } ( \omega ) d \omega$$

which is the covariance function of a stochastic process whose spectral density is B(e-)r.f(e-)f(ω) . The result follows from the symmetry about k = 0 of the covariance function of a stochastic process.


<!-- p:17 -->


and so the asymmetry in ps(e-iw) is manifested in more exotic forms of asymmetry in ρt(τ).

### 3.2. Difference Stationary Data Generating Mechanisms

We estimated time series models of the form (2.8) for four data sets often studied in macroeconomic analysis. In each case, we fit a model to the monthly, quarterly and annuai data. The variables, t, considered are: inflation, output (GDP for the annual and quarterly frequencies and industrial production for monthly), the rate of interest (measured by the three-month return on US Treasury bills) and the unemployment rate. Inflation is measured as the first difference of the log of the consumer price index (CPI); the rate of interest is measured as the logarithm of the net rate; and output was transformed using the logarithm. The data set covers the period 1960-1997. The estimation results are presented in Table 1. With one exception, the Box-Pierce statistic ('Q') indicates little evidence of serial correlation in the errors, as indicated by the p-values in the table. In the exceptional case, monthly inflation, the addition of higher order lags does not raise the p-value.

The spectral density of (1 – L)zt for each model is graphed in Figure 3. Note that the spectral densities of output, interest rates and unemployment are very similar. They exhibit relatively high power in the low frequencies. Quarterly and monthly inflation deviates from this pattern in having relatively more power in the higher frequencies.


<!-- p:18 -->


| Table 1: Time Series Representations for Selected US Data - L)xg = e + Oe_ + O2Eg_2 + 0c_ + O4Eg...4 + Ee? = - variable, Xt (1   |   Table 1: Time Series Representations for Selected US Data - L)xg = e + Oe_ + O2Eg_2 + 0c_ + O4Eg...4 + Ee? = |   Table 1: Time Series Representations for Selected US Data - L)xg = e + Oe_ + O2Eg_2 + 0c_ + O4Eg...4 + Ee? = - )__0 | Table 1: Time Series Representations for Selected US Data - L)xg = e + Oe_ + O2Eg_2 + 0c_ + O4Eg...4 + Ee? = - J__02   |   Table 1: Time Series Representations for Selected US Data - L)xg = e + Oe_ + O2Eg_2 + 0c_ + O4Eg...4 + Ee? = - f, |   Table 1: Time Series Representations for Selected US Data - L)xg = e + Oe_ + O2Eg_2 + 0c_ + O4Eg...4 + Ee? = - f |   Table 1: Time Series Representations for Selected US Data - L)xg = e + Oe_ + O2Eg_2 + 0c_ + O4Eg...4 + Ee? = - 0 | Table 1: Time Series Representations for Selected US Data - L)xg = e + Oe_ + O2Eg_2 + 0c_ + O4Eg...4 + Ee? = - Q   | Table 1: Time Series Representations for Selected US Data - L)xg = e + Oe_ + O2Eg_2 + 0c_ + O4Eg...4 + Ee? = - F1equency   |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| log(CPIt/CPIg_i)                                                                                                                 |                                                                                                         0.0021 |                                                                                                                 -0.75 |                                                                                                                        |                                                                                                                     |                                                                                                                    |                                                                                                                    | 0.00 (36.1)                                                                                                        | M                                                                                                                          |
|                                                                                                                                  |                                                                                                         0.0042 |                                                                                                                 -0.23 | -0.27                                                                                                                  |                                                                                                                0.32 |                                                                                                                    |                                                                                                                    | 0.11 (30-3)                                                                                                        | Q                                                                                                                          |
|                                                                                                                                  |                                                                                                          0.015 |                                                                                                                  0.81 |                                                                                                                        |                                                                                                                     |                                                                                                                    |                                                                                                                    | 0.34 (9-1)                                                                                                         | A                                                                                                                          |
| log(CDPg)                                                                                                                        |                                                                                                         0.0075 |                                                                                                                  0.28 | 0.21                                                                                                                   |                                                                                                                 020 |                                                                                                               0.16 |                                                                                                                    | 0.20 (36-4)                                                                                                        | M                                                                                                                          |
|                                                                                                                                  |                                                                                                         0.0088 |                                                                                                                  0.25 | 0.16                                                                                                                   |                                                                                                                0.10 |                                                                                                               0.12 |                                                                                                                    | 0.09 (30-4)                                                                                                        | Q                                                                                                                          |
|                                                                                                                                  |                                                                                                          0.021 |                                                                                                                  0.34 |                                                                                                                        |                                                                                                                     |                                                                                                                    |                                                                                                                    | 0.89 (9-1)                                                                                                         | A                                                                                                                          |
| Log(Tbillt)                                                                                                                      |                                                                                                          0.064 |                                                                                                                  0.26 |                                                                                                                        |                                                                                                                     |                                                                                                                    |                                                                                                                    | 0.05 (36-1)                                                                                                        | M                                                                                                                          |
|                                                                                                                                  |                                                                                                          0.105 |                                                                                                                  0.45 | -.16                                                                                                                   |                                                                                                                     |                                                                                                                    |                                                                                                                    | 0.24 (30-2)                                                                                                        | Q                                                                                                                          |
|                                                                                                                                  |                                                                                                           0.21 |                                                                                                                  0.58 |                                                                                                                        |                                                                                                                     |                                                                                                                    |                                                                                                                    | 0.54 (9-1)                                                                                                         | A                                                                                                                          |
| Unempk'ymentt                                                                                                                    |                                                                                                           0.18 |                                                                                                                 -0.02 | 0.19                                                                                                                   |                                                                                                                0.17 |                                                                                                               0.20 |                                                                                                               0.05 | 0.021 (36-5)                                                                                                       | M                                                                                                                          |
|                                                                                                                                  |                                                                                                           0.27 |                                                                                                                  0.65 | 0.48                                                                                                                   |                                                                                                                0.41 |                                                                                                                    |                                                                                                                    | 0.66 (30-3)                                                                                                        | Q                                                                                                                          |
|                                                                                                                                  |                                                                                                           0.96 |                                                                                                                  0.28 | --                                                                                                                     |                                                                                                                     |                                                                                                                    |                                                                                                                    | 0.80 (9-1)                                                                                                         | A                                                                                                                          |

Note: All time series models estimated using the RATS command, boxjenk. Data cover the period 1960-1997. Q denotes the p-value of the Box-Pierce test of the null hypothesis of zero autocorrelation in the residuals. In (n, m), n denotes number of autocorrelations in residuals used, and m denotes degrees of freedom of chi-square test statistic.

### 3.3. Properties of the Optimal Filter Approximation

We evaluate various procedures for computing Ît under a variety of specifications of the time series representation for t, various data sampling intervals and frequency bands. The procedures we consider are listed in Table 2. Comparison of Optimal Symmetric and Optimal Fixed permits us to assess the importance of time stationarity in the filter. Comparison of Optimal and Optimal Symmetric permits us to assess the importance of symmetry. Comparison of Optimal and Random Walk permits us to assess the importance of getting the details of the time series representation of It just right.


<!-- p:19 -->


| Table 2: Band Pass Filter Approximation Procedures Considered - Name   | Table 2: Band Pass Filter Approximation Procedures Considered - Definition   |
|------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Optimal                                                                | Optimal                                                                      |
| Random Walk                                                            | Optimal, assuming random walk zt ((1.2)-(??))                                |
| Optimal, Symmetric                                                     | Optimal, subject to p = I                                                    |
| Optimal, Fixed                                                         | Optimal, subject to p =1=36                                                  |
| Random Walk, Fixed                                                     | Optimal, subject to p = f = 36, assuming random walk Xg                      |

This section reports our results, based on the unit root representations in Table 1, and on the Near IID ((2.13) with η = .01) and Persistent, (2.15), representations considered in the previous section. Given the evidence in Figure 3, it is not surprising that the findings for many of the time series representations in Table 1 are very similar. Therefore, of the time series representations in Table 1, we only present results for inflation. We selected this time series representation because it provides the weakest support for our contention that the Random Walk filter is close to optimal. Results based on the Persistent representation are similar to those for the other representations in Table 1, and so we do not present these. Results based on annual, monthly and quarterly data sampling intervals are also very similar. Consequently, we only present the findings based on the monthly sampling interval. We consider three frequency bands: 1.5 to 8 years, 8 to 20 years, and 20 to 40 years.

The results we present are based on two monthly time series representations: the one estimated using inflation (see Figure 4) and the Near IID representation (Figure 5). Consider Figure 4 first. The first, second and third columns of the figure provide information on corr(ýt, yt), [var,(ýt)/var(yt)]1/2, and corre(ýt, yt-k), respectively. We report results for t = 1, .., 240, since statistics are symmetric across the first and second halves of the sample. The first, second and third rows in the figure correspond to three different frequency bands: 1.5 to 8 years; 8 – 20 years; and 20 – 40 years, respectively. Each panel in the frst column contains four curves, differentiated according to the procedure used to compute it: Optimal, Random Walk, Optimal Symmetric, or Optimal Fixed. Results for Optimal and Random Walk are presented for t = 1,..., T/2. Results for Optimal Symmetric and Optimal Fixed are presented for t = 37, ..,T/2, since we set p = f = 36. Here, T = 480, which is slightly more than the number of monthly observations in the estimation period for the monthly time series representations in Table 1. The second column contains results for Optimal and Random Walk alone. Here, results for Optimal are simply repeated for convenience from the first column. As discussed above, for filters that solve a projection problemn, the correlation and relative standard deviation coincide. Finally, the third column reports corrt(ýe, yt-k) for five different values of t: t = 1,31,61, 121, 240. In each case, k ranges from -24 to 24. Also, the location of k = 0 is indicated by a '+'.


<!-- p:20 -->


The main findings in Figure 4 are as follows. First, the efficiency differences between Random Walk and Optimal are very small (column 1). A minor exception to this can be found in the business cycle frequencies for t = 4, ..., 11. For these dates, the difference between corrt(ét, yt) based on Optimal and Random Walk is between 0.08 and 0.12. Although these differences are noticeable, they do not seem quantitatively large. Moreover, the differences between Random Walk and Optimal are barely visible when the analysis is based on the other time series representations in Table 1.

Second, imposing symmetry (see Optimal Symmetric) results in a relatively small loss of efficiency in the center of the data set, but that loss grows in the tails. Third, imposing stationarity in addition to symmetry (Optimal Fixed) results in a noticeable loss of efficiency throughout the data set. However, the efficiency losses due to the imposition of symmetry and stationarity are comparatively small in the business cycle frequencies. They are dramatic in the lowest frequencies.

Fourth, Ît based on Optimal and Random Walk appears to be reasonably stationary, except in an area in the tails. This tail area is fairly small (about 1.5 years) for the business cycle frequencies, but Fs  s  s r r  (        nn ae shift between Ît and yt (column 3). There is essentially no phase shift, even at the lowest frequencies.

We conclude from these results that the noticeable efficiency gains obtained by filters that use all the data come at little cost in terms of nonstationarity and phase shift. However, the gains of going from a simple procedure like Random Walk to Optimal are quite small.

These findings apply to all the time series models in Table 1, as well as to the Persistent time series representation. One time series representation where these findings do not hold up is the Near IID case, which is reported in Figure 5. In particular, the finding that Random Walk is nearly optimal and roughly stationary no longer holds (columns 1 and 2). However, the other conclusions continue to hold. For example, Optimal is still nearly stationary outside of tail areas. Also, imposing symmetry and time-stationarity on the filter imposes substantial efficiency costs, especially in the low frequencies.

### 3.4. Properties of Alternative Filter Approximations

Next we discuss three alternative band pass filter approximations that have been used in the literature. The first of these, the one due to Baxter and King (1999), is the fixed-lag, symmetric filter defined in (2.14). This filter can do no better than Optimal Fixed, discussed in the previous section. That filter is dominated by Random Walk, which is nearly optimal for the time series models reported in Table 1. Below, we provide a detailed analysis of two other filters: the HP filter and Trigonometric Regression. Again, we find that Random Walk is nearly optimal and dominates the HP filter and Trigonometric Regression.


<!-- p:21 -->


#### 3.4.1. Hodrick-Prescott Filter

Proponents of the HP filter offer several interpretations of what it does (see section 4 below for an elaboration). The interpretation that we adopt here is that it approximates a band pass filter designed to isolate, in quarterly data, frequencies corresponding to the business cycle and higher.27 We identify these with cycles of period 8 years and less. We display evidence which suggests that, for data like US GDP, unemployment and the CPI, our Random Walk filter is nearly optimal and outperforms the HP filter. This finding also applies when these filters are used to obtain real-time estimates of yt. We stress this here because the HP filter is sometimes used in a macroeconomic stabilization context, when estimates of current yt are needed.

Our discussion in this section is divided into two parts. We first discuss the evidence on Ît in Columns 1 and 2 of Figure 6, ignoring the first 2-5 years' observations. We then focus separately on those observations and on the information in Column 3 because this allows us to assess the value of the filters for obtaining real-time estimates of yt.

The first column in Figure 6 displays corrt(ýt, yt) associated with the HP filter, Random Walk, and Optimal Fixed for t = 1, .., 80 and for the indicated three quarterly time series models. We do not display these statistics for Optimal, because they are virtually indistinguishable from Random Walk. Interestingly, despite the fact that HP uses all the data, it nevertheless performs less well than Optimal Fixed. Moreover, it does notably less well than Random Walk, particularly for Unemployment and GDP. .Outside of a tail area of roughly two years, corrt(űt, yt) exceeds 0.95 and it is closer to 0.99 towards the middle of the data set for Random Walk. For GDP and Unemployment, this statistic based on the HP filter never exceeds 0.90.

Column 2 shows that, outside of a five year tail area, the performance of Random Walk is similar to that of the HP filter, in terms of the standard deviation of Ît: Random Walk undershoots Var(yt) somewhat while HP overshoots.

Another way to compare HP filter and Randomn Walk focuses on the metric, (1.1), that we use to construct optimal filters. In particular, we consider R. the absolute size of the tpical estimation error, Ît - yt (measured by its standard deviation), to the absolute size of the typical value of yt (measured by its standard deviation): R = [Var(ý: - yt)/Var(yt)]1/2 28 A large value of Rę indicates a poor filter approximation. In the extreme case when R is greater than or equal to unity, then the filter approximation is literally useless. In this case one can do just as well, or better, estimating yt by its mean with Ît ≡ 0. In the case of Random Walk, R is 0.14 towards the middle of the data set and R is no greater than 0.31 if we ignore the first two years' data. In the case of the HP filter, this number is 0.49 for Unemployment and GDP and around 0.37 for Inflation. These results are the basis for our conclusion that, outside of the tail area, Random Walk outperforms the HP filter.

The HP filter parameter, λ, is set to 1600, as is typical in applications using quarterly data.


<!-- p:22 -->


We now turn to the implications of the results in Figure 6 for the real time performance of the filters. We do this because it is of interest in the context of stabilization policy, when current estimates of the output and unemployment gaps are used. For example, John Taylor has argued persuasively that monetary policy makers set current policy as a function of the current output gap, among other things. 29 The output gap is the log difference between actual GDP and 'potential' GDP, and the unemployment gap is the difference between actual unemployment and the 'natural' rate of unemployment. One interpretation of potential GDP and the natural rate of unemployment is that they correspond to the HP trend in actual GDP and unemployment, respectively.30 For this reason, we now investigate how effective HP filter, Random Walk and Optimal are in estimating yt in real time.

At the outset, it should be clear that estimating the current value of yt is likely to be a difficult task. Suppose, for example, that the variable, xt, has recently changed value. How is one to decide whether that change is temporary (i.e., part of yt) or more persistent (i.e., part of )? No doubt we can confidently answer this question with a sufficient passage of time, with more data. In the light of hindsight, it is relatively easy to determine whether a given change in a variable was just a blip or a movement in the trend. But, in real time without the advantage of hindsight, we can expect that even our best estimates of yt will be noisy. That is the case for Random Walk and HP Filter. However, we show that the estimate based on HP filter is noisier than that based on Random Walk.

28Here,

<!-- p:23 -->


Recall the symmetry properties of the statistics in Columns 1 and 2 in Figure 6: their properties in the second half of the sample are the mirror image of their properties in the first half. As a result, the statistics at the left end-point of these two columns provide evidence on the real-time performance of the filters being considered. That is because, by symmetry, these statistics can be viewed as being based upon the estimate, īr, of 'current' yT, where T = 160. (In the case of Random Walk, T is computed using the one-sided filter, (1.4).) Note that the correlation between Ît and ye is at its lowest for t = T (t = 1) for both Random Walk and HP filter. That is, the real time correlation between the estimated and actual gaps is lower than what it is after the arrival of new data.31 The drop is fairly substantial.

The evidence in Column 2 shows that, for the three time series representations considered, the real-time variance of ýt computed using Random Walk is less than what it is after new data arrives. In this sense, the estimate of the trend implicit in this filtering procedure (and Optimal) tends to follow the actual data more closely in real time than after the arrival of new data.32 We do not know if this is a general property of Random Walk, true for all time series representations. Evidently, it is not a general property of the HP filter. With the data generating mechanisms based on GDP and inflation, we see that the real time variance of Ît is at its global maximum for t = T and t = 1.33

We now compare Random Walk and HP filter using the Re statistic described above, for t = T. Using Random Walk, Rr = 0.77, 0.78, and 0.69 for GNP, unemployment, and inflation respectively. Note that these numbers are substantially larger than what they are for data points closer to the middle. Still, they indicate Random Walk provides at least some information about yr. Now consider HP filter. For GDP, Rr = 1.01. For unemployment and inflation, Rr is 1.03 and 0.80, respectively. Evidently, these statistics indicate that Random Walk dominates HP filter in real time. Moreover, for purposes of estimating the GDP and unemployment gaps in real time, HP filter is worse than useless. The estimate, ÎT = 0, produces a smaller error than using the HP filter estimate, r.

The statistics on the real-time properties of the filters that we have just considered abstract from scale. The evidence in Column 3 exhibits the magnitude of the error in real-time gap estimates for our variables. We consider the standard deviation of the error , yt -ût, for a fixed date, t = 160. We display this statistic for the time when t is the current date and continuing as new data become available and the data set becomes correspondingly larger. These results allow us to quantify the value of hindsight when estimating yt.

3iThe evidence in Columns 1 and 2 actually do not allow us to literally infer what happens with the arrival of new data. The data set underlying the experiments in these columins are based on a fixed sample of length 160.

These are counterexamples to the conjectures by Barrell and Sefton (1995, p. 68) and St-Amant and van Norden (1997, p. 11).

2In our context, the estimated trend is d, where de equals it plus the drift in the data, where it = x - t (recall our decomposition, (2.1).)


<!-- p:24 -->


We study [var16o(ġ160 – y16o0)]1/2 for T = 160, 161, .., 200, based on Random Walk, Optimal and HP filter. For Random Walk and Optimal, the standard deviations are based on įı6o = P[yı6olx1, ..., T], for T = 160, .., 200. In the case of HP, they are based on 16o, the 160th observation in the HP filtered x, ..., xT, for T = 160, 161, .., 200. There are several things worth emphasizing in the third column of Figure 6. First, Random Walk and Optimal essentially coincide, and both dominate the HP filter. Second the error in estimating yi6o declines by roughly one-half in the first year after t = 160. Thereafter, further declines in the error come more slowly. Third, after initially falling with the arrival of the first two years' data, the error of the HP filter asymptotes to a relatively high level. The reason is that, as the size of the data set grows, the HP filter does not asymptote to a band p'a        a  t t    et ely [varı6o(Î16o – y16o)]1/2 would shrink to zero for Random Walk and Optimal. The information in Figure 6 suggests that this requires a very large value of T. These results are the basis for our conclusion that Random Walk is nearly optimal and outperforms the HP filter in terms of real-time performance.34

In this discussion, we have emphasized the differences in the performance of the Hodrick-Prescott filter and Random Walk. We note, however, that the quantitative magnitude of the differences is not very great for some purposes. For example, in Appendix B we display business cycle statistics based on US data using various filter approximations and the HP filter, and there is little quantitative difference between them. The differences seem relatively larger when we consider real-time estimation of yt. The HP filter performs very poorly on this dimension. Indeed, in the case of GDP it is useless.35 However, even the optimal procedure seems relatively unreliable in this case.36

e ed e   sn e t ens ree   e nn   sr and econometric framework, by Staiger, Stock and Watson (1997). Their estimated standard deviations of this gap range from 0.46 to 1.25 percentage points, depending on the data used in the analysis. They note how wide this range is and so it is not surprising that our estimates fall inside it.

3sThese conclusions about the real time performance of the HP filter complement those obtained using different methods by others, including Laxton and Tetlow (1992), Orphanides (1999) and St-Amant and van Norden (1997).

3We have abstracted from several real-time issues which could make the HP filter, Optimal and Random Walk seem ev es  t  e i i g e i   e   e s ion and data revisions. A more complete analysis would also take these factors into account in characterizing the accuracy of real time estimates of the business cycle and higher frequency components of the data. For further discussion, see Orphanides (1999) and Orphanides and van Norden (1999).


<!-- p:25 -->


#### 3.4.2. Trigonometric Regression

We now discuss the Trigonometric Regression procedure. This procedure makes use of the entire dataset, x1, ..., IT: to estimate each yt, as follows:

$$\dot { y } _ { t } = B _ { t } ( L ) x _ { t } , \, t = 1 , \dots , T ,$$

where

$$B _ { ( L ) } ( x _ { l } ) & = \sum _ { l = T } ^ { t - 1 } \left \{ \frac { 2 } { T } \sum _ { j \in J } \cos ( \omega _ { j } l ) \right \} z _ { l - l _ { l } } , \, \text {if} \, \frac { T } { 2 } \notin J \, , \\ & = \sum _ { l = T } ^ { t - 1 } \left \{ \frac { 2 } { T } \sum _ { j \in J _ { 1 } } \cos ( \omega _ { j } l ) + \frac { 1 } { T } \cos ( \pi ( t - l ) ) \cos ( \pi ) \right \} z _ { l - l _ { l } } , \, \text {if} \, \frac { T } { 2 } \in J \, \\ & \quad t = 1 , \dots , T , \, w _ { j } = \frac { 2 } { T } j . \quad u .$$

Here, J indexes the set of frequencies we wish to isolate, and is a subset of the integers 1..., T/2.37 It a t t Bt .. =   s     t   = t t s   ly has a second unit root for t in the middle of the data set, when Bt(L) is symmetric.39 For this reason. it is important to drift adjust xt prior to filtering.

We assume T is even. Also, J is the set of integers between ji and j2, where ji = T/pu and j2 = T/pr. The representation of i: given in the text, while convenient for our purposes, is not the conventional one. The conventional representation is based on the following relation:

$$\dot { u } = \sum _ { i \in J } \{ a , \cos ( \omega _ { i } t ) + b _ { j } \sin ( \omega _ { i } t ) \} \, ,$$

where the a,'s and b,'s are coefficients computed by ordinary least squares regression of zt on the indicated sine and cosine functions. The regression coefficients are:

$$y = \{ \begin{array} { c } 4 , 5 \sum _ { 1 } ^ { 2 } \cos ( \omega _ { 1 } t ) z _ { 1 } , j = 1 , \dots , T / 2 - 1 \\ 4 \sum _ { 1 } ^ { 2 } \cos ( \pi t ) z _ { 1 } , j = T / 2 , \end{array} , \, , b = \left \{ \begin{array} { c } 4 \sum _ { 1 } ^ { T } \sin ( \omega _ { 1 } t ) z _ { 1 } , j = 1 , \dots , T / 2 - 1 \\ 4 \sum _ { 1 } ^ { T } \sin ( \pi t ) z _ { 1 } , j = T / 2 \end{array} .$$

The expression in the text is obtained by collecting terms in z, and making use of the trigonometric identity. cos(z) cos(y)- sin(z) sin(y) = cos(r − y).

To see that B.(1) = 0 when T/2  J, simply evaluate the sum of the coefficients on 1, 2..., T for each t :

$$\frac { 1 } { T } \sum _ { j \in J ( J = 1 ) } \sum _ { 1 } ^ { 1 - T } 2 \cos ( y , t ) = \frac { 1 } { T } \sum _ { j \in J ( J = 1 ) } \sum _ { 1 - j } ^ { 1 - T } \left [ e ^ { i t } + e ^ { - i t } \right ] = \frac { 1 } { T } \sum _ { j \in J } \left [ e ^ { - i t ( j - 1 ) } \frac { 1 - e ^ { i t } } { 1 - e ^ { i t } } + e ^ { i t } \right ] ( i - 1 ) ^ { 1 - e ^ { i t } - T } \right ] = 0 ,$$

because 1 - e,T = 1 − e−T = 1 − cos(2xj) + sin(2xj) = 1 for all integers, j.

sWhen T is even, then there cannot be an eract second unit root since it rules out the existence of a date precisely in the middle of the dataset. By B.(L) having n unit roots we mean that it can be expressed as B.(L)(1 – L)", where B.(L) is a finite ordered polynomial. The discussion of two unit roots in the text exploits the fact that the roots of a symmetric polynomial come in pairs.

When T/2 ∈ J, the expression for B.(1) includes ∑ ns  s s sdxr s  {(ak ((1 - kt s } 1of an even number of 1's and -1's, so it sums to 0.


<!-- p:26 -->


Our basic finding is that when the when the data are generated by the time series representations in Table 1, the performance of Trigonometric Regression is worse than that of Random Walk. Since the results based on these time series representations are fairly similar, we present only those based on the data generating mechanism for inflation. These are displayed in Figure 7, which has the same format as Figures 4 and 5. The results for Random Walk and Optimal in Figure 7 correspond to those reported in Figure 4, and are reproduced here for convenience. In Column 1, we see that in terms of corrt(Ît, yt), Trigonometric Regression is outperformed in all frequency ranges by Random Walk, which is nearly optimal. Column 2 shows that the estimates of yt based on Trigonometric Regression overshoot Var(yt), sometimes by a great deal, and performs worse on this dimension than either Random Walk or Optimal. The relative performance of Trigonometric Regression is particularly poor in the lower y e . t t r t   ot i eot' which is even worse than HP filter. Column 3 displays the dynamic cross correlations between Ît and yt when the former are computed by Trigonometric Regression. The evidence shows that there is very little phase shift between the variables, but there appears to be a substantial departure from covariance stationarity. The correlations in the tails of the data set are notably smaller than they are in the middle.

Although Trigonometric Regression appears in Figure 7 to be substantially worse than Random Walk, for some purposes the poor performance may not be quantitatively important. For example, in Appendix B we find that, for standard business cycle statistics, Trigonometric Regression produces results quite similar to Random Walk.

### 3.5. Robustness of Analysis to Trend Stationarity

The quantitative analysis of our filters has been based, up to now, on the assumption that the data are generated by a difference stationary process estimated for one of the standard macroeconomic data series. Our basic finding is that Random Walk is nearly Optimal. Here, we show that - with a slight qualification - the same basic conclusion holds, even if we assume the data are trend stationary.

Our first step in the analysis was to redo the calculations in Table 2, by fitting moving average representations to the residuals from regressions of log GDP, inflation, the interest rate and unemployment on a constant and time trend. We then repeated the preceding calculations, using Optimal, Random Walk, HP filter and Trigonometric regression. Although the results are fairly similar across different time series representations, the model for inflation poses a modestly greater challenge for Random Walk. This is why we decided to only present results based on the time series representation for monthly inflation.

Results are presented in Figure 8, which is in the same format as Figures 4, 5, and 7. There are two things worth emphasizing here. First, consider the results for Random Walk. As in the difference stationary case (see Figure 4), Random Walk is nearly optimal in the business cycle frequencies, if we ignore the first and last two years' observations. However, some discrepancies between Random Walk and Optimal are apparent in the lower frequencies. Still, in the 8-20 year frequencies, there is no noticeable difference if we ignore the first and last five years' observations. Second, note that Trigonometric Regression still performs worse than Random Walk. Any concerns about Random Walk that might be raised by the results in Figure 8 do not warrant adopting the Trigonometric Regression procedure. If anything, they suggest adopting something closer to Optimal.


<!-- p:27 -->


## 4.Related Literature

Ea tat      t   a   t  ued forcefully the case that economic hypotheses are usefully cast in the frequency domain. One of the examples studied in the next section of this paper, an analysis of the relationship between money growth and inflation, is inspired in part by Engle's work on the same subject.

On a methodological level, the closest work to ours is that of Baxter and King (1999). They emphasize the potential usefulness of the band pass filter for constructing statistics to characterize the dynamics in the data. They confront the same practical problem that we do. Namely, to apply the band pass filter in a finite data set requires approximating it in some way. As noted above, the approximation t't r 't          r King and Watson (1994), and Stock and Watson (1998). They show how the Baxter-King recommended filter can be used to address interesting empirical questions.

Our analysis can be compared with Baxter and King's in three ways. First, our approach to approximating the band pass filter differs from theirs. We select the approximation which minimizes (1.1). Baxter and King adopt a different optimization criterion. They require that the approximating ilter optimize (2.7) with fr ≡ 1, subject to the requirement, B(1) = 0. This is equivalent to optimizing (2.7) under the assumption that xt has a Near IID time series representation. This is the representation analyzed in the previous section, in which the spectral density is flat over most frequencies, and then rises sharply in a small neighborhood of zero. This observation is useful because it clarifies the set of circumstances in which the Baxter-King filter is expected to work well, in the sense of (1.1).40 Second, we supply formulas for the optimal approximation to the band pass filter that apply in a broad class of time series representations. This provides alternatives to the Baxter-King filter, which is suitable for cases when the Near IID assumption is a poor one. We do not expect the Near IID representation to be well suited for many macroeconomic variables. As noted by Granger (1966) (see also Sargent (1987, pp. 280-281)), the 'typical spectral shape' of macroeconomic time series is one in which there is substantial power in a significant range of low frequencies. Third, the Baxter-King approach works with symmetric, fixed lag filters. In the previous section we presented experiments which suggest that adopting filters which use all the data, and which are therefore asymmetric and time-varying, improves the estimate of yt. There is a valid basis for concern that filters like this might result in no               th time series representations like those that fit several key postwar macroeconomic data series, these effects are not quantitatively large.

We have not established that the Near //D representation is the only one that rationalizes the Baxter-King filter as the optimal one.


<!-- p:28 -->


Our approach can also be compared to that of Hodrick and Prescott (1997). They provide a linear filter of the data, which has three interpretations. Under the first interpretation, their filter is viewed as solving a particular projection problem: extract a signal from a data series that is the sum of a signal and an orthogonal noise. As is evident from (2.1) and the discussion thereafter, optimally extracting a particular band of frequencies from the data requires solving the same kind of problem. The difference between the two approaches is that, under this interpretation of the HP filter, it is based on a particular statistical model of the data while ours is not.41 Under this interpretation, the HP filter has two shortcomings: (i) The underlying model has the same difficulty of interpretation as do other trend-cycle decompositions: the concepts of 'signal' and 'noise' they seek to extract from the data do not correspond to meaningful economic objects in standard business cycle models. The data generated by these business cycle models do contain components that could perhaps loosely be characterized as trend and noise. But, they do not satisfy the orthogonality conditions posited by typical trend-cycle decompositions, including the one underlying the HP filter (see Christiano and Eichenbaum (1990)). (ii) Under the first interpretation of the HP filter, one has to take the underlying statistical model seriously. For example, a parameter λ, which corresponds to the relative variance of the signal and noise in the underlying model, needs to be estimated. This gives rise to numerous estimation and model evaluation issues that, from our perspective, are tangential. The decomposition we focus on is guaranteed to exist under very general conditions by the Spectral Representation Theorem.42 In our approach, the decomposition selected simply reflects the research interests of the analyst. Focusing on a particular decomposition does not require a commitment to any particular model of the data, beyond the relatively weak assumptions needed for the Spectral Representation Theorem to hold.

4Lucas (1980) also adopts a structural model like that of Hodrick-Prescott. Both assume that the data, , are the sum of a signal, st, and a noise, n. The signal and noise are assumed to be orthogonal, and the noise is uncorrelated over time. Lucas assumes the signal has the representation, s, = pst-1 + v, where v, is a white noise and |ρ| &lt; 1. Hodrick and Prescott assume 3, = 2st-1 - st-2 + vt.

42For a formal analysis of the Spectral Decomposition Theorem, see Koopmans (1974). A simplified discussion appears in Christiano and Fitzgerald (1998, Appendix).


<!-- p:29 -->


A second interpretation of the HP filter is that it is a particular band pass filter. For λ = 1600, it has been argued that the filter does well at isolating frequencies 8 years and higher (see Prescott (1986), King and Rebelo (1993), and Singleton (1988)). No claim has ever been made that the HP filter isa  ins si   s    d    oe o ns in section 3.4.1 which show that the Random Walk and Optimal filters dominate HP, especially for computing real-time estimates of èt. Still, it is shown in the Appendix that these differences are not quantitatively large enough to produce substantial differences in the computation of standard business cycle statistics. A problem is that when one wants to isolate different frequençy bands or use monthly or annual data, it is not clear how to proceed under this interpretation of the Hodrick-Prescott approach.43 The framework of this paper, which focuses on developing optimal approximations to the band pass filter, provides a straightforward way to proceed in these cases.

A thind interpretation of the HP filter is that it is a precisely stated algorithm which simply, draws a smooth line through the data. All the other filters discussed in this paper do this too.

We find the second two interpretations of the HP filter appealing. Under these interpretations, the band pass filter represents a natural extension of the work of Hodrick and Prescott. The band pass filter performs similarly to the HP filter in situations for which the latter was designed: extracting the business cycle component from quarterly time series data (see Appendix B). However, the band pass filter - particularly the approach advocated bere - can be used to construct filters that are effective in isolating other frequency bands as well. The next subsection describes empirical applications where filters of this type are of interest.

## 5. Applications

We illustrate the use of our recommended filter, presented in the introduction, using two examples. The first focuses on the relationship between unemployment and inflation, and the second examines the relationship between money growth and inflation.

We divide the annual data available for the period 1900 to 1997 into two parts: 1900-1960 and

The perspective adopted in this paper does offer one strategy: optimize, by choice of λ, the version of (2.7) with BP.f replaced by the Hodrick-Prescott filter. This strategy produces a vaiue of λ that is time-dependent and dependent upon the properties of the true time series representation. We suspect that closed form solutions for the values of λ that solve these optimization problems do not exist. We think that this strategy for filtering the data is not a good one. First, implementing it is likely to be computationaily burdensome. Second, as this paper shows, identifying the optimal band-pass filter approximation is straightforward.


<!-- p:30 -->


1961-1997. In each case, the data are broken into three sets of frequencies: those corresponding to 2-8 years (the business cycle), 8-20 years and 20-40 years. With respect to the Phillips curve, we find that in the pre-1960 sample, the correlation between inflation and unemployment is negative at all frequencies. Loosely, we characterize this as reflecting that all frequencies of the data exhibit a Phillips curve trade-of.. The most significant change in the post-1960 sample is that the 20-40 year correlation ap  s   o   in  e    rs this evidence in light of the Barro-Gordon model of inflation.

We then turn to the inflation-money growth relation. We find that in the pre-1960 period, the two variables move closely together in all frequencies. The relationship remains positive in the low frequencies in the post-1960s data. However, at the business cycle and 8-20 year frequencies, there is a substantial change.

### 5.1. The Phillips Curve

We consider annual data for the 1900-1960 and 1960-1997 periods separately. Figure 9a displays the raw unemployment and inflation data for the first sample. For convenience, the figure also depicts the NBER business cycle peak and trough dates. Casual inspection suggests a negative relationship (i.e., a 'Phillips curve') at all frequencies.44 The various frequency components of the data are displayed in Figures 9b - 9d, and they confirm this impression. The contemporaneous correlations between filtered inflation and unemployment are reported in Table 4, Panel A. The table also reports p-values under the null hypothesis that there is no relationship between the variables in any frequency band.45 The ne  e ts Gts td i   s   tt tor these observations, it is not surprising that the scatter plot of inflation and unemployment, exhibited in Figure 9b, also shows a negative relationship. This is just the classic Phillips curve, of textbook fame.46

It is worth emphasizing that, by 'Phillips Curve', we mean a statistical relationship, and not necessarily a relationship exploitable by policy.

The slope of the regression line drawn through the scatter plot of points in Figure 9b is -0.42, with a t-statistic of 3.77 and an R2 of 0.20.

isThese are computed by fitting separate q-lag scalar autoregressive representations to the level of inflation (first difference, log CPI) and to the level of the unemployment rate, and using the ftted disturbances and actual historical initial conditions to simulate 2,000 artificial data sets on inflation and unemployment. For annual data, q = 3; for monthly. q = 12; and for quarterly, q = 8. The data sets on unemployment and inflation are independent by construction. In each artifcial data set we compute correlations between the various frequency components, as we did in the actual data. In the data and the simulations, we dropped the first and last three years of the filtered data before computing sample correlations. The numbers in parentheses in Table 4 are the frequency of times that the simulated correlation is greater (less) than the positive (negative) estimated correlation. These are p-values under the null hypothesis that there is no relationship between the inflation and unemployment data.


<!-- p:31 -->


| Table 4: Phillips Curve and Money Growth-Inflation Correlations - Sample   | Table 4: Phillips Curve and Money Growth-Inflation Correlations - H. Frequency   | Table 4: Phillips Curve and Money Growth-Inflation Correlations - Bus. Cyc. Frequency   | Table 4: Phillips Curve and Money Growth-Inflation Correlations - &o   | Table 4: Phillips Curve and Money Growth-Inflation Correlations - 20-40 years   |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Panel A: CPI Inflation and Unemployment                                    | Panel A: CPI Inflation and Unemployment                                          | Panel A: CPI Inflation and Unemployment                                                 | Panel A: CPI Inflation and Unemployment                                | Panel A: CPI Inflation and Unemployment                                         |
| 1900-1960 (A)                                                              |                                                                                  | -0.57 (0.00)                                                                            | -0.32 (0.19)                                                           | -0.51 (0.23)                                                                    |
| 1961-1997 (A)                                                              |                                                                                  | -0.38 (0.11)                                                                            | -0.16 (0.41)                                                           | 0.45 (0.32)                                                                     |
| 1961, Q2 - 1997, Q4 (Q)                                                    | -0.37 (0.00)                                                                     | -0.65 (0.00)                                                                            | -0.30 (0.29)                                                           | 0.25 (0.34)                                                                     |
| 1961, Jan. - 1997, Dec. (M)                                                | -0.24 (0.00)                                                                     | -0.69 (0.00)                                                                            | -0.27 (0.30)                                                           | 0.23 (0.40)                                                                     |
| Panel B: CPI Inflation and M2 Growth                                       | Panel B: CPI Inflation and M2 Growth                                             | Panel B: CPI Inflation and M2 Growth                                                    | Panel B: CPI Inflation and M2 Growth                                   | Panel B: CPI Inflation and M2 Growth                                            |
| . 1900-1960 (A)                                                            |                                                                                  | 0.45 (0.00)                                                                             | 0.59 (0.04)                                                            | 0.95 (0.01)                                                                     |
| 1961 - 1997 (A)                                                            |                                                                                  | -0.72 (0.00)                                                                            | -0.77 (0.02)                                                           | 0.90 (0.10)                                                                     |
| 1961, Q2 - 1997, Q44Q)                                                     | -0.34 (0.00)                                                                     | -13.67 (0.00)                                                                           | -0.71 (0.05)                                                           | 0.87 (0.09)                                                                     |
| 1961, Jan. - 1997, Dec. (M)                                                | -0.13 (0.02)                                                                     | -0.66 (0.00)                                                                            | -0.74 (0.04)                                                           | 0.87 (0.10)                                                                     |

Note: Contemporaneous correlation between indicated two variables, over indicated sample periods and frequencies. Numbers in parentheses are p- values, in decimals, against the null hypothesis of zero correlation at all frequencies. For further details, see the text and footnote 25.

The post 1960 monthly inflation and unemployment data are analyzed in Figures 10a-f.47 There is a surprising degree of similarity between the pre and post 1960s data. For example, it is plain from the raw data in Figure 10a that for frequencies in the neighborhood of the business cycle, inflation and unemployment covary negatively. That is, the Phillips curve seems to be a pronounced feature of the higher frequency component of the data. At the same time, the Phillips curve appears to have vanished in the very lowest frequencies. The data in Figure 10a show a slow trend rise in unemployment throughout the 1960s and 1970s, which is reversed starting in early 1983." A similar pattern occurs in inflation, though the turnaround in inflation begins in April 1980, roughly three years before the turnaround in unemployment. The low frequency component of the data dominates in the scatter plot of inflation versus unemployment, exhibited in Figure 10b. That figure suggests that the relationship between inflation and unemployment is positive, in contrast with the pre-1960's data, which suggest otherwise (see Figure 9b). Clearly, this scatter plot exaggerates the degree to which the inflationunemployment dynamics have changed in the post-1960s data.48

4Figure 10 exhibits monthly observations on infiation and unemployment. To reduce the high frequency fuctuations in inflation, Figure 10a exhibits the annual average of inflation, rather than monthly inflation rate. The scatter plot in Figure 10b is based on the same data used in Figure 10a. Figures 10c-10f are based on monthly inflation, i.e., Iaos     o    e   n e tetr plot. The slope of that line, based on monthly data covering the period 1959:2 - 1998:1, is 0.47 with a t-statistic of 5.2.


<!-- p:32 -->


Impressions based on casual inspection of the raw data can be formalized and quantified using the band pass filtered data reported in Figures 10c - 10f. Thus, the frequency range from two months to 20 years (see Figures 10c and 10e) is characterized by a noticeable Phillips curve. Table 4 shows that the correlation in the range of high frequencies (when available) and in the business cycle frequencies is significantly negative. The correlation between inflation and unemployment is also negative in the 8-20 year range, but it is not statistically significantly different from zero in this case. Presumably, this reflects the relative paucity of information about these frequencies in the post-1960s data. Finally, Figure 10f indicates that the correlation between 20-40 year components is now positive, with unemployment lagging inflation. These results are consistent with the hypothesis that the Phillips curve changed relatively little in the 2-20 year frequency range, and that the changes that did occur are primarily concentrated in the very low frequencies.

Formal tests of this hypothesis, presented in Panel A of Table 5, fail to reject it. The table displays p-values for the null hypothesis that the post-1960s data on inflation and unemployment are generated by the bivariate vector autoregression (VAR) that generated the pre-1960s data. We implement the test using 2,000 artificial post-1960s data sets obtained by simulating a three-lag VAR and its fitted residuals estimated using the pre-1960s unemployment and inflation data.49 In each artificial data set we compute correlations between filtered inflation and unemployment just like we did in the actual post 1960s data. Table 5 indicates that 9 percent of correlations between the business cycle component of inflation and unemployment exceed the -0.38 value reported in Table 4 for the post-1960s data, so that the null hypothesis fails to be rejected at the 5 percent level. The p-value for the 8 - 20 year correlation is quite large, and is consistent with the null hypothesis at any significance level.

The statistical evidence against the null hypothesis that there has been no change in the 20 - 40 year component of the data is also not strong. This may in part reflect a lack of power stemming from the relatively small amount of information in the sample about the 20 – 40 year frequency component of the data. But, the p-value may also be overstated for bias reasons. The table indicates that there is a small sample bias in this correlation, since the small sample mean, -0.35, is substantially larger than the corresponding probability limit of -0.45. This bias may, at least in part, be the reason the VAR's small sample mean overstates the pre-1960s sample mean of -0.51. A bias-adjustment procedure would adjust the coefficients of the estimated pre-1960s VAR so that the implied small sample mean lines up better with the pre-1960s empirical estimate. Presumably, such an adjustment procedure would shift the simulated correlations to the left, reducing the p-value. It is beyond the scope of our analysis to develop a suitable bias adjustment method.50 However we suspect that, given the large magnitude of the bias, the bias-corrected p-value would be substantially smaller than the 14 percent value reported in the table.51

4Consistent with these observations, when inflation and unemployment are detrended using a linear trend with a break in slope (not level) in 1980:4 for inflation and 1983:1 for unemployment, the scatter plot of the detrended variables show a negative relationship. The regression of detrended inflation on detrended unemployment has a coefficient of -0.31, with t statistic of -4.24 and R2 = 0.037. The slope coefficient is similar to what was obtained in an earlier footnote for the pre-1960s period, but the R2 is considerably smaller.

inflation and unemployment is 0.06 and the p-value for these correlations in the 20 – 40 year range is 0.11.

49We redid the calculations in both panels of Table 4 using a 5-lag VAR and found that the results were essentially unchanged. The only notable differences in the results are that the p-value for the business cycle correlations between


<!-- p:33 -->


s0One could be developed along the lines pursued by Kilian (1998).

siTo get a feel for the likely quantitative magnitude of the effects of bias adjustment, we redid the bootstrap simulations by adjusting the varianc-covariance matrix of the VAR disturbances used in the bootstrap simulations. Let V = [V]ij denote the variance-covariance matrix. In the pre-1960s estimation results, Vi,a = -0.1024, Vi.1 = 0.0018, V2.2 = 6.0653. When we set the value of Vi.2 to -0.0588 and recomputed the entries in Table 4, we found that the mean correlations were as follows: business cycle, -0.75 (0.01); 8-20 year: -0.54 (0.09); 20–40 year: -0.51 (0.06). The numbers in parentheses are the analogs of the p-values in Table 4. Note how the mean correlation in the 20-40 year frequency coincides with the empirical estimate reported in the first row of Panel A of Table 4, and that the p-value has dropped substantially, from 0.23 to 0.06. This confirms our conjecture that bias adjustment may have an important impact on the p-value for the 20-40 year correlation. However, the other numbers indicate that the bias adjustment procedure that we applied, by varying Vi.2 only, is not a good one. Developing a superior bias adjustment method is clearly beyond the scope of this paper.


<!-- p:34 -->


| Table 5: Testing Null Hypothesis That Post-1960s Equal pre-1960s Correlations - Frequency - Panel A: DGM, Bivariate VAR with CPI Inflation (x) and Unemployment (y) - 2-8 year - 8-20 year - 20-40 year - Panel B: DGM,_Bivariate VAR with CPI Inflation (x) and M2 Growth (y) - 2-8 year - 8-20 year - 20-40 year   | Table 5: Testing Null Hypothesis That Post-1960s Equal pre-1960s Correlations - Plim - Panel A: DGM, Bivariate VAR with CPI Inflation (x) and Unemployment (y) - -0.66 - -0.36 - -0.45 - Panel B: DGM,_Bivariate VAR with CPI Inflation (x) and M2 Growth (y) - 0.49 - 0.73 - 0.78   | Table 5: Testing Null Hypothesis That Post-1960s Equal pre-1960s Correlations - Small Sample - Mean - Panel A: DGM, Bivariate VAR with CPI Inflation (x) and Unemployment (y) - -0.61 - -0.38 - -0.35 - Panel B: DGM,_Bivariate VAR with CPI Inflation (x) and M2 Growth (y) - 0.48 - 0.64   | Table 5: Testing Null Hypothesis That Post-1960s Equal pre-1960s Correlations - Std. Dev., Small - Sample Mean - Panel A: DGM, Bivariate VAR with CPI Inflation (x) and Unemployment (y) - 0.0036x - 0.0079x '/öö - 0.0129xiñö - Panel B: DGM,_Bivariate VAR with CPI Inflation (x) and M2 Growth (y) - 0.0044x '/&iö - 0.0062x - 0.0099x   | Table 5: Testing Null Hypothesis That Post-1960s Equal pre-1960s Correlations - p-value - Panel A: DGM, Bivariate VAR with CPI Inflation (x) and Unemployment (y) - 0.09 - 0.25 - 0.14 - Panel B: DGM,_Bivariate VAR with CPI Inflation (x) and M2 Growth (y) - 0.00 - 0.37   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Notes: (i) Data Generating Mechanism (DGM) in all cases is 3-lag, Bivariate VAR fit to pre-1960s data. (ii) P-value: frequency, in 2000 artificial post-1960s data sets, that contemporaneous correlation between indicated frequency components of x and y exceeds, in absolute value, corresponding post 1960s estimate. (iii) Plim: mean, over 1,000 artificial samples of length 2,000 observations each, of correlation.

- (iv) Small Sample Mean: mean of correlation, across 2000 artificial post-1960s data sets.
- (v) Std. dev., small sample (product of Monte Carlo std. error for mean and √2000) :

stanti  ss at stod ett a si ait orins

The low-frequency observations on unemployment have been documented using other methods (see, for example, Barro (1987, Chapter 16)). Similarly, using the Baxter-King band-pass filtering approach, the presence of the Phillips curve in the business cycle frequency range has been documented by King and Watson (1994) and Stock and Watson (1998) (see also Sargent (1999, p.12)). What has not been documented is how far the Phillips curve extends into the low frequencies of the post war data. In addition, we draw attention to the evidence that inflation leads unemployment in the low frequency range. We think these frequency domain properties of inflation and unemployment are interesting because we suspect that they pose a challenge for at least simple versions of conventional interpretations of the post war data.

One such interpretation is articulated by the theory developed in Kydland and Prescott (1977) and Barro and Gordon (1983), which builds on the idea of the expectations-augmented Phillips curve initially suggested by Friedman (1968) and Phelps (1968).52 The basic idea is that institutional impediments that had previously constrained US monetary policy, such as the gold standard, ceased to do so by the early 1960s. With institutional constraints impeding discretionary monetary policy minimized, a new monetary regime was initiated, in which the monetary authority set out to improve economic performance by attempting to actively exploit the Phillips curve. But, according to this view, the Phillips curve is merely a statistical relation, and does not represent a menu of inflation, un  o   o d o  s   tat s don theory predicts that the new monetary regime should have caused it to disappear, and be replaced by a deterministic, positive relationship between inflation and unemployment.53


<!-- p:35 -->


Our scatter diagrams show that before the 1960s inflation and unemployment are negatively related, while they are positively related after the 1960s. At first glance, this appears to be a resounding victory fot at   d a  r t tt  bn a   tioen series and is formalized using the band pass filter suggests a different picture. The simple version of the Barro-Gordon theory implies that, after 1960, the Phillips curve relationship should have evaporated, not just at the low frequencies, but at all frequencies. It also implies that inflation and unemployment should be perfectly in phase. Both these implications appear to be contradicted by the data.

Barro and Gordon (1983, pp. 601-602) recognize these extreme implications of their theory and describe an extension to their model that is designed to deal with them. The extension involves making the (plausible) assumption that the monetary authority's control over inflation is imperfect, perhaps because of lags in the effects of monetary actions. Under these conditions, inflation surprises occur, thus opening up the possibility that the forecast errors between infiation and unemployment might be negatively correlated. In turn, this may put the model into better conformity with the observation that there is a Phillips curve in the high frequencies, but not in the low frequencies.

s2Our discussion builds on Ireland (1998), who emphasizes the importance of evaluating the time series implications of the Barro-Gordon model.

a(1-k) π=u, = &gt;0. γ

s3For convenience, we briefly remind the reader of the Barro-Gordon model. The loss function of the monetary authority is [(u - ku~)2 + γx2] /2, where γ &gt; 0 is 8 parameter that specifies the relative social cost associated with inflation, ; u is the actual unemployment rate; and u~ is the natural rate of unemployment, i.e., the rate that would prevail if inflation were at its expected level. Also, 0 &lt; k &lt; 1. Inflation surprises generate a fall in the unemployment rate according to the 'expectations augmented Phillips curve': u - u~ = -α(x - π°), α &gt; 0. where π° is expected inflation. At the time the monetary authority chooses its action, π* is a state variable. The policy maker's objective is to minimize: L(xjx°, u~) = { [a (π − x*) − (1 − k) uN]2 + γx2 } /2. Let π [x°, uN] = arg min L(x|x°, u~). Conventionaly, the Markv equilibrium concept is used, in which equilibrium π and x* depend only on u~, and not the past history of central bank actions. This equilibrium concept has the advantage that, in the Barro-Gordon model, it is unique. The equilibrium is an expectation function, π"(u~), with the property x"(u~) = π [x"(u~), u~}, so that, in a Markov equilibrium, u = u~. Examining the first order condition associated with the monetary authority's problem and imposing the fixed point condition, implies

The microeconomic environment in the Barro-Gordon theory is specified at the reduced form level. Environments in which preferences and technology are stated explicitly, and which capture elements of the Barro-Gordon analysis may be found in Ireland (1997), and Chari, Christiano and Eichenbaum (1998).


<!-- p:36 -->


Perhaps it is possible to reconcile the last observation with plausible implementation delays.54 However, we suspect that it will be difficult to identify variations on the model that make it consistent with the observation that inflation leads unemployment in the low frequency range.s5 This phase relationship calls into question a basic feature of the Barro-Gordon model, according to which policy makers set inflation in response to developments in unemployment. A fruitful approach may be to explore modifications of the theory, in which policymakers' incentives to inflate are driven by variables that exhibit a more plausible timing relationship to inflation than unemployment.

We hope that this discussion demonstrates that statistics based on approximations to the band pass filter have a potentially useful role to play in helping us think about the inflation, unemployment dynamics. This is true, whether they are used for evaluating a Barro-Gordon type conception of the inflation process, or some other conception.56

Ireland (1998) introduces a one period lag, and he shows that this is this is strongly rejected by the data. In addition to considering longer implementation lags, another potentially useful modification would introduce rigidities that lead inflation surprises to have long-lasting effects. In the standard Barro-Gordon model, the effect of such a surprise is only contemporaneous.

ssOur skepticism is based in part on analysis of an extension of Ireland (1998)'s version of the Barro-Gordon model in which a one-period implementation lag is replaced by a p &gt; 0 period implementation lag in policy. Thus, we replace the p         =                 sd variable chosen p periods in the past by the policy maker, and θ  η captures the shocks that impact on π between the time i is set and π is realized. Here,

$$\theta * \eta _ { 3 } = ( \theta _ { 0 } + \theta _ { 1 } L + \dots + \theta _ { p - 1 } L ^ { p - 1 } ) \eta _ { 3 } ,$$

where η is a white noise and L is the lag operator. The policymaker's problem is optimized by setting i = ψü~, where u is the forecast of the natural rate of unemployment available at the time π is selected. As in footnote 37, we suppose that u~ is a random walk with innovation ν, so that u~ = u" + g * ν, where

$$g * \nu _ { t } = ( 1 + \mathcal { L } + \dots + \mathcal { L } ^ { r - 1 } ) \nu _ { t } .$$

Suppose the Lucas supply curve is u = u~ – a(π - x*) + ε, where ε is a shock. We impose rational expectations, which implies π = i. Then, it is easy to verify that inflation and unemployment evolve according to

$$\pi _ { t } \dot { = } \psi \frac { L \mathcal { P } } { 1 - L } \nu _ { t } + \theta ( L ) \eta _ { t } , \, u _ { t } = \frac { 1 } { 1 - L } \nu _ { t } - \alpha \theta ( L ) \eta _ { t } + \epsilon _ { t } ,$$

respectively. We make the simplifying assumption that all shocks are uncorrelated with each other. Then, the cross spectrum between these variables is:

$$g _ { \infty } ( \omega ) = \psi \sigma _ { \nu } ^ { 2 } \left [ \frac { e ^ { - i \omega \nu } } { ( 1 - e ^ { - \omega \nu } ) ( 1 - e ^ { i \omega \nu } ) } - \frac { a } { \psi } \theta ( e ^ { - \omega \nu } ) \theta ( e ^ { - \omega \nu } ) \lambda \right ] ,$$

where λ = σ2/σ2. The phase angle, θ(ω), between inflation and unemployment is:

$$\theta ( \omega ) = \tan ^ { - 1 } \left [ \frac { i m a g n i a r y \left [ g _ { r } ( \omega ) \right ] } { \real { \left [ g _ { r } ( \omega ) \right ] } } \right ] = \tan ^ { - 1 } \left [ \frac { - \sin ( p \omega ) } { \cos ( p \omega ) - 2 ( 1 - \cos ( \omega ) ) \frac { \theta ( e ^ { r } - 1 ) \theta ( e ^ { r } - 1 ) \lambda } { \theta ( e ^ { r } - 1 ) \theta ( e ^ { r } - 1 ) \lambda } \right ] ,$$

subject to −π ≤ θ(ω) ≤ π. It is easy to verify that for ω sufficiently small, θ(ω)/ω = p, so that infation lags unemployment

sé An alternative approach, based on the assumption that policy makers have bounded rationality, is pursued in Sargent

by p periods at these frequencies.


<!-- p:37 -->


### 5.2. Money Growth and Inflation

Figure 11a displays annual M2 growth and CPI inflation for in the pre-1960s period. The figure suggests, and the results in Table 4 confirm, that the two variables move very closely with each other. The primary exception appears to be the period of the second world war, when M2 growth was strong and inflation rose relatively less. But, this presumably reflects the effects of wage and price controls. The impression of the strong contemporaneous correlation at all frequencies is confirmed by the evidence in Figures 11b - 11d. Now consider Figures 12a-d. These depict the same data over the post-1960 period. Note first that there is essentially no difference in the 20-40 year frequency. In this band, money growth and inflation are highly correlated and there is very little phase shift between the two. However, there is a striking change in the relationship at the higher frequencies. The two variables are now strongly negatively correlated. According to Table 5, the null hypothesis that the business cycle and 8-20 year correlations in the post-1960s coincide with the corresponding pre-1960s correlation is strongly rejected. The change appears to be that in these frequencies, inflation now lags money growth by a few years. We think these are interesting statistics which a good model of money ought to confront.57

## 6. Conclusion

The theory of spectral analysis informs us that data can be viewed as the sum of uncorrelated components with different frequencies of fluctuation. This way of thinking about the data makes rigorous a perspective that is standard in macroeconomics: that the data are the sum of low frequency components, a business cycle component and a high frequency component. The various components can in principle be extracted by a suitably chosen 'ideal' band-pass filter.

Unfortunately, application of the ideal band pass filter requires substantially more data than is available in typical macroeconomic time series. This is not surprising. A subinterval of frequencies in a time series is composed of a continuum of objects, and in general there is no way that a discrete set of observations can pin these down. However, if something is known about the time series representation that generated the data, then it is possible to use projection theory to extrapolate from the observed time series to the frequency components of interest. We derive a set of formulas for this that are valid under standard time series representations, and are easy to implement. We identify one approximation which, though it is only optimal for one particular time series representation, nevertheless works well for standard macroeconomic time series. It is displayed in the introduction.

'ae t   e  e de  e e (  't s '(t s e (r it has difficulty accounting for the burst of inflation in the late 1970s.

s7Lucas (1980) was also interested in examining the relationship between the low frequency components of inflation and money growth. However, rather than using an approximation to the band pass filter, he used an early precursor to what later became known as the Hodrick-Prescott filter. Our comments on the Hodrick-Prescott filter, stated in the previous section, aiso apply to Lucas' filter. We think the band pass filter represents an advance over that filter. In a comment on Lucas (1980), Whiteman (1984) presents a useful reminder of the pitfalls of trying to interpret statistics like those discussed in this paper without the assistance of explicit economic theory.


<!-- p:38 -->


To illustrate the use of our recommended filter approximation, we use it to characterize the change in the nature of the Phillips curve and the money-inflation relation before and after the 1960s. We find that there is surprisingly little change in the Phillips curve and substantial change in money grouthinfation relation. In this analysis, we display a bootstrap methodology for conducting statistical inference on statistics computed using filtered data.


<!-- p:39 -->


##### A. Derivation of the Filter

This Appendix derives the optimal filtering formulas analyzed in the body of the paper.

##### A.1. The Problem

In our discussion we feature the unit root case (i.e., θ(1) ≠ 0 in (2.8)) and indicate later how to adjust things to accommodate covariance stationarity. The problem is to optimize (2.7):

$$b _ { j } ^ { \prime } f _ { j = - f , - p } ^ { \min } \int _ { \pi } \delta ( \omega ) \delta ( - \omega ) f _ { z } ( \omega ) d \omega ,$$

where f(ω) is defined in (2.9) and,

where where

and and

$$\delta ( \omega ) = B ( e ^ { - \omega } ) - \hat { B } ^ { \prime } \rho ( e ^ { - \omega } ) .$$

A necessary condition for an optimum is P(1) = 0. Without this, the criterion is infinite. With this condition,

is a finite-ordered polynomial in z:

$$b ( z ) = b _ { f - 1 } z ^ { p - 1 } + b _ { f - 1 } z ^ { p - 2 } + \dots + b _ { 0 } + \dots + b _ { - f + 1 } z ^ { - f + 1 } + b _ { - f } z ^ { - f } ,$$

with with

$$b _ { j } = - \sum _ { i = j + 1 } ^ { p } \hat { B } _ { i } ^ { f , p } , \, j = p - 1 , \dots , - f .$$

ae  f + de e  f + e ee e e e el, e  f e de ae ds g.

Write the criterion as follows:

$$b _ { j } = \min _ { P = 1 , \dots , - 1 } \int _ { - P } ^ { 1 } \bar { \delta } ( \omega ) \bar { \delta } ( - \omega ) g ( e ^ { - \omega } ) d \omega ,$$

$$\bar { \delta } ( \omega ) = \bar { B } ( e ^ { - i \omega } ) - b ( e ^ { - i \omega } ) ,$$

$$\tilde { B } ( z ) = \frac { B ( z ) } { 1 - z } .$$

$$b ( z ) = \frac { \hat { B } ^ { \prime } p _ { ( z ) } } { 1 - z } ,$$


<!-- p:40 -->


To obtain the first order conditions, note first that

so that,

Then, the first order conditions are:

$$\int _ { - \pi } ^ { \pi } \left [ \bar { \delta } ( \omega ) e ^ { i \omega j } + \bar { \delta } ( - \omega ) e ^ { - i \omega j } \right ] g ( e ^ { - i \omega j } ) d \omega = 0 , \ j = p - 1 , \dots , - f ,$$

or,

j = p - 1, .., -f. This expression reduces further to:

$$\int _ { - \pi } \bar { B } ( e ^ { - i \omega } ) g ( e ^ { - i \omega } ) e ^ { i j } d \omega = \int _ { - \pi } \bar { B } ( e ^ { - i \omega } ) g ( e ^ { - i \omega } ) e ^ { i j } d \omega ,$$

j = p − 1, .., − f.1 Our strategy for computing the BfP's is to translate the p + f equations, (A.2) into a system of linear equations in BjP, j = p,...,−f. We obtain the p + f + 1a equation in the Bj's from the fact, Bf-P(1) = 0.

We begin by replacing the system of p + f equations, (A.2), with another system composed of the equation with j = − f and the p + f − 1 equations formed by subtracting the j − 1th equation in (A.2) from the jth, j = p − 1, ..., − f + 1.

'To see this, note that

so that R is real. Consequently.

and

$$\int _ { - \pi } f ( \omega ) d \omega & = \int _ { - \pi } f ( - \omega ) d \omega , \\ 2 \int _ { - \pi } f ( \omega ) d \omega & = \int _ { - \pi } [ f ( \omega ) + f ( - \omega ) ] d \omega .$$


<!-- p:41 -->


##### A.2. Representing the Solution as a Solution to a System of Linear Equations

Consider the term on the left of (A.2). That term, evaluated at j, minus itself at j - 1, for j = p − 1, .., −f + 1, is:

$$& \int _ { - \pi } ^ { \pi } \{ \bar { B } ( e ^ { - i \omega } ) e ^ { i j } - \bar { B } ( e ^ { - i \omega } ) e ^ { i j - 1 } \} g ( e ^ { - i \omega } ) d \omega \\ & = \int _ { - \pi } ^ { \pi } \bar { B } ( e ^ { - i \omega } ) ( 1 - e ^ { - i \omega } ) e ^ { i j } g ( e ^ { - i \omega } ) d \omega \\ & = \int _ { - \pi } ^ { \pi } B ( e ^ { - i \omega } ) g ( e ^ { - i \omega } ) e ^ { i j } d \omega .$$

To evaluate this integral and others like it, we find it convenient to apply the well-known results:

$$\int _ { \pi } e ^ { i \omega h } d \omega \ = \ 0 , \, \text {for} \, h = \pm 1 , \, \pm 2 , \dots \\ \int _ { \pi } e ^ { i \omega } \ = \ 2 \pi , \, \text {for} \, h = 0 .$$

With this, it is easy to see that the integral in (A.3) is the product of 2π and the constant (i.e., the coefficient on z0) in the polynomial in z, B(z)g(z)z−j.

To evaluate the integral in (A.3), consider first the case q = 0, so that g(e-) = θ2. In this case, (A.3) reduces to 2π Bjθ2, where Bj is defined in (1.3). When q &gt; 0,

$$& \int _ { - \pi } ^ { \pi } B ( e ^ { - i \omega } ) g ( e ^ { - i \omega } ) e ^ { i \omega j } d \omega \\ & = \ 2 \pi \left ( B _ { j } c _ { 0 } + \sum _ { i = 1 } ^ { q } \left [ B _ { | j | + i } + B _ { | i | - i } \right ] c _ { i } \right ) ^ { \dots } \quad ^ { \circ } \\$$

The reason why the absolute value of j, ljl, appears in this expression is that the constant term in B(z)g(z)z-i corresponding to a given value of j, coincides with the constant term associated with -j. This is because B(z)g(z) = B(z−1)g(z−1).

Now consider the term on the right of (A.2). For j = p − 1,..., -f + 1, subtract that term minus itself at j - 1 to obtain:

$$& \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

This integral is the product of 2π and the constant term in the polynomial in z, f.P(z)g(z)z-j, for j = p − 1,...,−f + 1. When q = 0, this is 2πBθ2. When q &gt; 0,


<!-- p:42 -->


$$\int _ { - \infty } ^ { \infty } \dot { B } ^ { \prime \prime } ( e ^ { - i \omega } ) e ^ { i \omega j } g ( e ^ { - i \omega } ) d \omega = 2 \pi A _ { j } \hat { B } ^ { \prime \prime } ,$$

where /p is a p + f + 1 column vector:

$$\hat { B } ^ { l p } = \left \{ \begin{matrix} \end{matrix}$$

and Aj is a p + f + 1 row vector, j = p − 1, .., − f + 1. For p − q ≥ j ≥ q − f:

$$A _ { j } = \begin{bmatrix} 0 , \dots , 0 & , c , & 0 , \dots , 0 \\ 1 x ( \underbrace { - j - q } _ { 1 } ) & 1 x ( \underbrace { - j - q } _ { 1 } + n ) \end{bmatrix} ,$$

where c = [cq, Cq-1, . o, .., Cq-1, Cq] . When j = p − q, the first set of zeros is absent in Aj, and whenn j = q − f, the second set of zeros is absent. When j &gt; p − q, the first set of zeros is absent in Aj, and the first j – (p − q) elements of c are absent too. When j &lt; q – f, the last set of zeros is absent in Aj, and the last q - f - j elements of c are absent too.

We now consider equation (A.2) for j = −f :

$$\int _ { - \pi } \bar { B } ( e ^ { - i \omega } ) g ( e ^ { - i \omega } ) e ^ { - i \omega f } d \omega = \int _ { - \pi } ^ { \pi } b ( e ^ { - i \omega } ) e ^ { - i \omega f } g ( e ^ { - i \omega } ) d \omega .$$

This equation can be written

$$\int _ { a } ^ { a } \left [ \frac { i - \omega f } { 1 - e ^ { i \omega } } + \frac { e ^ { i \omega f } } { 1 - e ^ { i \omega } } \right ] g ( e ^ { - i \omega } ) d \omega = 2 \pi F b ,$$

x

where b = [bp-1: bp–2, .., o,...,b-s]' is a p + f− dimensional column vector and F is the p + f dimensional row vector:

$$F = [ \underbrace { 0 , \dots , 0 } _ { 1 \times ( p + f - q - 1 ) } , \underbrace { , c _ { q } , c _ { q - 1 } , \dots , c _ { 0 } ] } _ { 1 } .$$

If p + f - q – 1 = 0, the row vector is as above, with the zeros deleted. We want to express the right hand side of (A.8) in terms of Àfp instead of b. We do this using the matrix representation of the relation, (A.1):

$$Q \dot { B } ^ { t p } = b _ { 0 } ,$$


<!-- p:43 -->


where Q is the following (p + f) × (p + f + 1) matrix:

$$\varrho = \begin{bmatrix} - 1 & 0 & 0 & \cdots & 0 & 0 \\ - 1 & - 1 & 0 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ - 1 & - 1 & - 1 & \cdots & - 1 & 0 \end{bmatrix} .$$

Substitute (A.10) into (A.6) to get:

$$\begin{array} { l } \int _ { 0 } ^ { \infty } \left [ \frac { e ^ { - i \omega f } } { 1 - e ^ { - i \omega } } + \frac { e ^ { i \omega f } } { 1 - e ^ { i \omega } } \right ] g ( e ^ { - i \omega } ) d \omega = 2 \pi F Q \dot { B } ^ { \prime } P = 2 \pi A _ { - } \hat { B } ^ { \prime } P , \\ \end{array}$$

say, where A-j = FQ.

We have now achieved what we set out to do. We have a linear system of p + f + 1 equations in the p + f + 1 unknown B/P's. We summarize this as follows:

$$d = A \hat { B } ^ { f _ { 0 } } ,$$

$$\text {where} \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

where where

where Aj, j = p − 1, .., −f + 1 is defined in (A.7) and A\_/ = FQ, where Q is defined in (A.11) and F is defined in (A.9).

With a small adjustment to d and A, the filter weights are also determined by an expression like (A.12) when xt is covariance stationary. To indicate the adjustment, it is convenient to adopt a notational convention that is different from the one used in section 2 of the paper. In the covariance stationary case, we specify that xt has the representation

$$\tau _ { t } = \theta ( L ) \varepsilon _ { t } , \ E \varepsilon _ { t } ^ { 2 } = 1 ,$$

$$\theta ( z ) = \overset { \cdot } { \theta } _ { 0 } + \theta _ { 1 } z + \dots + \theta _ { q } z ^ { q } , \ q \geq 0 ,$$

where and the spectral density of θ(L)εt is g(e-), with


<!-- p:44 -->


$$g ( e ^ { - i \omega } ) = \theta ( e ^ { - i \omega } ) \theta ( e ^ { i \omega } ) = c _ { 0 } + c _ { 1 } ( e ^ { - i \omega } + e ^ { i \omega } ) + \dots + c _ { 0 } ( e ^ { - i \omega } + e ^ { i \omega } ) .$$

Here, c is the covariance function of θ(L)εt. As before, we wish to solve (2.6) subject to (2.5). The unknown filter weights satisfy the linear system, (A.12), in which all but the last two rows of A and d are unchanged. The last two rows of d contain ∫ B(e-)g(e−)edω for l = p and -f, respectively. The last two rows of A contain Ap and A\_f, where these are evaluated using (A.7).

A.3. The Solution

We solve for the 's using

$$\bar { B } ^ { f _ { 2 } } = A ^ { - 1 } d . \quad u \quad ( \Lambda . 1 4 )$$

When q = 0, this problem is very simple. In this case,

$$\hat { B } _ { j } ^ { ( j ) } & = B _ { j } , \, j = p - 1 , \dots , - f + 1 \\ \hat { B } _ { - j } ^ { ( j ) } & = \frac { 1 } { 2 \pi } \int _ { \Delta } ^ { \Delta } \left [ \frac { e ^ { - i \omega } } { 1 - e ^ { - i \omega } } + \frac { e ^ { i \omega } } { 1 - e ^ { i \omega } } \right ] \omega \\ \hat { B } _ { p } ^ { ( p ) } & = - \sum _ { j = p - 1 } ^ { - f } \hat { B } _ { j } ^ { ( j ) } .$$

It is of interest to note that, when p = f, pp(L) is a symmetric polynomial. To see this, note first that BP.P = Bj for j = p − 1,...,0,..., 1 − p and recall that the Bj's are themselves symmetric. But, is it the case that BpP = BPp? To see that this is indeed the case, note first from (A.1) that p = −bp-1. p But, after evaluating (A.2) at j = p − 1, we conclude:

$$\hat { B } _ { P } ^ { P P } = - \frac { 1 } { 2 \pi } \int _ { a } ^ { b } \left [ \frac { e ^ { - i \omega ( P - 1 ) } } { 1 - e ^ { - i \omega } } + \frac { e ^ { i \omega ( P - 1 ) } } { 1 - e ^ { i \omega } } \right ] d \omega .$$

Combining this with the middle expression in (A.15), evaluated at f = p, we find that Bp = BPp if. and only if

$$\int _ { 0 } ^ { 0 } \left [ \frac { e ^ { - i w } } { 1 - e ^ { - i w } } + \frac { e ^ { i w } } { 1 - e ^ { i w } } + \frac { e ^ { i w ( p - 1 ) } } { 1 - e ^ { - i w } } + \frac { e ^ { - i w ( p - 1 ) } } { 1 - e ^ { i w } } \right ] d w = 0 .$$

To see that this relationship indeed is satisfied, first collect terms in ep :

$$e ^ { i \omega p } \left [ \frac { 1 } { 1 - e ^ { i \omega } } + \frac { e ^ { - i \omega } } { 1 - e ^ { - i \omega } } \right ] = e ^ { i \omega p } \frac { 1 - e ^ { - i \omega } + ( 1 - e ^ { i \omega } ) e ^ { - i \omega } } { ( 1 - e ^ { i \omega } ) ( 1 - e ^ { - i \omega } ) } = 0 .$$


<!-- p:45 -->


The same is true for the term in e-ip. We conclude,

$$\hat { B } _ { p } ^ { p , p } = \hat { B } _ { - p } ^ { p , p } ,$$

so that when p = f and q = 0, the filter produced by this projection is symmetric.

##### A.4. Computational Note

Note from (A.7), (A.4), (A.13), that, with one exception, we have closed form expressions for all the objects- that are needed to solve our problem. The exception occurs in the unit root case, with the expression

$$R ( f ) = \int _ { 0 } ^ { b } \left [ \frac { e ^ { - i \omega f } } { 1 - e ^ { - i \omega } } + \frac { e ^ { i \omega f } } { 1 - e ^ { i \omega } } \right ] g ( e ^ { - i \omega } ) d \omega .$$

This expression could be solved using a numerical integration procedure. The drawback is that such computations take time, and, as emphasized in the paper, in practice the expression needs to be evaluated for many different values of f. For this reason, we now describe a quick way to evaluate this integral.

Note first that when f = 0,

$$\begin{array} { r l } { R ( 0 ) } & { = \int _ { a } ^ { b } \left [ \frac { 1 } { 1 - e ^ { - i j } } + \frac { 1 } { 1 - e ^ { i j } } \right ] g ( e ^ { - i j } ) d \omega } \\ & { = \frac { 1 } { 2 } \int _ { - x } ^ { x } B ( e ^ { - i j } ) g ( e ^ { - i j } ) d \omega , } \end{array}$$

since the object in square brackets is unity. The expression, R(0), can be evaluated using (A.4).

$$R ( f ) - R ( f + 1 ) \ = \ \int _ { \varnothing } ^ { \flat } \left ( e ^ { - i w f } + e ^ { i w f } \right ) g ( e ^ { - i w } ) d \omega \quad \\ \cdot \quad \cdot \quad \cdot \quad = \frac { 1 } { 2 } \int _ { - \pi } ^ { \pi } B ( e ^ { - i w } ) g ( e ^ { - i w } ) \left ( e ^ { - i w } + e ^ { i w } \right ) \dot { \omega } \quad \\ \cdot \quad \cdot \quad \cdot \quad = \int _ { - \pi } ^ { \pi } B ( e ^ { - i w } ) g ( e ^ { - i w } ) e ^ { - i w } d \omega .$$

The last integral in this expression can be evaluated using (A.4). This gives us a recursive way to compute R(0), R(1), .., using closed-form formulas.


<!-- p:46 -->


##### B. Second Moments of Aggregate Variables

We compare the second moment properties of aggregate time series, filtered using the various procedures discussed in this paper. Results are presented for various frequencies: the high frequencies with period of oscillation between 2 and 6 quarters; business cycle frequencies with period of oscillation between 6 and 32 quarters; low frequencies with period of oscillation between 32 and 80 quarters; and very low frequencies with period of oscillation between 80 and 160 quarters. We also present results based on combining the high and business cycle frequencies, so that we can do a direct comparison with results based on the HP filter.

Our findings are presented in Tables B.1-B.5. The tables are differentiated according to the frequency band isolated by the filter method used. The band pass filter approximations considered are Random Walk, Random Walk Fixed, Random Walk Symmetric, the Baxter-King method (BK), and Trigonometric Regression. All but the last two of these methods are defined in Table 2. BK is den    s          e   s always the same, and sets λ = 1600. The data cover the period 1948 to 1998. In most cases, they are logged prior to filtering. Exceptions are cases where the variable can potentially be negative. Thus, '(Ex-Im)/GDP' represents net exports deflated by GDP, and this is not logged. The same is true for 'Chg Invntry/GDP' which is the change in the stock of inventories (i.e., inventory investment), scaled by GDP. In addition, interest rates have not been logged.

Our basic finding is that results are very similar across the different filtering methods, except at the very lowest frequencies. There, they differ sharply. It is our impression that nothing of substantive turns on which filter is used to isolate the higher frequency components of the data.

Three observations about the sensitivity of the Random Walk results to the choice of frequency band are worth noting. First, consistent with findings in Hornstein (1998), the correlation between inventory investmnent and sales is negative in the high frequencies, and positive in the lower frequencies. Perhaps this reflects the predominance of different types of shocks in these frequency bands. Second. consumption is about 25 percent more volatile than output in the very lowest frequencies. This stands in striking contrast to its behavior in the higher frequencies, where consumption is substantially less volatile than output. Third, the correlation between the price level and output is more negative in the low frequencies than in the higher frequencies. On the other hand, the correlation between output and inflation increases as one goes from the high frequencies to the low frequencies. The switch in the sign of the correlation between inflation and output and the price level and output has been noted before (see Ball and Mankiw (1994), Christiano (1991), and Cooley and Ohanian (1991)), and has generated

I


<!-- p:47 -->


considerable discussion. That the phenomenon is more pronounced in the lower frequencies has not been noted before.


<!-- p:48 -->
