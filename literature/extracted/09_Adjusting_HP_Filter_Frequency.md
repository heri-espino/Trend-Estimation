---
id: "09_Adjusting_HP_Filter_Frequency"
source_pdf: "../pdf/09_Adjusting_HP_Filter_Frequency.pdf"
source_filename: "09_Adjusting_HP_Filter_Frequency.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/09_Adjusting_HP_Filter_Frequency.references.md"
---

<!-- p:1 -->

## NOTES

#### ON ADJUSTING THE HODRICK-PRESCOTT FILTER FOR THE FREQUENCY OF OBSERVATIONS

Morten O. Ravn and Harald Uhlig*

Abstract -This paper studies how the Hodrick-Prescott filter should be adjusted when changing the frequency of observations. It complements the results of Baxter and King (1999) with an analytical analysis, demonstrating that the filter parameter should be adjusted by multiplying it with the fourth power of the observation frequency ratios. This yields an HP parameter value of 6.25 for annual data given a value of 1600 for quarterly data. The relevance of the suggestion is illustrated empirically.

Baxter and King (1999) have recently shown that a value of around 10 for annual data is much more reasonable. They arrive at this value by visually inspecting the transfer function of the HP filter for annual data and comparing it to a bandpass filter. Hassler et al. (1992) had already obtained a similar value by investigating the average cycle length obtained in a time series of output.

## I. Introduction

T HE Hodrick and Prescott (1980, 1997) filter (hereafter, the HP filter) has become a standard method for removing trend movements in the business cycle literature. The filter has been applied both to actual data (Backus &amp; Kehoe, 1992; Blackburn &amp; Ravn, 1992; Brandner &amp; Neusser, 1992; Danthine &amp; Donaldson, 1993; Danthine &amp; Girardin, 1989; Fiorito &amp; Kollintzas, 1994; Kydland &amp; Prescott, 1990) and in studies in which artificial data from a model are compared with the actual data (Backus, Kehoe, &amp; Kydland, 1992; Cooley &amp; Hansen, 1989; Hansen, 1985; Kydland &amp; Prescott, 1982).

Although the use of the HP filter has been subject to heavy criticism (Canova, 1994, 1998; Cogley &amp; Nason, 1995; Harvey &amp; Jaeger, 1993; King &amp; Rebelo, 1993; So  ̈derlind, 1994), it has withstood the test of time and the fire of discussion remarkably well. Thus, although elegant new bandpass filters are being developed (Baxter &amp; King, 1999; Baxter, 1994; Christiano &amp; Fitzgerald, 1999), it is likely that the HP filter will remain one of the standard methods for detrending.

Most applications of this filter have been to quarterly data, but data is often available only at the annual frequency, whereas in other cases monthly data might be published. This raises the question of how one can adjust the HP filter to the frequency of the observations so that the main properties of the results are conserved across alternative sampling frequencies. Although most researchers have followed Hodrick and Prescott (1980, 1997) and used the value of 1600 for the smoothing parameter when using quarterly data, there is less agreement in the literature when moving to other frequencies. Backus and Kehoe (1992) use a value of 100 for annual data, whereas Correia, Neves, and Rebelo (1992) and Cooley and Ohanian (1991) suggest a value of 400.

Received for publication October 22, 1999. Revision accepted for publication May 10, 2001.

* London Business School and Centre for Economic Policy Research, and Humboldt University and Centre for Economic Policy Research, respectively.

We are grateful to James Stock, three anynomous referees, Albert Marcet, and Dan Knudsen for useful comments. We also thank Dave Backus for provision of data.

This paper complements these insights using two different analytical approaches. The first approach uses the time domain and focuses on the ratio of the variance of the cyclical component to the variance of the second difference of the trend component: this ratio is often used for calculating the smoothing parameter. For a particular benchmark stochastic process, it is shown that time aggregation changes this ratio by the fourth power of the observation frequency. The second approach uses the frequency domain and investigates the transfer function of the HP filter, thereby obtaining a general result. Again, a change-of-variable argument shows that one should adjust the HP parameter with approximately the fourth power of the frequency change. Both approaches therefore yield a value of approximately 1600/ 4 4 = 6.25 for annual data, which is close to the value of 10 given by Baxter and King (1999).

We then show that our recommendations work extremely well on U.S. GDP data: using a value of the smoothing parameter of 6.25 for annual data and 1600 for quarterly data produces almost exactly the same trend. This leads us to reconsider the business cycle 'facts' reported in earlier studies. As an example, we cast doubt on a finding by Backus and Kehoe (1992) on the historical changes in output volatility and return instead to older conventional wisdom (Baily, 1978; Lucas, 1977): output volatility turns out to have decreased after World War II.

The remainder of the paper is organized as follows. Section II presents the HP filter and provides the first, time domain-based approach, whereas section III provides the second, frequency domain-based approach. In section IV, we recompute some facts about business cycles. Finally, section V concludes.

## II. A Time Domain Perspective

The HP filter removes a smooth trend τ t from some given data yt by solving

$$& \text { for } & & \min _ { \tau _ { l } } \sum _ { t = 1 } ^ { T } ( ( y _ { t } - \tau _ { l } ) ^ { 2 } + \lambda ( ( \tau _ { l + 1 } - \tau _ { l } ) - ( \tau _ { l } - \tau _ { l - 1 } ) ) ^ { 2 } ) .$$

The residual yt - τ t (the deviation from the trend) is then commonly referred to as the business cycle component.


<!-- p:2 -->


The filter involves the smoothing parameter λ , which penalizes the acceleration in the trend relative to the business cycle component. Researchers typically set λ = 1600 when working with quarterly data. However, data does not always come at quarterly intervals. It may even be desirable to move to annual, monthly, or some other time interval of observation instead.

Thus, the question arises how the HP filter should be adjusted for the frequency of observations, and this question is the focus of this paper. We do not investigate whether the HP filter is desirable per se or aim at a comparison to some optimal bandpass filter as in Baxter and King (1999). Rather, we take it as granted that a researcher wishes to filter the data using the HP filter, and ask how the parameter λ should be adjusted when changing the sampling frequency.

Apopular perspective on the smoothing parameter in the literature is to consider the decomposition of some given time series yt into a trend τ t and a cycle ct :

$$y _ { t } = \tau _ { t } + c _ { t } & & ( 1 ) & \Delta _ { x } x$$

If ct as well as the second difference of τ t are normally and independently distributed, then the HP filter is known to be optimal, and λ is given as the ratio of the two variances, λ = σ c 2 / σΔ 2 τ t 2 (Hodrick &amp; Prescott, 1980, 1997; King &amp; Rebelo, 1993). However, even if the HP filter is optimal for equation (1), it is unlikely to be optimal when time aggregating the process (1) because time aggregation usually introduces moving average terms. As our focus is on adjusting λ , when changing the frequency of observation, we shall however ignore the issue of optimal filtering and instead simply focus on the question of how the ratio of the variances change.

It is convenient to consider a benchmark continuous-time version of equation (1) that satisfies the conditions previously stated, that is, where the cycle as well as the second difference of the trend are independently and normally distributed, taking the form of Brownian motion increments. 1 We then analyze the change in the variances when observing the process at discrete time intervals. Let yt be the 'flow' dzt of some stochastic process zt with

$$d z _ { t } = \tau _ { t } d t + \sigma _ { c } d W _ { t } ^ { 1 } & & ( 2 ) & \int _ { t i n o } ^ { \text {Substitition} }$$

where

$$d \tau _ { t } = \mu _ { t } d t , \, d \mu _ { t } = \sigma _ { \tau } d W _ { t } ^ { 2 } \quad ( 3 )$$

and dWt 1 and dWt 2 are two independent Brownian motions. There are two possibilities for observing the process at some discrete time interval α : these observations may be time aggregated (or time averaged) or they may be sampled at these discrete time intervals. (See Christiano and Eichenbaum (1986).)

1 See the appendix of Ravn and Uhlig (2001) for a discrete time analysis and for an extended discussion of the links with optimal filtering.

Consider time aggregation first; that is, for some length α &gt; 0, consider observing

$$\alpha & > 0 , \, \text {considering} \\ y _ { t ; \alpha } & = \int _ { s = 0 } ^ { \alpha } d z _ { t - s } = \tau _ { t ; \alpha } + c _ { t ; \alpha }$$

where

$$\text {where} \\ \tau _ { t ; \alpha } = \int _ { s = 0 } ^ { \alpha } \mu _ { t - s } d s ,$$

$$j _ { s = 0 } ^ { \alpha } \\ c _ { t ; \alpha } = \int _ { s = 0 } ^ { \alpha } \sigma _ { c } d W _ { t } ^ { 1 } .$$

For any stochastic process xt , define the α -differencing operator

$$\Delta _ { \alpha } x _ { t } = x _ { t } - x _ { t - \alpha } .$$

We are interested in how

$$\lambda _ { \alpha } = \frac { \sigma ^ { 2 } ( c _ { i ; \alpha } ) } { \sigma ^ { 2 } ( \Delta _ { \alpha } ^ { 2 } \tau _ { t ; \alpha } ) }$$

changes with α .

2 Clearly,

$$\sigma ^ { 2 } ( c _ { t ; \alpha } ) = \alpha \sigma _ { c } ^ { 2 } = \alpha \sigma ^ { 2 } ( c _ { t ; 1 } ) .$$

For Δα 2 τ t ; α , introduce first xt = Δατ t ; α and write it as

$$For \Delta _ { \alpha } ^ { 2 } \tau _ { t ; \alpha } , \, \text { introduce first } x _ { t } & = \Delta _ { \alpha } \tau _ { t ; \alpha } \\ x _ { t } & = \int _ { s _ { 1 } = 0 } ^ { \alpha } \left ( \mu _ { t - s _ { 1 } } - \mu _ { t - \alpha - s _ { 1 } } \right ) d s _ { 1 } \\ & = \int _ { s _ { 1 } = 0 } ^ { \alpha } \int _ { s _ { 2 } = 0 } ^ { \alpha } d \mu _ { t - s _ { 1 } - s _ { 2 } } d s _ { 1 } . \\$$

Substitute d μ t - s 1 - s 2 = xt - s 1 - s 2 ds 2 and repeat this calculation to obtain an expression of the second α difference,

$$\ t i o { \ t o b a i n a n } \exp x { \sigma _ { 1 } - \xi _ { 1 } - \xi _ { 2 } } & = \sigma _ { 1 } - \xi _ { 1 } - \xi _ { 2 } \, 2 \, d s \, 2 \, d \sigma \, \exp x { \sigma _ { 1 } - \xi _ { 2 } } \, 2 \, d s \, 2 \, d \sigma \, 2 \, d \sigma \, \exp ^ { 2 } \frac { \sigma _ { 1 } } { \sigma _ { 2 } } \, , \\ \intertext { s . } \Delta _ { \alpha } ^ { 2 } \tau _ { t ; \alpha } & = \sigma _ { \tau } \int _ { s _ { 1 } = 0 } ^ { \alpha } \int _ { s _ { 2 } = 0 } ^ { \alpha } \int _ { s _ { 3 } = 0 } ^ { \alpha } d W _ { t - s _ { 1 } - s _ { 2 } - s _ { 3 } } ^ { 2 } d s _ { 2 } d s _ { 1 } \\ \intertext { s . } & = \sigma _ { \tau } \int _ { s = 0 } ^ { 3 \alpha } A ( s ; \alpha ) d W _ { t - s } ^ { 2 } , \\ \intertext { l . } \intertext { a t }$$

where

2 One can equally well divide the processes by α to obtain time averaging rather than time aggregation: this makes no difference for λα and the calculation is very similar.


<!-- p:3 -->


$$A ( s ; \alpha ) = \int _ { s _ { 1 } = 0 } ^ { \alpha } \int _ { s _ { 2 } = 0 } ^ { \alpha } \, 1 _ { [ 0 , \alpha ] } ( s - s _ { 1 } - s _ { 2 } ) d s _ { 2 } d s _ { 1 }$$

and where the last equality was obtained by a change of variables, s = s 1 + s 2 + s 3. The variance is therefore given by

$$\text {by} \\ \sigma ^ { 2 } ( \Delta _ { \alpha } ^ { 2 } \tau _ { t ; \alpha } ) = \sigma _ { \tau } \int _ { s = 0 } ^ { 3 \alpha } A ( s ; \alpha ) ^ { 2 } d s . & & ( 4 ) \\ & \text {That is,} & & \text {adjusted}$$

Although one could calculate A ( s ; α ), one does not have to. Simply observe that

$$A ( s ; \alpha ) = \alpha ^ { 2 } A ( s / \alpha ; 1 ) .$$

With one more change of variable to s  ̃ = s / α in equation (4), we finally find

$$( 4 ) , \, \text {we finally find} \\ & \sigma ^ { 2 } ( \Delta _ { \alpha } ^ { 2 } \tau _ { r ; \alpha } ) = \alpha ^ { 5 } \sigma _ { \tau } \int _ { \tilde { s } = 0 } ^ { 3 } A ( \tilde { s } ; 1 ) ^ { 2 } d \tilde { s } = \alpha ^ { 5 } \sigma ^ { 2 } ( \Delta _ { 1 } ^ { 2 } \tau _ { r ; 1 } ) , & \quad \text {for} \\$$

and hence

$$\lambda _ { \alpha } = \frac { 1 } { \alpha ^ { 4 } } \, \lambda _ { 1 } .$$

That is, the HP parameter λ should be adjusted with the fourth power of the frequency change. This finding will be reconfirmed in section III, using another approach.

For sampling at discrete time intervals α , the calculations become simpler yet. Suppose we observe the flow yt = dzt at intervals α . 3 The diffusion part still has variance σ c 2 dt . What needs to be calculated is the variance of Δα 2 τ t . The same calculation as before leads to

$$\text {same calculation as before leads to} \\ \Delta _ { \alpha } ^ { 2 } \tau _ { t } & = \int _ { s _ { 1 } = 0 } ^ { \alpha } \int _ { s _ { 2 } } ^ { \alpha } \sigma _ { \tau } d W _ { t - s _ { 1 } - s _ { 2 } } ^ { 2 } \\ & = \int _ { s = 0 } ^ { 2 \alpha } B ( s ; \alpha ) d W _ { t - s } ,$$

where

$$\text {where} \\ B ( s ; \alpha ) = \int _ { s _ { 1 } = 0 } ^ { \alpha } 1 _ { [ 0 , \alpha ] } ( s - s _ { 1 } ) d s _ { 1 } = \alpha B ( s / \alpha ; 1 )$$

Similar to the calculation above, As one can see, the optimal adjustment is generally between 3.8 and 4.0 at the relevant frequencies.

3 Observing should be understood here in the sense that the continuoustime limit approximates some discrete time process at very small time intervals.

TABLE 1.-OPTIMAL POWER ADJUSTMENT AT FREQUENCY ω FOR AN ADJUSTMENT LOCALLY AROUND A QUARTERLY SAMPLING RATE

| ω         |   0 |   π /20 |   π /10 |   π /5 |
|-----------|-----|---------|---------|--------|
| m (1, ω ) |   4 |   3.992 |   3.967 |  3.868 |

$$\lambda _ { \alpha } ^ { ( s ) } = \frac { \sigma _ { c } ^ { 2 } d t } { \sigma ^ { 2 } ( \Delta _ { \alpha } ^ { 2 } \tau _ { t } ) } = \frac { 1 } { \alpha ^ { 3 } } \, \lambda _ { 1 } ^ { ( s ) } .$$

That is, the smoothing parameter for the HP filter should be adjusted using the third power of α . This result differs from the fourth-power result for the previous time-averaged data, but it also differs from the literature suggestion of adjusting with the second or the first power of α .

In practice, one may therefore wonder whether adjustment with the fourth or the third power is more appropriate. Our recommendation here is to always use the fourth power rather than the third. First, most macroeconomic time series are time averaged, so that the preceding calculation would suggest adjusting with the fourth power anyhow. But, even for the sampling case, simulations of this process shows that adjusting with the fourth power rather than the third produces essentially the same trend. The next section can be read as an explanation why this is the case.

## III. A Frequency Domain Perspective

An alternative way to look at the issue is from a frequency domain perspective, which allows us to provide a general result, as we no longer need to assume the special structure (2) and (3). The transfer function of the HP filter is given by (King &amp; Rebelo, 1993)

$$d z _ { t } & & & & 4 \lambda ( 1 - \cos \left ( \omega \right ) ) ^ { 2 } \\ \intertext { f o r } \frac { d t } { \text {The} } & & & h ( \omega ; \lambda ) = \frac { 4 \lambda ( 1 - \cos \left ( \omega \right ) ) ^ { 2 } } { 1 + 4 \lambda ( 1 - \cos \left ( \omega \right ) ) ^ { 2 } } & & & \\$$

This filter is similar to a high-pass filter. (See, for example, Ravn and Uhlig (1997) or Baxter and King (1999) for a plot of the transfer function.) Choosing different values for λ is comparable to choosing different values for the cutoff point of the high-pass filter.

Let h ( ω ; λ 1 ) be the filter representation for quarterly data and let h ( ω / s ; λ s ) be the filter representation for an alternative sampling frequency, s , where we let s be the ratio of the frequency of observation compared to quarterly data ( s = 1/4 for annual data or s = 3 for monthly data). Then, ideally, we would like to have

$$h ( \omega ; \lambda _ { 1 } ) \approx h ( \omega / s ; \lambda _ { s } ) .$$

Although this cannot hold exactly for all ω , it should hold at least approximately. 4 To derive the appropriate adjustment The figure illustrates the HP filter trend components of U.S. real GDP sampled either at the quarterly frequency and using λ quarterly = 1600 (the solid line) or at the annual frequency using alternative values for λ annual . For λ annual = 6.25, the trend components are practically identical. To make the figure clearer, we have taken a linear trend out of the HP filter trend components.

4 By this equation we do not mean to say that the HP filter is 'optimal' in any sense; rather, it says that, as the frequency of the observations is altered, the filter-being optimal or not-should have approximately the same properties.


<!-- p:4 -->


FIGURE 1.-TREND COMPONENTS OF US REAL GDP

rule λ s , one could, in principle, find λ s as to minimize some distance metric between h ( ω ; λ 1) and h ( ω / s ; λ s ). However, we take a shortcut to this and specify a simple functional rule for this adjustment process: we apply the simple criterion to multiply λ with some power of the frequency adjustment, that is, to choose

$$\lambda _ { s } = s ^ { m } \lambda _ { 1 } .$$

Thus, the problem is to choose m so as to fit equation (6). Consider a marginal change in the observation frequency ratio s around s = 1, and look at its differential impact on the HP filter. For the correct adjustment, it should be the case that

$$\frac { d } { d s } \, h ( \omega / s ; \lambda _ { s } ) \approx 0 & & ( 8 ) \int _ { \ } w h e t h e$$

where d ds denotes the total derivative with respect to s . For each ω and s , this equation can be solved for the parameter m = m ( s , ω ): one finds that

$$m ( s , \omega ) = 2 \, \frac { \omega / s \, \sin \left ( \omega / s \right ) } { 1 - \cos \left ( \omega / s \right ) } .$$

If the power specification is appropriate, then this expression should be approximately constant over the range of 'relevant' frequencies, ω . Inspection of the transfer function shows that it suffices to restrict attention to values 0 ≤ ω ≤ π /5 (Ravn &amp; Uhlig, 1997). Table 1 lists values of m = m (1, ω ) = m ( s , ω s ) for ω in this range. The values in this table suggest that m = 4 (or something close to it) is an excellent choice if one wishes to make the transfer function invariant to the frequency of observation, thereby reconfirming the results of section II for time-aggregated data. The analysis furthermore shows that m = 4 is the exact outcome only at ω = 0: otherwise, a slightly lower number between, say, m = 3.8 and m = 4 might be more appropriate.

Thus, for λ quarterly = 1600, this implies that λ annual = 1600/4 4 = 6.25 (or 8.25 for m = 3.8) and λ monthly = 1600 H18528 3 4 = 129600 (104035 for m = 3.8).

Given these results, we now check how well this adjustment rule works in practice. We examine U.S. real GDP from the Bureau of Economic Analysis for the period 1947-2000 sampled at the quarterly and the annual frequency. We compare the trend component of the quarterly data using λ quarterly = 1600 with the trend components of the annual data using λ annual = 400, 100, 25, or 6.25. The results are shown in figure 1. 5 This figure clinches our case once more: the trend component of the quarterly data using λ quarterly = 1600 and the trend component of the annual data using λ annual = 6.25 are practically identical, whereas large differences are visible for λ annual = 400, 100, or 25.

## IV. Recomputing the Facts

Based on the preceding analysis, it seems natural to ask whether the modification of the rule for adjusting the smoothing parameter matters for reported business cycle 'facts.' For an application, we recompute some of the

5 To make the results visually clearer, we have removed a linear trend from the HP filter trend components.

TABLE 2.-OUTPUT VOLATILITY

|                | Standard Deviations (%) - I. Prewar   | Standard Deviations (%) - II. Interwar   | Standard Deviations (%) - III. Postwar   |   n = 4 - I/III |   n = 4 - II/III |   n = 2* - I/III |   n = 2* - II/III |
|----------------|---------------------------------------|------------------------------------------|------------------------------------------|-----------------|------------------|------------------|-------------------|
| Australia      | 3.77 (0.37)                           | 2.47 (0.35)                              | 1.40 (0.14)                              |            2.69 |             1.77 |              3.3 |               2.5 |
| Canada         | 3.13 (0.27)                           | 5.06 (0.77)                              | 1.50 (0.21)                              |            2.09 |             3.38 |              2.0 |               4.4 |
| Denmark        | 2.20 (0.17)                           | 2.45 (0.37)                              | 1.35 (0.15)                              |            1.63 |             1.82 |              1.6 |               1.8 |
| Germany        | 2.32 (0.21)                           | 5.26 (0.88)                              | 1.80 (0.24)                              |            1.29 |             2.92 |              1.5 |               4.4 |
| Italy          | 2.13 (0.20)                           | 2.60 (0.30)                              | 1.51 (0.14)                              |            1.41 |             1.72 |              1.2 |               1.8 |
| Japan          | 2.10 (0.27)                           | 2.47 (0.38)                              | 1.45 (0.18)                              |            1.45 |             1.70 |              0.8 |               1.0 |
| Norway         | 1.07 (0.09)                           | 2.89 (0.56)                              | 1.06 (0.12)                              |            1.01 |             2.72 |              1.1 |               2.0 |
| Sweden         | 1.73 (0.22)                           | 2.41 (0.47)                              | 1.03 (0.09)                              |            1.68 |             2.34 |              1.7 |               2.6 |
| United Kingdom | 1.54 (0.16)                           | 2.50 (0.30)                              | 1.27 (0.17)                              |            1.21 |             1.97 |              1.3 |               2.1 |
| United States  | 3.30 (0.35)                           | 4.91 (0.70)                              | 1.58 (0.17)                              |            2.09 |             3.11 |              1.9 |               4.1 |

Numbers from Backus and Kehoe (1992). Numbers in parentheses are standard errors computed from GMM estimations of the unconditional moments.


<!-- p:5 -->


TABLE 3.-THE CORRELATION OF PRICES AND OUTPUT

|           | n = 4 - I. Prewar   | n = 4 - II. Interwar   | n = 4 - III. Postwar   | n = 2* - I. Prewar   | n = 2* - II. Interwar   | n = 2* - III. Postwar   |
|-----------|---------------------|------------------------|------------------------|----------------------|-------------------------|-------------------------|
| Australia | 0.29 (0.14)         | 0.30 (0.18)            | - 0.26 (0.18)          | 0.60 (0.10)          | 0.59 (0.12)             | - 0.47 (0.11)           |
| Canada    | 0.11 (0.15)         | 0.69 (0.12)            | - 0.01 (0.15)          | 0.41 (0.13)          | 0.77 (0.08)             | 0.12 (0.16)             |
| Denmark   | 0.18 (0.12)         | 0.02 (0.26)            | - 0.60 (0.09)          | 0.18 (0.12)          | - 0.26 (0.25)           | - 0.48 (0.11)           |
| Germany   | 0.04 (0.13)         | 0.86 (0.06)            | - 0.17 (0.14)          | - 0.01 (0.15)        | 0.71 (0.09)             | 0.01 (0.16)             |
| Italy     | 0.01 (0.10)         | 0.14 (0.15)            | - 0.33 (0.14)          | - 0.02 (0.11)        | 0.58 (0.09)             | - 0.24 (0.14)           |
| Japan     | - 0.49 (0.11)       | - 0.18 (0.25)          | - 0.37 (0.18)          | - 0.45 (0.11)        | 0.03 (0.22)             | - 0.60 (0.10)           |
| Norway    | 0.47 (0.11)         | 0.16 (0.16)            | 0.57 (0.10)            | 0.65 (0.08)          | 0.16 (0.19)             | - 0.63 (0.08)           |
| Sweden    | - 0.08 (0.17)       | 0.23 (0.09)            | - 0.38 (0.09)          | 0.15 (0.13)          | 0.30 (0.10)             | - 0.53 (0.07)           |
| U.K.      | 0.16 (0.14)         | 0.14 (0.24)            | - 0.72 (0.08)          | 0.26 (0.12)          | 0.20 (0.21)             | - 0.50 (0.14)           |
| U.S.      | 0.05 (0.11)         | 0.75 (0.09)            | - 0.25 (0.21)          | 0.22 (0.11)          | 0.72 (0.13)             | - 0.30 (0.16)           |

Numbers taken from Backus and Kehoe (1992). Numbers in parentheses are standard errors.

results reported by Backus and Kehoe (1992) for a cross section of OECD countries using historical annual data. These authors used λ annual = 100, whereas we shall use λ annual = 6.25.

One of Backus and Kehoe's (1992) most interesting findings was that output volatility was higher in the interwar period than during the postwar period, but that there is no general rule as far as a comparison of the postwar period with the prewar (prior to World War I) period is concerned. This result is in contrast to the conventional wisdom of, for example, Burns (1960), Lucas (1977), and Tobin (1980) that output volatility declined after World War II relative to both earlier periods. Another interesting result was that prices changed from generally being procyclical before World War II to being countercyclical thereafter.

Table 2 lists the results for output volatility when using our recommended value for the smoothing parameter. We find that the difference in volatility between the prewar and the postwar period generally narrows and that, for most countries, there has been a decline in volatility in the postwar period relative to either the interwar period or the prewar period. 6 In contrast to Backus and Kehoe (1992), these results are in line with the traditional wisdom previously quoted. This is an important result that Baily (1978) and Tobin (1980) have interpreted in terms of stabilization policy.

Table 3 reports the results for the cyclical behavior of the price level. There, and except for Norway, our results reconfirm the finding of Backus and Kehoe (1992), that prices have become countercyclical in the postwar period and that the interwar period historically was the period in which procyclicality was most pronounced. That is, this result seems to be fairly robust to the choice of the smoothing parameter. These results are also in line with other studies, such as Cooley and Ohanian (1991) and Ravn and Sola (1995).

6 By this we do not mean to challenge Romer's, 1989 argument that the high prewar volatility is due to measurement error. However, one should notice that, for example, UK data do not suffer from these measurement problems.

## V. Conclusions

This paper provides an analytic investigation into how the smoothing parameter, λ , of the HP filter should be adjusted when changing the frequency of observation. The major conclusion is that the λ parameter should be adjusted according to the fourth power of a change in the frequency of observations. For annual observations, this suggests setting λ = 6.25, which is close to the value found in Baxter and King (1999), but different from the value λ = 100 or λ = 400 typically found in the literature. Some well-known comparisons of business cycles moments across countries and time periods have been recomputed using the recommended fourth-power adjustment. In particular, we cast doubt on a finding by Backus and Kehoe (1992) and return instead to older conventional wisdom (Baily, 1978; Lucas, 1977; Tobin, 1980): based on the new HP filter adjustment rule, output volatility turns out to be lower in the postwar period compared to the prewar period.

#### IDIOSYNCRATIC RISK AND VOLATILITY BOUNDS, OR CAN MODELS WITH IDIOSYNCRATIC RISK SOLVE THE EQUITY PREMIUM PUZZLE?

Martin Lettau*

## I. Introduction

R ECENTLY, there has been of lot of interest in computing asset prices in incomplete market models; see, for example, Constantinides and Duffie (1996), Heaton and Lucas (1996), den Haan (1996), Krusell and Smith (1997) and Storesletten, Telmer, and Yaron (1997). These papers have shown that market incompleteness can affect prices of financial assets qualitatively. In this paper, I propose a simple method to check whether these effects are quantitatively important enough to solve the equity premium puzzle.

Received for publication April 20, 1999. Revision accepted for publication May 10, 2001.

* Federal Reserve Bank of New York and Centre for Economic Policy Research.

This paper was written during a visit at the Department of Economics at New York University; I am grateful for its hospitality. John Campbell, Mark Gertler, Blake LeBaron, Sydney Ludvigson, Anthony Lynch, Harald Uhlig, two anonymous referees, and seminar participants at Humboldt University, New York University, and the Federal Reserve Bank of New York provided helpful comments. The views are those of the author and do not necessarily reflect those of the Federal Reserve Bank of New York or the Federal Reserve System.

The main argument is as follows. Most incomplete market models specify endogenous endowment (labor income) shocks that are not fully insurable. Agents are allowed to trade in a small number of securities and solve for their optimal portfolio and consumption policies. It is difficult to test these types of models directly because the quality of household-level consumption data is very poor. 1 Instead of this direct approach using consumption data, I use data on individual income, which is measured more precisely than is individual consumption. In other words, I assume that agents cannot smooth idiosyncratic income shocks at all and are forced to consume their endowment. If agents were allowed to trade using some restricted set of securities, they would be able to smooth, at least partially, their individual shocks. Hence, the income process provides an upper bound on the volatility of individual consumption. If models with idiosyncratic risk are not able to generate large risk premia, they will most likely not be able to perform better with consumption data. I find even very volatile income shocks

1 One exception is Cogley (1998).


<!-- p:7 -->


### This article has been cited by:

1. Rainer Metz. 2010. Filter-design and model-based analysis of trends and cycles in the presence of outliers and structural breaks. Cliometrica 4 :1, 51-73. [CrossRef]
2. Andreas  Billmeier.  2010.  Ghostbusting:  which  output  gap  really  matters?. International  Economics  and  Economic  Policy 6 :4, 391-419. [CrossRef]
3. Carlo Ciccarelli, Stefano Fenoaltea, Tommaso Proietti. 2009. The effects of unification: markets, policy, and cyclical convergence in Italy, 1861-1913. Cliometrica . [CrossRef]
4. Sheila Dow, Matthias Klaes, Alberto Montagnoli. 2009. RISK AND UNCERTAINTY IN CENTRAL BANK SIGNALS: AN ANALYSIS OF MONETARY POLICY COMMITTEE MINUTES. Metroeconomica 60 :4, 584-618. [CrossRef]
5. Joseph H.  Davis, Christopher Hanes,  Paul W.  Rhode.  2009.  Harvests  and Business Cycles  in  Nineteenth-Century America*Harvests  and  Business  Cycles  in  Nineteenth-Century  America*. Quarterly  Journal  of  Economics 124 :4,  1675-1727. [Abstract] [PDF] [PDF Plus]
6. Ben Dolman. 2009. What Happened to Australia's Productivity Surge?. Australian Economic Review 42 :3, 243-263. [CrossRef]
7. Robert E. Evenson, Keith O. Fuglie. 2009. Technology capital: the price of admission to the growth club. Journal of Productivity Analysis . [CrossRef]
8. F . Carmignani. 2009. Endogenous Optimal Currency Areas: the Case of the Central African Economic and Monetary Community. Journal of African Economies . [CrossRef]
9. Davide Furceri. 2009. Fiscal Convergence, Business Cycle Volatility, and Growth. Review of International Economics 17 :3, 615-630. [CrossRef]
10. Lisa Chauvet, Patrick Guillaumont. 2009. Aid, Volatility, and Growth Again: When Aid Volatility Matters and When it Does Not. Review of Development Economics 13 :3, 452-463. [CrossRef]
11. Fernando Alvarez, Andrew Atkeson, Chris Edmond. 2009. Sluggish Responses of Prices and Inflation to Monetary Shocks in an Inventory Model of Money Demand*Sluggish Responses of Prices and Inflation to Monetary Shocks in an Inventory Model of Money Demand*. Quarterly Journal of Economics 124 :3, 911-967. [Abstract] [PDF] [PDF Plus]
12. Nir Jaimovich, Henry E Siu. 2009. The Young, the Old, and the Restless: Demographics and Business Cycle Volatility. American Economic Review 99 :3, 804-826. [CrossRef]
13. Carlo Rosa. 2009. Forecasting the Direction of Policy Rate Changes: The Importance of ECB Words. Economic Notes 38 :1-2, 39-66. [CrossRef]
14. Fabrizio Coricelli, Roman Horv￿￿th. 2009. Price setting and market structure: an empirical analysis of micro data in Slovakia. Managerial and Decision Economics n/a-n/a. [CrossRef]
15. Keith O. Fuglie. 2008. Is a slowdown in agricultural productivity growth contributing to the rise in commodity prices?. Agricultural Economics 39 , 431-441. [CrossRef]
16. Davide Furceri, Georgios Karras. 2008. Is the Middle East an Optimum Currency Area? A Comparison of Costs and Benefits. Open Economies Review 19 :4, 479-491. [CrossRef]
17. Alberto Alesina , Filipe R. Campante , Guido Tabellini . 2008. Why Is Fiscal Policy Often Procyclical?Why Is Fiscal Policy Often Procyclical?. Journal of the European Economic Association 6 :5, 1006-1036. [Abstract] [PDF] [PDF Plus]
18. S. J.-A. Tapsoba. 2008. Trade Intensity and Business Cycle Synchronicity in Africa. Journal of African Economies 18 :2, 287-318. [CrossRef]
19. Lourdes Acedo Montoya, Jakob Haan. 2008. Regional business cycle synchronization in Europe?. International Economics and Economic Policy 5 :1-2, 123-137. [CrossRef]
20. Rui Castro, Daniele Coen-Pirani. 2008. WHY HAVE AGGREGATE SKILLED HOURS BECOME SO CYCLICAL SINCE THE MID-1980s?. International Economic Review 49 :1, 135-185. [CrossRef]
21. Vincenzo Quadrini, Antonella Trigari. 2008. Public Employment and the Business Cycle. Scandinavian Journal of Economics 109 :4, 723-742. [CrossRef]
22. Maurizio Bovi. 2008. Shadow Employment and Labor Productivity Dynamics. Labour 21 :4-5, 735-761. [CrossRef]
23. Subrata Ghatak, José R. Sánchez-Fung. 2007. Is Fiscal Policy Sustainable in Developing Economies?. Review of Development Economics 11 :3, 518-530. [CrossRef]
24. Julián Messina, Giovanna Vallanti. 2007. Job Flow Dynamics and Firing Restrictions: Evidence from Europe. The Economic Journal 117 :521, 279-301. [CrossRef]
25. Carol Corrado, Paul Lengermann, Eric J. Bartelsman, J. Joseph Beaulieu. 2007. Sectoral Productivity in the United States: Recent Developments and the Role of IT. German Economic Review 8 :2, 188-210. [CrossRef]
26. Michael Tomz , Mark L. J. Wright . 2007. Do Countries Default in 'Bad Times' ?Do Countries Default in 'Bad Times' ?. Journal of the European Economic Association 5 :2-3, 352-360. [Abstract] [PDF] [PDF Plus]
27. Davide Furceri. 2007. Is Government Expenditure Volatility Harmful for Growth? A Cross-Country Analysis. Fiscal Studies 28 :1, 103-120. [CrossRef]
28. Roger Perman, Christophe Tavera. 2007. Testing for convergence of the Okun's Law coefficient in Europe. Empirica 34 :1, 45-61. [CrossRef]
29. Anthony Garratt, Donald Robertson, Stephen Wright. 2006. Permanent vs transitory components and economic fundamentals. Journal of Applied Econometrics 21 :4, 521-542. [CrossRef]
30. Davide Furceri. 2006. Does labour respond to cyclical fluctuations? The case of Italy. Applied Economics Letters 13 :3, 135-139. [CrossRef]
31. Kai Carstensen. 2006. Estimating the ECB Policy Reaction Function. German Economic Review 7 :1, 1-34. [CrossRef]
32. Roger Perman, Christophe Tavera. 2006. A cross-country analysis of the Okun's Law coefficient convergence in Europe. Applied Economics 37 :21, 2501-2513. [CrossRef]
33. José Sánchez-fung. 2006. Estimating a monetary policy reaction function for the dominican republic. International Economic Journal 19 :4, 563-577. [CrossRef]
34. Phan  M  Ngoc,  Phan  T  Nga,  Nguyen  T.  Phuong  Anh,  Shigeru  Uchida.  2005.  Effects  of  Cyclical  Movements  of  Foreign Currency Interest Rates and Exchange Rates on the Vietnamese Currency's Interest Rate and Exchange Rate. Asian Business &amp;#38; Management 4 :3, 315-330. [CrossRef]
35. Alessandra Iacobucci, Alain Noullez. 2005. A Frequency Selective Filter for Short-Length Time Series. Computational Economics 25 :1-2, 75-102. [CrossRef]


<!-- p:8 -->
