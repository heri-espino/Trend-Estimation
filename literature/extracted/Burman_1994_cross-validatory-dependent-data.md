---
id: "Burman_1994_cross-validatory-dependent-data"
source_pdf: "../pdf/Burman_1994_cross-validatory-dependent-data.pdf"
source_filename: "Burman_1994_cross-validatory-dependent-data.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
references_file: "../references/Burman_1994_cross-validatory-dependent-data.references.md"
---

<!-- p:1 -->

## A cross-validatory method for dependent data

BY PRABIR BURMAN

Division of Statistics, University of California, Davis, California 95616, U.S.A

##### EDMOND CHOW AND DEBORAH NOLAN

Department of Statistics, University of California, Berkeley, California 94720, U.S.A.

###### SUMMARY

In this paper we extend the technique of cross-validation to the case where observations form a general stationary sequence. We call it h-block cross-validation, because the idea is to reduce the training set by removing the h observations preceding and following the observation in the test set. We propose taking h to be a fixed fraction of the sample size, and we add a term to our h-block cross-validated estimate to compensate for the underuse of the sample. The advantages of the proposed modification over the cross-validation technique are demonstrated via simulation.

Some key words: Cross-validation; Dependence; Integrated square error; Prediction error.

## 1. INTRODUCTION

Cross-validation (Stone, 1974; Geisser, 1975) is acclaimed as a method for estimating prediction error in regression and classification problems, and in recent years it has received much attention for its model selection ability in the nonparametric setting. See for example Härdle &amp; Marron (1985). Even more recently, the technique of cross-validation has been applied to prediction error estimation in the dependent setting. Work in this area includes that of Györfi et al. (1989), C. K. Chu, in a University of North Carolina Ph.D. thesis, and Burman &amp; Nolan (1992). Here we continue this line of development, and present a modification of the traditional leave-one-out method of cross-validation for use with dependent observations. Our approach is suggested by the well-known technique of removing blocks or subseries of observations, which originates from estimation problems for dependent random variables.

To best illustrate our procedure, suppose the goal is to fit the (k + 1)-parameter model

$$x _ { i } = \theta _ { 0 } + \theta _ { 1 } x _ { i - 1 } + \dots + \theta _ { k } x _ { i - k }$$

to N observations X1, ..., XN from a stationary process. Let (o, ..., k) be the leastsquares estimate, where (Xi,..., X+k) for i= 1,..., N − k are the cases on which the calculation is based. Following Akaike (1970), we assess the predictive ability of the fitted model by the expectation:

$$E \{ \text {PE} ( \hat { \theta } _ { 0 } , \dots , \hat { \theta } _ { k } ) \} = E \{ ( \tilde { X } _ { k + 1 } - \hat { \theta } _ { o } - \hat { \theta } _ { 1 } X _ { k } - \dots - \hat { \theta } _ { k } \tilde { X } _ { 1 } ) ^ { 2 } \} ,$$

where X1, . .. , XN is another process that has the same distribution as X1, . . . , XN but is independent of it. Leave-one-out, or ordinary, cross-validation estimates the expected value in (2) by where j,i ( j = 0, . . . , k) denotes the ith least-squares estimate of θj, obtained after deleting the ith case (X, . . . , X+ k), and n = N − k is the number of cases.


<!-- p:2 -->


$$O C V _ { n } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left ( X _ { i + k } - \hat { \theta } _ { 0 , i } - \hat { \theta } _ { 1 , i } X _ { i + k - 1 } - \dots - \hat { \theta } _ { k , i } X _ { i } \right ) ^ { 2 } , \\ \hat { \theta } _ { 0 } \left ( i - 0 \right ) \sum _ { k = 1 } ^ { k } \left ( X _ { i + k } - \hat { \theta } _ { 0 , i } - \hat { \theta } _ { 1 , i } X _ { i + k - 1 } - \dots - \hat { \theta } _ { k , i } X _ { i } \right ) ^ { 2 } ,$$

In classical applications of leave-one-out cross-validation, the cases are independent, therefore making the cross-validated prediction error a good approximation to the true expected prediction error. Here, however, the cases overlap, so leave-one-out cross-validation (3) may provide a very poor estimate of E{PE(o, . . . , k)}. In this note we examine an alternative method of cross-validation, which we dub 'h-block cross-validation', that can handle general forms of dependence. The idea is a simple one. Rather than remove the single case (Xi, ..., X+k) when calculating the ith least-squares estimate, remove as well a block of h cases from either side of it. Now the training set contains 2h fewer cases, but the test set remains a singleton. Carlstein (1986), Künsch (1989) and Lele (1991) use a similar technique with jackknife variance estimates for stationary sequences, and Chu, in the thesis mentioned above, and Györfi et al. (1989) propose this modification to crossvalidation when selecting the nuisance parameter in nonparametric curve estimation with dependent data. This approach is quite different from v-fold cross-validation. There, the n cases are divided into v sets roughly of size n/v. Each group of n/v cases constitutes a test set; the remaining n — (n/v) cases comprise the corresponding training set. Here instead, there are n test sets, each consisting of one case, and the training sets contain roughly n — 2h - 1 cases. So, h-block cross-validation maintains a leave-one-out aspect.

According to the underlying structure of the data, blocking allows near independence between these two sets. It remains a question how to select the value of h. This is our main concern here. Intuitively, one should shrink the block size relative to the sample size, but to maintain independence between the test set and the training set, h should remain large. Chu, in the thesis mentioned above, and Györfi et al. (1989) require that h/n tend to 0, with the rate of decrease a complex function of the underlying structure of the data and the amount of smoothness in the model. In practice this structure is unknown and, for small samples, h will necessarily be large relative to n. Alternatively, we propose to take h as a fixed fraction of n, that is h/n = p for some 0 &lt; p &lt; 1, and to correct for the underuse of the sample by adding a simple term to the h-block cross-validated estimate. The correction term makes possible our omnibus choice of h. It is analogous to the correction used for v-fold cross-validation (Burman, 1989). We find through simulation that, with the correction term proposed here, h-block cross-validation estimates the expected prediction error well in a wide range of settings, and we also find that, without this correction, h-block cross-validation may be as ineffective as ordinary leave-one-out cro or os  rn so  o os  osnone.. Although long-range dependence models have been proven useful in a variety of applications (Hosking, 1981; Cox, 1984; Dahlhaus, 1989), we do not know if our methodology is applicable.

The next section formally introduces h-block cross validation. Section 3 outlines a few examples where h-block cross-validation can be used. Finally in the last section, a variety of simulations are presented in support of our proposal.

## 2. THE TECHNIQUE

Let Z1,..., Z be a segment of length n from a stationary process where each Z has distribution P on Rd. For h a positive integer and for each i, define Pn,i, an empirical estimate of P, as follows:


<!-- p:3 -->


$$P _ { n , i } ( A ) & = \sum _ { j = 1 } ^ { n } \omega _ { _ { i , j } } I ( Z _ { j } \in A ) , \\$$

for A a Borel set in Rd. Here the weights {ωij: 1 ≤i, j ≤n} form a double array of nonnegative numbers such that

$$\omega _ { i , j } = 0 \quad \text {if } | i - j | \leqslant h ,$$

$$\sum _ { i = 1 } ^ { n } \omega _ { i , j } = 1 \quad \text {for all $j$} .$$

Many choices for the weight function satisfy these two constraints. In our simulation study we simply take:

for 1 ≤j≤ h,

for h&lt;j≤n− h

for n−h&lt;j≤n,

$$\omega _ { i , j } = \begin{cases} 0 & ( 1 \leqslant i \leqslant j + h ) , \\ 1 / ( n - j - h ) & \text {otherwise} ; \end{cases}$$

$$\omega _ { i , j } = \begin{cases} 0 & ( j - h \leqslant i \leqslant j + h ) , \\ 1 / ( n - 2 h - 1 ) & \text {otherwise} ; \end{cases}$$

$$\omega _ { i , j } = \begin{cases} 0 & ( j - h \leqslant i \leqslant n ) , \\ 1 / ( j - h - 1 ) & \text {otherwise} . \end{cases}$$

The intent of condition (4) is to make the training set and the test set nearly independent. Our notation suppresses the dependence of h on n, of Pn,i on h, and of ω,j on h and n. The empirical estimates P,i need not be probability measures, but condition (5) ensures ∑ Pn,i = nPn, where Pn denotes the standard empirical distribution that places mass 1/n on each of the observations.

For some functional T on Rd × P, where P is a collection of probability measures on Ra, define the prediction error by

$$P E _ { n } = \int T ( z , P _ { n } ) \, d P ( z ) ,$$

and the h-block cross-validated estimate of E(PE) to be

$$C v _ { n } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } T ( Z _ { i } , P _ { n , i } ) . \\$$

Examples of functionals T are found in the next section. Also define the corrected h-block cross-validated estimate as

$$C C V _ { n } = C V _ { n } - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \, \int T ( z , P _ { n , i } ) \, d P _ { n } ( z ) + \int T ( z , P _ { n } ) \, d P _ { n } ( z ) .$$

Heuristically, the extra terms in (8) follow from matching the expectation of Cv with that of PE. To see this write CV as:


<!-- p:4 -->


$$\left \{ \frac { 1 } { n } \sum _ { i = 1 } ^ { n } T ( Z _ { i } , P _ { n , i } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \int T ( z , P _ { n , i } ) \, d P ( z ) \right \} + \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \int \{ T ( z , P _ { n , i } ) - T ( z , P _ { n } ) \} \, d P ( z ) + \text {PE} _ { n } . \\ \\ \text {If the } \{ Z \} \text { or independent than the } \text { approximation } \text { of the } \text { first } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text { } \text {$$

If the {Z} are independent then the expectation of the first term is zero. If not, this expectation is small when Z and {Zj: |i —j| &gt; h} are nearly independent. The correction in (8) is an approximation to the second term in (9). It is needed because this term's expectation is of order h/{n(n − 2h)}. If h = np, for 0 &lt; p &lt; 1, then the order of the expectation becomes 1/n, whereas the order of the expectation of CCv — PE is 1/n2. Note that the order terms include a constant that increases with dimension of the fitted model implicit in T.

Remark 1. Burman &amp; Nolan (1992) consider the problem of estimating the prediction function μ for a stationary process (X, Yi), where

$$Y _ { i } = \mu ( X _ { i } ) + \varepsilon _ { i } , \ E ( \varepsilon _ { i } | X _ { i } ) = 0 .$$

It is argued there that leave-one-out cross-validation for model selection is asymptotically optimal in the sense of Shibata (1980) in many cases. It is important to point out that the test and training set need not be independent for cross-validation to work. Briefly, the prediction error can be well approximated by a quadratic form in the errors plus a bias term, provided E(εiεj|X1, . . . , Xj) = 0 (i &lt;j). A stationary Markov process with Yi = X+1 satisfies this condition, which implies the AR(1) process also meets this condition. See Burman &amp; Nolan (1992) for details of the argument.

Remark 2. Conditions for asymptotic optimality for this proposal remain open. It is noted however that in the independent case Burman (1990) has shown the closely related corrected v-fold cross-validation is asymptotically optimal for 0 &lt; p &lt; 1.

## 3. EXAMPLES

In this section we present three examples where h-block cross-validation may prove useful in estimating the prediction error. The first is a formalization of the example used in § 1 to introduce the notion of h-block cross-validation, i.e. the autoregressive model. The second example concerns additive prediction and the last is a nonparametric model.

Example 1. Let X1,..., XN be N observations from a stationary process. Use least squares to fit an autoregressive model of order k to the data as in (1). Call the fitted parameters o, ... , Ôk. Then the expected quadratic loss (2) in predicting a new observation is

$$E ( \mathbf P _ { n } ) = E \left \{ \int ( x _ { k + 1 } - \hat { \theta } _ { 0 } - \hat { \theta } _ { 1 } x _ { k } - \dots - \hat { \theta } _ { k } x _ { 1 } ) ^ { 2 } \, d P ( x _ { 1 } , \dots , x _ { k + 1 } ) \right \} .$$

Here

$$Z _ { i } = ( X _ { i } , \dots , X _ { i + k } ) , \ \ T ( z , P _ { n } ) = ( x _ { k + 1 } - \hat { \theta } _ { o } - \hat { \theta } _ { 1 } x _ { k } - \dots - \hat { \theta } _ { k } x _ { 1 } ) ^ { 2 } ,$$

To explain further, take k = 1. Then the least squares estimates , θ1 in (10) are the

with z = (x1, . . . , Xk+1) and n = N − k. This is the model that is fitted in the simulations of the next section.


<!-- p:5 -->


minimizers of

$$\sum _ { i = 1 } ^ { n } \left ( X _ { i + 1 } - \theta _ { 0 } - \theta _ { 1 } X _ { i } \right ) ^ { 2 } ,$$

P is the joint distribution of (X1, X2), and Pn puts mass 1/n, or 1/(N − 1), on each of the pairs (Xi, Xi+1) for i = 1, . . . , N − 1. The leave-one-out cross-validated estimate (3) in this case is

$$O C V _ { n } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left ( X _ { i + 1 } - \hat { \theta } _ { 0 , i } - \hat { \theta } _ { 1 , i } X _ { i } \right ) ^ { 2 } , \\$$

where Ôo,i and 1, minimize

$$\sum _ { j \neq i } ( X _ { j + 1 } - \theta _ { 0 } - \theta _ { 1 } X _ { j } ) ^ { 2 } .$$

To h-block cross-validate, minimize for each i the following quadratic:

$$\sum _ { j = 1 } ^ { n } \left ( X _ { j + 1 } - \theta _ { 0 } - \theta _ { 1 } X _ { j } \right ) ^ { 2 } \omega _ { i , j } , \\$$

where the weights ωi,j satisfy (4) and (5). Call the minimizers ,i,w and 1,i,w. Finally, the corrected h-block cross-validated estimate of (10) is

$$C C _ { n } = & - \sum _ { n = 1 } ^ { 1 } \left ( X _ { i + 1 } - \hat { \theta } _ { 0 , i , w } - \hat { \theta } _ { 1 , i , w } X _ { i } \right ) ^ { 2 } - \frac { 1 } { n ^ { 2 } } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \left ( X _ { j + 1 } - \hat { \theta } _ { 0 , i , w } - \hat { \theta } _ { 1 , i , w } X _ { j } \right ) ^ { 2 } \\ & + \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left ( X _ { i + 1 } - \hat { \theta } _ { 0 } - \hat { \theta } _ { 1 } X _ { i } \right ) ^ { 2 } . \\ \intertext { f o r a l l } \Example 2 _ { A } & \text { as in the previous example. take } X _ { 1 } , \dots X _ { w } \text { to be } N \text { observations from a } A$$

Example 2. As in the previous example, take X1, ... , XN to be N observations from a stationary process. Generalize the ideas of Hastie &amp; Tibshirani (1987) and Stone (1985) by considering the problem of predicting X by an additive nonparametric model: μ0 + μ1(Xi-1) + ... + μk(Xi-k). If we employ least-squares to fit splines or polynomials then, as in the above example, the prediction error (6) is given by

$$P E _ { n } = \int \{ x _ { k + 1 } - \hat { \mu } _ { 0 } - \hat { \mu } _ { 1 } ( x _ { k } ) - \dots - \hat { \mu } _ { k } ( x _ { 1 } ) \} ^ { 2 } \, d P ( x _ { 1 } , \dots , x _ { k + 1 } ) .$$

Again, P represents the distribution of Zi = (Xi, . . . , Xi + k), the function T is the quadratic integrand above, z = (x1, . . . , χk + 1) and n = N − k.

Example 3. Consider the nonparametric regression model

$$E ( Y | X = x ) = \mu ( x ) .$$

Take {Zi = (Xi, Yi): i = 1, . . . , N } to be N observations from a strictly stationary process. Once again if a polynomial of order k, or a spline with k knots, is fitted to the data by the method of least squares then the prediction error using quadratic loss is

$$P _ { n } = \int \{ y - \hat { \mu } _ { k } ( x ) \} ^ { 2 } \, d P ( x , y ) ,$$

where βk is the estimate of μ. In this example n = N.

In each of these examples, quadratic loss was used both to estimate the unknown prediction function and to evaluate the prediction error. Our method is not restricted to the use of quadratic loss; in fact, the functional T can be any reasonably smooth function of z and P. We do not investigate the performance of other loss functions here.


<!-- p:6 -->


## 4. SIMULATION STUDY

Six simulations are presented here. The simulations demonstrate a variety in autocorrelation, sample size, and fitted model. Each simulation is based on 10 000 replications. For one replication, N observations are generated from a stationary zero-mean Gaussian sequence with standard deviation 3 and specified autocorrelation. A model is fitted to the generated data using least squares; the exact one-step prediction error is calculated based on the fitted parameters and pre-specified correlation structure; and, finally, the expected e   s as o o s o es ss co rco and according to corrected (8) and uncorrected (7) h-block cross-validation for h as the nearest integer to each of the following fractions of n: 0·05, 0·10, 0·15, 0·20, 0·25, 0·30, where n is the effective number of cases. Example 1 in § 3 provides details for computing these quantities. Table 1 reports estimates of E(PEn), E(Cvn), E(CCv) based on the 10 000 repetitions.

The simulations show that classical leave-one-out cross-validation can be very misleading, and caution should be exercised in using the leave-one-out technique when observations are not independent. On the other hand, these simulations also demonstrate that blocking effectively adapts cross-validation to the dependent setting. In each of the simulations, at least one block size produces good results for uncorrected h-block cross-validation. However, as discussed earlier, the best block size to use is determined by the autocorrelation and the appropriateness of the fitted model, both of which are presumed unknown. Therefore it is reassuring to see positive results for corrected h-block crossvalidation over a wide range of block sizes. Whether  or 1 of the cases are removed, blocking with the corrective term yields good cross-validated estimates of the expected prediction error. Our simulations suggest the rule-of-thumb of removing 1 of the data; that is the fourth column in each simulation of Table 1 shows that h = n/6 appears to be a sensible choice in a variety of settings. Finally, it is noted that it can be difficult for the corrective term to compensate for large data loss, where h exceeds 0·25n, because it makes only a first order correction.

Specifically, the first simulation fits the linear model

$$x _ { i } = \theta _ { 0 } + \theta _ { 1 } x _ { i - 1 } .$$

The sample is of size N = 25 with autocorrelations C(Xi, X+ j) = 0·3, 0·4, 0·3, 0·3, 0·3, 0·46, 0·47, 0·48, . .. , 0·424, for j = 1, ... , 24. The results appear at the top of Table 1. Notice ordinary leave-one-out cross-validation greatly underestimates the expected prediction error in this example.

The next two simulation results presented in Table 1 are based on the same stationary process, an autoregressive model with single coefficient 0·7. Burman &amp; Nolan (1992) show that ordinary cross-validation is asymptotically equivalent to PE for the AR(1) process. The first of these two simulations fits a model that is linear in the first lag, and the second fits a model that is quadratic in the first lag:

$$x _ { i } = \theta _ { 0 } + \theta _ { 1 } x _ { i - 1 } + \theta _ { 2 } x _ { i - 1 } ^ { 2 } .$$

The fourth and fifth simulations generate observations from a sequence of Gaussians with autocorrelations: 0, 0·6, 0, 0·4, 0, 0·46, 0, 0·48, . ... In the fourth simulation a linear fit in one lag is made to the data, for N = 25. The results show a large expected prediction error, and the h-block method does a very good job estimating it. In the fifth simulation, N = 64 and the fitted model is linear in two lags:


<!-- p:7 -->


Table 1. Mean and standard deviations of h-block and corrected h-block estimates of the prediction error for six simulations

|          | N = 25, n = 24, E(PEn) = 10·38, SD(PEn) = 2·74 - h=0   | N = 25, n = 24, E(PEn) = 10·38, SD(PEn) = 2·74 - h= 1   | N = 25, n = 24, E(PEn) = 10·38, SD(PEn) = 2·74 - h=2   | N = 25, n = 24, E(PEn) = 10·38, SD(PEn) = 2·74 - h=4   | N = 25, n = 24, E(PEn) = 10·38, SD(PEn) = 2·74 - h=5   | N = 25, n = 24, E(PEn) = 10·38, SD(PEn) = 2·74 - h= 6   | N = 25, n = 24, E(PEn) = 10·38, SD(PEn) = 2·74 - h=7   |
|----------|--------------------------------------------------------|---------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------|--------------------------------------------------------|
| E(Cvn)   | 7.96                                                   | 8·22                                                    | 8.89                                                   | 10·58                                                  | 11·82                                                  | 12·32                                                   | 13·01                                                  |
| E(CCvn)  | 7.93                                                   | 8·12                                                    | 8.64                                                   | 9.81                                                   | 10·68                                                  | 10.73                                                   | 10·83                                                  |
| SD(CVvn) | 2.83                                                   | 3.00                                                    | 3.52                                                   | 4.85                                                   | 5.92                                                   | 6.75                                                    | 7.86                                                   |
| SD(cCvn) | 2.82                                                   | 2.96                                                    | 3.39                                                   | 4.32                                                   | 5·05                                                   | 5.43                                                    | 5.96                                                   |
|          | N = 36, n = 35, E(PEn) = 5·09, SD(PEn) = 0·75          | N = 36, n = 35, E(PEn) = 5·09, SD(PEn) = 0·75           | N = 36, n = 35, E(PEn) = 5·09, SD(PEn) = 0·75          | N = 36, n = 35, E(PEn) = 5·09, SD(PEn) = 0·75          | N = 36, n = 35, E(PEn) = 5·09, SD(PEn) = 0·75          | N = 36, n = 35, E(PEn) = 5·09, SD(PEn) = 0·75           | N = 36, n = 35, E(PEn) = 5·09, SD(PEn) = 0·75          |
|          | h=0                                                    | h= 2                                                    | h= 4                                                   | h=5                                                    | h=7                                                    | h= 9                                                    | h= 11                                                  |
| E(Cvn)   | 4.84                                                   | 5.03                                                    | 5·20                                                   | 5.30                                                   | 5.52                                                   | 5.84                                                    | 6·32                                                   |
| E(CCVn)  | 4.83                                                   | 4.97                                                    | 5.07                                                   | 5·12                                                   | 5·20                                                   | 5·30                                                    | 5.42                                                   |
| SD(CVn)  | 1·19                                                   | 1·28                                                    | 1·43                                                   | 1·52                                                   | 1·79                                                   | 2·19                                                    | 2.82                                                   |
| SD(CCVn) | 1·19                                                   | 1·26                                                    | 1·36                                                   | 1·42                                                   | 1·57                                                   | 1·78                                                    | 2.09                                                   |
|          | N = 36, n = 35, E(PEn) = 5·50, SD(PEn) = 0·75          | N = 36, n = 35, E(PEn) = 5·50, SD(PEn) = 0·75           | N = 36, n = 35, E(PEn) = 5·50, SD(PEn) = 0·75          | N = 36, n = 35, E(PEn) = 5·50, SD(PEn) = 0·75          | N = 36, n = 35, E(PEn) = 5·50, SD(PEn) = 0·75          | N = 36, n = 35, E(PEn) = 5·50, SD(PEn) = 0·75           | N = 36, n = 35, E(PEn) = 5·50, SD(PEn) = 0·75          |
|          | h=0                                                    | h= 2                                                    | h=4                                                    | h= 5                                                   | h=7                                                    | h=9                                                     | h=11                                                   |
| E(CVn)   | 5·12                                                   | 5.43                                                    | 5.82                                                   | 6.04                                                   | 6.69                                                   | 7.79                                                    | 10·34                                                  |
| E(CCvn)  | 5·11                                                   | 5.32                                                    | 5.55                                                   | 5.65                                                   | 5.95                                                   | 6.36                                                    | 7.25                                                   |
| SD(Cvn)  | 1·37                                                   | 1·68                                                    | 2.34                                                   | 2.73                                                   | 4.42                                                   | 7.72                                                    | 18·24                                                  |
| SD(CCVn) | 1·36                                                   | 1·61                                                    | 2·10                                                   | 2.36                                                   | 3.47                                                   | 5.68                                                    | 14·26                                                  |
|          | N = 25, n = 24, E(PEn) = 11·59, sD(PEn) = 2·94         | N = 25, n = 24, E(PEn) = 11·59, sD(PEn) = 2·94          | N = 25, n = 24, E(PEn) = 11·59, sD(PEn) = 2·94         | N = 25, n = 24, E(PEn) = 11·59, sD(PEn) = 2·94         | N = 25, n = 24, E(PEn) = 11·59, sD(PEn) = 2·94         | N = 25, n = 24, E(PEn) = 11·59, sD(PEn) = 2·94          | N = 25, n = 24, E(PEn) = 11·59, sD(PEn) = 2·94         |
|          | h=0                                                    | h= 1                                                    | h=2                                                    | h=4                                                    | h=5                                                    | h= 6                                                    | h=7                                                    |
| E(Cvn)   | 8.01                                                   | 8.62                                                    | 10·08                                                  | 12·17                                                  | 12·70                                                  | 13·32                                                   | 13.92                                                  |
| E(CCvn)  | 7.99                                                   | 8.48                                                    | 9.74                                                   | 11·21                                                  | 11·34                                                  | 11·46                                                   | 11·47                                                  |
| SD(Cvn)  | 3.31                                                   | 3.72                                                    | 4.85                                                   | 6.73                                                   | 7.42                                                   | 8.40                                                    | 9.25                                                   |
| SD(CCVn) | 3.30                                                   | 3.65                                                    | 4.63                                                   | 6.00                                                   | 6·31                                                   | 6.82                                                    | 7.14                                                   |
|          | N = 64, n = 62, E(PEn) = 6·18, SD(PEn) = 0·.56         | N = 64, n = 62, E(PEn) = 6·18, SD(PEn) = 0·.56          | N = 64, n = 62, E(PEn) = 6·18, SD(PEn) = 0·.56         | N = 64, n = 62, E(PEn) = 6·18, SD(PEn) = 0·.56         | N = 64, n = 62, E(PEn) = 6·18, SD(PEn) = 0·.56         | N = 64, n = 62, E(PEn) = 6·18, SD(PEn) = 0·.56          | N = 64, n = 62, E(PEn) = 6·18, SD(PEn) = 0·.56         |
|          | h=0                                                    | h= 3                                                    | h=6                                                    | h=9                                                    | h= 12                                                  | h= 16                                                   | h= 19                                                  |
| E(CVn)   | 6.06                                                   | 6·21                                                    | 6·30                                                   | 6.40                                                   | 6.51                                                   | 6.76                                                    | 7.07                                                   |
| E(CCVn)  | 6.06                                                   | 6·16                                                    | 6·20                                                   | 6·23                                                   | 6·25                                                   | 6·31                                                    | 6.38                                                   |
| SD(Cvn)  | 1·23                                                   | 1·29                                                    | 1·37                                                   | 1.47                                                   | 1.58                                                   | 1·81                                                    | 2·08                                                   |
| SD(CCVn) | 1·23                                                   | 1·28                                                    | 1·34                                                   | 1·40                                                   | 1·44                                                   | 1·54                                                    | 1·66                                                   |
|          | N = 60, n = 58, E(PEn) = 10·17, sD(PEn) = 1·78         | N = 60, n = 58, E(PEn) = 10·17, sD(PEn) = 1·78          | N = 60, n = 58, E(PEn) = 10·17, sD(PEn) = 1·78         | N = 60, n = 58, E(PEn) = 10·17, sD(PEn) = 1·78         | N = 60, n = 58, E(PEn) = 10·17, sD(PEn) = 1·78         | N = 60, n = 58, E(PEn) = 10·17, sD(PEn) = 1·78          | N = 60, n = 58, E(PEn) = 10·17, sD(PEn) = 1·78         |
|          | h= 0                                                   | h= 3                                                    | h=6                                                    | h=9                                                    | h= 12                                                  | h = 15                                                  | h=17                                                   |
| E(CVn)   | 8.19                                                   | 8.54                                                    | 9.64                                                   | 10·36                                                  | 11·03                                                  | 11·53                                                   | 12·24                                                  |
| E(CCVn)  | 8.18                                                   | 8.34                                                    | 9.34                                                   | 9.79                                                   | 10·10                                                  | 10·09                                                   | 10·34                                                  |
| SD(Cvn)  | 2·18                                                   | 2·29                                                    | 2.99                                                   | 3.62                                                   | 4.34                                                   | 4.92                                                    | 5.73                                                   |
| SD(cCvn) | 2·18                                                   | 2·25                                                    | 2.85                                                   | 3.30                                                   | 3.74                                                   | 3.93                                                    | 4.39                                                   |

#### xi= θ0 + θ1xi−1+θ2xi−2.

Here, both the h-block method and leave-one-out cross-validation perform well, which is not surprising given the results of Burman &amp; Nolan (1992).


<!-- p:8 -->


Finally, the last simulation further exemplifies the advantages of h-blocking. There the autocorrelations are: 0·2, 02, 0·2, 0·6, 0·1, 0·1, 0, 0·62, 0, 0, 0, 0.63, 0, 0, 0, 0.64, . . . ; and the fitted model is

$$x _ { i } = \theta _ { 0 } + \theta _ { 1 } x _ { i - 1 } + \theta _ { 2 } x _ { i - 1 } ^ { 2 } + \theta _ { 3 } x _ { i - 2 } .$$

### ACKNOWLEDGEMENT

The authors thank the referees for helpful comments. This research was partially supported by the United States National Science Foundation.
