

<!-- BEGIN SOURCE 32/40: Liu_2022_common-risk-factors-cryptocurrency.md -->

# Source: `Liu_2022_common-risk-factors-cryptocurrency.md`

---
id: "Liu_2022_common-risk-factors-cryptocurrency"
source_pdf: "../pdf/Liu_2022_common-risk-factors-cryptocurrency.pdf"
source_filename: "Liu_2022_common-risk-factors-cryptocurrency.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/Liu_2022_common-risk-factors-cryptocurrency.references.md"
---

<!-- p:1 -->

NBER WORKING PAPER SERIES

COMMON RISK FACTORS IN CRYPTOCURRENCY

Yukun Liu Aleh Tsyvinski Xi Wu

Working Paper 25882 http://www.nber.org/papers/w25882

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 May 2019

We thank Nicola Borri, Markus Brunnermeier, Kent Daniel, Zhiguo He, Andrew Karolyi, Alan Kwan, Ye  Li,  Nikolai  Roussanov,  Jinfei  Sheng,  Michael  Sockin,  and  Jessica  Wachter  for comments. We are grateful to Colton Conley and Dean Li for their excellent research assistance. The views expressed herein are those of the authors and do not necessarily reflect the views of the National Bureau of Economic Research.

NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications.

© 2019 by Yukun Liu, Aleh Tsyvinski, and Xi Wu. All rights reserved. Short sections of text, not to  exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source.


<!-- p:2 -->


Common Risk Factors in Cryptocurrency Yukun Liu, Aleh Tsyvinski, and Xi Wu NBER Working Paper No. 25882 May 2019 JEL No. G12

#### ABSTRACT

We find that  three  factors  -  cryptocurrency  market,  size,  and  momentum  -  capture  the  crosssectional expected  cryptocurrency  returns.  We  consider  a  comprehensive  list  of  price-  and market-related factors in the stock market, and construct their cryptocurrency counterparts. Nine cryptocurrency factors form successful long-short strategies that generate sizable and statistically significant  excess  returns.  We show  that  all  of  these  strategies  are  accounted  for  by  the cryptocurrency three-factor model.

Yukun Liu Department of Economics Yale University New Haven, CT 06520-8268 yukun.liu@yale.edu

Aleh Tsyvinski Department of Economics Yale University Box 208268 New Haven, CT  06520-8268 and NBER a.tsyvinski@yale.edu Xi Wu Stern School of Business New York University New York, NY 10012 xwu@stern.nyu.edu


<!-- p:3 -->


## 1 Introduction

The cryptocurrency market has experienced rapid growth. This market allows companies to raise money without engaging with venture capitalists and to be traded without being listed on stock exchanges. The entire set of coins in the crypto market ranges from wellknown currencies such as Bitcoin, Ripple, and Ethereum to much more obscure coins. There are two views on the cryptocurrency market. The first is that most and perhaps all of the coins represent bubbles and fraud. The second is that the blockchain technology embodied in coins may become an important innovation and that at least some coins may be assets that represent a stake in the future of this technology. If the latter case is true, analyzing the cryptocurrency market from the empirical asset pricing point of view is important for at least two reasons. The first reason is to understand whether the returns of cryptocurrencies share similarities with other asset classes, most importantly, with equities. The second reason is to establish a set of empirical regularities that can be used as stylized facts and important inputs to assess and develop theoretical models of cryptocurrency.

In this paper, we study the cross-section of cryptocurrency returns. Our primary goal is to examine this market using standard empirical asset pricing tools. We consider all of the coins with market capitalizations above one million dollars and their returns from the beginning of 2014 to the end of 2018. The number of such coins grew from 109 in 2014 to 1,583 in 2018.

We examine whether the characteristics that are deemed important in the cross-section of equity returns are also present in the cryptocurrency market. We find that many of the known characteristics in the equity market also form successful long-short trading strategies in the cross-section of cryptocurrencies. In particular, three factors - cryptocurrency market, size, and momentum - capture most of the cross-sectional expected returns.

The literature on the stock market established a number of factors that explain the cross-section of stock returns. Among the factors compiled by Feng et al. (2017) and Chen and Zimmermann (2018), we select those that are constructed based only on price and market information - 25 such factors in total. We first describe the construction of the cryptocurrency counterparts for all these factors in the cross-section of cryptocurrencies. There are broadly four groups of factors: size, momentum, volume, and volatility. We also construct a coin market return using all of the coins for which the data is readily available. The coin market return series comprises 1,707 coins weighted by their market capitalization.

We then analyze the performance of all the 25 factors in the cryptocurrency market.


<!-- p:4 -->


Each week, we sort the returns of individual cryptocurrencies into quintile portfolios based on the value of a given factor. We track the return of each portfolio in the week that follows and calculate the average excess return over the risk-free rate of each portfolio. We then form the long-short strategy based on the difference between the fifth and the first quintiles. We find that the returns of the zero-investment strategies are statistically significant for 9 out of the 25 factors. Specifically, these are: market capitalization, price, and maximum price; one-, two-, three-, and four-week momentum; dollar volume; and standard deviation of dollar volume. We now turn to the detailed description of the results for each group of factors.

For the statistically significant size related strategies, a zero-investment long-short strategy that longs the smallest coins and shorts the largest coins generates more than 3 percent excess weekly returns (3.4 percent for the market capitalization, 3.9 percent for the end of week price, and 4.1 percent for the highest price of the week strategies). For the momentum strategies, a zero-investment long-short strategy that longs the coins with comparatively large price increases and shorts the coins with comparatively small increases generates about 3 percent excess weekly returns (2.7 percent for one-week momentum, 3.3 percent for two-week momentum, 4.1 percent for three-week momentum, and 2.5 percent for four-week momentum strategies). For the volume related strategies, a zero-investment strategy that longs the lowest volume coins and shorts the highest volume coins generates about 3 percent excess weekly returns (3.2 percent for the dollar volume). For the volatility strategy, a zero-investment strategy that longs the lowest dollar volume volatility coins and shorts the highest dollar volume volatility coins generates about 3 percent excess weekly returns. For all of these factors, the returns on individual quintile portfolios are almost monotonic with the quintiles. Determining the cryptocurrency factors that predict the cross-section of the entire cryptocurrency space is the first main result of the paper.

Next, we investigate whether these nine cross-sectional cryptocurrency return predictors can be spanned by a small number of factors. Our second main result is to develop a factor model for the cross-section of the cryptocurrency returns. We first consider a one-factor model with the coin market factor only. This is, in essence, a cryptocurrency CAPM model. The results are similar to those found in other asset classes - the model performs poorly in pricing the cross-section of the coin returns. The alphas for most of the successful zeroinvestment strategies remain large and statistically significant. The alphas for some of the strategies decrease marginally. The explanatory power of the model is low, with the R 2 s of the long-short strategies ranging from about zero percent for the one-week momentum to


<!-- p:5 -->


6.8 percent for the maximum day price strategies.

We next show that a three-factor model with the cryptocurrency market factor (CMKT), a cryptocurrency size factor (CSMB), and a cryptocurrency momentum factor (CMOM), accounts for the excess returns of all of the nine successful zero-investment strategies. Adjusted for the cryptocurrency three-factor model, none of the alphas of the nine strategies remains statistically significant. The CSMB factor accounts for the following strategies: market capitalization, price, maximum day price, dollar volume, and the standard deviation of dollar volume. The CMOM factor accounts for the two-week, three-week, and four-week momentum strategies. Both CSMB and CMOM account for the one-week momentum strategy. We conclude that the cryptocurrency three-factor model captures the cross-section of expected returns of cryptocurrencies.

Finally, we note several additional results. First, as the construction of the long-short strategies relies on the ability to short coins, a natural criticism of our findings is that short selling is either not possible or limited for most of the coins. We thus analyze each strategy that shorts Bitcoin instead of shorting the relevant quintile portfolio. The results virtually do not change. Second, we find that the momentum strategies perform significantly better among the larger coins. The momentum strategy in the below median size group generates statistically insignificant 0.6 percent weekly excess returns; the momentum strategy in the above median size group generates statistically significant 4.2 percent weekly returns. We also show that the stock market factor models, such as the Fama-French 3-factor, Carhart 4-factor, and the Fama-French 5-factor models, do not account for the cross-section of cryptocurrency returns. Additionally, we show that the procedure that removes the unpriced risks similar to Daniel et al. (2018) strengthens the cryptocurrency size factor but not the cryptocurrency momentum factor. One possible explanation is that loadings on the cryptocurrency momentum factor are more transient than loadings on the cryptocurrency size factor.

We briefly discuss the relationship to the literature. Size and momentum are among the most studied strategies in asset pricing. The size effect in the stock market is first documented in Banz (1981). Fama and French (1992) show that size and value are important factors in explaining the cross-section of expected stock returns. Our findings on momentum are related to many papers on the topic such as Jegadeesh and Titman (1993), Moskowitz and Grinblatt (1999), Moskowitz et al. (2012), Asness et al. (2013). The use of factor models to analyze asset returns dates back to the papers of Fama and French (1993) and Fama and French (1996). Lustig et al. (2011), Szymanowska et al. (2014), and Bai et al. (2018) develop factor models for the currency, commodity, and corporate bond markets, respectively.


<!-- p:6 -->


Yermack (2015) is one of the first papers that brings academic attention to the field of cryptocurrency. A number of recent papers develop models of cryptocurrencies (see, e.g., Weber, 2016; Biais et al., 2018a; Chiu and Koeppl, 2017; Cong and He, 2018; Cong et al., 2018a; Cong et al., 2018b; Sockin and Xiong, 2018; Schilling and Uhlig, 2018; Abadi and Brunnermeier, 2018; Routledge and Zetlin-Jones, 2018). Several recent papers document empirical facts related to cryptocurrency investments (e.g., Stoffels, 2017; Hubrich, 2017; Borri, 2018; Borri and Shakhnov, 2018a; Borri and Shakhnov, 2018b; Hu et al., 2018; Makarov and Schoar, 2018; Liu and Tsyvinski, 2018; Li and Yi, 2018).

## 2 Data

We collect trading data of all cryptocurrencies available from Coinmarketcap.com. Coinmarketcap.com is a leading source of cryptocurrency price and volume data. It aggregates information from over 200 major exchanges and provides daily data on opening, closing, high, low prices, volume and market capitalization (in dollars) for most of the cryptocurrencies. 1 For each cryptocurrency on the website, its price is calculated by taking the volume weighted average of all prices reported at each market. A cryptocurrency needs to meet a list of criteria to be listed, such as being traded on a public exchange with an API that reports the last traded price and the last 24-hour trading volume, and having a non-zero trading volume on at least one supported exchange so that a price can be determined. Coinmarketcap.com lists both active and defunct cryptocurrencies, thus alleviating concerns about survivorship bias.

We use daily close prices to construct weekly coin returns. Specifically, we divide each year into 52 weeks. The first week of the year consists of the first seven days of the year. The first 51 weeks of the year consist of seven days each and the last week of the year consists of the last eight days of the year. 2 Our sample includes 1,707 coins from the beginning of 2014 to the end of 2018. The trading volume data became available in the last week of 2013, and thus our sample period starts from the beginning of 2014. We require that the coins have information on price, volume, and market capitalization. We further exclude coins with market capitalizations of less than $1,000,000. To alleviate concerns for outliers, we winsorize all non-return variables by the 1st and 99th percentiles each week.

1 Some coins are not tracked by the website because the coins' exchanges do not provide accessible APIs.

2 The last week of 2016 consists of the last nine days of the year.


<!-- p:7 -->


The summary statistics are presented in Panel A of Table 1. The number of coins in our sample that satisfy all the filters increases from 109 in 2014 to 1,583 in 2018. The mean (median) market capitalization in the sample is 356.71 (8.17) million dollars. The mean (median) daily dollar volume in our sample is 18,305.83 (103.89) thousand dollars.

We construct a cryptocurrency market return as the value-weighted return of all the underlying available coins. The cryptocurrency excess market return (CMKT) is constructed as the difference between the cryptocurrency market index return and the risk-free rate measured as the one-month Treasury bill rate. The summary statistics are presented in Panel B of Table 1. During the sample period, the average coin market index return is 1.3 percent per week, which is higher than the average Bitcoin return (1.2 percent per week) but is lower than the average Ripple return (3.5 percent per week) or Ethereum return (4.6 percent per week). 3 The weekly standard deviation of the coin market index return is 0.117, which is slightly higher than that of Bitcoin (0.114) but much lower than those of Ripple (0.267) and Ethereum (0.241). The coin market index returns have positive skewness and kurtosis. Figure 1 plots the cryptocurrency market index against Bitcoin, Ripple, and Ethereum. The values are presented as the US dollar value of investing one dollar from the inception of the given cryptocurrency to facilitate comparisons. The figure shows strong correlations among the cryptocurrency market index and the investment values of the major coins.

We obtain the stock market factors for the Fama French 3-factor, Carhart 4-factor, and Fama French 5-factor models from Kenneth French's website.

3 Bitcoin, Ripple, and Ethereum are the three largest cryptocurrencies by market capitalization and thus form a natural reference group.


<!-- p:8 -->


##### Table 1: Summary Statistics

Panel A reports the number of coins, the mean and median of market capitalization, and the mean and median of daily trading dollar volume by year. Panel B reports the characteristics of coin market index returns, Bitcoin returns, Ripple returns, and Ethereum returns. The coin market index returns, Bitcoin returns, and Ripple returns start from the first week of 2014. The Ethereum returns start from the thirtysecond week of 2015.

| Panel A - Year   |   Panel A - Number of Coins |   Panel A - Market Cap (mil) - Mean |   Panel A - Market Cap (mil) - Median |   Panel A - Volume (thous) - Mean |   Panel A - Volume (thous) - Median |
|------------------|-----------------------------|-------------------------------------|---------------------------------------|-----------------------------------|-------------------------------------|
| 2014             |                         109 |                              239.83 |                                  3.89 |                          1,146.09 |                               36.24 |
| 2015             |                          77 |                              134.53 |                                  2.76 |                          1,187.64 |                               11.51 |
| 2016             |                         155 |                              160.06 |                                  3.39 |                          1,789.24 |                               23.73 |
| 2017             |                         804 |                              435.68 |                                  9.01 |                         18,509.55 |                              133.56 |
| 2018             |                       1,583 |                              357.20 |                                  8.91 |                         20,829.12 |                              124.02 |
| Full             |                       1,707 |                              356.71 |                                  8.17 |                         18,305.83 |                              103.89 |

| Panel B            |   Panel B - Mean |   Panel B - Median |   Panel B - SD |   Panel B - Skewness |   Panel B - Kurtosis |
|--------------------|------------------|--------------------|----------------|----------------------|----------------------|
| Coin Market Return |            0.013 |              0.006 |          0.117 |                0.294 |                4.574 |
| Bitcoin Return     |            0.012 |              0.005 |          0.114 |                0.367 |                4.580 |
| Ripple Return      |            0.035 |             -0.007 |          0.267 |                3.478 |               21.263 |
| Ethereum Return    |            0.046 |              0.001 |          0.241 |                1.841 |                9.843 |


<!-- p:9 -->


Figure 1: Cryptocurrency Market Index and Major Coins

This figure plots the cryptocurrency market index against Bitcoin, Ripple, and Ethereum.

<!-- p:10 -->


## 3 Cross-Sectional Factors

We consider a comprehensive list of the established factors in the cross-section of stock returns, compiled by Feng et al. (2017) and Chen and Zimmermann (2018). Among these, we select all the factors that can be directly constructed using only the information on price, volume, and market capitalization. The reason we consider only the market-based factors is that financial and accounting data for the cross-section of coins is either not readily available or not applicable. We hence investigate 25 factors, which we present in Table 2. We further group them into four broad categories: size, momentum, volume, and volatility.

### 3.1 Size Factors

We analyze the performance of the zero-investment long-short strategies based on the size-related factors: market capitalization, price, maximum price, and age. Each week, we sort individual cryptocurrencies into quintile portfolios based on the value of a given factor. We track the return of each portfolio in the week that follows. We then calculate the average excess returns over the risk-free rate of each portfolio, and the excess returns of the longshort strategies based on the difference between the fifth and the first quintiles. We find that the first three factors generate statistically significant long-short strategy returns. The result of the zero-investment long-short strategy for age is not statistically significant and is summarized in the last part of the section.

Table 3 presents the results. For the first three factors, the average mean excess returns decrease from the top to the bottom quintiles. The differences in the average returns of the highest and lowest quintiles are -3.4 percent for market capitalization, -3.9 percent for the end of week price, and -4.1 percent for the highest price of the week. All of these differences are statistically significant at the 5 percent level. In other words, a zero-investment strategy that longs the smallest coins and shorts the largest coins generates about 3 percent excess weekly returns. Of course, this strategy does not take into account trading costs and the feasibility of short selling. We consider strategies that short Bitcoin, and present results that long the smallest coins and short Bitcoin in Section 5. In the Appendix, we also present results based on tercile instead of quintile portfolios. 4 The results based on tercile portfolios are qualitatively similar.

4 The same robustness results are presented for all other successful strategies in the Appendix.


<!-- p:11 -->


Table 2: Factor Definitions

| Category   | Factor    | Definition                                                                                                                                                                                                                                                                                                                                |
|------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Size       | MCAP      | Log last day market capitalization in the portfolio formation week                                                                                                                                                                                                                                                                        |
| Size       | PRC       | Log last day price in the portfolio formation week                                                                                                                                                                                                                                                                                        |
| Size       | MAXDPRC   | The maximum price of the portfolio formation week                                                                                                                                                                                                                                                                                         |
| Size       | AGE       | The number of weeks that have been listed on Coinmarketcap.com                                                                                                                                                                                                                                                                            |
| Momentum   | r 1,0     | One-week momentum                                                                                                                                                                                                                                                                                                                         |
| Momentum   | r 2,0     | Two-week momentum                                                                                                                                                                                                                                                                                                                         |
| Momentum   | r 3,0     | Three-week momentum                                                                                                                                                                                                                                                                                                                       |
| Momentum   | r 4,0     | Four-week momentum                                                                                                                                                                                                                                                                                                                        |
| Momentum   | r 8,0     | Eight-week momentum                                                                                                                                                                                                                                                                                                                       |
| Momentum   | r 16,0    | Sixteen-week momentum                                                                                                                                                                                                                                                                                                                     |
| Momentum   | r 50,0    | Fifty-week momentum                                                                                                                                                                                                                                                                                                                       |
| Momentum   | r 100,0   | Hundred-week momentum                                                                                                                                                                                                                                                                                                                     |
| Volume     | VOL       | Log average daily volume in the portfolio formation week                                                                                                                                                                                                                                                                                  |
| Volume     | PRCVOL    | Log average daily volume times price in the portfolio formation week                                                                                                                                                                                                                                                                      |
| Volume     | VOLSCALED | Log average daily volume times price scaled by market capitalization in the portfolio formation week                                                                                                                                                                                                                                      |
| Volatility | BETA      | The regression coefficient i CMKT in R i R f = i + i CMKT CMKT + i . The model is estimated using daily returns of the previous 365 days before the formation week.                                                                                                                                                                       |
| Volatility | BETA2     | Beta squared                                                                                                                                                                                                                                                                                                                              |
| Volatility | IDIOVOL   | The idiosyncratic volatility is measured as the standard deviation of the residual after estimating R i R f = i + i CMKT CMKT + i . The model is estimated using daily returns of the previous 365 days before the formation week.                                                                                                        |
| Volatility | RETVOL    | The standard deviation of daily returns in the portfolio formation week                                                                                                                                                                                                                                                                   |
| Volatility | RETSKEW   | The skewness of daily returns in the portfolio formation week                                                                                                                                                                                                                                                                             |
| Volatility | RETKURT   | The kurtosis of daily returns in the portfolio formation week                                                                                                                                                                                                                                                                             |
| Volatility | MAXRET    | Maximum daily return of the portfolio formation week                                                                                                                                                                                                                                                                                      |
| Volatility | DELAY     | The improvement of R 2 in R i R f = i + i CMKT CMKT + i CMKT 1 CMKT 1 + i CMKT 2 CMKT 2 + i , where CMKT 1 and CMKT 2 are the lagged one and two day coin market index returns, compared to using only current coin market excess returns. The model is estimated using daily returns of the previous 365 days before the formation week. |
| Volatility | STDPRCVOL | Log standard deviation of dollar volume in the portfolio formation week                                                                                                                                                                                                                                                                   |
| Volatility | DAMIHUD   | The average absolute daily return divided by dollar volume in the portfolio formation week                                                                                                                                                                                                                                                |


<!-- p:12 -->


##### Table 3: Size Factor Returns

This table reports the mean quintile portfolio returns based on the market capitalization, last day price, and maximum day price factors. The mean returns are the time-series averages of weekly value-weighted portfolio excess returns. *, **, *** denote significance levels at the 10%, 5%, and 1%.

|         | Quintiles - 1   | Quintiles - 2   | Quintiles - 3   | Quintiles - 4   | Quintiles - 5   | Quintiles - 5-1   |
|---------|-----------------|-----------------|-----------------|-----------------|-----------------|-------------------|
| MCAP    | Low             |                 |                 |                 | High            |                   |
| Mean    | 0.047***        | 0.018           | 0.013           | 0.013           | 0.013*          | -0.034**          |
| t(Mean) | (2.958)         | (1.610)         | (1.286)         | (1.439)         | (1.766)         | (-2.557)          |
| PRC     | Low             |                 |                 |                 | High            |                   |
| Mean    | 0.051***        | 0.029**         | 0.001           | 0.018           | 0.012*          | -0.039**          |
| t(Mean) | (2.739)         | (2.118)         | (0.117)         | (1.419)         | (1.689)         | (-2.420)          |
| MAXDPRC | Low             |                 |                 |                 | High            |                   |
| Mean    | 0.053***        | 0.025*          | 0.002           | 0.021           | 0.012*          | -0.041**          |
| t(Mean) | (2.791)         | (1.905)         | (0.143)         | (1.568)         | (1.681)         | (-2.483)          |

### 3.2 Momentum

We analyze the performance of the zero-investment long-short strategies based on the one-, two-, three-, four-, eight-, sixteen-, fifty-, and one hundred-week momentum factors. Each week, we sort individual cryptocurrencies into quintile portfolios based on the value of a given factor. All strategies are rebalanced weekly. We find that the one-, two-, three-, and four-week momentum factors generate statistically significant long-short strategy returns. The results of the zero-investment long-short strategies for the eight-, sixteen-, fifty, and one hundred-week momentum are not statistically significant and are summarized in the last part of the section.

Table 4 presents the results of the successful factors for the portfolios sorted in quintiles. For the one-, two-, three-, and four-week momentum strategies, the average mean excess returns increase with the quintiles. The patterns are almost universally monotonic. The difference in the average returns of the highest and lowest quintiles is about 3 percent for each horizon and statistically significant at the 5 percent level (1 percent level for three-week momentum). In other words, a zero-investment strategy that longs the coins with comparatively large increases and shorts the coins with comparatively small increases generates about 3 percent excess weekly returns. The differences in the average returns of the highest and lowest quintiles are 2.7 percent for the one-week momentum, 3.3 percent for the two-week momentum, 4.1 percent for the three-week momentum, and 2.5 percent for the four-week momentum.


<!-- p:13 -->


##### Table 4: Momentum Factor Returns

This table reports the mean quintile portfolio returns based on the one-week, two-week, three-week, and fourweek momentum factors. The mean returns are the time-series averages of weekly value-weighted portfolio excess returns. *, **, *** denote significance levels at the 10%, 5%, and 1%.

|         | Quintiles - 1   | Quintiles - 2   | Quintiles - 3   | Quintiles - 4   | Quintiles - 5   | Quintiles - 5-1   |
|---------|-----------------|-----------------|-----------------|-----------------|-----------------|-------------------|
| r 1,0   | Low             |                 |                 |                 | High            |                   |
| Mean    | -0.006          | -0.002          | 0.010           | 0.042**         | 0.021           | 0.027**           |
| t(Mean) | (-0.552)        | (-0.176)        | (1.094)         | (2.317)         | (1.550)         | (1.994)           |
| r 2,0   | Low             |                 |                 |                 | High            |                   |
| Mean    | -0.002          | 0.005           | 0.010           | 0.018*          | 0.030**         | 0.033**           |
| t(Mean) | (-0.225)        | (0.493)         | (1.155)         | (1.894)         | (2.314)         | (2.442)           |
| r 3,0   | Low             |                 |                 |                 | High            |                   |
| Mean    | 0.002           | 0.001           | 0.016           | 0.020**         | 0.043***        | 0.041***          |
| t(Mean) | (0.156)         | (0.124)         | (1.587)         | (2.091)         | (2.956)         | (2.742)           |
| r 4,0   | Low             |                 |                 |                 | High            |                   |
| Mean    | 0.002           | 0.004           | 0.008           | 0.019*          | 0.027**         | 0.025**           |
| t(Mean) | (0.243)         | (0.435)         | (0.935)         | (1.921)         | (2.033)         | (2.002)           |


<!-- p:14 -->


### 3.3 Volume Factors

We analyze the performance of the volume-related factors: volume, dollar volume, and scaled volume. Each week, we sort individual cryptocurrencies into quintile portfolios based on the value of a given factor. All strategies are rebalanced weekly. The dollar volume strategy generates statistically significant long-short strategy returns. The results of the zero-investment long-short strategies based on the other volume factors are not statistically significant and are summarized in the last part of the section.

Table 5 presents the results for the portfolios sorted in quintiles based on the dollar volume factor. The average mean excess returns decrease with the quintiles. The patterns are mostly monotonic from the lowest to the highest quintiles. The difference in the average returns of the highest and lowest quintiles is -3.2 percent for the dollar volume factor. The difference is statistically significant at the five percent level. In other words, a zero-investment strategy that longs the lowest dollar volume coins and shorts the highest dollar volume coins generates about 3 percent excess weekly returns.

##### Table 5: Volume Factor Returns

This table reports the mean quintile portfolio returns based on the price dollar volume factor. The mean returns are the time-series averages of weekly value-weighted portfolio excess returns. *, **, *** denote significance levels at the 10%, 5%, and 1%.

|         | Quintiles - 1   | Quintiles - 2   | Quintiles - 3   | Quintiles - 4   | Quintiles - 5   | Quintiles - 5-1   |
|---------|-----------------|-----------------|-----------------|-----------------|-----------------|-------------------|
| PRCVOL  | Low             |                 |                 |                 | High            |                   |
| Mean    | 0.045**         | 0.028**         | 0.017           | 0.018           | 0.013*          | -0.032**          |
| t(Mean) | (2.438)         | (2.154)         | (1.375)         | (1.456)         | (1.745)         | (-2.016)          |

### 3.4 Volatility Factors

We analyze the performance of the volatility-related factors: beta, beta squared, idiosyncratic volatility, the standard deviation of returns, the skewness of returns, the kurtosis of returns, maximum day return, delay, the standard deviation of dollar volume, and Amihud's illiquidity measure. Each week, we sort individual cryptocurrencies into quintile portfolios on the value of a given factor. All strategies are rebalanced weekly. The standard deviation of dollar volume measure generates statistically significant long-short strategy returns, but the other factors do not. We summarize the insignificant volatility factors in the last part of the section.


<!-- p:15 -->


Table 6 presents the results for the portfolios sorted in quintiles for the standard deviation of dollar volume - the only factor out of ten in this group that generates statistically significant excess returns on the long-short strategies. For the standard deviation of dollar volume, the average mean excess returns of the portfolios decrease monotonically with the quintiles and are statistically significant for each quintile except quintile four. The difference in the average returns of the highest and lowest quintiles is -3.0 percent. In other words, a zero-investment strategy that longs the lowest dollar volume volatility coins and shorts the highest dollar volume volatility coins generates about 3 percent excess weekly returns. 5

##### Table 6: Volatility Factor Returns

This table reports the mean quintile portfolio returns based on the standard deviation of dollar volume factor. The mean returns are the time-series averages of weekly value-weighted portfolio excess returns. *, **, *** denote significance levels at the 10%, 5%, and 1%.

|           | Quintiles - 1   | Quintiles - 2   | Quintiles - 3   | Quintiles - 4   | Quintiles - 5   | Quintiles - 5-1   |
|-----------|-----------------|-----------------|-----------------|-----------------|-----------------|-------------------|
| STDPRCVOL | Low             |                 |                 |                 | High            |                   |
| Mean      | 0.043***        | 0.032**         | 0.021*          | 0.021           | 0.013*          | -0.030**          |
| t(Mean)   | (2.711)         | (2.114)         | (1.687)         | (1.644)         | (1.739)         | (-2.269)          |


<!-- p:16 -->


##### Table 7: Insignificant Factor Returns

This table reports the mean quintile portfolio returns based on the insignificant factors. The mean returns are the time-series averages of weekly value-weighted portfolio excess returns. *, **, *** denote significance levels at the 10%, 5%, and 1%.

|                  | 1        | 2       | 3       | 4       | 5        | 5-1      |
|------------------|----------|---------|---------|---------|----------|----------|
| AGE Mean         | 0.018    | 0.010   | 0.019*  | 0.014   | 0.013*   | -0.005   |
| t(Mean)          | (1.070)  | (1.034) | (1.902) | (1.445) | (1.732)  | (-0.358) |
| r 8,0 Mean       | 0.016    | 0.011   | 0.025** | 0.022** | 0.022*   | 0.006    |
| t(Mean)          | (1.366)  | (1.266) | (2.016) | (2.211) | (1.740)  | (0.421)  |
| Mean             | 0.017*   | 0.017*  | 0.006   | 0.013   | 0.021*   | 0.004    |
| r 16,0 t(Mean)   | (1.693)  | (1.806) | (0.714) | (1.300) | (1.661)  | (0.310)  |
| Mean             | 0.015    | 0.021** | 0.017   | 0.014   | 0.008    | -0.008   |
| r 50,0 t(Mean)   | (1.572)  | (2.167) | (1.593) | (1.447) | (0.680)  | (-0.764) |
| 100,0 Mean       | 0.032*** | 0.027** | 0.027*  | 0.024*  | 0.018    | -0.011   |
| t(Mean)          | (2.842)  | (2.556) | (1.971) | (1.923) | (1.376)  | (-0.804) |
|                  | 0.014    | 0.034*  | 0.017*  | 0.014   | 0.013*   | -0.002   |
| VOL Mean t(Mean) | (1.237)  | (1.736) | (1.695) | (1.289) | (1.780)  | (-0.170) |
| VOLSCALED Mean   | 0.028*   | 0.035** | 0.019   | 0.001   | 0.012*   | -0.016   |
| t(Mean)          | (1.913)  | (2.347) | (1.481) | (0.120) | (1.699)  | (-1.332) |
| BETA Mean        | 0.019*   | 0.017   | 0.020*  | 0.016   | 0.006    | -0.013   |
| t(Mean)          | (1.967)  | (1.573) | (1.817) | (1.488) | (0.544)  | (-1.256) |
| Mean             | 0.018*   | 0.024** | 0.017   | 0.015   | 0.005    | -0.012   |
| BETA2 t(Mean)    | (1.847)  | (2.074) | (1.616) | (1.334) | (0.484)  | (-1.191) |
| IDIOVOL Mean     | 0.014*   | 0.027** | 0.023*  | 0.007   | 0.022    | 0.009    |
| t(Mean)          | (1.894)  | (2.200) | (1.803) | (0.564) | (1.378)  | (0.682)  |
| RETVOL Mean      | 0.013    | 0.022** | 0.026*  | 0.020   | -0.004   | -0.017   |
| t(Mean)          | (1.549)  | (2.102) | (1.951) | (1.163) | (-0.281) | (-1.237) |
| Mean             | 0.011    | 0.002   | 0.020*  | 0.011   | 0.016    | 0.005    |
| RETSKEW t(Mean)  | (1.206)  | (0.270) | (1.947) | (1.015) | (1.191)  | (0.383)  |
| RETKURT Mean     | -0.002   | 0.022** | 0.011   | 0.021** | 0.005    | 0.006    |
| t(Mean)          | (-0.185) | (2.255) | (1.135) | (2.009) | (0.412)  | (0.647)  |
| Mean             | 0.012    | 0.018*  | 0.013   | 0.030*  | 0.006    | -0.006   |
| MAXRET t(Mean)   | (1.452)  | (1.691) | (1.358) | (1.778) | (0.388)  | (-0.441) |
| Mean             | 0.014*   | 0.019*  | 0.018   | 0.018   | 0.012    | -0.001   |
| DELAY t(Mean)    | (1.876)  | (1.783) | (1.629) | (1.338) | (1.264)  | (-0.159) |
| Mean             | 0.013*   | 0.013   | 0.039** | 0.015   | 0.038*   | 0.026    |
| DAMIHUD t(Mean)  | (1.739)  | (1.074) | (2.159) | (1.511) | (1.914)  | (1.478)  |


<!-- p:17 -->


### 3.5 Insignificant Factors

In this section, we present the table that summarizes the results for the zero-investment strategies for the factors that do not generate statistically significant returns. There are sixteen such factors in total: age; eight-, sixteen-, fifty-, and one hundred-week momentum; volume, and scaled volume; beta, beta squared, idiosyncratic volatility, the standard deviation of returns, the skewness of returns, the kurtosis of returns, maximum day return, delay, and the Amihud's illiquidity measure. Each week, we sort individual cryptocurrencies into quintile portfolios on the value of a given factor. All strategies are rebalanced weekly.

Table 7 presents the results of the performance of the zero-investment long-short strategies. None of the measures generates statistically significant long-short strategy returns. The average mean excess returns do not change monotonically with the quintiles. The differences in the average returns of the highest and lowest quintiles are small and statistically insignificant. For example, the sixteen-week momentum strategy generates statistically insignificant excess returns of 0.4 percent per week on the long-short strategy.

## 4 Cryptocurrency Factors

In this section, we investigate whether the nine cross-sectional cryptocurrency return predictors that we have identified can be spanned by a small number of factors. We perform an analysis similar to that of Fama and French (1996). We first show that a one-factor model with only the coin market return, or the cryptocurrency CAPM, cannot account for most of the excess returns of the nine strategies. Then, we analyze two-factor models: a two-factor model that adds the cryptocurrency size factor and a two-factor model that adds the cryptocurrency momentum factor. The two-factor model with the cryptocurrency market factor and a cryptocurrency size factor can account for the excess returns of five out of the nine zero-investment strategies but cannot explain any of the momentum related strategies. The two-factor model with the cryptocurrency market factor and a cryptocurrency momentum factor can account for the four momentum related strategies but not for any of the other strategies. Finally, we show that a three-factor model with the cryptocurrency market factor, a cryptocurrency size factor, and a cryptocurrency momentum factor explains the excess returns of all nine strategies.

The construction of the cryptocurrency market excess returns is discussed in Section 2. We construct the cryptocurrency size and momentum factors following the method used by Fama and French (1993). Specifically, for size, each week we split the coins into three size groups by market capitalization: bottom 30 percent (small, S), middle 40 percent (middle, M), and top 30 percent (big, B). 6 We then form value-weighted portfolios for each of the three groups. The cryptocurrency size factor (CSMB) is the return difference between the portfolios of the small and the big size portfolios. We construct the momentum factor (CMOM) using the three-week momentum. 7 Each week, we split the coins into three threeweek momentum groups: bottom 30 percent, middle 40 percent, and top 30 percent. Then, we form value-weighted portfolios for each of the three three-week momentum groups. The cryptocurrency momentum factor (CMOM) is the return difference between the top and the bottom momentum portfolios. In the Appendix, we provide summary statistics for each of the cryptocurrency factors.


<!-- p:18 -->


We first consider a one-factor model with only the cryptocurrency market factor, or the cryptocurrency CAPM. Table 8 presents the results for all the nine significant zeroinvestment strategies that we have found in the previous section. The alphas for all of the zero-investment long-short strategies remain significant. Moreover, the decreases in magnitude are small compared to the unadjusted excess returns. The average decrease of the zero-investment strategy alphas for the statistically significant strategies is only 8.61 percent of the orignal values. The strategies have some exposures to the coin market returns. In particular, the zero-investment long-short strategies based on market capitalization, price, maximum day price, dollar volume, and standard deviation of dollar volume are significantly exposed to the coin market excess returns. The strategies based on past returns - one-week momentum, two-week momentum, three-week momentum, and four-week momentum - are not significantly exposed to the coin market returns. The average of the absolute value of the statistically significant betas is 0.39 (with a range of 0.210 for the market capitalization strategy to 0.592 for the maximum day price). However, for all the strategies, the one-factor model does not explain a sizable portion of the excess returns, with the zero-investment strategy R 2 s ranging from about zero percent for the one-week momentum strategy to 6.8 percent for the maximum day price.

6 We use market capitalization as our main size measure because of the tradition in the stock market size literature. The results are robust to using alternative measures of size.

7 We use three-week momentum as our main momentum measure because it generates the largest longshort spread in the data. The results are qualitatively similar using alternative measures of momentum.


<!-- p:19 -->


##### Table 8: Cryptocurrency One-Factor Model

$$R _ { i } - R _ { f } = \alpha ^ { i } + \beta _ { C M K T } ^ { i } C M K T + \epsilon _ { i }$$

where CMKT is the cryptocurrency excess market returns. The formation of the quintile portfolios for the nine significant strategies are discussed in Section 3. The t-statistics are reported in the parentheses. *, **, *** denote significance levels at the 10%, 5%, and 1%. m.a.e and  ̄ R 2 are the mean of the absolute pricing errors and the average R 2 of the five portfolios, respectively.

|         |            | 1        | 2        | 3        | 4        | 5         | 5-1       |   m.a.e |    ̄ R 2 |
|---------|------------|----------|----------|----------|----------|-----------|-----------|---------|---------|
|         |            | 0.031**  | 0.005    | -0.001   | 0.002    | 0.001     | -0.031**  |         |         |
|         | t ' '      | (2.346)  | (0.640)  | (-0.148) | (0.257)  | (1.400)   | (-2.284)  |         |         |
| MCAP    | CMKT       | 1.208*** | 1.074*** | 0.990*** | 0.984*** | 0.998***  | -0.210*   |   0.008 |   0.571 |
|         | t ' CMKT ' | (10.606) | (15.302) | (16.023) | (18.662) | (200.564) | (-1.841)  |         |         |
|         | R 2        | 0.305    | 0.478    | 0.501    | 0.576    | 0.994     | 0.013     |         |         |
|         |            | 0.033**  | 0.013    | -0.011   | 0.005    | 0.000     | -0.032**  |         |         |
|         | t ' '      | (2.153)  | (1.307)  | (-1.484) | (0.502)  | (0.314)   | (-2.035)  |         |         |
| PRC     | CMKT       | 1.544*** | 1.307*** | 1.073*** | 1.083*** | 0.958***  | -0.585*** |   0.012 |   0.539 |
|         | t ' CMKT ' | (11.858) | (15.688) | (16.277) | (12.295) | (89.475)  | (-4.299)  |         |         |
|         | R 2        | 0.355    | 0.490    | 0.509    | 0.371    | 0.969     | 0.067     |         |         |
|         |            | 0.034**  | 0.010    | -0.011   | 0.008    | 0.000     | -0.034**  |         |         |
|         | t ' '      | (2.218)  | (1.009)  | (-1.459) | (0.722)  | (0.271)   | (-2.101)  |         |         |
| MAXDPRC | CMKT       | 1.551*** | 1.290*** | 1.070*** | 1.094*** | 0.958***  | -0.592*** |   0.013 |   0.533 |
|         | t ' CMKT ' | (11.796) | (15.753) | (16.244) | (11.579) | (89.511)  | (-4.310)  |         |         |
|         | R 2        | 0.352    | 0.492    | 0.508    | 0.344    | 0.969     | 0.068     |         |         |
|         |            | -0.019** | -0.014** | -0.002   | 0.029*   | 0.009     | 0.028**   |         |         |
|         | t ' '      | (-2.415) | (-2.220) | (-0.399) | (1.754)  | (0.774)   | (2.012)   |         |         |
| r 1,0   | CMKT       | 1.036*** | 1.015*** | 0.975*** | 1.111*** | 1.015***  | -0.021    |   0.015 |   0.437 |
|         | t ' CMKT ' | (15.653) | (18.950) | (21.158) | (7.865)  | (10.058)  | (-0.175)  |         |         |
|         | R 2        | 0.489    | 0.584    | 0.636    | 0.195    | 0.283     | 0.000     |         |         |
|         |            | -0.013   | -0.007   | -0.002   | 0.006    | 0.018     | 0.031**   |         |         |
|         | t ' '      | (-1.515) | (-1.000) | (-0.386) | (0.955)  | (1.649)   | (2.306)   |         |         |
| r 2,0   | CMKT       | 0.872*** | 0.998*** | 0.941*** | 1.048*** | 1.041***  | 0.169     |   0.009 |   0.484 |
|         | t ' CMKT ' | (11.682) | (16.539) | (19.940) | (20.302) | (11.241)  | (1.468)   |         |         |
|         | R 2        | 0.348    | 0.517    | 0.608    | 0.617    | 0.330     | 0.008     |         |         |
|         |            | -0.009   | -0.011*  | 0.003    | 0.007    | 0.031**   | 0.040***  |         |         |
|         | t ' '      | (-1.047) | (-1.651) | (0.469)  | (1.273)  | (2.431)   | (2.652)   |         |         |
| r 3,0   | CMKT       | 0.904*** | 0.994*** | 0.955*** | 1.037*** | 1.005***  | 0.101     |   0.012 |   0.459 |
|         | t ' CMKT ' | (11.864) | (17.958) | (15.591) | (21.437) | (9.318)   | (0.782)   |         |         |
|         | R 2        | 0.355    | 0.557    | 0.487    | 0.642    | 0.253     | 0.002     |         |         |


<!-- p:20 -->


| Table 3 Continued   |            | 1        | 2        | 3        | 4        | 5         | 5-1      |   m.a.e |    ̄ R 2 |
|---------------------|------------|----------|----------|----------|----------|-----------|----------|---------|---------|
|                     |            | -0.009   | -0.008   | -0.004   | 0.006    | 0.014     | 0.024*   |         |         |
|                     | t ' '      | (-1.333) | (-1.071) | (-0.770) | (0.993)  | (1.300)   | (1.906)  |         |         |
| r 4,0               | CMKT       | 0.939*** | 0.979*** | 0.959*** | 1.067*** | 1.064***  | 0.125    |   0.008 |   0.522 |
|                     | t ' CMKT ' | (15.586) | (15.407) | (22.943) | (21.056) | (11.353)  | (1.174)  |         |         |
|                     | R 2        | 0.487    | 0.481    | 0.673    | 0.634    | 0.335     | 0.005    |         |         |
|                     |            | 0.029*   | 0.014    | 0.003    | 0.004    | 0.001     | -0.028*  |         |         |
|                     | t ' '      | (1.814)  | (1.389)  | (0.309)  | (0.465)  | (0.924)   | (-1.758) |         |         |
| PRCVOL              | CMKT       | 1.334*** | 1.193*** | 1.125*** | 1.114*** | 0.997***  | -0.337** |   0.010 |   0.520 |
|                     | t ' CMKT ' | (9.789)  | (14.131) | (14.640) | (14.268) | (156.767) | (-2.454) |         |         |
|                     | R 2        | 0.272    | 0.438    | 0.456    | 0.443    | 0.990     | 0.023    |         |         |
|                     |            | 0.028**  | 0.017    | 0.006    | 0.007    | 0.001     | -0.028** |         |         |
|                     | t ' '      | (2.118)  | (1.374)  | (0.713)  | (0.689)  | (0.843)   | (-2.048) |         |         |
| STDPRCVOL           | CMKT       | 1.223*** | 1.292*** | 1.192*** | 1.209*** | 0.993***  | -0.230** |   0.012 |   0.524 |
|                     | t ' CMKT ' | (10.734) | (12.332) | (15.557) | (14.870) | (152.231) | (-1.997) |         |         |
|                     | R 2        | 0.310    | 0.373    | 0.486    | 0.463    | 0.989     | 0.015    |         |         |

In the last two columns, we report the absolute pricing errors and average R 2 s of the five quintile portfolios for each strategy. We report the mean of the absolute pricing errors, m.a.e, for each strategy. The mean of the absolute pricing errors is defined as the average of the absolute value of the alphas for all the five quintile portfolios. In particular, the m.a.e ranges from 0.8 percent for the market capitalization and the four-week momentum strategies to 1.5 percent for the one-week momentum strategy. The average R 2 ,  ̄ R 2 , is about 50 percent for most of the strategies, indicating that the model explains substantial fractions of the return variations of the individual portfolios. In other words, there is strong comovement across different coins.


<!-- p:21 -->


##### Table 9: Cryptocurrency Market and Size Factor Model

$$R _ { i } - R _ { f } = \alpha ^ { i } + \beta _ { C M K T } ^ { i } C M K T + \beta _ { C S M B } ^ { i } C S M B + \epsilon _ { i }$$

where CMKT is the cryptocurrency excess market returns and CSMB is the cryptocurrency size factor. The formation of the quintile portfolios for the nine significant strategies are discussed in Section 3. The tstatistics are reported in the parentheses. *, **, *** denote significance levels at the 10%, 5%, and 1%. m.a.e and  ̄ R 2 are the mean of the absolute pricing errors and the average R 2 of the five portfolios, respectively.

|         |            | 1         | 2        | 3        | 4        | 5         | 5-1       |   m.a.e |    ̄ R 2 |
|---------|------------|-----------|----------|----------|----------|-----------|-----------|---------|---------|
|         |            | 0.006     | -0.005   | -0.006   | -0.004   | 0.001     | -0.005    |         |         |
|         | t ' '      | (1.051)   | (-0.740) | (-0.858) | (-0.712) | (1.413)   | (-0.912)  |         |         |
|         | CMKT       | 1.036***  | 1.004*** | 0.944*** | 0.946*** | 0.998***  | -0.037    |         |         |
| MCAP    | t ' CMKT ' | (20.427)  | (17.636) | (16.906) | (19.744) | (199.107) | (-0.737)  |   0.004 |   0.755 |
|         | CSMB       | 1.343***  | 0.548*** | 0.359*** | 0.300*** | -0.001    | -1.344*** |         |         |
|         | t ' CSMB ' | (32.427)  | (11.777) | (7.873)  | (7.667)  | (-0.211)  | (-32.480) |         |         |
|         | R 2        | 0.864     | 0.662    | 0.598    | 0.656    | 0.994     | 0.808     |         |         |
|         |            | 0.019     | 0.008    | -0.017** | 0.002    | 0.001     | -0.018    |         |         |
|         | t ' '      | (1.363)   | (0.792)  | (-2.254) | (0.147)  | (0.690)   | (-1.241)  |         |         |
|         | CMKT       | 1.448***  | 1.271*** | 1.037*** | 1.057*** | 0.962***  | -0.486*** |         |         |
| PRC     | t ' CMKT ' | (12.272)  | (15.661) | (16.492) | (12.095) | (90.547)  | (-3.929)  |   0.009 |   0.584 |
| PRC     | CSMB       | 0.748***  | 0.279*** | 0.278*** | 0.197*** | -0.025*** | -0.773*** |         |         |
| PRC     | t ' CSMB ' | (7.762)   | (4.206)  | (5.418)  | (2.763)  | (-2.884)  | (-7.650)  |         |         |
| PRC     | R 2        | 0.478     | 0.523    | 0.559    | 0.390    | 0.970     | 0.241     |         |         |
|         |            | 0.020     | 0.004    | -0.016** | 0.004    | 0.001     | -0.019    |         |         |
|         | t ' '      | (1.440)   | (0.463)  | (-2.176) | (0.386)  | (0.644)   | (-1.319)  |         |         |
|         | CMKT       | 1.454***  | 1.253*** | 1.036*** | 1.069*** | 0.962***  | -0.493*** |         |         |
| MAXDPRC | t ' CMKT ' | (12.188)  | (15.761) | (16.389) | (11.372) | (90.569)  | (-3.941)  |   0.009 |   0.577 |
| MAXDPRC | CSMB       | 0.749***  | 0.287*** | 0.263*** | 0.200*** | -0.025*** | -0.774*** |         |         |
| MAXDPRC | t ' CSMB ' | (7.686)   | (4.424)  | (5.093)  | (2.607)  | (-2.871)  | (-7.576)  |         |         |
| MAXDPRC | R 2        | 0.474     | 0.528    | 0.553    | 0.361    | 0.970     | 0.239     |         |         |
|         |            | -0.021*** | -0.014** | -0.006   | 0.028*   | 0.004     | 0.025*    |         |         |
|         | t ' '      | (-2.737)  | (-2.260) | (-1.176) | (1.661)  | (0.346)   | (1.810)   |         |         |
|         | CMKT       | 1.019***  | 1.012*** | 0.948*** | 1.103*** | 0.980***  | -0.039    |         |         |
| r 1,0   | t ' CMKT ' | (15.462)  | (18.767) | (21.743) | (7.751)  | (9.850)   | (-0.327)  |   0.015 |   0.455 |
|         | CSMB       | 0.132**   | 0.021    | 0.208*** | 0.068    | 0.274***  | 0.141     |         |         |
|         | t ' CSMB ' | (2.460)   | (0.475)  | (5.826)  | (0.584)  | (3.369)   | (1.459)   |         |         |
|         | R 2        | 0.501     | 0.584    | 0.679    | 0.196    | 0.314     | 0.008     |         |         |


<!-- p:22 -->


| Table 9 Continued   |            | 1        | 2        | 3        | 4        | 5         | 5-1       |   m.a.e |    ̄ R 2 |
|---------------------|------------|----------|----------|----------|----------|-----------|-----------|---------|---------|
|                     |            | -0.016*  | -0.010   | -0.003   | 0.004    | 0.014     | 0.030**   |         |         |
|                     | t ' '      | (-1.841) | (-1.438) | (-0.611) | (0.696)  | (1.325)   | (2.230)   |         |         |
|                     | CMKT       | 0.852*** | 0.977*** | 0.932*** | 1.037*** | 1.016***  | 0.164     |         |         |
| r 2,0               | t ' CMKT ' | (11.474) | (16.416) | (19.727) | (20.098) | (11.031)  | (1.415)   |   0.009 |   0.496 |
|                     | CSMB       | 0.152**  | 0.160*** | 0.068*   | 0.084**  | 0.190**   | 0.039     |         |         |
|                     | t ' CSMB ' | (2.498)  | (3.295)  | (1.751)  | (1.982)  | (2.528)   | (0.408)   |         |         |
|                     | R 2        | 0.363    | 0.536    | 0.613    | 0.623    | 0.347     | 0.009     |         |         |
|                     |            | -0.013   | -0.014** | 0.000    | 0.006    | 0.026**   | 0.039**   |         |         |
|                     | t ' '      | (-1.445) | (-2.170) | (0.058)  | (1.085)  | (2.093)   | (2.566)   |         |         |
|                     | CMKT       | 0.880*** | 0.972*** | 0.935*** | 1.030*** | 0.975***  | 0.095     |         |         |
| r 3,0               | t ' CMKT ' | (11.668) | (17.920) | (15.447) | (21.211) | (9.097)   | (0.729)   |   0.012 |   0.477 |
|                     | CSMB       | 0.186*** | 0.168*** | 0.159*** | 0.055    | 0.234***  | 0.048     |         |         |
|                     | t ' CSMB ' | (3.012)  | (3.782)  | (3.207)  | (1.379)  | (2.672)   | (0.456)   |         |         |
|                     | R 2        | 0.377    | 0.581    | 0.507    | 0.645    | 0.274     | 0.003     |         |         |
|                     |            | -0.012*  | -0.012   | -0.006   | 0.005    | 0.011     | 0.023*    |         |         |
|                     | t ' '      | (-1.716) | (-1.615) | (-1.159) | (0.790)  | (0.997)   | (1.831)   |         |         |
|                     | CMKT       | 0.921*** | 0.952*** | 0.946*** | 1.059*** | 1.041***  | 0.120     |         |         |
| r 4,0               | t ' CMKT ' | (15.418) | (15.348) | (22.851) | (20.834) | (11.143)  | (1.120)   |   0.009 |   0.537 |
|                     | CSMB       | 0.141*** | 0.204*** | 0.100*** | 0.063    | 0.179**   | 0.038     |         |         |
|                     | t ' CSMB ' | (2.893)  | (4.023)  | (2.967)  | (1.516)  | (2.344)   | (0.431)   |         |         |
|                     | R 2        | 0.503    | 0.512    | 0.684    | 0.637    | 0.349     | 0.006     |         |         |
|                     |            | 0.008    | 0.006    | -0.006   | -0.001   | 0.001     | -0.007    |         |         |
|                     | t ' '      | (0.646)  | (0.659)  | (-0.728) | (-0.101) | (1.110)   | (-0.575)  |         |         |
|                     | CMKT       | 1.190*** | 1.140*** | 1.065*** | 1.078*** | 0.998***  | -0.193*   |         |         |
| PRCVOL              | t ' CMKT ' | (11.093) | (14.422) | (15.499) | (14.236) | (156.423) | (-1.780)  |   0.004 |   0.623 |
|                     | CSMB       | 1.116*** | 0.408*** | 0.465*** | 0.276*** | -0.008    | -1.124*** |         |         |
|                     | t ' CSMB ' | (12.738) | (6.324)  | (8.281)  | (4.460)  | (-1.483)  | (-12.726) |         |         |
|                     | R 2        | 0.555    | 0.514    | 0.571    | 0.483    | 0.990     | 0.402     |         |         |
|                     |            | 0.011    | 0.007    | -0.001   | -0.001   | 0.001     | -0.010    |         |         |
|                     | t ' '      | (1.018)  | (0.581)  | (-0.133) | (-0.134) | (1.124)   | (-0.926)  |         |         |
|                     | CMKT       | 1.102*** | 1.221*** | 1.140*** | 1.156*** | 0.995***  | -0.107    |         |         |
| STDPRCVOL           | t ' CMKT ' | (12.379) | (12.623) | (16.116) | (15.315) | (152.720) | (-1.191)  |   0.004 |   0.632 |
|                     | CSMB       | 0.946*** | 0.550*** | 0.403*** | 0.416*** | -0.012**  | -0.957*** |         |         |
|                     | t ' CSMB ' | (13.011) | (6.964)  | (6.967)  | (6.749)  | (-2.176)  | (-13.040) |         |         |
|                     | R 2        | 0.586    | 0.473    | 0.568    | 0.545    | 0.989     | 0.409     |         |         |


<!-- p:23 -->


We then consider a two-factor model with the cryptocurrency market factor and the cryptocurrency size factor. Table 9 presents the results for all nine strategies. The longshort alphas for most of them, with the exception of the momentum strategies, are no longer significant. For example, the absolute value of the alpha for dollar volume drops from 2.8 percent under the one-factor model to an insignificant 0.7 percent under the two-factor model. All non-momentum strategies have significant exposures to the cryptocurrency size factor. Among the non-momentum strategies, the absolute values of their size factor loadings range from 1.344 for the market capitalization factor to 0.773 for the last day price factor. In other words, the small coins are also more illiquid and have lower trading volume, similar to results in the stock market. Many strategies have significant loadings on CMKT, with the exception of the market capitalization, the standard deviation of dollar volume, the one-, two-, three- and four-week momentum factors. For all non-momentum strategies, the model explains substantial fractions of the return variations beyond what the coin market factor explains. Among the non-momentum strategies, the zero-investment long-short strategy R 2 s range from 23.9 percent for the strategy based on the maximum day price factor to more than 80 percent for the strategy based on the market capitalization factor. However, this two-factor model based on the cryptocurrency market and size falls short in explaining any of the momentum based strategies. The alphas on the momentum based strategies are all statistically significant adjusting for this two-factor model. Compared to those of the one-factor model, the means of absolute pricing errors decrease dramatically for the nonmomentum strategies. For example, the m.a.e of the dollar volume strategy reduces from 1.0 percent in the one-factor model to 0.4 percent in the two-factor model controlling for the cryptocurrency market and size factors - a 60 percent decrease. The means of absolute pricing errors do not materially change for the momentum strategies controlling for the two-factor model.

We next consider an alternative two-factor model by combining the cryptocurrency market factor and the cryptocurrency momentum factor. Table 10 presents the results for all nine zero-investment long-short strategies adjusting for the alternative two-factor model. This two-factor model performs well in capturing the excess returns of the four momentum factors - one-, two-, three-, and four-week momentum factors. After controlling for this alternative two-factor model, the alphas for all four momentum strategies are no longer statistically significant. For example, the alpha of the one-week momentum strategy drops from 2.8 percent under the one-factor model to 0.7 percent under this alternative two-factor model. All four momentum strategies have statistically significant exposures to the momentum factor. For these four strategies, their momentum factor loadings range from 0.582 for the one-week momentum to 0.985 for the three-week momentum. All non-momentum strategies, with the exception of dollar volume, have significant exposures to the market. On the other hand, none of the momentum strategies significantly exposes to the cryptocurrency market factor. For the momentum strategies, this alternative two-factor model explains a substantial fraction of the return variations in contrast to the market one-factor model or the market and size two-factor model. The zero-investment strategy R 2 s range from 23.2 percent for the one-week momentum to 56.1 percent for the three-week momentum. However, the model underperforms in explaining the return variations of the non-momentum strategies compared to the two-factor model with the cryptocurrency market and the cryptocurrency size factors. The alphas of the non-momentum strategies, with the exception of the dollar volume strategy, remain statistically significant. Compared to the one-factor model, the means of absolute pricing errors largely decrease for the momentum factors. For example, the m.a.e of the two-week momentum strategy reduces from 0.9 percent in the one-factor model to 0.2 percent in the two-factor model.


<!-- p:24 -->


Finally, we consider a three-factor model that combines the cryptocurrency market, size, and momentum factors. Table 11 presents the results for all nine strategies. Adjusted for the cryptocurrency three-factor model, none of the alphas for the nine strategies remains statistically significant. We now turn to the discussion of exposures to the three factors. The one-week momentum long-short strategy is statistically significantly exposed to both the size and momentum factors. The market capitalization and standard deviation of dollar volume zero-investment long-short strategies are statistically significantly exposed to the size factor only but not to the market or momentum factors. The two-, three- and four-week momentum zero-investment long-short strategies are statistically significantly exposed to the momentum factor only but not to the market or size factors. The following strategies are statistically significantly exposed to both the market and size factors: price, maximum day price, and dollar volume. None of the strategies is exposed to the market factor only. In other words, both size and momentum are important in explaining the cross-section of expected returns of cryptocurrencies. Compared to the one-factor model, the means of absolute pricing errors largely decrease for all of the nine strategies.


<!-- p:25 -->


##### Table 10: Cryptocurrency Market and Momentum Factor Model

$$R _ { i } - R _ { f } = \alpha ^ { i } + \beta _ { C M K T } ^ { i } C M K T + \beta _ { C S M B } ^ { i } C M O M + \epsilon _ { i }$$

where CMKT is the cryptocurrency excess market returns and CMOM is the cryptocurrency momentum factor. The formation of the quintile portfolios for the nine significant strategies are discussed in Section 3. The t-statistics are reported in the parentheses. *, **, *** denote significance levels at the 10%, 5%, and 1%. m.a.e and  ̄ R 2 are the mean of the absolute pricing errors and the average R 2 of the five portfolios, respectively.

|         |            | 1         | 2         | 3         | 4        | 5         | 5-1       |   m.a.e |    ̄ R 2 |
|---------|------------|-----------|-----------|-----------|----------|-----------|-----------|---------|---------|
|         |            | 0.034**   | 0.004     | 0.001     | 0.003    | 0.001     | -0.033**  |         |         |
|         | t ' '      | (2.503)   | (0.509)   | (0.179)   | (0.458)  | (1.341)   | (-2.444)  |         |         |
|         | CMKT       | 1.218***  | 1.071***  | 0.991***  | 0.989*** | 0.998***  | -0.219*   |         |         |
| MCAP    | t ' CMKT ' | (10.657)  | (15.184)  | (15.956)  | (18.693) | (199.519) | (-1.920)  |   0.009 |   0.572 |
|         | CMOM       | -0.076    | 0.027     | -0.007    | -0.036   | 0.000     | 0.076     |         |         |
|         | t ' CMOM ' | (-1.040)  | (0.609)   | (-0.179)  | (-1.067) | (0.155)   | (1.047)   |         |         |
|         | R 2        | 0.308     | 0.478     | 0.501     | 0.578    | 0.994     | 0.017     |         |         |
|         |            | 0.035**   | 0.011     | -0.012    | 0.005    | 0.001     | -0.034**  |         |         |
|         | t ' '      | (2.257)   | (1.082)   | (-1.490)  | (0.520)  | (0.888)   | (-2.088)  |         |         |
|         | CMKT       | 1.552***  | 1.300***  | 1.072***  | 1.084*** | 0.961***  | -0.591*** |         |         |
| PRC     | t ' CMKT ' | (11.870)  | (15.556)  | (16.178)  | (12.244) | (90.786)  | (-4.319)  |   0.013 |   0.540 |
| PRC     | CMOM       | -0.063    | 0.055     | 0.008     | -0.008   | -0.020*** | 0.043     |         |         |
| PRC     | t ' CMOM ' | (-0.755)  | (1.040)   | (0.188)   | (-0.143) | (-2.979)  | (0.491)   |         |         |
| PRC     | R 2        | 0.356     | 0.492     | 0.509     | 0.371    | 0.970     | 0.068     |         |         |
|         |            | 0.036**   | 0.007     | -0.012    | 0.008    | 0.001     | -0.035**  |         |         |
|         | t ' '      | (2.290)   | (0.761)   | (-1.468)  | (0.689)  | (0.850)   | (-2.124)  |         |         |
|         | CMKT       | 1.557***  | 1.282***  | 1.069***  | 1.094*** | 0.961***  | -0.596*** |         |         |
| MAXDPRC | t ' CMKT ' | (11.792)  | (15.619)  | (16.145)  | (11.512) | (90.851)  | (-4.316)  |   0.013 |   0.534 |
| MAXDPRC | CMOM       | -0.050    | 0.062     | 0.009     | 0.006    | -0.020*** | 0.030     |         |         |
| MAXDPRC | t ' CMOM ' | (-0.600)  | (1.189)   | (0.203)   | (0.095)  | (-3.005)  | (0.344)   |         |         |
| MAXDPRC | R 2        | 0.353     | 0.495     | 0.508     | 0.344    | 0.970     | 0.068     |         |         |
| MAXDPRC |            | -0.013*   | -0.009    | 0.001     | 0.027    | -0.006    | 0.007     |         |         |
| MAXDPRC | t ' '      | (-1.651)  | (-1.507)  | (0.118)   | (1.570)  | (-0.527)  | (0.552)   |         |         |
| MAXDPRC | CMKT       | 1.057***  | 1.031***  | 0.985***  | 1.102*** | 0.963***  | -0.094    |         |         |
| r 1,0   | t ' CMKT ' | (16.404)  | (19.671)  | (21.553)  | (7.772)  | (10.364)  | (-0.905)  |   0.011 |   0.473 |
| r 1,0   | CMOM       | -0.168*** | -0.125*** | -0.077*** | 0.070    | 0.414***  | 0.582***  |         |         |
| r 1,0   | t ' CMOM ' | (-4.089)  | (-3.762)  | (-2.664)  | (0.771)  | (7.010)   | (8.781)   |         |         |
| r 1,0   | R 2        | 0.520     | 0.606     | 0.646     | 0.196    | 0.399     | 0.232     |         |         |


<!-- p:26 -->


| Table 10 Continued   |            | 1         | 2         | 3         | 4        | 5         | 5-1               |   m.a.e |    ̄ R 2 |
|----------------------|------------|-----------|-----------|-----------|----------|-----------|-------------------|---------|---------|
|                      |            | -0.003    | -0.001    | 0.001     | 0.001    | 0.003     | 0.006             |         |         |
|                      | t ' '      | (-0.350)  | (-0.134)  | (0.157)   | (0.088)  | (0.346)   | (0.569)           |         |         |
|                      | CMKT       | 0.908***  | 1.019***  | 0.951***  | 1.030*** | 0.990***  | 0.082             |         |         |
| r 2,0                | t ' CMKT ' | (13.062)  | (17.485)  | (20.365)  | (20.644) | (11.736)  | (0.876)           |   0.002 |   0.542 |
|                      | CMOM       | -0.286*** | -0.170*** | -0.083*** | 0.145*** | 0.399***  | 0.685***          |         |         |
|                      | t ' CMOM ' | (-6.476)  | (-4.579)  | (-2.799)  | (4.583)  | (7.428)   | (11.435)          |         |         |
|                      | R 2        | 0.440     | 0.553     | 0.620     | 0.646    | 0.450     | 0.344             |         |         |
|                      |            | 0.004     | -0.002    | 0.007     | 0.005    | 0.008     | 0.004             |         |         |
|                      | t ' '      | (0.462)   | (-0.399)  | (0.980)   | (0.885)  | (0.769)   | (0.435)           |         |         |
|                      | CMKT       | 0.950***  | 1.023***  | 0.968***  | 1.030*** | 0.926***  | -0.024            |         |         |
| r 3,0                | t ' CMKT ' | (14.006)  | (20.119)  | (15.939)  | (21.324) | (10.364)  | (-0.276)          |   0.005 |   0.553 |
|                      | CMOM       | -0.362*** | -0.229*** | -0.103*** | 0.059*   | 0.623***  | 0.985***          |         |         |
|                      | t ' CMOM ' | (-8.386)  | (-7.095)  | (-2.663)  | (1.918)  | (10.971)  | (18.005)          |         |         |
|                      | R 2        | 0.494     | 0.630     | 0.501     | 0.647    | 0.493     | 0.561             |         |         |
|                      |            | 0.000     | -0.000    | -0.001    | 0.004    | -0.004    | -0.004            |         |         |
|                      | t ' '      | (0.031)   | (-0.013)  | (-0.141)  | (0.639)  | (-0.376)  | (-0.422)          |         |         |
|                      | CMKT       | 0.973***  | 1.006***  | 0.970***  | 1.060*** | 1.001***  | 0.028             |         |         |
| r 4,0                | t ' CMKT ' | (17.809)  | (16.732)  | (23.553)  | (20.932) | (12.419)  | (0.373)           |   0.002 |   0.592 |
|                      | CMOM       | -0.266*** | -0.218*** | -0.085*** | 0.057*   | 0.495***  | 0.760***          |         |         |
|                      | t ' CMOM ' | (-7.652)  | (-5.698)  | (-3.249)  | (1.756)  | (9.648)   | (15.751)          |         |         |
|                      | R 2        | 0.583     | 0.540     | 0.686     | 0.638    | 0.513     | 0.496             |         |         |
|                      |            | 0.011     | 0.005     | 0.013     | 0.007    | -0.003    | -0.014            |         |         |
|                      | t ' '      | (1.233)   | (0.980)   | (1.304)   | (0.944)  | (-0.314)  | (-1.114)          |         |         |
|                      | CMKT       | 1.137***  | 0.888***  | 1.061***  | 1.006*** | 1.114***  | -0.023            |         |         |
| PRCVOL               | t ' CMKT ' | (15.660)  | (19.048)  | (12.723)  | (16.897) | (14.675)  | (-0.227)          |   0.008 |   0.509 |
|                      | CMOM       | -0.235*** | -0.145*** | -0.025    | 0.099*** | 0.299***  | 0.534***          |         |         |
|                      | t ' CMOM ' | (-5.099)  | (-4.895)  | (-0.467)  | (2.611)  | (6.184)   | (8.252)           |         |         |
|                      | R 2        | 0.505     | 0.595     | 0.389     | 0.542    | 0.514     | 0.211             |         |         |
|                      |            | 0.029**   | 0.012     | 0.008     | 0.006    | 0.001     | -0.028**          |         |         |
|                      | t ' '      | (2.118)   | (0.954)   | (0.885)   | (0.629)  | (0.912)   | (-2.044)          |         |         |
|                      | CMKT       | 1.225***  | 1.274***  | 1.198***  | 1.208*** | 0.994***  |                   |         |         |
| STDPRCVOL            | t ' CMKT ' | (10.698)  | (12.205)  | (15.581)  | (14.775) | (151.535) | -0.232** (-2.002) |   0.011 |   0.527 |
|                      | CMOM       | -0.016    | 0.139**   | -0.047    | 0.012    | -0.002    | 0.015             |         |         |
|                      | t ' CMOM ' | (-0.226)  | (2.086)   | (-0.956)  | (0.240)  | (-0.445)  | (0.198)           |         |         |
|                      | R 2        | 0.311     | 0.383     | 0.488     | 0.464    | 0.989     | 0.015             |         |         |


<!-- p:27 -->


##### Table 11: Cryptocurrency Three-Factor Model

$$R _ { i } - R _ { f } = \alpha ^ { i } + \beta _ { C M K T } ^ { i } C M K T + \beta _ { C S M B } ^ { i } C S M B + \beta _ { C H M L } ^ { i } C M O M + \epsilon _ { i }$$

where CMKT is the cryptocurrency excess market returns, CSMB is the cryptocurrency size factor, and CMOM is the cryptocurrency momentum factor. The formation of the quintile portfolios for the nine significant strategies are discussed in Section 3. The t-statistics are reported in the parentheses. *, **, *** denote significance levels at the 10%, 5%, and 1%. m.a.e is the mean of the absolute pricing errors.  ̄ R 2 is the average R 2 of the five portfolios.

|         |            | 1        | 2        | 3        | 4        | 5         | 5-1       |   m.a.e |    ̄ R 2 |
|---------|------------|----------|----------|----------|----------|-----------|-----------|---------|---------|
|         |            | 0.007    | -0.007   | -0.006   | -0.003   | 0.001     | -0.007    |         |         |
|         | t ' '      | (1.224)  | (-0.974) | (-0.865) | (-0.528) | (1.354)   | (-1.091)  |         |         |
|         | CMKT       | 1.040*** | 0.998*** | 0.943*** | 0.949*** | 0.998***  | -0.042    |         |         |
|         | t ' CMKT ' | (20.436) | (17.487) | (16.802) | (19.735) | (198.002) | (-0.818)  |         |         |
| MCAP    | CSMB       | 1.341*** | 0.550*** | 0.359*** | 0.298*** | -0.001    | -1.342*** |   0.005 |   0.756 |
|         | t ' CSMB ' | (32.355) | (11.833) | (7.856)  | (7.620)  | (-0.205)  | (-32.409) |         |         |
|         | CMOM       | -0.032   | 0.045    | 0.005    | -0.026   | 0.000     | 0.032     |         |         |
|         | t ' CMOM ' | (-0.981) | (1.256)  | (0.133)  | (-0.857) | (0.146)   | (0.997)   |         |         |
|         | R 2        | 0.865    | 0.664    | 0.598    | 0.657    | 0.994     | 0.809     |         |         |
|         |            | 0.020    | 0.005    | -0.017** | 0.002    | 0.002     | -0.019    |         |         |
|         | t ' '      | (1.435)  | (0.531)  | (-2.290) | (0.149)  | (1.309)   | (-1.258)  |         |         |
|         | CMKT       | 1.453*** | 1.262*** | 1.035*** | 1.058*** | 0.964***  | -0.488*** |         |         |
|         | t ' CMKT ' | (12.254) | (15.517) | (16.370) | (12.031) | (92.059)  | (-3.927)  |         |         |
| PRC     | CSMB       | 0.746*** | 0.282*** | 0.279*** | 0.197*** | -0.026*** | -0.772*** |   0.009 |   0.585 |
|         | t ' CSMB ' | (7.722)  | (4.260)  | (5.423)  | (2.754)  | (-3.065)  | (-7.620)  |         |         |
|         | CMOM       | -0.038   | 0.065    | 0.017    | -0.002   | -0.021*** | 0.017     |         |         |
|         | t ' CMOM ' | (-0.511) | (1.254)  | (0.427)  | (-0.029) | (-3.154)  | (0.221)   |         |         |
|         | R 2        | 0.478    | 0.526    | 0.560    | 0.390    | 0.971     | 0.242     |         |         |
|         |            | 0.021    | 0.002    | -0.017** | 0.004    | 0.002     | -0.020    |         |         |
|         | t ' '      | (1.476)  | (0.175)  | (-2.214) | (0.337)  | (1.269)   | (-1.302)  |         |         |
|         | CMKT       | 1.458*** | 1.243*** | 1.034*** | 1.067*** | 0.964***  | -0.494*** |         |         |
|         | t ' CMKT ' | (12.152) | (15.616) | (16.268) | (11.292) | (92.112)  | (-3.924)  |         |         |
| MAXDPRC | CSMB       | 0.748*** | 0.291*** | 0.264*** | 0.201*** | -0.026*** | -0.774*** |   0.009 |   0.578 |
|         | t ' CSMB ' | (7.652)  | (4.489)  | (5.099)  | (2.609)  | (-3.053)  | (-7.552)  |         |         |
|         | CMOM       | -0.026   | 0.072    | 0.017    | 0.012    | -0.021*** | 0.005     |         |         |
|         | t ' CMOM ' | (-0.341) | (1.421)  | (0.428)  | (0.206)  | (-3.180)  | (0.060)   |         |         |
|         | R 2        | 0.474    | 0.532    | 0.553    | 0.361    | 0.971     | 0.239     |         |         |


<!-- p:28 -->


| Table 11 Continued   |            | 1         | 2         | 3         | 4        | 5        | 5-1      |   m.a.e |    ̄ R 2 |
|----------------------|------------|-----------|-----------|-----------|----------|----------|----------|---------|---------|
|                      |            | -0.015**  | -0.010    | -0.003    | 0.025    | -0.012   | 0.003    |         |         |
|                      | t ' '      | (-1.970)  | (-1.535)  | (-0.657)  | (1.470)  | (-1.080) | (0.274)  |         |         |
|                      | CMKT       | 1.041***  | 1.029***  | 0.958***  | 1.093*** | 0.924*** | -0.117   |         |         |
|                      | t ' CMKT ' | (16.198)  | (19.486)  | (22.122)  | (7.650)  | (10.171) | (-1.126) |         |         |
| r 1,0                | CSMB       | 0.124**   | 0.014     | 0.204***  | 0.072    | 0.297*** | 0.173**  |   0.013 |   0.491 |
|                      | t ' CSMB ' | (2.360)   | (0.328)   | (5.776)   | (0.617)  | (4.014)  | (2.043)  |         |         |
|                      | CMOM       | -0.164*** | -0.125*** | -0.071**  | 0.072    | 0.424*** | 0.587*** |         |         |
|                      | t ' CMOM ' | (-4.022)  | (-3.739)  | (-2.581)  | (0.796)  | (7.378)  | (8.914)  |         |         |
|                      | R 2        | 0.531     | 0.606     | 0.687     | 0.198    | 0.435    | 0.245    |         |         |
|                      |            | -0.006    | -0.004    | -0.000    | -0.001   | -0.001   | 0.005    |         |         |
|                      | t ' '      | (-0.677)  | (-0.572)  | (-0.068)  | (-0.218) | (-0.073) | (0.430)  |         |         |
|                      | CMKT       | 0.890***  | 0.999***  | 0.943***  | 1.017*** | 0.962*** | 0.072    |         |         |
|                      | t ' CMKT ' | (12.847)  | (17.352)  | (20.136)  | (20.443) | (11.529) | (0.764)  |         |         |
| r 2,0                | CSMB       | 0.136**   | 0.151***  | 0.063*    | 0.092**  | 0.212*** | 0.076    |   0.002 |   0.554 |
|                      | t ' CSMB ' | (2.415)   | (3.224)   | (1.656)   | (2.260)  | (3.123)  | (0.986)  |         |         |
|                      | CMOM       | -0.282*** | -0.165*** | -0.081*** | 0.148*** | 0.405*** | 0.687*** |         |         |
|                      | t ' CMOM ' | (-6.429)  | (-4.522)  | (-2.736)  | (4.711)  | (7.679)  | (11.466) |         |         |
|                      | R 2        | 0.452     | 0.571     | 0.624     | 0.653    | 0.470    | 0.347    |         |         |
|                      |            | 0.000     | -0.006    | 0.004     | 0.004    | 0.003    | 0.002    |         |         |
|                      | t ' '      | (0.053)   | (-0.924)  | (0.565)   | (0.680)  | (0.273)  | (0.236)  |         |         |
|                      | CMKT       | 0.928***  | 1.002***  | 0.948***  | 1.022*** | 0.890*** | -0.037   |         |         |
|                      | t ' CMKT ' | (13.819)  | (20.117)  | (15.779)  | (21.089) | (10.160) | (-0.432) |         |         |
| r 3,0                | CSMB       | 0.166***  | 0.155***  | 0.153***  | 0.058    | 0.268*** | 0.102    |   0.003 |   0.570 |
|                      | t ' CSMB ' | (3.039)   | (3.829)   | (3.130)   | (1.470)  | (3.758)  | (1.451)  |         |         |
|                      | CMOM       | -0.356*** | -0.224*** | -0.098**  | 0.061**  | 0.632*** | 0.988*** |         |         |
|                      | t ' CMOM ' | (-8.385)  | (-7.114)  | (-2.574)  | (1.983)  | (11.399) | (18.089) |         |         |
|                      | R 2        | 0.512     | 0.651     | 0.519     | 0.650    | 0.519    | 0.564    |         |         |
|                      |            | -0.002    | -0.004    | -0.003    | 0.003    | -0.008   | -0.005   |         |         |
|                      | t ' '      | (-0.358)  | (-0.557)  | (-0.532)  | (0.418)  | (-0.809) | (-0.591) |         |         |
|                      | CMKT       | 0.956***  | 0.981***  | 0.957***  | 1.051*** | 0.974*** | 0.018    |         |         |
|                      | t ' CMKT ' | (17.645)  | (16.687)  | (23.437)  | (20.700) | (12.221) | (0.234)  |         |         |
| r 4,0                | CSMB       | 0.127***  | 0.192***  | 0.096***  | 0.066    | 0.206*** | 0.079    |   0.004 |   0.606 |
|                      | t ' CSMB ' | (2.876)   | (4.019)   | (2.883)   | (1.599)  | (3.174)  | (1.273)  |         |         |
|                      | CMOM       | -0.262*** | -0.212*** | -0.082*** | 0.059*   | 0.501*** | 0.763*** |         |         |
|                      | t ' CMOM ' | (-7.632)  | (-5.690)  | (-3.171)  | (1.827)  | (9.943)  | (15.810) |         |         |
|                      | R 2        | 0.596     | 0.567     | 0.696     | 0.642    | 0.531    | 0.499    |         |         |


<!-- p:29 -->


| Table 11 Continued   |            | 1        | 2        | 3        | 4        | 5         | 5-1       |   m.a.e |    ̄ R 2 |
|----------------------|------------|----------|----------|----------|----------|-----------|-----------|---------|---------|
|                      |            | 0.006    | 0.002    | -0.005   | 0.000    | 0.001     | -0.005    |         |         |
|                      | t ' '      | (0.433)  | (0.193)  | (-0.582) | (0.024)  | (1.151)   | (-0.362)  |         |         |
|                      | CMKT       | 1.181*** | 1.125*** | 1.069*** | 1.082*** | 0.998***  | -0.183*   |         |         |
|                      | t ' CMKT ' | (10.968) | (14.298) | (15.483) | (14.221) | (155.617) | (-1.688)  |         |         |
| PRCVOL               | CSMB       | 1.120*** | 0.415*** | 0.463*** | 0.274*** | -0.008    | -1.128*** |   0.003 |   0.626 |
|                      | t ' CSMB ' | (12.770) | (6.471)  | (8.236)  | (4.425)  | (-1.492)  | (-12.759) |         |         |
|                      | CMOM       | 0.069    | 0.116**  | -0.029   | -0.030   | -0.001    | -0.070    |         |         |
|                      | t ' CMOM ' | (1.014)  | (2.329)  | (-0.665) | (-0.624) | (-0.324)  | (-1.025)  |         |         |
|                      | R 2        | 0.557    | 0.525    | 0.572    | 0.484    | 0.990     | 0.405     |         |         |
|                      |            | 0.010    | 0.001    | 0.000    | -0.002   | 0.001     | -0.009    |         |         |
|                      | t ' '      | (0.945)  | (0.067)  | (0.017)  | (-0.239) | (1.207)   | (-0.848)  |         |         |
|                      | CMKT       | 1.100*** | 1.200*** | 1.145*** | 1.152*** | 0.995***  | -0.105    |         |         |
|                      | t ' CMKT ' | (12.290) | (12.499) | (16.107) | (15.193) | (152.008) | (-1.160)  |         |         |
| STDPRCVOL            | CSMB       | 0.947*** | 0.559*** | 0.401*** | 0.417*** | -0.012**  | -0.958*** |   0.003 |   0.635 |
|                      | t ' CSMB ' | (12.986) | (7.143)  | (6.923)  | (6.757)  | (-2.194)  | (-13.017) |         |         |
|                      | CMOM       | 0.015    | 0.157**  | -0.034   | 0.026    | -0.002    | -0.017    |         |         |
|                      | t ' CMOM ' | (0.258)  | (2.582)  | (-0.747) | (0.545)  | (-0.540)  | (-0.295)  |         |         |
|                      | R 2        | 0.586    | 0.486    | 0.569    | 0.545    | 0.989     | 0.409     |         |         |

## 5 Other Results

In this section, we describe four sets of additional results: using Bitcoin for short portfolios, the analysis of the Fama-MacBeth regressions, using the stock market factors, and hedging unpriced risks.

### 5.1 Using Bitcoin for Short Portfolios

One concern with constructing the zero-investment strategies in cryptocurrencies is that shorting is not readily available for most of the coins. Table 12 presents the analysis of the strategies that short Bitcoin rather than shorting the relevant factor quintiles. The results are qualitatively similar to those of Section 4. The reason is that most of the relevant factor quintiles behave similarly to Bitcoin. The exceptions are the momentum factors for which the lowest quintiles behave differently from Bitcoin. As a result, the mean returns of the one-, two-, and four-week momentum strategies are no longer statistically significant, and the returns to the Bitcoin zero-investment strategies are somewhat different. We also report the results adjusting for the oneand three-factor cryptocurrency models. For the onefactor cryptocurrency model, the only major difference is that the alpha of the dollar volume strategy is no longer statistically significant. Consistent with the previous section, none of the alphas remain statistically significant controlling for the three-factor cryptocurrency model.


<!-- p:30 -->


### 5.2 Additional Cross-Sectional Results

We first present the results of the cross-sectional regressions using the Fama-MacBeth method in Table 13. We only report the factors that form successful long-short strategies. Panel A shows the results for the size related factors. All of them are individually statistically significant but not jointly significant. This is consistent with the fact that these factors are highly correlated. Panel B shows the results for the volume related factors. The dollar volume factor is individually statistically significant. Panel C shows the results for the volatility factor, which is statistically significant. Panel D shows that the momentum factors are not statistically significant in the Fama-MacBeth regressions. This is different from what we have found in the previous section for the value-weighted portfolio strategies. A potential reason for this discrepancy is that, in essence, the Fama-MacBeth regressions consider each observation equally and thus are close to strategies formed on equally weighted portfolios. In Panel E, we show that the momentum strategies perform strongly for the larger coins, defined as coins with more than 10 million dollar market capitalization. We further confirm this in the Appendix. We double sort first on market capitalization into two groups at the median. Then, within each size group, we sort on the past three-week returns into five groups. We find that the long-short momentum strategy in the below median size group only generates 0.6 percent weekly returns which is not statistically significant. In contrast, the long-short momentum strategy in the above median size group generates statistically significant 4.2 percent weekly returns. This implies that the momentum strategy works better for the larger coins in the cryptocurrency market. This is in sharp contrast to the equity market where momentum strategies work better among smaller stocks (see Hong et al., 2000).


<!-- p:31 -->


##### Table 12: Bitcoin for Short Portfolios

CMKT is the cryptocurrency excess market returns, CSMB is the cryptocurrency size factor, and CMOM is the cryptocurrency momentum factor. The formation of nine quintiles are discussed in Section 3. The t-statistics are reported in the parentheses. *, **, *** denote significance levels at the 10%, 5%, and 1%.

|           |      | Cons     | t        | CMKT     | t       | CSMB     | t        | CMOM     | t        |   R 2 |
|-----------|------|----------|----------|----------|---------|----------|----------|----------|----------|-------|
|           | Mean | 0.034**  | (2.423)  |          |         |          |          |          |          |       |
| MCAP      | C-1  | 0.031**  | (2.216)  | 0.141    | (1.464) |          |          |          |          | 0.008 |
|           | C-3  | 0.004    | (0.601)  | 0.071*   | (1.719) | 1.431*** | (33.786) | -0.024   | (-0.716) | 0.819 |
|           | Mean | 0.039**  | (2.295)  |          |         |          |          |          |          |       |
| PRC       | C-1  | 0.031*   | (1.864)  | 0.397*** | (3.531) |          |          |          |          | 0.046 |
|           | C-3  | 0.015    | (0.978)  | 0.357*** | (3.542) | 0.850*** | (8.237)  | -0.025   | (-0.306) | 0.247 |
|           | Mean | 0.040**  | (2.358)  |          |         |          |          |          |          |       |
| MAXDPRC   | C-1  | 0.032*   | (1.924)  | 0.405*** | (3.571) |          |          |          |          | 0.047 |
|           | C-3  | 0.016    | (1.018)  | 0.363*** | (3.572) | 0.852*** | (8.182)  | -0.012   | (-0.151) | 0.245 |
|           | Mean | 0.009    | (0.694)  |          |         |          |          |          |          |       |
| r 1,0     | C-1  | 0.007    | (0.559)  | 0.085    | (0.991) |          |          |          |          | 0.004 |
|           | C-3  | -0.016   | (-1.345) | 0.027    | (0.345) | 0.378*** | (4.804)  | 0.428*** | (6.949)  | 0.215 |
|           | Mean | 0.018    | (1.498)  |          |         |          |          |          |          |       |
| r 2,0     | C-1  | 0.016    | (1.321)  | 0.102    | (1.277) |          |          |          |          | 0.006 |
|           | C-3  | -0.005   | (-0.439) | 0.050    | (0.684) | 0.295*** | (3.986)  | 0.411*** | (7.083)  | 0.205 |
|           | Mean | 0.030**  | (2.248)  |          |         |          |          |          |          |       |
| r 3,0     | C-1  | 0.036*** | (2.607)  | 0.092    | (0.800) |          |          |          |          | 0.003 |
|           | C-3  | 0.006    | (0.506)  | 0.004    | (0.054) | 0.348*** | (4.536)  | 0.636*** | (10.602) | 0.338 |
|           | Mean | 0.014    | (1.204)  |          |         |          |          |          |          |       |
| r 4,0     | C-1  | 0.012    | (1.000)  | 0.122    | (1.505) |          |          |          |          | 0.009 |
|           | C-3  | -0.012   | (-1.109) | 0.061    | (0.869) | 0.290*** | (4.051)  | 0.506*** | (9.027)  | 0.277 |
|           | Mean | 0.032*   | (1.896)  |          |         |          |          |          |          |       |
| PRCVOL    | C-1  | 0.027    | (1.607)  | 0.254**  | (2.199) |          |          |          |          | 0.018 |
|           | C-3  | 0.001    | (0.041)  | 0.186**  | (2.067) | 1.209*** | (13.087) | 0.079    | (1.090)  | 0.412 |
|           | Mean | 0.030**  | (2.109)  |          |         |          |          |          |          |       |
| STDPRCVOL | C-1  | 0.027*   | (1.853)  | 0.187*   | (1.908) |          |          |          |          | 0.014 |
|           | C-3  | 0.005    | (0.468)  | 0.133*   | (1.751) | 1.033*** | (13.304) | 0.023    | (0.379)  | 0.417 |


<!-- p:32 -->


Table 13: Fama-MacBeth Cross-Sectional Regression

This table reports the Fama-MacBeth regression results. Each factor is first sorted into five portfolios at the end of each week. Panel A, B, C, and D are based on the sample of coins with market capitalizations of more than 1 million dollars. Panel E is based on the sample of coins with market capitalizations of more than 10 million dollars. The t-statistics of the coefficient estimates are reported in the parentheses.*, **, *** denote significance levels at the 10%, 5%, and 1%.

|          | Panel A   | MCAP - PRC - MAXDPRC   | -0.011* - (-1.890)   | -0.008*** - (-3.120)   | ret t + 1 - -0.008*** - (-3.256)   |          | -0.000 - (-0.210) - -0.027 - (-1.136) - 0.019 - (0.802)   |
|----------|-----------|------------------------|----------------------|------------------------|------------------------------------|----------|-----------------------------------------------------------|
|          | Panel B   | PRCVOL                 | -0.006**             |                        |                                    |          |                                                           |
|          |           |                        | (-2.546)             |                        |                                    |          |                                                           |
| > 1 mil  | Panel C   | STDPRCVOL              | -0.007***            |                        |                                    |          |                                                           |
|          |           |                        | (-2.894)             |                        |                                    |          |                                                           |
|          |           | r 1,0                  | -0.002               |                        |                                    |          | -0.004                                                    |
|          |           |                        | (-0.692)             |                        |                                    |          | (-1.427)                                                  |
|          |           | r 2,0                  |                      | 0.000                  |                                    |          | 0.003                                                     |
|          |           |                        |                      | (0.020)                |                                    |          | (0.751)                                                   |
|          | Panel D   | r 3,0                  |                      |                        | -0.000                             |          | -0.002                                                    |
|          |           |                        |                      |                        | (-0.148)                           |          | (-0.499)                                                  |
|          |           | r 4,0                  |                      |                        |                                    | -0.001   | 0.000                                                     |
|          |           |                        |                      |                        |                                    | (-0.274) | (0.107)                                                   |
|          |           | r 1,0                  | 0.005*               |                        |                                    |          | -0.006                                                    |
|          |           |                        | (1.668)              |                        |                                    |          | (-1.520)                                                  |
|          |           | r 2,0                  |                      | 0.007**                |                                    |          | 0.005                                                     |
|          |           |                        |                      | (2.095)                |                                    |          | (0.866)                                                   |
| > 10 mil | Panel E   | r 3,0                  |                      |                        | 0.007**                            |          | 0.006                                                     |
|          |           |                        |                      |                        | (1.978)                            |          | (1.086)                                                   |
|          |           | r 4,0                  |                      |                        |                                    | 0.003    | -0.000                                                    |
|          |           |                        |                      |                        |                                    | (0.693)  | (-0.061)                                                  |


<!-- p:33 -->


##### Table 14: Fama-French Three-Factor Model

$$R _ { i } - R _ { f } = \alpha ^ { i } + \beta _ { M K T } ^ { i } M K T + \beta _ { S M B } ^ { i } S M B + \beta _ { H M L } ^ { i } H M L + \epsilon _ { i }$$

where MKT is the excess stock market returns, SMB is the Fama-French size factor, and HML is the FamaFrench value factor. The formation of the quintile portfolios for the nine significant strategies are discussed in Section 3. The t-statistics are reported in the parentheses. *, **, *** denote significance levels at the 10%, 5%, and 1%. m.a.e and  ̄ R 2 are the mean of the absolute pricing errors and the average R 2 of the five portfolios.

|         |           | 1        | 2        | 3        | 4        | 5        | 5-1      |   m.a.e |    ̄ R 2 |
|---------|-----------|----------|----------|----------|----------|----------|----------|---------|---------|
|         |           | 0.044*** | 0.017    | 0.013    | 0.012    | 0.012    | -0.032** |         |         |
|         | t ' '     | (2.737)  | (1.469)  | (1.220)  | (1.278)  | (1.626)  | (-2.372) |         |         |
|         | MKT       | 0.859    | 0.981    | 0.311    | 0.615    | 0.404    | -0.455   |         |         |
|         | t ' MKT ' | (0.976)  | (1.573)  | (0.551)  | (1.178)  | (1.002)  | (-0.615) |         |         |
| MCAP    | SMB       | -0.298   | -0.966   | 0.124    | -0.412   | -0.682   | -0.384   |   0.020 |   0.008 |
|         | t ' SMB ' | (-0.210) | (-0.961) | (0.136)  | (-0.490) | (-1.050) | (-0.323) |         |         |
|         | HML       | -1.398   | 0.589    | -0.434   | -0.642   | -0.222   | 1.176    |         |         |
|         | t ' HML ' | (-1.014) | (0.603)  | (-0.491) | (-0.786) | (-0.352) | (1.016)  |         |         |
|         | R 2       | 0.008    | 0.013    | 0.002    | 0.008    | 0.007    | 0.007    |         |         |
|         |           | 0.049**  | 0.027**  | 0.000    | 0.017    | 0.011    | -0.037** |         |         |
|         | t ' '     | (2.551)  | (1.999)  | (0.026)  | (1.295)  | (1.560)  | (-2.256) |         |         |
|         | MKT       | 1.254    | 0.503    | 0.624    | 1.125    | 0.396    | -0.858   |         |         |
|         | t ' MKT ' | (1.202)  | (0.669)  | (1.029)  | (1.578)  | (1.010)  | (-0.944) |         |         |
| PRC     | SMB       | -1.295   | -1.512   | -0.403   | -0.837   | -0.592   | 0.702    |   0.021 |   0.008 |
|         | t ' SMB ' | (-0.770) | (-1.249) | (-0.412) | (-0.729) | (-0.938) | (0.480)  |         |         |
|         | HML       | -1.176   | 0.396    | -0.395   | 1.071    | -0.131   | 1.045    |         |         |
|         | t ' HML ' | (-0.720) | (0.337)  | (-0.416) | (0.960)  | (-0.213) | (0.734)  |         |         |
|         | R 2       | 0.008    | 0.007    | 0.005    | 0.014    | 0.006    | 0.006    |         |         |
|         |           | 0.050*** | 0.024*   | 0.001    | 0.020    | 0.011    | -0.039** |         |         |
|         | t ' '     | (2.603)  | (1.793)  | (0.051)  | (1.457)  | (1.553)  | (-2.319) |         |         |
|         | MKT       | 1.180    | 0.499    | 0.609    | 1.111    | 0.395    | -0.785   |         |         |
|         | t ' MKT ' | (1.122)  | (0.673)  | (1.006)  | (1.482)  | (1.008)  | (-0.855) |         |         |
| MAXDPRC | SMB       | -1.565   | -1.195   | -0.381   | -0.636   | -0.592   | 0.972    |   0.021 |   0.007 |
|         | t ' SMB ' | (-0.924) | (-1.001) | (-0.391) | (-0.526) | (-0.938) | (0.658)  |         |         |
|         | HML       | -1.207   | 0.293    | -0.257   | 1.083    | -0.131   | 1.076    |         |         |
|         | t ' HML ' | (-0.733) | (0.252)  | (-0.271) | (0.923)  | (-0.213) | (0.749)  |         |         |
|         | R 2       | 0.008    | 0.005    | 0.004    | 0.012    | 0.006    | 0.006    |         |         |


<!-- p:34 -->


| Table 14 Continued   |           | 1        | 2        | 3        | 4        | 5        | 5-1      |   m.a.e |    ̄ R 2 |
|----------------------|-----------|----------|----------|----------|----------|----------|----------|---------|---------|
|                      |           | -0.008   | -0.003   | 0.009    | 0.042**  | 0.021    | 0.029**  |         |         |
|                      | t ' '     | (-0.732) | (-0.321) | (0.953)  | (2.306)  | (1.495)  | (2.094)  |         |         |
|                      | MKT       | 0.766    | 0.472    | 0.367    | 1.600    | -0.381   | -1.148   |         |         |
|                      | t ' MKT ' | (1.291)  | (0.883)  | (0.745)  | (1.592)  | (-0.498) | (-1.522) |         |         |
| r 1,0                | SMB       | 0.047    | -1.340   | -0.775   | 1.171    | -1.934   | -1.981   |   0.017 |   0.014 |
|                      | t ' SMB ' | (0.049)  | (-1.558) | (-0.978) | (0.724)  | (-1.568) | (-1.631) |         |         |
|                      | HML       | -1.394   | -0.381   | -0.517   | 2.795*   | -0.588   | 0.806    |         |         |
|                      | t ' HML ' | (-1.499) | (-0.456) | (-0.671) | (1.777)  | (-0.490) | (0.682)  |         |         |
|                      | R 2       | 0.016    | 0.011    | 0.006    | 0.026    | 0.013    | 0.027    |         |         |
|                      |           | -0.004   | 0.005    | 0.009    | 0.018*   | 0.029**  | 0.034**  |         |         |
|                      | t ' '     | (-0.402) | (0.457)  | (0.965)  | (1.827)  | (2.218)  | (2.498)  |         |         |
|                      | MKT       | 0.856    | 0.373    | -0.020   | 0.186    | -0.190   | -1.046   |         |         |
|                      | t ' MKT ' | (1.442)  | (0.665)  | (-0.041) | (0.346)  | (-0.261) | (-1.414) |         |         |
| r 2,0                | SMB       | -0.139   | 0.308    | -1.085   | -1.294   | -1.933*  | -1.794   |   0.013 |   0.010 |
|                      | t ' SMB ' | (-0.146) | (0.341)  | (-1.389) | (-1.497) | (-1.654) | (-1.505) |         |         |
|                      | HML       | -0.783   | -0.125   | -0.640   | 0.416    | -1.140   | -0.357   |         |         |
|                      | t ' HML ' | (-0.842) | (-0.142) | (-0.843) | (0.496)  | (-1.003) | (-0.308) |         |         |
|                      | R 2       | 0.011    | 0.003    | 0.010    | 0.010    | 0.015    | 0.022    |         |         |
|                      |           | 0.001    | 0.001    | 0.014    | 0.018*   | 0.043*** | 0.042*** |         |         |
|                      | t ' '     | (0.130)  | (0.087)  | (1.373)  | (1.924)  | (2.961)  | (2.799)  |         |         |
|                      | MKT       | 0.436    | 0.094    | 0.615    | 0.892*   | -0.798   | -1.234   |         |         |
|                      | t ' MKT ' | (0.714)  | (0.174)  | (1.115)  | (1.718)  | (-0.997) | (-1.507) |         |         |
| r 3,0                | SMB       | 1.219    | -0.373   | -0.484   | -0.891   | -1.864   | -3.083** |   0.015 |   0.009 |
|                      | t ' SMB ' | (1.241)  | (-0.431) | (-0.545) | (-1.065) | (-1.446) | (-2.338) |         |         |
|                      | HML       | -0.474   | -0.520   | -0.137   | 0.247    | -0.177   | 0.297    |         |         |
|                      | t ' HML ' | (-0.496) | (-0.619) | (-0.158) | (0.304)  | (-0.141) | (0.232)  |         |         |
|                      | R 2       | 0.011    | 0.002    | 0.005    | 0.014    | 0.015    | 0.038    |         |         |
|                      |           | 0.002    | 0.003    | 0.007    | 0.017*   | 0.026*   | 0.024**  |         |         |
|                      | t ' '     | (0.210)  | (0.265)  | (0.843)  | (1.749)  | (1.969)  | (1.975)  |         |         |
|                      | MKT       | 0.206    | 0.711    | 0.332    | 0.717    | -0.551   | -0.757   |         |         |
|                      | t ' MKT ' | (0.379)  | (1.251)  | (0.706)  | (1.331)  | (-0.750) | (-1.121) |         |         |
| r 4,0                | SMB       | 0.623    | -0.071   | -0.850   | -0.977   | -1.752   | -2.375** |   0.011 |   0.009 |
|                      | t ' SMB ' | (0.712)  | (-0.077) | (-1.120) | (-1.126) | (-1.479) | (-2.183) |         |         |
|                      | HML       | -0.027   | -0.279   | 0.405    | -0.338   | -1.659   | -1.633   |         |         |
|                      | t ' HML ' | (-0.031) | (-0.314) | (0.550)  | (-0.401) | (-1.441) | (-1.544) |         |         |
|                      | R 2       | 0.003    | 0.007    | 0.007    | 0.010    | 0.020    | 0.036    |         |         |


<!-- p:35 -->


| Table 14 Continued   |           | 1        | 2        | 3        | 4        | 5        | 5-1      |   m.a.e |    ̄ R 2 |
|----------------------|-----------|----------|----------|----------|----------|----------|----------|---------|---------|
|                      |           | 0.042**  | 0.026**  | 0.015    | 0.017    | 0.012    | -0.030*  |         |         |
|                      | t ' '     | (2.222)  | (1.987)  | (1.190)  | (1.366)  | (1.607)  | (-1.826) |         |         |
|                      | MKT       | 1.691    | 0.759    | 1.009    | 0.495    | 0.393    | -1.299   |         |         |
|                      | t ' MKT ' | (1.648)  | (1.047)  | (1.506)  | (0.733)  | (0.973)  | (-1.453) |         |         |
| PRCVOL               | SMB       | -1.596   | -0.898   | -0.803   | -0.098   | -0.678   | 0.918    |   0.022 |   0.008 |
|                      | t ' SMB ' | (-0.965) | (-0.769) | (-0.744) | (-0.090) | (-1.043) | (0.638)  |         |         |
|                      | HML       | -0.563   | -0.855   | -0.105   | -0.509   | -0.232   | 0.331    |         |         |
|                      | t ' HML ' | (-0.350) | (-0.752) | (-0.101) | (-0.482) | (-0.368) | (0.236)  |         |         |
|                      | R 2       | 0.012    | 0.007    | 0.009    | 0.003    | 0.007    | 0.009    |         |         |
|                      |           | 0.040**  | 0.029*   | 0.019    | 0.020    | 0.012    | -0.029** |         |         |
|                      | t ' '     | (2.508)  | (1.902)  | (1.491)  | (1.528)  | (1.601)  | (-2.098) |         |         |
|                      | MKT       | 1.302    | 1.322    | 0.894    | 0.721    | 0.393    | -0.909   |         |         |
|                      | t ' MKT ' | (1.475)  | (1.556)  | (1.300)  | (1.007)  | (0.978)  | (-1.215) |         |         |
| STDPRCVOL            | SMB       | -1.251   | -1.581   | -1.137   | -0.172   | -0.678   | 0.573    |   0.024 |   0.009 |
|                      | t ' SMB ' | (-0.880) | (-1.156) | (-1.027) | (-0.149) | (-1.047) | (0.475)  |         |         |
|                      | HML       | -0.517   | -0.734   | -0.667   | -0.417   | -0.221   | 0.296    |         |         |
|                      | t ' HML ' | (-0.374) | (-0.552) | (-0.620) | (-0.372) | (-0.351) | (0.253)  |         |         |
|                      | R 2       | 0.010    | 0.013    | 0.010    | 0.005    | 0.007    | 0.006    |         |         |

### 5.3 Stock Market Factors

We next investigate whether the nine successful long-short strategies can be explained by the stock market risk factors. Previous research (e.g., Asness et al., 2013) finds that value and momentum strategies comove strongly across different asset classes. Hence, the cryptocurrency strategies may comove with their corresponding counterparts in the equity market as well. In this section, we present results controlling for the Fama-French threefactor model. In the Appendix, we also present results based on the Carhart four-factor and the Fama-French five-factor models. The results are qualitatively similar using any of the stock market factor models.

Table 14 presents the results based on the Fama-French three-factor model. Overall, the Fama-French three-factor model adjusted alphas of the strategies are quantitatively similar to the unadjusted excess returns. For example, the adjusted alpha for the market capitalization long-short strategy is -3.2 percent per week with a t-statistic of -2.372. The unadjusted average excess returns of the long-short strategy is -3.4 percent per week with a t-statistic of -2.557. The adjusted alpha for the three-week momentum long-short strategy is 4.2 percent per week with a t-statistic of 2.799. The unadjusted average excess returns of the long-short strategy is 4.1 percent per week with a t-statistic of 2.742.


<!-- p:36 -->


### 5.4 Hedged Strategies

Recent empirical asset pricing literature has found that the common practice to create factor-portfolios by sorting on characteristics associated with average returns captures both priced and unpriced risks. Daniel et al. (2018) develop a method to hedge the unpriced risks in the stock market using covariance information estimated from past returns. In this section, we apply their method to our factors and evaluate whether we can further strengthen the performance of our cryptocurrency factors.

We follow the procedure in Daniel et al. (2018) and provide an example based on the cryptocurrency size factor. Detailed descriptions of the theoretical motivation and empirical account can be found in Daniel et al. (2018). We first rank all cryptocurrencies by their previous week market capitalization. Break-points are selected at the 30 percent and 70 percent marks. Then, all cryptocurrencies are assigned to one of the three bins. Next, each of the three bins is further sorted into three equal bins based on the coins' expected covariances with the cryptocurrency size factor. Therefore, cryptocurrencies with similar size but different loadings on size factor are assigned into different bins. We estimate the expected covariance between coin returns and the size factor using the rolling past 365 days of data. Finally, the hedge-portfolio for the cryptocurrency size factor is constructed as going long on an equal-weighted portfolio of the low size-factor-loading portfolios and short on an equal-weighted portfolio of the high size-factor-loading portfolios. We find that the hedgeportfolio does not carry statistically significant return spreads for either the cryptocurrency size strategy or momentum strategy, similar to findings in the stock market (See Daniel and Titman, 1997). Therefore, the construction ensures that the hedge-portfolio captures unpriced risks. We construct the cryptocurrency momentum hedge-portfolio in the same way.

We use the squared Sharpe-ratio to evaluate the performance of the strategies. For the cryptocurrency size factor, we find considerable gains from hedging the unpriced risks. The squared weekly Sharpe-ratio goes from 0.057 for the unhedged strategy to 0.076 for the hedged strategy when the hedge-portfolio is available. The gains are economically large. However, for the cryptocurrency momentum factor, the adjustment does not increase the squared Sharpe-ratio of the momentum strategy. One possibility for the lack of improvement of the cryptocurrency momentum strategy is that the expected loadings on the momentum factors change faster and are more transient than those on the size factors.


<!-- p:37 -->


## 6 Conclusion

The results of this paper show that the cross-section of cryptocurrencies can be meaningfully analyzed using standard asset pricing tools. We document that, similar to other asset classes (see, e.g., Asness et al., 2013), size and momentum factors are important in capturing the cross-section of cryptocurrency returns. Moreover, a parsimonious three-factor model that can be constructed using the market information is successful in pricing the strategies in the cryptocurrency market. The paper thus establishes a set of stylized facts on the cross-section of cryptocurrencies that can be used to assess and develop theoretical models.


<!-- p:38 -->

## Online Appendix

##### Table A.1: Summary Statistics of Factors

Panel A reports mean, median, standard deviation, skewness, and kurtosis of the cryptocurrency market excess returns, the cryptocurrency size factor returns, and the cryptocurrency momentum factor returns. Panel B reports the correlation matrix of the cryptocurrency market excess returns, the cryptocurrency size factor returns, the cryptocurrency momentum factor returns, the Bitcoin returns, the Ethereum returns, and the Ripple returns.

| Panel A              |   Panel A - Mean |   Panel A - Median |   Panel A - SD |   Panel A - Skewness |   Panel A - Kurtosis |
|----------------------|------------------|--------------------|----------------|----------------------|----------------------|
| Market Excess Return |            0.013 |              0.005 |          0.117 |                0.292 |                4.574 |
| Size Return          |            0.020 |             -0.005 |          0.143 |                3.067 |               19.616 |
| Mom Return           |            0.038 |              0.034 |          0.184 |                0.791 |                7.868 |

| Panel B              |   Panel B - CMKT |   Panel B - CSIZE |   Panel B - CMOM |   Panel B - Bitcoin |   Panel B - Ethereum |   Panel B - Ripple |
|----------------------|------------------|-------------------|------------------|---------------------|----------------------|--------------------|
| Market Excess Return |            1.000 |                   |                  |                     |                      |                    |
| Size Return          |            0.187 |             1.000 |                  |                     |                      |                    |
| Mom Return           |           -0.001 |            -0.033 |            1.000 |                     |                      |                    |
| Bitcoin Return       |            0.927 |             0.055 |           -0.030 |               1.000 |                      |                    |
| Ethereum Return      |            0.531 |             0.146 |           -0.019 |               0.367 |                1.000 |                    |
| Ripple Return        |            0.549 |             0.268 |            0.022 |               0.376 |                0.289 |              1.000 |

##### Table A.2: Double Sort on Size and Momentum

This table shows results based on double sorting on both the size and momentum factors. Each coin is first sorted into one of two size portfolios. Within each size portfolio, the coins are further sorted into one of five momentum portfolios. *, **, *** denote significance levels at the 10%, 5%, and 1%.

|      | Momentum - 1 - Low   | Momentum - 2   | Momentum - 3   | Momentum - 4 - High   | Momentum - 5 - High   | Momentum - 5 - 1 - High   |
|------|----------------------|----------------|----------------|-----------------------|-----------------------|---------------------------|
| Low  | 0.032**              | 0.015          | 0.020*         | 0.015                 | 0.039**               | 0.006                     |
|      | (2.05)               | (1.29)         | (1.72)         | (1.26)                | (2.05)                | (0.30)                    |
| High | -0.002               | -0.00          | 0.018          | 0.019**               | 0.040**               | 0.042***                  |
|      | (-0.15)              | (-0.01)        | (1.60)         | (1.98)                | (2.48)                | (2.57)                    |


<!-- p:44 -->


##### Table A.3: Carhart Four-Factor

$$R _ { i } - R _ { f } = \alpha ^ { i } + \beta _ { M K T } ^ { i } M K T + \beta _ { S M B } ^ { i } S M B + \beta _ { H M L } ^ { i } H M L + \beta _ { M O M } ^ { i } M O M + \epsilon _ { i }$$

where MKT is the excess stock market returns, SMB is the Fama-French size factor, HML is the FamaFrench value factor, and MOM is the momentum factor. The formation of the quintile portfolios for the nine significant strategies are discussed in Section 3. *, **, *** denote significance levels at the 10%, 5%, and 1%. m.a.e and  ̄ R 2 are the mean of the absolute pricing errors and the average R 2 of the five portfolios.

|             | 1        | 2       |      3 | 4       | 5       | 5-1      |   m.a.e |    ̄ R 2 |
|-------------|----------|---------|--------|---------|---------|----------|---------|---------|
|             | 0.043*** | 0.017   |  0.012 | 0.012   | 0.012   | -0.031** |   0.019 |   0.008 |
| MKT         | 0.937    | 0.998   |  0.333 | 0.672   | 0.400   | -0.536   |   0.019 |   0.008 |
| MCAP SMB    | -0.177   | -0.941  |  0.159 | -0.322  | -0.689  | -0.512   |   0.019 |   0.008 |
| HML         | -1.023   | 0.667   | -0.326 | -0.365  | -0.244  | 0.779    |   0.019 |   0.008 |
| MOM         | 0.607    | 0.126   |  0.175 | 0.449   | -0.036  | -0.643   |   0.019 |   0.008 |
| R 2         | 0.009    | 0.013   |  0.003 | 0.010   | 0.007   | 0.009    |   0.019 |   0.008 |
|             | 0.049**  | 0.027** |  0.000 | 0.017   | 0.011   | -0.038** |   0.021 |   0.008 |
| MKT         | 1.210    | 0.522   |  0.637 | 1.112   | 0.410   | -0.800   |         |   0.008 |
| PRC SMB     | -1.364   | -1.483  | -0.383 | -0.857  | -0.571  | 0.792    |         |   0.008 |
| HML         | -1.392   | 0.485   | -0.335 | 1.008   | -0.067  | 1.325    |         |   0.008 |
| MOM         | -0.351   | 0.144   |  0.096 | -0.104  | 0.103   | 0.454    |         |   0.008 |
| R 2         | 0.009    | 0.008   |  0.005 | 0.014   | 0.006   | 0.006    |         |   0.008 |
|             | 0.050*** | 0.024*  |  0.000 | 0.020   | 0.011   | -0.039** |         |   0.008 |
| MKT         | 1.157    | 0.515   |  0.631 | 1.077   | 0.409   | -0.748   |         |   0.008 |
| MAXDPRC SMB | -1.601   | -1.169  | -0.346 | -0.690  | -0.571  | 1.030    |   0.021 |   0.008 |
| HML         | -1.319   | 0.373   | -0.148 | 0.913   | -0.064  | 1.255    |         |   0.008 |
| MOM         | -0.183   | 0.128   |  0.176 | -0.276  | 0.107   | 0.290    |         |   0.008 |
| R 2         | 0.009    | 0.005   |  0.005 | 0.013   | 0.006   | 0.006    |         |   0.008 |
|             | -0.009   | -0.003  |  0.008 | 0.042** | 0.021   | 0.029**  |         |         |
| MKT         | 0.927    | 0.467   |  0.408 | 1.604   | -0.337  | -1.265*  |         |         |
| r 1,0 SMB   | 0.298    | -1.348  | -0.711 | 1.178   | -1.866  | -2.165*  |   0.017 |   0.017 |
| HML         | -0.613   | -0.406  | -0.319 | 2.816   | -0.376  | 0.237    |         |         |
| MOM         | 1.265*   | -0.041  |  0.320 | 0.032   | 0.343   | -0.922   |         |         |
| R 2         | 0.028    | 0.011   |  0.007 | 0.026   | 0.014   | 0.031    |         |         |
|             | -0.005   | 0.005   |  0.009 | 0.017*  | 0.029** | 0.034**  |         |         |
| MKT         | 0.979    | 0.329   | -0.064 | 0.270   | -0.121  | -1.100   |         |         |
| r 2,0 SMB   | 0.053    | 0.239   | -1.153 | -1.163  | -1.826  | -1.879   |   0.013 |   0.013 |
| HML         | -0.186   | -0.337  | -0.854 | 0.823   | -0.807  | -0.620   |         |         |
| MOM         | 0.967    | -0.345  | -0.347 | 0.658   | 0.539   | -0.428   |         |         |
| R 2         | 0.018    | 0.004   |  0.012 | 0.014   | 0.017   | 0.022    |         |         |


<!-- p:45 -->


| Table A.3 Continued   |     | 1       | 2       |      3 | 4      | 5        | 5-1      |   m.a.e |    ̄ R 2 |
|-----------------------|-----|---------|---------|--------|--------|----------|----------|---------|---------|
|                       |     | 0.001   | 0.001   |  0.014 | 0.018* | 0.042*** | 0.041*** |   0.015 |   0.012 |
|                       | MKT | 0.494   | 0.082   |  0.596 | 0.952* | -0.636   | -1.130   |         |   0.012 |
| r 3,0                 | SMB | 1.309   | -0.391  | -0.514 | -0.798 | -1.610   | -2.920** |         |   0.012 |
|                       | HML | -0.193  | -0.578  | -0.230 | 0.537  | 0.611    | 0.804    |         |   0.012 |
|                       | MOM | 0.455   | -0.095  | -0.152 | 0.468  | 1.277    | 0.823    |         |   0.012 |
|                       | R 2 | 0.013   | 0.002   |  0.005 | 0.016  | 0.022    | 0.041    |         |   0.012 |
|                       |     | 0.002   | 0.002   |  0.007 | 0.017* | 0.026*   | 0.024*   |         |   0.012 |
|                       | MKT | 0.264   | 0.738   |  0.304 | 0.718  | -0.426   | -0.690   |         |   0.012 |
| r 4,0                 | SMB | 0.713   | -0.028  | -0.895 | -0.976 | -1.556   | -2.270** |   0.011 |   0.011 |
|                       | HML | 0.253   | -0.148  |  0.264 | -0.335 | -1.054   | -1.307   |         |   0.012 |
|                       | MOM | 0.453   | 0.212   | -0.230 | 0.005  | 0.981    | 0.529    |         |   0.012 |
|                       | R 2 | 0.005   | 0.007   |  0.008 | 0.010  | 0.025    | 0.038    |         |   0.012 |
|                       |     | 0.049** | 0.027** |  0.000 | 0.017  | 0.011    | -0.038** |         |         |
|                       | MKT | 1.210   | 0.522   |  0.637 | 1.112  | 0.410    | -0.800   |         |         |
| PRCVOL                | SMB | -1.364  | -1.483  | -0.383 | -0.857 | -0.571   | 0.792    |   0.021 |   0.008 |
|                       | HML | -1.392  | 0.485   | -0.335 | 1.008  | -0.067   | 1.325    |         |         |
|                       | MOM | -0.351  | 0.144   |  0.096 | -0.104 | 0.103    | 0.454    |         |         |
|                       | R 2 | 0.009   | 0.008   |  0.005 | 0.014  | 0.006    | 0.006    |         |         |
|                       |     | 0.040** | 0.029*  |  0.019 | 0.019  | 0.012    | -0.028** |         |         |
|                       | MKT | 1.380   | 1.305   |  0.873 | 0.796  | 0.389    | -0.992   |         |         |
| STDPRCVOL             | SMB | -1.129  | -1.608  | -1.170 | -0.054 | -0.686   | 0.443    |   0.024 |   0.009 |
|                       | HML | -0.139  | -0.818  | -0.772 | -0.053 | -0.246   | -0.107   |         |         |
|                       | MOM | 0.612   | -0.137  | -0.170 | 0.590  | -0.042   | -0.654   |         |         |
|                       | R 2 | 0.011   | 0.013   |  0.010 | 0.006  | 0.007    | 0.008    |         |         |


<!-- p:46 -->


##### Table A.4: Fame-French Five-Factor

$$R _ { i } - R _ { f } = \alpha ^ { i } + \beta _ { M K T } ^ { i } M K T + \beta _ { S M B } ^ { i } S M B + \beta _ { H M L } ^ { i } H M L + \beta _ { R M W } ^ { i } R M W + \beta _ { C M A } ^ { i } C M A + \epsilon _ { i } \quad \ \ ( 7 )$$

where MKT is the excess stock market returns, SMB is the Fama-French size factor, HML is the Fama-French value factor, and RMW is the Fama French profitability factor, and CMA is the Fama French investment factor. The formation of the quintile portfolios for the nine significant strategies are discussed in Section 3. *, **, *** denote significance levels at the 10%, 5%, and 1%. m.a.e and  ̄ R 2 are the mean of the absolute pricing errors and the average R 2 of the five portfolios.

|         |     | 1        | 2       |      3 | 4       | 5       | 5-1      |   m.a.e |    ̄ R 2 |
|---------|-----|----------|---------|--------|---------|---------|----------|---------|---------|
|         |     | 0.045*** | 0.017   |  0.013 | 0.013   | 0.012   | -0.033** |         |         |
|         | MKT | 0.903    | 0.762   |  0.164 | 0.555   | 0.357   | -0.546   |         |         |
|         | SMB | -0.554   | -1.326  |  0.001 | -0.747  | -0.743  | -0.188   |         |         |
| MCAP    | HML | -1.992   | 0.716   | -0.143 | -1.020  | -0.163  | 1.829    |   0.020 |   0.011 |
|         | RMW | -1.147   | -1.932  | -0.744 | -1.636  | -0.341  | 0.806    |         |         |
|         | CMA | 1.789    | -0.129  | -0.723 | 1.243   | -0.123  | -1.912   |         |         |
|         | R 2 | 0.010    | 0.018   |  0.004 | 0.015   | 0.007   | 0.009    |         |         |
|         |     | 0.049**  | 0.028** |  0.001 | 0.017   | 0.011   | -0.038** |         |         |
|         | MKT | 1.395    | 0.368   |  0.758 | 1.240   | 0.305   | -1.090   |         |         |
|         | SMB | -1.593   | -1.813  | -0.619 | -0.766  | -0.614  | 0.980    |         |         |
| PRC     | HML | -2.178   | 0.335   | -1.227 | 0.800   | 0.145   | 2.322    |   0.021 |   0.011 |
| PRC     | RMW | -1.231   | -1.561  | -0.853 | 0.461   | -0.206  | 1.025    |         |         |
| PRC     | CMA | 2.935    | 0.352   |  2.416 | 0.705   | -0.742  | -3.676   |         |         |
| PRC     | R 2 | 0.012    | 0.010   |  0.011 | 0.015   | 0.007   | 0.012    |         |         |
|         |     | 0.051*** | 0.025*  |  0.001 | 0.020   | 0.011   | -0.040** |         |         |
|         | MKT | 1.386    | 0.328   |  0.670 | 1.240   | 0.304   | -1.082   |         |         |
|         | SMB | -1.856   | -1.503  | -0.669 | -0.548  | -0.614  | 1.242    |         |         |
| MAXDPRC | HML | -2.419   | 0.343   | -0.964 | 0.793   | 0.146   | 2.565    |   0.022 |   0.010 |
| MAXDPRC | RMW | -1.119   | -1.635  | -1.271 | 0.553   | -0.209  | 0.910    |         |         |
| MAXDPRC | CMA | 3.506    | 0.050   |  2.119 | 0.744   | -0.745  | -4.251   |         |         |
| MAXDPRC | R 2 | 0.013    | 0.008   |  0.011 | 0.013   | 0.007   | 0.013    |         |         |
| MAXDPRC |     | -0.008   | -0.003  |  0.008 | 0.041** | 0.022   | 0.029**  |         |         |
| MAXDPRC | MKT | 0.701    | 0.530   |  0.344 | 2.065*  | -0.548  | -1.249   |         |         |
| MAXDPRC | SMB | -0.135   | -1.344  | -0.790 | 1.675   | -2.363* | -2.228*  |         |         |
| r 1,0   | HML | -1.484   | -0.587  | -0.466 | 2.075   | -0.759  | 0.724    |   0.016 |   0.017 |
| r 1,0   | RMW | -0.924   | 0.048   | -0.098 | 2.879   | -2.189  | -1.265   |         |         |
| r 1,0   | CMA | 0.359    | 0.570   | -0.130 | 1.676   | 0.732   | 0.373    |         |         |
| r 1,0   | R 2 | 0.017    | 0.011   |  0.006 | 0.031   | 0.018   | 0.029    |         |         |


<!-- p:47 -->


| Table A.4 Continued   |     | 1       | 2       |      3 | 4      | 5        | 5-1      |   m.a.e |    ̄ R 2 |
|-----------------------|-----|---------|---------|--------|--------|----------|----------|---------|---------|
|                       |     | -0.004  | 0.005   |  0.008 | 0.017* | 0.030**  | 0.034**  |         |         |
|                       | MKT | 0.632   | 0.282   |  0.057 | 0.341  | -0.336   | -0.968   |         |         |
|                       | SMB | -0.324  | 0.012   | -0.991 | -0.926 | -2.365*  | -2.041   |         |         |
| r 2,0                 | HML | -0.334  | -0.327  | -0.741 | 0.525  | -1.386   | -1.053   |   0.013 |   0.014 |
|                       | RMW | -1.122  | -1.482  |  0.525 | 1.889  | -2.180   | -1.058   |         |         |
|                       | CMA | -1.120  | 0.736   |  0.221 | -0.520 | 0.940    | 2.061    |         |         |
|                       | R 2 | 0.014   | 0.007   |  0.011 | 0.017  | 0.020    | 0.025    |         |         |
|                       |     | 0.002   | 0.001   |  0.013 | 0.018* | 0.044*** | 0.042*** |         |         |
|                       | MKT | 0.304   | 0.106   |  0.563 | 0.916  | -0.695   | -0.999   |         |         |
|                       | SMB | 0.901   | -0.478  | -0.378 | -0.723 | -2.170   | -3.071** |         |         |
| r 3,0                 | HML | -0.572  | -0.746  |  0.229 | 0.459  | -1.060   | -0.488   |   0.016 |   0.012 |
|                       | RMW | -1.632  | -0.479  |  0.434 | 0.810  | -1.306   | 0.326    |         |         |
|                       | CMA | 0.464   | 0.685   | -1.066 | -0.682 | 2.614    | 2.149    |         |         |
|                       | R 2 | 0.015   | 0.003   |  0.007 | 0.016  | 0.020    | 0.040    |         |         |
|                       |     | 0.002   | 0.003   |  0.007 | 0.017* | 0.027**  | 0.025**  |         |         |
|                       | MKT | 0.181   | 0.671   |  0.317 | 0.720  | -0.259   | -0.439   |         |         |
|                       | SMB | 0.602   | -0.228  | -0.801 | -0.818 | -1.813   | -2.415** |         |         |
| r 4,0                 | HML | 0.024   | -0.414  |  0.541 | -0.070 | -2.770*  | -2.794** |   0.011 |   0.011 |
|                       | RMW | -0.130  | -0.780  |  0.206 | 0.743  | 0.049    | 0.179    |         |         |
|                       | CMA | -0.125  | 0.467   | -0.402 | -0.832 | 3.088    | 3.213    |         |         |
|                       | R 2 | 0.003   | 0.008   |  0.008 | 0.012  | 0.026    | 0.043    |         |         |
|                       |     | 0.043** | 0.028** |  0.014 | 0.017  | 0.012    | -0.031*  |         |         |
|                       | MKT | 1.450   | 0.719   |  1.156 | 0.886  | 0.327    | -1.123   |         |         |
|                       | SMB | -2.261  | -1.451  | -0.652 | -0.139 | -0.749   | 1.512    |         |         |
| PRCVOL                | HML | -0.891  | -1.677  | -0.344 | -1.923 | -0.130   | 0.761    |   0.023 |   0.014 |
|                       | RMW | -3.382  | -2.623  |  0.874 | 0.263  | -0.411   | 2.971    |         |         |
|                       | CMA | 1.306   | 2.596   |  0.565 | 3.908* | -0.235   | -1.541   |         |         |
|                       | R 2 | 0.018   | 0.018   |  0.011 | 0.014  | 0.007    | 0.015    |         |         |
|                       |     | 0.041** | 0.031** |  0.018 | 0.021  | 0.012    | -0.030** |         |         |
|                       | MKT | 1.176   | 1.124   |  1.160 | 0.873  | 0.333    | -0.843   |         |         |
|                       | SMB | -1.662  | -2.271  | -1.038 | -0.484 | -0.744   | 0.918    |         |         |
| STDPRCVOL             | HML | -0.798  | -1.250  | -1.406 | -1.477 | -0.126   | 0.672    |   0.025 |   0.014 |
|                       | RMW | -2.065  | -3.442  |  0.767 | -1.279 | -0.379   | 1.687    |         |         |
|                       | CMA | 1.021   | 1.836   |  1.972 | 3.101  | -0.221   | -1.242   |         |         |
|                       | R 2 | 0.013   | 0.023   |  0.013 | 0.012  | 0.007    | 0.010    |         |         |


<!-- p:48 -->


##### Table A.5: Crypto Factor - Tercile

CMKT is the cryptocurrency excess market returns, CSMB is the cryptocurrency size factor, and CMOM is the cryptocurrency momentum factor. The formation of the quintile portfolios for the nine significant strategies are discussed in Section 3. The t-statistics are reported in the parentheses. *, **, *** denote significance level at the 10%, 5%, and 1%.

|           |      | Cons     | t        | CMKT      | t         | CSMB      | t         | CMOM     | t        |   R 2 |
|-----------|------|----------|----------|-----------|-----------|-----------|-----------|----------|----------|-------|
|           | Mean | -0.015*  | (-1.810) |           |           |           |           |          |          |       |
| MCAP      | C-1  | -0.013   | (-1.633) | -0.121*   | (-1.741)  |           |           |          |          | 0.012 |
|           | C-3  | 0.004**  | (1.970)  | -0.006    | (-0.369)  | -0.893*** | (-72.831) | -0.004   | (-0.429) | 0.994 |
|           | Mean | -0.027** | (-2.080) |           |           |           |           |          |          |       |
| PRC       | C-1  | -0.022*  | (-1.721) | -0.441*** | (-4.094)  |           |           |          |          | 0.062 |
|           | C-3  | -0.010   | (-0.815) | -0.365*** | (-3.621)  | -0.544*** | (-6.630)  | -0.047   | (-0.738) | 0.201 |
|           | Mean | -0.027** | (-2.099) |           |           |           |           |          |          |       |
| MAXDPRC   | C-1  | -0.022*  | (-1.741) | -0.436*** | (-4.070)  |           |           |          |          | 0.061 |
|           | C-3  | -0.010   | (-0.819) | -0.359*** | (-3.589)  | -0.545*** | (-6.685)  | -0.051   | (-0.807) | 0.203 |
|           | Mean | 0.041*** | (3.719)  |           |           |           |           |          |          |       |
| r 1,0     | C-1  | 0.041*** | (3.633)  | 0.060     | (0.628)   |           |           |          |          | 0.002 |
|           | C-3  | 0.021**  | (2.072)  | -0.019    | (-0.219)  | 0.127*    | (1.852)   | 0.479*** | (8.947)  | 0.246 |
|           | Mean | 0.029*** | (2.698)  |           |           |           |           |          |          |       |
| r 2,0     | C-1  | 0.030*** | (2.997)  | 0.168**   | (1.978)   |           |           |          |          | 0.015 |
|           | C-3  | 0.007    | (1.031)  | 0.089     | (1.484)   | -0.014    | (-0.286)  | 0.618*** | (16.236) | 0.519 |
|           | Mean | 0.031*** | (2.836)  |           |           |           |           |          |          |       |
| r 3,0     | C-1  | 0.030*** | (2.696)  | 0.120     | (1.287)   |           |           |          |          | 0.006 |
|           | C-3  | -0.003   | (-0.828) | 0.005     | (0.147)   | -0.009    | (-0.346)  | 0.897*** | (44.227) | 0.886 |
|           | Mean | 0.027**  | (2.518)  |           |           |           |           |          |          |       |
| r 4,0     | C-1  | 0.025**  | (2.340)  | 0.157*    | (1.742)   |           |           |          |          | 0.012 |
|           | C-3  | 0.000    | (0.029)  | 0.073     | (1.218)   | -0.046    | (-0.943)  | 0.692*** | (18.278) | 0.576 |
|           | Mean | -0.020*  | (-1.686) |           |           |           |           |          |          |       |
| PRCVOL    | C-1  | -0.017   | (-1.408) | -0.300*** | (-2.920)  |           |           |          |          | 0.032 |
|           | C-3  | 0.002    | (0.231)  | -0.181**  | (-2.184)  | -0.805*** | (-11.921) | -0.113** | (-2.153) | 0.385 |
|           | Mean | -0.021*  | (-1.764) |           |           |           |           |          |          |       |
| STDPRCVOL | C-1  | -0.018   | (-1.494) | -0.284*** | (-2.845)  |           |           |          |          | 0.031 |
|           | C-3  | 0.001    | (0.820)  | 0.998***  | (171.436) | -0.006    | (-1.170)  | -0.002   | (-0.588) | 0.992 |

<!-- END SOURCE 32/40: Liu_2022_common-risk-factors-cryptocurrency.md -->

---

<!-- BEGIN SOURCE 33/40: Mise_2005_hp-filter-time-series-endpoints.md -->

# Source: `Mise_2005_hp-filter-time-series-endpoints.md`

---
id: "Mise_2005_hp-filter-time-series-endpoints"
source_pdf: "../pdf/Mise_2005_hp-filter-time-series-endpoints.pdf"
source_filename: "Mise_2005_hp-filter-time-series-endpoints.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 104.8
visual_assets: "disabled"
---

<!-- p:1 -->

##### UNIVERSITY OF NOTTINGHAM

RLUNIVERSSIYO

## Discussion Papers in Economics

Discussion Paper No.03/08

##### THE HODRICK-PRESCOTT FILTER AT TIME SERIES ENDPOINTS

by Emi Mise, Tae-Hwan Kim and Paul Newbold


<!-- p:2 -->


##### UNIVERSITY OF NOTTINGHAM

### Discussion Papers in Economics

Discussion Paper No.03/08

##### THE HODRICK-PRESCOTT FILTER AT TIME SERIES ENDPOINTS

by Emi Mise, Tae-Hwan Kim and Paul Newbold

Emi Mise is Lecturer, University of Edinburgh, Tae-Hwan Kim is Lecturer and Paul Newbold is Professor, both in the School of Economics, University of Nottingham

May 2003


<!-- p:3 -->


#### The Hodrick-Prescott filter at time series endpoints

Emi Mise, Tae-Hwan Kim and Paul Newbold

####### Department of Economics, University of Nottingham Nottingham, NG7 2RD, UK

####### Abstract

The Hodrick-Prescott filter is often applied to economic series as part of the study of business cycles. Its properties have most frequently been explored through the development of essentially asymptotic results which are practically relevant only some distance from series endpoints. Our concern here is with the most recent observations, as policy-makers will often require an assessment of whether, and by how much, an economic variable is "above trend." We show that if such an issue is important, an easily implemented adjustment to the filter is desirable.


<!-- p:4 -->


####### 1Introduction

a n- o s sn  n n  cus n oo a given time series in an attempt to isolate "its cyclical component." The outcome will depend of course on precisely what approach is taken to detrending. Although there is no uniquely satisfactory answer to this question, a frequently employed strategy is to apply to the raw data a filter proposed by Hodrick and Prescott (1980) in a discussion paper, published many years later essentially unchanged as Hodrick and Prescott (1997). Although their procedure is universally referred to as "the Hodrick-Prescott filter," it should be noted that Akaike (1980) proposed precisely the same approach in the context of seasonal adjustment. The Akaike model incorporates a seasonal component in addition to trend and cyclical components, but his approach to isolating individual components is the same as that of Hodrick and Prescott, whose filter amounts to a special case of Akaike's procedure when seasonality is absent.

The Hodrick-Prescott (HP) filter was not developed to be appropriate, much less optimal, for specific time series generating processes. Rather, apart from the possible choice of a single "smoothness parameter," the same filter is intended to be applied to all series. It is motivated through plausibility rather than optimality considerations. Indeed, even the single free parameter value is generally chosen subjectively, on rather ad hoc grounds. Nevertheless, the properties of the filter have been analysed by, for example King and Rebelo (1993) and Ehglen (1998), from the viewpoint of optimal signal extraction. We discuss this issue in the following section, noting that if a given time series is generated by a process that is integrated of order one or two and is autoregressive-moving average on reduction by differencing to stationarity, HP yields a decomposition that is optimal into orthogonal components that can be regarded as "trend" and "cycle." However, estimated components will not obey the same generating processes as the corresponding "true" components, and a further line of enquiry, as in Harvey and Jaeger (1993) and Cogley and Nason (1995), is to consider the stochastic properties of the estimated components induced by the filter. Also in Section 2 we provide an extended discussion of the application of the HP filter to a random walk.

The optimality result of the previous paragraph is based on application of the filter to an infinitely long time series, though for all practical purposes it applies also to the estimation of components at the centre of a moderately long series. However, our concern in the remainder of this paper is with cyclical components estimation for the most recent time periods, which will be of most interest for example to policy makers. Results on HP optimality do not apply here, and indeed the filter is demonstrably suboptimal. Sections 3 and 4 of the paper explore the extent of that suboptimality for individual data generating processes from two perspectives that are apparently distinct, but in fact are very closely connected.


<!-- p:5 -->


In Section 3, we continue with the notion that there exists a "true" cyclical component, and that the purpose of the filter is to estimate that component. We further take the standpoint that the true component is the one for which HP yields optimal estimates at the series centre, and go on to assess the quality of the most recent HP figures as estimates of the most recent values of that component.

The consequences of HP filtering at time series endpoints can be explored without overt recourse to the concept of "true" components - after all, that concept is not present in the original work of Hodrick and Prescott. We do so in Section 4 through the notion of endpoint revisions. Suppose, having computed an HP decomposition for a given time series, further time elapses and more data accumulate. The filter could be re-applied to the extended data set, which would yield revisions to the original components estimates at the most recent time periods. Although such revisions are necessary (and desirable), one would hope, if current cyclical values are to be taken seriously, sthp   s   t        tads to revisions with larger standard deviations than necessary, and we analyse and illustrate the extent of this suboptimality. Finally, Section 5 concludes.

####### 2 Some technical issues

Given a series of observations yt (t = 1, 2, ..., T) on a time series, the HP filter is an additive decomposition

$$y _ { t } = y _ { t } ^ { g } + y _ { t } ^ { c }$$

where yt is identified as a growth (trend) component and yf as a cyclical component. In much of the business cycle literature, the purpose is to analyse relationships among the cyclical components of given time series. Hodrick and Prescott estimate the growth component as êt through solution of the constrained minimisation problem

$$\min _ { [ y _ { t } ^ { g } ] _ { t = 1 } ^ { T } } \sum _ { t = 1 } ^ { T } ( y _ { t } - y _ { t } ^ { g } ) ^ { 2 } + \lambda \sum _ { t = 2 } ^ { T - 1 } \left [ ( y _ { t + 1 } ^ { g } - y _ { t } ^ { g } ) - ( y _ { t } ^ { g } - y _ { t - 1 } ^ { g } ) \right ] ^ { 2 } \ \ ; \ \ \lambda > 0 \ \ ( 1 )$$

where the parameter λ controls the smoothness of the estimated growth component. Hodrick and Prescott (1980/1997) proposed on somewhat subjective grounds a value λ = 1600, and we shall follow much applied work that exploits the HP filter in employing that value in the bulk of this paper. However, in research that has gone largely unnoticed in this field, Akaike (1980), while further allowing a seasonal component in the decomposition, proposed precisely the HP approach together with a data-dependent Bayesian procedure for the choice of λ.


<!-- p:6 -->


Apart from the choice of λ, the structure of the HP filter is identical for all time series. In that sense, one might say that it is not intended to provide "optimal" cyclical component estimates êc = (yt-Îi) for specific time series. Nevertheless, the filter that results from the solution to (1) can be viewed in terms of the optimal signal extraction literature pioneered by Wiener (1949) and Whittle (1963) and, crucially in the present context, extended by Bell (1984) to incorporate integrated time series generating processes. Results in that literature generally apply to infinitely long series, or in practical terms relate to the midpoints, but not the endpoints, of series of practically interesting length. In subsequent sections we shall be interested in endpoint issues, but here we review the asymptotic optimality results. King and Rebelo (1993) and Ehglen (1998) analysed the HP filter in this framework. It can be shown that the estimated cyclical component is provided by the symmetric two-sided filter

$$\hat { y } _ { t } ^ { c } = H ( L ) y _ { t } \quad ; \quad H ( L ) = \frac { ( 1 - L ) ^ { 2 } ( 1 - L ^ { - 1 } ) ^ { 2 } } { \lambda ^ { - 1 } + ( 1 - L ) ^ { 2 } ( 1 - L ^ { - 1 } ) ^ { 2 } } \quad ( 2 )$$

where L is the lag operator. The HP filter is optimal, in expected squared error sense, for data generating processes of the form

$$( 1 - L ) ^ { 2 } y _ { t } ^ { g } \ & = \ A ( L ) \varepsilon _ { t } \quad ; \quad y _ { t } ^ { c } = A ( L ) u _ { t } \\ A ( L ) \ & = \ \sum _ { j = 0 } ^ { \infty } a _ { j } L ^ { j } \quad ; \quad \sum _ { j = 0 } ^ { \infty } a _ { j } ^ { 2 } < \infty$$

where εt and ut are mutually stochastically uncorrelated white noise processes, so that

$$E ( \varepsilon _ { t } u _ { s } ) = 0 \quad ; \quad \forall \ t , s$$

and where their variance ratio is

$$\lambda = \frac { \sigma _ { u } ^ { 2 } } { \sigma _ { \varepsilon } ^ { 2 } }$$

where λ is the value of the smoothness parameter used in (1). It is difficult to say whether the orthogonality restriction implied by (4) is "reasonable," but clearly permitting an arbitrary correlation structure would lead to lack of identification.

In practice, one directly observes yt rather than its components, so it is interesting to view the optimality result (3) in terms of the process generating the original series. It is generally agreed that a great many economic time series are integrated of order d, I(d) - that is, require differencing some positive number d of times to induce stationarity. There is some controversy as to whether d = 1 or 2 is typically the more appropriate, witness for example the contrasting views of Granger (1997) and Harvey (1997), but there is scant support for higher values. It is standard practice, following Box and Jenkins (1970), to fit to data autoregressive integrated moving average, ARIMA(p, d, q) models and we shall restrict attention to such generating models with d = 1 or 2 for yt.


<!-- p:7 -->


It should be noted that all such models fit into the framework (3), with A(L) involving a unit moving average root in the case d = 1, so that then the growth component ya is also I(1). Since yt is the sum of the individual components, it follows from (3) that

$$( 1 - L ) ^ { 2 } y _ { t } \ & = \ A ( L ) \varepsilon _ { t } + ( 1 - L ) ^ { 2 } A ( L ) u _ { t } = A ( L ) \left [ \varepsilon _ { t } + ( 1 - L ) ^ { 2 } u _ { t } \right ] \ ( 6 ) \\ & = \ A ( L ) ( 1 - \gamma _ { 1 } L - \gamma _ { 2 } L ^ { 2 } ) \eta _ { t }$$

where ηt is white noise, whose variance along with the parameters γi depends through (5) on the smoothness parameter λ. For example, solving the usual autocovariance equalities yields for λ = 1600

$$\gamma _ { 1 } = 1 . 7 7 , \, \gamma _ { 2 } = - 0 . 8 0 , \, \sigma _ { \eta } ^ { 2 } = 1 . 2 5 \sigma _ { u } ^ { 2 } .$$

Consider first the case where yt is I(2), with stationary autoregressive operator φ(L) and invertible moving average operator θ(L) in its generating model. Then in (6) set

$$A ( L ) = \frac { \theta ( L ) } { \phi ( L ) ( 1 - \gamma _ { 1 } L - \gamma _ { 2 } L ^ { 2 } ) }$$

$$\phi ( L ) ( 1 - L ) ^ { 2 } y _ { t } = \theta ( L ) \eta _ { t } .$$

so that

Since there is no restriction, other than stationarity and invertibility, on the parameterisations φ(L) and θ(L), the implication is that, whatever the choice of λ, an optimal HP decomposition of the form (3) exists. Given σ2, σ2 is determined through (7), or the corresponding expression for some other λ, and σ2 through (5). The parameters γi of (8) are also functions of λ. It follows from (9), (8), and (3) that, in general, if the data generating pr  (   +   s    (     s  s at for yc is stationary ARM A(p + 2, q).

Now let yt be I(1), with stationary autoregressive operator φ(L) and ss ( s  (e vd ae  ot

$$A ( L ) = \frac { \theta ( L ) ( 1 - L ) } { \phi ( L ) ( 1 - \gamma _ { 1 } L - \gamma _ { 2 } L ^ { 2 } ) }$$

which is permissible as (3) does not preclude a unit moving average root in A(L). Then

$$\phi ( L ) ( 1 - L ) y _ { t } = \theta ( L ) \eta _ { t }$$


<!-- p:8 -->


and it immediately follows that if the process represented by (11) is ARIMA (p, 1, q), that for yt is ARIM A(p + 2, 1, q) and that for yt is stationary ARM A(p + 2, q + 1) with a unit moving average root. Of course, in such conclusions for either I(2) or I(1) processes the possibility exists of pathological cases where cancelling factors in the autoregressive and moving average operators generate lower dimensional generating models for the components series.

We have seen, unsurprisingly since no dimensionality reductions are required, that, although it was not explicitly developed to do so, the HP filter provides optimal estimators of components that could be viewed as "growth" and "cyclical" for any I(1) or I(2) generating model, whatever value is chosen for the parameter λ in (1). In that sense these could perhaps be viewed as the "true" components implied by the adoption of HP. After all, the filter estimates such components as accurately as possible in expected squared error sense, and components generated any other way would either be incompatible with the generating process for yt or more efficiently estimated through some other filter. Nevertheless, as emphasised for example by Ehglen (1998), the stochastic process followed by the component estimate Îf differs from that followed by the true process yf as a well known consequence of optimal filtering. To illustrate this point, since many economic time series appear to be generated by processes which at least closely resemble random walks, we explore the behaviour of the HP estimated cyclical component Îc when actual yt is generated by the process (11) with φ(L) = θ(L) = 1. Of course, as we have seen, and as follows from (10), the "true" HP cyclical component is then generated by

$$( 1 - \gamma _ { 1 } L - \gamma _ { 2 } L ^ { 2 } ) y _ { t } ^ { c } = ( 1 - L ) u _ { t } \,$$

where, for λ = 1600, the parameters γi are given by (7). However, it follows from (2) that

$$\hat { y } _ { t } ^ { c } = h ( L ) \eta _ { t } \quad ; \quad h ( L ) = \frac { ( 1 - L ) ( 1 - L ^ { - 1 } ) ^ { 2 } } { \lambda ^ { - 1 } + ( 1 - L ) ^ { 2 } ( 1 - L ^ { - 1 } ) ^ { 2 } } .$$

Hence, the autocovariance-generating function of Îf is

where

$$c \ a u t o c o v a n i m a c { - g } { \text {circuit} } { 5 } { \text {circuit} } { 5 } { \text {circuit} } { 1 } { \text {circuit} } { 1 } { \text {circuit} } { 1 } { \text {circuit} } { 2 } \\ g _ { \hat { c } } ( z ) = \sigma _ { \eta } ^ { 2 } \frac { ( 1 - z ) ^ { 3 } ( 1 - z ^ { - 1 } ) ^ { 3 } } { k ^ { 2 } [ D ( z ) ] ^ { 2 } \left [ D ( z ^ { - 1 } ) \right ] ^ { 2 } } \\ \\ \lambda ^ { - 1 } + ( 1 - z ) ^ { 2 } ( 1 - z ^ { - 1 } ) ^ { 2 } = k D ( z ) D ( z ^ { - 1 } ) \\ \text {is a polynomial of degree } 2 \text {, } \text {with } D ( 0 ) = 1 \text {. } \text {It for } \\$$

$$( 1 3 )$$

and D(z) is a polynomial of degree two in z with D(0) = 1. It follows that the generating model for Îc can be written

$$v _ { t } \ \ ; \ \ \sigma _ { v } ^ { 2 } = k ^ { - 2 } \sigma _ { \eta } ^ { 2 } \ \ ; \ \ D ( L ) = 1 - \gamma _ { 1 } L - \gamma _ { 2 } L ^ { 2 }$$


<!-- p:9 -->


where vt is white noise. It is permissible to use the same notation γi as before since it is straightforward to see from (13) that the algebra that leads to the derivation of those parameters is precisely the same as that which flows from (6). For example, for λ = 1600, the γi values are precisely those given in (7) with k = 1.25. This ARMA(4, 3) data generating process, with three unit moving average roots, is, as expected, quite different from the process (12) that generates the "true" yc. The autoregressive operator D2(L) in (14) has t  t s    st    s  il exhibit an element of damped cyclical behaviour. This phenomenon, which of course is absent in the original random walk series, is in effect spuriously induced by the HP filter.

This result appears rather complex and does not give an easily interpreted impression of how the behaviour of the estimated cyclical component will appear when the HP filter is applied to a random walk series of practically interesting length. To obtain a different perspective, we generated series of T = 100 observations from the random walk process (11) with φ(L) = θ(L) = 1 and ηt normally distributed white noise with zero mean and variance one. The HP filter was applied to each generated series, yielding actual components estimates. To explore the apparent behaviour of the cyclical component, we attempted ARM A(p, q) modelling. All combinations satisfying p + q 7 were considered, parameter estimation was through maximisation of the exact Gaussian likelihood, and the order (p, q) was selected through both the SBC and AIC criteria. Table 1 summarises the percentage times models of each entertained order were selected by these criteria. The selected models are generally more lightly parameterised than the ARM A(4, 3) model predicted by the theory. Moreover, this feature is unconnected with the end-effect phenomenon to be discussed in the following two sections (applying the filter to much longer series, and discarding at least 1,000 observations from each end of the series to leave 100 cyclical component estimates unaffected by this phenomenon produced results that did not differ substantially from these of Table 1). From Table 1(a) we see that for the majority of series Îf is identified by SBC as first order autoregressive. The average value of the autoregressive parameter estimates for these series was 0.67. When an autoregressive component of order at least two was identified, that component almost invariably (on 98% of such occasions) contained complex roots. Also in line with (14), on the great majority of times a model with q ≥ 1 was identified (88% of such occasions), the fitted model contained at least one unit moving average root. These last two conditional frequencies were repeated for models selected by AIC, though as is standard these models were in the aggregate somewhat more heavily parameterised than the SBC-selected models, the most frequently chosen specification being ARM A(2, 1). One way to summarise these conclusions is that, while the phenomena of complex autoregressive roots and unit moving average roots predicted by the theory could often be detected in practice for series of 100 observations, this is most likely when a model selection criterion, AIC, known to overfit asymptotically, is employed. Under a parsimonious model selection strategy, which is likely to mimic SBC, the filtered series Îf will often appear to be first order autoregressive with parameter value close to 0.7. This phenomenon of relatively sparse models appearing to provide adequate representations of series of cyclical component estimates stems from the relatively small number of series observations in relation to the number of parameters in the "true model." This is demonstrated in Table 2 which reports results of the same type of simulation experiments, but with 200 replications of series of 500 observations. Even with such a large sample size, the correct ARM A(4, 3) order is selected only on a small minority of occasions, though at least this is the most frequently selected -o i ( t      l   om rect, that structure will generally not be manifest for series of practically occurringlength.


<!-- p:10 -->


The impact of the features in the estimated cyclical component induced by HP filtering on inference about business cycle "stylized facts" has been discussed by, among others, Harvey and Jaeger (1993) and Cogley and Nason (1995). The former note a problem with a methodology, as employed for example by Canova (1998), that attempts to base business cycle inference on sample cross-correlations at various leads and lags between cyclical component estimates of pairs of series. This approach can generate a "spurious regression" phenomenon in the sense of Granger and Newbold (1974) - that is, the appearance of a strong relation where none exists. Moreover, as a few simulation experiments would demonstrate, a related phenomenon, highlighted by Box and Newbold (1971), is also likely to occur. The sample cross-correlations tend to exhibit a smooth pattern completely unrelated to any real relationship between the variables, and which indeed will materialise when independent I(1) variables are separately subjected to the HP filter to produce estimated cyclical components.

In the following two sections, our concern is with the most recent HP cyclical component estimates in a series of finite length. Suppose that a time series is generated by the process (3), so that implicitly yf is the cyclical component estimated by the filter. That estimate will be optimal at the centre of a "long" series. However, towards the series endpoints components estimates will in general be inefficient, a conclusion that mirrors that of Wallis (1982) in a study of the linear filter version of the Census X – 11 seasonal adjustment procedure. That conclusion is easily seen in the present context. The filter (2) is symmetric two-sided, but of course such a filter is not directly applicable towards the end-points, and does not of necessity correspond to the solution of (1). However, as follows directly from results of Burman (1980), optimal components estimates follow from augmenting a given series yt with optimal forecasts (and optimal backcasts if interest is also in the earliest values), and applying the filter to the augmented series.


<!-- p:11 -->


For example, if the generating process is given by (3), such an approach will yield optimal components estimates for the entire period covered by an observed data set. This approach differs from the usual HP filter, for which for example Î€, following from the solution of (1), will be the same linear function of yT-j (j ≥ 0) whatever the true data generating process, whereas optimal forecasts depend on those observations according to that process. We go on to examine the extent of this HP suboptimality from two perspectives. First, in Section 3, we view the filter as an attempt to estimate the quantity yc of (3), and assess the efficiency of the HP estimates of the most recent time periods. Then in Section 4 we abandon the explicit view of a "true" component and ask to what extent the current cyclical component would require revision in a few years time if the filter were reapplied as new data became available - that is, we compare Îf based on yT−j (j ≥ 0) with an estimate based on yT+H−j (j ≥ 0) for moderately large H. It is well known that estimates based on forecast-augmented series, as described above, will generate minimum expected squared revisions, and these are compared with revisions that would follow from the standard HP application. The issue is practically relevant, as very often it is the most recent cyclical components that are of greatest interest, since concern might focus on whether, and by how much, an economic variable is currently "above trend."

###### 3 Estimation of recent cyclical components

Let the time series yt be generated through (3), so that at the "centre" of a long series the HP filter optimally estimates the cyclical component yf. We shall explore in detail the case where A(L) is a first order autoregressive operator (1−aL)−1, |a| &lt; 1, or a first order moving average operator (1−bL), |b| &lt; 1. As follows from (6) the generating processes for yt in these cases are respectively

$$( 1 - a L ) ( 1 - L ) ^ { 2 } y _ { t } = ( 1 - \gamma _ { 1 } L - \gamma _ { 2 } L ^ { 2 } ) \eta _ { t }$$

and

$$( 1 - L ) ^ { 2 } y _ { t } = ( 1 - b L ) ( 1 - \gamma _ { 1 } L - \gamma _ { 2 } L ^ { 2 } ) \eta _ { t }$$

where the γi depend on λ of (5). Specifically, for λ = 1600 they are given by (7), which also fixes σ2 in terms of σ2, as (5) fixes σ2. In the simulations that follow, we set λ = 1600, and, without loss of generality, σ2 = 1. Also, in these simulations, the white noise processes εt and ut were taken to be independent Gaussian. The value λ = 1600 was fixed in the filter that solves (1). The usual HP components estimate Îc then follows directly from yt (t = 1, 2, ..., T).

Each generated series was augmented by H minimum mean squared error-optimal forecasts, giving series  ̄t (t = 1, 2, ..., T + H) where  ̄t = yt (t = 1, 2, ..., T), and the remaining elements of  ̄t are forecasts based on yT-j


<!-- p:12 -->


(j = 0, 1, 2, ...) and (15) or (16) in the usual way. Estimation results are more or less invariant to T, provided that sample size is moderately large, and in our simulations we set its value at 80. The theoretical conclusion on forecast augmentation strictly requires forecasts infinitely far ahead. However, the weights given by the filter to distant forecasts become negligible. After some experimentation with both real and generated data, we found it sufficient to fix H = 28 (corresponding to seven years of quarterly data). We denote by ¿ the estimated cyclical components obtained by applying the HP filter to  ̄t (t = 1, 2, ., T + H).

In our experiments, cyclical components are of course known quantities, given by (3) with A(L) = (1 − aL)−1 or A(L) = (1 − bL), and in our simulations directly generated from these processes, so it is straightforward to assess the precision of their estimation. We measured this through the standard deviation of estimation error, that is (yf–j − Îf−j) for the standard HP filter and (yT−j −  ̄T−j) for the filter applied to the forecast-augmented series, estimated through 10,000 replications. These estimates are denoted s and sf respectively. The latter, of course, estimates the error standard deviation of optimal estimates of y¢ of (3). Results for the AR(1) and M A(1) representations of A(L) are given respectively in Tables 3 and 4 for estimation of the cyclical components yf−j (j = 0, 1, 2, 10). The estimates based on forecast-augmentation are squared error-optimal, and the results of these tables demonstrate the general suboptimality of the HP filter as an estimator of recent cyclical components when that filter is known to provide optimal estimates of such components at a series "centre." The degree of that suboptimality strongly depends on the values of the model parameters, being most pronounced in Table 3 for low negative a and in Table 4 for high positive b, both of which correspond to substantial negative first autocorrelation teet t d   s e .(   t , o e efficiency of the standard HP estimators gradually increases with increasing distance from the series endpoints. By the stage that the observation of interest is ten values from the series end, standard HP is virtually fully efficient in all cases. The actual values of s are quite interesting, keeping in mind that σu = 1 is the standard deviation of the white noise generating the quantity of interest yf. For the most recent observations, these estimation error standard deviations are far from negligible, and for some parameter values, notably large positive a in the case of Table 3, disturbingly large. The implication must be that, even if the components decomposition (3), implied by HP filter optimality, is viewed as "reasonable," estimation of such a decomposition can be quite imprecise.

Taken together, the results of Tables 3 and 4 demonstrate that, while suboptimality of the HP estimators at or near the endpoints of a series is a priori obvious, even in cases where HP is theoretically optimal at the series centre, the extent of that suboptimality can be serious. It must be con   s s s   is n s man estimators of the cyclical component at all time periods, though it is clear from the tables that in some cases it comes close to doing so.


<!-- p:13 -->


To our choice of data generating processes for Tables 3 and 4, it might be objected that the corresponding processes (15) and (16) for yt are I(2), ws a s m s   an a s ans series. However, in a further simulation not reported in detail here, we generated 10,000 replications of series of 100 observations from each of the models of these tables, and applied the usual Dickey-Fuller test to the first differences of these series. Thus, we tested the null hypothesis that the original undifferenced series is I(2) against the alternative that is I(1), choosing by general-to-specific testing the number of lagged changes incorporated in the Dickey-Fuller regressions. In virtually all cases the (true) null hypothesis was rejected at the 5%-level on an overwhelming majority of occasions, the one e g x  e t st  =   e  ate was still 34%. This finding is a consequence of the fact that the generating processes (15) and (16) with γi given by (7) have a moving average root that is close to one - a situation that is well known to generate spurious rejections of the null hypothesis by Dickey-Fuller tests (see, for example, Schwert 1989 and Agiakloglou and Newbold 1992, 1996). The conclusion then is that, even if series were truly generated by such processes, it would be extremely difficult to distinguish such models from I(1) processes for practically commonly occurring sample sizes.

###### 4 Revision of most recent cyclical components

In Section 2, we noted that, although it was not specifically developed with that purpose in mind, for any I(1) or I(2) process yt, the HP estimated cyclical component could be viewed as an optimal estimator, in squarederror-loss sense, of a "true" cyclical component defined in a specific way. In Section 3 we saw that then HP estimators of the most recent values could be far from optimal. In this section we shall examine what is essentially the same issue from a somewhat different perspective, superficially abandoning the notion of a "true" component.

Consider again a time series yt (t = 1, 2, ..., T) and let êc (t = 1, 2, ..., T) be the HP cyclical component, following in the usual way through (1): spuot one    t o st o pe o eos th o e d  e  s e d d t  et (t = 1, 2, ..., T + H). The analyst could then pass this entire extended series though the HP filter, obtaining a new estimate ê%* of the cyclical component at time T, revising the original estimate by an amount (ê°C — êf). Of course, some revision of this sort would be inevitable, but it seems reasonable to take the view that one would like it to be as small as possible - that is, the standard deviation s of the revision should ideally be no larger than is necessary. The issue of revision size can be directly explored in terms of the generating process for a given series yt, without recourse to explicit specification of components generating models. We do so here for two types of I(1) processes - the ARI M A(1, 1, 0) model


<!-- p:14 -->


$$( 1 - \phi L ) ( 1 - L ) y _ { t } = \varepsilon _ { t } \quad ; \quad | \phi | < 1$$

and the ARIMA(0,1, 1) model

$$( 1 - L ) y _ { t } = ( 1 - \theta L ) \varepsilon _ { t } \quad ; \quad | \theta | < 1 .$$

We generated series of T observations from these processes with εt indepenGeneration was continued for H subsequent observations and the filter was applied also to the extended series so that revisions could be calculated: their standard deviations were estimated through 10,000 replications. The result is virtually invariant to T, provided that number is moderately large: here we took T = 80. The quantity H is chosen sufficiently large for the revision process to "settle down." As in the previous section, we found H = 28 to be sufficient.

In fact, the HP filter is easily modified to yield smaller revisions. Define the forecast-augmented series  ̄t (t = 1, 2, ..., T + H) precisely as in the previous section and apply the full HP filter to the complete series 黛t, taking the estimated cyclical component at time T,  ̄p, as an alternative estimator of the time T cyclical component. It should be emphasised that ĩp depends only on data available at time T - that is, on yT−j (j ≥ 0). For the two models of our study, forecasts can be obtained directly from (17) and (18). It is quite clear that such an approach minimises revision standard deviation. The quantity to be estimated is simply ÎT, which is precisely the same linear function of yt (t = 1, 2, ..., T + H) as is  ̄f of the forecast augmented series B   e   e  s an ( +    =  n squared error, so must be ĩf for the corresponding linear function of yt (t = 1, 2, .., T + H). We estimated in our simulations sf, the standard deviation of revisions (ûf* —  ̄f) of the estimated time T cyclical components when this forecast-augmented approach is used in conjunction with the HP filter, calculating the ratios sf/s. Simulation results for the generating processes (17) and (18) are given respectively in Tables 5 and 6 for a range of parameter values.

It can be seen from Tables 5 and 6 that, compared with the standard deviation σε = 1 of the white noise generating yt, the revision standard deviations s for the usual HP cyclical component can be very large, particularly when first differences of the series are positively autocorrelated. This phenomenon can be somewhat mitigated if the filter is applied to the forecast-augmented series, which will lead to reductions of generally at least


<!-- p:15 -->


20%, and in some cases much more, in these revision standard deviations. It should be emphasised that, although this phenomenon is very closely related to that of the previous section, these results do not presume the estimation by the filter of particular "true" components.

####### 5 Conclusions

The Hodrick-Prescott filter is often applied to individual economic time series as an initial step in real business cycle analyses. The filter generates cyclical components, which are then subjected to further analysis. Although the view is implicitly taken that actual time series are made up of the sum of growth and cyclical components, little attention is paid to either the rrt trae tr  ort n u o  s HP filter was not developed to optimally estimate specific unobserved components, but rather is presented as an intuitively plausible transformation. Whether or why this should be so is not our concern.

In Section 2 we note that, whatever the intention, the HP filter does optimally estimate a particular components decomposition, and one might take the view that, inadvertently or otherwise, precisely that is the decomposition that is being estimated when the filter is applied. As we have noted, a number of previous authors have analysed HP from this viewpoint. However, the optimality conclusion strictly applies to infinitely long time series, or from a practical viewpoint to the midpoints of series of typical length. It does not apply at or close to series endpoints. Since the most recent cyclical components might be viewed by practitioners as of most interest, it seems reasonable to analyse the performance of the HP filter here.

At the endpoints the filter is demonstrably suboptimal, and it is easy to construct a modification whose performance is superior from two different, but closely related, perspectives. We examined those in turn in Sections 3 and 4. In Section 3, the "true" cyclical component was taken to be that implied by the optimality results of Section 2, and the estimation of the most recent values of this component was analysed. It might be objected that HP was not explicitly developed as a components estimator, and moreover that the optimal decompositions of Section 2 are not unique, since they impose orthogonality of the trend and cycle, though there is no particular reason to view such a restriction as plausible. In Section 4, we view the filter's output at the series endpoints in terms of revisions - that is, changes to initial components estimates that would inevitably occur as new data became available. It seems reasonable to argue that, on average, the magnitude of such revisions should be as small as possible.

The results of Sections 3 and 4 demonstrate, for specific special model cases, the non-trivial suboptimality of the usual HP filter from both perspectives at series endpoints. Moreover, it is seen that, from each perspective, a simple easily applied remedy generating significant improvements is readily available.


<!-- p:16 -->


####### References

- [1] Akaike, H., 1980, Seasonal adjustment by a Bayesian modeling, Journal of Time Series Analysis 1, 1-13.
- [2] Agiakloglou, C. and P. Newbold, 1992, Empirical evidence on DickeyFuller-type tests, Journal of Time Series Analysis 13, 471-483.
- [3] Agiakloglou, C. and P. Newbold, 1996, The balance between size and power in Dickey-Fuller tests with data-dependent rules for the choice of truncation lag, Economics Letters 52, 229-234.
- [4] Bell, W., 1984, Signal extraction for nonstationary time series, Annals of Statistics 12, 646-664.
- [5] Box, G.E.P. and G.M. Jenkins, 1970, Time series analysis, forecasting, and control (Holden-Day, San Francisco).
- [6] Box, G.E.P. and P. Newbold, 1971, Some comments on a paper of Coen, Gomme and Kendall, Journal of Royal Statistical Society A 134, 229-240.
- [7] Burman, J.P., 1980, Seasonal adjustment by signal extraction, Journal of Royal Statistical Society A 143, 321-337.
- [8] Canova, F. 1998, Detrending and business cycle facts, Journal of Monetary Economics 41, 475-512.
- [9] Cogley, T. and J.M. Nason, 1995, Effects of the Hodrick-Prescott filter on trend and difference stationary time series: Implications for business cycle research, Journal of Economic Dynamics and Control 19, 253-278.
- [10] Ehglen, J., 1998, Distortionary effects of the optimal Hodrick-Prescott filter, Economics Letters 61, 345-349.
- [11] Granger, C.W.J., 1997, On modelling the long run in applied economics, Economic Journal 107, 169-177.
- [12] Granger, C.W.J. and P. Newbold, 1974, Spurious regressions in econometrics, Journal of Econometrics 2, 111-120.


<!-- p:17 -->


- [13] Harvey, A.C., 1997, Trends, cycles and autoregressions, Economic Journal 107, 192-201.
- [14] Harvey, A.C. and A. Jaeger, 1993, Detrending, stylized facts and the business cycle, Journal of Applied Econometrics 8, 231-247.
- [15] Hodrick, R.J. and E.C. Prescott, 1980, Post-war U.S. business cycles: an empirical investigation, Mimeo (Carnegie-Mellon University, Pittsburgh, PA).
- [16] Hodrick, R.J. and E.C. Prescott, 1997, Post-war U.S. business cycles: an empirical investigation, Journal of Money, Credit and Banking 29, 1-16.
- [17] King, R.G. and S.T. Rebelo, 1993, Low frequency filtering and real business cycles, Journal of Economic Dynamics and Control 17, 207232.
- [18] Schwert, G.W., 1989, Tests for unit roots: a Monte Carlo investigation, Journal of Business and Economic Statistics 7, 147-160.
- [19] Wallis, K.F., 1982, Seasonal adjustment and revision of current data: Linear filters for the X-11 method, Journal of Royal Statistical Society A 145, 74-85.
- [20] Whittle, P., 1963, Prediction and regulation (Van Nostrand, Princeton, NJ).
- [21] Wiener, N., 1949, Extrapolation, interpolation and smoothing of stationary time series (Wiley, New York).


<!-- p:18 -->


Table 1. Percentage times particular ARMA(p, q) models are selected for Ît from HP filtered random walks (T = 100; 1,000 replications)

(a)

SBC selection

AIC

(b)

selection

|   q Â p |   0 | 1    | 2    | 3   | 4   | 5   | 6   | 7   |
|---------|-----|------|------|-----|-----|-----|-----|-----|
|       0 |   0 | 56.5 | 4.3  | 0.3 | 0.1 | 0.1 | 0   | 0   |
|       1 |   0 | 1.7  | 26.1 | 5.0 | 0.6 | 0.3 | 0.1 | .   |
|       2 |   0 | 0.7  | 1.9  | 0.2 | 0.2 | 0   | .   | .   |
|       3 |   0 | 0.1  | 1.1  | 0   | 0   | .   | .   | .   |
|       4 |   0 | 0.2  | 0.5  | 0   | .   | .   | .   | .   |
|       5 |   0 | 0    | 0    | .   | .   | .   | .   | .   |
|       6 |   0 | 0    | .    | .   | .   | .   | .   | .   |
|       7 |   0 | .    | .    | .   | .   | .   | .   | .   |

|   q Â p |   0 | 1   | 2    | 3    | 4   | 5   | 6   | 7   |
|---------|-----|-----|------|------|-----|-----|-----|-----|
|       0 |   0 | 7.5 | 1.8  | 0.3  | 0.1 | 0.1 | 0   | 0.4 |
|       1 |   0 | 0.6 | 26.5 | 11.3 | 7.8 | 4.3 | 4.5 | .   |
|       2 |   0 | 0.5 | 6.3  | 3.7  | 2.8 | 1.4 | .   | .   |
|       3 |   0 | 0.5 | 5.3  | 1.6  | 2.6 | .   | .   | .   |
|       4 |   0 | 0.5 | 3.3  | 1.8  | .   | .   | .   | .   |
|       5 |   0 | 0.9 | 2.1  | .    | .   | .   | .   | .   |
|       6 |   0 | 1.5 | .    | .    | .   | .   | .   | .   |
|       7 |   0 | .   | .    | .    | .   | .   | .   | .   |


<!-- p:19 -->


Table 2. Percentage times particular ARMA(p, q) models are selected for Îf from HP filtered random walks (T = 500; 200 replications)

|   q Â p |   0 | 1   | 2    | 3   | 4   | 5   | 6   | 7   |
|---------|-----|-----|------|-----|-----|-----|-----|-----|
|       0 |   0 | 0.5 | 0    | 0   | 0   | 0   | 0   | 0   |
|       1 |   0 | 0   | 22.5 | 11  | 8.5 | 3.5 | 2   | .   |
|       2 |   0 | 0   | 13   | 21  | 4   | 0   | .   | .   |
|       3 |   0 | 0   | 7    | 0   | 1.5 | .   | .   | .   |
|       4 |   0 | 0   | 5.5  | 0   | .   | .   | .   | .   |
|       5 |   0 | 0   | 0    | .   | .   | .   | .   | .   |
|       6 |   0 | 0   | .    | .   | .   | .   | .   | .   |
|       7 |   0 | .   | .    | .   | .   | .   | .   | .   |

(a)

SBC selection

(b)

AIC

selection

|   q Â p |   0 | 1   | 2   | 3   | 4   | 5   | 6    | 7   |
|---------|-----|-----|-----|-----|-----|-----|------|-----|
|       0 |   0 | 0   | 0   | 0   | 0   | 0   | 0    | 0   |
|       1 |   0 | 0   | 5   | 7   | 6.5 | 4.5 | 13.5 | .   |
|       2 |   0 | 0   | 6   | 10  | 4   | 7   | .    | .   |
|       3 |   0 | 0   | 5.5 | 1.5 | 19  | .   | .    | .   |
|       4 |   0 | 0   | 6.5 | 1   | .   | .   | .    | .   |
|       5 |   0 | 0.5 | 2.5 | .   | .   | .   | .    | .   |
|       6 |   0 | 0   | .   | .   | .   | .   | .    | .   |
|       7 |   0 | .   | .   | .   | .   | .   | .    | .   |


<!-- p:20 -->


Table 3. Standard deviations of estimators of recent cyclical components in generating processes (3) for which HP is theoretically optimal:

|   A ( L ) =(1 ¡ aL ) ¡ 1 - Observation - a |   A ( L ) =(1 ¡ aL ) ¡ 1 - T - s |   A ( L ) =(1 ¡ aL ) ¡ 1 - T - s f =s |   A ( L ) =(1 ¡ aL ) ¡ 1 - T ¡ 1 - s |   A ( L ) =(1 ¡ aL ) ¡ 1 - T ¡ 1 - s f =s |   A ( L ) =(1 ¡ aL ) ¡ 1 - T ¡ 2 - s |   A ( L ) =(1 ¡ aL ) ¡ 1 - T ¡ 2 - s f =s |   A ( L ) =(1 ¡ aL ) ¡ 1 - T ¡ 10 - s |   A ( L ) =(1 ¡ aL ) ¡ 1 - T ¡ 10 - s f =s |
|--------------------------------------------|----------------------------------|---------------------------------------|--------------------------------------|-------------------------------------------|--------------------------------------|-------------------------------------------|---------------------------------------|--------------------------------------------|
|                                       -0.9 |                             0.34 |                                  0.73 |                                 0.30 |                                      0.74 |                                 0.27 |                                      0.75 |                                  0.13 |                                       0.98 |
|                                       -0.8 |                             0.30 |                                  0.87 |                                 0.27 |                                      0.87 |                                 0.24 |                                      0.87 |                                  0.14 |                                       0.99 |
|                                       -0.7 |                             0.30 |                                  0.92 |                                 0.27 |                                      0.93 |                                 0.24 |                                      0.93 |                                  0.15 |                                       0.99 |
|                                       -0.6 |                             0.30 |                                  0.96 |                                 0.27 |                                      0.96 |                                 0.25 |                                      0.96 |                                  0.15 |                                       1.00 |
|                                       -0.5 |                             0.32 |                                  0.96 |                                 0.28 |                                      0.97 |                                 0.25 |                                      0.97 |                                  0.16 |                                       1.00 |
|                                       -0.4 |                             0.33 |                                  0.99 |                                 0.30 |                                      0.98 |                                 0.27 |                                      0.98 |                                  0.18 |                                       1.00 |
|                                       -0.3 |                             0.36 |                                  0.98 |                                 0.32 |                                      0.99 |                                 0.28 |                                      0.99 |                                  0.19 |                                       1.00 |
|                                       -0.2 |                             0.38 |                                  1.00 |                                 0.34 |                                      1.00 |                                 0.31 |                                      1.00 |                                  0.20 |                                       1.00 |
|                                       -0.1 |                             0.41 |                                  1.00 |                                 0.37 |                                      1.00 |                                 0.33 |                                      1.00 |                                  0.22 |                                       1.00 |
|                                          0 |                             0.45 |                                  1.00 |                                 0.40 |                                      1.00 |                                 0.36 |                                      1.00 |                                  0.24 |                                       1.00 |
|                                        0.1 |                             0.49 |                                  1.00 |                                 0.44 |                                      1.00 |                                 0.40 |                                      1.00 |                                  0.27 |                                       1.00 |
|                                        0.2 |                             0.55 |                                  0.99 |                                 0.49 |                                      1.00 |                                 0.44 |                                      1.00 |                                  0.30 |                                       1.00 |
|                                        0.3 |                             0.61 |                                  1.00 |                                 0.56 |                                      0.99 |                                 0.50 |                                      0.99 |                                  0.34 |                                       1.00 |
|                                        0.4 |                             0.71 |                                  0.98 |                                 0.63 |                                      0.98 |                                 0.57 |                                      0.98 |                                  0.40 |                                       1.00 |
|                                        0.5 |                             0.84 |                                  0.97 |                                 0.74 |                                      0.98 |                                 0.67 |                                      0.98 |                                  0.48 |                                       1.00 |
|                                        0.6 |                             1.00 |                                  0.97 |                                 0.91 |                                      0.96 |                                 0.82 |                                      0.96 |                                  0.59 |                                       1.00 |
|                                        0.7 |                             1.28 |                                  0.92 |                                 1.14 |                                      0.93 |                                 1.04 |                                      0.94 |                                  0.76 |                                       1.00 |
|                                        0.8 |                             1.73 |                                  0.89 |                                 1.57 |                                      0.89 |                                 1.43 |                                      0.91 |                                  1.09 |                                       1.00 |
|                                        0.9 |                             2.81 |                                  0.81 |                                 2.50 |                                      0.85 |                                 2.28 |                                      0.89 |                                  1.86 |                                       1.00 |


<!-- p:21 -->


Table 4. Standard deviations of estimators of recent cyclical components in generating processes (3) for which HP is theoretically optimal:

|   A ( L )= (1 ¡ bL ) - Observation - b |   A ( L )= (1 ¡ bL ) - T - s |   A ( L )= (1 ¡ bL ) - T - s f =s |   A ( L )= (1 ¡ bL ) - T ¡ 1 - s |   A ( L )= (1 ¡ bL ) - T ¡ 1 - s f =s |   A ( L )= (1 ¡ bL ) - T ¡ 2 - s |   A ( L )= (1 ¡ bL ) - T ¡ 2 - s f =s |   A ( L )= (1 ¡ bL ) - T ¡ 10 - s |   A ( L )= (1 ¡ bL ) - T ¡ 10 - s f =s |
|----------------------------------------|------------------------------|-----------------------------------|----------------------------------|---------------------------------------|----------------------------------|---------------------------------------|-----------------------------------|----------------------------------------|
|                                   -0.9 |                         0.83 |                              0.97 |                             0.74 |                                  0.98 |                             0.67 |                                  0.98 |                              0.46 |                                   1.00 |
|                                   -0.8 |                         0.79 |                              0.98 |                             0.71 |                                  0.98 |                             0.64 |                                  0.98 |                              0.44 |                                   1.00 |
|                                   -0.7 |                         0.74 |                              0.99 |                             0.67 |                                  0.98 |                             0.60 |                                  0.98 |                              0.41 |                                   1.00 |
|                                   -0.6 |                         0.69 |                              1.00 |                             0.62 |                                  0.99 |                             0.56 |                                  0.99 |                              0.38 |                                   1.00 |
|                                   -0.5 |                         0.65 |                              0.98 |                             0.58 |                                  0.99 |                             0.52 |                                  0.99 |                              0.36 |                                   1.00 |
|                                   -0.4 |                         0.61 |                              1.00 |                             0.55 |                                  0.99 |                             0.50 |                                  0.99 |                              0.34 |                                   1.00 |
|                                   -0.3 |                         0.57 |                              0.99 |                             0.51 |                                  1.00 |                             0.46 |                                  0.99 |                              0.32 |                                   1.00 |
|                                   -0.2 |                         0.53 |                              1.00 |                             0.47 |                                  1.00 |                             0.43 |                                  1.00 |                              0.29 |                                   1.00 |
|                                   -0.1 |                         0.49 |                              0.99 |                             0.43 |                                  1.00 |                             0.39 |                                  1.00 |                              0.27 |                                   1.00 |
|                                      0 |                         0.45 |                              1.00 |                             0.40 |                                  1.00 |                             0.36 |                                  1.00 |                              0.24 |                                   1.00 |
|                                    0.1 |                         0.41 |                              1.00 |                             0.37 |                                  1.00 |                             0.33 |                                  1.00 |                              0.22 |                                   1.00 |
|                                    0.2 |                         0.38 |                              0.98 |                             0.33 |                                  0.99 |                             0.30 |                                  1.00 |                              0.20 |                                   1.00 |
|                                    0.3 |                         0.33 |                              1.00 |                             0.30 |                                  0.98 |                             0.27 |                                  0.98 |                              0.17 |                                   1.00 |
|                                    0.4 |                         0.30 |                              0.95 |                             0.27 |                                  0.97 |                             0.24 |                                  0.97 |                              0.15 |                                   1.00 |
|                                    0.5 |                         0.27 |                              0.92 |                             0.24 |                                  0.93 |                             0.22 |                                  0.93 |                              0.13 |                                   0.99 |
|                                    0.6 |                         0.24 |                              0.88 |                             0.22 |                                  0.88 |                             0.19 |                                  0.88 |                              0.10 |                                   0.99 |
|                                    0.7 |                         0.22 |                              0.77 |                             0.20 |                                  0.78 |                             0.17 |                                  0.79 |                              0.08 |                                   0.98 |
|                                    0.8 |                         0.21 |                              0.66 |                             0.19 |                                  0.66 |                             0.16 |                                  0.68 |                              0.06 |                                   0.97 |
|                                    0.9 |                         0.21 |                              0.46 |                             0.18 |                                  0.50 |                             0.16 |                                  0.52 |                              0.05 |                                   0.91 |


<!-- p:22 -->


Table 5. Standard deviations of revisions of most recent HP cyclical components when (1 − φL)(1 − L)yt = εt

|    Á |    s |   s f =s |
|------|------|----------|
| -0.9 | 0.65 |     0.79 |
| -0.8 | 0.68 |     0.79 |
| -0.7 | 0.72 |     0.79 |
| -0.6 | 0.76 |     0.78 |
| -0.5 | 0.80 |     0.79 |
| -0.4 | 0.87 |     0.78 |
| -0.3 | 0.94 |     0.78 |
| -0.2 | 1.00 |     0.77 |
| -0.1 | 1.09 |     0.76 |
|    0 | 1.21 |     0.75 |
|  0.1 | 1.32 |     0.75 |
|  0.2 | 1.48 |     0.73 |
|  0.3 | 1.70 |     0.72 |
|  0.4 | 1.94 |     0.70 |
|  0.5 | 2.28 |     0.68 |
|  0.6 | 2.78 |     0.66 |
|  0.7 | 3.52 |     0.62 |
|  0.8 | 4.67 |     0.56 |
|  0.9 | 6.64 |     0.49 |


<!-- p:23 -->


Table 6. Standard deviations of revisions of most recent HP cyclical components when (1 − L)yt = (1 − θL)εt

|    μ |    s |   s f =s |
|------|------|----------|
| -0.9 | 2.27 |     0.72 |
| -0.8 | 2.14 |     0.72 |
| -0.7 | 2.01 |     0.71 |
| -0.6 | 1.92 |     0.72 |
| -0.5 | 1.79 |     0.73 |
| -0.4 | 1.69 |     0.72 |
| -0.3 | 1.56 |     0.73 |
| -0.2 | 1.43 |     0.74 |
| -0.1 | 1.32 |     0.74 |
|    0 | 1.21 |     0.75 |
|  0.1 | 1.08 |     0.76 |
|  0.2 | 0.98 |     0.78 |
|  0.3 | 0.86 |     0.79 |
|  0.4 | 0.74 |     0.81 |
|  0.5 | 0.64 |     0.82 |
|  0.6 | 0.54 |     0.84 |
|  0.7 | 0.44 |     0.84 |
|  0.8 | 0.36 |     0.81 |
|  0.9 | 0.30 |     0.72 |

<!-- END SOURCE 33/40: Mise_2005_hp-filter-time-series-endpoints.md -->

---

<!-- BEGIN SOURCE 34/40: Phillips_2021_boosting-hp-filter.md -->

# Source: `Phillips_2021_boosting-hp-filter.md`

---
id: "Phillips_2021_boosting-hp-filter"
source_pdf: "../pdf/Phillips_2021_boosting-hp-filter.pdf"
source_filename: "Phillips_2021_boosting-hp-filter.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/Phillips_2021_boosting-hp-filter.references.md"
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

<!-- END SOURCE 34/40: Phillips_2021_boosting-hp-filter.md -->

---

<!-- BEGIN SOURCE 35/40: Ravn_2002_adjusting-hp-filter-frequency.md -->

# Source: `Ravn_2002_adjusting-hp-filter-frequency.md`

---
id: "Ravn_2002_adjusting-hp-filter-frequency"
source_pdf: "../pdf/Ravn_2002_adjusting-hp-filter-frequency.pdf"
source_filename: "Ravn_2002_adjusting-hp-filter-frequency.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/Ravn_2002_adjusting-hp-filter-frequency.references.md"
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

<!-- END SOURCE 35/40: Ravn_2002_adjusting-hp-filter-frequency.md -->

---

<!-- BEGIN SOURCE 36/40: Tashman_2000_out-of-sample-forecast-accuracy.md -->

# Source: `Tashman_2000_out-of-sample-forecast-accuracy.md`

---
id: "Tashman_2000_out-of-sample-forecast-accuracy"
source_pdf: "../pdf/Tashman_2000_out-of-sample-forecast-accuracy.pdf"
source_filename: "Tashman_2000_out-of-sample-forecast-accuracy.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/Tashman_2000_out-of-sample-forecast-accuracy.references.md"
---

<!-- p:1 -->

ELSEVIER

###### Abstract

In evaluations of forecasting accuracy, including forecasting competitions, researchers have paid attention to the selection of time series and to the appropriateness of forecast-error measures. However, they have not formally analyzed choices in the implementation of out-of-sample tests, making it difficult to replicate and compare forecasting accuracy studies. In this paper, I (1) explain the structure of out-of-sample tests, (2) provide guidelines for implementing these tests, and (3) evaluate the adequacy of out-of-sample tests in forecasting software. The issues examined include series-splitting rules, fixed versus rolling origins, updating versus recalibration of model coefficients, fixed versus rolling windows, single versus multiple test periods, diversification through multiple time series, and design characteristics of forecasting competitions. For individual time series, the efficiency and reliability of out-of-sample tests can be improved by employing rolling-origin evaluations, recalibrating coefficients, and using multiple test periods. The results of forecasting competitions would be more generalizable if based upon precisely described groups of time series, in which the series are homogeneous within group and heterogeneous between groups. Few forecasting software programs adequately implement out-of-sample evaluations, especially general statistical packages and spreadsheet add-ins. 2000 International Institute of Forecasters. Published by Elsevier Science B. V . All rights reserved.

Keywords : Out-of-sample; Fit period; Test period; Fixed origin; Rolling origin; Updating; Recalibration; Rolling window; Sliding simulation; Forecasting competitions

## 1. Introduction

In this paper, I discuss the implementation of out-of-sample tests of forecasting accuracy. Section 2 summarizes the rationale for out-ofsample testing. Section 3 compares fixed-origin and rolling-origin procedures. Section 4 examines the application of out-of-sample testing

*Tel.: 1 1-802-425-3805; fax: 1 1-802-425-3806.

lentashman@compuserve.com

(L.J.

Tashman).

to an individual time series: Issues addressed are rules for splitting the series between fit and test periods, updating versus recalibrating model coefficients, single versus multiple test periods and the use of rolling windows. Section 5

method selection. Section 6 describes the extension of out-of-sample testing from an individual time series to multiple time series and forecasting competitions. Section 7 evaluates the adequacy of out-of-sample tests in forecasting software. Section 8 contains my conclusions and recommendations.

International Journal of Forecasting 16 (2000) 437-450

www.elsevier.com/locate/ijforecast

## Out-of-sample tests of forecasting accuracy: an analysis and review

### Leonard J. Tashman *

School of Business Administration , University of Vermont , Burlington , Vermont 05405, USA


<!-- p:2 -->


## 2. In-sample versus out-of-sample evaluation

Forecasters generally agree that forecasting methods should be assessed for accuracy using out-of-sample tests rather than goodness of fit to past data (in-sample tests). 'The performance of a model on data outside that used in its construction remains the touchstone for its utility in all applications; (Fildes and Makridakis, 1995, p. 293).

The argument has two related aspects. First, for a given forecasting method, in-sample errors are likely to understate forecasting errors. Method selection and estimation are designed to calibrate a forecasting procedure to the historical data. But the nuances of past history are unlikely to persist into the future, and the nuances of the future may not have revealed themselves in the past.

methods selected by best in-sample fit may not best predict post-sample data. Bartolomei and Sweet (1989) and Pant and Starbuck (1990) provide particularly convincing evidence on this point.

One way to ascertain post-sample forecasting performance is to wait and see in real time. The M2-competition (Makridakis et al., 1993) did exactly this. In one phase, forecasts (for 1-15 months ahead) made in September 1987 were evaluated at the conclusion of 1988.

Real time assessment has practical limitations for forecasting practitioners, since a long wait may be necessary before a reliable picture of a forecasting track record will materialize. As a result, tests based on holdout samples have become commonplace. The fi t period is used to identify and estimate a model (or method) while the test period is reserved to assess the model's forecasting accuracy.

Overfitting and structural changes may further aggravate the divergence between in-sample and post-sample performance. The Mcompetition (Makridakis et al., 1982) and many subsequent empirical studies show that forecasting errors generally exceed in-sample errors, even at reasonably short horizons. As well, prediction intervals built on in-sample standard errors are likely to be too narrow (Chatfield, 1993, p.131).

Moreover, common extrapolative forecasting methods, such as exponential smoothing, are based on updating procedures, in which one makes each forecast as if one were standing in the immediately prior period. For updating methods, the traditional measurement of goodness-of-fit is based on one step - ahead errors - errors made in estimating the next time period from the current time period. However, research shows (e.g., Schnaars, 1986, Exhibit 2, p.76) that errors in forecasting into the more distant future will be larger than those made in forecasting one step ahead.

The second aspect to the argument is that If the forecaster withholds all data about events occurring after the end of the fit period, the forecast-accuracy evaluation is structurally identical to the real-world-forecasting environment, in which we stand in the present and forecast the future. However, 'peeking' at the held-out data while selecting the forecasting method pollutes the evaluation environment.

## 3. Fixed-origin versus rolling-origin procedures

An out-of-sample evaluation of forecasting accuracy begins with the division of the historical data series into a fi t period and a test period . The final time in the fit period ( T ) - the point from which the forecasts are generated - is the forecasting origin . The number of time periods between the origin and the time being forecast is the lead time or the forecasting horizon . The longest lead time is the N step-ahead forecast. Equivalently, N denotes the length of the test period.


<!-- p:3 -->


### 3.1. Fixed - origin evaluations

In performing an out-of-sample test, we can use either a single forecasting origin or multiple forecasting origins. The former can be called a fixed - origin evaluation: Standing at origin ( T ), we generate forecasts for time periods T 1 1, T 1 2, . . . T 1 N . By subtracting each of these forecasts from the known data values of the test period, we determine the forecast errors. We can average the errors in various ways to obtain summary statistics.

Applied to a single time series, the fixedorigin evaluation has several shortcomings. Because it yields only one forecast (and hence, only one forecast error) for each lead time, it requires a fairly long test period to produce a forecasting track record. Second, forecasts generated from a single origin are susceptible to corruption by occurrences unique to that origin. Third, in the usual software implementation of a fixed-origin evaluation, summary error measures are computed by averaging forecasting errors across lead times. The resulting summary statis- ́ tic is a melange of near-term and far-term forecast errors.

We can partly overcome the three problems by successively updating the forecasting origin. We can also mitigate the problems by using multiple time series . Still, even within a singleseries context, the fixed-origin evaluation can play a useful role: it is the only way we can assess the post-sample accuracy of forecasts, such as judgmental forecasts, when we do not know or can not replicate the underlying forecasting methodology.

### 3.2. Rolling - origin evaluations

In a rolling - origin evaluation , we successively update the forecasting origin and produce forecasts from each new origin. One of the first explicit descriptions of the procedure was Armstrong and Grohman's (1972). Armstrong

(1985, p. 343) provides a schematic illustration of the rolling-origin procedure.

When N 5 4, for example, the fixed-origin evaluation results in four forecasts, all from origin T . The rolling-origin evaluation also generates four forecasts from this origin, but then supplies an additional three forecasts from origin T 1 1, two from origin T 1 2, and one from origin T 1 3, for a total of 10 forecasts. The total number of forecasts grows from 4 to 10. In general, the rolling-origin procedure provides N ( N 1 1)/2 forecasts, against N from the fixed-origin. With eight time periods forming the test set, for example, the rolling-origin evaluation supplies 36 forecasts, a multiple of 4.5 times N .

### 3.3. Analysis of forecasting errors by lead time

In contrast to the fixed-origin evaluation, the rolling out-of-sample evaluation produces multiple forecasts for every lead time but the longest, N . As a result, it permits us to assess the forecasting accuracy of an individual time series at each lead time. Moreover, the errors for a given lead time form a coherent empirical distribution, one we can profitably analyze for further distributional information, such as outliers. Makridakis and Winkler (1989) describe such analysis.

## 4. Issues in implementing out-of-sample evaluations

In designing an out-of-sample test for an individual time series, the most fundamental choice is how to split the series between fit and test periods. This decision determines the amount of data that will be available to identify and fit a forecasting model and the number of forecasts generated for the out-of-sample evaluation of the model's performance.


<!-- p:4 -->


### 4.1. Series splitting rules

In deciding upon the appropriate number of periods N to withhold from the time series, we can be guided by several considerations, the most important of which is the longest-term forecast required. Denote this maximal length forecast by H . Manifestly, N must be at least as large as H .

However, we may wish to increase the length of the test period to insure a certain minimum number of forecasts M at lead time H . We would then set the length of the test period to equal H 1 M 2 1 forecasts. If this minimum is M 5 3, we should design a rolling-origin evaluation with a test period of length H 1 2. For example, if the longest-term forecast required is a five-year ahead forecast ( H 5 5), we would specify a test period of seven years, thus insuring that the assessment of accuracy in forecasting five years ahead is based on a minimum of three forecasts. We would need a much larger number of forecasts than this to examine a distribution of forecast errors, rather than simply measures of average error.

Short time series impose restrictions on the length of the test period, since truncating the data could leave too few observations to fit the model. In this circumstance, we might profit from the efficiency of the rolling-origin procedure and still be able to examine one-step ahead forecast errors without greatly truncating the period of fit.

### 4.2. Updating versus recalibrating

In the rolling-origin evaluation, each update of the forecasting origin leads to a revision of the forecasting equation.The successive revisions to the forecasting equation may arise simply from the addition of a data point to the fit period, or may arise as well from recalibration (reoptimization) of the smoothing weights as the new data point comes in.

Recalibration is the preferred procedure. Updating without recalibrating imposes an arbitrary handicap on the forecasting method. Recalibration, moreover, desensitizes error measures to events unique to the original fit period. However, recalibration is more computationally intensive than simply updating, and only two of 15 forecasting software packages examined by Tashman and Hoover (2001) recalibrate as they update the forecasting origin.

When it is a (causal) regression model under evaluation, failure to recalibrate transforms a rolling-origin evaluation into a fixed-origin evaluation at one step ahead and into meaningless figures at longer horizons. Without recalibration, the addition of a new data point changes neither the inputs to nor the coefficients of the forecasting equation.

For extrapolative methods, research is lacking on the extent to which recalibration of the smoothing weights across the test period influences the reported absolute and relative accuracy of forecasting methods. Fildes, Hibon, Makridakis and Meade (1998) provide evidence that recalibrating weights in fi tting an exponential smoothing method improves the out-of-sample accuracy of the method. However, they did not recalibrate the smoothing weights within the test period of a rolling-origin evaluation.

Similarly, no one has examined the empirical significance of recalibration in the context of out-of-sample evaluations of regression models. If the model contains dynamic terms, such as a lagged dependent variable or a lagged error, each forecast will adjust as the origin is successively updated. Unless the sample size is small, these effects may be more substantial than the changes that arise from recalibrating the regression coefficients.

### 4.3. Multiple test periods

Fildes (1992, p.82) observed that replacing a fixed-origin design with a rolling-origin design removes 'the possibility that the arbitrary choice of time origin might unduly affect the [forecasting accuracy] results' Distinguishing sensitivity to outliers in the test period from sensitivity to the phase of the business cycle , however, is useful. The test period marks a single calendar interval. Especially for monthly and quarterly data, therefore, it is likely to reflect a single phase of the business cycle or single period of business activity. To attain cyclical diversity in analyzing an individual time series, we should use multiple test periods .


<!-- p:5 -->


Pack (1990) illustrated the virtues of multiple test periods using a retail sales series of 95 consecutive months. For each of three forecasting methods, he designated three distinct test periods, and performed a rolling-origin evaluation for each test period. Table 1 is a portion of his Exhibit 5 (p. 217).

The MAPEs are sensitive to the choice of test period. For lead time 4, for example, forecasting method A earned a MAPE of 3.1 percent over test period 61-71; however, the same measure applied to test period 73-83 yielded a MAPE of 5.8 percent, nearly twice as high. At lead time 1 in test period 85-95, the three methods appear about equally accurate (MAPEs of 3.1%, 3.3% and 3.4%), while, in test period 73-83, method B looks significantly worse (at both lead times) than the others.

Diversifying into multiple test periods seems prudent. Perhaps individual test-period MAPEs should be averaged. The average MAPE for Method A at four-steps head is 4.5 percent, which is the most broad-based indication of this method's expected accuracy in forecasting four months into the future.

Table 1 How the MAPE varies by lead time and test period in comparing three methods

| Lead time   | Method   |   Test periods - 61-71 |   Test periods - 73-83 |   Test periods - 85-95 |   Average |
|-------------|----------|------------------------|------------------------|------------------------|-----------|
| 1           | A        |                    3.0 |                    4.1 |                    3.1 |       3.4 |
| B           |          |                    3.2 |                    5.0 |                    3.3 |       3.8 |
| C           |          |                    2.3 |                    2.7 |                    3.4 |       2.8 |
| 4           | A        |                    3.1 |                    4.6 |                    5.8 |       4.5 |
| B           | 5.3      |                        |                    7.4 |                    6.0 |       6.2 |
| C           | 3.5      |                        |                    3.9 |                    7.0 |       4.8 |

Fildes et al. (1998) used multiple test periods, which they called multiple origins , to compare the accuracy of five designated extrapolative methods on a batch of monthly telecommunications time series. While they found that one method was uniformly most accurate (across lead time and for every test period), the relative accuracy of three of the other methods was not consistent across test periods.

Schnaars (1986) examined the cyclical sensitivity of forecast error measures by sorting all one year-ahead forecast errors by calendar year (1978-1984). He then compared forecast errors for (a) years in which cyclical turning points occurred and (b) years in which the overall direction of the economy did not change. For almost all of the methods included, he found that one-year-ahead forecasting accuracy was poorer during the years of cyclical turning points.

Using multiple test periods may be particularly beneficial when we are limited by software to fixed-origin evaluations. However, the procedure requires a long time series.

### 4.4. Rolling windows

In a rolling-origin evaluation, each update of the forecasting origin adds one new observation to the fit period. Alternatively, in some studies, researchers have maintained a fit period (or sample or window ) of constant length. They do this by pruning the oldest observation at each update, much as we would in taking a moving average. The procedure is called a fixed-size, rolling window (Swanson and White, 1997) or fixed-size rolling sample (Callen, Kwan, Yip and Yuan, 1996).


<!-- p:6 -->


Why prune the fit period at each update of the forecasting origin? One reason is to 'clean out old data' in an attempt to update model coefficients. Doing so may be unnecessary in common time-series methods, however, because the weighting systems in these methods mitigate the influence of data from the distant past.

Swanson and White (1997) discussed the usefulness of rolling windows in econometric modeling, particularly in determining how econometric models evolve over time to fixed specifications.

For out-of-sample testing, the principal purpose of a rolling window is to level the playing field in a multiperiod comparison of forecasting accuracy. We might analyze whether a particular method's performance deteriorates between an earlier and later test period. The comparison would be confounded if the second fit period were longer than the first.

for out-of-sample analysis.) Fildes (1989) also used the procedure - under the name rolling horizon - to compare the efficacy of various method-selection rules.

The sliding simulation requires a three - way division of the time series. N observations withheld from the time series serve as a test set. The remaining period of fit is subdivided between the first T observations, which represent the in - sample fit period and the remaining P observations, T 1 1 to T 1 P , which constitute the post - sample fit period .

For each method under consideration, the sliding simulation entails a pair of rolling outof-sample evaluations. In the first, we optimize the smoothing weights to the post - sample fit period , and select a best method for each lead time. The second is performed on the test set, with the traditional purpose of evaluating the accuracy of the forecasts made with this method.

Swanson and White (1997) further pruned their rolling windows to generate the same frequency of forecasts at each horizon of the test period . They wished to ensure equality between the number of one step-ahead forecasts and the number of four step-ahead forecasts. That procedure, however, results in a different calendar fit period for each forecast horizon: the fit period for a fourstep-ahead forecast will begin and end three periods earlier than the fit period underlying the one step-ahead forecasts. As a result of the calendar shift, the evidence on how forecasting accuracy of any method deteriorates as the forecasting horizon increases may be confounded.

## 5. 'Sliding simulations'

Makridakis (1990) extended the rolling-origin design to serve as a process for method selection and estimation. He called this process a sliding simulation . (He did not intend the term simulation to mean a resampling or Monte Carlo process; he used it rather as a synonym In the same spirit, Weiss and Anderson (1984, p.485) proposed that, for cumulative forecasts, a model be calibrated to minimize a cumulative post-sample error measure.

Makridakis (1990) applied variants of the sliding simulation to a subsample of 111 time series used in the M-competition (Makridakis et al., 1982). For each of three exponential smoothing methods, post-sample forecasting accuracy improved when he calibrated smoothing weights to minimize a post-sample error measure instead of calibrating weights in-sample, as is traditional.

Results reported in the M2-Competition (Makridakis et al., 1993) were not so positive for the sliding simulation process. There, the method chosen as best - from among simple, damped, and linear-trend smoothing - did not systematically outperform any individual smoothing method (Exhibit 3, p.9). In fact, two of the three smoothing methods performed more poorly when calibrated post-sample, the linear trend being the exception.

Fildes (1989) used the sliding simulation to compare individual - selection and aggregate - selection rules. When following an individualselection rule, we identify a best method for each time series in a batch. When following aggregate-selection rule, we apply to every series in the batch the method that works best in the aggregate.


<!-- p:7 -->


Fildes considered two extrapolative methods, both involving damping of trends and smoothing of outliers. He calibrated each method to a post-sample fit period and chose the better of the two methods based on post-sample fit. He concluded that the extra effort needed in individual rather than aggregate selection was not worth the small potential gain in accuracy for forecasting one month ahead, the most important horizon when forecasting for inventory control. At longer lead times, individual selection has more potential to improve accuracy.

## 6. Multiple time series: forecasting competitions

For a single time series, desirable characteristics of an out-of-sample test are adequacy , enough forecasts at each lead time, and diversi - ty , desensitizing forecast error measures to special events and specific phases of business. To achieve these goals with an individual time series, we must use rolling origins and multiple test periods.

Alternatively, we can attain adequacy and diversity by using multiple time series. To promote adequacy, we need to select component series that are homogeneous in some relevant characteristic. For diversity, we should collect time series that are heterogeneous in both nature and calendar time, thus establishing a broadbased track record for a forecasting method.

Diversity was the primary motivation in the early forecasting competitions. Newbold and Granger (1974) amassed 106 economic series, a mixture of monthly and quarterly as well as of micro-level and macro-level data. The Mcompetition (Makridakis et al., 1982) included 1001 time series, a compendium of annual, quarterly, and monthly as well as firm, industry, macroeconomic, and demographic data. ''Although the [M-competition] sample is not random, efforts were made to select series covering a wide spectrum of possibilities. This included different sources of statistical data and different starting/ending dates.'' (p.113).

In contrast, selectivity was the principal objective for Schnaars (1986). Schnaars wished to ''discover how well extrapolations are able to perform on a specific type of data series - annual unit sales by industry - rather than a wide assortment of potentially disparate series.'' (p.72). Selectivity was also an objective for the M2-competition (Makridakis et al., 1993). Of its 29 time series, 23 were monthly firm-level series, chosen to compare the accuracy of designated methods in forecasting for budgeting and capital investment.

The diversity objective for the M-competition returns with the M3-competition (Makridakis and Hibon, 2000), in which the database is enlarged from 1001 to 3003 time series. Again, the authors chose time series to represent data of different periodicities (yearly, quarterly, monthly, and other) and types (micro, industry, macro, finance, demographic, and other). The selection process was essentially downloading a convenience sample of data from the Internet.

The emphasis in a forecasting competition affects both the selection of time series and the implementation of the out-of-sample tests. With the emphasis on diversity , the authors of the M-competition and the M3-competition amassed a large collection of heterogeneous time series, but relied on fixed-origin evaluations and a single test period per series to obtain postsample error measures. In emphasizing selectivi - ty , Schnaars and the authors of the M2-competition employed a relatively small number of homogeneous series and used rolling-origin evaluations (Schnaars) and multiple test periods (M2-competition) for diversity.


<!-- p:8 -->


The reliance on fixed-origin rather than rolling-origin evaluations in the three M-competitions was probably also essential for keeping the forecasting process manageable. In these studies, participants provided forecasts to the researchers, who had withheld the test period data. To implement a rolling-origin evaluation, the participants would have had to be shown the test period data, so that they could successively update the forecasting origins. In contrast, Schnaars (1986) produced his own forecasts.

In principle, a synthesis of the diversity and selectivity strategies is to be recommended. Ideally, a forecasting competition would begin with precisely described groups of time series, in which the series are homogeneous within group but heterogeneous between groups. Randomized selection could then be used to obtain a sample of series from each group.

Armstrong et al. (1998, p. 360) observed that within - group homogeneity abets method selection by helping the forecaster to determine which methods are best suited to the specific characteristics of the data. Within-group homogeneity can also be of value for forecasting product hierarchies. At the same time, the forecaster needs heterogeneity among groups to draw general inferences about the relative forecasting accuracy of different methods.

In practice, it is difficult to implement a random-sampling design. Time series are multiattributed: periodicity and type were the two explicit attributes in the forecasting competitions. However, type is really a catchall descriptor, comprising level of aggregation (item, product, brand, company, industry, economy), domain (financial, marketing, operations), geog - raphic area (country, region) and data charac - teristics (seasonal versus nonseasonal, stable versus volatile, trended versus untrended). Another dimension of importance is calendar time interval: Series differ in starting date, ending date, and length, and span different stages of economic cycles and product life cycles. Moreover, the attributes are interdependent in many ways: Seasonality is likely to be most pronounced in quarterly and monthly data, volatility greatest in micro level series, and trends strongest in macroeconomic data.

A perfectly stratified random sample, hence, is not a realistic possibility. Nevertheless, the competitions can be faulted for a lack of formality in the collection of data. Series were collected and retrospectively classified by attribute. For this reason alone, tabulations based on 'all series' are suspect.

### 6.1. Pooled data structure

The use of multiple time series, as in a forecasting competition, creates a pooled data structure: S time series, s 5 1 to S , and up to T 1 N time periods per series. Individual time series need not be of equal length nor need they cover the same calendar period. Hence, the periods of fit can vary in both length and calendar interval.

The length of the test period , however, is normally fixed for all time series of a given periodicity. For example, Schnaars (1986) withheld the last five years from all the historical series. In the three M-competitions, the test period was specified to be six years, eight quarters and 18 months for annual, quarterly and monthly data respectively.

Fixing the length of the test period is partly a matter of statistical convenience: it simplifies the calculation and presentation of forecast-error averages. Still, considerable obfuscation can result if the forecast error measures are tabulated for an aggregate of series of different periodicities. For the M-competition results, the 'all data' tables combined monthly, quarterly and annual series. Thus, a one step-ahead error figure blended the one-month-ahead, one-quarter-ahead and one-year-ahead forecast errors. The M2-competition and M3-competition have avoided this confusion by separately reporting results for series of different periodicities.


<!-- p:9 -->


### 6.2. Pooled averages

To calculate forecast error statistics in a multiseries data set, we can average errors across time series, o ; across lead time, o ; or s n both, o . Precisely how the averaging is done sn can be important.

#### 6.2.1. Choice of error statistic for averaging over series

Much has been written about the choice of forecast-error statistics. A good overview is provided in a series of articles and commentaries in the International Journal of Forecast - ing (Armstrong and Collopy, 1992; Fildes, 1992; Ahlburg et al., 1992).

There are two arithmetic issues. One concerns the choice of error measure : Should we be averaging squared errors, percent errors or relative errors? The second deals with the appropriate statistical operator: should we use a median, an arithmetic mean or geometric mean?

The lessons from the research are at least threefold: When averaging over series o , we s should:

1. Avoid scale dependent error measures, such as root mean squared error RMSE or mean absolute deviation MAD. With these, if you rescale the measurement (for example, from one currency to another or from millions of units to thousands of units), you alter the numerical value of the error measure. Moreover, a subset of the time series with large numerical values may dominate the error measures, and that subset would change with the scaling.
2. Use percent error measures instead, such as the absolute percent error (APE), because (for data with a natural zero) they are scale independent. However, the distribution of percent errors can be badly skewed, especially if the series contains values close to zero. In this case using the median absolute per-
3. cent error (MdAPE) may be preferable to using the MAPE. MdAPE is the principal error statistic used in Vokurka, Flores and Pearce (1996). Still another alternative to the MAPE is the symmetric MAPE (Armstrong, 1985, p. 348), which makes underforecasts and overforecasts of the same percent equal. This statistic is being featured in the M3competition.
3. Use relative error measures when it is necessary to average over time series that differ in volatility. Collopy and Armstrong proposed a ratio of an absolute error from a designated method to the analogous absolute error from  ̈ a naıve method, which they call the relative absolute error , RAE (Collopy and Armstrong, 1992, p.71). They showed that the RAE is not only scale independent but also serves to standardize the component series for degree of change and, hence, degree of forecasting difficulty. Tashman and Kruk (1996) used relative error measures to compare the accuracy of a forecasting method between distinct groups of time series. Recommended operators for averaging relative errors are the median (MdRAE) and geometric mean (GMRAE). Fildes (1992, p.84) endorses a variant (calculable only in a rolling-origin evaluation) called the relative geometric root mean square.

By using a single summation o , we obtain s an average error for an individual method at a specific horizon. In reporting the M-competition results, the authors refer an average of absolute percent errors (APEs) as an average MAPE (Makridakis et al., 1982, Table 2). For an individual lead time, however, it may be called simply a MAPE, without the preceding average , since we are averaging a single APE per time series.

#### 6.2.2. Cumulating over lead times

For cumulative lead time error measures, such as 1-4 quarters or 1-12 months ahead, we can use a double summation o , summing sn individual APEs over both the series and the lead times. Doing so gives equal weight to errors at short and long lead times. Alternatively, we can start with each individual lead time MAPE and then take an average or weighted average across lead times, o MAPE. The latter n properly requires a modifier such as average MAPE.


<!-- p:10 -->


The route taken for calculating cumulative lead time error measures can make a difference. Using the o approach maintains the distinctiven ness of the individual lead times and thus permits flexibility in assigning weights to reflect the relative importance of the individual horizons. Moreover, in a rolling-origin evaluation, the alternative o approach would assign sn greater weight for the first lead time, successively smaller weights for each longer lead. If equal weighting of each lead time is desired, the o n MAPE calculation is preferred.

Sensitivity to outliers can be mitigated in both approaches. With the doubly summed measure, we can calculate a median absolute percent error MdAPE or we can employ the median MAPE, as do Tashman and Kruk (1996, Table 7).

For measuring forecast accuracy over a cumulative lead time, Collopy and Armstrong propose the cumulative RAE (Collopy and Armstrong, 1992, p. 75-76).

### 6.3. Stability of error measures across forecasting origins

Pooling time series and cross-sectional data can create analytical and interpretational difficulties. Normally, as a precondition of pooling, we perform tests to see if the parameters of cross-sectional models are stable over time.

Fildes et al. (1998) used a data set of 263 telecommunications series to examine the stability of error measures across forecasting origins. Their results, similar to those reported earlier from Pack (1990), indicate that the relative accuracy (ranking) of different forecasting methods changed appreciably as the forecasting origin varied. Such instability, they concluded, should discourage forecasters from using a single forecasting origin.

Whether their concern extends to the forecasting competitions is uncertain. Their time series were of equal length and had identical starting and ending dates. The series in the M-competition and in the M3-competition have considerable diversity in length and calendar dates.

Calendar diversity plays the same role in multiseries evaluations that multiple test periods play in individual-series evaluations: Both mitigate the sensitivity of forecast error measures to the phase of the business cycle.

### 6.4. Method selection rules

In the forecasting competitions, every forecasting method was applied to every time series, whether or not the method was appropriate for the series. For example, Holt's exponential smoothing method was applied to nontrended series, and simple exponential smoothing was applied to trended series. Tashman and Kruk (1996, p. 5) call this unselective application and argue that, by fusing appropriate and inappropriate cases, unselective application tends to denigrate a method's expected performance. The alternative is to first screen out those series for which a method is judged inappropriate. Effective screening, however, requires a reliable method-selection rule.

Fildes (1989) articulated the distinction between (a) knowledge of a method's forecasting accuracy after a test and (b) the ability to select a best method in advance. 'Forecasting competitions, such as the M-competition, only offer the forecaster information on the relative accuracy of (methods) A and B, ex post; these show which of the two turned out to be better; but they do not demonstrate how to pick a winner' (1989, p. 1057).


<!-- p:11 -->


Effective method selection, ex ante, requires effective method - selection rules . Among the forecasting competitions, the M3-competition (Makridakis and Hibon, 2000) is the first to examine automatic forecasting systems , many of which incorporate method-selection rules. Although the M3-competition summary tables do not include a direct comparison of the category of automatic forecasting systems against the aggregate of single-method procedures, automatic systems were found to be among the methods that give best results for many types of time series.

This result is more promising than prior research would have suggested. Gardner and McKenzie (1988) offered selection rules for choosing among exponential smoothing procedures. Tashman and Kruk (1996) compared the Gardner-McKenzie protocol with two other protocols for method selection. They found that (1) none of method-selection protocols effectively identified an appropriate smoothing procedure for time series that lacked strong trends, (2) the protocols frequently disagreed as to what constituted an appropriate method, and (3) even when they agreed on an appropriate method, following their advice did not ensure improved forecasting accuracy (1996, p. 252).

### 6.5. Product hierarchies

While the authors of the forecasting competitions have classified time series by periodicity and level of aggregation, they have not incorporated hierarchical data structures. New techniques for demand forecasting have emerged in the past decade that link forecasts for one item (stock keeping unit) to the product class to which the item belongs. For example, Bunn and Vassilopoulis (1993) showed how the seasonal pattern in the product class aggregate could be applied effectively to forecast the seasonality in individual items. Several forecasting programs permit automatic adjustment of forecasts for individual items to reconcile them with the product-class aggregate, thus effectively imposing the structure of the product-class series on the individual components. Doing so is appealing when individual item series are short and irregular.

Testing product hierarchy methodologies should be a high priority for future research.

## 7. Out-of-sample evaluations in forecasting software

In a review of 13 business-forecasting programs with automatic forecasting features, Tashman and Leach (1991) reported that only six programs included post-sample tests of forecasting accuracy. Of these, moreover, all but two were limited to fixed-origin evaluations on a single series. In the two packages that offered rolling-origin evaluations, the implementation was based on a single series in a single test period and model coefficients that were held fixed rather than recalibrated through the test period. While the authors warned forecasting practitioners to evaluate those methods the software selected automatically, the forecasting software of the early 1990s did not facilitate this process.

Has out-of-sample testing in forecasting software been upgraded during the past decade? Of the 13 programs Tashman and Leach investigated, 10 have ceased to exist. In the remaining three, Autobox , Forecast Pro and SmartFore - casts , the developers have enhanced their postsample testing options All three now offer rolling out-of-sample evaluations and a variety of forecast error measures.

During the 1990s, the forecasting software market has seen many new entrants. Tashman and Hoover (2001) examined 15 forecasting software programs, of which 9 had their roots in the 1990s. They divided the forecasting packages into four categories: spreadsheet add-ins, forecasting modules of general statistical programs, neural-network programs, and dedicated business-forecasting programs. The last category included the three aforementioned packages plus Time Series Expert and tsMetrix .


<!-- p:12 -->


Tashman and Hoover (2001, Table 4) reported that only one of the three spreadsheet add-ins and one of the four general statistical programs effectively distinguished within - sam - ple from out - of - sample forecasting accuracy. In contrast, two of the three neural-network packages and three of the five dedicated businessforecasting programs made this distinction effectively.

In my further analysis of the 12 non-neural network programs (software references are at the end of the paper), I found that none of the four general statistical programs and none of the three spreadsheet add-ins offered a rolling outof-sample evaluation. In addition, most of these include a limited set of error measures: their developers essentially ignore the recent literature on forecast error measurement.

Within the category of dedicated businessforecasting software, tsMetrix comes closest to providing the opportunity for systematic out-ofsample tests on individual series. Once the user selects a test period, the program will perform a rolling-origin evaluation, recalibrating the coefficients of the forecasting equations at each update of the origin. This option is available for smoothing, ARIMA, and regression methods. Users can define multiple test periods; however, the program does not integrate error measures across test periods.

The post-sample procedure in Autobox matches that in tsMetrix , although it is available only for ARIMA modeling. The Forecast Pro procedure is also similar, except that it does not recalibrate coefficients with each update of the forecasting origin.

A major growth segment of the forecasting software market has been demand planning packages, which incorporate automatic batch forecasting for large product hierarchies. Unfortunately, few reviews and evaluations of this market segment have been published. Developers of demand planning packages have focused on the technology of managing forecasting databases and automating forecasting methods. This focus has come at the expense of transparency regarding how forecasts are made and what forecast errors to expect. Useful out-ofsample tests are seldom included in this type of program.

Forecast Pro , SmartForecasts and Autobox , which can serve as forecasting engines in a demand planning package, are major exceptions. These programs enable users to view average forecast errors made on an entire batch of time series. The programs perform rollingorigin evaluations on individual time series, sorts the forecasting errors by lead time and then report averages of the forecast errors across time series.

## 8. Summary

For an individual time series, out-of-sample testing of forecasting accuracy is facilitated by use of rolling-origin evaluations. The rollingorigin procedure permits more efficient seriessplitting rules, allows for distinct error distributions by lead time, and desensitizes the error measures to special events at any single origin. Applying the procedure across multiple test periods is desirable to mitigate the sensitivity of error measures to single phases of the business cycle. In an implementation of a rolling-origin evaluation, recalibration of the parameters of a forecasting equation can be important in general and is essential in the context of a regression model.

Forecasting software does not always nurture the proper implementation of post-sample tests. Many programs permit only fixed-origin evaluations and report few error measures. Those that offer rolling-origin evaluations often restrict them to certain methods, usually extrapolative.


<!-- p:13 -->


Few demand planning packages incorporate useful out-of-sample evaluations.

Forecasting competitions would be more generalizable if based upon precisely described groups of time series, in which the series were homogeneous within group and heterogeneous between groups. Even a large collection of time series does not automatically ensure diversity of forecasting situations, especially if calendar dates are more or less coterminous. Measures based on a single cross-section can be unstable over time. Error statistics that are calculated by applying every method to every time series may give misleading results. Evaluating methods used in forecasting product hierarchies remain an important avenue for further research.

<!-- END SOURCE 36/40: Tashman_2000_out-of-sample-forecast-accuracy.md -->

---

<!-- BEGIN SOURCE 37/40: Weinert_2007_efficient-whittaker-henderson-smoothing.md -->

# Source: `Weinert_2007_efficient-whittaker-henderson-smoothing.md`

---
id: "Weinert_2007_efficient-whittaker-henderson-smoothing"
source_pdf: "../pdf/Weinert_2007_efficient-whittaker-henderson-smoothing.pdf"
source_filename: "Weinert_2007_efficient-whittaker-henderson-smoothing.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 98.0
visual_assets: "disabled"
references_file: "../references/Weinert_2007_efficient-whittaker-henderson-smoothing.references.md"
---

<!-- p:1 -->

ELSEVIER

### COMPUTATIONAL STATISTICS &amp; DATA ANALYSIS

www.elsevier.com/locate/csda

##### Available online at www.sciencedirect.com

ScienceDirect

Computational Statistics &amp; Data Analysis 52 (2007) 959–974

## Efficient computation for Whittaker-Henderson smoothing

Howard L. Weinert*

Johns Hopkins University, 3400 N. Charles St., 105 Barton Hall, Baltimore, MD 21218, USA

Available online 22 December 2006

##### Abstract

Efficient algorithms that compute both the estimates and the generalized cross-validation score for the problem of WhittakerHenderson smoothing are presented. Algorithm efficiency results from carefully exploiting the problem's rich structure to reduce execution time and memory use. The algorithms are much faster than existing ones, and use significantly less memory. MATLAB M-files are included.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Smoothing; Graduation; Cross-validation; Hodrick-Prescott filter

### 1. Introduction

In the nineteenth century, actuaries began to develop smoothing methods to adjust, or graduate, raw mortality data in order to set life insurance premiums. These early methods involved the application of a moving weighted average filter to the data. The filter coefficients and length were determined by a variety of criteria, and each filter smoothed the data to a different degree. Although simple to implement, these filters have two major drawbacks. They cannot smooth near the ends of the data record, and the degree of smoothing for any particular filter is fixed. See Seal (1981) for a review of this early work. Henderson (1938), Miller (1946), and London (1985) are also useful.

Bohlmann (1899) made the first attempt to rectify both deficiencies of moving weighted average filters. He proposed solving a regularized least-squares problem in which a scalar parameter determines the tradeoff between fidelity to the data and smoothness of the filtered sequence. Whittaker (1923), unaware of Bohlmann's work, proposed the same idea two decades later, and is commonly credited with its invention.

Here is the idea. Given a sequence of n measurements {y1, y2, . . . , yn}, a positive real number λ, and a positive integer p &lt; n, find the sequence {x1, x2, . . . , xn} that minimizes

$$\lambda \sum _ { j = 1 } ^ { n } ( y _ { j } - x _ { j } ) ^ { 2 } + \sum _ { j = 1 } ^ { n - p } ( \Delta ^ { p } x _ { j } ) ^ { 2 } , \\$$

where ∆ is the forward difference operator:

$$\Delta x _ { j } & = x _ { j + 1 } - x _ { j } , \\ \Delta ^ { 2 } x _ { j } & = \Delta ( \Delta x _ { j } ) = x _ { j + 2 } - 2 x _ { j + 1 } + x _ { j } ,$$

* Tel.: +1 443 310 4332; fax: +1 410 516 5566.


<!-- p:2 -->


and so on. The first sum in (1.1) measures fidelity to the data, and the second measures smoothness, where a polynomial of degree p — 1 is considered maximally smooth. The parameter λ controls the tradeoff between fidelity and smoothness: as λ → 0 the solution converges to the polynomial of degree p — 1 that is the best least-squares fit to the data, and as λ → ∞ the solution converges to the measurement sequence. Furthermore, the first sum is a monotonically decreasing function of λ, while the second is a monotonically increasing function of λ.

If

$$y ^ { T } = [ y _ { 1 } \ y _ { 2 } \ \cdots \ y _ { n } ] ,$$

xT = [x1 x2 · · · xn],

the cost functional (1.1) can be written as

$$\lambda ( y - x ) ^ { T } ( y - x ) + x ^ { T } M ^ { T } M x ,$$

where M is a (n − p) × n differencing matrix. For example, when p = 2 and n = 6,

1

-2

1

0


1

-2 1 0

0


-21

0


1-2 1

The minimizer of (1.2) is the solution of the normal equations

$$A \hat { x } = \lambda y ,$$

where

$$A = \lambda I + M ^ { T } M .$$

The A matrix is symmetric, persymmetric (hence centrosymmetric), positive definite, banded (bandwidth = p), and quasi-Toeplitz (Toeplitz except for upper left and lower right p × p blocks). For example, when p = 2 and n = 6,

$$A = \left [ \begin{array} { c c c c c c c } 1 + \lambda & - 2 & 1 & 0 & 0 & 0 \\ - 2 & 5 + \lambda & - 4 & 1 & 0 & 0 \\ 1 & - 4 & 6 + \lambda & - 4 & 1 & 0 \\ 0 & 1 & - 4 & 6 + \lambda & - 4 & 1 \\ 0 & 0 & 1 & - 4 & 5 + \lambda & - 2 \\ 0 & 0 & 0 & 1 & - 2 & 1 + \lambda \end{array} \right ] . \\$$

The solution can also be obtained via

$$( I + \dot { \lambda } ^ { - 1 } M M ^ { T } ) M \hat { x } = M y ,$$

$$\hat { x } = y - \lambda ^ { - 1 } M ^ { \top } M \hat { x } .$$

This smoothing problem has a number of desirable features. Reversing the order of the measurements simply reverses the order of the estimates. Also, the first p moments of the data are preserved: when p = 2,

$$\sum _ { j = 1 } ^ { n } \hat { x } _ { j } = \sum _ { j = 1 } ^ { n } y _ { j } , \quad \sum _ { j = 1 } ^ { n } j \hat { x } _ { j } = \sum _ { j = 1 } ^ { n } j y _ { j } .$$

M =


<!-- p:3 -->


Polynomials of degree p – 1 are unaffected by the smoothing operation:

$$\hat { x } = y \ \Leftrightarrow \ M y = 0 .$$

Furthermore, since the eigenvalues of M MT are all positive, the eigenvalues of (I + λ−1 M MT)-1 are all less than one, and therefore (see (1.6)), as long as My ≠ 0,

$$\hat { x } ^ { T } M ^ { T } M \hat { x } < y ^ { T } M ^ { T } M y ,$$

which means that the estimates are actually smoother than the data. See Greville (1957) for a different proof of this fact. Finally, if the smoothing operation is applied iteratively,

$$M \hat { x } ^ { ( k ) } = ( I + \lambda ^ { - 1 } M M ^ { T } ) ^ { - 1 } M \hat { x } ^ { ( k - 1 ) } = ( I + \lambda ^ { - 1 } M M ^ { T } ) ^ { - k } M y \to 0 ,$$

as k → ∞. Since each x(k) will have the same first p moments as the data, X(k) will converge to the polynomial of degree p — 1 that is the best least-squares fit to the data. In other words, iterated smoothing produces the same result as letting λ → 0.

Both Bohlmann (1899) and Whittaker (1923) treated the normal equations as a difference equation of order 2p with p boundary conditions at each end. Bohlmann (1899) gave a complete solution for p = 1, while for p = 3, Whittaker (1923) provided an approximate solution valid for small λ. Later, Whittaker (1924) expressed the solution as an infinite series. For p = 1, 2, 3, Henderson (1924) solved the difference equation by first ignoring the boundary conditions, then approximately compensating for them. Aitken (1925) derived an exact solution to the difference equation and boundary conditions. Spoerl (1937) has an in-depth treatment of the difference equation approach. Henderson (1925) was the first to use matrix methods to solve the normal equations with what appears to be the earliest use of LDLT matrix factorization. His implementation is very efficient and is in fact identical to that of Martin et al. (1965).

Another way to solve the problem is to formulate it as a stochastic estimation problem, in which the smoothing parameter λ is the signal-to-noise ratio, and then apply a fixed interval smoothing algorithm. Kitagawa and Gersch (1984) and Verrall (1993) did so, but their state space algorithms are relatively inefficient.

None of the early researchers proposed an automatic way of choosing the smoothing parameter λ. However, Brooks et al. (1988) showed that the measurement-based generalized cross-validation (GCV) method, introduced by Craven and Wahba (1979) for continuous spline smoothing, can also be used for Whittaker-Henderson smoothing. With this adaptive method, λ is chosen to minimize the GCV score

$$n ^ { - 1 } \sum _ { j = 1 } ^ { n } \left ( \frac { y _ { j } - \hat { x } _ { j } } { 1 - n ^ { - 1 } \text { trace} ( \lambda A ^ { - 1 } ) } \right ) ^ { 2 } .$$

Consequently, the estimates and the trace of λA-1 (often called the "hat" matrix) must be computed for many trial values of λ. Fortunately, by using a trick generally attributed to Takahashi et al. (1973) but first employed by Spoerl (1943), the trace can be computed with only O(n) flops. Hutchinson and de Hoog (1985) took this approach for continuous spline smoothing. Alternatively, Kohn and Ansley (1989), using a result from Wahba (1983), computed the trace with O(n) flops as part of a state space algorithm for continuous spline smoothing. For our problem, the work load can be further cut in half by fully exploiting the structure of A. Additionally, Eilers (2003) developed a scaling method to approximately compute the GCV score with O(n) flops.

The issue of algorithm efficiency is critical with large data sets, which occur, for example, in communications or surveillance applications involving either a long observation interval Td or a high sampling rate Fs. In general, n = Fs Ta so even a 10 s observation interval coupled with a 100 kHz sampling rate produces one million measurements.

In the remainder of this paper we restrict attention to the p =2 case used in most applications. See, for example, Leser I1   ()    ()  e  ()    (  (1n) (1999), Ravn and Uhlig (2002), Eilers (2003). In Section 2 we present a LDLT factorization algorithm that computes both the estimates and the GCV score. In Section 3 we show that the estimates and GCV score can alternatively be obtained by solving an equivalent stochastic estimation problem, for which we give a simple derivation and a stable sht e ei e e o  so   o  oo e e s te version of our factorization algorithm. In Section 5 we examine the performance of our full and truncated algorithms. In Section 6 we consider the frequency response in the steady-state case, and comment on the Hodrick-Prescott filter. Section 7 has conclusions and Section 8 contains MATLAB M-files of our algorithms.


<!-- p:4 -->


### 2. Factorization algorithm

To solve (1.3) we factor the coefficient matrix as

$$A = L D L ^ { T } ,$$

where L is a banded (bandwidth = 2) unit lower triangular matrix and D is a diagonal matrix. Denote the elements on the first subdiagonal of L as {−e1, −e2, . . . , −en−1} and those on the second subdiagonal as {f1, f2, . . . , fn−2}. Denote the elements on the diagonal of D as {d1, d2, . . . , dn}. In (2.1), equating corresponding entries, row by row, on the diagonal and first and second superdiagonals leads to

$$d _ { 1 } = 1 + \lambda , \quad f _ { 1 } = 1 / d _ { 1 } , \quad \mu _ { 1 } = 2 , \quad e _ { 1 } = \mu _ { 1 } f _ { 1 } ,$$

$$d _ { 2 } = 5 + \lambda - \mu _ { 1 } e _ { 1 } , \quad f _ { 2 } = 1 / d _ { 2 } , \quad \mu _ { 2 } = 4 - e _ { 1 } , \quad e _ { 2 } = \mu _ { 2 } f _ { 2 } ,$$

$$d _ { j } = 6 + \lambda - \mu _ { j - 1 } e _ { j - 1 } - f _ { j - 2 } , \quad f _ { j } = 1 / d _ { j } , \quad \mu _ { j } = 4 - e _ { j - 1 } , \quad e _ { j } = \mu _ { j } f _ { j } ,$$

$$d _ { n - 1 } = 5 + \lambda - \mu _ { n - 2 } e _ { n - 2 } - f _ { n - 3 } , \quad f _ { n - 1 } = 1 / d _ { n - 1 } , \quad \mu _ { n - 1 } = 2 - e _ { n - 2 } , \quad e _ { n - 1 } = \mu _ { n - 1 } f _ { n - 1 } ,$$

$$d _ { n } = 1 + \lambda - \mu _ { n - 1 } e _ { n - 1 } - f _ { n - 2 } , \quad f _ { n } = 1 / d _ { n } .$$

In this way we do not need to form the A matrix in the MATLAB M-file, thus greatly reducing memory use and array access time. As L and D are being obtained, we solve the triangular system

$$L D b = \lambda y ,$$

using

$$b _ { 1 } = f _ { 1 } \lambda y _ { 1 } , \ \ b _ { 2 } = f _ { 2 } ( \lambda y _ { 2 } + \mu _ { 1 } b _ { 1 } ) ,$$

$$b _ { j } = f _ { j } ( \lambda y _ { j } + \mu _ { j - 1 } b _ { j - 1 } - b _ { j - 2 } ) .$$

Finally, we solve the triangular system

LTx = b,

using

$$\hat { x } _ { n } = b _ { n } , \quad \hat { x } _ { n - 1 } = b _ { n - 1 } + e _ { n - 1 } \hat { x } _ { n } ,$$

$$\hat { x } _ { j } = b _ { j } + e _ { j } \hat { x } _ { j + 1 } - f _ { j } \hat { x } _ { j + 2 } .$$

Note that we could just as easily have used a U DUT factorization of A, where U is unit upper triangular, but this produces the same d, e, f sequences only in reverse order. In other words, U and D are 180° rotations of L and D.

The GCV score depends on the diagonal entries of A−1. Since A−1 is centrosymmetric, only about half of its diagonal entries are unique. From (2.1),

$$A ^ { - 1 } = L ^ { - T } D ^ { - 1 } L ^ { - 1 } ,$$

and thus,

$$L ^ { \top } A ^ { - 1 } = D ^ { - 1 } L ^ { - 1 } .$$

Consequently,

$$A ^ { - 1 } = A ^ { - 1 } + D ^ { - 1 } L ^ { - 1 } - L ^ { T } A ^ { - 1 } = D ^ { - 1 } L ^ { - 1 } + ( I - L ^ { T } ) A ^ { - 1 } .$$

Since L−1 is unit lower triangular, D−1 L-1 is lower triangular with jth diagonal entry f j . Furthermore, I — LT is upper triangular and banded (bandwidth = 2) with zeros on its diagonal and with {e1, e2, . . . , en−1} and {− f1, − f2, . . . , — fn-2} on its first and second superdiagonals, respectively. The unique diagonal entries of A−1 can be obtained from


<!-- p:5 -->


(2.11) by equating corresponding entries on the lower parts of the diagonal and first and second superdiagonals. If g j, h j, and q j, respectively, denote entries on the diagonal and first and second superdiagonals of A−1, then the resulting recursions are

$$g _ { 1 } = f _ { n } , \ \ h _ { 1 } = e _ { n - 1 } \, g _ { 1 } , \ \ g _ { 2 } = f _ { n - 1 } + e _ { n - 1 } \, h _ { 1 } ,$$

$$q _ { j - 2 } = e _ { n - j + 1 } h _ { j - 2 } - f _ { n - j + 1 } g _ { j - 2 } , \quad h _ { j - 1 } = e _ { n - j + 1 } g _ { j - 1 } - f _ { n - j + 1 } h _ { j - 2 } ,$$

$$g _ { j } = f _ { n - j + 1 } + e _ { n - j + 1 } h _ { j - 1 } - f _ { n - j + 1 } q _ { j - 2 } ,$$

Whs         e n nn  o (n      sna  oon can be evaluated.

### 3. State space algorithm

Consider the stochastic model

$$M x = u ,$$

$$y = x + v ,$$

where u and v are mutually uncorrelated with zero means and covariance matrices I and λ-1I, respectively. Also let

$$\theta _ { 1 } = \begin{bmatrix} x _ { 1 } \\ x _ { 2 } \end{bmatrix} ,$$

where θ1 is uncorrelated with u and v, and has zero mean and covariance matrix βI with β &gt; 0. We can solve (3.1), (3.3) as

$$x = W \left [ \begin{smallmatrix} \theta _ { 1 } \\ u \end{smallmatrix} \right ] ,$$

where W is a n × n unit lower triangular matrix satisfying

$$[ I _ { 2 } \, \ 0 ] W & = [ I _ { 2 } \, \ 0 ] , \\ M W & = [ 0 \, \ I _ { n - 2 } ] .$$

If Rx denotes the covariance matrix of x, then from (3.4),

Rx = W

WT.

βI2

0


In−2

If ê is the linear least-squares estimate of x given the measurements y in (3.2), and Re is the associated error covariance matrix, then

$$\hat { x } = R _ { x } ( \lambda ^ { - 1 } I + R _ { x } ) ^ { - 1 } y = ( \lambda I + R _ { x } ^ { - 1 } ) ^ { - 1 } \lambda y ,$$

$$R _ { e } = R _ { x } - R _ { x } ( \lambda ^ { - 1 } I + R _ { x } ) ^ { - 1 } R _ { x } = ( \lambda I + R _ { x } ^ { - 1 } ) ^ { - 1 } .$$

Since (3.5) implies

$$M ^ { T } M = W ^ { - T } \left [ \begin{matrix} 0 & 0 \\ 0 & I _ { n - 2 } \end{matrix} \right ] W ^ { - 1 } ,$$

then for β−1 = 0 (diffuse prior),

$$\lambda I + R _ { x } ^ { - 1 } = \lambda I + M ^ { T } M = A .$$


<!-- p:6 -->


Therefore,

$$\hat { x } = A ^ { - 1 } \lambda y ,$$

which is the minimizer of (1.2), and

$$A ^ { - 1 } = R _ { e } .$$

Therefore, we can determine the Whittaker-Henderson estimates and GCV score by solving the signal-plus-noise estimation problem modeled by (3.1)–(3.2) with a diffuse prior, and evaluating the trace of Re.

This estimation problem can be solved by writing (3.1)–(3.3) in state space form. If

$$\theta _ { k } = \begin{bmatrix} x _ { k } \\ x _ { k + 1 } \end{bmatrix} ,$$

then

$$\theta _ { k + 1 } & = F \theta _ { k } + G u _ { k } , \\ y _ { k } & = H \theta _ { k } + v _ { k } ,$$

where the system matrices are

$$F = \left [ \begin{matrix} 0 & 1 \\ - 1 & 2 \end{matrix} \right ] , \quad G = \left [ \begin{matrix} 0 \\ 1 \\ 1 \end{matrix} \right ] , \quad H = [ 1 \ \ 0 ] .$$

The state estimate k can be obtained by applying a recursive fixed interval smoothing algorithm, of which there are four basic types (Weinert, 2001). Only the backward–forward algorithm of Mayne (1966) and Desai et al. (1983) and the forward–backward algorithm of Watanabe and Tzafestas (1989) can seamlessly accommodate a diffuse prior without any modifications or complications. Since both algorithms are equally efficient, we will examine only the backward–forward one.

The backward recursions of this algorithm are

$$S _ { n } = \lambda H ^ { \top } H , \ \ r _ { n } = \lambda H ^ { \top } y _ { n } ,$$

$$K _ { k } = ( 1 + G ^ { T } S _ { k } G ) ^ { - 1 } G ^ { T } S _ { k } F ,$$

$$S _ { k - 1 } = ( F - G K _ { k } ) ^ { T } S _ { k } ( F - G K _ { k } ) + K _ { k } ^ { T } K _ { k } + \lambda H ^ { T } H ,$$

$$r _ { k - 1 } = ( F - G K _ { k } ) ^ { T } r _ { k } + \lambda H ^ { T } y _ { k - 1 } .$$

The forward recursion is

$$\hat { \theta } _ { 1 } = S _ { 1 } ^ { - 1 } r _ { 1 } ,$$

$$\hat { \theta } _ { k } = ( F - G K _ { k } ) \hat { \theta } _ { k - 1 } + ( 1 + G ^ { T } S _ { k } G ) ^ { - 1 } G G ^ { T } r _ { k } ,$$

$$\hat { x } _ { k } = H \hat { \theta } _ { k } .$$

The matrix S1 is nonsingular if n &gt; 1.

If Pk denotes the covariance matrix of (θk — θk), then from (3.6)–(3.7), (3.15),

$$g _ { k } = ( A ^ { - 1 } ) _ { k k } = ( R _ { e } ) _ { k k } = H \, P _ { k } \, H ^ { T } .$$

Pk can be computed from the forward recursion

$$( 3 . 1 7 )$$

$$P _ { k } = ( F - G K _ { k } ) P _ { k - 1 } ( F - G K _ { k } ) ^ { \top } + ( 1 + G ^ { \top } S _ { k } G ) ^ { - 1 } G G ^ { \top } ,$$


<!-- p:7 -->


where, since A−1 is centrosymmetric, k runs from 2 to ceil (n/2). All the above recursions are stable because, for our system matrices (3.8), the spectral radius of (F — G K k) is less than one for all k &lt; n. Note that any off-diagonal entry in A−1 can be expressed in terms of Pk via

$$( A ^ { - 1 } ) _ { j k } = ( R _ { e } ) _ { j k } = H ( F - G K _ { j } ) \cdots ( F - G K _ { k + 1 } ) P _ { k } H ^ { \top } , \ \ j > k .$$

See Weinert (2001) and, for related results, Koopman and Harvey (2003). Furthermore, one can verify that

$$P _ { k } = \begin{bmatrix} g _ { k } & h _ { k } \\ h _ { k } & g _ { k + 1 } \end{bmatrix} , \ 1 \leqslant k \leqslant n - 1 ,$$

so that (3.17)–(3.18) is just a version of (2.12)–(2.14).

It has long been known that there is a close connection between triangular factorization and the solution of Riccati equations (Kailath et al., 2000). For our particular problem, one can obtain the following explicit relations between the Riccati equation solution and closed-loop system matrix, and the entries in L:

$$S _ { j } = \begin{bmatrix} \lambda + 1 - f _ { n - j - 1 } & \ e _ { n - j - 1 } - 2 \\ \ e _ { n - j - 1 } - 2 & f _ { n - j } ^ { - 1 } - 1 \end{bmatrix} , \ \ 2 \leqslant j \leqslant n - 2 ,$$

$$F - G K _ { j } = \left [ \begin{matrix} 0 & 1 \\ - f _ { n - j } & e _ { n - j } \end{matrix} \right ] , \quad 2 \leqslant j \leqslant n - 1 .$$

Hence the Riccati equation (3.11) is a version of (2.2)–(2.6). Therefore, we would expect a MATLAB implementation of the state space algorithm to have nearly the same execution time and memory use as that of the factorization algorithm, and indeed that is the case. Consequently, we will not include its MATLAB M-file in Section 8.

### 4. Truncated factorization algorithm

Both Weaver (1943) and Spoerl (1943) observed that the sequences in (2.4) converge. Bauer (1954, 1955, 1956) proved convergence and identified the limits and the rate of convergence. See also Malcolm and Palmer (1974) and Hafner (1995). In particular, Bauer showed that as j, n → ∞,

$$e _ { j } \rightarrow e , \quad f _ { j } \rightarrow f ,$$

where e and f satisfy the polynomial equation (recall (1.5))

$$^ { 2 } - 4 z + 1 = \frac { 1 } { f } ( z ^ { 2 } - e z + f ) ( f z ^ { 2 } - e z + 1 ) .$$

He also showed that

$$| f _ { j } - f | \leqslant \gamma \rho ^ { 2 j } ,$$

for γ &gt; 0, where ρ is the magnitude of the roots of the polynomial (4.2) that lie inside the unit circle. (Since this polynomial has real, symmetric coefficients, its roots occur in conjugate and reciprocal pairs.) The e j sequence converges at the same rate. In light of (3.21)–(3.22), one can also deduce (4.1) and (4.3) from known facts about the convergence of the solution of the Riccati equation (3.11) (Kailath et al., 2000).

Earlier, Henderson (1924) had studied the factorization (4.2) and had shown that

$$e = \frac { 2 \alpha } { \alpha + 1 } , \quad f = \frac { \alpha } { \alpha + 2 } ,$$

where α &gt; 0 is related to the original smoothing parameter λ by

$$\lambda = \frac { 4 } { \alpha ( \alpha + 1 ) ^ { 2 } ( \alpha + 2 ) } .$$


<!-- p:8 -->


Table 1 Number of iterations in (2.4) and (2.13)–(2.14)

| afii9846   |   N |   ˆ N |
|------------|-----|-------|
| J = 6      |     |       |
| 0.1        |  70 |    70 |
| 0.3        |  24 |    24 |
| 0.5        |  14 |    14 |
| 0.7        |  10 |     9 |
| J = 9      |     |       |
| 0.1        | 104 |   105 |
| 0.3        |  35 |    35 |
| 0.5        |  20 |    20 |
| 0.7        |  14 |    13 |

However, it will prove more convenient to use σ ∈ (0, 1) as the basic smoothing parameter, where

$$\sigma = \frac { 1 } { \alpha + 1 } ,$$

in which case,

$$e = 2 ( 1 - \sigma ) , \quad f = \frac { 1 - \sigma } { 1 + \sigma } , \quad \lambda = \frac { 4 \sigma ^ { 4 } } { 1 - \sigma ^ { 2 } } .$$

Note that as σ → 0, λ → 0, and as σ → 1, λ → ∞. It turns out (see (6.3)) that σ = sin φρ, where φ is the angle of the first quadrant roots of (4.2), and

$$\rho ^ { 2 } = f .$$

Spoerl (1937, 1943), expanding on the work of Aitken (1925), showed that the sequences in (2.12)–(2.14) also o ovd s   s    ←n ←  u  s ad r r)

$$g = \frac { 1 - \sigma ^ { 2 } } { 4 \sigma ^ { 3 } ( 2 - \sigma ^ { 2 } ) } .$$

The rate of convergence of the g j sequence is identical to that of the fj and e j sequences.

With the above facts, we can greatly reduce execution time and memory use for large data sets by computing the sequences in (2.4) and (2.13)–(2.14) only until they are sufficiently close to their limiting values. Ideally, we want to find the smallest integer N such that

$$\max \left \{ \left | \frac { f _ { j } - f } { f } \right | , \left | \frac { e _ { j } - e } { e } \right | , \left | \frac { g _ { j } - g } { g } \right | \right \} < 1 0 ^ { - J } , \ \ j \geqslant N ,$$

where the error exponent J is chosen by the user. For programming purposes, however, it is more efficient to estimate the number of required iterations ahead of time, in terms of σ and J. Recalling (4.3) and (4.8), we seek the smallest integer N such that

$$\max \left \{ f ^ { j - 1 } , \frac { f ^ { j } } { \ e } , \frac { f ^ { j } } { \ g } \right \} < 1 0 ^ { - J } , \ \ j \geq \hat { N } .$$

Since f &lt; e and f &lt; g, the first quantity in the braces is the largest, so we will take

$$\hat { N } = \text {ceil} \left ( 1 - \frac { J } { \log _ { 1 0 } f } \right ) ,$$

where f is given by (4.7). With this estimate, we evaluate the quantities in (2.4) and (2.13)–(2.14) for 3 ≤ j ≤ , then set

$$f _ { j } = f , \quad e _ { j } = e , \quad g _ { j } = g , \ \ j \geq \hat { N } + 1 .$$


<!-- p:9 -->


Note that as σ → 0, f. → 1 and  will eventually exceed ceil(n/2), in which case one should use the full algorithm. Table 1 shows N and  for four values of σ and two values of the error exponent J.

We see that the estimate of N is extremely good, and that for large data sets, the number of necessary iterations will be relatively small.

### 5. Algorithm performance

Table 2 shows the execution time and memory use of our full and truncated factorization algorithms and that of Eilers (2003). All tests were run on a 1.73 GHz (Centrino) Windows laptop using MATLAB 7.0. Execution times are averages for 50 runs, all using the same simulated measurements and the same value for σ to compute the estimates and the GCV score. Results for the truncated algorithm were the same for all values of σ and J considered in Table 1. Execution time and memory use are proportional to the number of measurements for all three algorithms. The full algorithm runs about 30 times faster than Eilers' while using about one-fifth of the memory. The truncated algorithm requires half the memory and less than 60% of the execution time of the full algorithm.

To assess how much accuracy is lost when the truncated algorithm is used, measurements were simulated with the following MATLAB commands:

```
n = 1 : 100000,

y = n. * exp(-.01 * n) + randn(size(n)).

```

The estimates and GCV score were computed with the full and truncated algorithms. Table 3 shows the maximum relative error in the estimates and the relative error in the GCV score for four values of σ and two values of the error exponent J. Not surprisingly, the errors decreased as J increased. In general, a larger σ meant smaller errors. The entries changed only slightly with different realizations of the random number generator or with different n.

w  u   v    g     v t s       es the GCV score. So we should compare the estimates from the two algorithms when both use optimal σ values. As an signal example, measurements were simulated using the commands

Table 2 Execution time/memory use

| Number of measurements   | Full algorithm        | Truncated algorithm   | Eilers' algorithm       |
|--------------------------|-----------------------|-----------------------|-------------------------|
| 10 5 10 6                | 21ms/3.2MB 210ms/32MB | 12ms/1.6MB 123ms/16MB | 555ms/15MB 6047ms/148MB |

Table 3 Accuracy of truncated algorithm

| afii9846   | Maximum relative error in estimates   | Relative error in GCV score   |
|------------|---------------------------------------|-------------------------------|
| J = 6      |                                       |                               |
| 0.1        | 1 . 6 × 10 - 6                        | 1 . 9 × 10 - 10               |
| 0.3        | 4 . 8 × 10 - 7                        | 1 . 1 × 10 - 10               |
| 0.5        | 2 . 5 × 10 - 7                        | 2 . 2 × 10 - 11               |
| 0.7        | 3 . 3 × 10 - 7                        | 3 . 4 × 10 - 12               |
| J = 9      |                                       |                               |
| 0.1        | 3 . 7 × 10 - 8                        | 8 . 7 × 10 - 13               |
| 0.3        | 3 . 2 × 10 - 10                       | 5 . 0 × 10 - 13               |
| 0.5        | 3 . 5 × 10 - 10                       | 1 . 2 × 10 - 13               |
| 0.7        | 3 . 1 × 10 - 10                       | 1 . 3 × 10 - 12               |


<!-- p:10 -->


Fig. 1. Smoothing example.

data

13

14

13

12


11


10


9


8


7


6

0

2

4

6

8

10

0

2

4

6

8

10

x10^4

00

estimate (full algorithm)

estimate (truncated algorithm)

14


13


12


11


10


9


8


7


0

2

4

6

8

10

0

2

4

6

8

10

x10^4

```
c=x.npre, nca.mean.c - we c.minuated as img the command.s

                n = 1 : 1000000,

                c = .000001,

                s = 10 + cos(100 * c * n) + cos(197 * c * n) + cos(338 * c * n),

                y = s + 0.1 * randn(size(n)).

    The syntax is: u1.n = y, for the y-th, n-th, n-cumsum, for the y-th, c = 0.1(0, . . 0) and . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
```

The optimal value for the smoothing parameter was found to be σ = .010 (corresponding to λ = 4 × 10−8) for both the full and truncated algorithms. With error exponent J = 6, the maximum relative error between the two estimates was 2.5 × 10−6; for J = 9, the maximum relative error was 8.5 × 10−9. The rms errors were much smaller: 7.9 × 10−15 and 3.9 × 10−17, respectively. Plots of the signal s, the data y, and the estimates from the full and truncated (J = 6) algorithms are shown in Fig. 1. Simulations with other signals and other noise levels produced similar excellent results. The choice J = 6 should be sufficient for most applications, although taking J = 9 entails only a negligible increase in execution time and memory use. Since the user can control the resulting error, the truncated algorithm should be the algorithm of choice.

### 6. Frequency response of the steady-state smoother

For finite n, the Whittaker-Henderson smoother is a time-varying linear filter and thus is not amenable to standard y r -t  r     r s  e    ept

x10^4


<!-- p:11 -->


near the ends of the data record. These boundary effects can be eliminated by letting the number of measurements eco    o o -   s t   o s ows of A:

$$\hat { x } _ { i } - 4 \hat { x } _ { i + 1 } + ( \lambda + 6 ) \hat { x } _ { i + 2 } - 4 \hat { x } _ { i + 3 } + \hat { x } _ { i + 4 } = \lambda y _ { i + 2 } .$$

This particular difference equation was studied in detail by Spoerl (1937), whose work was based on the earlier research of Henderson (1924) and Aitken (1925). These results, some of which have been rederived by Unser et al. (1991), are summarized in the next paragraph.

Taking the (bilateral) z-transform of (6.1), we see that the transfer function of the steady-state smoother is

$$H ( z ) = \frac { \hat { X } ( z ) } { Y ( z ) } = \frac { \lambda z ^ { 2 } } { z ^ { 4 } - 4 z ^ { 3 } + ( \lambda + 6 ) z ^ { 2 } - 4 z + 1 } = \frac { \lambda z ^ { 2 } } { ( z - 1 ) ^ { 4 } + \lambda z ^ { 2 } } .$$

The four poles occur in conjugate and reciprocal pairs, and are in the first and fourth quadrants of the complex plane. Iie   t     oe  ie  e e o  t e    oe  e d n relations hold (see (4.7)–(4.8)):

$$\sin ^ { 2 } \varphi = \frac { 2 \sqrt { \lambda } } { \sqrt { \lambda + 1 6 } + \sqrt { \lambda } } , \quad \rho ^ { 2 } = \frac { 1 - \sin \varphi } { 1 + \sin \varphi } .$$

Note that the region of convergence of H (z) is ρ &lt; |z| &lt; ρ−1. By expanding (6.2) in partial fractions and carrying out long division term by term, we can write the transfer function as

$$H ( z ) = k _ { 0 } + \sum _ { i = 1 } ^ { \infty } k _ { i } ( z ^ { - i } + z ^ { i } ) ,$$

where

$$k _ { i } = k _ { 0 } \rho ^ { i } ( \cos ( i \varphi ) + \cos \varphi \sin ( i \varphi ) ) ,$$

and

$$k _ { 0 } = \frac { \sin \varphi } { 2 - \sin ^ { 2 } \varphi } = \frac { \sigma } { 2 - \sigma ^ { 2 } } .$$

Consequently, the solution to the steady-state problem is

$$\hat { x } _ { j } = k _ { 0 } y _ { j } + \sum _ { i = 1 } ^ { \infty } k _ { i } ( y _ { j - i } + y _ { j + i } ) .$$

Furthermore,

$$k _ { 0 } + 2 \sum _ { i = 1 } ^ { \infty } k _ { i } = 1 , \quad \lim _ { i \to \infty } k _ { i } = 0 , \quad k _ { 0 } = \max _ { i } \, k _ { i } .$$

A comparison of (1.3) and (6.7) shows that

$$\lim _ { n \to \infty } n ^ { - 1 } \text {trace} ( \lambda A ^ { - 1 } ) = k _ { 0 } ,$$

and thus when n is very large, the GCV score for a given σ could be estimated as

$$n ^ { - 1 } \sum _ { j = 1 } ^ { n } \left ( \frac { y _ { j } - \hat { x } _ { j } } { 1 - k _ { 0 } } \right ) ^ { 2 } .$$


<!-- p:12 -->


Fig. 2. Frequency response.

1

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0


0.4

0.6

0.8

De Nicolao et al. (2000) obtained a result analogous to (6.9) for continuous cubic spline smoothing. Also, the fact that the k sequence converges exponentially to zero could be deduced from general properties of the inverses of band matrices (Demko, 1977).

Although neither Henderson, Aitken, nor Spoerl studied the frequency response, it can easily be obtained from the transfer function (6.2) by replacing z with ejω, in which case

$$H ( \omega ) = \frac { \lambda } { \lambda + 4 ( 1 - \cos \omega ) ^ { 2 } } .$$

Clearly,

$$\lim _ { \lambda \to \infty } \, H \left ( \omega \right ) = 1 , \quad \lim _ { \lambda \to 0 } \, H \left ( \omega \right ) = \begin{cases} 1 , & \omega = 0 , \\ 0 , & \omega \neq 0 . \end{cases}$$

See Fig. 2 for plots of the frequency response as a function of the normalized frequency ω/π. From left to right, the curves correspond to λ = 4.0 × 10−4 (σ = 0.1), λ = 3.6 × 10−2 (σ = 0.3), λ = 0.33 (σ = 0.5), λ = 1.9 (σ = 0.7).

As long as

$$\lambda \leqslant \frac { 4 } { \sqrt { 2 } - 1 } \cong 9 . 6 ,$$

this low-pass filter has a cutoff frequency ωc given by

$$\omega _ { c } = \cos ^ { - 1 } \left ( 1 - \frac { 1 } { 2 } \sqrt { ( \sqrt { 2 } - 1 ) \lambda } \right ) .$$

Note that

$$H ( \omega ) \cong \frac { \lambda } { \lambda + \omega ^ { 4 } } \quad \text {for small $\omega$} .$$

Also, since H(2)(0) = 0, the steady-state smoother reproduces cubics (Schoenberg, 1946). For finite n, the WhittakerHenderson smoother will reproduce lines, but not cubics.

0.2


<!-- p:13 -->


Economists have used a modification of the Whittaker-Henderson smoother to study business cycles (King and Rebelo, 1993; Hodrick and Prescott, 1997; Baxter and King, 1999; Ravn and Uhlig, 2002). This so-called HodrickPrescott filter computes (y — x) instead of . Its steady-state version is therefore a high-pass filter with frequency response:

$$H _ { h p } ( \omega ) = 1 - H ( \omega ) = \frac { 4 ( 1 - \cos \omega ) ^ { 2 } } { \lambda + 4 ( 1 - \cos \omega ) ^ { 2 } } .$$

As long as

$$\lambda \leqslant \frac { 1 6 ( \sqrt { 2 } - 1 ) } { 4 - \sqrt { 2 } } \cong 2 . 5 6 ,$$

the steady-state Hodrick-Prescott filter has a cutoff frequency  ̄c given by

$$\bar { \omega } _ { c } = \cos ^ { - 1 } \left ( 1 - \frac { 2 \sqrt { \bar { \lambda } } } { \sqrt { \sqrt { 2 } ( \lambda + 1 6 ) - 1 6 } } \right ) .$$

Instead of letting the measurements speak for themselves by using generalized cross-validation to choose λ, economists arbitrarily set  ̄c = π/16 when smoothing quarterly data, thus cutting off cyclical components with periods exceeding eight years, or 32 quarters. This choice implies λ−1 = 1635, which is rounded to 1600. There is less unanimity when data are acquired annually or at some other rate. However, if one accepts λ-1 = 1635 for quarterly data, then for other rates the filter should continue to cutoff periods above eight years. For annual data, therefore, we should set c = π/4 which implies λ-1 = 6.822. This is approximately the conclusion of Ravn and Uhlig (2002), who reasoned along different lines. Of course, any rationale related to cutoff frequency requires that the number of measurements be large enough to make the steady-state approximation reasonable.

### 7. Conclusions

The key to efficient computation is special-purpose code that takes advantage of the mathematical structure of the problem and the characteristics of the programming language. We have produced full and truncated algorithms for the Whittaker-Henderson smoothing problem. The truncated algorithm involves a slight approximation, but the resulting error can be controlled by the user. By using our approach, the interested reader can produce similar code for other values of p. In forthcoming work, we will address the problem of smoothing with interpolation.

### 8. MATLAB M-files

The M-files for the full factorization algorithm smooth and the truncated algorithm tsmooth are given below. The inputs to smooth are the row vector of measurements and the smoothing parameter σ. The outputs are the row vector of estimates and the GCV score. The inputs to tsmooth are the row vector of measurements, the smoothing parameter σ, and the error exponent J. The outputs are the row vector of estimates and the GCV score.

function[x, score] = smooth(y, sig)

n = length(y); nc = ceil(n/2);

e = zeros(1, n − 1); f = zeros(1, n); x = zeros(1, n);

lam = 4 * sig^4/(1 − sig^2);

a1 = 1 + lam; a2 = 5 + lam; a3 = 6 + lam;


<!-- p:14 -->


%Factor the coefficient matrix and solve the first triangular system

```
d = a 2 - mu * e ( 1); f ( 2) = 1 / d; x ( 2) = f ( 2 ) * ( lam * y ( 2 ) + mu * x ( 1 ) ); mu = 4 - e ( 1 ) ; e ( 2 ) = mu * f ( 2 );
```

H.L. Weinert / Computational Statistics & Data Analysis 52 (2007) 959-974

%Factor the coefficient matrix and solve the first triangular system

d = a1; f(1) = 1/d; x(1) = f(1) * 1am * y(1); mu = 2; e(1) = mu * f(1);
d = a2 - mu * e(1); f(2) = 1/d; x(2) = f(2) * (lam * y(2) + mu * x(1)); mu = 4 - e(1); e(2) = e(1);
for j = 3 : n - 2
    m1 = j - 1;
    m2 = j - 2;
    d = a3 - mu * e(m1) - f(m2);
    f(j) = 1/d;
    x(j) = f(j) * (lam * y(j) + mu * x(m1) - x(m2));
    mu = 4 - e(m1);
    e(j) = mu * f(j);
end
d = a2 - mu * e(n - 2) - f(n - 3); f(n - 1) = 1/d;
x(n - 1) = f(n - 1) * (lam * y(n - 1) + mu * x(n - 2) - x(n - 3));
mu = 2 - e(n - 2); e(n - 1) = mu * f(n - 1);
d = a1 - mu * e(n - 1) - f(n - 2); f(n) = 1/d;
x(n) = f(n) * (lam * y(n) + mu * x(n - 1) - x(n - 2));

%Solve the second triangular system and find avg squared error
sq = (y(n) - x(n))^2;
x(n - 1) = x(n - 1) + e(n - 1) * x(n);
sq = sq + (y(n - 1) - x(n - 1))^2;
for j = n - 2 : -1 : 1
    x(j) = x(j) + e(j) * x(j + 1) - f(j) * x(j + 2);
    sq = sq + (y(j) - x(j))^2;
end
sq = sq/n;

%Compute GCV score

g2 = f(n); tr = g2; h = e(n - 1) * g2;
g1 = f(n - 1) + e(n - 1) * h; tr = tr + g1;
for k = n - 2 : -1 : n - nc + 1
    q = e(k) * h - f(k) * g2;
    h = e(k) * g1 - f(k) * h; g2 = g1;
    g1 = f(k) + e(k) * h - f(k) * q;
    tr = tr + g1;
end
tr = (2 * tr - rem(n, 2) * g1) * lam/n;
score = sq/(1 - tr)^2;

function[x, score] = tsmooth(y, sig, J)
r = length(y); nc = ceil(n/2);
elim = 2 * (1 - sig); flim = (1 - sig)/(1 + sig); lam = 4 * sig^4/(1 - sig^2);
N = ceil(1 - J / log 10(flim)); glim = (1 - sig^2)/(4 * sig^3 * (2 - sig^2));
e = zeros(1, N + 1); f = zeros(1, N + 2); x = zeros(1, n);
a1 = 1 + lam; a2 = 5 + lam; a3 = 6 + lam;
if N > nc
    error('sig too small, use smooth instead')
end
```


<!-- p:15 -->


%Factor the coefficient matrix and solve the first triangular system

```
%Factor the coefficient matrix and solve the first triangular system

    d = a1; f (1) = 1/d; x (1) = f (1) * lam * y (1); mu = 2; e(1) = mu * f (1);
    d = a2 - mu * e(1); f (2) = 1/d; x (2) = f (2) * (lam * y (2) + mu * x (1)); mu = 4 - e(1); e(2) = mu * f (2);
    for j = 3 : N
        m1 = j - 1; m2 = j - 2;
        d = a3 - mu * e(m1) - f (m2);
        f (j) = 1/d;
        x (j) = f (j) * (lam * y (j) + mu * x (m1) - x (m2));
        mu = 4 - e(m1);
        e(j) = mu * f (j);
    end
    mu = 4 - elim;
    for j = N + 1 : n - 2
        x (j) = film * (lam * y (j) + mu * x (j - 1) - x (j - 2));
    end
    d = a2 - mu * elim - film; f (N + 1) = 1/d;
    x (n - 1) = f (N + 1) * (lam * y (n - 1) + mu * x (n - 2) - x (n - 3));
    mu = 2 - elim; e(N + 1) = mu * f (N + 1);
    d = a1 - mu * e(N + 1) - film; f (N + 2) = 1/d;
    x (n) = f (N + 2) * (lam * y (n) + mu * x (n - 1) - x (n - 2));

    %Solve the second triangular system and find avg squared error
```

end
                    d = a2 - mu * elim - film; f(N + 1) = 1/d;
                    x(n - 1) = f(N + 1) * (lam * y(n - 1) + mu * x(n - 2) - x(n - 3));
                    mu = 2 - elim; e(N + 1) = mu * f(N + 1);
                    d = a1 - mu * e(N + 1) - film; f(N + 2) = 1/d;
                    x(n) = f(N + 2) * (lam * y(n) + mu * x(n - 1) - x(n - 2));

                    %Solve the second triangular system and find avg squared error

                    sq = (y(n) - x(n))^2;
                    x(n - 1) = x(n - 1) + e(N + 1) * x(n);
                    sq = sq + (y(n - 1) - x(n - 1))^2;
                    for j = n - 2 : -1 : N + 1
                        x(j) = x(j) + elim * x(j + 1) - film * x(j + 2);
                        sq = sq + (y(j) - x(j))^2;
                    end
                    for j = N : -1 : 1
                        x(j) = x(j) + e(j) * x(j + 1) - f(j) * x(j + 2);
                        sq = sq + (y(j) - x(j))^2;
                    end
                    sq = sq/n;

                    %Compute GCV score

                    g2 = f(N + 2); tr = g2; h = e(N + 1) * g2;
                    g1 = f(N + 1) + e(N + 1) * h; tr = tr + g1;
                    for k = n - 2 : -1 : n - N + 1
                        q = elim * h - film * g2;
                        h = elim * g1 - film * h; g2 = g1;
                        g1 = film + elim * h - film * q;
                        tr = tr + g1;
                    end
                    tr = tr + (nc - N) * glim;
                    tr = (2 * tr - rem(n, 2) * glim) * lam / n;
                    score = sq/(1 - tr)^2;

                References

                Aitken, A.C., 1925. On the theory of gradation. Proc. Roy. Soc. Edinburgh 46, 36-45.
                Bauer, FL., 1954. Bethetrage zurntwirtschaftung numerischer verfächremgesteuerte rechene
```

<!-- END SOURCE 37/40: Weinert_2007_efficient-whittaker-henderson-smoothing.md -->

---

<!-- BEGIN SOURCE 38/40: Welch_2008_equity-premium-prediction.md -->

# Source: `Welch_2008_equity-premium-prediction.md`

---
id: "Welch_2008_equity-premium-prediction"
source_pdf: "../pdf/Welch_2008_equity-premium-prediction.pdf"
source_filename: "Welch_2008_equity-premium-prediction.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/Welch_2008_equity-premium-prediction.references.md"
---

<!-- p:1 -->

## A Comprehensive Look at The Empirical Performance of Equity Premium Prediction

### Ivo Welch

Brown University Department of Economics NBER

### Amit Goyal

Emory University Goizueta Business School

Our article comprehensively reexamines the performance of variables that have been suggested by the academic literature to be good predictors of the equity premium. We find that by and large, these models have predicted poorly both in-sample (IS) and out-of-sample (OOS) for 30 years now; these models seem unstable, as diagnosed by their out-of-sample predictions and other statistics; and these models would not have helped an investor with access only to available information to profitably time the market. ( JEL G12, G14)

Attempts to predict stock market returns or the equity premium have a long tradition in finance. As early as 1920, Dow (1920) explored the role of dividend ratios. A typical specification regresses an independent lagged predictor on the stock market rate of return or, as we shall do, on the equity premium,

$$E q u i t y \, \text {Premium} ( t ) \, = \, \gamma _ { 0 } \, + \, \gamma _ { 1 } \times x ( t - 1 ) + \epsilon ( t ) . \quad ( 1 )$$

γ 1 is interpreted as a measure of how significant x is in predicting the equity premium. The most prominent x variables explored in the literature are the dividend price ratio and dividend yield, the earnings price ratio and dividend-earnings (payout) ratio, various interest rates and spreads, the inflation rates, the book-to-market ratio, volatility, the investment-capital ratio, the consumption, wealth, and income ratio, and aggregate net or equity issuing activity.

The literature is difficult to absorb. Different articles use different techniques, variables, and time periods. Results from articles that were written years ago may change when more recent data is used. Some articles

Thanks to Malcolm Baker, Ray Ball, John Campbell, John Cochrane, Francis Diebold, Ravi Jagannathan, Owen Lamont, Sydney Ludvigson, Rajnish Mehra, Michael Roberts, Jay Shanken, Samuel Thompson, Jeff Wurgler, and Yihong Xia for comments, and Todd Clark for providing us with some critical McCracken values. We especially appreciate John Campbell and Sam Thompson for challenging our earlier drafts, and iterating mutually over working papers with opposite perspectives. Address correspondence to Amit Goyal, http://www.goizueta.emory.edu/agoyal E-mail: mailto:amit goyal@bus.emory.edu http://welch.econ.brown.edu E-mail: mailto:ivo welch@ brown.edu, or e-mail: amit goyal@bus.emory.edu.



The Author 2007.

Published by Oxford University Press on behalf of The Society for Financial Studies.

All rights reserved. For Permissions, please email: journals.permissions@oxfordjournals.org.

doi:10.1093/rfs/hhm014

Advance Access publication March 17, 2007


<!-- p:2 -->


contradict the findings of others. Still, most readers are left with the impression that ''prediction works''-though it is unclear exactly what works. The prevailing tone in the literature is perhaps best summarized by Lettau and Ludvigson (2001, p.842)

''It is now widely accepted that excess returns are predictable by variables such as dividend-price ratios, earnings-price ratios, dividend-earnings ratios, and an assortment of other financial indicators.''

Therearealsoahealthynumberofcurrentarticlethatfurthercementthis perspective and a large theoretical and normative literature has developed that stipulates how investors should allocate their wealth as a function of the aforementioned variables.

The goal of our own article is to comprehensively re-examine the empirical evidence as of early 2006, evaluating each variable using the same methods (mostly, but not only, in linear models), time-periods, and estimation frequencies. The evidence suggests that most models are unstable or even spurious. Most models are no longer significant even insample (IS), and the few models that still are usually fail simple regression diagnostics. Most models have performed poorly for over 30 years IS. For many models, any earlier apparent statistical significance was often based exclusively on years up to and especially on the years of the Oil Shock of 1973-1975. Most models have poor out-of-sample (OOS) performance, but not in a way that merely suggests lower power than IS tests. They predict poorly late in the sample, not early in the sample. (For many variables, we have difficulty finding robust statistical significance even when they are examined only during their most favorable contiguous OOS sub-period.) Finally, the OOS performance is not only a useful model diagnostic for the IS regressions but also interesting in itself for an investor who had sought to use these models for market-timing. Our evidence suggests that the models would not have helped such an investor.

Therefore, although it is possible to search for, to occasionally stumble upon, and then to defend some seemingly statistically significant models, we interpret our results to suggest that a healthy skepticism is appropriate when it comes to predicting the equity premium, at least as of early 2006. The models do not seem robust.

Our article now proceeds as follows. We describe our data-available at the RFSwebsite-inSection 1andourtestsinSection 2.Section 3explores our base case-predicting equity premia annually using OLS forecasts. In Sections 4 and 5, we predict equity premia on 5-year and monthly horizons, the latter with special emphasis on the suggestions in Campbell and Thompson (2005). Section 6 tries earnings and dividend ratios with longer memory as independent variables, corrections for persistence in regressors, and encompassing model forecasts. Section 7 reviews earlier literature. Section 8 concludes.


<!-- p:3 -->


## 1. Data Sources and Data Construction

Our dependent variable is always the equity premium, that is, the total rate of return on the stock market minus the prevailing short-term interest rate.

Stock Returns : We use S&amp;P 500 index returns from 1926 to 2005 from Center for Research in Security Press (CRSP) month-end values. Stock returns are the continuously compounded returns on the S&amp;P 500 index, including dividends. For yearly and longer data frequencies, we can go back as far as 1871, using data from Robert Shiller's website. For monthly frequency, we can only begin in the CRSP period, that is, 1927.

Risk-free Rate : The risk-free rate from 1920 to 2005 is the Treasury-bill rate. Because there was no risk-free short-term debt prior to the 1920s, we had to estimate it. Commercial paper rates for New York City are from the National Bureau of Economic Research (NBER) Macrohistory data base. These are available from 1871 to 1970. We estimated a regression from 1920 to 1971, which yielded

Treasury-bill rate = - 0 . 004 + 0 . 886 × Commercial Paper Rate , (2)

with an R 2 of 95.7%. Therefore, we instrumented the risk-free rate from 1871 to 1919 with the predicted regression equation. The correlation for the period 1920 to 1971 between the equity premium computed using the actual Treasury-bill rate and that computed using the predicted Treasury-bill rate (using the commercial paper rate) is 99.8%.

The equity premium had a mean (standard deviation) of 4.85% (17.79%) over the entire sample from 1872 to 2005; 6.04% (19.17%) from 1927 to 2005; and 4.03% (15.70%) from 1965 to 2005.

Our first set of independent variables are primarily stock characteristics: Dividends : Dividends are 12-month moving sums of dividends paid on the S&amp;P 500 index. The data are from Robert Shiller's website from 1871 to 1987. Dividends from 1988 to 2005 are from the S&amp;P Corporation. The Dividend Price Ratio ( d/p ) is the difference between the log of dividends and the log of prices. The Dividend Yield ( d/y ) is the difference between the log of dividends and the log of lagged prices. [See, e.g., Ball (1978), Campbell (1987), Campbell and Shiller (1988a, 1988b), Campbell and Viceira (2002), Campbell and Yogo (2006), the survey in Cochrane (1997), Fama and French (1988), Hodrick (1992), Lewellen (2004), Menzly, Santos, and Veronesi (2004), Rozeff (1984), and Shiller (1984).]

Earnings : Earnings are 12-month moving sums of earnings on the S&amp;P 500 index. The data are again from Robert Shiller's website from 1871 to 1987. Earnings from 1988 to 2005 are our own estimates based on interpolation of quarterly earnings provided by the S&amp;P Corporation. The Earnings Price Ratio ( e/p ) is the difference between the log of earnings and the log of prices. (We also consider variations, in which we explore multiyear moving averages of numerator or denominator, e.g., as in e 10 /p , which is the moving ten-year average of earnings divided by price.) The Dividend Payout Ratio ( d/e ) is the difference between the log of dividends and the log of earnings. [See, e.g., Campbell and Shiller (1988a, 1998) and Lamont (1998).]


<!-- p:4 -->


Stock Variance (svar) : Stock Variance is computed as sum of squared daily returns on the S&amp;P 500. G. William Schwert provided daily returns from 1871 to 1926; data from 1926 to 2005 are from CRSP. [See Guo (2006).]

Cross-Sectional Premium (csp) : The cross-sectional beta premium measures the relative valuations of highand low-beta stocks and is proposed in Polk, Thompson, and Vuolteenaho (2006). The csp data are from Samuel Thompson from May 1937 to December 2002.

Book Value : Bookvalues from 1920 to 2005 are from Value Line's website, specifically their Long-Term Perspective Chart of the Dow Jones Industrial Average. The Book-to-Market Ratio ( b/m ) is the ratio of book value to market value for the Dow Jones Industrial Average. For the months from March to December, this is computed by dividing book value at the end of the previous year by the price at the end of the current month. For the months of January and February, this is computed by dividing book value at the end of two years ago by the price at the end of the current month. [See, e.g, Kothari and Shanken (1997) and Pontiff and Schall (1998).]

Corporate Issuing Activity : We entertain two measures osf corporate issuing activity. Net Equity Expansion ( ntis ) is the ratio of 12-month moving sums of net issues by NYSE listed stocks divided by the total end-of-year market capitalization of NYSE stocks. This dollar amount of net equity issuing activity (IPOs, SEOs, stock repurchases, less dividends) for NYSE listed stocks is computed from CRSP data as

$$\text {Net Issue} _ { t } \, = \, \text {Mcap} _ { t } - \text {Mcap} _ { t - 1 } \times ( 1 + v w r e t x _ { t } ) , \quad ( 3 )$$

where Mcap is the total market capitalization, and vwretx is the value weighted return (excluding dividends) on the NYSE index. 1 These data are available from 1926 to 2005. ntis is closely related, but not identical, to a variable proposed in Boudoukh, Michaely, Richardson, and Roberts (2007). The second measure, Percent Equity Issuing ( eqis ), is the ratio of equity issuing activity as a fraction of total issuing activity. This is the variable proposed in Baker and Wurgler (2000). The authors provided us with the data, except for 2005, which we added ourselves. The first equity issuing measure is relative to aggregate market cap, while the second is relative to aggregate corporate issuing.

1 This calculation implicitly assumes that the delisting return is - 100 percent. Using the actual delisting return, where available, or ignoring delistings altogether, has no impact on our results.


<!-- p:5 -->


Our next set of independent variables is interest-rate related:

Treasury Bills (tbl) : Treasury-bill rates from 1920 to 1933 are the U.S. Yields On Short-Term United States Securities, Three-Six Month Treasury Notes and Certificates, Three Month Treasury series in the NBER Macrohistory data base. Treasury-bill rates from 1934 to 2005 are the 3Month Treasury Bill: Secondary Market Rate from the economic research data base at the Federal Reserve Bank at St. Louis (FRED. [See, e.g., Campbell (1987) and Hodrick (1992).]

Long Term Yield (lty) : Our long-term government bond yield data from 1919 to 1925 is the U.S. Yield On Long-Term United States Bonds series in the NBER's Macrohistory data base. Yields from 1926 to 2005 are from Ibbotson's Stocks, Bonds, Bills and Inflation Yearbook , the same source that provided the Long Term Rate of Returns ( ltr ). The Term Spread ( tms ) is the difference between the long term yield on government bonds and the Treasury-bill. [See, e.g., Campbell (1987) and Fama and French (1989).]

Corporate Bond Returns : Long-term corporate bond returns from 1926 to 2005 are again from Ibbotson's Stocks, Bonds, Bills and Inflation Yearbook . Corporate Bond Yields on AAA and BAA-rated bonds from 1919 to 2005 are from FRED. The Default Yield Spread ( dfy ) is the difference between BAA and AAA-rated corporate bond yields . The Default Return Spread ( dfr ) is the difference between long-term corporate bond and long-term government bond returns . [See, e.g., Fama and French (1989) and Keim and Stambaugh (1986).]

Inflation (infl) : Inflation is the Consumer Price Index (All Urban Consumers) from 1919 to 2005 from the Bureau of Labor Statistics. Because inflation information is released only in the following month, we wait for one month before using it in our monthly regressions. [See, e.g., Campbell and Vuolteenaho (2004), Fama (1981), Fama and Schwert (1977), and Lintner (1975).]

Like inflation, our next variable is also a common broad macroeconomic indicator.

Investment to Capital Ratio (i/k) : The investment to capital ratio is the ratio of aggregate (private nonresidential fixed) investment to aggregate capital for the whole economy. This is the variable proposed in Cochrane (1991). John Cochrane kindly provided us with updated data.

Of course, many articles explore multiple variables. For example, Ang and Bekaert (2003) explore both interest rate and dividend related variables. In addition to simple univariate prediction models, we also entertain two methods that rely on multiple variables ( all and ms ), and two models that are rolling in their independent variable construction ( cay and ms ).


<!-- p:6 -->


A ''Kitchen Sink'' Regression (all): This includes all the aforementioned variables. (It does not include cay , described below, partly due to limited data availability of cay .)

Consumption, wealth, income ratio (cay): Lettau and Ludvigson (2001) estimate the following equation:

$$c _ { t } \, = \alpha + \beta _ { a } \cdot & a _ { t } + \beta _ { y } \cdot y _ { t } + \sum _ { i = - k } ^ { k } b _ { a , i } \cdot \Delta a _ { t - i } \\ & + \sum _ { i = - k } ^ { k } b _ { y , i } \cdot \Delta y _ { t - i } + \epsilon _ { t } , \quad t = k + 1 , \dots , T - k , \quad ( 4 ) \\ \text {where } c \text { is the aggregate consumption, } a \text { is the aggregate health, and }$$

where c is the aggregate consumption, a is the aggregate wealth, and y is the aggregate income. Using estimated coefficients from the above equation provides cay ≡ ̂ cay t = ct - ˆ β a · at - ˆ β y · yt , t = 1 , . . . , T . Note that, unlike the estimation equation, the fitting equation does not use look-ahead data. Eight leads/lags are used in quarterly estimation ( k = 8) while two lags are used in annual estimation ( k = 2). [For further details, see Lettau and Ludvigson (2001).] Data for cay 's construction are available from Martin Lettau's website at quarterly frequency from the second quarter of 1952 to the fourth quarter of 2005. Although annual data from 1948 to 2001 is also available from Martin Lettau's website, we reconstruct the data following their procedure as this allows us to expand the time-series from 1945 to 2005 (an addition of 7 observations).

BecausetheLettau-Ludvigsonmeasureof cay is constructed using lookahead (in-sample) estimation regression coefficients, we also created an equivalent measure that excludes advance knowledge from the estimation equation and thus uses only prevailing data. In other words, if the current time period is ' s ', then we estimated Equation (4) using only the data up to ' s ' through

$$c _ { t } \, = \alpha + \beta _ { a } ^ { s } \cdot a _ { t } + \beta _ { y } ^ { s } \cdot y _ { t } + \sum _ { i = - k } ^ { k } b _ { a , i } ^ { s } \cdot \Delta a _ { t - i } \\ + \sum _ { i = - k } ^ { k } b _ { y , i } ^ { s } \cdot \Delta y _ { t - i } + \epsilon _ { t } , \, t = k + 1 , \dots , s - k , \quad ( 5 ) \\ \text {This measure is called caya ( ``ante'')} \, to distinguish it from the traditional}$$

This measure is called caya (''ante'') to distinguish it from the traditional variable cayp constructed with look-ahead bias (''post''). The superscript on the betas indicates that these are rolling estimates, that is, a set of coefficients used in the construction of one caya S measure in one period.

A model selection approach, named '' ms .'' If there are K variables, we consider 2 K models essentially consisting of all possible combinations of variables. (As with the kitchen sink model, cay is not a part of the ms selection.) Every period, we select one of these models that gives the minimum cumulative prediction errors up to time t . This method is based on Rissanen (1986) and is recommended by Bossaerts and Hillion (1999). Essentially, this method uses our criterion of minimum OOS prediction errors to choose among competing models in each time period t . This is also similar in spirit to the use of a more conventional criterion (like R 2 ) in Pesaran and Timmermann (1995) (who do not entertain our NULL hypothesis). This selection model also shares a certain flavor with our encompassing tests in Section 6, where we seek to find an optimal rolling combination between each model and an unconditional historical equity premium average, and with the Bayesian model selection approach in Avramov (2002).


<!-- p:7 -->


The latter two models, cay and ms , are revised every period, which render IS regressions problematic. This is also why we did not include caya in the kitchen sink specification.

## 2. Empirical Procedure

Our base regression coefficients are estimated using OLS, although statistical significance is always computed from bootstrapped F -statistics (taking correlation of independent variables into account).

OOSstatistics: The OOS forecast uses only the data available up to the time at which the forecast is made. Let eN denote the vector of rolling OOS errors from the historical mean model and eA denote the vector of rolling OOS errors from the OLS model. Our OOS statistics are computed as

$$O O S \, \text {errors from the OLS model. Our OOS statistics are computed as} \\ R ^ { 2 } = 1 - \frac { \text {MSE} _ { A } } { \text {MSE} _ { N } } , \quad \overline { R } ^ { 2 } \, = R ^ { 2 } - ( 1 - R ^ { 2 } ) \times \left ( \frac { T - k } { T - 1 } \right ) , \\ \Delta R M S E = \sqrt { \text {MSE} _ { N } } \, - \, \sqrt { \text {MSE} _ { A } } , \\ \text {MSE-F} = ( T - h + 1 ) \times \left ( \frac { \text {MSE} _ { N } - \text {MSE} _ { A } } { \text {MSE} _ { A } } \right ) , \quad ( 6 ) \\ \text {where } h \text { is the degree of overlap } ( h = 1 \text { for } n \text { overland} ) \, \text { MSE-F is}$$

where h is the degree of overlap ( h = 1 for no overlap). MSE-F is McCracken's(2004) F -statistic. It tests for equal MSE of the unconditional forecast and the conditional forecast (i.e., Delta1 MSE = 0). 2 We generally do not report MSE-F statistics, but instead use their bootstrapped critical levels to provide statistical significance levels via stars in the tables.

2 Our earlier drafts also entertained another performance metric, the mean absolute error difference Delta1 MAE. The results were similar. These drafts also described another OOS-statistic, MSE-T = √ T + 1 - 2 · h + h · (h - 1 )/T · [ d ̂ se ( d ) ] , where dt = e Nt - e At , and d = T - 1 · ∑ T t dt = MSE N - MSE A over the entire OOS period, and T is the total number of forecast observations. This is the Diebold and Mariano (1995) t -statistic modified by Harve, Leybourne, and Newbold (1997). (We still use the latter as bounds in our plots, because we know the full distribution.) Again, the results were similar. We chose to use the MSE-F in this article because Clark and McCracken (2001) find that MSE-F has higher power

than MSE-T.


<!-- p:8 -->


For our encompassing tests in Section 6, we compute

$$\text {ENC} = \frac { T - h + 1 } { T } \, \times \, \frac { \sum _ { t = 1 } ^ { T } \left ( e _ { N _ { t } } ^ { 2 } - e _ { N _ { t } } \cdot e _ { A _ { t } } \right ) } { \text {MSE} _ { A } } ,$$

which is proposed by Clark and McCracken (2001). They also show that the MSE-F and ENC statistics follow nonstandard distributions when testing nested models, because the asymptotic difference in squared forecast errors is exactly 0 with 0 variance under the NULL, rendering the standard distributions asymptotically invalid. Because our models are nested, we could use asymptotic critical values for MSE tests provided by McCracken, and asymptotic critical values for ENC tests provided by Clark and McCracken. However, because we use relatively small samples, because our independent variables are often highly serially correlated, and especially because we need critical values for our 5-year overlapping observations (for which asymptotic critical values are not available), we obtain critical values from the bootstrap procedure described below. (The exceptions are that critical values for caya , cayp , and all models are not calculated using a bootstrap, and critical values for ms model are not calculated at all.) The NULL hypothesis is that the unconditional forecast is not inferior to the conditional forecast, so our critical values for OOS test are for a one-sided test (critical values of IS tests are, as usual, based on two-sided tests). 3

Bootstrap : Our bootstrap follows Mark (1995) and Kilian (1999) and imposes the NULL of no predictability for calculating the critical values. In other words, the data generating process is assumed to be

$$y _ { t + 1 } & = \alpha & + u _ { 1 t + 1 } \\ x _ { t + 1 } & = \mu + \rho \times x _ { t } + u _ { 2 t + 1 } . \\$$

The bootstrap for calculating power assumes the data generating process is

$$y _ { t + 1 } & = \alpha + \beta \times x _ { t } + u _ { 1 t + 1 } \\ x _ { t + 1 } & = \mu + \rho \times x _ { t } + u _ { 2 t + 1 } , \\$$

where both β and ρ are estimated by OLS using the full sample of observations, with the residuals stored for sampling. We then generate

3 If the regression coefficient β is small (so that explanatory power is low or the IS R 2 is low), it may happen that our unconditional model outperforms on OOS because of estimation error in the rolling estimates of β . In this case, Delta1 RMSE might be negative but still significant because these tests are ultimately tests of whether β is equal to zero .


<!-- p:9 -->


10,000 bootstrapped time series by drawing with replacement from the residuals. The initial observation-preceding the sample of data used to estimate the models-is selected by picking one date from the actual data at random. This bootstrap procedure not only preserves the autocorrelation structure of the predictor variable, thereby being valid under the Stambaugh (1999) specification, but also preserves the cross-correlation structure of the two residuals. 4

Statistical Power: Our article entertains both IS and OOS tests. Inoue and Kilian (2004) show that the OOS tests used in this paper are less powerful than IS tests, even though their size properties are roughly the same. Similar critiques of the OOS tests in our article have been noted by Cochrane (2005) and Campbell and Thompson (2005). We believe this is the wrong way to look at the issue of power for two reasons:

- (i) It is true that under a well-specified, stable underlying model, an IS OLS estimator is more efficient. Therefore, a researcher who has complete confidence in her underlying model specification (but not the underlying model parameters) should indeed rely on IS tests to establish significance-the alternative to OOS tests does have lower power. However, the point of any regression diagnostics, such as those for heteroskedasticity and autocorrelation, is always to subject otherwise seemingly successful regression models to a number of reasonable diagnostics when there is some model uncertainty. Relative to not running the diagnostic, by definition, any diagnostic that can reject the model at this stage sacrifices power if the specified underlying model is correct. In our forecasting regression context, OOS performance just happens to be one natural and especially useful diagnostic statistic. It can help determine whether a model is stable and wellspecified, or changing over time, either suddenly or gradually. This also suggests why the simple power experiment performed in some of the aforementioned critiques of our own paper is wrong. It is unreasonable to propose a model if the IS performance is insignificant, regardless of its OOS performance. Reasonable (though not necessarily statistically significant) OOS performance is not a substitute, but a necessary complement for IS performance in order to establish the quality of the underlying model specification. The thought experiments and analyses in the critiques, which simply compare the power of OOS tests to that of IS tests, especially under their assumption of a correctly

specified stable model, is therefore incorrect. The correct power experiment instead should explore whether conditional on observed IS significance , OOS diagnostics are reasonably powerful. We later show that they are.

4 We do not bootstrap for cayp because it is calculated using ex-post data; for caya and ms because these variables change each period; and for all because of computational burden.


<!-- p:10 -->


Not reported in the tables, we also used the CUSUMQ test to test for model stability. Although this is a weak test, we can reject stability for all monthly models: and for all annual models except for ntis , i/k , and cayp , when we use data beginning in 1927. Thus, the CUSUMQ test sends the same message about the models as the findings that we shall report.

- (ii) All of the OOS tests in our paper do not fail in the way the critics suggest. Low-power OOS tests would produce relatively poor predictions early and relatively good predictions late in the sample. Instead, all of our models show the opposite behavior-good OOS performance early, bad OOS performance late.
- A simple alternative OOS estimator, which downweights early OOSpredictions relative to late OOS predictions, would have more power than our unweighted OOS prediction test. Such a modified it would show that all models explored in our article perform even worse. (We do not use it only to keep it simple and to avoid a ''cherry-picking-the-test''

estimator would both be more powerful, and critique.)

Estimation Period : It is not clear how to choose the periods over which a regression model is estimated and subsequently evaluated. This is even more important for OOS tests. Although any choice is necessarily ad-hoc in the end, the criteria are clear. It is important to have enough initial data to get a reliable regression estimate at the start of evaluation period, and it is important to have an evaluation period that is long enough to be representative. We explore three time period specifications: the first begins OOS forecasts 20 years after data are available; the second begins OOS forecast in 1965 (or 20 years after data are available, whichever comes later); the third ignores all data prior to 1927 even in the estimation. 5 If a variable does not have complete data, some of these time-specifications can overlap. Using three different periods reflects different trade-offs between the desire to obtain statistical power and the desire to obtain results that remain relevant today. In our graphical analysis later, we also evaluate the rolling predictive performance of variables. This analysis helps us identify periods of superior or inferior performance and can be seen as invariant to the choice of the OOS evaluation period (though not to the choice of the estimation period).

5 We also tried estimating our models only with data after World War II, as recommended by Lewellen (2004). Some properties in some models change, especially when it comes to statistical significance and the importance of the Oil Shock for one variable, d/p . However, the overall conclusions of our article remain.


<!-- p:11 -->


## 3. Annual Prediction

Table 1 shows the predictive performance of the forecasting models on annual forecasting horizons. Figures 1 and 2 graph the IS and OOS performance of variables in Table 1. For the IS regressions, the performance is the cumulative squared demeaned equity premium minus the cumulative squared regression residual. For the OOS regressions, this is the cumulative squared prediction errors of the prevailing mean minus the cumulative squared prediction error of the predictive variable from the linear historical regression. Whenever a line increases, the ALTERNATIVE predicted better; whenever it decreases, the NULL predicted better. The units in the graphs are not intuitive, but the timeseries pattern allows diagnosis of years with good or bad performance. Indeed, the final Delta1 SSE statistic in the OOS plot is sign-identical with the Delta1 RMSE statistic in our tables. The standard error of all the observations in the graphs is based on translating MSE-T statistic into symmetric 95% confidence intervals based on the McCracken (2004) critical values; the tables differ in using the MSE-F statistic instead.

The reader can easily adjust perspective to see how variations in starting or ending date would impact the conclusion-by shifting the graph up or down (redrawing the y = 0 horizontal zero line). Indeed, a horizontal line and the right-side scale indicate the equivalent zero-point for the second time period specification, in which we begin forecasts in 1965 (this is marked ''Start = 1965 Zero Val'' line). The plots have also vertically shifted the IS errors, so that the IS line begins at zero on the date of our first OOS prediction. The Oil Shock recession of 1973 to 1975, as identified by the NBER, is marked by a vertical (red) bar in the figures. 6

In addition to the figures and tables, we also summarize models' performances in small in-text summary tables, which give the ISR 2 and OOSR 2 for two time periods: the most recent 30 years and the entire sample period. The R 2 for the subperiod is not the R 2 for a different model estimated only over the most recent three decades, but the residual fit for the overall model over the subset of data points (e.g., computed simply as 1-SSE/SST for the last 30 years' residuals). The most recent three decades after the Oil Shock can help shed light on whether a model is likely to still perform well nowadays. Generally, it is easiest to understand the data by looking first at the figures, then at the in-text table, and finally at the full table.

A well-specified signal would inspire confidence in a potential investor if it had Explanation: These figures plot the IS and OOS performance of annual predictive regressions. Specifically, these are the cumulative squared prediction errors of the NULL minus the cumulative squared prediction error of the ALTERNATIVE. The ALTERNATIVE is a model that relies on predictive variables noted in each graph. The NULL is the prevailing equity premium mean for the OOS graph, and the full-period equity premium mean for the IS graph. The IS prediction relative performance is dotted (and usually above), the OOS prediction relative perfomance is solid. An increase in a line indicates better performance of the named model; a decrease in a line indicates better performance of the NULL. The blue band is the equivalent of 95% two-sided levels, based on MSE-T critical values from McCracken (2004). (MSE-T is the Diebold and Mariano (1995) t -statistic modified by Harvey, Leybourne, and Newbold (1998)). The right axis shifts the zero point to 1965. The Oil Shock is marked by a red vertical line.

6 The actual recession period was from November 1973 to March 1975. We treat both 1973 and 1975 as years of Oil Shock recession in annual prediction.


<!-- p:12 -->


Figure 1

Annual performance of IS insignificant predictors.

Year

02

10

02

10

02

10

<!-- p:13 -->


Figure 1 Continued

Year Year


<!-- p:14 -->


02

Figure 1 Continued

<!-- p:15 -->


Figure 1 Continued

Year Table 1 Forecasts at annual frequency This table presents statistics on forecast errors in-sample (IS) and out-of-sample (OOS) for log equity premium forecasts at annual frequency (both in the forecasting equation and forecast). Variables are explained in Section 2. Stock returns are price changes, including dividends, of the S&amp;P500. All numbers are in percent per year, except except R 2 and power which are simple percentages. A star next to ISR 2 denotes significance of the in-sample regression as measured by F -statistics (critical values of which are obtained empirically from bootstrapped distributions). The column 'IS for OOS' gives the ISR 2 for the OOS period. Delta1 RMSE is the RMSE (root mean square error) difference between the unconditional forecast and the conditional forecast for the same sample/forecast period. Positive numbers signify superior out-of-sample conditional forecast. The OOSR 2 is defined in Equation 6. A star next to OOSR 2 is based on significance of MSE-F statistic by McCracken (2004), which tests for equal MSE of the unconditional forecast and the conditional forecast. One-sided critical values of MSE statistics are obtained empirically from bootstrapped distributions, except for caya and all models where they are obtained from McCracken (2004). Critical values for the ms model are not calculated. Power is calculated as the fraction of draws where the simulated Delta1 RMSE is greater than the empirically calculated 95% critical value. The two numbers under the power column are for all simulations and for those simulations in which the in-sample estimate was significant at the 95% level. Significance levels at 90%, 95%, and 99% are denoted by one, two, and three stars, respectively.


<!-- p:16 -->


| 1927-2005 Sample IS R 2               | - 1.31 - 0.99 - 1.32 - 1.24 - 0.94 0.89 0.15 0.32 1.67 2.71 * 0.92 3.20 *                                                                                                               |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| begin 1965 OOS Delta1 RMSE Power      | - 0.12 - 0.08 + 0.01 - 0.18 - 0.76 - 0.03 - 0.18 - 0.02 - 0.09 - 0.31 - 1.18 0.11                                                                                                       |
| Forecasts IS for OOS R 2 R 2          | - 4.15 - 3.56 - 2.44 - 4.99 - 12.57 - 2.96 - 4.90 - 2.82 - 3.69 - 6.68 - 18.38 - 1.10                                                                                                   |
| years after OOS R 2 Delta1 RMSE Power | - 3.29 - 0.14 - 4.07 - 0.20 - 27.14 - 2.33 - 4.33 - 0.31 - 7.72 - 0.47 - 2.42 - 0.07 - 3.37 - 0.14 - 2.16 - 0.03 - 2.06 - 0.11 - 1.93 - 0.10 - 11.79 - 0.76 - 1.78 - 0.08               |
| IS 2                                  | - 1.18 - 1.00 - 0.76 - 0.75 - 0.63 0.16 0.34 0.40 0.49 0.91 0.99 1.08                                                                                                                   |
| Variable                              | Default yield Inflation Stock variance Dividend payout Long term yield Term spread Treasury-bill rate Default return Dividend price Dividend yield Long term return Earning price ratio |
|                                       | dfy infl svar d/e lty tms tbl dfr d/p d/y ltr                                                                                                                                           |
|                                       | Significant IS spread 1919-2005 1919-2005 1885-2005 ratio 1872-2005 1919-2005 1920-2005 1920-2005 spread 1926-2005 ratio 1872-2005 1872-2005 1926-2005 1872-2005                        |
| IS for R OOS R 2                      |                                                                                                                                                                                         |
| Data                                  |                                                                                                                                                                                         |
| Not                                   |                                                                                                                                                                                         |
|                                       | e/p                                                                                                                                                                                     |
| Sample,                               |                                                                                                                                                                                         |
| Full                                  | Full                                                                                                                                                                                    |


<!-- p:17 -->


Table 1

| 1927-2005                         | Sample IS R 2   | 4.14 * Same Same Same Same                                                 | Same Same Same                                      | Full Sample 0.91 1.08 3.20 *               |
|-----------------------------------|-----------------|----------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------------|
| begin 1965                        | OOS Power       | 40 (61) 53 (72) 66 (77) - (-)                                              | - (-)                                               | 30 (71) 39 (64) 45 (64)                    |
| Forecasts                         | Delta1 RMSE     | - 0.77 Same - 0.32 + 0.12 - 6.19                                           | Same Same - 1.79                                    | - 0.30 - 0.05 - 1.26                       |
|                                   | R 2             | - 12.71 - 6.79 - 1.00 - 176.18                                             | - 23.71                                             | - 6.44 - 3.15 - 19.46                      |
|                                   | IS for OOS R 2  | - 7.29 0.96 3.64 - 20.91                                                   | -                                                   | - 0.35 - 0.94 - 8.65                       |
| Full Sample 20 years after sample | Power           | 42 (67) 47 (77) 57 (78) 72 (85) - (-)                                      | - (-) - (-) - (-)                                   |                                            |
| OOS                               | Delta1 RMSE     | - 0.01 0.07 - 0.26 0.30 - 5.97                                             | 1.61 - 0.14 - 1.69                                  |                                            |
| begin                             | R 2             | - 1 . 72 - 1 . 77 - 5 . 07 2 . 04 ** - 139 . 03                            | 16 . 78 *** - 4 . 33 - 22 . 50                      |                                            |
| Forecasts IS for                  | OOS R 2         | 1.13 - 0.25 - 4.21 2.81 2.62                                               | (cayp) 20.70 - -                                    |                                            |
| IS                                | R 2             | 3.20 * 6.63 ** 8.15 *** 9.15 *** 13.81 **                                  | Information 15.72 *** - -                           | 2.71 * 3.20 * 4.14 *                       |
|                                   | Data            | 1921-2005 1947-2005 1927-2005 1927-2005 1927-2005                          | (caya, ms) or Ex-Post 1945-2005 1945-2005 1927-2005 | 1927-2005 1927-2005 1927-2005              |
|                                   | Variable IS     | ratio expansion                                                            | equivalent incme incme                              | Significant IS yield price ratio to market |
|                                   | Significant     | Book to market Invstmnt capital Net equity Pct equity issuing Kitchen sink | no IS Cnsmptn, wlth, Cnsmptn, wlth, Model selection | Sample, Dividend Earning Book              |
| Continued                         | Full Sample,    | b/m i/k ntis eqis all                                                      | Full sample, cayp caya ms                           | 1927-2005 d/y e/p b/m                      |


<!-- p:18 -->


01

02

01

02

10

Year Year

Figure 2 Annual performance of predictors that are not in-sample significant Explanation: See Figure 1.


<!-- p:19 -->


02

03

02

Figure 2 Continued

<!-- p:20 -->


- (i) both significant IS and reasonably good OOS performance over the entire sample period;
- (ii) a generally upward drift (of course, an irregular one);
- (iii) an upward drift which occurs not just in one short or unusual sample period-say just the two years around the Oil Shock;
- (iv) an upward drift that remains positive over the most recent several decades-otherwise, even a reader taking the long view would have to be concerned with the possibility that the underlying model has drifted.

There are also other diagnostics that stable models should pass (heteroskedasticity, residual autocorrelation, etc.), but we do not explore them in our article.

### 3.1 In-sample insignificant models

As already mentioned, if a model has no IS performance, its OOS performance is not interesting. However, because some of the IS insignificant models are so prominent, and because it helps to understand why they may have been considered successful forecasters in past articles, we still provide some basic statistics and graph their OOS performance. The most prominent such models are the following:

Dividend Price Ratio: Figure 1 shows that there were four distinct periods for the d/p model, and this applies both to IS and OOS performance. d/p had mild underperformance from 1905 to WW II, good performance from WW II to 1975, neither good nor bad performance until the mid-1990s, and poor performance thereafter. The best sample period for d/p was from the mid 1930s to the mid-1980s. For the OOS, it was 1937 to 1984, although over half of the OOS performance was due to the Oil Shock. Moreover, the plot shows that the OOS performance of the d/p regression was consistently worse than the performance of its IS counterpart. The distance between the IS and OOS performance increased steadily until the Oil Shock.

Over the most recent 30 years (1976 to 2005), d/p 's performance is negative both IS and OOS. Over the entire period, d/p underperformed the prevailing mean OOS, too:

|         | Recent   | All   |
|---------|----------|-------|
| d/p     | 30 years | years |
| IS R 2  | - 4.80%  | 0.49% |
| OOS R 2 | 15.14%   | 2.06% |

Dividend Yield : Figure 1 shows that the d/y model's IS patterns look broadly like those of d/p . However, its OOS pattern was much more volatile: d/y predicted equity premia well during the Great Depression (1930 to 1933), the period from World War II to 1958, the Oil Shock of


<!-- p:21 -->


1973-1975, and the market decline of 2000-2002. It had large prediction errors from 1958 to 1965 and from 1995 to 2000, and it had unremarkable performance in other years. The best OOS sample period started around 1925 and ended either in 1957 or 1975. The Oil Shock did not play an important role for d/y . Over the most recent 30 years, d/y 's performance is again negative IS and OOS. The full-sample OOS performance is also again negative:

$$\begin{array} { c c c c } & R e c e n t & & A l l \\ & 3 0 \, y a r s & & y \, O a l \, S \\ I S \ \overline { R } ^ { 2 } & & - 5 . 5 2 \% & & 0 . 9 1 \% \\ & O O S \ R ^ { 2 } & & - 2 0 . 7 9 \% & & - 1 . 9 3 \% \end{array}$$

Earnings Price Ratio : Figure 1 shows that e/p had inferior performance until WW II, and superior performance from WW II to the late 1970s. After the Oil Shock, it had generally nondescript performance (with the exception of the late 1990s and early 2000s). Its best sample period was 1943 to 2002. 2003 and 2004 were bad years for this model. Over the most recent 30 years, e/p 's performance is again negative IS and OOS. The full-sample OOS performance is negative too.

$$\begin{array} { c c c c } & & & & R e c e n t & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

Table 1 shows that these three price ratios are not statistically significant IS at the 90% level. However, some disagreement in the literature can be explained by differences in the estimation period. 7

Other Variables : The remaining plots in Figure 1 and the remaining IS insignificant models in Table 1 show that d/e , dfy , and infl essentially never had significantly positive OOS periods, and that svar had a huge drop in OOS performance from 1930 to 1933. Other variables (that are IS insignificant) often had good sample performance early on, ending somewhere between the Oil Shock and the mid-1980s, followed by poor performance over the most recent three decades. The plots also show that it was generally not just the late 1990s that invalidated them, unlike the case with the aforementioned price ratio models.

7 For example, the final lines in Table 1 show that d/y and e/p had positive and statistically significant IS performance at the 90% level if all data prior to 1927 is ignored. Nevertheless, Table 1 also shows that the OOSR 2 performance remains negative for both of these. Moreover, when the data begins in 1927 and the forecast begins in 1947 (another popular period choice), we find

(Data Begins in 1927) e/p d/y (Forecast Begins in 1947) Recent All Recent All IS R 2 - 3.83% 3.20% - 5.20% 2.71% OOS R 2 - 13.58% 3.41% - 28.05% - 16.65%

Finally, and again not reported in the table, another choice of estimation period can also make a difference. The three price models lost statistical significance over the full sample only in the 1990s. This is not because the ISDelta1 RMSE decreased further in the 1990s, but because the 1991-2005 prediction errors were more volatile, which raised the standard errors of point estimates.


<!-- p:22 -->


In sum, 12 models had insignificant IS full-period performance and, not surprisingly, these models generally did not offer good OOS performance.

### 3.2 In-sample significant models

Five models were significant IS ( b/m , i/k , ntis , eqis , and all ) at least at the 10% two-sided level. Table 1 contains more details for these variables, such as the IS performance during the OOS period, and a power statistic. Together with the plots in Figure 2, this information helps the reader to judge the stability of the models-whether poor OOS performance is driven by less accurately estimated parameters (pointing to lower power), and/or by the fact that the model fails IS and/or OOS during the OOS sample period (pointing to a spurious model).

Book-to-market ratio: b/m is statistically significant at the 6% level IS. Figure 2 shows that it had excellent IS and OOS predictive performance right until the Oil Shock. Both its IS and OOS performance were poor from 1975 to 2000, and the recovery in 2000-2002 was not enough to gain back the 1997-2000 performance. Thus, the b/m model has negative performance over the most recent three decades, both IS and OOS.

|         | Recent   | All   |
|---------|----------|-------|
| b/m     | 30 years | years |
| IS R 2  | - 12.37% | 3.20% |
| OOS R 2 | 29.31%   | 1.72% |

Over the entire sample period, the OOS performance is negative, too. The ''IS for OOS'' R 2 in Table 1 shows how dependent b/m 's performance is on the first 20 years of the sample. The IS R 2 is - 7.29%for the 1965-2005 period. The comparable OOS R 2 even reaches - 12.71%.

As with other models, b/m 's lack of OOS significance is not just a matter of low test power. Table 1 shows that in the OOS prediction beginning in 1941, under the simulation of a stable model, the OOS statistic came out statistically significantly positive in 67% 8 of our (stable-model) simulations in which the IS regression was significant. Not reported in the table, positive performance (significant or insignificant) occurred in 78% of our simulations. A performance as negative as the observed Delta1 RMSEof - 0.01 occurred in none of the simulations.

8 The 42% applies to all simulation draws. It is the equivalent of the experiment conducted in some other articles. However, because OOS performance is relevant only when the IS performance is significant, this is the wrong measure of power.


<!-- p:23 -->


Investment-capital ratio : i/k is statistically significant IS at the 5% level. Figure 2 shows that, like b/m , it performed well only in the first half of its sample, both IS and OOS. About half of its performance, both IS and OOS, occurs during the Oil Shock. Over the most recent 30 years, i/k has underperformed:

|         | Recent   | All   |
|---------|----------|-------|
| i/k     | 30 years | years |
| IS R 2  | - 8.09%  | 6.63% |
| OOS R 2 | 18.02%   | 1.77% |

Corporate Issuing Activity : Recall that ntis measures equity issuing and repurchasing (plus dividends) relative to the price level; eqis measures equity issuing relative to debt issuing. Figure 2 shows that both variables had superior IS performance in the early 1930s, a part of the sample that is not part of the OOS period. eqis continues good performance into the late 1930s but gives back the extra gains immediately thereafter. In the OOS period, there is one stark difference between the two variables: eqis had superior performance during the Oil Shock, both IS and OOS. It is this performance that makes eqis the only variable that had statistically significant OOS performance in the annual data. In other periods, neither variable had superior performance during the OOS period.

Both variables underperformed over the most recent 30 years

|         | ntis Recent - 30 years   | All - years   | eqis Recent - 30 years   | All - years   |
|---------|--------------------------|---------------|--------------------------|---------------|
| IS R 2  | - 5.14%                  | 8.15%         | - 10.36%                 | 9.15%         |
| OOS R 2 | 8.63%                    | 5.07%         | 15.33%                   | 2.04%         |

-


The plot can also help explain dueling perspectives about eqis between Butler, Grullon, and Weston (2005) and Baker, Taliaferro, and Wurgler (2004). One part of their disagreement is whether eqis 's performance is just random underperformance in sampled observations. Of course, some good years are expected to occur in any regression. Yet eqis 's superior performance may not have been so random, because it (i) occurred in consecutive years, and (ii) in response to the Oil Shock events that are often considered to have been exogenous, unforecastable, and unusual. Butler, Grullon, and Weston (2005) also end their data in 2002, while Baker, Taliaferro, and Wurgler (2004) refer to our earlier draft and to Rapach and Wohar (2006), which end in 2003 and 1999, respectively. Our figure shows that small variations in the final year choice can make a difference in whether eqis turns out significant or not. In any case, both articles have good points. We agree with Butler, Grullon, and Weston (2005) that eqis would not have been a profitable and reliable predictor for an external investor, especially over the most recent 30 years. But we also agree with Baker, Taliaferro, and Wurgler (2004) that conceptually, it is not the OOS performance, but the IS performance that matters in the sense in which Baker and Wurgler (2000) were proposing eqis -not as a third-party predictor, but as documentary evidence of the fund-raising behavior of corporations. Corporations did repurchase profitably in the Great Depression and the Oil Shock era (though not in the ''bubble period'' collapse of 2001-2002).


<!-- p:24 -->


all The final model with IS significance is the kitchen sink regression. It had high IS significance, but exceptionally poor OOS performance.

### 3.3 Time-changing models

caya and ms have no IS analogs, because the models themselves are constantly changing.

Consumption-Wealth-Income : Lettau and Ludvigson (2001) construct their cay proxy assuming that agents have some ex-post information. The experiment their study calls OOS is unusual: their representative agent still retains knowledge of the model's full-sample CAYconstruction coefficients. It is OOS only in that the agent does not have knowledge of the predictive coefficient and thus has to update it on a running basis. We call the Lettau and Ludvigson (2001) variable cayp . We also construct caya , which represents a more genuine OOS experiment, in which investors are not assumed to have advance knowledge of the cay construction estimation coefficients.

Figure 2 shows that cayp had superior performance until the Oil Shock, and nondescript performance thereafter. It also benefited greatly from its performance during the Oil Shock itself.

| cay                                  | Recent 30 years   | All years   |
|--------------------------------------|-------------------|-------------|
| Some ex-post knowledge, cayp IS R 2  | 10.52%            | 15.72%      |
| Some ex-post knowledge, cayp OOS R 2 | 7.60%             | 16.78%      |
| No advance knowledge, caya OOS R 2   | 12.39%            | 4.33%       |

-


The full-sample cayp result confirms the findings in Lettau and Ludvigson (2001). cayp outperforms the benchmark OOS RMSE by 1.61% per annum. It is stable and its OOS performance is almost identical to its IS performance. In contrast to cayp , caya has had no superior OOS performance, either over the entire sample period or the most recent years. In fact, without advance knowledge, caya had the worst OOS R 2 performance among our single variable models.


<!-- p:25 -->


Model Selection : Finally, ms fails with a pattern similar to earlier variables-good performance until 1976, bad performance thereafter.

$$\begin{array} { c c c c } & & & & R e c e n t & & A l l \\ & & & 3 0 \, y e a r s & & y e a r s \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & &$$

Conclusion : There were a number of periods with sharp stock market changes, such as the Great Depression of 1929-1933 (in which the S&amp;P500 dropped from 24.35 at the end of 1928 to 6.89 at the end of 1932) and the ''bubble period'' from 1999-2001 (with its subsequent collapse). However, it is the Oil Shock recession of 1973-1975, in which the S&amp;P500 dropped from 108.29 in October 1973 to 63.54 in September 1974-and its recovery back to 95.19 in June 1975-that stands out. Many models depend on it for their apparent forecasting ability, often both IS and OOS. (And none performs well thereafter.) Still, we caution against overreading or underreading this evidence. In favor of discounting this period, the observed source of significance seems unusual, because the important years are consecutive observations during an unusual period. (They do not appear to be merely independent draws.) In favor of not discounting this period, we do not know how one would identify these special multiyear periods ahead of time, except through a model. Thus, good prediction during such a large shock should not be automatically discounted. More importantly and less ambiguously, no model seems to have performed well since-that is, over the last 30 years.

In sum, on an annual prediction basis, there is no single variable that meets all of our four suggested investment criteria (IS significance, OOS performance, reliance not just on some outliers, and good positive performance over the last three decades.) Most models fail on all four criteria.

## 4. Five-yearly Prediction

Somemodelsmaypredictlong-termreturns better than short-term returns. Unfortunately, we do not have many years to explore five-year predictions thoroughly, and there are difficult econometric issues arising from data overlap. Therefore, we only briefly describe some preliminary and perhaps naive findings. (See, e.g., Boudoukh, Richardson and Whitelaw (2005) and LamoureuxandZhou(1996)formoredetailedtreatments.)Table 2repeats Table 1 with five-year returns. As before, we bootstrap all critical significance levels. This is especially important here, because the observations are overlapping and the asymptotic critical values are not available.

Table 2 shows that there are four models that are significant IS over the entire sample period: ntis , d/p , i/k , and all . ntis and i/k were also significant Table 2 (Continued)


<!-- p:26 -->


Table 2 Forecasts at 5-year frequency This table is identical to Table 1, except that we predict overlapping 5-yearly equity premia, rather than annual equity premia

| 1927-2005 Sample                                                          | IS     | R 2         | - 1 . 39 - 1 . 36 - 1 . 21 - 0 . 30 - 0 . 84 1 . 64 0 . 94 4 . 91 14 . 99 * 14 . 96 * 12 . 47 * Same 13 . 93                                                                                                                                      | Same 21 . 24 ** Same Same                                                       |
|---------------------------------------------------------------------------|--------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| equity premia Forecasts begin 1965                                        |        | Power       |                                                                                                                                                                                                                                                   | 21 ( 67 ) 20 ( 51 ) - ( - )                                                     |
| annual                                                                    | OOS    | Delta1 RMSE | - 2 . 72 - 0 . 25 - 0 . 85 - 10 . 96 0 . 03 0 . 31 + 1 . 38 - 4 . 70 - 2 . 19 - 0 . 07 + 2 . 44 - 0 . 56 - 7 . 17                                                                                                                                 | - 1 . 92 - 3 . 54 Same - 34 . 19                                                |
| than                                                                      |        | R 2         | - 18 . 92 - 4 . 01 - 7 . 34 - 72 . 47 - 2 . 37 - 0 . 64 4 . 97 * - 30 . 19 - 16 . 84 - 3 . 03 10 . 46 ** - 5 . 75 - 46 . 34                                                                                                                       | - 13 . 77 - 26 . 09 - 442 . 08                                                  |
| premia, rather                                                            | IS for | OOS R 2     |                                                                                                                                                                                                                                                   | 1 . 49 8 . 30 19 . 75                                                           |
| predict 5-yearly equity Full sample Forecasts begin 20 years after sample |        | Power       |                                                                                                                                                                                                                                                   | 21 ( 70 ) 21 ( 69 ) 22 ( 78 ) - ( - )                                           |
| overlapping                                                               | OOS    | Delta1 RMSE | - 1 . 10 - 0 . 77 - 1 . 70 - 17 . 41 - 13 . 31 - 0 . 76 - 9 . 18 - 2 . 78 - 0 . 68 - 0 . 03 - 4 . 24 - 0 . 11 - 2 . 03                                                                                                                            | - 0 . 32 - 0 . 06 + 3 . 39 - 45 . 47                                            |
| that we                                                                   |        | R 2         | - 7 . 40 - 5 . 71 - 11 . 25 - 122 . 13 - 79 . 33 - 4 . 87 - 59 . 33 - 17 . 66 - 4 . 45 - 1 . 04 - 26 . 52 - 2 . 35 - 13 . 06                                                                                                                      | - 3 . 46 - 1 . 19 * 12 . 99 ** - 499 . 83                                       |
| 1, except                                                                 | IS for | OOS R 2     |                                                                                                                                                                                                                                                   | - 8 . 28 14 . 35 27 . 42 43 . 29                                                |
| to Table                                                                  | IS     | R 2         | - 1 . 36 - 1 . 36 - 1 . 21 - 0 . 15 0 . 33 0 . 66 3 . 54 3 . 83 6 . 04 6 . 24 7 . 84 9 . 50 10 . 78                                                                                                                                               | 6 . 59 * 10 . 24 * 33 . 99 *** 41 . 48 ***                                      |
| table is identical                                                        |        | Data        | 1926-2005 1926-2005 1919-2005 1919-2005 1885-2005 1872-2005 1919-2005 1920-2005 1872-2005 1872-2005 1920-2005 1927-2005 1921-2005                                                                                                                 | 1927-2005 1872-2005 1947-2005 1927-2005                                         |
| frequency This                                                            |        | Variable    | Not Significant IS Long term return Default return spread Inflation Long term yield Stock variance Dividend payout ratio Default yield spread Treasury-bill rate Dividend yield Earning price ratio Term spread Pct equity issuing Book to market | Significant IS Net equity expansion Dividend price ratio Invstmnt capital ratio |
| Forecasts at 5-year                                                       |        |             | Full Sample, ltr dfr infl lty svar d/e dfy tbl d/y e/p tms eqis b/m                                                                                                                                                                               | Full Sample, ntis d/p i/k all Kitchen sink                                      |


<!-- p:27 -->


| 1927-2005                             | Sample IS   | R 2                            | Same Same Same                                                         | Full Sample   | 7 . 84 6 . 24 6 . 04 10 . 24 *                                                                                      |
|---------------------------------------|-------------|--------------------------------|------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------|
| Forecasts begin 1965                  | OOS         | R 2 Delta1 RMSE Power          | Same Same 122 . 89 - 18 . 03 - ( - )                                   | -             | 12 . 59 ** + 2 . 77 11 ( 65 ) - 15 . 33 - 2 . 18 28 ( 65 ) - 9 . 47 - 1 . 19 22 ( 72 ) - 12 . 69 - 1 . 74 29 ( 61 ) |
| Full sample                           | IS for      | Power OOS R 2                  | - (-) - (-) - (-) -                                                    |               | 23 . 24 - 4 . 04 6 . 16 4 . 28                                                                                      |
| Forecasts begin 20 years after sample | OOS         | R 2 Delta1 RMSE                | 63 . 11 30 . 35 *** + 7 . 50 - 9 . 10 *** + 2 . 50 14465 . 67 408 . 06 | -             |                                                                                                                     |
|                                       | IS IS for   | R 2 OOS R 2 Information (cayp) | 36 . 05 *** - - - -                                                    |               | 12 . 47 * 14 . 96 * 14 . 99 * 21 . 24 **                                                                            |
|                                       |             | ms)                            |                                                                        | IS            | 1927-2005 1927-2005 1927-2005                                                                                       |
|                                       |             | Data or Ex-Post                | 1945-2005 1945-2005 1927-2005                                          |               |                                                                                                                     |
|                                       |             | (caya,                         | incme Incme                                                            | Significant   | 1927-2005                                                                                                           |
|                                       | Variable    |                                | wlth, Wlth, Selection                                                  | Sample,       | Spread Price Ratio Yield Price Ratio                                                                                |
|                                       |             | Full Sample, No IS Equivalent  | cayp Cnsmptn, caya Cnsmptn, ms Model                                   | 1927-2005     | tms Term e/p Earning d/y Dividend d/p Dividend                                                                      |


<!-- p:28 -->


in the annual data (Table 1). Two more variables, d/y and tms , are IS significant if no data prior to 1927 is used.

Dividend Price Ratio : d/p had negative performance OOS regardless of period.

Term Spread : tms is significant IS only if the data begins in 1927 rather than 1921. An unreported plot shows that tms performed well from 1968

to 1979, poorly from 1979 to 1986, and then well again from 1986 to 2005. Indeed, its better years occur in the OOS period, with an IS R 2 of 23.54% from 1965 to 2005. This was sufficient to permit it to turn in a superior OOS Delta1 RMSE performance of 2.77% per five-years-a meaningful difference. Onthe negative side, tms has positive OOS performance only if forecasting begins in 1965. Using 1927-2005 data and starting forecasts in 1947, the OOS Delta1 RMSE and R 2 are negative.

TheKitchenSink:all again turned in exceptionally poor OOS performance.

Model selection ( ms ) and caya again have no IS analogs. ms had the worst predictive performance observed in this paper. caya had good OOS performance of 2.50% per five-year period. Similarly, the investmentcapital ratio, i/k , had both positive IS and OOS performance, and both over the most recent three decades as well as over the full sample (where it was also statistically significant).

|         | Recent   | All    |
|---------|----------|--------|
| i/k     | 30 years | years  |
| IS R 2  | 30.60%   | 33.99% |
| OOS R 2 | 28.00%   | 12.99% |

i/k 's performance is driven by its ability to predict the 2000 crash. In 1997, it had already turned negative on its 1998-2002 equity premium prediction, thus predicting the 2000 collapse, while the unconditional benchmark prediction continued with its 30% plus predictions:

|   Forecast made in | For years   |   Actual EqPm |   Forecast - Unc . |   Forecast - i/k |   Forecast made in | For years   | Actual EqPm   | Forecast Unc. i/k   |
|--------------------|-------------|---------------|--------------------|------------------|--------------------|-------------|---------------|---------------------|
|               1995 | 1996-2000   |          0.58 |               0.30 |             0.22 |               1998 | 1999-2003   | - 0.19        | 0.33 - 0.09         |
|               1996 | 1997-2001   |          0.27 |               0.31 |             0.09 |               1999 | 2000-2004   | - 0.25        | 0.34 - 0.07         |
|               1997 | 1998-2002   |          0.23 |               0.31 |             0.01 |               2000 | 2001-2005   | 0.08          | 0.34 0.06           |

-


This model (and perhaps caya ) seem promising. We hesitate to endorse them further only because our inference is based on a small number of observations, and because statistical significance with overlapping multiyear returns raises a set of issues that we can only tangentially address. We hope more data will allow researchers to explore these models in more detail.


<!-- p:29 -->


## 5. Monthly Prediction and Campbell-Thompson

Table 3 describes the performance of models predicting monthly equity premia. It also addresses a number of points brought up by Campbell and Thompson (2005), henceforth CT. We do not have dividend data prior to 1927, and thus no reliable equity premium data before then. This is why even our the estimation period begins only in 1927.

### 5.1 In-sample performance

Table 3 presents the performance of monthly predictions both IS and OOS. The first data column shows the IS performance when the predicted variable is logged (as in the rest of the article). Eight out of eighteen models are IS significant at the 90% level, seven at the 95% level. Because CT use simple rather than log equity premia, the remaining data columns follow their convention. This generally improves the predictive power of most models, and the fourth column (by which rows are sorted) shows that three more models turn in statistically significant IS. 9

CT argue that a reasonable investor would not have used a model to forecast a negative equity premium. Therefore, they suggest truncation of such predictions at zero. In a sense, this injects caution into the models themselves, a point we agree with. Because there were high equity premium realizations especially in the 1980s and 1990s, a time when many models were bearish, this constraint can improve performance. Of course, it also transforms formerly linear models into nonlinear models, which are generally not the subject of our paper. CT do not truncate predictions in their IS regressions, but there is no reason not to do so. Therefore, the fifth column shows a revised IS R 2 statistic. Some models now perform better, some perform worse.

### 5.2 Out-of-sample prediction performance

The remaining columns explore the OOS performance. The sixth column shows that without further manipulation, eqis is the only model with both superior IS ( R 2 = 0 . 82% and 0.80%) and OOS ( R 2 = 0 . 14%) untruncated performance. The term-spread, tms , has OOS performance that is even better ( R 2 = 0 . 22%), but it just misses statistical significance IS at the 90% level. infl has marginally good OOS performance, but poor IS performance. All other models have negative IS or OOS untruncated R 2 .

The remaining columns show model performance when we implement the Campbell and Thompson (2005) suggestions. The seventh column describes the frequency of truncation of negative equity premium Table 3 Forecasts at monthly frequency using Campbell and Thompson (2005) procedure Refer to Table 1 for basic explanations. This table presents statistics on forecast errors in-sample (IS) and out-of-sample (OOS) for equity premium forecasts at the monthly frequency (both in the forecasting equation and forecast). Variables are explained in Section 2. The data period is December 1927 to December 2004, except for csp (May 1937 to December 2002) and cay3 (December 1951 to December 2004). Critical values of all statistics are obtained empirically from bootstrapped distributions, except for cay3 model where they are obtained from McCracken (2004). The resulting significance levels at 90%, 95%, and 99% are denoted by one, two, and three stars, respectively. They are two-sided for IS model significance, and one-sided for OOS superior model performance. The first data column is the IS R 2 when returns are logged, as they are in our other tables. The remaining columns are based on predicting simple returns for correspondence with Campbell and Thompson (2005). Certainty Equivalence (CEV) gains are based on the utility of an optimizer with a risk-aversion coefficient of γ = 3 who trades based on unconditional forecast and conditional forecast. Equity positions are winsorized at 150% ( w = w max). At this risk-aversion, the base CEV are 82bp for a market-timer based on the unconditional forecast, 79bp for the market, and 40bp for the risk-free rate. ''T'' means ''truncated'' to avoid a negative equity premium prediction. ''U'' means unconditional, that is, to avoid a forecast that is based on a coefficient that is inverse to what the theory predicts. A superscript h denotes high trading turnover of about 10%/month more than the trading strategy

9 Geert Bekaert pointed out to us that if returns are truly log-normal, part of their increased explanatory power could be due to the ability of these variables to forecast volatility.


<!-- p:30 -->


#### based on unconditional forecasts.

##### Simple returns

Log Month permitted. The Oil Shock (Nov 1973 to Mar 1975) is marked by a red vertical line.

| Fig                       | F 3 .G F 3 .F                                                                                                     | F 3 .E                                                       | F 3 .D F 3 .B F 3 .C F 3 .A                                                                                                                                  |
|---------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Delta1 CEV                | - 0 . 01 - 0 . 04 0 . 01 0 . 06 0 . 06 0 . 04 0 . 14                                                              | 0 . 10 - 0 . 08 - 0 . 10                                     | - 0 . 14 - 0 . 04 0 . 14 - 0 . 22 - 0 . 13 0 . 06 0 . 02 0 . 06                                                                                              |
| w = w max                 | 57 . 7 35 . 4 44 . 9 19 . 5 51 . 2 h 43 . 5 h 59 . 3                                                              | 16 . 4 27 . 3 16 . 1                                         | 16 . 4 34 . 4 55 . 8 31 . 3 15 . 4 13 . 5 57 . 4 13 . 2                                                                                                      |
| (2005) OOS Delta1 RMSE TU | - 0 . 0114 - 0 . 0134 - 0 . 0030 + 0 . 0085 + 0 . 0053 + 0 . 0045 + 0 . 0073                                      | + 0 . 0081 - 0 . 0071 + 0 . 0066                             | + 0 . 0023 - 0 . 0183 + 0 . 0093 - 0 . 0432 - 0 . 0071 + 0 . 0072 - 0 . 0003 + 0 . 0088                                                                      |
| and Thompson R 2 TU       | - 0 . 69 - 0 . 79 - 0 . 29 0 . 26 ** 0 . 11 ** 0 . 07 ** 0 . 21 **                                                | 0 . 25 ** - 0 . 49 0 . 17 *                                  | - 0 . 04 * - 1 . 03 0 . 30 *** - 2 . 23 - 0 . 48 0 . 15 ** - 0 . 16 - 0 . 34 *                                                                               |
| Campbell Frcst= U         | 7 . 9 0 . 0 20 . 9 0 . 0 38 . 2 0 . 0 0 . 0                                                                       | 0 . 0 0 . 0 0 . 0                                            | 0 . 0 0 . 0 0 . 0 0 . 0 0 . 0 0 . 0 0 . 0 0 . 0                                                                                                              |
| T                         | 0 . 0 0 . 0 0 . 0 34 . 1 3 . 0 1 . 3 3 . 7                                                                        | 23 . 1 4 . 0 32 . 3                                          | 54 . 2 18 . 1 6 . 7 44 . 3 52 . 4 44 . 7 0 . 4 44 . 7                                                                                                        |
| OOS R 2                   | - 0 . 70 - 0 . 79 - 0 . 37 - 0 . 80 - 0 . 63 0 . 01 * 0 . 22 **                                                   | - 0 . 08 * - 0 . 56 - 0 . 30                                 | - 1 . 12 - 1 . 04 0 . 14 ** - 3 . 28 - 2 . 21 - 0 . 94 - 0 . 16 - 2 . 05                                                                                     |
| R 2 T                     | - 0 . 10 - 0 . 07 - 0 . 08 0 . 02 0 . 08 - 0 . 05 0 . 20                                                          | 0 . 15 0 . 28 0 . 29                                         | 0 . 45 0 . 45 0 . 59 0 . 88 0 . 96 0 . 93 0 . 88 1 . 57                                                                                                      |
| IS R 2                    | - 0 . 10 - 0 . 07 - 0 . 07 0 . 02 0 . 07 0 . 14 0 . 18                                                            | 0 . 20 * 0 . 28 * 0 . 33 *                                   | 0 . 47 ** 0 . 54 ** 0 . 80 *** 0 . 81 *** 0 . 86 *** 0 . 99 *** 1 . 02 *** 1 . 87 ***                                                                        |
| returns IS R 2            | 0 . 02 - 0 . 09 - 0 . 02 - 0 . 03 0 . 04 - 0 . 01 0 . 12                                                          | 0 . 10 - 0 . 06 0 . 12                                       | 0 . 22 * 0 . 51 ** 0 . 82 *** 0 . 45 ** 0 . 46 ** 0 . 92 *** 0 . 94 *** 1 . 88 ***                                                                           |
| Variable                  | Dividend payout ratio Stock variance Default return spread Long term yield Long term return Inflation Term spread | Treasury-bill rate Default yield spread Dividend price ratio | Dividend yield Earning price ratio Pct equity issuing Book to market Earning(10Y) price ratio Cross-sectional prem Net equity expansion Cnsmptn, wlth, incme |
|                           | d/e svar dfr lty ltr infl tms                                                                                     | tbl dfy d/p                                                  | d/y e/p eqis b/m e 10 /p csp ntis cay 3                                                                                                                      |


<!-- p:31 -->


Figure 3 Monthly performance of in-sample significant predictors

Explanation: These figures are the analogs of Figures 1 and 2, plotting the IS and OOS performance of the named model. However, they use monthly data. The IS performance is in black. The Campbell-Thompson (2005) (CT) OOS model performance is plotted in blue, the plain OOS model performance is plotted in green. The top bars (''T'') indicate truncation of the equity prediction at 0, inducing the CT investor to hold the risk-free security. (This also lightens the shade of blue in the CT line.) The lower bars (''M'') indicate when the CT risk-averse investor would purchase equities worth 150% of his wealth, the maximum

TTT

IT

fff IT TTT


<!-- p:32 -->


Figure 3 Continued

predictions. For example, d/y 's equity premium predictions are truncated to zero in 54.2% of all months; csp 's predictions are truncated in 44.7% of all months. Truncation is a very effective constraint.

CT also suggest using the unconditional model if the theory offers one coefficient sign and the estimation comes up with the opposite sign. For some variables, such as the dividend ratios, this is easy. For other models, it is not clear what the appropriate sign of the coefficient would be. In any case, this matters little in our data set. The eighth column shows that the

Month coefficient sign constraint matters only for dfr and ltr (and mildly for d/e). None of these three models has IS performance high enough to make this worthwhile to explore further.


<!-- p:33 -->


Figure 3 Continued

The ninth and tenth columns, R 2 TU and Delta1 RMSETU, show the effect of the CT truncations on OOS prediction. For many models, the performance improves. Nevertheless, the OOS R 2 's remain generally much lower than their IS equivalents. Some models have positive Delta1 RMSE but negative

Month OOS R 2 . This reflects the number of degrees of freedom: even though we have between 400 and 800 data months, the plain Delta1 RMSE and R 2 are often so small that the R 2 turns negative. For example, even with over 400 months of data, the loss of three degrees of freedom is enough for cay3 to render a positive Delta1 RMSE of 0.0088 (equivalent to an unreported unadjusted R 2 of 0.0040) into a negative adjusted R 2 of - 0.0034.


<!-- p:34 -->


Figure 3 Continued

Even after these truncations, ten of the models that had negative plain OOS R 2 's still have negative CT OOS R 2 's. Among the eleven IS significant models, seven ( cay3 , ntis , e 10 /p , b/m , e/p , d/y , and dfy ) have negative OOS R 2 performance even after the truncation. Three of the models ( lty , ltr , and infl ) that benefit from the OOS truncation are not close to statistical significance IS, and thus can be ignored. All in all, this leaves four models that are both OOS and IS positive and significant: csp, eqis , d/p , tbl , plus possibly tms (which is just barely not IS significant). We investigate these models further below.

### 5.3 OOSutility performance of a trading strategy

Like Brennan and Xia (2004), CT also propose to evaluate the OOS usefulness of models based on the certainty equivalence (CEV) measure of a trading strategy. Specifically, they posit a power-utility investor with an assumed risk-aversion parameter, γ , of three. This allows a conditional model to contribute to an investment strategy not just by increasing the mean trading performance, but also by reducing the variance. (Breen, Glosten and Jagannathan (1989) have shown this to be a potentially important factor.)


<!-- p:35 -->


Although the focus of our article is on mean prediction, we know of no better procedure to judge the economic significance of forecasting models, andtherefore follow their suggestion here. To prevent extreme investments, there is a 150% maximum equity investment. A positive investment weight is guaranteed by the truncation of equity premium predictions at zero.

CT show that even a small improvement in Delta1 RMSE by a model over the unconditional benchmark can translate into CEV gains that are ten times as large. 10 We can confirm this-and almost to a fault. cay3 offers 6.1bp/month performance, even though it had a negative R 2 . Column 12 also shows that even models that have a negative OOS Delta1 RMSE (not just a negative R 2 ), like dfr , can produce positive gains in CEV. This is because the risk-aversion parameter γ of 3 is low enough to favor equity-tilted strategies. Put differently, some strategy CEV gains are due to the fact that the risky equity investment was a better choice than the risk-free rate in our data. (This applies not only to strategies based on the conditional models, but also to the strategy based on the unconditional mean.) An alternative utility specification that raises the risk-aversion coefficient to 7.48 would have left an investor indifferent between the risk-free and the equity investments. Briefly considering this parameter can help judge the role of equity bias in a strategy; it does seem to matter for the eqis and tms models, as explained below.

In order, among the IS reasonably significant models, those providing positive CEV gains were tms (14bp/month), eqis (14bp/month), tbl (10bp/month), csp (6bp/month), cay3 (6bp/month), and ntis (2bp/month).

### 5.4 Details

We now look more closely at the set of variables with potentially appealing forecasting characteristics. csp , eqis , tbl , and tms have positive IS performance (either statistically significant or close to it), positive OOS R 2 (truncated), and positive CEV gains. cay3 and ntis have negative OOS R 2 , but very good IS performance and positive CEV gains. d/p has a negative CEV gain, but is positive IS and OOS R 2 . Thus, we describe these seven models in more detail (and with equivalent graphs):

10 CT show in Equation (8) of their paper that the utility gain is roughly equal to OOSR 2 /γ . This magnification effect occurs only on the monthly horizon, because the difference between OOSR 2 and the Delta1 RMSE scales with the square root of the forecasting horizon (for small Delta1 RMSE, OOSR 2 ≈ 2 × Delta1 RMSE / StdDev (R) ). That is, at a monthly frequency, the OOSR 2 is about 43 times as large as Delta1 RMSE.Onanannual prediction basis, this number drops from 43 to 12. An investor with a risk aversion of 10 would therefore consider the economic significance on annual investment horizon to be roughly the same as the Delta1 RMSE we consider. (We repeated the CT CEV equivalent at annual frequency to confirm

this analysis.)


<!-- p:36 -->


- (i) cay3: The best CT performer is an alternative cay model that also appears in Lettau and Ludvigson (2005). It predicts the equity premium not with the linear cay , but with all three of its highly cointegrated ingredients up to date. We name this model cay3 . In unreported analysis, we found that the cay model and cay3 models are quite different. For most of the sample period, the unrestricted predictive regression coefficients of the cay3 model wander far off their cointegration-restricted cay equivalents. The model may not be as well founded theoretically as the Lettau and Ludvigson (2001) cay , but if its components are known ex-ante , then cay3 is fair game for prediction.

Table 3 shows that cay3 has good performance IS, but only marginal performance OOS (a positive Delta1 RMSE, but a negative R 2 ). It offers good CEV gains among the models considered, an extra 6.10 bp/month. The h superscript indicates that its trading strategy requires an extra 10% more trading turnover than the unconditional model. It also reaches the maximum permitted 150% equity investment in 13.2% of all months.

Afirst drawback is that the cay3 model relies on data that may not be immediately available. Its components are publicly released by the Bureau of Economic Analysis about 1-2 months after the fact. Adding just one month delay to trading turns cay3 's performance negative:

```
Immediate availability (CT)-2.88 bp	+0.88 bp	+6.10 bp
		One month delayed			-5.10 bp	-1.62 bp	-11.82 bp
		Two months delayed			-5.38 bp	-1.11 bp	-9.80 bp
```

A second drawback is visible in Figure 3. Like caya and cayp , much of cay3 's performance occurs around the Oil Shock (most of its OOS performance are between one-half and one-third of its IS performance). Even IS, cay3 has not performed well for over 30 years now:

```
Recent       All
       cay3 (CT)       30 years     years
       IS  R^            -0.30%    1.87%
       OOS  R^         -1.60%    -0.34%
;
figure  shows  that  many  of  cay3's  re
```

Finally, the figure shows that many of cay3 's recent equity premium forecasts have been negative and therefore truncated. And, therefore, the information in its current forecasts is limited.

- (ii) csp: Table 3 shows that the relative valuations of highover low-beta stocks had good IS and truncated OOS performance,


<!-- p:37 -->


and offered a market timer 6.12 bp/month superior the CEVequivalent performance. The plot in Figure 3 shows that csp had good performance from September 1965 to March 1980. It underperformed by just as much from about April 1980 to October 2000. In fact, from its first OOS prediction in April 1957 to August 2001, csp 's total net performance was zero even after the CT truncations, and both IS and OOS. All of csp 's superior OOS performance has occurred since mid-2001. Although it is commendable that it has performed well late rather than early, better performance over its first 45 years would have made us deem this variable more reliable.

The plot raises one other puzzle. The CT-truncated version performs better than the plain OLS version because it truncated the csp predictions from July 1957 through January 1963. These CT truncations are critically responsible for its superior OOS performance, but make no difference thereafter. It is the truncation treatment of these specific 66 months that would make an investor either believe in superior positive or inferior outright negative performance for csp (from August 2001 to December 2005). We do not understand why the particular 66 month period from 1957 to 1963 is so crucial.

Finally, the performance during the Oil Shock recession is not important for IS performance, but it is for the OOS performance. It can practically account for its entire OOS performance. Since the Oil Shock, csp has outperformed IS, but not OOS:

|          | Recent   | All   |
|----------|----------|-------|
| csp (CT) | 30 years | years |
| IS R 2   | 0.33%    | 0.99% |
| OOS R 2  | 0.41%    | 0.15% |

- (iii) ntis: Net issuing activity had good IS performance, but a negative OOS R 2 . Its CEV gain is a tiny 1.53 bp/month. These 1.53 bp are likely to be offset by trading costs to turn over an additional 4.6% of the portfolio every month. 11 The strategy was very optimistic, reaching the maximum 150% investment constraint in 57.4% of all months. We do not report it in the table, but an investor with a higher 7.48 risk-aversion parameter, who would not have been so eager to highly lever herself into the market,

11 Keim and Madhavan (1997) show that one typical roundtrip trade in large stocks for institutional investors would have conservatively cost around 38 bp from 1991-1993. Costs for other investors and earlier time-periods were higher. Futures trading costs are not easy to gage, but a typical contract for a notional amount of $250,000 costs around $10-$30. A 20% movement in the underlying index-about the annual volatility-would correspond to $50,000, which would come to around 5 bp.


<!-- p:38 -->


- would have experienced a negative CEV with an ntis optimized trading strategy. Finally, the plot shows that almost all of the csp model's IS power derives from its performance during the Great Depression. There was really only a very short window from 1982 to 1987 when csp could still perform well.
- (iv) eqis: Equity Issuing Activity had good IS performance and a good OOS performance, and improved the CEV for an investor by a meaningful 13.67 bp/month. It, too, was an optimistic equityaggressive strategy. With a γ = 3, trading based on this variable leads to the maximum permitted equity investment of 150% in 56% of all months. Not reported, with the higher risk-aversion coefficient of 7.48, that would leave an investor indifferent between bonds and stocks, the 13.67 bp/month gain would shrink to 8.74 bp/month.

As in the annual data, Figure 3 shows that eqis 's performance relies heavily on the good Oil Shock years. It has not performed well in the last 30 years.

|           | Recent   | All   |
|-----------|----------|-------|
| eqis (CT) | 30 years | years |
| IS R 2    | - 0.88%  | 0.80% |
| OOS R 2   | 1.00%    | 0.30% |

- (v) d/p: The dividend price ratio has good IS and OOS R 2 . (The OOS R 2 is zero when predicting log premia.) An investor trading on d/p would have lost the CEV of 10 bp/month. (Not reported, a more risk-averse investor might have broken even.) The plot shows that d/p has not performed well over the last 30 years; d/p has predicted negative equity premia since January 1992.
- (vi) tbl: The short rate is insignificant IS if we forecast log premia. If we forecast unlogged premia, it is statistically significant IS at the 9% level, although this declines further if we apply the CT truncation. In its favor, tbl 's full-sample CT-truncated performance is statistically significant OOS, and it offers a respectable 9.53 bp/month market timing advantage. The plot shows that this is again largely Oil Shock dependent. tbl has offered no advantage over the last thirty years.

|          | Recent   | All   |
|----------|----------|-------|
| d/p (CT) | 30 years | years |
| IS R 2   | - 0.39%  | 0.33% |
| OOS R 2  | 1.09%    | 0.17% |


<!-- p:39 -->


|          | Recent   | All   |
|----------|----------|-------|
| tbl (CT) | 30 years | years |
| IS R 2   | - 0.41%  | 0.20% |
| OOS R 2  | 1.06%    | 0.25% |

- (vii) tms: The term-spread has IS significance only at the 10.1% level. (With logged returns, this drops to the 14.5% level.) Nevertheless, tms had solid OOS performance, either with or without the CT truncation. As a consequence, its CEV gain was a respectable 14.40 bp/month. Not reported in the table, when compared to the CEVgain of an investor with a risk-aversion coefficient of 7.48, we learn that about half of this gain comes from the fact that the termspread was equity heavy. (It reaches its maximum of 150% equity investment in 59.3% of all months.) The figure shows that TMS performed well in the period from 1970 to the mid-1980s, that TMS has underperformed since then, and that the Oil Shock gain was greater than the overall OOS sample performance of tms . Thus,

|          | Recent   | All   |
|----------|----------|-------|
| tms (CT) | 30 years | years |
| IS R 2   | - 0.19%  | 0.18% |
| OOS R 2  | 0.81%    | 0.21% |

b/m , e/p , e 10 /p , d/y , and dfy have negative OOS R 2 and/or CT CEV gains, and so are not further considered. The remaining models have low or negative IS R 2 , and therefore should not be considered, either. Not reported, among the models that are IS insignificant, but OOS significant, none had positive performance from 1975 till today.

### 5.5 Comparing findings and perspectives

The numbers we report are slightly different from those in Campbell and Thompson (2005). In particular, they report cay3 to have a Delta1 RMSE of 0.0356, more than the 0.0088 we report. This can be traced back to three equally important factors: they end their data 34 months earlier (in 2/2003), they begin their estimation one month later (1/1952), and they use an earlier version of the cay data from Martin Lettau's website. Differences in other variables are sometimes due to use of pre-1927 data (relying on price changes because returns are not available) for estimation though not prediction, while we exclude all pre-1927 data.

More importantly, our perspective is different from CT's. We believe that the data suggests not only that these models are not good enough for actual investing, but also that the models are not stable. Therefore, by and large, we consider even their IS significance to be dubious. Because they fail stability diagnostics, we would recommend against their continued use. Still, we can agree with some points CT raise:


<!-- p:40 -->


- (i) One can reasonably truncate the models' predictions.
- (ii) On shorter horizons, even a small predictive Delta1 RMSE difference can gain a risk-averse investor good CEV gains.
- (iii) OOS performance should not be used for primary analysis.

We draw different conclusions from this last point. We view OOS performancenotasasubstitute but as a necessary complement to IS performance. We consider it to be an important regression diagnostic , and if and only if the model is significant IS. Consequently, we disagree with the CT analysis of the statistical power of OOS tests. In our view, because the OOS power matters only if the IS regression is statistically significant, the power of the OOS tests is conditional and thus much higher than suggested in CT, Cochrane (2005), and elsewhere. Of course, any additional diagnostic test can only reject a model-if an author is sure that the linear specification is correct, then not running the OOS test surely remains more powerful.

In judging the usefulness of these models, our article attaches more importance than CT to the following facts:

- (i) Most models are not IS significant. That is, many variables in the academic literature no longer have IS significance (even at the 90% level). It is our perspective that this disqualifies them as forecasters for researchers without strong priors.
- (ii) After three decades of poor performance, often even IS, one should further doubt the stability of most prediction models.
- (iii) Even after the CT truncation, many models earn negative CEV gains.
- (iv) What we call OOS performance is not truly OOS, because it still relies on the same data that was used to establish the models. (This is especially applicable to eqis and csp , which were only recently proposed.)
- (v) For practical use, an investor would have had to have known exante which of the models would have held up, and that none of the models had superior performance over the last three decades-in our opinion because the models are unstable.

We believe it is now best left to the reader to concur either with our or CT's perspective. (The data is posted on the website.)

## 6. Alternative Specifications

We now explore some other models and specifications that have been proposed as improvements over the simple regression specifications.


<!-- p:41 -->


### 6.1 Longer-memory dividend and earnings ratios

Table 4 considers dividend-price ratios, earnings-price ratios, and dividend-earnings ratios with memory (which simply means that we consider sums of multiple year dividends or earnings in these ratios). The table is an excerpt from a complete set of one-year, five-year, and tenyear dividend-price ratios, earnings-price ratios, and dividend-earnings ratios. (That is, we tried all 90 possible model combinations.) The table contains all 27 IS significant specifications from our monthly regressions that begin forecasting in 1965, and from our annual and 5-yearly forecasts that begin forecasting either in 1902 or 1965.

Even though there were more combinations of dividend-earnings ratios than either dividend-price or earnings-price ratios, not a single dividend-earnings ratio turned out IS statistically significant. The reader can also see that out of our 27 IS-significant models, only 5 had OOS positive and statistically significant performance. (For 2 of these models, the OOS significance is modest, not even reaching the 95% significance level.) Unreported graphs show that none of these performed well over the last three decades. (We also leave it to the readers to decide whether they believe that real-world investors would have been able to choose the right five models for prediction, and to get out right after the Oil Shock.)

### 6.2 Different estimation methods to improve power for nonstationary independent variables

Stambaugh (1999) shows that predictive coefficients in small samples are biased if the independent variable is close to a random walk. Many of our variables have autoregressive coefficients above 0.5 on monthly frequency. Goyal and Welch (2003) show that d/p and d/y 's autocorrelations are not stable but themselves increase over the sample period, and similar patterns occur with other variables in our study. (The exceptions are ntis , ltr , and dfy .) Our previously reported statistics took stable positive autoregressive coefficients into account, because we bootstrapped for significance levels mimicking the IS autocorrelation of each independent variable.

However, one can use this information itself to design more powerful tests. Compared to the plain OLS techniques in our preceding tables, the Stambaugh coefficient correction is a more powerful test in nonasymptotic samples. There is also information that the autocorrelation is not constant for the dividend ratios, which we are ignoring in our current article. Goyal and Welch (2003) use rolling dividend-price ratio and dividend-growth autocorrelation estimates as instruments in their return predictions. This is model specific, and thus can only apply to one model, the dividend price ratio ( d/p ). In contrast, Lewellen (2004) and Campbell and Yogo (2006) introduce two further statistical corrections, extending Stambaugh (1999) and assuming different boundary behavior. This subsection, therefore, explores equity premium forecasts using these corrected coefficients.


<!-- p:42 -->


Table 4 Significant forecasts using various d/p, e/p, and d/e Ratios

| Variable                          | Data      | Freq     | IS - R 2   | OOS - R 2   | OOS - Delta1 RMSE   |
|-----------------------------------|-----------|----------|------------|-------------|---------------------|
| e/p Earning(1Y) price ratio       | 1927-2005 | M1965-   | 0 . 54 **  | - 1 . 20    | - 0.02              |
| e 5 /p Earning(5Y) price ratio    | 1927-2005 | M1965-   | 0 . 32 *   | - 0 . 60    | - 0.01              |
| e 10 /p Earning(10Y) price ratio  | 1927-2005 | M1965-   | 0 . 49 **  | - 0 . 83    | - 0.01              |
| e 3 /p Earning(3Y) price ratio    | 1882-2005 | A1902-   | 2 . 53 **  | - 1 . 05 *  | - 0.01              |
| e 5 /p Earning(5Y) price ratio    | 1882-2005 | A1902-   | 2 . 88 **  | - 0 . 52 *  | + 0.04              |
| e 10 /p Earning(10Y) price ratio  | 1882-2005 | A1902-   | 4 . 89 **  | 2 . 12 **   | + 0.30              |
| d 10 /p Dividend(3Y) price ratio  | 1882-2005 | A1902-   | 1 . 85 *   | - 1 . 53    | - 0.05              |
| d 5 /p Dividend(5Y) price ratio   | 1882-2005 | A1902-   | 2 . 48 *   | - 0 . 54 *  | + 0.04              |
| d 10 /p Dividend(10Y) price ratio | 1882-2005 | A1902-   | 2 . 11 *   | - 1 . 07 *  | - 0.01              |
| e 3 /p Earning(3Y) price ratio    | 1882-2005 | A1965-   | 2 . 53 **  | - 3 . 41    | - 0.06              |
| e 5 /p Earning(5Y) price ratio    | 1882-2005 | A1965-   | 2 . 88 **  | - 5 . 01    | - 0.19              |
| e 10 /p Earning(10Y) price ratio  | 1882-2005 | A1965-   | 4 . 89 **  | - 11 . 45   | - 0.66              |
| d 3 /p Dividend(3Y) price ratio   | 1882-2005 | A1965-   | 1 . 85 *   | - 6 . 55    | - 0.30              |
| d 5 /p Dividend(5Y) price ratio   | 1882-2005 | A1965-   | 2 . 48 *   | - 8 . 79    | - 0.47              |
| d 10 /p Dividend(10Y) price ratio | 1882-2005 | A1965-   | 2 . 11 *   | - 8 . 32    | - 0.43              |
| e 3 /p Earning(3Y) price ratio    | 1882-2005 | 5Y 1902- | 11 . 35 *  | 3 . 46 **   | + 0.89              |
| e 5 /p Earning(5Y) price ratio    | 1882-2005 | 5Y 1902- | 16 . 16 ** | 4 . 76 **   | + 1.16              |
| e 10 /p Earning(10Y) price ratio  | 1882-2005 | 5Y 1902- | 16 . 47 ** | - 2 . 85 *  | - 0.37              |
| d/p Dividend(1Y) price ratio      | 1882-2005 | 5Y 1902- | 12 . 30 *  | - 0 . 66 *  | + 0.06              |
| d 3 /p Dividend(3Y) price ratio   | 1882-2005 | 5Y 1902- | 13 . 11 *  | - 2 . 02 *  | - 0.21              |
| d 5 /p Dividend(5Y) price ratio   | 1882-2005 | 5Y 1902- | 13 . 75 *  | - 3 . 85 *  | - 0.57              |
| e 3 /p Earning(3Y) price ratio    | 1882-2005 | 5Y 1965- | 11 . 35 *  | - 12 . 55   | - 1.56              |
| e 5 /p Earning(5Y) price ratio    | 1882-2005 | 5Y 1965- | 16 . 16 ** | - 21 . 16   | - 2.85              |
| e 10 /p Earning(10Y) price ratio  | 1882-2005 | 5Y 1965- | 16 . 47 ** | - 25 . 65   | - 3.51              |
| d/p Dividend(1Y) price ratio      | 1882-2005 | 5Y 1965- | 12 . 30 *  | - 29 . 33   | - 4.03              |
| d 3 /p Dividend(3Y) price ratio   | 1882-2005 | 5Y 1965- | 13 . 11 *  | - 28 . 11   | - 3.86              |
| d 5 /p Dividend(5Y) price ratio   | 1882-2005 | 5Y 1965- | 13 . 75 *  | - 30 . 71   | - 4.23              |

Refer to Table 1 for basic explanations. The table reports only those combinations of d/p , e/p , and d/e that were found to predict equity premia significantly in-sample. This table presents statistics on forecast errors in-sample (IS) and out-of-sample (OOS) for excess stock return forecasts at various frequencies. Variables are explained in Section 2. All Delta1 RMSEnumbers are in percent per frequency

corresponding to the column entitled 'Freq'. The 'Freq' column also gives the first year of forecast. 2 statistics are obtained empirically from bootstrapped distributions. Significance levels at 90%, 95%,

Astar next to OOSR is based on the MSEF -statistic by McCracken (2004), which tests for equal MSE of the unconditional forecast and the conditional forecast. One-sided critical values of MSE and 99% are denoted by one, two, and three stars, respectively.

In Table 5, we predict with Stambaugh and Lewellen corrected coefficients. Both methods break the link between R 2 (which is maximized by OLS) and statistical significance. The Lewellen coefficient is often dramatically different from the OLS coefficients, resulting in negative R 2 , even among its IS significant variable estimations. However, it is also tremendously powerful. Given our bootstrapped critical rejection levels under the NULL hypothesis, this technique is able to identify eight (rather than just three) ALTERNATIVE models as different from the NULL. In six of them, it even imputes significance in each and every one of our 10,000 bootstraps!


<!-- p:43 -->


Table 5 Forecasts at monthly frequency with alternative procedures and total returns Refer to Table 1 for basic explanations.Columns under the heading ''OLS'' are unadjusted betas, columns under the heading ''Stambaugh'' correct for betas following Stambaugh (1999), and columns under the heading 'Lewellen' correct for betas following Lewellen (2004). ρ under the column OLS gives the autoregressive coefficient of the variable over the entire sample period (the variables are sorted in descending order of ρ ).

| OOS Power     | 15 (69) 10 (67) 32 (72) 3 (3) 20 (68) 41 (41) 19 (19) 65 (81) 5 (43) 58 (74) 20 (65)                                                                                                                                                                    | 7 (7) 15 (56) 12 (12) 10 (38)                                                     |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Lewellen R 2  | - 2 . 05 - 1 . 05 - 0 . 26 - 1 . 03 - 0 . 27 - 0 . 01 ** - 0 . 31 0 . 71 *** - 0 . 71 - 0 . 38 0 . 06 *                                                                                                                                                 | - 0 . 63 - 0 . 13 - 6 . 41 - 2 . 64                                               |
| IS R 2        | 0 . 01 - 0 . 01 0 . 25 * - 0 . 15 ** 0 . 11 0 . 02 *** - 0 . 14 ** 0 . 91 *** - 0 . 15 0 . 74 *** 0 . 07                                                                                                                                                | - 1 . 66 ** - 0 . 03 - 1 . 55 *** - 1 . 32 *                                      |
| OOS Power     | 15 (69) 9 (68) 33 (71) 26 (69) 20 (69) 59 (73) 48 (71) 65 (80) 8 (59) 59 (76) 20 (65)                                                                                                                                                                   | 7 (53) 14 (62) 18 (62) 12 (61)                                                    |
| Stambaugh R 2 | - 2.11 - 1.71 - 0.36 - 0.31 - 0.33 - 0.54 - 1.61 0.70 *** - 0.33 - 0.29 0.07 *                                                                                                                                                                          | - 0.34 - 0.07 - 0.48 - 0.30                                                       |
| IS R 2        | 0.01 - 0.01 0.25 * 0.05 0.11 0.48 ** 0.36 ** 0.92 *** - 0.07 0.75 *** 0.07                                                                                                                                                                              | - 0.08 - 0.00 0.04 - 0.02                                                         |
| OOS Power     | 15 (70) 9 (68) 33 (71) 29 (56) 19 (69) 56 (64) 48 (65) 65 (80) 9 (59) 59 (76) 21 (66)                                                                                                                                                                   | 7 (53) 14 (62) 18 (62) 12 (61)                                                    |
| OLS R 2       | - 2.02 - 1.15 - 0.40 - 0.15 - 0.18 - 1.21 - 2.45 0.70 *** - 0.14 - 0.28 0.09 *                                                                                                                                                                          | - 0.34 - 0.07 - 0.49 - 0.30                                                       |
| R 2           | 0.01 - 0.01 0.25 * 0.15 0.11 0.54 ** 0.40 ** 0.92 *** - 0.07 0.75 *** 0.07                                                                                                                                                                              | - 0.08 - 0.00 0.04 - 0.02                                                         |
| IS ρ          | 0.9989 0.9963 0.9929 0.9927 0.9922 0.9879 0.9843 0.9788 0.9763 0.9680 0.9566                                                                                                                                                                            | 0.6008 0.5513 0.0532 - 0.1996                                                     |
| Data          | 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 193705-200212 192701-200512 192701-200512 192701-200512                                                                                               | 192701-200512 192701-200512 192701-200512 192701-200512                           |
| Variable      | d/e Dividend payout ratio lty Long term yield d/y Dividend yield d/p Dividend price ratio tbl Treasury-bill rate e/p Earning price ratio b/m Book to market csp Cross-Sectional prem dfy Default yield spread ntis Net equity expansion tms Term spread | svar Stock variance infl Inflation ltr Long term return dfr Default return spread |


<!-- p:44 -->


Unfortunately, neither the Stambaugh nor the Lewellen technique manages to improve OOS prediction. Of all models, only the e/p ratio in the Lewellen specification seems to perform better with a positive Delta1 RMSE. However, like other variables, it has not performed particularly well over the most recent 30 years-even though it has nonnegative OOS Delta1 RMSE (but not R 2 ) performance over the last three decades.

|                | Recent   | All   |
|----------------|----------|-------|
| e/p (Lewellen) | 30 years | years |
| IS R 2         | - 0.16%  | 0.02% |
| 2              |          |       |

OOS

R

### 6.3 Encompassing tests

Our next tests use encompassing predictions. A standard encompassing test is a hybrid of ex-ante OOS predictions and an ex-post optimal convex combination of unconditional forecast and conditional forecast. A parameter λ gives the ex-post weight on the conditional forecast for the optimal forecast that minimizes the ex-post MSE. The ENC statistic in Equation (7) can be regarded as a test statistic for λ . If λ is between 0 and 1, we can think of the combination model as a ''shrinkage'' estimator. It produces an optimal combination OOS forecast error, which we denote Delta1 RMSE ⋆ . However, investors would not have known the optimal ex-post λ . This means that they would have computed λ on the basis of the best predictive up-to-date combination of the two OOS model (NULL and ALTERNATIVE), and then would have used this λ to forecast one month ahead. We denote the relative OOS forecast error of this rolling λ procedure as Delta1 RMSE ⋆r . 12

Table 6 shows the results of encompassing forecast estimates. Panel A predicts annual equity premia. Necessarily, all ex-post λ combinationshave positive Delta1 RMSE ⋆ -but almost all rolling λ combinations have negative Delta1 RMSE ⋆r . The exceptions are d/e and cayp (with OOS knowledge). In some but not all specifications, this also applies to dfy , all , and caya . d/e , dfy , and all can immediately be excluded, because their optimal λ is negative. This leaves caya . Again, not reported, caya could not outperform over the most recent three decades. In the monthly rolling encompassing tests (not reported), only svar and d/e (in one specification) are positive, neither with a positive λ .

12 For the first three observations, we presume perfect optimal foresight, resulting in the minimum Delta1 RMSE. This tilts the rolling statistic slightly in favor of superior performance. The results remain the same if we use reasonable variations.

0.08%

-


0.01%


<!-- p:45 -->


Table 6 Encompassing tests This table presents statistics on encompassing tests for excess stock return forecasts at various frequencies. Variables are explained in Section 1. All numbers are in percent per frequency corresponding to the panel. λ gives the ex-post weight on the conditional forecast for the optimal forecast that minimizes the MSE. ENC is the test statistic proposed by Clark and McCracken (2001) for a test of forecast encompassing. One-sided critical values of ENC statistic are obtained empirically from bootstrapped distributions, except for caya, cayp, and all models where they are obtained from Clark and McCracken (2001). Critical values for ms model are not calculated. cayp uses ex-post information. Delta1 RMSE ∗ is the RMSE difference between the unconditional forecast and the optimal forecast for the same sample/forecast period. Delta1 RMSE ∗ r is the RMSE difference between the unconditional forecast and the optimal forecast for the same sample/forecast period using rolling estimates of λ . Significance levels at 90%, 95%, and 99% are denoted by one, two, and three stars, respectively.

| 1965                      | ∗ Delta1 RMSE ∗ r 0.3539      | - - 0.2858 - 0.4049 + 0.7796 + 0.4490 - 0.4821 - 0.9310 - 0.7106 - 0.5619 - 0.5682 - 8.7284 - 0.5375 + 0.4496 - 0.3877 - 0.4697 - 0.1950 + 0.3315 - 0.4666 - 0.3185 - 1.1268                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1927                      | Delta1 RMSE                   | + 0.2297 + 0.2662 + 0.2346 + 1.2308 + 0.5906 + 0.0689 + 0.0805 + 0.3342 + 0.1863 + 0.1317 + 0.1348 + 0.1880 + 0.5677 + 0.0692 + 0.5541 + 0.3330 + 1.7225 + 0.0342 + 0.3117 + 0.0094                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| After After               | R 2 λ ENC 1.67 0.54 *         | 2.19 ** 2.71 0.41 3.24 ** 3.20 * 0.48 2.51 ** - 1.24 - 4.57 - 1.25 - 1.32 - 16.73 - 0.18 4.14 * 0.18 1.67 * 8.15 *** 0.31 1.30 * 9.15 *** 0.56 3.12 ** 0.15 0.33 2.72 ** - 0.94 0.25 2.39 ** 0.92 0.25 2.44 ** 0.89 0.50 1.95 ** - 1.31 - 11.91 - 0.24 0.32 0.48 0.74 - 0.99 - 3.12 - 0.86 6.63 ** 0.53 3.01 ** 15.72 *** 1.34 7.62 *** 13.81 ** - 0.07 - 1.26 - 0.45 3.39 ** - 0.07 0.59                                                                                                                                                                                                                                                                       |
| Data After 1965           | ENC Delta1 RMSE ∗ Delta1 ∗ r  | * + 0.0664 - * + 0.0749 - ** + 0.1508 - 0.45 + 0.7545 + 0.03 + 0.0134 - * + 0.0559 - * + 0.0805 - ** + 0.3342 - ** + 0.1790 - ** + 0.1447 - ** + 0.1300 - * + 0.0977 - 0.30 + 0.6395 + 0.78 + 0.0710 - 0.15 + 0.0429 - ** + 0.3330 - *** + 1.7225 + 1.26 + 0.0342 - ** + 0.3117 - 0.59 + 0.0094 - 1.1268                                                                                                                                                                                                                                                                                                                                                        |
| All                       | λ RMSE 0.40 0.87              | 0.4989 0.30 1.24 0.5389 0.66 1.21 0.4845 8.46 - 0.2858 2.07 0.5937 0.20 1.27 0.7885 0.31 1.30 0.9310 0.56 3.12 0.7106 0.41 2.16 1.3058 0.28 2.39 0.9358 0.24 2.45 8.4290 0.47 1.07 0.8750 10.65 - 0.4999 0.47 0.3808 1.48 - 15.1368 0.53 3.01 0.1950 1.34 7.62 0.3315 0.07 - 0.4666 0.45 3.39 0.3185 0.07                                                                                                                                                                                                                                                                                                                                                       |
| All data After 20 years   | Delta1 RMSE ∗ Delta1 RMSE ∗ r | 0.0084 - 0.2583 0.0614 - 0.5713 0.0074 - 0.2266 0.2135 + 0.0960 - 0.2387 - 0.6475 0.2532 - 0.0575 0.0619 - 0.2708 0.3917 - 0.0564 0.1031 - 1.2425 0.0971 - 0.7012 0.2077 - 0.1412 0.0433 - 1.0292 0.1503 - 0.9718 - 0.0501 - 0.3698 0.2019 - 0.4520 - 0.3330 - 0.1950 1.7225 + 0.3315 0.1607 + 0.0160 - 0.3117 - 0.3185 0.1870 + 0.0739                                                                                                                                                                                                                                                                                                                         |
|                           | R 2 λ ENC 0.49                | 0.21 0.48 + 0.91 0.38 1.94 + 1.08 0.22 0.40 + - 0.75 - 1.73 - 1.46 + - 0.76 - 0.42 - 4.74 + 3.20 * 0.49 4.16 ** + 8.15 *** 0.31 1.46 + 9.15 *** 0.67 4.45 ** + 0.34 0.39 2.14 * + - 0.63 0.29 2.67 * + 0.99 0.31 4.55 ** + 0.16 0.38 0.93 + - 4.18 - 2.62 - 0.48 + 0.40 0.44 0.87 + - 1.00 - 2.46 - 0.68 + 6.63 ** 0.53 3.01 ** + 15.72 *** 1.34 7.62 *** + 13.81 ** 0.13 4.86 + - 0.45 3.39 ** + - 0.24 4.82 +                                                                                                                                                                                                                                                 |
| Estimation: OOS Forecast: | Data d/p                      | Dividend Price Ratio 1872-2005 d/y Dividend Yield 1872-2005 e/p Earning price ratio 1872-2005 d/e Dividend payout ratio 1872-2005 svar Stock variance 1885-2005 b/m Book to market 1921-2005 ntis Net equity expansion 1927-2005 eqis Pct equity issuing 1927-2005 tbl Treasury-bill rate 1920-2005 lty Long term yield 1919-2005 ltr Long term return 1926-2005 tms Term Spread 1920-2005 dfy Default yield spread 1919-2005 dfr Default Return Spread 1926-2005 infl Inflation 1919-2005 i/k Invstmnt capital ratio 1947-2005 cayp Cnsmptn, wlth, incme 1945-2005 all Kitchen sink 1927-2005 caya Cnsmptn, wlth, incme 1945-2005 ms Model Selection 1927-2005 |


<!-- p:46 -->


| Delta1 RMSE ∗ r               | - 0 . 0109 - 0 . 0084 - 0 . 0172 + 0 . 0003 + 0 . 0060 - 0 . 0007 - 0 . 0260 - 0 . 0180 - 0 . 0218 - 0 . 0161 - 0 . 0234 - 0 . 0538 - 0 . 0197 - 0 . 0221 - 0 . 0541 - 0 . 0366 - 0 . 0245                                                                                                                                                                                    |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 196501 Delta1 RMSE ∗          | + 0 . 0063 + 0 . 0078 + 0 . 0039 + 0 . 0152 + 0 . 0184 + 0 . 0219 + 0 . 0003 + 0 . 0058 + 0 . 0110 + 0 . 0086 + 0 . 0014 + 0 . 0076 + 0 . 0019 + 0 . 0000 + 0 . 0030 + 0 . 0040 + 0 . 0009                                                                                                                                                                                    |
| After ENC                     | 2 . 67 ** 3 . 90 ** 3 . 08 ** - 3 . 01 - 0 . 32 5 . 50 *** 0 . 89 2 . 77 ** 4 . 86 *** 5 . 47 *** 1 . 02 * 2 . 37 ** 0 . 20 - 0 . 01 0 . 58 5 . 88 ** 1 . 39                                                                                                                                                                                                                  |
| λ                             | 0 . 53 0 . 45 0 . 28 - 1 . 12 - 12 . 93 0 . 82 0 . 07 0 . 47 0 . 51 0 . 35 0 . 30 0 . 73 2 . 15 - 0 . 03 1 . 19 0 . 14 0 . 14                                                                                                                                                                                                                                                 |
| Delta1 RMSE ∗ r               | - 0 . 0134 - 0 . 0115 - 0 . 0135 - 0 . 0146 + 0 . 0046 - 0 . 0138 - 0 . 0416 - 0 . 0055 - 0 . 0222 - 0 . 0084 - 4 . 0129 - 0 . 0311 - 0 . 0070 - 0 . 0134 - 0 . 0114 - 0 . 0150 - 0 . 0232                                                                                                                                                                                    |
| 194701 Delta1 RMSE ∗          | + 0 . 0065 + 0 . 0083 + 0 . 0097 + 0 . 0000 + 0 . 0172 + 0 . 0093 + 0 . 0016 + 0 . 0075 + 0 . 0081 + 0 . 0079 + 0 . 0003 + 0 . 0050 + 0 . 0008 + 0 . 0018 + 0 . 0021 + 0 . 0008 + 0 . 0004                                                                                                                                                                                    |
| After ENC                     | 4 . 14 ** 6 . 53 *** 9 . 27 *** - 0 . 22 - 0 . 47 6 . 21 *** 3 . 04 ** 4 . 28 ** 5 . 47 ** 7 . 57 *** - 0 . 77 2 . 51 ** - 0 . 27 - 0 . 72 0 . 69 4 . 39 1 . 51                                                                                                                                                                                                               |
| λ                             | 0 . 53 0 . 43 0 . 35 - 0 . 02 - 12 . 30 0 . 38 0 . 18 0 . 60 0 . 50 0 . 35 - 0 . 15 0 . 68 - 1 . 04 - 0 . 85 1 . 01 0 . 05 0 . 09                                                                                                                                                                                                                                             |
| R 2                           | 0 . 15 0 . 25 * 0 . 54 ** 0 . 01 - 0 . 08 0 . 92 *** 0 . 40 ** 0 . 75 *** 0 . 11 - 0 . 01 0 . 04 0 . 07 - 0 . 07 - 0 . 02 - 0 . 00 1 . 98 *** -                                                                                                                                                                                                                               |
| OOS Forecast: Data            | 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 193705-200212 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512 192701-200512                                                                                                                                 |
| Table 6 panel B: Monthly Data | d/p Dividend price ratio d/y Dividend yield e/p Earning price ratio d/e Dividend payout ratio svar Stock variance csp Cross-sectional prem b/m Book to market ntis Net equity expansion tbl Treasury-bill rate lty Long term yield ltr Long term return tms Term spread dfy Default yield spread dfr Default return spread infl Inflation all Kitchen sink ms Model selection |


<!-- p:47 -->


In sum, ''learned shrinking'' does not improve any of our models to the point where we would expect them to outperform.

## 7. Other Literature

Our article is not the first to explore or to be critical of equity premium predictions. Many bits and pieces of evidence we report have surfaced elsewhere, and some authors working with the data may already know which models work, and when and why-but this is not easy to systematically determine for a reader of this literature. There is also a publication bias in favor of significant results-nonfindings are often deemedless interesting. Thus, the general literature tenet has remained that the empirical evidence and professional consensus is generally supportive of predictability. This is why we believe that it is important for us to review models in a comprehensive fashion-variable-wise, horizon-wise, and time-wise-and to bring all variables up-to-date. The updating is necessary to shed light on post-Oil Shock behavior and explain some otherwise startling disagreements in the literature.

There are many other articles that have critiqued predictive regressions. In the context of dividend ratios, see, for example, Goetzmann and Jorion (1993) and Ang and Bekaert (2003). A number of articles have also documented low IS power [e.g., see Goetzmann and Jorion (1993), Nelson and Kim (1993), and Valkanov (2003)). We must apologize to everyone whose article we omit to cite here-the literature is simply too voluminous to cover fully.

The articles that explore model instability and/or OOS tests have the closest kinship to our own. The possibility that the underlying model has changed(oftenthroughregimeshifts)hasalsobeenexploredinsucharticles as Heaton and Lucas (2000), Jagannathan, McGrattan and Scherbina (2000), Bansal, Tauchan and Zhou (2003), and Kim, Morley, and Nelson (2005), and Lettau and Nieuwerburgh (2005). Interestingly, Kim, Morley, and Nelson (2005) cannot find any structural univariate break post WW II. Bossaerts and Hillion (1999) suggest one particular kind of change in the underlying model-a disconnect between IS and OOS predictability because investors themselves are learning about the economy.

Again, many of the earlier OOS tests have focused on the dividend ratios.

- Fama and French (1988) interpret the OOS performance of dividend ratios to have been a success. Our article comes to the opposite conclusion primarily because we have access to a longer sample period.
- Bossaerts and Hillion (1999) interpret the OOS performance of the dividend yield (not dividend price ratio) to be a failure, too. However, they rely on a larger cross-section of 14 (correlated) countries and not


<!-- p:48 -->


- on a long OOS time period (1990-1995). Because this was a period when the dividend yield was known to have performed poorly, the findings were difficult to generalize.
- Ang and Bekaert (2003) similarly explore the dividend yield in a more rigorous structural model. They, too, find poor OOS predictability for the dividend yield.
- GoyalandWelch(2003) explore the OOS performance of the dividend ratios in greater detail on annual horizons. (Our current article has much overlap in perspective, but little overlap in implementation.)

Lettau and Ludvigson (2001) run rolling OOS regressions-but not in the same spirit as our article: the construction of their cay variable itself relies on ex-post coefficient knowledge. This thought experiment applies to a representative investor who knows the full-sample estimation coefficients for cay , but does not know the full-sample predictive coefficients. This is not the experiment our own article pursues. (Lettau and Ludvigson (2001) also do not explore their model's stability, or note its performance since 1975.) Some tests are hybrids between IS and OOS tests (as are our encompassing tests). For example, Fisher and Statman (2006) explore mechanical rules based on P/E and dividend-yield ratios, which are based on prespecified numerical cutoff values. None works robustly across countries.

Most of the above articles focus on a relatively small number of models. There are at least three studies in which the authors seek to explore more comprehensive sets of variables:

- Pesaran and Timmermann (1995) (and others) point out that our profession has snooped data (and methods) in search of models that seem to predict the equity premium in the same single U.S. or OECD data history. Their article considers model selection in great detail, exploring dividend yield, earnings-price ratios, interest rates, and money in 2 9 = 512 model variations. Their data series is monthly, begins in 1954, and ends (by necessity) 12 years ago in 1992. They conclude that investors could have succeeded, especially in the volatile periods of the 1970s (i.e., the Oil Shock). But they do not entertain the historical equity premium mean as a NULL hypothesis, which makes it difficult to compare their results to our own. Our article shows that the Oil Shock experience generally is almost unique in making many predictive variables seem to outperform. Still, even including the 2-year Oil Shock period in the sample, the overall OOS performance of our ALTERNATIVE models is typically poor.
- Ferson, Sarkissian and Simin (2003) explore spurious regressions and data mining in the presence of serially correlated independent variables. They suggest increasing the critical t -value of the IS regression. The article concludes that ''many of the regressions in the literature, based on individual predictor variables, may be spurious.''


<!-- p:49 -->


Torous and Valkanov (2000) disagree with Ferson, Sarkissian, and Simin. They find that a low signal-noise ratio of many predictive variables makes a spurious relation between returns and persistent predictive variables unlikely and, at the same time, would lead to no OOS forecasting power.

- Anindependent study, Rapach and Wohar (2006), is perhaps closest to our article. It is also fairly recent, fairly comprehensive, and explores OOS performance for a number of variables. We come to many similar conclusions. Their study ends in 1999, while our data end in 2005-a fairly dramatic five years. Moreover, our study focuses more on diagnosis of weaknesses, rather than just on detection. 13

## 8. Conclusion

Findings: Our article systematically investigates the IS and OOS performance of (mostly) linear regressions that predict the equity premium with prominent variables from earlier academic research. Our analysis can be regarded as conservative because we do not even conduct a true OOS test-we select variables from previously published articles and include the very same data that were used to establish the models in the first place. We also ignore the question of how a researcher or investor would have known which among the many models we considered would ultimately have worked.

There is one model for which we feel judgment should be reserved ( eqis ), and some models that deserve more investigation on very-long term frequencies (5 years). None of the remaining models seems to have worked well. To draw this conclusion, our article relies not only on the printed tables in this final version, but on a much larger set of tables that explore combinations of modified data definitions, data frequencies, time periods, econometric specifications, etc). 14 Our findings are not driven by a few outlier years. Our findings do not disappear if we use different definitions and corrections for the time-series properties of the independent variable. Our findings do not arise because our tests have weak power (which would have manifested itself mostly in poor early predictions). Our findings hold up if we apply statistical corrections, data driven model selection, and encompassing tests.

13 Another study by Guo (2006) finds that svar has OOS predictive power. However, Guo uses post WW II sample period and downweights the fourth quarter of 1987 in calculating stock variance. We check that this is why he can find significance where we find none. In the pre-WW2 period, there are many more quarters that have even higher stock variance than the fourth quarter of 1987. If we use a longer sample period, Guo's results also disappear regardless of whether we downweight the highest observation or not.

14 The tables in this article have been distilled from a larger set of tables, which are available from our website-and on which we sometimes draw in our text description of results.


<!-- p:50 -->


Instead, our view based on this evidence is now that most models seem unstable or even spurious. Our plots help diagnose when they performed well or poorly, both IS and OOS. They shine light on the two most interesting subperiods, the 1973-75 Oil Shock, and the most recent 30 years, 1975 till today. (And we strongly suggest that future articles proposing equity premium predictive models include similar plots.) If we exclude the Oil Shock, most models perform even worse-many were statistically significant in the past only because of the stellar model performance during these contiguous unusual years. One can only imagine whether our profession would have been equally comfortable rationalizing away these years ''as unusual'' if they had been the main negative and not the main positive influence.

As of the end of 2005, most models have lost statistical significance, both IS and OOS. OOS, most models not only fail to beat the unconditional benchmark (the prevailing mean) in a statistically or economically significant manner, but underperform it outright. If we focus on the most recent decades, that is, the period after 1975, we find that no model had superior performance OOS and few had acceptable performance IS. With 30 years of poor performance, believing in a model today would require strong priors that the model is well specified and that the underlying model has not changed.

Of course, even today, researchers can cherry-pick models-intentionally or unintentionally. Still, this does not seem to be an easy task. It is rare that a choice of sample start, data frequency, and method leads to robust superior statistical performance IS. Again, to ignore OOS tests even as a diagnostic, a researcher would have to have supreme confidence that the underlying model is stable. Despite extensive search, we were unsuccessful in identifying any models on annual or shorter frequency that systematically had both good IS and OOS performance, at least in the period from 1975 to 2005-although more search might eventually produce one. To place faith in a model, we would want to see genuine superior and stable IS and OOS performance in years after the model identification. Switching perspective from a researcher to an investor, we believe the evidence suggests that none of the academic models we reexamine warrants a strong investment endorsement today. By assuming that the equity premium was ''like it always has been,'' an investor would have done just as well.

Directions: An academic researcher could explore more variables and/or more sophisticated models (e.g., through structural shifts or Kalman filters). Alternatively, one could predict disaggregated returns, for example, the returns on value stocks and the returns on growth stocks. The former could respond more strongly to dividends, while the latter could respond more strongly to book-to-market factors. However, such explorations aggravate the problems arising from (collective) specification search. Some of these models are bound to work both IS or OOS by pure chance. At the very least, researchers should wait for more new OOS data to become available in order to accumulate faith in such new variables or more sophisticated models.


<!-- p:51 -->


Having stated the obvious, there are promising directions. We are looking forward to accumulating more data. Lettau and Van Nieuwerburgh (2005) model structural change not on the basis of the forecasting regression, but on the basis of mean shifts in the dependent variables. This reduces (but does not eliminate) snooping bias. Another promising method relies on theory-an argument along the line of Cochrane's (2005) observation that the dividend yield must predict future returns eventually if it fails to predict dividend growth. 15

Broader Implications: Our article is simple, but we believe its implications are not. The belief that the state variables that we have explored in our article can predict stock returns and/or equity premia is not only widely held, butthebasisfortwoentireliteratures: one literature on how these state variables predict the equity premium and one literature on how smart investors should use these state variables in better portfolio allocations. This is not to argue that an investor would not update his estimate of the equity premium as more equity premium realizations come in. Updating will necessarily induce time-varying opportunity sets [see Xia (2001) and Lewellen and Shanken (2002)). Instead, our article suggests only that the profession has yet to find some variable that has meaningful and robust empirical equity premium forecasting power, both IS and OOS. We hope that the simplicity of our approach strengthens the credibility of our evidence.

### Website Data Sources

Robert Shiller's Website: http://aida.econ.yale.edu/ ∼ shiller/data.htm. NBER Macrohistory Data Base: http://www.nber.org/databases/ macrohistory/contents/chapter13.html.

FRED: http://research.stlouisfed.org/fred2/categories/22.

Value-Line: http://www.valueline.com/pdf/valueline 2005.pdf.

Bureau of Labor Statistics Webpage:

http://www.bls.gov/cpi/

, http://pages.stern.nyu.edu/

Martin Lettau's Webpage: (cay)

mlettau/.

, http://schwert.ssb.rochester.edu/.

William Schwert's Webpage: (svar)

Jeff Wurgler's Webpage: (eqis)

∼

, http://pages.stern.nyu.edu/ ∼ jwurgler/

15 We do not agree with all of Cochrane's (2005) conclusions. He has strong priors, placing full faith in a stationary specification of the underlying model-even though Goyal and Welch (2003) have documented dramatic increases in the autocorrelation of dividend growth. Therefore, he does not consider whether changes in the model over the last 30 years could lead one to the conclusion that dividend ratios do not predict as of 2006 . He also draws a stark dichotomy between a NULL (no return prediction, but dividend growth prediction) and an ALTERNATIVE (no dividend growth prediction, but return prediction). He evaluates both hypotheses separately for dividend growth and return predictability. He then proceeds under unconditional confidence in the ALTERNATIVE to show that if dividend growth rates are truly unpredictable, then dividend ratios increase in significance to conventional levels. With residual doubts about the ALTERNATIVE, this conclusion could change.


<!-- p:52 -->


The Review of Financial Studies / v 21 n 4 2008

<!-- END SOURCE 38/40: Welch_2008_equity-premium-prediction.md -->

---
