---
id: "36_Multiple_Structural_Changes"
source_pdf: "../pdf/36_Multiple_Structural_Changes.pdf"
source_filename: "36_Multiple_Structural_Changes.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 98.0
visual_assets: "disabled"
---

<!-- p:1 -->

## Estimating and Testing Linear Models with Multiple Structural Changes

Jushan Bai; Pierre Perron

Econometrica, Vol. 66, No. 1 (Jan., 1998), 47-78.

Stable URL:

http://links.jstor.org/sici?sici=0012-9682%28199801%2966%3A1%3C47%3AEATLMW%3E2.0.CO%3B2-3

Econometrica is currently published by The Econometric Society.

Your use of the JSTOR archive indicates your acceptance of JSTOR's Terms and Conditions of Use, available at t s ts nd s omd  s  t n  oos  s /ou have obtained prior permission, you may not download an entire issue of a journal or multiple copies of articles, and you may use content in the JSTOR archive only for your personal, non-commercial use.

Please contact the publisher regarding any further use of this work. Publisher contact information may be obtained at http://www.jstor.org/journals/econosoc.html.

Each copy of any part of a JSTOR transmission must contain the same copyright notice that appears on the screen or printed page of such transmission.

JSTOR is an independent not-for-profit organization dedicated to creating and preserving a digital archive of scholarly journals. For more information regarding JSTOR, please contact support@jstor.org.

<!-- p:2 -->


Econometrica, Vol. 66, No. 1 (January, 1998), 47–78

### ESTIMATING AND TESTING LINEAR MODELS WITH MULTIPLE STRUCTURAL CHANGES

BY JUSHAN BAI AND PIERRE PERRON1

This paper considers issues related to multiple structural changes, occurring at unknown dates, in the linear regression model estimated by least squares. The main aspects are the properties of the estimators, including the estimates of the break dates, and the construction of tests that allow inference to be made about the presence of structural change and the number of breaks. We consider the general case of a partial structural change model where not all parameters are subject to shifts. We study both fixed and shrinking magnitudes of shifts and obtain the rates of convergence for the estimated break fractions. We also propose a procedure that allows one to test the null hypothesis ohtir s i s     is t  vss   is o useful in that it allows a specific to general modeling strategy to consistently determine the appropriate number of changes present. An estimation strategy for which the location of the breaks need not be simultaneously determined is discussed. Instead, our method successively estimates each break point.

KEYwoRDs: Asymptotic distribution, change point, rate of convergence, model selection.

## 1. INTRODUCTION

THIS PAPER CONSIDERS ISSUES related to multiple structural changes in the linear regression model estimated by minimizing the sum of squared residuals. Throughout, we treat the dates of the breaks as unknown variables to be estimated. The main aspects considered are the properties of the estimators, including the estimates of the break dates, and the construction of tests that allow inference to be made about the presence of structural change and the number of breaks.

Both the statistics and econometrics literature contains a vast amount of work on issues related to structural change, most of it specifically designed for the case of a single change.2 The econometric literature has witnessed recently an upsurge of interest in extending procedures to various models with an unknown h aouns n n  hun   hn n n ns ec io  nc n o none non ) and Andrews and Ploberger (1994). This issue has also received a lot of attention in the debate on unit root versus structural change in the trend function of a univariate time series (see Perron (1989)). Issues about the distributional properties of the parameter estimates, in particular those of the break dates, have also been considered (see Bai (1994a, b)).

1 This paper has benefited from the comments of seminar participants at Harvard/MIT, Northwestern University, McGill University, the University of Copenhagen, the University of Illinois at Urbana-Champaign, the Université de Montréal, the University of Sao Paulo, PUC at Rio de Janeiro, Hitotsubashi University, the Université de Lausanne, the CREST-INSEE, the European University Institute, the University of York, the University of Pennsylvania, the 1995 Winter Meeting of the Econometric Society, the 1995 Joint Meeting of the Institute of Mathematical Statistics and the Canadian Statistical Association, and the Symposium on Nonlinear Dynamics and Econometrics, Boston. Financial support is acknowledged from the National Science Foundation under Grant SBR-9414083, the Social Sciences and Humanities Research Council of Canada, the Natural Sciences and Engineering Research Council of Canada, and the Fonds pour la Formation de Chercheurs et l'Aide à la Recherche du Québec. Finally, we thank three anonymous referees for their valuable comments.

2 See the surveys of Zacks (1983), Krishnaiah and Miao (1988), and Bhattacharya (1994).


<!-- p:3 -->


In comparison, the literature addressing the issue of multiple structural changes is relatively sparse. Recent developments include Andrews, Lee, and Ploberger (1996) who consider optimal tests in the linear model with known variance. Garcia and Perron (1996) study the sup Wald test for two changes in a dynamic time series. In an independent study, Liu, Wu, and Zidek (1997) consider, as we do, multiple shifts in a linear model estimated by least squares. They study the rate of convergence of the estimated break dates, as well as the consistency of a modified Schwarz model selection criterion to determine the number of breaks. Their analysis considers only the so-called pure-structural change case where all the parameters are subject to shifts. Our assumptions are much less restrictive than those of Liu, Wu, and Zidek (1997), and our main idea of argument differs from theirs. Our model allows for general forms of serial correlation and heteroskedasticity in the errors, lagged dependent variables, trending regressors, as well as different distributions for the errors and the regressors across segments. Furthermore, we consider the more general case of ssts l s r satl  o r   as ats t A partial change model is useful in allowing potential savings in the number of degrees of freedom, an issue particularly relevant for multiple changes. We obtain the rates of convergence for the estimated break points not only for fixed but also for shrinking magnitudes of shifts. The latter is the basis for the derivation of feasible asymptotic distributions and confidence intervals for the break dates.

Our study considers, in addition, the important problem of testing for multiple structural changes for the case with no trending regressors. To that effect, we present sup Wald type tests for the null hypothesis of no change versus an alternative hypothesis containing an arbitrary number of changes. We also propose a test where the alternative specifies an unknown number of changes up to some maximum and a test of the null hypothesis of, say, l changes versus l + 1 changes. The latter is useful for a specific to general modeling strategy to determine the number of changes present. Finally our paper contains a discussion of an estimation strategy for which the locations of the breaks need not be simultaneously determined. Rather our method successively estimates each break point.

The rest of this paper is structured as follows. Section 2 discusses the model and the assumptions imposed on the variables and the errors. Section 3 contains results about the consistency, the rate of convergence, and the asymptotic distribution of the estimates of the break dates (as well as other parameters of the model). Section 4 proposes test statistics, derives their asymptotic distributions, and presents critical values. Section 5 discusses sequential methods to estimate the model without treating all break points simultaneously. All proofs are collected in an appendix.


<!-- p:4 -->


## 2. THE MODEL AND ASSUMPTIONS

Consider the following multiple linear regression with m breaks (m + 1 regimes):

$$( 1 ) \quad y _ { t } = x _ { t } ^ { \prime } \, \beta + z _ { t } ^ { \prime } \, \delta _ { j } + u _ { t } & & ( t = T _ { j - 1 } + 1 , \dots , T _ { j } ) ,$$

I = 1 +    =     n    +   .  =   )p In this model, y, is the observed independent variable, x, (p × 1) and z, (q × 1) are vectors of covariates, and β and δ, (j = 1, .. . , m + 1) are the corresponding vectors of coefficients; u, is the disturbance. The indices (T1,..., T), or the break points, are explicitly treated as unknown. The purpose is to estimate the unknown regression coefficients together with the break points when T observations on (y, x, z,) are available. Note that this is a partial structural change model in the sense that β is not subject to shifts and is effectively estimated using the entire sample. When p = 0, we obtain a pure structural change model where all the coefficients are subject to change.

The multiple linear regression system (1) may be expressed in matrix form as Y = Xβ + Zδ + U, where Y = (y1,. . ., yτ), X = (x1,. . ., xT), U = (u1, . . ., uT), δ = (δi, δ2, . . ., δ' + 1)', and  ̄ is the matrix which diagonally partitions Z at the m-partition (T1, . . ., T), i.e., Z = diag(Z1, . . ., Zm + 1) with Zi = (zTi−1 + 1, · . ., Ti) . Throughout, we denote the true value of a parameter with a 0 superscript. In particular, δ0 = (δ1 ,..., δ + 1) and (T1,..., T0) are, respectively, the true values of the parameters δ and of the break points. The matrix Ž0 is the one which diagonally partitions Z at (T0 , . .., To). Hence the data-generating process is assumed to be

## (2) ∩+080Z+0∂X=X

The goal is first to estimate the unknown coefficients ( β0, 8,..,+1,T1, ..., T0), assuming δi0 ≠ δi+ 1 (1 ≤ k ≤ m). We do not impose the restriction that the regression function is continuous at the turning points. For the latter, readers are referred to Feder (1975) and Gallant and Fuller (1973) for the special case of a polynomial trend regression. This paper focuses on discrete shifts. In general, the number of breaks m can be treated as an unknown variable with true value m0. However, for now, we treat it as known and discuss methods of estimating it in later sections. We also postpone the problem of testing for the presence of structural change to Section 4.

The method of estimation considered is that based on the least-squares principle. For each m-partition (T1,..., T), denoted {T}, the associated leastsquares estimates of β and δ, are obtained by minimizing the sum of squared residuals Σi=1\_T T-1+1[y, −x, β−z,δ. Let β(T}) and δ(T}) denote the resulting estimates. Substituting them in the objective function and denoting the resulting sum of squared residuals as S(T1,..., T), the estimated break points (T1, . .., T m) are such that


<!-- p:5 -->


$$( \hat { T } _ { 1 } , \dots , \hat { T } _ { m } ) = \arg \min _ { T _ { 1 } , \dots , T _ { m } } S _ { T } ( T _ { 1 } , \dots , T _ { m } ) ,$$

where the minimization is taken over all partitions (T1,...,T) such that T- T-1≥q. Thus the break-point estimators are global minimizers of the objective function. Finally, the regression parameter estimates are the associated least-squares estimates at the estimated m-partition {T}, i.e. β = β({T}) and δ = δ({Î}). Note that the break points need not be obtained via an exhaustive grid search. We discuss in Bai and Perron (1996) an efficient algorithm based on the principle of dynamic programming which allows global minimizers to be obtained using a number of sums of squared residuals that is of order O(T2) for any m ≥ 2.

The statistical properties of the resulting estimators are studied in the next section under the following set of assumptions. As a matter of notation, we let ←, 'coti ceooe  coi cone oee." p and"⇒" weak converge in the space D[0, 1] under the Skorohod metric (e.g., Pollard (1984)).

AsSUMPTION A1: Let w, = (x′, zi), W = (w1, . .., WT), and W° be the diagonal prf      =   ns )    or each i = 1,.. . , m + 1, with T0 = 1 and Tm + 1 = T, that Wi Wi0 (Ti0 − Ti− 1) converges in probability to some nonrandom positive definite matrix not necessarily the same for all i.

AssUMPTION A2: There exists an l0 &gt; 0 such that for all l &gt; l0, the minimum away from zero (i = 1, . . . , m + 1).

AssUMPTION A3: The matrix Bkl = Σk zt z′ is invertible for l − k ≥ q, the dimension of z.

The sequence of errors {u,} satisfies one of the following two sets of conditions:

AssUMPTION A4(i): With {Fi:i = 1,2,...} a sequence of increasing σ-fields, assume that {u,F} forms a L'-mixingale sequence with r = 4 + δ for some δ &gt; 0 (McLeish (1975) and Andrews (1988)). That is, there exist nonnegative constants {c: i ≥ 1} and {ψj : j ≥ 0} such that ψ ↓ 0 as j → ∞ and for all i ≥ 1 and j ≥ 0, we have: (a) E|E(ui|Fi−j)|′ ≤ c{ψj, (b) E|ui − E(ui|Fi+j)|′ ≤ cν4j+ 1, (c) maxi ci ≤ K &lt; ∞, (d) Σj= 0j1 +kψj &lt; ∞ for some κ &gt; 0. We also assume (e) that the disturbances u, are independent of the regressors ws for all t and s.


<!-- p:6 -->


:1O

ASsSUMPTION A4(): Let Ft* = σ-field {...,Wt− 1, W1,. .., t−2, u,−1}. We assume (a) that {u,} is a martingale difference sequence relative to {i*} and sup, E\u,|4+c &lt; ∞ for some c &gt; 0; (b) T− 1 ∑[T 1z,z′ →p Q(v) uniformly in v ∈ [0, 1], where Q(v) is positive definite for v &gt; 0 and strictly increasing in v; (c) If the disturbances u, are not independent of the regressors {z} for all t and s, the minimization problem defined by (3) is taken over all possible partitions such that T − Ti− &gt; εT (i = 1, . . . , m + 1) for some ∈ &gt; 0.

ASSUMPTION A5: Ti0 = [Tλ ], where 0 &lt; λ0 &lt; ... &lt; λ0 &lt; 1.

Assumption A1 is standard for multiple linear regressions. Assumption A2 requires that there be enough observations near the true break points so that they can be identified. A2 can be weakened as follows. For some c &gt;0 and values of A,, and A, are bounded away from zero in probability for large T. A3 is imposed because the break points are estimated by a global least-squares search. If the number of observations in each segment is at least some fixed h (h ≥ q, not depending on T), the invertibility requirement in A3 can be weakened to hold for all combinations (l, k) for which l – k ≥ h.3

The assumptions stated in A4 pertain to two specific cases related to the presence or absence of a lagged dependent variable in w,. The conditions described in part (i) pertain to the case where no lagged dependent variables are allowed in w, implied by part (e). In this case, the conditions on the residuals are quite general and allow substantial correlation andheterogeneity. Part (ii) of Assumption A4 considers the case where lagged dependent variables are allowed as regressors. In this case, no serial correlation is permitted in the errors {u,}. This extra generality is obtained at the expense of some restrictions on the admissible partitions if a lagged dependent variable is present in the z,. In such cases, each segment considered to compute global minimizers must contain a positive fraction of the total sample. This is not constraining from a practical point of view since ∈ can be arbitrarily small. Note, however, that this restriction is not necessary if a lagged dependent variable is present only in the x,'s. In both A4(i) and A4(ii), the assumptions are general enough to allow different distributions for both the regressors and the errors in each segment.

The choice between assumptions A4(i) and A4(ii) can be especially interesting in the case of dynamic models when the coefficients associated with the lagged dependent variables are not subject to change. In this case, the investigator can take the dynamic effects into account either in a direct parametric fashion (e.g. introducing lagged dependent variables so as to have uncorrelated residuals) or using an indirect nonparametric approach (e.g. leaving the dynamics in the disturbances and applying a nonparametric correction for proper asymptotic inference).

3 Note that, for the proof of the consistency, A3 could be dispensed using generalized inverses.


<!-- p:7 -->


Assumption A5 is a standard requirement to permit the development of an asymptotic theory and allows the break points to be asymptotically distinct. It considers the asymptotic experiments under the assumption that each segment increases proportionately as the sample size increases. We refer to the quantities λ0 = (λ9, ., λ0) as the break fractions and we let λ0 = 0 and λm + 1 = 1. Finally, we assume that polynomial trending regressors are written in the form of (t/T) (l ≥ 0) or, more generally, written as a continuous function of the time trend, g(t/T) (see Bai (1994b, 1995) for the case of a single break). The consistency and rate of convergence of the estimated break points apply to trending regressors. However, the assumptions in Section 4 for the test statistics rule out trending regressors.

## 3. CONSISTENCY AND LIMITING DISTRIBUTIONS

srno ao   t nso  c  s s ons and their rate of convergence. The latter allow us to derive results about the asymptotic distribution of the estimates (β, δ1, ..., δ + 1, T1, ..., Tm). We let λ = (λ1, . . . , λ) = (T1/T,. . . , Tm/T) with corresponding true values λ0 = (λ0, ..., λo). We shall first show that λ is consistent for λo and later that the rate of convergence is T.

### 3.1. Consistency

The main result of this section is summarized in the following proposition which states the consistency of λ for λ0.

$$P _ { R O P O S I T I O N } \, 1 \colon \, U n d e r \, A 1 { - A 5 } \colon \, \hat { \lambda } _ { k } \to _ { p } \, \lambda _ { k } ^ { 0 } , \, k = 1 , \dots , m .$$

We outline the main steps of the proof using a few lemmas that are proved in the appendix. Denote by û, the estimated residuals and by d, the difference between the fitted and true values. That is, û, = yt − x, β − z, δk, for t ∈ [Tk−1 + 1, Tk] and d, = x′( β − β0) + z′(δk − δj0), for t ∈ [Tk−1 + 1, Tk]∩[Tj−1 + 1, Tj0] (k, j = 1,. .., m + 1). Note that,in general, d, is defined over (m + 1)2 different segments for each of the possible m-partitions {T} and {T0}. Using properties of projections,

$$\left ( 4 \right ) \quad & \frac { 1 } { T } \sum _ { t = 1 } ^ { T } \hat { u } _ { t } ^ { 2 } \leq \frac { 1 } { T } \sum _ { t = 1 } ^ { T } u _ { t } ^ { 2 } , \\$$

and using û, = ut, − dt,

$$\frac { 1 } { T } \sum _ { t = 1 } ^ { T } \hat { u } _ { t } ^ { 2 } = \frac { 1 } { T } \sum _ { t = 1 } ^ { T } u _ { t } ^ { 2 } + \frac { 1 } { T } \sum _ { t = 1 } ^ { T } d _ { t } ^ { 2 } - 2 \frac { 1 } { T } \sum _ { t = 1 } ^ { T } u _ { t } d _ { t } .$$


<!-- p:8 -->


The proof of Proposition 1 simply uses relations (4) and (5) and the associated limit of T-1 Στ= u,d,. We start with the latter.

LEMMA 1: Under A1−A5, we have T− 1 Στ= 1u,d, = op(1).

Lemma 1 together with (4) and (5) implies that T− 1Σt= 1d2 →p 0. The proof 0 p cannot hold if λj ↔p λj for some j. This is stated in the following lemma.

LEMMA 2: Assume A1-A5 hold and that λj →p λj for some j; then

$$\lim _ { T \to \infty } \sup P \left ( T ^ { - 1 } \sum _ { l = 1 } ^ { T } d _ { l } ^ { 2 } > C \| \delta _ { j } ^ { 0 } - \delta _ { j + 1 } ^ { 0 } \| ^ { 2 } \right ) > \epsilon _ { 0 } ,$$

for some C &gt; 0 and ∈0 &gt; 0.

We are now in the position to prove Proposition 1. Using (5) and Lemmas 1 and 2, and under the supposition that some break date is not consistently estimated, we have the inequality

$$T ^ { - 1 } \sum _ { 1 } ^ { T } \hat { u } _ { t } ^ { 2 } \geq T ^ { - 1 } \sum _ { 1 } ^ { T } u _ { t } ^ { 2 } + C \| \delta _ { j } ^ { 0 } - \delta _ { j + 1 } ^ { 0 } \| ^ { 2 } + o _ { p } ( 1 )$$

hon o ws s    s ons oins  w i n inn the inequality (4), which holds with probability 1 for all T. Hence, all break dates are consistently estimated.

### 3.2. Rates of Convergence

We now consider the rate of convergence of the estimates. We start by showing that λk converges to its true value at rate T. More precisely, we have the following proposition.

PROPOsITION 2: Under A1-A5, for every η &gt; 0, there exists a C &lt; ∞, such that for all large T, P(|T(λk − λk)| &gt; C) &lt; η (k = 1, . . . , m).

It is important to remark that the rate T convergence pertains to the estimated break fraction λ and not to T, the estimated break date. For the latter, our result states that with high probability its deviation from the true break is bounded by some constant C that is independent of T, i.e. with high probability, we have |Ti − Ti0| &lt; C.

The rate T convergence of the estimated break fractions allows us to obtain standard root-T asymptotic normality of the estimated coefficients β and δ. The relevant results are stated in the following proposition whose proof is similar to Corollary 1 of Bai (1994b) and is therefore omitted.


<!-- p:9 -->


PROPOSITION 3: Let ê =(β, δ) and θ0 =(β°, δ0). Under A1-A5, √T(ê − Ω= E(UU').

Note that when the errors are serially uncorrelated and homoskedastic we have Φ = σ2V and the asymptotic covariance matrix reduces to σ2V−1, which can be consistently estimated using a consistent estimate of σ2. When serial correlation and/or heteroskedasticity is present, a consistent estimate of Φ can be constructed along the lines of Andrews (1991), assuming identical distributions across segments or allowing the distributions of both the regressors and the errors to differ.

### 3.3. Limiting Distributions of Break Dates

Note first that, as in the single break case, the usual limiting distribution of the break dates obtained specifying fixed magnitude of changes depends on the exact distribution of the pair {z,, u,}. On the other hand, a strategy that permits obtaining pivotal statistics is to consider an asymptotic framework where the magnitudes of the shifts converge to zero as the sample size increases. Even though the setup is particularly well suited to provide an adequate approximation to the exact distribution when the shifts are small, it remains adequate even for moderate shifts. The required conditions are stated in the next assumptions defined for i = 1, .. . , m.

independent of T, where vT &gt; 0 is a scalar satisfying vT → 0 and T(1/2)- d vT →∞ for      &gt;     n   (      of some M &lt; ∞ and all t.

Note that for a smaller magnitude of shift (small vτ), which corresponds to a smaller θ, A6 requires the existence of a higher moment of u,. When vp is a fixed constant, we can choose θ arbitrarily close to 1/2. In this case, the requirement of E|u,|2/θ &lt; M reduces to the existence of 4 + δ moment, as stated in A4.

PROPOSITION 4: Under Assumptions A1-A6, we have for k = 1, ... , m: (i) λk → λk; and (ii) for every η &gt; 0 there exists a C &lt; ∞ such that for all large T, P(\Tv(λk − λ0 )| &gt; C) &lt; η.

Prssso tsna s ao  t  sssn t noent even in the case where the shifts decrease as the sample size increases. The rate of convergence is, of course, no longer T but rather Tv2. This rate is sufficient to establish root-T consistency for the estimated regression parameters. This result will not be presented to save space, and interested readers are referred to Bai (1994a, 1994b) for the case of a single break. Proposition 4 allows us to study the limiting distribution of the estimated break dates. It asserts that we can restrict the analysis to a "neighborhood" of length C/v2 around the true break dates To which makes possible the application of a central limit theorem since this "neighborhood" increases when v decreases. With the mixing assumptions on the errors, each segment is asymptotically distinct and the analysis of the limiting distribution of the break dates is similar to that in the single break case as analyzed in Bai (1994a, 1994b). We provide, in the rest of this section, a description of the results when the data are not trending and under the assumption that the following conditions are satisfied.


<!-- p:10 -->


AsSUMPTION A7: Let ∆Ti0 = Ti0 − Ti− 1; we assume, for i = 1,..., m + 1, that as ∆Ti0 → ∞:

$$\Delta _ { t } ^ { ( 1 ) } \cdot \Delta _ { t - 1 } ^ { ( 0 ) } \sum _ { t = T _ { i - 1 } ^ { 0 } + 1 } ^ { T _ { i - 1 } ^ { 0 } + [ s \Delta T _ { i } ^ { 0 } ] } z _ { t } z _ { t } ^ { \prime } & \to _ { p } s Q _ { i } , \ \ ( \Delta T _ { i } ^ { 0 } ) ^ { - 1 } \sum _ { t = T _ { i - 1 } ^ { 0 } + 1 } ^ { T _ { i - 1 } ^ { 0 } + [ s \Delta T _ { i } ^ { 0 } ] } u _ { t } ^ { 2 } & \to _ { p } s \sigma _ { i } ^ { 2 }$$

and

$$( \Delta T _ { i } ^ { 0 } ) ^ { - 1 } \sum _ { r ^ { \prime } = T _ { r - 1 } ^ { 0 } + 1 } ^ { T _ { i - 1 } ^ { 0 } + [ s \, \Delta T _ { i } ^ { 0 } ] \ T _ { i - 1 } ^ { 0 } + [ s \, \Delta T _ { r } ^ { 0 } ] } E ( z _ { r } z _ { t } ^ { \prime } u _ { r } u _ { t } ) \to _ { p } s \Omega _ { i } \\$$

uniformly in s ∈ [0, 1];

$$( b ) \quad ( \Delta T _ { i } ^ { 0 } ) ^ { - 1 / 2 } \sum _ { t = T _ { i - 1 } ^ { 0 } + 1 } ^ { T _ { i - 1 } ^ { 0 } + [ s \, \Delta T _ { i } ^ { 0 } ] } z _ { t } u _ { t } & = B _ { i } ( S ) \\$$

where B(s) is a multivariate Gaussian process on [0,1] with mean zero and covariance EB(s)B(u) = min{s, u}Ωi.

Now, define for i = 1, ..., m: ξi = ∆iQi+ 1 ∆i/ ∆iQi ∆i, φi,1 = ∆ Ωi ∆i/∆iQi ∆i, φλ,2 = ∆′ Ωi+ 1 ∆i/∆Qi+ 1 ∆i, and let W(i)(s) and Wγi)(s) be independent Wiener processes defined on [0, ∞), starting at 0 when s = 0. These processes are also independent across i. Also, define Z(i)(s) = φi, 1W(i)(−s) − |s|/2, for s ≤ 0, and Z(i)(s) = √ξi φi,2Wγi)(s) − ξi|s|/2, for s &gt; 0. We can state the following result.

PROPOSITION 5: Under A1−A7, (∆Q ∆i)v2(Ti − Ti0) ⇒ argmaxsZ(i)(s) (i = 1,..., m).

The limiting distribution is the same as that occurring in a single break model. The density function of argmaxZ(i)(s) is derived in Bai (1994b) and is nonsymmetric. When the limits Q, Ω, and σ2 are the same for adjacent i's, ξi = 1, and φi,1 = φ,2 ≡ φ, in which case the limiting distribution reduces to:

$$1 , 1 , 1 , 2 & = 1 , 2 \\ ( 6 ) & = \frac { ( \Delta _ { i } ^ { \prime } Q \Delta _ { i } ) ^ { 2 } } { ( \Delta _ { i } ^ { \prime } \Omega \Delta _ { i } ) ^ { 2 } } v _ { T } ^ { 2 } ( \hat { T } _ { i } - T _ { i } ^ { 0 } ) \Rightarrow \arg \max _ { s } \{ W ^ { ( i ) } ( s ) - | s | / 2 \}$$


<!-- p:11 -->


which is symmetric about the origin and has distribution function (see Yao (1987)):

$$H ( x ) & = 1 + ( 2 \pi ) ^ { - 1 / 2 } \sqrt { x } e ^ { - x / 8 } - \frac { 1 } { 2 } ( x + 5 ) \Phi ( - \sqrt { x } / 2 ) \\ & + \frac { 3 } { 2 } e ^ { x } \Phi ( - 3 \sqrt { x } / 2 ) , \\$$

for x &gt; 0 and H(x) = 1 − H(−x), with Φ(x) the distribution function of a standard normal variable. For instance the 95% and 97.5% quantiles are 7.7 and 11.0.

The results discussed above allows easy construction of confidence intervals for the break dates. All that is needed is to construct consistent estimates of the various parameters; T− 1Σt= 1z, z′ for Q, T− 1Σt= 1u2 for σ2, and δi+ 1 − δi for vτ ∆j. When serial correlation is present, Ω can be estimated using a kernelbased method as discussed in Andrews (1991). Note that when the segments are not homogeneous, obtaining consistent estimates is still possible using data over the relevant subsamples only.

The limiting distribution in the case of trending regressors is discussed in Bai (1994b, 1995) for a single structural change model. His results remain valid for multiple breaks. We omit the details and refer the reader to those papers.

## 4. TEST STATISTICS FOR MULTIPLE BREAKS

### 4.1. A Test of No Break Versus Some Fixed Number of Breaks

s ( = e rr s r t t l  un  sl the alternative hypothesis that there are m = k breaks. Let (T1,..., Tk) be a partition such that Ti = [Tλ] (i = 1, . . . , k). Define

$$F _ { T } ( \lambda _ { 1 } , \dots , \lambda _ { k } ; q ) = \left ( \frac { T - ( k + 1 ) q - p } { k q } \right ) \frac { \hat { \delta } ^ { \prime } R ^ { \prime } \left ( R ( \bar { Z } ^ { \prime } M _ { X } \bar { Z } ) ^ { - 1 } R ^ { \prime } \right ) ^ { - 1 } R \hat { \delta } } { S S R _ { k } }$$

where R is the conventional matrix such that (Rδ) = (δi − δ2,  ., δk − δk+ 1) and Mx = I − X(X'X)−1X'. Here SSRk is the sum of squared residuals under the alternative hypothesis, which depends on (T1,...,Tk). To carry out the asymptotic analysis, we need to impose some restrictions on the possible values o   da d t    da d s dau  to asymptotically distinct and bounded from the boundaries of the sample. To this effect, we define the following set for some arbitrary small positive number e: Λe = {(λ1, . . . , λk); |λi + 1 − λj| ≥ ∈, λ1 ≥ ∈, λk ≤ 1 − ∈}. The sup F type test statistic is then defined as supFT(k; q) = sup(λ,.., λk)∈ A FT(λ1,..., λk; q). It is a generalization of the sup F test considered by Andrews (1993) and others for the case k = 1. The limiting distribution of the test depends on the nature of the regressors and the presence or absence of serial correlation and heterogeneity in the residuals. We consider the case where the following assumptions are imposed.


<!-- p:12 -->


AssUMPTION A8: T−1 Σ[Tslw,w′ →p sQ, uniformly in s ∈ [0, 1], for Q some positive definite matrix.

Note that A8 precludes the presence of trending regressors. Extensions to the general case where plimτ → ∞T− 1 Σ[Ts}w,w′ = Q(s), which allows trending regressors, are beyond the scope of the present paper.

AssUMPTION A9: The errors {u} form an array of martingale differences relative to {F} = σ-field {..., Wt− 1,W1, ..., ut−2, u1− 1}. Also, E[u2] = σ2 for all t and T−1/2Σ[=1w,u, ⇒ σQ1/2W*(r), with W*(r) a (p + q) vector of independent Wiener processes.

The case where {u} satisfies the general conditions stated in Assumption A4 is discussed in Section 4.4 below. We show how the results remain valid provided appropriate modifications are made to account for the effect of serial correlation on the asymptotic distributions. The following proposition is proved in the appendix.

PROPOsITION 6: Let W(·) be a q-vector of independent Wiener processes on def [0, 1]. Under A8−A9 and m = 0, sup FT(k; q) ⇒ sup Fk,q = sup(λ., )∈  F(λ1, .., λk; q), with

$$\dots , \lambda _ { k } ; q ) , \text { with} \\ F ( \lambda _ { 1 } , \dots , \lambda _ { k } ; q ) \\ \stackrel { d e f } { = } \frac { 1 } { k q } \sum _ { i = 1 } ^ { k } \frac { \left [ \lambda _ { i } W _ { q } ( \lambda _ { i + 1 } ) - \lambda _ { i + 1 } W _ { q } ( \lambda _ { i } ) \right ] ^ { \prime } \left [ \lambda _ { i } W _ { q } ( \lambda _ { i + 1 } ) - \lambda _ { i + 1 } W _ { q } ( \lambda _ { i } ) \right ] } { \lambda _ { i } \lambda _ { i + 1 } ( \lambda _ { i + 1 } - \lambda _ { i } ) } .$$

Note that the asymptotic distribution of the test statistic depends on the value of ∈ in ∆€. As ε converges to zero, the critical values of the limiting random variable of supFτ(k; q) diverge to infinity. Because the computed test statistic for a given sample is finite, a small positive value of ε can improve the power significantly; see Andrews (1993) for further details. In what follows, we have adopted ε = 0.05. No critical values for k ≥ 2 are available except those of Garcia and Perron (1996) for k = 2 and q = 1.

Asymptotic critical values are obtained via simulations. The Wiener process W (λ) is approximated by the partial sums n−1/2Σ[nle; with e; i.i.d. N(0, 1) and n = 1,000. The number of replications is 10,000. For each replication, the supremum of F(λ1,..., λk; q) with respect to (λ1,..., λk) over the set Λe is obtained via a dynamic programming algorithm. We present, in Table I, critical values covering cases with up to 9 breaks (k = 1,...,9) and up to 10 regressors (q = 1,..., 10) whose coefficients are the object of the test. The values reported are scaled up by q for comparison purposes. The column corresponding to k = 1 can also be found in Andrews (1993). Because supFT(1; q) ≤ 2 sup FT(2; q) ≤ ksup FT(k; q), the consistency of the supFT(k; q) (k ≥ 2) follows from Andrews (1993) who proved the consistency of supFτ(1; q) for various alternatives including multiple breaks.


<!-- p:13 -->


TABLEI ASYMPTOTIC CRITICAL VALUES OF THE MULTIPLE-BREAK TEST. THE ENTRIES ARE QUANTILES x SUCH THAT P(supFk, q ≤x/q) = α.

|   q | α       |   Number of Breaks, k - 1 | Number of Breaks, k - 2   | Number of Breaks, k - 3   | Number of Breaks, k - 4   | Number of Breaks, k - 5   | Number of Breaks, k - 6   | Number of Breaks, k - 7   | Number of Breaks, k - 8   | Number of Breaks, k - 9   | Number of Breaks, k - UDmax   | Number of Breaks, k - WDmax   |
|-----|---------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|-------------------------------|-------------------------------|
|   1 | .90     |                      8.02 | 7.87                      | 7.07                      | 6.61                      | 6.14                      | 5.74                      | 5.40                      | 5.09                      | 4.81                      | 8.78                          | 9.14                          |
|   1 | .95     |                      9.63 | 8.78                      | 7.85                      | 7.21                      | 6.69                      | 6.23                      | 5.86                      | 5.51                      | 5.20                      | 10.17                         | 10.91                         |
|   1 | .975    |                     11.17 | 9.81                      | 8.52                      | 7.79                      | 7.22                      | 6.70                      | 6.27                      | 5.92                      | 5.56                      | 11.52                         | 12.53                         |
|   1 | .99     |                     13.58 | 10.95                     | 9.37                      | 8.50                      | 7.85                      | 7.21                      | 6.75                      | 6.33                      | 5.98                      | 13.74                         | 15.02                         |
|   2 | .90     |                     11.02 | 10.48                     | 9.61                      | 8.99                      | 8.50                      | 8.06                      | 7.66                      | 7.32                      | 7.01                      | 11.69                         | 12.33                         |
|   2 | .95     |                     12.89 | 11.60                     | 10.46                     | 9.71                      | 9.12                      | 8.65                      | 8.19                      | 7.79                      | 7.46                      | 13.27                         | 14.19                         |
|   2 | .975    |                     14.53 | 12.64                     | 11.20                     | 10.29                     | 9.69                      | 9.10                      | 8.64                      | 8.18                      | 7.80                      | 14.69                         | 16.04                         |
|   2 | .99     |                     16.64 | 13.78                     | 12.06                     | 11.00                     | 10.28                     | 9.65                      | 9.11                      | 8.66                      | 8.22                      | 16.79                         | 18.11                         |
|   3 | .90     |                     13.43 | 12.73                     | 11.76                     | 11.04                     | 10.49                     | 10.02                     | 9.59                      | 9.21                      | 8.86                      | 14.05                         | 14.76                         |
|   3 | .95     |                     15.37 | 13.84                     | 12.64                     | 11.83                     | 11.15                     | 10.61                     | 10.14                     | 9.71                      | 9.32                      | 15.80                         | 16.82                         |
|   3 | .975    |                     17.17 | 14.91                     | 13.44                     | 12.49                     | 11.75                     | 11.13                     | 10.62                     | 10.14                     | 9.72                      | 17.36                         | 18.79                         |
|   3 | .99     |                     19.25 | 16.27                     | 14.48                     | 13.40                     | 12.56                     | 11.80                     | 11.22                     | 10.67                     | 10.19                     | 19.38                         | 20.81                         |
|   4 | .90     |                     15.53 | 14.65                     | 13.63                     | 12.91                     | 12.33                     | 11.79                     | 11.34                     | 10.93                     | 10.55                     | 16.17                         | 16.95                         |
|   4 | .95     |                     17.60 | 15.84                     | 14.63                     | 13.71                     | 12.99                     | 12.42                     | 11.91                     | 11.49                     | 11.04                     | 17.88                         | 19.07                         |
|   4 | .975    |                     19.35 | 16.85                     | 15.44                     | 14.43                     | 13.64                     | 13.01                     | 12.46                     | 11.94                     | 11.49                     | 19.51                         | 20.89                         |
|   4 | .99     |                     21.20 | 18.21                     | 16.43                     | 15.21                     | 14.45                     | 13.70                     | 13.04                     | 12.48                     | 12.02                     | 21.25                         | 22.81                         |
|   5 | .90     |                     17.42 | 16.45                     | 15.44                     | 14.69                     | 14.05                     | 13.51                     | 13.02                     | 12.59                     | 12.18                     | 17.94                         | 18.85                         |
|   5 | .95     |                     19.50 | 17.60                     | 16.40                     | 15.52                     | 14.79                     | 14.19                     | 13.63                     | 13.16                     | 12.70                     | 19.74                         | 20.95                         |
|   5 | .975    |                     21.47 | 18.75                     | 17.26                     | 16.13                     | 15.40                     | 14.75                     | 14.19                     | 13.66                     | 13.17                     | 21.57                         | 23.04                         |
|   5 | .99     |                     23.99 | 20.18                     | 18.19                     | 17.09                     | 16.14                     | 15.34                     | 14.81                     | 14.26                     | 13.72                     | 24.00                         | 25.46                         |
|   6 | .90     |                     19.38 | 18.15                     | 17.17                     | 16.39                     | 15.74                     | 15.18                     | 14.63                     | 14.18                     | 13.74                     | 19.92                         | 20.89                         |
|   6 | .95     |                     21.59 | 19.61                     | 18.23                     | 17.27                     | 16.50                     | 15.86                     | 15.29                     | 14.77                     | 14.30                     | 21.90                         | 23.27                         |
|   6 | .975    |                     23.73 | 20.80                     | 19.15                     | 18.07                     | 17.21                     | 16.49                     | 15.84                     | 15.29                     | 14.78                     | 23.83                         | 25.22                         |
|   6 | .99     |                     25.95 | 22.18                     | 20.29                     | 18.93                     | 17.97                     | 17.20                     | 16.54                     | 15.94                     | 15.35                     | 26.07                         | 27.63                         |
|   7 | .90     |                     21.23 | 19.93                     | 18.75                     | 17.98                     | 17.28                     | 16.69                     | 16.16                     | 15.69                     | 15.24                     | 21.79                         | 22.81                         |
|   7 | .95     |                     23.50 | 21.30                     | 19.83                     | 18.91                     | 18.10                     | 17.43                     | 16.83                     | 16.28                     | 15.79                     | 23.77                         | 25.02                         |
|   7 | .975    |                     25.23 | 22.54                     | 20.85                     | 19.68                     | 18.79                     | 18.03                     | 17.38                     | 16.79                     | 16.31                     | 25.46                         | 26.92                         |
|   7 | .99     |                     28.01 | 24.07                     | 21.89                     | 20.68                     | 19.68                     | 18.81                     | 18.10                     | 17.49                     | 16.96                     | 28.02                         | 29.57                         |
|   8 | .90     |                     22.92 | 21.56                     | 20.43                     | 19.58                     | 18.84                     | 18.21                     | 17.69                     | 17.19                     | 16.70                     | 23.53                         | 24.55                         |
|   8 | .95     |                     25.22 | 23.03                     | 21.48                     | 20.46                     | 19.66                     | 18.97                     | 18.37                     | 17.80                     | 17.30                     | 25.51                         | 26.83                         |
|   8 | .975    |                     27.21 | 24.20                     | 22.41                     | 21.29                     | 20.39                     | 19.63                     | 18.98                     | 18.34                     | 17.78                     | 27.32                         | 28.98                         |
|   8 | .99     |                     29.60 | 25.66                     | 23.44                     | 22.22                     | 21.22                     | 20.40                     | 19.66                     | 19.03                     | 18.46                     | 29.60                         | 31.32                         |
|   9 | .90     |                     24.75 | 23.15                     | 21.98                     | 21.12                     | 20.37                     | 19.72                     | 19.13                     | 18.58                     | 18.09                     | 25.19                         | 26.40                         |
|   9 | .95     |                     27.08 | 24.55                     | 23.16                     | 22.08                     | 21.22                     | 20.49                     | 19.90                     | 19.29                     | 18.79                     | 27.28                         | 28.78                         |
|   9 | .975    |                     29.13 | 25.92                     | 24.14                     | 22.97                     | 21.98                     | 21.28                     | 20.59                     | 19.98                     | 19.39                     | 29.20                         | 30.82                         |
|   9 |         |                     31.66 |                           |                           | 24.01                     | 23.06                     | 22.18                     |                           | 20.63                     |                           | 31.72                         |                               |
|   9 | .99     |                     26.13 | 27.42                     | 25.13                     |                           |                           |                           | 21.35 20.57               |                           | 19.94                     |                               | 33.32                         |
|  10 | .90 .95 |                     28.49 | 24.70 26.17               | 23.48 24.59               | 22.57 23.59               | 21.83 22.71               | 21.16 21.93               | 21.34                     | 20.03 420.74              | 19.55 20.17               | 26.66 28.75                   | 27.79 30.16                   |
|   9 | .975    |                     30.67 | 27.52                     | 25.69                     | 24.47                     | 23.45                     | 22.71                     | 21.95                     | 21.34                     | 20.79                     | 30.84                         | 32.46                         |
|   9 | .99     |                     33.62 | 29.14                     | 26.90                     | 25.58                     | 24.44                     | 23.49                     | 22.75                     | 22.09                     | 21.47                     | 33.86                         | 35.47                         |

Notes: 1. The test UDmax is deined as max1 ≤ k ≤ ssup(λ..λk)∈ A F(λ1,.., Ak; q) multiplied by q. 2. The test WDmax is given in (9) multiplied by q, and M is chosen to be 5.

### 4.2. A Double Maximum Test

The test discussed above requires the specification of the number of breaks, mnt o nt s  nss  ses e st nt  s no structural break against an unknown number of breaks given some upper bound M. Consider the following new class of tests, called the double maximum tests:


<!-- p:14 -->


$$( 8 ) \quad \ D { \max } { F _ { T } ( M , q , a _ { 1 } , \dots , a _ { M ^ { \prime } } ) } = \max _ { 1 \leq m \leq M } a _ { m } \sup _ { ( \lambda _ { 1 } , \dots , \lambda _ { m } ) \in \Lambda _ { c } } F _ { T } ( \lambda _ { 1 } , \dots , \lambda _ { m } ; q ) ,$$

defined for some fixed weights {a1, ... , a}. Note that the asymptotic distribution of this class of tests is easily obtained from Proposition 6. Indeed, we have

$$\ D { \max } { F _ { T } ( M , \L q , a _ { 1 } , \dots , a _ { M } ) } \Rightarrow \max _ { 1 \leq m \leq M } a _ { m } \sup _ { ( \lambda _ { 1 } , \dots , \lambda _ { m } ) \in \Lambda _ { \epsilon } } F ( \lambda _ { 1 } , \dots , \lambda _ { m } ; q ) .$$

The weights may reflect the imposition of some priors on the likelihood of various numbers of breaks. Apart from such considerations, precise theoretical guidelines about their choice remain an open question. An obvious candidate is to set all weights equal to unity and we label this version of the test as UDmax FT(M, q) = max1 ≤ m ≤ sup(λ1,.., ,m) ∈ Λ F T(λ1,. .., λm; q). For a fixed m, F(λ1,..., λ; q) is the sum of m dependent chi-square random variables with q degrees of freedom, each one divided by m. This scaling by m can be viewed, in some sense, as a prior imposed to account for the fact that as m increases a fixed sample of data becomes less informative about the hypotheses being confronted. Since for any fixed q the critical values of the individual tests sup(λ,.., ,)∈ ΛFT(λ1,..., λ; q) decrease as m increases, this implies that the marginal p-values decrease with m and may lead to a test with low power if the number of breaks is large. One way to alleviate this problem is to consider a set of weights such that the marginal p-values are equal across values of m. This implies weights that depend on q and the significance level of the test, say α. To be more precise, let c(q, α,m) be the asymptotic critical value of the test suP(λ..m)∈ FT(λ,..,  q) for a significance level α. The weights are then defined as a1 = 1 and for m &gt; 1 as am = c(q, α, 1)/c(q, α, m). This version is denoted

$$( 9 ) \quad & W d \max F _ { T } ( M , q ) = \max _ { 1 \leq m \leq M } \frac { c ( q , \alpha , 1 ) } { c ( q , \alpha , m ) } \\ & \quad \times \sup _ { ( \lambda _ { 1 } , \dots , \lambda _ { m } ) \in \Lambda _ { \epsilon } } F _ { T } ( \lambda _ { 1 } , \dots , \lambda _ { m } ; q ) . \\$$

The last two columns of Table I report the asymptotic critical values of both tests for M = 5 and ε = 0.05. This should be sufficient for most empirical applications. In any event, the critical values vary little for choices of the upper bound M larger than 5. The consistency of the tests follows directly from the consistency of supFτ(k; q).

### 4.3. Test of l versus l + 1 Breaks

This section considers a test of the null hypothesis of l breaks against the alternative that an additional break exists. Ideally, one would base the test on the difference between the sum of squared residuals obtained with l breaks and that obtained with l + 1 breaks. The limiting distribution of this test statistic is, however, difficult to obtain. Here, we pursue a different strategy. For the model with l breaks, the estimated break points, denoted by 1, ..., Î, are obtained by a global minimization of the sum of squared residuals. Our strategy proceeds by testing each (l + 1) segment (obtained using the estimated partition Î1,..., Î) for the presence of an additional break. We assume the magnitude of shifts is fixed (nonshrinking) in this section.


<!-- p:15 -->


The test amounts to the application of (l + 1) tests of the null hypothesis of no structural change versus the alternative hypothesis of a single change. It is applied to each segment containing the observations Ti-1 + 1 to T (i = 1,..., l + 1) using again the convention that Î0 = 0 and Î1+ 1 = T. We conclude for a rejection in favor of a model with (l + 1) breaks if the overall minimal value of the sum of squared residuals (over all segments where an additional break is included) is sufficiently smaller than the sum of squared residuals from the l break model. The break date thus selected is the one associated with this overall minimum. More precisely, the test is defined by

$$F _ { T } ( l + 1 | l ) & = \left \{ S _ { T } \left ( \hat { T } _ { 1 } , \dots , \hat { T } _ { l } \right ) \\ & - \min _ { 1 \leq i \leq l + 1 } \inf _ { \tau \in \Lambda _ { i , \eta } } S _ { T } \left ( \hat { T } _ { 1 } , .$$

where

$$( 1 1 ) \quad \Lambda _ { i , \, \eta } = \left \{ \tau ; \hat { T } _ { i - 1 } + \left ( \hat { T } _ { i } - \hat { T } _ { i - 1 } \right ) \eta \leq \tau \leq \hat { T } _ { i } - \left ( \hat { T } _ { i } - \hat { T } _ { i - 1 } \right ) \eta \right \}$$

and ô2 is a consistent estimate of σ2 under the null hypothesis. Note that for i = 1, ST(T1,. . ., Ti− 1, τ, Ti, . . ., T1) is understood as ST(τ, T1, . . ., T1) and for i = l + 1 as S(Î1, ..., Î, τ). We have the following result, proved in the Appendix:

PROPOSITION 7: Under Assumptions A8−A9 and m = l: limτ → ∞P(FT(l + 1|l) ≤ x) = Gq,x)+1 with G,η(x) the distibution function of suPn≤ μ≤1-1 (μ)− μW9(1)||2/(μ(1 − μ)).

The critical values of this test for different values of l can be obtained from the distribution function Gq, η(x). A partial tabulation of some percentage points can be found in DeLong (1981) and Andrews (1993) (see also the first column of our Table I). However, the grid presented is not fine enough to allow obtaining the relevant percentage points of Gq, η(x)l+1. Accordingly, we provide a full set of critical values in Table II calculated with η = .05. These were obtained using a simulation method similar to that used for Table I.

Note that ô2 is only required to be consistent under the null hypothesis for the validity of the stated asymptotic distribution. The test may, however, have better power if î2 is also consistent under the alternative hypothesis. Also, it is important to note that the results carry through allowing different distributions across segments for the regressors and the errors. That is, Proposition 7 remains ASYMPTOTIC CRITICAL VALUES OF THE SEQUENTIAL TEST FT(l + 1l).


<!-- p:16 -->


TABLE II

|   q |    α |     0 |     1 |     2 |     3 |   1 4 |     5 | 6 7                     |     8 |     9 |
|-----|------|-------|-------|-------|-------|-------|-------|-------------------------|-------|-------|
|   1 |  .90 |  8.02 |  9.56 | 10.45 | 11.07 | 11.65 | 12.07 | 12.47 14.29             | 13.07 | 13.34 |
|   1 |  .95 |  9.63 | 11.14 | 12.16 | 12.83 | 13.45 | 14.05 | 12.70 14.50 15.73       | 14.69 | 14.88 |
|   1 | .975 | 11.17 | 12.88 | 14.05 | 14.50 | 15.03 | 15.37 | 15.56                   | 16.02 | 16.39 |
|   1 |  .99 | 13.58 | 15.03 | 15.62 | 16.39 | 16.60 | 16.90 | 17.04 17.27 16.12       | 17.32 | 17.61 |
|   2 |  .90 | 11.02 | 12.79 | 13.72 | 14.45 | 14.90 | 15.35 | 15.81                   | 16.44 | 16.58 |
|   2 |  .95 | 12.89 | 14.50 | 15.42 | 16.16 | 16.61 | 17.02 | 17.27 17.55             | 17.76 | 17.97 |
|   2 | .975 | 14.53 | 16.19 | 17.02 | 17.55 | 17.98 | 18.15 | 18.46                   | 18.98 | 19.22 |
|   2 |  .99 | 16.64 | 17.98 | 18.66 | 19.22 | 20.03 | 20.87 | 18.74 20.97 21.19       | 21.43 | 21.74 |
|   3 |  .90 | 13.43 | 15.26 | 16.38 | 17.07 | 17.52 | 17.91 | 18.35 18.61 20.31       | 18.92 | 19.19 |
|   3 |  .95 | 15.37 | 17.15 | 17.97 | 18.72 | 19.23 | 19.59 | 19.94                   | 21.05 | 21.20 |
|   3 | .975 | 17.17 | 18.75 | 19.61 | 20.31 | 21.33 | 21.59 | 21.78                   | 22.41 | 22.73 |
|   3 |  .99 | 19.25 | 21.33 | 22.01 | 22.73 | 23.13 | 23.48 | 22.07 23.70 23.79 20.73 | 23.84 | 24.59 |
|   4 |  .90 | 15.53 | 17.54 | 18.55 | 19.30 | 19.80 | 20.15 | 20.48                   | 20.94 | 21.10 |
|   4 |  .95 | 17.60 | 19.33 | 20.22 | 20.75 | 21.15 | 21.55 | 21.90 22.27             | 22.63 | 22.83 |
|   4 | .975 | 19.35 | 20.76 | 21.60 | 22.27 | 22.84 | 23.44 | 23.74 24.14 25.58       | 24.36 | 24.54 |
|   4 |  .99 | 21.20 | 22.84 | 24.04 | 24.54 | 24.96 | 25.36 | 25.51                   | 25.63 | 25.88 |
|   5 |  .90 | 17.42 | 19.38 | 20.46 | 21.37 | 21.96 | 22.47 | 22.77                   | 23.56 | 23.81 |
|   5 |  .95 | 19.50 | 21.43 | 22.57 | 23.33 | 23.90 | 24.34 | 23.23 24.62 25.14       | 25.34 | 25.51 |
|   5 | .975 | 21.47 | 23.34 | 24.37 | 25.14 | 25.58 | 25.79 | 25.96 26.39             | 26.60 | 26.84 |
|   5 |  .99 | 23.99 | 25.58 | 26.32 | 26.84 | 27.39 | 27.86 | 27.90 28.32             | 28.38 | 28.39 |
|   6 |  .90 | 19.38 | 21.51 | 22.81 | 23.64 | 24.19 | 24.59 | 24.86 25.27             | 25.53 | 25.87 |
|   6 |  .95 | 21.59 | 23.72 | 24.66 | 25.29 | 25.89 | 26.36 | 26.84 27.10             | 27.26 | 27.40 |
|   6 | .975 | 23.73 | 25.41 | 26.37 | 27.10 | 27.42 | 28.02 | 28.39 28.75             | 29.13 | 29.44 |
|   6 |  .99 | 25.95 | 27.42 | 28.60 | 29.44 | 30.18 | 30.52 | 30.64 30.99             | 31.25 | 31.33 |
|   7 |  .90 | 21.23 | 23.41 | 24.51 | 25.07 | 25.75 | 26.30 | 26.74 27.06             | 27.46 | 27.70 |
|   7 |  .95 | 23.50 | 25.17 | 26.34 | 27.19 | 27.96 | 28.25 | 28.64 28.84             | 28.97 | 29.14 |
|   7 | .975 | 25.23 | 27.24 | 28.25 | 28.84 | 29.14 | 29.72 | 30.41                   | 31.09 | 31.43 |
|   7 |  .99 | 28.01 | 29.14 | 30.61 | 31.43 | 32.56 | 32.75 | 30.76 32.90 33.25       | 33.25 | 33.85 |
|   8 |  .90 | 22.92 | 25.15 | 26.38 | 27.09 | 27.77 | 28.15 | 28.61                   | 29.19 | 29.49 |
|   8 |  .95 | 25.22 | 27.18 | 28.21 | 28.99 | 29.54 | 30.05 | 28.90 30.45 30.79       | 31.29 | 31.75 |
|   8 | .975 | 27.21 | 29.01 | 30.09 | 30.79 | 31.80 | 32.50 | 32.81 32.86             | 33.20 | 33.60 |
|   8 |  .99 | 29.60 | 31.80 | 32.84 | 33.60 | 34.23 | 34.57 | 34.75 35.01             | 35.50 | 35.65 |
|   9 |  .90 | 24.75 | 26.99 | 28.11 | 29.03 | 29.69 | 30.18 | 30.61                   | 31.14 | 31.46 |
|   9 |  .95 | 27.08 | 29.10 | 30.24 | 30.99 | 31.48 | 32.46 | 30.93 32.71 32.89       | 33.15 | 33.43 |
|   9 | .975 | 29.13 | 31.04 | 32.48 | 32.89 | 33.47 | 33.98 | 34.25                   | 34.88 | 35.07 |
|   9 |  .99 | 31.66 | 33.47 | 34.60 | 35.07 | 35.49 | 37.08 | 34.74 37.12 37.23 32.78 | 37.47 | 37.68 |
|  10 |  .90 | 26.13 | 28.40 | 29.68 | 30.62 | 31.25 | 31.81 | 32.37                   | 33.09 | 33.53 |
|  10 |  .95 | 28.49 | 30.65 | 31.90 | 32.83 | 33.57 | 34.27 | 34.53                   | 35.33 | 35.65 |
|  10 | .975 | 30.67 | 32.87 | 34.27 | 35.01 | 35.86 | 36.32 | 35.01 36.65 36.90       | 37.15 | 37.41 |
|  10 |  .99 | 33.62 | 35.86 | 36.68 | 37.41 | 38.20 | 38.70 | 38.91 39.09             | 39.11 | 39.12 |

valid under A7 instead of A8-A9, provided 2 is replaced by σ2 2 in (44) of the Appendix.

We next argue that the test based on FT(l + 1|l) is also consistent. If there are more than l breaks and a model with only l breaks is estimated, there must be at least one break that is not estimated. Hence, at least one segment contains a nontrivial break point in the sense that both boundaries of each segment are separated from the true break point by a positive fraction of the total number of observations. For this segment, the supFτ(1; q) test statistic diverges to infinity as the sample size increases since it is consistent. 'Accordingly, the statistic FT(l + 1|l) (computed for l + 1 segments) also diverges to infinity. This shows consistency.


<!-- p:17 -->


### 4.4. Extensions to Serially Correlated Errors

The tests discussed above can be applied without the imposition of serially uncorrelated errors as specified in Assumption A9. A simple modification is to use the following version of the F test instead of that specified in (7):

$$F _ { T } ^ { * } ( \lambda _ { 1 } , \dots , \lambda _ { k } ; q ) = \left ( \frac { T - ( k + 1 ) q - p } { k q } \right ) \hat { \delta } ^ { \prime } R ^ { \prime } ( R \hat { V } ( \hat { \delta } ) R ^ { \prime } ) ^ { - 1 } R \hat { \delta } , \\$$

where (δ) is an estimate of the variance covariance matrix of δ that is robust to serial correlation and heteroskedasticity; i.e. a consistent estimate of

$$V ( \hat { \delta } ) = \text {plim} T \left ( \bar { Z } ^ { \prime } M _ { X } \bar { Z } \right ) ^ { - 1 } \bar { Z } ^ { \prime } \dot { M } _ { X } \Omega M _ { X } \bar { Z } ( \bar { Z } ^ { \prime } M _ { X } \bar { Z } ) ^ { - 1 } .$$

Note that it can be constructed allowing identical or different distributions for the regressors and the errors across segments. In some instances, the form of the statistic reduces in an interesting way. For example, consider a pure structural change model (β = 0) where the explanatory variables are such that plim T− 1Ž'ΩZ = hu(0)plim T- 1Ž'Z with hμ(0) the spectral density function of t  t  ta   n  t   sr th asymptotically equivalent test

$$F _ { T } ^ { * } ( \lambda _ { 1 } , \dots , \lambda _ { k } ; q ) = \left ( \hat { \sigma } ^ { 2 } / \hat { h } _ { u } ( 0 ) \right ) F _ { T } ( \lambda _ { 1 } , \dots , \lambda _ { k } ; q ) ,$$

with ρ2 = T-1Σt=1û2 and hu(0) a consistent estimate of hu(0). Hence, the robust version of the test is simply a scaled version of the original statistic. This is the case, for instance, when testing for a change in mean as in Garcia and Perron (1996).

The computation of the robust version of the F test (12) can be involved especially if a data dependent method is used to construct the robust asymptotic covariance matrix of δ. Since the break fractions are T-consistent even with correlated errors, an asymptotically equivalent version is to first take the supremum of the original F test to obtain the break points, i.e. imposing Ω = σ2I. The robust version of the test is obtained by evaluating (12) and (13) at these estimated break dates.

## 5. SEQUENTIAL METHODS

In this section we discuss issues related to the sequential estimation of the break points. We start, in Section 5.1 with results about the limit of break point estimates in underspecified models. An interesting by-product is a sequential algorithm to estimate models with an unknown number of breaks discussed in Section 5.2.


<!-- p:18 -->


### 5.1. The Limit of Break Point Estimates in Underspecified Models

In this section, we show that the estimate of the break fraction in a single structural change regression applied to data that contain two breaks converges thn  m n e ik n      4a) obtains a similar result (see also Bai (1994c) for an earlier exposition). To present our arguments, we consider a simple three-regime model:

$$y _ { t } = \mu _ { j } + \epsilon _ { t } , \text { if } [ T \lambda _ { j - 1 } ] + 1 \leq t \leq [ T \lambda _ { j } ] ,$$

for j = 1, 2,3 and with ∈, ∼ i.i.d.(0, σ2). Assume μ1 ≠ μ2, μ2 ≠ μ3, and λ1 &lt; λ2, so there are two break points in the model. Let Îa denote the estimated single shift point. Our aim is to show that Îa/T is consistent for either λ, or λ2 depending on the relative magnitudes of the shifts and the spell of each regime. To verify this claim, we examine the global behavior of S(τ), the limit of T−1S([Tτ]). We let S(0) andST(T) be the sum of squared residuals for the full sample without a break and S([Tτ]) is then well defined for all τ∈ [0, 1]. It is not difficult to show that the convergence of T−1Sτ([Tτ]) to S(τ) is uniform in τ ∈ [0, 1]. In particular

$$\frac { 1 } { T } S _ { T } ( [ T \lambda _ { 1 } ] ) \rightarrow _ { p } S ( \lambda _ { 1 } ) = \sigma _ { \epsilon } ^ { 2 } + \frac { ( 1 - \lambda _ { 2 } ) ( \lambda _ { 2 } - \lambda _ { 1 } ) } { 1 - \lambda _ { 1 } } ( \mu _ { 2 }$$

$$( 1 6 ) \quad \frac { 1 } { T } S _ { T } ( [ T \lambda _ { 2 } ] ) \rightarrow _ { p } S ( \lambda _ { 2 } ) = \sigma _ { \epsilon } ^ { 2 } + \frac { \lambda _ { 1 } } { \lambda _ { 2 } } ( \lambda _ { 2 } - \lambda _ { 1 } ) ( \mu _ { 1 } - \mu _ { 2 } ) ^ { 2 } .$$

Without loss of generality we consider the case where S(λ1) &lt; S(λ2); our result is stated in the following lemma.

LEMMA 3: Suppose that the dta are generated by (14) and that S(λ1) &lt; S(λ2); the estimated single break point Ta/T is consistent for λ1.

The assumption that S(λ1) &lt; S(λ2) implies that the first break point is dominating in terms of the relative magnitudes of shifts and the regime spells. The above lemma shows that the sum of squared resiuals is reduced the most when the dominating break is identified. Given that Ta/T is consistent for λ1, one can use the subsample [Ta, T] to estimate another break point associated with a minimized sum of squared residuals for this subsample. The resulting estimate is then consistent for λ2. This follows from the same type of argument because only λ2 can be the dominating break in the sample [Ta, T], even if Ta &lt; [Tλ1].


<!-- p:19 -->


It is relatively straightforward to extend the argument to the case where a one-break model is fitted to a relationship that exhibits more than two breaks. The estimate of the break fraction converges to one of the true break fractions, namely the one which allows the greatest reduction in the sum of squared residuals. It is also conjectured that a similar result holds when, say an m, break model is fitted to a relationship that has m2 breaks (with m2 &gt; m1). Such a general result is not, however, needed for the arguments that follow.

### 5.2. Sequential Estimation of the Break Points

The arguments in Section 5.1 showed that Îa/T is consistent for one of the true break points, the one that allows the greatest reduction in the sum of squared residuals. Suppose, as above, that this break point is λ1, which, in general, may not be known. In that case, we choose one break point either in the intervals [1, Îa] or [Ta, T], such that the sum of squared residuals for all observations [1T] is minimized. Let î be this estimator. With probability tending to 1 as T increaşes, it is easy to show that the estimated break point î will be in the interval [Ta, T]. Similarly, if Ta is actually consistent for λ2 (this will be true if S(λ1) &gt; S(λ2)), the second estimated break point will be iņ [1, Ta]. Generally, let (N1, N2) be the ordered version of (Ta, τ) such that N1 &lt; 2. Then (N1/T, N2/T) is consistent for (λ1, λ2). The preceding argument implies that we can obtain consistent estimates of λ1 and λ2 in a sequential way.

#### 5.2.1. Sequential Estimation with a Known Number of Break Points

The above analysis suggests a straightforward sequential algorithm for estimating models with multiple break points. Consider first the case of a known number of break points, say m. Once the first break point is identified, the sad ai te ss st  aas ss os  s s uns. For each subsample, a one break model is estimated and the second break point is chosen as that break point (of the two obtained) which allows the greatest reduction in the sum of squared residuals. The sample is then partitioned in three regimes and a third break point is selected as the estimate from three estimated one-break models that allows the greatest reduction in the sum of squared residuals. This process is continued until the m break points are selected. It yields consistent estimates of the break points though the estimates are not guaranteed to be identical to those obtained by global minimization. Interestingly, it allows the estimation of models with any fixed number of structural changes using least-squares operations that are only of order O(T).

#### 5.2.2. Sequential Estimation with an Unknown Number of Breaks

Consider now the case of an unknown number of breaks which is likely to be of particular relevance in practice. A standard problem is that an improvement in the objective function is always possible by allowing more breaks. This naturally leads to the consideration of a penalty factor for the increased dimension of a model. Yao (1988) suggests the use of the Bayesian Information Criterion and Liu, Wu, and Zidek (1997) suggest a modified Schwarz' criterion; see also Yao and Au (1989). We propose an alternative method directly related to the sequential procedure outlined above. Start by estimating a model with a n l as l css     t sa  t r break). Then perform parameter-constancy tests for every subsample (those obtained by cutting off at the estimated breaks), adding a break to a subsample associated with a rejection using the test Fτ(l + 1l). This process is repeated by increasing I sequentially until thé test fails to reject the null hypothesis of no additional structural changes. A distinct advantage of such a model selection device over those based on information criteria is that it can easily allow and take into account the effect of possible serial correlation in the errors.


<!-- p:20 -->


Note that the application of the test Fτ(l + 1l) in this sequential context is different from that discussed earlier. Indeed, the result of Proposition 7 is based on having the first I breaks obtained as global minimizers of the sum of squared residuals assuming l breaks. The limiting distribution of the Fτ(l + 1l) test in the sequential setup is the same because rate T convergence still holds, as shown in Bai (1997), when the break points are obtained sequentially.

With probability approaching 1 as the sample size increases, the number of breaks determined this way will be no less than the true number. The procedure does not provide a consistent estimate of the true number of breaks, say m, since it implies a nonzero probability of rejection under the null hypothesis g i t  v  t s  t    tr selecting a model with a larger number of breaks, say m0 +j, is given by α which decreases rapidly. Hence, there is no need (with large probability) to ate    m   ma o  st tal procedure could be made consistent by adopting a significance level for the test Fτ(l + 1|l) that decreases to zero, at a suitable rate, as the sample size increases. A result to that effect is presented in the next proposition whose proof is similar to that of Hosoya (1989) and is, therefore, omitted.

PROPOsITiON 8: Let î be the number of breaks obtained using the sequential method based on the statistic Fτ(l + 1l) applied with some size ατ, and let m0 be the true number of breaks. If απ converges to 0 slowly enough (for the test based on Fτ(l + 1l) to remain consistent), then, under Assumptions A1-A5, P(mî = m0) → 1, as T → ∞.

## 6. CONCLUSIONS

Our analysis has presented a comprehensive treatment of issues related to the estimation of linear models with multiple structural changes, to tests for the presence of multiple structural changes and to the determination of the number of changes present. Our results being asymptotic in nature, there is certainly a need to evaluate the quality of the approximations and the power of the tests in finite samples via simulations. We present such a simulation study in a companion paper, Bai and Perron (1996). Among the topics to be investigated, an important one appears to be the relative merits of different methods to select the number of structural changes. There are, of course, many other issues on the agenda: for instance, extensions of the test procedures to include tests that are optimal with respect to some criteria and extensions to nonlinear models. In addition, while the consistency and rate of convergence for the estimated break points apply to trending regressors, the limiting distributions of the various tests -ie rt  tun  e s     st sts sors.


<!-- p:21 -->


Dept. of Economics, E52-247B, Massachusetts Institute of Technology, Cambridge, MA 02139, U.S.A; jbai@mit.edu

and

Dept. of Economics, Boston University, 270 Bay State Rd., Boston, MA 02215, U.S.A.; perron@bu.edu

Manuscript received September, 1995; final revision received March, 1997.

####### MATHEMATICAL APPENDIX

As a matter of notation, for a sequence of matrices Br, we write Bπ = op(1) if each of its elements is op(1) and likewise for Op(1). For a matrix A, MA = I − PA with PA = A(A'A)−1A'. We use∥·∥ to denote the Euclidean norm, i.e. ∥x∥ = (Σfx2)1/2 for x ∈ RP. For a matrix A, we use the vector-induced norm, i.e. ∥A∥ = supx ≠ 0llAxl/∥x∥. Note that the norm of A is equal to the square root of the maximum eigenvalue of A'A, and thus ∥A∥ ≤ [tr(A'A)]1/2. Also, for a projection matrix P, PA∥l ≤ ∥A∥. Limits are taken as T, the sample size, increases to infinity. We start with a series of lemmas that will be used subsequently. Assumption A5 is assumed throughout.

LEmMA A.1: Let S and V be two matrices having the same number of rows. Then the matrix S'MyS is nondecreasing as more rows are added to the matrix (S, V).

PRooF: Write S = (S1, S2) and V = (VI, V2Y. We need to show that for an arbitrary vector α (having the same dimension as the number of rows of S and V) α'S'MγSα ≥ α'S1 Mν,S1α. Note that α′S'MγSα (α′S1Mν,S1α) is the sum of squares of the residuals from a projection of Sα (S1α) on the space spanned by'V (V1). The inequality is verified using the fact that the sum of squared residuals is nondecreasing as the number of observations increases (here the number of rows of S1 and S). See, e.g., Brown, Durbin, and Evans (1975). Q.E.D.

LEMMA A.2: Under A1, supT1.., ,(X'MzX/T)- 1 = Op(1), where the supremum is taken over alll ( +       = 1   | − 1 −  ns ud sd

PROOF: We have the identity X′MzX = X1Mz1X1 + . +Xm+1Mzm+1Xm+1. Each partition (T1, ..., T) leaves at least one true regime intact. In other words, there exists an i such that (X, Z) contains (X}0, Z0) as a submatrix. We have X/Mz,X≥ X0'Mz0Xi0 using Lemma A.1. Hence (X′MzX/T)−1 ≤ (X1′Mz0Xi/T)−1. This implies |(X′MzX/T)−1∥ ≤ max(X0′Mz0X10/T)−1∥for all partitions. The lemma now follows from Assumption A.1. Q.E.D.


<!-- p:22 -->


LEMMA A.3: Under A1, supT{.., , 'MZ0 = Op(T).

PRooF: Because Mz is a projection matrix, we have ∥X′MzZ0∥≤∥X∥MzZ0∥≤∥X∥∥Z0∥ uniformly over all partitions. The lemma follows from ∥X| ≤ [tr(X'X)]1/2 = O(Tt/2) and similarly ∥|Z0∥= O(T1/2). Q.E.D.

LEMMA A.4: Under A4, there exists α &lt; 1/2 such that supr,.., m PzU∥ = Op(Tα), where the supremum with respect to (T1,...,T) is taken over all possible partitions such that |Ti-1 − T|≥ q (i = 1, ... , m + 1) under Assumption A4(i) and over partitions such that |Ti− 1 − T| ≥ ∈T for some ε &gt; 0 under Assumption A4(ii).

PRooF: Consider first the case where A4(i) is assumed to hold. Because of the independence between zs and u,, we can treat the z,'s as nonstochastic, otherwise conditional arguments can be used. We shall prove that |U′PzU| = Op(T2α) uniformly in T1,..., T. Note that U'PzU is the summation of the m + 1 terms

$$\left ( \sum _ { T _ { i } + 1 } ^ { T _ { i + 1 } } z _ { t } u _ { t } \right ) ^ { \prime } \left ( \sum _ { T _ { i } + 1 } ^ { T _ { i + 1 } } z _ { t } z _ { t } ^ { \prime } \right ) ^ { - 1 } & \left ( \sum _ { T _ { i } + 1 } ^ { T _ { i + 1 } } z _ { t } u _ { t } \right ) , \\$$

for i = 0, ..., m. Thus it suffices to prove that

$$( 1 7 ) \sup _ { 1 \leq k < l \leq T } \left \| \sum _ { l = k } ^ { l } \xi _ { l } \right \| & = O _ { p } ( T ^ { \alpha } ) \\$$

with l − k ≥ q and ξ, = ξ,(k, l) = (Ak1)−1/2z,u, with Akl = Σj=kzjzj. Now

$$with 1 - k \geq q \text { and } \xi , & = \xi _ { k } ( k , l ) = ( A _ { k ^ { \prime } } ) ^ { 1 / 2 } z _ { u _ { 1 } } \text { with } A _ { k _ { 1 } } = \Sigma _ { j = k } ^ { 1 } z _ { j } z _ { j } ^ { 2 } . \text { Now} \\ ( 1 8 ) & \quad P \left ( \sup _ { 1 \leq k < l \leq T } \left \| \sum _ { t = k } ^ { l } \xi _ { l } \right \| > T ^ { \alpha } \right ) \leq \sum _ { k = 1 } ^ { T } \sum _ { l = k + q } ^ { T } P \left ( \left \| \sum _ { t = k } ^ { l } \xi _ { t } \right \| > T ^ { \alpha } \right ) \\ & \leq T ^ { - 2 \alpha s } \sum _ { k = 1 } ^ { T } \sum _ { l = k + q } ^ { T } E \left \| \sum _ { t = k } ^ { l } \xi _ { l } \right \| ^ { 2 s } . \\ \intertext { B y the m i g n a l e p r o w , } \text {by the mixed angle property, we can write } \mu _ { k } = \Sigma _ { k } ^ { \infty } \mu _ { k } \text { with } \mu _ { k } = E ( \mu _ { k } | \mathcal { F } _ { k } ) - E ( \mu _ { k } | \mathcal { F } _ { k } ) .$$

By the mixingale property, we can write u, = Σj= − xujt, with ujt = E(u,|Fτ−j) − E(u,|Ft-j−1) and for each j, {ujt,F-j} is a sequence of martingale differences. Hence, we have ∑/=kξ, = Σj= −∞Σt=k ξjr, where ξj = (Ak1)−1/2z,u jt. By Minkowski's inequality,

$$E \left \| \sum _ { l = k } ^ { l } \xi _ { l } \right \| ^ { 2 s } \leq \left ( \sum _ { j = - \infty } ^ { \infty } \left [ E \left \| \sum _ { l = k } ^ { l } \xi _ { j l } \right \| ^ { 2 s } \right ] ^ { 1 / 2 s } \right ) ^ { 2 s } .$$

A key point is that for fixed j, k, and l, {ξjt,F,\_j} (t = k,..., l) form a sequence of martingale differences. Thus by Burkholder's inequality (Hall and Heyde (1980, p. 23)) there exists a C &gt; 0, only depending on q and s, such that

$$E \left \| \sum _ { l = k } ^ { l } \xi _ { j _ { l } } \right \| ^ { 2 s } & \leq C E \left ( \sum _ { l = k } ^ { l } \| \xi _ { j _ { l } } \| ^ { 2 } \right ) ^ { s } \leq C \left ( \sum _ { l = k } ^ { l } ( \ E | \| \xi _ { j _ { l } } \| ^ { 2 s } ) ^ { 1 / s } \right ) ^ { s } , \\$$

where the second step follows by Minkowski's inequality. Now ∥ξj/|2 = z'(Akl)− 1z,u2. Thus (E∥ξjtl[2s)1/2 = z′(Akl)− 1z,(E|ujt|2s)1/s. By A4(a), for r = 2s, we can show (see Hansen (1991)) (E|uj|25)1/2s ≤ 2c,ψj ≤ 2(maxci)ψj| ≤ Kψj| for all j. It follows that (Ell j||2s)1/s ≤ z(Ak1)− 1z, K2ψj|. Thus from (20),

$$E \left \| \sum _ { t = k } ^ { l } \xi _ { j _ { l } } \right \| ^ { 2 s } \leq C \left ( \sum _ { l = k } ^ { l } z _ { r _ { k } } ^ { \prime } ( A _ { k l } ) ^ { - 1 } z _ { t } K ^ { 2 } \psi _ { | j | } ^ { 2 } \right ) ^ { s } = C ( K \psi _ { | j | } ) ^ { 2 s } q ^ { s }$$


<!-- p:23 -->


where we have used the fact that Σt= k z′(Ak1)− 1 z, = tr((Akl)− 1 Σk z, z′) = tr(I) = q. Using (21) and (19), we have ElΣt= k ξ1|12s ≤ CqK 2s(Σj= − xψj)2s &lt; ∞. Since the bound does not depend on k and 1, this implies, in view of (18), that with 1 − k ≥ q, P(sup1 ≤ k &lt; 1 ≤ τ|Σt= k ξ,|| &gt; Tα) ≤ C1T−2 αs + 2 for some C1 &gt; 0. Let s = 2 + c/2 (the moment of order 4 + c of u, exists by A4(i)); we can choose an α ∈ (0, 2/(4 + c)) such that T−2 αs + 2 → 0. This proves (17) and hence the lemma when A4(i) holds. Consider now the case where A4(ii) is assumed to hold. Here, T-1 [Te1 [t=[Tu]+ 1ztzt → Q(v) − Q(u), and hence (T−1Σ[Te] t=[Tu]+ 1z, zi)−1 → (Q(v) − Q(u))−1 uniformly in v and u such that v − u &gt; ε&gt; 0. Also, T−1/2Σ[Te] {T]+ 1ž,u, = Op(1) uniformly using a functional central limit theorem for martingale differences. Accordingly, |U'PzU| = Op(1) uniformly in T1, . .., T and the statement of the lemma holds with α = 0. Q.E.D.

$$\lim _ { \sup _ { T _ { 1 } , \dots , T _ { m } } \overline { Z } ^ { 0 } P _ { Z } } A _ { U } \colon & \text {Under } A _ { 1 } - A _ { 4 } , \text { for } \text { some } \alpha < 1 / 2 , \text { (a) } \sup _ { T _ { 1 } , \dots , T _ { m } } X ^ { \prime } P _ { Z } U = O _ { p } ( T ^ { \alpha + 1 / 2 } ) ; \text { (b) } \\ \sup _ { T _ { 1 } , \dots , T _ { m } } & \overline { Z } ^ { 0 } P _ { Z } U = O _ { p } ( T ^ { \alpha + 1 / 2 } ) .$$

P0 ∥,X|(τ/1) =|oo:or arguments apply for part (b). Q.E.D.

PROOF OF LEMMA 1: By the definition of d1, Στu,d, = U'X( β − β0) + U'Z*δ − U'Z080 where Z* is the diagonal partition of Z at (T1,..., T). To prove the lemma, it suffices to show T− 1U'X( β − β0) = op(1) and T− 1(U'Z*δ − U'Z080) = op(1). We shall prove a stronger result. Let (T1,..., T) be an arbitrary partition and Z be the associated diagonal partition of Z. Also let β({T}) and δ({T}) be, respectively, the estimates of β and δ corresponding to this same partition. We shall prove

$$\sup _ { T _ { 1 } , \dots , T _ { m } } \frac { 1 } { T } | U ^ { \prime } X ( \hat { \beta } ( \{ T _ { j } \} ) - \beta ^ { 0 } ) | = O _ { p } ( T ^ { - 1 / 2 } ) = o _ { p } ( 1 ) ,$$

$$( 2 3 ) \sup _ { T _ { 1 } , \dots , T _ { m } } \frac { 1 } { T } | U ^ { \prime } \bar { Z }$$

where α is given in Lemma A.4. First consider (22). We can rewrite

$$\hat { \beta } ( \{ T _ { j } \} ) - \beta _ { 0 } = ( X ^ { \prime } M _ { \bar { Z } } X ) ^ { - 1 } \, X ^ { \prime } M _ { \bar { Z } } \bar { Z } ^ { 0 } \delta ^ { 0 } + ( X ^ { \prime } M _ { \bar { Z } } X ) ^ { - 1 } \, X ^ { \prime } M _ { \bar { Z } } U .$$

The first term is Op(1) uniformly over all partitions by Lemmas A.2 and A.3. The second term is Op(T α− 1/2) = op(1) by Lemmas A.2 and A.4 (note that X′MZU = Op(Tα + 1/2)). Thus β(Tj}) − β0 = Op(1) uniformly over all partitions. This implies (22) since U'X = Op(T1/2). Next, from δ({Tj}) = (ZMXZ)− 1Z'MX Y, Mχ X = 0, and (2), we obtain

$$( 2 5 ) \quad U ^ { \prime } \bar { Z } \hat { \delta } ( \{ T _ { j } \} ) - U ^ { \prime } \bar { Z } ^ { 0 } \delta ^ { 0 }$$

$$= U ^ { \prime } \bar { Z } ( \bar { Z } ^ { \prime } M _ { X } \bar { Z } ) ^ { - 1 } \bar { Z } ^ { \prime } M _ { X } \bar { Z } ^ { 0 } \delta ^ { 0 } + U ^ { \prime } \bar { Z } ( \bar { Z } ^ { \prime } M _ { X } \bar { Z } ) ^ { - 1 } \bar { Z } ^ { \prime } M _ { X } U - U ^ { \prime } \bar { Z } ^ { 0 } \delta ^ { 0 } .$$

From the identity

$$( \bar { Z } ^ { \prime } M _ { X } \bar { Z } ) ^ { - 1 } = ( \bar { Z } ^ { \prime } \bar { Z } ) ^ { - 1 } + ( \bar { Z } ^ { \prime } \bar { Z } ) ^ { - 1 } ( \bar { Z } ^ { \prime } X ) ( X ^ { \prime } M _ { \bar { Z } } X ) ^ { - 1 } X ^ { \prime } \bar { Z } ( \bar { Z } ^ { \prime } \bar { Z } ) ^ { - 1 } ,$$

the first term of (25) is equal to

$$U ^ { \prime } \bar { Z } ( \bar { Z } ^ { \prime } M _ { x } \bar { Z } ) ^ { - 1 } \bar { Z } ^ { \prime } M _ { x } \bar { Z } ^ { 0 } \delta ^ { 0 } = U ^ { \prime } P _ { \bar { Z } } [ M _ { x } + X ( X ^ { \prime } M _ { \bar { Z } } X ) ^ { - 1 } X ^ { \prime } P _ { \bar { Z } } M _ { x } ] \bar { Z } ^ { 0 } \delta ^ { 0 } .$$

Because Pz and MX are projection matrices, ∥MχZ0∥≤∥Z0∥= Op(T1/2) and∥X′PzMχZ0∥≤ ∥X∥∥Z0∥ = Op(T). Hence, this term is Op(T α+ 1/2) uniformly over all partitions using Lemmas A.2, A.4, and A.5. Similar arguments show that the second term of (25) is Op(T2α). The last term of (25) is Op(T1/2). Combining these results and noting that 2 α &lt; α + 1/2, we have U'Zδ((T}) − U'Z080 = Op(Tα+ 1/2). This implies (23). Q.E.D.


<!-- p:24 -->


PRoOF OF LEMMA 2: If there exists a break, say λ%, which cannot be consistently estimated, then with some positive probability €0 &gt; 0 there exists a η &gt; 0 such that no estimated break falls in the interval [T(λ% − η), T(λ, + η)] for a subsequence of T (without loss of generality, assume this subsequence is the same as T). Suppose this interval is classified into the kth regime, namely, Tk− i ≤ T(λ0 − η) and T( λj + η) ≤ Tk. Then d, = x( β − β0) + z,( δk − δj0 ) for t ∈ [T( λj − η), Tλj ] and d, = x,( β − β0) + z(δk − δj+ 1) for [Tλj + 1, T(λj + η)]. We have

$$1 _ { k - t } \leq 1 ( \lambda _ { j } - \eta ) \text { and } 1 ( \lambda _ { j } + \eta ) \leq 1 , \text { then } \alpha _ { t } = & x _ { t } ( \beta - \beta ^ { t } ) + z _ { t } ( \delta _ { k } - \delta _ { j } ^ { t } ) \text { for } [ T \lambda _ { j } ^ { 0 } + 1 , T ( \lambda _ { k } ^ { 0 } + \eta ) ] . \text { We have } \\ \text { and } d _ { t } = & x _ { t } ^ { \prime } ( \hat { \beta } - \beta ^ { t } ) + z _ { t } ^ { \prime } ( \hat { \delta } _ { k } - \delta _ { j + 1 } ^ { t } ) \text { for } [ T \lambda _ { j } ^ { 0 } + 1 , T ( \lambda _ { k } ^ { 0 } + \eta ) ] . \text { We have } \\ = & \left ( \begin{array} { c c } T \\ \hat { \delta } _ { k } - \delta _ { j } ^ { t } \end{array} \right ) ^ { 2 } \left ( \begin{array} { c c } \sum _ { i } x _ { i } , x _ { i } ^ { \prime } & \sum _ { i } x _ { i } , z _ { i } ^ { \prime } \\ & 1 \end{array} \right ) \left ( \begin{array} { c c } \hat { \beta } - \beta ^ { t } \\ \sum _ { i } z _ { i } , x _ { i } ^ { \prime } & \sum _ { i } z _ { i } , z _ { i } ^ { \prime } \end{array} \right ) \left ( \begin{array} { c c } \hat { \beta } - \beta ^ { t } \\ \hat { \delta } _ { k } - \delta _ { j } ^ { t } \end{array} \right ) \\ & \quad + \left ( \begin{array} { c c } \hat { \beta } - \beta ^ { t } \\ \hat { \delta } _ { k } - \delta _ { j + 1 } ^ { t } \end{array} \right ) ^ { 2 } \left ( \begin{array} { c c } \sum _ { i } x _ { i } , x _ { i } ^ { \prime } & \sum _ { i } x _ { i } , z _ { i } ^ { \prime } \\ & 2 \end{array} \right ) \left ( \begin{array} { c c } \hat { \beta } - \beta ^ { t } \\ \sum _ { i } z _ { i } , x _ { i } ^ { \prime } & \sum _ { i } z _ { i } , z _ { i } ^ { \prime } \end{array} \right ) \left ( \begin{array} { c c } \hat { \beta } - \beta ^ { t } \\ \hat { \delta } _ { k } - \delta _ { j + 1 } ^ { t } \end{array} \right ) , \\ \text {where } \Sigma _ { i } \text { extends over the set } T ( \lambda _ { j } ^ { 0 } - \eta ) \leq t \leq T \lambda _ { j } ^ { 0 } \text { and } \Sigma _ { i } \text { extends over the set } T$$

where Σ1 extends over the set T(λ% − η) ≤ t ≤ Tλj and Σ2 extends over the set TλI + 1 ≤ t ≤ T( λ0 + η). Let γr and γ be the smallest eigenvalue of the first and second matrices in (27). Then

$$+ \eta , & \text { Let } \gamma _ { f } \text { and } \gamma _ { f } = \text {c} \text { the small} \text { eigenvalue of } \text {i} \text { in the } \text {st} \text { and } \text {second matrix} \text { in } \text {$(} \infty \text {).} \\ & \sum _ { 1 } d _ { f } ^ { 2 } + \sum _ { 2 } d _ { i } ^ { 2 } \geq \gamma _ { r } \left [ \| \hat { \beta } - \beta ^ { \prime } \| ^ { 2 } + \| \hat { \delta } _ { k } - \delta _ { j } ^ { \prime \prime } \| ^ { 2 } \right ] + \gamma _ { f } ^ { * } \left [ \| \hat { \beta } - \beta ^ { \prime \prime } \| ^ { 2 } + \| \hat { \delta } _ { k } - \delta _ { j + 1 } ^ { \prime \prime } \| ^ { 2 } \right ] \\ & \geq \min \{ \gamma _ { r } , \gamma _ { f } ^ { * } \} \left ( \| \hat { \delta } _ { k } - \delta _ { j } ^ { \prime \prime } \| ^ { 2 } + \| \hat { \delta } _ { k } - \delta _ { j + 1 } ^ { \prime \prime } \| ^ { 2 } \right ) \\ & \geq ( 1 / 2 ) \min \{ \gamma _ { r } , \gamma _ { f } ^ { * } \} \| \delta _ { j } ^ { \prime \prime } - \delta _ { j + 1 } ^ { \prime \prime } \| ^ { 2 } .$$

The last inequality follows from

$$( x - u ) ^ { \prime } \, A ( x - a ) + ( x - b ) ^ { \prime } \, A ( x - b ) \geq ( 1 / 2 ) ( a - b ) \, A ( a - b )$$

for an arbitrary positive definite matrix A and for all x. Now the first matrix in (27) can be written as (Tη)(1/Tη)ΣTAy ,w,w′ ≡ (Tη)Ar, say. By A2, the smallest eigenvalue of AT is bounded away T(A9 − n) from zero. Thus the smallest eigenvalue of (Tη)Ar, γr, is of the order Tη. The same can be said for γ. Therefore, Σ{d2 &gt; TCllδj0 − δj+ 1|2 for some C &gt; 0 with probability no less than ∈0 &gt; 0. Q.E.D.

PRoOF OF PRoPOsiTiON 2: Without loss of generality, we assume there are only three breaks (m = 3) and provide an explicit proof of T-consistency for λ2 only. The analysis for λ, and λ3 is virtually the same (and actually simpler) and is thus omitted. For each e &gt; 0, let Ve = {(T1, T2, T3); |T − T| ≤ ∈T}. From Proposition 1, P({T1, T2, T3} ∈ Ve) → 1. Therefore we only need to examine the behavior of the sum of squared residuals, Sτ(T1, T2, T3), for those T, such that |T, − Tj0| &lt; ∈T for all i. Also using an argument of symmetry, we can, without loss of generality, consider the case T2 &lt; T0. For C &gt; 0, define

$$V _ { \epsilon } ( C ) = \{ ( T _ { 1 } , T _ { 2 } , T _ { 3 } ) ; | T _ { i } - T _ { i } ^ { ( 0 ) } | < \epsilon T , 1 \leq i \leq 3 , T _ { 2 } - T _ { 2 } ^ { ( i ) } < - C \} .$$

Thus, V(C) ⊂ Ve. Because Sr(T1, T2, T3) ≤ Sr(T1, T0, Î3) with probability 1, it is enough to show that for each η &gt; 0, there exist C &gt; 0 and e&gt; 0 such that for large T, P(min{ST(T1, T2, T3) − ST(T1, T0, T3)} ≤ 0) &lt; η, or equivalently,

$$P ( \min \{ [ S _ { T } ( T _ { 1 } , T _ { 2 } , T _ { 3 } ) - S _ { T } ( T _ { 1 } , T _ { 2 } ^ { ( i } , T _ { 3 } ) ] / ( T _ { 2 } ^ { ( i } - T _ { 2 } ) \} \leq 0 ) < \eta ,$$


<!-- p:25 -->


where the minimum is taken over the set V€(C). Such a relation would imply tat for a large C, global optimization cannot be achieved on V€(C). Thus with large probability, |T2 − T0| ≤ C. Now denote SSR1 = ST(T1, T2, T3), SSR2 = ST(T1, T2, T3), and introduce SSR3 = ST(T1, T2, T2, T3). By definition, we have

$$S _ { T } ( T _ { 1 } , T _ { 2 } , T _ { 3 } ) - S _ { T } ( T _ { 1 } , T _ { 2 } ^ { 0 } , T _ { 3 } ) = ( S S R _ { 1 } - S S R _ { 3 } ) - ( S S R _ { 2 } - S S R _ { 3 } ) .$$

This latter relation is useful because it allows us to carry the analysis in terms of two problems involving a single structural change, the first allowing an additional fourth break at time T0 between T2 and T3 and the second an additional fourth break at time T2 between the T1 and T2. It is then denote the estimator of (δ1, δ2, δ0, δ3, δ0) based on the partition (T1, T2, T2, T3) (note δ0 is repeated once). In particular, δ is an estimate of δ2 associated with the regressor (0,...,0, zT1 + 1, .., ZT2,0,..., 0), δ is an estimate of δ2 associated with the regressor Z∆ = (0,..., 0, ZT2+ 1,.., zT9, 0,.., 0), and δ is an estimate of δ0 associated with the regressor (0,..., , zT9 + 1,..., r3, 0, .., 0). Now consider SSR1 − SSR3; we have (e.g., Amemiya (1985, p. 31)),

$$S _ { T } ( T _ { 1 } , T _ { 2 } , T _ { 3 } ) - S _ { T } ( T _ { 1 } , T _ { 2 } , T _ { 2 } ^ { 0 } , T _ { 3 } ) = ( \hat { \delta } _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ) ^ { ^ { \prime } } Z _ { \Delta } ^ { \prime } M _ { \overline { W } } Z _ { \Delta } ( \hat { \delta } _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ) ,$$

where W=(X, Ž), with Z the diagonal partition of Z at (T1,T2,T3). Similarly, we have for SSR2 − SSR3,

$$S _ { T } ( T _ { 1 } , T _ { 2 } ^ { 0 } , T _ { 3 } ) - S _ { T } ( T _ { 1 } , T _ { 2 } , T _ { 2 } ^ { 0 } , T _ { 3 } ) = ( \hat { \delta } _ { 2 } ^ { * } - \hat { \delta } _ { \Delta } ^ { ^ { \prime } } ) ^ { \prime } Z _ { \Delta } ^ { \prime } M _ { \dot { W } } Z _ { \Delta } ( \hat { \delta } _ { 2 } ^ { * } - \hat { \delta } _ { \Delta } ) ,$$

where W = (X, Ž) with Ž the diagonal partition of Z at (T1, T2, T3). Thus

$$S S R _ { 1 } - S S R _ { 2 } & = ( \hat { \delta } _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ^ { ^ { \prime } } Z _ { \Delta } ^ { \prime } M _ { \varpi } Z _ { \Delta } ( \hat { \delta } _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ) - ( \hat { \delta } _ { 2 } ^ { * } - \hat { \delta } _ { \Delta } ^ { ^ { \prime } } Z _ { \Delta } ^ { \prime } M _ { \varpi } Z _ { \Delta } ( \hat { \delta } _ { 2 } ^ { * } - \hat { \delta } _ { \Delta } ) \\ & \geq ( \hat { \delta } _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ) ^ { \prime } Z _ { \Delta } ^ { \prime } M _ { \varpi } Z _ { \Delta } ( \hat { \delta } _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ) - ( \hat { \delta } _ { 2 } ^ { * } - \hat { \delta } _ { \Delta } ^ { ^ { \prime } } Z _ { \Delta } ^ { \prime } Z _ { \Delta } ( \hat { \delta } _ { 2 } ^ { * } - \hat { \delta } _ { \Delta } ) .$$

The inequality is due to ZM Z ≤ Z′sZ. From the definition of Mw, we have

$$The inequality is due to Z _ { \Delta } ^ { \Delta } M _ { W } Z _ { \Delta } \leq & 2 _ { \Delta } Z _ { \Delta } . \text { From the definition of } M _ { \overline { W } } , \text { we have} \\ ( 3 1 ) & \quad ( S S R _ { 1 } - S S R _ { 2 } ) / ( T _ { 2 } ^ { 0 } - T _ { 2 } ) \\ & \geq ( \hat { \delta } _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ) ^ { \prime } [ Z _ { \Delta } ^ { \prime } Z _ { \Delta } / ( T _ { 2 } ^ { 0 } - T _ { 2 } ) ] ( \hat { \delta } _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ) \\ & \quad - ( \hat { \delta } _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ) ^ { \prime } [ Z _ { \Delta } ^ { \prime } W / ( T _ { 2 } ^ { 0 } - T _ { 2 } ) ] [ W ^ { \prime } W / T ] \ \{ W ^ { \prime } Z _ { \Delta } / T \} ( \delta _ { 3 } ^ { * } - \hat { \delta } _ { \Delta } ) \\ & \quad - ( \hat { \delta } _ { 2 } ^ { * } - \hat { \delta } _ { \Delta } ) ^ { \prime } \{ Z _ { \Delta } ^ { \prime } Z _ { \Delta } / ( T _ { 2 } ^ { 0 } - T _ { 2 } ) \} ( \hat { \delta } _ { 2 } ^ { * } - \hat { \delta } _ { \Delta } ) \\ & \equiv ( 1 ) - ( I I ) - ( I I I ) . \\ \text {Consider term } ( I ) . \text { Note first that } \hat { \delta } _ { 1 } ^ { * } \text { is close to } \delta _ { 1 } ^ { 0 } \text { given that, on the set } V ( C ) , \text { the distance}$$

Consider term (I). Note first that δ* is close to δ0 given that, on the set V(C), the distance between T, and T0 can be conitrolled and made small by choosing a small e. Noting that δ is estimated using observations from the second true regime only, δ is close to δ0 for a large enough C, on V(C). Hence, for large C, large T and small €, (I) is no less than (1/2)(δ0 − δ0 )[Z'Z/(T0 − T2)](δ0 − δ0) with large probability. Next consider term (II). It is easy to show that on V (C), δ% and δ∆ are Op(1) uniformly. Also on V(C), (W'W/T)−1 = Op(1) and Z′W/(T0 − T2) = Op(1) (because Z'W involves no more than T0 – T2 observations). Furthermore,

$$\| \overline { W } ^ { \prime } Z _ { \Delta } / T \| = \| \overline { W } ^ { \prime } Z _ { \Delta } / ( T _ { 2 } ^ { 0 } - T _ { 2 } ) \| ( T _ { 2 } ^ { 0 } - T _ { 2 } ) / T \leq \epsilon \, O _ { p } ( 1 ) .$$

Thus (II) is no larger than εOp(1). Consider finally (III). Because both δ and δ are close to δ0, l2 — δ∥l &lt; ρ with large probability for every ρ&gt; 0 (this is true for large T, large C, and small ε). ()     (I)  ()  n () = ( −- )/z s )) Hence, the inequality

$$\frac { \ S S R _ { 1 } - \ S S R _ { 2 } } { T _ { 2 } ^ { 0 } - T _ { 2 } } \geq 2 ^ { - 1 } ( \delta _ { 3 } ^ { 0 } - \delta _ { 2 } ^ { 0 } ) ^ { \prime } \frac { Z _ { \Delta } ^ { \prime } Z _ { \Delta } } { T _ { 2 } ^ { 0 } - T _ { 2 } } ( \delta _ { 3 } ^ { 0 } - \delta _ { 2 } ^ { 0 } ) - \epsilon O _ { p } ( 1 ) - \rho O _ { p } ( 1 )$$


<!-- p:26 -->


holds with large probability. By A2,

$$Z _ { \perp } ^ { \prime } Z _ { \perp } / ( T _ { 2 } ^ { 0 } - T _ { 2 } ) = \frac { 1 } { T _ { 2 } ^ { 0 } - T _ { 2 } } \sum _ { t = T _ { 2 } + 1 } ^ { T _ { 2 } ^ { 0 } } z _ { t } z _ { t } ^ { \prime }$$

has its minimum eigenvalue bounded away from zero on V€(C). Thus the first term on the right-hand side of (32) is positive and dominates the other two terms. It follows that with large probability, (SSR − SSR2)/(T0 − T2) &gt; 0. This proves (28) and the proposition. Q.E.D.

PROOF OF PROPOsITION 4(i): The structure of the proof is similar to that of Proposition 1 but modifications are necessary in view of the fact that T−1 Στ= d2 → 0 even supposing a break is not consistently estimated when the shifts are shrinking. Using (4) and (5) (without dividing T on both sides), we can arrive at the desired contradiction if we can show that Σt= 1d2 &gt; 2Σ7= 1u,d, in the limit as T → ∞. To do this we show that Στ= 1d2 diverges at a faster rate than ΣT= 1u,d,.

We will make use of vp being small to strengthen the result of (22) and (23). We shall drop the subscript T in δf,i. From δi0 − δi+ 1 = O(vτ) under A6, by adding and subtracting terms, we have δi0 − δj0 = O(vp) for all i and j. Now consider (24). The first term on the right-hand side can be rewritten as (X'MzX)− 1X'Mz(Z0 − Z)80 because MzZ = 0. A key to the proof lies in the fact that (Zo – Ž)δ0 depends on changes in the parameters (i.e. δ0 – δj0). In the case of a single change point, for example, assume T1 &lt; T1; then

$$( \bar { Z } ^ { 0 } - \bar { Z } ) \, \delta ^ { 0 } = ( 0 , \dots , 0 , z _ { T _ { 1 } + 1 } , \dots , z _ { T _ { 1 } ^ { 0 } } , 0 , \dots , 0 ) ^ { \prime } ( \delta _ { 1 } ^ { 0 } - \delta _ { 2 } ^ { 0 } ) .$$

This implies that X'Mz(Z0 – Ž)δ0 is at most Op(T)vτ. By Lemma A.2,

$$( X ^ { \prime } M _ { \bar { Z } } X ) ^ { - 1 } X ^ { \prime } M _ { \bar { Z } } ( \bar { Z } ^ { 0 } - \bar { Z } ) \, \delta ^ { 0 } = O _ { p } ( v _ { T } ) .$$

This implies that, from (24),

$$\hat { \beta } ( \{ T _ { j } \} ) - \beta ^ { 0 } = O _ { p } ( v _ { T } ) + O _ { p } ( T ^ { \alpha - 1 / 2 } ) .$$

Thus

$$U ^ { \prime } X ( \hat { \beta } ( \{ T _ { j } \} ) - \beta ^ { 0 } ) = O _ { p } ( T ^ { 1 / 2 } v _ { T } ) + O _ { p } ( T ^ { \alpha } )$$

over all partitions. Next, we combine the first and the third terms of (25) and rewrite them as

$$U ^ { \prime } \bar { Z } ( \bar { Z } ^ { \prime } M _ { X } \bar { Z } ) ^ { ^ { - 1 } } \bar { Z } ^ { \prime } M _ { X } ( \bar { Z } ^ { 0 } - \bar { Z } ) \delta ^ { 0 } + U ^ { \prime } ( \bar { Z } - \bar { Z } ^ { 0 } ) \delta ^ { 0 } .$$

Each term above involves (Ž – Z0)δ0. Using the argument in proving (26) and (33), the first term of t      s  (    i t  t  ( / +   (t middle term of (25) is Op(T2α), we have

$$U ^ { \prime } \overline { Z } \hat { \delta } ( \{ T _ { j } \} ) - U ^ { \prime } \overline { Z } ^ { 0 } \delta ^ { 0 } = O _ { p } ( T ^ { \alpha + 1 / 2 } v _ { T } ) + O _ { p } ( T ^ { 2 \alpha } ) .$$

Noting that (35) dominates (33), we have ΣT= 1u,d, = Op(T α+ 1/2 vT + T2α).

Next, consider Στ= 1d2. The proof of Lemma 2 is not changed under shrinking shifts. If there exists a change point that cannot be consistently estimated, then

$$\sum _ { t = 1 } ^ { T } d _ { t } ^ { 2 } > T C \| \delta _ { j } ^ { 0 } - \delta _ { j + 1 } ^ { 0 } \| ^ { 2 } > T C ^ { \prime } v _ { T } ^ { 2 }$$

for some C′ &gt; 0. Thus Σt= 1d2 &gt; 2Στ=1u,d, if Tvγ/(Tα+ 1/2vT + T2α) → ∞. This is the case if T(1/2)− α vp → ∞. Under E|u,|2/ θ &lt; ∞ of A6, we can choose α such that α &lt; θ in Lemma A.4. Thus, ∞←-(2/)L-(/)6. Q.E.D.


<!-- p:27 -->


To prove Proposition 4(ii), we first prove a lemma, which generalizes the Hajek and Renyi inequality to mixingales.

LEMMA A.6: Let {ξ1,F} be a q × 1 L2 mixingale satisfying (a)−(e) of A4(i) with ui replaced by ξi and |·| replaced by ∥·. Then there exists an L &lt; ∞ such that, for every c &gt; 0 and m &gt; 0,

$$P \left ( \sup _ { k \geq m } \frac { 1 } { k } \left \| \sum _ { t = 1 } ^ { k } \xi _ { t } \right \| > c \right ) \leq \frac { L } { c ^ { 2 } m } \, .$$

PROOF: Let ξjt = E(ξ1| t− j) − E(ξ{|Ft−j− 1). Then ξt = Σj= − x ξjt, and so Σk= 1 ξt = Σj= − ∞∑t= 1 ξjt. Thus, for each N &gt; 0,

$$P \left ( \sup _ { N \geq k \geq m } \frac { 1 } { k } \left \| \sum _ { l = 1 } ^ { k } \xi _ { l } \right \| > c \right ) \leq P \left ( \sum _ { j = - \varkappa } ^ { \varkappa } \sup _ { N \geq k \geq m } \frac { 1 } { k } \left \| \sum _ { l = 1 } ^ { k } \xi _ { l j } \right \| > c \right ) .$$

For each j, {ξjr,Ft\_j} forms a sequence of martingale differences. Let aj &gt; 0 for all j such that Σj= − ∞a j = 1. The right-hand side above is bounded by

$$\L _ { j = - \alpha } ^ { j = - \alpha } d _ { j } & = 1 . \ \text {In the $g$-land side above is bounded by} \\ & \sum _ { j = - \alpha } ^ { \varkappa } P \left ( \sup _ { N \geq k \geq m } \frac { 1 } { k } \left \| \sum _ { t = 1 } ^ { k } \xi _ { j _ { t } } \right \| > a _ { j } c \right ) \\ & \leq \frac { 1 } { c ^ { 2 } } \sum _ { j = - \infty } ^ { \varkappa } a _ { j } ^ { - 2 } \left ( m ^ { - 2 } \sum _ { i = 1 } ^ { m } E \| \xi _ { j _ { i } } \| ^ { 2 } + \sum _ { i = m + 1 } ^ { N } i ^ { - 2 } E \| \xi _ { j _ { i } } \| ^ { 2 } \right ) ; \\ \intertext { h o l t r o w b i d e s }$$

the latter bound is due to Hajek and Renyi's inequality for martingale differences. From the definition of a mixingale and A4(i(c), Elξ2 ≤ 4c≤ 4K2ψ. Thus the above is bounded by c−24K2(Σj=-xaj24j)(m−1 + Σi=m+1l−2). Since Σi=m+1-2 ≤2m−1, if we let L = 12 K2(Σj= – xaj 2ψ), then the desired upper bound is obtained for a fixed N. Since the bound does not depend on N, the lemma is obtained by letting N →∞. It remains to choose appropriate a'js such that Σjaj 2ψ2, is bounded. Let ν0 = 1 and νj = j− 1− k(j ≥ 1), where κ &gt; 0 as given in A4(i)(d). Let a j = νj/(1 + 2Σt= 1 ν1) and a − j = a j for j ≥ 0. Then Σja j = 1. By Assumption A4(i)(d),

$$\sum _ { j } a _ { j } ^ { - 2 } \psi _ { | j | } ^ { 2 } = \left ( \psi _ { 0 } ^ { 2 } + 2 \sum _ { j = 1 } ^ { \infty } j ^ { 2 + 2 \kappa } \psi _ { j } ^ { 2 } \right ) \left ( 1 + 2 \sum _ { j = 1 } ^ { \infty } j ^ { - 2 - 2 \kappa } \right ) < \varphi .$$

PROOF OF PROPOsITION 4(ii): We shall maintain all the notations in the proof of Proposition 2. Define a new set

$$V _ { \epsilon } ^ { * } ( C ) = \{ ( T _ { 1 } , T _ { 2 } , T _ { 3 } ) ; | T _ { i } - T _ { i } ^ { 0 } | \leq \epsilon T , 1 \leq i \leq 3 , T _ { 2 } - T _ { 2 } ^ { 0 } < - C / v _ { T } ^ { 2 } \} ,$$

which is a subset of V€. We only need to show that (28) holds when the minimum is taken over V*(C). We can prove that, uniformly on the set V*(C),

$$\hat { \delta } _ { i } ^ { * } - \delta _ { i } ^ { 0 } = \epsilon O _ { p } ( v _ { T } ) + O _ { p } ( T ^ { - 1 / 2 } )$$

$$\hat { \delta } _ { \Delta } - \delta _ { 2 } ^ { 0 } = ( Z _ { \Delta } ^ { \prime } Z _ { \Delta } ) ^ { - 1 } Z _ { \Delta } U + \epsilon O _ { p } ( v _ { T } ) + O _ { p } ( T ^ { - 1 / 2 } ) .$$

The above is easily seen to be true in the case of pure structural changes. In this case, for example, δ − δ0 is given exactly by (Z′Z)−1ZU. In the case of partial structural changes, the proof of (36) and (37) is more complicated. We shall omit the details and give a brief explanation instead. A detailed proof is available upon request. The term εOp(vp) on the right-hand side of (36) is due to misspecification in the sense that T, may not be the same as T0. However, this misspecification is

$$( i = 1 , \dots , 4 ) ,$$


<!-- p:28 -->


cono  ( nd   s   on   as    nm O(T-1/2) is related to disturbances and this specific rate is due to the fact that each δ* is estimated with a positive fraction of the sample for partitions in V€*(C). The last two terms of (37) are due to spillover from the misspecification via partial structural changes.

Using (36) and (37), expression (I) in (31) is no smaller than

$$( \delta _ { 3 } ^ { 0 } - \delta _ { 2 } ^ { \theta } ) ^ { \prime } [ Z _ { \perp } ^ { \prime } Z _ { \Delta } / ( T _ { 2 } ^ { 0 } - T _ { 2 } ) ] ( \delta _ { 3 } ^ { 0 } - \delta _ { 2 } ^ { 0 } ) - \epsilon O _ { p } ( v _ { T } ^ { 2 } ) - O _ { p } ( T ^ { - 1 / 2 } v _ { r } ) - O _ { p } ( T ^ { - 1 } ) .$$

Because the minimum eigenvalue of Z'Z/(T0 – T2) is bounded away from zero on V *(C) for all large C and δ0 − δ0 = O(vT), (I) is no smaller than Av) − εOp(v2), where A is a positive constant. Note that εOp(v2) dominates Op(T−1/2 v,) and Op(T−1). The latter two terms also appear in (II) and (III) of (31) and will be absorbed into εO,(v). Expression (II) in (31) is bounded by εOp(vγ). Expression (III) is bounded by

$$( T _ { 2 } ^ { ( 0 } - T _ { 2 } ) ^ { - 1 } U ^ { \prime } Z _ { \perp } ( Z _ { \perp } ^ { \prime } Z _ { \perp } ) ^ { - 1 } Z _ { \perp } ^ { \prime } U + \epsilon O _ { p } ( v _ { T } ^ { 2 } ) .$$

q  r s (I    ()  (I) = -(  − )/] idy

$$O _ { \rho } ( 1 ) \| ( T _ { 2 } ^ { 0 } - T _ { 2 } ) ^ { - 1 } Z _ { \varrho } U \| ^ { 2 } + \epsilon O _ { \rho } ( v _ { T } ^ { 2 } ) .$$

In summary,

$$\frac { S S R _ { 1 } - S S R _ { 2 } } { T _ { 2 } ^ { 0 } - T _ { 2 } } \geq A v _ { T } ^ { \frac { 2 } { 2 } } + \left \| \frac { Z _ { \Delta } U } { T _ { 2 } ^ { 0 } - T _ { 2 } } \right \| ^ { 2 } O _ { p } ( 1 ) - \epsilon O _ { p } ( v _ { T } ^ { 2 } ) .$$

For every η &gt; 0, we can choose a small ∈ &gt; 0 such that P(εOp(ψ2) &gt; Av1⁄2/2) &lt; η and we can also choose B &lt; ∞ such that P(|O(1)| &gt; B) &lt; ν. Thus

$$\text {choose $B<0$ such that } P ( | _ { P } ( 1 ) | > B ) ^ { 2 } \colon & \max _ { T \colon \left ( S S R _ { 1 } - S S R _ { 2 } \right ) / ( T _ { 2 } ^ { 0 } - T _ { 2 } ) } \leq 0 ) \\ & \leq 2 \eta + P \left ( \max \left \{ B | ( T _ { 2 } ^ { 0 } - T _ { 2 } ) ^ { - 1 } Z _ { \downarrow } U | ^ { 2 } \right \} > A v _ { T } ^ { 2 } / 2 \right ) \\ & \quad = 2 \eta + P \left ( \max _ { T _ { 1 } , < T _ { 2 } ^ { \frac { 1 } { 9 } - C \cdot C ^ { \frac { 1 } { 2 } } } } ( T _ { 2 } ^ { 0 } - T _ { 2 } ) ^ { - 1 } \right | \sum _ { t = T _ { 1 } + 1 } ^ { R _ { 1 } ^ { 0 } } z _ { t } u _ { t } \right | > [ A / ( 2 B ) ] ^ { 1 / 2 } v _ { T } \right ) . \\ \intertext { By I c mma A 6 with } & \varepsilon = z _ { 1 } u _ { 1 } \left [ 4 \left ( 2 B \right ) \right ] ^ { 1 / 2 } v _ { t } - 2 \left ( \text {applied with data order reversed} \right )$$

By Lemma A.6 with ξt = z,u,, c = [A/(2 B)]1/2 vT, and m = Cv−2 (applied with data order reversed, i.e. treating T0 as the first observation), the above probability is bounded by

$$2 \eta + ( 2 B / A ) L ( v _ { T } ^ { 2 } C w _ { T } ^ { - 2 } ) ^ { - 1 } = 2 \eta + ( 2 B / A ) L C ^ { - 1 } < 3 \eta \\ \text {for large $C$.} & & Q . E . D .$$

PROOF OF PROPOSITION 6: Note that we can write

$$F _ { T } ( \lambda _ { 1 } , \dots , \lambda _ { k } ; q ) = ( S S R _ { 0 } - S S R _ { k } ) / [ k q ( T - ( k + 1 ) q - p ) ^ { - 1 } S S R _ { k } ] ,$$

where SSR0 and SSR are the sum of squared residuals under the null and alternative hypotheses, respectively. We have

$$( T - ( k + 1 ) q - p ) ^ { - 1 } S S R _ { k } \to _ { \varphi } \sigma ^ { 2 } .$$

Hence, we concentrate on the limit of F = SSR0 − SSRk. Now, let DU(i, j) (DR(i, j), resp.) be the sum of squared residuals from the unrestricted (restricted, resp.) model using data from segments i to j (inclusively), i.e. from observation Ti− 1 + 1 to Tj. We can write F = DR(1, k + 1) − Σk+ 1Dν(i, i), or

$$F _ { \bar { r } } ^ { * } = \sum _ { i = 1 } ^ { k } [ D ^ { R } ( 1 , i + 1 ) - D ^ { R } ( 1 , i ) - D ^ { u } ( i + 1 , i + 1 ) ] + D ^ { R } ( 1 , 1 ) - D ^ { v } ( 1 , 1 ) .$$


<!-- p:29 -->


Let β and βR be the estimate of β in the unrestricted and restricted models, respectively. We Ha N (1zz) = Z  XX-(X,X) = y  ,X-(X,X) =  rt Y1, j, U1, j, X1, j, and Z1, j denote the corresponding vectors or matrices containing elements belonging to the partition from segment 1 to segment j (inclusively) and let Yj, Uj, Xj, and Zj be the vectors or matrices containing elements from segment j only. Also, let δ j be the estimate of δ using data on the z's from segment 1 to j only in the restricted model and v be the estimate of δj using data on the z's from segment j only in the unrestricted model. We have

$$\hat { \delta } _ { 1 , j } ^ { R } & = ( Z _ { 1 , j } ^ { \prime } Z _ { 1 , j } ) ^ { - 1 } Z _ { 1 , j } ^ { \prime } ( Y _ { 1 , j } - X _ { 1 , j } \hat { \beta } ^ { R } ) , \quad \text {and} \\ \hat { \delta } _ { j } ^ { U } & = ( Z _ { j } ^ { \prime } Z _ { j } ) ^ { - 1 } Z _ { j } ^ { \prime } ( Y _ { j } - X _ { j } \hat { \beta } ^ { U } ) .$$

Using the fact that, under the null hypothesis,

$$Y & = X \beta + Z \delta + U = X \beta + \overline { Z } \overline { \delta } + U \quad \text {and} \\ Y _ { j } & = X _ { j } \beta + Z _ { j } \delta + U _ { j }$$

(with δ = (δ, ... , δ) a q(k + 1) vector with δ defined by δ1 = δ2 = ... = δk + 1 ≡ δ), straightforward algebra yields

DR(1, j) = ∥|(I − Pz1,1)(U1,j − X1, jAT)|2 and

Du(j, j) = (I − Pz,)(Uj − XjAT)|{2,

where AT = (X'MzX)−1X'MzU, and AT = (X'MzX)−1X'MzU. Consider the ith element in the summation defining F in (39); we have

$$F _ { T , i } = & D ^ { R } ( 1 , i + 1 ) - D ^ { R } ( 1 , i ) - D ^ { u } ( i + 1 , i + 1 ) \\ = & \| ( I - P _ { Z _ { 1 , i + 1 } } ) ( U _ { 1 , i + 1 } - X _ { 1 , i + 1 } A _ { T } ) \| ^ { 2 } - \| ( I - P _ { Z _ { 1 , i } } ) ( U _ { 1 , i } - X _ { 1 , i } A _ { T } ) \| ^ { 2 } \\ & - \| ( I - P _ { Z _ { i + 1 } } ) ( U _ { i + 1 } - X _ { i + 1 } \bar { A } _ { T } ) \| ^ { 2 } .$$

To simplify the exposition, let Sj = Z1, jU1,j, Hj = Z1, jZ1, j, Kj = Z1,jX1,j, Lj = X1, jX1, j, and Mj = Xí, jU1, j. Noting that

$$U _ { 1 , i + 1 } ^ { \prime } U _ { 1 , i + 1 } = U _ { 1 , i } ^ { \prime } U _ { 1 , i } + U _ { i + 1 } ^ { \prime } U _ { i + 1 } , \\ X _ { 1 , i + 1 } ^ { \prime } X _ { 1 , i + 1 } ^ { \dot { \cdot } } = X _ { 1 , i } ^ { \prime } X _ { 1 , i } + X _ { i + 1 } ^ { \prime } X _ { i + 1 } ,$$

and and

$$U _ { 1 , i + 1 } ^ { \prime } X _ { 1 , i + 1 } = U _ { 1 , i } ^ { \prime } X _ { 1 , i } + U _ { i + 1 } ^ { \prime } X _ { i + 1 } ,$$

we deduce that

$$We deduce that \\ ( 4 ) \quad F _ { T , i } = - S _ { i + 1 } ^ { \prime } H _ { i + 1 } ^ { - 1 } S _ { i + 1 } + S _ { i } ^ { \prime } H _ { i } ^ { - 1 } S _ { i } + ( S _ { i + 1 } - S _ { i } ) [ H _ { i + 1 } - H _ { i } ] ^ { - 1 } ( S _ { i + 1 } - S _ { i } ) \\ + 2 S _ { i + 1 } ^ { \prime } H _ { i + 1 } ^ { - 1 } K _ { i + 1 } A _ { T } - 2 S _ { i } ^ { \prime } H _ { i } ^ { - 1 } K _ { i } A _ { T } \\ - 2 ( S _ { i + 1 } - S _ { i } ) [ H _ { i + 1 } - H _ { i } ] ^ { - 1 } ( K _ { i + 1 } - K _ { i } ) \bar { A } _ { T } \quad . \\ + 2 ( M _ { i + 1 } - M _ { i } ) ( \bar { A } _ { T } - A _ { T } ) + ( \bar { A } _ { T } - A _ { T } ) ^ { \prime } ( L _ { i + 1 } - L _ { i } ) ( \bar { A } _ { T } - A _ { T } ) .$$

Using the stated assumptions, we have the following basic convergence results:

$$( i ) \quad T ^ { - 1 / 2 } ( X _ { 1 , j } , Z _ { 1 , j } ) ^ { \prime } U _ { 1 , j } \mapsto \sigma ( B _ { 1 } ( \lambda _ { j } ) , B _ { 2 } ( \lambda _ { j } ) ) ^ { \prime } \equiv \sigma B ( \lambda _ { j } ) ^ { \prime }$$


<!-- p:30 -->


where B(r) is a (q + p) dimensional vector Brownian motion with covariance matrix

$$= \begin{bmatrix} Q _ { 1 1 } & Q _ { 1 2 } \\ Q _ { 1 1 } & Q _ { 1 2 } \end{bmatrix} .$$

$$Q = \begin{bmatrix} Q _ { 1 1 } & Q _ { 1 2 } \\ Q _ { 2 1 } & Q _ { 2 2 } \end{bmatrix} . \\ T ^ { - 1 } ( X _ { 1 , j } , Z _ { 1 , j } ) ^ { \prime } ( X _ { 1 , j } , Z _ { 1 , j } ) \to _ { \rho } \sigma ^ { 2 } \lambda _ { j } Q .$$

From these two limits, we deduce easily the following results:

- (a) T−1/2Sj ⇒ σ B2(λj);
- (b) T−1 Hj →p σ2λjQ22;
- (c) T−1Kj →p σ2λjQ21;
- (d) T−1Lj →p σ 2λjQ11;
- (e) T−1/2Mj ⇒ σ B1(λj);
- (f) T1/2AT ⇒ σ− 1(Q1 − Q12Q221 Q21)−1(B1(1) − Q12Q221 B2(1)) ≡ A*.

It remains to consider the limit of T1/2Ap. Let Λ = diag{ λ1, λ2 − λ1, . . ., 1 − λk}, a (k + 1) by (k + 1) diagonal matrix. We deduce that

- (i) T− 1 Z'Z →p σ2(A ∅ Q22);
- (ii) T− 1X'Z →p σ2(e'∆ ∅ Q12) where e' = (1, 1,. .., 1),

a (k + 1) vector;

$$( \ddot { \Pi } ) \quad T ^ { - 1 / 2 } \bar { Z } ^ { \prime } U \Rightarrow \sigma ( B _ { 2 } ( \lambda _ { 1 } ) , B _ { 2 } ( \lambda _ { 2 } ) - B _ { 2 } ( \lambda _ { 1 } ) , \dots , B _ { 2 } ( 1 ) - B _ { 2 } ( \lambda _ { k } ) ) ^ { \prime } \equiv B ^ { * } .$$

We then obtain

$$We then obtain \\ ( 4 ) \quad T ^ { 1 / 2 } \bar { A } _ { T } = [ T ^ { - 1 } X ^ { \prime } X - T ^ { - 1 } X ^ { \prime } \bar { Z } ( T ^ { - 1 } \bar { Z } ^ { \prime } \bar { Z } ) ^ { - 1 } T ^ { - 1 } \bar { Z } ^ { \prime } X ] ^ { - 1 } \\ \times [ T ^ { - 1 / 2 } X ^ { \prime } U - T ^ { - 1 } X ^ { \prime } \bar { Z } ( T ^ { - 1 } \bar { Z } ^ { \prime } \bar { Z } ) ^ { - 1 } T ^ { - 1 / 2 } \bar { Z } ^ { \prime } U ] \\ \Rightarrow \sigma ^ { - 1 } [ Q _ { 1 } - ( e ^ { \prime } A \otimes Q _ { 1 2 } ) ( A \otimes Q _ { 1 2 } ) ^ { - 1 } ( \Lambda e \otimes Q _ { 2 1 } ) ] ^ { - 1 } \\ \times [ B _ { 1 } ( 1 ) - ( e ^ { \prime } A \otimes Q _ { 1 2 } ) ( \Lambda \otimes Q _ { 2 1 } ) ^ { - 1 } B ^ { * } ] \\ = \sigma ^ { - 1 } [ Q _ { 1 } - ( e ^ { \prime } \Lambda e \otimes Q _ { 1 2 } Q _ { 1 2 } ^ { - 1 } Q _ { 2 1 } ) ] ^ { - 1 } [ B _ { 1 } ( 1 ) - ( e ^ { \prime } \otimes Q _ { 1 2 } Q _ { 2 1 } ^ { - 1 } B ^ { * } ] \\ = \sigma ^ { - 1 } [ Q _ { 1 1 } - Q _ { 1 2 } Q _ { 2 2 } ^ { - 1 } Q _ { 2 1 } ] ^ { - 1 } [ B _ { 1 } ( 1 ) - Q _ { 1 2 } Q _ { 2 2 } ^ { - 1 } B ^ { 1 } ( 1 ) ] = A ^ { * } . \\ \intertext { The second equality follows since } \intertext { the second equality follows since } \intertext { ( 1 ) } \intertext { ( 2 ) } \intertext { ( 3 ) } \intertext { ( 4 ) } \intertext { ( 5 ) } \intertext { ( 6 ) } \intertext { ( 7 ) } \intertext { ( 8 ) } \intertext { ( 9 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2 ) } \intertext { ( 5 2 ) } \intertext { ( 6 2 ) } \intertext { ( 7 2 ) } \intertext { ( 8 2 ) } \intertext { ( 9 2 ) } \intertext { ( 1 2 ) } \intertext { ( 3 2 ) } \intertext { ( 4 2$$

The second equality follows since e'Ae = 1 and (e′ ⊗ Q12 Q221) B* = Q12Q221 B2(1). Using the results stated above we easily deduce that (Mi+ 1 − Mi)(AT − Ap) ⇒ 0, (ĀT − AT)(L+ 1 − Lj)(ĀT − AT) ⇒ 0, and

$$S _ { i + 1 } ^ { \prime } H _ { i + 1 } ^ { - 1 } K _ { i + 1 } A _ { T } - S _ { i } ^ { \prime } H _ { i } ^ { - 1 } K _ { i } A _ { T } - ( S _ { i + 1 } - S _ { i } ) \{ [ H _ { i + 1 } - H _ { i } ] ^ { - 1 } ( K _ { i + 1 } - K _ { i } ) \bar { A } _ { T } \\ \Rightarrow \sigma B _ { 2 } ( \lambda _ { i + 1 } ) Q _ { 2 2 } ^ { - 1 } Q _ { 2 1 } A ^ { * } - \sigma B _ { 2 } ( \lambda _ { i } ) Q _ { 2 2 } ^ { - 1 } Q _ { 2 1 } A ^ { * } \\ - \sigma ( B _ { 2 } ( \lambda _ { i + 1 } ) - B _ { 2 } ( \lambda _ { i } ) ) Q _ { 2 2 } ^ { - 1 } Q _ { 2 1 } A ^ { * } = 0 .$$

Hence, we are left with

$$F _ { T , i } = - S _ { i + 1 } ^ { \prime } H _ { i + 1 } ^ { - 1 } S _ { i + 1 } + S _ { i } ^ { \prime } H _ { i } ^ { - 1 } S _ { i } + ( S _ { i + 1 } - S _ { i } ) ^ { \prime } [ H _ { i + 1 } - H _ { i } ] ^ { \sim 1 } ( S _ { i + 1 } - S _ { i } ) + o _ { p } ( 1 ) ,$$


<!-- p:31 -->


and we deduce, using the fact that B2(λj) = σ Q1⁄22Wq(λj),

$$and \text {we deduce, using the fact that } B _ { 2 } ( \lambda _ { j } ) = \sigma Q _ { 2 2 } ^ { 1 / 2 } W _ { q } ( \lambda _ { j } ) , \\ ( 4 ) \quad F _ { T , l } & \Rightarrow - B _ { 2 } ( \lambda _ { i + 1 } ) ^ { \prime } Q _ { 2 2 } ^ { - 1 } B _ { 2 } ( \lambda _ { i + 1 } ) / \lambda _ { i + 1 } + B _ { 2 } ( \lambda _ { i } ) ^ { \prime } Q _ { 2 2 } ^ { - 1 } B _ { 2 } ( \lambda _ { i } ) / \lambda _ { i } \\ & \quad + ( B _ { 2 } ( \lambda _ { i + 1 } ) - B _ { 2 } ( \lambda _ { i } ) ) ^ { \prime } Q _ { 2 2 } ^ { - 1 } ( B _ { 2 } ( \lambda _ { i + 1 } ) - B _ { 2 } ( \lambda _ { i } ) ) / ( \lambda _ { i + 1 } - \lambda _ { i } ) \\ & = - \sigma ^ { 2 } \| W _ { q } ( \lambda _ { i + 1 } ) \| ^ { 2 } / \lambda _ { i + 1 } + \sigma ^ { 2 } \| W _ { q } ( \lambda _ { i } ) \| ^ { 2 } / \lambda _ { i } \\ & \quad + \sigma ^ { 2 } \| W _ { q } ( \lambda _ { i + 1 } ) - W _ { q } ( \lambda _ { i } ) \| ^ { 2 } / ( \lambda _ { i + 1 } - \lambda _ { i } ) \\ & = \sigma ^ { 2 } \| \lambda _ { i } W _ { q } ( \lambda _ { i + 1 } ) - \lambda _ { i + 1 } W _ { q } ( \lambda _ { i } ) \| ^ { 2 } / \lambda _ { i + 1 } ( \lambda _ { i + 1 } - \lambda _ { i } ) . \\ \text {Finally, it is easy to verify that } D ^ { r } ( 1 , 1 ) - D ^ { v } ( 1 , 1 ) \Rightarrow 0 . \text { Note that this convergence result}$$

Finally, it is easy to verify that DR(1, 1) − D'(1, 1) ⇒ 0. Note that this convergence result holds jointly for i = 1, . . . , k; hence

$$F _ { T } ^ { * } \rightarrow \sigma ^ { 2 } \sum _ { i = 1 } ^ { k } \frac { \| \lambda _ { i } W _ { q ^ { ( \lambda _ { i + 1 } ) } } - \lambda _ { i + 1 } W _ { q } ( \lambda _ { i } ) \| ^ { 2 } } { \lambda _ { i + 1 } \lambda ( \lambda _ { i + 1 } - \lambda _ { i } ) } , \\ \intertext { a n d the result of $Proposition 6$ follows. } Q . E . D .$$

PROOF OF PROPOsITION 7: For simplicity, we present the arguments in the case of a pure structural change. Let SSR(i,j) be the minimized sum of squared residuals for the segment containing observations from (i + 1) to j; then we can write

$$F _ { T } ( l + 1 | l ) = \sup _ { 1 \leq i \leq l + 1 } \sup _ { \tau \in \Delta _ { l , \eta } } \{ S S R ( \hat { T } _ { i - 1 } , \hat { T } _ { i } ) - S S R ( \hat { T } _ { i - 1 } , \tau ) - S S R ( \tau , \hat { T } _ { i } ) \} / \hat { \sigma } ^ { 2 } .$$

Under Assumptions A8-A9, arguments as in the proof of Proposition 6 show that

$$\sigma ^ { - ? } \sup _ { i = 0 } \left \{ S S R ( T _ { i - 1 } ^ { 0 } , T _ { i } ^ { 0 } ) - S S R ( T _ { i - 1 } ^ { 0 } , \tau ) - S S R ( \tau , T _ { i } ^ { 0 } ) \right \}$$

$$\sigma ^ { - 2 } \sup _ { \tau \in \varrho _ { i , \eta } ^ { 0 } } \{ S S R ( T _ { i - 1 } ^ { 0 } , T _ { i } ^ { 0 } ) - S S R ( T _ { i - 1 } ^ { 0 } , \tau ) - S S R ( \\ \Rightarrow \sup _ { \eta \leq \mu \leq 1 - \eta } \frac { \| W _ { q } ( \mu ) - \mu W _ { q } ( 1 ) \| ^ { 2 } } { \mu ( 1 - \mu ) } , \\$$

asserts that Ti = Ti0 + Op(1). Using this result, we can show that (45) also holds with Ti−1 and Ti0 replaced by Î\_, and T, respectively. In addition, because over different regimes SSR(·,) are computed using nonoverlapping observations, the weak limits in (45) for different i's are independent. Thus the limit of (44) is the maximum of I + 1 independent random variables in the form of (45).

PROOF OF LEMMA 3: We show that S(τ) for τ ∈ [0, 1] has a unique minimum at λ1. The function S(τ) has different expressions over [0, 1]. Some algebra reveals that

$$S ( \tau ) - S ( \lambda _ { 1 } ) = \frac { \lambda _ { 1 } - \tau } { ( 1 - \tau ) ( 1 - \lambda _ { 1 } ) } [ ( 1 - \lambda _ { 1 } ) ( \mu _ { 1 } - \mu _ { 2 } ) + ( 1 - \lambda _ { 2 } ) ( \mu _ { 2 } - \mu _ { 3 } ) ] ^ { 2 } , \ \tau \leq \lambda _ { 1 } ,$$

which is nonnegative. Under the assumption that S(λ,) &lt; S(λ2), the expression in brackets is nonzero, so S(τ) − S(λ) is strictly positive for τ &lt; λ1. By symmetry (regarded as reversing the data order), S(τ) − S(λ2) is nonnegative for τ &gt; λ2. Thus for τ ∈ [ λ2, 1],

$$S ( \tau ) - S ( \lambda _ { 1 } ) = S ( \tau ) - S ( \lambda _ { 2 } ) + S ( \lambda _ { 2 } ) - S ( \lambda _ { 1 } ) \geq S ( \lambda _ { 2 } ) - S ( \lambda _ { 1 } ) > 0 .$$


<!-- p:32 -->


It remains to consider the case where τ ∈ (λ, λ2). Again, simple algebra shows

where the first inequality follows from [τ(1 − λ2)]/[ λ2(1 − τ)] ≤ 1 and the second inequality follows from λ2/ τ≥ 1. Thus S(τ) − S(λ1) is strictly positive for τ ∈ (λ1, λ2) and we have shown that S(τ) has a unique global minimum at λ1 when S(λ1) &lt; S(λ2). Because ST(T) ≤ ST([Tλ1 ]), it follows that Ta/T is consistent for λ1. Q.E.D.

####### REFERENCES

AMEMIYA, T. (1985): Advanced Econometrics. Cambridge: Harvard University Press.

- ANDREws, D. W. K. (1988): "Laws of Large Numbers for Dependent Nonidentically Distributed Random Variables,"Econometric Theory, 4, 458-467.
- (1991): "Heteroskedasticity and Autocorrelation Consistent Covariance Matrix Estimation,' Econometrica, 59, 817–858.
- (1993): "Tests for Parameter Instability and Structural Change with Unknown Change Point,"Econometrica, 61, 821–856.
- ANDREws, D. W. K., I. LEE, AND W. PLOBERGER (1996): "Optimal Changepoint Tests for Normal Linear Regression," Journal of Econometrics, 70, 9–38.
- ANDREWS, D. W. K., AND W. PLOBERGER (1994): "Optimal Tests when a Nuisance Parameter is Present Only Under the Alternative," Econometrica, 62, 1383–1414.
- BAi, J. (1994a): "Least Squares Estimation of a Shift in Linear Processes," Journal of Time Series Analysis, 15, 453–472.
- (1994b): "Estimation of Structural Change Based on Wald Type Statistics," Working Paper

No. 94-6, Department of Economics, M.I.T., forthcoming in Review' of Economics and Statistics.

- (1994c): "GMM Estimation of Multiple Structural Changes,"NSF Proposal.
- (1995): "Least Absolute Deviation Estimate of a Shift," Econometric Theory, 11, 403–436.

(1997): "Estimating Multiple Breaks One at a Time," Econometric Theory, 13, 315–352.

- BAI, J., AND P. PERRON (1996): "Computation and Analysis of Multiple Structural Change Models," Manuscript in Preparation, Université de Montréal.
- BHATTACHARYA, P. K. (1994): "Some Aspects of Change-point Analysis," Change Point Problens, IMS Lecture Notes—Monograph Series, Vol. 23, ed. by E. Carlstein, H.-G, Müller, and D. Siegmund. Hayward, CA: Institute of Mathematical Statistics, 28–56.
- BROwN, R. L., J. DURBIN, AND J. M. EVANS (1975): "Techniques for Testing the Constancy of Regression Relationships Over Time," Journal of the Royal Statistical Society, Series B, 37, 149-192.
- CHoNG, T. T-L. (1994): "Consistency of Change-Point Estimators When the Number of ChangePoints in Structural Models is Underspecified," Manuscript, Department of Economics, University of Rochester.
- DELoNG, D. M. (1981): "Crossing Probabilities for a Square Root Boundary by a Bessel Process," Communications in Statistics-Theory and Methods, A10(21), 2197–2213.
- FEDER, P. I. (1975): "On Asymptotic Distribution Theory in Segmented Regression Problem: Identified Case," Annals of Statistics, 3, 49–83.
- GALLANT, A. R., AND W. A. FULLER (1973): "Fitting Segmented Polynomial Regression Models whose Join Points have to be Estimated," Journal of the American Statistical Association, 68, 144-147.
- GARCIA, R., AND P. PERRON (1996): "An Analysis of the Real Interest Rate under Regime Shifts," Review of Economics and Statistics, 78, 111–125.


<!-- p:33 -->


- HALL, P., AND C. C. HEYDE (1980): Martingale Limit Theory and its Applications. New York: Academic Press.
- HANsEN, B. E. (1991): "Strong Laws for Dependent Heterogeneous Processes," Econometric Theory, 7, 213-221.
- HosoYA, Y. (1989): "Hierarchical Statistical Models and a Generalized Likelihood Ratio Test," Journal of the Royal Statistical Society, Series B, 51, 435–447.
- LIU, J., S. WU, AND J. V. ZıDEK (1997): "On Segmented Multivariate Regressions," Statistica Sinica, 7, 497-525.
- KRIsHNAIAH, P. R., AND B. Q. MIAO (1988): "Review about Estimation of Change Points," in Handbook of Statistics, Vol. 7, ed. by P. R. Krishnaiah and C. R. Rao. New York: Elsevier.
- McLEIsH, D. L. (1975): "A Maximal Inequality and Dependent Strong Laws," The Annals of Probability, 5, 829–839.
- PERRON, P. (1989): "The Great Crash, the Oil Price Shock and the Unit Root Hypothesis," Econometrica, 57,1361-1401.
- PoLLARD, D. (1984): Convergence of Stochastic Processes. New York: Springer-Verlag.
- YAO, Y.-C. (1987): "Approximating the Distribution of the ML Estimate of the Change-Point in a Sequence of Independent r.v.'s," Annals of Statistics, 3, 1321–1328.
- (1988): "Estimating the Number of Change-Points via Schwarz' Criterion,"Statistics and Probability Letters, 6, 181-189.
- YAO, Y.-C., AND S. T. Au (1989): "Least Squares Estimation of a Step Function," Sankhyā, 51, Ser. A, 370-381.
- ZACks, S. (1983): "Survey of Classical and Bayesian Approaches to the Change-Point Problem: Fixed and Sequential Procedures of Testing and Estimation," in Recent Advances in Statistics, ed. by M. H. Rivzi, J. S. Rustagi, and D. Sigmund. New York: Academic Press, 245-269.
